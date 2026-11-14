---
title: "sg_vpd(8)"
name: "sg_vpd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_vpd/"
description: "sg_vpd – fetch Vital Product Data (VPD) pages via a SCSI INQUIRY command"
---

<p>sg_vpd &#8211; fetch Vital Product Data (VPD) pages via a SCSI INQUIRY command</p>
<h2>Synopsis</h2>
<p><code>sg_vpd</code> [<i>&#8211;enumerate</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;ident</i>] [<i>&#8211;long</i>] [<i>&#8211;maxlen=LEN</i>] [<i>&#8211;page=PG</i>] [<i>&#8211;quiet</i>] [<i>&#8211;raw</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>This utility fetches a Vital Product Data page and decodes it or outputs it in ASCII hexadecimal or binary. VPD pages are fetched with a SCSI INQUIRY command. </p>
<p> Probably the most important page is the Device Identification VPD page (page number: 0x83). Since SPC-3, support for this page has been flagged as mandatory. This page can be fetched by using the <i>&#8211;ident</i> option. </p>
<p> The reference document used for interpreting VPD pages (and the INQUIRY standard response) is T10/1713-D Revision 36e (SPC-4, 24 August 2012) found at <a rel="nofollow" href="http://www.t10.org">http://www.t10.org</a> . Obsolete and reserved items in the standard INQUIRY response output are displayed in square brackets. </p>
<p> When no options are given, other than a <i>DEVICE</i>, then the &quot;Supported VPD pages&quot; (0x0) VPD page is fetched and decoded.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well. The options are arranged in alphabetical order based on the long option name.</p>
<dl>
<dt><code>-e</code>, <code>&#8211;enumerate</code></p>
<dd>list the names of the known VPD pages, first the standard pages, then the vendor specific pages. Each group is sorted in abbreviation order. The <i>DEVICE</i> and other options are ignored and this utility exits after listing the VPD page names.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>outputs the usage message summarizing command line options then exits. Ignores <i>DEVICE</i> if given.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>outputs the requested VPD page in ASCII hexadecimal. Can be used multiple times, see section on the ATA information vpd page.</p>
<dt><code>-i</code>, <code>&#8211;ident</code></p>
<dd>decode the device identification (0x83) VPD page. When used once this option has the same effect as &#8216;&#8211;page=di&#8217;. When use twice then the short form of the device identification VPD page&#8217;s logical unit designator is decoded. In the latter case this option has the same effect as &#8216;&#8211;quiet &#8211;page=di_lu&#8217;.</p>
<dt><code>-l</code>, <code>&#8211;long</code></p>
<dd>when decoding some VPD pages, give a little more output. For example the ATA Information VPD page only shows the signature (in hex) and the IDENTIFY (PACKET) DEVICE (in hex) when this option is given.</p>
<dt><code>-m</code>, <code>&#8211;maxlen</code>=<i>LEN</i></p>
<dd>where <i>LEN</i> is the (maximum) response length in bytes. It is placed in the cdb&#8217;s &quot;allocation length&quot; field. If not given (or <i>LEN</i> is zero) then 252 is used (apart from the ATA Information VPD page which defaults to 572) and, if the response indicates this value is insufficient, another INQUIRY command is sent with a larger value in the cdb&#8217;s &quot;allocation length&quot; field. If this option is given and <i>LEN</i> is greater than 0 then only one INQUIRY command is sent. Since many simple devices implement the INQUIRY command badly (and do not support VPD pages) then the safest value to use for <i>LEN</i> is 36. See the sg_inq man page for the more information.</p>
<dt><code>-p</code>, <code>&#8211;page</code>=<i>PG</i></p>
<dd>where <i>PG</i> is the VPD page to be decoded or output. The <i>PG</i> argument can either be an abbreviation, a number or a pair or numbers separated by a comma. The VPD page abbreviations can be seen by using the <i>&#8211;enumerate</i> option. If a number is given it is assumed to be decimal unless it has a hexadecimal indicator which is either a leading &#8216;0x&#8217; or a trailing &#8216;h&#8217;. If one number is given then it is assumed to be a VPD page number. If two numbers are given the second number indicates which vendor specific VPD page to decode when several pages share the same VPD page number. If this option is not given (nor &#8216;-i&#8217;, &#8216;-l&#8217; nor &#8216;-V&#8217;) then the &quot;Supported VPD pages&quot; (0x0) VPD page is fetched and decoded. If <i>PG</i> is &#8216;-1&#8217; or &#8216;sinq&#8217; then the standard INQUIRY response is output.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>suppress the amount of decoding output.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>output requested VPD page in binary. The output should be piped to a file or another utility when this option is used. The binary is sent to stdout, and errors are sent to stderr.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increases the level or verbosity.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print out version string then exit.</dl>
<h2>Ata Information Vpd Page</h2>
<p>This VPD page (0x89 or &#8216;ai&#8217;) is defined by the SCSI to ATA Translation standard. It contains information about the SAT layer, the &quot;signature&quot; of the ATA device and the response to the ATA IDENTIFY (PACKET) DEVICE command. The latter part has 512 bytes of identity, capability and settings data which the hdparm utility is capable of decoding (so this utility doesn&#8217;t decode it). </p>
<p> To unclutter the output for this page, the signature and the IDENTIFY (PACKET) DEVICE response are not output unless the <i>&#8211;long</i> option (or <i>&#8211;hex</i> or <i>&#8211;raw</i>) are given. When the <i>&#8211;long</i> option is given the IDENTIFY (PACKET) DEVICE response is output as 256 (16 bit) words as is the fashion for ATA devices. To see that response as a string of bytes use the &#8216;-HH&#8217; option. To format the output suitable for hdparm to decode use either the &#8216;-HHH&#8217; or &#8216;-rr&#8217; option. For example if &#8216;dev/sdb&#8217; is a SATA disk behind a SAT layer then this command: &#8216;sg_vpd -p ai -HHH /dev/sdb | hdparm &#8211;Istdin&#8217; should decode the ATA IDENTIFY (PACKET) DEVICE response.</p>
<h2>Notes</h2>
<p>Since some VPD pages (e.g. the Extended INQUIRY page) depend on settings in the standard INQUIRY response, then the standard INQUIRY response is output as a pseudo VPD page when <i>PG</i> is set to &#8216;-1&#8217; or &#8216;sinq&#8217;. Also the decoding of some fields (e.g. the Extended INQUIRY page&#8217;s SPT field) is expanded when the &#8216;&#8211;long&#8217; option is given using the standard INQUIRY response information (e.g. the PDT and the PROTECT fields). </p>
<p> In the 2.4 series of Linux kernels the <i>DEVICE</i> must be a SCSI generic (sg) device. In the 2.6 series block devices (e.g. disks and ATAPI DVDs) can also be specified. For example &quot;sg_inq /dev/sda&quot; will work in the 2.6 series kernels. From lk 2.6.6 other SCSI &quot;char&quot; device names may be used as well (e.g. &quot;/dev/st0m&quot;).</p>
<h2>Exit Status</h2>
<p>The exit status of sg_vpd is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Examples</h2>
<p>The examples in this page use Linux device names. For suitable device names in other supported Operating Systems see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page. To see the VPD pages that a device supports, use with no options. The command line invocation is shown first followed by a typical response:<br />
#&nbsp;<wbr>sg_vpd&nbsp;<wbr>/dev/sdb<br />
 Supported VPD pages VPD page: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Supported VPD pages&nbsp;<wbr>[sv] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Unit serial number&nbsp;<wbr>[sn] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Device identification&nbsp;<wbr>[di] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Extended inquiry data&nbsp;<wbr>[ei] </p>
<p>&nbsp;<wbr>&nbsp;<wbr>Block limits&nbsp;<wbr>(SBC)&nbsp;<wbr>[bl] To see the VPD page numbers associated with each supported page then add the &#8216;&#8211;long&#8217; option to the above command line. To view a VPD page either its number or abbreviation can be given to the &#8216;&#8211;page=&#8217; option. The page name abbreviations are shown within square brackets above. In the next example the Extended inquiry data VPD page is listed: </p>
<pre><code># sg_vpd --page=ei /dev/sdb

extended INQUIRY data VPD page:

ACTIVATE_MICROCODE=0 SPT=0 GRD_CHK=0 APP_CHK=0 REF_CHK=0

UASK_SUP=0 GROUP_SUP=0 PRIOR_SUP=0 HEADSUP=1 ORDSUP=1 SIMPSUP=1

WU_SUP=0 CRD_SUP=0 NV_SUP=0 V_SUP=0

P_I_I_SUP=0 LUICLR=0 R_SUP=0 CBCS=0

Multi I_T nexus microcode download=0

Extended self-test completion minutes=0

POA_SUP=0 HRA_SUP=0 VSA_SUP=0</code></pre>
<p> To check if any protection types are supported by a disk use the &#8216;&#8211;long&#8217; option on the Extended inquiry data VPD page: </p>
<pre><code># sg_vpd --page=ei --long /dev/sdb


extended INQUIRY data VPD page:

ACTIVATE_MICROCODE=0

SPT=1 [protection types 1 and 2 supported]

GRD_CHK=1

....</code></pre>
<p> Further examples can be found on the <a rel="nofollow" href="http://sg.danny.cz/sg/sg3_utils.html">http://sg.danny.cz/sg/sg3_utils.html</a> web page.</p>
<h2>Author</h2>
<p>Written by Douglas Gilbert</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2012 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>sg_inq(sg3_utils), sg3_utils(sg3_utils), sdparm(sdparm), hdparm(hdparm)</code> </p>
