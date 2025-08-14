nums = {'7', '2', '3', '0', '1', '.', ',', '5', '8', '9', '4', '6'}


def parse_weight(weight: str) -> float | False:
    if weight is None:
        return False

    if weight.count(',') + weight.count('.') > 1:
        return False

    if not weight.strip():
        return False

    if weight[0] in '.,' or weight[-1] in ',.':
        return False

    if not (set(weight) <= nums):
        return False

    if ',' in weight:
        weight = weight.replace(',', '.')
    try:
        weight = float(weight)
    except Exception:
        return False

    weight *= 0.001

    return weight
