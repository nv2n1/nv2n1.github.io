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
<dt><code>-v, &#8211;version</code></dt>
<dd> Prints out the makeself version number and exits.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print out help information.</dd>
<dt><code>&#8211;gzip</code></dt>
<dd> Compress using gzip (default if detected).</dd>
<dt><code>&#8211;bzip2</code></dt>
<dd> Compress using bzip2.</dd>
<dt><code>&#8211;pbzip2</code></dt>
<dd> Compress using pbzip2.</dd>
<dt><code>&#8211;xz</code></dt>
<dd> Compress using xz.</dd>
<dt><code>&#8211;compress</code></dt>
<dd> Compress using the UNIX &#8216;compress&#8217; command.</dd>
<dt><code>&#8211;nocomp</code></dt>
<dd> Do not compress the data.</dd>
<dt><code>&#8211;complevel lvl</code></dt>
<dd> Specify the compression level for gzip,bzip2,pbzui2 or xz</dd>
<dt><code>&#8211;notemp</code></dt>
<dd> The archive will create archive_dir in the current directory and uncompress in ./archive_dir.</dd>
<dt><code>&#8211;copy</code></dt>
<dd> Upon extraction, the archive will first copy itself to a temporary directory.</dd>
<dt><code>&#8211;append</code></dt>
<dd> Append more files to an existing makeself archive. The label and startup scripts will then be ignored.</dd>
<dt><code>&#8211;current</code></dt>
<dd> Files will be extracted to the current directory. Both &#8211;current and &#8211;target dir imply &#8211;notemp.</dd>
<dt><code>&#8211;target dir</code></dt>
<dd> Extract directly to a target directory. Directory path can be either absolute or relative.</dd>
<dt><code>&#8211;header file</code></dt>
<dd> Specify location of the header script.</dd>
<dt><code>&#8211;follow</code></dt>
<dd> Follow the symlinks in the archive.</dd>
<dt><code>&#8211;noprogress</code></dt>
<dd> Do not show the progress during the decompression.</dd>
<dt><code>&#8211;nox11</code></dt>
<dd> Disable automatic spawn of an xterm if running in X11.</dd>
<dt><code>&#8211;nowait</code></dt>
<dd> Do not wait for user input after executing embedded program from an xterm.</dd>
<dt><code>&#8211;nomd5</code></dt>
<dd> Do not create a MD5 checksum for the archive.</dd>
<dt><code>&#8211;nocrc</code></dt>
<dd> Do not create a CRC32 checksum for the archive.</dd>
<dt><code>&#8211;lsm file</code></dt>
<dd> LSM file describing the package.</dd></dl>
<h2>AUTHORS</h2>
<p> Makeself has been written by Stéphane Peter &lt;megastep [at] megastep.org&gt;. This man page was originally written by Bartosz Fenski &lt;fenio [at] o2.pl&gt; for the Debian GNU/Linux distribution (but it may be used by others). </p>
