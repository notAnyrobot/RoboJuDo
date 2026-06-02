from robojudo.environment.env_cfgs import MujocoEnvCfg

from .astro_env_cfg import AstroEnvCfg


class AstroMujocoEnvCfg(AstroEnvCfg, MujocoEnvCfg):
    env_type: str = MujocoEnvCfg.model_fields["env_type"].default
    is_sim: bool = MujocoEnvCfg.model_fields["is_sim"].default
    update_with_fk: bool = True
