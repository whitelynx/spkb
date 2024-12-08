# SPKB

_SolidPython-based Keyboard Builder_

![Action Shot](images/action-shot.jpg)

A [SolidPython][]-based library for building custom keyboards with [Python][] and [OpenSCAD][].

Some portions ported from Clojure, originally from [the Dactyl Keyboard][] and my fork thereof,
[the Dactyl Lynx Keyboard][].

[SolidPython]: https://github.com/jeff-dh/SolidPython
[Python]: https://www.python.org/
[OpenSCAD]: https://openscad.org/
[the Dactyl Keyboard]: https://github.com/adereth/dactyl-keyboard
[the Dactyl Lynx Keyboard]: https://github.com/whitelynx/dactyl-lynx-keyboard


## Prerequisites

* [Python][] version 3.11 or newer
* [poetry](https://python-poetry.org/docs/)

## Installing dependencies

```bash
poetry install
```


## Usage

For simply generating interesting key testers, see the example scripts in the `examples/`
directory.

---

In your own code, you can simply import what you need from the submodules of `spkb`:
```python
from spkb.switch_plate import plate_thickness, mx_plate
from spkb.board_mount import stm32_blackpill
from spkb.keycaps import sa_double_length, sa_cap
```

See the sidebar of the documentation for a reference of what's available.


## Testing

You can run simple tests from some of the submodules:

```bash
poetry run python -m spkb.keycaps         # Renders the built-in keycap approximations
poetry run python -m spkb.single_key_pcb  # Renders a simple approximation of a single-key PCB
poetry run python -m spkb.single_tester   # Renders a single-key tester
poetry run python -m spkb.keyswitch.choc  # Renders a switch socket with backplate for a Kailh Choc switch
poetry run python -m spkb.keyswitch.mx    # Renders a switch socket with backplate for an MX-style switch

# Deprecated modules
poetry run python -m spkb.switch_plate    # Renders a variety of keyswitch plates (sockets)
poetry run python -m spkb.keyswitch       # Renders a basic approximation of an MX-style switch body
```


## Documentation

You can view the generated API documentation locally by running [pdoc][]:

```bash
poetry run pdoc -n -t templates spkb
```

[pdoc]: https://pdoc.dev/


## Links

* [parametric-key-tester](https://github.com/whitelynx/parametric-key-tester) - the original project this library was forked from
* [the Dactyl Keyboard][] and my fork, [the Dactyl Lynx Keyboard][] - original switch sockets, keycap approximations, etc.


## License

This project is released under [the BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause).
