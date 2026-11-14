---
title: "hciconfig(8)"
name: "hciconfig"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hciconfig/"
description: "hciconfig – configure Bluetooth devices"
---

<p>hciconfig &#8211; configure Bluetooth devices</p>
<h2>Synopsis</h2>
<p><code>hciconfig</code> <code>-h</code><br />
 <code>hciconfig</code> [<code>-a</code>]<br />
 <code>hciconfig</code> [<code>-a</code>] <code>hciX</code> [<i>command</i> [<i>command parameters</i>]] </p>
<h2>Description</h2>
<p><code>hciconfig</code> is used to configure Bluetooth devices. <i>hciX</i> is the name of a Bluetooth device installed in the system. If <i>hciX</i> is not given, <code>hciconfig</code> prints name and basic information about all the Bluetooth devices installed in the system. If <i>hciX</i> is given but no command is given, it prints basic information on device <i>hciX</i> only. Basic information is interface type, BD address, ACL MTU, SCO MTU, flags (up, init, running, raw, page scan enabled, inquiry scan enabled, inquiry, authentication enabled, encryption enabled).</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd>Gives a list of possible commands.</p>
<dt><code>-a, &#8211;all</code></p>
<dd>Other than the basic info, print features, packet type, link policy, link mode, name, class, version.</dl>
<h2>Commands</h2>
<dl>
<dt><code>up</code></p>
<dd>Open and initialize HCI device.</p>
<dt><code>down</code></p>
<dd>Close HCI device.</p>
<dt><code>reset</code></p>
<dd>Reset HCI device.</p>
<dt><code>rstat</code></p>
<dd>Reset statistic counters.</p>
<dt><code>auth</code></p>
<dd>Enable authentication (sets device to security mode 3).</p>
<dt><code>noauth</code></p>
<dd>Disable authentication.</p>
<dt><code>encrypt</code></p>
<dd>Enable encryption (sets device to security mode 3).</p>
<dt><code>noencrypt</code></p>
<dd>Disable encryption.</p>
<dt><code>secmgr</code></p>
<dd>Enable security manager (current kernel support is limited).</p>
<dt><code>nosecmgr</code></p>
<dd>Disable security manager.</p>
<dt><code>piscan</code></p>
<dd>Enable page and inquiry scan.</p>
<dt><code>noscan</code></p>
<dd>Disable page and inquiry scan.</p>
<dt><code>iscan</code></p>
<dd>Enable inquiry scan, disable page scan.</p>
<dt><code>pscan</code></p>
<dd>Enable page scan, disable inquiry scan.</p>
<dt><code>ptype</code> [<i>type</i>]</p>
<dd>With no <i>type</i> , displays the current packet types. Otherwise, all the packet types specified by <i>type</i> are set. <i>type</i> is a comma-separated list of packet types, where the possible packet types are <code>DM1</code>, <code>DM3</code>, <code>DM5</code>, <code>DH1</code>, <code>DH3</code>, <code>DH5</code>, <code>HV1</code>, <code>HV2</code>, <code>HV3</code>.</p>
<dt><code>name</code><i> [name]</i></p>
<dd>With no <i>name</i>, prints local name. Otherwise, sets local name to <i>name</i>.</p>
<dt><code>class</code><i> [class]</i></p>
<dd>With no <i>class</i>, prints class of device. Otherwise, sets class of device to <i>class</i>. <i>class</i> is a 24-bit hex number describing the class of device, as specified in section 1.2 of the Bluetooth Assigned Numers document.</p>
<dt><code>voice</code><i> [voice]</i></p>
<dd>With no <i>voice</i>, prints voice setting. Otherwise, sets voice setting to <i>voice</i>. <i>voice</i> is a 16-bit hex number describing the voice setting.</p>
<dt><code>iac</code><i> [iac]</i></p>
<dd>With no <i>iac</i>, prints the current IAC setting. Otherwise, sets the IAC to <i>iac</i>.</p>
<dt><code>inqtpl</code><i> [level]</i></p>
<dd>With no <i>level</i>, prints out the current inquiry transmit power level. Otherwise, sets inquiry transmit power level to <i>level</i>.</p>
<dt><code>inqmode</code><i> [mode]</i></p>
<dd>With no <i>mode</i>, prints out the current inquiry mode. Otherwise, sets inquiry mode to <i>mode</i>.</p>
<dt><code>inqdata</code><i> [data]</i></p>
<dd>With no <i>name</i>, prints out the current inquiry data. Otherwise, sets inquiry data to <i>data</i>.</p>
<dt><code>inqtype</code><i> [type]</i></p>
<dd>With no <i>type</i>, prints out the current inquiry scan type. Otherwise, sets inquiry scan type to <i>type</i>.</p>
<dt><code>inqparams</code> [<i>win</i>:<i>int</i>]</p>
<dd>With no <i>win</i>:<i>int</i>, prints inquiry scan window and interval. Otherwise, sets inquiry scan window to <i>win</i> slots and inquiry scan interval to <i>int</i> slots.</p>
<dt><code>pageparms</code> [<i>win</i>:<i>int</i>]</p>
<dd>With no <i>win</i>:<i>int</i>, prints page scan window and interval. Otherwise, sets page scan window to <i>win</i> slots and page scan interval to <i>int</i> slots.</p>
<dt><code>pageto</code><i> [to]</i></p>
<dd>With no <i>to</i>, prints page timeout. Otherwise, sets page timeout to .I to slots.</p>
<dt><code>afhmode</code><i> [mode]</i></p>
<dd>With no <i>mode</i>, prints out the current AFH mode. Otherwise, sets AFH mode to <i>mode</i>.</p>
<dt><code>sspmode</code><i> [mode]</i></p>
<dd>With no <i>mode</i>, prints out the current Simple Pairing mode. Otherwise, sets Simple Pairing mode to <i>mode</i>.</p>
<dt><code>aclmtu</code> <i>mtu</i>:<i>pkt</i></p>
<dd>Sets ACL MTU to to <i>mtu</i> bytes and ACL buffer size to <i>pkt</i> packets.</p>
<dt><code>scomtu</code> <i>mtu</i>:<i>pkt</i></p>
<dd>Sets SCO MTU to <i>mtu</i> bytes and SCO buffer size to <i>pkt</i> packets.</p>
<dt><code>putkey</code><i> &lt;bdaddr&gt;</i></p>
<dd>This command stores the link key for <i>bdaddr</i> on the device.</p>
<dt><code>delkey</code><i> &lt;bdaddr&gt;</i></p>
<dd>This command deletes the stored link key for <i>bdaddr</i> from the device.</p>
<dt><code>oobdata</code></p>
<dd>Display local OOB data.</p>
<dt><code>commands</code></p>
<dd>Display supported commands.</p>
<dt><code>features</code></p>
<dd>Display device features.</p>
<dt><code>version</code></p>
<dd>Display version information.</p>
<dt><code>revision</code></p>
<dd>Display revision information.</p>
<dt><code>lm</code><i> [mode]</i></p>
<dd>With no <i>mode</i> , prints link mode. <code>MASTER</code> or <code>SLAVE</code> mean, respectively, to ask to become master or to remain slave when a connection request comes in. The additional keyword <code>ACCEPT</code> means that baseband connections will be accepted even if there are no listening <i>AF_BLUETOOTH</i> sockets. <i>mode</i> is <code>NONE</code> or a comma-separated list of keywords, where possible keywords are <code>MASTER</code> and <code>ACCEPT .</code> <code>NONE</code> sets link policy to the default behaviour of remaining slave and not accepting baseband connections when there are no listening <i>AF_BLUETOOTH</i> sockets. If <code>MASTER</code> is present, the device will ask to become master if a connection request comes in. If <code>ACCEPT</code> is present, the device will accept baseband connections even when there are no listening <i>AF_BLUETOOTH</i> sockets.</dl>
<h2>Authors</h2>
<p>Written by Maxim Krasnyansky &lt;maxk [at] qualcomm.com&gt; and Marcel Holtmann &lt;marcel [at] holtmann.org&gt; </p>
<p> man page by Fabrizio Gennari &lt;fabrizio.gennari [at] philips.com&gt;</p>
