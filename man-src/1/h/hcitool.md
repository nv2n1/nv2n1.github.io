---
title: "hcitool(1)"
name: "hcitool"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hcitool/"
description: "hcitool – Configure Bluetooth connections"
---

<h2 class="name">NAME</h2>
<p> hcitool &#8211; Configure Bluetooth connections </p>
<h2>SYNOPSIS</h2>
<p> <code>hcitool</code> -h </p>
<p> <code>hcitool</code> <i>COMMAND</i> &#8211;help </p>
<p> <code>hcitool</code> [-i <i>hciX</i>] [<i>COMMAND</i> [<i>PARAMETERS</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-hcitool/">hcitool</a>(1)</code> is used to configure Bluetooth connections and send some special command to Bluetooth devices. If no <code>command</code> is given, or if the option <code>-h</code> is used, <i>hcitool</i> prints some usage information and exits.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code><i>&nbsp;&lt;hciX&gt;</i></p>
<dd> The command is applied to device <i>hciX</i>, which must be the name of an installed Bluetooth device. If not specified, the command will be sent to the first available Bluetooth device.</p>
<dt><code>-h</code></p>
<dd> Gives a list of possible commands</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>dev</code></p>
<dd> Display local devices</p>
<dt><code>inq</code></p>
<dd> Inquire remote devices. For each discovered device, Bluetooth device address, clock offset and class are printed.</p>
<dt><code>scan</code></p>
<dd> Inquire remote devices. For each discovered device, device name are printed.</p>
<dt><code>name &lt;</code><i>bdaddr</i>&gt;</p>
<dd> Print device name of remote device with Bluetooth address <i>bdaddr</i>.</p>
<dt><code>info &lt;</code><i>bdaddr</i>&gt;</p>
<dd> Print device name, version and supported features of remote device with Bluetooth address <i>bdaddr</i>.</p>
<dt><code>spinq</code></p>
<dd> Start periodic inquiry process. No inquiry results are printed.</p>
<dt><code>epinq</code></p>
<dd> Exit periodic inquiry process.</p>
<dt><code>cmd &lt;</code><i>ogf</i>&gt; &lt;<i>ocf</i>&gt; [<i>parameters</i>]</p>
<dd> Submit an arbitrary HCI command to local device. <i>ogf</i>, <i>ocf</i> and parameters are hexadecimal bytes.</p>
<dt><code>con</code></p>
<dd> Display active baseband connections</p>
<dt><code>cc [&#8211;</code><i>role</i>=c|p] [&#8211;<i>pkt-type</i>=&lt;<i>ptype</i>&gt;] &lt;<i>bdaddr</i>&gt;</p>
<dd> Create baseband connection to remote device with Bluetooth address <i>bdaddr</i>. </p>
<p> Option <code>&#8211;pkt-type</code> specifies a list of allowed packet types. &lt;<i>ptype</i>&gt; is a comma-separated list of packet types, where the possible packet types are <code>DM1</code>, <code>DM3</code>, <code>DM5</code>, <code>DH1</code>, <code>DH3</code>, <code>DH5</code>, <code>HV1</code>, <code>HV2</code>, <code>HV3</code>. Default is to allow all packet types. </p>
<p> Option <code>&#8211;role</code> can have value <code>c</code> (do not allow role switch, stay central) or <code>p</code> (allow role switch, become peripheral if the peer asks to become central). Default is <code>c</code>.</p>
<dt><code>dc &lt;</code><i>bdaddr</i>&gt; [<i>reason</i>]</p>
<dd> Delete baseband connection from remote device with Bluetooth address <i>bdaddr</i>. </p>
<p> The reason can be one of the Bluetooth HCI error codes. Default is <code>19</code> for user ended connections. The value must be given in decimal.</p>
<dt><code>sr &lt;</code><i>bdaddr</i>&gt; &lt;<i>role</i>&gt;</p>
<dd> Switch role for the baseband connection from the remote device to <code>central</code> or <code>peripheral</code>.</p>
<dt><code>cpt &lt;</code><i>bdaddr</i>&gt; &lt;<i>ptypes</i>&gt;</p>
<dd> Change packet types for baseband connection to device with Bluetooth address <i>bdaddr</i>. <i>ptypes</i> is a comma-separated list of packet types, where the possible packet types are <code>DM1</code>, <code>DM3</code>, <code>DM5</code>, <code>DH1</code>, <code>DH3</code>, <code>DH5</code>, <code>HV1</code>, <code>HV2</code>, <code>HV3</code>.</p>
<dt><code>rssi &lt;</code><i>bdaddr</i>&gt;</p>
<dd> Display received signal strength information for the connection to the device with Bluetooth address <i>bdaddr</i>.</p>
<dt><code>lq &lt;</code><i>bdaddr</i>&gt;</p>
<dd> Display link quality for the connection to the device with Bluetooth address <i>bdaddr</i>.</p>
<dt><code>tpl &lt;</code><i>bdaddr</i>&gt; [<i>type</i>]</p>
<dd> Display transmit power level for the connection to the device with Bluetooth address <i>bdaddr</i>. </p>
<p> The <i>type</i> can be <code>0</code> for the current transmit power level (which is default) or <code>1</code> for the maximum transmit power level.</p>
<dt><code>afh &lt;</code><i>bdaddr</i>&gt;</p>
<dd> Display AFH channel map for the connection to the device with Bluetooth address <i>bdaddr</i>.</p>
<dt><code>lp &lt;</code><i>bdaddr</i>&gt; [<i>value</i>]</p>
<dd> With no value, displays link policy settings for the connection to the device with Bluetooth address <i>bdaddr</i>. </p>
<p> If <i>value</i> is given, sets the link policy settings for that connection to <i>value</i>. Possible values are <code>RSWITCH</code>, <code>HOLD</code>, <code>SNIFF</code> and <code>PARK</code>.</p>
<dt><code>lst &lt;</code><i>bdaddr</i>&gt; [<i>value</i>]</p>
<dd> With no value, displays link supervision timeout for the connection to the device with Bluetooth address <i>bdaddr</i>. </p>
<p> If <i>value</i> is given, sets the link supervision timeout for that connection to <i>value</i> slots, or to infinite if value is 0.</p>
<dt><code>auth &lt;</code><i>bdaddr</i>&gt;</p>
<dd> Request authentication for the device with Bluetooth address <i>bdaddr</i>.</p>
<dt><code>enc &lt;</code><i>bdaddr</i>&gt; [<i>encrypt</i>]</p>
<dd> <code>enable</code> or <code>disable</code> the encryption for the device with Bluetooth address <i>bdaddr</i>.</p>
<dt><code>key &lt;</code><i>bdaddr</i>&gt;</p>
<dd> Change the connection link key for the device with Bluetooth address <i>bdaddr</i>.</p>
<dt><code>clkoff &lt;</code><i>bdaddr</i>&gt;</p>
<dd> Read the clock offset for the device with Bluetooth address <i>bdaddr</i>.</p>
<dt><code>clock [</code><i>bdaddr</i>] [<i>clock</i>]</p>
<dd> Read the clock for the device with Bluetooth address <i>bdaddr</i>. </p>
<p> The <i>clock</i> can be <code>0</code> for the local clock or <code>1</code> for the piconet clock (which is default).</p>
<dt><code>lescan [&#8211;</code><i>privacy</i>] [&#8211;<i>passive</i>] [&#8211;<i>acceptlist</i>] [&#8211;<i>discovery</i>=g|l] [&#8211;<i>duplicates</i>]</p>
<dd> Start LE scan</p>
<dt><code>leinfo [&#8211;</code><i>static</i>] [&#8211;<i>random</i>] &lt;<i>bdaddr</i>&gt;</p>
<dd> Get LE remote information</p>
<dt><code>lealadd [&#8211;</code><i>random</i>] &lt;<i>bdaddr</i>&gt;</p>
<dd> Add device to LE Accept List</p>
<dt><code>lealrm &lt;</code><i>bdaddr</i>&gt;</p>
<dd> Remove device from LE Accept List</p>
<dt><code>lealsz</code></p>
<dd> Read size of LE Accept List</p>
<dt><code>lealclr</code></p>
<dd> Clear LE Accept List</p>
<dt><code>lerladd [&#8211;</code><i>local_irk</i>] [&#8211;<i>peer_irk</i>] [&#8211;<i>random</i>] &lt;<i>bdaddr</i>&gt;</p>
<dd> Add device to LE Resolving List</p>
<dt><code>lerlrm &lt;</code><i>bdaddr</i>&gt;</p>
<dd> Remove device from LE Resolving List</p>
<dt><code>lerlclr</code></p>
<dd> Clear LE Resolving List</p>
<dt><code>lerlsz</code></p>
<dd> Read size of LE Resolving List</p>
<dt><code>lerlon</code></p>
<dd> Enable LE Address Resolution</p>
<dt><code>lerloff</code></p>
<dd> Disable LE Address Resolution</p>
<dt><code>lecc [&#8211;</code><i>static</i>] [&#8211;<i>random</i>] &lt;<i>bdaddr</i>&gt; | [&#8211;<i>acceptlist</i>]</p>
<dd> Create a LE Connection</p>
<dt><code>ledc &lt;</code><i>handle</i>&gt; [<i>reason</i>]</p>
<dd> Disconnect a LE Connection</p>
<dt><code>lecup &lt;</code><i>handle</i>&gt; &lt;<i>min</i>&gt; &lt;<i>max</i>&gt; &lt;<i>latency</i>&gt; &lt;<i>timeout</i>&gt;</p>
<dd> LE Connection Update</dl>
<h2>RESOURCES</h2>
<p> <i><a rel="nofollow" href="http://www.bluez.org">http://www.bluez.org</a></i></p>
<h2>REPORTING BUGS</h2>
<p> <i>linux-bluetooth [at] vger.kernel.org</i></p>
<h2>AUTHOR</h2>
<p> Maxim Krasnyansky &lt;maxk [at] qualcomm.com&gt;, Marcel Holtmann &lt;marcel [at] holtmann.org&gt;, Fabrizio Gennari &lt;fabrizio.gennari [at] philips.com&gt;</p>
<h2>COPYRIGHT</h2>
<p> Free use of this software is granted under ther terms of the GNU Lesser General Public Licenses (LGPL). </p>
<h2>Index</h2>
