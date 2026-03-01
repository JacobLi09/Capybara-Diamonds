# The script of the game goes in this file.

#Characters: 
define r = Character('????', color="#c8ffc8")
image r = "images/Villager.png"

define m = Character('Mackenzeighlynnabelle')
image m = "images/Mackenzie.png"
image m neutral = "images/Mackenzie.png"
image m happy = "images/MackenzieHappy.png"
image m scared = "images/MackenzieDizzy.png"
image m yay = "images/MackenzieYay.png"

define g = Character("Grafat")
image g neutral = "images/Grafat.png"
image g happy = "images/GrafatHappy.png"
image g scared = "images/GrafatScared.png"
image g yay = "images/GrafatYay.png"
image g dead = "images/GrafatDead.png"

define v = Character("Vlad")
image v = "images/Vlad.png"

image monster = "images/Monster.png"

image bg cave = "images/Cave.png"
image bg town = "images/townCapybara.png"
image bg forest = "images/townCapybara.png"
image miner = "images/Vlad.png"

default has_pickaxe = False
default has_cheese = False
default has_gravel = False
default has_dynamite = False
default tools_chosen = 0



#Scenes:
image town_capybara = "images/townCapybara.png"

transform town_bg_zoomed_out:
    zoom 0.85
    xalign 0.5
    yalign 0.5

image cave = "images/cave.png"

transform cave_bg_zoomed_out:
    zoom 0.57
    xalign 0.5
    yalign 0.5

transform villager_higher:
    zoom 1.45
    xalign 0.5
    yalign 0.5

transform Mackenzeighlynnabelle_higher:
    zoom 1.90
    xalign 0.5
    yalign 0.5

transform Grafat_higher:
    zoom 1.90
    xalign 0.5
    yalign 0.5

transform Vlad_higher:
    zoom 1.10
    xalign 0.5
    yalign 0.5

transform monster_higher:
    zoom 2.00
    xalign 0.5
    yalign 0.5

transform monster_hit_shake:
    xoffset 0
    linear 0.04 xoffset -25
    linear 0.04 xoffset 25
    linear 0.04 xoffset -18
    linear 0.04 xoffset 18
    linear 0.04 xoffset -10
    linear 0.04 xoffset 10
    linear 0.04 xoffset 0

transform monster_chase_shake:
    xoffset 0
    yoffset 0
    linear 0.07 xoffset -12 yoffset 2
    linear 0.07 xoffset 12 yoffset -2
    repeat


# The game starts here.


label start:
    scene black


    "{cps=25}...{/cps}"
    "{cps=25}Long before time had a name, there rested a humble village in the Northern Lands.{/cps}"
    "{cps=25}Inhabiting this village were little, cute, adorable Capybaras!{cps=25}"
    "{cps=25}For a long time, the little town prospered, never having to worry about food or resources, until… recently.{cps=25}"
    "{cps=25}A landslide had blocked off major trade routes and left the village, resources were left scarce and draining.{cps=25}"
    "{cps=25}Passing through the Northern Lands during your journey, you stop at a small village to rest and resupply your stash.{/cps}"
    
    scene town_capybara at town_bg_zoomed_out
    with dissolve
    show r at villager_higher

    r "{cps=25}Adventurer! Thank heavens you passed by! We are in desperate need of aid.{/cps}"
    r "{cps=25}A landslide has blocked off our most valuable trade route, leaving us running out of diamonds!{/cps}"
    r "{cps=25}Some of us Capy’s were gonna go mining and we need help we can get!{/cps}"
   
    menu:
        "Are you in?"

        "Yes!":
            jump same_outcome

        "Or... Yes!":
            jump same_outcome

label same_outcome:
    r "{cps=25}Thank you so much!! I'll lead you over to the mines{/cps}"

    scene black
    with fade

    "{cps=25}You follow the mysterious villager as he leads you to the mines.{/cps}"

    scene cave at cave_bg_zoomed_out
    with dissolve
    "{cps=25}As you step into the mine, you are encountered with 3 different capybaras.{/cps}"
    show m at Mackenzeighlynnabelle_higher
    "{cps=25}A mage, named Mackenzeighlynnabelle,{/cps}"
    hide m
    show g neutral at Grafat_higher
    "{cps=25}a warrior, named Graf Granat,{/cps}"
    hide g
    show v at Vlad_higher
    "{cps=25}and an old miner, named Vlad.{/cps}"
    hide v
    "{cps=25}They stand before you, waiting for your decision.{/cps}"
    "{cps=25}Which capybara will you accompany?{/cps}"
    menu:
        "Who would you like to accompany?"

        "Mackenzeighlynnabelle":
            jump mackenzie_story    

        "Granat":
            jump grafat_story

        "Vlad":
            jump vlad_story

