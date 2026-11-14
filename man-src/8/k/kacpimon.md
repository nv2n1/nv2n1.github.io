---
title: "kacpimon(8)"
name: "kacpimon"
section: "8"
letter: "k"
url: "/docs/linux/man/8-kacpimon/"
description: "kacpimon – Kernel ACPI Event Monitor"
---

<p>kacpimon &#8211; Kernel ACPI Event Monitor</p>
<h2>Synopsis</h2>
<p><code>kacpimon</code></p>
<h2>Description</h2>
<p><code>kacpimon</code> is a monitor program that connects to three sources of ACPI events:</p>
<dl>
<dd>1. /proc/acpi/event<br />
 2. netlink<br />
 3. the input layer (/dev/input/event*)</dl>
<p> <code>kacpimon</code> then reports on what it sees while it is connected. </p>
<p> Use <code>kacpimon</code> to make sure your kernel is sending acpi-related events via the three sources mentioned above. </p>
<p> Since both <code><a href="/docs/linux/man/8-acpid/">acpid</a></code>(8) and <code>kacpimon</code> connect to the same sources, be sure to stop <code><a href="/docs/linux/man/8-acpid/">acpid</a></code>(8) before running kacpimon. If you are using <code><a href="/docs/linux/man/7-upstart/">upstart</a></code>(7), use <code><a href="/docs/linux/man/8-initctl/">initctl</a></code>(8) to stop <code><a href="/docs/linux/man/8-acpid/">acpid</a></code>(8). If you are using <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), use <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1) to stop <code><a href="/docs/linux/man/8-acpid/">acpid</a></code>(8). If you aren&#8217;t using either of those, you can try <code><a href="/docs/linux/man/1-killall/">killall</a></code>(1) to stop <code><a href="/docs/linux/man/8-acpid/">acpid</a></code>(8). </p>
<p> Be sure to run <code>kacpimon</code> as root or else it won&#8217;t be able to open /proc/acpi/event or the input layer:</p>
<dl>
<dd>sudo kacpimon</dl>
<p> If you want to pipe the output of <code>kacpimon</code> to a file, be sure to use the &quot;Esc&quot; key to exit rather than Ctrl-C. Using Ctrl-C will cause output to be lost.</p>
<h2>Files</h2>
<dl>
<dt><i>/proc/acpi/event</i></p>
<dd>kernel ACPI event file</p>
<dt><i>/dev/input/event*</i></p>
<dd>input layer event files</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-acpi_listen/">acpi_listen</a></code>(8), <code><a href="/docs/linux/man/8-acpid/">acpid</a></code>(8)</p>
<h2>Author</h2>
<p>Ted Felix &lt;<a rel="nofollow" href="http://www.tedfelix.com">www.tedfelix.com</a>&gt;</p>
<h2>Todo</h2>
<p>&#8211; Make kacpimon something that actually gets installed?</p>
<h2>License</h2>
<p>kacpimon &#8211; Kernel ACPI Event Monitor<br />
 Copyright (C) 2009-2013 Ted Felix (<a rel="nofollow" href="http://www.tedfelix.com">www.tedfelix.com</a>) </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA Or visit <a rel="nofollow" href="http://www.gnu.org">www.gnu.org</a>.</p>
