---
title: "deb-md5sums(5)"
name: "deb-md5sums"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-md5sums/"
description: "deb-md5sums – package MD5 file digests"
---

<p>deb-md5sums &#8211; package MD5 file digests</p>
<h2>Synopsis</h2>
<p><code>DEBIAN/md5sums</code></p>
<h2>Description</h2>
<p>A package declares the <font SIZE="-1">MD5</font> digests for the package file contents by including an <i>md5sums</i> file in its control archive (i.e. <i>DEBIAN/md5sums</i> during package creation). This file is used for integrity verification and deduplication purposes, and not for any kind of security purpose. </p>
<p> This file contains a list of <font SIZE="-1">MD5</font> digests (as 32 case-insensitive hexadecimal characters) followed by two spaces (U+0020 <font SIZE="-1"><code>SPACE</code></font>) and the absolute pathname of a plain file, one per line. </p>
<p> Trailing slashes (U+002F <code>/</code>) in the pathname will be trimmed. Neither trailing whitespace nor empty or whitespace-only lines are accepted. </p>
<p> If the control file does not exist in the binary package, <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1) will generate the matching information at unpack time (since <code>dpkg</code> 1.16.3).</p>
<h2>Example</h2>
<pre> 53c0d4afe4bc4eccb5cb234d2e06ef4d usr/bin/dpkg
 f8da2bc74cdcad8b81c48a4f0d7bb0a8 usr/bin/dpkg-deb
 70b913132de56e95e75de504979309b4 usr/bin/dpkg-divert
 […]</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-md5sum/">md5sum</a></code>(1), <code><a href="/docs/linux/man/1-dpkg-deb/">dpkg-deb</a></code>(1), <code><a href="/docs/linux/man/1-dpkg/">dpkg</a></code>(1). </p>
