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
<dt><code>-b</code></p>
<dd>Send break.</p>
<dt><code>-n</code></p>
<dd>Don&#8217;t detach from controlling terminal.</p>
<dt><code>-p</code></p>
<dd>Print the PID when detaching.</p>
<dt><code>-t</code><i> timeout</i></p>
<dd>Specify an initialization timeout. (Default is 5 seconds.)</p>
<dt><code>-s</code><i> speed</i></p>
<dd>Specify an initial speed instead of the hardware default.</p>
<dt><code>-l</code></p>
<dd>List all available configurations.</p>
<dt><code>-r</code></p>
<dd>Set the HCI device into raw mode (the kernel and bluetoothd will ignore it).</p>
<dt><i>tty</i></p>
<dd>This specifies the serial device to attach. A leading <code>/dev</code> can be omitted. Examples: <code>/dev/ttyS1</code> <code>ttyS2</code></p>
<dt><i>type</i>|<i>id</i></p>
<dd>The <i>type</i> or <i>id</i> of the Bluetooth device that is to be attached, i.e. vendor or other device specific identifier. Currently supported types are</p>
<dl>
<dd>
<dl>
<dt><code>type</code></p>
<dd><code>description</code></p>
<dt><code>any</code></p>
<dd>Unspecified HCI_UART interface, no vendor specific options</p>
<dt><code>ericsson</code></p>
<dd>Ericsson based modules</p>
<dt><code>digi</code></p>
<dd>Digianswer based cards</p>
<dt><code>xircom</code></p>
<dd>Xircom PCMCIA cards: Credit Card Adapter and Real Port Adapter</p>
<dt><code>csr</code></p>
<dd>CSR Casira serial adapter or BrainBoxes serial dongle (BL642)</p>
<dt><code>bboxes</code></p>
<dd>BrainBoxes PCMCIA card (BL620)</p>
<dt><code>swave</code></p>
<dd>Silicon Wave kits</p>
<dt><code>bcsp</code></p>
<dd>Serial adapters using CSR chips with BCSP serial protocol</p>
<dt><code>ath3k</code></p>
<dd>Atheros AR300x based serial Bluetooth device</p>
<dt><code>intel</code></p>
<dd>Intel Bluetooth device</dl>
</dl>
<p> Supported IDs are (manufacturer id, product id)</p>
<dl>
<dd>
<dl>
<dt><code>0x0105, 0x080a</code></p>
<dd>Xircom PCMCIA cards: Credit Card Adapter and Real Port Adapter</p>
<dt><code>0x0160, 0x0002</code></p>
<dd>BrainBoxes PCMCIA card (BL620)</dl>
</dl>
<dt><i>speed</i></p>
<dd>The <i>speed</i> specifies the UART speed to use. Baudrates higher than 115.200bps require vendor specific initializations that are not implemented for all types of devices. In general the following speeds are supported: </p>
<p> <code>9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600</code> </p>
<p> Supported vendor devices are automatically initialised to their respective best settings.</p>
<dt><i>flow</i></p>
<dd>If the keyword <i>flow</i> is appended to the list of options then hardware flow control is forced on the serial link ( <code>CRTSCTS</code> ). All above mentioned device types have <code>flow</code> set by default. To force no flow control use <code>noflow</code> instead.</p>
<dt><i>sleep</i></p>
<dd>Enables hardware specific power management feature. If <i>sleep</i> is appended to the list of options then this feature is enabled. To disable this feature use <code>nosleep</code> instead. All above mentioned device types have <code>nosleep</code> set by default. </p>
<p> Note: This option will only be valid for hardware which support hardware specific power management enable option from host.</p>
<dt><i>bdaddr</i></p>
<dd>The <i>bdaddr</i> specifies the Bluetooth Address to use. Some devices (like the STLC2500) do not store the Bluetooth address in hardware memory. Instead it must be uploaded during the initialization process. If this argument is specified, then the address will be used to initialize the device. Otherwise, a default address will be used. </p>
</dl>
<h2>Authors</h2>
<p>Written by Maxim Krasnyansky &lt;maxk [at] qualcomm.com&gt; </p>
<p> Manual page by Nils Faerber &lt;nils [at] kernelconcepts.de&gt;</p>
