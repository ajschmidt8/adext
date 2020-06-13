"""Tests for adext"""

from unittest.mock import Mock
import pytest
from alarmdecoder.panels import DSC, ADEMCO as HONEYWELL
from adext import AdExt


@pytest.mark.parametrize(
    "code,code_arm_required,auto_bypass,brand,arm_sequence",
    #    code  req   bypa
    [
        (1234, True, True, HONEYWELL, "12346#12343"),
        (1234, True, False, HONEYWELL, "12343"),
        (1234, False, True, HONEYWELL, "12346##3"),
        (1234, False, False, HONEYWELL, "#3"),
        (None, True, True, HONEYWELL, ""),
        (None, True, False, HONEYWELL, ""),
        (None, False, True, HONEYWELL, "#3"),
        (None, False, False, HONEYWELL, "#3"),
        (1234, True, True, DSC, "1234"),
        (1234, True, False, DSC, "1234"),
        (1234, False, True, DSC, chr(4) * 3),
        (1234, False, False, DSC, chr(4) * 3),
        (None, True, True, DSC, ""),
        (None, True, False, DSC, ""),
        (None, False, True, DSC, chr(4) * 3),
        (None, False, False, DSC, chr(4) * 3),
    ],
)
def test_arm_home(code, code_arm_required, auto_bypass, brand, arm_sequence):
    """Test all variations of arm_home"""
    ad = AdExt("device")
    ad.mode = brand
    ad.send = Mock()
    ad.arm_home(
        code=code, code_arm_required=code_arm_required, auto_bypass=auto_bypass,
    )

    if arm_sequence:
        return ad.send.assert_called_once_with(arm_sequence)
    return ad.send.assert_not_called()


@pytest.mark.parametrize(
    "code,code_arm_required,auto_bypass,brand,arm_sequence",
    #    code  req   bypa
    [
        (1234, True, True, HONEYWELL, "12346#12342"),
        (1234, True, False, HONEYWELL, "12342"),
        (1234, False, True, HONEYWELL, "12346##2"),
        (1234, False, False, HONEYWELL, "#2"),
        (None, True, True, HONEYWELL, ""),
        (None, True, False, HONEYWELL, ""),
        (None, False, True, HONEYWELL, "#2"),
        (None, False, False, HONEYWELL, "#2"),
        (1234, True, True, DSC, "1234"),
        (1234, True, False, DSC, "1234"),
        (1234, False, True, DSC, chr(5) * 3),
        (1234, False, False, DSC, chr(5) * 3),
        (None, True, True, DSC, ""),
        (None, True, False, DSC, ""),
        (None, False, True, DSC, chr(5) * 3),
        (None, False, False, DSC, chr(5) * 3),
    ],
)
def test_arm_away(code, code_arm_required, auto_bypass, brand, arm_sequence):
    """Test all variations of arm_away"""
    ad = AdExt("device")
    ad.mode = brand
    ad.send = Mock()
    ad.arm_away(
        code=code, code_arm_required=code_arm_required, auto_bypass=auto_bypass,
    )

    if arm_sequence:
        return ad.send.assert_called_once_with(arm_sequence)
    return ad.send.assert_not_called()


@pytest.mark.parametrize(
    "code,code_arm_required,alt_night_mode,auto_bypass,brand,arm_sequence",
    #    code  req   alt   bypa
    [
        (1234, True, True, True, HONEYWELL, "12346#123433"),
        (1234, True, True, False, HONEYWELL, "123433"),
        (1234, True, False, True, HONEYWELL, "12346#12347"),
        (1234, True, False, False, HONEYWELL, "12347"),
        (1234, False, True, True, HONEYWELL, "12346#123433"),
        (1234, False, True, False, HONEYWELL, "123433"),
        (1234, False, False, True, HONEYWELL, "12346##7"),
        (1234, False, False, False, HONEYWELL, "#7"),
        (None, True, True, True, HONEYWELL, ""),
        (None, True, True, False, HONEYWELL, ""),
        (None, True, False, True, HONEYWELL, ""),
        (None, True, False, False, HONEYWELL, ""),
        (None, False, True, True, HONEYWELL, ""),
        (None, False, True, False, HONEYWELL, ""),
        (None, False, False, True, HONEYWELL, "#7"),
        (None, False, False, False, HONEYWELL, "#7"),
        (1234, True, True, True, DSC, "*91234"),
        (1234, True, True, False, DSC, "*91234"),
        (1234, True, False, True, DSC, "1234"),
        (1234, True, False, False, DSC, "1234"),
        (1234, False, True, True, DSC, "*91234"),
        (1234, False, True, False, DSC, "*91234"),
        (1234, False, False, True, DSC, chr(4) * 3),
        (1234, False, False, False, DSC, chr(4) * 3),
        (None, True, True, True, DSC, ""),
        (None, True, True, False, DSC, ""),
        (None, True, False, True, DSC, ""),
        (None, True, False, False, DSC, ""),
        (None, False, True, True, DSC, ""),
        (None, False, True, False, DSC, ""),
        (None, False, False, True, DSC, chr(4) * 3),
        (None, False, False, False, DSC, chr(4) * 3),
    ],
)
def test_arm_night(
    code, code_arm_required, alt_night_mode, auto_bypass, brand, arm_sequence
):
    """Test all variations of arm_night."""
    ad = AdExt("device")
    ad.mode = brand
    ad.send = Mock()
    ad.arm_night(
        code=code,
        code_arm_required=code_arm_required,
        auto_bypass=auto_bypass,
        alt_night_mode=alt_night_mode,
    )

    if arm_sequence:
        return ad.send.assert_called_once_with(arm_sequence)
    return ad.send.assert_not_called()


def test_arm_night_no_alt():
    """Test arm_night without alt_night_mode arg"""
    ad = AdExt("device")
    ad.mode = HONEYWELL
    ad.send = Mock()
    ad.arm_night(
        code="1234", code_arm_required=True, auto_bypass=True,
    )
    return ad.send.assert_called_once_with("12346#12347")
