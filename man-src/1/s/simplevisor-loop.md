---

title: "simplevisor-loop(1)"
name: "simplevisor-loop"
section: "1"
letter: "s"
url: "/docs/linux/man/1-simplevisor-loop/"
description: "simplevisor-loop – execute the given command in a loop"
---

<p> simplevisor-loop &#8211; execute the given command in a loop </p>
<h2>SYNOPSIS</h2>
<p> <code>simplevisor-loop</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <font SIZE="-1">COMMAND&#8230;</font></p>
<h2>DESCRIPTION</h2>
<p> By default, this program executes the given command in a loop, forever, until the command fails (i.e. return a non zero exit status). </p>
<p> It can optionally sleep between consecutive executions of the command (see the <code>&#8211;sleep</code> option) and stop after a given number of executions (see the <code>&#8211;count</code> option).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;count</code>, <code>-c</code> <i></i><font SIZE="-1"><i>INTEGER</i></font><i></i></dt>
<dd> stop after having executed the command the given number of times</dd>
<dt><code>&#8211;daemon</code></dt>
<dd> detach <code>simplevisor-loop</code> so that it becomes a daemon running in the background; debug, warning and error messages get sent to syslog</dd>
<dt><code>&#8211;debug</code>, <code>-d</code></dt>
<dd> show debugging information</dd>
<dt><code>&#8211;help</code>, <code>-h</code>, <code>-?</code></dt>
<dd> show some help</dd>
<dt><code>&#8211;manual</code>, <code>-m</code></dt>
<dd> show this manual</dd>
<dt><code>&#8211;pidfile</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></dt>
<dd> use this pid file</dd>
<dt><code>&#8211;quit</code></dt>
<dd> tell another instance of <code>simplevisor-loop</code> (identified by its pid file, as specified by the <code>&#8211;pidfile</code> option) to quit</dd>
<dt><code>&#8211;sleep</code>, <code>-s</code> <i></i><font SIZE="-1"><i>NUMBER</i></font><i></i></dt>
<dd> sleep during the given number of seconds between executions of the command; can be fractional</dd>
<dt><code>&#8211;status</code></dt>
<dd> get the status of another instance of <code>simplevisor-loop</code> (identified by its pid file, as specified by the <code>&#8211;pidfile</code> option); the exit code will be zero if the instance is alive and non-zero otherwise</dd></dl>
<h2>AUTHOR</h2>
<p> Lionel Cons &lt;<a rel="nofollow" href="http://cern.ch/lionel.cons">http://cern.ch/lionel.cons</a>&gt; </p>
<p> Copyright (C) <font SIZE="-1">CERN 2012-2016</font> </p>
