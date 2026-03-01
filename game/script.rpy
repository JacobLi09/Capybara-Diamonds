init python:
    gui.textbox_yalign       = 1.0
    gui.textbox_height       = 185
    gui.choice_button_width  = 640
    gui.choice_button_xalign = 0.5


define vlad     = Character("Vlad",     color="#c8a96e", what_color="#f5e8c8", window_yalign=1.0)
define you      = Character("You",      color="#7ec8e8", what_color="#d8f0ff", window_yalign=1.0)
define narrator = Character(None,       what_color="#dddddd", what_italic=True, window_yalign=1.0)


image bg cave   = "Cave.png"
image bg forest = "Grass.png"
image bg town   = "Town.png"
image miner     = "miner.png"


default has_pickaxe = False
default has_cheese  = False
default has_gravel  = False
default has_dynamite = False
default tools_chosen = 0


label start:

    scene bg forest with fade
    show miner at truecenter with dissolve

    narrator "The valley smells of pine resin and cold stone."
    narrator "A very old capybara leans against the mine entrance, squinting at you from beneath a helmet held together by faith and one piece of wire."

    vlad "Comrade. Why brings you here?"

    menu:
        "Not sure.":
            jump response_not_sure
        "I need help finding diamonds.":
            jump response_diamonds


label response_not_sure:

    vlad "Not sure? NOT SURE? I wait sixty year for visitor and they arrive — not sure. Bah."
    vlad "You strange. But I see small potential. Like very small rock. Come. I explain."
    jump tool_selection


label response_diamonds:

    vlad "Diamond! In mine! Right place you come."
    vlad "I am Vlad. I know every tunnel, every rock, every place I hide dynamite. But first — tool."
    vlad "Go. Choose. Before I change mind and go back to nap."
    jump tool_selection


label tool_selection:

    scene bg town with fade
    show miner at truecenter with dissolve

    narrator "Vlad leads you to a battered table covered in mining equipment. Some of it looks useful. Some of it looks haunted."
    vlad "You pick three. No more. Choose with brain, not with paw."

    jump pick_tool_loop


label pick_tool_loop:

    if tools_chosen >= 3:
        jump tools_done

    narrator "( [tools_chosen] / 3 tools chosen )"

    menu:
        "⛏️  Whispering Pickaxe — mines fast, has opinions" if not has_pickaxe:
            $ has_pickaxe    = True
            $ tools_chosen  += 1
            narrator "The pickaxe hums the moment you pick it up. Judgmentally."
            vlad "Good pickaxe. Talks too much. You get used to it. Mostly."
            jump pick_tool_loop

        "🧀  Emergency Cheese Wheel — heals a little, smells a lot" if not has_cheese:
            $ has_cheese     = True
            $ tools_chosen  += 1
            narrator "The smell reaches you before your hand does. You take it anyway."
            vlad "Cheese. Useful in mine. You will see why. Maybe."
            jump pick_tool_loop

        "🪨  Pocket Gravel — throw to distract things" if not has_gravel:
            $ has_gravel     = True
            $ tools_chosen  += 1
            narrator "You fill your pockets with small rocks. Vlad nods approvingly."
            jump pick_tool_loop

        "🧨  Suspicious Dynamite — big results, definite opinions from Vlad" if not has_dynamite:
            $ has_dynamite   = True
            $ tools_chosen  += 1
            narrator "You pocket it with care."
            vlad "You use correctly, yes? Not like — you know what, I tell you later."
            jump pick_tool_loop

        "Head to the mine.":
            jump tools_done


label tools_done:

    if tools_chosen == 0:
        vlad "You come to mine with nothing? No tool? Just paw?"
        pause 0.4
        vlad "...I respect. Very stupid. But also very brave. Like capybara proverb: the empty paw fears no loss."
        vlad "I make that up just now. Still true."
    else:
        vlad "Good. You are ready as you will ever be. That is not very ready. But is enough. Come."

    jump mine_entrance


