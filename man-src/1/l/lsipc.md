---
title: "lsipc(1)"
name: "lsipc"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lsipc/"
description: "lsipc – show information on IPC facilities currently employed in the system"
---

<h2 class="name">NAME</h2>
<p> lsipc &#8211; show information on IPC facilities currently employed in the system </p>
<h2>SYNOPSIS</h2>
<p> <code>lsipc</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>lsipc</code> shows information on the System V inter-process communication facilities for which the calling process has read access.</p>
<h2>OPTIONS</h2>
<p> <code>-i</code>, <code>&#8211;id</code> <i>id</i></p>
<dl>
<dt>
<dd> Show full details on just the one resource element identified by <i>id</i>. This option needs to be combined with one of the three resource options: <code>-m</code>, <code>-q</code> or <code>-s</code>. It is possible to override the default output format for this option with the <code>&#8211;list</code>, <code>&#8211;raw</code>, <code>&#8211;json</code> or <code>&#8211;export</code> option.</dl>
<p> <code>-g</code>, <code>&#8211;global</code></p>
<dl>
<dt>
<dd> Show system-wide usage and limits of IPC resources. This option may be combined with one of the three resource options: <code>-m</code>, <code>-q</code> or <code>-s</code>. The default is to show information about all resources.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<h3>Resource options</h3>
<p> <code>-m</code>, <code>&#8211;shmems</code></p>
<dl>
<dt>
<dd> Write information about active shared memory segments.</dl>
<p> <code>-q</code>, <code>&#8211;queues</code></p>
<dl>
<dt>
<dd> Write information about active message queues.</dl>
<p> <code>-s</code>, <code>&#8211;semaphores</code></p>
<dl>
<dt>
<dd> Write information about active semaphore sets.</dl>
<h3>Output formatting</h3>
<p> <code>-c</code>, <code>&#8211;creator</code></p>
<dl>
<dt>
<dd> Show creator and owner.</dl>
<p> <code>-e</code>, <code>&#8211;export</code></p>
<dl>
<dt>
<dd> Produce output in the form of key=&quot;value&quot; pairs. All potentially unsafe value characters are hex-escaped (
