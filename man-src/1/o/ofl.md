---

title: "ofl(1)"
name: "ofl"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ofl/"
description: "ofl — open file lister"
---

<p> ofl &#8212; open file lister</p>
<h2>Syntax</h2>
<p> <code>ofl</code> [<code>-P</code>] [<code>-k</code> <i>signalspec</i>] <i>path</i>[&#8230;]</p>
<h2>Description</h2>
<p> Lists all processes that have directories or files open or in use within <i>path</i>. Additionally it can send a signal to these processes to free up a mountpoint for example.</p>
<h2>Options</h2>
<dl>
<dt><code>-k</code> <i>signalspec</i></dt>
<dd> Send the given signal to all processes that match.</dd>
<dt><code>-P</code></dt>
<dd> Show only the PIDs of the processes that matched.</dd></dl>
<h2>Differences to lsof/fuser</h2>
<dl>
<dt>&bull;</dt>
<dd> `lsof /home/user` and `fuser /home/user` would not list processes that have a descriptor open on /home/user/subdir.</dd>
<dt>&bull;</dt>
<dd> `fuser -m /home/subdir` would automatically go down to the root of a vfsmount (e.g. /home) and list all processes, instead of limiting to /home/subdir.</dd></dl>
<h2>See also</h2>
<p> <code>hxtools</code>(7) </p>
