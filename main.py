from game import Game
from transform_card import transform_card
import cards 


s,f,c = transform_card(cards.str_card_3)
a = Game(s,f,c)
a.run()