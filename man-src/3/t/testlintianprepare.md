---
title: "testlintianprepare(3)"
name: "testlintianprepare"
section: "3"
letter: "t"
url: "/docs/linux/man/3-testlintianprepare/"
description: "Test::Lintian::Prepare — routines to prepare the work directories"
---

<p>Test::Lintian::Prepare &#8212; routines to prepare the work directories </p>
<h2>Synopsis</h2>
<pre> use Test::Lintian::Prepare qw(prepare);</pre>
<h2>Description</h2>
<p>The routines in this module prepare the work directories in which the tests are run. To do so, they use the specifications in the test set.</p>
<h2>Functions</h2>
<dl COMPACT>
<dt>prepare(<font SIZE="-1">SPEC_PATH, SOURCE_PATH, TEST_SET, REBUILD</font>)</p>
<dd>Populates a work directory <font SIZE="-1">SOURCE_PATH</font> with data from the test located in <font SIZE="-1">SPEC_PATH.</font> The optional parameter <font SIZE="-1">REBUILD</font> forces a rebuild if true.</p>
<dt>filleval(<font SIZE="-1">SPEC_PATH, EVAL_PATH, TEST_SET, REBUILD</font>)</p>
<dd>Populates a evaluation directory <font SIZE="-1">EVAL_PATH</font> with data from the test located in <font SIZE="-1">SPEC_PATH.</font> The optional parameter <font SIZE="-1">REBUILD</font> forces a rebuild if true.</p>
<dt>combine_fields</p>
<dd>
<dt>fill_hash_from_hash</p>
<dd></dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
