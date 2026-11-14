---
title: "smokeping_matchers_exploss(3)"
name: "smokeping_matchers_exploss"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_matchers_exploss/"
---

Smokeping::matchers::ExpLoss - exponential weighting matcher for packet loss with RMON-like thresholds 

<h2>Description</h2>Match against exponential weighted average of last samples, thus new values are more valuable as old ones. Two thresholds - rising and falling - produce hysteresis loop like in <font SIZE="-1">RMON</font> alert subsystem. If the average reaches the ``rising'' threshold, matcher go to the ``match'' state and hold It until the average drops under the ``falling'' threshold. 

 Call the matcher with the following sequence: 

 <pre> type = matcher
 pattern = CheckLoss(hist =&gt; &lt;hist&gt;, rising=&gt;&lt;rising&gt; \
 [,falling =&gt; &lt;falling&gt;] [,skip=&gt;&lt;stat&gt;] [,fast=&gt;&lt;fast&gt;])</pre>Arguments: 
&nbsp;<wbr>hist&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- number of samples to weight against;&nbsp;<wbr>weight will be disposed with 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>exponetial decreasing manner from newest to oldest, so that the 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>oldest sample would have 1%&nbsp;<wbr>significance; 
&nbsp;<wbr>rising&nbsp;<wbr>&nbsp;<wbr>- rising threshold for packet loss, 0-100% 
&nbsp;<wbr>falling - falling threshold for packet loss, default is&nbsp;<wbr>&lt;rising&gt; 
&nbsp;<wbr>skip&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- skip&nbsp;<wbr>&lt;skip&gt;&nbsp;<wbr>number of samples after startup before&nbsp;<wbr>``fire''&nbsp;<wbr>alerts. 
&nbsp;<wbr>fast&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>- use&nbsp;<wbr>&lt;fast&gt;&nbsp;<wbr>samples for fast transition: if the values of last&nbsp;<wbr>&lt;fast&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>samples more then&nbsp;<wbr>&lt;rising&gt;&nbsp;<wbr>- take&nbsp;<wbr>``match''&nbsp;<wbr>state, if less then 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;falling&gt;&nbsp;<wbr>- take&nbsp;<wbr>``no match''&nbsp;<wbr>state. 

 Note: 
&nbsp;<wbr>If the actual history is less then&nbsp;<wbr>&lt;hist&gt;&nbsp;<wbr>value then this value is taken&nbsp;<wbr> 
&nbsp;<wbr>as the actual history.
<h2>Copyright</h2>Copyright (c) 2008 Veniamin Konoplev 

 Developed in cooperation with <font SIZE="-1">EU EGEE</font> project
<h2>License</h2>This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font>
<h2>Author</h2>Veniamin Konoplev &lt;vkonoplev [at] acm.org&gt;
