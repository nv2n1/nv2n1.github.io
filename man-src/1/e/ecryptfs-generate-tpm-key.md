---
title: "ecryptfs-generate-tpm-key(1)"
name: "ecryptfs-generate-tpm-key"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ecryptfs-generate-tpm-key/"
description: "ecryptfs-generate-tpm-key – generate an eCryptfs key for TPM hardware."
---

<h2 class="name">NAME</h2>
<p> ecryptfs-generate-tpm-key &#8211; generate an eCryptfs key for TPM hardware.</p>
<h2>SYNOPSIS</h2>
<p> <code>ecryptfs-generate-tpm-key -p PCR </code> [-p PCR]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>ecryptfs-generate-tpm-key</code> is a utility to generate a sealing (storage) key bound to a specified set of PCRs values in the current TPM&#8217;s PCR&#8217;s. </p>
<h2>EXAMPLE</h2>
<p> ecryptfs-generate-tpm-key -p 0 -p 2 -p 3 </p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/7-ecryptfs/">ecryptfs</a></code>(7)</p>
<dd>
<dt><i>/usr/share/doc/ecryptfs-utils/ecryptfs-faq.html</i></p>
<dd>
<dt><i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i></p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> This manpage was written by Dustin Kirkland &lt;kirkland [at] ubuntu.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
