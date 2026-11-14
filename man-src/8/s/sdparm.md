---
title: "sdparm(8)"
name: "sdparm"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sdparm/"
description: "sdparm – access SCSI modes pages; read VPD pages; send simple SCSI commands."
---

<p>sdparm &#8211; access SCSI modes pages; read VPD pages; send simple SCSI commands.</p>
<h2>Synopsis</h2>
<p><code>sdparm</code> [<i>&#8211;all</i>] [<i>&#8211;clear=STR</i>] [<i>&#8211;command=CMD</i>] [<i>&#8211;dbd</i>] [<i>&#8211;defaults</i>] [<i>&#8211;dummy</i>] [<i>&#8211;flexible</i>] [<i>&#8211;get=STR</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;inquiry</i>] [<i>&#8211;long</i>] [<i>&#8211;num-desc</i>] [<i>&#8211;page=PG[,SPG]</i>] [<i>&#8211;quiet</i>] [<i>&#8211;readonly</i>] [<i>&#8211;save</i>] [<i>&#8211;set=STR</i>] [<i>&#8211;six</i>] [<i>&#8211;transport=TN</i>] [<i>&#8211;vendor=VN</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i> [<i>DEVICE</i>&#8230;] </p>
<p> <code>sdparm</code> <i>&#8211;enumerate</i> [<i>&#8211;all</i>] [<i>&#8211;inquiry</i>] [<i>&#8211;long</i>] [<i>&#8211;page=PG[,SPG]</i>] [<i>&#8211;transport=TN</i>] [<i>&#8211;vendor=VN</i>] </p>
<p> <code>sdparm</code> <i>&#8211;wscan</i> [<i>&#8211;verbose</i>]</p>
<h2>Description</h2>
<p>This utility fetches and potentially changes SCSI device (e.g. disk) mode pages. Inquiry data including Vital Product Data (VPD) pages can also be displayed. Commands associated with starting and stopping the medium; loading and unloading the medium; and other housekeeping function may also be issued by this utility. </p>
<p> Of the three invocations shown in the synopsis, the first is the most general. The second variant that uses <i>&#8211;enumerate</i> is for dumping information held in sdparm&#8217;s internal tables. The last variant is for Windows only and lists the available device names; see the OPTIONS entry for <i>&#8211;wscan</i>. </p>
<p> If no options (other than <i>DEVICE</i>) are given then a selection of common mode page fields for that device are listed. If the <i>&#8211;long</i> option is also given then a description of the fields is placed on the right of each line. If the <i>&#8211;all</i> option is given then all known mode page fields for that device are listed. Individual fields can be displayed with the <i>&#8211;get=STR</i> option (e.g. &#8216;&#8211;get=WCE&#8217; to fetch the state of the Writeback Cache Enable field). </p>
<p> This utility completes with an exit status of 0 when successful. For other values see the EXIT STATUS section below. </p>
<p> One or more <i>DEVICE</i> arguments can be given. The utility will essentially apply the given options to each <i>DEVICE</i> in the list. If an error is detected, it is noted and the utility continues. Error value 5 (file open or close problem) is treated as lower priority when other errors are detected. The exit status is the most recently detected error value (excluding error value 5 if other errors have been detected). If all actions succeed the exit status is zero. </p>
<p> By default this utility shows mode pages that are common to all transport protocols. These are termed as &quot;generic&quot; mode pages. If there is no match on a generic mode page name or field then those pages specific to the SAS transport are checked. Transport protocol specific mode pages are selected with the <i>&#8211;transport=TN</i> option. See the TRANSPORT section below. Vendor specific mode pages are selected with the <i>&#8211;vendor=VN</i> option. See the VENDORS section below. </p>
<p> Although originally for SCSI disks (or storage devices that appear to the OS as SCSI disks) many of the mode pages are for other SCSI device types. These include CD/DVD players that use the ATAPI (or any other) transport, SCSI tapes drives and SCSI enclosures. </p>
<p> When the <i>&#8211;inquiry</i> option is given without a page number then the Device Identification VPD page (page number 0x83) is requested and if found it is decoded and output. If no page number is given and the <i>&#8211;all</i> option is given then a list of VPD page names (but not their contents) supported by the <i>DEVICE</i> is output. When both the <i>&#8211;inquiry</i> and <i>&#8211;page=PG</i> options are given then the VPD page can be specified as an abbreviation (e.g. &quot;sp&quot; for the SCSI ports VPD page) or numerically (e.g. &quot;0x88&quot;). If a VPD page is returned by the <i>DEVICE</i> but sdparm cannot decode it or the <i>&#8211;hex</i> option is given then it is output in hex.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well. If an option takes a numeric argument then that argument is assumed to be decimal unless otherwise indicated (e.g. with a leading &quot;0x&quot; or a trailing &quot;h&quot;). The options are in alphabetical order, based on the long option name.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd>output all recognized fields for the device type (e.g. disk) of the <i>DEVICE</i>. Without this option (or the <i>&#8211;page=PG[,SPG]</i> option) the default action is to output a relatively small number of commonly used fields from different pages. When a specific (mode) page number is given with the <i>&#8211;page=PG[,SPG]</i> option then all the fields of that page are output (irrespective of the setting of this option). For this option&#8217;s action when used with the <i>&#8211;enumerate</i> option see the ENUMERATE section below.</p>
<dt><code>-c</code>, <code>&#8211;clear</code>=<i>STR</i></p>
<dd>In its simplest form <i>STR</i> contains a field acronym_name or a field numerical descriptor. In the absence of an explicit value argument (e.g. &#8216;&#8211;clear=WCE=1&#8217;), the field has its value cleared to zero. See the PARAMETERS section below.</p>
<dt><code>-C</code>, <code>&#8211;command</code>=<i>CMD</i></p>
<dd>Perform given <i>CMD</i>. See section below on COMMANDS. To enumerate supported commands use &#8216;-e -C x&#8217; (using any CMD name, valid or otherwise).</p>
<dt><code>-B</code>, <code>&#8211;dbd</code></p>
<dd>disable block descriptors. This is a bit in MODE SENSE cdbs that rarely needs to be set. One known case is a MODE SENSE 6 issued to a Reduced Block Commands (RBC) device where the RBC standard says it shall be set.</p>
<dt><code>-D</code>, <code>&#8211;defaults</code></p>
<dd>sets the given mode page to its default values. Requires the <i>&#8211;page=PG[,SPG]</i> option to be given to specify the mode page. To make the default mode page values also the saved mode page values, use the <i>&#8211;save</i> option as well.</p>
<dt><code>-d</code>, <code>&#8211;dummy</code></p>
<dd>when set inhibits changes being placed in the <i>DEVICE</i>&#8216;s mode page. Instead the mode data that would have been sent to a MODE SELECT command, is output in ASCII hex to the console. This option is mainly for testing.</p>
<dt><code>-e</code>, <code>&#8211;enumerate</code></p>
<dd>lists out descriptive information about the pages and fields known to this utility. Ignores the <i>DEVICE</i> argument and other options apart from the <i>&#8211;all</i>, <i>&#8211;inquiry</i>, <i>&#8211;long</i>, <i>&#8211;page=PG[,SPG]</i>, <i>&#8211;transport=TN</i> and <i>&#8211;vendor=VN</i>. If <i>&#8211;enumerate</i> is given without other options then the known (generic) mode pages are listed. See the ENUMERATE section below.</p>
<dt><code>-f</code>, <code>&#8211;flexible</code></p>
<dd>Some devices, bridges and/or drivers attempt crude transformations between mode sense 6 and 10 byte commands without correctly rebuilding the response. This will cause the response to be mis-interpreted (usually with an error saying the response is malformed). With this option, the length of the response is checked, and if it looks wrong, various corrections are attempted. This option will also allow mode pages that don&#8217;t belong to the current device&#8217;s peripheral type to be listed.</p>
<dt><code>-g</code>, <code>&#8211;get</code>=<i>STR</i></p>
<dd>In its simplest form <i>STR</i> contains a field acronym_name or a field numerical descriptor. The field is fetched from mode page. See the PARAMETERS section below. The <i>&#8211;long</i> and <i>&#8211;hex</i> options effect the output format. Also if a value of &quot;1&quot; is given (e.g. &#8216;&#8211;get=WCE=1&#8217;) only the current value is output (i.e. not the change mask, the default value and the saved value).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>rather than trying to decode mode (or VPD) pages, print them out in hex. When used with the <i>&#8211;get=STR</i> option the corresponding current, changeable, default and saved values are output in hex, prefixed by &quot;0x&quot; and space separated. If a value of &quot;1&quot; is given with the <i>&#8211;get=STR</i> option (e.g. &#8216;&#8211;get=WCE=1&#8217;) then only the current value is output in hex, prefixed by &quot;0x&quot;. If a value of &quot;2&quot; is given with the <i>&#8211;get=STR</i> option then only the current value is output as a (signed) integer. This option can be used multiple times (e.g. &#8216;-HH&#8217;). Useful with the ATA Information VPD page which usually outputs its IDENTIFY (PACKET) DEVICE response in 16 bit hex words; with &#8216;-HH&#8217; outputs that response in hex bytes; with &#8216;-HHH&#8217; outputs the same response in a format suitable for &#8216;hdparm &#8211;Istdin&#8217; to decode.</p>
<dt><code>-i</code>, <code>&#8211;inquiry</code></p>
<dd>output INQUIRY VPD pages. In the absence of this option the default action is to output mode pages. If the <i>&#8211;inquiry</i> option is given without the <i>&#8211;page=PG[,SPG]</i> option then the device identification VPD page (0x83) is decoded and output. If this option and the <i>&#8211;all</i> option are given then the supported VPD pages page (0x0) is decoded and output.</p>
<dt><code>-l</code>, <code>&#8211;long</code></p>
<dd>output extra information. In the case of mode page fields a description (with units if applicable) is output to the right. If used twice, then for some fields more information about its values is given on one or more following lines, each prefixed by a tab character. For usage with <i>&#8211;enumerate</i> see the ENUMERATE section below.</p>
<dt><code>-n</code>, <code>&#8211;num-desc</code></p>
<dd>for a mode page that can have descriptors, the number of descriptors for the given page on the <i>DEVICE</i> is output. Otherwise 0 is output.</p>
<dt><code>-p</code>, <code>&#8211;page</code>=<i>PG[,SPG]</i></p>
<dd>supply the page number (<i>PG</i>) and optionally the sub page number (<i>SPG</i>) of the mode (or VPD) page to fetch. These numbers are interpreted as decimal unless prefixed with &quot;0x&quot; or a trailing. Sub page numbers are only valid for mode pages (not VPD pages). Alternatively an abbreviation for a page can be given (see next entry).</p>
<dt><code>-p</code>, <code>&#8211;page</code>=<i>STR</i></p>
<dd>a two or three letter abbreviation for a page can be given. Known mode page abbreviations are checked first followed by known VPD page abbreviations. For example &#8216;&#8211;page=ca&#8217; matches the caching mode page. If no match is found then an error is issued and a list of possibilities in the current context is given (so &#8216;-p x&#8217; can be quite useful). If the <i>STR</i> matches a known VPD page abbreviation then the <i>&#8211;inquiry</i> option is assumed. For usage with <i>&#8211;enumerate</i> see the ENUMERATE section below.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd>suppress output of device name followed by the vendor, product and revision strings fetched from an INQUIRY response. Without this option such a line is typically the first line output by sdparm. Reduces output from the device identification VPD page, typically to one line (or none) for each of di_lu, di_port, di_target and di_asis.</p>
<dt><code>-r</code>, <code>&#8211;readonly</code></p>
<dd>override other logic to open <i>DEVICE</i> in read-only mode. The default setting of the open read-only/read-write mode depends on the operation requested (e.g. a <i>&#8211;set=STR</i> operation by default will try a read-write mode open on <i>DEVICE</i>). This option may be useful if a command is being sent to an ATA disk via a SCSI command set. For example in Linux &#8216;-C stop&#8217; may require this option to stop an ATA disk being restarted immediately.</p>
<dt><code>-S</code>, <code>&#8211;save</code></p>
<dd>when a mode page is being modified (by using the <i>&#8211;clear=STR</i> and/or <i>&#8211;set=STR</i> options) then the default action is to modify only the current values mode page. When this option is given then the corresponding value(s) in the saved values mode page is also changed. The next time the device is power cycled (or reset) the saved values mode page becomes (i.e. is copied to) the current values mode page. See NOTES section below.</p>
<dt><code>-s</code>, <code>&#8211;set</code>=<i>STR</i></p>
<dd>in its simplest form <i>STR</i> contains a field acronym_name or a field numerical descriptor. In the absence of an explicit value, each acronym_name has its value set to (all) ones. This means a 16 bit field will be set to 0xffff which is 65535 in decimal. Alternatively each acronym_name or numerical descriptor may be followed by &quot;=&lt;n&gt;&quot; where &lt;n&gt; is the value to set that field to. See the PARAMETERS section below.</p>
<dt><code>-6</code>, <code>&#8211;six</code></p>
<dd>The default action of this utility is to issue MODE SENSE and MODE SELECT SCSI commands with 10 byte cdbs. When this option is given the 6 byte cdb variants are used. RBC and old SCSI devices may need this option. This utility outputs a suggestion to use this option if the SCSI status indicates that the 10 byte cdb variant is not supported.</p>
<dt><code>-t</code>, <code>&#8211;transport</code>=<i>TN</i></p>
<dd>Specifies the transport protocol where <i>TN</i> is either a number in the range 0 to 15 (inclusive) or an abbreviation (e.g. &quot;fcp&quot; for the Fibre Channel Protocol). One way to list available transport protocols numbers and their associated abbreviations is to give an invalid transport protocol number such as &#8216;-t x&#8217;; another way is &#8216;-e -l&#8217;.</p>
<dt><code>-M</code>, <code>&#8211;vendor</code>=<i>VN</i></p>
<dd>Specifies the vendor (i.e. manufacturer) where <i>VN</i> is either a number (0 or more) or an abbreviation (e.g. &quot;sea&quot; for Seagate disk vendor specific). One way to list available vendor numbers and their associated abbreviations is to give an invalid vendor number such as &#8216;-M x&#8217;; another way is &#8216;-e -l&#8217;.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output). In some cases more decoding is done (e.g. fields within a standard INQUIRY response).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</p>
<dt><code>-w</code>, <code>&#8211;wscan</code></p>
<dd>this option is available in Windows only. It lists storage device names and the corresponding volumes, if any. When used twice it adds the &quot;bus type&quot; of the closest transport (e.g. a SATA disk in a USB connected enclosure has bus type Usb). When used three times a SCSI adapter scan is added. When used four times only a SCSI adapter scan is shown. See examples below and the &quot;Win32 port&quot; section in the README file.</dl>
<h2>Notes</h2>
<p>The reference document used for interpreting mode and VPD pages (and the INQUIRY standard response) is T10/1713-D Revision 36e (SPC-4, 24 August 2012) found at <a rel="nofollow" href="http://www.t10.org">http://www.t10.org</a> . Obsolete and reserved items in the standard INQUIRY response output are displayed in brackets. </p>
<p> A mode page for which no abbreviation is known (e.g. a vendor specific mode page) can be listed in hexadecimal by using the option combination &#8216;&#8211;page=PG &#8211;hex&#8217;. </p>
<p> Numbers input to sdparm (e.g. in the command line arguments) are assumed to be in decimal unless there is a hexadecimal indicator. A hexadecimal indicator is either a leading &#8216;0x&#8217; or &#8216;0X&#8217; (i.e. the C language convention) or a trailing &#8216;h&#8217; or &#8216;H&#8217; (i.e. the convention used at <a rel="nofollow" href="http://www.t10.org">www.t10.org</a> ). In the case of <i>&#8211;page</i>= either a string or number is expected, so hex numbers like &#8216;ch&#8217; (12) should be prefixed by a zero (e.g. &#8216;0ch&#8217;). </p>
<p> The SPC-4 draft (rev 2) says that devices that implement no distinction between current and saved pages can return an error (ILLEGAL REQUEST, invalid field in cdb) if the SP bit (which corresponds to the <i>&#8211;save</i> option) is _not_ set. In such cases the <i>&#8211;save</i> option needs to be given. </p>
<p> If the <i>&#8211;save</i> option is given but the existing mode page indicates (via its PS bit) that the page is not savable, then this utility generates an error message. That message suggests to try again without the <i>&#8211;save</i> option. </p>
<p> Since the device identification VPD page (acronym_name &quot;di&quot;) potentially contains a lot of diverse designators, several associated acronyms are available. They are &quot;di_lu&quot; for designators associated with the addressed logical unit, &quot;di_port&quot; for designators associated with the target port (which the command arrived via) and &quot;di_target&quot; for designators associated with the target device. When &quot;di&quot; is used designators are grouped by lu, then port and then target device. To see all designators decoded in the order that they appear in the VPD page use &quot;di_asis&quot;. </p>
<p> Only those VPD pages defined by t10.org are decoded by this utility. SPC-4 sets aside VPD pages codes from 0xc0 to 0xff (inclusive) for vendor specific pages some of which are decoded in the sg_vpd utility. </p>
<p> In the linux kernel 2.6 series any device node that understands a SCSI command set (e.g. SCSI disks and CD/DVD drives) may be specified. More precisely the driver that &quot;owns&quot; the device node must support the SG_IO ioctl. In the lk 2.4 series only SCSI generic (sg) device nodes support the SG_IO ioctl. However in the lk 2.4 series other SCSI device nodes are mapped within this utility to their corresponding sg device nodes. So if there is a SCSI disk at /dev/sda then &#8216;sdparm /dev/sda&#8217; will work in both the lk 2.6 and lk 2.4 series. However if there is an ATAPI cd/dvd drive at /dev/hdc then &#8216;sdparm /dev/hdc&#8217; will only work in the lk 2.6 series. </p>
<p> In the Linux 2.6 series, especially with ATA disks, using sdparm to stop (spin down) a disk may not be sufficient and other mechanisms will start the disk again some time later. The user might additionally mark the disk as &quot;offline&quot; with &#8216;echo offline &gt; /sys/block/sda/device/state&#8217; where sda is the block name of the disk. To restart the disk &quot;offline&quot; can be replaced with &quot;running&quot;.</p>
<h2>Parameters</h2>
<p>In their simplest form the <i>&#8211;clear</i>=, <i>&#8211;get</i>= and <i>&#8211;set</i>= options (or their short forms) take an acronym_name such as &quot;WCE&quot;. In the case of &#8216;&#8211;get=WCE&#8217; the value of &quot;Writeback Cache Enable&quot; in the caching mode page will be fetched. In the case of &#8216;&#8211;set=WCE&#8217; that bit will be set (to one). In the case of &#8216;&#8211;clear=WCE&#8217; that bit will be cleared (to zero). When an acronym_name is given then the mode page is imputed from that acronym_name (e.g. WCE is in the caching mode page). </p>
<p> Instead of an acronym_name a field within a mode page can be described numerically with a &lt;start_byte&gt;:&lt;start_bit&gt;:&lt;num_bits&gt; tuple. These are the &lt;start_byte&gt; (origin 0) within the mode page, a &lt;start_bit&gt; (0 to 7 inclusive) and &lt;num_bits&gt; (1 to 64 inclusive). For example, the low level representation of the RCD bit (the &quot;Read Cache Disable bit in the caching mode page) is &quot;2:0:1&quot;. The &lt;start_byte&gt; can optionally be given in hex (e.g. &#8216;&#8211;set=0x2:0:1&#8217; or &#8216;&#8211;set=2h:0:1&#8217;). With this form the <i>&#8211;page</i>= option is required to establish which mode page is to be used. </p>
<p> Either form can optionally be followed by &quot;=&lt;val&gt;&quot;. By default &lt;val&gt; is decimal but can be given in hex in the normal fashion. Here are some examples: &#8216;&#8211;set=2h:0:1=1h&#8217; and &#8216;-s MRIE=0x3&#8217;. When the acronym_name or numeric form following <i>&#8211;clear</i>= is not given an explicit &#8216;=&lt;val&gt;&#8217; then the value defaults to zero. When the acronym_name or numeric form following <i>&#8211;set</i>= is not given an explicit &#8216;=&lt;val&gt;&#8217; then the value defaults to &quot;all ones&quot; (i.e. as many as &lt;num_bits&gt; permits). For example &#8216;&#8211;clear=WCE&#8217; and &#8216;&#8211;clear=WCE=0&#8217; have the same meaning: clear Writeback Cache Enable or, put more simply: turn off the writeback cache. </p>
<p> Multiple fields within the same mode page can be changed by giving a comma separated list of acronym_names and/or the numerical form. For example: &#8216;&#8211;set=TEST,MRIE=6&#8217;. </p>
<p> Some mode page have multiple descriptors. They typically have a fixed header section at the start of the mode page that includes a field containing the number of descriptors that follow. Following the header is a variable number of descriptors. An example is the SAS Phy Control and Discover mode page. An acronym_name may include a trailing &#8216;.&lt;num&gt;&#8217; where &quot;&lt;num&gt;&quot; is a descriptor number (origin 0). For example &#8216;-t sas -g PHID.0&#8217; and &#8216;-t sas -g PHID&#8217; will yield the phy identifier of the first descriptor of the above mode page; &#8216;-t sas -g PHID.1&#8217; will yield the phy identifier of the second descriptor.</p>
<h2>Enumerate</h2>
<p>The <i>&#8211;enumerate</i> option essentially dumps out static information held by this utility. A list of <i>&#8211;enumerate</i> variants and their actions follows. For brevity subsequent examples of options are shown in their shorter form. </p>
<p>&nbsp;<wbr>&#8211;enumerate&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list generic mode page information </p>
<p>&nbsp;<wbr>-e &#8211;all&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list generic mode page contents </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>(i.e. parameters) </p>
<p>&nbsp;<wbr>-e &#8211;page=rw&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list contents of read write error </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>recovery mode page </p>
<p>&nbsp;<wbr>-e &#8211;inquiry&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list VPD pages this utility can decode </p>
<p>&nbsp;<wbr>-e &#8211;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list generic mode pages, transport </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>protocols, mode pages for each </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>supported transport protocol and </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>supported commands </p>
<p>&nbsp;<wbr>-e -l &#8211;all&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>additionally list the contents of </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>each mode page </p>
<p>&nbsp;<wbr>-e &#8211;transport=fcp&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list mode pages for the fcp </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>transport protocol </p>
<p>&nbsp;<wbr>-e -t fcp &#8211;all&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>additionally list the contents of </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>each mode page </p>
<p>&nbsp;<wbr>-e &#8211;vendor=sea&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list vendor specific mode pages for </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&quot;sea&quot;&nbsp;<wbr>(Seagate) </p>
<p>&nbsp;<wbr>-e -M sea &#8211;all&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>additionally list the contents of vendor </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specific mode pages for&nbsp;<wbr>&quot;sea&quot;&nbsp;<wbr>(Seagate) </p>
<p>&nbsp;<wbr>-e -p pcd -l&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>list contents of SAS phy control and </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>discovery mode page plus&nbsp;<wbr>(due to&nbsp;<wbr>&quot;-l&quot;) </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>some descfriptor format information </p>
<p> When known mode pages are listed (via the <i>&#8211;enumerate </i> option) each line starts with a two or three letter abbreviation. This is followed by the page number (in hex prefixed by &quot;0x&quot;) optionally followed by a comma and the subpage number. Finally the descriptive name of the mode page (e.g. as found in SPC-4) is output. </p>
<p> When known parameters (fields) of a mode page are listed, each line starts with an acronym (indented a few spaces). This will match (or be an acronym for) the description for that field found in the (draft) standards. Next are three numbers, separated by colons, surrounded by brackets. These are the start byte (in hex, prefixed by &quot;0x&quot;) of the beginning of the field within the mode page; the starting bit (0 through 7 inclusive) and then the number of bits. The descriptive name of the parameter (field) is then given. If appropriate the descriptive name includes units (e.g. &quot;(ms)&quot; means the units are milliseconds). Adding the &#8216;-ll&#8217; option will list information about possible field values for selected mode page parameters. </p>
<p> Mode parameters for which the num_bits is greater than 1 can be viewed as unsigned integers. Often 16 and 32 bit fields are set to 0xffff and 0xffffffff respectively (all ones) which usually has a special meaning (see drafts). This utility outputs such values as &quot;-1&quot; to save space (rather than their unsigned integer equivalents). &quot;-1&quot; can also be given as the value to a mode page field acronym (e.g. &#8216;&#8211;set=INTT=-1&#8217; sets the interval timer field in the Informational Exceptions control mode page to 0xffffffff).</p>
<h2>Transports</h2>
<p>SCSI transport protocols are a relatively specialized area that can be safely ignored by the majority of users. </p>
<p> Some transport protocols have protocol specific mode pages. These are usually the disconnect-reconnect (0x2), the protocol specific logical unit (0x18) and the protocol specific port (0x19) mode pages. In some cases the latter mode page has several subpages. The most common transport protocol abbreviations likely to be used are &quot;fcp&quot;, &quot;spi&quot; and &quot;sas&quot;. </p>
<p> Many of the field names are re-used in the same position so the acronym_name namespaces have been divided between generic mode pages (i.e. when the <i>&#8211;transport</i>= option is _not_ given) and a namespace for each transport protocol. A LUPID field from the protocol specific logical unit (0x18) mode page and the PPID field from protocol specific port (0x19) mode page are included in the generic modes pages; this is so the respective (transport) protocol identifiers can be seen. In most cases the user will know what the &quot;port&quot; transport is (i.e. the same transport as the HBA in the computer) but the logical unit&#8217;s transport could be different.</p>
<h2>Vendors</h2>
<p>SCSI leaves a lot of space for vendor specific information. Often this is described in product manuals. The <i>&#8211;vendor=VN</i> (or <i>-M=VN</i>) option allows known vendor specific mode pages to be examined and/or modified by acronym. </p>
<p> In this utility the syntax and semantics of vendor specific mode pages is very similar to those of transport protocol specific mode pages. Both cannot be specified together. Vendor specific modes pages can still be accessed numerically (as shown at the end of the EXAMPLES section).</p>
<h2>Commands</h2>
<p>The command option sends a SCSI command to the <i>DEVICE</i>. If the command fails then this is reflected in the non-zero exit status. To obtain more information about the error use the <i>-v</i> option.</p>
<dl>
<dt>capacity</p>
<dd>sends a READ CAPACITY command (valid for disks and cd/dvd media). If successful yields &quot;blocks: &quot; [the number of blocks], &quot;block_length: &quot; [typically either 512 or 2048] and &quot;capacity_mib: &quot; [capacity in MibiBytes (1048576 byte units)].</p>
<dt>eject</p>
<dd>stops the medium and ejects it from the device. Note that ejection (by command or button) may be prevented in which case the &#8216;unlock&#8217; command may be useful in extreme cases. Typically only appropriate for cd/dvd drives and disk drives with removable media. Objects if sent to another peripheral device type (but objection can be overridden with &#8216;-f&#8217; option).</p>
<dt>load</p>
<dd>loads the medium and and starts it (i.e. spins it up). See &#8216;eject&#8217; command for supported device types.</p>
<dt>profile</p>
<dd>lists the various formats that a CD/DVD/HD-DVD/BD drive supports. These are called &quot;profiles&quot; in the MMC standard. The profiles are listed one per line. If media is in the drive then the profile that matches the media (if any) has an &quot;*&quot; to the right of the line.</p>
<dt>ready</p>
<dd>sends the &quot;Test Unit Ready&quot; SCSI command to the <i>DEVICE</i>. No error is reported if the device will respond to data requests (e.g. READ) in a reasonable timescale. For example, if a disk is stopped then it will report &quot;not ready&quot;. All devices should respond to this command.</p>
<dt>sense</p>
<dd>sends a REQUEST SENSE command. It reports a hardware threshold exceeded, warning or low power condition if flagged. If a progress indication is present (e.g. during a format) then it will be output as a percentage. Yields a process status of 0 if the command succeeds and the sense key is 0; else yields 1. The <i>&#8211;quiet</i> option can be used to lessen output, and <i>&#8211;hex</i> to output sense data in hex.</p>
<dt>speed=SPEED</p>
<dd>permits the speed of a CD, DVD, HD_DVD or BD disc in a drive to be set (or at least influenced). It has this format: <i>&#8211;command=speed=SPEED</i> where SPEED is in kilobytes per second. In this case a kilobyte is 1000 bytes. The &quot;times one&quot; speed for a CD is 176.4 kB/s, for a DVD is 1350 kB/s and for both HD-DVD and BD it is 4500 kB/s. If SPEED is zero then the drive is set to the speed that it considers gives optimal performance. This command sends a SET STREAMING multi-media command (MMC) to the drive. The EXACT bit is clear so the drive will round the given SPEED as necessary. The command is designed to control read speed; setting write speed should be left to &quot;burning&quot; programs.</p>
<dt>start</p>
<dd>starts the medium (i.e. spins it up). Harmless if medium has already been started. See &#8216;eject&#8217; command for supported device types. If the <i>DEVICE</i> is an ATA disk in Linux the &#8216;&#8211;readonly&#8217; option may be required.</p>
<dt>stop</p>
<dd>stops the medium (i.e. spins it down). Harmless if medium has already been stopped. See &#8216;eject&#8217; command for supported device types. If the <i>DEVICE</i> is an ATA disk in Linux the &#8216;&#8211;readonly&#8217; option may be required. See the NOTES section above.</p>
<dt>sync</p>
<dd>sends a SYNCHRONIZE CACHE command. The device should flush any data held in its (volatile) buffers to the media.</p>
<dt>unlock</p>
<dd>tells a device to allow medium removal. It uses the SCSI &quot;prevent allow medium removal&quot; command. This is desperation stuff, possibly overriding a prevention applied by the OS on a mounted file system. The &quot;eject&quot; utility (from the &quot;eject&quot; package) is more graceful and should be tried first. This command is only appropriate for devices with removable media.</dl>
<p> For loading and ejecting tapes the mt utility should be used (i.e. not these commands). The &#8216;ready&#8217; command is valid for tape devices.</p>
<h2>Examples</h2>
<p>To list the common (generic) mode parameters of a disk:<br />
sdparm&nbsp;<wbr>/dev/sda To list the designators within the device identification VPD page of a disk:<br />
sdparm &#8211;inquiry&nbsp;<wbr>/dev/sda To see all parameters for the caching mode page: </p>
<pre><code>sdparm --page=ca /dev/sda</code></pre>
<p> To see all parameters for the caching mode page with parameter descriptions to the right: sdparm &#8211;page=ca &#8211;long /dev/sda To get the WCE values (current changeable default and saved) in hex:<br />
sdparm -g WCE -H&nbsp;<wbr>/dev/sda<br />
 0x01 0x00 0x01 0x01 To get the WCE current value in hex: sdparm -g WCE=1 -H /dev/sda</p>
<p>0x01 To set the &quot;Writeback Cache Enable&quot; bit in the current values page: sdparm &#8211;set=WCE /dev/sda To set the &quot;Writeback Cache Enable&quot; bit in the current and saved values page: sdparm &#8211;set=WCE &#8211;save /dev/sda To set the &quot;Writeback Cache Enable&quot; and clear &quot;Read Cache Disable&quot;: sdparm &#8211;set=WCE &#8211;clear=RCD &#8211;save /dev/sda The previous example can also by written as: sdparm -s WCE=1,RCD=0 -S /dev/sda To re-establish the manufacturer&#8217;s defaults in the current and saved values of the caching mode page: sdparm &#8211;page=ca &#8211;defaults &#8211;save /dev/sda If an ATAPI cd/dvd drive is at /dev/hdc then its common (mode) parameters could be listed in the lk 2.6 series with:<br />
sdparm&nbsp;<wbr>/dev/hdc If there is a DVD in the drive at /dev/hdc then it could be ejected in the lk 2.6 series with: sdparm &#8211;command=eject /dev/hdc If the ejection is being prevented by software then that can be overridden with: sdparm &#8211;command=unlock /dev/hdc One disk vendor has a &quot;Performance Mode&quot; bit (PM) in the vendor specific unit attention mode page [0x0,0x0]. PM=0 is server mode (the default) while PM=1 is desktop mode. Desktop mode can be set (both current and saved values) with: sdparm &#8211;page=0 &#8211;set=2:7:1=1 &#8211;save /dev/sda The resultant change can be viewed in hex with the <i>&#8211;hex</i> option as there are no acronyms for vendor extensions yet. The PM bit is now covered by vendor specific mode pages and the above can also be accomplished with: sdparm &#8211;vendor=sea &#8211;set=PM &#8211;save /dev/sda What follows are some examples from Windows using the &#8216;&#8211;wscan&#8217; option. The idea is to list the storage device names on the system that might be invoked by other uses of sdparm.<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sdparm &#8211;wscan<br />
 PD0 [C] FUJITSU MHY2160BH 0000<br />
 PD1 [DF] WD 2500BEV External 1.05 WD-WXE90<br />
 CDROM0 [E] MATSHITA DVD/CDRW UJDA775 CB03 So &#8216;sdparm -a CDROM0&#8217; and &#8216;sdparm -a E&#8217; will show all the (known) mode page fields for the Matshita DVD/CD drive. By using the &#8216;&#8211;wsacan&#8217; option twice, the bus type (as seen by the OS) is added to the output:<br />
&nbsp;<wbr>&nbsp;<wbr>#&nbsp;<wbr>sdparm -ww<br />
 PD0 [C] &lt;Ata &gt; FUJITSU MHY2160BH 0000<br />
 PD1 [DF] &lt;Usb &gt; WD 2500BEV External 1.05 WD-WXE90<br />
 CDROM0 [E] &lt;Atapi&gt; MATSHITA DVD/CDRW UJDA775 CB03 And the pattern continues to add a SCSI adapter scan. This may be useful if there are specialized storage related devices (e.g. a SES device in an enclosure) but does add much extra information in this case. </p>
<pre><code># sdparm -www

PD0     [C]     &lt;Ata  &gt;  FUJITSU   MHY2160BH         0000

PD1     [DF]    &lt;Usb  &gt;  WD        2500BEV External  1.05  WD-WXE90

CDROM0  [E]     &lt;Atapi&gt;  MATSHITA DVD/CDRW UJDA775  CB03




SCSI0:0,0,0   claimed=1 pdt=0h  FUJITSU   MHY2160BH         0000

SCSI1:0,0,0   claimed=1 pdt=5h  MATSHITA  DVD/CDRW UJDA775  CB03
</code></pre>
<h2>Exit Status</h2>
<p>To aid scripts that call sdparm, the exit status is set to indicate success (0) or failure (1 or more). Note that some of the lower values correspond to the SCSI sense key values. The exit status values are:</p>
<dl>
<dt><code>0</code></p>
<dd>success</p>
<dt><code>1</code></p>
<dd>syntax error. Either illegal command line options, options with bad arguments or a combination of options that is not permitted.</p>
<dt><code>2</code></p>
<dd>the <i>DEVICE</i> reports that it is not ready for the operation requested. The device may be in the process of becoming ready (e.g. spinning up but not at speed) so the utility may work after a wait.</p>
<dt><code>3</code></p>
<dd>the <i>DEVICE</i> reports a medium or hardware error (or a blank check). For example an attempt to read a corrupted block on a disk will yield this value.</p>
<dt><code>5</code></p>
<dd>the <i>DEVICE</i> reports an &quot;illegal request&quot; with an additional sense code other than &quot;invalid operation code&quot;. This is often a supported command with a field set requesting an unsupported capability. For commands that require a &quot;service action&quot; field this value can indicate that the command is not supported.</p>
<dt><code>6</code></p>
<dd>the <i>DEVICE</i> reports a &quot;unit attention&quot; condition. This usually indicates that something unrelated to the requested command has occurred (e.g. a device reset) potentially before the current SCSI command was sent. The requested command has not been executed by the device. Note that unit attention conditions are usually only reported once by a device.</p>
<dt><code>9</code></p>
<dd>the <i>DEVICE</i> reports an illegal request with an additional sense code of &quot;invalid operation code&quot; which means that it doesn&#8217;t support the requested command.</p>
<dt><code>11</code></p>
<dd>the <i>DEVICE</i> reports an aborted command. In some cases aborted commands can be retried immediately (e.g. if the transport aborted the command due to congestion).</p>
<dt><code>15</code></p>
<dd>the utility is unable to open, close or use the given <i>DEVICE</i>. The given file name could be incorrect or there may be permission problems. Adding the <i>-v</i> option may give more information.</p>
<dt><code>20</code></p>
<dd>the <i>DEVICE</i> reports it has a check condition but &quot;no sense&quot;. Some polling commands (e.g. REQUEST SENSE) can react this way. It is unlikely that this value will occur as an exit status.</p>
<dt><code>21</code></p>
<dd>the <i>DEVICE</i> reports a &quot;recovered error&quot;. The requested command was successful. Most likely a utility will report a recovered error to stderr and continue, probably leaving the utility with an exit status of 0 .</p>
<dt><code>33</code></p>
<dd>the command sent to <i>DEVICE</i> has timed out. This occurs in Linux only; in other ports a command timeout will appear as a transport (or OS) error.</p>
<dt><code>97</code></p>
<dd>the response to a SCSI command failed sanity checks.</p>
<dt><code>98</code></p>
<dd>the <i>DEVICE</i> reports it has a check condition but the error doesn&#8217;t fit into any of the above categories.</p>
<dt><code>99</code></p>
<dd>any errors that can&#8217;t be categorized into values 1 to 98 may yield this value. This includes transport and operating system errors after the command has been sent to the device.</dl>
<p> Most of the error conditions reported above will be repeatable (an example of one that is not is &quot;unit attention&quot;) so the utility can be run again with the <i>-v</i> option (or several) to obtain more information.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2005-2013 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>Web Site</h2>
<p>There is a web page discussing this package at <a rel="nofollow" href="http://sg.danny.cz/sg/sdparm.html">http://sg.danny.cz/sg/sdparm.html</a> .</p>
<h2>See Also</h2>
<p><code>hdparm(hdparm),</code> <code>sg_modes, sg_wr_mode, sginfo, sg_inq, sg_vpd(all in sg3_utils),</code> <code>smartmontools(smartmontools.sourceforge.net), mt, eject(eject),</code> </p>
