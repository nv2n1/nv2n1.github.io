---
title: "h5unjam(1)"
name: "h5unjam"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h5unjam/"
description: "h5unjam – Extract the user block from a HDF5 file"
---

<h2>NAME</h2>
<p> h5unjam &#8211; Extract the user block from a HDF5 file</p>
<h2>SYNOPSIS</h2>
<p> <code>h5unjam</code> <code>-i</code> <i>in_file.h5</i> [<code>-u</code> <i>user_block</i> | <code>&#8211;delete</code>] [<code>-o</code> <i>out_file.h5</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>h5unjam </code> splits an HDF5 file, writing the user block to a file or stdout and the HDF5 file to an HDF5 file with a header at byte 0 (i.e., with no user block). </p>
<p> If <i>out_file.h5</i> is given, a new file is created with the <i>in_file.h5</i> without the user block. In this case, <i>infile.h5</i> is unchanged. </p>
<p> If <i>out_file.h5</i> is not specified, the <i>user_block</i> is removed and <i>in_file.h5</i> is rewritten, starting at byte 0. </p>
<p> If <i>user_block</i> is set, the user block will be written to <i>user_block</i>. If <i>user_block</i> is not set, the user block (if any) will be written to stdout. If <code>&#8211;delete</code> is selected, the user block will not be not written.</p>
<h2>EXAMPLE USAGE</h2>
<p> For an HDF5 file, <i>with_ub.h5</i>, with a user block, extract the user block to <i>user_block.txt </i> and the HDF5 file to <i>wo_ub.h5</i>. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>h5unjam -i with_ub.h5 -u user_block.txt -i wo_ub.h5</p>
<h2>RETURN VALUE</h2>
<p> <code>h5unjam</code> returns the size of the output file, or -1 if an error occurs.</p>
<h2>CAVEATS</h2>
<p> This tool copies all the data (sequentially) in the file(s) to new offsets. For a large file, this copy will take a long time. </p>
<p> The most efficient way to create a user block is to create the file with a user block (see <code>H5Pset_user_block</code>), and write the user block data into that space from a program. </p>
<p> The user block is completely opaque to the HDF5 library and to the <code>h5jam</code> and <code>h5unjam</code> tools. The user block is simply read or written as a string of bytes, which could be text or any kind of binary data. It is up to the user to know what the contents of the user block means and how to process it. </p>
<p> When the user block is extracted, all the data is written to the output, including any padding or unwritten data. </p>
<p> This tool moves the HDF5 file through byte copies, i.e., it does not read or interpret the HDF5 objects.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-h5dump/">h5dump</a></i>(1), <i><a href="/docs/linux/man/1-h5ls/">h5ls</a></i>(1), <i><a href="/docs/linux/man/1-h5diff/">h5diff</a></i>(1), <i><a href="/docs/linux/man/1-h5import/">h5import</a></i>(1), <i><a href="/docs/linux/man/1-gif2h5/">gif2h5</a></i>(1), <i><a href="/docs/linux/man/1-h52gif/">h52gif</a></i>(1), <i><a href="/docs/linux/man/1-h5perf/">h5perf</a></i>(1), <i><a href="/docs/linux/man/1-h5jam/">h5jam</a></i>(1). </p>
<h2>Index</h2>
