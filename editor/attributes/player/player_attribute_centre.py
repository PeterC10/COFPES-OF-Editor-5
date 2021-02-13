from editor.attributes.player.player_attribute import (
    PlayerAttribute,
    PlayerAttributeTypes,
)


class PlayerAttributeCentre(PlayerAttribute):
    @classmethod
    def att_class_name(cls):
        return "Centre"

    @classmethod
    def att_class_type(cls):
        return PlayerAttributeTypes.SpecialAbilities

    def get_raw_value(self):
        return self.parent.get_value()

    def get_value(self):
        return self.parent.get_value()

    def get_label(self):
        """
        Get full label from parent
        and return third value (centre is set third)
        """
        full_label = self.parent.get_label()
        return full_label[2]

    def set_value(self, value):
        return self.parent.set_value(value)

    def set_value_from_label(self, label):
        injury_tolerance_label = self.parent.injury_tolerance.get_label()
        weak_foot_frequency_label = self.parent.weak_foot_frequency.get_label()
        penalties_label = self.parent.penalties.get_label()
        one_touch_pass_label = self.parent.one_touch_pass.get_label()
        
        full_label = (
            injury_tolerance_label,
            weak_foot_frequency_label,
            label,
            penalties_label,
            one_touch_pass_label,
        )

        return self.parent.set_value_from_label(full_label)
