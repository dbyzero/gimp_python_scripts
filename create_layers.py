#!/usr/bin/env python

from gimpfu import *
import gimp

def dbyzero_deimos_layers_creation():
    rawImage = pdb.gimp_image_new( 1000, 1000, RGB )
    pdb.gimp_display_new(rawImage)
    image = gimp.image_list()[0]
    layer = gimp.Layer(image, "calque1", 100, 100, RGB_IMAGE, 100, NORMAL_MODE)
    layer.translate(100,100)

    group_layer = pdb.gimp_layer_group_new(image)
    pdb.gimp_image_insert_layer(image, group_layer, None, 1)
    pdb.gimp_image_insert_layer(image, layer, group_layer, 1)


register(
    "dbyzero_deimos_layers_creation",
    "Create basic layer structure to use with spritesheets",
    "Create basic layer structure to use with spritesheets",
    "Dbyzero",
    "GPL Licence",
    "2015",
    "Create deimos layers structure",
    "*",
    [],
    [],
    dbyzero_deimos_layers_creation,
    menu="<Image>/Deimos"
)

main()
