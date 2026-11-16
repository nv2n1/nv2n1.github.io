---
title: "icecc-scheduler(1)"
name: "icecc-scheduler"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icecc-scheduler/"
description: "scheduler – Icecream scheduler"
---

<h2>NAME</h2>
<p> scheduler &#8211; Icecream scheduler</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>scheduler</code> [<code>-n</code> | <code>&#8211;netname</code><i> name</i>] [<code>-p</code> | <code>&#8211;port</code><i> port</i>] [<code>-h</code> | <code>&#8211;help</code>] [<code>-l</code> | <code>&#8211;log-file</code><i> file</i>] [<code>-d</code> | <code>&#8211;daemonize</code>] [<code>-r</code> | <code>&#8211;allow-run-as-user</code>] [-v&nbsp;<wbr>[v&nbsp;<wbr>[v]]] </dt>
</dl>
<h2>DESCRIPTION</h2>
<dd>The Icecream scheduler is the central instance of an Icecream compile network. It distributes the compile jobs and provides the data for the monitors. </dd>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;netname</code> <i>netname</i></dt>
<dd> The name of the Icecream network the scheduler controls. </dd>
<dt><code>-p</code>, <code>&#8211;port</code> <i>port</i></dt>
<dd> IP port the scheduler uses. </dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print help message. </dd>
<dt><code>-l</code>, <code>&#8211;log-file</code> <i>logfile</i></dt>
<dd> Name of file where log output is written to. </dd>
<dt><code>-d</code>, <code>&#8211;daemonize</code></dt>
<dd> Detach daemon from shell. </dd>
<dt><code>-v</code>, <code>-vv</code>, <code>-vvv</code></dt>
<dd> Control verbosity of daemon. The more v the more verbose. </dd>
<dt><code>-r</code>, <code>&#8211;allow-run-as-user</code></dt>
<dd> Force running the scheduler with user rights. Usually you will need to run the scheduler with root rights. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> icecream, scheduler, iceccd, icemon </p>
<h2>AUTHOR</h2>
<p> Cornelius Schumacher </p>
<h2>Index</h2>
