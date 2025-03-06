def on_overlap_tile(sprite, location):
    pass
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile19
    """),
    on_overlap_tile)

def startlevel():
    if level == 0:
        tiles.set_current_tilemap(tilemap("""
            level0
        """))
    elif level == 1:
        tiles.set_current_tilemap(tilemap("""
            level3
        """))
    elif level == 2:
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
    else:
        tiles.set_current_tilemap(tilemap("""
            level4
        """))

def on_overlap_tile2(sprite2, location2):
    global level
    game.show_long_text("NEXT LEVEL", DialogLayout.BOTTOM)
    pause(1000)
    level += 1
    startlevel()
    tiles.place_on_random_tile(mySprite, assets.tile("""
        myTile10
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        End - Tile
    """),
    on_overlap_tile2)

level = 0
mySprite: Sprite = None
scene.set_background_image(assets.image("""
    Forest Forest
"""))
scroller.set_camera_scrolling_multipliers(2, 0, scroller.BackgroundLayer.LAYER0)
scroller.scroll_background_with_speed(-25, 0)
scroller.scroll_background_with_speed(50, 0, scroller.BackgroundLayer.LAYER1)
scroller.set_layer_image(scroller.BackgroundLayer.LAYER1,
    assets.image("""
        clouds
    """))
tiles.set_current_tilemap(tilemap("""
    level0
"""))
mySprite = sprites.create(img("""
        ........................
            .....ffff...............
            ...fff22fff.............
            ..fff2222fff............
            .fffeeeeeefff...........
            .ffe222222eef...........
            .fe2ffffff2ef...........
            .ffffeeeeffff...........
            ffefbf44fbfeff..........
            fee41fddf14eef..........
            .ffffdddddeef...........
            fddddf444eef............
            fbbbbf2222f4e...........
            fbbbbf2222fd4...........
            .fccf45544f44...........
            ..ffffffff..............
            ....ff..ff..............
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.player)
controller.player1.move_sprite(mySprite, 50, 50)
scene.camera_follow_sprite(mySprite)
tiles.place_on_random_tile(mySprite, assets.tile("""
    myTile10
"""))