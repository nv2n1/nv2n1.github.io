---
title: "dpkgbuildprofiles(3)"
name: "dpkgbuildprofiles"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dpkgbuildprofiles/"
description: "Dpkg::BuildProfiles – handle build profiles"
---

<p>Dpkg::BuildProfiles &#8211; handle build profiles </p>
<h2>Description</h2>
<p>The Dpkg::BuildProfiles module provides functions to handle the build profiles.</p>
<h2>Functions</h2>
<dl COMPACT>
<dt>my @profiles = <i>get_build_profiles()</i></p>
<dd>Get an array with the currently active build profiles, taken from the environment variable <font SIZE="-1"><code>DEB_BUILD_PROFILES</code></font>.</p>
<dt>set_build_profiles(@profiles)</p>
<dd>Set <tt>@profiles</tt> as the current active build profiles, by setting the environment variable <font SIZE="-1"><code>DEB_BUILD_PROFILES</code></font>.</p>
<dt>my @profiles = parse_build_profiles($string)</p>
<dd>Parses a build profiles specification, into an array of array references.</p>
<dt>evaluate_restriction_formula(\@formula, \@profiles)</p>
<dd>Evaluate whether a restriction formula of the form &#8220;&lt;foo bar&gt; &lt;baz&gt;&#8221;, given as a nested array, is true or false, given the array of enabled build profiles.</dl>
<h2>Changes</h2>
<h3>Version 1.00</h3>
<p>Mark the module as public.</p>
