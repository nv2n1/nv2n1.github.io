---
title: "smokeping_sorters_max(3)"
name: "smokeping_sorters_max"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_sorters_max/"
---

Smokeping::sorters::Max - Order the target charts by Max RTT 

<h2>Overview</h2>Find the charts with the highest round trip time.
<h2>Description</h2>Call the sorter in the charts section of the config file 

 <pre> + charts
 menu = Charts
 title = The most interesting destinations
 ++ max
 sorter = Max(entries=&gt;10)
 title = Sorted by Max Roundtrip Time
 menu = by Max
 format = Max Roundtrip Time %f seconds</pre><h2>Copyright</h2>Copyright (c) 2007 by OETIKER+PARTNER AG. All rights reserved.
<h2>License</h2>This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details. 

 You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
<h2>Author</h2>Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;
