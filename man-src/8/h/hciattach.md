---
title: "hciattach(8)"
name: "hciattach"
section: "8"
letter: "h"
url: "/docs/linux/man/8-hciattach/"
description: "hciattach – attach serial devices via UART HCI to BlueZ stack"
---

<p>hciattach &#8211; attach serial devices via UART HCI to BlueZ stack</p>
<h2>Synopsis</h2>
<p><code>hciattach</code> [<code>-b</code>] [<code>-n</code>] [<code>-p</code>] [<code>-t</code> <i>timeout</i>] [<code>-s</code> <i>speed</i>] [<code>-l</code>] [<code>-r</code>] <i>tty</i> <i>type</i>|<i>id</i> <i>speed</i> <i>flow</i> <i>bdaddr</i></p>
<h2>Description</h2>
<p>Hciattach is used to attach a serial UART to the Bluetooth stack as HCI transport interface.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code></dt>
<dd>Send break.</dd>
<dt><code>-n</code></dt>
<dd>Don&#8217;t detach from controlling terminal.</dd>
<dt><code>-p</code></dt>
<dd>Print the PID when detaching.</dd>
<dt><code>-t</code><i> timeout</i></dt>
<dd>Specify an initialization timeout. (Default is 5 seconds.)</dd>
<dt><code>-s</code><i> speed</i></dt>
<dd>Specify an initial speed instead of the hardware default.</dd>
<dt><code>-l</code></dt>
<dd>List all available configurations.</dd>
<dt><code>-r</code></dt>
<dd>Set the HCI device into raw mode (the kernel and bluetoothd will ignore it).</dd>
<dt><i>tty</i></dt>
<dd>This specifies the serial device to attach. A leading <code>/dev</code> can be omitted. Examples: <code>/dev/ttyS1</code> <code>ttyS2</code></dd>
<dt><i>type</i>|<i>id</i></dt>
<dd>The <i>type</i> or <i>id</i> of the Bluetooth device that is to be attached, i.e. vendor or other device specific identifier. Currently supported types are</dd>
<dl>
<dd>
</dd><dl>
<dt><code>type</code></dt>
<dd><code>description</code></dd>
<dt><code>any</code></dt>
<dd>Unspecified HCI_UART interface, no vendor specific options</dd>
<dt><code>ericsson</code></dt>
<dd>Ericsson based modules</dd>
<dt><code>digi</code></dt>
<dd>Digianswer based cards</dd>
<dt><code>xircom</code></dt>
<dd>Xircom PCMCIA cards: Credit Card Adapter and Real Port Adapter</dd>
<dt><code>csr</code></dt>
<dd>CSR Casira serial adapter or BrainBoxes serial dongle (BL642)</dd>
<dt><code>bboxes</code></dt>
<dd>BrainBoxes PCMCIA card (BL620)</dd>
<dt><code>swave</code></dt>
<dd>Silicon Wave kits</dd>
<dt><code>bcsp</code></dt>
<dd>Serial adapters using CSR chips with BCSP serial protocol</dd>
<dt><code>ath3k</code></dt>
<dd>Atheros AR300x based serial Bluetooth device</dd>
<dt><code>intel</code></dt>
<dd>Intel Bluetooth device</dd></dl>
</dl>
<p> Supported IDs are (manufacturer id, product id)</p>
<dl>
<dd>
</dd><dl>
<dt><code>0x0105, 0x080a</code></dt>
<dd>Xircom PCMCIA cards: Credit Card Adapter and Real Port Adapter</dd>
<dt><code>0x0160, 0x0002</code></dt>
<dd>BrainBoxes PCMCIA card (BL620)</dd></dl>
</dl>
<dt><i>speed</i></dt>
<dd>The <i>speed</i> specifies the UART speed to use. Baudrates higher than 115.200bps require vendor specific initializations that are not implemented for all types of devices. In general the following speeds are supported: </dd>
<p> <code>9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600</code> </p>
<p> Supported vendor devices are automatically initialised to their respective best settings.</p>
<dt><i>flow</i></dt>
<dd>If the keyword <i>flow</i> is appended to the list of options then hardware flow control is forced on the serial link ( <code>CRTSCTS</code> ). All above mentioned device types have <code>flow</code> set by default. To force no flow control use <code>noflow</code> instead.</dd>
<dt><i>sleep</i></dt>
<dd>Enables hardware specific power management feature. If <i>sleep</i> is appended to the list of options then this feature is enabled. To disable this feature use <code>nosleep</code> instead. All above mentioned device types have <code>nosleep</code> set by default. </dd>
<p> Note: This option will only be valid for hardware which support hardware specific power management enable option from host.</p>
<dt><i>bdaddr</i></dt>
<dd>The <i>bdaddr</i> specifies the Bluetooth Address to use. Some devices (like the STLC2500) do not store the Bluetooth address in hardware memory. Instead it must be uploaded during the initialization process. If this argument is specified, then the address will be used to initialize the device. Otherwise, a default address will be used. </dd>
</dl>
<h2>Authors</h2>
<p>Written by Maxim Krasnyansky &lt;maxk [at] qualcomm.com&gt; </p>
<p> Manual page by Nils Faerber &lt;nils [at] kernelconcepts.de&gt;</p>
