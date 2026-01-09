from robojudo.config import cfg_registry 
from robojudo.controller.ctrl_cfgs import (
    JoystickCtrlCfg,  # noqa: F401
    KeyboardCtrlCfg,  # noqa: F401
)
from robojudo.pipeline.pipeline_cfgs import (
    RlMultiPolicyPipelineCfg,  # noqa: F401
    RlPipelineCfg,  # noqa: F401
)

from .ctrl.atom_beyondmimic_ctrl_cfg import AtomBeyondmimicCtrlCfg  # noqa: F401
# from .ctrl.atom_motion_ctrl_cfg import AtomMotionCtrlCfg    # noqa: F401
from .env.atom_dummy_env_cfg import AtomDummyEnvCfg # noqa: F401
from .env.atom_mujoco_env_cfg import AtomMujocoEnvCfg   # noqa: F401
from .policy.atom_beyondmimic_policy_cfg import AtomBeyondMimicPolicyCfg    # noqa: F401


# ======================== Basic Configs ======================== #
@cfg_registry.register
class atom(RlPipelineCfg):
    """
    Atom robot configuration, Velocity Policy, Sim2Sim.
    """

    robot: str = "atom"
    env: AtomMujocoEnvCfg = AtomMujocoEnvCfg()

    ctrl: list[JoystickCtrlCfg | KeyboardCtrlCfg] = [
        JoystickCtrlCfg(),
        # KeyboardCtrlCfg(),
    ]

    policy: AtomBeyondMimicPolicyCfg = AtomBeyondMimicPolicyCfg()


@cfg_registry.register
class atom_beyondmimic(RlPipelineCfg):
    """
    BeyondMimic Policy, support bot with and without state estimator.
    """

    robot: str = "atom"
    env: AtomMujocoEnvCfg = AtomMujocoEnvCfg()
    ctrl: list[KeyboardCtrlCfg] = [
        KeyboardCtrlCfg()
    ]

    policy: AtomBeyondMimicPolicyCfg = AtomBeyondMimicPolicyCfg(
        policy_name="walk_straight",
        # policy_name="run1_subjec2_20000",
        # policy_name="single",
        without_state_estimator=True,
        use_modelmeta_config=True,  # use robot dof config from modelmeta
        use_motion_from_model=True, #use motion from onnx model
        max_timestep=9999,
    )


@cfg_registry.register
class atom_beyondmimic_with_ctrl(RlPipelineCfg):
    """
    BeyondMimic with External BeyondMimicCtrl as motion source.
    """

    robot: str = "atom"
    env: AtomMujocoEnvCfg = AtomMujocoEnvCfg()
    ctrl: list[KeyboardCtrlCfg | AtomBeyondmimicCtrlCfg] = [
        KeyboardCtrlCfg(),
        AtomBeyondmimicCtrlCfg(
            motion_name="dance1_subject2",  # you can put your own motiion file in assets/motions/atom
        ),
    ]

    policy: AtomBeyondMimicPolicyCfg = AtomBeyondMimicPolicyCfg(
        policy_name="Slow_walk",
        use_motion_from_model=False,    # use motion from BeyondmimicCtrl of the onnx
    )