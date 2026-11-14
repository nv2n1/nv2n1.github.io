---
title: "gpspipe(1)"
name: "gpspipe"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpspipe/"
description: "gpspipe – tool to connect to gpsd and retrieve sentences"
---

<h2 class="name">NAME</h2>
<p> gpspipe &#8211; tool to connect to gpsd and retrieve sentences </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gpspipe</code> [-h] [-d] [-l] [-o&nbsp;<wbr><i>filename</i>] [-n&nbsp;<wbr><i>count</i>] [-r] [-R] [-s&nbsp;<wbr><i>serial-device</i>] [-t] [-T&nbsp;<wbr><i>timestamp-format</i>] [-u] [-p] [-w] [-S] [-2] [-v] [-D&nbsp;<wbr><i>debug-level</i>] [<i>server</i> [<i>:port</i> [<i>:device</i>]]]</dl>
<h2>DESCRIPTION</h2>
<dd>gpspipe is a tool to connect to gpsd and output the received sentences to stdout. This makes the program useful as a pipe from gpsd to another program or file. </p>
<p> gpspipe does not require root privileges, and can be run concurrently with other tools connecting to the local gpsd without causing problems. </p>
<p> The output will consist of one or both of the raw NMEA or native gpsd sentences. Each line can be optionally time stamped. There is also an option to exit gracefully after a given count of packets. </p>
<p> Optionally a server, TCP/IP port number and remote device can be given. If omitted, gpspipe connects to localhost on the default port (2947) and watches all devices opened by gpsd. </p>
<p> gpspipe may be run as a daemon, but requires the -o flag for writing the output to a file.</p>
<h2>OPTIONS</h2>
<p> -h makes gpspipe print a usage message and exit. </p>
<p> -d causes gpspipe to run as a daemon. </p>
<p> -l causes gpspipe to sleep for ten seconds before attempting to connect to gpsd. This is very useful when running as a daemon, giving gpsd time to start before attempting a connection. </p>
<p> -r causes raw NMEA sentences to be output. </p>
<p> -R causes super-raw (gps binary) data to be output. This overrides NMEA and gpsd output modes. </p>
<p> -s option causes the collected data to be written to the specified serial device with settings 4800 8N1. Thus gpspipe can be used with -s and -r options to emulate a serial port hardwired to a GPS that gpsd is managing. </p>
<p> -o option causes the collected data to be written to the specified file. Use of this option is mandatory if gpspipe is run as a daemon. </p>
<p> -w causes native gpsdsentences to be output. </p>
<p> -S sets the scaled flag. </p>
<p> -2 sets the split24 flag on AIS reports. Note: this option is experimental and may be changed or removed in a future release. </p>
<p> -t adds a timestamp to each sentence output. </p>
<p> -T sets the format of the timestamp. See <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) for the available placeholders. Setting this option implies -t. Default setting is &quot;%F %T&quot; </p>
<p> -u usec resolution time stamp, implies -t. Use -uu to output sec.usec. </p>
<p> -p enables dumping of profiling information in JSON. </p>
<p> -P enables dumping of PPS drift JSON is NMEA and raw modes. </p>
<p> -n [count] causes [count] sentences to be output. gpspipe will then exit gracefully. </p>
<p> -v causes gpspipe to show a spinning activity indicator on stderr. This is useful if stdout is redirected into a file or a pipe. By default the spinner is advanced with every messages written; specifying -v more than once will double the number of messages required to rotate the spinner. </p>
<p> -V prints the version, then exits. </p>
<p> At least one of -R, -r or -w must be specified.</p>
<h2>EXAMPLE</h2>
<p> When gpsd is running<code>gpspipe -r -n 100</code> will send one hundred raw NMEA sentences to standard output, then exit.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3), <code><a href="/docs/linux/man/1-gpsprof/">gpsprof</a></code>(1), <code><a href="/docs/linux/man/1-gpsfake/">gpsfake</a></code>(1), <code><a href="/docs/linux/man/1-gpsctl/">gpsctl</a></code>(1), <code><a href="/docs/linux/man/1-gpscat/">gpscat</a></code>(1). <code><a href="/docs/linux/man/1-gpsmon/">gpsmon</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> Gary E. Miller &lt;gem [at] rellim.com&gt;. </p>
<h2>Index</h2>
