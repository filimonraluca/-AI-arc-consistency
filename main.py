from collections import deque


class Region:
    name = None
    neighbors = []
    colors = []

    def __init__(self, r_name, r_neighbors, r_colors):
        self.name = r_name
        self.neighbors = r_neighbors
        self.colors = r_colors


def get_region_by_name(regions, name):
    for region in regions:
        if region.name == name:
            return region
    return None


def init_deque(q, regions):
    for region in regions:
        for neighbor in region.neighbors:
            q.append((region.name, neighbor))


def remove_inconsistent_values(regions, xi, xj):
    removed = False
    r_xi = get_region_by_name(regions, xi)
    r_xj = get_region_by_name(regions, xj)
    for x in r_xi.colors:
        compatible_colors = list(filter(lambda el: el != x, r_xj.colors))
        if not compatible_colors:
            r_xi.colors.remove(x)
            removed = True
    return removed


def AC_3(regions):
    q = deque()
    init_deque(q, regions)
    while q:
        (xi, xj) = q.popleft()
        if remove_inconsistent_values(regions, xi, xj):
            r_xi = get_region_by_name(regions, xi)
            for xk in r_xi.neighbors:
                q.append((xk, xi))


# reading data
if __name__ == '__main__':
    regions = []

    regions.append(Region('WA', ['SA', 'NT'], ['r', 'g', 'b']))
    regions.append(Region('SA', ['WA', 'NT'], ['r', 'g']))
    regions.append(Region('NT', ['SA', 'WA'], ['g']))

    # regions.append(Region('T', ['V'], ['r', 'b', 'g']))
    # regions.append(Region('WA', ['NT', 'SA'], ['r']))
    # regions.append(Region('NT', ['WA', 'Q', 'SA'], ['r', 'b', 'g']))
    # regions.append(Region('SA', ['WA', 'NT', 'Q', 'NSW', 'V'], ['r', 'b', 'g']))
    # regions.append(Region('Q', ['NT', 'SA', 'NSW'], ['g']))
    # regions.append(Region('NSW', ['Q', 'SA', 'V'], ['r', 'b', 'g']))
    # regions.append(Region('V', ['SA', 'NSW', 'T'], ['r', 'b', 'g']))

    AC_3(regions)
    for r in regions:
        print(r.name, r.colors)
