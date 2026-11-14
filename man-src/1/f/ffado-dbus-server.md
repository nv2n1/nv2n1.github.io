---
title: "ffado-dbus-server(1)"
name: "ffado-dbus-server"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffado-dbus-server/"
description: "dbus – expose the mixer features of connected FFADO devices through DBus"
---

<h2>NAME</h2>
<p> dbus &#8211; expose the mixer features of connected FFADO devices through DBus</p>
<h2>SYNOPSIS</h2>
<p> <code>ffado-dbus-server [OPTION&#8230;]</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ffado-dbus-server</code> exposes the mixer and control features of connected FFADO devices though a DBUS interface. The extent of support for controls on a given device depends entirely on the status of that device&#8217;s FFADO driver. </p>
<p> By using DBus it is possible for control applications to be developed independently of FFADO. The DBus interface provided by <code>ffado-dbus-server</code> is used by <code>ffado-mixer</code> but there is no reason other implementations could not be written.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?, &#8211;help, &#8211;usage</code></p>
<dd> Show brief usage information and exit</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print the program version and exit</p>
<dt><code>-q, -q, &#8211;quiet, &#8211;silent</code></p>
<dd> Don&#8217;t produce any output</p>
<dt><code>-n, &#8211;node=ID</code></p>
<dd> Only expose the mixer of a device on a specific node with an ID of <i>ID</i></p>
<dt><code>-p, &#8211;port=NUM</code></p>
<dd> Specify use of IEEE1394 port <i>NUM</i></p>
<dt><code>-v, &#8211;verbose=LEVEL</code></p>
<dd> Produce verbose output. The higher the <i>LEVEL</i> the more verbose the messages. The some verbose messages may only be available of FFADO was compiled with debugging enabled.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffado-mixer/">ffado-mixer</a></code>(1) </p>
<h2>Index</h2>
