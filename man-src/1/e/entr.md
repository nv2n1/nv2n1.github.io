---
title: "entr(1)"
name: "entr"
section: "1"
letter: "e"
url: "/docs/linux/man/1-entr/"
description: "entr – run arbitrary commands when files change"
---

<h2>NAME</h2>
<p> <code>entr</code> &#8211; run arbitrary commands when files change</p>
<h2>SYNOPSIS</h2>
<p> [-<code>cdpr</code> ] <i>utility</i> [<i>argument &#8230;</i> ] [<i>/_</i> ]</p>
<h2>DESCRIPTION</h2>
<p> A list of files provided on the standard input and the <i>utility</i> is executed using the supplied arguments if any of them change. waits for the child process to finish before responding to subsequent file system events. A TTY is also opened before entering the watch loop in order to support interactive utilities. </p>
<p> The arguments are as follows:</p>
<dl>
<dt><code>-c</code></p>
<dd> Execute /usr/bin/clear before invoking the <i>utility</i> specified on the command line.</p>
<dt><code>-d</code></p>
<dd> Track the directories of regular files provided as input and exit if a new file is added. This option also enables directories to be specified explicitly. Files with names beginning with `.&#8217; are ignored.</p>
<dt><code>-p</code></p>
<dd> Postpone the first execution of the <i>utility</i> until a file is modified.</p>
<dt><code>-r</code></p>
<dd> Reload a persistent child process. <code>SIGTERM</code> is used to terminate the <i>utility before it is restarted.</i> A process group is created to prevent shell scripts from masking signals. waits for the <i>utility</i> to exit to ensure that resources such as sockets have been closed.</dl>
<p> The first occurrence of <i>/_</i> on the command line will be replaced with the absolute path of the first file that was modified. If the restart option is used the first file under watch is treated as the default.</p>
<h2>ENVIRONMENT</h2>
<p> If <code>PAGER</code> is undefined, <code>entr</code> will assign /bin/cat to prevent interactive utilities from waiting for keyboard input if output does not fit on the screen.</p>
<h2>EXIT STATUS</h2>
<p> The utility exits with one of the following values: </p>
<dl>
<dt><code>0</code></p>
<dd> <code>SIGINT</code> or <code>SIGTERM</code> was received</p>
<dt><code>1</code></p>
<dd> No regular files were provided as input or an error occurred</p>
<dt><code>2</code></p>
<dd> A file was added to a directory and the directory watch option was specified</dl>
<h2>EXAMPLES</h2>
<p> Rebuild a project if source files change, limiting output to the first 20 lines: </p>
<blockquote><p><tt>$ find src/ | entr sh -c 'make | head -n 20'</tt></p></blockquote>
<p> Launch and auto-reload a node.js server: </p>
<blockquote><p><tt>$ ls *.js | entr -r node app.js</tt></p></blockquote>
<p> Clear the screen and run a query after the SQL script is updated: </p>
<blockquote><p><tt>$ echo my.sql | entr -p psql -f /_</tt></p></blockquote>
<p> Rebuild project if a source file is modified or added to the src/ directory: </p>
<blockquote><p><tt>$ while true; do ls src/*.rb | entr -d make; done</tt></p></blockquote>
<h2>Index</h2>
