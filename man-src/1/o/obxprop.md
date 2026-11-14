---
title: "obxprop(1)"
name: "obxprop"
section: "1"
letter: "o"
url: "/docs/linux/man/1-obxprop/"
description: "openbox — A minimalistic, highly configurable, next generation window manager with extensive standards support."
---

<h2>NAME</h2>
<p> openbox &#8212; A minimalistic, highly configurable, next generation window manager with extensive standards support.</p>
<h2>SYNOPSIS</h2>
<p> <code>openbox</code> [&#8211;help] [&#8211;display DISPLAY] [&#8211;id ID] [&#8211;root] [&#8211;] [PROPERTY &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> obxprop is a tool for displaying the properties on an x window. </p>
<p> This tool has a similar functionality to <code>xprop</code>, but obxprop allows you to see UTF-8 strings as text. </p>
<p> You may use the <code>&#8211;id</code> option to specify a window identifier, otherwise obxprop will allow you to select a window by clicking on it. </p>
<p> Primarily, this tool exists for Openbox users to see the value of the _OB_APP_NAME, _OB_APP_CLASS, _OB_APP_ROLE, and _OB_APP_TYPE properties, which Openbox uses for matching windows against user-defined application rules.</p>
<h2>OPTIONS</h2>
<p> These are the possible options that <code>openbox</code> accepts:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Show a summary of the options available.</p>
<dt><code>&#8211;display</code> DISPLAY</p>
<dd> Specify the X display to use.</p>
<dt><code>&#8211;id</code> ID</p>
<dd> Specify the window identifier for the window whose properties will be displayed.</dl>
<p> Similar to <code>xprop</code>, you may pass one or more property names to have <code>openbox</code> limit its output to only the properties requested.</p>
<h2>SEE ALSO</h2>
<p> openbox (1), <a href="/docs/linux/man/1-openbox-session/">openbox-session</a>(1), <a href="/docs/linux/man/1-openbox-gnome-session/">openbox-gnome-session</a>(1), <a href="/docs/linux/man/1-openbox-kde-session/">openbox-kde-session</a>(1). </p>
<p> Please report bugs to: <code><a rel="nofollow" href="http://bugzilla.icculus.org/">http://bugzilla.icculus.org/</a> </code> </p>
<h2>Index</h2>
