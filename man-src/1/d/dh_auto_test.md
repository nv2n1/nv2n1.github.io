---
title: "dh_auto_test(1)"
name: "dh_auto_test"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_auto_test/"
description: "dh_auto_test – automatically runs a package’s test suites"
---

<h2 class="name">NAME</h2>
<p> dh_auto_test &#8211; automatically runs a package&#8217;s test suites </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_auto_test</code> [<i>build system options</i>] [<i>debhelper options</i>] [<code>&#8212;</code> <i>params</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_auto_test</code> is a debhelper program that tries to automatically run a package&#8217;s test suite. It does so by running the appropriate command for the build system it detects the package uses. For example, if there&#8217;s a Makefile and it contains a <code>test</code> or <code>check</code> target, then this is done by running <code>make</code> (or <font SIZE="-1"><code>MAKE</code></font>, if the environment variable is set). If the test suite fails, the command will exit nonzero. If there&#8217;s no test suite, it will exit zero without doing anything. </p>
<p> This is intended to work for about 90% of packages with a test suite. If it doesn&#8217;t work, you&#8217;re encouraged to skip using <code>dh_auto_test</code> at all, and just run the test suite manually.</p>
<h2>OPTIONS</h2>
<p> See &quot;<font SIZE="-1"><code>BUILD SYSTEM OPTIONS</code></font>&quot; in <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) for a list of common build system selection and control options.</p>
<dl>
<dt><code>&#8212;</code> <i>params</i></p>
<dd> Pass <i>params</i> to the program that is run, after the parameters that <code>dh_auto_test</code> usually passes.</dl>
<h2>NOTES</h2>
<p> If the <font SIZE="-1"><code>DEB_BUILD_OPTIONS</code></font> environment variable contains <code>nocheck</code>, no tests will be performed.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
