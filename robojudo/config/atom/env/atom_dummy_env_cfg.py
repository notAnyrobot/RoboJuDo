from typing import Literal

from robojudo.environment.env_cfgs import RobotEnvCfg
from robojudo.tools.tool_cfgs import ZedOdometryCfg  # noqa: F401

# from robojudo.tools.tool_cfgs import ForwardKinematicCfg
from .atom_env_cfg import AtomEnvCfg


class AtomDummyEnvCfg(AtomEnvCfg, RobotEnvCfg):
    env_type: str = RobotEnvCfg.model_fields["env_type"].default
    # ====== ENV CONFIGURATION ======
    odometry_type: Literal["NONE", "DUMMY", "ZED"] = "DUMMY"
