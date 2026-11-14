---
title: "vncpasswd(1)"
name: "vncpasswd"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vncpasswd/"
description: "vncpasswd – change the VNC password"
---

<h2>NAME</h2>
<p> vncpasswd &#8211; change the VNC password</p>
<h2>SYNOPSIS</h2>
<p> <code>vncpasswd</code> [<i>passwd-file</i>]<br />
 <code>vncpasswd</code> -f</p>
<h2>DESCRIPTION</h2>
<p> <code>vncpasswd</code> allows you to set the password used to access VNC desktops. Its default behavior is to prompt for a VNC password and then store an obfuscated version of this password to <i>passwd-file</i> (or to $HOME/.vnc/passwd if no password file is specified.) The <code>vncserver</code> script runs <code>vncpasswd</code> the first time you start a VNC desktop, and it invokes <code>Xvnc</code> with the appropriate <code>-rfbauth</code> option. <code>vncviewer</code> can also be given a password file to use via the <code>-passwd</code> option. </p>
<p> The password must be at least six characters long (unless the <code>-f</code> command-line option is used&#8211; see below), and only the first eight characters are significant. Note that the stored password is <code>not</code> encrypted securely &#8211; anyone who has access to this file can trivially find out the plain-text password, so <code>vncpasswd</code> always sets appropriate permissions (read and write only by the owner.) However, when accessing a VNC desktop, a challenge-response mechanism is used over the wire making it hard for anyone to crack the password simply by snooping on the network. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code></p>
<dd> Filter mode. Read a plain-text password from stdin and write an encrypted version to stdout. Note that in filter mode, short or even empty passwords will be silently accepted. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>$HOME/.vnc/passwd</p>
<dd> Default location of the VNC password file. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-vncviewer/">vncviewer</a></code>(1), <code><a href="/docs/linux/man/1-vncserver/">vncserver</a></code>(1), <code><a href="/docs/linux/man/1-xvnc/">Xvnc</a></code>(1) <code><a href="/docs/linux/man/1-vncconfig/">vncconfig</a></code>(1),<br />
 <a rel="nofollow" href="http://www.tigervnc.org">http://www.tigervnc.org</a> </p>
<h2>AUTHORS</h2>
<p> Tristan Richardson, RealVNC Ltd., Antoine Martin, D. R. Commander and others. </p>
<p> VNC was originally developed by the RealVNC team while at Olivetti Research Ltd / AT&amp;T Laboratories Cambridge. TightVNC additions were implemented by Constantin Kaplinsky. Many other people have since participated in development, testing and support. This manual is part of the TigerVNC software suite. </p>
<h2>Index</h2>
