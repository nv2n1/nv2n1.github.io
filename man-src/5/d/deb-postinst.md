---
title: "deb-postinst(5)"
name: "deb-postinst"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-postinst/"
description: "deb-postinst – package post-installation maintainer script"
---

<p>deb-postinst &#8211; package post-installation maintainer script</p>
<h2>Synopsis</h2>
<p><code>DEBIAN/postinst</code></p>
<h2>Description</h2>
<p>A package can perform several post-installation actions via maintainer scripts, by including an executable <i>postinst</i> file in its control archive (i.e. <i>DEBIAN/postinst</i> during package creation). </p>
<p> The script can be called in the following ways:</p>
<dl>
<dt><i>postinst</i> <code>configure</code> <i>old-version</i></p>
<dd>After the package was installed.</p>
<dt><i>postinst</i> <code>triggered</code> &quot;<i>trigger-name&#8230;</i>&quot;</p>
<dd>After the package was triggered. The list of space-separated <i>trigger-name</i>s is passed as the second argument.</p>
<dt><i>old-postinst</i> <code>abort-upgrade</code> <i>new-version</i></p>
<dd>If <i>prerm</i> fails during upgrade or fails on failed upgrade.</p>
<dt><i>old-postinst</i> <code>abort-remove</code></p>
<dd>If <i>prerm</i> fails during removal.</p>
<dt><i>postinst</i> <code>abort-deconfigure in-favour</code> <i>new-package new-version</i></p>
<dd>
<dt>       [ <code>removing</code> <i>old-package old-version</i> ]</p>
<dd>If <i>prerm</i> fails during deconfiguration of a package.</p>
<dt><i>postinst</i> <code>abort-remove in-favour</code> <i>new-package new-version</i></p>
<dd>If <i>prerm</i> fails during replacement due to conflict.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). </p>
