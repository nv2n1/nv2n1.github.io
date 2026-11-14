---
title: "crc32(1)"
name: "crc32"
section: "1"
letter: "c"
url: "/docs/linux/man/1-crc32/"
description: "crc32 – compute CRC-32 checksums for the given files"
---

<h2 class="name">NAME</h2>
<p> crc32 &#8211; compute CRC-32 checksums for the given files </p>
<h2>SYNOPSIS</h2>
<p> <code>crc32</code> <i>filename</i> [ <i>filename</i> &#8230; ]</p>
<h2>DESCRIPTION</h2>
<p> <code>crc32</code> is a simple utility that calculates the CRC-32 checksum for each of the given files. </p>
<p> Note that the CRC-32 checksum is merely used for error detection in transmission and storage. It is not intended to guard against the malicious modification of files (i.e., it is not a cryptographic hash). </p>
<p> This utility is supplied with the <code>Archive::Zip</code> module for Perl.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="//www.systutorials.com/docs/linux/man/3pm-Archive::Zip/">Archive::Zip</a></code>(3pm).</p>
<h2>AUTHOR</h2>
<p> The Archive::Zip module was written by Ned Konz.<br />
 This manual page was prepared by Ben Burton &lt;bab [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
