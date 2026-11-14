---
title: "xkbbell(1)"
name: "xkbbell"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xkbbell/"
description: "xkbbell – XKB extension user utility"
---

<h2 class="name">NAME</h2>
<p> xkbbell &#8211; XKB extension user utility </p>
<h2>SYNOPSIS</h2>
<p> <code>xkbbell</code> [-display &lt;dpy&gt;] [-synch] [-dev &lt;id&gt;] [-force] [-nobeep] [-bf &lt;id&gt;] [-kf &lt;id&gt;] [-v &lt;volume&gt;] [-w &lt;id&gt;] [-help|-version]</p>
<h2>DESCRIPTION</h2>
<p> user utility</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-display &lt;dpy&gt;</code></p>
<dd> specifies which display to use</p>
<dt><code>-synch</code></p>
<dd> turns on synchronization</dl>
<dl>
<dt><code>-dev &lt;id&gt;</code></p>
<dd> specifies which device to use</dl>
<dl>
<dt><code>-force</code></p>
<dd> force audible bell</dl>
<dl>
<dt><code>-nobeep</code></p>
<dd> suppress server bell, event only</dl>
<dl>
<dt><code>-bf &lt;id&gt;</code></p>
<dd> specifies which bell feedback to use</dl>
<dl>
<dt><code>-kf &lt;id&gt;</code></p>
<dd> specifies which keyboard feedback to use</dl>
<dl>
<dt><code>-v &lt;volume&gt;</code></p>
<dd> specifies which volume to use</dl>
<dl>
<dt><code>-w &lt;id&gt;</code></p>
<dd> specifies which window to use</dl>
<dl>
<dt><code>-help</code></p>
<dd> print list of options and exit</dl>
<dl>
<dt><code>-version</code></p>
<dd> print program version and exit</dl>
<p> If neither device nor feedback are specified, xkbbell uses the default values for the core keyboard device. </p>
<h2>Index</h2>
