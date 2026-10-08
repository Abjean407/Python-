# I KNOW BALL — Hardware & Mechanical Specification (Concept)

## Intended physical layout

**Target mounted mass:** under 150 g (unverified).

- **Rear center housing:** battery, ESP32/BLE electronics, switch; positioned behind the rear rim rod.
- **Two low-profile arms:** follow the outer rear curve of the rim, without crossing the hoop opening.
- **Two small optical pods:** beneath the rim near the arm ends, facing inward across a lower detection plane. The **physical hardware stays out of the ball and net path**. Target ~2 inches below rim height, subject to geometry tests.
- The rim's upper opening remains completely unobstructed.

## Clamp concept

- Spring-tensioned dual jaw gripping an accessible rear steel rim section.
- Textured silicone jaw liners and rubber isolation.
- Adjustable fit: do **not** assume all rims provide the same accessible 5/8-inch attachment rod.
- Clamp must withstand impacts without rotating, loosening, or releasing.
- Claimed 50G shock protection is **not validated**; establish measurable drop/impact tests.
- Indoor/outdoor, double-rim, chain-net, damaged-net, and netless compatibility are design goals, not established capabilities.

## Telescoping pole

- Collapsible multi-stage pole, gym-bag-friendly when collapsed.
- Y-shaped fork retains tracker while raising/lowering.
- Mount: lift to rear rim, press clamp until locked, then detach pole.
- Remove: recapture tracker in fork **before** unlocking clamp, then lower safely.
- Prevent unintended release and falling hardware; use redundant retention during prototyping.
- No ladder required for final product; **do not attempt ground installation until retention and release are proven safe**.

## Optical detection research

A single break-beam between two rear pods may fail to cover the entire hoop. Outdoor sunlight, rim/net reflections, off-center swishes, and balls moving back upward are risks. Consider multiple beams or another sensing geometry after bench tests. The optical signal alone must not be assumed to reliably identify every made shot.

## Verification checklist

1. Measure actual rim rod and bracket dimensions across several hoops.
2. Mock up rim and net clearance; verify no ball/net contact.
3. Pass a basketball through center and edge positions at different speeds.
4. Test rebounds, near misses, rim hits, upward ball motion, and moving net.
5. Test outdoors in direct sunlight and indoors under different lighting.
6. Verify one count per make, BLE reconnection, and no lost counts.
7. Test clamp retention and safe pole removal before overhead use.
