---
title: "ctdbd_wrapper(1)"
name: "ctdbd_wrapper"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ctdbd_wrapper/"
description: "ctdbd_wrapper – Wrapper for ctdbd"
---

<h2 class="name">NAME</h2>
<p> ctdbd_wrapper &#8211; Wrapper for ctdbd </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ctdbd_wrapper</code> {<i>PIDFILE</i>} {start | stop}</dl>
<h2>DESCRIPTION</h2>
<dd>ctdbd_wrapper is used to start or stop the main CTDB daemon. </p>
<p> <i>PIDFILE</i> specifies the location of the file containing the PID of the main CTDB daemon. </p>
<p> ctdbd_wrapper constructs command-line options for ctdbd from configuration variables specified in <code><a href="/docs/linux/man/5-ctdbd-conf/">ctdbd.conf</a></code>(5). </p>
<p> See <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7) for an overview of CTDB.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ctdbd/">ctdbd</a></code>(1), <code><a href="/docs/linux/man/5-ctdbd-conf/">ctdbd.conf</a></code>(5), <code><a href="/docs/linux/man/7-ctdb/">ctdb</a></code>(7), m[blue]<code><a rel="nofollow" href="http://ctdb.samba.org/">http://ctdb.samba.org/</a></code>m[]</p>
<h2>AUTHOR</h2>
<p> This documentation was written by Amitay Isaacs, Martin Schwenke</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007 Andrew Tridgell, Ronnie Sahlberg </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, see m[blue]<code><a rel="nofollow" href="http://www.gnu.org/licenses">http://www.gnu.org/licenses</a></code>m[]. </p>
<h2>Index</h2>
