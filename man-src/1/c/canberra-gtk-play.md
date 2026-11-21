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
<dt><code>-v</code>,<code> &#8211;version</code></dt>
<dd> Display version number and quit</dd>
<dt><code>-i</code>,<code> &#8211;id=</code><i>STRING</i></dt>
<dd> Event sound identifier</dd>
<dt><code>-f</code>,<code> &#8211;file=</code><i>PATH</i></dt>
<dd> Play file</dd>
<dt><code>-d</code>,<code> &#8211;description=</code><i>STRING</i></dt>
<dd> Event sound description</dd>
<dt><code>-c</code>,<code> &#8211;cache-control=</code>{ <i>permanent</i>|<i>volatile</i>|<i>never</i> }</dt>
<dd> Specify how <code>canberra-gtk-play</code> manages its cache. <i>permanent</i> will cause the sample to be cached permanently, <i>volatile</i> to be cached until the cache needs to be freed.</dd>
<dt><code>-l</code>,<code> &#8211;loop=</code><i>INTEGER</i></dt>
<dd> Loop how many times (default: 1)</dd>
<dt><code>-V</code>,<code> &#8211;volume=</code><i>STRING</i></dt>
<dd> A floating point dB value for the sample volume (ex: 0.0)</dd>
<dt><code>&#8211;property=</code><i>STRING</i></dt>
<dd> An arbitrary property</dd>
<dt><code>&#8211;display=</code><i>DISPLAY</i></dt>
<dd> X display to use</dd></dl>
<h3>Help Options</h3>
<dl>
<dt><code>-h</code>,<code> &#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Show all help options</dd>
<dt><code>&#8211;help-gtk</code></dt>
<dd> Show GTK+ Options</dd></dl>
<h3>GTK+ Options</h3>
<dl>
<dt><code>&#8211;class=</code><i>CLASS</i></dt>
<dd> Program class as used by the window manager</dd>
<dt><code>&#8211;name=</code><i>NAME</i></dt>
<dd> Program name as used by the window manager</dd>
<dt><code>&#8211;screen=</code><i>SCREEN</i></dt>
<dd> X screen to use</dd>
<dt><code>&#8211;sync</code></dt>
<dd> Make X calls synchronous</dd>
<dt><code>&#8211;gtk-module=</code><i>MODULES</i></dt>
<dd> Load additional GTK+ modules</dd>
<dt><code>&#8211;g-fatal-warnings</code></dt>
<dd> Make all warnings fatal</dd></dl>
<h2>AUTHORS</h2>
<p> <code>canberra-gtk-play</code> is Copyright 2008 Lennart Poettering. </p>
<p> This manual page was written by Francois Wendling &lt;frwendling [at] free.fr&gt; for the Debian GNU/Linux system (but may be used by others). </p>
