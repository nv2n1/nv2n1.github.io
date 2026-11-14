---
title: "readom(1)"
name: "readom"
section: "1"
letter: "r"
url: "/docs/linux/man/1-readom/"
description: "readom – read or write data Compact Discs"
---

<h2>NAME</h2>
<p> readom &#8211; read or write data Compact Discs</p>
<h2>SYNOPSIS</h2>
<p> <code>readom</code> <code>dev=</code><i>device</i> [ <i>options</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>Readom</code> is used to read or write Compact Discs. </p>
<p> The <i>device</i> refers to a device location similar to the one used in the wodim command. Refer to its manpage for details. </p>
<p> Also note that this version of readom uses a modified libusal library which has a different behaviour compared to the one distributed by its original author. </p>
<h2>OPTIONS</h2>
<p> If no options except the <i>dev=</i> option have been specified, <code>readom</code> goes into interactive mode. Select a primary function and then follow the instructions. </p>
<dl>
<dt><code>-version</code></p>
<dd> Print version information and exit.</p>
<dt><code>dev=</code><i>target</i></p>
<dd> Sets the SCSI target for the drive, see notes above. A typical device specification is <code>dev=</code><i>6,0</i> . If a filename must be provided together with the numerical target specification, the filename is implementation specific. The correct filename in this case can be found in the system specific manuals of the target operating system. On a <i>FreeBSD</i> system without <i>CAM</i> support, you need to use the control device (e.g. <i>/dev/rcd0.ctl</i>). A correct device specification in this case may be <code>dev=</code><i>/dev/rcd0.ctl:@</i> . </p>
<p> On Linux, drives connected to a parallel port adapter are mapped to a virtual SCSI bus. Different adapters are mapped to different targets on this virtual SCSI bus. </p>
<p> If no <i>dev</i> option is present, <code>readom</code> will try to get the device from the <code>CDR_DEVICE</code> environment. </p>
<p> If the argument to the <code>dev=</code> option does not contain the characters &#8216;,&#8217;, &#8216;/&#8217;, &#8216;@&#8217; or &#8216;:&#8217;, it is interpreted as an label name that may be found in the file /etc/wodim.conf (see FILES section).</p>
<dt><code>timeout=</code><i>#</i></p>
<dd> Set the default SCSI command timeout value to <i>#</i> seconds. The default SCSI command timeout is the minimum timeout used for sending SCSI commands. If a SCSI command fails due to a timeout, you may try to raise the default SCSI command timeout above the timeout value of the failed command. If the command runs correctly with a raised command timeout, please report the better timeout value and the corresponding command to the author of the program. If no <i>timeout </i> option is present, a default timeout of 40 seconds is used.</p>
<dt><code>debug=</code><i>#, </i><code>-d</code></p>
<dd> Set the misc debug value to # (with debug=#) or increment the misc debug level by one (with -d). If you specify <i>-dd,</i> this equals to <code>debug=</code><i>2.</i> This may help to find problems while opening a driver for libusal. as well as with sector sizes and sector types. Using <code>-debug</code> slows down the process and may be the reason for a buffer underrun.</p>
<dt><code>kdebug=</code>#, <code>kd=</code>#</p>
<dd> Tell the <code>usal</code>-driver to modify the kernel debug value while SCSI commands are running.</p>
<dt><code>-silent</code>, <code>-s</code></p>
<dd> Do not print out a status report for failed SCSI commands.</p>
<dt><code>-v</code></p>
<dd> Increment the level of general verbosity by one. This is used e.g. to display the progress of the process.</p>
<dt><code>-V</code></p>
<dd> Increment the verbose level with respect of SCSI command transport by one. This helps to debug problems during the process, that occur in the CD-Recorder. If you get incomprehensible error messages you should use this flag to get more detailed output. <code>-VV</code> will show data buffer content in addition. Using <code>-V</code> or <code>-VV</code> slows down the process.</p>
<dt><code>f=</code><i>file</i></p>
<dd> Specify the filename where the output should be written or the input should be taken from. Using &#8216;-&#8216; as filename will cause <code>readom</code> to use <code>stdout</code> resp. <code>stdin</code>.</p>
<dt><code>-w</code></p>
<dd> Switch to write mode. If this option is not present, <code>readom</code> reads from the specified device.</p>
<dt><code>-c2scan</code></p>
<dd> Scans the whole CD or the range specified by the <code>sectors=</code><i>range</i> for C2 errors. C2 errors are errors that are uncorrectable after the second stage of the 24/28 + 28/32 Reed Solomon correction system at audio level (2352 bytes sector size). If an audio CD has C2 errors, interpolation is needed to hide the errors. If a data CD has C2 errors, these errors are in most cases corrected by the ECC/EDC code that makes 2352 bytes out of 2048 data bytes. The ECC/EDC code should be able to correct about 100 C2 error bytes per sector. </p>
<p> If you find C2 errors you may want to reduce the speed using the <code>speed=</code> option as C2 errors may be a result of dynamic unbalance on the medium.</p>
<dt><code>-scanbus</code></p>
<dd> Scan all SCSI devices on all SCSI busses and print the inquiry strings. This option may be used to find SCSI address of the devices on a system. The numbers printed out as labels are computed by: <code>bus * 100 + target</code></p>
<dt><code>sectors=</code><i>range</i></p>
<dd> Specify a sector range that should be read. The range is specified by the starting sector number, a minus sign and the ending sector number. The end sector is not included in the list, so <code>sectors=</code>0-0 will not read anything and may be used to check for a CD in the drive.</p>
<dt><code>speed=</code>#</p>
<dd> Set the speed factor of the read or write process to #. # is an integer, representing a multiple of the audio speed. This is about 150 KB/s for CD-ROM and about 172 KB/s for CD-Audio. If no <i>speed</i> option is present, <code>readom</code> will use maximum speed. Only MMC compliant drives will benefit from this option. The speed of non MMC drives is not changed. </p>
<p> Using a lower speed may increase the readability of a CD or DVD.</p>
<dt><code>ts=</code>#</p>
<dd> Set the maximum transfer size for a single SCSI command to #. The syntax for the <code>ts=</code> option is the same as for wodim fs=# or sdd bs=#. </p>
<p> If no <code>ts=</code> option has been specified, <code>readom</code> defaults to a transfer size of 256 kB. If libusal gets lower values from the operating system, the value is reduced to the maximum value that is possible with the current operating system. Sometimes, it may help to further reduce the transfer size or to enhance it, but note that it may take a long time to find a better value by experimenting with the <code>ts=</code> option.</p>
<dt><code>-notrunc</code></p>
<dd> Do not truncate the output file when opening it.</p>
<dt><code>-fulltoc</code></p>
<dd> Retrieve a full TOC from the current disk and print it in hex.</p>
<dt><code>-clone</code></p>
<dd> Do a clone read. Read the CD with all sub-channel data and a full TOC. The full TOC data will be put into a file with similar name as with the <code>f=</code> option but the suffix <code>.toc</code> added.</p>
<dt><code>-noerror</code></p>
<dd> Do not abort if the high level error checking in <code>readom</code> found an uncorrectable error in the data stream.</p>
<dt><code>-nocorr</code></p>
<dd> Switch the drive into a mode where it ignores read errors in data sectors that are a result of uncorrectable ECC/EDC errors before reading. If <code>readom</code> completes, the error recovery mode of the drive is switched back to the remembered old mode.</p>
<dt><code>retries=</code><i>#</i></p>
<dd> Set the retry count for high level retries in <code>readom</code> to <i>#</i>. The default is to do 128 retries which may be too much if you like to read a CD with many unreadable sectors.</p>
<dt><code>-overhead</code></p>
<dd> Meter the SCSI command overhead time. This is done by executing several commands 1000 times and printing the total time used. If you divide the displayed times by 1000, you get the average overhead time for a single command.</p>
<dt><code>meshpoints=</code>#</p>
<dd> Print read-speed at # locations. The purpose of this option is to create a list of read speed values suitable for e.g. <code>gnuplot</code>. The speed values are calculated assuming that 1000 bytes are one kilobyte as documented in the SCSI standard. The output data created for this purpose is written to <i>stdout</i>.</p>
<dt><code>-factor</code></p>
<dd> Output the speed values for <code>meshpoints=</code># as factor based on <i>single speed</i> of the current medium. This only works if <code>readom</code> is able to determine the current medium type.</dl>
<h2>EXAMPLES</h2>
<p> For all examples below, it will be assumed that the drive is connected to the primary SCSI bus of the machine. The SCSI target id is set to 2. </p>
<p> To read the complete media from a CD-ROM writing the data to the file <i>cdimage.raw</i>: </p>
<p>&nbsp;<wbr>readom dev=2,0 f=cdimage.raw </p>
<p> To read sectors from range 150 &#8230; 10000 from a CD-ROM writing the data to the file <i>cdimage.raw</i>: </p>
<p>&nbsp;<wbr>readom dev=2,0 sectors=150-10000 f=cdimage.raw </p>
<p> To write the data from the file <i>cdimage.raw</i> (e.g. a filesystem image from <code>genisoimage</code>) to a DVD-RAM, call: </p>
<p>&nbsp;<wbr>readom dev=2,0 -w f=cdimage.raw </p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>RSH</code></p>
<dd> If the <code>RSH</code> environment is present, the remote connection will not be created via <code><a href="/docs/linux/man/3-rcmd/">rcmd</a></code>(3) but by calling the program pointed to by <code>RSH</code>. Use e.g. <code>RSH=</code>/usr/bin/ssh to create a secure shell connection. </p>
<p> Note that this forces <code>wodim</code> to create a pipe to the <code><a href="/docs/linux/man/1-rsh/">rsh</a>(1)</code> program and disallows <code>wodim</code> to directly access the network socket to the remote server. This makes it impossible to set up performance parameters and slows down the connection compared to a <code>root</code> initiated <code><a href="/docs/linux/man/3-rcmd/">rcmd</a>(3)</code> connection.</p>
<dt><code>RSCSI</code></p>
<dd> If the <code>RSCSI</code> environment is present, the remote SCSI server will not be the program <code>/opt/schily/sbin/rscsi</code> but the program pointed to by <code>RSCSI</code>. Note that the remote SCSI server program name will be ignored if you log in using an account that has been created with a remote SCSI server program as login shell.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wodim/">wodim</a></code>(1), <code><a href="/docs/linux/man/1-genisoimage/">genisoimage</a></code>(1), <code><a href="/docs/linux/man/3-rcmd/">rcmd</a></code>(3), <code><a href="/docs/linux/man/1-ssh/">ssh</a></code>(1). </p>
<h2>NOTES</h2>
<p> Unless you want to risk getting problems, <code>readom</code> should be run as root. If you don&#8217;t want to allow users to become root on your system, <code>readom</code> may safely be installed suid root. For more information see the additional notes of your system/program distribution or README.suidroot which is part of the Cdrkit source. </p>
<p> Documentation of the <code>wodim</code> program contains more technical details which could also apply to <code>readom.</code> </p>
<h2>DIAGNOSTICS</h2>
<p> A typical error message for a SCSI command looks like: </p>
<dl>
<dt>
<dd>
<pre>
readom: I/O error. test unit ready: scsi sendcmd: no error
CDB:  00 20 00 00 00 00
status: 0x2 (CHECK CONDITION)
Sense Bytes: 70 00 05 00 00 00 00 0A 00 00 00 00 25 00 00 00 00 00
Sense Key: 0x5 Illegal Request, Segment 0
Sense Code: 0x25 Qual 0x00 (logical unit not supported) Fru 0x0
Sense flags: Blk 0 (not valid)
cmd finished after 0.002s timeout 40s
</pre>
</dl>
<p> The first line gives information about the transport of the command. The text after the first colon gives the error text for the system call from the view of the kernel. It usually is: <code>I/O error</code> unless other problems happen. The next words contain a short description for the SCSI command that fails. The rest of the line tells you if there were any problems for the transport of the command over the SCSI bus. <code>fatal error</code> means that it was not possible to transport the command (i.e. no device present at the requested SCSI address). </p>
<p> The second line prints the SCSI command descriptor block for the failed command. </p>
<p> The third line gives information on the SCSI status code returned by the command, if the transport of the command succeeds. This is error information from the SCSI device. </p>
<p> The fourth line is a hex dump of the auto request sense information for the command. </p>
<p> The fifth line is the error text for the sense key if available, followed by the segment number that is only valid if the command was a <i>copy</i> command. If the error message is not directly related to the current command, the text <i>deferred error</i> is appended. </p>
<p> The sixth line is the error text for the sense code and the sense qualifier if available. If the type of the device is known, the sense data is decoded from tables in <i>scsierrs.c</i> . The text is followed by the error value for a field replaceable unit. </p>
<p> The seventh line prints the block number that is related to the failed command and text for several error flags. The block number may not be valid. </p>
<p> The eight line reports the timeout set up for this command and the time that the command really needed to complete. </p>
<h2>BUGS</h2>
<p> The <code>readom</code> program described here is the Cdrkit spinoff from the original <code>readcd</code> application (see AUTHOR section for details). It may contain bugs not present in the original implementation. </p>
<p> It is definitely less portable than the original implementation. </p>
<p> For platform specific bugs, see the corresponding README.platform file in the Cdrkit documentation (eg. README.linux). </p>
<h2>MAILING LISTS</h2>
<p> If you want to actively take part on the development of readom, you may join the developer mailing list via this URL: </p>
<p> <code><a rel="nofollow" href="http://alioth.debian.org/mail/?group_id=31006">http://alioth.debian.org/mail/?group_id=31006</a></code> </p>
<p> The mail address of the list is: <code>debburn-devel [at] lists.alioth.debian.org</code> </p>
<h2>AUTHOR</h2>
<pre>
Joerg Schilling
Seestr. 110
D-13353 Berlin
Germany
</pre>
<p> This is application is a spinoff from the original implementation of readcd delivered in the cdrtools package [1] created by Joerg Schilling, who deserves the most credits for its success. However, he is not involved into the development of this spinoff and therefore he shall not be made responsible for any problem caused by it. Do not try to get support from the original author! </p>
<p> Additional information can be found on:<br />
 <a rel="nofollow" href="https://alioth.debian.org/projects/debburn/">https://alioth.debian.org/projects/debburn/</a> </p>
<p> If you have support questions, send them to </p>
<p> <code>debburn-devel [at] lists.alioth.debian.org</code> </p>
<p> If you have definitely found a bug, send a mail to this list or to </p>
<p> <code>submit [at] bugs.debian.org</code> </p>
<p> writing at least a short description into the Subject and &quot;Package: cdrkit&quot; into the first line of the mail body.</p>
<h2>SOURCES</h2>
<p> [1] Cdrtools 2.01.01a08 from May 2006, <a rel="nofollow" href="http://cdrecord.berlios.de">http://cdrecord.berlios.de</a> </p>
<h2>Index</h2>
