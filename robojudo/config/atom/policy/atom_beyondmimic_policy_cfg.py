from robojudo.policy.policy_cfgs import BeyondMimicPolicyCfg
from robojudo.tools.tool_cfgs import DoFConfig


class AtomBeyondMimicDoF(DoFConfig):
    joint_names: list[str] = [
        *[
            "left_hip_pitch_joint",
            "right_hip_pitch_joint",
            "waist_yaw_joint",
            "left_hip_roll_joint",
            "right_hip_roll_joint",
            # "waist_roll_joint",
            "left_hip_yaw_joint",
            "right_hip_yaw_joint",
            # "waist_pitch_joint",
            "left_knee_joint",
            "right_knee_joint",
        ],
        *[
            "left_shoulder_pitch_joint",
            "right_shoulder_pitch_joint",
            "left_ankle_pitch_joint",
            "right_ankle_pitch_joint",
            "left_shoulder_roll_joint",
            "right_shoulder_roll_joint",
            "left_ankle_roll_joint",
            "right_ankle_roll_joint",
            "left_shoulder_yaw_joint",
            "right_shoulder_yaw_joint",
        ],
        *[
            "left_elbow_joint",
            "right_elbow_joint",
            "left_wrist_roll_joint",
            "right_wrist_roll_joint",
            "left_wrist_pitch_joint",
            "right_wrist_pitch_joint",
            "left_wrist_yaw_joint",
            "right_wrist_yaw_joint",
        ],
    ]

    default_pos: list[float] | None = [
        *[-0.312, -0.312, 0.000, 0.000, 0.000, 0.000, 0.000, 0.669, 0.669],
        *[0.200, 0.200, -0.363, -0.363, 0.200, -0.200, 0.000, 0.000, 0.000, 0.000],
        *[0.200, 0.200, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000],
    ]

    stiffness: list[float] | None = [
        *[156.335, 156.335, 156.335, 99.486, 99.486, 56.849, 56.849, 113.698, 113.698],
        *[100.000, 100.000, 21.318, 21.318, 100.000, 100.000, 21.318, 21.318, 100.000, 100.000],
        *[100.000, 100.000, 50.000, 50.000, 50.000, 50.000, 50.000, 50.000],
    ]

    damping: list[float] | None = [
        *[16.588, 16.588, 16.588, 10.556, 10.556, 6.032, 6.032, 12.064, 12.064],
        *[5.000, 5.000, 2.262, 2.262, 5.000, 5.000, 2.262, 2.262, 5.000, 5.000],
        *[5.000, 5.000, 2.000, 2.000, 2.000, 2.000, 2.000, 2.000],
    ]


class AtomBeyondMimicPolicyCfg(BeyondMimicPolicyCfg):
    robot: str = "atom"

    # policy_name: str = "Slow_walk"
    # policy_name: str = "walk_straight_2000"
    policy_name: str = "run1_subject2_3000"

    obs_dof: DoFConfig = AtomBeyondMimicDoF()
    action_dof: DoFConfig = obs_dof

    action_beta: float = 1.0
    # ====== POLICY SPECIFIC CONFIGURATION ======
    without_state_estimator: bool = True

    action_scales: list[float] = [
        *[0.3198, 0.3198, 0.2878, 0.6031, 0.6031, 0.4398, 0.4398, 0.4618, 0.4618],
        *[0.1750, 0.1750, 1.0554, 1.0554, 0.1750, 0.1750, 1.0554, 1.0554, 0.1750, 0.1750],
        *[0.1750, 0.1750, 0.1700, 0.1700, 0.1700, 0.1700, 0.1700, 0.1700],
    ]
