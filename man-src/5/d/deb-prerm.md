---
title: "deb-prerm(5)"
name: "deb-prerm"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-prerm/"
description: "deb-prerm – package pre-removal maintainer script"
---

<p>deb-prerm &#8211; package pre-removal maintainer script</p>
<h2>Synopsis</h2>
<p><code>DEBIAN/prerm</code></p>
<h2>Description</h2>
<p>A package can perform several pre-removal actions via maintainer scripts, by including an executable <i>prerm</i> file in its control archive (i.e. <i>DEBIAN/prerm</i> during package creation). </p>
<p> The script can be called in the following ways:</p>
<dl>
<dt><i>prerm</i> <code>remove</code></p>
<dd>Before the package is removed.</p>
<dt><i>old-prerm</i> <code>upgrade</code> <i>new-version</i></p>
<dd>Before an upgrade.</p>
<dt><i>new-prerm</i> <code>failed-upgrade</code> <i>old-version new-version</i></p>
<dd>If the above <code>upgrade</code> fails. </p>
<p> The <i>new-version</i> is passed only since dpkg 1.18.5.</p>
<dt><i>prerm</i> <code>deconfigure in-favour</code> <i>new-package new-version</i></p>
<dd>
<dt>    [ <code>removing</code> <i>old-package old-version</i> ]</p>
<dd>Before package is deconfigured while dependency is replaced due to conflict.</p>
<dt><i>prerm</i> <code>remove in-favour</code> <i>new-package new-version</i></p>
<dd>Before the package is replaced due to conflict.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). </p>
