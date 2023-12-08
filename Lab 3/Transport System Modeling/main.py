from TransportSystemModeling import *
from cityGraph import Graph
from trafficLight import TrafficSignal
import random
random.seed(0)

firstSimulation = Simulator()

firstSimulation.createRoadsFromGraph(Graph)


firstSimulation.createGen({
    'vehicleRate' : 50,
    'vehicles' : [
        [1, {"path" : [(0, 3), (3, 7), (7, 6), (6, 9)]}],
        [1, {"path" : [(0, 3), (3, 2)]}],
        [1, {"path" : [(4, 3)]}],
        [1, {"path" : [(11, 7)]}],
        [1, {"path" : [(4, 3), (3, 2), (2, 5)]}],
        [1, {"path" : [(11, 7), (7, 6), (6, 2), (2, 1)]}],
        [1, {"path" : [(10, 7), (7, 6), (6, 8)]}],
        [1, {"path" : [(3, 2), (2, 6), (6, 7), (7, 3)]}]


    ]
})

trafficRoads1 = [[firstSimulation.roads[(0, 3)], firstSimulation.roads[(7, 3)]], [firstSimulation.roads[(4, 3)], firstSimulation.roads[(2, 3)]]]
trafficRoads2 = [[firstSimulation.roads[(3, 7)], firstSimulation.roads[(10, 7)]], [firstSimulation.roads[(11, 7)], firstSimulation.roads[(6, 7)]]]
trafficRoads3 = [[firstSimulation.roads[(2, 6)], firstSimulation.roads[(8, 6)]], [firstSimulation.roads[(7, 6)], firstSimulation.roads[(9, 6)]]]
trafficRoads4 = [[firstSimulation.roads[(1, 2)], firstSimulation.roads[(6, 2)]], [firstSimulation.roads[(3, 2)], firstSimulation.roads[(5, 2)]]]



trafficSignal1 = TrafficSignal(trafficRoads1)
trafficSignal2 = TrafficSignal(trafficRoads2)
trafficSignal3 = TrafficSignal(trafficRoads3)
trafficSignal4 = TrafficSignal(trafficRoads4)
firstSimulation.createTrafficSignal(trafficSignal1)
firstSimulation.createTrafficSignal(trafficSignal2)
firstSimulation.createTrafficSignal(trafficSignal3)
firstSimulation.createTrafficSignal(trafficSignal4)
firstSimulation.createLoads()


# Starting the simulation
firstWindow = Window(firstSimulation)
firstWindow.loop()