# quad

__Quantified Developer__.

## Install

You'll need python, mercurial and watchdog.

### OSX

Your should have python already installed.  I recommend you install
[homebrew][homebrew], it'll make further installation simpler.  Then use it to
install mercurial and pip, the python package manager.

    brew install mercurial
    brew install pip

Now you have pip, so you're ready to install watchdog.  It gets installed
globally, so you'll be prompted for your password.

    sudo pip install watchdog

  [homebrew]: http://brew.sh/

### Ubuntu Linux

I haven't tried it yet, but it's supposed to work

    sudo apt-get install python mercurial watchdog

### Windows

I don't know and it's a low priority for me to make it install it on Windows,
but it's not supposed to be that difficult.

## Usage

### Prerequisites once in your lifetime

Initialize mercurial by editing `~/.hgrc` to contain

    [ui]
    username = Your Name <your@email>
    ignore = ~/.hgignore

Edit `~/.hgignore` to contain

    syntax: glob
    .git/*

### Prerequisites once for a project

Go to the project directory and enter

    hg init

### Everyday usage

Suppose you want track your for a project.
Open a separate terminal for it and just enter

    ./quad.py <directory_to_monitor>

You can specify more directories.
