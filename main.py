% Open Duplex A document in own repository
load_path = "C:\\Users\\Pc\\OneDrive - Danmarks Tekniske Universitet\\DTU\\Master\\3. semester\\41934 - Advanced BIM\\Duplex_A_20110907.ifc"
bpy.ops.bim.load_project(filepath=load_path)

import ifcopenshell
import bpy
from blenderbim.bim.ifc import IfcStore

% Add the IFC file that is active in your Blender environment so we can access the IFC file
file = IfcStore.get_file()

% Get all the spaces in your file by
spaces = file.by_type("IfcSpace")

% Check how many spaces we have
len(spaces)

% Print the names of the spaces by
for space in spaces:
	print(space.LongName)

IfcPropertyset
Se evt #700 i listen når man åbner Duplex med notesblokken. 
IfcPropertySingleValue indeholder info om areal
IfcElementQuantity
IfcQuantityArea

#38257=IFCPROPERTYSINGLEVALUE('Area',$,IFCAREAMEASURE(0.3269088000000023),$);

