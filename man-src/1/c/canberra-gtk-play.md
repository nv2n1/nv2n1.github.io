---
title: "canberra-gtk-play(1)"
name: "canberra-gtk-play"
section: "1"
letter: "c"
url: "/docs/linux/man/1-canberra-gtk-play/"
description: "canberra-gtk-play – play a sound event"
---

<h2 class="name">NAME</h2>
<p> canberra-gtk-play &#8211; play a sound event </p>
<h2>SYNOPSIS</h2>
<p> <code>canberra-gtk-play</code> [ <i>OPTIONS&#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>canberra-gtk-play</code> command. </p>
<p> <code>canberra-gtk-play</code> plays sound events that are specified by the XDG Sound Theme and Name Specification.</p>
<h2>OPTIONS</h2>
<h3>Application Options</h3>
<dl>
<dt><code>-v</code>,<code> &#8211;version</code></p>
<dd> Display version number and quit</p>
<dt><code>-i</code>,<code> &#8211;id=</code><i>STRING</i></p>
<dd> Event sound identifier</p>
<dt><code>-f</code>,<code> &#8211;file=</code><i>PATH</i></p>
<dd> Play file</p>
<dt><code>-d</code>,<code> &#8211;description=</code><i>STRING</i></p>
<dd> Event sound description</p>
<dt><code>-c</code>,<code> &#8211;cache-control=</code>{ <i>permanent</i>|<i>volatile</i>|<i>never</i> }</p>
<dd> Specify how <code>canberra-gtk-play</code> manages its cache. <i>permanent</i> will cause the sample to be cached permanently, <i>volatile</i> to be cached until the cache needs to be freed.</p>
<dt><code>-l</code>,<code> &#8211;loop=</code><i>INTEGER</i></p>
<dd> Loop how many times (default: 1)</p>
<dt><code>-V</code>,<code> &#8211;volume=</code><i>STRING</i></p>
<dd> A floating point dB value for the sample volume (ex: 0.0)</p>
<dt><code>&#8211;property=</code><i>STRING</i></p>
<dd> An arbitrary property</p>
<dt><code>&#8211;display=</code><i>DISPLAY</i></p>
<dd> X display to use</dl>
<h3>Help Options</h3>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Show help options</p>
<dt><code>&#8211;help-all</code></p>
<dd> Show all help options</p>
<dt><code>&#8211;help-gtk</code></p>
<dd> Show GTK+ Options</dl>
<h3>GTK+ Options</h3>
<dl>
<dt><code>&#8211;class=</code><i>CLASS</i></p>
<dd> Program class as used by the window manager</p>
<dt><code>&#8211;name=</code><i>NAME</i></p>
<dd> Program name as used by the window manager</p>
<dt><code>&#8211;screen=</code><i>SCREEN</i></p>
<dd> X screen to use</p>
<dt><code>&#8211;sync</code></p>
<dd> Make X calls synchronous</p>
<dt><code>&#8211;gtk-module=</code><i>MODULES</i></p>
<dd> Load additional GTK+ modules</p>
<dt><code>&#8211;g-fatal-warnings</code></p>
<dd> Make all warnings fatal</dl>
<h2>AUTHORS</h2>
<p> <code>canberra-gtk-play</code> is Copyright 2008 Lennart Poettering. </p>
<p> This manual page was written by Francois Wendling &lt;frwendling [at] free.fr&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
