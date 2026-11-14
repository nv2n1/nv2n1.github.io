---
title: "testlintianhelper(3)"
name: "testlintianhelper"
section: "3"
letter: "t"
url: "/docs/linux/man/3-testlintianhelper/"
description: "Test::Lintian::Helper — Helper functions for various testing parts"
---

<p>Test::Lintian::Helper &#8212; Helper functions for various testing parts </p>
<h2>Synopsis</h2>
<pre> use Test::Lintian::Helper qw(get_latest_policy);
 my $policy_version = get_latest_policy();</pre>
<h2>Description</h2>
<p>Helper functions for preparing and running Lintian tests.</p>
<h2>Functions</h2>
<dl COMPACT>
<dt><code>cache_dpkg_architecture_values()</code></p>
<dd>Ensures that the output from dpkg-architecture has been cached.</p>
<dt><code>get_latest_policy()</code></p>
<dd>Returns a list with two elements. The first is the most recent version of the Debian policy. The second is its effective date.</p>
<dt><code>get_recommended_debhelper_version()</code></p>
<dd>Returns the version of debhelper recommended in &#8216;debhelper/compat-level&#8217; via Lintian::Data, relative to the established <font SIZE="-1">LINTIAN_ROOT.</font></p>
<dt><code>get_required_debhelper_version()</code></p>
<dd>Returns the version of debhelper required in the file &#8216;debian/control&#8217; relative to the established <font SIZE="-1">LINTIAN_ROOT.</font> The return value is the exact string, which can include characters like a tilde.</p>
<dt>copy_dir_contents(<font SIZE="-1">SRC_DIR, TARGET_DIR</font>)</p>
<dd>Populates <font SIZE="-1">TARGET_DIR</font> with files/dirs from <font SIZE="-1">SRC_DIR,</font> preserving all attributes but dereferencing links. For an empty directory, no dummy file is required.</p>
<dt>rfc822date(<font SIZE="-1">EPOCH</font>)</p>
<dd>Returns a string with the date and time described by <font SIZE="-1">EPOCH,</font> formatted according to <font SIZE="-1">RFC822.</font> </p>
</dl>
