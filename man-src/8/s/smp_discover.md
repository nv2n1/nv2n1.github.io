---
title: "smp_discover(8)"
name: "smp_discover"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_discover/"
description: "smp_discover – invoke DISCOVER SMP function"
---

<p>smp_discover &#8211; invoke DISCOVER SMP function</p>
<h2>Synopsis</h2>
<p><code>smp_discover</code> [<i>&#8211;adn</i>] [<i>&#8211;brief</i>] [<i>&#8211;cap</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;ignore</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;list</i>] [<i>&#8211;multiple</i>] [<i>&#8211;my</i>] [<i>&#8211;num=NUM</i>] [<i>&#8211;phy=ID</i>] [<i>&#8211;raw</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;summary</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>&#8211;zero</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends one or more SAS Serial Management Protocol (SMP) DISCOVER function requests to an SMP target and decodes or outputs the responses. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present. </p>
<p> If the <i>&#8211;phy=ID</i> option is not given then <i>&#8211;summary</i> is assumed. When <i>&#8211;summary</i> is given or assumed, this utility shows the disposition of each active expander phy in table form. One row is shown for each phy and is described in the SINGLE LINE PER PHY FORMAT section below. For this purpose disabled expander phys and those with errors are considered &quot;active&quot; and can be suppressed from the output by adding the <i>&#8211;brief</i> option.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-A</code>, <code>&#8211;adn</code></p>
<dd>causes the &quot;attached device name&quot; field to be output when the <i>&#8211;multiple</i> or <i>&#8211;summary</i> option is also given. See the section below on SINGLE LINE PER PHY FORMAT. Note the &quot;attached device name&quot; field was added is SAS-2.</p>
<dt><code>-b</code>, <code>&#8211;brief</code></p>
<dd>reduce the decoded response output. If used twice will exit if there is no attached device (after outputting that). When used with <i>&#8211;multiple</i>, unattached phys are not listed; when used twice, trims attached phys output.</p>
<dt><code>-c</code>, <code>&#8211;cap</code></p>
<dd>decode and print phy capabilities bits fields (see SNW-3 in draft). Each expander phy has three of these fields: programmed, current and attached. By default these fields are only printed out in hex, or not at all if the <i>&#8211;brief</i> option is given or implied. Of the three the attached phy capability field is probably the most interesting. If the <i>&#8211;verbose</i> option is given, then the various &quot;G&quot; identifiers are expanded (e.g. instead of &quot;G4:&quot; it prints &quot;G4 (12 Gbps):&quot;).</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-i</code>, <code>&#8211;ignore</code></p>
<dd>sets the Ignore Zone Group bit in the SMP Discover request. Expander phys hidden by zoning will appear as &quot;phy vacant&quot; unless this option is given.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd>list attributes in &quot;name=value&quot; form, one entry per line.</p>
<dt><code>-m</code>, <code>&#8211;multiple</code></p>
<dd>loops over multiple phys within SMP target (typically an expander) and does a DISCOVER request and outputs a one line summary. Phy 0 is queried first, then phy 1, continuing until an error occurs. The starting phy and the number of phys &quot;discovered&quot; can be controlled by <i>&#8211;phy=ID</i> and <i>&#8211;num=NUM</i>. If <i>&#8211;brief</i> is given then there is no output for phys that indicate there is no attached device. When this option is used twice then multi-line output is produced for each phy. See the section below on SINGLE LINE PER PHY FORMAT.</p>
<dt><code>-M</code>, <code>&#8211;my</code></p>
<dd>outputs my (this expander&#8217;s) SAS address in hex (prefixed by &quot;0x&quot;). This is obtained from the DISCOVER response of phy id 0 (unless <i>&#8211;phy=ID</i> is given). The expander&#8217;s SAS address is typically available even if a phy is not connected, &quot;vacant&quot; or disabled. This option overrides most other options (e.g. overrides <i>&#8211;multiple</i> and <i>&#8211;summary</i> options).</p>
<dt><code>-n</code>, <code>&#8211;num</code>=<i>NUM</i></p>
<dd>number of phys to fetch, starting at <i>&#8211;phy=ID</i> when the <i>&#8211;multiple</i> option is given. The default value is 0 which is interpreted as &quot;the rest&quot; (i.e. until a &quot;phy does not exist&quot; function result is received). This option is ignored in the absence of the <i>&#8211;multiple</i> option.</p>
<dt><code>-p</code>, <code>&#8211;phy</code>=<i>ID</i></p>
<dd>phy identifier. <i>ID</i> is a value between 0 and 254. If this option is not given then the <i>&#8211;summary</i> option is assumed.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. Typically this is an expander. This option may not be needed if the <i>SMP_DEVICE</i> has the target&#8217;s SAS address within it. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-S</code>, <code>&#8211;summary</code></p>
<dd>output a multi line summary, with one line per active phy. Checks all phys (or less is <i>&#8211;num=NUM</i> is given), starting at phy 0 (unless <i>&#8211;phy=ID</i> is given). Equivalent to &#8216;&#8211;multiple &#8211;brief&#8217; (&#8216;-mb&#8217;). See the section below on SINGLE LINE PER PHY FORMAT. If the <i>&#8211;phy=ID</i> is not given then this option is assumed.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</p>
<dt><code>-z</code>, <code>&#8211;zero</code></p>
<dd>zero the Allocated Response Length field in the request. This option also zeros the Request Length field in the request. This is required for strict SAS-1.1 compliance. However this option should not be given in SAS-2 and later; if it is given an abridged response may result.</dl>
<h2>Single Line Per Phy Format</h2>
<p>The <i>&#8211;summary</i> option causes SMP DISCOVER responses to be compressed to a header followed by one line per phy. To save space SAS addresses are shown in hex without a &#8216;0x&#8217; prefix or &#8216;h&#8217; suffix. The header line gives the SAS address of the SMP target itself and assumes it is an expander. </p>
<p> Each line starts with &quot; phy &lt;n&gt;:&quot; where &lt;n&gt; is the phy identifier (and they are origin zero). That is followed by the routing attribute represented by a single letter which is either &quot;D&quot; for direct routing, &quot;S&quot; for subtractive routing, &quot;T&quot; or &quot;U&quot;. Both &quot;T&quot; and &quot;U&quot; imply table routing, the difference is that if REPORT GENERAL indicates &quot;table to table supported&quot; then &quot;U&quot; is output to indicate that phy can be part of an enclosure <code>universal</code> port; otherwise &quot;T&quot; is used. Next comes the negotiated physical link rate which is either &quot;disabled&quot;, &quot;reset problem&quot; or &quot;spinup hold&quot;. Other states are mapped to &quot;attached&quot;. This includes enabled phys with nothing connected which appear as &quot;attached:[0000000000000000:00]&quot;. </p>
<p> Information shown between the brackets is for the attached device. Phys that are connected display something like: &quot;attached:[5000c50000520a2a:01 &quot; where the first number is the attached SAS address (in hex) and the second number is the attached device&#8217;s phy identifier. If the attached device type is other than a SAS or SATA device then one of these abbreviations is output: &quot;exp&quot; (for expander), &quot;fex&quot; (for fanout expander) or &quot;res&quot; (for unknown attached device type). If a phy is flagged as &quot;virtual&quot; then the letter &quot;V&quot; appears next. Next are the protocols supported by the attached device which are shown as &quot;i(&lt;list&gt;)&quot; for initiator protocols and/or &quot;t(&lt;list&gt;)&quot; for target protocols. The &lt;list&gt; is made up of &quot;PORT_SEL&quot;, &quot;SSP&quot;, &quot;STP&quot;, &quot;SMP&quot; and &quot;SATA&quot; with &quot;+&quot; used as a separator. For example a SAS host adapter will most likely appear as: &quot;i(SSP+STP+SMP)&quot;. This completes the information about the attached phy, hence the closing right bracket. </p>
<p> If appropriate, the negotiated physical link rate is shown in gigabits per second. Here is an example of a line for expander phy identifier 11 connected to a SATA target (or SATA &quot;device&quot; to use the t13.org term): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>phy&nbsp;<wbr>&nbsp;<wbr>11:T:attached:[500605b000000afb:00&nbsp;<wbr>&nbsp;<wbr>t(SATA)]&nbsp;<wbr>&nbsp;<wbr>1.5 Gbps </p>
<p> If the expander has zoning enabled (i.e. REPORT GENERAL response bit for &#8216;zoning enabled&#8217; is set) and a phy&#8217;s zone group is other than zg 1 then the phy&#8217;s zone group is shown (e.g. &quot;ZG:2&quot;). </p>
<p> If the <i>&#8211;adn</i> option is given then after the attached SAS address and the attached device&#8217;s phy identifier are output an extra field is inserted containing the &quot;attached device name&quot; field. For a SAS disk this should be its target device name (in NAA-5 format) and for a SATA disk its WWN (if provided, also in NAA-5 format). Also when the <i>&#8211;adn</i> option is given the phy speed and zone group are not output in order to keep the line length reasonable.</p>
<h2>Notes</h2>
<p>In SAS-2 and later both the DISCOVER and DISCOVER LIST functions are available. The DISCOVER LIST function should be favoured for several reasons: its response can hold up to 40 descriptors each describing the state of one expander phy. The vast majority of expander chips on the market support 36 phys or less so one DISCOVER LIST response will summarize the states of all its phys. With the DISCOVER function only one expander phy&#8217;s state is returned in its response. Other advantages of the DISCOVER LIST function are its &quot;phy filter&quot; and &quot;descriptor type&quot; function request fields.</p>
<h2>Examples</h2>
<p>See &quot;Examples&quot; section in <a rel="nofollow" href="http://sg.danny.cz/sg/smp_utils.html">http://sg.danny.cz/sg/smp_utils.html</a></p>
<h2>Conforming To</h2>
<p>The SMP DISCOVER function was introduced in SAS-1, with small additions in SAS-1.1 . There were a large number of additions in SAS-2 . After SAS-2 the protocol sections of SAS were split into another document series known as SPL. Now SPL and SPL-2 are standards and SPL-3 is in the draft stage.</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2014 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_discover_list, smp_phy_control</code> </p>
