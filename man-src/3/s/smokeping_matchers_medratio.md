---
title: "smokeping_matchers_medratio(3)"
name: "smokeping_matchers_medratio"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_matchers_medratio/"
---

Smokeping::matchers::Medratio - detect changes in the latency median 

<h2>Overview</h2>The Medratio matcher establishes a historic median latency over several measurement rounds. It compares this median, against a second median latency value again build over several rounds of measurement. 

 By looking at the median value this matcher is largly imune against spikes and will only react to long term developments.
<h2>Description</h2>Call the matcher with the following sequence: 

 <pre> type = matcher
 pattern = Medratio(historic=&gt;a,current=&gt;b,comparator=&gt;o,percentage=&gt;p)</pre><dl COMPACT><dt>historic
<dd>The number of values to use for building the 'historic' median.
<dt>current
<dd>The number of values to use for building the 'current' median.
<dt>comparator
<dd>Which comparison operator should be used to compare current/historic with percentage.
<dt>percentage
<dd>Right hand side of the comparison.</dl>
 

 <pre> old &lt;--- historic ---&gt;&lt;--- current ---&gt; now</pre><h2>Example</h2>Take the 12 last median values. Build the median out of the first 10 and the median from the other 2 values. Divide the results and decide if it is bigger than 150 percent. 

 <pre> Medratio(historic=&gt;10,current=&gt;2,comparator=&gt;'&gt;',percentage=&gt;150);
 med(current)/med(historic) &gt; 150/100</pre>This means the matcher will activate when the current latency median is more than 1.5 times the historic latency median established over the last 10 rounds of measurement.
<h2>Copyright</h2>Copyright (c) 2006 by <font SIZE="-1">OETIKER+PARTNER AG.</font> All rights reserved.
<h2>Sponsorship</h2>The development of this matcher has been paied for by Virtela Communications, &lt;<a rel="nofollow" HREF="http://www.virtela.net/">http://www.virtela.net/</a>&gt;.
<h2>License</h2>This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font>
<h2>Author</h2>Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;
