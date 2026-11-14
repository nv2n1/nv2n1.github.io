---
title: "sigfind(1)"
name: "sigfind"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sigfind/"
description: "sigfind – Find a binary signature in a file"
---

<h2 class="name">NAME</h2>
<p> sigfind &#8211; Find a binary signature in a file </p>
<h2>SYNOPSIS</h2>
<p> <code>sigfind [-b</code> <i>bsize</i> <code>] [-o</code> <i>offset</i> <code>] [-t</code> <i>template</i> <code>] [-lV] [</code> <i>hex_signature</i> <code>]</code> <i>file</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>sigfind</code> searches through a file and looks for the hex_signature at a given offset. This can be used to search for lost boot sectors, superblocks, and partition tables. </p>
<h2>ARGUMENTS</h2>
<dl>
<dt>-b bsize</p>
<dd> Specify the block size in which to search. The default is 512 and the value must be a multiple of 512.</p>
<dt>-o offset</p>
<dd> Specify the offset in a block in which the signature must exist. The default is 0.</p>
<dt>-t template</p>
<dd> Specify a template name that defines the signature value and offset. Run with no options to get a list of supported templates.</p>
<dt>-l</p>
<dd> The signature is stored in little-endian ordering and must therefore be reversed.</p>
<dt>-V</p>
<dd> Display version</p>
<dt>[hex_signature]</p>
<dd> The binary signature that you are searching for. It must be given in hexadecimal format. This argument must exist if -t is not used.</p>
<dt>file</p>
<dd> Any raw data. </p>
</dl>
<h2>EXAMPLES</h2>
<p> sigfind -o 510 -l AA55 disk.dd </p>
<p> sigfind -t fat disk.dd </p>
<h2>AUTHOR</h2>
<p> Brian Carrier &lt;carrier at sleuthkit dot org&gt; </p>
<p> Send documentation updates to &lt;doc-updates at sleuthkit dot org&gt; </p>
<h2>Index</h2>
