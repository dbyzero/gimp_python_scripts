#/usr/bin/env python

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


for row in rows:
	for step in steps:
		if row[0] % 2 == 0:
		    sprites = [
		        (0, "leftHand"),
		        (1, "feet"),
		        (2, "body"),
		        (3, "head"),
		        (4, "rightHand")
		    ]
		else:
		    sprites = [
		        (0, "rightHand"),
		        (1, "feet"),
		        (2, "body"),
		        (3, "head"),
		        (4, "leftHand")
		    ]
		for sprite in sprites:
			print "layer_sprite[" + str(row[0]) + "][" + str(step[0]) + "][" + str(sprite[0]) + "] = (0, 0, {'orientation':" + str(row[0] % 2) + ", 'delta':{'x':0, 'y':0}}) #"  + str(row[1]) + " " + str(step[1]) + " " + str(sprite[1])
