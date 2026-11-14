---
title: "checkisomd5(1)"
name: "checkisomd5"
section: "1"
letter: "c"
url: "/docs/linux/man/1-checkisomd5/"
description: "checkisomd5 — check an MD5 checksum implanted by implantisomd5"
---

<h2>NAME</h2>
<p> checkisomd5 &#8212; check an MD5 checksum implanted by <code>implantisomd5</code></p>
<h2>SYNOPSIS</h2>
<p> <code>checkisomd5</code> [<code>&#8211;md5sumonly</code>] [<code>&#8211;verbose</code>] [<code>&#8211;gauge</code>] [isofilename | blockdevice ]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>checkisomd5</code> command. <code>checkisomd5</code> is a program that checks an embedded MD5 checksum in a ISO9660 image (.iso), or block device. The checksum is embedded by the corresponding <code>implantisomd5</code> command. </p>
<p> The check can be aborted by pressing Esc key.</p>
<h2>EXIT STATUS</h2>
<p> Program returns exit status 0 if the checksum is correct, 1 if the checksum is incorrect or non-existent, or 2 if the check was aborted.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;md5sumonly</code></p>
<dd> Do not check the target. Instead, output human-readable information about the target&#8217;s checksums.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Display human-readable progress as the target is checked. Without this option, nothing is outputted except errors.</p>
<dt><code>&#8211;gauge</code></p>
<dd> Display a series of numbers from 0 to 100, corresponding to check progress. This output can be piped to <code>dialog &#8211;gauge</code> for a user-friendly progress bar.</dl>
<h2>SEE ALSO</h2>
<p> implantisomd5 (1). </p>
<h2>Index</h2>
