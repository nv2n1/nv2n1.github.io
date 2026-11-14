---
title: "smp_rep_zone_perm_tbl(8)"
name: "smp_rep_zone_perm_tbl"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_rep_zone_perm_tbl/"
description: "smp_rep_zone_perm_tbl – invoke REPORT ZONE PERMISSION TABLE function"
---

<p>smp_rep_zone_perm_tbl &#8211; invoke REPORT ZONE PERMISSION TABLE function</p>
<h2>Synopsis</h2>
<p><code>smp_rep_zone_perm_tbl</code> [<i>&#8211;append</i>] [<i>&#8211;bits=COL</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;multiple</i>] [<i>&#8211;nocomma</i>] [<i>&#8211;num=MD</i>] [<i>&#8211;permf=FN</i>] [<i>&#8211;raw</i>] [<i>&#8211;report=RT</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;start=SS</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends one or more SAS Serial Management Protocol (SMP) REPORT ZONE PERMISSION TABLE function requests to an SMP target. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>&#8211;sa=SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present. </p>
<p> This SMP function returns zone permission descriptors which represent rows of the zone permission table. There is a row for each source zone group starting at zone group 0 and finishing at zone group 127 or zone group 255. Due to the SMP response size restriction of 1028 bytes (including trailing CRC), not all the zone permission table rows can be returned in one REPORT ZONE PERMISSION TABLE function response. So multiple function calls may be required with the <i>&#8211;start=SS</i> option being used on the latter calls to specify the next starting source zone group. </p>
<p> The <i>&#8211;multiple</i> option will send multiple REPORT ZONE PERMISSION TABLE requests until all source zone groups (or starting from <i>&#8211;start=SS</i>) are output. This option is the most convenient way to output the whole zone permission table. In the absence of the <i>&#8211;multiple</i> option only one REPORT ZONE PERMISSION TABLE request is sent. </p>
<p> The output of this utility is designed to be useful as input to the smp_conf_zone_perm_tbl utility. In other words these utilities can be used to save and restore zone permission table settings.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;append</code></p>
<dd>used in conjunction with <i>&#8211;permf=FN</i> to append to <i>FN</i> if it already exists. If <i>FN</i> does not exist then it is created.</p>
<dt><code>-B</code>, <code>&#8211;bits</code>=<i>COL</i></p>
<dd>This is an alternate zone permission table represention showing single bits with the origin (i.e. ZP[0,0]) in the top left. The output is a bit array with <i>COL</i> columns and up to <i>COL</i> rows. This output resembles the example zone permission tables shown in the SAS draft documents (at t10.org). The default (i.e. without this option) is output that reflects the byte oriented, big endian nature of SCSI (and hence SMP) commands. The output produced by this option is not suitable as input for the smp_conf_zone_perm_tbl utility.</p>
<dt><code>-f</code>, <code>&#8211;start</code>=<i>SS</i></p>
<dd>starting (first and lowest numbered) source zone group (default: zone group 0).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-m</code>, <code>&#8211;multiple</code></p>
<dd>starting at source zone group 0 (or <i>SS</i>), multiple REPORT ZONE PERMISSION TABLE requests are issued until the last (127th and 255th) source zone descriptor is output. This option should not be given together with the <i>&#8211;num=MD</i> option.</p>
<dt><code>-N</code>, <code>&#8211;nocomma</code></p>
<dd>output each zone group descriptor as a long string of hexadecimal digits, two digits per byte. Default action is to output a comma separated list of hexadecimal ASCII bytes for each zone group descriptor.</p>
<dt><code>-n</code>, <code>&#8211;num</code>=<i>MD</i></p>
<dd>where <i>MD</i> is the maximum number of descriptors that can be reported in the one response. The default value is 63. 63 is the maximum number of &quot;128 zone groups&quot; sized descriptors that can fit in one response. If the expander is using &quot;256 zone groups&quot; sized descriptors then a maximum of 31 descriptors can fit in one response. This option should not be given together with the <i>&#8211;multiple</i> option.</p>
<dt><code>-P</code>, <code>&#8211;permf</code>=<i>FN</i></p>
<dd><i>FN</i> is a file to write the zone permission descriptors to. The default action is to output the zone permissions descriptors to stdout. Note that the whole permissions table may not fit in one response. If the <i>FN</i> exists then it is truncated prior to the write unless <i>&#8211;append</i> is given. To append to the existing <i>FN</i> add the <i>&#8211;append</i> option.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-R</code>, <code>&#8211;report</code>=<i>RT</i></p>
<dd>set the &#8216;report type&#8217; field in the SMP request. <i>RT</i> may take these values: 0 for report current values (default); 1 for report the shadow values; 2 for report saved values; 3 for report default values.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. The mpt interface needs this option and it will typically be an expander&#8217;s SAS address. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-f</code>, <code>&#8211;start</code>=<i>SS</i></p>
<dd>See entry above, listed in order by its short option letter (i.e. <i>-f</i>).</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>When the <i>&#8211;permf=FN</i> is given and <i>SS</i> is greater than zero then a line of the form &quot;&#8211;start=<i>SS</i>&quot; is written to <i>FN</i> just prior to the first row of zone permissions. </p>
<p> There are some examples of the <i>&#8211;permf=FN</i> format in the examples directory.</p>
<h2>Conforming To</h2>
<p>The SMP REPORT ZONE PERMISSION TABLE function was introduced in SAS-2 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2011 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_conf_zone_perm_tbl, smp_zone_lock(smp_utils)</code> </p>
