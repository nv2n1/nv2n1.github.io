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
<p> <code>cloud-publish-image [OPTIONS] ARCH IMAGE BUCKET</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l|&#8211;add-launch &lt;user_id&gt;</code></dt>
<dd> user_id can be &quot;all&quot;, or &quot;none&quot;</dd>
<dt><code>&#8211;dry-run</code></dt>
<dd> only report what would be done</dd>
<dt><code>&#8211;allow-existing</code></dt>
<dd> if a image is already registered simply report as if work was done</dd>
<dt><code>-o|&#8211;output &lt;file&gt;</code></dt>
<dd> write registered id and manifest to file</dd>
<dt><code>&#8211;rename &lt;publish_path&gt;</code></dt>
<dd> publish to bucket/&lt;publish_path&gt;, default: bucket/&lt;basename(image)&gt;</dd>
<dt><code>-t|&#8211;type &lt;type&gt;</code></dt>
<dd> type is one of kernel/ramdisk/image/auto. if type is &#8216;image&#8217;, then:<br />
&nbsp;<wbr>&nbsp;<wbr>-k | &#8211;kernel&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>k : use previously registered kernel with id&nbsp;<wbr>&#8216;k&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specify&nbsp;<wbr>&#8216;none&#8217;&nbsp;<wbr>for no kernel<br />
&nbsp;<wbr>&nbsp;<wbr>-K | &#8211;kernel-file&nbsp;<wbr>&nbsp;<wbr>f : bundle, upload, use file&nbsp;<wbr>&#8216;f&#8217;&nbsp;<wbr>as kernel<br />
&nbsp;<wbr>&nbsp;<wbr>-r | &#8211;ramdisk&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>r : use previously registered ramdisk with id&nbsp;<wbr>&#8216;r&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specify&nbsp;<wbr>&#8216;none&#8217;&nbsp;<wbr>for no ramdisk<br />
&nbsp;<wbr>&nbsp;<wbr>-R | &#8211;ramdisk-file f : bundle, upload, use file&nbsp;<wbr>&#8216;f&#8217;&nbsp;<wbr>as ramdisk<br />
&nbsp;<wbr>&nbsp;<wbr>-B | &#8211;block-device-mapping m : specify block device mapping in bundle </dd>
<dt><code>&#8211;save-downloaded d</code></dt>
<dd> save the download image to directory &#8216;d&#8217; (applicable only if TARBALL is an URL)</dd>
<dt><code>-v|&#8211;verbose</code></dt>
<dd> increase verbosity </dd>
<dt><code>&#8211;name &lt;name&gt;</code></dt>
<dd> register image with given name. basename(publish_path) </dd>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>ARCH</code></dt>
<dd> Target architecture, one of i386 or x86_64</dd>
<dt><code>IMAGE</code></dt>
<dd> Target image to upload and register. If this is a URL, it will be downloaded.</dd>
<dt><code>BUCKET</code></dt>
<dd> Target bucket to publish the image to </dd>
</dl>
<h2>ENVIRONMENT</h2>
<p> Behavior of this program can be modified by environment variables as described below: </p>
<dl>
<dt><code>EC2PRE</code></dt>
<dd> Underlying tools will be invoked using this prefix. The default is &#8216;euca-&#8216;, which results in using tools like &#8216;euca-register&#8217; and &#8216;euca-bundle-image&#8217;. To use the ec2-api-tools or ec2-ami-tools, set EC2PRE=&#8217;ec2-&#8216; </dd>
</dl>
<p> Publish an image to a cloud </p>
<h2>AUTHOR</h2>
<p> This manpage was written by Dustin Kirkland &lt;kirkland [at] canonical.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
