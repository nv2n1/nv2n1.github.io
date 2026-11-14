---
title: "pdldataflow(1)"
name: "pdldataflow"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdldataflow/"
---

PDL::Dataflow -- description of the dataflow philosophy 

<h2>Synopsis</h2><pre> pdl&gt; $a = zeroes(10);
 pdl&gt; $b = $a-&gt;slice(&quot;2:4:2&quot;);
 pdl&gt; $b ++;
 pdl&gt; print $a;
 [0 0 1 0 1 0 0 0 0 0]</pre><h2>Warning</h2>Dataflow is very experimental. Many features of it are disabled for 2.0, particularly families for one-directional dataflow. If you wish to use one-directional dataflow for something, please contact the author first and we'll work out how to make it functional again. 

 Two-directional dataflow (which implements -&gt;<i>slice()</i> etc.) is fully functional, however. Just about any function which returns some subset of the values in some piddle will make a binding so that 

 <pre> $a = some piddle
 $b = $a-&gt;slice(&quot;some parts&quot;);
 $b-&gt;set(3,3,10);</pre>also changes the corresponding element in <tt>$a</tt>. <tt>$b</tt> has become effectively a window to some sub-elements of <tt>$a</tt>. You can also define your own routines that do different types of subsets. If you don't want <tt>$b</tt> to be a window to <tt>$a</tt>, you must do 

 <pre> $b = $a-&gt;slice(&quot;some parts&quot;)-&gt;copy;</pre>The copying turns off all dataflow between the two piddles. 

 The difficulties with one-directional dataflow are related to sequences like 

 <pre> $b = $a + 1;
 $b ++;</pre>where there are several possible outcomes and the semantics get a little murky.
<h2>Description</h2>Dataflow is new to <font SIZE="-1">PDL2.0.</font> The basic philosophy behind dataflow is that 

 <pre> &gt; $a = pdl 2,3,4;
 &gt; $b = $a * 2;
 &gt; print $b
 [2 3 4]
 &gt; $a-&gt;set(0,5);
 &gt; print $b;
 [10 3 4]</pre>should work. It doesn't. It was considered that doing this might be too confusing for novices and occasional users of the language. Therefore, you need to explicitly turn on dataflow, so 

 <pre> &gt; $a = pdl 2,3,4;
 &gt; $a-&gt;doflow();
 &gt; $b = $a * 2;
 ...</pre>produces the unexpected result. The rest of this documents explains various features and details of the dataflow implementation.
<h2>Lazy evaluation</h2>When you calculate something like the above 

 <pre> &gt; $a = pdl 2,3,4;
 &gt; $a-&gt;doflow();
 &gt; $b = $a * 2;</pre>nothing will have been calculated at this point. Even the memory for the contents of <tt>$b</tt> has not been allocated. Only the command 

 <pre> &gt; print $b</pre>will actually cause <tt>$b</tt> to be calculated. This is important to bear in mind when doing performance measurements and benchmarks as well as when tracking errors. 

 There is an explanation for this behaviour: it may save cycles but more importantly, imagine the following: 

 <pre> &gt; $a = pdl 2,3,4;
 &gt; $b = pdl 5,6,7;
 &gt; $c = $a + $b;
 ...
 &gt; $a-&gt;<a HREF="//www.systutorials.com/docs/linux/man/4-resize/">resize</a>(4);
 &gt; $b-&gt;<a HREF="//www.systutorials.com/docs/linux/man/4-resize/">resize</a>(4);
 &gt; print $c;</pre>Now, if <tt>$c</tt> were evaluated between the two resizes, an error condition of incompatible sizes would occur. 

 What happens in the current version is that resizing <tt>$a</tt> raises a flag in <tt>$c:</tt> ``<font SIZE="-1">PDL_PARENTDIMSCHANGED''</font> and <tt>$b</tt> just raises the same flag again. When <tt>$c</tt> is next evaluated, the flags are checked and it is found that a recalculation is needed. 

 Of course, lazy evaluation can sometimes make debugging more painful because errors may occur somewhere where you'd not expect them. A better stack trace for errors is in the works for <font SIZE="-1">PDL,</font> probably so that you can toggle a switch <tt>$PDL::traceevals</tt> and get a good trace of where the error actually was.
