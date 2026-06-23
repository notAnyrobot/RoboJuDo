import numpy as np
import pytest
import torch

from robojudo.utils.motion_utils import MotionPlayer


def _write_single_clip_cache(path):
    num_frames = 3
    torch.save(
        {
            "dof_pos": np.zeros((num_frames, 2), dtype=np.float32),
            "dof_vel": np.zeros((num_frames, 2), dtype=np.float32),
            "body_rot": np.zeros((num_frames, 1, 4), dtype=np.float32),
            "body_pos": np.zeros((num_frames, 1, 3), dtype=np.float32),
            "body_vel": np.zeros((num_frames, 1, 3), dtype=np.float32),
            "body_ang_vel": np.zeros((num_frames, 1, 3), dtype=np.float32),
            "control_dt": 0.02,
            "num_frames": num_frames,
        },
        path,
    )


def test_motion_player_rejects_nonzero_index_for_single_clip_cache(tmp_path):
    cache_path = tmp_path / "single_clip.50fps.pt"
    _write_single_clip_cache(cache_path)

    with pytest.raises(ValueError, match="single-clip cache.*motion_index=10"):
        MotionPlayer(cache_path, motion_index=10)
