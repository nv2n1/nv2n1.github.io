---
title: "smp_conf_zone_perm_tbl(8)"
name: "smp_conf_zone_perm_tbl"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_conf_zone_perm_tbl/"
description: "smp_conf_zone_perm_tbl – invoke CONFIGURE ZONE PERMISSION TABLE function"
---

<p>smp_conf_zone_perm_tbl &#8211; invoke CONFIGURE ZONE PERMISSION TABLE function</p>
<h2>Synopsis</h2>
<p><code>smp_conf_zone_perm_tbl</code> [<i>&#8211;deduce</i>] [<i>&#8211;expected=EX</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;numzg=NG</i>] <i>&#8211;permf=FN</i> [<i>&#8211;raw</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;save=SAV</i>] [<i>&#8211;start=SS</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends one or more SAS Serial Management Protocol (SMP) CONFIGURE ZONE PERMISSION TABLE function requests to an SMP target. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>&#8211;sa=SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify an HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present. </p>
<p> The zone permission table has a row for each source zone group and a column for each destination zone group. Each element in the table (ZP[s,d]) is a single bit indicating whether the source zone group can access the destination zone group (the bit is set: 1) or not (the bit is clear: 0). There are two different table sizes: 128 and 256 zone groups. Descriptors provided to this function request are either 16 bytes (128 bits) or 32 bytes (256 bits) long. Each descriptor is basically a row in the zone permission table. </p>
<p> Apart from being row in the zone permission table each descriptor is transposed and applied to the corresponding destination column. This &quot;maintains symmetry about the ZP[s,s] table axis&quot; in the words of the draft. Also descriptors are applied in the order that they appear in the request (i.e. ascending source zone group numbers). </p>
<p> The maximum number of descriptors that one CONFIGURE ZONE PERMISSION TABLE function request can hold is limited to 63 if there are 128 zone groups; and is limited to 31 if there are 256 zone groups. A full zone table will contain 128 (or 256) descriptors so to configure a full table requires multiple CONFIGURE ZONE PERMISSION TABLE requests. </p>
<p> The number of zone permission configuration descriptors is determined by reading the <i>FN</i> file associated with the <i>&#8211;permf=FN</i> option. If there are more descriptors than can fit in one CONFIGURE ZONE PERMISSION TABLE function request then multiple requests are sent. All descriptors found in the <i>FN</i> file will be sent unless an earlier function response indicates there has been an error.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-d</code>, <code>&#8211;deduce</code></p>
<dd>deduce number of zone groups from number of bytes on active <i>FN</i> lines. With 128 zone groups each active line will contain 16 (or less) bytes. With this option if any active line in <i>FN</i> contains more than 16 bytes then 256 zone groups are assumed, otherwise 128 zone groups are assumed. This option cannot be given with the <i>&#8211;numzg=NG</i> option (as they may contradict one another).</p>
<dt><code>-E</code>, <code>&#8211;expected</code>=<i>EX</i></p>
<dd>set the &#8216;expected expander change count&#8217; field in the SMP request. The value <i>EX</i> is from 0 to 65535 inclusive with 0 being the default value. When <i>EX</i> is greater than zero then if the value doesn&#8217;t match the expander change count of the SMP target (i.e. the expander) when the request arrives then the target ignores the request and sets a function result of &quot;invalid expander change count&quot; in the response.</p>
<dt><code>-f</code>, <code>&#8211;start</code>=<i>SS</i></p>
<dd>starting (first) source zone group (default: zone group 0). If multiple function requests are sent, this field in subsequent function requests will be adjusted to reflect those descriptors already sent. Note that the <i>SS</i> value may be picked up from <i>FN</i> and if this option and that value are not the same, an error is generated.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-n</code>, <code>&#8211;numzg</code>=<i>ZG</i></p>
<dd>number of zone groups. <i>ZG</i> can be 0 (default) or 1. 0 implies 128 zone groups while 1 implies 256 zone groups. This option cannot be used with the <i>&#8211;deduce</i> option.</p>
<dt><code>-P</code>, <code>&#8211;permf</code>=<i>FN</i></p>
<dd>FN is a file containing zone permission configuration descriptors in ASCII hexadecimal; either as bytes separated by space, tab, comma or newline, or as longer strings of hexadecimal bytes in which every 2 digits represents a byte. Empty lines and those starting with &quot;#&quot; are ignored. A line with &quot;&#8211;start=&lt;num&gt;&quot; will be taken as the starting source zone group number (i.e. &lt;num&gt; becomes <i>SS</i>) unless it contradicts the command line <i>&#8211;start=SS</i> option. Otherwise lines starting with &quot;-&quot; are ignored.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. The mpt interface needs this option and it will typically be an expander&#8217;s SAS address. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-S</code>, <code>&#8211;save</code>=<i>SAV</i></p>
<dd>set the &#8216;save&#8217; field in the SMP request. <i>SAV</i> may take these values: 0 for updating the shadow values (default), 1 for updating the saved values, 2 for updating shadow values and if available the saved values, 3 for updating both saved and shadow values.</p>
<dt><code>-f</code>, <code>&#8211;start</code>=<i>SS</i></p>
<dd>See entry above, listed in order by its short option letter (i.e. <i>-f</i>).</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>For simplicity, each active line in the <i>FN</i> file should contain 16 or 32 bytes. 16 bytes if there are 128 zone groups or 32 bytes if there are 256 zone groups. </p>
<p> SCSI is big endian. So for 128 zone groups, the first byte placed in the zone permission configuration descriptor is ZP[0,127-120]. If the <i>&#8211;start=SS</i> option is given then the first byte is ZP[<i>SS</i>,127-120]. For 256 zone groups, the first bytes are ZP[0,255-248] and ZP[<i>SS</i>,255-248] respectively. </p>
<p> There is an annex called &quot;Zone permission configuration descriptor examples&quot; in recent SAS-2 and later drafts (Annex H in spl2r03.pdf). </p>
<p> There are some examples of the <i>&#8211;permf=FN</i> format in the examples directory. Not all SAS-2 expanders properly implement descriptor transpose and only place the descriptor in the row corresponding to the source zone group.</p>
<h2>Conforming To</h2>
<p>The SMP CONFIGURE ZONE PERMISSION TABLE function was introduced in SAS-2 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_conf_zone_phy_info, smp_zone_activate(smp_utils)</code> </p>
