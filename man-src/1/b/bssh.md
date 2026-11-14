---
title: "bssh(1)"
name: "bssh"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bssh/"
description: "bssh/bvnc/bshell – Browse for SSH/VNC servers on the local network"
---

<h2>NAME</h2>
<p> bssh/bvnc/bshell &#8211; Browse for SSH/VNC servers on the local network</p>
<h2>SYNOPSIS</h2>
<p> <code>bssh </p>
<p> bvnc </p>
<p> bshell </code></p>
<h2>DESCRIPTION</h2>
<p> bssh/bvnc/bshell browses for SSH/VNC servers on the local network, shows them in a GUI for the user to select one and finally calls ssh/vncviewer after a selection was made. </p>
<p> If the binary is called as bssh only ssh servers will be shown. If the binary is called as bvnc only VNC servers will be shown. If the binary is called as bshell both VNC and SSH servers are shown.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s | &#8211;ssh</code></p>
<dd> Browse for SSH servers (and only SSH servers) regardless under which name the binary is called.</p>
<dt><code>-v | &#8211;vnc</code></p>
<dd> Browse for VNC servers (and only VNC servers) regardless under which name the binary is called.</p>
<dt><code>-S | &#8211;shell</code></p>
<dd> Browse for both VNC and SSH servers regardless under which name the binary is called.</p>
<dt><code>-d | &#8211;domain=</code> <i>DOMAIN</i></p>
<dd> Browse in the specified domain. If omitted bssh/bvnc/bshell will browse in the default browsing domain (usually .local)</p>
<dt><code>-h | &#8211;help</code></p>
<dd> Show help.</dl>
<h2>AUTHORS</h2>
<p> The Avahi Developers &lt;avahi (at) lists (dot) freedesktop (dot) org&gt;; Avahi is available from <code><a rel="nofollow" href="http://avahi.org/">http://avahi.org/</a></code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-avahi-browse/">avahi-browse</a>(1)</code>, <code><a href="/docs/linux/man/1-ssh/">ssh</a>(1)</code>, <code><a href="/docs/linux/man/1-vncviewer/">vncviewer</a>(1)</code></p>
<h2>COMMENTS</h2>
<p> This man page was written using <code><a href="/docs/linux/man/1-xml2man/">xml2man</a>(1)</code> by Oliver Kurth. </p>
<h2>Index</h2>
