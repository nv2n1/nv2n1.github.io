---
title: "cifsdd(8)"
name: "cifsdd"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cifsdd/"
description: "cifsdd – convert and copy a file over SMB"
---

<p>cifsdd &#8211; convert and copy a file over SMB</p>
<h2>Synopsis</h2>
<dl>
<dd>cifsdd [OPERAND]&#8230; <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt></p>
<dd>cifsdd OPTION</dl>
<h2>Description</h2>
<p>This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> Copy a file, converting and formatting according to the operands. </p>
<p> bs=BYTES</p>
<dl>
<dd>read and write up to BYTES bytes at a time (default: 4096)</dl>
<p> ibs=BYTES</p>
<dl>
<dd>read up to BYTES bytes at a time (default: 4096)</dl>
<p> obs=BYTES</p>
<dl>
<dd>write BYTES bytes at a time (default: 4096)</dl>
<p> if=FILE</p>
<dl>
<dd>read from FILE instead of stdin</dl>
<p> of=FILE</p>
<dl>
<dd>write to FILE instead of stdout</dl>
<p> count=N</p>
<dl>
<dd>copy only N input blocks</dl>
<p> seek=N</p>
<dl>
<dd>skip N obs-sized blocks at start of output</dl>
<p> skip=N</p>
<dl>
<dd>skip N ibs-sized blocks at start of input</dl>
<p> direct</p>
<dl>
<dd>use direct I/O for data</dl>
<p> sync</p>
<dl>
<dd>use synchronous writes</dl>
<p> oplock</p>
<dl>
<dd>take oplocks on the input and output files</dl>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The cifsdd manpage was written by Andreas Schneider.</p>
