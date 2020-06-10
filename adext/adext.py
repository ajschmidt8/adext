"""
Extends the AlarmDecoder class to include helper methods for HomeAssistant
"""

from alarmdecoder.decoder import AlarmDecoder
from alarmdecoder.panels import DSC, ADEMCO as HONEYWELL

ARM_HOME = "arm_home"
ARM_AWAY = "arm_away"
ARM_NIGHT = "arm_night"


class AdExt(AlarmDecoder):
    """
    Extended AlarmDecoder class
    """

    def _get_arm_sequence(
        self, arm_mode, code, code_arm_required, alt_night_mode, auto_bypass
    ):
        """
        Returns arming sequences based on panel brand & config settings
        """

        arming_sequences = {
            HONEYWELL: {
                "code": {
                    ARM_HOME: f"{code!s}3",
                    ARM_AWAY: f"{code!s}2",
                    ARM_NIGHT: f"{code!s}33" if alt_night_mode else f"{code!s}7",
                },
                "nocode": {
                    ARM_HOME: "#3",
                    ARM_AWAY: "#2",
                    ARM_NIGHT: f"{code!s}33" if alt_night_mode else "#7",
                },
            },
            DSC: {
                "code": {
                    ARM_HOME: str(code),
                    ARM_AWAY: str(code),
                    ARM_NIGHT: f"*9{code!s}" if alt_night_mode else str(code),
                },
                "nocode": {
                    ARM_HOME: chr(4) * 3,
                    ARM_AWAY: chr(5) * 3,
                    ARM_NIGHT: f"*9{code!s}" if alt_night_mode else chr(4) * 3,
                },
            },
        }

        brand = self.mode
        if code_arm_required and not code:
            return ""
        if alt_night_mode and arm_mode == ARM_NIGHT and not code:
            return ""

        auto_bypass_code = (
            f"{code!s}6#" if auto_bypass and brand == HONEYWELL and code else ""
        )
        code_key = "code" if code_arm_required else "nocode"
        return auto_bypass_code + arming_sequences[brand][code_key][arm_mode]

    def _arm_panel(self, arm_mode, **kwargs):
        arm_sequence = self._get_arm_sequence(arm_mode, **kwargs)
        if arm_sequence:
            return self.send(arm_sequence)

    def arm_night(
        self, code=None, code_arm_required=True, alt_night_mode=False, auto_bypass=False
    ):
        """Arms an alarm panel in night mode"""
        arm_mode = ARM_NIGHT
        return self._arm_panel(
            arm_mode,
            code=code,
            code_arm_required=code_arm_required,
            alt_night_mode=alt_night_mode,
            auto_bypass=auto_bypass,
        )

    def arm_home(
        self, code=None, code_arm_required=True, alt_night_mode=False, auto_bypass=False
    ):
        """Arms an alarm panel in home/stay mode"""
        arm_mode = ARM_HOME
        return self._arm_panel(
            arm_mode,
            code=code,
            code_arm_required=code_arm_required,
            alt_night_mode=alt_night_mode,
            auto_bypass=auto_bypass,
        )

    def arm_away(
        self, code=None, code_arm_required=True, alt_night_mode=False, auto_bypass=False
    ):
        """Arms an alarm panel in away mode"""
        arm_mode = ARM_AWAY
        return self._arm_panel(
            arm_mode,
            code=code,
            code_arm_required=code_arm_required,
            alt_night_mode=alt_night_mode,
            auto_bypass=auto_bypass,
        )
