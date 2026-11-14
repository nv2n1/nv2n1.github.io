---
title: "lnav(1)"
name: "lnav"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lnav/"
description: "lnav – ncurses-based log file viewer"
---

<h2>NAME</h2>
<p> lnav &#8211; ncurses-based log file viewer</p>
<h2>SYNOPSIS</h2>
<p> <code>lnav </code> [-hVsar] [logfile1 logfile2 &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The log file navigator, lnav, is an enhanced log file viewer that takes advantage of any semantic information that can be gleaned from the files being viewed, such as timestamps and log levels. Using this extra semantic information, lnav can do things like interleaving messages from different files, generate histograms of messages over time, and providing hotkeys for navigating through the file. It is hoped that these features will allow the user to quickly and efficiently zero in on problems.</p>
<h2>KEY BINDINGS</h2>
<dl>
<dt>?</p>
<dd> View/leave the online help text.</p>
<dt>q</p>
<dd> Quit the program.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> Print help and exit</p>
<dt><code>-H</code></p>
<dd> Display the internal help text.</p>
<dt><code>-I</code> path</p>
<dd> Add the given configuration directory to the search path.</p>
<dt><code>-i</code></p>
<dd> Install the given format files in the $HOME/.lnav/formats/installed directory and exit.</p>
<dt><code>-C</code></p>
<dd> Check the configuration and exit.</p>
<dt><code>-d</code> file</p>
<dd> Write debug messages to the given file.</p>
<dt><code>-V</code></p>
<dd> Print version information.</p>
<dt><code>-a</code></p>
<dd> Load all of the most recent log file types.</p>
<dt><code>-r</code></p>
<dd> Load older rotated log files as well.</p>
<dt><code>-t</code></p>
<dd> Prepend timestamps to the lines of data being read in on the standard input.</p>
<dt><code>-w</code> file</p>
<dd> Write the contents of the standard input to this file.</dl>
<h3>Optional arguments:</h3>
<dl>
<dt>logfile1</p>
<dd> The log files or directories to view. If a directory is given, all of the files in the directory will be loaded.</dl>
<h2>EXAMPLES</h2>
<p> To load and follow the syslog file: </p>
<pre>
    lnav -s
</pre>
<p> To load all of the files in /var/log: </p>
<pre>
    lnav /var/log
</pre>
<p> To watch the output of make with timestamps prepended: </p>
<pre>
    make 2&gt;&amp;1 | lnav -t
</pre>
<h2>AUTHOR</h2>
<p> This manual page was written by Salvatore Bonaccorso &lt;carnil [at] debian.org&gt; for the Debian system (but may be used by others). </p>
<h2>Index</h2>
