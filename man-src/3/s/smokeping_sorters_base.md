---
title: "smokeping_sorters_base(3)"
name: "smokeping_sorters_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_sorters_base/"
---

Smokeping::sorters::base - Base Class for implementing SmokePing Sorters 

<h2>Overview</h2>Sorters are at the core of the SmokePing Charts feature, where the most interesting graphs are presented on a single page. The Sorter decides which graphs are considerd interesting. 

 Every sorter must inherit from the base class and provide it's own methods for the 'business' logic. 

 In order to maintain a decent performance the sorters activity is split into two parts. 

 The first part is active while the smokeping daemon gathers its data. Whenever data is received, the sorter is called to calculate a 'value' for the present data. On every 'query round' this information is stored in the sorter store directory. Each smokeping process stores it's own information. Since smokeping can run in multiple instances at the same time, the data may be split over several files 

 The second part of the sorter is called from smokeping.cgi. It loads all the information from the sorter store and integrates it into a single 'tree'. It then calls each sorter with the pre-calculated data to get it sorted and to and to select the interesting information.
<h2>Description</h2>Every sorter must provide the following methods:
<h3>new</h3>The new method expects hash elements as an argument eg new({x=&gt;'\d+',y=&gt;'\d+'},x=&gt;1,y=&gt;2). The first part is a syntax rule for the arguments it should expect and the second part are the arguments itself. The first part will be supplied by the child class as it calls the parent method.
<h3>Desc</h3>Simply return the description of the function. This method must be overwritten by a children of the base class.
<h3>SortTree</h3>Returns an array of 'targets'. It is up to the sorter to decide how many entries the list should contain. If the list is empty, the whole entry will be supressed in the webfrontend. 

 The methode gets access to all the targets in the system, together with the last data set acquired for each target.
<h3>CalcValues</h3>Figure out the curent sorting value using te following input. 

 <pre> $info = { uptime =&gt; w,
 loss =&gt; x,
 median =&gt; y,
 alert =&gt; z, # (0/1)
 pings =&gt; [qw(a b c d)] }</pre>The output can have any structure you want. It will be returned to the sorter method for further processng.
<h2>Copyright</h2>Copyright (c) 2007 by <font SIZE="-1">OETIKER+PARTNER AG.</font> All rights reserved.
<h2>License</h2>This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font>
<h2>Author</h2>Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;
