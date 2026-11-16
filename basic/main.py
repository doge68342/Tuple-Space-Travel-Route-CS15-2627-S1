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
