---
title: "gps2udp(1)"
name: "gps2udp"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gps2udp/"
description: "gps2udp – feed the take from gpsd to one or more aggregation sites"
---

<h2 class="name">NAME</h2>
<p> gps2udp &#8211; feed the take from gpsd to one or more aggregation sites </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gps2udp</code> [-h] [-n] [-j] [-a] [-u&nbsp;<wbr><i>hostname:udpport</i>] [-c&nbsp;<wbr><i>count</i>] [-d&nbsp;<wbr><i>1|2</i>] [-v] [<i>server</i> [<i>:port</i> [<i>:device</i>]]]</dl>
<h2>DESCRIPTION</h2>
<dd>gps2udp is a tool to connect to gpsd and output the received sentences to one or many UDP host:port destinations. This makes the program useful for feeding AIS information from gpsd to aishub, marinetraffic, shipfinder,&#8230; </p>
<p> gps2udp does not require root privileges, and can be run concurrently with other tools connecting to the local gpsd without causing problems. </p>
<p> The output will consist of one or both of NMEA (-n option) or JSON (-j option) gpsd sentences. The output is sent to one or many destinations host through a UDP network socket (-u host:port options) . </p>
<p> Optionally a server, TCP/IP port number and remote device can be given. If omitted, gps2udp connects to localhost on the default port (2947) and watches all devices opened by gpsd. </p>
<p> gps2udp may be run as a daemon (-b option). </p>
<p> gps2udp is designed to run smoothly in background; it reconnects automatically to gpsd whenever it is restarted. For debugging purporses, there is an option to exit gracefully after a given count of packets (-c option).</p>
<h2>OPTIONS</h2>
<p> -h makes gps2udp print a usage message and exit. </p>
<p> -n causes NMEA sentences to be output. </p>
<p> -j causes JSON sentences to be output. </p>
<p> -u host:port UDP destination for output sentenses (up to five destinations). </p>
<p> -a output only AIS messages. </p>
<p> -b causes gps2udp to run as a daemon. </p>
<p> -c [count] causes [count] sentences to be output. gps2udp will then exit gracefully. </p>
<p> -d 1 prints sent packet on stdout. </p>
<p> -v prints the version, then exits.</p>
<h2>EXAMPLE</h2>
<p> With a running gpsd accessible on the network </p>
<p> <code>gps2udp -d 1 -n -u data.aishub.net:2222 </code> will collect data from localhost:gpsd display them on stdout and send a copy to test aishub in NMEA format. </p>
<p> <code>gps2udp -a -n -b -u data.aishub.net:2222 -u 5.9.207.224:5321 -u 109.200.19.151:4001 fridu.net:2947</code> will collect data from a remote gpsd located on fridu.net host, will filter AIS messages and send them to 3 destination (aishub, marinetraffic, shipfinder) in NMEA format, command is running in background mode</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3), <code><a href="/docs/linux/man/1-gpsprof/">gpsprof</a></code>(1), <code><a href="/docs/linux/man/1-gpsfake/">gpsfake</a></code>(1), <code><a href="/docs/linux/man/1-gpsctl/">gpsctl</a></code>(1), <code><a href="/docs/linux/man/1-gpscat/">gpscat</a></code>(1). <code><a href="/docs/linux/man/1-gpsmon/">gpsmon</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> Fulup Ar Foll &lt;fulup [at] sinagot.net&gt;. </p>
<h2>Index</h2>
