---
title: "ofl(1)"
name: "ofl"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ofl/"
description: "ofl — open file lister"
---

<h2>Name</h2>
<p> ofl &#8212; open file lister</p>
<h2>Syntax</h2>
<p> <code>ofl</code> [<code>-P</code>] [<code>-k</code> <i>signalspec</i>] <i>path</i>[&#8230;]</p>
<h2>Description</h2>
<p> Lists all processes that have directories or files open or in use within <i>path</i>. Additionally it can send a signal to these processes to free up a mountpoint for example.</p>
<h2>Options</h2>
<dl>
<dt><code>-k</code> <i>signalspec</i></p>
<dd> Send the given signal to all processes that match.</p>
<dt><code>-P</code></p>
<dd> Show only the PIDs of the processes that matched.</dl>
<h2>Differences to lsof/fuser</h2>
<dl>
<dt>&bull;</p>
<dd> `lsof /home/user` and `fuser /home/user` would not list processes that have a descriptor open on /home/user/subdir.</p>
<dt>&bull;</p>
<dd> `fuser -m /home/subdir` would automatically go down to the root of a vfsmount (e.g. /home) and list all processes, instead of limiting to /home/subdir.</dl>
<h2>See also</h2>
<p> <code><a href="/docs/linux/man/7-hxtools/">hxtools</a></code>(7) </p>
<h2>Index</h2>
