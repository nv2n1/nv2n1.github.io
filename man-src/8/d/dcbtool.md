---
title: "dcbtool(8)"
name: "dcbtool"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dcbtool/"
description: "dcbtool – manage the Data Center Bridging (DCB) settings of a CEE DCB interface"
---

<p>dcbtool &#8211; manage the Data Center Bridging (DCB) settings of a CEE DCB interface</p>
<h2>Synopsis</h2>
<p><code>dcbtool -h</code><br />
 <code>dcbtool -v</code><br />
 <code>dcbtool [-rR]</code><br />
 <code>dcbtool [-rR] [</code><i>command</i><code>] [</code><i>command arguments</i><code>]</code> </p>
<h2>Description</h2>
<p><code>dcbtool</code> is used to query and set the DCB settings of a Converged Enhanced Ethernet (CEE) DCB capable Ethernet interface. It connects to the client interface of <code>lldpad</code> to perform these operations. <code>dcbtool</code> will operate in interactive mode if it is executed without a <i>command</i>. In interactive mode, <code>dcbtool</code> also functions as an event listener and will print out events received from <code>lldpad</code> as they arrive. It will use libreadline for interactive input when available. 802.1Qaz DCBX is not controllable from <code>dcbtool</code> instead <code>lldptool</code> can be used in this case.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>show the <code>dcbtool</code> usage message</p>
<dt><code>-v</code></p>
<dd>shows <code>dcbtool</code> version information</p>
<dt><code>-r</code></p>
<dd>display the raw <code>lldpad</code> client interface messages as well as the readable output.</p>
<dt><code>-R</code></p>
<dd>display only the raw <code>lldpad</code> client interface messages</dl>
<h2>Commands</h2>
<dl>
<dt><code>help</code></p>
<dd>shows the dcbtool usage message</p>
<dt><code>ping</code></p>
<dd>test command. <code>lldpad</code> responds with &quot;PPONG&quot; if the client interface is operational.</p>
<dt><code>license</code></p>
<dd>displays <code>dcbtool</code> license information</p>
<dt><code>quit</code></p>
<dd>exit from interactive mode </p>
</dl>
<p> The following commands interact with <code>lldpad</code> to manage the daemon and DCB features on DCB capable interfaces. </p>
<p> <code>dcbtool</code> general configuration commands:</p>
<dl>
<dt>&lt;<code>gc</code>|<code>go</code>&gt;<code> dcbx</code></p>
<dd>Get the configured or operational legacy version of the DCBX protocol which will be supported by <code>lldpad.</code> The configured version, if different from the operational version, will take effect after <code>lldpad</code> is restarted.</p>
<dt><code>sc dcbx v:</code>[<code>cin</code>|<code>cee</code>|<code>force-cin</code>|<code>force-cee</code>]</p>
<dd>Set the legacy version of DCBX which will be supported by <code>lldpad</code> the next time it is started.<br />
 Information about the CIN version can be found at:<br />
 &lt;<a rel="nofollow" href="http://download.intel.com/technology/eedc/dcb_cep_spec.pdf">http://download.intel.com/technology/eedc/dcb_cep_spec.pdf</a>&gt;<br />
 Information about the CEE version can be found at:<br />
 &lt;<a rel="nofollow" href="http://www.ieee802.org/1/files/public/docs2008/az-wadekar-dcbx-capability-exchange-discovery-protocol-1108-v1.01.pdf">http://www.ieee802.org/1/files/public/docs2008/az-wadekar-dcbx-capability-exchange-discovery-protocol-1108-v1.01.pdf</a>&gt;<br />
 The dcbx setting is a global setting and changes only take effect when <code>lldpad</code> is restarted. The default DCBX version used is the IEEE standard version. If a pre-IEEE DCBX version is received (per port) which matches the dcbx setting, then <code>lldpad</code> will fall back to the configured global dcbx setting. If the dcbx setting is set to either &#8216;force-cin&#8217; or &#8216;force-cee&#8217; then any port doing DCBX will start out in the corresponding legacy DCBX mode.</dl>
