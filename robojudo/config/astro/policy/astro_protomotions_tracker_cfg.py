from pydantic import Field

from robojudo.config.g1.policy.g1_protomotions_tracker_cfg import ProtoMotionsTrackerPolicyCfg

ASTRO_DEFAULT_JOINT_POS_PATTERNS: dict[str, float] = {
    ".*_hip_pitch_joint": -0.312,
    ".*_knee_joint": 0.669,
    ".*_ankle_pitch_joint": -0.363,
    ".*_elbow_joint": 0.2,
    "left_shoulder_roll_joint": 0.2,
    "left_shoulder_pitch_joint": 0.2,
    "right_shoulder_roll_joint": -0.2,
    "right_shoulder_pitch_joint": 0.2,
}


class AstroProtoMotionsTrackerPolicyCfg(ProtoMotionsTrackerPolicyCfg):
    robot: str = "astro"
    default_joint_pos_patterns: dict[str, float] = Field(
        default_factory=lambda: ASTRO_DEFAULT_JOINT_POS_PATTERNS.copy()
    )
