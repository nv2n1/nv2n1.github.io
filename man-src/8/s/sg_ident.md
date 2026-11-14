---
title: "sg_ident(8)"
name: "sg_ident"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_ident/"
description: "sg_ident – send SCSI REPORT/SET IDENTIFYING INFORMATION command"
---

<p>sg_ident &#8211; send SCSI REPORT/SET IDENTIFYING INFORMATION command</p>
<h2>Synopsis</h2>
<p><code>sg_ident</code> [<i>&#8211;ascii</i>] [<i>&#8211;clear</i>] [<i>&#8211;help</i>] [<i>&#8211;itype=IT</i>] [<i>&#8211;raw</i>] [<i>&#8211;set</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Send a SCSI REPORT IDENTIFYING INFORMATION or SET IDENTIFYING INFORMATION command to <i>DEVICE</i>. Prior to SPC-4 (revision 7) these commands were called REPORT DEVICE IDENTIFIER and SET DEVICE IDENTIFIER respectively. SCSI devices that support these two commands allow users to write (set) identifying information and report it back at some later time. The information is persistent (i.e. stored on some non-volatile medium within the SCSI device that will survive a power outage). </p>
<p> Typically the space allocated for the information is limited: SPC-4 (revision 7) states that for information type 0, the minimum length is 64 bytes and the maximum is 512 bytes. For other information types (1 to 126 inclusive) the maximum length is 256 bytes. Also information types 1 to 126 (inclusive) should contain a null terminated UTF-8 string. The author has seen older disks that only support 16 bytes. </p>
<p> The default action when no options are given is to invoke the Report Identifying Information command with the information type defaulting to zero. Error reports are sent to stderr. By default the information is shown in ASCII-HEX (up to 16 bytes per line) with an ASCII representation to the right with dots replacing non printable characters.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-A</code>, <code>&#8211;ascii</code></p>
<dd>invokes the Report Identifying Information command and if anything is found interprets it as ASCII (or UTF-8 depending on the locale) and prints the information to stdout.</p>
<dt><code>-C</code>, <code>&#8211;clear</code></p>
<dd>invokes the Set Identifying Information command with an information length of zero. This has the effect of clearing the existing information.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-i</code>, <code>&#8211;itype</code>=<i>IT</i></p>
<dd>where <i>IT</i> is the information type. Defaults to zero. The maximum value is 127 which is special and cannot be used with <i>&#8211;set</i> or <i>&#8211;clear</i>. The information type of 127 (if supported) causes the REPORT IDENTIFYING INFORMATION command to respond with a list of available information types and their maximum lengths in bytes. The odd numbered information types between 3 and 125 (inclusive) are not to be used (as they clash with the SCC-2 standard).</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>invokes the Report Identifying information command and if anything is found sends the information (which may be binary) to stdout. Nothing else is sent to stdout however error reports, if any, are sent to stderr.</p>
<dt><code>-S</code>, <code>&#8211;set</code></p>
<dd>first reads stdin until an EOF is detected then invokes the Set Identifying Information command to set what has been fetched from stdin as the information. The amount of data read must be between 1 and 512 bytes length (inclusive).</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<p> This utility permits users to write their own identifying information to their SCSI devices. There are several other types of descriptors (or designators) that the user cannot change. These include the SCSI INQUIRY command with its standard vendor and product identification strings and the product revision level; plus the large amount of information provided by the &quot;Device Identification&quot; VPD page (see sg_vpd). There is also the READ MEDIA SERIAL NUMBER command (see sg_rmsn). The MMC-4 command set for CD and DVDs has a &quot;media serial number&quot; feature (0x109) [and a &quot;logical unit serial number&quot; feature]. These can be viewed with the sg_get_config utility.</p>
<h2>Examples</h2>
<p>First, to see if there is an existing information whose format is unknown (for information type 0), use no options: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sg_ident&nbsp;<wbr>/dev/sdb </p>
<p>00&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>31 32 33 34 35 36 37 38&nbsp;<wbr>&nbsp;<wbr>39 30&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>1234567890 </p>
<p> If it is ASCII then it can printed as such: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sg_ident &#8211;ascii&nbsp;<wbr>/dev/sdb </p>
<p>&nbsp;<wbr>&nbsp;<wbr>1234567890 </p>
<p> The information can be copied to a file, cleared and then re-asserted with this sequence: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sg_ident &#8211;raw&nbsp;<wbr>/dev/sdb&nbsp;<wbr>&gt;&nbsp;<wbr>t </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sg_ident &#8211;clear&nbsp;<wbr>/dev/sdb </p>
<p>&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>cat t | sg_ident &#8211;set&nbsp;<wbr>/dev/sdb</p>
<h2>Exit Status</h2>
<p>The exit status of sg_ident is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2005-2012 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_vpd(sg3_utils), sg_rmsn(sg3_utils), sg_get_config(sg3_utils)</code> </p>
