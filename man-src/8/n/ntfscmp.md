---
title: "ntfscmp(8)"
name: "ntfscmp"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntfscmp/"
description: "ntfscmp – compare two NTFS filesystems and tell the differences"
---

<p>ntfscmp &#8211; compare two NTFS filesystems and tell the differences</p>
<h2>Synopsis</h2>
<p><code>ntfscmp</code> [<i>OPTIONS</i>] <i>DEVICE1</i> <i>DEVICE2</i></p>
<h2>Description</h2>
<p>The <code>ntfscmp</code> program makes a comparison between two NTFS filesystems from all aspects and reports all variances it finds. The filesystems can be on block devices or images files. Ntfscmp can be used for volume verification however its primary purpose was to be an efficient development tool, used to quickly locate, identify and check the correctness of the metadata changes made to NTFS. </p>
<p> If one is interested only in the NTFS metadata changes then it could be useful to compare the metadata images created by using the &#8211;metadata option of <code><a href="/docs/linux/man/8-ntfsclone/">ntfsclone</a></code>(8) to eliminate the usually uninteresting timestamp changes. </p>
<p> The terse output of <code>ntfscmp</code> is intentional because the provided information is enough in each case to determine the exact differences. This can be achieved, for instance, if one compares the verbose outputs of <code><a href="/docs/linux/man/8-ntfsinfo/">ntfsinfo</a></code>(8) for each reported inodes by the <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1) utility.</p>
<h2>Options</h2>
<p>Below is a summary of the options that <code>ntfscmp</code> accepts.</p>
<dl>
<dt><code>-P</code>, <code>&#8211;no-progress-bar</code></p>
<dd>Don&#8217;t show progress bars.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>More informational output.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Display help and exit.</dl>
<h2>Exit Codes</h2>
<p>The exit code is 0 on success, non-zero otherwise.</p>
<h2>Known Issues</h2>
<p>No problem is known. If you would find otherwise then please send your report to the development team: ntfs-3g-devel [at] lists.sf.net</p>
<h2>Author</h2>
<p><code>ntfscmp</code> was written by Szabolcs Szakacsits. It was ported to ntfs-3g by Erik Larsson.</p>
<h2>Availability</h2>
<p><code>ntfscmp</code> is part of the <code>ntfs-3g</code> package and is available from:<br />
 <a rel="nofollow" href="https://github.com/tuxera/ntfs-3g/wiki/">https://github.com/tuxera/ntfs-3g/wiki/</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ntfsinfo/">ntfsinfo</a></code>(8), <code><a href="/docs/linux/man/8-ntfscat/">ntfscat</a></code>(8), <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1), <code><a href="/docs/linux/man/8-ntfsclone/">ntfsclone</a></code>(8), <code><a href="/docs/linux/man/8-ntfsprogs/">ntfsprogs</a></code>(8) </p>
