---
title: "func(1)"
name: "func"
section: "1"
letter: "f"
url: "/docs/linux/man/1-func/"
---

<h2>NAME</h2>

 Func -- Fedora Unified Network Controller.

<h2>SYNOPSIS</h2>

 func ``*'' list_minions 

 func target.example.org call module method [args ...] 

 func ``target*.example.org'' call module method [args ...] 

 func ``webserver1;mailserver2'' call module method [args ...]

<h2>DESCRIPTION</h2>

 ``func'' allows remote control of machines running funcd (called ``minions'') that are set to obey this machine (called the ``overlord''). This includes performing various remote operations and gathering data. 

 ``func'' can address multiple machines at the same time by specifying their names with globs, which follow shell glob syntax. 

 Groups of machines can also be specified in /etc/func/groups. To invoke func on a group of machines specifying ``@groupname''. 

 See the project homepage (below) for a list of modules available and a more in-depth description of what each of them do.

<h2>THE CALL MODULE</h2>

 The ``call'' module is used for running func modules remotely. 

 Format: func ``*.example.org'' call &lt;module&gt; &lt;function&gt; [ args ... ]

<h2>LISTING REMOTE MODULES AVAILABLE</h2>

 It's possible to ask func minions what modules they have installed: 

 func ``*.example.org'' call system list_modules

<h2>LISTING REMOTE FUNCTIONS AVAILABLE IN A MODULE</h2>

 It is also possible to ask remote func modules what functions they support: 

 func target.example.org call modulename list_methods

<h2>CALLING A REMOTE COMMAND</h2>

 Once you have the name of a module you want to run, use call to invoke it: 

 func target.example.org call modulename methodname

<h2>OUTPUT FORMATS</h2>

 The ``call'' command by default outputs data using a ``pretty printer''. Other display options include --raw, --json, and --xmlrpc, which may be more desirable if you are running func inside another script or prefer to read those display formats. 

 Example: func ``*'' call --json service inventory

<h2>HELPER MODULES</h2>

 In addition to ``call'', there are other modules that make control of remote machines, as well as data display, more user friendly. They augment ``call'' by providing some additional functionality. 

 You will notice that the syntax for using one of these helper modules varies slightly from just using ``call'' directly. 

 For example ``show'' can be used to show remote data. The normal command &quot;func '*' command would dump a very large amount of data, while the show command can mine only a few details. This might make things more readable, for instance, when not going through the Python <font SIZE="-1">API</font> (where you would not care). 

 func ``*.example.org'' show hardware --help 

 func ``*.example.org'' show hardware systemMemory 

 func ``*.example.org'' show hardware os 

 Another useful helper command module is copyfile, which allows func to work like scp from the shell, though it can address multiple systems at the same time. 

 The following example pushes one file out to multiple systems: 

 func ``*.example.org'' copyfile --file=/tmp/foo --remotepath=/tmp/foo 

 While these helper modules will grow over time, usage of ``call'' syntax directly is fine also. See the Wiki for more examples as they evolve.

<h2>--verbose</h2>

 Use this flag to output extra information from func while it is running. All func commands can take this flag.

<h2>EXIT_STATUS</h2>

 Func commands have return values that vary based on the module being called. See the project page (linked below) for more information.

<h2>ADDITONAL RESOURCES</h2>

 See <a rel="nofollow" HREF="https://fedorahosted.org/func/">https://fedorahosted.org/func/</a> for more information, including information on scripting func from Python. 

 See also the manpages for ``func-inventory'', ``funcd'', ``certmaster'', ``certmaster-ca'', and ``func-transmit''.

<h2>AUTHOR</h2>

 Various. See <a rel="nofollow" HREF="https://fedorahosted.org/func/">https://fedorahosted.org/func/</a> 

<h2>Index</h2>


