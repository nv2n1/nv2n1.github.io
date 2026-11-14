---
title: "testlintianrun(3)"
name: "testlintianrun"
section: "3"
letter: "t"
url: "/docs/linux/man/3-testlintianrun/"
description: "Test::Lintian::Run — generic runner for all suites"
---

<p>Test::Lintian::Run &#8212; generic runner for all suites </p>
<h2>Synopsis</h2>
<pre> use Test::Lintian::Run qw(runner);
 my $runpath = &quot;test working directory&quot;;
 runner($runpath);</pre>
<h2>Description</h2>
<p>Generic test runner for all Lintian test suites</p>
<h2>Functions</h2>
<dl COMPACT>
<dt>logged_runner(<font SIZE="-1">RUN_PATH</font>)</p>
<dd>Starts the generic test runner for the test located in <font SIZE="-1">RUN_PATH</font> and logs the output.</p>
<dt>runner(<font SIZE="-1">RUN_PATH</font>)</p>
<dd>This routine provides the basic structure for all runners and runs the test located in <font SIZE="-1">RUN_PATH.</font></p>
<dt>check_literal</p>
<dd>
<dt>check_tags</p>
<dd>
<dt>check_result(<font SIZE="-1">DESC, EXPECTED, ACTUAL</font>)</p>
<dd>This routine checks if the <font SIZE="-1">EXPECTED</font> tags match the calibrated <font SIZE="-1">ACTUAL</font> for the test described by <font SIZE="-1">DESC.</font> For some additional checks, also need the <font SIZE="-1">ORIGINAL</font> tags before calibration. Returns a list of errors, if there are any.</dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
