---
title: "kodi-send(1)"
name: "kodi-send"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kodi-send/"
description: "xbmc-send – program to send some action to Kodi"
---

<h2>NAME</h2>
<p> xbmc-send &#8211; program to send some action to Kodi</p>
<h2>SYNOPSIS</h2>
<p> xbmc-send [OPTION] <code>&#8211;action</code>=<i>ACTION</i></p>
<h2>DESCRIPTION</h2>
<p> This program is used for sending actions for Kodi. </p>
<p> Example</p>
<dl>
<dt>
<dd> kodi-send <code>&#8211;host</code>=<i>192</i>.168.0.1 <code>&#8211;port</code>=<i>9777</i> <code>&#8211;action=</code>&quot;Quit&quot;</dl>
<p> Options</p>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd> Display help message</p>
<dt><code>&#8211;host</code>=<i>HOST</i></p>
<dd> Choose what HOST to connect to (default=localhost)</p>
<dt><code>&#8211;port</code>=<i>PORT</i></p>
<dd> Choose what PORT to connect to (default=9777)</p>
<dt><code>&#8211;action</code>=<i>ACTION</i></p>
<dd> Sends an action to Kodi, this option can be added multiple times to create a macro. </p>
</dl>
<h2>Index</h2>
