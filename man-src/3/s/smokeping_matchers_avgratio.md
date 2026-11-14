---
title: "smokeping_matchers_avgratio(3)"
name: "smokeping_matchers_avgratio"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_matchers_avgratio/"
---

Smokeping::matchers::Avgratio - detect changes in average median latency 

<h2>Overview</h2>The Avgratio matcher establishes a historic average median latency over several measurement rounds. It compares this average, against a second average latency value again build over several rounds of measurement.
<h2>Description</h2>Call the matcher with the following sequence: 

 <pre> type = matcher
 pattern = Avgratio(historic=&gt;a,current=&gt;b,comparator=&gt;o,percentage=&gt;p)</pre><dl COMPACT><dt>historic
<dd>The number of median values to use for building the 'historic' average.
<dt>current
<dd>The number of median values to use for building the 'current' average.
<dt>comparator
<dd>Which comparison operator should be used to compare current/historic with percentage.
<dt>percentage
<dd>Right hand side of the comparison.</dl>
 

 <pre> old &lt;--- historic ---&gt;&lt;--- current ---&gt; now</pre><h2>Example</h2>Take build the average median latency over 10 samples, use this to divide the current average latency built over 2 samples and check if it is bigger than 150%. 

 <pre> Avgratio(historic=&gt;10,current=&gt;2,comparator=&gt;'&gt;',percentage=&gt;150);
 avg(current)/avg(historic) &gt; 150/100</pre>This means the matcher will activate when the current latency average is more than 1.5 times the historic latency average established over the last 10 rounds of measurement.
<h2>Copyright</h2>Copyright (c) 2004 by <font SIZE="-1">OETIKER+PARTNER AG.</font> All rights reserved.
<h2>Sponsorship</h2>The development of this matcher has been sponsored by Virtela Communications, &lt;<a rel="nofollow" HREF="http://www.virtela.net/">http://www.virtela.net/</a>&gt;.
<h2>License</h2>This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font>
<h2>Author</h2>Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;
