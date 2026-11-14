---
title: "deb-preinst(5)"
name: "deb-preinst"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-preinst/"
description: "deb-preinst – package pre-installation maintainer script"
---

<p>deb-preinst &#8211; package pre-installation maintainer script</p>
<h2>Synopsis</h2>
<p><code>DEBIAN/preinst</code></p>
<h2>Description</h2>
<p>A package can perform several pre-installation actions via maintainer scripts, by including an executable <i>preinst</i> file in its control archive (i.e. <i>DEBIAN/preinst</i> during package creation). </p>
<p> The script can be called in the following ways:</p>
<dl>
<dt><i>new-preinst</i> <code>install</code></p>
<dd>Before the package is installed.</p>
<dt><i>new-preinst</i> <code>install</code> <i>old-version new-version</i></p>
<dd>Before removed package is upgraded. </p>
<p> The <i>new-version</i> is passed only since dpkg 1.18.5.</p>
<dt><i>new-preinst</i> <code>upgrade</code> <i>old-version new-version</i></p>
<dd>Before the package is upgraded. </p>
<p> The <i>new-version</i> is passed only since dpkg 1.18.5.</p>
<dt><i>old-preinst</i> <code>abort-upgrade</code> <i>new-version</i></p>
<dd>If <i>postrm</i> fails during upgrade or fails on failed upgrade.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). </p>
