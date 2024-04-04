import ezdxf
from ezdxf.addons import Importer

# set the input and output file names and paths
input_file = "new.svg"
input_path = r"C:\Users\ASUS\Desktop\me, myself and I\svgtodxf\new.svg"

output_file = "new.dxf"
output_path =  r"C:\Users\ASUS\Desktop\me, myself and I\svgtodxf\new.dxf"

# create a new DXF document using the new method
doc = ezdxf.new()

# import the SVG file using the read_svg_file method of the Importer class
importer = Importer.read_svg_file(input_path)

# import the entities into the modelspace of the new document using the import_to_modelspace method of the Importer instance
importer.import_to_modelspace(doc)

# save the DXF file using the saveas method of the document instance
doc.saveas(output_path)

# print a success message
print(f"Successfully converted {input_file} to {output_file}")
