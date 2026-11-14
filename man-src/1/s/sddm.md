---
title: "sddm(1)"
name: "sddm"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sddm/"
description: "sddm – the simple desktop display manager"
---

<h2>NAME</h2>
<p> sddm &#8211; the simple desktop display manager</p>
<h2>SYNOPSIS</h2>
<p> sddm [OPTIONS&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> sddm is a display and login manager based on Qt technologies. </p>
<p> Using QtQuick and QML, designers are given the ability to easily create pleasant, modern looking interfaces for sddm. </p>
<p> sddm runs the greeter as a system user named <code>sddm</code> whose home directory needs to be set to <code>/var/lib/sddm</code>. </p>
<p> If pam and systemd are available, the greeter will go through logind, which will give it access to drm devices. </p>
<p> Distributions without pam and systemd will need to put the <code>sddm</code> user into the <code>video</code> group, otherwise errors regarding GL and drm devices might be experienced.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;test-mode</code></p>
<dd> Start daemon in test mode.</p>
<dt><code>&#8211;help</code>,<code> -h</code></p>
<dd> Show help message and exit.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/sddm.conf</code></p>
<dd> System configuration file</p>
<dt><code>/usr/share/sddm/themes</code></p>
<dd> Where sddm looks for themes</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-sddm-conf/">sddm.conf</a></code>(5) </p>
<p> The full documentation for sddm is available at <i><a rel="nofollow" href="https://github.com/sddm/sddm">https://github.com/sddm/sddm</a></i> </p>
<h2>Index</h2>
