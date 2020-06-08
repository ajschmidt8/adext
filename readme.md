# adext

`adext` is a small package that extends [alarmdecoder](https://github.com/nutechsoftware/alarmdecoder/) to include some additional methods for [Home Assistant](https://github.com/home-assistant/core).

Specifically, the following methods have been added:

- `arm_home`
- `arm_away`
- `arm_night`

Each method accepts arguments described below to determine which key sequences are used to arm a panel based on factors like panel brand and user config settings (i.e. whether or not a code is required to arm the panel).

## Arguments:

- **code**:
- **auto_bypass**:
- **code_arm_required**:
- **alt_night_mode**:
