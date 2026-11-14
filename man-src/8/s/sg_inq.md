---
title: "sg_inq(8)"
name: "sg_inq"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_inq/"
description: "sg_inq – issue SCSI INQUIRY command, output and decode response"
---

<p>sg_inq &#8211; issue SCSI INQUIRY command, output and decode response</p>
<h2>Synopsis</h2>
<p><code>sg_inq</code> [<i>&#8211;ata</i>] [<i>&#8211;cmddt</i>] [<i>&#8211;descriptors</i>] [<i>&#8211;export</i>] [<i>&#8211;extended</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;id</i>] [<i>&#8211;len=LEN</i>] [<i>&#8211;maxlen=LEN</i>] [<i>&#8211;page=PG</i>] [<i>&#8211;raw</i>] [<i>&#8211;vendor</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>&#8211;vpd</i>] <i>DEVICE</i> </p>
<p> <code>sg_inq</code> [<i>-36</i>] [<i>-a</i>] [<i>-A</i>] [<i>-b</i>] [<i>-c</i>] [<i>-cl</i>] [<i>-d</i>] [<i>-e</i>] [<i>-h</i>] [<i>-H</i>] [<i>-i</i>] [<i>-l=LEN</i>] [<i>-m</i>] [<i>-M</i>] [<i>-o=OPCODE_PG</i>] [<i>-p=VPD_PG</i>] [<i>-P</i>] [<i>-r</i>] [<i>-s</i>] [<i>-u</i>] [<i>-v</i>] [<i>-V</i>] [<i>-x</i>] [<i>-36</i>] [<i>-?</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>This utility by default sends a SCSI INQUIRY command to the given device and then outputs the response. All SCSI devices are meant to respond to a &quot;standard&quot; INQUIRY command with at least a 36 byte response (in SCSI 2 and higher). An INQUIRY is termed as &quot;standard&quot; when both the EVPD and CmdDt (now obsolete) bits are clear. </p>
<p> This utility supports two command line syntaxes, the preferred one is shown first in the synopsis and explained in this section. A later section on the old command line syntax outlines the second group of options. </p>
<p> An important &quot;non-standard&quot; INQUIRY page is the Device Identification Vital Product Data (VPD) page [0x83]. Since SPC-3, support for this page is mandatory. The <i>&#8211;id</i> option decodes this page. New VPD page information is no longer being added to this utility. To get information on new VPD pages see the <a href="/docs/linux/man/8-sg_vpd/">sg_vpd</a>(8) or <a href="/docs/linux/man/8-sdparm/">sdparm</a>(8) utilities. </p>
<p> If the <i>DEVICE</i> exists and the SCSI INQUIRY fails (because the SG_IO ioctl is not supported) then an ATA IDENTIFY (PACKET) DEVICE is tried. If it succeeds then device identification strings are output. The <i>&#8211;raw</i> and <i>&#8211;hex</i> options can be used to manipulate the output. If the <i>&#8211;ata</i> option is given then the SCSI INQUIRY is not performed and the <i>DEVICE</i> is assumed to be ATA (or ATAPI). </p>
<p> The reference document used for interpreting an INQUIRY is T10/1713-D Revision 36e (SPC-4, 24 August 2012) found at <a rel="nofollow" href="http://www.t10.org">http://www.t10.org</a> . Obsolete and reserved items in the standard INQUIRY response output are displayed in brackets. The reference document for the ATA IDENTIFY (PACKET) DEVICE command is ATA8-ACS found at <a rel="nofollow" href="http://www.t13.org">http://www.t13.org</a> .</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well. The options are arranged in alphabetical order based on the long option name.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;ata</code></p>
<dd>Assume given <i>DEVICE</i> is an ATA or ATAPI device which can receive ATA commands from the host operating system. Skip the SCSI INQUIRY command and use either the ATA IDENTIFY DEVICE command (for non-packet devices) or the ATA IDENTIFY PACKET DEVICE command. To show the response in hex, add a &#8216;&#8211;verbose&#8217; option. This option is only available in Linux.</p>
<dt><code>-c</code>, <code>&#8211;cmddt</code></p>
<dd>set the Command Support Data (CmdDt) bit (defaults to clear(0)). Used in conjunction with the <i>&#8211;page=PG</i> option where <i>PG</i> specifies the SCSI command opcode to query. When used twice (e.g. &#8216;-cc&#8217;) this utility forms a list by looping over all 256 opcodes (0 to 255 inclusive) only outputting a line for found commands. The CmdDt bit is now obsolete. It has been replaced by the REPORT SUPPORTED OPERATION CODES command, see the <a href="/docs/linux/man/8-sg_opcodes/">sg_opcodes</a>(8) utility.</p>
<dt><code>-d</code>, <code>&#8211;descriptors</code></p>
<dd>decodes and prints the version descriptors found in a standard INQUIRY response. There are up to 8 of them. Version descriptors indicate which versions of standards and/or drafts the <i>DEVICE</i> complies with. The normal components of a standard INQUIRY are output (typically from the first 36 bytes of the response) followed by the version descriptors if any.</p>
<dt><code>-e</code></p>
<dd>see entry below for <i>&#8211;vpd</i>.</p>
<dt><code>-u</code>, <code>&#8211;export</code></p>
<dd>prints out information obtained from the device. The output can be modified by selecting a VPD page with <i>PG</i> (from <i>&#8211;page=PG</i>). If the device identification VPD page 0x83 is given it prints out information in the form: &quot;SCSI_IDENT_&lt;assoc&gt;_&lt;type&gt;=&lt;ident&gt;&quot; to stdout. If the device serial number VPD page 0x80 is given it prints out information in the form: &quot;SCSI_SERIAL=&lt;ident&gt;&quot;. Other VPD pages are not supported. If no VPD page is given it prints out information in the form: &quot;SCSI_VENDOR=&lt;vendor&gt;&quot;, &quot;SCSI_MODEL=&lt;model&gt;&quot;, and &quot;SCSI_REVISION=&lt;rev&gt;&quot;, taken from the standard inquiry. This may be useful for tools like <a href="/docs/linux/man/7-udev/">udev</a>(7) in Linux.</p>
<dt><code>-E</code>, <code>-x</code>, <code>&#8211;extended</code></p>
<dd>prints the extended INQUIRY VPD page [0x86].</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print out the usage message then exit. When used twice, after the usage message, there is a list of available abbreviations than can be given to the <i>&#8211;page=PG</i> option.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>rather than decode a standard INQUIRY response, a VPD page or command support data; print out the response in hex to stdout. Error messages and warnings are typically output to stderr. When used twice with the ATA Information VPD page [0x89] decodes the start of the response then outputs the ATA IDENTIFY (PACKET) DEVICE response in hexadecimal bytes (not 16 bit words). When used three times with the ATA Information VPD page [0x89] or the <i>&#8211;ata</i> option, this utility outputs the ATA IDENTIFY (PACKET) DEVICE response in hexadecimal words suitable for input to &#8216;hdparm &#8211;Istdin&#8217;. See note below.</p>
<dt><code>-i</code>, <code>&#8211;id</code></p>
<dd>prints the device identification VPD page [0x83].</p>
<dt><code>-l</code>, <code>&#8211;len</code>=<i>LEN</i></p>
<dd>the number <i>LEN</i> is the &quot;allocation length&quot; field in the INQUIRY cdb. This is the (maximum) length of the response to be sent by the device. The default value of <i>LEN</i> is 0 which is interpreted as: first request is for 36 bytes and if necessary execute another INQUIRY if the &quot;additional length&quot; field in the response indicates that more than 36 bytes is available. If <i>LEN</i> is greater than 0 then only one INQUIRY command is performed. See paragraph below about &quot;36 byte INQUIRYs&quot;.</p>
<dt><code>-m</code>, <code>&#8211;maxlen</code>=<i>LEN</i></p>
<dd>this option has the same action as the <i>&#8211;len=LEN</i> option. It has been added for compatibility with the sg_vpd, sg_modes and sg_logs utilities.</p>
<dt><code>-O</code>, <code>&#8211;old</code></p>
<dd>switch to older style options.</p>
<dt><code>-p</code>, <code>&#8211;page</code>=<i>PG</i></p>
<dd>the <i>PG</i> argument can be either a number of an abbreviation for a VPD page. To enumerate the available abbreviations for VPD pages use &#8216;-hh&#8217; or a bad abbreviation (e.g, &#8216;&#8211;page=xxx&#8217;). When the <i>&#8211;cmddt</i> option is given (once) then <i>PG</i> is interpreted as an opcode number (so VPD page abbreviations make little sense).</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>output the response in binary to stdout. Error messages and warnings, if any, are sent to stderr.</p>
<dt><code>-s</code>, <code>&#8211;vendor</code></p>
<dd>output a standard INQUIRY response&#8217;s vendor specific field from offset 36 to 55 in ASCII. When used twice (i.e. &#8216;-ss&#8217;) also output the vendor specific field from offset 96 in ASCII. This is only done if the data passes some simple sanity checks.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase level of verbosity. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print out version string then exit.</p>
<dt><code>-e</code>, <code>&#8211;vpd</code></p>
<dd>set the Enable Vital Product Data (EVPD) bit (defaults to clear(0)). Used in conjunction with the <i>&#8211;page=PG</i> option where <i>PG</i> specifies the VPD page number to query. If the <i>&#8211;page=PG</i> is not given then <i>PG</i> defaults to zero which is the &quot;Supported VPD pages&quot; VPD page.</dl>
<h2>Notes</h2>
<p>Some devices with weak SCSI command set implementations lock up when they receive commands they don&#8217;t understand (or even response lengths that they don&#8217;t expect). Such devices need to be treated carefully, use the &#8216;&#8211;len=36&#8217; option. Without this option this utility will issue an initial standard INQUIRY requesting 36 bytes of response data. If the device indicates it could have supplied more data then a second INQUIRY is issued to fetch the longer response. That second command may lock up faulty devices. </p>
<p> ATA or ATAPI devices that use a SCSI to ATA Translation layer (see SAT at <a rel="nofollow" href="http://www.t10.org">www.t10.org</a>) may support the ATA Information VPD page. This returns the IDENTIFY (PACKET) DEVICE response amongst other things. The ATA Information VPD page can be fetched with &#8216;&#8211;page=ai&#8217;. </p>
<p> In the INQUIRY standard response there is a &#8216;MultiP&#8217; flag which is set when the device has 2 or more ports. Some vendors use the preceding vendor specific (&#8216;VS&#8217;) bit to indicate which port is being accessed by the INQUIRY command (0 -&gt; relative port 1 (port &quot;a&quot;), 1 -&gt; relative port 2 (port &quot;b&quot;)). When the &#8216;MultiP&#8217; flag is set, the preceding vendor specific bit is shown in parentheses. SPC-3 compliant devices should use the device identification VPD page (0x83) to show which port is being used for access and the SCSI ports VPD page (0x88) to show all available ports on the device. </p>
<p> In the 2.4 series of Linux kernels the <i>DEVICE</i> must be a SCSI generic (sg) device. In the 2.6 series block devices (e.g. disks and ATAPI DVDs) can also be specified. For example &quot;sg_inq /dev/sda&quot; will work in the 2.6 series kernels. From lk 2.6.6 other SCSI &quot;char&quot; device names may be used as well (e.g. &quot;/dev/st0m&quot;). </p>
<p> The number of bytes output by <i>&#8211;hex</i> and <i>&#8211;raw</i> is 36 bytes or the number given to <i>&#8211;len=LEN</i> (or <i>&#8211;maxlen=LEN</i>). That number is reduced if the &quot;resid&quot; returned by the HBA indicates less bytes were sent back from <i>DEVICE</i>.</p>
<h2>Ata Devices</h2>
<p>There are two major types of ATA devices: non-packet devices (e.g. ATA disks) and packet devices (ATAPI). The majority of ATAPI devices are CD/DVD/BD drives in which the ATAPI transport carries the MMC set (i.e. a SCSI command set). Further, both types of ATA devices can be connected to a host computer via a &quot;SCSI&quot; (or some other) transport. When an ATA disk is controlled via a SCSI (or non-ATA) transport then two approaches are commonly used: tunnelling (e.g. STP in Serial Attached SCSI (SAS)) or by emulating a SCSI device (e.g. with a SCSI to ATA translation layer, see SAT at <a rel="nofollow" href="http://www.t10.org">www.t10.org</a> ). Even when the physical transport to the host computer is ATA (especially in the case of SATA) the operating system may choose to put a SAT layer in the driver &quot;stack&quot; (e.g. libata in Linux). </p>
<p> The main identifying command for any SCSI device is an INQUIRY. The corresponding command for an ATA non-packet device is IDENTIFY DEVICE while for an ATA packet device it is IDENTIFY PACKET DEVICE. </p>
<p> When this utility is invoked for an ATAPI device (e.g. a CD/DVD/BD drive with &quot;sg_inq /dev/hdc&quot;) then a SCSI INQUIRY is sent to the device and if it responds then the response to decoded and output and this utility exits. To see the response for an ATA IDENTIFY PACKET DEVICE command add the <i>&#8211;ata</i> option (e.g. &quot;sg_inq &#8211;ata /dev/hdc). </p>
<p> This utility doesn&#8217;t decode the response to an ATA IDENTIFY (PACKET) DEVICE command, hdparm does a good job at that. The &#8216;-HHH&#8217; option has been added for use with either the &#8216;&#8211;ata&#8217; or &#8216;&#8211;page=ai&#8217; option to produce a format acceptable to &quot;hdparm &#8211;Istdin&quot;. An example: &#8216;sg_inq &#8211;ata -HHH /dev/hdc | hdparm &#8211;Istdin&#8217;. See hdparm.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_inq is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Older Command Line Options</h2>
<p>The options in this section were the only ones available prior to sg3_utils version 1.23 . In sg3_utils version 1.23 and later these older options can be selected by either setting the SG3_UTILS_OLD_OPTS environment variable or using <i>&#8211;old</i> (or <i>-O</i>) as the first option.</p>
<dl>
<dt><code>-36</code></p>
<dd>only requests 36 bytes of response data for an INQUIRY. Furthermore even if the device indicates in its response it can supply more data, a second (longer) INQUIRY is not performed. This is a paranoid setting. Equivalent to &#8216;&#8211;len=36&#8217; in the main description.</p>
<dt><code>-a</code></p>
<dd>fetch the ATA Information VPD page [0x89]. Equivalent to &#8216;&#8211;page=ai&#8217; in the main description. This page is defined in SAT (see at <a rel="nofollow" href="http://www.t10.org">www.t10.org</a>).</p>
<dt><code>-A</code></p>
<dd>Assume given <i>DEVICE</i> is an ATA or ATAPI device. Equivalent to <i>&#8211;ata</i> in the main description.</p>
<dt><code>-b</code></p>
<dd>decodes the Block Limits VPD page [0xb0]. Equivalent to &#8216;&#8211;page=bl&#8217; in the main description. This page is defined in SBC-2 (see <a rel="nofollow" href="http://www.t10.org">www.t10.org</a>).</p>
<dt><code>-c</code></p>
<dd>set the Command Support Data (CmdDt) bit (defaults to clear(0)). Used in<br />
&nbsp;<wbr>conjunction with the&nbsp;<wbr><i>-o=OPCODE_PG</i>&nbsp;<wbr>option to specify the SCSI command opcode to query. Equivalent to <i>&#8211;cmddt</i> in the main description.</p>
<dt><code>-cl</code></p>
<dd>lists the command data for all supported commands (followed by the command name) by looping through all 256 opcodes. This option uses the CmdDt bit which is now obsolete. See the <a href="/docs/linux/man/8-sg_opcodes/">sg_opcodes</a>(8) utility. Equivalent to &#8216;&#8211;cmddt &#8211;cmddt&#8217; in the main description.</p>
<dt><code>-d</code></p>
<dd>decodes depending on context. If <i>-e</i> option is given, or any option that implies <i>-e</i> (e.g. &#8216;-i&#8217; or &#8216;-p=80&#8217;), then this utility attempts to decode the indicated VPD page. Otherwise the version descriptors (if any) are listed following a standard INQUIRY response. In the version descriptors sense, equivalent to <i>&#8211;descriptors</i> in the main description.</p>
<dt><code>-e</code></p>
<dd>enable (i.e. sets) the Vital Product Data (EVPD) bit (defaults to clear(0)). Used in conjunction with the <i>-p=VPD_PG</i> option to specify the VPD page to fetch. If <i>-p=VPD_PG</i> is not given then VPD page 0 (list supported VPD pages) is assumed.</p>
<dt><code>-h</code></p>
<dd>outputs INQUIRY response in hex rather than trying to decode it. Equivalent to <i>&#8211;hex</i> in the main description.</p>
<dt><code>-H</code></p>
<dd>same action as <i>-h</i>. Equivalent to <i>&#8211;hex</i> in the main description.</p>
<dt><code>-i</code></p>
<dd>decodes the Device Identification VPD page [0x83]. Equivalent to <i>&#8211;id</i> in the main description. This page is made up of several &quot;designation descriptors&quot;. If <i>-h</i> is given then each descriptor header is decoded and the identifier itself is output in hex. To see the whole VPD 0x83 page response in hex use &#8216;-p=83 -h&#8217;.</p>
<dt><code>-m</code></p>
<dd>decodes the Management network addresses VPD page [0x85]. Equivalent to &#8216;&#8211;page=mna&#8217; in the main description.</p>
<dt><code>-M</code></p>
<dd>decodes the Mode page policy VPD page [0x87]. Equivalent to &#8216;&#8211;page=mpp&#8217; in the main description.</p>
<dt><code>-N</code></p>
<dd>switch to the newer style options.</p>
<dt><code>-o</code>=<i>OPCODE_PG</i></p>
<dd>used in conjunction with the <i>-e</i> or <i>-c</i> option. If neither given then the <i>-e</i> option assumed. When the <i>-e</i> option is also given (or assumed) then the argument to this option is the VPD page number. The argument is interpreted as hexadecimal and is expected to be in the range 0 to ff inclusive. Only VPD page 0 is decoded and it lists supported VPD pages and their names (if known). To decode the mandatory device identification page (0x83) use the <i>-i</i> option. A now obsolete usage is when the <i>-c</i> option is given in which case the argument to this option is assumed to be a command opcode number. Recent SCSI draft standards have moved this facility to a separate command (see <a href="/docs/linux/man/8-sg_opcodes/">sg_opcodes</a>(8)). Defaults to 0 so if <i>-e</i> is given without this option then VPD page 0 is output.</p>
<dt><code>-p</code>=<i>VPD_PG</i></p>
<dd>same action as <i>-o=OPCODE_PG</i> option described in the previous entry. Since the opcode value with the CmdDt is now obsolete, the main use of this option is to specify the VPD page number. The argument is interpreted as hexadecimal and is expected to be in the range 0 to ff inclusive. Defaults to 0 so if <i>-e</i> is given without this option then VPD page 0 is output.</p>
<dt><code>-P</code></p>
<dd>decodes the Unit Path Report VPD page [0xc0] which is EMC specific. Equivalent to &#8216;&#8211;page=upr&#8217; in the main description.</p>
<dt><code>-r</code></p>
<dd>outputs the response in binary to stdout. Equivalent to <i>&#8211;raw</i> in the main description. Can be used twice (i.e. &#8216;-rr&#8217; (and &#8216;-HHH&#8217; has same effect)) and if used with the <i>-A</i> or <i>-a</i> option yields output with the same format as &quot;cat /proc/ide/hd&lt;x&gt;/identify&quot; so that it can then be piped to &quot;hdparm &#8211;Istdin&quot;.</p>
<dt><code>-s</code></p>
<dd>decodes the SCSI Ports VPD page [0x88]. Equivalent to &#8216;&#8211;page=sp&#8217; in the main description.</p>
<dt><code>-u</code></p>
<dd>equivalent to &#8216;&#8211;export&#8217; in the main description.</p>
<dt><code>-v</code></p>
<dd>increase level of verbosity. Can be used multiple times.</p>
<dt><code>-V</code></p>
<dd>print out version string then exit.</p>
<dt><code>-x</code></p>
<dd>decodes the Extended INQUIRY data VPD [0x86] page. Equivalent to &#8216;&#8211;page=ei&#8217; in the main description.</p>
<dt><code>-?</code></p>
<dd>output usage message and exit. Ignore all other parameters.</dl>
<h2>Examples</h2>
<p>The examples in this page use Linux device names. For suitable device names in other supported Operating Systems see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. </p>
<p> To view the standard inquiry response use without options: </p>
<p>sg_inq&nbsp;<wbr>/dev/sda </p>
<p> Some SCSI devices include version descriptors indicating the various SCSI standards and drafts they support. They can be viewed with: </p>
<p>sg_inq -d&nbsp;<wbr>/dev/sda </p>
<p> Modern SCSI devices include Vital Product Data (VPD)pages which can be viewed with the SCSI INQUIRY command. To list the supported VPD pages (but not their contents) try: </p>
<p>sg_inq -e&nbsp;<wbr>/dev/sda </p>
<p> Some VPD pages can be read with the sg_inq utility but a newer utility called sg_vpd specializes in showing their contents. The sdparm utility can also be used to show the contents of VPD pages. </p>
<p> Further examples of sg_inq together with some typical output can be found on <a rel="nofollow" href="http://sg.danny.cz/sg/sg3_utils.html">http://sg.danny.cz/sg/sg3_utils.html</a> web page.</p>
<h2>Author</h2>
<p>Written by Douglas Gilbert</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2001-2013 Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sg_opcodes/">sg_opcodes</a>(8), <a href="/docs/linux/man/8-sg_vpd/">sg_vpd</a>(8), <a href="/docs/linux/man/8-sdparm/">sdparm</a>(8), <a href="/docs/linux/man/8-hdparm/">hdparm</a>(8), sgdiag(scsirastools)</code> </p>