#Mackenzie Story Start:
label mackenzie_story:
    "{cps=25}Mackenzeighlynnabelle smiles and steps forward.{/cps}"

    menu:
        "Are you ready to go?"

        "Yes!":
            show m neutral at Mackenzeighlynnabelle_higher
            jump mackenzie_story1

        "Who are you?":
            show m happy at Mackenzeighlynnabelle_higher
            with dissolve
            m "{cps=25}I’m Mackenzeighlynnabelle, a mage living in the village! You can call me Mackenzie.{/cps}"
            m "{cps=25}I enjoy helping villagers with daily tasks using my magic.{/cps}"
            m "{cps=25}It’s a shame that the trade routes got blocked off.{/cps}"
            m "{cps=25}Anyways, how about we embark on our journey!{/cps}"
            show m neutral at Mackenzeighlynnabelle_higher
            with dissolve
            jump mackenzie_story1

label mackenzie_story1:
    "{cps=25}You and Mackenzie venture into the cave, immedietly hearing  eerie sounds echoing through the tunnels.{/cps}"
    "{cps=25}Suprisingly, you see a suspiciously placed stack of diamonds on the right, and on the left...{/cps}"
    "{cps=25}A less suspicious pile of rocks with subtle but eerie sounds coming from it.{/cps}"
    hide m

    menu:
        "Which pile do you investigate?"

        "The Diamonds":
            "{cps=25}With exuberant luck, you excitedly grab all the diamonds, shoving them into your bag.{/cps}"
            "{cps=25}CRASH!!!{/cps}"
            with vpunch
            "{cps=25}You look behind you to see the entrance blocked with collapsed rubble.{/cps}"
            "{cps=25}Not having any other choice, you traverse further into the cave, trying to find another way out.{/cps}"
            jump mackenzie_story2

        "The Rocks":
            m "{cps=25}Hey, I think I saw footsteps over here…{/cps}"
            m "{cps=25}Let me go look.{/cps}"
            "{cps=25}In a split second, Mackenzie disappears.{/cps}"
            "{cps=25}Startled, you start trying to find where she went.{/cps}"
            jump mackenzie_story3

label mackenzie_story2:
    "{cps=25}Trying to find another way out, you stumble upon a crossroad with the option of turning left or right{/cps}"

    menu:
        "Turn Left":
            jump mackenzie_story2_1
        "Turn Right":
            jump mackenzie_story2_1

label mackenzie_story2_1:
    "{cps=25}Walking down the tunnel, you start to feel the ground shaking.{/cps}"
    "{cps=25}Startled, you brace yourself for whatever is waiting for you at the end of the tunnel.{/cps}"
    "{cps=25}At the end of the tunnel, you see a dim glimmer of light.{/cps}"
    "{cps=25}Excited, you haul the diamonds quickly in order to escape.{/cps}"
    "{cps=25}Approaching the exit, you notice something drastically wrong…{/cps}"
    "{cps=25}CRASH!!!{/cps}"
    with vpunch
    hide m
    show monster at monster_higher
    "{cps=25}ARGAHRHAHAGHRHAGHGRHAHGRAHRGAHR{/cps}"
    "{cps=25}A grotesque monster burrows out from the wall. Surrounding you and Mackenzie.{/cps}"

    menu:
        "Fight":
            "{cps=25}Standing your ground, both you and Mackenzie prepare yourselves for a brutal fight.{/cps}"
            "{cps=25}Being a decoy, you take the initiative of striking first.{/cps}"
            "{cps=25}Using the wall, you leap into the air, charging up your sword ready to attack.{/cps}"
            "{cps=25}Striking the monster on the right shoulder, it slams you into the wall, holding you in head lock with his enormous hand.{/cps}"
            show monster at monster_higher, monster_hit_shake
            "{cps=25}Gasping for air, you frantically try to escape, proving useless.{/cps}"
            "{cps=25}As the monster winds up to sucker punch you right in the face, you brace, slamming your eyes shut.{/cps}"
            "{cps=25}ARGAHRHAHAGHRHAGHGRHAHGRAHRGAHR{/cps}"
            "{cps=25}Silence…{/cps}"
            "{cps=25}Confused on what happened, you open your eyes.{/cps}"
            "{cps=25}You see the monster… without a head.{/cps}"
            hide monster
            "{cps=25}Looking at Mackenzie, staff in hand, you realize she has decapitated the monster using her magic.{/cps}"
            jump mackenzie_ending

        "Make a break for the exit":
            "{cps=25}Grabbing Mackenzie, you sprint for the exit, trying to dodge, weave and escape through the little slivers of space.{/cps}"
            "{cps=25}Just as you approach the exit of the cave, all sense of hope is immediately crushed.{/cps}"
            "{cps=25}SLAM!{/cps}"
            "{cps=25}You open your eyes, face to face with the monster.{/cps}"
            "{cps=25}Horrified you let out a blood curdling scream as the monster opens its mouth.{/cps}"
            "{cps=25}Your vision goes black.{/cps}"
            return

