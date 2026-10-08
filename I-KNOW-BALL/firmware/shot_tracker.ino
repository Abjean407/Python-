/*
  I KNOW BALL — ESP32 BLE experimental sensor prototype

  WARNING: GPIO4 is a placeholder digital optical trigger (active LOW).
  It has NOT been validated for accurate basketball made-shot detection.
  Use 3.3V-safe sensor output, never direct 5V on ESP32 GPIO.
  Requires an ESP32 Arduino core with BLEDevice.h support.
*/

#include <Arduino.h>
#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

constexpr int SENSOR_PIN = 4;
constexpr unsigned long COOLDOWN_MS = 600; // Starting value; tune experimentally.

const char* SERVICE_UUID = "13d12001-76d1-47aa-9e28-9b4d3c214a10";
const char* COUNT_UUID = "13d12002-76d1-47aa-9e28-9b4d3c214a10";
const char* RESET_UUID = "13d12003-76d1-47aa-9e28-9b4d3c214a10";

BLECharacteristic* countCharacteristic = nullptr;
uint32_t makes = 0;
unsigned long lastTriggerMs = 0;
bool previousActive = false;
bool connected = false;

void publishCount() {
  uint8_t bytes[4] = {
    static_cast<uint8_t>(makes),
    static_cast<uint8_t>(makes >> 8),
    static_cast<uint8_t>(makes >> 16),
    static_cast<uint8_t>(makes >> 24)
  };
  countCharacteristic->setValue(bytes, sizeof(bytes));
  if (connected) countCharacteristic->notify();
}

class ConnectionCallbacks : public BLEServerCallbacks {
  void onConnect(BLEServer*) override { connected = true; }
  void onDisconnect(BLEServer* server) override {
    connected = false;
    server->getAdvertising()->start();
  }
};

class ResetCallbacks : public BLECharacteristicCallbacks {
  void onWrite(BLECharacteristic* characteristic) override {
    // For this experimental prototype, any write resets the counter.
    // Add authentication/validation before real-world use.
    makes = 0;
    publishCount();
  }
};

void setup() {
  Serial.begin(115200);
  pinMode(SENSOR_PIN, INPUT_PULLUP);
  BLEDevice::init("IKNOWBALL");
  BLEServer* server = BLEDevice::createServer();
  server->setCallbacks(new ConnectionCallbacks());

  BLEService* service = server->createService(SERVICE_UUID);
  countCharacteristic = service->createCharacteristic(
    COUNT_UUID,
    BLECharacteristic::PROPERTY_READ | BLECharacteristic::PROPERTY_NOTIFY
  );
  countCharacteristic->addDescriptor(new BLE2902());

  BLECharacteristic* resetCharacteristic = service->createCharacteristic(
    RESET_UUID, BLECharacteristic::PROPERTY_WRITE
  );
  resetCharacteristic->setCallbacks(new ResetCallbacks());
  publishCount();
  service->start();
  server->getAdvertising()->addServiceUUID(SERVICE_UUID);
  server->getAdvertising()->start();
  Serial.println("IKNOWBALL sensor prototype advertising");
}

void loop() {
  bool active = digitalRead(SENSOR_PIN) == LOW;
  unsigned long now = millis();
  if (active && !previousActive && (lastTriggerMs == 0 || now - lastTriggerMs >= COOLDOWN_MS)) {
    makes++;
    lastTriggerMs = now;
    publishCount();
    Serial.printf("Made baskets (unverified trigger): %lu\n", static_cast<unsigned long>(makes));
  }
  previousActive = active;
  delay(10);
}
