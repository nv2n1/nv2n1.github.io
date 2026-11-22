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
<p><code>hciconfig</code> <code>-h</code><br/>
 <code>hciconfig</code> [<code>-a</code>]<br/>
 <code>hciconfig</code> [<code>-a</code>] <code>hciX</code> [<i>command</i> [<i>command parameters</i>]] </p>
<h2>Description</h2>
<p><code>hciconfig</code> is used to configure Bluetooth devices. <i>hciX</i> is the name of a Bluetooth device installed in the system. If <i>hciX</i> is not given, <code>hciconfig</code> prints name and basic information about all the Bluetooth devices installed in the system. If <i>hciX</i> is given but no command is given, it prints basic information on device <i>hciX</i> only. Basic information is interface type, BD address, ACL MTU, SCO MTU, flags (up, init, running, raw, page scan enabled, inquiry scan enabled, inquiry, authentication enabled, encryption enabled).</p>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Gives a list of possible commands.</dd>
<dt><code>-a, &#8211;all</code></dt>
<dd>Other than the basic info, print features, packet type, link policy, link mode, name, class, version.</dd></dl>
<h2>Commands</h2>
<dl>
<dt><code>up</code></dt>
<dd>Open and initialize HCI device.</dd>
<dt><code>down</code></dt>
<dd>Close HCI device.</dd>
<dt><code>reset</code></dt>
<dd>Reset HCI device.</dd>
<dt><code>rstat</code></dt>
<dd>Reset statistic counters.</dd>
<dt><code>auth</code></dt>
<dd>Enable authentication (sets device to security mode 3).</dd>
<dt><code>noauth</code></dt>
<dd>Disable authentication.</dd>
<dt><code>encrypt</code></dt>
<dd>Enable encryption (sets device to security mode 3).</dd>
<dt><code>noencrypt</code></dt>
<dd>Disable encryption.</dd>
<dt><code>secmgr</code></dt>
<dd>Enable security manager (current kernel support is limited).</dd>
<dt><code>nosecmgr</code></dt>
<dd>Disable security manager.</dd>
<dt><code>piscan</code></dt>
<dd>Enable page and inquiry scan.</dd>
<dt><code>noscan</code></dt>
<dd>Disable page and inquiry scan.</dd>
<dt><code>iscan</code></dt>
<dd>Enable inquiry scan, disable page scan.</dd>
<dt><code>pscan</code></dt>
<dd>Enable page scan, disable inquiry scan.</dd>
<dt><code>ptype</code> [<i>type</i>]</dt>
<dd>With no <i>type</i> , displays the current packet types. Otherwise, all the packet types specified by <i>type</i> are set. <i>type</i> is a comma-separated list of packet types, where the possible packet types are <code>DM1</code>, <code>DM3</code>, <code>DM5</code>, <code>DH1</code>, <code>DH3</code>, <code>DH5</code>, <code>HV1</code>, <code>HV2</code>, <code>HV3</code>.</dd>
<dt><code>name</code><i> [name]</i></dt>
<dd>With no <i>name</i>, prints local name. Otherwise, sets local name to <i>name</i>.</dd>
<dt><code>class</code><i> [class]</i></dt>
<dd>With no <i>class</i>, prints class of device. Otherwise, sets class of device to <i>class</i>. <i>class</i> is a 24-bit hex number describing the class of device, as specified in section 1.2 of the Bluetooth Assigned Numers document.</dd>
<dt><code>voice</code><i> [voice]</i></dt>
<dd>With no <i>voice</i>, prints voice setting. Otherwise, sets voice setting to <i>voice</i>. <i>voice</i> is a 16-bit hex number describing the voice setting.</dd>
<dt><code>iac</code><i> [iac]</i></dt>
<dd>With no <i>iac</i>, prints the current IAC setting. Otherwise, sets the IAC to <i>iac</i>.</dd>
<dt><code>inqtpl</code><i> [level]</i></dt>
<dd>With no <i>level</i>, prints out the current inquiry transmit power level. Otherwise, sets inquiry transmit power level to <i>level</i>.</dd>
<dt><code>inqmode</code><i> [mode]</i></dt>
<dd>With no <i>mode</i>, prints out the current inquiry mode. Otherwise, sets inquiry mode to <i>mode</i>.</dd>
<dt><code>inqdata</code><i> [data]</i></dt>
<dd>With no <i>name</i>, prints out the current inquiry data. Otherwise, sets inquiry data to <i>data</i>.</dd>
<dt><code>inqtype</code><i> [type]</i></dt>
<dd>With no <i>type</i>, prints out the current inquiry scan type. Otherwise, sets inquiry scan type to <i>type</i>.</dd>
<dt><code>inqparams</code> [<i>win</i>:<i>int</i>]</dt>
<dd>With no <i>win</i>:<i>int</i>, prints inquiry scan window and interval. Otherwise, sets inquiry scan window to <i>win</i> slots and inquiry scan interval to <i>int</i> slots.</dd>
<dt><code>pageparms</code> [<i>win</i>:<i>int</i>]</dt>
<dd>With no <i>win</i>:<i>int</i>, prints page scan window and interval. Otherwise, sets page scan window to <i>win</i> slots and page scan interval to <i>int</i> slots.</dd>
<dt><code>pageto</code><i> [to]</i></dt>
<dd>With no <i>to</i>, prints page timeout. Otherwise, sets page timeout to .I to slots.</dd>
<dt><code>afhmode</code><i> [mode]</i></dt>
<dd>With no <i>mode</i>, prints out the current AFH mode. Otherwise, sets AFH mode to <i>mode</i>.</dd>
<dt><code>sspmode</code><i> [mode]</i></dt>
<dd>With no <i>mode</i>, prints out the current Simple Pairing mode. Otherwise, sets Simple Pairing mode to <i>mode</i>.</dd>
<dt><code>aclmtu</code> <i>mtu</i>:<i>pkt</i></dt>
<dd>Sets ACL MTU to to <i>mtu</i> bytes and ACL buffer size to <i>pkt</i> packets.</dd>
<dt><code>scomtu</code> <i>mtu</i>:<i>pkt</i></dt>
<dd>Sets SCO MTU to <i>mtu</i> bytes and SCO buffer size to <i>pkt</i> packets.</dd>
<dt><code>putkey</code><i> &lt;bdaddr&gt;</i></dt>
<dd>This command stores the link key for <i>bdaddr</i> on the device.</dd>
<dt><code>delkey</code><i> &lt;bdaddr&gt;</i></dt>
<dd>This command deletes the stored link key for <i>bdaddr</i> from the device.</dd>
<dt><code>oobdata</code></dt>
<dd>Display local OOB data.</dd>
<dt><code>commands</code></dt>
<dd>Display supported commands.</dd>
<dt><code>features</code></dt>
<dd>Display device features.</dd>
<dt><code>version</code></dt>
<dd>Display version information.</dd>
<dt><code>revision</code></dt>
<dd>Display revision information.</dd>
<dt><code>lm</code><i> [mode]</i></dt>
<dd>With no <i>mode</i> , prints link mode. <code>MASTER</code> or <code>SLAVE</code> mean, respectively, to ask to become master or to remain slave when a connection request comes in. The additional keyword <code>ACCEPT</code> means that baseband connections will be accepted even if there are no listening <i>AF_BLUETOOTH</i> sockets. <i>mode</i> is <code>NONE</code> or a comma-separated list of keywords, where possible keywords are <code>MASTER</code> and <code>ACCEPT .</code> <code>NONE</code> sets link policy to the default behaviour of remaining slave and not accepting baseband connections when there are no listening <i>AF_BLUETOOTH</i> sockets. If <code>MASTER</code> is present, the device will ask to become master if a connection request comes in. If <code>ACCEPT</code> is present, the device will accept baseband connections even when there are no listening <i>AF_BLUETOOTH</i> sockets.</dd></dl>
<h2>Authors</h2>
<p>Written by Maxim Krasnyansky &lt;maxk [at] qualcomm.com&gt; and Marcel Holtmann &lt;marcel [at] holtmann.org&gt; </p>
<p> man page by Fabrizio Gennari &lt;fabrizio.gennari [at] philips.com&gt;</p>
