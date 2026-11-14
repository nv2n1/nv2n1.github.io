---
title: "beesu(1)"
name: "beesu"
section: "1"
letter: "b"
url: "/docs/linux/man/1-beesu/"
description: "beesu – A wrapper for \"su\" that provides a graphical interface in Fedora."
---

<h2>NAME</h2>
<p> beesu &#8211; A wrapper for &quot;su&quot; that provides a graphical interface in Fedora.</p>
<h2>SYNOPSIS</h2>
<p> <code>beesu [-P] [-v] [-l] [-m] [-f] [-s] [-c]</code> <i>COMMAND</i> <i>ARGs</i> <code>&#8230;</code></p>
<h2>DESCRIPTION</h2>
<p> <code>beesu</code> is a wrapper around <code><a href="/docs/linux/man/1-su/">su</a></code>(1) and works with <code><a href="/docs/linux/man/8-consolehelper/">consolehelper</a></code>(8) in Fedora to provide a graphical interface like gksu. </p>
<p> <code>beesu</code> is dedicated to all the friends of honey bees!</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;version</p>
<dd> display the software version and exit</p>
<dt>&#8211;print-conf</p>
<dd> display the configuration file contents and exit</p>
<dt>-P</p>
<dd> don&#8217;t join ARGs together</p>
<dt>-v</p>
<dd> verbose output</p>
<dt>-, -l, &#8211;login</p>
<dd> make the shell a login shell</p>
<dt>-c COMMAND</p>
<dd> pass a single COMMAND to the shell with -c</p>
<dt>-f, &#8211;fast</p>
<dd> pass -f to the shell (for csh or tcsh)</p>
<dt>-m, &#8211;preserve-environment</p>
<dd> do not reset environment variables</p>
<dt>-s SHELL</p>
<dd> run SHELL </p>
</dl>
<h2>EXAMPLES</h2>
<p> <code>beesu &#8211; nautilus</code> </p>
<p> To start <code>nautilus</code> as root. </p>
<p> <code>beesu -l -P whoami test</code> </p>
<p> That will start <code>whoami</code> impersonating the user <code>test</code> (note that the root&#8217;s password is asked, and not test&#8217;s). Due to the <code>-P</code> switch, all parameters are directly passed to <code><a href="/docs/linux/man/1-su/">su</a></code>(1). Therefore, the command to execute must be single or double quoted <code>together</code> <code>with</code> <code>its</code> <code>arguments</code> (but in this case there isn&#8217;t anything to quote). </p>
<h2>FILES</h2>
<p> <i>/etc/beesu.conf</i></p>
<dl>
<dt>
<dd> This is the configuration file for beesu. This file allows you to restrict the usage of beesu to run only with a specified list of commands. This may prevent you to run commands that, because of your mistakes, can damage your system.</dl>
<h2>BUGS</h2>
<p> The command name could be any command. Be careful to not type something that could wipe away your system.</p>
<h2>AUTHOR</h2>
<p> Bee &lt;<a rel="nofollow" href="http://honeybeenet.altervista.org">http://honeybeenet.altervista.org</a>&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-su/">su</a></code>(1) </p>
<h2>Index</h2>
