---
title: "deb-override(5)"
name: "deb-override"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-override/"
description: "deb-override – Debian archive override file"
---

<p>deb-override &#8211; Debian archive override file</p>
<h2>Synopsis</h2>
<p><code>override</code></p>
<h2>Description</h2>
<p>While most information about a package can be found in the control file, some is managed centrally by the distribution czars rather than by the maintainer in order to offer some global consistency. This information is found in the override file. </p>
<p> The override file has a simple whitespace-delimited format. Comments are allowed (denoted with a <code>#</code>). </p>
<dl>
<dd><i>package</i> <i>priority</i> <i>section</i> [<i>maintainer-info</i>]</dl>
<p> <i>package</i> is the name of the package. Entries in the override file for packages not found in the tree of binary packages are ignored. </p>
<p> <i>priority</i> and <i>section</i> correspond to the respective control fields available in the .deb. The allowed values are specific to each distribution archive. </p>
<p> <i>maintainer-info</i>, if present, can be either the name of a maintainer for an unconditional override, or else <i>old-maintainer</i> <code>=&gt;</code> <i>new-maintainer</i> to perform a substitution. </p>
<p> The override files used to make the official Packages lists may be found in the <i>indices</i> directory on any Debian mirror.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-dpkg-scanpackages/">dpkg-scanpackages</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-scansources/">dpkg-scansources</a></code>(1), <code><a href="/docs/linux/man/1-apt-ftparchive/">apt-ftparchive</a></code>(1). </p>
