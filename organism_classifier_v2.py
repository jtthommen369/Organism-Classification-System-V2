
movement = input("Movement detected? yes/no: ").lower()
heat = input("Heat detected? yes/no: ").lower()
color = input("Color: ").lower()
angularity = input("Angular? yes/no: ").lower()
shape = input("Shape (spherical/irregular/flat): ").lower()
facial_features = input("Facial features present? yes/no: ").lower()
density = input("Density (light/medium/dense): ").lower()
minerals = input("Minerals present? yes/no: ").lower()

classified = False

if movement == "yes" and heat == "yes" and angularity == "no" and shape == "irregular" and facial_features == "yes" and density == "medium" and minerals == "no":
    kingdom = "Animal"
    print(f"Kingdom: {kingdom}")
    backbone = input("Backbone present? yes/no: ").lower()
    if backbone == "yes":
        blood = input("Warm blooded? yes/no: ").lower()
        if blood == "yes":
            covering = input("Fur or feathers? ").lower()
            if covering == "fur":
                print("Mammal")
            elif covering == "feathers":
                print("Bird")
        elif blood == "no":
              habitat = input("Terrestrial or aquatic? ").lower()

              if habitat == "terrestrial":
                  print("Reptile")

              elif habitat == "aquatic":
                    scales = input("Scales present? yes/no: ").lower()

                    if scales == "yes":
                        print("Fish")
                    else:
                     print("Amphibian")
    else:
     exoskeleton = input("Exoskeleton present? yes/no: ").lower()
     if exoskeleton == "yes":
         print("Arthropod")
     else:
         shell = input("Shell present? yes/no: ").lower()
         if shell == "yes":
             print("Mollusk")
         else: 
            wormlike = input("Worm-like body? yes/no: ").lower()
            if wormlike == "yes":
              print("Annelid or Flatworm")

    classified = True

elif movement == "no" and heat == "no" and color == "green" and angularity == "no" and shape == "irregular" and facial_features == "no" and minerals == "no":
     kingdom = "Plant"
     print(f"Kingdom: {kingdom}")
     height = float(input("Height in feet: "))
     if height <= 5:
       plant_type = "Grass"
     elif height <= 10:
       plant_type = "Shrub"
     else:
       plant_type = "Tree"
     print(f"Plant type: {plant_type}")
     subtype = "Unknown"

     leaf = input("Leaf type (needle/broad/blade): ").lower()
     if leaf == "needle":
         smell = input("Pine smell? yes/no: ").lower()
         if smell == "yes":
           subtype = "Evergreen"
     elif leaf == "broad":
         subtype = "Deciduous"
     elif leaf == "blade":
         subtype = "Grass" 
     print(f"Plant subtype: {subtype}")
     classified = True

elif movement == "no" and heat == "no" and angularity == "yes" and (shape == "spherical" or shape == "flat") and facial_features == "no" and density == "light" and minerals == "no":
    kingdom = "Fungus or Protist"
    print(f"Kingdom: {kingdom}")
    classified = True

elif movement == "no" and heat == "no" and angularity == "yes" and (shape == "spherical" or shape == "flat") and facial_features == "no" and density == "dense" and minerals == "yes":
    classification = "Rock or Mineral"
    print (f"Classification: {classification}")
    classified = True
if not classified:
    print("Classification uncertain")