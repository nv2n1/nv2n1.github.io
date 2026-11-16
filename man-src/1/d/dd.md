---
title: "dd(1)"
name: "dd"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dd/"
description: "dd – convert and copy a file"
---

<h2 class="name">NAME</h2>
<p> dd &#8211; convert and copy a file </p>
<h2>SYNOPSIS</h2>
<p> <code>dd</code> [<i>,OPERAND/</i>]&#8230;<br />
 <code>dd</code> <i>,OPTION/</i></p>
<h2>DESCRIPTION</h2>
<p> Copy a file, converting and formatting according to the operands.</p>
<dl>
<dt>bs=BYTES</dt>
<dd> read and write up to BYTES bytes at a time (default: 512); overrides ibs and obs</dd>
<dt>cbs=BYTES</dt>
<dd> convert BYTES bytes at a time</dd>
<dt>conv=CONVS</dt>
<dd> convert the file as per the comma separated symbol list</dd>
<dt>count=N</dt>
<dd> copy only N input blocks</dd>
<dt>ibs=BYTES</dt>
<dd> read up to BYTES bytes at a time (default: 512)</dd>
<dt>if=FILE</dt>
<dd> read from FILE instead of stdin</dd>
<dt>iflag=FLAGS</dt>
<dd> read as per the comma separated symbol list</dd>
<dt>obs=BYTES</dt>
<dd> write BYTES bytes at a time (default: 512)</dd>
<dt>of=FILE</dt>
<dd> write to FILE instead of stdout</dd>
<dt>oflag=FLAGS</dt>
<dd> write as per the comma separated symbol list</dd>
<dt>seek=N</dt>
<dd> skip N obs-sized blocks at start of output</dd>
<dt>skip=N</dt>
<dd> skip N ibs-sized blocks at start of input</dd>
<dt>status=LEVEL</dt>
<dd> The LEVEL of information to print to stderr; &#8216;none&#8217; suppresses everything but error messages, &#8216;noxfer&#8217; suppresses the final transfer statistics, &#8216;progress&#8217; shows periodic transfer statistics</dd></dl>
<p> N and BYTES may be followed by the following multiplicative suffixes: c=1, w=2, b=512, kB=1000, K=1024, MB=1000*1000, M=1024*1024, xM=M, GB=1000*1000*1000, G=1024*1024*1024, and so on for T, P, E, Z, Y. Binary prefixes can be used, too: KiB=K, MiB=M, and so on. </p>
<p> Each CONV symbol may be:</p>
<dl>
<dt>ascii</dt>
<dd> from EBCDIC to ASCII</dd>
<dt>ebcdic</dt>
<dd> from ASCII to EBCDIC</dd>
<dt>ibm</dt>
<dd> from ASCII to alternate EBCDIC</dd>
<dt>block</dt>
<dd> pad newline-terminated records with spaces to cbs-size</dd>
<dt>unblock</dt>
<dd> replace trailing spaces in cbs-size records with newline</dd>
<dt>lcase</dt>
<dd> change upper case to lower case</dd>
<dt>ucase</dt>
<dd> change lower case to upper case</dd>
<dt>sparse</dt>
<dd> try to seek rather than write all-NUL output blocks</dd>
<dt>swab</dt>
<dd> swap every pair of input bytes</dd>
<dt>sync</dt>
<dd> pad every input block with NULs to ibs-size; when used with block or unblock, pad with spaces rather than NULs</dd>
<dt>excl</dt>
<dd> fail if the output file already exists</dd>
<dt>nocreat</dt>
<dd> do not create the output file</dd>
<dt>notrunc</dt>
<dd> do not truncate the output file</dd>
<dt>noerror</dt>
<dd> continue after read errors</dd>
<dt>fdatasync</dt>
<dd> physically write output file data before finishing</dd>
<dt>fsync</dt>
<dd> likewise, but also write metadata</dd></dl>
<p> Each FLAG symbol may be:</p>
<dl>
<dt>append</dt>
<dd> append mode (makes sense only for output; conv=notrunc suggested)</dd>
<dt>direct</dt>
<dd> use direct I/O for data</dd>
<dt>directory</dt>
<dd> fail unless a directory</dd>
<dt>dsync</dt>
<dd> use synchronized I/O for data</dd>
<dt>sync</dt>
<dd> likewise, but also for metadata</dd>
<dt>fullblock</dt>
<dd> accumulate full blocks of input (iflag only)</dd>
<dt>nonblock</dt>
<dd> use non-blocking I/O</dd>
<dt>noatime</dt>
<dd> do not update access time</dd>
<dt>nocache</dt>
<dd> Request to drop cache. See also oflag=sync</dd>
<dt>noctty</dt>
<dd> do not assign controlling terminal from file</dd>
<dt>nofollow</dt>
<dd> do not follow symlinks</dd>
<dt>count_bytes</dt>
<dd> treat &#8216;count=N&#8217; as a byte count (iflag only)</dd>
<dt>skip_bytes</dt>
<dd> treat &#8216;skip=N&#8217; as a byte count (iflag only)</dd>
<dt>seek_bytes</dt>
<dd> treat &#8216;seek=N&#8217; as a byte count (oflag only)</dd></dl>
<p> Sending a USR1 signal to a running &#8216;dd&#8217; process makes it print I/O statistics to standard error and then resume copying. </p>
<p> Options are:</p>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<h2>AUTHOR</h2>
<p> Written by Paul Rubin, David MacKenzie, and Stuart Kemp.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/dd">https://www.gnu.org/software/coreutils/dd</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) dd invocation&#8217; </p>
<h2>Index</h2>
