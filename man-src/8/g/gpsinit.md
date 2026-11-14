---
title: "gpsinit(8)"
name: "gpsinit"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpsinit/"
description: "gpsinit – initialize CAN kernel modules for GPSD"
---

<p>gpsinit &#8211; initialize CAN kernel modules for GPSD</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>gpsinit</code> [-n&nbsp;<wbr><i>control</i>] [-s&nbsp;<wbr><i>speed</i>] <i>module_name</i> [<i>interface_name</i>]</p>
<dt> <code>gpsinit</code> -h</p>
<dt> <code>gpsinit</code> -v</dl>
<h2>Description</h2>
<dd>gpsinit initializes whatever kernel-level modules are needed to enable special non-serial hardware to communicate with a gpsd instance. Note: it will need root permissions to load modules and perform other special operations, such as changing kernel-interface baudrates. </p>
<p> At present, all modes of this tool are concerned with setting up kernel-level interfaces to hardware on a CAN (Control Area Network) speaking NMEA2000. </p>
<p> The program accepts the following options: </p>
<p> -h</p>
<dl>
<dd>Display a brief help text.</dl>
<p> -v</p>
<dl>
<dd>Display the version of gpsinit.</dl>
<p> -n</p>
<dl>
<dd>Set the CAN network number. The default is 0.</dl>
<p> -s</p>
<dl>
<dd>Set the baudrate to be used to communicate over the serial line to the CAN hardware. The default is 38400 baud.</dl>
<p> The parameter <i>module_name</i> is mandatory. The socket CAN driver module <i>module_name</i>.ko will be loaded. <code>gpsinit</code> recognize the following module names: </p>
<p> plx_pci, esd_usb2, vcan, slcan</p>
<dl>
<dd>The parameter <i>interface_name</i> and <i>-s </i><i>speed</i> can used here.</dl>
<p> beaglebone</p>
<dl>
<dd>The dcan module needed for the beaglebone is part of the Linux kernel, so no module is loaded in this case.</dl>
<p> The parameter <i>interface_name</i> is needed for slcan hardware only. It gives the name of the serial device to which the SL CAN hardware is connected. The default is /dev/ttyUSB0.</p>
<h2>Examples</h2>
<p><code>sudo gpsinit plx_pci</code></p>
<dl>
<dd>Attempt to load the module plx_pci and initialize net 0 for the connection to a NMEA2000 network. It will set the baudrate to 250kBits.</dl>
<p> <code>sudo gpsinit -n 1 plx_pci</code></p>
<dl>
<dd>As above, but use net 1.</dl>
<p> <code>sudo gpsinit -s 38400 slcan /dev/ttyUSB0</code></p>
<dl>
<dd>Attempt to load the module slcan and talk to the hardware at 38400 baud connected to port /dev/ttyUSB0.</dl>
<p> <code>gpsinit -h </code></p>
<dl>
<dd>Display a brief help message.</dl>
<p> <code>gpsinit -v </code></p>
<dl>
<dd>Display the version of gpsinit.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3).</p>
<h2>Author</h2>
<p>Reinhard Arlt &lt;reinhard.arlt [at] t-online.de&gt;.</p>
