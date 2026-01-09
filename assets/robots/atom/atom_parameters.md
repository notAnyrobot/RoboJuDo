# Atom actuator parameters

Generated via `uv run python scripts/update_atom_parameters.py`.

`atom_constants.py` drives all position actuators. For the joints that use the helper 
in that module the damping and stiffness follow:

- natural frequency (`NATURAL_FREQ`) = `6 * 2π` ≈ 37.699 rad/s (10 Hz)
- damping ratio (`DAMPING_RATIO`) = 2.000
- stiffness `k = armature * NATURAL_FREQ²`
- damping `c = 2 * DAMPING_RATIO * armature * NATURAL_FREQ`

`ATOM_ACTION_SCALE` is computed as `0.25 * effort_limit / stiffness`. Effort limits mirror the 
`ElectricActuator.effort_limit` values in `atom_constants.py`. Default joint positions come from 
`KNEES_BENT_KEYFRAME`; joints without overrides remain at 0 rad.

| Joint name / pattern | Stiffness (N·m/rad) | Damping (N·m·s/rad) | Effort limit (N·m) | Default pos (rad) | Action scale (rad) |
| --- | --- | --- | --- | --- | --- |
| `.*_ankle_pitch_joint` | 21.318 | 2.262 | 90.000 | -0.363 | 1.0554 |
| `.*_ankle_roll_joint` | 21.318 | 2.262 | 90.000 | 0.000 | 1.0554 |
| `.*_shoulder_pitch_joint` | 100.000 | 5.000 | 70.000 | +0.200 left / +0.200 right | 0.1750 |
| `.*_elbow_joint` | 100.000 | 5.000 | 70.000 | +0.600 | 0.1750 |
| `.*_shoulder_roll_joint` | 100.000 | 5.000 | 70.000 | +0.200 left / -0.200 right | 0.1750 |
| `.*_shoulder_yaw_joint` | 100.000 | 5.000 | 70.000 | 0.000 | 0.1750 |
| `.*_hip_pitch_joint` | 156.335 | 16.588 | 200.000 | -0.312 | 0.3198 |
| `.*_hip_roll_joint` | 99.486 | 10.556 | 240.000 | 0.000 | 0.6031 |
| `.*_hip_yaw_joint` | 56.849 | 6.032 | 100.000 | 0.000 | 0.4398 |
| `.*_knee_joint` | 113.698 | 12.064 | 210.000 | +0.669 | 0.4618 |
| `waist_yaw_joint` | 156.335 | 16.588 | 180.000 | 0.000 | 0.2878 |
| `.*_wrist_pitch_joint` | 50.000 | 2.000 | 34.000 | 0.000 | 0.1700 |
| `.*_wrist_roll_joint` | 50.000 | 2.000 | 34.000 | 0.000 | 0.1700 |
| `.*_wrist_yaw_joint` | 50.000 | 2.000 | 34.000 | 0.000 | 0.1700 |

Notes:
- Shoulder roll defaults differ per side because `KNEES_BENT_KEYFRAME` sets `left_shoulder_roll_joint` to +0.2 rad and `right_shoulder_roll_joint` to -0.2 rad.
- The same ankle actuator drives both pitch and roll joints, so they share the same stiffness/damping/action scale but have different default poses.
