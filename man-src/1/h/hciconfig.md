---
title: "hciconfig(1)"
name: "hciconfig"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hciconfig/"
description: "hciconfig – Configure Bluetooth devices"
---

<h2 class="name">NAME</h2>
<p> hciconfig &#8211; Configure Bluetooth devices </p>
<h2>SYNOPSIS</h2>
<p> <code>hciconfig</code> -h </p>
<p> <code>hciconfig</code> [-a] </p>
<p> <code>hciconfig</code> [-a] <i>hciX</i> [<i>COMMAND</i> [<i>PARAMETERS</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-hciconfig/">hciconfig</a>(1)</code> is used to configure Bluetooth devices. <i>hciX</i> is the name of a Bluetooth device installed in the system. If hciX is not given, hciconfig prints name and basic information about all the Bluetooth devices installed in the system. </p>
<p> If <i>hciX</i> is given but no command is given, it prints basic information on device <i>hciX</i> only. Basic information is interface type, BD address, ACL MTU, SCO MTU, flags (up, init, running, raw, page scan enabled, inquiry scan enabled, inquiry, authentication enabled, encryption enabled).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code>,<code> &#8211;all</code></p>
<dd> Print features, packet type, link policy, link mode, class, Version other than the basic info.</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Show help options</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>up</code></p>
<dd> Open and initialize HCI device.</p>
<dt><code>down</code></p>
<dd> Close HCI device.</p>
<dt><code>reset</code></p>
<dd> Reset HCI device.</p>
<dt><code>rstat</code></p>
<dd> Reset statistic counters.</p>
<dt><code>auth</code></p>
<dd> Enable authentication (sets device to security mode 3).</p>
<dt><code>noauth</code></p>
<dd> Disable authentication.</p>
<dt><code>encrypt</code></p>
<dd> Enable encryption (sets device to security mode 3).</p>
<dt><code>noencrypt</code></p>
<dd> Disable encryption.</p>
<dt><code>secmgr</code></p>
<dd> Enable security manager (current kernel support is limited).</p>
<dt><code>nosecmgr</code></p>
<dd> Disable security manager.</p>
<dt><code>piscan</code></p>
<dd> Enable page and inquiry scan.</p>
<dt><code>noscan</code></p>
<dd> Disable page and inquiry scan.</p>
<dt><code>iscan</code></p>
<dd> Enable inquiry scan, disable page scan.</p>
<dt><code>pscan</code></p>
<dd> Enable page scan, disable inquiry scan.</p>
<dt><code>ptype [</code><i>type</i>]</p>
<dd> With no <i>type</i> , displays the current packet types. Otherwise, all the packet types specified by <i>type</i> are set. <i>type</i> is a comma-separated list of packet types, where the possible packet types are <code>DM1</code>, <code>DM3</code>, <code>DM5</code>, <code>DH1</code>, <code>DH3</code>, <code>DH5</code>, <code>HV1</code>, <code>HV2</code>, <code>HV3</code>.</p>
<dt><code>name [</code><i>name</i>]</p>
<dd> With no <i>name</i>, prints local name. Otherwise, sets local name to <i>name</i>.</p>
<dt><code>class [</code><i>class</i>]</p>
<dd> With no <i>class</i>, prints class of device. Otherwise, sets class of device to <i>class</i>. <i>class</i> is a 24-bit hex number describing the class of device, as specified in section 1.2 of the Bluetooth Assigned Numers document.</p>
<dt><code>voice [</code><i>voice</i>]</p>
<dd> With no <i>voice</i>, prints voice setting. Otherwise, sets voice setting to <i>voice</i>. <i>voice</i> is a 16-bit hex number describing the voice setting.</p>
<dt><code>iac [</code><i>iac</i>]</p>
<dd> With no <i>iac</i>, prints the current IAC setting. Otherwise, sets the IAC to <i>iac</i>.</p>
<dt><code>inqtpl [</code><i>level</i>]</p>
<dd> With no <i>level</i>, prints out the current inquiry transmit power level. Otherwise, sets inquiry transmit power level to <i>level</i>.</p>
<dt><code>inqmode [</code><i>mode</i>]</p>
<dd> With no <i>mode</i>, prints out the current inquiry mode. Otherwise, sets inquiry mode to <i>mode</i>. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>mode</i> </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 0 </td>
<td> Standard Inquiry
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 1 </td>
<td> Inquiry with RSSI
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 2 </td>
<td> Inquiry with RSSI or Extended Inquiry
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>inqdata [</code><i>data</i>]</p>
<dd> With no <i>data</i>, prints out the current inquiry data. Otherwise, sets inquiry data to <i>data</i>.</p>
<dt><code>inqtype [</code><i>type</i>]</p>
<dd> With no <i>type</i>, prints out the current inquiry scan type. Otherwise, sets inquiry scan type to <i>type</i>.</p>
<dt><code>inqparams [</code><i>win:int</i>]</p>
<dd> With no <i>win:int</i>, prints inquiry scan window and interval. Otherwise, sets inquiry scan window to <i>win</i> slots and inquiry scan interval to <i>int</i> slots.</p>
<dt><code>pageparms [</code><i>win:int</i>]</p>
<dd> With no <i>win:int</i>, prints page scan window and interval. Otherwise, sets page scan window to <i>win</i> slots and page scan interval to <i>int</i> slots.</p>
<dt><code>pageto [</code><i>to</i>]</p>
<dd> With no <i>to</i>, prints page timeout. Otherwise, sets page timeout <i>to</i> to slots.</p>
<dt><code>afhmode [</code><i>mode</i>]</p>
<dd> With no <i>mode</i>, prints out the current AFH mode. Otherwise, sets AFH mode to <i>mode</i>. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>mode</i> </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 0 </td>
<td> Enable
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 1 </td>
<td> Disable
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>sspmode [</code><i>mode</i>]</p>
<dd> With no <i>mode</i>, prints out the current Simple Pairing mode. Otherwise, sets Simple Pairing mode to <i>mode</i>. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>mode</i> </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 0 </td>
<td> Enable
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 1 </td>
<td> Disable
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>aclmtu </code><i>mtu:pkt</i></p>
<dd> Sets ACL MTU to <i>mtu</i> bytes and ACL buffer size to <i>pkt</i> packets.</p>
<dt><code>scomtu </code><i>mtu:pkt</i></p>
<dd> Sets SCO MTU to <i>mtu</i> bytes and SCO buffer size to <i>pkt</i> packets.</p>
<dt><code>delkey &lt;</code><i>bdaddr</i>&gt;</p>
<dd> This command deletes the stored link key for <i>bdaddr</i> from the device.</p>
<dt><code>oobdata</code></p>
<dd> Get local OOB data (invalidates previously read data).</p>
<dt><code>commands</code></p>
<dd> Display supported commands.</p>
<dt><code>features</code></p>
<dd> Display device features.</p>
<dt><code>version</code></p>
<dd> Display version information.</p>
<dt><code>revision</code></p>
<dd> Display revision information.</p>
<dt><code>lm [</code><i>mode</i>]</p>
<dd> With no <i>mode</i>, prints link mode. <code>CENTRAL</code> or <code>PERIPHERAL</code> mean, respectively, to ask to become central or to remain peripheral when a connection request comes in. The additional keyword <code>ACCEPT</code> means that baseband connections will be accepted even if there are no listening <i>AF_BLUETOOTH</i> sockets. <i>mode</i> is <code>NONE</code> or a comma-separated list of keywords, where possible keywords are <code>CENTRAL</code> and <code>ACCEPT</code>. <code>NONE</code> sets link policy to the default behaviour of remaining peripheral and not accepting baseband connections when there are no listening <i>AF_BLUETOOTH</i> sockets. If <code>CENTRAL</code> is present, the device will ask to become central if a connection request comes in. If <code>ACCEPT</code> is present, the device will accept baseband connections even when there are no listening <i>AF_BLUETOOTH</i> sockets.</p>
<dt><code>block &lt;</code><i>bdaddr</i>&gt;</p>
<dd> Add a device to the reject list</p>
<dt><code>unblock &lt;</code><i>bdaddr</i>&gt;</p>
<dd> Remove a device from the reject list</p>
<dt><code>lerandaddr &lt;</code><i>bdaddr</i>&gt;</p>
<dd> Set LE Random Address</p>
<dt><code>leadv [</code><i>type</i>]</p>
<dd> Enable LE Advertising. <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> <i>type</i> </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 0 </td>
<td> Connectable undirected advertising (default)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 3 </td>
<td> Non connectable undirected advertising
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><code>noleadv</code></p>
<dd> Disable LE Advertising</p>
<dt><code>lestates</code></p>
<dd> Display the supported LE states</dl>
<h2>RESOURCES</h2>
<p> <i><a rel="nofollow" href="http://www.bluez.org">http://www.bluez.org</a></i></p>
<h2>REPORTING BUGS</h2>
<p> <i>linux-bluetooth [at] vger.kernel.org</i></p>
<h2>AUTHOR</h2>
<p> Maxim Krasnyansky &lt;maxk [at] qualcomm.com&gt;, Marcel Holtmann &lt;marcel [at] holtmann.org&gt;, Fabrizio Gennari &lt;fabrizio.gennari [at] philips.com&gt;</p>
<h2>COPYRIGHT</h2>
<p> Free use of this software is granted under ther terms of the GNU Lesser General Public Licenses (LGPL). </p>
<h2>Index</h2>
