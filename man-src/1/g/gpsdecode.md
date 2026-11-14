---
title: "gpsdecode(1)"
name: "gpsdecode"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpsdecode/"
description: "gpsdecode – decode GPS, RTCM or AIS streams into a readable format"
---

<h2 class="name">NAME</h2>
<p> gpsdecode &#8211; decode GPS, RTCM or AIS streams into a readable format </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gpsdecode</code> [-c] [-d] [-e] [-j] [-s] [-t&nbsp;<wbr><i>typelist</i>] [-u] [-v] [-D&nbsp;<wbr><i>debuglevel</i>] [-V]</dl>
<h2>DESCRIPTION</h2>
<dd>This tool is a batch-mode decoder for NMEA and various binary packet formats associated with GPS, AIS, and differential-correction services. It produces a JSON dump on standard output from binary on standard input. The JSON is the same format documented in <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8); this tool uses the same decoding logic as gpsd, but with a simpler interface intended for batch processing of data files. </p>
<p> All sensor-input formats known to the GPSD project can be decoded by this tool. These include: NMEA, AIVDM (the NMEA-derived sentence format used by AIS, the marine Automatic Identification System), RTCM2, and all supported GPS binary formats (notably including SiRF). See <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8) for applicable standards and known limitations of the decoding logic. </p>
<p> You can use this tool with <code><a href="/docs/linux/man/1-nc/">nc</a></code>(1) to examine AIS feeds from AIS pooling services, RTCM feeds from RTCM receivers or NTRIP broadcasters.</p>
<h2>OPTIONS</h2>
<p> The <code>-d</code> option tells the program to decode packets presented on standard input to standard output. This is the default behavior. </p>
<p> The <code>-j</code> explicitly sets the output dump format to JSON (the default behavior). </p>
<p> The <code>-e</code> option option tells the program to encode JSON on standard input to JSON on standard output. This option is only useful for regression-testing of the JSON dumping and parsing code. </p>
<p> The <code>-s</code> option option tells the program to report AIS Type 24 sentence halves separately rather than attempting to aggregate them. </p>
<p> The <code>-t</code> accepts a comma-separated list of numeric types. Packets with a numeric AIS, RTCM2, or RTCM3 type are passed through and output only if they match a type in the list. Packets of other kinds (in particular GPS packets) are passed through unconditionally. </p>
<p> The <code>-u</code> suppresses scaling of AIS data to float quantities and text expansion of numeric codes. A dump with this option is lossless. </p>
<p> The <code>-v</code> enables dumping of textual packets to output as they are received on input, immediately preceding corresponding output. </p>
<p> The <code>-c</code> sets the AIS dump format to separate fields with an ASCII pipe symbol. Fields are dumped in the order they occur in the AIS packet. Numerics are not scaled (-u is forced). Strings are unpacked from six-bit to full ASCII </p>
<p> The <code>-V</code> option directs the program to emit its version number, then exit. </p>
<p> The <code>-D</code> option sets a debug verbosity level. It is mainly of interest to developers.</p>
<h2>AIS DSV FORMAT</h2>
<p> With the <code>-c</code> option, dump lines are values of AIS payload fields, pipe-separated, in the order that they occur in the payload. Spans of fields expressing a date are emitted as an ISO8601 timestamp (look for colons and the trailing Z indicating Zulu/UTC time), and the 19-bit group of TDMA status fields found at the end of message types 1-4 are are dumped as a single unsigned integer (in hex preceded by &quot;0x&quot;). Unused regional-authority fields are also dumped (in hex preceded by &quot;0x&quot;). Variable-length binary fields are dumped as an integer bit length, followed by a colon, followed by a hex dump.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/1-gpsctl/">gpsctl</a></code>(1), <code><a href="/docs/linux/man/8-gpsdctl/">gpsdctl</a></code>(8), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3), <code><a href="/docs/linux/man/1-gpsprof/">gpsprof</a></code>(1), <code><a href="/docs/linux/man/1-gpsfake/">gpsfake</a></code>(1),</p>
<h2>AUTHOR</h2>
<p> Eric S. Raymond &lt;esr [at] thyrsus.com&gt;. </p>
<h2>Index</h2>
