---
title: "par(1)"
name: "par"
section: "1"
letter: "p"
url: "/docs/linux/man/1-par/"
description: "par – parallel command processing"
---

<h2>NAME</h2>
<p> par &#8211; parallel command processing</p>
<h2>SYNOPSIS</h2>
<p> <code>par</code> [<code>-defiqx</code>] [<code>-c&nbsp;<wbr></code> command] [<code>-l&nbsp;<wbr></code> logfile] [<code>-n</code><br />
&nbsp;<wbr>#] [<code>-p</code><br />
&nbsp;<wbr>#] [file [file&#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> <code>par</code> takes a list of files to run a command on. The first line of each file begins with a colon (:) or a pound-sign (#). If a colon, the remainder of the line is a command to run for each of the subsequent lines. If a pound-sign, then each subsequent line is a (self-contained) command, unless the <code>-c</code> option was specified, in which case it operates as if the argument to <code>-c</code> had followed a colon on the first line. </p>
<p> In each of the cases where the lines of the file following the first are not commands (ie: colon or -c), instances of open-close braces ({}) in the command will be replaced by these values. </p>
<p> For example, an inputfile whose contents is: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>: echo {}</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>a</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>b</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>c</p>
<p> run with <code>par</code> like so: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>%par -q inputfile</p>
<p> will produce the following output (order will vary): </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>b</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>a</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>c</p>
<p> The command-line options are as follows: </p>
<dl>
<dt><code>-c</code></p>
<dd> Command to be run on each of the arguments following the command-line options, where the first line of the input file(s) begins with a pound-sign (#).</p>
<dt><code>-d</code></p>
<dd> Print debugging information on standard error (stderr). Repeat the option up to three times for more verbosity.</p>
<dt><code>-e</code></p>
<dd> Split args by spaces, rather than using sh -c. Note: <code>-e</code> is incompatible with the <code>-i</code> option.</p>
<dt><code>-f</code></p>
<dd> No input file or STDIN, just run a quantity of the command specified with -c.</p>
<dt><code>-i</code></p>
<dd> Run commands interactively through (multiple) <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) processes.</p>
<dt><code>-l</code></p>
<dd> Prefix of logfile name, as in prefix.N where N is the <code>par</code> process number ([0..]). </p>
<p> Default: par.log.&lt;time&gt;.[0..]</p>
<dt><code>-n</code></p>
<dd> Number of simultaneous processes. </p>
<p> Default: 3</p>
<dt><code>-p N</code></p>
<dd> Pause N seconds between running commands.</p>
<dt><code>-q</code></p>
<dd> Quiet mode. Omit the typical processing logs and do not create the log files from -l, instead the children inherit stdout and stderr from <code>par.</code> <code>-q</code> is mutually exclusive with the <code>-x</code> and <code>-l</code> options and the option appearing last will take precedence.</p>
<dt><code>-x</code></p>
<dd> View par logs in real-time via an <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1). </p>
</dl>
<h2>FILES</h2>
<pre>
<i>par.log.T.N</i> Log file; where T is the current time in seconds since the
epoch and N is the par process number ([0..]).
</pre>
<h2>HISTORY</h2>
<p> <code>par</code> was ported from the perl version. </p>
<h2>Index</h2>