label mackenzie_ending:
    scene black
    with fade
    "{cps=25}Having defeated the monster, you and Mackenzie sprint for the exit.{/cps}"
    "{cps=25}With the bag of diamonds hauled on your bag, you let out a giant sigh of relief seeing the blue sky and puffy clouds.{/cps}"
    "{cps=25}Returning to the village, capybaras crowd around you, exclaiming in cries of celebration.{/cps}"
    "{cps=25}You have managed to bring back enough diamonds to support the village for at least 5 years.{/cps}"
    "{cps=25}Relieved, you make your way out of the village to continue your journey but are held back by the villagers, offering hospitality and celebration to honour you{/cps}"
    return

label mackenzie_story3:
    "{cps=25}Trying to find out where Mackenzie went, you journey further into the cave.{/cps}"
    "{cps=25}You stumble upon a crossroad with the option of turning left of right{/cps}"

    menu:
        "Turn Left":
            jump mackenzie_story3_1
        "Turn Right":
            jump mackenzie_story3_1

label mackenzie_story3_1:
    "{cps=25}Walking down the tunnel, you hear a loud shriek.{/cps}"
    "{cps=25}With the ground starting to shake, you dash forward after hearing the screams of who you think is Mackenzie.{/cps}"
    "{cps=25}Bolting forward, you come across Mackenzie surrounded by a grotesque monster, walls collapsed.{/cps}"
    hide m
    show monster at monster_higher
    "{cps=25}ARGAHRHAHAGHRHAGHGRHAHGRAHRGAHR{/cps}"

    menu:
        "Turn around and run":
            "{cps=25}You panic, turn around and start running away.{/cps}"
            "{cps=25}CRASH!!{/cps}"
            show monster at monster_higher, monster_hit_shake
            "{cps=25}The roof of the cave collapses, trapping you with Mackenzie and the monster.{/cps}"
            "{cps=25}You turn around. The monster stares dead in your eyes and notices you.{/cps}"
            "{cps=25}You frantically try to dig up rocks to access an escape route.{/cps}"
            hide monster
            show m scared at Mackenzeighlynnabelle_higher
            "{cps=25}Looking behind you, Mackenzie’s body is limp on the ground. The screams stop.{/cps}"
            scene black
            with fade
            "{cps=25}Inch by inch, the monster creeps closer and closer, unphased by your shouts.{/cps}"
            "{cps=25}You try to fight back, but without magic your sword swings do almost nothing.{/cps}"
            "{cps=25}SMASH{/cps}"
            return

        "Help Mackenzie":
            "{cps=25}Drawing your sword, you prepare a surprise attack on the monster from behind.{/cps}"
            "{cps=25}You jump up, charging your sword and striking the back of its head.{/cps}"
            show monster at monster_higher, monster_hit_shake
            "{cps=25}Frustrated, the monster turns and corners you, ready to deliver a fatal strike.{/cps}"
            "{cps=25}WOOSH!{/cps}"
            "{cps=25}You brace yourself and shut your eyes.{/cps}"
            "{cps=25}Peeking out, you see the monster standing still for a second... then collapsing.{/cps}"
            "{cps=25}Standing behind it, you see Mackenzie with her staff still in hand.{/cps}"
            show m yay at Mackenzeighlynnabelle_higher
            "{cps=25}Behind the monster, you spot a giant vein of diamonds.{/cps}"
            "{cps=25}Excited, you quickly mine the diamonds and pack your bag.{/cps}"
            jump mackenzie_ending
    
#Mackenzie Story End


#Grafat Story Start:

label grafat_story:   
    show g neutral at Grafat_higher

    menu:
        "Alright! Are you ready to go?"

        "Yes!":
            jump graf_story

        "Who are you?":
            show g happy at Grafat_higher
            with dissolve
            g "{cps=25}I’m Graf Granat, the village's strongest warrior!{/cps}"
            g "{cps=25}I’ve been protecting the village from monsters of all sorts with my trusty axe.{/cps}"
            g "{cps=25}That is… until the mountain decided to block off all of our trade routes…{/cps}"
            g "{cps=25}Anyways let’s get going and find some diamonds eh!{/cps}"
            show g neutral at Grafat_higher
            with dissolve
            jump graf_story



