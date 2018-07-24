"""
Program displays shapes with properties defined by a
colours file, input file and coordinates files
Author: Dennis Playdon
"""

from tkinter import *

#-------------------------------------------
# -- Returns a colours dictionary
#-------------------------------------------
def create_colours_dictionary(filename):
    colours_dict = {}

    file = open(filename, 'r')
    contents_str = file.read()
    file.close()
    contents = contents_str.split("\n")
    
    for line in contents:
        element = line.split(':')   
        colours_dict[int(element[0])] = element[1]

    return colours_dict
    
	
#-------------------------------------------
# -- Returns a list of filenames
#-------------------------------------------
def create_filenames_list(filename):
    file = open(filename, 'r')
    contents = file.read()
    file.close

    filenames_list = contents.split("\n")


    return filenames_list
	
#-------------------------------------------
# -- Reads the coordinates from the input file
#-------------------------------------------
def read_coordinates(filename, shapes_dict):
    file = open(filename, 'r')
    contents_str = file.read()
    file.close()
    contents = contents_str.split('\n')

    for line in contents:
        line = line.split(',')
        
        for i in range(0, len(line)):
            line[i] = int(line[i])

        if len(line) == 4:
            shapes_dict[int(2)] = line
        elif len(line) == 6:
            shapes_dict[3] = line
        elif len(line) == 10:
            shapes_dict[5] = line
        elif len(line) == 12:
            shapes_dict[6] = line
	
	

#-------------------------------------------
# -- Draws all shapes
#-------------------------------------------
def draw_shapes(canvas, colours_dict, shapes_dict):
    if shapes_dict[2] != []:
        canvas.create_rectangle(shapes_dict[2], fill = colours_dict[2])
    if shapes_dict[3] != []:
        canvas.create_polygon(shapes_dict[3], fill = colours_dict[3])
    if shapes_dict[5] != []:
        canvas.create_polygon(shapes_dict[5], fill = colours_dict[5])
    if shapes_dict[6] != []:
        canvas.create_polygon(shapes_dict[6], fill = colours_dict[6])
    

#------------------------------------------
# MAIN FUNCTION
#------------------------------------------
def main():
    window = Tk()
    window.title("A5 - dpla823")
    window.geometry("600x600")
    a_canvas = Canvas(window)
    a_canvas.pack(fill=BOTH, expand=True)

    colours_dict = create_colours_dictionary('colours.txt')
    print(colours_dict)

    shapes_dict = {}
    for key in colours_dict.keys():
        shapes_dict[key] = []

    filenames_list = create_filenames_list('input.txt')
    print(filenames_list)

    for filename in filenames_list:
        read_coordinates(filename, shapes_dict)
        print(shapes_dict)
        draw_shapes(a_canvas, colours_dict, shapes_dict)

    window.mainloop()

main()
