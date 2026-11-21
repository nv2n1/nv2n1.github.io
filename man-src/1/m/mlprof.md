---

title: "mlprof(1)"
name: "mlprof"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mlprof/"
description: "mlprof – display profiling information for a MLton-compiled executable"
---

<p> <code>mlprof</code> &#8211; display profiling information for a MLton-compiled executable</p>
<h2>SYNOPSIS</h2>
<p> <code>mlprof </code><i>[option &#8230;] a.out [mlmon.out &#8230;]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>mlprof</code> extracts information from an executable compiled by <code>MLton</code> with <code>-profile alloc</code> or <code>-profile time</code> and the resulting <code>mlmon.out</code> file produced by running the executable. </p>
<p> The output of <code>mlprof</code> consists of an initial line indicating the total amount of CPU time or bytes allocated. After this, source functions are listed along with the percentage of this total that they used, in decreasing order. If the program was compiled with <code>-profile-stack true</code>, <code>mlprof</code> will display the time spent or bytes allocated while the function was on the stack and in GC in addition to the time or bytes that the function is directly responsible for. </p>
<p> With multiple <code>mlmon.out</code> files, <code>mlprof</code> will sum the profiling information. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-call-graph </code><i>file</i></dt>
<dd> Write a call graph containing the table data to a dot file. See the <code>MLton User Guide</code> for details.</dd>
<dt><code>-graph-title </code><i>string</i></dt>
<dd> Set the call-graph title.</dd>
<dt><code>-gray </code><i>{</i><code>false</code>|<code>true</code>}</dt>
<dd> Gray call-graph nodes according to stack %. This only makes sense if the executable was compiled <code>-profile-stack true</code>.</dd>
<dt><code>-keep </code><i>exp</i></dt>
<dd> Only show functions specified by <i>exp</i>. For details on the allowed expressions, see the <code>MLton User Guide</code>. Multiple <code>-keep</code> expressions are not allowed.</dd>
<dt><code>-mlmon </code><i>file</i></dt>
<dd> Process the list of whitespace-separated <code>mlmon.out</code> files found in the specified file.</dd>
<dt><code>-raw </code><i>{</i><code>false</code>|<code>true</code>}</dt>
<dd> Show the raw counts in addition to the percentages.</dd>
<dt><code>-show-line </code><i>{</i><code>false</code>|<code>true</code>}</dt>
<dd> Show the file and line for each function.</dd>
<dt><code>-split </code><i>regexp</i></dt>
<dd> Treat duplicates of functions whose name matches <i>regexp</i> as different functions.</dd>
<dt><code>-thresh </code><i>x</i></dt>
<dd> An abbreviation for <code>-keep &#8216;(thresh x)&#8217;</code>, which only prints information about functions whose percentage is greater than or equal to <code>x</code>, where 0 &lt;= <code>x</code> &lt;= 100.0.</dd>
<dt><code>-tolerant </code><i>{</i><code>false</code>|<code>true</code>}</dt>
<dd> Print a warning about broken <code>mlmon.out</code> files, but do not exit.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mlton/">mlton</a></code>(1) and the <code>MLton Guide</code>. </p>
