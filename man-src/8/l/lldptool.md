---
title: "lldptool(8)"
name: "lldptool"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lldptool/"
description: "lldptool – manage the LLDP settings and status of lldpad"
---

<p>lldptool &#8211; manage the LLDP settings and status of lldpad</p>
<h2>Synopsis</h2>
<p><code>lldptool &lt;command&gt; [options] [argument]</code> </p>
<h2>Description</h2>
<p><code>lldptool</code> is used to query and configure <code>lldpad.</code> It connects to the client interface of <code>lldpad</code> to perform these operations. <code>lldptool</code> will operate in interactive mode if it is executed without a <i>command</i>. In interactive mode, <code>lldptool</code> will also function as an event listener to print out events as they are received asynchronously from <code>lldpad.</code> It will use libreadline for interactive input when available. </p>
<h2>Options</h2>
<dl>
<dt><code>-i [ifname]</code></p>
<dd>specifies the network interface to which the command applies. Most lldptool commands require specifying a network interface.</p>
<dt><code>-V [tlvid]</code></p>
<dd>specifies the TLV identifier<br />
 The tlvid is an integer value used to identify specific LLDP TLVs. The tlvid value is the Type value for types not equal to 127 (the organizationally specific type). For organizationally specific TLVs, the tlvid is the value represented by the 3 byte OUI and 1 byte subtype &#8211; where the subtype is the lowest order byte of the tlvid.<br />
 The tlvid can be entered as a numerical value (e.g. 10 or 0xa), or for supported TLVs, as a keyword. Review the <code>lldptool</code> help output to see the list of supported TLV keywords.</p>
<dt><code>-n</code></p>
<dd>&quot;neighbor&quot; option for commands which can use it (e.g. get-tlv)</p>
<dt><code>-g [bridge scope]</code></p>
<dd>specify the bridge scope this command operates on. Allows to set and query all LLDP TLV modules for &quot;nearest_bridge&quot; (short: &quot;nb&quot;), &quot;nearest_customer_bridge&quot; (&quot;ncb&quot;) and &quot;nearest_nontpmr_bridge&quot; (&quot;nntpmrb&quot;) group mac addresses. Configurations are saved into independent sections in lldpad.conf. If no bridge scope is supplied this defaults to &quot;nearest bridge&quot; to preserve the previous behaviour.</p>
<dt><code>-c &lt;argument list&gt;</code></p>
<dd>&quot;config&quot; option for TLV queries. Indicates that the query is for the configuration elements for the specified TLV. The argument list specifies the specific elements to query. If no arguments are listed, then all configuration elements for the TLV are returned.</p>
<dt><code>-r</code></p>
<dd>show raw client interface messages</p>
<dt><code>-R</code></p>
<dd>show only raw Client interface messages</dl>
<h2>Commands</h2>
<dl>
<dt><code>license</code></p>
<dd>show license information</p>
<dt><code>-h, help</code></p>
<dd>show usage information</p>
<dt><code>-v, version</code></p>
<dd>show version information</p>
<dt><code>-S, stats</code></p>
<dd>get LLDP statistics for the specified interface</p>
<dt><code>-t, get-tlv</code></p>
<dd>get TLV information for the specified interface</p>
<dt><code>-T, set-tlv</code></p>
<dd>set TLV information for the specified interface</p>
<dt><code>-l, get-lldp</code></p>
<dd>get LLDP parameters for the specified interface</p>
<dt><code>-L, set-lldp</code></p>
<dd>set LLDP parameters for the specified interface</p>
<dt><code>-p, ping</code></p>
<dd>display the process identifier of the running lldpad process</p>
<dt><code>-q, quit</code></p>
<dd>exit from interactive mode</dl>
<h2>Arguments</h2>
<p>This section lists arguments which are available for administration of LLDP parameters. Arguments for basic TLV&#8217;s (non-organizationally specific TLVs) are also described. See the SEE ALSO section for references to other lldptool man pages which contain usage details and arguments for various organizationally specific TLVs. </p>
<dl>
<dt><code>adminStatus</code></p>
<dd>Argument for the <code>get-lldp/set-lldp</code> commands. Configures the LLDP adminStatus parameter for the specified interface. Valid values are: <i>disabled</i>, <i>rx</i>, <i>tx</i>, <i>rxtx</i> </p>
<dt><code>enableTx</code></p>
<dd>Argument for the <code>get-tlv/set-tlv</code> commands. May be applied per interface for a specified TLV. Valid values are: <i>yes</i>, <i>no</i>. If the DCBX TLV enableTx is set to <i>no</i>, then all of the DCB feature TLVs DCBX advertise settings will be turned off as well. Setting enableTx to <i>yes</i> will enable the DCBX advertise settings. </p>
<dt><code>ipv4</code></p>
<dd>Argument for the <code>get-tlv/set-tlv</code> commands with respect to the Management Address TLV. The get command will retrieve the configured value. Set values take the form of an IPv4 address: <i>A.B.C.D</i> </p>
<dt><code>ipv6</code></p>
<dd>Argument for the <code>get-tlv/set-tlv</code> commands with respect to the Management Address TLV. The get command will retrieve the configured value. Set values take the form of an IPv6 address: <i>1111:2222:3333:4444:5555:6666:7777:8888</i> and various shorthand variations. </p>
</dl>
<h2>Examples</h2>
<dl>
<dt>Configure LLDP adminStatus to Receive and Transmit for interface <i>eth2</i></p>
<dd><code>lldptool -L -i eth2 adminStatus=rxtx</code><br />
 <code>lldptool set-lldp -i eth2 adminStatus=rxtx</code></p>
