---

title: "callgrind_annotate(1)"
name: "callgrind_annotate"
section: "1"
letter: "c"
url: "/docs/linux/man/1-callgrind_annotate/"
description: "callgrind_annotate – post-processing tool for the Callgrind"
---

<p> callgrind_annotate &#8211; post-processing tool for the Callgrind </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>callgrind_annotate</code> [<i>options</i>] [<i>callgrind-out-file</i>&nbsp;[<i>source-files</i>&#8230;]]</dt></dl>
<h2>DESCRIPTION</h2>
<p> <code>callgrind_annotate</code></p>
<dd>takes an output file produced by the Valgrind tool Callgrind and prints the information in an easy-to-read form.</dd>
<h2>OPTIONS</h2>
<p> <code>-h &#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show summary of options.</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Show version of callgrind_annotate.</dd></dl>
<p> <code>&#8211;show=A,B,C [default: all]</code></p>
<dl>
<dt>
</dt><dd> Only show figures for events A,B,C.</dd></dl>
<p> <code>&#8211;threshold=&lt;0&#8211;100&gt; [default: 99%] </code></p>
<dl>
<dt>
</dt><dd> Percentage of counts (of primary sort event) we are interested in. </dd>
<p> callgrind_annotate stops printing functions when the sum of the cost percentage of the printed functions is bigger or equal to the given threshold percentage.</dl>
<p> <code>&#8211;sort=A,B,C</code></p>
<dl>
<dt>
</dt><dd> Sort columns by events A,B,C [event column order]. </dd>
<p> Optionally, each event is followed by a : and a threshold, to specify different thresholds depending on the event. </p>
<p> callgrind_annotate stops printing functions when the sum of the cost percentage of the printed functions for all the events is bigger or equal to the given event threshold percentages. </p>
<p> When one or more thresholds are given via this option, the value of <code>&#8211;threshold</code> is ignored.</dl>
<p> <code>&#8211;show-percs=&lt;no|yes&gt; [default: no] </code></p>
<dl>
<dt>
</dt><dd> When enabled, a percentage is printed next to all event counts. This helps gauge the relative importance of each function and line.</dd></dl>
<p> <code>&#8211;auto=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
</dt><dd> Annotate all source files containing functions that helped reach the event count threshold.</dd></dl>
<p> <code>&#8211;context=N [default: 8] </code></p>
<dl>
<dt>
</dt><dd> Print N lines of context before and after annotated lines.</dd></dl>
<p> <code>&#8211;inclusive=&lt;yes|no&gt; [default: no] </code></p>
<dl>
<dt>
</dt><dd> Add subroutine costs to functions calls.</dd></dl>
<p> <code>&#8211;tree=&lt;none|caller|calling|both&gt; [default: none] </code></p>
<dl>
<dt>
</dt><dd> Print for each function their callers, the called functions or both.</dd></dl>
<p> <code>-I, &#8211;include=&lt;dir&gt; </code></p>
<dl>
<dt>
</dt><dd> Add <code>dir</code> to the list of directories to search for source files.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-valgrind/">valgrind</a>(1), $INSTALL/share/doc/valgrind/html/index.html or <a rel="nofollow" href="http://www.valgrind.org/docs/manual/index.html.">http://www.valgrind.org/docs/manual/index.html.</a></p>
<h2>AUTHOR</h2>
<p> Josef Weidendorfer &lt;Josef.Weidendorfer [at] gmx.de&gt;. </p>
<p> This manual page was written by Philipp Frauenfelder &lt;pfrauenf [at] debian.org&gt;. </p>
