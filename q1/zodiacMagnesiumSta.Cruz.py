Date_of_birth = int(input("Enter year of birth: "))
if Date_of_birth < 1900:
  print("Year of birth must not be earlier than 1900.")
else:
  zodiac = [
    "Rat (鼠 / Shǔ)",
    "Ox (牛 / Niú)",
    "Tiger (虎 / Hǔ)",
    "Rabbit (兔 / Tù)",
    "Dragon (龙 / Lóng)",
    "Snake (蛇 / Shé)",
    "Horse (马 / Mǎ)",
    "Goat (羊 / Yáng)",
    "Monkey (猴 / Hóu)",
    "Rooster (鸡 / Jī)",
    "Dog (狗 / Gǒu)",
    "Pig (猪 / Zhū)",
  ]

index = (Date_of_birth - 1900) % 12
print("Your chinese zodiac sign is",zodiac[index])
