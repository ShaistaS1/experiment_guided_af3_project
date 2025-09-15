import torch

def crosslink_loss(coords, crosslinks, weight=1.0):
    loss = 0.0
    for (c1, r1, c2, r2, dmax) in crosslinks:
        d = torch.norm(coords[c1][r1-1] - coords[c2][r2-1])
        loss += torch.relu(d - dmax)**2
    return weight * loss
