---
title: "scsi_readcap(8)"
name: "scsi_readcap"
section: "8"
letter: "s"
url: "/docs/linux/man/8-scsi_readcap/"
description: "scsi_readcap – do SCSI READ CAPACITY command on disks"
---

<p>scsi_readcap &#8211; do SCSI READ CAPACITY command on disks</p>
<h2>Synopsis</h2>
<p><code>scsi_readcap</code> [<i>&#8211;brief</i>] [<i>&#8211;help</i>] [<i>&#8211;long</i>] [<i>&#8211;verbose</i>] <i>DEVICE</i> [<i>DEVICE</i>]*</p>
<h2>Description</h2>
<p>This bash shell script calls the sg_readcap utility on each given <i>DEVICE</i>. This will send a SCSI READ CAPACITY command to each <i>DEVICE</i>. </p>
<p> The default action of this script is to send the 10 byte cdb READ CAPACITY(10) command to each <i>DEVICE</i>. If a response indicates the number of blocks is greater than or equal to &#8216;2**32 &#8211; 1&#8217; then the READ CAPACITY(16) is sent and its response is output.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;brief</code></p>
<dd>shortens the output to two hexadecimal numbers, both prefixed by &#8216;0x&#8217;. The first number is the number of blocks available and the second is the size of each blocks in bytes (e.g. &#8216;0x12a19eb0 0x200&#8217;). If an error is detected &#8216;0x0 0x0&#8217; is output and the script continues if there are more <i>DEVICE</i>s.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print out the usage message then exit.</p>
<dt><code>-l</code>, <code>&#8211;long</code></p>
<dd>the default is to send the READ CAPACITY(10) command (i.e. the 10 byte cdb variant). When this option is given the READ CAPACITY(16) command is sent. The latter command yields more information in its response.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase level or verbosity.</dl>
<h2>Exit Status</h2>
<p>The exit status of this script is 0 when it is successful. Otherwise the exit status is that of the last sg_readcap utility called. See the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by D. Gilbert</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2009-2013 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_readcap (sg3_utils)</code> </p>
