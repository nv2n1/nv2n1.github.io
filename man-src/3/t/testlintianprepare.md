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
<dt>prepare(SPEC_PATH, SOURCE_PATH, TEST_SET, REBUILD)</dt>
<dd>Populates a work directory SOURCE_PATH with data from the test located in SPEC_PATH. The optional parameter REBUILD forces a rebuild if true.</dd>
<dt>filleval(SPEC_PATH, EVAL_PATH, TEST_SET, REBUILD)</dt>
<dd>Populates a evaluation directory EVAL_PATH with data from the test located in SPEC_PATH. The optional parameter REBUILD forces a rebuild if true.</dd>
<dt>combine_fields</dt>
<dd>
</dd><dt>fill_hash_from_hash</dt>
<dd></dd></dl>
<h2>Author</h2>
<p>Originally written by Felix Lechner &lt;felix.lechner [at] lease-up.com&gt; for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
