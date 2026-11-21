---
title: "cloud-publish-tarball(1)"
name: "cloud-publish-tarball"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cloud-publish-tarball/"
description: "cloud-publish-tarball – publish a cloud archive"
---

<h2>NAME</h2>
<p> cloud-publish-tarball &#8211; publish a cloud archive </p>
<h2>SYNOPSIS</h2>
<p> <code>cloud-publish-tarball [OPTIONS] TARFILE BUCKET [ARCH]</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-k | &#8211;kernel k</code></dt>
<dd> Use previously registered kernel with id &#8216;k&#8217; specify &#8216;none&#8217; for no kernel</dd>
<dt><code>-K | &#8211;kernel-file f</code></dt>
<dd> Bundle, upload, use file &#8216;f&#8217; as kernel</dd>
<dt><code>-q | &#8211;quiet</code></dt>
<dd> Be quiet, only output produced image ids</dd>
<dt><code>-r | &#8211;ramdisk r</code></dt>
<dd> Use previously registered ramdisk with id &#8216;r&#8217; specify &#8216;none&#8217; for no ramdisk</dd>
<dt><code>-R | &#8211;ramdisk-file f</code></dt>
<dd> Bundle, upload, use file &#8216;f&#8217; as ramdisk</dd>
<dt><code>&#8211;rename-image i</code></dt>
<dd> rename the image file before publishing (publish to &lt;bucket&gt;/i)</dd>
<dt><code>&#8211;rename-kernel k</code></dt>
<dd> rename the kernel file before publishing (publish to &lt;bucket&gt;/k)</dd>
<dt><code>&#8211;rename-ramdisk r</code></dt>
<dd> rename the ramdisk file before publishing (publish to &lt;bucket&gt;/r)</dd>
<dt><code>&#8211;save-downloaded d</code></dt>
<dd> save the download image to directory &#8216;d&#8217; (applicable only if TARBALL is an URL) </dd>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>TARFILE</code></dt>
<dd> Target archive. This may be a URL.</dd>
<dt><code>BUCKET</code></dt>
<dd> Target bucket</dd>
<dt><code>ARCH</code></dt>
<dd> Image architecture; if is not provided, a name-based attempt is made to guess </dd>
</dl>
<h2>ENVIRONMENT</h2>
<p> Behavior of this program can be modified by environment variables as described below: </p>
<dl>
<dt><code>EC2PRE</code></dt>
<dd> Underlying tools will be invoked using this prefix. The default is &#8216;euca-&#8216;, which results in using tools like &#8216;euca-register&#8217; and &#8216;euca-bundle-image&#8217;. To use the ec2-api-tools or ec2-ami-tools, set EC2PRE=&#8217;ec2-&#8216; </dd>
</dl>
<h2>DESCRIPTION</h2>
<p> Register a Ubuntu Cloud image tarball per <a rel="nofollow" href="http://cloud-images.ubuntu.com">http://cloud-images.ubuntu.com</a> </p>
<h2>EXAMPLES</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>cloud-publish-tarball lucid-cloud-i386.tar.gz my-lucid-bucket i386 </p>
<h2>AUTHOR</h2>
<p> This manpage was written by Dustin Kirkland &lt;kirkland [at] canonical.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