<dt>Query the LLDP adminStatus for interface <i>eth3</i></p>
<dd><code>lldptool -l -i eth3 adminStatus</code><br />
 <code>lldptool get-lldp -i eth3 adminStatus</code></p>
<dt>Query the LLDP statistics for interface <i>eth3</i></p>
<dd><code>lldptool -S -i eth3 adminStatus</code><br />
 <code>lldptool stats -i eth3 adminStatus</code></p>
<dt>Query the local TLVs which are being transmitted for a given interface:</p>
<dd><code>lldptool -t -i eth3</code><br />
 <code>lldptool get-tlv -i eth3</code></p>
<dt>Query the received neighbor TLVs received on a given interface:</p>
<dd><code>lldptool -t -n -i eth3</code><br />
 <code>lldptool get-tlv -n -i eth3</code></p>
<dt>Query the value of the System Description TLV as received from the neighbor on a given interface:</p>
<dd><code>lldptool -t -n -i eth3 -V sysDesc</code><br />
 <code>lldptool get-tlv -n -i eth3 -V 6</code></p>
<dt>Disable transmit of the IEEE 802.3 MAC/PHY Configuration Status TLV for a given interface:</p>
<dd><code>lldptool -T -i eth3 -V macPhyCfg enableTx=no</code><br />
 <code>lldptool set-tlv -i eth3 -V 0x120f01 enableTx=no</code></p>
<dt>Query value of the transmit setting for the Port Description TLV for a given interface:</p>
<dd><code>lldptool -t -i eth3 -V portDesc -c enableTx</code><br />
 <code>lldptool get-tlv -i eth3 -V 4 -c enableTx</code></p>
<dt>Set a Management Address TLV on eth3 to carry IPv4 address 192.168.10.10</p>
<dd><code>lldptool -T -i eth3 -V mngAddr ipv4=192.168.10.10</code></p>
<dt>Set a Management Address TLV on eth3 to carry IPv6 address ::192.168.10.10</p>
<dd><code>lldptool -T -i eth3 -V mngAddr ipv6=::192.168.10.10</code></p>
<dt>Get the configured IPv4 address for the Management Address TLV on eth3</p>
<dd><code>lldptool -t -i eth3 -V mngAddr -c ipv4</code></p>
<dt>Get all configured attributes for the Management Address TLV on eth3</p>
<dd><code>lldptool -t -i eth3 -V mngAddr -c</code></p>
<dt>Enable transmit of the Edge Virtual Bridging TLV for interface eth4</p>
<dd><code>lldptool -i eth4 -T -g ncb -V evbCfg enableTx=yes</code></p>
<dt>Enable transmit of VDP for interface eth4</p>
<dd><code>lldptool -i eth4 -T -V vdp enableTx=yes</code></p>
<dt>Display process identifier of lldpad</p>
<dd><code>lldptool -p</code> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lldptool-dcbx/">lldptool-dcbx</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-ets/">lldptool-ets</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-pfc/">lldptool-pfc</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-app/">lldptool-app</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-med/">lldptool-med</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-vdp/">lldptool-vdp</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-evb/">lldptool-evb</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-evb22/">lldptool-evb22</a></code>(8), <code><a href="/docs/linux/man/8-dcbtool/">dcbtool</a></code>(8), <code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8) </p>
<h2>Copyright</h2>
<p>lldptool &#8211; LLDP agent configuration utility<br />
 Copyright(c) 2007-2012 Intel Corporation. Portions of lldptool are based on:</p>
<dl>
<dt>hostapd-0.5.7</p>
<dd>
<dt>Copyright</p>
<dd>(c) 2004-2008, Jouni Malinen &lt;j@w1.fi&gt; </p>
</dl>
<h2>License</h2>
<p>This program is free software; you can redistribute it and/or modify it under the terms and conditions of the GNU General Public License, version 2, as published by the Free Software Foundation. </p>
<p> This program is distributed in the hope it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin St &#8211; Fifth Floor, Boston, MA 02110-1301 USA. </p>
<p> The full GNU General Public License is included in this distribution in the file called &quot;COPYING&quot;.</p>
<h2>Support</h2>
<p>Contact Information: open-lldp Mailing List &lt;lldp-devel [at] open-lldp.org&gt;</p>
