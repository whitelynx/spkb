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

You can install prerequisites with `pip`:

```bash
pip install -r requirements.txt
```


This will install the following Python packages:

- [solidpython2](https://github.com/jeff-dh/SolidPython)
## Prerequisites

* [Python][] version 3.11 or newer
* [pipenv](https://pipenv.pypa.io/en/latest/)

## Installing dependencies

```bash
pipenv install
```

## Usage

For simply generating interesting key testers, see the example scripts in the `examples/`
directory.

---

In your own code, you can simply import from the `spkb` module:
```python
import * from spkb
```

See `spkb/__init__.py` for more detail about what's exported.

You can also import directly from the submodules, which is especially useful for objects that
aren't re-exported by the top-level module:

```python
from spkb.switch_plate import plate_thickness, mx_plate
from spkb.board_mount import stm32_blackpill
from spkb.keycaps import sa_double_length, sa_cap
```

## Testing

You can run simple tests from some of the submodules:

```bash
pipenv run python -m spkb.switch_plate  # Renders a variety of keyswitch plates (sockets)
pipenv run python -m spkb.keycaps       # Renders the built-in keycap approximations
pipenv run python -m spkb.single_tester # Renders a single-key tester
```

## Links

* [parametric-key-tester](https://github.com/whitelynx/parametric-key-tester) - the original project this library was forked from
* [the Dactyl Keyboard][] and my fork, [the Dactyl Lynx Keyboard][] - original switch sockets, keycap approximations, etc.


## License

This project is released under [the BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause).
