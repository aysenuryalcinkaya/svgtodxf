import svg2dxf

# set the input and output file names and paths
input_file = "new.svg"
input_path = "/path/to/myvector.svg"
output_file = "myvector.dxf"
output_path = "/path/to/myvector.dxf"

# create an instance of the converter class
converter = svg2dxf.Converter()

# convert the input file to the output file
converter.convert(input_path, output_path)

# print a success message
print(f"Successfully converted {input_file} to {output_file}")
