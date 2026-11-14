---
title: "icewm(1)"
name: "icewm"
section: "1"
letter: "i"
url: "/docs/linux/man/1-icewm/"
description: "icewm – lightweight X11 window manager"
---

<h2>NAME</h2>
<p> icewm &#8211; lightweight X11 window manager </p>
<h2>DESCRIPTION</h2>
<p> <i>IceWM</i> is lightweight X11 window manager. The goal of IceWM is to provide a small, fast and familiar window manager for the X11 window system. Compatibility with the window manager is desired and will be implemented where appropriate. </p>
<p> It was originally designed to emulate the look of Motif, OS/2 Warp 4, OS/2 Warp 3 and Windows 95. Since it has a theming engine (hint: <a rel="nofollow" href="http://www.icewm.org/)">http://www.icewm.org/)</a> others styles are possible. It also tries to combine the feel of the above systems whenever it is compatible. </p>
<p> Generally, it tries to make all functions available both by keyboard and by mouse (this is not currently possible when using mouse focus). Extreme configurability similar to fvwm and many other window managers is NOT the goal. However IceWM configurability is very good throught its various <i>preferences</i> files. </p>
<p> IceWM consists of several parts: </p>
<p> <code>icewm </code> &#8211; the actual window manager binary. This is the one you need to get window decorations. </p>
<p> <code>icewmbg </code> &#8211; the background setting applications. It can assign plain background color or images in different formats to the X background, shared or separated for different workspaces. This program should be started before IceWM startup. </p>
<p> <code>icewmtray </code> &#8211; catches the Docklet objects installed by various applications like PSI. </p>
<p> <code>icewm-session </code> &#8211; runs all of the above when needed. Implements basic session management. </p>
<p> <code>icesh</code> &#8211; could be used to manage IceWM internals from command line. </p>
<p> <code>icewmhint</code> &#8211; used internaly. </p>
<p> <code>icesound</code> &#8211; plays audio files on GUI events raised by IceWM. </p>
<h2>OPTIONS</h2>
<p> For most of the parts use option</p>
<dl>
<dt>
<dd> <code>-h, &#8211;help</code> to see all of the options.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <i>ICEWM_PRIVCFG=PATH </i></p>
<dl>
<dt>
<dd> Directory to use for user private configuration files, &quot;$HOME/.icewm/&quot; by default.</dl>
<p> <i>DISPLAY=NAME</i></p>
<dl>
<dt>
<dd> Name of the X server to use, depends on Xlib by default. See <a href="/docs/linux/man/1-x/">X</a>(1).</dl>
<p> <i>MAIL=URL</i></p>
<dl>
<dt>
<dd> Location of your mailbox. If the schema is omitted the local &quot;file&quot; schema is assumed.</dl>
<h2>FILES</h2>
<p> IceWM looks for its configuration files in the following directories, in the following order: </p>
<p> <i>$(HOME)/.icewm/</i></p>
<dl>
<dt>
<dd> User-specific configurations</dl>
<p> <i>/etc/X11/icewm/</i></p>
<dl>
<dt>
<dd> System-wide customized defaults</dl>
<p> <i>/usr/local/share/icewm/</i></p>
<dl>
<dt>
<dd> Default installation settings</dl>
<p> <code>Configuration files</code> </p>
<p> <i>keys</i></p>
<dl>
<dt>
<dd> global keybindings to launch applications (not window manager related)</dl>
<p> <i>menu</i></p>
<dl>
<dt>
<dd> menu of startable applications; usually customized by the user</dl>
<p> <i>preferences</i></p>
<dl>
<dt>
<dd> general settings &#8211; paths, colors, fonts&#8230;</dl>
<p> <i>prefoverride</i></p>
<dl>
<dt>
<dd> settings that should override the themes</dl>
<p> <i>programs</i></p>
<dl>
<dt>
<dd> automatically generated menu of startable applications (this should be used for wmconfig, menu or similar packages, perhaps as a part of the login or X startup sequence)</dl>
<p> <i>theme</i></p>
<dl>
<dt>
<dd> currently selected theme</dl>
<p> <i>toolbar</i></p>
<dl>
<dt>
<dd> quick launch application icons on the taskbar</dl>
<p> <i>winoptions</i></p>
<dl>
<dt>
<dd> application window options</dl>
<p> <i>startup</i></p>
<dl>
<dt>
<dd> commands to execute on IceWM startup</dl>
<p> <i>shutdown</i></p>
<dl>
<dt>
<dd> commands to execute on IceWM shutdown</dl>
<p> <code>Configuration directories</code> </p>
<p> <i>icons</i></p>
<dl>
<dt>
<dd> icons used for applications (usually XPM files *_16x16.xpm and *_32x32.xpm)</dl>
<p> <i>ledclock</i></p>
<dl>
<dt>
<dd> pictures of digits for clocks displayed in taskbar</dl>
<p> <i>mailbox</i></p>
<dl>
<dt>
<dd> icons used for different states of mailbox</dl>
<p> <i>taskbar</i></p>
<dl>
<dt>
<dd> pictures to customize look of the taskbar</dl>
<p> <i>themes</i></p>
<dl>
<dt>
<dd> directory to store themes</dl>
<h2>EXAMPLES</h2>
<p> Examples of above configuration files you can find in default instalation path or in system-wide customizable defaults.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-xinit/">xinit</a></i>(1), <i><a href="/docs/linux/man/1-x/">X</a></i>(1), </p>
<p> <i><a rel="nofollow" href="http://www.icewm.org/manual/">http://www.icewm.org/manual/</a></i> </p>
<p> <i><a rel="nofollow" href="http://www.icewm.org/FAQ/">http://www.icewm.org/FAQ/</a></i> </p>
<p> <i><a rel="nofollow" href="http://www.icewm.org/themes/">http://www.icewm.org/themes/</a></i></p>
<h2>AUTHORS</h2>
<p> The original version of <i>IceWM</i> was designed and implemented in 1997 by Marko Macek, in year 2001 it was maintained by Mathias Hasselmann then again Marko Macek took over. </p>
<p> IceWM man page written by Adam Pribyl, covex [at] ahoj.fsik.cvut.cz, 2005</p>
<h2>BUG REPORTS</h2>
<p> If you find a bug in <i>IceWM</i> please use bug reporting system on <code><a rel="nofollow" href="http://sourceforge.net/projects/icewm/">http://sourceforge.net/projects/icewm/</a></code> to report it.</p>
<h2>COPYING</h2>
<p> <i>IceWM</i> is released under GNU Library General Public License. </p>
<p> This library is free software; you can redistribute it and/or modify it under the terms of the GNU Library General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Library General Public License for more details. </p>
<p> You should have received a copy of the GNU Library General Public License along with this library; if not, write to the Free Software Foundation, Inc., 59 Temple Place &#8211; Suite 330, Boston, MA 02111-1307 USA. </p>
<h2>Index</h2>