label graf_story:
    stop skipping
    "{cps=25}You and Granat venture deeper into the cave, your footsteps echoing through the tunnels.{/cps}"
    "{cps=25}20 minutes pass{/cps}"
    pause 0.3
    g "{cps=25}We’ve been walking for hours... where is the giant monster we have to defeat? Ugh.{/cps}"

    menu:
        "We’ve been walking for houurrrssssss, where is the giant monster we have to defeat.. Ugh."

        "It's only been 20 minutes...":
            show g scared at Grafat_higher
            with dissolve
            g "{cps=25}Has it? It feels like being down here for days, maybe years even… how much longer must I endure such torture.{/cps}"
            jump graf_story1

        "Stay Silent":
            show g scared at Grafat_higher
            with dissolve
            g "{cps=25}...You’re really not helping my morale here, you know.{/cps}"
            jump graf_story1

label graf_story1:
    g "{cps=25}Where did you get that sword by the way? Looks sick.{/cps}"

    menu:
        "Bought it back in my village":
            show g yay at Grafat_higher
            g "{cps=25}Hmmm... that's pretty cool.{/cps}"
            g "{cps=25}Still, that blade has a strange aura to it. Keep it close.{/cps}"
            jump graf_story2

        "Pulled it out of a rock":
            g "{cps=25}So… you’re saying you’re the strongest hero to ever exist… No one’s been able to pull that in millions of years!{/cps}"

            menu:
                "Yea that's me...":
                    g "{cps=25}You’re not a very good liar, no one’s ever been able to pull that sword out..{/cps}"
                    jump graf_story2

                "Haha, I was joking, just some sword my grandfather handed down to me. Not sure why he had it.. He was a priest. A really good one though.":
                    g "{cps=25}Hmmm… my father always told me stories about a priest and his party of heroes. Don’t know how good of a priest he was though, just knew he loved his alcohol.{/cps}"
                    jump graf_story2

label graf_story2:
    "{cps=25}You journey for a bit longer before finding a subtle glow in the wall.{/cps}"
    show g yay at Grafat_higher
    with dissolve
    g "{cps=25}No way… Diamonds???{/cps}"
    "{cps=25}Eagerly, Granat swings his enormous axe at the rock to mine the diamonds.{/cps}"
    "{cps=25}CRASH!!{/cps}"
    with vpunch
    "{cps=25}Rocks start falling down as ash fills the air.{/cps}"
    g "{cps=25}cough cough{/cps}"
    g "{cps=25}Ugh all this ash I can’t see a thing!{/cps}"
    "{cps=25}As the ash settles down, faint footsteps start to emerge, gradually becoming louder and louder.{/cps}"
    "{cps=25}An enormous monster emerges from the ash, banging its head on the top of the mine due to it’s gigantic size.{/cps}"
    hide g
    show monster at monster_higher
    with dissolve
    "{cps=25}The monster towers over you, blocking the path ahead.{/cps}"
    "{cps=25}The monster lets out a deafening roar.{/cps}"
    show g scared at Grafat_higher
    g "{cps=25}BIG SCARY MONSTER!! RUNNNNNN{/cps}"
    hide g

    menu:
        "Stay and Fight":
            jump graf_fight

        "Grab the diamonds and run (Didn’t you want to fight a big monster?)":
            jump graf_run

label graf_fight:
    "{cps=25}Granat jumps up ready to strike. Axe gripped tightly in hand, Granat lunges towards the monster.{/cps}"
    "{cps=25}CLANK!!!!!{/cps}"
    show monster at monster_higher, monster_hit_shake
    "{cps=25}The monster roars and staggers back, then turns toward the diamonds.{/cps}"

    menu:
        "Defend the diamonds":
            "{cps=25}You throw yourself in front of the monster. Sword in hand, you block as it charges the gem pile.{/cps}"
            show monster at monster_higher, monster_hit_shake
            "{cps=25}From the shadows, Granat stumbles back to his feet and swings his trusty axe, incapacitating the monster.{/cps}"
            hide m
            jump grafgood_ending

label graf_run:
    show monster at monster_higher, monster_chase_shake
    "{cps=25}You and Granat quickly scoop up all the diamonds you can and bolt for the entrance of the cave.{/cps}"
    "{cps=25}The monster roars behind you, but the two of you escape the collapsing tunnel.{/cps}"
    g "{cps=25}YO! SLOW DOOOWWNNNNNN! WHY ARE YOU SO FAST OH MY DAYS{/cps}"

    menu:
        "Slow down to help Granat":
            "{cps=25}You slow down to help Granat as the monster strays slightly behind you.{/cps}"

            menu:
                "Stay and fight the monster":
                    jump graf_fight

                "Keep running":
                    jump graf_story3

        "Make Granat drop the diamonds":
            jump grafbad_ending


