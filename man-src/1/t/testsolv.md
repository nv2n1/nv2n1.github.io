---
title: "testsolv(1)"
name: "testsolv"
section: "1"
letter: "t"
url: "/docs/linux/man/1-testsolv/"
description: "testsolv – run a libsolv testcase through the solver"
---

<h2 class="name">NAME</h2>
<p> testsolv &#8211; run a libsolv testcase through the solver </p>
<h2>SYNOPSIS</h2>
<p> <code>testsolv</code> [<i>OPTIONS</i>] <i>TESTCASE</i></p>
<h2>DESCRIPTION</h2>
<p> The testsolv tools can be used to run a testcase. Testcases can either be manually created to test specific features, or they can be written by libsolv&#8217;s testcase_write function. This is useful to evaluate bug reports about the solver. </p>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Increase the debug level of the solver. This option can be specified multiple times to further increase the amount of debug data.</dl>
<p> <code>-r</code></p>
<dl>
<dt>
<dd> Write the output in testcase format instead of human readable text. The output can then be used in the result section of the test case. If the <code>-r</code> option is given twice, the output is formated for verbatim inclusion.</dl>
<p> <code>-l</code> <i>PKGSPEC</i></p>
<dl>
<dt>
<dd> Instead of running the solver, list packages in the repositories.</dl>
<p> <code>-s</code> <i>SOLUTIONSPEC</i></p>
<dl>
<dt>
<dd> This is used in the solver test suite to test the calculated solutions to encountered problems.</dl>
<h2>AUTHOR</h2>
<p> Michael Schroeder &lt;mls [at] suse.de&gt; </p>
<h2>Index</h2>
