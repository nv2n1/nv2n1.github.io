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
<dt>bs=BYTES</p>
<dd> read and write up to BYTES bytes at a time (default: 512); overrides ibs and obs</p>
<dt>cbs=BYTES</p>
<dd> convert BYTES bytes at a time</p>
<dt>conv=CONVS</p>
<dd> convert the file as per the comma separated symbol list</p>
<dt>count=N</p>
<dd> copy only N input blocks</p>
<dt>ibs=BYTES</p>
<dd> read up to BYTES bytes at a time (default: 512)</p>
<dt>if=FILE</p>
<dd> read from FILE instead of stdin</p>
<dt>iflag=FLAGS</p>
<dd> read as per the comma separated symbol list</p>
<dt>obs=BYTES</p>
<dd> write BYTES bytes at a time (default: 512)</p>
<dt>of=FILE</p>
<dd> write to FILE instead of stdout</p>
<dt>oflag=FLAGS</p>
<dd> write as per the comma separated symbol list</p>
<dt>seek=N</p>
<dd> skip N obs-sized blocks at start of output</p>
<dt>skip=N</p>
<dd> skip N ibs-sized blocks at start of input</p>
<dt>status=LEVEL</p>
<dd> The LEVEL of information to print to stderr; &#8216;none&#8217; suppresses everything but error messages, &#8216;noxfer&#8217; suppresses the final transfer statistics, &#8216;progress&#8217; shows periodic transfer statistics</dl>
<p> N and BYTES may be followed by the following multiplicative suffixes: c=1, w=2, b=512, kB=1000, K=1024, MB=1000*1000, M=1024*1024, xM=M, GB=1000*1000*1000, G=1024*1024*1024, and so on for T, P, E, Z, Y. Binary prefixes can be used, too: KiB=K, MiB=M, and so on. </p>
<p> Each CONV symbol may be:</p>
<dl>
<dt>ascii</p>
<dd> from EBCDIC to ASCII</p>
<dt>ebcdic</p>
<dd> from ASCII to EBCDIC</p>
<dt>ibm</p>
<dd> from ASCII to alternate EBCDIC</p>
<dt>block</p>
<dd> pad newline-terminated records with spaces to cbs-size</p>
<dt>unblock</p>
<dd> replace trailing spaces in cbs-size records with newline</p>
<dt>lcase</p>
<dd> change upper case to lower case</p>
<dt>ucase</p>
<dd> change lower case to upper case</p>
<dt>sparse</p>
<dd> try to seek rather than write all-NUL output blocks</p>
<dt>swab</p>
<dd> swap every pair of input bytes</p>
<dt>sync</p>
<dd> pad every input block with NULs to ibs-size; when used with block or unblock, pad with spaces rather than NULs</p>
<dt>excl</p>
<dd> fail if the output file already exists</p>
<dt>nocreat</p>
<dd> do not create the output file</p>
<dt>notrunc</p>
<dd> do not truncate the output file</p>
<dt>noerror</p>
<dd> continue after read errors</p>
<dt>fdatasync</p>
<dd> physically write output file data before finishing</p>
<dt>fsync</p>
<dd> likewise, but also write metadata</dl>
<p> Each FLAG symbol may be:</p>
<dl>
<dt>append</p>
<dd> append mode (makes sense only for output; conv=notrunc suggested)</p>
<dt>direct</p>
<dd> use direct I/O for data</p>
<dt>directory</p>
<dd> fail unless a directory</p>
<dt>dsync</p>
<dd> use synchronized I/O for data</p>
<dt>sync</p>
<dd> likewise, but also for metadata</p>
<dt>fullblock</p>
<dd> accumulate full blocks of input (iflag only)</p>
<dt>nonblock</p>
<dd> use non-blocking I/O</p>
<dt>noatime</p>
<dd> do not update access time</p>
<dt>nocache</p>
<dd> Request to drop cache. See also oflag=sync</p>
<dt>noctty</p>
<dd> do not assign controlling terminal from file</p>
<dt>nofollow</p>
<dd> do not follow symlinks</p>
<dt>count_bytes</p>
<dd> treat &#8216;count=N&#8217; as a byte count (iflag only)</p>
<dt>skip_bytes</p>
<dd> treat &#8216;skip=N&#8217; as a byte count (iflag only)</p>
<dt>seek_bytes</p>
<dd> treat &#8216;seek=N&#8217; as a byte count (oflag only)</dl>
<p> Sending a USR1 signal to a running &#8216;dd&#8217; process makes it print I/O statistics to standard error and then resume copying. </p>
<p> Options are:</p>
<dl>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
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
