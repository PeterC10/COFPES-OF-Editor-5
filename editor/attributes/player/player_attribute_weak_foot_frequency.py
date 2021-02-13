from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeWeakFootFrequency(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Weak Foot Frequency"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.StandardAbilities

    def get_raw_value(self):
        return self.parent.get_value()

    def get_value(self):
        return self.parent.get_value()

    def get_label(self):
        """
        Get full label from parent
        and return second value (weak foot frequency is set second)
        """
        full_label = self.parent.get_label()
        return full_label[1]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        injury_tolerance_label = self.parent.injury_tolerance.get_label()
        centre_label = self.parent.centre.get_label()
        penalties_label = self.parent.penalties.get_label()
        one_touch_pass_label = self.parent.one_touch_pass.get_label()
        
        full_label = (
            injury_tolerance_label,
            label,
            centre_label,
            penalties_label,
            one_touch_pass_label,
        )

        return self.parent.set_value_from_label(full_label)
