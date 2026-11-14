---
title: "friendsd2(1)"
name: "friendsd2"
section: "1"
letter: "f"
url: "/docs/linux/man/1-friendsd2/"
description: "friendsd2 – displays GPS position on a map"
---

<h2>NAME</h2>
<p> friendsd2 &#8211; displays GPS position on a map</p>
<h2>SYNOPSIS</h2>
<p> <code>friendsd2 [options]</code> </p>
<h2>About this manual page</h2>
<p> This manual page explain the basic functions of Friendsd2 for GpsDrive and some additional info. </p>
<h2>DESCRIPTION</h2>
<p> <code>Friendsd2</code> is a central daemon which takes UDP packets from gpsdrive clients and stores them. Later he sends them back to all the connecte gpsd-client so they can show all the Geo-Locations of all other users connected to this friendsd. One central friendsd is running at friends.gpsdrive.de.<br />
&nbsp;<wbr></p>
<h2>BUGS</h2>
<p> The current friendsd can only hold a limited number of users, since he sends only one UDP packet to the client for response. </p>
<h2>AUTHOR</h2>
<p> Fritz Ganter<br />
 <a rel="nofollow" href="http://www.gpsdrive.de">http://www.gpsdrive.de</a></p>
<h2>WARRANTY</h2>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001-2007 by Fritz Ganter<br />
 This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>Index</h2>