label graf_story3:  
    show monster at monster_higher, monster_chase_shake
    "{cps=25}You and Granat keep running for your lives.{/cps}"
    "{cps=25} As the monster creeps closer and closer, a sense of dread sets in as you haul your heavy bag filled with diamonds.{/cps}"
    "{cps=25}You start panting as your vision goes blurry.{/cps}"
    "{cps=25}AARHRAHRGHEHGAGHHHG{/cps}"
    "{cps=25}The monster smashes the ground, exerting the force of a mild earthquake.{/cps}"
    show monster at monster_higher, monster_hit_shake
    "{cps=25}The walls crack, blossoming towards the top of the cave.{/cps}"
    "{cps=25}The hardstone shatters, crumpling and crushing both you and Granat.{/cps}"

    scene black
    with fade
    g "{cps=25}Cough cough{/cps}"
    show g dead at Grafat_higher
    g "{cps=25}Adventurer… help my leg is stuck.. I can’t get out.{/cps}"

    menu:
        "Help Granat":
            "{cps=25}Hearing Granat’s cries, you drag yourself through the rubble and pull at his arm with all your strength.{/cps}"
            "{cps=25}Boulders have buried him up to his waist, but you refuse to let go.{/cps}"
            "{cps=25}Holding Granat by the cloth of his jacket, you keep trying to pull him out… {/cps}"
            "{cps=25}SMASH{/cps}"
            return

        "Leave Granat":
            "{cps=25}You frantically run out of the cave as Granat’s desperate cries echo behind you.{/cps}"
            "{cps=25}You hear one last blood curdling scream from the monster.{/cps}"
            "{cps=25}SMASH.{/cps}"
            "{cps=25}Silence…{/cps}"
            "{cps=25}Your ears fill with static…{/cps}"
            "{cps=25}You run…{/cps}"
            "{cps=25}Away from the cave, away from the village…{/cps}"
            return



label grafbad_ending:
    "{cps=25}Panicking, you bolt for the door with Granat draped over your shoulder.{/cps}"
    "{cps=25}Returning to the village without any diamonds, you feel a sense of sadness overcome you.{/cps}"
    "{cps=25}Reflecting upon the decisions you made, if they were the right ones or not. {/cps}"
    "{cps=25}At least you’re alive.{/cps}"
    return
    
label grafgood_ending:
    scene black
    with fade
    "{cps=25}Emerging from the mine with a heavy diamond bag, you let out a sigh of relief.{/cps}"
    "{cps=25}Back at the village, capybaras rush over to see your findings.{/cps}"
    "{cps=25}They praise you for saving their home and restoring their supply for years to come.{/cps}"

    return

#Grafat Story End

#Vlad Story Start:

label vlad_story:
    $ has_pickaxe = False
    $ has_cheese = False
    $ has_gravel = False
    $ has_dynamite = False
    $ tools_chosen = 0

    scene bg forest with fade
    show miner at truecenter with dissolve

    "{cps=25}The valley smells of pine resin and cold stone.{/cps}"
    "{cps=25}A very old capybara leans against the mine entrance, squinting at you from beneath a helmet held together by faith and one piece of wire.{/cps}"

    v "{cps=25}Comrade. Why brings you here?{/cps}"

    menu:
        "Not sure.":
            jump vlad_response_not_sure
        "I need help finding diamonds.":
            jump vlad_response_diamonds


label vlad_response_not_sure:
    v "{cps=25}Not sure? NOT SURE? I wait sixty year for visitor and they arrive — not sure. Bah.{/cps}"
    v "{cps=25}You strange. But I see small potential. Like very small rock. Come. I explain.{/cps}"
    jump vlad_tool_selection


label vlad_response_diamonds:
    v "{cps=25}Diamond! In mine! Right place you come.{/cps}"
    v "{cps=25}I am Vlad. I know every tunnel, every rock, every place I hide dynamite. But first — tool.{/cps}"
    v "{cps=25}Go. Choose. Before I change mind and go back to nap.{/cps}"
    jump vlad_tool_selection


label vlad_tool_selection:
    scene bg town with fade
    show miner at truecenter with dissolve

    "{cps=25}Vlad leads you to a battered table covered in mining equipment. Some of it looks useful. Some of it looks haunted.{/cps}"
    v "{cps=25}You pick three. No more. Choose with brain, not with paw.{/cps}"
    jump vlad_pick_tool_loop


