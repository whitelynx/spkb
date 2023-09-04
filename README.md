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


## Usage

```python
import * from spkb
```

See the example scripts in the `examples/` directory.


## Links

* [parametric-key-tester](https://github.com/whitelynx/parametric-key-tester) - the original project this library was forked from
* [the Dactyl Keyboard][] and my fork, [the Dactyl Lynx Keyboard][] - original switch sockets, etc.


## License

This project is released under [the BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause).
