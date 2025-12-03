from turtle import forward
from robojudo.config import ASSETS_DIR
from robojudo.environment.env_cfgs import EnvCfg
from robojudo.tools.tool_cfgs import DoFConfig, ForwardKinematicCfg


class Atom_27DoF(DoFConfig):
    # num_dofs as 27
    joint_names: list[str] = [
        *[
            "left_hip_pitch_joint",
            "left_hip_roll_joint",
            "left_hip_yaw_joint",
            "left_knee_joint",
            "left_ankle_pitch_joint",
            "left_ankle_roll_joint",
        ],
        *[
            "right_hip_pitch_joint",
            "right_hip_roll_joint",
            "right_hip_yaw_joint",
            "right_knee_joint",
            "right_ankle_pitch_joint",
            "right_ankle_roll_joint",
        ],
        *["waist_yaw_joint",],
        *[
            "left_shoulder_pitch_joint",
            "left_shoulder_roll_joint",
            "left_shoulder_yaw_joint",
            "left_elbow_joint",
            "left_wrist_roll_joint",
            "left_wrist_pitch_joint",
            "left_wrist_yaw_joint",
        ],
        *[
            "right_shoulder_pitch_joint",
            "right_shoulder_roll_joint",
            "right_shoulder_yaw_joint",
            "right_elbow_joint",
            "right_wrist_roll_joint",
            "right_wrist_pitch_joint",
            "right_wrist_yaw_joint",
        ],
    ]
    default_pos: list[float] | None = [
        *[-0.1, 0.0, 0.0, 0.3, -0.2, 0.0],
        *[-0.1, 0.0, 0.0, 0.3, -0.2, 0.0],
        *[0.0],
        *[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        *[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ]
    stiffness: list[float] | None = [
        *[100, 100, 100, 150, 40, 40],
        *[100, 100, 100, 150, 40, 40],
        *[200,],
        *[40, 40, 40, 40, 20, 20, 20],
        *[40, 40, 40, 40, 20, 20, 20],
    ]
    damping: list[float] | None = [
        *[5, 5, 5, 5, 2, 2],
        *[5, 5, 5, 5, 2, 2],
        *[6],
        *[2, 2, 2, 2, 2, 2, 2],
        *[2, 2, 2, 2, 2, 2, 2],
    ]
    torque_limits: list[float] | None = [
        *[200, 200, 200, 300, 40, 40],
        *[200, 200, 200, 300, 40, 40],
        *[200,],
        *[40, 40, 40, 40, 18, 18, 18],
        *[40, 40, 40, 40, 18, 18, 18],
    ]
    position_limits: list[list[float]] | None = [
        *[
            [-2.5656, 3.0194],
            [-0.2618, 1.6581],
            [-2.7925, 2.7925],
            [0, 2.4871],
            [-0.8727, 0.5236],
            [-0.48, 0.48],
        ],
        *[
            [-2.5656, 3.0194],
            [-1.6581, 0.2618],
            [-2.7925, 2.7925],
            [0, 2.4871],
            [-0.8727, 0.5236],
            [-0.48, 0.48],
        ],
        *[
            [-2.7925, 2.7925],
        ],
        *[
            [-2.97, 2.97],
            [-0.43, 3.14],
            [-2.97, 2.97],
            [-1.57, 2.0],
            [-2.97, 2.97],
            [-1.57, 1.57],
            [-1.57, 1.57],
        ],
        *[
            [-2.97, 2.97],
            [-3.14, 0.43],
            [-2.97, 2.97],
            [-1.57, 2.0],
            [-2.97, 2.97],
            [-1.57, 1.57],
            [-1.57, 1.57],
        ],
    ]


class AtomEnvCfg(EnvCfg):
    xml: str = (ASSETS_DIR / "robots" / "atom" / "atom_27dof.xml").as_posix()

    dof: DoFConfig = Atom_27DoF()

    forward_kinematic: ForwardKinematicCfg | None = ForwardKinematicCfg(
        xml_path=xml,
        debug_viz=False,
        kinematic_joint_names=dof.joint_names,
    )
    update_with_fk: bool = True
    torso_name: str = "torso_link"