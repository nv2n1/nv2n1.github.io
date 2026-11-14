---
title: "lintiancommand(3)"
name: "lintiancommand"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintiancommand/"
description: "Lintian::Command – Utilities to execute other commands from lintian code"
---

<p>Lintian::Command &#8211; Utilities to execute other commands from lintian code </p>
<h2>Synopsis</h2>
<pre> use Lintian::Command qw(spawn);
 # simplest possible call
 my $success = spawn({}, ['command']);
 # catch output
 my $opts = {};
 $success = spawn($opts, ['command']);
 if ($success) {
 print &quot;STDOUT: $opts-&gt;{out}
&quot;;
 print &quot;STDERR: $opts-&gt;{err}
&quot;;
 }
 # from file to file
 $opts = { in =&gt; 'infile.txt', out =&gt; 'outfile.txt' };
 $success = spawn($opts, ['command']);
 # piping
 $success = spawn({}, ['command'], &quot;|&quot;, ['othercommand']);</pre>
<h2>Description</h2>
<p>Lintian::Command is a thin wrapper around IPC::Run, that catches exception and implements a useful default behaviour for input and output redirection. </p>
<p> Lintian::Command provides a function <code>spawn()</code> which is a wrapper around <code>IPC::Run::run()</code> resp. <code>IPC::Run::start()</code> (depending on whether a pipe is requested). To wait for finished child processes, it also provides the <code>reap()</code> function as a wrapper around <code>IPC::Run::finish()</code>.</p>
<h3>spawn($opts, @cmds)</h3>
<p>The <tt>@cmds</tt> array is given to <code>IPC::Run::run()</code> (or ::<code>start()</code>) unaltered, but should only be used for commands and piping symbols (i.e. all of the elements should be either an array reference, a code reference, &#8216;|&#8217;, or &#8216;&amp;&#8217;). I/O redirection is handled via the <tt>$opts</tt> hash reference. If you need more fine grained control than that, you should just use IPC::Run directly. </p>
<p> <tt>$opts</tt> is a hash reference which can be used to set options and to retrieve the status and output of the command executed. </p>
<p> The following hash keys can be set to alter the behaviour of <code>spawn()</code>:</p>
<dl COMPACT>
<dt>in</p>
<dd><font SIZE="-1">STDIN</font> for the first forked child. Defaults to <tt>&quot;
