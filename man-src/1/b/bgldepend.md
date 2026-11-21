---
title: "bgldepend(1)"
name: "bgldepend"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bgldepend/"
description: "bgldepend – create Bigloo dependencies in makefiles"
---

<h2>SYNOPSIS</h2>
<p> <code>bgldepend</code> [ options ] <i>sourcefile &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>bgldepend</code> program reads each <i>sourcefile</i> in sequence and parses it to find the module <code>include</code> and <code>import</code> module directives. <code>bgldepend</code> computes the transitive closure of the import relationship. That is, it is sufficient to provide <code>bgldepend</code> with a single Bigloo file that imports all the project file (e.g. the &quot;main&quot; file.) </p>
<p> Every file that a <i>sourcefile</i> includes, directly or indirectly, is what <code>bgldepend</code> calls a <i>dependency</i>. These dependencies are then written to a <i>makefile</i> in such a way that <code><a href="/docs/linux/man/1-make/">make</a>(1)</code> will know which object files must be recompiled when a dependency has changed. </p>
<p> By default, <code>bgldepend</code> writes its output on the standard output device. If <code>bgldepend</code> is provided with a <code>-o</code> <i>makefile</i> option, it will update the <i>makefile</i> file. That is, it will search the makefile for the line: </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>bgldepend start&nbsp;<wbr>(don&#8217;t edit) </p>
<p> and </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>bgldepend stop </p>
<p>&nbsp;<wbr>&nbsp;<wbr> Dependencies will be written in between these two lines. </p>
<h2>OPTIONS</h2>
<dl>
<dt>
</dt><dt>file</dt>
<dd>
</dd><dd> Is an file implementing a module. <code>Afile</code> reads that file to discover the name of the implemented module. </dd>
<dt>-search-path &lt;path&gt;</dt>
<dd> Add <i>path</i> to the directory list read for searching Bigloo source files. </dd>
<dt>-exclude-path &lt;path&gt;</dt>
<dd> Exclude <i>path</i> from the directory list read for searching Bigloo source files. </dd>
<dt>-suffix &lt;suf&gt;</dt>
<dd> Adds <i>suf</i> to the <code>bmake</code> source file suffixes list. Default suffixes are &quot;scm&quot;, &quot;sch&quot; and &quot;bgl&quot;. </dd>
<dt>-v</dt>
<dd> Verbose mode </dd>
<dt>-o &lt;makefile&gt;</dt>
<dd> The name of the <i>makefile</i> file to be updated </dd>
</dl>
<h2>EXAMPLE</h2>
<p> Normally, bgldepend will be used in a makefile target so that typing &#8220;make bgldepend&#8221; will bring the dependencies up to date for the makefile. For example, </p>
<p>MAIN=foo.scm </p>
<p>SRCS&nbsp;<wbr>=&nbsp;<wbr>$(MAIN)&nbsp;<wbr>bar.scm gee.scm </p>
<p>bgldepend: </p>
<p>&nbsp;<wbr>bgldepend -o Makefile&nbsp;<wbr>$(MAIN) </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bigloo/">bigloo</a>(1), <a href="/docs/linux/man/1-bglafile/">bglafile</a>(1), <a href="/docs/linux/man/1-bglmake/">bglmake</a>(1), <a href="/docs/linux/man/1-bglpp/">bglpp</a>(1), <a href="/docs/linux/man/1-bglprof/">bglprof</a>(1), <a href="/docs/linux/man/1-bgltags/">bgltags</a>(1), <a href="/docs/linux/man/1-make/">make</a>(1) </p>
<h2>AUTHOR</h2>
<p> Manuel SERRANO, Manuel.Serrano [at] inria.fr </p>