label vlad_pick_tool_loop:
    if tools_chosen >= 3:
        jump vlad_tools_done

    "{cps=25}([tools_chosen] / 3 tools chosen){/cps}"

    menu:
        "⛏️  Whispering Pickaxe — mines fast, has opinions" if not has_pickaxe:
            $ has_pickaxe = True
            $ tools_chosen += 1
            "{cps=25}The pickaxe hums the moment you pick it up. Judgmentally.{/cps}"
            v "{cps=25}Good pickaxe. Talks too much. You get used to it. Mostly.{/cps}"
            jump vlad_pick_tool_loop

        "🧀  Emergency Cheese Wheel — heals a little, smells a lot" if not has_cheese:
            $ has_cheese = True
            $ tools_chosen += 1
            "{cps=25}The smell reaches you before your hand does. You take it anyway.{/cps}"
            v "{cps=25}Cheese. Useful in mine. You will see why. Maybe.{/cps}"
            jump vlad_pick_tool_loop

        "🪨  Pocket Gravel — throw to distract things" if not has_gravel:
            $ has_gravel = True
            $ tools_chosen += 1
            "{cps=25}You fill your pockets with small rocks. Vlad nods approvingly.{/cps}"
            jump vlad_pick_tool_loop

        "🧨  Suspicious Dynamite — big results, definite opinions from Vlad" if not has_dynamite:
            $ has_dynamite = True
            $ tools_chosen += 1
            "{cps=25}You pocket it with care.{/cps}"
            v "{cps=25}You use correctly, yes? Not like — you know what, I tell you later.{/cps}"
            jump vlad_pick_tool_loop

        "Head to the mine.":
            jump vlad_tools_done


label vlad_tools_done:
    if tools_chosen == 0:
        v "{cps=25}You come to mine with nothing? No tool? Just paw?{/cps}"
        pause 0.4
        v "{cps=25}...I respect. Very stupid. But also very brave.{/cps}"
    else:
        v "{cps=25}Good. You are ready as you will ever be. That is not very ready. But is enough. Come.{/cps}"

    jump vlad_mine_entrance


label vlad_mine_entrance:
    scene bg cave with fade
    show miner at truecenter with dissolve

    "{cps=25}The mine swallows daylight the moment you step inside.{/cps}"
    v "{cps=25}Welcome to mine. I give tour later. After diamond. Come.{/cps}"

    menu:
        "Follow Vlad deeper in.":
            jump vlad_tunnel_fork
        "What are we actually looking for?":
            jump vlad_what_looking_for
        "Examine the entrance walls.":
            jump vlad_examine_entrance


label vlad_what_looking_for:
    v "{cps=25}Diamond! Big shiny stone. You not know diamond?{/cps}"
    menu:
        "Fair enough. Lead on.":
            jump vlad_tunnel_fork
        "Have you found one before?":
            jump vlad_found_before


label vlad_found_before:
    v "{cps=25}Once. Long ago. Beautiful stone. Then I drop in puddle.{/cps}"
    pause 0.4
    v "{cps=25}Very sad day. We do not speak of puddle.{/cps}"
    menu:
        "I'm sorry about the puddle.":
            jump vlad_sorry_puddle
        "Let's keep moving.":
            jump vlad_tunnel_fork


label vlad_sorry_puddle:
    v "{cps=25}...You good comrade. Strange, maybe little stupid. But good.{/cps}"
    jump vlad_tunnel_fork


label vlad_examine_entrance:
    "{cps=25}Carvings cover the walls, scratched in at different heights over many years.{/cps}"
    "{cps=25}Rule 1: Never go to cold. Rule 2: Do not touch Vlad dynamite.{/cps}"
    v "{cps=25}Most important: no go cold. Second: no eat glowing mushroom.{/cps}"
    menu:
        "What's in that barrel?":
            jump vlad_the_barrel
        "Decide not to ask and move on.":
            jump vlad_tunnel_fork


label vlad_the_barrel:
    v "{cps=25}NOTHING. Is barrel of cheese. Just cheese.{/cps}"
    "{cps=25}You: Did it just tick?{/cps}"
    v "{cps=25}Old mine make many noise! Come now.{/cps}"
    jump vlad_tunnel_fork


label vlad_tunnel_fork:
    "{cps=25}The tunnel splits. Cold air breathes from both passages.{/cps}"
    v "{cps=25}Left go toward diamond vein — according to map. Right go toward... hard to say.{/cps}"

    menu:
        "Go left — follow the map.":
            jump vlad_left_tunnel
        "Go right — into the unknown.":
            jump vlad_right_tunnel
        "Vlad, which way would you go?":
            jump vlad_vlad_opinion