<p> DCB per-interface commands:</p>
<dl>
<dt><code>gc </code>&lt;<i>ifname</i>&gt; &lt;<i>feature</i>&gt;</p>
<dd>get configuration of <i>feature</i> on interface <i>ifname</i>.</p>
<dt><code>go </code>&lt;<i>ifname</i>&gt; &lt;<i>feature</i>&gt;</p>
<dd>get operational status of <i>feature</i> on interface <i>ifname</i>.</p>
<dt><code>gp </code>&lt;<i>ifname</i>&gt; &lt;<i>feature</i>&gt;</p>
<dd>get peer configuration of <i>feature</i> on interface <i>ifname</i>.</p>
<dt><code>sc </code>&lt;<i>ifname</i>&gt; &lt;<i>feature</i>&gt; &lt;<i>args</i>&gt;</p>
<dd>set the configuration of <i>feature</i> on interface <i>ifname</i>.</dl>
<p> <i>feature</i> may be one of the following:</p>
<dl>
<dt><code>dcb</code></p>
<dd>DCB state of the port</p>
<dt><code>pg</code></p>
<dd>priority groups</p>
<dt><code>pfc</code></p>
<dd>priority flow control</p>
<dt><code>app:</code>&lt;<i>subtype</i>&gt;</p>
<dd>application specific data</p>
<dt><code>ll:</code>&lt;<i>subtype</i>&gt;</p>
<dd>logical link status</dl>
<p> <i>subtype</i> can be:</p>
<dl>
<dt><code>0</code>|<code>fcoe</code></p>
<dd>Fiber Channel over Ethernet (FCoE)</p>
<dt><code>1</code>|<code>iscsi</code></p>
<dd>Internet Small Computer System Interface (iSCSI)</p>
<dt><code>2</code>|<code>fip</code></p>
<dd>FCoE Initialization Protocol (FIP)</dl>
<p> <i>args</i> can include:</p>
<dl>
<dt><code>e:</code>&lt;<code>0</code>|<code>1</code>&gt;</p>
<dd>controls feature enable</p>
<dt><code>a:</code>&lt;<code>0</code>|<code>1</code>&gt;</p>
<dd>controls whether the feature is advertised via DCBX to the peer</p>
<dt><code>w:</code>&lt;<code>0</code>|<code>1</code>&gt;</p>
<dd>controls whether the feature is willing to change its operational configuration based on what is received from the peer</p>
<dt>[<i>feature specific args</i>]</p>
<dd>arguments specific to a DCB feature </p>
</dl>
<p> Feature specific arguments for <code>dcb</code>:</p>
<dl>
<dt><code>on</code>|<code>off</code></p>
<dd>enable or disable DCB for the interface. The <code>go</code> and <code>gp</code> commands are not needed for the <code>dcb</code> feature. Also, the enable(<i>e</i>), advertise(<i>a</i>) and willing(<i>w</i>) arguments are not required. </p>
</dl>
<p> Feature specific arguments for <code>pg</code>:</p>
<dl>
<dt><code>pgid:</code><i>xxxxxxxx</i></p>
<dd>Priority group ID for the 8 priorities. From left to right (priorities 0-7), <i>x</i> is the corresponding priority group ID value, which can be <i>0-7</i> for priority groups with bandwidth allocations or <i>f</i> (priority group ID 15) for the unrestricted priority group. </p>
<dt><code>pgpct:</code><i>x</i><code>,</code><i>x</i><code>,</code><i>x</i><code>,</code><i>x</i><code>,</code><i>x</i><code>,</code><i>x</i><code>,</code><i>x</i><code>,</code><i>x</i></p>
<dd>Priority group percentage of link bandwidth. From left to right (priority groups 0-7), <i>x</i> is the percentage of link bandwidth allocated to the corresponding priority group. The total bandwidth must equal 100%. </p>
<dt><code>uppct:</code><i>x</i><code>,</code><i>x</i><code>,</code><i>x</i><code>,</code><i>x</i><code>,</code><i>x</i><code>,</code><i>x</i><code>,</code><i>x</i><code>,</code><i>x</i></p>
<dd>Priority percentage of priority group bandwidth. From left to right (priorities 0-7), <i>x</i> is the percentage of priority group bandwidth allocated to the corresponding priority. The sum of percentages for priorities which belong to the same priority group must total 100% (except for priority group 15). </p>
<dt><code>strict:</code><i>xxxxxxxx</i></p>
<dd>Strict priority setting. From left to right (priorities 0-7), <i>x</i> is <code>0</code> or <code>1</code>. <code>1</code> indicates that the priority may utilize all of the bandwidth allocated to its priority group. </p>
<dt><code>up2tc:</code><i>xxxxxxxx</i></p>
<dd>Priority to traffic class mapping. From left to right (priorities 0-7), <i>x</i> is the traffic class (0-7) to which the priority is mapped. </p>
</dl>
<p> Feature specific arguments for <code>pfc</code>:</p>
<dl>
<dt><code>pfcup:</code><i>xxxxxxxx</i></p>
<dd>Enable/disable priority flow control. From left to right (priorities 0-7), <i>x</i> is <code>0</code> or <code>1</code>. <code>1</code> indicates that the corresponding priority is configured to transmit priority pause. </p>
</dl>
<dl>
<dt>Feature specific arguments for <code>app:</code>&lt;<i>subtype</i>&gt;:</p>
<dd>The app features uses global enable and willing bits for all subtypes. To remove or add subtypes to the TLV set the advertise bit. </p>
<dt><code>appcfg:</code><i>xx</i></p>
<dd><i>xx</i> is a hexadecimal value representing an 8 bit bitmap where 1 bits indicate the priorities which frames for the applications specified by <i>subtype</i> should use. The lowest order bit maps to priority 0. </p>
</dl>
<p> Feature specific arguments for <code>ll:</code>&lt;<i>subtype</i>&gt;:</p>
<dl>
<dt><code>status:</code>[<code>0</code>|<code>1</code>]</p>
<dd>For testing purposes, the logical link status may be set to 0 or 1. Changes to the logical link status are not saved in the configuration file. </p>
</dl>
<h2>Examples</h2>
<p>Enable DCB on interface <i>eth2</i> <code>dcbtool sc eth2 dcb on</code> Assign priorities 0-3 to priority group 0, priorities 4-6 to priority group 1 and priority 7 to the unrestricted priority. Also, allocate 25% of link bandwidth to priority group 0 and 75% to group 1. <code>dcbtool sc eth2 pg pgid:0000111f pgpct:25,75,0,0,0,0,0,0</code> Enable transmit of Priority Flow Control for priority 3 and assign FCoE to priority 3. <code>dcbtool sc eth2 pfc pfcup:00010000</code><br />
 <code>dcbtool sc eth2 app:0 appcfg:08</code> </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-lldpad/">lldpad</a></code>(8), <code><a href="/docs/linux/man/8-lldptool/">lldptool</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-dcbx/">lldptool-dcbx</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-ets/">lldptool-ets</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-pfc/">lldptool-pfc</a></code>(8), <code><a href="/docs/linux/man/8-lldptool-app/">lldptool-app</a></code>(8) </p>
<h2>Copyright</h2>
<p>dcbtool &#8211; DCB configuration utility<br />
 Copyright(c) 2007-2012 Intel Corporation. Portions of dcbtool are based on:</p>
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
