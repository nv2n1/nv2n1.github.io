---
title: "cg_annotate(1)"
name: "cg_annotate"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cg_annotate/"
description: "cg_annotate – post-processing tool for Cachegrind"
---

<h2 class="name">NAME</h2>
<p> cg_annotate &#8211; post-processing tool for Cachegrind </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>cg_annotate</code> [<i>options</i>] <i>cachegrind-out-file</i> [<i>source-files</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>cg_annotate</code></p>
<dd>takes an output file produced by the Valgrind tool Cachegrind and prints the information in an easy-to-read form.</p>
<h2>OPTIONS</h2>
<p> <code>-h &#8211;help </code></p>
<dl>
<dt>
<dd> Show the help message.</dl>
<p> <code>&#8211;version </code></p>
<dl>
<dt>
<dd> Show the version number.</dl>
<p> <code>&#8211;show=A,B,C [default: all, using order in cachegrind.out.&lt;pid&gt;] </code></p>
<dl>
<dt>
<dd> Specifies which events to show (and the column order). Default is to use all present in the cachegrind.out.&lt;pid&gt; file (and use the order in the file). Useful if you want to concentrate on, for example, I cache misses (<code>&#8211;show=I1mr,ILmr</code>), or data read misses (<code>&#8211;show=D1mr,DLmr</code>), or LL data misses (<code>&#8211;show=DLmr,DLmw</code>). Best used in conjunction with <code>&#8211;sort</code>.</dl>
<p> <code>&#8211;sort=A,B,C [default: order in cachegrind.out.&lt;pid&gt;] </code></p>
<dl>
<dt>
<dd> Specifies the events upon which the sorting of the function-by-function entries will be based.</dl>
<p> <code>&#8211;threshold=X [default: 0.1%] </code></p>
<dl>
<dt>
<dd> Sets the threshold for the function-by-function summary. A function is shown if it accounts for more than X% of the counts for the primary sort event. If auto-annotating, also affects which files are annotated. </p>
<p> Note: thresholds can be set for more than one of the events by appending any events for the <code>&#8211;sort</code> option with a colon and a number (no spaces, though). E.g. if you want to see each function that covers more than 1% of LL read misses or 1% of LL write misses, use this option: </p>
<p> <code>&#8211;sort=DLmr:1,DLmw:1</code></dl>
<p> <code>&#8211;show-percs=&lt;no|yes&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When enabled, a percentage is printed next to all event counts. This helps gauge the relative importance of each function and line.</dl>
<p> <code>&#8211;auto=&lt;no|yes&gt; [default: no] </code></p>
<dl>
<dt>
<dd> When enabled, automatically annotates every file that is mentioned in the function-by-function summary that can be found. Also gives a list of those that couldn&#8217;t be found.</dl>
<p> <code>&#8211;context=N [default: 8] </code></p>
<dl>
<dt>
<dd> Print N lines of context before and after each annotated line. Avoids printing large sections of source files that were not executed. Use a large number (e.g. 100000) to show all source lines.</dl>
<p> <code>-I&lt;dir&gt; &#8211;include=&lt;dir&gt; [default: none] </code></p>
<dl>
<dt>
<dd> Adds a directory to the list in which to search for files. Multiple <code>-I</code>/<code>&#8211;include</code> options can be given to add multiple directories.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-valgrind/">valgrind</a>(1), $INSTALL/share/doc/valgrind/html/index.html or <a rel="nofollow" href="http://www.valgrind.org/docs/manual/index.html.">http://www.valgrind.org/docs/manual/index.html.</a></p>
<h2>AUTHOR</h2>
<p> Nicholas Nethercote. </p>
<h2>Index</h2>
