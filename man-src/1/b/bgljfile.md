---
title: "bgljfile(1)"
name: "bgljfile"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bgljfile/"
description: "Bgljfile – a Jvm Access File Generator"
---

<h2 class="name">NAME</h2>
<p> Bgljfile &#8211; a Jvm Access File Generator</p>
<h2>SYNOPSIS</h2>
<p> <code>bgljfile</code> [ options ] <i>file &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>Bgljfile</code> is a Jvm Access File generator. It produces file that suits Bigloo option <i>-bgljfile</i>. A Jvm Access File is a scheme list. Each elements of that list is a list of at least two elements: a module name, the Java class file that implements that module. </p>
<h2>OPTIONS</h2>
<dl>
<dt>
<dt><code>file</code></p>
<dd>
<dd> Is an file implementing a module. <code>Bgljfile</code> reads that file to discover the name of the implemented module. </p>
<dt><code>-base</code></p>
<dd> Set the Jvm base package. </p>
<dt><code>-o &lt;file&gt;</code></p>
<dd> Print Module Access File into <i>file</i>. The default is to print the list on the standard output device. </p>
<dt><code>-suffix &lt;suf&gt;</code></p>
<dd> Adds <i>suf</i> to the <code>bgljfile</code> source file suffixes list. Default suffixes are &quot;scm&quot;, &quot;sch&quot; and &quot;bgl&quot;. </p>
</dl>
<h2>EXAMPLE</h2>
<p> If the three files exists and contain legal Bigloo module clause, then: </p>
<p>$&nbsp;<wbr>bgljfile foo.scm bar.scm gee.scm </p>
<p> could print out a list like: </p>
<p> ( </p>
<p>&nbsp;<wbr>&nbsp;<wbr>(foo&nbsp;<wbr>&quot;./foo&quot;) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>(bar&nbsp;<wbr>&quot;./bar&quot;) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>(gee&nbsp;<wbr>&quot;./gee&quot;) </p>
<p> ) </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bigloo/">bigloo</a>(1), <a href="/docs/linux/man/1-bgldepend/">bgldepend</a>(1), <a href="/docs/linux/man/1-bglmake/">bglmake</a>(1), <a href="/docs/linux/man/1-bglpp/">bglpp</a>(1), <a href="/docs/linux/man/1-bglprof/">bglprof</a>(1), <a href="/docs/linux/man/1-bgltags/">bgltags</a>(1) </p>
<h2>AUTHOR</h2>
<p> Manuel SERRANO, Manuel.Serrano [at] inria.fr </p>
<h2>Index</h2>
