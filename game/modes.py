import random
from .roles import ROLES

def get_modes():
    return list(ROLES.keys())

def assign_roles(players, mode):
    roles = ROLES[mode]
    assigned = random.sample(roles * ((len(players)//len(roles))+1), len(players))
    return dict(zip(players, assigned))