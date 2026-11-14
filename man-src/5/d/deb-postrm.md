---
title: "deb-postrm(5)"
name: "deb-postrm"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-postrm/"
description: "deb-postrm – package post-removal maintainer script"
---

<p>deb-postrm &#8211; package post-removal maintainer script</p>
<h2>Synopsis</h2>
<p><code>DEBIAN/postrm</code></p>
<h2>Description</h2>
<p>A package can perform several post-removal actions via maintainer scripts, by including an executable <i>postrm</i> file in its control archive (i.e. <i>DEBIAN/postrm</i> during package creation). </p>
<p> The script can be called in the following ways:</p>
<dl>
<dt><i>postrm</i> <code>remove</code></p>
<dd>After the package was removed.</p>
<dt><i>postrm</i> <code>purge</code></p>
<dd>After the package was purged.</p>
<dt><i>old-postrm</i> <code>upgrade</code> <i>new-version</i></p>
<dd>After the package was upgraded.</p>
<dt><i>new-postrm</i> <code>failed-upgrade</code> <i>old-version</i> <i>new-version</i></p>
<dd>If the above <code>upgrade</code> call fails. </p>
<p> The <i>new-version</i> is passed only since dpkg 1.18.5.</p>
<dt><i>postrm</i> <code>disappear</code> <i>overwriter-package</i> <i>overwriter-version</i></p>
<dd>After all of the packages files have been replaced.</p>
<dt><i>new-postrm</i> <code>abort-install</code></p>
<dd>If <i>preinst</i> fails during install.</p>
<dt><i>new-postrm</i> <code>abort-install</code> <i>old-version new-version</i></p>
<dd>If <i>preinst</i> fails during upgrade of removed package. </p>
<p> The <i>new-version</i> is passed only since dpkg 1.18.5.</p>
<dt><i>new-postrm</i> <code>abort-upgrade</code> <i>old-version new-version</i></p>
<dd>If <i>preinst</i> fails during upgrade. </p>
<p> The <i>new-version</i> is passed only since dpkg 1.18.5.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). </p>
