---
title: "sg_modes(8)"
name: "sg_modes"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_modes/"
description: "sg_modes – reads mode pages with SCSI MODE SENSE command"
---

<p>sg_modes &#8211; reads mode pages with SCSI MODE SENSE command</p>
<h2>Synopsis</h2>
<p><code>sg_modes</code> [<i>&#8211;all</i>] [<i>&#8211;control=PC</i>] [<i>&#8211;dbd</i>] [<i>&#8211;dbout</i>] [<i>&#8211;examine</i>] [<i>&#8211;flexible</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;list</i>] [<i>&#8211;llbaa</i>] [<i>&#8211;maxlen=LEN</i>] [<i>&#8211;page=PG[,SPG]</i>] [<i>&#8211;raw</i>] [<i>-R</i>] [<i>&#8211;six</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>DEVICE</i>] </p>
<p> <code>sg_modes</code> [<i>-6</i>] [<i>-a</i>] [<i>-A</i>] [<i>-c=PC</i>] [<i>-d</i>] [<i>-D</i>] [<i>-e</i>] [<i>-f</i>] [<i>-h</i>] [<i>-H</i>] [<i>-l</i>] [<i>-L</i>] [<i>-m=LEN</i>] [<i>-p=PG[,SPG]</i>] [<i>-r</i>] [<i>-subp=SPG</i>] [<i>-v</i>] [<i>-V</i>] [<i>-?</i>] [<i>DEVICE</i>]</p>
<h2>Description</h2>
<p>This utility sends a MODE SENSE SCSI command to the <i>DEVICE</i> and outputs the response. There is a 6 byte and 10 byte (cdb) variant of the MODE SENSE command, this utility defaults to the 10 byte variant. </p>
<p> This utility decodes mode page headers and block descriptors but outputs the contents of each mode page in hex. It also has no facility to change the mode page contents or block descriptor data. Mode page contents are decoded and can be changed by the <code>sdparm</code> utility. </p>
<p> This utility supports two command line syntaxes, the preferred one is shown first in the synopsis and explained in this section. A later section on the old command line syntax outlines the second group of options. </p>
<p> If no page is given (and <i>&#8211;list</i> is not selected) then <i>&#8211;all</i> is assumed. The <i>&#8211;all</i> option requests all mode pages (but not subpages) in a single response.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd>output all the mode pages reported by the <i>DEVICE</i>. This is what the page code 63 (0x3f) is defined to do. When used once, mode subpages are not fetched. When used twice (e.g. &#8216;-aa&#8217;), all mode pages and subpages are requested which is equivalent to &#8216;&#8211;page=63,255&#8217;.</p>
<dt><code>-c</code>, <code>&#8211;control</code>=<i>PC</i></p>
<dd><i>PC</i> is the page control value. Up to four different versions of each page are held by the device: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>0</code>&nbsp;<wbr>: current values&nbsp;<wbr>(i.e. those active at present) </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>1</code>&nbsp;<wbr>: changeable values </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>2</code>&nbsp;<wbr>: default values&nbsp;<wbr>(i.e. the manufacturer&#8217;s settings) </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>3</code>&nbsp;<wbr>: saved values<br />
 The changeable values are bit masks showing which fields could be changed with a MODE SELECT. The saved values will be re-instated the next time the device is power cycled or reset. If this option is not given then current values [0] are assumed.</p>
<dt><code>-d</code>, <code>&#8211;dbd</code></p>
<dd>disable block descriptors. By default, block descriptors (usually one (for disks) or none) are returned in a MODE SENSE response. This option sets the &quot;disable block descriptors&quot; (DBD) bit in the cdb which instructs the device not to return any block descriptors in its response. Older devices may not support this setting and may return an &quot;illegal request&quot; sense key; alternatively they may ignore it. Oddly the Reduced Block Command set (RBC) requires this bit set.</p>
<dt><code>-D</code>, <code>&#8211;dbout</code></p>
<dd>disable outputting block descriptors. Irrespective of whether block descriptors are present in the response or not, they are not output.</p>
<dt><code>-e</code>, <code>&#8211;examine</code></p>
<dd>examine each mode page in the range 0 through to 62 (inclusive). If some response is given then print out the mode page name or number (in hex) if the name is not known.</p>
<dt><code>-f</code>, <code>&#8211;flexible</code></p>
<dd>Some devices, bridges and/or drivers attempt crude translations between MODE SENSE 6 and 10 byte commands without correcting the response. This will cause the response to be mis-interpreted (usually with an error saying the response is malformed). With this option, the length of the response is checked, and if it looks wrong, the response is then decoded as if the other mode sense (cdb length) was sent.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print out the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>The default action is to decode known mode page numbers (and subpage numbers) into text. When this option is used once, the response is output in hexadecimal. When this option is used twice, mode page numbers and page control values are output in hex.</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd>lists all common page and subpage codes and their names that are found in the command set that matches the peripheral type of the given <i>DEVICE</i>. If no <i>DEVICE</i> and no <i>&#8211;page=PG</i> is given then the common page and subpage codes and their names are listed for SBC (e.g. a disk). If no <i>DEVICE</i> is given and a <i>&#8211;page=PG</i> is given then the common page and subpage codes and their names are listed for the command set whose peripheral device type matches the value given to <i>PG</i>. For example &#8216;sg_mode &#8211;list &#8211;page=1&#8217; lists the command mode pages and subpages for tape devices. Additionally if a sub_page_code is given then it is interpreted as a transport identifier and command transport specific mode page codes and their names are listed following the main mode page list. Other options are ignored.</p>
<dt><code>-L</code>, <code>&#8211;llbaa</code></p>
<dd>set the Long LBA Accepted (LLBAA) bit in the MODE SENSE (10) cdb. This bit is not defined in the MODE SENSE (6) cdb so setting the &#8216;-L&#8217; and &#8216;&#8211;six&#8217; options is reported as an error. When set the <i>DEVICE</i> may respond with 16 byte block descriptors as indicated by the &#8216;LongLBA&#8217; field in the response. In most cases setting this option is not needed.</p>
<dt><code>-m</code>, <code>&#8211;maxlen</code>=<i>LEN</i></p>
<dd>The <i>LEN</i> argument is the maximum response length in bytes. It is the &#8216;allocation length&#8217; field in the cdb. When not given (or <i>LEN</i> is zero) then the allocation length field is set to 4096 for MODE SENSE (10) or 252 for MODE SENSE (6). The <i>LEN</i> argument must be non-negative and no greater than 65535 for MODE SENSE (10) and not greater than 255 for MODE SENSE (6).</p>
<dt><code>-O</code>, <code>&#8211;old</code></p>
<dd>switch to older style options.</p>
<dt><code>-p</code>, <code>&#8211;page</code>=<i>PG</i></p>
<dd>page code to fetch. The <i>PG</i> is assumed to be a decimal value unless prefixed by &#8216;0x&#8217; or has a trailing &#8216;h&#8217;. It should be a value between 0 and 63 (inclusive). When not given and a default is required then a value of 63 (0x3f), which fetches all mode pages, is used.</p>
<dt><code>-p</code>, <code>&#8211;page</code>=<i>PG,SPG</i></p>
<dd>page code and subpage code values to fetch. Both arguments are assumed to be decimal unless flagged as hexadecimal. The page code should be between 0 and 63 inclusive. The subpage code should be between 0 and 255 inclusive. The default value for the subpage code is 0.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>output the response in binary to stdout. Error messages and warnings, if any, are sent to stderr. When this option is used twice (e.g. &#8216;-rr&#8217;) then has the same action as &#8216;-R&#8217;</p>
<dt><code>-R</code></p>
<dd>output the selected mode page to stdout a byte per line. Each line contains two hexadecimal digits (e.g. &quot;3e&quot;). Useful as input (after editing) to the <a href="/docs/linux/man/8-sg_wr_mode/">sg_wr_mode</a>(8) utility.</p>
<dt><code>-6</code>, <code>&#8211;six</code></p>
<dd>by default this utility sends a 10 byte MODE SENSE command to the <i>DEVICE</i>. However some SCSI devices only support 6 byte MODE SENSE commands (e.g. SCSI-2 tape drives). This parameter forces the use of 6 byte MODE SENSE commands.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase level of verbosity. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print out version string then exit.</dl>
<h2>Notes</h2>
<p>If the normal sg_modes utility fails with &quot;illegal command operation code&quot; then try the &#8216;&#8211;six&#8217; (or &#8216;-6&#8217;) option. </p>
<p> This utility performs a SCSI INQUIRY command to determine the peripheral type of the device (e.g. 0 -&gt; Direct Access Device (disk)) prior to sending a MODE SENSE command. This helps in decoding the block descriptor and mode pages. </p>
<p> In the 2.4 series of Linux kernels the <i>DEVICE</i> must be a SCSI generic (sg) device. In the 2.6 series block devices (e.g. SCSI disks and DVD drives) can also be specified. For example &quot;sg_modes -a /dev/sda&quot; will work in the 2.6 series kernels.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_modes is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Older Command Line Options</h2>
<p>The options in this section were the only ones available prior to sg3_utils version 1.23 . In sg3_utils version 1.23 and later these older options can be selected by either setting the SG3_UTILS_OLD_OPTS environment variable or using &#8216;&#8211;old&#8217; (or &#8216;-O) as the first option.</p>
<dl>
<dt><code>-6</code></p>
<dd>by default this utility sends a 10 byte MODE SENSE command to the <i>DEVICE</i>. This parameter forces the use of 6 byte MODE SENSE commands. See <i>&#8211;six</i> in the main description.</p>
<dt><code>-a</code></p>
<dd>see <i>&#8211;all</i> in the main description.</p>
<dt><code>-A</code></p>
<dd>output all the mode pages and subpages supported by the <i>DEVICE</i>. Same as &#8216;&#8211;all &#8211;all&#8217; in the new syntax.</p>
<dt><code>-c</code>=<i>PC</i></p>
<dd><i>PC</i> is the page control value. See <code>&#8211;control</code>=<i>PC</i> in the main description.</p>
<dt><code>-d</code></p>
<dd>see <code>&#8211;dbd</code> in the main description.</p>
<dt><code>-D</code></p>
<dd>see <code>&#8211;dbout</code> in the main description.</p>
<dt><code>-e</code></p>
<dd>see <code>&#8211;examine</code> in the main description.</p>
<dt><code>-f</code></p>
<dd>see <code>&#8211;flexible</code> in the main description.</p>
<dt><code>-h</code></p>
<dd>The default action is to decode known mode page numbers (and subpage numbers) into text. With this option mode page numbers (and subpage numbers) are output in hexadecimal.</p>
<dt><code>-H</code></p>
<dd>same action as the &#8216;-h&#8217; option.</p>
<dt><code>-l</code></p>
<dd>see <code>&#8211;list</code> in the main description.</p>
<dt><code>-L</code></p>
<dd>see <code>&#8211;llbaa</code> in the main description.</p>
<dt><code>-N</code></p>
<dd>switch to the newer style options.</p>
<dt><code>-m</code>=<i>LEN</i></p>
<dd>see <code>&#8211;maxlen</code>=<i>LEN</i> in the main description.</p>
<dt><code>-p</code>=<i>PG</i></p>
<dd><i>PG</i> is page code to fetch. Should be a hexadecimal number between 0 and 3f inclusive (0 to 63 decimal). The default value when required is 3f (fetch all mode pages).</p>
<dt><code>-p</code>=<i>PG,SPG</i></p>
<dd>page code and subpage code values to fetch. The page code should be a hexadecimal number between 0 and 3f inclusive. The subpage code should be a hexadecimal number between 0 and ff inclusive. The default value for the subpage code is 0.</p>
<dt><code>-r</code></p>
<dd>output the selected mode page to stdout a byte per line. Each line contains two hexadecimal digits (e.g. &quot;3e&quot;). Useful as input (after editing) to the <a href="/docs/linux/man/8-sg_wr_mode/">sg_wr_mode</a>(8) utility.</p>
<dt><code>-subp</code>=<i>SPG</i></p>
<dd>sub page code to fetch. Should be a hexadecimal number between 0 and 0xff inclusive. The default value is 0.</p>
<dt><code>-v</code></p>
<dd>increase verbosity of output.</p>
<dt><code>-V</code></p>
<dd>print out version string then exit.</p>
<dt><code>-?</code></p>
<dd>output usage message then exit. Ignore all other parameters.</dl>
<h2>Author</h2>
<p>Written by Douglas Gilbert</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2000-2012 Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sdparm/">sdparm</a>(8), <a href="/docs/linux/man/8-sg_wr_mode/">sg_wr_mode</a>(8), <a href="/docs/linux/man/8-sginfo/">sginfo</a>(8),</code> <code>sgmode(scsirastools), scsiinfo(net), scu(net),</code> <code>seatools(seagate)</code> All these utilities offer some facility to change mode page (or block descriptor) parameters. </p>
