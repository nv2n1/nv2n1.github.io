---
title: "ciptool(1)"
name: "ciptool"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ciptool/"
description: "ciptool – Bluetooth Common ISDN Access Profile (CIP)"
---

<h2 class="name">NAME</h2>
<p> ciptool &#8211; Bluetooth Common ISDN Access Profile (CIP) </p>
<h2>SYNOPSIS</h2>
<p> <code>ciptool</code> [<i>OPTIONS</i>] <i>COMMANDS</i></p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-ciptool/">ciptool</a>(1)</code> is used to set up, maintain, and inspect the CIP configuration of the Bluetooth subsystem in the Linux kernel.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code><i>&nbsp;&lt;hciX|BDADDR&gt;</i></p>
<dd> The command is applied to device <i>hciX</i> , which must be the name or the address of an installed Bluetooth device. </p>
<p> If not specified, the command will be use the first available Bluetooth device.</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Show help options</dl>
<h2>COMMANDS</h2>
<dl>
<dt><code>show</code></p>
<dd> Display information about the connected devices.</p>
<dt><code>search</code></p>
<dd> Search for Bluetooth devices and connect to first one that offers CIP support.</p>
<dt><code>connect &lt;</code><i>BDADDR</i>&gt; [<i>PSM</i>]</p>
<dd> Connect the local device to the remote Bluetooth device on the specified <i>PSM</i> number. If no <i>PSM</i> is specified, it will use the SDP to retrieve it from the remote device.</p>
<dt><code>release [</code><i>BDADDR</i>]</p>
<dd> Release a connection to the specific device. If no <i>BDADDR</i> is given and only one device is connected this will be released.</p>
<dt><code>loopback &lt;</code><i>BDADDR</i>&gt; [<i>PSM</i>]</p>
<dd> Create a connection to the remote device for Bluetooth testing. This command will not provide a CAPI controller, because it is only for testing the CAPI Message Transport Protocol.</dl>
<h2>RESOURCES</h2>
<p> <i><a rel="nofollow" href="http://www.bluez.org">http://www.bluez.org</a></i></p>
<h2>REPORTING BUGS</h2>
<p> <i>linux-bluetooth [at] vger.kernel.org</i></p>
<h2>AUTHOR</h2>
<p> Marcel Holtmann &lt;marcel [at] holtmann.org&gt;</p>
<h2>COPYRIGHT</h2>
<p> Free use of this software is granted under ther terms of the GNU Lesser General Public Licenses (LGPL). </p>
<h2>Index</h2>
