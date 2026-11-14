---
title: "startxfce4(1)"
name: "startxfce4"
section: "1"
letter: "s"
url: "/docs/linux/man/1-startxfce4/"
description: "startxfce4 – initialize an Xfce session"
---

<h2 class="name">NAME</h2>
<p> startxfce4 &#8211; initialize an Xfce session </p>
<h2>SYNOPSIS</h2>
<p> <code>startxfce4</code></p>
<h2>DESCRIPTION</h2>
<p> <code>startxfce4 </code> is a script responsible for starting an Xfce session. It runs <code>xinit </code> passing the file specified in the <code>FILES</code> subsection as an argument. </p>
<p> You may want to modify the default <code>xinitrc</code> file. In order to do that, copy <i>/etc/xdg/xfce4/xinitrc</i> to <i>~/.config/xfce4/xinitrc</i> and modify that file.</p>
<h2>FILES</h2>
<dl>
<dt>~/.config/xfce4/xinitrc</p>
<dd> User configuration file</p>
<dt>/etc/xdg/xfce4/xinitrc</p>
<dd> System wide configuration file</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xfce4-session/">xfce4-session</a></code>(1), <code><a href="/docs/linux/man/1-xinit/">xinit</a></code>(1), <code><a href="/docs/linux/man/1-dbus-launch/">dbus-launch</a></code>(1), <code><a href="/docs/linux/man/1-ssh-agent/">ssh-agent</a></code>(1), <code>file:///usr/share/xfce4/doc/C/xfce4-use.html#xfce4-getting-started</code></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2005 Emanuele Rocca<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>Index</h2>
