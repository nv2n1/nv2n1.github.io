---
title: "gpsd(8)"
name: "gpsd"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpsd/"
description: "gpsd – interface daemon for GPS receivers"
---

<p>gpsd &#8211; interface daemon for GPS receivers</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>gpsd</code> [-F&nbsp;<wbr><i>control-socket</i>] [-S&nbsp;<wbr><i>listener-port</i>] [-b] [-l] [-G] [-n] [-N] [-h] [-P&nbsp;<wbr><i>pidfile</i>] [-D&nbsp;<wbr><i>debuglevel</i>] [-V] [[<i>source-name</i>]&#8230;]</dl>
<h2>Quick Start</h2>
<dd>If you have a GPS attached on the lowest-numbered USB port of a Linux system, and want to read reports from it on TCP/IP port 2947, it will normally suffice to do this: </p>
<dl>
<dd>
<pre>gpsd /dev/ttyUSB0</pre>
</dl>
<p> For the lowest-numbered serial port: </p>
<dl>
<dd>
<pre>gpsd /dev/ttyS0</pre>
</dl>
<p> Change the device number as appropriate if you need to use a different port. Command-line flags enable verbose logging, a control port, and other optional extras but should not be needed for basic operation; the one exception, on very badly designed hardware, might be <code>-b</code> (which see). </p>
<p> On Linux systems supporting udev, gpsd is normally started automatically when a USB plugin event fires (if it is not already running) and is handed the name of the newly active device. In that case no invocation is required at all. </p>
<p> For your initial tests set your GPS hardware to speak NMEA, as gpsd is guaranteed to be able to process that. If your GPS has a native or binary mode with better performance that gpsd knows how to speak, gpsd will autoconfigure that mode. </p>
<p> You can verify correct operation by first starting gpsd and then xgps, the X windows test client. </p>
<p> If you have problems, the GPSD project maintains a FAQ to assist troubleshooting.</p>
<h2>Description</h2>
<p>gpsd is a monitor daemon that collects information from GPSes, differential-GPS radios, or AIS receivers attached to the host machine. Each GPS, DGPS radio, or AIS receiver is expected to be direct-connected to the host via a USB or RS232C serial device. The serial device may be specified to gpsd at startup, or it may be set via a command shipped down a local control socket (e.g. by a USB hotplug script). Given a GPS device by either means, gpsd discovers the correct port speed and protocol for it. </p>
<p> gpsd should be able to query any GPS that speaks either the standard textual NMEA 0183 protocol, or the (differing) extended NMEA dialects used by MKT-3301, iTrax, Motorola OnCore, Sony CXD2951, and Ashtech/Thales devices. It can also interpret the binary protocols used by EverMore, Garmin, Navcom, Rockwell/Zodiac, SiRF, Trimble, and u-blox ANTARIS devices. Under Linux it can read NMEA2000 packets through the kernel CAN socket. It can read heading and attitude information from the Oceanserver 5000 or TNT Revolution digital compasses. </p>
<p> The GPS reporting formats supported by your instance of gpsd may differ depending on how it was compiled; general-purpose versions support many, but it can be built with protocol subsets down to a singleton for use in constrained environments. For a list of the GPS protocols supported by your instance, see the output of <code>gpsd -l</code> </p>
<p> gpsd effectively hides the differences among the GPS types it supports. It also knows about and uses commands that tune these GPSes for lower latency. By using gpsd as an intermediary applications avoid contention for serial devices. </p>
<p> gpsd can use differential-GPS corrections from a DGPS radio or over the net, from a ground station running a DGPSIP server or a Ntrip broadcaster that reports RTCM-104 data; this will shrink position errors by roughly a factor of four. When gpsd opens a serial device emitting RTCM-104, it automatically recognizes this and uses the device as a correction source for all connected GPSes that accept RTCM corrections (this is dependent on the type of the GPS; not all GPSes have the firmware capability to accept RTCM correction packets). See the section called &#8220;ACCURACY&#8221; and the section called &#8220;FILES&#8221; for discussion. </p>
<p> Client applications will communicate with gpsd via a TCP/IP port, 2947 by default). Both IPv4 and IPv6 connections are supported and a client may connect via either. </p>
<p> The program accepts the following options: </p>
<p> -F</p>
<dl>
<dd>Create a control socket for device addition and removal commands. You must specify a valid pathname on your local filesystem; this will be created as a Unix-domain socket to which you can write commands that edit the daemon&#8217;s internal device list.</dl>
<p> -S</p>
<dl>
<dd>Set TCP/IP port on which to listen for GPSD clients (default is 2947).</dl>
<p> -b</p>
<dl>
<dd>Broken-device-safety mode, otherwise known as read-only mode. A few bluetooth and USB receivers lock up or become totally inaccessible when probed or reconfigured; see the hardware compatibility list on the GPSD project website for details. This switch prevents gpsd from writing to a receiver. This means that gpsd cannot configure the receiver for optimal performance, but it also means that gpsd cannot break the receiver. A better solution would be for Bluetooth to not be so fragile. A platform independent method to identify serial-over-Bluetooth devices would also be nice.</dl>
<p> -G</p>
<dl>
<dd>This flag causes gpsd to listen on all addresses (INADDR_ANY) rather than just the loop back (INADDR_LOOPBACK) address. For the sake of privacy and security, TPV information is now private to the local machine until the user makes an effort to expose this to the world.</dl>
<p> -l</p>
<dl>
<dd>List all drivers compiled into this gpsd instance. The letters to the left of each driver name are the gpsd control commands supported by that driver.</dl>
<p> -n</p>
<dl>
<dd>Don&#8217;t wait for a client to connect before polling whatever GPS is associated with it. Some RS232 GPSes wait in a standby mode (drawing less power) when the host machine is not asserting DTR, and some cellphone and handheld embedded GPSes have similar behaviors. Accordingly, waiting for a watch request to open the device may save battery power. (This capability is rare in consumer-grade devices).</dl>
<p> -N</p>
<dl>
<dd>Don&#8217;t daemonize; run in foreground. This switch is mainly useful for debugging.</dl>
<p> -h</p>
<dl>
<dd>Display help message and terminate.</dl>
<p> -P</p>
<dl>
<dd>Specify the name and path to record the daemon&#8217;s process ID.</dl>
<p> -D</p>
<dl>
<dd>Set debug level. At debug levels 2 and above, gpsd reports incoming sentence and actions to standard error if gpsd is in the foreground (-N) or to syslog if in the background.</dl>
<p> -V</p>
<dl>
<dd>Dump version and exit.</dl>
<p> Arguments are interpreted as the names of data sources. Normally, a data source is the device pathname of a local device from which the daemon may expect GPS data. But there are three other special source types recognized, for a total of four: </p>
<p> Local serial or USB device</p>
<dl>
<dd>A normal Unix device name of a serial or USB device to which a sensor is attached. Example: /dev/ttyUSB0.</dl>
<p> TCP feed</p>
<dl>
<dd>A URI with the prefix &quot;tcp://&quot;, followed by a hostname, a colon, and a port number. The daemon will open a socket to the indicated address and port and read data packets from it, which will be interpreted as though they had been issued by a serial device. Example: <a href="tcp://data.aishub.net:4006.">tcp://data.aishub.net:4006.</a></dl>
<p> UDP feed</p>
<dl>
<dd>A URI with the prefix &quot;udp://&quot;, followed by a hostname, a colon, and a port number. The daemon will open a socket listening for UDP datagrams arriving on the indicated address and port, which will be interpreted as though they had been issued by a serial device. Example: <a href="udp://127.0.0.1:5000.">udp://127.0.0.1:5000.</a></dl>
<p> Ntrip caster</p>
<dl>
<dd>A URI with the prefix &quot;ntrip://&quot; followed by the name of an Ntrip caster (Ntrip is a protocol for broadcasting differential-GPS fixes over the net). For Ntrip services that require authentication, a prefix of the form &quot;username:password@&quot; can be added before the name of the Ntrip broadcaster. For Ntrip service, you must specify which stream to use; the stream is given in the form &quot;/streamname&quot;. An example DGPSIP URI could be &quot;<a href="dgpsip://dgpsip.example.com">dgpsip://dgpsip.example.com</a>&quot; and a Ntrip URI could be &quot;<a href="ntrip://foo:bar@ntrip.example.com:80/example-stream">ntrip://foo:bar@ntrip.example.com:80/example-stream</a>&quot;. Corrections from the caster will be send to each attached GPS with the capability to accept them.</dl>
<p> DGPSIP server</p>
<dl>
<dd>A URI with the prefix &quot;dgpsip://&quot; followed by a hostname, a colon, and an optional colon-separated port number (defaulting to 2101). The daemon will handshake with the DGPSIP server and read RTCM2 correction data from it. Corrections from the server will be set to each attached GPS with the capability to accept them. Example: <a href="dgpsip://dgps.wsrcc.com:2101.">dgpsip://dgps.wsrcc.com:2101.</a></dl>
<p> Remote gpsd feed</p>
<dl>
<dd>A URI with the prefix &quot;gpsd://&quot;, followed by a hostname and optionally a colony and a port number (if the port is absent the default gpsd port will be used). The daemon will open a socket to the indicated address and port and emulate a gpsd client, collecting JSON reports from the remote gpsd instance that will be passed to local clients.</dl>
<p> NMEA2000 CAN data</p>
<dl>
<dd>A URI with the prefix &quot;nmea2000://&quot;, followed by a CAN devicename. Only Linux socket CAN interfaces are supported. The interface must be configured to receive CAN messages before gpsd can be started. If there is more then one unit on the CAN bus that provides GPS data, gpsd chooses the unit from which a GPS message is first seen. Example: nmea2000://can0.</dl>
<p> (The &quot;ais:://&quot; source type supported in some older versions of the daemon has been retired in favor of the more general &quot;tcp://&quot;.) </p>
<p> Internally, the daemon maintains a device pool holding the pathnames of devices and remote servers known to the daemon. Initially, this list is the list of device-name arguments specified on the command line. That list may be empty, in which case the daemon will have no devices on its search list until they are added by a control-socket command (see the section called &#8220;GPS DEVICE MANAGEMENT&#8221; for details on this). Daemon startup will abort with an error if neither any devices nor a control socket are specified. </p>
<p> When a device is activated (i.e. a client requests data from it), gpsd attempts to execute a hook from /etc/gpsd/device-hook with first command line argument set to the pathname of the device and the second to <code>ACTIVATE</code>. On deactivation it does the same passing <code>DEACTIVATE</code> for the second argument. </p>
<p> gpsd can export data to client applications in three ways: via a sockets interface, via a shared-memory segment, and via D-Bus. The next three major sections describe these interfaces.</p>
<h2>The Socket Interface</h2>
<p>Clients may communicate with the daemon via textual request and responses over a socket. It is a bad idea for applications to speak the protocol directly: rather, they should use the libgps client library and take appropriate care to conditionalize their code on the major and minor protocol version symbols. </p>
<p> The request-response protocol for the socket interface is fully documented in <code><a href="/docs/linux/man/5-gpsd_json/">gpsd_json</a></code>(5).</p>
<h2>Shared-Memory And Dbus Interfaces</h2>
<p>gpsd has two other (read-only) interfaces. </p>
<p> Whenever the daemon recognizes a packet from any attached device, it writes the accumulated state from that device to a shared memory segment. The C and C++ client libraries shipped with GPSD can read this segment. Client methods, and various restrictions associated with the read-only nature of this interface, are documented at <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3). The shared-memory interface is intended primarily for embedded deployments in which gpsd monitors a single device, and its principal advantage is that a daemon instance configured with shared memory but without the sockets interface loses a significant amount of runtime weight. </p>
<p> The daemon may be configured to emit a D-Bus signal each time an attached device delivers a fix. The signal path is path /org/gpsd, the signal interface is &quot;org.gpsd&quot;, and the signal name is &quot;fix&quot;. The signal payload layout is as follows: </p>
<p> <code>Table 1. Satellite object</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Type </code></td>
<td><code> </p>
<p> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> DBUS_TYPE_DOUBLE </td>
<td>
<p> Time (seconds since Unix epoch)
</td>
</tr>
<tr VALIGN=top>
<td> DBUS_TYPE_INT32 </td>
<td>
<p> mode
</td>
</tr>
<tr VALIGN=top>
<td> DBUS_TYPE_DOUBLE </td>
<td>
<p> Time uncertainty (seconds).
</td>
</tr>
<tr VALIGN=top>
<td> DBUS_TYPE_DOUBLE </td>
<td>
<p> Latitude in degrees.
</td>
</tr>
<tr VALIGN=top>
<td> DBUS_TYPE_DOUBLE </td>
<td>
<p> Longitude in degrees.
</td>
</tr>
<tr VALIGN=top>
<td> DBUS_TYPE_DOUBLE </td>
<td>
<p> Horizontal uncertainty in meters, 95% confidence.
</td>
</tr>
<tr VALIGN=top>
<td> DBUS_TYPE_DOUBLE </td>
<td>
<p> Altitude in meters.
</td>
</tr>
<tr VALIGN=top>
<td> DBUS_TYPE_DOUBLE </td>
<td>
<p> Altitude uncertainty in meters, 95% confidence.
</td>
</tr>
<tr VALIGN=top>
<td> DBUS_TYPE_DOUBLE </td>
<td>
<p> Course in degrees from true north.
</td>
</tr>
<tr VALIGN=top>
<td> DBUS_TYPE_DOUBLE </td>
<td>
<p> Course uncertainty in meters, 95% confidence.
</td>
</tr>
<tr VALIGN=top>
<td> DBUS_TYPE_DOUBLE </td>
<td>
<p> Speed, meters per second.
</td>
</tr>
<tr VALIGN=top>
<td> DBUS_TYPE_DOUBLE </td>
<td>
<p> Speed uncertainty in meters per second, 95% confidence.
</td>
</tr>
<tr VALIGN=top>
<td> DBUS_TYPE_DOUBLE </td>
<td>
<p> Climb, meters per second.
</td>
</tr>
<tr VALIGN=top>
<td> DBUS_TYPE_DOUBLE </td>
<td>
<p> Climb uncertainty in meters per second, 95% confidence.
</td>
</tr>
<tr VALIGN=top>
<td> DBUS_TYPE_STRING </td>
<td>
<p> Device name
</td>
</tr>
</table>
<h2>Gps Device Management</h2>
<p>gpsd maintains an internal list of GPS devices (the &quot;device pool&quot;). If you specify devices on the command line, the list is initialized with those pathnames; otherwise the list starts empty. Commands to add and remove GPS device paths from the daemon&#8217;s device list must be written to a local Unix-domain socket which will be accessible only to programs running as root. This control socket will be located wherever the -F option specifies it. </p>
<p> A device may will also be dropped from the pool if GPSD gets a zero length read from it. This end-of-file condition indicates that the&#8217; device has been disconnected. </p>
<p> When gpsd is properly installed along with hotplug notifier scripts feeding it device-add commands over the control socket, gpsd should require no configuration or user action to find devices. </p>
<p> Sending SIGHUP to a running gpsd forces it to close all GPSes and all client connections. It will then attempt to reconnect to any GPSes on its device list and resume listening for client connections. This may be useful if your GPS enters a wedged or confused state but can be soft-reset by pulling down DTR. </p>
<p> To point gpsd at a device that may be a GPS, write to the control socket a plus sign (&#8216;+&#8217;) followed by the device name followed by LF or CR-LF. Thus, to point the daemon at /dev/foo. send &quot;+/dev/foo
&quot;. To tell the daemon that a device has been disconnected and is no longer available, send a minus sign (&#8216;-&#8216;) followed by the device name followed by LF or CR-LF. Thus, to remove /dev/foo from the search list. send &quot;-/dev/foo
&quot;. </p>
<p> To send a control string to a specified device, write to the control socket a &#8216;!&#8217;, followed by the device name, followed by &#8216;=&#8217;, followed by the control string. </p>
<p> To send a binary control string to a specified device, write to the control socket a &#8216;&amp;&#8217;, followed by the device name, followed by &#8216;=&#8217;, followed by the control string in paired hex digits. </p>
<p> Your client may await a response, which will be a line beginning with either &quot;OK&quot; or &quot;ERROR&quot;. An ERROR response to an add command means the device did not emit data recognizable as GPS packets; an ERROR response to a remove command means the specified device was not in gpsd&#8217;s device pool. An ERROR response to a ! command means the daemon did not recognize the devicename specified. </p>
<p> The control socket is intended for use by hotplug scripts and other device-discovery services. This control channel is separate from the public gpsd service port, and only locally accessible, in order to prevent remote denial-of-service and spoofing attacks.</p>
<h2>Accuracy</h2>
<p>The base User Estimated Range Error (UERE) of GPSes is 8 meters or less at 66% confidence, 15 meters or less at 95% confidence. Actual horizontal error will be UERE times a dilution factor dependent on current satellite position. Altitude determination is more sensitive to variability in ionospheric signal lag than latitude/longitude is, and is also subject to errors in the estimation of local mean sea level; base error is 12 meters at 66% confidence, 23 meters at 95% confidence. Again, this will be multiplied by a vertical dilution of precision (VDOP) dependent on satellite geometry, and VDOP is typically larger than HDOP. Users should <i>not</i> rely on GPS altitude for life-critical tasks such as landing an airplane. </p>
<p> These errors are intrinsic to the design and physics of the GPS system. gpsd does its internal computations at sufficient accuracy that it will add no measurable position error of its own. </p>
<p> DGPS correction will reduce UERE by a factor of 4, provided you are within about 100mi (160km) of a DGPS ground station from which you are receiving corrections. </p>
<p> On a 4800bps connection, the time latency of fixes provided by gpsd will be one second or less 95% of the time. Most of this lag is due to the fact that GPSes normally emit fixes once per second, thus expected latency is 0.5sec. On the personal-computer hardware available in 2005 and later, computation lag induced by gpsd will be negligible, on the order of a millisecond. Nevertheless, latency can introduce significant errors for vehicles in motion; at 50km/h (31mi/h) of speed over ground, 1 second of lag corresponds to 13.8 meters change in position between updates. </p>
<p> The time reporting of the GPS system itself has an intrinsic accuracy limit of 14 nanoseconds, but this can only be approximated by specialized receivers using that send the high-accuracy PPS (Pulse-Per-Second) over RS232 to cue a clock crystal. Most GPS receivers only report time to a precision of 0.01s or 0.001s, and with no accuracy guarantees below 1sec. </p>
<p> If your GPS uses a SiRF chipset at firmware level 231, reported UTC time may be off by the difference between whatever default leap-second offset has been compiled in and whatever leap-second correction is currently applicable, from startup until complete subframe information is received. Firmware levels 232 and up don&#8217;t have this problem. You may run gpsd at debug level 4 to see the chipset type and firmware revision level. </p>
<p> There are exactly two circumstances under which gpsd relies on the host-system clock: </p>
<p> In the GPS broadcast signal, GPS time is represented using a week number that rolls over after 2^10 or 2^13 weeks (about 19.6 years, or 157 years), depending on the spacecraft. Receivers are required to disambiguate this to the correct date, but may have difficulty due to not knowing time to within half this interval, or may have bugs. Users have reported incorrect dates which appear to be due to this issue. gpsd uses the startup time of the daemon detect and compensate for rollovers while it is running, but otherwise reports the date as it is reported by the receiver without attempting to correct it. </p>
<p> If you are using an NMEA-only GPS (that is, not using SiRF or Garmin or Zodiac binary mode), gpsd relies on the system clock to tell it the current century. If the system clock returns an invalid value near zero, and the GPS does not emit GPZDA at the start of its update cycle (which most consumer-grade NMEA GPSes do not) then the century part of the dates gpsd delivers may be wrong. Additionally, near the century turnover, a range of dates as wide in seconds as the accuracy of your system clock may be referred to the wrong century.</p>
<h2>Use With Ntp</h2>
<p>gpsd can provide reference clock information to ntpd, to keep the system clock synchronized to the time provided by the GPS receiver. </p>
<p> On Linux, gpsd includes support for interpreting the PPS pulses emitted at the start of every clock second on the carrier-detect lines of some serial GPSes; this pulse can be used to update NTP at much higher accuracy than message time provides. You can determine whether your GPS emits this pulse by running at -D 5 and watching for carrier-detect state change messages in the logfile. In addition, if your kernel provides the RFC 2783 kernel PPS API then gpsd will use that for extra accuracy. </p>
<p> Detailed instructions for using GPSD to set up a high-quality time service can be found among the documentation on the GPSD website.</p>
<h2>Use With D-Bus</h2>
<p>On operating systems that support D-BUS, gpsd can be built to broadcast GPS fixes to D-BUS-aware applications. As D-BUS is still at a pre-1.0 stage, we will not attempt to document this interface here. Read the gpsd source code to learn more.</p>
<h2>Security And Permissions Issues</h2>
<p>gpsd, if given the -G flag, will listen for connections from any reachable host, and then disclose the current position. Before using the -G flag, consider whether you consider your computer&#8217;s location to be sensitive data to be kept private or something that you wish to publish. </p>
<p> gpsd must start up as root in order to open the NTPD shared-memory segment, open its logfile, and create its local control socket. Before doing any processing of GPS data, it tries to drop root privileges by setting its UID to &quot;nobody&quot; (or another configured userid) and its group ID to the group of the initial GPS passed on the command line &#8212; or, if that device doesn&#8217;t exist, to the group of /dev/ttyS0. </p>
<p> Privilege-dropping is a hedge against the possibility that carefully crafted data, either presented from a client socket or from a subverted serial device posing as a GPS, could be used to induce misbehavior in the internals of gpsd. It ensures that any such compromises cannot be used for privilege elevation to root. </p>
<p> The assumption behind gpsd&#8217;s particular behavior is that all the tty devices to which a GPS might be connected are owned by the same non-root group and allow group read/write, though the group may vary because of distribution-specific or local administrative practice. If this assumption is false, gpsd may not be able to open GPS devices in order to read them (such failures will be logged). </p>
<p> In order to fend off inadvertent denial-of-service attacks by port scanners (not to mention deliberate ones), gpsd will time out inactive client connections. Before the client has issued a command that requests a channel assignment, a short timeout (60 seconds) applies. There is no timeout for clients in watcher or raw modes; rather, gpsd drops these clients if they fail to read data long enough for the outbound socket write buffer to fill. Clients with an assigned device in polling mode are subject to a longer timeout (15 minutes).</p>
<h2>Limitations</h2>
<p>If multiple NMEA talkers are feeding RMC, GLL, and GGA sentences to the same serial device (possible with an RS422 adapter hooked up to some marine-navigation systems), a &#8216;TPV&#8217; response may mix an altitude from one device&#8217;s GGA with latitude/longitude from another&#8217;s RMC/GLL after the second sentence has arrived. </p>
<p> gpsd may change control settings on your GPS (such as the emission frequency of various sentences or packets) and not restore the original settings on exit. This is a result of inadequacies in NMEA and the vendor binary GPS protocols, which often do not give clients any way to query the values of control settings in order to be able to restore them later. </p>
<p> When using SiRF chips, the VDOP/TDOP/GDOP figures and associated error estimates are computed by gpsd rather than reported by the chip. The computation does not exactly match what SiRF chips do internally, which includes some satellite weighting using parameters gpsd cannot see. </p>
<p> Autobauding on the Trimble GPSes can take as long as 5 seconds if the device speed is not matched to the GPS speed. </p>
<p> Generation of position error estimates (eph, epv, epd, eps, epc) from the incomplete data handed back by GPS reporting protocols involves both a lot of mathematical black art and fragile device-dependent assumptions. This code has been bug-prone in tbe past and problems may still lurk there. </p>
<p> AIDVM decoding of types 16-17, 22-23, and 25-26 is unverified. </p>
<p> GPSD presently fully recognizes only the 2.1 level of RTCM2 (message types 1, 3, 4, 5, 6, 7, 9, 16). The 2.3 message types 13, 14, and 31 are recognized and reported. Message types 8, 10-12, 15-27, 28-30 (undefined), 31-37, 38-58 (undefined), and 60-63 are not yet supported. </p>
<p> The ISGPS used for RTCM2 and subframes decoder logic is sufficiently convoluted to confuse some compiler optimizers, notably in GCC 3.x at -O2, into generating bad code. </p>
<p> Devices meant to to use PPS for high-precision timekeeping may fail if they are specified after startup by a control-socket command, as opposed to on the daemon&#8217;s original command line. Root privileges are dropped early, and some Unix variants require them in order to set the PPS line discipline. Under Linux the POSIX capability to set the line discipline is retained, but other platforms cannot use this code. </p>
<p> USB GPS devices often do not identify themselves through the USB subsystem; they typically present as the class 00h (undefined) or class FFh (vendor-specific) of USB-to-serial adapters. Because of this, the Linux hotplug scripts must tell gpsd to sniff data from every USB-to-serial adapter that goes active and is known to be of a type used in GPSes. No such device is sent configuration strings until after it has been identified as a GPS, and gpsd never opens a device that is opened by another process. But there is a tiny window for non-GPS devices not opened; if the application that wants them loses a race with GPSD its device open will fail and have to be retried after GPSD sniffs the device (normally less than a second later).</p>
<h2>Files</h2>
<p>/dev/ttyS0</p>
<dl>
<dd>Prototype TTY device. After startup, gpsd sets its group ID to the owning group of this device if no GPS device was specified on the command line does not exist.</dl>
<p> /etc/gpsd/device-hook</p>
<dl>
<dd>Optional file containing the device activation/deactivation script. Note that while /etc/gpsd is the default system configuration directory, it is possible to build the GPSD source code with different assumptions.</dl>
<h2>Applicable Standards</h2>
<p>The official NMEA protocol standards for NMEA0183 and NMEA2000 are available from the National Marine Electronics Association, but are proprietary and expensive; the maintainers of gpsd have made a point of not looking at them. The GPSD project website links to several documents that collect publicly disclosed information about the protocol. </p>
<p> gpsd parses the following NMEA sentences: RMC, GGA, GLL, GSA, GSV, VTG, ZDA, GBS, HDT, DBT. It recognizes these with either the normal GP talker-ID prefix, or with the GN prefix used by GLONASS, or with the II prefix emitted by Seahawk Autohelm marine navigation systems, or with the IN prefix emitted by some Garmin units, or with the EC prefix emitted by ECDIS units, or with the SD prefix emitted by depth sounders. It recognizes some vendor extensions: the PGRME emitted by some Garmin GPS models, the OHPR emitted by Oceanserver digital compasses, the PTNTHTM emitted by True North digital compasses, and the PASHR sentences emitted by some Ashtech GPSes. </p>
<p> Note that gpsd JSON returns pure decimal degrees, not the hybrid degree/minute format described in the NMEA standard. </p>
<p> Differential-GPS corrections are conveyed by the RTCM protocols. The applicable standard for RTCM-104 V2 is RTCM Recommended Standards for Differential GNSS (Global Navigation Satellite) Service RTCM Paper 136-2001/SC 104-STD. The applicable standard for RTCM-104 V3 is RTCM Standard 10403.1 for Differential GNSS Services &#8211; Version 3 RTCM Paper 177-2006-SC104-STD. Ordering instructions for the RTCM standards are accessible from the website of the Radio Technical Commission for Maritime Services under &quot;Publications&quot;. </p>
<p> AIS is defined by ITU Recommendation M.1371, Technical Characteristics for a Universal Shipborne Automatic Identification System Using Time Division Multiple Access. The AIVDM/AIVDO format understood by this program is defined by IEC-PAS 61162-100, Maritime navigation and radiocommunication equipment and systems. A more accessible description of both can be found at AIVDM/AIVDO Protocol Decoding, on the references page of the GPSD project website. </p>
<p> Subframe data is defined by IS-GPS-200E, GLOBAL POSITIONING SYSTEM WING (GPSW) SYSTEMS ENGINEERING &amp; INTEGRATION, INTERFACE SPECIFICATION IS-GPS-200 Revision E. The format understood by this program is defined in Section 20 (Appendix II) of the IS-GPS-200E, GPS NAVIGATION DATA STRUCTURE FOR DATA, D(t) </p>
<p> The API for PPS time service is specified by RFC 2783, Pulse-Per-Second API for UNIX-like Operating Systems, Version 1.0</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-gpsdctl/">gpsdctl</a></code>(8), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3), <code><a href="/docs/linux/man/5-gpsd_json/">gpsd_json</a></code>(5), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3), <code><a href="/docs/linux/man/1-gpsprof/">gpsprof</a></code>(1), <code><a href="/docs/linux/man/1-gpsfake/">gpsfake</a></code>(1), <code><a href="/docs/linux/man/1-gpsctl/">gpsctl</a></code>(1), <code><a href="/docs/linux/man/1-gpscat/">gpscat</a></code>(1),</p>
<h2>Authors</h2>
<p>Authors: Eric S. Raymond, Chris Kuethe, Gary Miller. Former authors whose bits have been plowed under by code turnover: Remco Treffcorn, Derrick Brashear, Russ Nelson. This manual page by Eric S. Raymond &lt;esr [at] thyrsus.com&gt;.</p>
