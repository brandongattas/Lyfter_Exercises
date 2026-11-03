# Cree las siguientes clases:
# Head
# Torso
# Arm
# Hand
# Leg
# Feet
# Ahora cree una clase de Human y conecte todas las clases de 
# manera lógica por medio de atributos.


class Head():
    def __init__(self):
        pass

class Torso():
    def __init__(self, head, right_arm, left_arm, right_leg, left_leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg        

class Arm():
    def __init__(self, hand):
        self.hand = hand

class Hand():
    def __init__(self):
        pass

    def perform_wave(self):
        return "Waving...."

class Leg():
    def __init__(self, feet):
        self.feet = feet

class Feet():
    def __init__(self):
        pass

    def perform_kick(self):
        return "Kicking...."

class Human():
    def __init__(self, torso):
        self.torso = torso

    def kick_with_right_foot(self):
        right_foot_instance = self.torso.right_leg.feet
        print(f"Right foot, {right_foot_instance.perform_kick()}")

    def wave_with_right_hand(self):
        right_hand_instance = self.torso.right_arm.hand
        print(f"Right hand, {right_hand_instance.perform_wave()}")

right_hand = Hand()
right_arm = Arm(right_hand)
right_foot = Feet()
right_leg = Leg(right_foot)

left_hand = Hand()
left_arm = Arm(left_hand)
left_foot = Feet()
left_leg = Leg(left_foot)

head = Head()

torso = Torso(head, right_arm, left_arm, right_leg, left_leg)

brandon = Human(torso)
brandon.kick_with_right_foot()
brandon.wave_with_right_hand()