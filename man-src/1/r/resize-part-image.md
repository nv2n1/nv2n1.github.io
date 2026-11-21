---

title: "resize-part-image(1)"
name: "resize-part-image"
section: "1"
letter: "r"
url: "/docs/linux/man/1-resize-part-image/"
description: "resize-part-image – resize a partition image"
---

<h2>NAME</h2>
<p> resize-part-image &#8211; resize a partition image </p>
<p> <code>resize-part-image [ options ] IMAGE SIZE [OUTPUT]</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v | &#8211;verbose</code></dt>
<dd> show output of resize and fsck commands</dd>
<dt><code>IMAGE</code></dt>
<dd> Target file for resizing</dd>
<dt><code>SIZE</code></dt>
<dd> New size is specified per <a href="/docs/linux/man/8-resize2fs/">resize2fs</a>(8), e.g. &quot;1G&quot; for 1 gigabyte</dd>
<dt><code>[OUTPUT]</code></dt>
<dd> If OUTPUT filname is given, do not modify &#8216;IMAGE&#8217;, but create new file &#8216;OUTPUT&#8217; </dd>
</dl>
<p> Resize a partition image to a new size. </p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/8-resize2fs/">resize2fs</a></code>(8)</dt>
<dd>
</dd></dl>
<h2>AUTHOR</h2>
<p> This manpage was written by Dustin Kirkland &lt;kirkland [at] canonical.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
