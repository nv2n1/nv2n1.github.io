---
title: "mt-gnu(1)"
name: "mt-gnu"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mt-gnu/"
description: "mt – control magnetic tape drive operation"
---

<h2 class="name">NAME</h2>
<p> mt &#8211; control magnetic tape drive operation </p>
<h2>SYNOPSIS</h2>
<p> <code>mt</code> [<code>-V</code>] [<code>-f</code> <i>device</i>] [<code>&#8211;file=</code><i>device</i>] [<code>&#8211;rsh-command=</code><i>command</i>] [<code>&#8211;version</code>] <i>operation</i> [<i>count</i>]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the GNU version of <code>mt</code>. <code>mt</code> performs the given <i>operation</i>, which must be one of the tape operations listed below, on a tape drive. </p>
<p> The default tape device to operate on is taken from the file <code>/usr/include/sys/mtio.h</code> when <code>mt</code> is compiled. It can be overridden by giving a device file name in the environment variable <code>TAPE</code> or by a command line option (see below), which also overrides the environment variable. </p>
<p> The device must be either a character special file or a remote tape drive. To use a tape drive on another machine as the archive, use a filename that starts with `HOSTNAME:&#8217;. The hostname can be preceded by a username and an `@&#8217; to access the remote tape drive as that user, if you have permission to do so (typically an entry in that user&#8217;s `~/.rhosts&#8217; file). </p>
<p> The available operations are listed below. Unique abbreviations are accepted. Not all operations are available on all systems, or work on all types of tape drives. Some operations optionally take a repeat count, which can be given after the operation name and defaults to 1.</p>
<dl>
<dt><code>eof</code>, <code>weof</code></dt>
<dd> Write <i>count</i> EOF marks at current position.</dd>
<dt><code>fsf</code></dt>
<dd> Forward space <i>count</i> files. The tape is positioned on the first block of the next file.</dd>
<dt><code>bsf</code></dt>
<dd> Backward space <i>count</i> files. The tape is positioned on the first block of the next file.</dd>
<dt><code>fsr</code></dt>
<dd> Forward space <i>count</i> records.</dd>
<dt><code>bsr</code></dt>
<dd> Backward space <i>count</i> records.</dd>
<dt><code>bsfm</code></dt>
<dd> Backward space <i>count</i> file marks. The tape is positioned on the beginning-of-the-tape side of the file mark.</dd>
<dt><code>fsfm</code></dt>
<dd> Forward space <i>count</i> file marks. The tape is positioned on the beginning-of-the-tape side of the file mark.</dd>
<dt><code>asf</code></dt>
<dd> Absolute space to file number <i>count</i>. Equivalent to rewind followed by fsf <i>count</i>.</dd>
<dt><code>seek</code></dt>
<dd> Seek to block number <i>count</i>.</dd>
<dt><code>eom</code></dt>
<dd> Space to the end of the recorded media on the tape (for appending files onto tapes).</dd>
<dt><code>rewind</code></dt>
<dd> Rewind the tape.</dd>
<dt><code>offline</code>, <code>rewoffl</code></dt>
<dd> Rewind the tape and, if applicable, unload the tape.</dd>
<dt><code>status</code></dt>
<dd> Print status information about the tape unit.</dd>
<dt><code>retension</code></dt>
<dd> Rewind the tape, then wind it to the end of the reel, then rewind it again.</dd>
<dt><code>erase</code></dt>
<dd> Perform long erase of tape. If <i>count</i> is 0, perform short erase of tape (some devices do not support this).</dd></dl>
<p> <code>mt</code> exits with a status of 0 if the operation succeeded, 1 if the operation or device name given was invalid, or 2 if the operation failed.</p>
<h3>OPTIONS</h3>
<dl>
<dt><code>-f</code>, <code>&#8211;file=</code><i>device</i></dt>
<dd> Use <i>device</i> as the file name of the tape drive to operate on. To use a tape drive on another machine, use a filename that starts with `HOSTNAME:&#8217;. The hostname can be preceded by a username and an `@&#8217; to access the remote tape drive as that user, if you have permission to do so (typically an entry in that user&#8217;s `~/.rhosts&#8217; file).</dd>
<dt><code>&#8211;rsh-command=</code><i>command</i></dt>
<dd> Notifies <code>mt</code> that it should use <i>command</i> to communicate with remote devices instead of <code>/usr/bin/ssh</code> or <code>/usr/bin/rsh</code>.</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print the version number of <code>mt</code>.</dd></dl>
<h2>BUG REPORTS</h2>
<p> Report bugs to &lt;bug-cpio [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2014 Free Software Foundation, Inc.<br />
 License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law. </p>
