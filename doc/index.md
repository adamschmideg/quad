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

# How to store wip changes

The obvious idea was to use version control for small wip changes, too.
I could use the same git as I use normally, but work an a different
branch, switching back and forth between wip and normal branches.  The
other approach that seemed easier to implement was to use another
version control system, namely mercurial for wip changes.  It had some
issues I haven't resolved yet.  It created new heads sometimes for some
unknown reason; it also had a problem "waiting for lock on working
directory".

So I'm thinking now if I really want to use a version control for wip
changes.  What I'm interested in is actually a large table for each
project where a record contains

  - a timestamp
  - the path of the file that was changed
  - a diff

Well, I actually need the file content before and after the change and
if I have only the diff without the original content, I can't calculate
structural changes from a diff.  It can be usable though if I have the
file content before the very first diff.  If I have this table of diffs
from the beginning of time, then all files were empty.  If I start
to store changes later, I'll need a starting status of all files.  It
boils then down to have an initial state of files and this table of
diffs.

What can I do when I switch branches?  It seems the table contains
mostly records described above and some rows that just point to a hash
of the normal repository.  Every time there is a branch switch, there
has to be a hash in the table which is actually a shorthand to have the
actual content of all files.

This table model has assumes furthermore that changes are saved so
frequently that it's reasonable to have only one record for a timestamp.
It's possible technically to have more records for the same timestamp,
showing that more files were changes at the same moment, like renaming a
variable in multiple files.

# Hierarchy of code importance

Developers waste most of the code they write.  There is a hierarchy of
code

  - Production code (version controlled, shared with peers)
  - Dev code (saved in local temp folders)
  - Throw-away code (living in the history until it gets too old)
  - Ad-hoc code written at the shell/REPL

The history of programming from this perspective is

  - Store only released code, maybe code of a few milestones (past)
  - Store meaningful changes (present)
  - Store any changes (future?)

What developers consider a "meaningful change" depends on a number of
factors.  It includes objective factors, like it's preferred to commit
only code that compiles, even better that runs all tests.  Continuous
integration tools aim to automatize these expectations.  I personally
prefer to commit every 30-60 minutes, that's a meaningful piece of work
for me.

Why is it important to store changes?  Older versions are rarely used,
version control is invisible most of the time, it's almost an autosave
feature we're not aware of.  Until we have to roll back to an earlier
version or in case there's a conflict between the changes of two team
members.

But reading code and changes in them have another important aspect.
That's the way we learn, our coding skills improve.  It mostly works on
an unconcious level, though.  I write a few lines of code, try it out,
see what happens, and carry on with the task at hand.  The other day, I
just walked past someone's monitor and saw this Python snippet,

    [] == False
    if []:
      print 'truthy'
    else:
      print 'FALSEY'

