import ifcopenshell
import bpy
from blenderbim.bim.ifc import IfcStore

## Open Duplex A document in own repository
#load_path = "C:\\Users\\Pc\\OneDrive - Danmarks Tekniske Universitet\\DTU\\Master\\3. semester\\41934 - Advanced BIM\\Duplex_A_20110907.ifc"
#bpy.ops.bim.load_project(filepath=load_path)

## Add the IFC file that is active in your Blender environment so we can access the IFC file
file = IfcStore.get_file()

## Get all the spaces in your file by
spaces = file.by_type("IfcSpace")
#walls = file-by_type("IfcWallsStandardCase")
#floors = file-by_type("IfcSlab")
beams = file.by_type("IfcBeam")

## Check how many spaces we have
#len(spaces)

## Print the names of the spaces by
#for space in spaces:
#    print(space.LongName)


## Get properties out - example with beams
#for beam in beams: 
#    for definition in beam.IsDefinedBy: #Find in Excel in column T in IfcBeams 
        
#        if definition.is_a("IfcRelDefinesByProperties"): # filter results
#            property_set = definition.RelatingPropertyDefinition
            
#            print(property_set.get_info())
            
            ## Sort by the name of the propertySet
#            if property_set.Name == "Pset_BeamCommon": 
#                for property in property_set.HasProperties:
                    
                    ## sort by the name of the property
#                    if property.Name == "IsExternal":
#                        print(property.NominalValue.wrappedValue)
             
             
## Try getting Area and volume properties out of space A102 (Current File\Collections\IfcSpace/A102 --> orange square object properties --> PSet_Revit_Dimensions)
for space in spaces: 
    for definition in space.IsDefinedBy: #Find in Excel in column N in IfcSpace 
        
        if definition.is_a("IfcRelDefinesByProperties"): # filter results
            property_set = definition.RelatingPropertyDefinition
            
#            print(property_set.get_info())
            
            ## Sort by the name of the propertySet
            if property_set.Name == "PSet_Revit_Dimensions": #PSet_Revit_Dimensions
                if property_set.HasProperties:
                    for property in property_set.HasProperties:
                    
                    ## sort by the name of the property
                        if property.Name == "Volume":
                            print("Volume = ",property.NominalValue.wrappedValue)
                            
                        if property.Name == "Area":
                            print("Area = ",property.NominalValue.wrappedValue)
                            
                            print(space.LongName)


## Prints [Volume, Area, LongName] (in that order)      
