from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    try:
        number = int(input("Enter a number: ").strip())
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if number % 4 == 0 and number % 5 == 0:
    result = f"{number} is divisible by both 4 and 5."
elif number % 4 == 0:
    result = f"{number} is divisible by 4."
elif number % 5 == 0:
    result = f"{number} is divisible by 5."
else:
    result = f"{number} is not divisible by 4 or 5."

mc.postToChat(result)

print("Result posted in Minecraft chat.")