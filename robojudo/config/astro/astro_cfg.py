from robojudo.config import cfg_registry
from robojudo.controller.ctrl_cfgs import KeyboardCtrlCfg
from robojudo.pipeline.pipeline_cfgs import RlPipelineCfg

from .env.astro_mujoco_env_cfg import AstroMujocoEnvCfg
from .policy.astro_protomotions_tracker_cfg import AstroProtoMotionsTrackerPolicyCfg


@cfg_registry.register
class astro_protomotions_tracker(RlPipelineCfg):
    """Astro ProtoMotions tracker in MuJoCo simulation."""

    robot: str = "astro"
    env: AstroMujocoEnvCfg = AstroMujocoEnvCfg(
        born_place_align=False,
        random_heading=True,
    )
    ctrl: list[KeyboardCtrlCfg] = [
        KeyboardCtrlCfg(
            triggers={
                "r": "[MOTION_RESET]",
                "i": "[SIM_REBORN]",
                "o": "[SHUTDOWN]",
                "<": "[MOTION_FADE_IN]",
                ">": "[MOTION_FADE_OUT]",
            },
        ),
    ]
    policy: AstroProtoMotionsTrackerPolicyCfg = AstroProtoMotionsTrackerPolicyCfg()
