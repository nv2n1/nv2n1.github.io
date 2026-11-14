---
title: "mogautomount(1)"
name: "mogautomount"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mogautomount/"
description: "mogautomount – automatically discover and mount MogileFS disks"
---

<h2 class="name">NAME</h2>
<p> mogautomount &#8211; automatically discover and mount MogileFS disks </p>
<h2>SYNOPSIS</h2>
<pre><code>
mogautomount[--verbose | -v] mogautomount[--help | -h]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Mounts all unmounted filesystems with labels of form &#8220;MogileDev&lt;n&gt;&#8221; at /var/mogdata/dev&lt;n&gt;, creating the needed directories as well. </p>
<p> You can do this at runtime without restarting mogstored, assuming you can add new block devices at runtime via your SCSI/SATA/etc controller.</p>
<h2>OPTIONS</h2>
<dl>
<dt>&#8211;help | -h</p>
<dd> this help</p>
<dt>&#8211;verbose | -verbose</p>
<dd> be verbose</p>
<dt>&#8211;chmod-mountpoints</p>
<dd> If a mogile device isn&#8217;t mounted yet, check to make sure the underlying filesystem has the directory set to be not readable or writable at all (chmod 0). This could help prevent mogstored from accidentally writing to the underlying filesystem.</dl>
<h2>RETURN CODE</h2>
<p> 0 on success or inaction because no action needed to happen. </p>
<p> 1 on partial failure (some mounts succeed). </p>
<p> 2 on total failure (things had to be done, but nothing was).</p>
<h2>AUTHOR</h2>
<p> Brad Fitzpatrick, &lt;brad [at] danga.com&gt;</p>
<h2>WARRANTY, BUGS, DISCLAIMER</h2>
<p> This tool mounts disks, and disks hold data, so naturally you should be afraid. Real the source code to see what it does. This tool comes with no warranty of any kind. You&#8217;re response for its use or misuse.</p>
<h2>COPYRIGHT &amp; LICENSE</h2>
<p> This tool is Copyright 2006, Six Apart, Ltd. You&#8217;re free to redistribute it under the same terms as perl itself.</p>
<h2>POD ERRORS</h2>
<p> Hey! <code>The above document had some coding errors, which are explained below:</code></p>
<dl>
<dt>Around line 134:</p>
<dd> &#8216;=end&#8217; without a target? </p>
</dl>
<h2>Index</h2>
