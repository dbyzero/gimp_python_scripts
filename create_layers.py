#!/usr/bin/env python

from gimpfu import *
import gimp

def dbyzero_deimos_layers_creation():
    global image
    global image_sprites
    global image_sprites_layer

    pdb.gimp_progress_update(0)
    rawImage = pdb.gimp_image_new( 1200, 1200, RGB )
    pdb.gimp_display_new(rawImage)
    image = gimp.image_list()[0]
    image_sprites = gimp.image_list()[1]
    image_sprites_layer = pdb.gimp_image_get_active_layer(image_sprites)

    rows = [
        (0, "standRight"),
        (1, "standLeft"),
        (2, "attackStandRight"),
        (3, "attackStandLeft"),
        (4, "runRight"),
        (5, "runLeft"),
        (6, "attackRunRight"),
        (7, "attackRunLeft"),
        (8, "flyRight"),
        (9, "flyLeft"),
        (10, "attackFlyRight"),
        (11, "attackFlyLeft")
    ]

    display = pdb.gimp_display_new(image)
    pdb.gimp_progress_init("Da job", display)

    for row in rows:
        add_row_layer(row)

    pdb.gimp_progress_end()
    # pdb.gimp_display_delete(display)

def add_row_layer(row):
    steps = [
        (0, "step1"),
        (1, "step2"),
        (2, "step3"),
        (3, "step4"),
        (4, "step5"),
        (5, "step6"),
        (6, "step7"),
        (7, "step8")
    ]

    row_layer = pdb.gimp_layer_group_new(image)
    pdb.gimp_image_insert_layer(image, row_layer, None, row[0])
    pdb.gimp_item_set_name(row_layer,row[1])
    for step in steps:
        add_a_layer(row_layer, row, step)

def add_a_layer(row_layer, row, step):
    group_layer = pdb.gimp_layer_group_new(image)
    pdb.gimp_image_insert_layer(image, group_layer, row_layer, step[0])
    pdb.gimp_item_set_name(group_layer,row[1] + '-' + step[1])

    if row[0] % 2 == 0:
        sprites = [
            (0, "leftHand"),
            (1, "feed"),
            (2, "body"),
            (3, "head"),
            (4, "rightHand")
        ]
    else:
        sprites = [
            (0, "rightHand"),
            (1, "feed"),
            (2, "body"),
            (3, "head"),
            (4, "leftHand")
        ]

    for sprite in sprites:
        x = 100 * step[0]
        y = 100 * row[0]
        layer_name = row[1] + '-' + step[1] + '-' + sprite[1]

        #create layer on created image
        layer = gimp.Layer(image, layer_name, 100, 100, RGB_IMAGE, 100, NORMAL_MODE)
        layer.translate(x,y)
        pdb.gimp_image_insert_layer(image, layer, group_layer, sprite[0])

        #copy the sprite from original layer
        pdb.gimp_image_select_rectangle(image_sprites, CHANNEL_OP_REPLACE, x, y ,100, 100)
        pdb.gimp_edit_copy(image_sprites_layer)

        #paste to created layer image the corresponding original layer
        target_layer = pdb.gimp_image_get_layer_by_name(image, layer_name)
        pdb.gimp_image_select_rectangle(image, CHANNEL_OP_REPLACE, x, y ,100, 100)
        layer_id = pdb.gimp_edit_paste(target_layer, True)
        pdb.gimp_floating_sel_anchor(layer_id)

        number_sprite = 12 * 8 * 5
        current_sprite = 0
        #previous rows
        current_sprite += row[0] * 8 * 5
        #previous step
        current_sprite += step[0] * 5
        #previous part
        current_sprite += sprite[0]
        pdb.gimp_progress_update(current_sprite / number_sprite)

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
    menu="<Image>/DeimosScript"
)

main()
