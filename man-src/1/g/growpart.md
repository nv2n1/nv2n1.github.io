---
title: "growpart(1)"
name: "growpart"
section: "1"
letter: "g"
url: "/docs/linux/man/1-growpart/"
description: "growpart – extend a partition in a partition table to fill available space"
---

<h2>NAME</h2>
<p> growpart &#8211; extend a partition in a partition table to fill available space </p>
<h2>SYNOPSIS</h2>
<p> <code>growpart [OPTIONS] DISK PARTITION-NUMBER</code> </p>
<p> growpart partition<br />
rewrite partition table so that partition takes up all the space it can<br />
options:<br />
&nbsp;<wbr>-h | &#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>print Usage an exit<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;fudge F&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>if part could be resized, but change would be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>less than&nbsp;<wbr>&#8216;F&#8217;, do not resize&nbsp;<wbr>(default: 20480)<br />
&nbsp;<wbr>-N | &#8211;dry-run&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>only report what would be done, show new&nbsp;<wbr>&#8216;sfdisk -d&#8217;<br />
&nbsp;<wbr>-v | &#8211;verbose&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>increase verbosity&nbsp;<wbr>/&nbsp;<wbr>debug </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h | &#8211;help</code></p>
<dd> Show usage and exit</p>
<dt><code>-N | &#8211;dry-run</code></p>
<dd> Only report what would be done</p>
<dt><code>&#8211;fudge COUNT</code></p>
<dd> Only modify partition table if the given partition would grow more than COUNT sectors (512 bytes). The default value is 20480 indicating that no change will be made unless more than 10M of space would be gained.</p>
<dt><code>-v | &#8211;verbose</code></p>
<dd> Give more information to stderr. </p>
</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>DISK</code></p>
<dd> The device or disk image to operate on</p>
<dt><code>PARTITION-NUMBER</code></p>
<dd> The number of the partition to resize (counting from 1) </p>
</dl>
<h2>DESCRIPTION</h2>
<p> Rewrite a the partition table in a disk or disk image so that the given partition takes up as much space as it can. After running, the partition will end at the end of the disk, or at the beginning of the next partition. </p>
<h2>EXAMPLES</h2>
<dl>
<dt>Extend partition 1 in /dev/sda to fill empty space until end of disk or next partitiong</p>
<dd>
growpart&nbsp;<wbr>/dev/sda 1</p>
<dt>Extend partition 2 in disk image my.image.</p>
<dd>
growpart my.image 2 </p>
</dl>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 if the partition was sucessfully grown or if &#8211;dry-run was specified and it could be grown. The exit status is 1 if the partition could not be grown due to lack of available space. The exit status is 2 if an error occured. </p>
<h2>AUTHOR</h2>
<p> This manpage was written by Scott Moser &lt;smoser [at] canonical.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 3 published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
