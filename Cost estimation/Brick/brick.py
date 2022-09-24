print("For volume-----------------------------")
Length=float(input("Length(m)="))
Depth=float(input("Depth(m)="))
Wall_Thickness=float(input("Wall Thickness="))

Brick_Masonry=Length*Depth*Wall_Thickness

print("Volume of Brick Masonry=",Brick_Masonry)


print("\n")
print("for no of bricks------------------------")
Length=float(input("Length(cm)="))
Width=float(input("Width(cm)="))
Height=float(input("Height(cm)="))

Brick_size=(Length*Width*Height)/1000000

print("Brick Size(m)=",Brick_size)


Total_Bricks=int(Brick_Masonry/Brick_size)

print("NO. of Bricks=",Total_Bricks)
