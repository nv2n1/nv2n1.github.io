---
title: "parallel(1)"
name: "parallel"
section: "1"
letter: "p"
url: "/docs/linux/man/1-parallel/"
description: "parallel – run programs in parallel"
---

<h2 class="name">NAME</h2>
<p> parallel &#8211; run programs in parallel </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>parallel</code> [options] [command]<code>&#8212;</code> [argument &#8230;]</p>
<dt> <code>parallel</code> [options]<code>&#8212;</code> [command &#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>parallel</code></p>
<dd>runs the specified command, passing it a single one of the specified arguments. This is repeated for each argument. Jobs may be run in parallel. The default is to run one job per CPU. </p>
<p> If no command is specified before the &#8211;, the commands after it are instead run in parallel.</p>
<h2>OPTIONS</h2>
<p> <code>-j maxjobs</code></p>
<dl>
<dt>
<dd> Use to limit the number of jobs that are run at the same time.</dl>
<p> <code>-l maxload</code></p>
<dl>
<dt>
<dd> Wait as needed to avoid starting new jobs when the system&#8217;s load average is not below the specified limit.</dl>
<p> <code>-i</code></p>
<dl>
<dt>
<dd> Normally the command is passed the argument at the end of its command line. With this option, any instances of &quot;{}&quot; in the command are replaced with the argument.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> Number of arguments to pass to a command at a time. Default is 1. Incompatible with -i</dl>
<h2>EXAMPLE</h2>
<p> <code>parallel sh -c &quot;echo hi; sleep 2; echo bye&quot; &#8212; 1 2 3</code> </p>
<p> This runs three subshells that each print a message, delay, and print another message. If your system has multiple CPUs, parallel will run some of the jobs in parallel, which should be clear from the order the messages are output. </p>
<p> <code>parallel -j 3 ufraw -o processed &#8212; *.NEF</code> </p>
<p> This runs three ufraw processes at the same time until all of the NEF files have been processed. </p>
<p> <code>parallel -j 3 &#8212; ls df &quot;echo hi&quot;</code> </p>
<p> This runs three independent commands in parallel.</p>
<h2>EXIT STATUS</h2>
<p> Its exit status is the combination of the exit statuses of each command ran, ORed together. (Thus, if any one command exits nonzero, <code>parallel</code> as a whole will exit nonzero.)</p>
<h2>NOTES</h2>
<p> All output to stdout and stderr is serialised through a corresponding internal pipe, in order to prevent annoying concurrent output behaviour. Note that serialisation is not done on any other file descriptors and file position based access to a nonstandard file descriptor might have unexpected results.</p>
<h2>AUTHOR</h2>
<p> Tollef Fog Heen </p>
<h2>Index</h2>
