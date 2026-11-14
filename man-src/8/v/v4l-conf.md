---
title: "v4l-conf(8)"
name: "v4l-conf"
section: "8"
letter: "v"
url: "/docs/linux/man/8-v4l-conf/"
description: "v4l-conf – configure a video4linux driver"
---

<p>v4l-conf &#8211; configure a video4linux driver</p>
<h2>Synopsis</h2>
<p><code>v4l-conf [ options ]</code></p>
<h2>Description</h2>
<p><code>v4l-conf</code> is a small helper tool. It figures out the video mode and framebuffer base address of the graphics board and configures a video4linux driver like bttv. This is needed for drivers which can DMA the video over PCI directly into the video memory. </p>
<p> Usually it is not required to use v4l-conf manually, <a href="/docs/linux/man/1-xawtv/">xawtv</a>(1) and <a href="/docs/linux/man/1-fbtv/">fbtv</a>(1) run it automatically at startup. It might be useful for trouble-shooting. <code>v4l-conf</code> must be installed suid-root. </p>
<p> <code>v4l-conf</code> knows three ways to get the informations:</p>
<dl>
<dt>
&nbsp;<wbr>*</p>
<dd>Query the X-Server using the XF86 DGA extension. This is the default if the DISPLAY environment variable is set.</p>
<dt>
&nbsp;<wbr>*&nbsp;<wbr></p>
<dd>Query the framebuffer driver. This is the default if DISPLAY is not set.</p>
<dt>
&nbsp;<wbr>*</p>
<dd>Query the console driver. This is used on mklinux only.</dl>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Print a short description of all command line options.</p>
<dt><code>-q</code></p>
<dd>Be quiet.</p>
<dt><code>-d</code> dpy</p>
<dd>Use the X11 display <code>dpy</code> to get the parameters.</p>
<dt><code>-f</code></p>
<dd>Use the framebuffer driver to get the parameters.</p>
<dt><code>-c</code> device</p>
<dd>Set the video4linux device.</p>
<dt><code>-b</code> n</p>
<dd>enforce <code>n</code> bpp color depth. Works for switching between 15/16 and 24/32 bpp.</p>
<dt><code>-s</code> n</p>
<dd>Shift the video display by <code>n</code> bytes.</p>
<dt><code>-a</code> adr</p>
<dd>Set framebuffer address to <code>adr</code>. The value should be specified in hex. This option is allowed for root only. You can&#8217;t overwrite the autodetected value, this switch is only useful if autodetect doesn&#8217;t work because the X-Server lacks DGA support. You can put this into /etc/conf.modules, as &quot;post-install bttv &#8230;&quot; for example.</p>
<dt><code>-p</code> pitch</p>
<dd>Set framebuffer pitch to <code>pitch</code> bytes. The value should be specified in decimal. Allowed for root only.</dl>
<h2>Bugs</h2>
<p>Hope I haven&#8217;t any security flaws in there. If you find one, drop me a note. Mails with patches are preferred :-)</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xawtv/">xawtv</a>(1), <a href="/docs/linux/man/1-fbtv/">fbtv</a>(1)</p>
<h2>Author</h2>
<p>Gerd Knorr &lt;kraxel [at] goldbach.in-berlin.de&gt;</p>
<h2>Copyright</h2>
<p>Copyright (C) 1997-99 Gerd Knorr &lt;kraxel [at] goldbach.in-berlin.de&gt; </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.</p>
