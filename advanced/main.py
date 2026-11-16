mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

print(f"First destination is {mission_route[0]} and last destination is {mission_route[-1]}")
print(f"There are {len(mission_route)} destinations")
for i in range(0, len(mission_route)):
    print(f"{i + 1}: {mission_route[i]}")

if "Europa" in mission_route:
    print("Europa is on route")
else:
    print("Europa is not on route")

print()

def getInput(): 
    selection = input("Input: ")
    if selection in mission_route:
        return selection
    else:
        print("Invalid destination, please try again")
        return getInput()

selection = getInput()

print(f"{selection} is {mission_route.index(selection)} steps away from start of the journey")
print(f"{selection} is {len(mission_route) - mission_route.index(selection) - 1} steps away from end of the journey")
if mission_route[-1] != selection:
    print(f"Next stop is {mission_route[mission_route.index(selection) + 1]}")
