---
title: "sddm-greeter(1)"
name: "sddm-greeter"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sddm-greeter/"
description: "sddm-greeter – sddm display manager greeter"
---

<h2>NAME</h2>
<p> sddm-greeter &#8211; sddm display manager greeter</p>
<h2>SYNOPSIS</h2>
<p> sddm-greeter [OPTIONS&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> sddm is a display and login manager based on Qt technologies. </p>
<p> Using QtQuick and QML, designers are given the ability to easily create pleasant, modern looking interfaces for sddm. </p>
<p> sddm-greeter is an auxiliary process that displays the greeter, a graphical user interface to perform the authentication and select the session to run. </p>
<p> It is launched by the sddm daemon, end users are not meant to run it.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;theme </code><i>PATH</i></p>
<dd> Specify theme full path.</p>
<dt><code>&#8211;socket </code><i>NAME</i></p>
<dd> Specify the socket used to communicate with sddm daemon.</p>
<dt><code>&#8211;test-mode</code></p>
<dd> Start greeter in test mode.</p>
<dt><code>&#8211;help</code>,<code> -h</code></p>
<dd> Show help message and exit.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/sddm.conf</code></p>
<dd> System configuration file</p>
<dt><code>/usr/share/sddm/themes</code></p>
<dd> Where sddm looks for themes</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sddm/">sddm</a></code>(1), <code><a href="/docs/linux/man/5-sddm-conf/">sddm.conf</a></code>(5) </p>
<p> The full documentation for sddm is available at <i><a rel="nofollow" href="https://github.com/sddm/sddm">https://github.com/sddm/sddm</a></i> </p>
<h2>Index</h2>
