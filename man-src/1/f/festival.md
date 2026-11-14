---
title: "festival(1)"
name: "festival"
section: "1"
letter: "f"
url: "/docs/linux/man/1-festival/"
description: "festival – a text-to-speech system."
---

<h2>NAME</h2>
<p> festival &#8211; a text-to-speech system.</p>
<h2>SYNOPSIS</h2>
<p> <code>festival </code> <i>[options]</i> <i>[file0]</i> <i>[file1]</i> <i>&#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> Festival is a general purpose text-to-speech system. As well as simply rendering text as speech it can be used in an interactive command mode for testing and developing various aspects of speech synthesis technology. </p>
<p> Festival has two major modes, command and tts (text-to-speech). When in command mode input (from file or interactively) is interpreted by the command interpreter. When in tts mode input is rendered as speech. When in command mode filenames that start with a left paranthesis are treated as literal commands and evaluated. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-q </code></p>
<dd> Load no default setup files</p>
<dt><code>&#8211;libdir </code><i>&lt;string&gt;</i></p>
<dd> Set library directory pathname</p>
<dt><code>-b </code></p>
<dd> Run in batch mode (no interaction)</p>
<dt><code>&#8211;batch </code></p>
<dd> Run in batch mode (no interaction)</p>
<dt><code>&#8211;tts </code></p>
<dd> Synthesize text in files as speech no files means read from stdin (implies no interaction by default)</p>
<dt><code>-i </code></p>
<dd> Run in interactive mode (default)</p>
<dt><code>&#8211;interactive </code></p>
<dd> Run in interactive mode (default)</p>
<dt><code>&#8211;pipe </code></p>
<dd> Run in pipe mode, reading commands from stdin, but no prompt or return values are printed (default if stdin not a tty)</p>
<dt><code>&#8211;language </code><i>&lt;string&gt;</i></p>
<dd> Run in named language, default is english, spanish and welsh are available</p>
<dt><code>&#8211;server </code></p>
<dd> Run in server mode waiting for clients of server_port (1314)</p>
<dt><code>&#8211;script </code></p>
<dd> &lt;ifile&gt; Used in #! scripts, runs in batch mode on file and passes all other args to Scheme</p>
<dt><code>&#8211;heap </code><i>&lt;int&gt;</i><code> {1000000}</code></p>
<dd> Set size of Lisp heap, should not normally need to be changed from its default</p>
<dt><code>-v </code></p>
<dd> Display version number and exit</p>
<dt><code>&#8211;version </code></p>
<dd> Display version number and exit</dl>
<h2>BUGS</h2>
<p> More than you can imagine. </p>
<p> A manual with much detail (though not complete) is available in distributed as part of the system and is also accessible at<br />
 <a rel="nofollow" href="http://www.cstr.ed.ac.uk/projects/festival/manual/">http://www.cstr.ed.ac.uk/projects/festival/manual/</a> </p>
<p> Although we cannot guarantee the time required to fix bugs, we would appreciated it if they were reported to<br />
 festival-bug [at] cstr.ed.ac.uk </p>
<h2>AUTHOR</h2>
<p> Alan W Black, Richard Caley and Paul Taylor<br />
 (C) Centre for Speech Technology Research, 1996-1998<br />
 University of Edinburgh<br />
 80 South Bridge<br />
 Edinburgh EH1 1HN<br />
 <a rel="nofollow" href="http://www.cstr.ed.ac.uk/projects/festival.html">http://www.cstr.ed.ac.uk/projects/festival.html</a> </p>
<h2>Index</h2>
