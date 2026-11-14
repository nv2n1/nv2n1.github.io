---
title: "gnustep-tests(1)"
name: "gnustep-tests"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnustep-tests/"
description: "gnustep-tests – script to run a GNUstep testsuite"
---

<h2>NAME</h2>
<p> gnustep-tests &#8211; script to run a GNUstep testsuite</p>
<h2>SYNOPSIS</h2>
<p> <code>gnustep-tests</code> [ <i>directory</i> | <i>test.m</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <code>gnustep-tests</code> runs the specified tests, or any tests found in the directory. If no arguments are given, the current directory and its subdirectories are scanned and processed accordingly.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;documentation</code></p>
<dd> prints full details about the testing framework </p>
<dt><code>&#8211;clean</code></p>
<dd> deletes old logs and any leftover files </p>
<dt><code>&#8211;failfast</code></p>
<dd> stops after the first encountered test failure </p>
<dt><code>&#8211;debug</code></p>
<dd> runs any failed tests in <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1) </p>
<dt><code>&#8211;developer</code></p>
<dd> treats any hopes as real tests </p>
<dt><code>&#8211;verbose</code></p>
<dd> detailed log output </p>
<dt><code>&#8211;sequential</code></p>
<dd> disables parallel building</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gnustep/">GNUstep</a></code>(7)</p>
<h2>AUTHORS</h2>
<p> <code>gnustep-tests</code> was written by Alexander Malmberg &lt;alexander [at] malmberg.org&gt; and Richard Frith-Macdonald &lt;rfm [at] gnu.org&gt;. </p>
<p> This man page was written by Yavor Doganov &lt;yavor [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2014 Free Software Foundation, Inc. </p>
<p> Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved. </p>
<h2>Index</h2>
