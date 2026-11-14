---
title: "sg_get_config(8)"
name: "sg_get_config"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sg_get_config/"
description: "sg_get_config – send SCSI GET CONFIGURATION command (MMC-4 +)"
---

<p>sg_get_config &#8211; send SCSI GET CONFIGURATION command (MMC-4 +)</p>
<h2>Synopsis</h2>
<p><code>sg_get_config</code> [<i>&#8211;brief</i>] [<i>&#8211;current</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;inner-hex</i>] [<i>&#8211;list</i>] [<i>&#8211;raw</i>] [<i>&#8211;readonly</i>] [<i>&#8211;rt=RT</i>] [<i>&#8211;starting=FC</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] <i>DEVICE</i></p>
<h2>Description</h2>
<p>Sends a SCSI GET CONFIGURATION command to <i>DEVICE</i> and decodes the response. The response includes the features and profiles of the device. Typically these devices are CD, DVD, HD-DVD and BD players that may (but not necessarily) have media in them. These devices may well be connected via ATAPI, USB or IEEE 1394 transports. In such cases they are &quot;SCSI&quot; devices only in the sense that they use the &quot;Multi-Media command&quot; set (MMC). MMC is a specialized SCSI command set whose definition can be found at <a rel="nofollow" href="http://www.t10.org">http://www.t10.org</a> . </p>
<p> This utility is based on the MMC-4 and later draft standards. See section 5 on &quot;Features and Profile for Multi_Media devices&quot; for more information on specific feature parameters and profiles. The manufacturer&#8217;s product manual may also be useful. </p>
<p> Since modern DVD and BD writers support many features and profiles, the decoded output from this utility can be large. There are various ways to cut down the output. If the <i>&#8211;brief</i> option is used only the feature names are shown and the feature parameters are not decoded. Alternatively if only one feature is of interest then this combination of options is appropriate: &quot;&#8211;rt=2 &#8211;starting=<i>FC</i>&quot;. Another possibility is to show only the features that are relevant to the media in the drive (i.e. &quot;current&quot;) with the &quot;&#8211;rt=1&quot; option.</p>
<h2>Options</h2>
<p>Arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;brief</code></p>
<dd>show the feature names but don&#8217;t decode the parameters of those features. When used with <i>&#8211;list</i> outputs known feature names but not known profile names.</p>
<dt><code>-c</code>, <code>&#8211;current</code></p>
<dd>output features marked as current. This option is equivalent to &#8216;&#8211;rt=1&#8217;.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response in hex (don&#8217;t decode response).</p>
<dt><code>-i</code>, <code>&#8211;inner-hex</code></p>
<dd>decode to the feature name level then output each feature&#8217;s data in hex.</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd>list all known feature and profile names. Ignore the device name (if given). Simply lists the feature names and profiles (followed by their hex values) that this utility knows about. If <i>&#8211;brief</i> is also given then only feature names are listed.</p>
<dt><code>-q</code>, <code>&#8211;readonly</code></p>
<dd>opens the DEVICE read-only rather than read-write which is the default. The Linux sg driver needs read-write access for the SCSI GET CONFIGURATION command but other access methods may require read-only access.</p>
<dt><code>-r</code>, <code>&#8211;rt</code>=<i>RT</i></p>
<dd>where <i>RT</i> is the field of that name in the GET CONFIGURATION cdb. Allowable values are 0, 1, 2, or 3 . The command&#8217;s action also depends on the value given to the <i>&#8211;starting=FC</i> option. The default value is 0. When <i>RT</i> is 0 then all features, regardless of currency, are returned (whose feature code is greater than or equal to <i>FC</i> given to <i>&#8211;starting=</i>). When <i>RT</i> is 1 then all current features are returned (whose feature code is greater than or equal to <i>FC</i>). When <i>RT</i> is 2 then the feature whose feature code is equal to <i>FC</i>, if any, is returned. When <i>RT</i> is 3 the response is reserved (probably yields an &quot;illegal field in cdb&quot; error). To simplify the meanings of the <i>RT</i> values are: </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>0</code>&nbsp;<wbr>: all features, current on not </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>1</code>&nbsp;<wbr>: only current features </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>2</code>&nbsp;<wbr>: only feature whose code is&nbsp;<wbr><i>FC</i> </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>3</code>&nbsp;<wbr>: reserved </p>
<dt><code>-R</code>, <code>&#8211;raw</code></p>
<dd>output response in binary (to stdout). Note that the short form is <i>-R</i> unlike most other utilities in this package that use <i>-r</i> for this action.</p>
<dt><code>-s</code>, <code>&#8211;starting</code>=<i>FC</i></p>
<dd>where <i>FC</i> is the feature code value. This option works closely with the <i>&#8211;rt=RT</i> option. The <i>FC</i> value is in the range 0 to 65535 (0xffff) inclusive. Its default value is 0. A value prefixed with &quot;0x&quot; (or a trailing &#8216;h&#8217;) is interpreted as hexadecimal.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the level of verbosity, (i.e. debug output).</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</dl>
<h2>Notes</h2>
<p>There are multiple versions of the MMC (draft) standards: MMC [1997], MMC-2 [2000], MMC-3 [2002], MMC-4 and MMC-5. The first three are now ANSI INCITS standards with the year they became standards shown in brackets. The draft immediately prior to standardization can be found at <a rel="nofollow" href="http://www.t10.org">http://www.t10.org</a> . In the initial MMC standard there was no GET CONFIGURATION command and the relevant information was obtained from the &quot;CD capabilities and mechanical status mode page&quot; (mode page 0x2a). It was later renamed the &quot;MM capabilities and mechanical status mode page&quot; and has been made obsolete in MMC-4 and MMC-5. The GET CONFIGURATION command was introduced in MMC-2 and has become a replacement for that mode page. New features such as support for &quot;BD&quot; (blue ray) media type can only be found by using the GET CONFIGURATION command. Hence older CD players may not support the GET CONFIGURATION command in which case the &quot;MM capabilities &#8230;&quot; mode page can be checked with <a href="/docs/linux/man/8-sdparm/">sdparm</a>(8), <a href="/docs/linux/man/8-sginfo/">sginfo</a>(8) or <a href="/docs/linux/man/8-sg_modes/">sg_modes</a>(8). </p>
<p> In the 2.4 series of Linux kernels the <i>DEVICE</i> must be a SCSI generic (sg) device. In the 2.6 series block devices can also be specified. For example &quot;sg_get_config /dev/hdc&quot; will work in the 2.6 series kernels as long as /dev/hdc is an ATAPI device. In the 2.6 series external DVD writers attached via USB could be queried with &quot;sg_get_config /dev/scd1&quot; for example.</p>
<h2>Exit Status</h2>
<p>The exit status of sg_get_config is 0 when it is successful. Otherwise see the <a href="/docs/linux/man/8-sg3_utils/">sg3_utils</a>(8) man page.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2012 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sginfo/">sginfo</a>(8), <a href="/docs/linux/man/8-sg_modes/">sg_modes</a>(8), <a href="/docs/linux/man/8-sg_inq/">sg_inq</a>(8), <a href="/docs/linux/man/8-sg_prevent/">sg_prevent</a>(8),</code> <code><a href="/docs/linux/man/8-sg_start/">sg_start</a>(8) [all in sg3_utils],</code> <code><a href="/docs/linux/man/8-sdparm/">sdparm</a>(8)</code> </p>
