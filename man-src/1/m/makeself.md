---
title: "makeself(1)"
name: "makeself"
section: "1"
letter: "m"
url: "/docs/linux/man/1-makeself/"
description: "makeself – An utility to generate self-extractable archives."
---

<h2>NAME</h2>
<p> makeself &#8211; An utility to generate self-extractable archives.</p>
<h2>SYNTAX</h2>
<p> <code>makeself [</code><i>options</i>] archive_dir file_name label <code>[</code><i>startup_script</i>] [<i>args</i>]</p>
<h2>DESCRIPTION</h2>
<p> This program is a free (GPL) utility designed to create self-extractable archives from a directory. </p>
<h2>OPTIONS</h2>
<p> The following options are supported. </p>
<dl>
<dt><code>-v, &#8211;version</code></p>
<dd> Prints out the makeself version number and exits.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print out help information.</p>
<dt><code>&#8211;gzip</code></p>
<dd> Compress using gzip (default if detected).</p>
<dt><code>&#8211;bzip2</code></p>
<dd> Compress using bzip2.</p>
<dt><code>&#8211;pbzip2</code></p>
<dd> Compress using pbzip2.</p>
<dt><code>&#8211;xz</code></p>
<dd> Compress using xz.</p>
<dt><code>&#8211;compress</code></p>
<dd> Compress using the UNIX &#8216;compress&#8217; command.</p>
<dt><code>&#8211;nocomp</code></p>
<dd> Do not compress the data.</p>
<dt><code>&#8211;complevel lvl</code></p>
<dd> Specify the compression level for gzip,bzip2,pbzui2 or xz</p>
<dt><code>&#8211;notemp</code></p>
<dd> The archive will create archive_dir in the current directory and uncompress in ./archive_dir.</p>
<dt><code>&#8211;copy</code></p>
<dd> Upon extraction, the archive will first copy itself to a temporary directory.</p>
<dt><code>&#8211;append</code></p>
<dd> Append more files to an existing makeself archive. The label and startup scripts will then be ignored.</p>
<dt><code>&#8211;current</code></p>
<dd> Files will be extracted to the current directory. Both &#8211;current and &#8211;target dir imply &#8211;notemp.</p>
<dt><code>&#8211;target dir</code></p>
<dd> Extract directly to a target directory. Directory path can be either absolute or relative.</p>
<dt><code>&#8211;header file</code></p>
<dd> Specify location of the header script.</p>
<dt><code>&#8211;follow</code></p>
<dd> Follow the symlinks in the archive.</p>
<dt><code>&#8211;noprogress</code></p>
<dd> Do not show the progress during the decompression.</p>
<dt><code>&#8211;nox11</code></p>
<dd> Disable automatic spawn of an xterm if running in X11.</p>
<dt><code>&#8211;nowait</code></p>
<dd> Do not wait for user input after executing embedded program from an xterm.</p>
<dt><code>&#8211;nomd5</code></p>
<dd> Do not create a MD5 checksum for the archive.</p>
<dt><code>&#8211;nocrc</code></p>
<dd> Do not create a CRC32 checksum for the archive.</p>
<dt><code>&#8211;lsm file</code></p>
<dd> LSM file describing the package.</dl>
<h2>AUTHORS</h2>
<p> Makeself has been written by Stéphane Peter &lt;megastep [at] megastep.org&gt;. This man page was originally written by Bartosz Fenski &lt;fenio [at] o2.pl&gt; for the Debian GNU/Linux distribution (but it may be used by others). </p>
<h2>Index</h2>
