# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())

    frontier = util.Stack();
    explored = []
    node = problem.getStartState()
    frontier.push(node)
    actionList = []
    transitionTable = dict()    #transitionTable = [parent, action]

    if problem.isGoalState(node):
        return ['Stop']
    while True:
        if frontier.isEmpty():
            util.raiseNotDefined()
        node = frontier.pop()
        explored.append(node)
        for child in problem.getSuccessors(node):
            if child[0] not in explored and child[0] not in frontier.list:
                transitionTable[child[0]] = [node,child[1]]
                now_state = child[0];
                if problem.isGoalState(child[0]):
                    while now_state!=problem.getStartState():
                        actionList.append(transitionTable[now_state][1])
                        now_state = transitionTable[now_state][0]
                    actionList.reverse()
                    return actionList
                frontier.push(child[0])
        
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())

    frontier = util.Queue();
    explored = []
    node = problem.getStartState()
    frontier.push(node)
    actionList = []
    transitionTable = dict()    #transitionTable = [parent, action]


    if problem.isGoalState(node):
        return ['Stop']
    while True:

        if frontier.isEmpty():
            util.raiseNotDefined()
        node = frontier.pop()
        explored.append(node)
        # print "node:", node
        # print "Is the node a goal?", problem.isGoalState(node)
        # print "node's successors:", problem.getSuccessors(node)
        for child in problem.getSuccessors(node):
            if child[0] not in explored and child[0] not in frontier.list:
                transitionTable[child[0]] = [node,child[1]]
                now_state = child[0];
                if problem.isGoalState(child[0]):
                    while now_state!=problem.getStartState():
                        actionList.append(transitionTable[now_state][1])
                        now_state = transitionTable[now_state][0]
                    actionList.reverse()
                    return actionList
                frontier.push(child[0])

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    frontier = util.PriorityQueue()
    explored = []
    actionList = []
    Map = dict()    #Map = [parent, action, total cost]
    node = problem.getStartState()
    frontier.push(node,0)
    Map[node] = [node,'Stop',0]
    
    if problem.isGoalState(node):
        return ['Stop']

    while True:
        if frontier.isEmpty():
            util.raiseNotDefined()
        node = frontier.pop()
        
        if problem.isGoalState(node):
            now_state = node
            while now_state!=problem.getStartState():
                actionList.append(Map[now_state][1])
                now_state = Map[now_state][0]
            actionList.reverse()
            return actionList
        
        explored.append(node)
        
        for child in problem.getSuccessors(node):
            # print node,child
            gn = Map[node][2]+child[2]
            if Map.has_key(child[0]):
                if gn<Map[child[0]][2]:
                    # print 'update map'
                    Map[child[0]][0] = node
                    Map[child[0]][1] = child[1]
                    Map[child[0]][2] = gn
                    if child[0] in frontier.heap:
                        frontier.update(child[0], gn)
                    else:
                        frontier.push(child[0], gn)
            else:
                Map[child[0]] = [node,child[1],gn]
                if child[0] in frontier.heap:
                        frontier.update(child[0], gn)
                else:
                    frontier.push(child[0], gn)
        

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    frontier = util.PriorityQueue()
    explored = []
    actionList = []
    Map = dict()    #Map = [parent, action, total cost(f(n) = g(n)+h(n))]
    node = problem.getStartState()
    frontier.push(node,heuristic(node,problem))    #now heuristic=manhattanHeuristic
    Map[node] = [node,'Stop',0]
    
    if problem.isGoalState(node):
        return ['Stop']

    while True:
        if frontier.isEmpty():
            util.raiseNotDefined()
        node = frontier.pop()

        # generate actionList when goal is finded
        if problem.isGoalState(node):
            now_state = node
            while now_state!=problem.getStartState():
                actionList.append(Map[now_state][1])
                now_state = Map[now_state][0]
            actionList.reverse()
            return actionList
        
        explored.append(node)
        
        for child in problem.getSuccessors(node):
            gn = Map[node][2]+child[2]
            hn = heuristic(child[0],problem)
            fn = gn + hn
            if Map.has_key(child[0]):
                if gn<Map[child[0]][2]:
                    # update Map
                    Map[child[0]][0] = node
                    Map[child[0]][1] = child[1]
                    Map[child[0]][2] = gn
                    if child[0] in frontier.heap:
                        frontier.update(child[0], fn)
                    else:
                        frontier.push(child[0], fn)
            else:
                Map[child[0]] = [node,child[1],gn]
                if child[0] in frontier.heap:
                        frontier.update(child[0], fn)
                else:
                    frontier.push(child[0], fn)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
