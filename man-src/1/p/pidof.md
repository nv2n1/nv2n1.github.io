---
title: "pidof(1)"
name: "pidof"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pidof/"
description: "pidof — find the process ID of a running program."
---

<h2>NAME</h2>
<p> pidof &#8212; find the process ID of a running program.</p>
<h2>SYNOPSIS</h2>
<p> <code>pidof</code> [<code>-s</code>] [<code>-c</code>] [<code>-x</code>] [<code>-o</code> <i>omitpid[,omitpid..]</i>] [<code>-o</code> <i>omitpid[,omitpid..]..</i>] <code>program</code> [<code>program..</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Pidof</code> finds the process id&#8217;s (pids) of the named programs. It prints those id&#8217;s on the standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-s</p>
<dd> Single shot &#8211; this instructs the program to only return one <i>pid</i>.</p>
<dt>-c</p>
<dd> Only return process ids that are running with the same root directory. This option is ignored for non-root users, as they will be unable to check the current root directory of processes they do not own.</p>
<dt>-x</p>
<dd> Scripts too &#8211; this causes the program to also return process id&#8217;s of shells running the named scripts.</p>
<dt>-o <i>omitpid</i></p>
<dd> Tells <i>pidof</i> to omit processes with that process id. The special pid <code>%PPID</code> can be used to name the parent process of the <i>pidof</i> program, in other words the calling shell or shell script.</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> At least one program was found with the requested name.</p>
<dt><code>1</code></p>
<dd> No program was found with the requested name. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pgrep/">pgrep</a></code>(1), <code><a href="/docs/linux/man/1-pkill/">pkill</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Jaromir Capik &lt;jcapik [at] redhat.com&gt; </p>
<h2>Index</h2>
