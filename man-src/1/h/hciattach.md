---
title: "hciattach(1)"
name: "hciattach"
section: "1"
letter: "h"
url: "/docs/linux/man/1-hciattach/"
description: "hciattach – attach serial devices via UART HCI to BlueZ stack"
---

<h2 class="name">NAME</h2>
<p> hciattach &#8211; attach serial devices via UART HCI to BlueZ stack </p>
<h2>SYNOPSIS</h2>
<p> <code>hciattach</code> [<i>OPTIONS</i>] &lt;<i>tty</i>&gt; &lt;<i>type|id</i>&gt; [<i>speed</i>] [<i>flow</i>] [<i>sleep</i>] [<i>bdaddr</i>] </p>
<p> <code>hciattach</code> -1</p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-hciattach/">hciattach</a>(1)</code> is used to attach a serial UART to the Bluetooth stack as HCI transport interface.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code></p>
<dd> Send break</p>
<dt><code>-n</code></p>
<dd> Don&#8217;t detach from controlling terminal.</p>
<dt><code>-p</code></p>
<dd> Print the PID when detaching.</p>
<dt><code>-t</code><i>&nbsp;timeout</i></p>
<dd> Specify an initialization timeout. Default is 5 seconds.</p>
<dt><code>-s</code><i>&nbsp;speed</i></p>
<dd> Specify an initial speed instead of the hardware default.</p>
<dt><code>-l</code></p>
<dd> List all available configurations.</p>
<dt><code>-r</code></p>
<dd> Set the HCI device into raw mode. The kernel and bluetooth daemon will ignore it.</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Show help options</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>show</i></p>
<dd> This specifies the serial device to attach. A leading /dev can be omitted. </p>
<p> Examples: <code>/dev/ttyS1 ttyS2</code></p>
<dt><i>type|id</i></p>
<dd> The <i>type</i> or <i>id</i> of the Bluetooth device that is to be attached, i.e. vendor or other device specific identifier. Currently supported types are <center></p>
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
<td> any </td>
<td> Unspecified HCI_UART interface, no vendor specific options
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> ericsson </td>
<td> Ericsson based modules
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> digi </td>
<td> Digianswer based cards
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> xircom </td>
<td> Xircom PCMCIA cards: Credit Card Adapter and Real Port Adapter
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> csr </td>
<td> CSR Casira serial adapter or BrainBoxes serial dongle (BL642)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> bboxes </td>
<td> BrainBoxes PCMCIA card (BL620)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> swave </td>
<td> Silicon Wave kits
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> bcsp </td>
<td> Serial adapters using CSR chips with BCSP serial protocol
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> ath3k </td>
<td> Atheros AR300x based serial Bluetooth device
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> intel </td>
<td> Intel Bluetooth device
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center> <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>
<pre>
Supported ID
(manufacturer id, product id)
</pre>
</td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 0x0105, 0x080a </td>
<td> Xircom PCMCIA cards: Credit Card Adapter and Real Port Adapter
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 0x0160, 0x0002 </td>
<td> BrainBoxes PCMCIA card (BL620)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><i>speed</i></p>
<dd> The <i>speed</i> specifies the UART speed to use. Baudrates higher than 115200bps require vendor specific initializations that are not implemented for all types of devices. In general the following speeds are supported: </p>
<p> Supported vendor devices are automatically initialised to their respective best settings. <center></p>
<table>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 9600
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 19200
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 38400
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 57600
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 115200
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 230400
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 460800
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> 921600
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
</tr>
</table>
<p></center></p>
<dt><i>flow</i></p>
<dd> If the <i>flow</i> is appended to the list of options then hardware flow control is forced on the serial link (<code>CRTSCTS</code>). All above mentioned device types have flow set by default. To force no flow control use <i>noflow</i> instead.</p>
<dt><i>sleep|nosleep</i></p>
<dd> Enables hardware specific power management feature. If <i>sleep</i> is appended to the list of options then this feature is enabled. To disable this feature use <i>nosleep</i> instead. All above mentioned device types have <i>nosleep</i> set by default. </p>
<p> Note: This option will only be valid for hardware which support hardware specific power management enable option from host.</p>
<dt><i>bdaddr</i></p>
<dd> The bdaddr specifies the Bluetooth Address to use. Some devices (like the STLC2500) do not store the Bluetooth address in hardware memory. Instead it must be uploaded during the initialization process. If this argument is specified, then the address will be used to initialize the device. Otherwise, a default address will be used.</dl>
<h2>RESOURCES</h2>
<p> <i><a rel="nofollow" href="http://www.bluez.org">http://www.bluez.org</a></i></p>
<h2>REPORTING BUGS</h2>
<p> <i>linux-bluetooth [at] vger.kernel.org</i></p>
<h2>AUTHOR</h2>
<p> Maxim Krasnyansky &lt;maxk [at] qualcomm.com&gt;, Nils Faerber &lt;nils [at] kernelconcepts.de&gt;</p>
<h2>COPYRIGHT</h2>
<p> Free use of this software is granted under ther terms of the GNU Lesser General Public Licenses (LGPL). </p>
<h2>Index</h2>
