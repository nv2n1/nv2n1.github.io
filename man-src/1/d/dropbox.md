---
title: "dropbox(1)"
name: "dropbox"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dropbox/"
description: "dropbox – A command line interface to the Dropbox service"
---

<h2>NAME</h2>
<p> dropbox &#8211; A command line interface to the Dropbox service</p>
<h2>SYNOPSIS</h2>
<pre><code>
dropbox status
    dropbox help[COMMAND] dropbox puburl FILE
        dropbox stop
            dropbox running
                dropbox start[-i] dropbox filestatus[-l][-a][FILE]... dropbox ls[FILE]... dropbox autostart[y / n] dropbox exclude[list] dropbox lansync[y / n]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <i>dropbox</i> command provides a command line interface to the Dropbox, the easiest online file storage, synchronization and sharing service.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>dropbox</code> <i>status</i></p>
<dd>
<pre>
Prints out the current status of the Dropbox daemon.
</pre>
<dt><code>dropbox</code> <i>help</i> [COMMAND]</p>
<dd>
<pre>
With no arguments, print a list of commands and a short description of each. With a command, print descriptive help on how to use the command.
</pre>
<dt><code>dropbox</code> <i>puburl</i> FILE</p>
<dd>
<pre>
Prints out a public url for FILE.
</pre>
<dt><code>dropbox</code> <i>stop</i></p>
<dd>
<pre>
Stops the dropbox daemon.
</pre>
<dt><code>dropbox</code> <i>running</i></p>
<dd>
<pre>
Returns 1 if running 0 if not running.
</pre>
<dt><code>dropbox</code> <i>start</i> [-i]</p>
<dd>
<pre>
Starts the dropbox daemon, dropboxd. If dropboxd is already running, this will do nothing.
options:
-i --install  auto install dropboxd if not available on the system
</pre>
<dt><code>dropbox</code> <i>filestatus</i> [-l] [-a] [FILE]&#8230;</p>
<dd>
<pre>
Prints the current status of each FILE.
options:
-l --list  prints out information in a format similar to ls. works best when your console supports color :)
-a --all   do not ignore entries starting with .
Aliases: stat
</pre>
<dt><code>dropbox</code> <i>ls</i> [FILE]&#8230;</p>
<dd>
<pre>
This is an alias for filestatus -l
</pre>
<dt><code>dropbox</code> <i>autostart</i> [y/n]</p>
<dd>
<pre>
options:
n  dropbox will not start automatically at login
y  dropbox will start automatically at login (default)
Note: May only work on current Ubuntu distributions.
</pre>
<dt><code>dropbox</code> <i>exclude</i> [list]dropbox exclude add [DIRECTORY] [DIRECTORY] &#8230;</p>
<dd>
dropbox exclude remove[DIRECTORY][DIRECTORY]&#8230; &#8220;list&#8221; prints a list of directories currently excluded from syncing.&#8221;add&#8221; adds one or more directories to the exclusion list, then resynchronizes Dropbox.&#8221;remove&#8221; removes one or more directories from the exclusion list, then resynchronizes Dropbox.With no arguments, executes &#8220;list&#8221;.Any specified path must be within Dropbox.</p>
<dt><code>dropbox</code> <i>lansync</i> [y/n]</p>
<dd>
<pre>
options:
y  dropbox will use LAN sync (default)
n  dropbox will not use LAN sync
</pre>
</dl>
<h2>BUGS</h2>
<p> There are currently no known bugs. If you think you have found a bug or have a feature request, post in the forums, or send us an e-mail (see the <code>RESOURCES</code> section below). </p>
<p> In the future there will be full command line support including linking accounts and setting preferences from the <i>dropbox</i> command.</p>
<h2>RESOURCES</h2>
<dl>
<dt>&bull;</p>
<dd> Dropbox &lt;<i><a rel="nofollow" href="https://www.dropbox.com/">https://www.dropbox.com/</a></i>&gt;</p>
<dt>&bull;</p>
<dd> Dropbox Forums &lt;<i><a rel="nofollow" href="https://forums.dropbox.com/">https://forums.dropbox.com/</a></i>&gt;</p>
<dt>&bull;</p>
<dd> Dropbox Support E-mail &lt;<i>support [at] dropbox.com</i>&gt;</dl>
<h2>AUTHORS</h2>
<pre><code>
Rian Hunter&lt;rian[at] dropbox.com&gt;
    Mike Haimes&lt;mike[at] dropbox.com&gt;
        David Euresti&lt;david[at] dropbox.com&gt;
</code></pre>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2008-2011 Evenflow, Inc. Free use of this software is granted under the terms of the GNU General Public License (GPL). </p>
<h2>Index</h2>
