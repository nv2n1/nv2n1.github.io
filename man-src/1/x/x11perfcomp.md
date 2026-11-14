---
title: "x11perfcomp(1)"
name: "x11perfcomp"
section: "1"
letter: "x"
url: "/docs/linux/man/1-x11perfcomp/"
description: "x11perfcomp – X11 server performance comparison program"
---

<h2 class="name">NAME</h2>
<p> x11perfcomp &#8211; X11 server performance comparison program </p>
<h2>SYNTAX</h2>
<p> <code>x11perfcomp</code> [ -r | -ro ] [ -l label_file ] files</p>
<h2>DESCRIPTION</h2>
<p> The <i>x11perfcomp</i> program merges the output of several <i><a href="/docs/linux/man/1-x11perf/">x11perf</a>(1)</i> runs into a nice tabular format. It takes the results in each file, fills in any missing test results if necessary, and for each test shows the objects/second rate of each server. If invoked with the -r or -ro options, it shows the relative performance of each server to the first server. </p>
<p> Normally, <i>x11perfcomp</i> uses the first file specified to determine which specific tests it should report on. Some (non-DEC :) servers may fail to perform all tests. In this case, <i>x11perfcomp</i> automatically substitutes in a rate of 0.0 objects/second. Since the first file determines which tests to report on, this file must contain a superset of the tests reported in the other files, else <i>x11perfcomp</i> will fail. </p>
<p> You can provide an explicit list of tests to report on by using the -l switch to specify a file of labels. You can create a label file by using the -label option in <i>x11perf.</i></p>
<h2>OPTIONS</h2>
<p> <i>x11perfcomp</i> accepts the options listed below:</p>
<dl>
<dt><code>-r</code></p>
<dd> Specifies that the output should also include relative server performance.</p>
<dt><code>-ro</code></p>
<dd> Specifies that the output should include only relative server performance.</p>
<dt><code>-l label_file</code></p>
<dd> Specifies a label file to use.</dl>
<h2>X DEFAULTS</h2>
<p> There are no X defaults used by this program.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/7-x/">X</a>(7), <a href="/docs/linux/man/1-x11perf/">x11perf</a>(1)</p>
<h2>AUTHORS</h2>
<p> Mark Moraes wrote the original scripts to compare servers.<br />
 Joel McCormack just munged them together a bit. </p>
<h2>Index</h2>
