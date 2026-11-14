---
title: "cloud-publish-image(1)"
name: "cloud-publish-image"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cloud-publish-image/"
description: "cloud-publish-image – publish a cloud image"
---

<h2>NAME</h2>
<p> cloud-publish-image &#8211; publish a cloud image </p>
<h2>SYNOPSIS</h2>
<p> <code>cloud-publish-image [OPTIONS] ARCH IMAGE BUCKET</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l|&#8211;add-launch &lt;user_id&gt;</code></p>
<dd> user_id can be &quot;all&quot;, or &quot;none&quot;</p>
<dt><code>&#8211;dry-run</code></p>
<dd> only report what would be done</p>
<dt><code>&#8211;allow-existing</code></p>
<dd> if a image is already registered simply report as if work was done</p>
<dt><code>-o|&#8211;output &lt;file&gt;</code></p>
<dd> write registered id and manifest to file</p>
<dt><code>&#8211;rename &lt;publish_path&gt;</code></p>
<dd> publish to bucket/&lt;publish_path&gt;, default: bucket/&lt;basename(image)&gt;</p>
<dt><code>-t|&#8211;type &lt;type&gt;</code></p>
<dd> type is one of kernel/ramdisk/image/auto. if type is &#8216;image&#8217;, then:<br />
&nbsp;<wbr>&nbsp;<wbr>-k | &#8211;kernel&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>k : use previously registered kernel with id&nbsp;<wbr>&#8216;k&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specify&nbsp;<wbr>&#8216;none&#8217;&nbsp;<wbr>for no kernel<br />
&nbsp;<wbr>&nbsp;<wbr>-K | &#8211;kernel-file&nbsp;<wbr>&nbsp;<wbr>f : bundle, upload, use file&nbsp;<wbr>&#8216;f&#8217;&nbsp;<wbr>as kernel<br />
&nbsp;<wbr>&nbsp;<wbr>-r | &#8211;ramdisk&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r : use previously registered ramdisk with id&nbsp;<wbr>&#8216;r&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specify&nbsp;<wbr>&#8216;none&#8217;&nbsp;<wbr>for no ramdisk<br />
&nbsp;<wbr>&nbsp;<wbr>-R | &#8211;ramdisk-file f : bundle, upload, use file&nbsp;<wbr>&#8216;f&#8217;&nbsp;<wbr>as ramdisk<br />
&nbsp;<wbr>&nbsp;<wbr>-B | &#8211;block-device-mapping m : specify block device mapping in bundle </p>
<dt><code>&#8211;save-downloaded d</code></p>
<dd> save the download image to directory &#8216;d&#8217; (applicable only if TARBALL is an URL)</p>
<dt><code>-v|&#8211;verbose</code></p>
<dd> increase verbosity </p>
<dt><code>&#8211;name &lt;name&gt;</code></p>
<dd> register image with given name. basename(publish_path) </p>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>ARCH</code></p>
<dd> Target architecture, one of i386 or x86_64</p>
<dt><code>IMAGE</code></p>
<dd> Target image to upload and register. If this is a URL, it will be downloaded.</p>
<dt><code>BUCKET</code></p>
<dd> Target bucket to publish the image to </p>
</dl>
<h2>ENVIRONMENT</h2>
<p> Behavior of this program can be modified by environment variables as described below: </p>
<dl>
<dt><code>EC2PRE</code></p>
<dd> Underlying tools will be invoked using this prefix. The default is &#8216;euca-&#8216;, which results in using tools like &#8216;euca-register&#8217; and &#8216;euca-bundle-image&#8217;. To use the ec2-api-tools or ec2-ami-tools, set EC2PRE=&#8217;ec2-&#8216; </p>
</dl>
<h2>DESCRIPTION</h2>
<p> Publish an image to a cloud </p>
<h2>AUTHOR</h2>
<p> This manpage was written by Dustin Kirkland &lt;kirkland [at] canonical.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
