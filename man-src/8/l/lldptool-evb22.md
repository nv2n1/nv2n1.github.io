---
title: "lldptool-evb22(8)"
name: "lldptool-evb22"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lldptool-evb22/"
description: "evb22 – Show / manipulate EVB IEEE 802.1 Ratified Standard TLV configuration"
---

<p>evb22 &#8211; Show / manipulate EVB IEEE 802.1 Ratified Standard TLV configuration</p>
<h2>Synopsis</h2>
<p><code>lldptool -t -i ethx -g ncb -V evb</code> </p>
<p> <code>lldptool -t -i ethx -g ncb -V evb -c</code> </p>
<p> <code>lldptool -t -i ethx -g ncb -V evb -c enabletx</code> </p>
<p> <code>lldptool -T -i ethx -g ncb -V evb -c enabletx=[yes|no]</code> </p>
<p> <code>lldptool -t -i ethx -g ncb -V evb -c evbmode</code> </p>
<p> <code>lldptool -T -i ethx -g ncb -V evb -c evbmode=[bridge|station]</code> </p>
<p> <code>lldptool -t -i ethx -g ncb -V evb -c evbrrreq</code> </p>
<p> <code>lldptool -T -i ethx -g ncb -V evb -c evbrrreq=[yes|no]</code> </p>
<p> <code>lldptool -t -i ethx -g ncb -V evb -c evbrrcap</code> </p>
<p> <code>lldptool -T -i ethx -g ncb -V evb -c evbrrcap=[yes|no]</code> </p>
<p> <code>lldptool -t -i ethx -g ncb -V evb -c evbgpid</code> </p>
<p> <code>lldptool -T -i ethx -g ncb -V evb -c evbgpid=[yes|no]</code> </p>
<p> <code>lldptool -t -i ethx -g ncb -V evb -c ecpretries</code> </p>
<p> <code>lldptool -T -i ethx -g ncb -V evb -c ecpretries=[0..7]</code> </p>
<p> <code>lldptool -t -i ethx -g ncb -V evb -c ecprte</code> </p>
<p> <code>lldptool -T -i ethx -g ncb -V evb -c ecprte=[0..31]</code> </p>
<p> <code>lldptool -t -i ethx -g ncb -V evb -c vdprwd</code> </p>
<p> <code>lldptool -T -i ethx -g ncb -V evb -c vdprwd=[0..31]</code> </p>
<p> <code>lldptool -t -i ethx -g ncb -V evb -c vdprka</code> </p>
<p> <code>lldptool -T -i ethx -g ncb -V evb -c vdprka=[0..31]</code></p>
<h2>Description</h2>
<p>The Edge Virtual Bridge (EVB) TLV is a TLV to announce the station and bridge&#8217;s edge virtual bridging (EVB) capabilities and may request the bridge port to be set into reflective relay (hairpin) mode. If both sides agree on the modes and time out values, the edge control protocol (ECP) will be used to exchange VSI discovery protocol (VDP) data using ECP frames between the host interface and the adjacent switch port facing the host interface. </p>
<p> This man pages describes the IEEE 802.1 Qbg ratified standard dated from July 5th, 2012. The arguments and parameters differ from the IEEE 802.1 Qbg draft 0.2, which is also implemented. The EVB protocol version to be used depends on the organizational unique identifier (OUI) of the EVB TLV in the LLDP data stream. A OUI value of 0x001b3f stands for the IEEE 802.1 Qbg draft 0.2, a OUI value of 0x0080c2 stands for the IEEE 802.1 Qbg ratified standard. The version of the ECP and VDP protocols are determined by the ethernet type field in the ethernet header. The ethernet type value for IEEE 802.1 Qbg draft 0.2 is 0x88b7, the value for IEEE 802.1 Qbg ratified standard is 0x8890. Note that the EVB protocol is exchanged between nearest customer bridges only, employing the reserved multicast MAC address 01:80:c2:00:00:00 as destination MAC address. <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8) supports both versions, the switch port configuration determines which version will be used. The switch port configuration should select only one protocol version, never both. </p>
<p> The command line options and arguments are explained in the <code><a href="/docs/linux/man/8-lldptool/">lldptool</a></code>(8) man pages. Only the EVB, ECP and VDP protocol specific parameters are detailed in this manual page.</p>
<h2>Arguments</h2>
<p>The invocation without command line option &#8216;-c&#8217; and argument displays the complete EVB, ECP and VDP protocol settings in a pretty print out. See below for a detailed description on how to interpret the output.</p>
<dl>
<dt><code>-c</code> <i>text</i></p>
<dd>Use of the command line option &#8216;-c&#8217; without any argument displays all known parameters in the format of <i>key</i>=<i>value</i>, which is suitable for post processing. Use command line option &#8216;-c&#8217; and one of the following arguments to display and set individual parameters. <i>Text</i> can be one of the following values:</p>
<dt><code>enabletx</code></p>
<dd>Enables or disables the EVB TLV to be transmitted. When set to disabled no EVB TLV will be included in the LLDP data stream. Furthermore the output of the complete EVB settings without option &#8216;-c&#8217; will be empty.</p>
<dt><code>evbmode</code></p>
<dd>Display the current role or sets the role the to given value. Supported values are either &quot;station&quot; or &quot;bridge&quot;.</p>
<dt><code>evbrrreq</code></p>
<dd>Shows the current reflective relay (hairpin) request mode or sets the reflective relay (hairpin) request mode. If the value is &quot;yes&quot;, the station requests the interface facing switch port to be set in reflective relay (hairpin) mode. This field is only valid for stations, the output of evbmode equals &quot;station&quot;.</p>
<dt><code>evbrrcap</code></p>
<dd>Shows the current reflective relay (hairpin) capabilities or sets the reflective relay (hairpin) capabilities. If the value is &quot;yes&quot;, the switch port will be set in reflective relay (hairpin) mode. This field is only valid for switches, the output of evbmode equals &quot;bridge&quot;.</p>
<dt><code>gpid</code></p>
<dd>Shows the current station or switch support for grouping or turns on/off the station or switch support for grouping. If set to true, the station or switch wants to use group identifiers in VDP protocols.</p>
<dt><code>ecpretries</code></p>
<dd>Shows or sets the maximum number of retries for ECP frames to be retransmitted. A retransmit occurs when no ECP acknowledgement message has been received during a given time period.</p>
<dt><code>ecprte</code></p>
<dd>Shows or sets the local run time exponent (RTE). The RTE will be used as the base for the timing of the ECP protocol time outs and retransmits. The wait time is calculated as 10*2<i>ecprte</i> micro seconds.</p>
<dt><code>vdprwd</code></p>
<dd>Shows or sets the number of resource wait delay value. This value is calculated as 10*2<i>vdprwd</i> micro seconds and determines the maximum wait time for VDP protocol acknowledgements.</p>
<dt><code>vdprka</code></p>
<dd>Shows or sets the number of re-init keep alive value. This value is calculated as 10*2<i>vdprka</i> micro seconds and determines the wait time for VDP protocol to send a keep alive message.</dl>
<h2>Theory of Operation</h2>
<p>The EVB TLV is used to announce and exchange supported parameters between the station and an adjacent switch. If <i>reflectiverelay</i> is active, the switch sends back ethernet frames on the very same port it received the frame on. This is an extension to the current bridging standard and allows communication between virtual machines on the same host through the switch port.</p>
<h2>EXAMPLE &amp; USAGE</h2>
<dl>
<dt>Display locally configured values for <i>eth0</i></p>
<dd><code>lldptool -t -g ncb -i eth0 -V evb</code> </p>
<pre>EVB Configuration TLV
 bridge:(00)
 station:rrreq,rrstat(0x5)
 retries:7 rte:31
 mode:station r/l:0 rwd:31
 r/l:0 rka:8</pre>
