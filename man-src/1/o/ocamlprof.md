---
title: "ocamlprof(1)"
name: "ocamlprof"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocamlprof/"
description: "ocamlprof – The OCaml profiler"
---

<h2 class="name">NAME</h2>
<p> ocamlprof &#8211; The OCaml profiler</p>
<h2>SYNOPSIS</h2>
<p> <code>ocamlprof</code> [ <i>options</i> ] <i>filename &#8230;</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code>ocamlprof</code> command prints execution counts gathered during the execution of a OCaml program instrumented with <code><a href="/docs/linux/man/1-ocamlcp/">ocamlcp</a></code>(1). </p>
<p> It produces a source listing of the program modules given as arguments where execution counts have been inserted as comments. For instance, </p>
<p> <code>ocamlprof foo.ml</code> </p>
<p> prints the source code for the foo module, with comments indicating how many times the functions in this module have been called. Naturally, this information is accurate only if the source file has not been modified since the profiling execution took place. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i>&nbsp;<wbr>dumpfile</i></p>
<dd> Specifies an alternate dump file of profiling information.</p>
<dt><code>-F</code><i>&nbsp;<wbr>string</i></p>
<dd> Specifies an additional string to be output with profiling information. By default, <code><a href="/docs/linux/man/1-ocamlprof/">ocamlprof</a></code>(1) will annotate programs with comments of the form <code>(*</code><i>&nbsp;<wbr>n</i><code>&nbsp;<wbr>*)</code> where <i>n</i> is the counter value for a profiling point. With option <code>-F</code><i>&nbsp;<wbr>s</i> the annotation will be <code>(*</code><i>&nbsp;<wbr>sn</i><code>&nbsp;<wbr>*)</code></p>
<dt><code>-impl</code><i>&nbsp;<wbr>filename</i></p>
<dd> Compile the file <i>filename</i> as an implementation file, even if its extension is not .ml.</p>
<dt><code>-intf</code><i>&nbsp;<wbr>filename</i></p>
<dd> Compile the file <i>filename</i> as an interface file, even if its extension is not .mli.</p>
<dt><code>-version</code></p>
<dd> Print version string and exit.</p>
<dt><code>-vnum</code></p>
<dd> Print short version number and exit.</p>
<dt><code>-help</code>&nbsp;<wbr>or<code>&nbsp;<wbr>&#8211;help</code></p>
<dd> Display a short usage summary and exit. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ocamlcp/">ocamlcp</a></code>(1).<br />
 <i>The OCaml user&#8217;s manual</i>, chapter &quot;Profiling&quot;. </p>
<h2>Index</h2>
