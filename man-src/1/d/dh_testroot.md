---
title: "dh_testroot(1)"
name: "dh_testroot"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_testroot/"
description: "dh_testroot – ensure that a package is built with necessary level of root permissions"
---

<h2 class="name">NAME</h2>
<p> dh_testroot &#8211; ensure that a package is built with necessary level of root permissions </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_testroot</code> [<i>debhelper options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_testroot</code> is used to determine if the package has access to at least the level of root access that it declared it needed via the Rules-Requires-Root (R³) field. </p>
<p> The following is how <code>dh_testroot</code> behaves based on the effective value of the R³ field:</p>
<dl>
<dt>&quot;binary-targets&quot;</p>
<dd> <code>dh_testroot</code> asserts that it is run as root or under <i><a href="/docs/linux/man/1-fakeroot/">fakeroot</a></i>(1).</p>
<dt>&quot;no&quot;</p>
<dd> <code>dh_testroot</code> returns successfully.</p>
<dt>Any other value than the above</p>
<dd> <code>dh_testroot</code> asserts that it is either run as root (or under <i><a href="/docs/linux/man/1-fakeroot/">fakeroot</a></i>(1)) or the builder has provided the <font SIZE="-1"><code>DEB_GAIN_ROOT_CMD</code></font> environment variable (e.g. via dpkg-buildpackage -r).</dl>
<p> For backwards compatibility, <code>dh_testroot</code> will consider the absence of the R³ field as if the R³ field was set to &#8220;binary-targets&#8221;.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
