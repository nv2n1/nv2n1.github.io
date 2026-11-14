---
title: "sg_logs(8)"
name: "sg_logs"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_logs/"
description: "sg_logs – access log pages with SCSI LOG SENSE command"
---

<p>sg_logs &#8211; access log pages with SCSI LOG SENSE command</p>
<h2>Synopsis</h2>
<p><code>sg_logs</code> [<i>&#8211;all</i>] [<i>&#8211;brief</i>] [<i>&#8211;control=PC</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;list</i>] [<i>&#8211;maxlen=LEN</i>] [<i>&#8211;name</i>] [<i>&#8211;page=PG[,SPG]</i>] [<i>&#8211;paramp=PP</i>] [<i>&#8211;pcb</i>] [<i>&#8211;ppc</i>] [<i>&#8211;raw</i>] [<i>&#8211;reset</i>] [<i>&#8211;select</i>] [<i>&#8211;sp</i>] [<i>&#8211;temperature</i>] [<i>&#8211;transport</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i> </p>
<p> <code>sg_logs</code> [<i>-a</i>] [<i>-A</i>] [<i>-b</i>] [<i>-c=PC</i>] [<i>-h</i>] [<i>-H</i>] [<i>-l</i>] [<i>-L</i>] [<i>-m=LEN</i>] [<i>-n</i>] [<i>-p=PG[,SPG]</i>] [<i>-paramp=PP</i>] [<i>-pcb</i>] [<i>-ppc</i>] [<i>-r</i>] [<i>-select</i>] [<i>-sp</i>] [<i>-t</i>] [<i>-T</i>] [<i>-v</i>] [<i>-V</i>] [<i>-?</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>This utility sends a SCSI LOG SENSE command to the <i>DEVICE</i> and then outputs the response. The LOG SENSE command is used to fetch log pages. Known log pages are decoded by default. When the <i>&#8211;reset</i> and/or <i>&#8211;select</i> option is given then a SCSI LOG SELECT command is issued to reset parameters (e.g. counters). </p>
<p> In SPC-4 revision 5 a subpage code was introduced to both the LOG SENSE and LOG SELECT command. At the same time a page code field was introduced to the to the LOG SELECT command. The log subpage code can range from 0 to 255 (0xff) inclusive. The subpage code value 255 can be thought of as a wildcard. </p>
<p> This utility supports two command line syntaxes, the preferred one is shown first in the synopsis and explained in this section. A later section on the old command line syntax outlines the second group of options.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd>outputs all the log pages supported by the device. This requires a two stage process: first the &quot;supported log pages&quot; log page is fetched, then for each entry in the response, the corresponding log page is fetched and displayed. When used twice (e.g. &#8216;-aa&#8217;) all log pages and subpages are fetched.</p>
<dt><code>-b</code>, <code>&#8211;brief</code></p>
<dd>shorten the amount of output for some log pages. For example the Tape Alert log page only outputs parameters whose flags are set when <i>&#8211;brief</i> is given.</p>
<dt><code>-c</code>, <code>&#8211;control</code>=<i>PC</i></p>
<dd>accepts 0, 1, 2 or 3 for the <i>PC</i> argument: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>0</code>&nbsp;<wbr>: current threshold values </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>1</code>&nbsp;<wbr>: current cumulative values </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>2</code>&nbsp;<wbr>: default threshold values </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>3</code>&nbsp;<wbr>: default cumulative values<br />
 The default value is 1 (i.e. current cumulative values).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print out the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>The default action is to decode known mode page numbers (and subpage numbers) into text. When this option is used once, the response is output in hexadecimal.</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd>lists the names of all logs sense pages supported by this device. This is done by reading the &quot;supported log pages&quot; log page. When used twice (e.g. &#8216;-ll&#8217;) lists the names of all logs sense pages and subpages supported by this device. There is a list of common log page codes below.</p>
<dt><code>-m</code>, <code>&#8211;maxlen</code>=<i>LEN</i></p>
<dd>sets the &quot;allocation length&quot; field in the LOG SENSE cdb. The is the maximum length in bytes that the response will be. Without this option (or <i>LEN</i> equal to 0) this utility first fetches the 4 byte response then does a second access with the length indicated in the first (4 byte) response. Negative values and 1 for <i>LEN</i> are not accepted. <i>LEN</i> cannot exceed 65535 (0xffff). Responses can be quite large (e.g. the background scan results log page) and this option can be used to limit the amount of information returned.</p>
<dt><code>-n</code>, <code>&#8211;name</code></p>
<dd>decode some log pages into &#8216;name=value&#8217; entries, one per line. The name contains no space and may be abbreviated and the value is decimal unless prefixed by &#8216;0x&#8217;. Nesting is indicated by leading spaces. This form is meant to be relatively easy to parse.</p>
<dt><code>-O</code>, <code>&#8211;old</code></p>
<dd>switch to older style options.</p>
<dt><code>-p</code>, <code>&#8211;page</code>=<i>PG[,SPG]</i></p>
<dd>log page code to access. <i>PG</i> is expected to be a decimal number between 0 and 63 inclusive. A hexadecimal number can be specified by a leading &quot;0x&quot; or a trailing &quot;h&quot;. Common log page codes are listed below. Optionally <i>SPG</i>, a subpage code, can be given. <i>SPG</i> is expected to be a decimal number between 0 and 255 inclusive.</p>
<dt><code>-P</code>, <code>&#8211;paramp</code>=<i>PP</i></p>
<dd><i>PP</i> is the parameter pointer value to place in a field of that name in the LOG SENSE cdb. A decimal number in the range 0 to 65535 (0xffff) is expected. When a value greater than 0 is given the <i>&#8211;ppc</i> option should be selected. The default value is 0.</p>
<dt><code>-q</code>, <code>&#8211;pcb</code></p>
<dd>show Parameter Control Byte settings (only relevant when log parameters being output in ASCII).</p>
<dt><code>-Q</code>, <code>&#8211;ppc</code></p>
<dd>sets the Parameter Pointer Control (PPC) bit in the LOG SENSE cdb. Default is 0 (i.e. cleared).</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>output the response in binary to stdout. Error messages and warnings are output to stderr.</p>
<dt><code>-R</code>, <code>&#8211;reset</code></p>
<dd>use SCSI LOG SELECT command (PCR bit set) to reset the all log pages (or the given page). [SPC-4 (rev 6) doesn&#8217;t say that a given log (sub)page can be reset yet.] Exactly what is reset depends on the accompanying SP bit (i.e. <i>&#8211;sp</i> option which defaults to 0) and the <i>PC</i> (&quot;page control&quot;) value (which defaults to 1). Supplying this option implies the <i>&#8211;select</i> option as well. This option seems to clear error counter log pages but leaves pages like self-test results, start-stop cycle counter and temperature log pages unaffected. This option may be required to clear log pages if a counter reaches its maximum value since the log page in which the counter is found will remain &quot;stuck&quot; until something is done.</p>
<dt><code>-S</code>, <code>&#8211;select</code></p>
<dd>use a LOG SELECT command. The default action (i.e. when neither this option nor <i>&#8211;reset</i> is given) is to do a LOG SENSE command. When this option is given, the SP bit (i.e. <i>&#8211;sp</i> option which defaults to 0), the <i>PC</i> (&quot;page control&quot;) value (which defaults to 1) and the PCR bit (i.e. <i>&#8211;reset</i> option which defaults to 0) are placed in the LOG SELECT cdb. At some stage the log page and subpage options may also be active [but SPC-4 (rev 6) doesn&#8217;t say that].</p>
<dt><code>-s</code>, <code>&#8211;sp</code></p>
<dd>sets the Saving Parameters (SP) bit. Default is 0 (i.e. cleared). When set this instructs the device to store the current log page parameters (as indicated by the DS and TSD parameter codes) in some non-volatile location. Hence the log parameters will be preserved across power cycles. This option is typically not needed, especially if the GLTSD flag is clear in the control mode page as this instructs the device to periodically save all saveable log parameters to non-volatile locations.</p>
<dt><code>-t</code>, <code>&#8211;temperature</code></p>
<dd>outputs the temperature. First looks in the temperature log page and if that is not available tries the Informational Exceptions log page which may also have the current temperature (especially on older disks).</p>
<dt><code>-T</code>, <code>&#8211;transport</code></p>
<dd>outputs the transport (&#8216;Protocol specific port&#8217;) log page. Equivalent to setting &#8216;&#8211;page=18h&#8217;.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase level of verbosity.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print out version string then exit.</dl>
<h2>Notes</h2>
<p>This utility will usually do a double fetch of log pages with the SCSI LOG SENSE command. The first fetch requests a 4 byte response (i.e. place 4 in the &quot;allocation length&quot; field in the cdb). From that response it can calculate the actual length of the response which is what it asks for on the second fetch. This is typical practice in SCSI and guaranteed to work in the standards. However some older devices don&#8217;t comply. For those devices using the <i>&#8211;maxlen=LEN</i> option will do a single fetch. A value of 252 should be a safe starting point. </p>
<p> Various log pages hold information error rates, device temperature, start stop cycles since device produced and the results of the last 20 self tests. Self tests can be initiated by the <a href="/docs/linux/man/8-sg_senddiag/">sg_senddiag</a>(8) utility. The smartmontools package provides much of the information found with sg_logs in a form suitable for monitoring the health of SCSI disks and tape drives. </p>
<p> Here is a list of log pages that are decoded by this utility. [The code values can be given to &#8216;&#8211;page=&#8217; as is, with a trailing &quot;h&quot; instead of the leading &quot;0x&quot;, or as their decimal equivalents.]: </p>
<p> 0x0 Supported log pages<br />
 0x0,0xff Supported log pages and subpages<br />
 0x1 Buffer overrun/underrun<br />
 0x2 Write error counter<br />
 0x3 Read error counter<br />
 0x4 Read reverse error counter<br />
 0x5 Verify error counter<br />
 0x6 Non-medium error<br />
 0x7 Last n error events<br />
 0x8 Format status (sbc-2)<br />
 0xb Last n deferred errors or asynchronous events<br />
 0xc Logical block provisioning (sbc-3) or Sequential access device (ssc-2)<br />
 0xd Temperature<br />
 0xe Start-stop cycle counter<br />
 0x10 Self-test results<br />
 0x11 Solid state media<br />
 0x15 Background scan results (sbc-3)<br />
 0x16 ATA pass-through results (sat-3)<br />
 0x17 Non-volatile cache (sbc-3)<br />
 0x18 Protocol specific port (SAS transport)<br />
 0x19 General statistics and performance<br />
 0x1a Power condition transitions<br />
 0x2f Informational exceptions<br />
 0x37 Seagate cache (vendor, disk)<br />
 0x3e Seagate factory (vendor, disk) </p>
<p> In the 2.4 series of Linux kernels the <i>DEVICE</i> must be a SCSI generic (sg) device. In the 2.6 series block devices (e.g. SCSI disks and DVD drives) can also be specified. For example &quot;sg_logs -a /dev/sda&quot; will work in the 2.6 series kernels.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_logs is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Older Command Line Options</h2>
<p>The options in this section were the only ones available prior to sg3_utils version 1.23 . In sg3_utils version 1.23 and later these older options can be selected by either setting the SG3_UTILS_OLD_OPTS environment variable or using &#8216;&#8211;old&#8217; (or &#8216;-O) as the first option. </p>
<p> Options with arguments or with two or more letters can have an extra &#8216;-&#8216; prepended. For example: both &#8216;-pcb&#8217; and &#8216;&#8211;pcb&#8217; are acceptable.</p>
<dl>
<dt><code>-a</code></p>
<dd>outputs all the log pages supported by the device. Equivalent to <i>&#8211;all</i> in the main description.</p>
<dt><code>-A</code></p>
<dd>outputs all the log pages and subpages supported by the device. Equivalent to &#8216;&#8211;all &#8211;all&#8217; in the main description.</p>
<dt><code>-c</code>=<i>PC</i></p>
<dd>Equivalent to <i>&#8211;control=PC</i> in the main description.</p>
<dt><code>-h</code></p>
<dd>suppresses decoding of known log sense pages and prints out the response in hex instead.</p>
<dt><code>-H</code></p>
<dd>same action as &#8216;-h&#8217; in this section and equivalent to <i>&#8211;hex</i> in the main description.</p>
<dt><code>-l</code></p>
<dd>lists the names of all logs sense pages supported by this device. Equivalent to <i>&#8211;list</i> in the main description.</p>
<dt><code>-L</code></p>
<dd>lists the names of all logs sense pages and subpages supported by this device. Equivalent to &#8216;&#8211;list &#8211;list&#8217; in the main description.</p>
<dt><code>-m</code>=<i>LEN</i></p>
<dd>request only <i>LEN</i> bytes of response data. Default is 0 which is interpreted as all that is available. <i>LEN</i> is decimal unless it has a leading &#8216;0x&#8217; or trailing &#8216;h&#8217;. Equivalent to <i>&#8211;maxlen=LEN</i> in the main description.</p>
<dt><code>-n</code></p>
<dd>Equivalent to <i>&#8211;name</i> in the main description.</p>
<dt><code>-N</code></p>
<dd>switch to the newer style options.</p>
<dt><code>-p</code>=<i>PG[,SPG]</i></p>
<dd><i>PG</i> is the log page code to access. Should be a hexadecimal number between 0 and 3f inclusive. If given <i>SPG</i> is the log subpage code. <i>SPG</i> should be a hexadecimal number between 0 and ff inclusive. The subpage code of &#8216;ff&#8217; can be thought of as a wildcard.</p>
<dt><code>-paramp</code>=<i>PP</i></p>
<dd><i>PP</i> is the parameter pointer value (in hex) to place in command. Should be a number between 0 and ffff inclusive.</p>
<dt><code>-pcb</code></p>
<dd>show Parameter Control Byte settings (only relevant when log parameters being output in ASCII).</p>
<dt><code>-ppc</code></p>
<dd>sets the Parameter Pointer Control (PPC) bit. Default is 0 (i.e. cleared).</p>
<dt><code>-r</code></p>
<dd>use SCSI LOG SELECT command (PCR bit set) to reset the all log pages (or the given page). Equivalent to <i>&#8211;reset</i> in the main description.</p>
<dt><code>-select</code></p>
<dd>use a LOG SELECT command. Equivalent to <i>&#8211;select</i> in the main description.</p>
<dt><code>-sp</code></p>
<dd>sets the Saving Parameters (SP) bit. Default is 0 (i.e. cleared). Equivalent to <i>&#8211;sp</i> in the main description.</p>
<dt><code>-t</code></p>
<dd>outputs the temperature. Equivalent to <i>&#8211;temperature in the main description.</p>
<dt></i><code>-T</code></p>
<dd>outputs the transport (&#8216;Protocol specific port&#8217;) log page. Equivalent to <i>&#8211;transport</i> in the main description.</p>
<dt><code>-v</code></p>
<dd>increase level of verbosity.</p>
<dt><code>-V</code></p>
<dd>print out version string then exit.</p>
<dt><code>-?</code></p>
<dd>output usage message then exit.</dl>
<h2>Author</h2>
<p>Written by Douglas Gilbert</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2002-2013 Douglas Gilbert<br />
 This software is distributed under the GPL version 2. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smartctl(smartmontools), <a href="/docs/linux/man/8-sg_senddiag/">sg_senddiag</a>(8)</code> </p>
