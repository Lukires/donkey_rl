from gym.envs.registration import register


register(
    id='donkey-generated-roads-v0',
    entry_point='donkey_gym.envs:GeneratedRoadsEnv',
    max_episode_steps=2000,
)

register(
    id='donkey-warehouse-v0',
    entry_point='donkey_gym.envs:WarehouseEnv',
    max_episode_steps=2000,
)

register(
    id='donkey-avc-sparkfun-v0',
    entry_point='donkey_gym.envs:AvcSparkfunEnv',
    max_episode_steps=2000,
)

