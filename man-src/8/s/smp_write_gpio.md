---
title: "smp_write_gpio(8)"
name: "smp_write_gpio"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_write_gpio/"
description: "smp_write_gpio – invoke WRITE GPIO REGISTER (ENHANCED) SMP function"
---

<p>smp_write_gpio &#8211; invoke WRITE GPIO REGISTER (ENHANCED) SMP function</p>
<h2>Synopsis</h2>
<p><code>smp_write_gpio</code> [<i>&#8211;count=CO</i>] [<i>&#8211;data=H,H&#8230;</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;index=IN</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;raw</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;type=TY</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends a SAS Serial Management Protocol (SMP) WRITE GPIO REGISTER or a WRITE GPIO REGISTER ENHANCED function request to an SMP target. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present. </p>
<p> This function is defined in SFF-8485 ( see <a rel="nofollow" href="http://www.sffcommittee.com">www.sffcommittee.com</a> ) together with its corresponding READ GPIO REGISTER (ENHANCED) SMP function. The other SMP functions are defined in SAS documents at <a rel="nofollow" href="http://www.t10.org">www.t10.org</a> . SFF-8485 defines a curious device called a &quot;virtual SMP port&quot; that lives in a host bus adapter (HBA) and allows SMP to manipulate the sideband signals in wide internal cables. To stop other initiators in a multi-initiator domain from accessing those sideband signals, the virtual SMP (target) port is not indicated in a DISCOVER response. </p>
<p> For notes on the SMP WRITE GPIO REGISTER ENHANCED function see the section on the ENHANCED FUNCTION below.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;count</code>=<i>CO</i></p>
<dd>where <i>CO</i> is the register count. This is the number of (4 byte) registers to send. The default value is 1.</p>
<dt><code>-d</code>, <code>&#8211;data</code>=<i>H,H&#8230;</i></p>
<dd>this option supplies a comma separated list of hexadecimal bytes (0 to ff inclusive) that will be used as write data in the WRITE GPIO REGISTER request. The number of bytes supplied should be four times <i>&#8211;count=C</i> The first 4 bytes will become the first register written.</p>
<dt><code>-d</code>, <code>&#8211;data</code>=<code>&#8211;</code></p>
<dd>reads string of hexadecimal bytes from stdin. Spaces, tabs and line feeds additionally are permitted as separators.</p>
<dt><code>-E</code>, <code>&#8211;enhanced</code></p>
<dd>sends a WRITE GPIO REGISTER ENHANCED function request (default: send a WRITE GPIO REGISTER function request).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-i</code>, <code>&#8211;index</code>=<i>IN</i></p>
<dd>where <i>IN</i> is the register index. This value is origin zero and its default value is 0. The request will send <i>&#8211;count=CO</i> registers starting from <i>&#8211;index=IN</i> of the given <i>&#8211;type=TY</i>.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. Typically this is an expander. This option may not be needed if the <i>SMP_DEVICE</i> has the target&#8217;s SAS address within it. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-t</code>, <code>&#8211;type</code>=<i>TY</i></p>
<dd>where <i>TY</i> is the register type. The default value is 0 (GPIO_CFG). The request will send <i>&#8211;count=CO</i> registers starting from <i>&#8211;index=IN</i> of the given <i>&#8211;type=TY</i>.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Enhanced Function</h2>
<p>In the technical review of SAS-2 prior to standardization in this t10 document: 08-212r8.pdf (page 871 or 552) there is a comment that the READ GPIO REGISTER and WRITE GPIO REGISTER function headers (i.e. first 4 bytes) do not comply with all the other SMP functions in SAS-2. </p>
<p> There is a suggestion that enhanced variants be introduced in the next version of the SFF-8485 document. If that ever happened then it has not been made public. In SAS-2.1 both the READ and WRITE GPIO REGISTER functions have been made obsolete and the corresponding ENHANCED function numbers are &quot;restricted&quot; for SFF-8485. </p>
<p> If the <i>&#8211;enhanced</i> option is given then the ENHANCED function number is sent; the register type, index and count fields (1 byte each) are increased by two byte positions leaving enough space for a compliant SAS-2 SMP header to be built.</p>
<h2>Conforming To</h2>
<p>The SMP WRITE GPIO REGISTER function is defined in SFF-8485 (see <a rel="nofollow" href="http://www.sffcommittee.com">www.sffcommittee.com</a> ) together with its corresponding READ GPIO REGISTER SMP function.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_read_gpio(smp_utils)</code> </p>
