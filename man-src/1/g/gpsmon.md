---
title: "gpsmon(1)"
name: "gpsmon"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpsmon/"
description: "gpsmon – real-time GPS packet monitor and control utility"
---

<h2 class="name">NAME</h2>
<p> gpsmon &#8211; real-time GPS packet monitor and control utility </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gpsmon</code> [-L] [-V] [-h] [-n] [-a] [-l&nbsp;<wbr><i>logfile</i>] [-t&nbsp;<wbr><i>driver-prefix</i>] [[&nbsp;<wbr><i>server</i>&nbsp;<wbr>[<i>:port</i>&nbsp;<wbr>[<i>:device</i>]]&nbsp;<wbr>|&nbsp;<wbr><i>device</i>]] [-D&nbsp;<wbr><i>debuglevel</i>]</dl>
<h2>DESCRIPTION</h2>
<dd>gpsmon is a monitor that watches packets coming from a GPS and displays them along with diagnostic information. It supports commands that can be used to tweak GPS settings in various ways; some are device-independent, some vary with the GPS chipset type. It will behave sanely, just dumping packets, when connected to a GPS type it knows nothing about. </p>
<p> gpsmon differs from a navigation client in that it mostly dumps raw data from the GPS, with only enough data-massaging to allow checks against expected output. In particular, this tool does not do any interpolation or modeling to derive climb/sink or error estimates. Nor does it discard altitude reports when the fix quality is too low. </p>
<p> gpsmon is a designed to run in a terminal emulator with a minimum 25&#215;80 size; the non-GUI interface is a design choice made to accommodate users operating in constrained environments and over telnet or ssh connections. If run in a larger window, the size of the packet-log window will be increased to fit. </p>
<p> gpsmon accepts an -h option that displays a usage message, or a -V option to dump the package version and exit. </p>
<p> This program may be run in either of two modes, as a client for the gpsd daemon (and its associated control socket) or directly connected to a specified serial device. When run with no argument, it attempts to connect to the daemon. If the argument looks like a server:port specification it will also attempt to connect to the daemon. If the argument looks like a bare server name it will attempt to connect to a daemon running on the default gpsd port on that server. Only if the device argument contains slashes but no colons will it be treated as a serial device for direct connection. In direct-connect mode gpsmon will hunt for a correct baud rate and lock on to it automatically. </p>
<p> Unlike gpsd, gpsmon run in direct mode does not do its own device probing. Thus, in particular, if you point it at a GPS with a native binary mode that happens to be emitting NMEA, it won&#8217;t identify the actual type unless the device emits a recognizable NMEA trigger sentence. The -t and -i options may help you. </p>
<p> The -F option is only valid in client mode; it specifies a control socket to which the program should send device control strings. You must specify a valid pathname of a Unix-domain socket on your local filesystem. </p>
<p> The -D option enables packet-getter debugging output and is probably only useful to developers of the GPSD code. Consult the packet-getter source code for relevant values. </p>
<p> The -L option lists a table showing which GPS device types gpsmon has built-in support for, and which generic commands can be applied to which GPS types, and then exits. Note that this does not list type-specific commands associated with individual GPS types. </p>
<p> The -l option sets up logging to a specified file to start immediately on device open. This may be useful is, for example, you want to capture the startup message from a device that displays firmware version information there. </p>
<p> The -n option forces gpsmon to request NMEA0183 packets instead of the raw datastream from gpsd. </p>
<p> The -t option sets up a fallback type. Give it a string that is a distinguishing prefix of exactly one driver type name; this will be used for mode, speed, and rate switching if the driver selected by the packet type lacks those capabilities. Most useful when the packet type is NMEA but the device is known to have a binary mode, such as SiRF binary. </p>
<p> The -a option enables a special debugging mode that does not use screen painting. Packets are dumped normally; any character typed suspends packet dumping and brings up a command prompt. This feature will mainly be of interest to GPSD developers. </p>
<p> After startup (without -a), the top part of the screen reports the contents of several especially interesting packet types. The &quot;PPS offset&quot; field, if nonempty, is the delta between the last 1PPS top of second and the system clock at that time. </p>
<p> The bottom half of the screen is a scrolling hex dump of all packets the GPS is issuing. Dump lines beginning &gt;&gt;&gt; represent control packets sent to the GPS. Lines consisting of &quot;PPS&quot; surrounded by dashes, if present, indicate 1PPS and the start of the reporting cycle.</p>
<h2>COMMANDS</h2>
<p> The following device-independent commands are available while gpsmon is running: </p>
<p> i</p>
<dl>
<dt>
<dd> (Direct mode only.) Enable/disable subtype probing and reinitialize the driver. In normal operation, gpsmon does not send configuration strings to the device (except for wakeup strings needed to get it to send data, if any). The command &#8216;i1&#8217; causes it to send the same sequence of subtype probes that gpsd would. The command &#8216;i0&#8217; turns off probing; &#8216;i&#8217; alone toggles the bit. In either case, the current driver is re-selected; if the probe bit is enabled, probes will begin to be issued immediately. </p>
<p> Note that enabling probing might flip the device into another mode; in particular, it will flip a SiRF chip into binary mode as if you had used the &#8220;n&#8221; command. This is due to a limitation in the SiRF firmware that we can&#8217;t fix.</dl>
<p> c</p>
<dl>
<dt>
<dd> (Direct mode only.) Change cycle time. Follow it with a number interpreted as a cycle time in seconds. Most devices have a fixed cycle time of 1 second, so this command may fail with a message.</dl>
<p> l</p>
<dl>
<dt>
<dd> Toggle packet logging. If packet logging is on, it will be turned off and the log closed. If it is off, logging to the filename following the l will be enabled. Differs from simply capturing the data from the GPS device in that only whole packets are logged. The logfile is opened for append, so you can log more than one portion of the packet stream and they will be stitched together correctly.</dl>
<p> n</p>
<dl>
<dt>
<dd> (Direct mode only.) With an argument of 0, switch device to NMEA mode at current speed; with an argument of 1, change to binary (native) mode. With no argument, toggle the setting. Will show an error if the device doesn&#8217;t have such modes.</dl>
<p> q</p>
<dl>
<dt>
<dd> Quit gpsmon. Control-C, or whatever your current interrupt character is, works as well.</dl>
<p> s</p>
<dl>
<dt>
<dd> (Direct mode only.) Change baud rate. Follow it with a number interpreted as bits per second, for example &quot;s9600&quot;. The speed number may optionally be followed by a colon and a wordlength-parity-stopbits specification in the traditional style, e.g 8N1 (the default), 7E1, etc. Some devices don&#8217;t support serial modes other than their default, so this command may fail with a message. </p>
<p> Use this command with caution. On USB and Bluetooth GPSes it is also possible for serial mode setting to fail either because the serial adaptor chip does not support non-8N1 modes or because the device firmware does not properly synchronize the serial adaptor chip with the UART on the GPS chipset when the speed changes. These failures can hang your device, possibly requiring a GPS power cycle or (in extreme cases) physically disconnecting the NVRAM backup battery.</dl>
<p> t</p>
<dl>
<dt>
<dd> (Direct mode only.) Force a switch of monitoring type. Follow it with a string that is unique to the name of a gpsd driver with gpsmon support; gpsmon will switch to using that driver and display code. Will show an error message if there is no matching gpsd driver, or multiple matches, or the unique match has no display support in gpsmon.</dl>
<p> x</p>
<dl>
<dt>
<dd> (Direct mode only.) Send hex payload to device. Following the command letter you may type hex digit pairs; end with a newline. These will become the payload of a control packet shipped to the device. The packet will be wrapped with headers, trailers, and checksum appropriate for the current driver type. The first one or two bytes of the payload may be specially interpreted, see the description of the <code>-x</code> of <code><a href="/docs/linux/man/1-gpsctl/">gpsctl</a></code>(1).</dl>
<p> X</p>
<dl>
<dt>
<dd> (Direct mode only.) Send raw hex bytes to device. Following the command letter you may type hex digit pairs; end with a newline. These will be shipped to the device.</dl>
<p> Ctrl-S</p>
<dl>
<dt>
<dd> Freeze display, suspend scrolling in debug window.</dl>
<p> Ctrl-Q</p>
<dl>
<dt>
<dd> Unfreeze display, resume normal operation.</dl>
<h3>NMEA support</h3>
<p> (These remarks apply to not just generic NMEA devices but all extended NMEA devices for which gpsmon presently has support.) </p>
<p> All fields are raw data from the GPS except (a) the &quot;Cooked PVT&quot; window near top of screen, provided as a check and (b) the &quot;PPS offset&quot; field. </p>
<p> There are no device-specific commands. Which generic commands are available may vary by type: examine the output of <code>gpsmon -l</code> to learn more.</p>
<h3>SiRF support</h3>
<p> Most information is raw from the GPS. Underlined fields are derived by translation from ECEF coordinates or application of leap-second and local time-zone offsets. 1PPS is the clock lag as usual. </p>
<p> The following commands are supported for SiRF GPSes only: </p>
<p> A</p>
<dl>
<dt>
<dd> (Direct mode only.) Toggle reporting of 50BPS subframe data.</dl>
<p> M</p>
<dl>
<dt>
<dd> (Direct mode only.) Set (M1) or clear (M0) static navigation. The SiRF documentation says &#8220;Static navigation is a position filter designed to be used with motor vehicles. When the vehicle&#8217;s velocity falls below a threshold, the position and heading are frozen, and velocity is set to zero. This condition will continue until the computed velocity rises above 1.2 times the threshold or until the computed position is at least a set distance from the frozen place. The threshold velocity and set distance may vary with software versions.&#8221; </p>
<p> Non-static mode is designed for use with road navigation software, which often snaps the reported position to the nearest road within some uncertainty radius. You probably want to turn static navigation off for pedestrian use, as it is likely to report speed zero and position changing in large jumps.</dl>
<p> P</p>
<dl>
<dt>
<dd> (Direct mode only.) Toggle navigation-parameter display mode. Toggles between normal display and one that shows selected navigation parameters from MID 19, including the Static Navigation bit toggled by the &#8216;M&#8217; command.</dl>
<p> To interpret what you see, you will need a copy of the SiRF Binary Protocol Reference Manual.</p>
<h3>u-blox support</h3>
<p> Most information is raw from the GPS. Underlined fields are derived by translation from ECEF coordinates. 1PPS is the clock lag as usual. There are no per-type special commands.</p>
<h2>BUGS AND LIMITATIONS</h2>
<p> The PPS Offset field will never be updated when running in client mode, even if you can see PPS events in the packet window. This limitation may be fixed in a future release.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/8-gpsdctl/">gpsdctl</a></code>(8), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3), <code><a href="/docs/linux/man/1-gpsprof/">gpsprof</a></code>(1), <code><a href="/docs/linux/man/1-gpsfake/">gpsfake</a></code>(1), <code><a href="/docs/linux/man/1-gpsctl/">gpsctl</a></code>(1), <code><a href="/docs/linux/man/1-gpscat/">gpscat</a></code>(1). <code><a href="/docs/linux/man/1-gpspipe/">gpspipe</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] thyrsus.com&gt;. </p>
<h2>Index</h2>
