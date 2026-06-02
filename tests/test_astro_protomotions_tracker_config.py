import re

import mujoco
import numpy as np

from robojudo.config.config_manager import ConfigManager
from robojudo.environment.mujoco_env import MujocoEnv
from robojudo.policy.protomotions_tracker_policy import ProtoMotionsTrackerPolicy


def _model_joint_names(model: mujoco.MjModel) -> list[str]:
    names = []
    for joint_id in range(model.njnt):
        name = mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_JOINT, joint_id)
        if name != "floating_base_joint":
            names.append(name)
    return names


def _model_actuator_joint_names(model: mujoco.MjModel) -> list[str]:
    names = []
    for actuator_id in range(model.nu):
        joint_id = int(model.actuator_trnid[actuator_id][0])
        names.append(mujoco.mj_id2name(model, mujoco.mjtObj.mjOBJ_JOINT, joint_id))
    return names


def _resolve_default_pose(cfg, joint_names: list[str]) -> np.ndarray:
    policy = object.__new__(ProtoMotionsTrackerPolicy)
    policy.cfg_policy = cfg
    return policy._resolve_default_dof_pos(joint_names)


def test_astro_protomotions_tracker_config_resolves():
    cfg = ConfigManager("astro_protomotions_tracker").get_cfg()

    assert cfg.robot == "astro"
    assert cfg.env.xml.endswith("assets/robots/astro/astro_v1.xml")
    assert cfg.env.update_with_fk is True
    assert cfg.env.torso_name == "torso_link"
    assert cfg.env.born_place_align is False
    assert cfg.env.random_heading is True
    assert cfg.env.dof.joint_names[12:15] == [
        "waist_yaw_joint",
        "waist_pitch_joint",
        "waist_roll_joint",
    ]
    assert cfg.policy.robot == "astro"
    assert cfg.policy.policy_file.endswith("assets/models/astro/protomotions_tracker/unified_pipeline.onnx")


def test_astro_mujoco_maps_joints_and_actuators_by_name():
    cfg = ConfigManager("astro_protomotions_tracker").get_cfg()
    model = mujoco.MjModel.from_xml_path(cfg.env.xml)

    qpos_joint_names = _model_joint_names(model)
    actuator_joint_names = _model_actuator_joint_names(model)

    assert qpos_joint_names[12:15] == [
        "waist_yaw_joint",
        "waist_pitch_joint",
        "waist_roll_joint",
    ]
    assert actuator_joint_names[12:15] == [
        "waist_yaw_joint",
        "waist_roll_joint",
        "waist_pitch_joint",
    ]
    assert qpos_joint_names != actuator_joint_names

    qpos_indices = MujocoEnv._build_joint_qpos_indices(model, cfg.env.dof.joint_names)
    qvel_indices = MujocoEnv._build_joint_qvel_indices(model, cfg.env.dof.joint_names)
    ctrl_indices = MujocoEnv._build_actuator_ctrl_indices(model, cfg.env.dof.joint_names)

    waist_pitch_id = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, "waist_pitch_joint")
    assert qpos_indices[13] == model.jnt_qposadr[waist_pitch_id]
    assert qvel_indices[13] == model.jnt_dofadr[waist_pitch_id]
    assert ctrl_indices[13] == actuator_joint_names.index("waist_pitch_joint")
    assert ctrl_indices[14] == actuator_joint_names.index("waist_roll_joint")


def test_tracker_default_pose_patterns_are_robot_specific():
    from robojudo.config.astro.policy.astro_protomotions_tracker_cfg import AstroProtoMotionsTrackerPolicyCfg
    from robojudo.config.g1.policy.g1_protomotions_tracker_cfg import ProtoMotionsTrackerPolicyCfg

    joint_names = ["left_elbow_joint", "right_elbow_joint", "left_knee_joint"]

    g1_pose = _resolve_default_pose(ProtoMotionsTrackerPolicyCfg(), joint_names)
    astro_pose = _resolve_default_pose(AstroProtoMotionsTrackerPolicyCfg(), joint_names)

    assert np.allclose(g1_pose, [0.6, 0.6, 0.669])
    assert np.allclose(astro_pose, [0.2, 0.2, 0.669])
    assert all(re.fullmatch(pattern, "left_elbow_joint") for pattern in [".*_elbow_joint"])
