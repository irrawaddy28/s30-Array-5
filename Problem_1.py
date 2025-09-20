'''
1041 Robot Bounded In Circle
https://leetcode.com/problems/robot-bounded-in-circle/description/

On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:
The north direction is the positive direction of the y-axis.
The south direction is the negative direction of the y-axis.
The east direction is the positive direction of the x-axis.
The west direction is the negative direction of the x-axis.

The robot can receive one of three instructions:
"G": go straight 1 unit.
"L": turn 90 degrees to the left (i.e., anti-clockwise direction).
"R": turn 90 degrees to the right (i.e., clockwise direction).

The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (0, 2). Direction: South.
"G": move one step. Position: (0, 1). Direction: South.
"G": move one step. Position: (0, 0). Direction: South.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (0, 2) --> (0, 1) --> (0, 0).
Based on that, we return true.

Example 2:
Input: instructions = "GG"
Output: false
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"G": move one step. Position: (0, 2). Direction: North.
Repeating the instructions, keeps advancing in the north direction and does not go into cycles.
Based on that, we return false.

Example 3:
Input: instructions = "GL"
Output: true
Explanation: The robot is initially at (0, 0) facing the north direction.
"G": move one step. Position: (0, 1). Direction: North.
"L": turn 90 degrees anti-clockwise. Position: (0, 1). Direction: West.
"G": move one step. Position: (-1, 1). Direction: West.
"L": turn 90 degrees anti-clockwise. Position: (-1, 1). Direction: South.
"G": move one step. Position: (-1, 0). Direction: South.
"L": turn 90 degrees anti-clockwise. Position: (-1, 0). Direction: East.
"G": move one step. Position: (0, 0). Direction: East.
"L": turn 90 degrees anti-clockwise. Position: (0, 0). Direction: North.
Repeating the instructions, the robot goes into the cycle: (0, 0) --> (0, 1) --> (-1, 1) --> (-1, 0) --> (0, 0).
Based on that, we return true.


Constraints:
1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.


Solution:
1. Linear traversal of array
The robot starts facing North and follows the instructions.

Note: Following one cycle of instructions may not land the robot
back at the origin. However, following the same set of instructions multiple times may land the robot at the origin. We are not given the number of times the robot needs to follow the instructions. All we know is that the robot will follow one round of instructions. We are required to declare if it is bounded or not.

After completing one set of instructions, the robot could be:
a) back at the origin, facing any direction
b) not at the origin and facing North
c) not at the origin and facing any direction but North

For the 3 cases above, We can declare that:
a) bounded
b) unbounded
c) bounded

The key insight is that after executing the instruction sequence once, if either:
The robot returns to the origin (0, 0), OR
The robot faces a different direction than north
Then the robot will stay within a bounded circle. This is because changing direction means the robot will eventually trace a closed path after multiple cycles (at most 4 cycles for a full rotation back to north).

For eg., consider
instructions = "GL". One set of instructions will not land the robot at the origin. But doing this 4 times (GL GL GL GL) will land the robot at the origin.
GL: (0,0) -> (0,1) (robot not at origin, facing west)
GL: (0,1) -> (-1,1)
GL: (-1,1) -> (-1,0)
GL: (-1,0) -> (0,0) (robot at origin)

Another eg.
GLRLG: (0,0) -> (-1,1) (robot not at origin, facing west)
GLRLG: (-1,1) -> (-2,0)
GLRLG: (-2,0) -> (-1,-1)
GLRLG: (-1,-1) -> (0,0) (robot at origin)

We track the:
1. position: using a tuple (x,y).

2. direction:  using an index i pointing to an element in a directions array
a) If the directions array is arranged clockwise: North, East, South, West
directions = [[0,1], [1,0], [0,-1], [-1,0]],
then,
Turn Right = (i + 1) % 4
Turn Left  = (i + 3) % 4
OR
a) If the directions array is arranged anti-clockwise: North, West, South, East
directions = [[0,1], [-1,0], [0,-1], [1,0]]
then,
Turn Right = (i + 3) % 4
Turn Left = (i + 1) % 4

https://youtu.be/fzGieY0mH2I?t=3329 (intro)
https://youtu.be/fzGieY0mH2I?t=4083 (directions array clockwise/anticlockwise formulation using NESW)
Time: O(N), Space: O(1)
'''
def isRobotBoundedClock(instructions: str) -> bool:
    if not instructions:
        return True

    # origin
    x, y = 0, 0
    i = 0 # index
    # directions array arranged clockwise
    dirs = [[0,1], [1,0], [0,-1], [-1,0]] # North, East, South, West
    for j in range(len(instructions)):
        c = instructions[j]
        if c == 'G':
            x = x + dirs[i][0]
            y = y + dirs[i][1]
        elif c == 'L':
            i = (i + 3) % 4
        elif c == 'R':
            i = (i + 1) % 4

    # is robot back at origin or robot not looking at North direction
    return (x == 0 and y == 0) or (i != 0)

def isRobotBoundedAntiClock(instructions: str) -> bool:
    if not instructions:
        return True

    # origin
    x, y = 0, 0
    i = 0 # index
    # directions array arranged anti-clockwise
    dirs = [[0,1], [-1,0], [0,-1], [1,0]] # North, West, South, East
    for j in range(len(instructions)):
        c = instructions[j]
        if c == 'G':
            x = x + dirs[i][0]
            y = y + dirs[i][1]
        elif c == 'L':
            i = (i + 1) % 4
        elif c == 'R':
            i = (i + 3) % 4

    # is robot back at origin or robot not looking at North direction
    return (x == 0 and y == 0) or (i != 0)

def run_isRobotBounded():
    tests = [("GGLLGG", True),
             ("GG", False), # robot keeps moving w/o changing dir
             ("LR", True ), # robot doesn't move but only changes dir
             ("GL", True), # anti clock
             ("GR", True), # clock
             ("GLRLG", True),
             ("LRG", False ),
    ]
    for test in tests:
        instructions, ans = test[0], test[1]
        print(f"\nInstructions: {instructions}")
        for method in ['clock', 'anticlock']:
            if method == 'clock':
                bounded = isRobotBoundedClock(instructions)
            elif method == 'anticlock':
                bounded = isRobotBoundedAntiClock(instructions)
            print(f"Is Robot Bounded? {bounded}")
            success = (ans == bounded)
            print(f"Pass: {success}")
            if not success:
                print(f"Failed")
                return

run_isRobotBounded()
