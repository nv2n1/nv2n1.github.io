---
title: "llvm-locstats-14(1)"
name: "llvm-locstats-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-locstats-14/"
description: "llvm-locstats – calculate statistics on DWARF debug location"
---

<h2 class="name">NAME</h2>
<p> llvm-locstats &#8211; calculate statistics on DWARF debug location </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-locstats</code> [<i>options</i>] [<i>filename</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-locstats</code> works like a wrapper around <code>llvm-dwarfdump</code>. It parses <code>llvm-dwarfdump</code> statistics regarding debug location by pretty printing it in a more human readable way. </p>
<p> The line 0% shows the number and the percentage of DIEs with no location information, but the line 100% shows the information for DIEs where there is location information in all code section bytes (where the variable or parameter is in the scope). The line [50%,60%) shows the number and the percentage of DIEs where the location information is between 50 and 60 percentage of its scope covered.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;only-variables</code></p>
<dd> calculate the location statistics only for local variables</p>
<dt><code>&#8211;only-formal-parameters</code></p>
<dd> calculate the location statistics only for formal parameters</p>
<dt><code>&#8211;ignore-debug-entry-values</code></p>
<dd> ignore the location statistics on locations containing the debug entry values DWARF operation</p>
<dt><code>&#8211;draw-plot</code></p>
<dd> make histogram of location buckets generated (requires matplotlib)</p>
<dt><code>&#8211;compare</code></p>
<dd> compare the debug location coverage on two files provided, and draw a plot showing the difference (requires matplotlib)</dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-locstats</code> returns 0 if the input file were parsed successfully. Otherwise, it returns 1.</p>
<h2>EXAMPLE 1</h2>
<p> Pretty print the location coverage on the standard output. </p>
<pre><code>
llvm-locstats a.out
  =================================================
            Debug Location Statistics
  =================================================
        cov%          samples       percentage(~)
  -------------------------------------------------
     0%                    1              16%
     (0%,10%)              0               0%
     [10%,20%)             0               0%
     [20%,30%)             0               0%
     [30%,40%)             0               0%
     [40%,50%)             0               0%
     [50%,60%)             1              16%
     [60%,70%)             0               0%
     [70%,80%)             0               0%
     [80%,90%)             1              16%
     [90%,100%)            0               0%
     100%                  3              50%
  =================================================
  -the number of debug variables processed: 6
  -PC ranges covered: 81%
  -------------------------------------------------
  -total availability: 83%
  =================================================
</code></pre>
<h2>EXAMPLE 2</h2>
<p> Generate a plot as an image file. </p>
<pre>
llvm-locstats --draw-plot file1.out
</pre>
<p> [image]</p>
<h2>EXAMPLE 3</h2>
<p> Generate a plot as an image file showing the difference in the debug location coverage. </p>
<pre>
llvm-locstats --compare file1.out file1.withentryvals.out
</pre>
<p> [image]</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-llvm-dwarfdump/">llvm-dwarfdump</a>(1)</code></p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
