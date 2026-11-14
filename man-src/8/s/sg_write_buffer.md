---
title: "sg_write_buffer(8)"
name: "sg_write_buffer"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_write_buffer/"
description: "sg_write_buffer – send SCSI WRITE BUFFER command"
---

<p>sg_write_buffer &#8211; send SCSI WRITE BUFFER command</p>
<h2>Synopsis</h2>
<p><code>sg_write_buffer</code> [<i>&#8211;help</i>] [<i>&#8211;id=ID</i>] [<i>&#8211;in=FILE</i>] [<i>&#8211;length=LEN</i>] [<i>&#8211;mode=MO</i>] [<i>&#8211;offset=OFF</i>] [<i>&#8211;raw</i>] [<i>&#8211;skip=SKIP</i>] [<i>&#8211;specific=MS</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Sends a SCSI WRITE BUFFER command to <i>DEVICE</i>, along with data provided by the user. In some cases no data is required, or data can be read from the file given in the <i>&#8211;in=FILE</i> option, or data is read from stdin when either <i>&#8211;raw</i> or <i>&#8211;in=-</i> is given. </p>
<p> Some WRITE BUFFER command variants do not have associated data to send to the device, for example &quot;activate_mc&quot; (&quot;activate deferred microcode&quot;).</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit. If used multiple times also prints the mode names and their acronyms.</p>
<dt><code>-i</code>, <code>&#8211;id</code>=<i>ID</i></p>
<dd>this option sets the buffer id field in the cdb. <i>ID</i> is a value between 0 (default) and 255 inclusive.</p>
<dt><code>-I</code>, <code>&#8211;in</code>=<i>FILE</i></p>
<dd>read data from file <i>FILE</i> that will be sent with the WRITE BUFFER command. If <i>FILE</i> is &#8216;-&#8216; then stdin is read until an EOF is detected (this is the same action as <i>&#8211;raw</i>).</p>
<dt><code>-l</code>, <code>&#8211;length</code>=<i>LEN</i></p>
<dd>where <i>LEN</i> is the length, in bytes, of data to be written to the device. If not given (and length cannot be deduced from <i>&#8211;in=FILE</i> or <i>&#8211;raw</i>) then defaults to zero. If the option is given and the length deduced from <i>&#8211;in=FILE</i> or <i>&#8211;raw</i> is less (or no data is provided), then bytes of 0xff are used as fill bytes.</p>
<dt><code>-m</code>, <code>&#8211;mode</code>=<i>MO</i></p>
<dd>this option sets the mode field in the cdb. <i>MO</i> is a value between 0 (default) and 31 inclusive. Alternatively an abbreviation can be given. To list the available mode abbreviations give an invalid one (e.g. &#8216;&#8211;mode=xxx&#8217;) or use the &#8216;-hh&#8217; option.</p>
<dt><code>-o</code>, <code>&#8211;offset</code>=<i>OFF</i></p>
<dd>this option sets the buffer offset field in the cdb. <i>OFF</i> is a value between 0 (default) and 2**24-1 . It is a byte offset.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>read data from stdin until an EOF is detected. This data is sent with the WRITE BUFFER command to <i>DEVICE</i>. The action of this option is the same as using &#8216;&#8211;in=-&#8216;.</p>
<dt><code>-s</code>, <code>&#8211;skip</code>=<i>SKIP</i></p>
<dd>this option is only active when <i>&#8211;in=FILE</i> is given and <i>FILE</i> is a regular file, rather than stdin. Data is read starting at byte offset <i>SKIP</i> to the end of file (or the amount given by <i>&#8211;length=LEN</i>). If not given the byte offset defaults to 0 (i.e. the start of the file).</p>
<dt><code>-S</code>, <code>&#8211;specific</code>=<i>MS</i></p>
<dd><i>MS</i> is the mode specific field in the cdb. This is a 3-bit field so the values 0 to 7 are accepted. This field was introduced in SPC-4 revision 32 and can be used to specify additional events that activate deferred microcode (when <i>MO</i> is 0xD).</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>If no <i>&#8211;length=LEN</i> is given this utility reads up to 8 MiB of data from the given file <i>FILE</i> (or stdin). If a larger amount of data is required then the <i>&#8211;length=LEN</i> option should be given. The user should be aware that most operating systems have limits on the amount of data that can be sent with one SCSI command. In Linux this depends on the pass through mechanism used (e.g. block SG_IO or the sg driver) and various setting in sysfs in the Linux lk 2.6 series (e.g. /sys/block/sda/queue/max_sectors_kb). </p>
<p> Downloading incorrect microcode into a device has the ability to render that device inoperable. One would hope that the device vendor verifies the data before activating it. If the SCSI WRITE BUFFER command is given values in its cdb (e.g. <i>LEN</i>) that are inappropriate (e.g. too large) then the device should respond with a sense key of ILLEGAL REQUEST and an additional sense code of INVALID FIELD in CDB. If a WRITE BUFFER command (or a sequence of them) fails due to device vendor verification checks then it should respond with a sense key of ILLEGAL REQUEST and an additional sense code of COMMAND SEQUENCE ERROR. </p>
<p> All numbers given with options are assumed to be decimal. Alternatively numerical values can be given in hexadecimal preceded by either &quot;0x&quot; or &quot;0X&quot; (or has a trailing &quot;h&quot; or &quot;H&quot;).</p>
<h2>Exit Status</h2>
<p>The exit status of sg_write_buffer is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Luben Tuikov and Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2012 Luben Tuikov and Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_read_buffer(sg3_utils)</code> </p>