</dl>
<p> This output is displayed when enabletx has been enabled. The first line shows the currently known status of the bridge. The second line shows the currently known status of the station. The status is displayed verbose appended by the hexadecimal value in parenthesis. The verbose output uses the bit naming convention used in the standard document. The third line displays the values for the ECP protocol number of retransmits (retries) and the retransmit timeout exponent. The forth line shows the current mode of operation, either bridge or station, the resource wait delay value (rwd) and an indication if the local (0) or remote (1) rwd value is used. The fifth line displays the value of the re-init keep alive counter (rka) and an indication if the local (0) or remote (1) rka value is used.</p>
<dl>
<dt>Display the currently requested forwarding mode for <i>eth0</i></p>
<dd><code>lldptool -t -g ncb -i eth0 -V evb -c evbrrreq</code></p>
<dt>Display the locally configured value for RTE</p>
<dd><code>lldptool -t -g ncb -i eth0 -V evb -c evbrte</code></p>
<dt>Set the value for RTE to its maximum value</p>
<dd><code>lldptool -T -g ncb -i eth0 -V evb -c rte=7</code></p>
<dt>Set the value for enabletx to yes</p>
<dd><code>lldptool -T -g ncb -i eth0 -V evb -c enabletx=yes</code></dl>
<h2>Notes</h2>
<p>Currently the code in lldpad reflects IEEE 802.1 Qbg draft 0.2 of the upcoming standard. Wireshark support for IEEE 802.1 Qbg ratified standard TLVs is currently missing. Support for the IEEE 802.1 Qbg ratified standard protocols ECP and VDP is currently under development and not fully functional.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lldptool-vdp/">lldptool-vdp</a></code>(8), <code><a href="/docs/linux/man/8-lldptool/">lldptool</a></code>(8), <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8)<br />
 IEEE 802.1Qbg (<a rel="nofollow" href="http://www.ieee802.org/1/pages/802.1bg.html)">http://www.ieee802.org/1/pages/802.1bg.html)</a></p>
<h2>Author</h2>
<p>Thomas Richter</p>
