# highlite

highlite is a simple utility for highlighting command line output using one or more regular expressions.

## Description

This tool was inspired by [Paolo Antinori's hhighlighter](https://github.com/paoloantinori/hhighlighter). It has very similar functionality, but under the hood hhighlighter uses _ack_ for highlighting. I needed a tool like hhighlighter without having to have ack on all my computers or servers.

Highlite is written in Python 3 and it uses Python's regular expressions. Its functionality can easily be extended or customized.

![Demo](screenshots/demo.gif)

## Requirements

Highlite requires Python 3 and [termcolors](https://pypi.org/project/termcolor/) module (see [requirements.txt](requirements.txt)).

All dependencies can be easily installed with pip: `pip install -r requirements.txt`.

## Installation

There are multiple ways to install highlite. You can just clone this repository and install it globally by symlinking the `highlite.py` file to `/usr/local/bin/hl` (or somewhere else, as long as it can be found in the user's `$PATH` variable). This way all the users in the system will be able to use highlite.

```shell
git clone https://github.com/jkavan/highlite.git
ln -s <path_to_highlite>/highlite.py /usr/local/bin/hl
```

The `highlite.plugin.zsh` and `highlite.sh` are just wrappers/aliases for Zsh and Bash, so that they can be included in the shell with a single _source_ -command.

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

### Examples

If your command has a long output, you can also pipe highlite to `less` (make sure to use the `-R` option):

```shell
echo hello world | hl hello | less -R
```

Highlite also works well with `tail -f`:

```shell
tail -f <file> | hl <regex>
```
