# adext

`adext` is a small package that extends [alarmdecoder](https://github.com/nutechsoftware/alarmdecoder/) to include some additional methods for [Home Assistant](https://github.com/home-assistant/core).

Specifically, the following methods have been added:

- `arm_home`
- `arm_away`
- `arm_night`

Each method accepts the arguments described below to determine which key sequences are used to arm a panel based on factors like panel brand and user config settings.

## Arguments:

- **code**: (`None` or `str`) - the code used to arm a panel (i.e. `'1234'`)
- **auto_bypass**: (`bool`) - for Honeywell only. set to `True` to prefix an arming sequence with `<code> + 6#` in order to automatically bypass any faulted zones. This will require a code to be entered even if `code_arm_required` is set to `false`."
- **code_arm_required**: (`bool`) - set to `False` to enable arming without a code. see [Arming Key Sequences](#Arming-Key-Sequences) below.
- **alt_night_mode**: (`bool`) - For Honeywell systems, set to `true` to enable *Night-Stay* mode instead of *Instant* mode for night arming. For DSC systems, set to `true` to enable *No-Entry* mode instead of *Stay* mode for night arming. For both systems, whenever this option is set to `true`, a code will be required for night arming **regardless of the `code_arm_required` setting.** See [Arming Key Sequences](#Arming-Key-Sequences) section below for more information.


## Arming Key Sequences

The tables below show the key press sequences used for arming for the different panel brands and configuration setting combinations.

### Honeywell

#### code_arm_required = true (default)

| Mode                                                    | Key Sequence                |
| ------------------------------------------------------- | --------------------------- |
| `alarm_arm_home`                                        | `code` + `3`                |
| `alarm_arm_away`                                        | `code` + `2`                |
| `alarm_arm_night` (`alt_night_mode` = `false`, default) | `code` + `7`                |
| `alarm_arm_night` (`alt_night_mode` = `true`)           | `code` + `33`               |

#### code_arm_required = false

| Mode                                                    | Key Sequence                |
| ------------------------------------------------------- | --------------------------- |
| `alarm_arm_home`                                        | `#3`                        |
| `alarm_arm_away`                                        | `#2`                        |
| `alarm_arm_night` (`alt_night_mode` = `false`, default) | `#7`                        |
| `alarm_arm_night` (`alt_night_mode` = `true`)           | `code` + `33`               |

### DSC

#### code_arm_required = true (default)

| Mode                                                    | Key Sequence                |
| ------------------------------------------------------- | --------------------------- |
| `alarm_arm_home`                                        | `code`                      |
| `alarm_arm_away`                                        | `code`                      |
| `alarm_arm_night` (`alt_night_mode` = `false`, default) | `code`                      |
| `alarm_arm_night` (`alt_night_mode` = `true`)           | `*9` + `code`               |

#### code_arm_required = false

<div class='note'>

The `chr(4)` and `chr(5)` sequences below are equivalent to pressing the <em>Stay</em> and <em>Away</em> keypad keys respectively (as outlined in the <a href='http://www.alarmdecoder.com/wiki/index.php/Protocol#Special_Keys'>AlarmDecoder documentation</a>).

</div>

| Mode                                                    | Key Sequence                    |
| ------------------------------------------------------- | ------------------------------- |
| `alarm_arm_home`                                        | `chr(4)` + `chr(4)` + `chr(4)`  |
| `alarm_arm_away`                                        | `chr(5)` + `chr(5)` + `chr(5)`  |
| `alarm_arm_night` (`alt_night_mode` = `false`, default) | `chr(4)` + `chr(4)` + `chr(4)`  |
| `alarm_arm_night` (`alt_night_mode` = `true`)           | `*9` + `code`                   |
