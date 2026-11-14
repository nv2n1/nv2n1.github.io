---
title: "vncconfig(1)"
name: "vncconfig"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vncconfig/"
description: "vncconfig – configure and control a VNC server"
---

<h2>NAME</h2>
<p> vncconfig &#8211; configure and control a VNC server</p>
<h2>SYNOPSIS</h2>
<p> <code>vncconfig</code> [<i>parameters</i>]<br />
 <code>vncconfig</code> [<i>parameters</i>] <code>-connect</code> <i>host</i>[:<i>port</i>]<br />
 <code>vncconfig</code> [<i>parameters</i>] <code>-disconnect</code><br />
 <code>vncconfig</code> [<i>parameters</i>] [<code>-set</code>] <i>Xvnc-param</i>=<i>value</i> &#8230;<br />
 <code>vncconfig</code> [<i>parameters</i>] <code>-list</code><br />
 <code>vncconfig</code> [<i>parameters</i>] <code>-get</code> <i>Xvnc-param</i><br />
 <code>vncconfig</code> [<i>parameters</i>] <code>-desc</code> <i>Xvnc-param</i></p>
<h2>DESCRIPTION</h2>
<p> <code>vncconfig</code> is used to configure and control a running instance of Xvnc, or any other X server with the VNC extension. Note that it cannot be used to control VNC servers prior to version 4. </p>
<p> When run with no options, it runs as a kind of &quot;helper&quot; application for Xvnc. Its main purpose when run in this mode is to query the user how new connections should be handled (provided this feature is enabled). The <code>-nowin</code> flag can be used if you always want the query support but don&#8217;t wish to clutter the desktop with the settings window &#8211; alternatively the <code>-iconic</code> option can be used to make it iconified by default. </p>
<p> When run in any other mode, <code>vncconfig</code> is a one-shot program used to configure or control Xvnc as appropriate. It can be used to tell Xvnc to connect or disconnect from listening viewers, and to set and retrieve Xvnc&#8217;s parameters. </p>
<p> Note that the DISPLAY environment variable or the <code>-display</code> option must be set as appropriate to control Xvnc. If you run it on an ordinary X server (or on a version 3 Xvnc) you will get an error message saying that there is no VNC extension. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-connect </code><i>host</i>[:<i>port</i>]</p>
<dd> Tells an Xvnc server to make a &quot;reverse&quot; connection to a listening VNC viewer (normally connections are made the other way round &#8211; the viewer connects to the server). <i>host</i> is the host where the listening viewer is running. If it&#8217;s not listening on the default port of 5500, you can specify <i>host:port</i> instead.</p>
<dt><code>-disconnect</code></p>
<dd> This causes Xvnc to disconnect from all viewers so that the VNC desktop is not displayed anywhere.</p>
<dt>[<code>-set</code>] <i>Xvnc-param</i>=<i>value</i></p>
<dd> Sets an Xvnc parameter to the given value. Note that some of Xvnc&#8217;s parameters are read only once at startup so that changing them in this way may not have any effect.</p>
<dt><code>-list</code></p>
<dd> Lists all the parameters supported by Xvnc.</p>
<dt><code>-get </code><i>Xvnc-param</i></p>
<dd> Prints the current value of the given Xvnc parameter.</p>
<dt><code>-desc </code><i>Xvnc-param</i></p>
<dd> Prints a short description of the given Xvnc parameter. </p>
</dl>
<h2>PARAMETERS</h2>
<p> <code>vncconfig</code> also has parameters of its own which can be set on the command line. These should not be confused with Xvnc&#8217;s parameters which are manipulated with the <code>-set</code>, <code>-get</code>, <code>-list</code> and <code>-desc</code> options. </p>
<p> Parameters can be turned on with &#8211;<i>param</i> or off with &#8211;<i>param</i>=0. Parameters which take a value can be specified as &#8211;<i>param</i> <i>value</i>. Other valid forms are <i>param</i><code>=</code><i>value</i> &#8211;<i>param</i>=<i>value</i> &#8212;<i>param</i>=<i>value</i>. Parameter names are case-insensitive. </p>
<dl>
<dt><code>-display </code><i>Xdisplay</i></p>
<dd> Specifies the Xvnc server to control.</p>
<dt><code>-nowin</code></p>
<dd> When run as a &quot;helper&quot; app, don&#8217;t put up a window.</p>
<dt><code>-iconic</code></p>
<dd> When run as a &quot;helper&quot; app, make the window iconified at startup. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-vncpasswd/">vncpasswd</a></code>(1), <code><a href="/docs/linux/man/1-vncviewer/">vncviewer</a></code>(1), <code><a href="/docs/linux/man/1-vncserver/">vncserver</a></code>(1), <code><a href="/docs/linux/man/1-xvnc/">Xvnc</a></code>(1)<br />
 <a rel="nofollow" href="http://www.tigervnc.org">http://www.tigervnc.org</a> </p>
<h2>AUTHOR</h2>
<p> Tristan Richardson, RealVNC Ltd. and others. </p>
<p> VNC was originally developed by the RealVNC team while at Olivetti Research Ltd / AT&amp;T Laboratories Cambridge. TightVNC additions were implemented by Constantin Kaplinsky. Many other people have since participated in development, testing and support. This manual is part of the TigerVNC software suite. </p>
<h2>Index</h2>
