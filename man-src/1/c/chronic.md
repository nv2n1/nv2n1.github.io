---
title: "chronic(1)"
name: "chronic"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chronic/"
---

<h2 class="name">NAME</h2>
 

 chronic - runs a command quietly unless it fails 

<h2>SYNOPSIS</h2>

 chronic [-ev] <font SIZE="-1">COMMAND...</font>

<h2>DESCRIPTION</h2>

 chronic runs a command, and arranges for its standard out and standard error to only be displayed if the command fails (exits nonzero or crashes). If the command succeeds, any extraneous output will be hidden. 

 A common use for chronic is for running a cron job. Rather than trying to keep the command quiet, and having to deal with mails containing accidental output when it succeeds, and not verbose enough output when it fails, you can just run it verbosely always, and use chronic to hide the successful output. 

 <pre>
        0    1 * * * chronic backup # instead of backup &gt;/dev/null 2&gt;&amp;1
        */20 * * * * chronic -ve my_script # verbose for debugging
</pre>

<h2>OPTIONS</h2>

<dl>
<dt>-v
<dd> Verbose output (distinguishes between <font SIZE="-1">STDOUT</font> and <font SIZE="-1">STDERR,</font> also reports <font SIZE="-1">RETVAL</font>)
<dt>-e
<dd> Stderr triggering. Triggers output when stderr output length is non-zero. Without -e chronic needs non-zero return value to trigger output. 

 In this mode, chronic's return value will be <tt>2</tt> if the command's return value is <tt>0</tt> but the command printed to stderr.</dl>

<h2>AUTHOR</h2>

 Copyright 2010 by Joey Hess &lt;id [at] joeyh.name&gt; 

 Original concept and ``chronic'' name by Chuck Houpt. Code for verbose and stderr trigger by Tomas 'Harvie' Mudrunka 2016. 

 Licensed under the <font SIZE="-1">GNU GPL</font> version 2 or higher. 

<h2>Index</h2>


