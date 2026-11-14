---
title: "byzanz-record(1)"
name: "byzanz-record"
section: "1"
letter: "b"
url: "/docs/linux/man/1-byzanz-record/"
description: "byzanz-record – record your desktop session to an animated GIF"
---

<h2>NAME</h2>
<p> byzanz-record &#8211; record your desktop session to an animated GIF</p>
<h2>SYNOPSIS</h2>
<p> <code>byzanz-record</code> [<i>options</i>]<i> filename.gif</i></p>
<h2>DESCRIPTION</h2>
<p> Byzanz records your desktop session to an animated GIF. You can record your entire screen, a single window, or an arbitrary region. <code>byzanz-record</code> allows you to make recordings from the command line. Graphical users may want to use the panel applet instead.</p>
<h2>OPTIONS</h2>
<h3>Application Options:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;duration</code>=<i>SECS</i></p>
<dd> Duration of animation (default: 10 seconds)</p>
<dt><code>&#8211;delay</code>=<i>SECS</i></p>
<dd> Delay before start (default: 1 second)</p>
<dt><code>-l</code>, <code>&#8211;loop</code></p>
<dd> Let the animation loop</p>
<dt><code>-c</code>, <code>&#8211;cursor</code></p>
<dd> Record mouse cursor</p>
<dt><code>-x</code>, <code>&#8211;x</code>=<i>PIXEL</i></p>
<dd> X coordinate of rectangle to record</p>
<dt><code>-y</code>, <code>&#8211;y</code>=<i>PIXEL</i></p>
<dd> Y coordinate of rectangle to record</p>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>PIXEL</i></p>
<dd> Width of recording rectangle</p>
<dt><code>-h</code>, <code>&#8211;height</code>=<i>PIXEL</i></p>
<dd> Height of recording rectangle</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Be verbose</p>
<dt><code>&#8211;display</code>=<i>DISPLAY</i></p>
<dd> X display to use</dl>
<h3>Help Options:</h3>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd> Show help options</p>
<dt><code>&#8211;help-gtk</code></p>
<dd> Show GTK+ Options</p>
<dt><code>&#8211;help-all</code></p>
<dd> Show all help options</dl>
<h2>AUTHOR</h2>
<p> byzanz was written by Benjamin Otte &lt;otte [at] gnome.org&gt;. </p>
<p> This manual page was written by Josh Triplett &lt;josh [at] freedesktop.org&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
