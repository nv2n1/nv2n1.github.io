---
title: "sg_sync(8)"
name: "sg_sync"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_sync/"
description: "sg_sync – send SCSI SYNCHRONIZE CACHE command"
---

<p>sg_sync &#8211; send SCSI SYNCHRONIZE CACHE command</p>
<h2>Synopsis</h2>
<p><code>sg_sync</code> [<i>&#8211;16</i>] [<i>&#8211;count=COUNT</i>] [<i>&#8211;group=GN</i>] [<i>&#8211;help</i>] [<i>&#8211;immed</i>] [<i>&#8211;lba=LBA</i>] [<i>&#8211;sync-nv</i>] [<i>&#8211;timeout=SECS</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Send SYNCHRONIZE CACHE(10) or SYNCHRONIZE CACHE(16) command to <i>DEVICE</i>. These commands are defined for SCSI block devices (see SBC-3). If successful these commands make sure that any blocks whose latest versions are held in cache are written to (also termed as &quot;synchronized with&quot;) the medium. </p>
<p> If the <i>LBA</i> and <i>COUNT</i> arguments are both zero (their defaults) then all blocks in the cache are synchronized. If <i>LBA</i> is greater than zero while <i>COUNT</i> is zero then blocks in the cache whose addresses are from and including <i>LBA</i> to the highest lba on the device are synchronized. If both <i>LBA</i> and <i>COUNT</i> are non zero then blocks in the cache whose addresses lie in the range <i>LBA</i> to <i>LBA</i>+<i>COUNT</i>-1 inclusive are synchronized with the medium.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-S</code>, <code>&#8211;16</code></p>
<dd>performs a SYNCHRONIZE CACHE(16) command. Default is to perform a SYNCHRONIZE CACHE(10) command.</p>
<dt><code>-c</code>, <code>&#8211;count</code>=<i>COUNT</i></p>
<dd>where <i>COUNT</i> is the number of blocks to synchronize from and including <i>LBA</i>. Default value is 0. When 0 then all blocks in the cache from and including <i>LBA</i> argument to the highest block address are synchronized.</p>
<dt><code>-g</code>, <code>&#8211;group</code>=<i>GN</i></p>
<dd>where <i>GN</i> is the group number which can be between 0 and 31 inclusive. The default value is 0 . Group numbers are used to segregate data collected within the device. This is a new feature in SBC-2 and can probably be ignored for the time being.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-i</code>, <code>&#8211;immed</code></p>
<dd>sets the IMMED bit in the SYNCHRONIZE CACHE command. This instructs the device, if the format of the command is acceptable, to return a GOOD status immediately rather than wait for the blocks in the cache to be synchronized with (i.e. written to) the medium.</p>
<dt><code>-l</code>, <code>&#8211;lba</code>=<i>LBA</i></p>
<dd>where <i>LBA</i> is the lowest logical block address in the cache to synchronize to the medium. Default value is 0 .</p>
<dt><code>-s</code>, <code>&#8211;sync-nv</code></p>
<dd>synchronize the (volatile) cache with the non-volatile cache. Without this option (or if there is no non-volatile cache in the device) the synchronization is with the medium. The SYNC_NV bit was made obsolete in SBC-3 revision 35d.</p>
<dt><code>-t</code>, <code>&#8211;timeout</code>=<i>SECS</i></p>
<dd>where <i>SECS</i> is the number of seconds the OS allows the SYNCHRONIZE CACHE(16) to complete before it tries to cancel the command. Cancelling commands (typically with the task management function &quot;abort task&quot;) is best avoided. Note this option is only active together with the <i>&#8211;16</i> option. The default timeout is 60 seconds for both SYNCHRONIZE CACHE(10) and SYNCHRONIZE CACHE(16). Note that timeout issues can be avoided with the <i>&#8211;immed</i> option.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>With the SYNCHRONIZE CACHE(16) command <i>LBA</i> can be up to 64 bits in size and <i>COUNT</i> up to 32 bits in size. With the SYNCHRONIZ CACHE(10) command <i>LBA</i> can be up to 32 bits in size and <i>COUNT</i> up to 16 bits in size. </p>
<p> Various numeric arguments (e.g. <i>LBA</i>) may include multiplicative suffixes or be given in hexadecimal. See the &quot;NUMERIC ARGUMENTS&quot; section in the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_sync is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2013 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_start(sg3_utils)</code> </p>
