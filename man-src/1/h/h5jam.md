---
title: "h5jam(1)"
name: "h5jam"
section: "1"
letter: "h"
url: "/docs/linux/man/1-h5jam/"
description: "h5jam – Add a user block to a HDF5 file"
---

<h2>NAME</h2>
<p> h5jam &#8211; Add a user block to a HDF5 file</p>
<h2>SYNOPSIS</h2>
<p> <code>h5jam </code> <code>-u</code> <i>user_block</i> <code>-i</code> <i>in_file.h5</i> [<code>-o</code> <i>out_file.h5</i>] [<code>&#8211;clobber</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>h5jam</code> concatenates a <i>user_block</i> file and an HDF5 file to create an HDF5 file with a user block. The user block can be either binary or text. The output file is padded so that the HDF5 header begins on byte 512, 1024, etc.. (See the HDF5 File Format.) </p>
<p> If <i>out_file.h5</i> is given, a new file is created with the <i>user_block</i> followed by the contents of <i>in_file.h5</i>. In this case, <i>infile.h5</i> is unchanged. </p>
<p> If <i>out_file.h5</i> is not specified, the <i>user_block</i> is added to <i>in_file.h5</i>. </p>
<p> If <i>in_file.h5</i> already has a user block, the contents of <i>user_block</i> will be added to the end of the existing user block, and the file shifted to the next boundary. If <code>&#8211;clobber</code> is set, any existing user block will be overwritten.</p>
<h2>EXAMPLE USAGE</h2>
<p> Create new file, <i>newfile.h5</i>, with the text in file <i>mytext.txt</i> as the user block for the HDF5 file <i>file.h5</i>. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>h5jam -u mytext.txt -i file.h5 -o newfile.h5</p>
<p> Add text in file <i>mytext.txt</i> to front of HDF5 dataset, <i>file.h5</i>. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>h5jam -u mytext.txt -i file.h5 </p>
<p> Overwrite the user block (if any) in <i>file.h5</i> with the contents of <i>mytext.txt</i>. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>h5jam -u mytext.txt -i file.h5 &#8211;clobber</p>
<h2>RETURN VALUE</h2>
<p> <code>h5jam</code> returns the size of the output file, or -1 if an error occurs.</p>
<h2>CAVEATS</h2>
<p> This tool copies all the data (sequentially) in the file(s) to new offsets. For a large file, this copy will take a long time. </p>
<p> The most efficient way to create a user block is to create the file with a user block (see <code>H5Pset_user_block</code>), and write the user block data into that space from a program. </p>
<p> The user block is completely opaque to the HDF5 library and to the <code>h5jam</code> and <code>h5unjam</code> tools. The user block is simply read or written as a string of bytes, which could be text or any kind of binary data. It is up to the user to know what the contents of the user block means and how to process it. </p>
<p> When the user block is extracted, all the data is written to the output, including any padding or unwritten data. </p>
<p> This tool moves the HDF5 file through byte copies, i.e., it does not read or interpret the HDF5 objects.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-h5dump/">h5dump</a></i>(1), <i><a href="/docs/linux/man/1-h5ls/">h5ls</a></i>(1), <i><a href="/docs/linux/man/1-h5diff/">h5diff</a></i>(1), <i><a href="/docs/linux/man/1-h5import/">h5import</a></i>(1), <i><a href="/docs/linux/man/1-gif2h5/">gif2h5</a></i>(1), <i><a href="/docs/linux/man/1-h52gif/">h52gif</a></i>(1), <i><a href="/docs/linux/man/1-h5perf/">h5perf</a></i>(1), <i><a href="/docs/linux/man/1-h5unjam/">h5unjam</a></i>(1). </p>
<h2>Index</h2>