label mine_entrance:

    scene bg cave with fade
    show miner at truecenter with dissolve

    narrator "The mine swallows daylight the moment you step inside. The air smells of old stone and something cheesy."
    vlad "Welcome to mine. I give tour later. After diamond. Come."

    menu:
        "Follow Vlad deeper in.":
            jump tunnel_fork
        "\"What are we actually looking for?\"":
            jump what_looking_for
        "Examine the entrance walls.":
            jump examine_entrance


label what_looking_for:

    vlad "Diamond! Big shiny stone. You not know diamond? Where you grow up, in cabbage?"
    menu:
        "\"Fair enough. Lead on.\"":
            jump tunnel_fork
        "\"Have you found one before?\"":
            jump found_before


label found_before:

    vlad "Once. Long ago. Beautiful stone. Then I drop in puddle."
    pause 0.4
    vlad "Very sad day. We do not speak of puddle."
    narrator "A single tear rolls down his ancient face."
    menu:
        "\"I'm sorry about the puddle.\"":
            jump sorry_puddle
        "\"Let's keep moving.\"":
            jump tunnel_fork


label sorry_puddle:

    vlad "...You good comrade. Strange, maybe little stupid. But good."
    narrator "He blows his nose into his mining glove and marches on."
    jump tunnel_fork


label examine_entrance:

    narrator "Carvings cover the walls, scratched in at different heights over what must have been many years."
    narrator "Rule 1: Never go to cold. Rule 2: Do not touch Vlad dynamite."
    narrator "The rules continue. There are a lot of rules."
    vlad "I write all seventy-three myself. Most important: no go cold. Second: no eat glowing mushroom."
    vlad "Third important — actually. Maybe you not need know third."
    narrator "He glances at a barrel in the corner. The barrel ticks faintly."
    menu:
        "\"What's in that barrel?\"":
            jump the_barrel
        "Decide not to ask and move on.":
            jump tunnel_fork


label the_barrel:

    vlad "NOTHING. Is barrel of cheese. Just cheese. Vlad allergic to question about barrel."
    you "Did it just tick?"
    vlad "Old mine make many noise! Is settling! Also your imagination very active. Come now."
    narrator "He ushers you down the tunnel at considerable speed."
    jump tunnel_fork


label tunnel_fork:

    narrator "The tunnel splits. Cold air breathes from both passages."
    vlad "Left go toward diamond vein — according to map. Right go toward... map is wrong edition. Hard to say."
    vlad "Both look cold. Rule 1 say never go to cold. And yet."

    menu:
        "Go left — follow the map.":
            jump left_tunnel
        "Go right — into the unknown.":
            jump right_tunnel
        "\"Vlad, which way would you go?\"":
            jump vlad_opinion


label vlad_opinion:

    vlad "I am old miner. Sixty year in this mine. I know every stone, every tunnel, every crack in ceiling."
    pause 0.4
    vlad "...I do not know. Both look bad."
    menu:
        "Go left.":
            jump left_tunnel
        "Go right.":
            jump right_tunnel


label right_tunnel:

    narrator "The tunnel grows colder. Your breath fogs. The walls glitter with frost."
    narrator "Ahead, a massive cave bear sleeps on a pile of gravel. A sign above it reads: DO NOT WAKE. — V.K."
    vlad "...I forget he was still here."

    menu:
        "Sneak past.":
            jump sneak_bear
        "Throw Pocket Gravel to distract it." if has_gravel:
            jump gravel_distract
        "Go back to the fork.":
            jump tunnel_fork


label sneak_bear:

    narrator "You move carefully, placing each step with total silence."
    narrator "The bear snorts. You freeze. It rolls over and resumes snoring."
    narrator "You exhale. The far end of the tunnel opens into the left passage."
    jump left_tunnel


label gravel_distract:

    narrator "You toss a fistful of gravel down the side of the hollow. The bear's head swings toward the sound."
    narrator "You and Vlad slip past cleanly."
    vlad "Good thinking. Gravel useful. I say this always."
    jump left_tunnel


label left_tunnel:

    narrator "The left tunnel is warmer and older. Vlad hums a slow, minor-key melody under his breath."
    narrator "Something skitters in the dark ahead."

    menu:
        "\"Vlad, what was that?\"":
            jump what_sound
        "Press forward.":
            jump gruyere_rat_encounter
        "Hold up the Whispering Pickaxe to sense ahead." if has_pickaxe:
            jump pickaxe_sense


