# The useless CLI
## What is this?
This is a useless CLI that does some things that are not really helpful. It is written in Python and is cross-platform. I mainly made this to learn how to use Typer and PyInstaller. I also wanted to make a CLI that does something useful, but I couldn't think of anything. So I made this.
## Installation
Use pip to download from PyPI:

```
pip install the-useless-cli
```

Or install from the .tar.gz, click this button to install the latest version:

[![](https://img.shields.io/github/release/ItsQuadrus/the-useless-cli.svg?style=flat-square)](https://github.com/ItsQuadrus/the-useless-cli/releases/latest)

```
pip install the_useless_cli-0.0.1.tar.gz
```

---
<details>
<summary>Build instructions (ignore if you want to install)</summary>
<br>
If you just want to install, don't build it yourself. Download the latest release from pip. If you want to build it yourself, follow these steps:

1. Clone the repository

2. `pyinstaller src/__main__.py --onefile --name useless`

3. Move the executable to a folder in your PATH

4. Run `useless` in your terminal

5. Enjoy!
</details>

## Commands
Everything is listed in [here](docs/commands.md).
If you don't want to read that, just try `useless --help` in your terminal.



## License
This project is licensed under the GNU GPLv3 license. See [LICENSE](LICENSE.md) for more information.

In short:
- Anyone who modifies or distributes this code must make their modifications or distribution available under the GPL.
- Anyone who distributes this code must give "ItsQuadrus" credit as the original author.
- Derivative works must be distributed under the same license terms as the original work.

(This is a summary, not the license itself. This is not legal advice. Read the full license for more information.)