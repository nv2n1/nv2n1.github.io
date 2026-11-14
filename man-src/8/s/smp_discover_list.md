---
title: "smp_discover_list(8)"
name: "smp_discover_list"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smp_discover_list/"
description: "smp_discover_list – invoke DISCOVER LIST SMP function"
---

<p>smp_discover_list &#8211; invoke DISCOVER LIST SMP function</p>
<h2>Synopsis</h2>
<p><code>smp_discover_list</code> [<i>&#8211;adn</i>] [<i>&#8211;brief</i>] [<i>&#8211;cap</i>] [<i>&#8211;descriptor=TY</i>] [<i>&#8211;filter=FI</i>] [<i>&#8211;help</i>] [<i>&#8211;hex</i>] [<i>&#8211;ignore</i>] [<i>&#8211;interface=PARAMS</i>] [<i>&#8211;num=NUM</i>] [<i>&#8211;one</i>] [<i>&#8211;phy=ID</i>] [<i>&#8211;raw</i>] [<i>&#8211;sa=SAS_ADDR</i>] [<i>&#8211;summary</i>] [<i>&#8211;verbose</i>] [<i>&#8211;version</i>] [<i>&#8211;zpi=FN</i>] <i>SMP_DEVICE[,N]</i></p>
<h2>Description</h2>
<p>Sends one or more SAS Serial Management Protocol (SMP) DISCOVER LIST function requests to an SMP target and decodes or outputs the responses. The SMP target is identified by the <i>SMP_DEVICE</i> and the <i>SAS_ADDR</i>. Depending on the interface, the <i>SAS_ADDR</i> may be deduced from the <i>SMP_DEVICE</i>. The mpt interface uses <i>SMP_DEVICE</i> to identify a HBA (an SMP initiator) and needs the additional <i>,N</i> to differentiate between HBAs if there are multiple present. </p>
<p> If the <i>&#8211;phy=ID</i> option is not given then <i>&#8211;summary</i> is assumed. When <i>&#8211;summary</i> is given or assumed, this utility shows the disposition of each active expander phy in table form. One row is shown for each phy and is described in the SINGLE LINE PER PHY FORMAT section below. For this purpose disabled expander phys and those with errors are considered &quot;active&quot; and can be suppressed from the output by adding the <i>&#8211;brief</i> option. </p>
<p> The DISCOVER LIST response may contain up to 8 descriptors when the &quot;descriptor type&quot; field in the request is set to 0 (e.g. <i>&#8211;descriptor=0</i>). The DISCOVER LIST response may contain up to 40 descriptors when the &quot;descriptor type&quot; field in the request is set to 1 (e.g. <i>&#8211;descriptor=1</i>). Multiple DISCOVER LIST requests will be made if more descriptors are requested (e.g. <i>&#8211;summary</i> requests 254) and the previous response indicates that more descriptors may be available.</p>
<h2>Options</h2>
<p>Mandatory arguments to long options are mandatory for short options as well.</p>
<dl>
<dt><code>-A</code>, <code>&#8211;adn</code></p>
<dd>causes the &quot;attached device name&quot; field to be output when the <i>&#8211;one</i> or <i>&#8211;summary</i> option is also given. See the section below on SINGLE LINE PER PHY FORMAT. Note the &quot;attached device name&quot; field is not available in the short format (e.g. <i>&#8211;descriptor=1</i>).</p>
<dt><code>-b</code>, <code>&#8211;brief</code></p>
<dd>reduce the decoded response output.</p>
<dt><code>-c</code>, <code>&#8211;cap</code></p>
<dd>decode and print phy capabilities bits fields (see SNW-3 in draft). Each expander phy has three of these fields: programmed, current and attached. By default these fields are only printed out in hex, or not at all if the <i>&#8211;brief</i> option is given or implied. Of the three the attached phy capability field is probably the most interesting. If the <i>&#8211;verbose</i> option is given, then the various &quot;G&quot; identifiers are expanded (e.g. instead of &quot;G4:&quot; it prints &quot;G4 (12 Gbps):&quot;).</p>
<dt><code>-d</code>, <code>&#8211;descriptor</code>=<i>TY</i></p>
<dd>set the &quot;descriptor type&quot; field in the request. When <i>TY</i> is 0 then the 120 byte response defined by the DISCOVER function response (less its CRC field) is placed in the descriptors of this function&#8217;s response. When <i>TY</i> is 1 the short format (i.e. 24 byte per descriptor) information is placed in the descriptors of this function&#8217;s response.</p>
<dt><code>-f</code>, <code>&#8211;filter</code>=<i>FI</i></p>
<dd>set the filter field in the request. When <i>FI</i> is 0 (default) fetch descriptors for all phys. When <i>FI</i> is 1 only fetch descriptors for phys attached to (other) expanders. When <i>FI</i> is 2 only fetch descriptors for phys attached to expanders, SAS or SATA devices. When <i>FI</i> is 1 or 2, expander phys that would yield &quot;phy vacant&quot; (indicating they are hidden by zoning) are filtered out.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>output the usage message then exit.</p>
<dt><code>-H</code>, <code>&#8211;hex</code></p>
<dd>output the response (less the CRC field) in hexadecimal.</p>
<dt><code>-i</code>, <code>&#8211;ignore</code></p>
<dd>sets the Ignore Zone Group bit in the SMP Discover list request.</p>
<dt><code>-I</code>, <code>&#8211;interface</code>=<i>PARAMS</i></p>
<dd>interface specific parameters. In this case &quot;interface&quot; refers to the path through the operating system to the SMP initiator. See the smp_utils man page for more information.</p>
<dt><code>-n</code>, <code>&#8211;num</code>=<i>NUM</i></p>
<dd>maximum number of descriptors fetch. If any descriptors are in the response the first phy id will be greater than or equal to the argument of <i>&#8211;phy=ID</i>. Note that maximum SMP frame size is 1032 bytes (including a trailing 4 byte CRC) which may limit the number of descriptors that can be fetched by a single DISCOVER LIST function (especially when &#8216;&#8211;descriptor=0&#8217;).</p>
<dt><code>-o</code>, <code>&#8211;one</code></p>
<dd>use one line (summarized) format for each descriptor in the response. The default action when this option is not given is to output multiple indented lines for each descriptor in the response. See the section below on SINGLE LINE PER PHY FORMAT.</p>
<dt><code>-p</code>, <code>&#8211;phy</code>=<i>ID</i></p>
<dd>phy identifier. <i>ID</i> is a value between 0 and 254. This is the starting (lowest numbered) phy id to fetch in the response. Note that due to the filter field setting, the first phy id in the response may be greater than the argument to this option.</p>
<dt><code>-r</code>, <code>&#8211;raw</code></p>
<dd>send the response (less the CRC field) to stdout in binary. All error messages are sent to stderr.</p>
<dt><code>-s</code>, <code>&#8211;sa</code>=<i>SAS_ADDR</i></p>
<dd>specifies the SAS address of the SMP target device. Typically this is an expander. This option may not be needed if the <i>SMP_DEVICE</i> has the target&#8217;s SAS address within it. The <i>SAS_ADDR</i> is in decimal but most SAS addresses are shown in hexadecimal. To give a number in hexadecimal either prefix it with &#8216;0x&#8217; or put a trailing &#8216;h&#8217; on it.</p>
<dt><code>-S</code>, <code>&#8211;summary</code></p>
<dd>output a multi line summary, with one line per active phy. Checks up to 254 phys starting at phy identifier <i>ID</i> (which defaults to 0). Equivalent to &#8216;-o -d 1 -n 254 -b&#8217; unless the <i>&#8211;adn</i> option was also given, in which case it is equivalent to &#8216;-o -d 0 -n 254 -b&#8217; . See the section below on SINGLE LINE PER PHY FORMAT.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>increase the verbosity of the output. Can be used multiple times.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>print the version string and then exit.</p>
<dt><code>-Z</code>, <code>&#8211;zpi</code>=<i>FN</i></p>
<dd><i>FN</i> is a file that will be created or truncated then have zone phy information written to it in a format suitable for input to the smp_conf_zone_phy_info utility&#8217;s <i>&#8211;pconf=FN</i> option. If <i>&#8211;num=NUM</i> is not given it is set to 254. The output will start from phy_id 0 unless <i>&#8211;phy=ID</i> is given.</dl>
<h2>Single Line Per Phy Format</h2>
<p>The <i>&#8211;summary</i> (or <i>&#8211;one</i>) option causes SMP DISCOVER LIST descriptors to be compressed to one line per phy. To save space SAS addresses are shown in hex without a &#8216;0x&#8217; prefix or &#8216;h&#8217; suffix. The header section outputs information found in the DISCOVER LIST response&#8217;s header section. </p>
<p> For each descriptor in the DISCOVER LIST response, one line is output starting with &quot; phy &lt;n&gt;:&quot; where &lt;n&gt; is the phy identifier (and they are origin zero). That is followed by the routing attribute represented by a single letter which is either &quot;D&quot; for direct routing, &quot;S&quot; for subtractive routing, &quot;T&quot; or &quot;U&quot;. Both &quot;T&quot; and &quot;U&quot; imply table routing, the difference is that if REPORT GENERAL indicates &quot;table to table supported&quot; then &quot;U&quot; is output to indicate that phy can be part of an enclosure <code>universal</code> port; otherwise &quot;T&quot; is used. Next comes the negotiated physical link rate which is either &quot;disabled&quot;, &quot;reset problem&quot; or &quot;spinup hold&quot;. Other states are mapped to &quot;attached&quot;. This includes enabled phys with nothing connected which appear as &quot;attached:[0000000000000000:00]&quot;. </p>
<p> Information shown between the brackets is for the attached device. Phys that are connected display something like: &quot;attached:[5000c50000520a2a:01 &quot; where the first number is the attached SAS address (in hex) and the second number is the attached device&#8217;s phy identifier. If the attached device type is other than an SAS or SATA device then one of these abbreviations is output: &quot;exp&quot; (for expander), &quot;fex&quot; (for fanout expander) or &quot;res&quot; (for unknown attached device type). If a phy is flagged as &quot;virtual&quot; then the letter &quot;V&quot; appears next. Next are the protocols supported by the attached device which are shown as &quot;i(&lt;list&gt;)&quot; for initiator protocols and/or &quot;t(&lt;list&gt;)&quot; for target protocols. The &lt;list&gt; is made up of &quot;PORT_SEL&quot;, &quot;SSP&quot;, &quot;STP&quot;, &quot;SMP&quot; and &quot;SATA&quot; with &quot;+&quot; used as a separator. For example a SAS host adapter will most likely appear as: &quot;i(SSP+STP+SMP)&quot;. This completes the information about the attached phy, hence the closing right bracket. </p>
<p> If appropriate, the negotiated physical link rate is shown in gigabits per second. Here is an example of a line for expander phy identifier 11 connected to a SATA target (or SATA &quot;device&quot; to use the t13.org term): </p>
<p>&nbsp;<wbr>&nbsp;<wbr>phy&nbsp;<wbr>&nbsp;<wbr>11:T:attached:[500605b000000afb:00&nbsp;<wbr>&nbsp;<wbr>t(SATA)]&nbsp;<wbr>&nbsp;<wbr>1.5 Gbps </p>
<p> If the expander has zoning enabled (i.e. REPORT GENERAL response bit for &#8216;zoning enabled&#8217; is set) and a phy&#8217;s zone group is other than zg 1 then the phy&#8217;s zone group is shown (e.g. &quot;ZG:2&quot;). </p>
<p> If the <i>&#8211;adn</i> option is given then after the attached SAS address and the attached device&#8217;s phy identifier are output an extra field is inserted containing the &quot;attached device name&quot; field. For a SAS disk this should be its target device name (in NAA-5 format) and for a SATA disk its WWN (if provided, also in NAA-5 format). Also when the <i>&#8211;adn</i> option is given the phy speed and zone group are not output in order to keep the line length reasonable.</p>
<h2>Notes</h2>
<p>In SAS-2 and later both the DISCOVER and DISCOVER LIST functions are available. The DISCOVER LIST function should be favoured for several reasons: its response can hold up to 40 descriptors each describing the state of one expander phy. The vast majority of expander chips on the market support 36 phys or less so one DISCOVER LIST response will summarize the states of all its phys. With the DISCOVER function only one expander phy&#8217;s state is returned in its response. Other advantages of the DISCOVER LIST function are its &quot;phy filter&quot; and &quot;descriptor type&quot; function request fields.</p>
<h2>Conforming To</h2>
<p>The SMP DISCOVER LIST function was introduced in SAS-2 .</p>
<h2>Authors</h2>
<p>Written by Douglas Gilbert.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;dgilbert at interlog dot com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2006-2014 Douglas Gilbert<br />
 This software is distributed under a FreeBSD license. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code>smp_utils, smp_discover, smp_phy_control, smp_conf_zone_phy_info</code> </p>