<h2>Families</h2>This is one of the more intricate concepts of one-directional dataflow. Consider the following code ($a and <tt>$b</tt> are pdls that have dataflow enabled): 

 <pre> $c = $a + $b;
 $e = $c + 1;
 $d = $c-&gt;diagonal();
 $d ++;
 $f = $c + 1;</pre>What should <tt>$e</tt> and <tt>$f</tt> contain now? What about when <tt>$a</tt> is changed and a recalculation is triggered. 

 In order to make dataflow work like you'd expect, a rather strange concept must be introduced: families. Let us make a diagram: 

 <pre> a b
 \ /
 c
 /|
 / |
 e d</pre>This is what <font SIZE="-1">PDL</font> actually has in memory after the first three lines. When <tt>$d</tt> is changed, we want <tt>$c</tt> to change but we don't want <tt>$e</tt> to change because it already is on the graph. It may not be clear now why you don't want it to change but if there were 40 lines of code between the 2nd and 4th lines, you would. So we need to make a copy of <tt>$c</tt> and <tt>$d:</tt> 

 <pre> a b
 \ /
 c' . . . c
 /| |\
 / | | \
 e d' . . . d f</pre>Notice that we primed the original c and d, because they do not correspond to the objects in <tt>$c</tt> and <tt>$d</tt> any more. Also, notice the dotted lines between the two objects: when <tt>$a</tt> is changed and this diagram is re-evaluated, <tt>$c</tt> really does get the value of c' with the diagonal incremented. 

 To generalize on the above, whenever a piddle is mutated i.e. when its actual *value* is forcibly changed (not just the reference: 

 <pre> $d = $d + 1</pre>would produce a completely different result ($c and <tt>$d</tt> would not be bound any more whereas 

 <pre> $d .= $d + 1</pre>would yield the same as <tt>$d</tt>++), a ``family'' consisting of all other piddles joined to the mutated piddle by a two-way transformation is created and all those are copied. 

 All slices or transformations that simply select a subset of the original pdl are two-way. Matrix inverse should be. No arithmetic operators are.
<h2>Sources</h2>What you were told in the previous section is not quite true: the behaviour described is not *always* what you want. Sometimes you would probably like to have a data ``source'': 

 <pre> $a = pdl 2,3,4; $b = pdl 5,6,7;
 $c = $a + $b;
 line($c);</pre>Now, if you know that <tt>$a</tt> is going to change and that you want its children to change with it, you can declare it into a data source (<font SIZE="-1">XXX</font> unimplemented in current version): 

 <pre> $a-&gt;<a HREF="//www.systutorials.com/docs/linux/man/1-datasource/">datasource</a>(1);</pre>After this, <tt>$a</tt>++ or <tt>$a</tt> .= something will not create a new family but will alter <tt>$a</tt> and cut its relation with its previous parents. All its children will follow its current value. 

 So if <tt>$c</tt> in the previous section had been declared as a source, <tt>$e</tt> and <tt>$f</tt> would remain equal.
<h2>Binding</h2>A dataflow mechanism would not be very useful without the ability to bind events onto changed data. Therefore, we provide such a mechanism: 

 <pre> &gt; $a = pdl 2,3,4
 &gt; $b = $a + 1;
 &gt; $c = $b * 2;
 &gt; $c-&gt;bind( sub { print &quot;A now: $a, C now: $c\n&quot; } )
 &gt; PDL::dowhenidle();
 A now: [2,3,4], C now: [6 8 10]
 &gt; $a-&gt;set(0,1);
 &gt; $a-&gt;set(1,1);
 &gt; PDL::dowhenidle();
 A now: [1,1,4], C now: [4 4 10]</pre>Notice how the callbacks only get called during PDL::dowhenidle. An easy way to interface this to Perl event loop mechanisms (such as Tk) is being planned. 

 There are many kinds of uses for this feature: self-updating graphs, for instance. 

 Blah blah blah <font SIZE="-1">XXX</font> more explanation
<h2>Limitations</h2>Dataflow as such is a fairly limited addition on top of Perl. To get a more refined addition, the internals of Perl need to be hacked a little. A true implementation would enable flow of everything, including
<dl><dt>data
<dd><dt>data size
<dd><dt>datatype
<dd><dt>operations
<dd></dl>
 

 At the moment we only have the first two (hey, 50% in a couple of months is not bad ;) but even this is useful by itself. However, especially the last one is desirable since it would add the possibility of flowing closures from place to place and would make many things more flexible. 

 To get the rest working, the internals of dataflow probably need to be changed to be a more general framework. 

 Additionally, it would be nice to be able to flow data in time, lucid-like (so you could easily define all kinds of signal processing things).
<h2>Author</h2>Copyright(C) 1997 Tuomas J. Lukka (lukka [at] fas.harvard.edu). Redistribution in the same form is allowed provided that the copyright notice stays intact but reprinting requires a permission from the author.