label vlad_vlad_opinion:
    v "{cps=25}I do not know. Both look bad.{/cps}"
    menu:
        "Go left.":
            jump vlad_left_tunnel
        "Go right.":
            jump vlad_right_tunnel


label vlad_right_tunnel:
    "{cps=25}The tunnel grows colder. Ahead, a massive cave bear sleeps on a pile of gravel.{/cps}"
    v "{cps=25}...I forget he was still here.{/cps}"

    menu:
        "Sneak past.":
            jump vlad_sneak_bear
        "Throw Pocket Gravel to distract it." if has_gravel:
            jump vlad_gravel_distract
        "Go back to the fork.":
            jump vlad_tunnel_fork


label vlad_sneak_bear:
    "{cps=25}You move carefully. The bear snores and rolls over. You slip by.{/cps}"
    jump vlad_left_tunnel


label vlad_gravel_distract:
    "{cps=25}You toss a fistful of gravel down the side of the hollow. The bear turns, and you slip past.{/cps}"
    v "{cps=25}Good thinking. Gravel useful.{/cps}"
    jump vlad_left_tunnel


label vlad_left_tunnel:
    "{cps=25}The left tunnel is warmer and older. Something skitters in the dark ahead.{/cps}"
    menu:
        "Vlad, what was that?":
            jump vlad_what_sound
        "Press forward.":
            jump vlad_gruyere_rat_encounter
        "Hold up the Whispering Pickaxe to sense ahead." if has_pickaxe:
            jump vlad_pickaxe_sense


label vlad_pickaxe_sense:
    "{cps=25}The pickaxe trembles once: 'Something old. Something watching. Something that wants cheese.'{/cps}"
    v "{cps=25}Gruyere Rat. If you have cheese — hide it now.{/cps}"
    jump vlad_gruyere_rat_encounter


label vlad_what_sound:
    v "{cps=25}Is nothing. Small cave creature. Or maybe very large.{/cps}"
    menu:
        "Trust Vlad and continue.":
            jump vlad_gruyere_rat_encounter
        "Investigate.":
            jump vlad_find_smolkov


label vlad_find_smolkov:
    "{cps=25}Behind a rock: a small capybara pup with a tiny pickaxe and a tag that says 'If found, return to Vlad.'{/cps}"
    "{cps=25}You: Vlad... is this yours?{/cps}"
    v "{cps=25}That is mine apprentice. Smolkov. He wander off. Again.{/cps}"
    jump vlad_gruyere_rat_encounter


label vlad_gruyere_rat_encounter:
    "{cps=25}Two amber eyes catch the light ahead. Something very large shuffles into view.{/cps}"
    v "{cps=25}Gruyere Rat. It was not legend.{/cps}"

    menu:
        "Slowly hide the cheese in your pack." if has_cheese:
            jump vlad_hide_cheese
        "Hold the cheese aloft." if has_cheese:
            jump vlad_wield_cheese
        "You have no cheese. Stand very still." if not has_cheese:
            jump vlad_no_cheese


label vlad_hide_cheese:
    "{cps=25}You hide the cheese. The rat sniffs the air, finds nothing, and lumbers away.{/cps}"
    jump vlad_diamond_vein


label vlad_wield_cheese:
    "{cps=25}You raise the cheese. The rat bows, then backs into the dark and disappears.{/cps}"
    jump vlad_diamond_vein


label vlad_no_cheese:
    "{cps=25}The rat sniffs your boots, finds no cheese, and leaves disappointed.{/cps}"
    jump vlad_diamond_vein


label vlad_diamond_vein:
    "{cps=25}The tunnel opens into a low chamber full of brilliant white stones embedded in black rock.{/cps}"
    v "{cps=25}There. There.{/cps}"
    "{cps=25}The ceiling is unstable. Cracks run above in long spidery lines.{/cps}"

    menu:
        "Mine carefully by hand.":
            jump vlad_mine_by_hand
        "Use the Whispering Pickaxe." if has_pickaxe:
            jump vlad_use_pickaxe
        "Use the Suspicious Dynamite." if has_dynamite:
            jump vlad_use_player_dynamite
        "Ask Vlad how to proceed.":
            jump vlad_ask_vlad


label vlad_ask_vlad:
    v "{cps=25}Careful approach best. I show you.{/cps}"
    "{cps=25}He reaches into his coat and pulls out something red. With a fuse.{/cps}"
    menu:
        "VLAD. PUT THAT DOWN.":
            jump vlad_vlad_stop
        "Where did you even get that?":
            jump vlad_where_dynamite


