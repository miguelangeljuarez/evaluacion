def vent_net(vent_tot: float, dev: float, desc: float) -> float:
    """This program calculate the net sales."""
    vents_nets = vent_tot - (dev + desc)
    return vents_nets


def comp_tot(comps: float, spends: float) -> float:
    """This program calculate the total sales."""
    tot = comps + spends
    return tot
