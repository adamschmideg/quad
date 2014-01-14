This is a list of what is written or I'm going to write

  - [Installation](..#install)
  - Usage
  - Similar projects
  - Further plans
  - Concepts
    - Measuring different programming activities
    - Measuring time
    - How big is a commit?  How to assign a numerical value to a commit?

# Short term plans

  - [ ] Use git instead of mercurial
  - [X] Monitor multiple repos
  - [ ] Use a single wip repo for multiple normal repos

## Use a single wip repo

What I'm experimenting with right now is to have all my projects in the
same folder (`~/p` for simplicity's sake).  Then

    cd ~/p
    hg init
    ./p/quad/quad.py ~/p &

I have some concerns though:
  
  - I'll have files from all projects into a single repo
  - Multiplied by many wip commits
  - All -- possibly sensitive -- company info would reside in my repo

## Use a different branch as wip repo

This is the alternative approach.  I won't have to think about who can
read what, it's the same people who can read the regular repo.  There is
however the risk that the company will have access to my private work
stats which may be uncomfortable for some developers.  (See Ethical
issues in Mining software repositories.)

## Similar projects

  - http://www.codeivate.com
  - http://wakati.me

## Tools for Mining software repositories

  - See http://stackoverflow.com/a/1829302/380587
  - https://bitbucket.org/sealuzh/tools-changedistiller/wiki/Home
  - https://github.com/yinwang0/psydiff
  - https://code.google.com/p/harmony/
  - http://www.monperrus.net/martin/tree-differencing (it basically
    mentions the above projects)