label vlad_where_dynamite:
    v "{cps=25}I store dynamite throughout mine! In walls, in floor, in rock you were sitting on —{/cps}"
    "{cps=25}You: HOW MUCH DYNAMITE IS IN HERE?!{/cps}"
    v "{cps=25}Everything largely accounted for. Mostly.{/cps}"
    jump vlad_vlad_stop


label vlad_vlad_stop:
    v "{cps=25}Vlad know what he do. I am professional —{/cps}"
    "{cps=25}You: VLAD.{/cps}"
    v "{cps=25}I just light fuse a little.{/cps}"
    jump vlad_the_explosion


label vlad_mine_by_hand:
    "{cps=25}You chip carefully and free a few diamonds. Dust rains from above.{/cps}"
    "{cps=25}Vlad looks at the ceiling. Then reaches into his coat anyway.{/cps}"
    jump vlad_the_explosion


label vlad_use_pickaxe:
    "{cps=25}The pickaxe sings against the rock. Diamonds tumble free. Vlad reaches into his coat anyway.{/cps}"
    jump vlad_the_explosion


label vlad_use_player_dynamite:
    "{cps=25}You set the charge. BOOM. Diamonds scatter across the floor.{/cps}"
    v "{cps=25}I use also. For thoroughness.{/cps}"
    jump vlad_the_explosion


label vlad_the_explosion:
    "{cps=25}Vlad looks at the diamonds. At the dynamite. At you.{/cps}"
    "{cps=25}You: Vlad. Don't.{/cps}"

    menu:
        "VLAD. I AM BEGGING YOU.":
            jump vlad_beg_vlad
        "Try to grab the dynamite.":
            jump vlad_grab_dynamite
        "Accept your fate.":
            jump vlad_fate_accepted


label vlad_beg_vlad:
    v "{cps=25}Is okay. Vlad know what he do.{/cps}"
    "{cps=25}You: YOU HAVE NEVER SUCCESSFULLY MINED A DIAMOND IN SIXTY YEARS.{/cps}"
    v "{cps=25}...This is fair point.{/cps}"
    "{cps=25}He lights the fuse anyway.{/cps}"
    jump vlad_run_sequence


label vlad_grab_dynamite:
    v "{cps=25}Ha! Old Vlad still quick!{/cps}"
    "{cps=25}He lights the fuse.{/cps}"
    jump vlad_run_sequence


label vlad_fate_accepted:
    "{cps=25}You close your eyes. You think of the barrel. The one that ticked.{/cps}"
    "{cps=25}Vlad lights the fuse.{/cps}"
    jump vlad_run_sequence


label vlad_run_sequence:
    v "{cps=25}Rule 1 — never go to cold. But sometimes... sometimes you must make warm.{/cps}"
    pause 0.4
    "{cps=25}THE MINE SHAKES.{/cps}"
    with hpunch
    jump vlad_post_explosion


label vlad_post_explosion:
    scene bg forest with fade
    show miner at truecenter with dissolve

    "{cps=25}You burst out of the entrance coughing, pockets inexplicably full of diamonds.{/cps}"
    pause 0.6
    "{cps=25}You: ...Vlad?{/cps}"
    "{cps=25}A silhouette walks out of the dust cloud, covered in soot and holding an enormous diamond.{/cps}"

    v "{cps=25}I okay. I always okay. I Vlad.{/cps}"
    v "{cps=25}For you, comrade. You strange. Possibly foolish. But brave enough for mine.{/cps}"

    menu:
        "You absolute madman.":
            jump vlad_ending_standard
        "I'm never going in a mine again.":
            jump vlad_ending_never_again
        "Hug him.":
            jump vlad_ending_hug


label vlad_ending_standard:
    v "{cps=25}(long, raspy cackle){/cps}"
    jump vlad_epilogue


label vlad_ending_never_again:
    v "{cps=25}Smart. But you say this now. In one year, maybe two — you come back.{/cps}"
    jump vlad_epilogue


label vlad_ending_hug:
    "{cps=25}You hug him. He pats your back exactly twice.{/cps}"
    v "{cps=25}Okay. Enough. Vlad is professional miner.{/cps}"
    jump vlad_epilogue


label vlad_epilogue:
    "{cps=25}You have diamonds. You have stories. You have soot in places soot should not be.{/cps}"
    v "{cps=25}You come back sometime, yes? Mine get lonely.{/cps}"
    "{cps=25}From somewhere deep in the dark, very faint, you hear an old work song.{/cps}"
    "{cps=25}THE END{/cps}"
    return

#Vlad Story End
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # # This shows a character sprite. A placeholder is used, but you can
    # # replace it by adding a file named "eileen happy.png" to the images
    # # directory.

    # show eileen happy

    # # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # # This ends the game.

    return
