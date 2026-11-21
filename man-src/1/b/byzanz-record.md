---

title: "byzanz-record(1)"
name: "byzanz-record"
section: "1"
letter: "b"
url: "/docs/linux/man/1-byzanz-record/"
description: "byzanz-record – record your desktop session to an animated GIF"
---

<p> byzanz-record &#8211; record your desktop session to an animated GIF</p>
<h2>SYNOPSIS</h2>
<p> <code>byzanz-record</code> [<i>options</i>]<i> filename.gif</i></p>
<h2>DESCRIPTION</h2>
<p> Byzanz records your desktop session to an animated GIF. You can record your entire screen, a single window, or an arbitrary region. <code>byzanz-record</code> allows you to make recordings from the command line. Graphical users may want to use the panel applet instead.</p>
<h2>OPTIONS</h2>
<h3>Application Options:</h3>
<dl>
<dt><code>-d</code>, <code>&#8211;duration</code>=<i>SECS</i></dt>
<dd> Duration of animation (default: 10 seconds)</dd>
<dt><code>&#8211;delay</code>=<i>SECS</i></dt>
<dd> Delay before start (default: 1 second)</dd>
<dt><code>-l</code>, <code>&#8211;loop</code></dt>
<dd> Let the animation loop</dd>
<dt><code>-c</code>, <code>&#8211;cursor</code></dt>
<dd> Record mouse cursor</dd>
<dt><code>-x</code>, <code>&#8211;x</code>=<i>PIXEL</i></dt>
<dd> X coordinate of rectangle to record</dd>
<dt><code>-y</code>, <code>&#8211;y</code>=<i>PIXEL</i></dt>
<dd> Y coordinate of rectangle to record</dd>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>PIXEL</i></dt>
<dd> Width of recording rectangle</dd>
<dt><code>-h</code>, <code>&#8211;height</code>=<i>PIXEL</i></dt>
<dd> Height of recording rectangle</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Be verbose</dd>
<dt><code>&#8211;display</code>=<i>DISPLAY</i></dt>
<dd> X display to use</dd></dl>
<h3>Help Options:</h3>
<dl>
<dt>-?, <code>&#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>&#8211;help-gtk</code></dt>
<dd> Show GTK+ Options</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Show all help options</dd></dl>
<h2>AUTHOR</h2>
<p> byzanz was written by Benjamin Otte &lt;otte [at] gnome.org&gt;. </p>
<p> This manual page was written by Josh Triplett &lt;josh [at] freedesktop.org&gt;, for the Debian project (but may be used by others). </p>
