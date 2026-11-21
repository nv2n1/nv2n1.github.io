---
title: "gpsctl(1)"
name: "gpsctl"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpsctl/"
description: "gpsctl – control the modes of a GPS"
---
<h2>SYNOPSIS</h2>
<dl>
<dt><code>gpsctl</code> [-h] [-b | -n] [-x&nbsp;<wbr><i>control</i>] [-e] [-f] [-l] [-s&nbsp;<wbr><i>speed</i>] [-t&nbsp;<wbr><i>devicetype</i>] [-D&nbsp;<wbr><i>debuglevel</i>] [-V] [<i>serial-port</i>] </dt>
</dl>
<h2>DESCRIPTION</h2>
<dd> <p> gpsctl can switch a dual-mode GPS between NMEA and vendor-binary modes. It can also be used to set the device baudrate. Note: Not all devices have these capabilities. </p>
<p> If you have only one GPS attached to your machine, and gpsd is running, it is not necessary to specify the device; gpsctl does its work through gpsd, which will locate it for you. </p>
<p> When gpsd is not running, the device specification is required, and you will need to be running as root or be a member of the device&#8217;s owning group in order to have write access to the device. On many Unix variants the owning group will be named &#8216;dialout&#8217;. </p>
<p> The program accepts the following options: </p>
<p> -b </p>
 </dd>
<dl>
<dd> <p> Put the GPS into native (binary) mode. </p>
 </dd></dl>
<p> -c </p>
<dl>
<dd> <p> Change the GPS&#8217;s cycle time. Units are seconds. Note, most GPSes have a fixed cycle time of 1 second. </p>
 </dd></dl>
<p> -e </p>
<dl>
<dd> <p> Generate the packet from any other arguments specified and ship it to standard output instead of the device. This switch can be used with the <code>-t</code> option without specifying a device. Note: the packet data for a binary prototype will be raw, not ASCII-ized in any way. </p>
 </dd></dl>
<p> -f </p>
<dl>
<dd> <p> Force low-level access (not through the daemon). </p>
 </dd></dl>
<p> -l </p>
<dl>
<dd> <p> List a table showing which option switches can be applied to which device types, and exit. </p>
 </dd></dl>
<p> -n </p>
<dl>
<dd> <p> Put GPS into NMEA mode. </p>
 </dd></dl>
<p> -s </p>
<dl>
<dd> <p> Set the baud rate at which the GPS emits packets. </p>
<p> Use this option with caution. On USB and Bluetooth GPSes it is also possible for serial mode setting to fail either because the serial adaptor chip does not support non-8N1 modes or because the device firmware does not properly synchronize the serial adaptor chip with the UART on the GPS chipset when the speed changes. These failures can hang your device, possibly requiring a GPS power cycle or (in extreme cases) physically disconnecting the NVRAM backup battery. </p>
 </dd></dl>
<p> -t </p>
<dl>
<dd> <p> Force the device type. </p>
 </dd></dl>
<p> -x </p>
<dl>
<dd> <p> Send a specified control string to the GPS; gpsctl will provide packet headers and trailers and checksum as appropriate for binary packet types, and whatever checksum and trailer is required for text packet types. (You must include the leading $ for NMEA packets.) When sending to a UBX device, the first two bytes of the string supplied will become the message class and type, and the remainder the payload. When sending to a Navcom NCT or Trimble TSIP device, the first byte is interpreted as the command ID and the rest as payload. When sending to a Zodiac device, the first two bytes are used as a message ID of type little-endian short, and the remainder as payload in byte pairs interpreted as little-endian short. For all other supported binary GPSes (notably including SiRF) the string is taken as the entire message payload and wrapped with appropriate header, trailer and checksum bytes. C-style backslash escapes in the string, notably \xNN for hex, will be interpreted; additionally, \e will be replaced with ESC. This switch implies <code>-f</code>. </p>
 </dd></dl>
<p> -T </p>
<dl>
<dd> <p> Change the sampling timeout. Defaults to 8 seconds, which should always be sufficient to get an identifying packet from a device emitting at the normal rate of 1 per second. </p>
 </dd></dl>
<p> -h </p>
<dl>
<dd> <p> Display program usage and exit. </p>
 </dd></dl>
<p> -D </p>
<dl>
<dd> <p> Set level of debug messages. </p>
 </dd></dl>
<p> -V </p>
<dl>
<dd> <p> Display program version and exit. </p>
 </dd></dl>
<p> The argument of the forcing option, <code>-t</code>, should be a string which is contained in exactly one of the known driver names; for a list, do <code>gpsctl -l</code>. </p>
<p> Forcing the device type behaves somewhat differently depending on whether this tool is going through the daemon or not. In high-level mode, if the device that daemon selects for you doesn&#8217;t match the driver you specified, gpsctl exits with a warning. (This may be useful in scripts.) </p>
<p> In low-level mode, if the device identifies as a Generic NMEA, use the selected driver instead. This will be useful if you have a GPS device of known type that is in NMEA mode and not responding to probes. (This option was originally implemented for talking to SiRFStar I chips, which don&#8217;t respond to the normal SiRF ID probe.) </p>
<p> If no options are given, the program will display a message identifying the GPS type of the selected device and exit. </p>
<p> Reset (-r) operations must stand alone; others can be combined. Multiple options will be executed in this order: mode changes (-b and -n) first, speed changes (-s) second, and control-string sends (-c) last.  </p>
<h2>EXAMPLES</h2>
<p> <code>gpsctl /dev/ttyUSB0</code> </p>
<dl>
<dd> <p> Attempt to identify the device on USB serial device 0. Time out after the default number of seconds. Adding the <code>-f</code> will force low-level access and suppress the normal complaint when this tool can&#8217;t find a GPSD to work through. </p>
 </dd></dl>
<p> gpsctl -f -n -s 9600 /dev/ttyUSB0 </p>
<dl>
<dd> <p> Use low-level operations (not going through a gpsd instance) to switch a GPS to NMEA mode at 9600bps. The tool will identify the GPS type itself. </p>
 </dd></dl>
<h2>BUGS</h2>
<p> SiRF GPSes can only be identified by the success of an attempt to flip them into SiRF binary mode. Thus, the process of probing one of these running in NMEA will change its behavior. </p>
<p> Baud rate and mode changes work in direct mode but are not reliable in client mode. This will be fixed in a future release.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/8-gpsdctl/">gpsdctl</a></code>(8), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3), <code><a href="/docs/linux/man/1-gpsprof/">gpsprof</a></code>(1), <code><a href="/docs/linux/man/1-gpsfake/">gpsfake</a></code>(1).  </p>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] thyrsus.com&gt;. </p>
