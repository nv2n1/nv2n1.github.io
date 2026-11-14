---
title: "gpsctl(1)"
name: "gpsctl"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpsctl/"
description: "gpsctl – control the modes of a GPS"
---

<h2 class="name">NAME</h2>
<p> gpsctl &#8211; control the modes of a GPS </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gpsctl</code> [-h] [-b | -n] [-x&nbsp;<wbr><i>control</i>] [-e] [-f] [-l] [-s&nbsp;<wbr><i>speed</i>] [-t&nbsp;<wbr><i>devicetype</i>] [-D&nbsp;<wbr><i>debuglevel</i>] [-V] [<i>serial-port</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>gpsctl can switch a dual-mode GPS between NMEA and vendor-binary modes. It can also be used to set the device baudrate. Note: Not all devices have these capabilities. </p>
<p> If you have only one GPS attached to your machine, and gpsd is running, it is not necessary to specify the device; gpsctl does its work through gpsd, which will locate it for you. </p>
<p> When gpsd is not running, the device specification is required, and you will need to be running as root or be a member of the device&#8217;s owning group in order to have write access to the device. On many Unix variants the owning group will be named &#8216;dialout&#8217;. </p>
<p> The program accepts the following options: </p>
<p> -b</p>
<dl>
<dt>
<dd> Put the GPS into native (binary) mode.</dl>
<p> -c</p>
<dl>
<dt>
<dd> Change the GPS&#8217;s cycle time. Units are seconds. Note, most GPSes have a fixed cycle time of 1 second.</dl>
<p> -e</p>
<dl>
<dt>
<dd> Generate the packet from any other arguments specified and ship it to standard output instead of the device. This switch can be used with the <code>-t</code> option without specifying a device. Note: the packet data for a binary prototype will be raw, not ASCII-ized in any way.</dl>
<p> -f</p>
<dl>
<dt>
<dd> Force low-level access (not through the daemon).</dl>
<p> -l</p>
<dl>
<dt>
<dd> List a table showing which option switches can be applied to which device types, and exit.</dl>
<p> -n</p>
<dl>
<dt>
<dd> Put GPS into NMEA mode.</dl>
<p> -s</p>
<dl>
<dt>
<dd> Set the baud rate at which the GPS emits packets. </p>
<p> Use this option with caution. On USB and Bluetooth GPSes it is also possible for serial mode setting to fail either because the serial adaptor chip does not support non-8N1 modes or because the device firmware does not properly synchronize the serial adaptor chip with the UART on the GPS chipset when the speed changes. These failures can hang your device, possibly requiring a GPS power cycle or (in extreme cases) physically disconnecting the NVRAM backup battery.</dl>
<p> -t</p>
<dl>
<dt>
<dd> Force the device type.</dl>
<p> -x</p>
<dl>
<dt>
<dd> Send a specified control string to the GPS; gpsctl will provide packet headers and trailers and checksum as appropriate for binary packet types, and whatever checksum and trailer is required for text packet types. (You must include the leading $ for NMEA packets.) When sending to a UBX device, the first two bytes of the string supplied will become the message class and type, and the remainder the payload. When sending to a Navcom NCT or Trimble TSIP device, the first byte is interpreted as the command ID and the rest as payload. When sending to a Zodiac device, the first two bytes are used as a message ID of type little-endian short, and the remainder as payload in byte pairs interpreted as little-endian short. For all other supported binary GPSes (notably including SiRF) the string is taken as the entire message payload and wrapped with appropriate header, trailer and checksum bytes. C-style backslash escapes in the string, notably 
