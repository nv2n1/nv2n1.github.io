---
title: "smokeping_matchers_base(3)"
name: "smokeping_matchers_base"
section: "3"
letter: "s"
url: "/docs/linux/man/3-smokeping_matchers_base/"
---

Smokeping::matchers::base - Base Class for implementing SmokePing Matchers 

<h2>Overview</h2>This is the base class for writing SmokePing matchers. Every matcher must inherit from the base class and provide it's own methods for the 'business' logic. 

 Note that the actual matchers must have at least one capital letter in their name, to differentiate them from the base class(es).
<h2>Description</h2>Every matcher must provide the following methods:
<h3>new</h3>The new method expects hash elements as an argument eg new({x=&gt;'\d+',y=&gt;'\d+'},x=&gt;1,y=&gt;2). The first part is a syntax rule for the arguments it should expect and the second part are the arguments itself. The first part will be supplied by the child class as it calls the parent method.
<h3>Length</h3>The Length method returns the number of values the matcher will expect from SmokePing. This method must be overridden by the children of the base class.
<h3>Desc</h3>Simply return the description of the function. This method must be overwritten by a children of the base class.
<h3>Test</h3>Run the matcher and return true or false. The Test method is called with a hash containing two arrays giving it access to both rtt and loss values. 

 <pre> my $data=shift;
 my @rtt = @{$data-&gt;{rtt}};
 my @loss = @{$data-&gt;{loss}};</pre>The arrays are ordered from old to new. 

 <pre> @rdd[old..new]</pre>There may be more than the expected number of elements in this array. Address them with <tt>$x</tt>[-1] to <tt>$x</tt>[-max]. 

 There's also a key called 'prevmatch' in the hash. It contains the value returned by the previous call of the 'Test' method. This allows for somewhat more intelligent alerting due to state awareness. 

 <pre> my $prevmatch = $data-&gt;{prevmatch};</pre><h2>Copyright</h2>Copyright (c) 2004 by <font SIZE="-1">OETIKER+PARTNER AG.</font> All rights reserved.
<h2>License</h2>This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. 

 This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. 

 You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 675 Mass Ave, Cambridge, <font SIZE="-1">MA 02139, USA.</font>
<h2>Author</h2>Tobias Oetiker &lt;tobi [at] oetiker.ch&gt;
