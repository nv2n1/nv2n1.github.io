---
title: "smp_phy_test(8)"
name: "smp_phy_test"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_phy_test/"
description: "smp_phy_test – invoke PHY TEST FUNTION SMP function"
---

<p>smp_phy_test &#8211; invoke PHY TEST FUNTION SMP function</p>
<h2>Synopsis</h2>
<p><code>smp_phy_test</code> [<i>&#8211;control=CO</i>] [<i>&#8211;dwords=DW</i>] [<i>&#8211;expected=EX</i>] [<i>&#8211;function=FN</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;linkrate=LR</i>] [<i>&#8211;pattern=PA</i>] [<i>&#8211;phy=ID</i>] [<i>&#8211;raw</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;sata</i>] [<i>&#8211;spread=SC</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends a SAS Serial Management Protocol (SMP) PHY TEST FUNCTION function request to an SMP target. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present. </p>
<p> The PHY TEST FUNCTION function can be used to start and stop test pattern transmission. When a phy associated with an SMP target (most likely an expander) starts test pattern transmission then the attached phy (if there is one) sees a link down. </p>
<p> SAS phys associated with SSP targets (e.g. a SAS disk) can generate similar test patterns by using the SEND DIAGNOSTIC SCSI command with page code 3fh . See the sg_senddiag utility.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;control</code>=<i>CO</i></p>
<dd>set the &#8216;phy test pattern dwords control&#8217; field. The argument <i>CO</i> can be from 0 to 255 inclusive, the default is 0 (each byte in &#8216;dwords&#8217; sent as data byte (Dxx.y) without scrambling). Only active when &#8216;pattern&#8217; is set to 40h (i.e. &quot;two_dwords&quot;).</p>
<dt><code>-d</code>, <code>&#8211;dwords</code>=<i>DW</i></p>
<dd>set the &#8216;phy test pattern dwords&#8217; field which is 8 bytes long. The argument <i>DW</i> would normally be entered in hex with a leading &#8216;0x&#8217; or a trailing &#8216;h&#8217; (otherwise it would be interpreted as decimal). Due to a quirk in the command line parser, the argument value ffffffffffffffffh (i.e. all bits sets) needs to be entered as &#8216;-1&#8217;.</p>
<dt><code>-E</code>, <code>&#8211;expected</code>=<i>EX</i></p>
<dd>set the &#8216;expected expander change count&#8217; field in the SMP request. The value <i>EX</i> is from 0 to 65535 inclusive with 0 being the default value. When <i>EX</i> is greater than zero then if the value doesn&#8217;t match the expander change count of the SMP target (i.e. the expander) when the request arrives then the target ignores the request and sets a function result of &quot;invalid expander change count&quot; in the response.</p>
<dt><code>-f</code>, <code>&#8211;function</code>=<i>FN</i></p>
<dd>set the &#8216;phy test function&#8217; field in the SMP request. Values between 0 and 255 are accepted with the default being 0. The value 0 stops the selected phy performing a phy test function. The value 1 starts the selected phy transmitting the test pattern (and anything that the phy receives is discarded).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-l</code>, <code>&#8211;linkrate</code>=<i>LR</i></p>
<dd>transmits the test pattern at the specified physical link rate: 8 -&gt; 1.5 Gbps, 9 -&gt; 3 Gbps, 10 -&gt; 6 Gbps, 11 -&gt; 12 Gbps. Default value is 9.</p>
<dt><code>-P</code>, <code>&#8211;pattern</code>=<i>PA</i></p>
<dd>specifies the type of test pattern to transmit. SAS-2 (rev15) values are: 1 -&gt; JTPAT, 2 -&gt; CJTPAT, 10h -&gt; TRAIN, 11h -&gt; TRAIN_DONE, 12h -&gt; IDLE, 13h -&gt; SCRAMBLED_0, 40h -&gt; &quot;two_dwords&quot;. Default value is 2.</p>
<dt><code>-p</code>, <code>&#8211;phy</code>=<i>ID</i></p>
<dd>phy identifier. <i>ID</i> is a value between 0 and 254. Default is 0.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. Typically this is an expander. This option may not be needed if the <i>SMP_DEVICE</i> has the target&#8217;s SAS address within it. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-t</code>, <code>&#8211;sata</code></p>
<dd>set phy test function SATA bit. The default action is to leave that bit clear (zero).</p>
<dt><code>-S</code>, <code>&#8211;spread</code>=<i>SC</i></p>
<dd>set the phy test function Spread Spectrum Clocking (SSC) field to <i>SC</i>. Default value is zero (no spreading). Other defined values are 1 for centre spreading and 2 for down spreading.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Conforming To</h2>
<p>The SMP PHY TEST function was introduced in SAS-1.1 and enhanced in SAS-2 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, sg_senddiag(sg3_utils)</code> </p>
