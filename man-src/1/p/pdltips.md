---
title: "pdltips(1)"
name: "pdltips"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pdltips/"
---

PDL::Tips - Small tidbits of useful arcana. Programming tidbits and such. 

<h2>Synopsis</h2><pre> use PDL;
 # Whatever happens here.</pre><h2>Description</h2>This page documents useful idioms, helpful hints and tips for using Perl Data Language v2.0.
<h3>Help</h3>Use <tt>&quot;help help&quot;</tt> within <i>perldl</i> or <i>pdl2</i> or use the <tt>&quot;pdldoc&quot;</tt> program from the command line for access to the PerlDL documentation. <font SIZE="-1">HTML</font> versions of the pages should also be present, in the <i>HtmlDocs/PDL</i> directory of the <font SIZE="-1">PDL</font> distribution. To find this directory, try the following 

 <pre> pdl&gt; foreach ( map{&quot;$_/PDL/HtmlDocs&quot;}@INC ) { p &quot;$_\n&quot; if -d $_ }</pre><h3>Indexing idioms</h3>The following code normalizes a bunch of vectors in <tt>$a</tt>. This works regardless of the dimensionality of <tt>$a</tt>. 

 <pre> $a /= $a-&gt;sumover-&gt;dummy(0);</pre><h3>What is actually happening?</h3>If you want to see what the code is actually doing, try the command 

 <pre> <a HREF="//www.systutorials.com/docs/linux/man/1-PDL::Core::set_debugging/">PDL::Core::set_debugging</a>(1);</pre>somewhere. This spews out a huge amount of debug info for <font SIZE="-1">PDL</font> into <font SIZE="-1">STDOUT.</font> Plans for the future include making it possible to redirect the output, and also making it possible to select mesages with more precision. 

 Many of the messages come from <tt>&quot;Basic/Core/pdlapi.c&quot;</tt> and you can look at the source to see what is going on. 

 If you have any extra time to work on these mechanisms, inform the pdl-porters mailing list.
<h3>Memory savings</h3>If you are running recursively something that selects certain indices of a large piddle, like 

 <pre> <a HREF="//www.systutorials.com/docs/linux/man/1-while/">while</a>(1) {
 $inds = where($a&gt;0);
 $a = $a-&gt;index($inds);
 $b = $b-&gt;index($inds);
 func($b,$a);
 }</pre>If you are not writing to <tt>$b</tt>, it saves a lot of memory to change this to 

 <pre> $b = $b-&gt;index($inds)-&gt;sever;</pre>The new method <tt>&quot;sever&quot;</tt> is a causes the write-back relation to be forgotten. It is like copy except it changes the original piddle and returns it). 

 Of course, the probably best way to do the above is 

 <pre> $inds = xvals ($a-&gt;long);
 <a HREF="//www.systutorials.com/docs/linux/man/1-while/">while</a>(1) {
 $inds0 = where($a&gt;0);
 $inds1 = $inds-&gt;index($inds)-&gt;sever;
 $a = $a0-&gt;index($inds1);
 $b = $b-&gt;index($inds1)-&gt;sever;
 func($b,$a);
 }</pre>which doesn't save all the temporary instances of <tt>$a</tt> in memory. See <tt>&quot;mandel.pl&quot;</tt> in the Demos subdirectory of the PerlDL distribution for an example.
<h3><font SIZE="-1">PP</font> speed</h3>If you really want to write speedy <font SIZE="-1">PP</font> code, the first thing you need to do is to make sure that your C compiler is allowed to do the necessary optimizations. 

 What this means is that you have to allow as many variables as possible to go into registers: 

 <pre> loop(a) %{
 $a() += $COMP(foo_member) * $b()
 %}</pre>expands to 

 <pre> for(i=0; i&lt;10000; i++) {
 a[i] += __privtrans-&gt;foo_member * b[i];
 }</pre>is about the worst you can do, since your C compiler is not allowed to assume that <tt>&quot;a&quot;</tt> doesn't clobber <tt>&quot;foo_member&quot;</tt> which completely inhibits vectorization. Instead, do 

 <pre> float foo = $COMP(foo_member);
 loop(a) %{
 $a() += foo * $b();
 %}</pre>This is not a restriction caused by <font SIZE="-1">PP</font> but by <font SIZE="-1">ANSI C</font> semantics. Of course, we could copy the struct into local variables and back but that could cause very strange things sometimes. 

 There are many other issues on organizing loops. 

 We are currently planning to make <font SIZE="-1">PP</font> able to do fixed-width things as well as physical piddles (where looping over the first dimensions would be cheaper as there are less distinct increments, which might make a difference on machines with a small number of registers).
<h2>Author</h2>Copyright (C) Tuomas J. Lukka 1997. All rights reserved. Duplication in the same form and printing a copy for yourself allowed.
