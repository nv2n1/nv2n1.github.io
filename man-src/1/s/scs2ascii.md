---
title: "scs2ascii(1)"
name: "scs2ascii"
section: "1"
letter: "s"
url: "/docs/linux/man/1-scs2ascii/"
description: "scs2ascii – convert IBM SCS printer data into ASCII"
---

<h2>NAME</h2>
<p> scs2ascii &#8211; convert IBM SCS printer data into ASCII</p>
<h2>SYNOPSIS</h2>
<p> <code>scs2ascii</code></p>
<h2>DESCRIPTION</h2>
<p> This program handles the conversion from an SCS print stream from an AS/400 printer emulation to something suitable for sending to lpr. It is only intended for use with <code>lp5250d</code>. </p>
<p> When using host print transform with <code>lp5250d</code>, <code>scs2ascii</code> will remove the remaining characters from the SCS print stream to leave only the data intended for the printer.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lp5250d/">lp5250d</a></code>(1), <code><a rel="nofollow" href="http://tn5250.sourceforge.net/">http://tn5250.sourceforge.net/</a></code></p>
<h2>COPYRIGHT</h2>
<p> <code>scs2ascii</code> is copyright 1997 &#8211; 1999 Michael Madore. This manpage is copyright 1999 &#8211; 2008 Carey Evans. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details. </p>
<p> You should have received a copy of the GNU Lesser General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA</p>
<h2>AUTHORS</h2>
<p> <code>scs2ascii</code> was written by Michael Madore. This manual page was written by Carey Evans. </p>
<h2>Index</h2>
