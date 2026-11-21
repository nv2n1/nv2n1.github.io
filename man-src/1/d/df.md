---
title: "df(1)"
name: "df"
section: "1"
letter: "d"
url: "/docs/linux/man/1-df/"
description: "df – report file system disk space usage"
---

<h2>SYNOPSIS</h2>
<p> <code>df</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the GNU version of <code>df</code>. <code>df</code> displays the amount of disk space available on the file system containing each file name argument. If no file name is given, the space available on all currently mounted file systems is shown. Disk space is shown in 1K blocks by default, unless the environment variable POSIXLY_CORRECT is set, in which case 512-byte blocks are used. </p>
<p> If an argument is the absolute file name of a disk device node containing a mounted file system, <code>df</code> shows the space available on that file system rather than on the file system containing the device node. This version of <code>df</code> cannot show the space available on unmounted file systems, because on most kinds of systems doing so requires very nonportable intimate knowledge of file system structures.</p>
<h2>OPTIONS</h2>
<p> Show information about the file system on which each FILE resides, or all file systems by default. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> include pseudo, duplicate, inaccessible file systems</dd>
<dt><code>-B</code>, <code>&#8211;block-size</code>=<i>,SIZE/</i></dt>
<dd> scale sizes by SIZE before printing them; e.g., &#8216;-BM&#8217; prints sizes in units of 1,048,576 bytes; see SIZE format below</dd>
<dt><code>-h</code>, <code>&#8211;human-readable</code></dt>
<dd> print sizes in powers of 1024 (e.g., 1023M)</dd>
<dt><code>-H</code>, <code>&#8211;si</code></dt>
<dd> print sizes in powers of 1000 (e.g., 1.1G)</dd>
<dt><code>-i</code>, <code>&#8211;inodes</code></dt>
<dd> list inode information instead of block usage</dd>
<dt><code>-k</code></dt>
<dd> like <code>&#8211;block-size</code>=<i>,1K/</i></dd>
<dt><code>-l</code>, <code>&#8211;local</code></dt>
<dd> limit listing to local file systems</dd>
<dt><code>&#8211;no-sync</code></dt>
<dd> do not invoke sync before getting usage info (default)</dd>
<dt><code>&#8211;output</code>[=<i>,FIELD_LIST/</i>]</dt>
<dd> use the output format defined by FIELD_LIST, or print all fields if FIELD_LIST is omitted.</dd>
<dt><code>-P</code>, <code>&#8211;portability</code></dt>
<dd> use the POSIX output format</dd>
<dt><code>&#8211;sync</code></dt>
<dd> invoke sync before getting usage info</dd>
<dt><code>&#8211;total</code></dt>
<dd> elide all entries insignificant to available space, and produce a grand total</dd>
<dt><code>-t</code>, <code>&#8211;type</code>=<i>,TYPE/</i></dt>
<dd> limit listing to file systems of type TYPE</dd>
<dt><code>-T</code>, <code>&#8211;print-type</code></dt>
<dd> print file system type</dd>
<dt><code>-x</code>, <code>&#8211;exclude-type</code>=<i>,TYPE/</i></dt>
<dd> limit listing to file systems not of type TYPE</dd>
<dt><code>-v</code></dt>
<dd> (ignored)</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> Display values are in units of the first available SIZE from <code>&#8211;block-size</code>, and the DF_BLOCK_SIZE, BLOCK_SIZE and BLOCKSIZE environment variables. Otherwise, units default to 1024 bytes (or 512 if POSIXLY_CORRECT is set). </p>
<p> The SIZE argument is an integer and optional unit (example: 10K is 10*1024). Units are K,M,G,T,P,E,Z,Y (powers of 1024) or KB,MB,&#8230; (powers of 1000). Binary prefixes can be used, too: KiB=K, MiB=M, and so on. </p>
<p> FIELD_LIST is a comma-separated list of columns to be included. Valid field names are: &#8216;source&#8217;, &#8216;fstype&#8217;, &#8216;itotal&#8217;, &#8216;iused&#8217;, &#8216;iavail&#8217;, &#8216;ipcent&#8217;, &#8216;size&#8217;, &#8216;used&#8217;, &#8216;avail&#8217;, &#8216;pcent&#8217;, &#8216;file&#8217; and &#8216;target&#8217; (see info page).</p>
<h2>AUTHOR</h2>
<p> Written by Torbjorn Granlund, David MacKenzie, and Paul Eggert.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/df">https://www.gnu.org/software/coreutils/df</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) df invocation&#8217; </p>