label pickaxe_sense:

    narrator "The pickaxe trembles once. Then, close to your ear:"
    narrator "\"Something old. Something watching. Something that wants cheese very badly.\""
    narrator "A pause. \"Also your grip is still wrong.\""
    vlad "Gruyere Rat. I thought it was legend. If you have cheese — hide it now."
    jump gruyere_rat_encounter


label what_sound:

    vlad "Is nothing. Small cave creature. Or medium. Or possibly large. Dark make hard to tell size."
    menu:
        "Trust Vlad and continue.":
            jump gruyere_rat_encounter
        "Investigate.":
            jump find_smolkov


label find_smolkov:

    narrator "Behind a rock — a small capybara pup, clutching a tiny pickaxe."
    narrator "A tag around its neck reads: If found, return to Vlad. — Vlad."
    you "Vlad. Is this yours?"
    vlad "That is mine apprentice. Smolkov. He wander off. Again."
    vlad "Smolkov! What I say about wandering?!"
    narrator "The pup squeaks. Vlad nods gravely."
    vlad "Yes. Exactly. Stay close."
    narrator "Smolkov falls into step beside you, tiny pickaxe raised with complete seriousness."
    jump gruyere_rat_encounter


label gruyere_rat_encounter:

    narrator "Two amber eyes catch the light ahead. Something very large shuffles into view."
    vlad "Gruyere Rat. It was not legend."
    narrator "The rat ignores you entirely. It is interested only in what you are carrying."

    menu:
        "Slowly hide the cheese in your pack." if has_cheese:
            jump hide_cheese
        "Hold the cheese aloft." if has_cheese:
            jump wield_cheese
        "You have no cheese. Stand very still." if not has_cheese:
            jump no_cheese


label hide_cheese:

    narrator "You ease the cheese to the bottom of your pack. The rat sniffs the air, finds nothing, and lumbers away disappointed."
    vlad "Good. You live. We move now."
    jump diamond_vein


label wield_cheese:

    narrator "You raise the cheese above your head. The rat and you stare at each other."
    narrator "Vlad is already on a high ledge of rock."
    narrator "The rat bows. Then backs into the dark and is gone."
    pause 0.5
    vlad "...We never speak of this. But we remember."
    jump diamond_vein


label no_cheese:

    narrator "The rat sniffs your feet. Finds nothing. Leaves with the expression of a creature deeply let down by the world."
    vlad "Lucky. Rat usually less forgiving."
    jump diamond_vein


label diamond_vein:

    narrator "The tunnel opens into a low chamber. Embedded in the black rock — clusters of brilliant white stones catch your light."
    vlad "There. There."
    pause 0.4
    vlad "Sixty year, comrade. Sixty."
    narrator "The ceiling is unstable. Cracks run across the rock above in long spidery lines."

    menu:
        "Mine carefully by hand.":
            jump mine_by_hand
        "Use the Whispering Pickaxe." if has_pickaxe:
            jump use_pickaxe
        "Use the Suspicious Dynamite." if has_dynamite:
            jump use_player_dynamite
        "Ask Vlad how to proceed.":
            jump ask_vlad


label ask_vlad:

    vlad "Careful approach best. I show you."
    narrator "He studies the ceiling, the vein, the walls. Then he reaches into his coat."
    narrator "Something red. With a fuse."
    menu:
        "\"VLAD. PUT THAT DOWN.\"":
            jump vlad_stop
        "\"Where did you even get that?\"":
            jump where_dynamite


label where_dynamite:

    vlad "I store dynamite throughout mine! Sixty year! In walls, in floor, in rock you were sitting on —"
    narrator "You stand up very quickly."
    you "HOW MUCH DYNAMITE IS IN HERE?!"
    vlad "Everything largely accounted for. Mostly."
    jump vlad_stop


label vlad_stop:

    vlad "Vlad know what he do. I am professional —"
    you "VLAD."
    vlad "I just light fuse a little."
    jump the_explosion


