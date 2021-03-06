from .grid import TileGrid, TravelGraph
from .traffic import Traffic


class RoadNetwork():
    """Controls all data structures necessary for storing and maintaining a
    road network.
    """

    def __init__(self, w, h,
                 *, vehicle_stop_wait_time, intersection_clear_time):
        self.w = w
        self.h = h

        # Passed Constants
        self.VEHICLE_STOP_WAIT_TIME = vehicle_stop_wait_time
        self.INTERSECTION_CLEAR_TIME = intersection_clear_time

        # Network components
        self.grid = TileGrid(w, h)
        self.graph = TravelGraph()
        self.traffic = Traffic()

    def add_road(self, r, c, restrict_to_neighbors=True):
        """Add road node to the network

        returns: road added (bool)"""
        tile_added = self.grid.add_tile(r, c, restrict_to_neighbors)
        if tile_added:
            nbrs = self.grid.get_neighbors(r, c)
            self.graph.register_tile_intersection(r, c,
                                                  self.grid.tile_type(r, c),
                                                  nbrs)
            return True
        return False

    def step(self, tick):
        """Step the network by some amount of ticks"""
        self.traffic.step(tick, self.grid, self.VEHICLE_STOP_WAIT_TIME,
                          self.INTERSECTION_CLEAR_TIME)
