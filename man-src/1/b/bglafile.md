---
title: "bglafile(1)"
name: "bglafile"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bglafile/"
description: "Bglafile – a Module Access File Generator"
---

<h2 class="name">NAME</h2>
<p> Bglafile &#8211; a Module Access File Generator</p>
<h2>SYNOPSIS</h2>
<p> <code>bglafile</code> [ options ] <i>file &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>Bglafile</code> is a Module Access File generator. It produces file that suits Bigloo option <i>-afile</i>. A Module Access File is a scheme list. Each elements of that list is a list of at least two elements: a module name, the file that implements that module. For BEE (the Bigloo Integrated Development Environment) to be able to retrieve files from module names, it is mandatory that the first parentheses of the global list is left alone on one line. </p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dt><code>file</code></p>
<dd>
<dd> Is an file implementing a module. <code>Bglafile</code> reads that file to discover the name of the implemented module. </p>
<dt><code>-v</code></p>
<dd> Verbose mode </p>
<dt><code>-o &lt;file&gt;</code></p>
<dd> Print Module Access File into <i>file</i>. The default is to print the list on the standard output device. </p>
<dt><code>-suffix &lt;suf&gt;</code></p>
<dd> Adds <i>suf</i> to the <code>bglafile</code> source file suffixes list. Default suffixes are &quot;scm&quot;, &quot;sch&quot; and &quot;bgl&quot;. </p>
</dl>
<h2>EXAMPLE</h2>
<p> If the three files exists and contain legal Bigloo module clause, then: </p>
<p>$&nbsp;<wbr>bglafile foo.scm bar.scm gee.scm </p>
<p> could print out a list like: </p>
<p> ;; foo </p>
<p> ;; Tue Aug 15 12:17:24 1998 </p>
<p> ( </p>
<p>&nbsp;<wbr>&nbsp;<wbr>(foo&nbsp;<wbr>&quot;foo.scm&quot;) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>(bar&nbsp;<wbr>&quot;bar.scm&quot;) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>(gee&nbsp;<wbr>&quot;gee.scm&quot;) </p>
<p> ) </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bigloo/">bigloo</a>(1), <a href="/docs/linux/man/1-bgldepend/">bgldepend</a>(1), <a href="/docs/linux/man/1-bglmake/">bglmake</a>(1), <a href="/docs/linux/man/1-bglpp/">bglpp</a>(1), <a href="/docs/linux/man/1-bglprof/">bglprof</a>(1), <a href="/docs/linux/man/1-bgltags/">bgltags</a>(1) </p>
<h2>AUTHOR</h2>
<p> Manuel SERRANO, Manuel.Serrano [at] inria.fr </p>
<h2>Index</h2>