label mine_by_hand:

    narrator "You chip carefully at the rock. Two diamonds come free. Then a third."
    narrator "You reach for a fourth. The ceiling drops a sheet of dust on your head."
    narrator "Vlad looks at the ceiling. Looks at his coat. Reaches into his coat."
    jump the_explosion


label use_pickaxe:

    narrator "The pickaxe sings against the rock. It murmurs: \"Third stratum. Seventeen degrees. Also grip still wrong.\""
    narrator "Diamonds tumble free. Then Vlad reaches into his coat anyway."
    jump the_explosion


label use_player_dynamite:

    narrator "You set the charge. BOOM. Diamonds scatter across the floor."
    narrator "Vlad looks at his own dynamite."
    vlad "I use also. For thoroughness."
    jump the_explosion


label the_explosion:

    narrator "Vlad looks at the diamonds. At the dynamite. At you."
    narrator "Smolkov begins backing toward the tunnel."
    you "Vlad. Don't."

    menu:
        "\"VLAD. I AM BEGGING YOU.\"":
            jump beg_vlad
        "Try to grab the dynamite.":
            jump grab_dynamite
        "Accept your fate.":
            jump fate_accepted


label beg_vlad:

    vlad "Is okay. Vlad know what he do."
    you "YOU HAVE NEVER SUCCESSFULLY MINED A DIAMOND IN SIXTY YEARS."
    vlad "...This is fair point."
    narrator "He lights the fuse anyway."
    jump run_sequence


label grab_dynamite:

    vlad "Ha! Old Vlad still quick! In mine, I am young man!"
    narrator "He lights the fuse."
    jump run_sequence


label fate_accepted:

    narrator "You close your eyes. You think of the barrel. The one that ticked."
    narrator "Vlad lights the fuse."
    jump run_sequence


label run_sequence:

    vlad "Rule 1 — never go to cold. But sometimes... sometimes you must make warm."
    narrator "He looks at the diamonds. At you. At Smolkov, who is already sprinting."
    pause 0.4
    narrator "THE MINE SHAKES."
    jump post_explosion


label post_explosion:

    scene bg forest with fade
    show miner at truecenter with dissolve

    narrator "You burst out of the entrance coughing, Smolkov under one arm, pockets inexplicably full of diamonds."
    narrator "The mine settles into silence."
    pause 0.6
    you "...Vlad?"

    narrator "A silhouette walks out of the dust cloud. Upright. Completely covered in soot. One ear slightly on fire."
    narrator "He is grinning. He is holding an enormous diamond."

    vlad "I okay. I always okay. I Vlad."
    narrator "He hands you the diamond."
    vlad "For you, comrade. You strange. Possibly foolish. But brave enough for mine."

    menu:
        "\"You absolute madman.\"":
            jump ending_standard
        "\"I'm never going in a mine again.\"":
            jump ending_never_again
        "Hug him.":
            jump ending_hug


label ending_standard:

    vlad "(long, raspy cackle)"
    narrator "Smolkov has already found a pebble and is examining it with total seriousness."
    narrator "The mine smolders gently behind you."
    narrator "You have diamonds. You have stories. You have soot in places soot should not be."
    jump epilogue


label ending_never_again:

    vlad "Smart. But you say this now. In one year, maybe two — you come back. They always come back."
    narrator "He pats your shoulder, leaving a perfect soot handprint."
    jump epilogue


label ending_hug:

    narrator "You hug him. He goes rigid. Pats your back exactly twice."
    vlad "Okay. Enough. Vlad is professional miner. This is not —"
    narrator "He doesn't let go for a while."
    narrator "Smolkov squeaks approvingly."
    jump epilogue


label epilogue:

    narrator "You have diamonds. You have stories. You have soot in places soot should not be."
    pause 0.4
    vlad "You come back sometime, yes? Mine need visitor. Smolkov get lonely. I mean — Vlad get lonely. No. Neither."
    vlad "Mine get lonely. This is thing I meant."
    narrator "He walks back into the smoking entrance without looking back."
    narrator "From somewhere deep in the dark, very faint, you hear a Soviet capybara work song."
    narrator "The barrel near the entrance ticks once."
    narrator "You decide not to think about it."
    pause 0.5
    narrator "THE END"

    return