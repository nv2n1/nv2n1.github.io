---
title: "deb-split(5)"
name: "deb-split"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-split/"
description: "deb-split – Debian multi-part binary package format"
---

<p>deb-split &#8211; Debian multi-part binary package format</p>
<h2>Synopsis</h2>
<p><i>filename</i><code>.deb</code></p>
<h2>Description</h2>
<p>The multi-part <code>.deb</code> format is used to split big packages into smaller pieces to ease transport in small media.</p>
<h2>Format</h2>
<p>The file is an <code>ar</code> archive with a magic value of <code>!&lt;arch&gt;</code>. The file names might contain a trailing slash (since dpkg 1.15.6). </p>
<p> The first member is named <code>debian-split</code> and contains a series of lines, separated by newlines. Currently eight lines are present:</p>
<dl>
<dt>&bull;</p>
<dd>The format version number, <code>2.1</code> at the time this manual page was written.</p>
<dt>&bull;</p>
<dd>The package name.</p>
<dt>&bull;</p>
<dd>The package version.</p>
<dt>&bull;</p>
<dd>The md5sum of the package.</p>
<dt>&bull;</p>
<dd>The total size of the package.</p>
<dt>&bull;</p>
<dd>The maximum part size.</p>
<dt>&bull;</p>
<dd>The current part number, followed by a slash and the total amount of parts (as in &#8216;1/10&#8217;).</p>
<dt>&bull;</p>
<dd>The package architecture (since dpkg 1.16.1).</dl>
<p> Programs which read multi-part archives should be prepared for the minor format version number to be increased and additional lines to be present, and should ignore these if this is the case. </p>
<p> If the major format version number has changed, an incompatible change has been made and the program should stop. If it has not, then the program should be able to safely continue, unless it encounters an unexpected member in the archive (except at the end), as described below. </p>
<p> The second, last required member is named <code>data.</code><i>N</i>, where <i>N</i> denotes the part number. It contains the raw part data. </p>
<p> These members must occur in this exact order. Current implementations should ignore any additional members after <code>data.</code><i>N</i>. Further members may be defined in the future, and (if possible) will be placed after these two.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-deb/">deb</a></code>(5), <code><a href="/docs/linux/man/1-dpkg-split/">dpkg-split</a></code>(1). </p>
