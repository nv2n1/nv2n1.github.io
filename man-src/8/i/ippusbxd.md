---
title: "ippusbxd(8)"
name: "ippusbxd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ippusbxd/"
description: "ippusbxd – Communication driver for IPP-over-USB class printers"
---

<p>ippusbxd &#8211; Communication driver for IPP-over-USB class printers</p>
<h2>Synopsis</h2>
<p><code>ippusbxd</code> [<code>-v</code>|<code>&#8211;vid </code> <i>VENDOR_ID</i>] [<code>-m</code>|<code>&#8211;pid </code> <i>PRODUCT_ID</i>] [<code>-s</code>|<code>&#8211;serial </code> <i>SERIAL_NUMBER</i>] [<code>&#8211;bus </code> <i>BUS</i>] [<code>&#8211;device </code> <i>DEVICE</i>] [<code>&#8211;bus-device </code> <i>BUS</i><code>:</code><i>DEVICE</i>] [<code>-p</code>|<code>&#8211;only-port </code> <i>PORT_NUMBER</i>] [<code>-P</code>|<code>&#8211;from-port </code> <i>PORT_NUMBER</i>] [<code>-i</code>|<code>&#8211;interface </code> <i>INTERFACE</i>] [<code>-l</code>|<code>&#8211;logging</code>] [<code>-q</code>|<code>&#8211;verbose</code>] [<code>-d</code>|<code>&#8211;debug</code>] [<code>-n</code>|<code>&#8211;no-fork</code>] [<code>-B</code>|<code>&#8211;no-broadcast</code>] [<code>-N</code>|<code>&#8211;no-printer</code>]</p>
<h2>Description</h2>
<p><code>ippusbxd</code> connects to a IPP-over-USB printer and exposes it to a network interface (like localhost or dummy0) on a given port, so that the printer can be accessed like an IPP network printer. The printer is also registered at Avahi to be advertised via DNS-SD on the interface, so <code>CUPS</code> and <code><a href="/docs/linux/man/8-cups-browsed/">cups-browsed</a>(8)</code> will auto-discover the printer for easy setup of a print queue. This requires avahi-daemon to be running and the network interface to be supported by the Avahi version in use. </p>
<p> Upon successful startup the TCP port it is listening on and the process ID of the daemon are printed to stdout. <code>ippusbxd</code> will shut itself down when the connected printer disconnects. When not specifying information about the desired printer, <code>ippusbxd</code> scans the USB and connects to the first available IPP-over-USB printer.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show help message.</p>
<dt><code>-v</code> <i>VENDOR_ID</i>, <code>&#8211;vid</code> <i>VENDOR_ID</i></p>
<dd>USB vendor ID of desired printer.</p>
<dt><code>-m</code> <i>PRODUCT_ID</i>, <code>&#8211;pid</code> <i>PRODUCT_ID</i></p>
<dd>USB product ID of desired printer.</p>
<dt><code>-s</code> <i>SERIAL_NUMBER</i>, <code>&#8211;serial</code> <i>SERIAL_NUMBER</i></p>
<dd>Serial number of desired printer.</p>
<dt><code>&#8211;bus</code> <i>BUS</i> <code>&#8211;device</code> <i>DEVICE</i>, <code>&#8211;bus-device</code> <i>BUS</i><code>:</code><i>DEVICE</i></p>
<dd>USB bus and device numbers where the device is currently connected (see output of <code><a href="/docs/linux/man/8-lsusb/">lsusb</a>(8)</code>). Note that these numbers change when the device is disconnected and reconnected. This method of calling <code>ippusbxd</code> is only for calling via UDEV. <i>BUS</i> and <i>DEVICE</i> have to be given in decimal numbers.</p>
<dt><code>-p</code> <i>PORT_NUMBER</i>, <code>&#8211;only-port</code> <i>PORT_NUMBER</i></p>
<dd>Port number <code>ippusbxd</code> will expose the printer over. If this port is already taken, <code>ippusbxd</code> will error out.</p>
<dt><code>-P</code> <i>PORT_NUMBER</i>, <code>&#8211;from-port</code> <i>PORT_NUMBER</i></p>
<dd>Port number <code>ippusbxd</code> will expose the printer over. If this port is already taken, <code>ippusbxd</code> will increase the port number by 1 and try again until it finds a free port.</p>
<dt><code>-i</code> <i>INTERFACE</i>, <code>&#8211;interface</code> <i>INTERFACE</i></p>
<dd>Network interface to use. Default is the loopback interface (lo, localhost).</p>
<dt><code>-l</code>, <code>&#8211;logging</code></p>
<dd>Send all logging to syslog.</p>
<dt><code>-q</code>, <code>&#8211;verbose</code></p>
<dd>Enable verbose logging.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>Enables debug mode. Implies -q and -n. Verbose logging will be sent to stdout</p>
<dt><code>-n</code>, <code>&#8211;no-fork</code></p>
<dd>Enables no fork mode. Disables deamonization.</p>
<dt><code>-B</code>, <code>&#8211;no-broadcast</code></p>
<dd>No-broadcast mode, do not DNS-SD-broadcast</p>
<dt><code>-N</code>, <code>&#8211;no-printer</code></p>
<dd>No-printer mode, debug/developer mode which makes <code>ippusbxd</code> run without IPP-over-USB printer</dl>
<h2>Bugs</h2>
<p><code>ippusbxd</code> does not detect whether a USB printer is already connected by another instance of <code>ippusbxd</code>, so the system/the user has to take care to not start <code>ippusbxd</code> more than once for one and the same printer. Especially one should never start <code>ippusbxd</code> repeatedly without specifying a printer to assure that all connected IPP-over-USB printers get their <code>ippusbxd</code> instance. </p>
