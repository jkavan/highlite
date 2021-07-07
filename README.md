# highlite

highlite is a simple utility for highlighting command line output using one or more regular expressions.

## Description

This tool was inspired by [Paolo Antinori's hhighlighter](https://github.com/paoloantinori/hhighlighter). It has a very similar functionality, but under the hood it uses _ack_ for highlighting. I needed a tool like _hhighlighter_ without having to have _ack_ on oll my computers or servers.

Highlite is written in Python 3 and it uses Python's regular expressions. Its functionality can easily be expanded or customized.

![Demo](screenshots/demo.gif)

## Requirements

Highlite requires Python 3 and [termcolors](https://pypi.org/project/termcolor/) module (see [requirements.txt](requirements.txt)).

You can easily install the dependencies with pip: `pip install -r requirements.txt`.

## Installation

There are multiple way to install highlite. You can just clone this repository and install it globally by symlinking the `highlite.py` file to `/usr/local/bin/hl` (or somewhere else, as long as it's in your `$PATH`).

```shell
git clone https://github.com/jkavan/highlite.git
ln -s <path_to_highlite>/highlite.py /usr/local/bin/hl
```

The `highlite.plugin.zsh` and `highlite.sh` are just wrappers/aliases for Zsh/Bash; they are not required.

### Zsh

Clone the repository somewhere and source the `highlite.plugin.zsh` file in your `.zshrc`:

```shell
source <path_to_highlite>/highlite.plugin.zsh
```

### Zsh with [ohmyzsh](https://github.com/ohmyzsh/ohmyzsh)

Clone the repository to ohmyzsh's plugin directory:

```shell
git clone https://github.com/ohmyzsh/ohmyzsh $ZSH_CUSTOM/plugins/highlite
```

Or if you're using Git to manage your dotfiles, you can add the plugin as a submodule:

```shell
git submodule add https://github.com/jkavan/highlite <path_to_ohmyzsh_plugins>/highlite
```

After cloning the repository, load the plugin in your `~/.zshrc` file:

```shell
plugins=(
  ... # other plugins
  highlite
)
```

### Bash

Clone the repository and copy and paste the following line in your `~/.bashrc`:

```shell
source <path_to_highlite>/highlite.sh
```

## Usage

```shell
Usage: [COMMAND] | hl [OPTION] REGEX...

OPTIONS:
  -h, --help         Print this help message
  -v, --version      Print version information
  -i, --ignore-case  Ignore case when searching
```
