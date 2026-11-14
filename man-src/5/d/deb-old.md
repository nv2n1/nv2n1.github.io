---
title: "deb-old(5)"
name: "deb-old"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-old/"
description: "deb-old – old style Debian binary package format"
---

<p>deb-old &#8211; old style Debian binary package format</p>
<h2>Synopsis</h2>
<p><i>filename</i><code>.deb</code></p>
<h2>Description</h2>
<p>The <code>.deb</code> format is the Debian binary package file format. This manual page describes the <code>old</code> format, used before Debian 0.93. Please see <code><a href="/docs/linux/man/5-deb/">deb</a></code>(5) for details of the new format.</p>
<h2>Format</h2>
<p>The file is two lines of format information as <font SIZE="-1">ASCII</font> text, followed by two concatenated gzipped ustar files. </p>
<p> The first line is the format version number padded to 8 digits, and is <code>0.939000</code> for all old-format archives. </p>
<p> The second line is a decimal string (without leading zeroes) giving the length of the first gzipped tarfile. </p>
<p> Each of these lines is terminated with a single newline character. </p>
<p> The first tarfile contains the control information, as a series of ordinary files. The file <code>control</code> must be present, as it contains the core control information. </p>
<p> In some very old archives, the files in the control tarfile may optionally be in a <font SIZE="-1"><code>DEBIAN</code></font> subdirectory. In that case, the <font SIZE="-1"><code>DEBIAN</code></font> subdirectory will be in the control tarfile too, and the control tarfile will have only files in that directory. Optionally the control tarfile may contain an entry for &#8216;<code>.</code>&#8216;, that is, the current directory. </p>
<p> The second gzipped tarfile is the filesystem archive, containing pathnames relative to the root directory of the system to be installed on. The pathnames do not have leading slashes.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-deb/">deb</a></code>(5), <code><a href="/docs/linux/man/1-dpkg-deb/">dpkg-deb</a></code>(1), <code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5). </p>
