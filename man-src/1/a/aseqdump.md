---
title: "aseqdump(1)"
name: "aseqdump"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aseqdump/"
description: "aseqdump – show the events received at an ALSA sequencer port"
---

<h2 class="name">NAME</h2>
<p> aseqdump &#8211; show the events received at an ALSA sequencer port</p>
<h2>SYNOPSIS</h2>
<p> <code>aseqdump</code> [<i>-p client:port,&#8230;</i>] </p>
<h2>DESCRIPTION</h2>
<p> <code>aseqdump</code> is a command-line utility that prints the sequencer events it receives as text. </p>
<p> To stop receiving, press Ctrl+C. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h,&#8211;help</i></p>
<dd> Prints a list of options. </p>
<dt><i>-V,&#8211;version</i></p>
<dd> Prints the current version. </p>
<dt><i>-l,&#8211;list</i></p>
<dd> Prints a list of possible input ports. </p>
<dt><i>-p,&#8211;port=client:port,&#8230;</i></p>
<dd> Sets the sequencer port(s) from which events are received. </p>
<p> A client can be specified by its number, its name, or a prefix of its name. A port is specified by its number; for port 0 of a client, the &quot;:0&quot; part of the port specification can be omitted. </p>
</dl>
<h2>AUTHOR</h2>
<p> Clemens Ladisch &lt;clemens [at] ladisch.de&gt; </p>
<h2>Index</h2>
