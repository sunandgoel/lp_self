from collections import defaultdict

jug1, jug2 = map(int, input("ENTER CAPACITY OF <JUG1, JUG2>: ").split())
aim = int(input("ENTER THE FINAL AMOUNT REQUIRED: "))
visited = defaultdict(lambda: False)

def waterJugSolver(amt1, amt2): 

    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print("JUG 1:", amt1, ", JUG 2:", amt2)
        return True

    if visited[(amt1, amt2)] == False:
        print("JUG 1:", amt1, ", JUG 2:", amt2)

        visited[(amt1, amt2)] = True

        return (waterJugSolver(0, amt2) or
                waterJugSolver(amt1, 0) or
                waterJugSolver(jug1, amt2) or
                waterJugSolver(amt1, jug2) or
                waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
                amt2 - min(amt2, (jug1-amt1))) or
                waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
                amt2 + min(amt1, (jug2-amt2))))

    else:
        return False
  
print("STEPS: ")

waterJugSolver(0, 0)
