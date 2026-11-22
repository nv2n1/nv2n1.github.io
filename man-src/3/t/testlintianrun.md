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
<dt>logged_runner(RUN_PATH)</dt>
<dd>Starts the generic test runner for the test located in RUN_PATH and logs the output.</dd>
<dt>runner(RUN_PATH)</dt>
<dd>This routine provides the basic structure for all runners and runs the test located in RUN_PATH.</dd>
<dt>check_literal</dt>
<dd>
</dd><dt>check_tags</dt>
<dd>
</dd><dt>check_result(DESC, EXPECTED, ACTUAL)</dt>
<dd>This routine checks if the EXPECTED tags match the calibrated ACTUAL for the test described by DESC. For some additional checks, also need the ORIGINAL tags before calibration. Returns a list of errors, if there are any.</dd></dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
