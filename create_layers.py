#!/usr/bin/env python

from gimpfu import *
import gimp

def dbyzero_deimos_layers_creation():
    global image
    global image_sprites
    global image_sprites_layer
    global layer_list

    layer_list = get_layer_list()
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

    # display = pdb.gimp_display_new(image)
    # pdb.gimp_progress_init("Da job", display)

    for row in rows:
        add_row_layer(row)

    # pdb.gimp_progress_end()
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
        layer_list_x = 100 * layer_list[row[0]][step[0]][sprite[0]][0]
        layer_list_y = 100 * layer_list[row[0]][step[0]][sprite[0]][1]
        layer_name = row[1] + '-' + step[1] + '-' + sprite[1]

        #create layer on created image
        layer = gimp.Layer(image, layer_name, 100, 100, RGB_IMAGE, 100, NORMAL_MODE)
        layer.translate(x,y)
        pdb.gimp_image_insert_layer(image, layer, group_layer, sprite[0])

        #copy the sprite from original layer
        pdb.gimp_image_select_rectangle(image_sprites, CHANNEL_OP_REPLACE, layer_list_x, layer_list_y ,100, 100)
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
        # pdb.gimp_progress_update(current_sprite / number_sprite)

def get_layer_list():
    layer_list = range(0,12)
    for i in layer_list:
        layer_list[i] = range(0,8)
        for j in layer_list[i]:
            layer_list[i][j] = range(0,5)
            for k in layer_list[i][j]:
                layer_list[i][j][k] = (0,0)
                # layer_list[i][j][k] = i * 8 * 5 + j * 5 + k

    layer_list[0][0][0] = (0, 0) #standRight step1 leftHand
    layer_list[0][0][1] = (0, 0) #standRight step1 feed
    layer_list[0][0][2] = (0, 0) #standRight step1 body
    layer_list[0][0][3] = (0, 0) #standRight step1 head
    layer_list[0][0][4] = (0, 0) #standRight step1 rightHand
    layer_list[0][1][0] = (0, 0) #standRight step2 leftHand
    layer_list[0][1][1] = (0, 0) #standRight step2 feed
    layer_list[0][1][2] = (0, 0) #standRight step2 body
    layer_list[0][1][3] = (0, 0) #standRight step2 head
    layer_list[0][1][4] = (0, 0) #standRight step2 rightHand
    layer_list[0][2][0] = (0, 0) #standRight step3 leftHand
    layer_list[0][2][1] = (0, 0) #standRight step3 feed
    layer_list[0][2][2] = (0, 0) #standRight step3 body
    layer_list[0][2][3] = (0, 0) #standRight step3 head
    layer_list[0][2][4] = (0, 0) #standRight step3 rightHand
    layer_list[0][3][0] = (0, 0) #standRight step4 leftHand
    layer_list[0][3][1] = (0, 0) #standRight step4 feed
    layer_list[0][3][2] = (0, 0) #standRight step4 body
    layer_list[0][3][3] = (0, 0) #standRight step4 head
    layer_list[0][3][4] = (0, 0) #standRight step4 rightHand
    layer_list[0][4][0] = (0, 0) #standRight step5 leftHand
    layer_list[0][4][1] = (0, 0) #standRight step5 feed
    layer_list[0][4][2] = (0, 0) #standRight step5 body
    layer_list[0][4][3] = (0, 0) #standRight step5 head
    layer_list[0][4][4] = (0, 0) #standRight step5 rightHand
    layer_list[0][5][0] = (0, 0) #standRight step6 leftHand
    layer_list[0][5][1] = (0, 0) #standRight step6 feed
    layer_list[0][5][2] = (0, 0) #standRight step6 body
    layer_list[0][5][3] = (0, 0) #standRight step6 head
    layer_list[0][5][4] = (0, 0) #standRight step6 rightHand
    layer_list[0][6][0] = (0, 0) #standRight step7 leftHand
    layer_list[0][6][1] = (0, 0) #standRight step7 feed
    layer_list[0][6][2] = (0, 0) #standRight step7 body
    layer_list[0][6][3] = (0, 0) #standRight step7 head
    layer_list[0][6][4] = (0, 0) #standRight step7 rightHand
    layer_list[0][7][0] = (0, 0) #standRight step8 leftHand
    layer_list[0][7][1] = (0, 0) #standRight step8 feed
    layer_list[0][7][2] = (0, 0) #standRight step8 body
    layer_list[0][7][3] = (0, 0) #standRight step8 head
    layer_list[0][7][4] = (0, 0) #standRight step8 rightHand
    layer_list[1][0][0] = (0, 0) #standLeft step1 rightHand
    layer_list[1][0][1] = (0, 0) #standLeft step1 feed
    layer_list[1][0][2] = (0, 0) #standLeft step1 body
    layer_list[1][0][3] = (0, 0) #standLeft step1 head
    layer_list[1][0][4] = (0, 0) #standLeft step1 leftHand
    layer_list[1][1][0] = (0, 0) #standLeft step2 rightHand
    layer_list[1][1][1] = (0, 0) #standLeft step2 feed
    layer_list[1][1][2] = (0, 0) #standLeft step2 body
    layer_list[1][1][3] = (0, 0) #standLeft step2 head
    layer_list[1][1][4] = (0, 0) #standLeft step2 leftHand
    layer_list[1][2][0] = (0, 0) #standLeft step3 rightHand
    layer_list[1][2][1] = (0, 0) #standLeft step3 feed
    layer_list[1][2][2] = (0, 0) #standLeft step3 body
    layer_list[1][2][3] = (0, 0) #standLeft step3 head
    layer_list[1][2][4] = (0, 0) #standLeft step3 leftHand
    layer_list[1][3][0] = (0, 0) #standLeft step4 rightHand
    layer_list[1][3][1] = (0, 0) #standLeft step4 feed
    layer_list[1][3][2] = (0, 0) #standLeft step4 body
    layer_list[1][3][3] = (0, 0) #standLeft step4 head
    layer_list[1][3][4] = (0, 0) #standLeft step4 leftHand
    layer_list[1][4][0] = (0, 0) #standLeft step5 rightHand
    layer_list[1][4][1] = (0, 0) #standLeft step5 feed
    layer_list[1][4][2] = (0, 0) #standLeft step5 body
    layer_list[1][4][3] = (0, 0) #standLeft step5 head
    layer_list[1][4][4] = (0, 0) #standLeft step5 leftHand
    layer_list[1][5][0] = (0, 0) #standLeft step6 rightHand
    layer_list[1][5][1] = (0, 0) #standLeft step6 feed
    layer_list[1][5][2] = (0, 0) #standLeft step6 body
    layer_list[1][5][3] = (0, 0) #standLeft step6 head
    layer_list[1][5][4] = (0, 0) #standLeft step6 leftHand
    layer_list[1][6][0] = (0, 0) #standLeft step7 rightHand
    layer_list[1][6][1] = (0, 0) #standLeft step7 feed
    layer_list[1][6][2] = (0, 0) #standLeft step7 body
    layer_list[1][6][3] = (0, 0) #standLeft step7 head
    layer_list[1][6][4] = (0, 0) #standLeft step7 leftHand
    layer_list[1][7][0] = (0, 0) #standLeft step8 rightHand
    layer_list[1][7][1] = (0, 0) #standLeft step8 feed
    layer_list[1][7][2] = (0, 0) #standLeft step8 body
    layer_list[1][7][3] = (0, 0) #standLeft step8 head
    layer_list[1][7][4] = (0, 0) #standLeft step8 leftHand
    layer_list[2][0][0] = (0, 0) #attackStandRight step1 leftHand
    layer_list[2][0][1] = (0, 0) #attackStandRight step1 feed
    layer_list[2][0][2] = (0, 0) #attackStandRight step1 body
    layer_list[2][0][3] = (0, 0) #attackStandRight step1 head
    layer_list[2][0][4] = (0, 0) #attackStandRight step1 rightHand
    layer_list[2][1][0] = (0, 0) #attackStandRight step2 leftHand
    layer_list[2][1][1] = (0, 0) #attackStandRight step2 feed
    layer_list[2][1][2] = (0, 0) #attackStandRight step2 body
    layer_list[2][1][3] = (0, 0) #attackStandRight step2 head
    layer_list[2][1][4] = (0, 0) #attackStandRight step2 rightHand
    layer_list[2][2][0] = (0, 0) #attackStandRight step3 leftHand
    layer_list[2][2][1] = (0, 0) #attackStandRight step3 feed
    layer_list[2][2][2] = (0, 0) #attackStandRight step3 body
    layer_list[2][2][3] = (0, 0) #attackStandRight step3 head
    layer_list[2][2][4] = (0, 0) #attackStandRight step3 rightHand
    layer_list[2][3][0] = (0, 0) #attackStandRight step4 leftHand
    layer_list[2][3][1] = (0, 0) #attackStandRight step4 feed
    layer_list[2][3][2] = (0, 0) #attackStandRight step4 body
    layer_list[2][3][3] = (0, 0) #attackStandRight step4 head
    layer_list[2][3][4] = (0, 0) #attackStandRight step4 rightHand
    layer_list[2][4][0] = (0, 0) #attackStandRight step5 leftHand
    layer_list[2][4][1] = (0, 0) #attackStandRight step5 feed
    layer_list[2][4][2] = (0, 0) #attackStandRight step5 body
    layer_list[2][4][3] = (0, 0) #attackStandRight step5 head
    layer_list[2][4][4] = (0, 0) #attackStandRight step5 rightHand
    layer_list[2][5][0] = (0, 0) #attackStandRight step6 leftHand
    layer_list[2][5][1] = (0, 0) #attackStandRight step6 feed
    layer_list[2][5][2] = (0, 0) #attackStandRight step6 body
    layer_list[2][5][3] = (0, 0) #attackStandRight step6 head
    layer_list[2][5][4] = (0, 0) #attackStandRight step6 rightHand
    layer_list[2][6][0] = (0, 0) #attackStandRight step7 leftHand
    layer_list[2][6][1] = (0, 0) #attackStandRight step7 feed
    layer_list[2][6][2] = (0, 0) #attackStandRight step7 body
    layer_list[2][6][3] = (0, 0) #attackStandRight step7 head
    layer_list[2][6][4] = (0, 0) #attackStandRight step7 rightHand
    layer_list[2][7][0] = (0, 0) #attackStandRight step8 leftHand
    layer_list[2][7][1] = (0, 0) #attackStandRight step8 feed
    layer_list[2][7][2] = (0, 0) #attackStandRight step8 body
    layer_list[2][7][3] = (0, 0) #attackStandRight step8 head
    layer_list[2][7][4] = (0, 0) #attackStandRight step8 rightHand
    layer_list[3][0][0] = (0, 0) #attackStandLeft step1 rightHand
    layer_list[3][0][1] = (0, 0) #attackStandLeft step1 feed
    layer_list[3][0][2] = (0, 0) #attackStandLeft step1 body
    layer_list[3][0][3] = (0, 0) #attackStandLeft step1 head
    layer_list[3][0][4] = (0, 0) #attackStandLeft step1 leftHand
    layer_list[3][1][0] = (0, 0) #attackStandLeft step2 rightHand
    layer_list[3][1][1] = (0, 0) #attackStandLeft step2 feed
    layer_list[3][1][2] = (0, 0) #attackStandLeft step2 body
    layer_list[3][1][3] = (0, 0) #attackStandLeft step2 head
    layer_list[3][1][4] = (0, 0) #attackStandLeft step2 leftHand
    layer_list[3][2][0] = (0, 0) #attackStandLeft step3 rightHand
    layer_list[3][2][1] = (0, 0) #attackStandLeft step3 feed
    layer_list[3][2][2] = (0, 0) #attackStandLeft step3 body
    layer_list[3][2][3] = (0, 0) #attackStandLeft step3 head
    layer_list[3][2][4] = (0, 0) #attackStandLeft step3 leftHand
    layer_list[3][3][0] = (0, 0) #attackStandLeft step4 rightHand
    layer_list[3][3][1] = (0, 0) #attackStandLeft step4 feed
    layer_list[3][3][2] = (0, 0) #attackStandLeft step4 body
    layer_list[3][3][3] = (0, 0) #attackStandLeft step4 head
    layer_list[3][3][4] = (0, 0) #attackStandLeft step4 leftHand
    layer_list[3][4][0] = (0, 0) #attackStandLeft step5 rightHand
    layer_list[3][4][1] = (0, 0) #attackStandLeft step5 feed
    layer_list[3][4][2] = (0, 0) #attackStandLeft step5 body
    layer_list[3][4][3] = (0, 0) #attackStandLeft step5 head
    layer_list[3][4][4] = (0, 0) #attackStandLeft step5 leftHand
    layer_list[3][5][0] = (0, 0) #attackStandLeft step6 rightHand
    layer_list[3][5][1] = (0, 0) #attackStandLeft step6 feed
    layer_list[3][5][2] = (0, 0) #attackStandLeft step6 body
    layer_list[3][5][3] = (0, 0) #attackStandLeft step6 head
    layer_list[3][5][4] = (0, 0) #attackStandLeft step6 leftHand
    layer_list[3][6][0] = (0, 0) #attackStandLeft step7 rightHand
    layer_list[3][6][1] = (0, 0) #attackStandLeft step7 feed
    layer_list[3][6][2] = (0, 0) #attackStandLeft step7 body
    layer_list[3][6][3] = (0, 0) #attackStandLeft step7 head
    layer_list[3][6][4] = (0, 0) #attackStandLeft step7 leftHand
    layer_list[3][7][0] = (0, 0) #attackStandLeft step8 rightHand
    layer_list[3][7][1] = (0, 0) #attackStandLeft step8 feed
    layer_list[3][7][2] = (0, 0) #attackStandLeft step8 body
    layer_list[3][7][3] = (0, 0) #attackStandLeft step8 head
    layer_list[3][7][4] = (0, 0) #attackStandLeft step8 leftHand
    layer_list[4][0][0] = (0, 0) #runRight step1 leftHand
    layer_list[4][0][1] = (0, 0) #runRight step1 feed
    layer_list[4][0][2] = (0, 0) #runRight step1 body
    layer_list[4][0][3] = (0, 0) #runRight step1 head
    layer_list[4][0][4] = (0, 0) #runRight step1 rightHand
    layer_list[4][1][0] = (0, 0) #runRight step2 leftHand
    layer_list[4][1][1] = (0, 0) #runRight step2 feed
    layer_list[4][1][2] = (0, 0) #runRight step2 body
    layer_list[4][1][3] = (0, 0) #runRight step2 head
    layer_list[4][1][4] = (0, 0) #runRight step2 rightHand
    layer_list[4][2][0] = (0, 0) #runRight step3 leftHand
    layer_list[4][2][1] = (0, 0) #runRight step3 feed
    layer_list[4][2][2] = (0, 0) #runRight step3 body
    layer_list[4][2][3] = (0, 0) #runRight step3 head
    layer_list[4][2][4] = (0, 0) #runRight step3 rightHand
    layer_list[4][3][0] = (0, 0) #runRight step4 leftHand
    layer_list[4][3][1] = (0, 0) #runRight step4 feed
    layer_list[4][3][2] = (0, 0) #runRight step4 body
    layer_list[4][3][3] = (0, 0) #runRight step4 head
    layer_list[4][3][4] = (0, 0) #runRight step4 rightHand
    layer_list[4][4][0] = (0, 0) #runRight step5 leftHand
    layer_list[4][4][1] = (0, 0) #runRight step5 feed
    layer_list[4][4][2] = (0, 0) #runRight step5 body
    layer_list[4][4][3] = (0, 0) #runRight step5 head
    layer_list[4][4][4] = (0, 0) #runRight step5 rightHand
    layer_list[4][5][0] = (0, 0) #runRight step6 leftHand
    layer_list[4][5][1] = (0, 0) #runRight step6 feed
    layer_list[4][5][2] = (0, 0) #runRight step6 body
    layer_list[4][5][3] = (0, 0) #runRight step6 head
    layer_list[4][5][4] = (0, 0) #runRight step6 rightHand
    layer_list[4][6][0] = (0, 0) #runRight step7 leftHand
    layer_list[4][6][1] = (0, 0) #runRight step7 feed
    layer_list[4][6][2] = (0, 0) #runRight step7 body
    layer_list[4][6][3] = (0, 0) #runRight step7 head
    layer_list[4][6][4] = (0, 0) #runRight step7 rightHand
    layer_list[4][7][0] = (0, 0) #runRight step8 leftHand
    layer_list[4][7][1] = (0, 0) #runRight step8 feed
    layer_list[4][7][2] = (0, 0) #runRight step8 body
    layer_list[4][7][3] = (0, 0) #runRight step8 head
    layer_list[4][7][4] = (0, 0) #runRight step8 rightHand
    layer_list[5][0][0] = (0, 0) #runLeft step1 rightHand
    layer_list[5][0][1] = (0, 0) #runLeft step1 feed
    layer_list[5][0][2] = (0, 0) #runLeft step1 body
    layer_list[5][0][3] = (0, 0) #runLeft step1 head
    layer_list[5][0][4] = (0, 0) #runLeft step1 leftHand
    layer_list[5][1][0] = (0, 0) #runLeft step2 rightHand
    layer_list[5][1][1] = (0, 0) #runLeft step2 feed
    layer_list[5][1][2] = (0, 0) #runLeft step2 body
    layer_list[5][1][3] = (0, 0) #runLeft step2 head
    layer_list[5][1][4] = (0, 0) #runLeft step2 leftHand
    layer_list[5][2][0] = (0, 0) #runLeft step3 rightHand
    layer_list[5][2][1] = (0, 0) #runLeft step3 feed
    layer_list[5][2][2] = (0, 0) #runLeft step3 body
    layer_list[5][2][3] = (0, 0) #runLeft step3 head
    layer_list[5][2][4] = (0, 0) #runLeft step3 leftHand
    layer_list[5][3][0] = (0, 0) #runLeft step4 rightHand
    layer_list[5][3][1] = (0, 0) #runLeft step4 feed
    layer_list[5][3][2] = (0, 0) #runLeft step4 body
    layer_list[5][3][3] = (0, 0) #runLeft step4 head
    layer_list[5][3][4] = (0, 0) #runLeft step4 leftHand
    layer_list[5][4][0] = (0, 0) #runLeft step5 rightHand
    layer_list[5][4][1] = (0, 0) #runLeft step5 feed
    layer_list[5][4][2] = (0, 0) #runLeft step5 body
    layer_list[5][4][3] = (0, 0) #runLeft step5 head
    layer_list[5][4][4] = (0, 0) #runLeft step5 leftHand
    layer_list[5][5][0] = (0, 0) #runLeft step6 rightHand
    layer_list[5][5][1] = (0, 0) #runLeft step6 feed
    layer_list[5][5][2] = (0, 0) #runLeft step6 body
    layer_list[5][5][3] = (0, 0) #runLeft step6 head
    layer_list[5][5][4] = (0, 0) #runLeft step6 leftHand
    layer_list[5][6][0] = (0, 0) #runLeft step7 rightHand
    layer_list[5][6][1] = (0, 0) #runLeft step7 feed
    layer_list[5][6][2] = (0, 0) #runLeft step7 body
    layer_list[5][6][3] = (0, 0) #runLeft step7 head
    layer_list[5][6][4] = (0, 0) #runLeft step7 leftHand
    layer_list[5][7][0] = (0, 0) #runLeft step8 rightHand
    layer_list[5][7][1] = (0, 0) #runLeft step8 feed
    layer_list[5][7][2] = (0, 0) #runLeft step8 body
    layer_list[5][7][3] = (0, 0) #runLeft step8 head
    layer_list[5][7][4] = (0, 0) #runLeft step8 leftHand
    layer_list[6][0][0] = (0, 0) #attackRunRight step1 leftHand
    layer_list[6][0][1] = (0, 0) #attackRunRight step1 feed
    layer_list[6][0][2] = (0, 0) #attackRunRight step1 body
    layer_list[6][0][3] = (0, 0) #attackRunRight step1 head
    layer_list[6][0][4] = (0, 0) #attackRunRight step1 rightHand
    layer_list[6][1][0] = (0, 0) #attackRunRight step2 leftHand
    layer_list[6][1][1] = (0, 0) #attackRunRight step2 feed
    layer_list[6][1][2] = (0, 0) #attackRunRight step2 body
    layer_list[6][1][3] = (0, 0) #attackRunRight step2 head
    layer_list[6][1][4] = (0, 0) #attackRunRight step2 rightHand
    layer_list[6][2][0] = (0, 0) #attackRunRight step3 leftHand
    layer_list[6][2][1] = (0, 0) #attackRunRight step3 feed
    layer_list[6][2][2] = (0, 0) #attackRunRight step3 body
    layer_list[6][2][3] = (0, 0) #attackRunRight step3 head
    layer_list[6][2][4] = (0, 0) #attackRunRight step3 rightHand
    layer_list[6][3][0] = (0, 0) #attackRunRight step4 leftHand
    layer_list[6][3][1] = (0, 0) #attackRunRight step4 feed
    layer_list[6][3][2] = (0, 0) #attackRunRight step4 body
    layer_list[6][3][3] = (0, 0) #attackRunRight step4 head
    layer_list[6][3][4] = (0, 0) #attackRunRight step4 rightHand
    layer_list[6][4][0] = (0, 0) #attackRunRight step5 leftHand
    layer_list[6][4][1] = (0, 0) #attackRunRight step5 feed
    layer_list[6][4][2] = (0, 0) #attackRunRight step5 body
    layer_list[6][4][3] = (0, 0) #attackRunRight step5 head
    layer_list[6][4][4] = (0, 0) #attackRunRight step5 rightHand
    layer_list[6][5][0] = (0, 0) #attackRunRight step6 leftHand
    layer_list[6][5][1] = (0, 0) #attackRunRight step6 feed
    layer_list[6][5][2] = (0, 0) #attackRunRight step6 body
    layer_list[6][5][3] = (0, 0) #attackRunRight step6 head
    layer_list[6][5][4] = (0, 0) #attackRunRight step6 rightHand
    layer_list[6][6][0] = (0, 0) #attackRunRight step7 leftHand
    layer_list[6][6][1] = (0, 0) #attackRunRight step7 feed
    layer_list[6][6][2] = (0, 0) #attackRunRight step7 body
    layer_list[6][6][3] = (0, 0) #attackRunRight step7 head
    layer_list[6][6][4] = (0, 0) #attackRunRight step7 rightHand
    layer_list[6][7][0] = (0, 0) #attackRunRight step8 leftHand
    layer_list[6][7][1] = (0, 0) #attackRunRight step8 feed
    layer_list[6][7][2] = (0, 0) #attackRunRight step8 body
    layer_list[6][7][3] = (0, 0) #attackRunRight step8 head
    layer_list[6][7][4] = (0, 0) #attackRunRight step8 rightHand
    layer_list[7][0][0] = (0, 0) #attackRunLeft step1 rightHand
    layer_list[7][0][1] = (0, 0) #attackRunLeft step1 feed
    layer_list[7][0][2] = (0, 0) #attackRunLeft step1 body
    layer_list[7][0][3] = (0, 0) #attackRunLeft step1 head
    layer_list[7][0][4] = (0, 0) #attackRunLeft step1 leftHand
    layer_list[7][1][0] = (0, 0) #attackRunLeft step2 rightHand
    layer_list[7][1][1] = (0, 0) #attackRunLeft step2 feed
    layer_list[7][1][2] = (0, 0) #attackRunLeft step2 body
    layer_list[7][1][3] = (0, 0) #attackRunLeft step2 head
    layer_list[7][1][4] = (0, 0) #attackRunLeft step2 leftHand
    layer_list[7][2][0] = (0, 0) #attackRunLeft step3 rightHand
    layer_list[7][2][1] = (0, 0) #attackRunLeft step3 feed
    layer_list[7][2][2] = (0, 0) #attackRunLeft step3 body
    layer_list[7][2][3] = (0, 0) #attackRunLeft step3 head
    layer_list[7][2][4] = (0, 0) #attackRunLeft step3 leftHand
    layer_list[7][3][0] = (0, 0) #attackRunLeft step4 rightHand
    layer_list[7][3][1] = (0, 0) #attackRunLeft step4 feed
    layer_list[7][3][2] = (0, 0) #attackRunLeft step4 body
    layer_list[7][3][3] = (0, 0) #attackRunLeft step4 head
    layer_list[7][3][4] = (0, 0) #attackRunLeft step4 leftHand
    layer_list[7][4][0] = (0, 0) #attackRunLeft step5 rightHand
    layer_list[7][4][1] = (0, 0) #attackRunLeft step5 feed
    layer_list[7][4][2] = (0, 0) #attackRunLeft step5 body
    layer_list[7][4][3] = (0, 0) #attackRunLeft step5 head
    layer_list[7][4][4] = (0, 0) #attackRunLeft step5 leftHand
    layer_list[7][5][0] = (0, 0) #attackRunLeft step6 rightHand
    layer_list[7][5][1] = (0, 0) #attackRunLeft step6 feed
    layer_list[7][5][2] = (0, 0) #attackRunLeft step6 body
    layer_list[7][5][3] = (0, 0) #attackRunLeft step6 head
    layer_list[7][5][4] = (0, 0) #attackRunLeft step6 leftHand
    layer_list[7][6][0] = (0, 0) #attackRunLeft step7 rightHand
    layer_list[7][6][1] = (0, 0) #attackRunLeft step7 feed
    layer_list[7][6][2] = (0, 0) #attackRunLeft step7 body
    layer_list[7][6][3] = (0, 0) #attackRunLeft step7 head
    layer_list[7][6][4] = (0, 0) #attackRunLeft step7 leftHand
    layer_list[7][7][0] = (0, 0) #attackRunLeft step8 rightHand
    layer_list[7][7][1] = (0, 0) #attackRunLeft step8 feed
    layer_list[7][7][2] = (0, 0) #attackRunLeft step8 body
    layer_list[7][7][3] = (0, 0) #attackRunLeft step8 head
    layer_list[7][7][4] = (0, 0) #attackRunLeft step8 leftHand
    layer_list[8][0][0] = (0, 0) #flyRight step1 leftHand
    layer_list[8][0][1] = (0, 0) #flyRight step1 feed
    layer_list[8][0][2] = (0, 0) #flyRight step1 body
    layer_list[8][0][3] = (0, 0) #flyRight step1 head
    layer_list[8][0][4] = (0, 0) #flyRight step1 rightHand
    layer_list[8][1][0] = (0, 0) #flyRight step2 leftHand
    layer_list[8][1][1] = (0, 0) #flyRight step2 feed
    layer_list[8][1][2] = (0, 0) #flyRight step2 body
    layer_list[8][1][3] = (0, 0) #flyRight step2 head
    layer_list[8][1][4] = (0, 0) #flyRight step2 rightHand
    layer_list[8][2][0] = (0, 0) #flyRight step3 leftHand
    layer_list[8][2][1] = (0, 0) #flyRight step3 feed
    layer_list[8][2][2] = (0, 0) #flyRight step3 body
    layer_list[8][2][3] = (0, 0) #flyRight step3 head
    layer_list[8][2][4] = (0, 0) #flyRight step3 rightHand
    layer_list[8][3][0] = (0, 0) #flyRight step4 leftHand
    layer_list[8][3][1] = (0, 0) #flyRight step4 feed
    layer_list[8][3][2] = (0, 0) #flyRight step4 body
    layer_list[8][3][3] = (0, 0) #flyRight step4 head
    layer_list[8][3][4] = (0, 0) #flyRight step4 rightHand
    layer_list[8][4][0] = (0, 0) #flyRight step5 leftHand
    layer_list[8][4][1] = (0, 0) #flyRight step5 feed
    layer_list[8][4][2] = (0, 0) #flyRight step5 body
    layer_list[8][4][3] = (0, 0) #flyRight step5 head
    layer_list[8][4][4] = (0, 0) #flyRight step5 rightHand
    layer_list[8][5][0] = (0, 0) #flyRight step6 leftHand
    layer_list[8][5][1] = (0, 0) #flyRight step6 feed
    layer_list[8][5][2] = (0, 0) #flyRight step6 body
    layer_list[8][5][3] = (0, 0) #flyRight step6 head
    layer_list[8][5][4] = (0, 0) #flyRight step6 rightHand
    layer_list[8][6][0] = (0, 0) #flyRight step7 leftHand
    layer_list[8][6][1] = (0, 0) #flyRight step7 feed
    layer_list[8][6][2] = (0, 0) #flyRight step7 body
    layer_list[8][6][3] = (0, 0) #flyRight step7 head
    layer_list[8][6][4] = (0, 0) #flyRight step7 rightHand
    layer_list[8][7][0] = (0, 0) #flyRight step8 leftHand
    layer_list[8][7][1] = (0, 0) #flyRight step8 feed
    layer_list[8][7][2] = (0, 0) #flyRight step8 body
    layer_list[8][7][3] = (0, 0) #flyRight step8 head
    layer_list[8][7][4] = (0, 0) #flyRight step8 rightHand
    layer_list[9][0][0] = (0, 0) #flyLeft step1 rightHand
    layer_list[9][0][1] = (0, 0) #flyLeft step1 feed
    layer_list[9][0][2] = (0, 0) #flyLeft step1 body
    layer_list[9][0][3] = (0, 0) #flyLeft step1 head
    layer_list[9][0][4] = (0, 0) #flyLeft step1 leftHand
    layer_list[9][1][0] = (0, 0) #flyLeft step2 rightHand
    layer_list[9][1][1] = (0, 0) #flyLeft step2 feed
    layer_list[9][1][2] = (0, 0) #flyLeft step2 body
    layer_list[9][1][3] = (0, 0) #flyLeft step2 head
    layer_list[9][1][4] = (0, 0) #flyLeft step2 leftHand
    layer_list[9][2][0] = (0, 0) #flyLeft step3 rightHand
    layer_list[9][2][1] = (0, 0) #flyLeft step3 feed
    layer_list[9][2][2] = (0, 0) #flyLeft step3 body
    layer_list[9][2][3] = (0, 0) #flyLeft step3 head
    layer_list[9][2][4] = (0, 0) #flyLeft step3 leftHand
    layer_list[9][3][0] = (0, 0) #flyLeft step4 rightHand
    layer_list[9][3][1] = (0, 0) #flyLeft step4 feed
    layer_list[9][3][2] = (0, 0) #flyLeft step4 body
    layer_list[9][3][3] = (0, 0) #flyLeft step4 head
    layer_list[9][3][4] = (0, 0) #flyLeft step4 leftHand
    layer_list[9][4][0] = (0, 0) #flyLeft step5 rightHand
    layer_list[9][4][1] = (0, 0) #flyLeft step5 feed
    layer_list[9][4][2] = (0, 0) #flyLeft step5 body
    layer_list[9][4][3] = (0, 0) #flyLeft step5 head
    layer_list[9][4][4] = (0, 0) #flyLeft step5 leftHand
    layer_list[9][5][0] = (0, 0) #flyLeft step6 rightHand
    layer_list[9][5][1] = (0, 0) #flyLeft step6 feed
    layer_list[9][5][2] = (0, 0) #flyLeft step6 body
    layer_list[9][5][3] = (0, 0) #flyLeft step6 head
    layer_list[9][5][4] = (0, 0) #flyLeft step6 leftHand
    layer_list[9][6][0] = (0, 0) #flyLeft step7 rightHand
    layer_list[9][6][1] = (0, 0) #flyLeft step7 feed
    layer_list[9][6][2] = (0, 0) #flyLeft step7 body
    layer_list[9][6][3] = (0, 0) #flyLeft step7 head
    layer_list[9][6][4] = (0, 0) #flyLeft step7 leftHand
    layer_list[9][7][0] = (0, 0) #flyLeft step8 rightHand
    layer_list[9][7][1] = (0, 0) #flyLeft step8 feed
    layer_list[9][7][2] = (0, 0) #flyLeft step8 body
    layer_list[9][7][3] = (0, 0) #flyLeft step8 head
    layer_list[9][7][4] = (0, 0) #flyLeft step8 leftHand
    layer_list[10][0][0] = (0, 0) #attackFlyRight step1 leftHand
    layer_list[10][0][1] = (0, 0) #attackFlyRight step1 feed
    layer_list[10][0][2] = (0, 0) #attackFlyRight step1 body
    layer_list[10][0][3] = (0, 0) #attackFlyRight step1 head
    layer_list[10][0][4] = (0, 0) #attackFlyRight step1 rightHand
    layer_list[10][1][0] = (0, 0) #attackFlyRight step2 leftHand
    layer_list[10][1][1] = (0, 0) #attackFlyRight step2 feed
    layer_list[10][1][2] = (0, 0) #attackFlyRight step2 body
    layer_list[10][1][3] = (0, 0) #attackFlyRight step2 head
    layer_list[10][1][4] = (0, 0) #attackFlyRight step2 rightHand
    layer_list[10][2][0] = (0, 0) #attackFlyRight step3 leftHand
    layer_list[10][2][1] = (0, 0) #attackFlyRight step3 feed
    layer_list[10][2][2] = (0, 0) #attackFlyRight step3 body
    layer_list[10][2][3] = (0, 0) #attackFlyRight step3 head
    layer_list[10][2][4] = (0, 0) #attackFlyRight step3 rightHand
    layer_list[10][3][0] = (0, 0) #attackFlyRight step4 leftHand
    layer_list[10][3][1] = (0, 0) #attackFlyRight step4 feed
    layer_list[10][3][2] = (0, 0) #attackFlyRight step4 body
    layer_list[10][3][3] = (0, 0) #attackFlyRight step4 head
    layer_list[10][3][4] = (0, 0) #attackFlyRight step4 rightHand
    layer_list[10][4][0] = (0, 0) #attackFlyRight step5 leftHand
    layer_list[10][4][1] = (0, 0) #attackFlyRight step5 feed
    layer_list[10][4][2] = (0, 0) #attackFlyRight step5 body
    layer_list[10][4][3] = (0, 0) #attackFlyRight step5 head
    layer_list[10][4][4] = (0, 0) #attackFlyRight step5 rightHand
    layer_list[10][5][0] = (0, 0) #attackFlyRight step6 leftHand
    layer_list[10][5][1] = (0, 0) #attackFlyRight step6 feed
    layer_list[10][5][2] = (0, 0) #attackFlyRight step6 body
    layer_list[10][5][3] = (0, 0) #attackFlyRight step6 head
    layer_list[10][5][4] = (0, 0) #attackFlyRight step6 rightHand
    layer_list[10][6][0] = (0, 0) #attackFlyRight step7 leftHand
    layer_list[10][6][1] = (0, 0) #attackFlyRight step7 feed
    layer_list[10][6][2] = (0, 0) #attackFlyRight step7 body
    layer_list[10][6][3] = (0, 0) #attackFlyRight step7 head
    layer_list[10][6][4] = (0, 0) #attackFlyRight step7 rightHand
    layer_list[10][7][0] = (0, 0) #attackFlyRight step8 leftHand
    layer_list[10][7][1] = (0, 0) #attackFlyRight step8 feed
    layer_list[10][7][2] = (0, 0) #attackFlyRight step8 body
    layer_list[10][7][3] = (0, 0) #attackFlyRight step8 head
    layer_list[10][7][4] = (0, 0) #attackFlyRight step8 rightHand
    layer_list[11][0][0] = (0, 0) #attackFlyLeft step1 rightHand
    layer_list[11][0][1] = (0, 0) #attackFlyLeft step1 feed
    layer_list[11][0][2] = (0, 0) #attackFlyLeft step1 body
    layer_list[11][0][3] = (0, 0) #attackFlyLeft step1 head
    layer_list[11][0][4] = (0, 0) #attackFlyLeft step1 leftHand
    layer_list[11][1][0] = (0, 0) #attackFlyLeft step2 rightHand
    layer_list[11][1][1] = (0, 0) #attackFlyLeft step2 feed
    layer_list[11][1][2] = (0, 0) #attackFlyLeft step2 body
    layer_list[11][1][3] = (0, 0) #attackFlyLeft step2 head
    layer_list[11][1][4] = (0, 0) #attackFlyLeft step2 leftHand
    layer_list[11][2][0] = (0, 0) #attackFlyLeft step3 rightHand
    layer_list[11][2][1] = (0, 0) #attackFlyLeft step3 feed
    layer_list[11][2][2] = (0, 0) #attackFlyLeft step3 body
    layer_list[11][2][3] = (0, 0) #attackFlyLeft step3 head
    layer_list[11][2][4] = (0, 0) #attackFlyLeft step3 leftHand
    layer_list[11][3][0] = (0, 0) #attackFlyLeft step4 rightHand
    layer_list[11][3][1] = (0, 0) #attackFlyLeft step4 feed
    layer_list[11][3][2] = (0, 0) #attackFlyLeft step4 body
    layer_list[11][3][3] = (0, 0) #attackFlyLeft step4 head
    layer_list[11][3][4] = (0, 0) #attackFlyLeft step4 leftHand
    layer_list[11][4][0] = (0, 0) #attackFlyLeft step5 rightHand
    layer_list[11][4][1] = (0, 0) #attackFlyLeft step5 feed
    layer_list[11][4][2] = (0, 0) #attackFlyLeft step5 body
    layer_list[11][4][3] = (0, 0) #attackFlyLeft step5 head
    layer_list[11][4][4] = (0, 0) #attackFlyLeft step5 leftHand
    layer_list[11][5][0] = (0, 0) #attackFlyLeft step6 rightHand
    layer_list[11][5][1] = (0, 0) #attackFlyLeft step6 feed
    layer_list[11][5][2] = (0, 0) #attackFlyLeft step6 body
    layer_list[11][5][3] = (0, 0) #attackFlyLeft step6 head
    layer_list[11][5][4] = (0, 0) #attackFlyLeft step6 leftHand
    layer_list[11][6][0] = (0, 0) #attackFlyLeft step7 rightHand
    layer_list[11][6][1] = (0, 0) #attackFlyLeft step7 feed
    layer_list[11][6][2] = (0, 0) #attackFlyLeft step7 body
    layer_list[11][6][3] = (0, 0) #attackFlyLeft step7 head
    layer_list[11][6][4] = (0, 0) #attackFlyLeft step7 leftHand
    layer_list[11][7][0] = (0, 0) #attackFlyLeft step8 rightHand
    layer_list[11][7][1] = (0, 0) #attackFlyLeft step8 feed
    layer_list[11][7][2] = (0, 0) #attackFlyLeft step8 body
    layer_list[11][7][3] = (0, 0) #attackFlyLeft step8 head
    layer_list[11][7][4] = (0, 0) #attackFlyLeft step8 leftHand
    return layer_list


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
