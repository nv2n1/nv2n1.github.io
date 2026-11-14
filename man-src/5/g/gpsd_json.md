---
title: "gpsd_json(5)"
name: "gpsd_json"
section: "5"
letter: "g"
url: "/docs/linux/man/5-gpsd_json/"
description: "gpsd_json – gpsd request/response protol"
---

<p>gpsd_json &#8211; gpsd request/response protol</p>
<h2>Overview</h2>
<p>gpsd is a service daemon that can be used to monitor GPSes, DGPS receivers, Marine AIS broadcasts, and various other location-related and kinematic sensors. </p>
<p> Clients may communicate with gpsd via textual requests and responses over a socket. It is a bad idea for applications to speak the protocol directly: rather, they should use the libgps client library (for C; bindings also exist for other languages) and take appropriate care to conditionalize their code on the major and minor protocol version symbols. </p>
<p> The GPSD protocol is built on top of JSON, JavaScript Object Notation. GPSD&#8217;s use of JSON is restricted in some ways that make parsing it in fixed-extent languages (such as C) easier. </p>
<p> A request line is introduced by &quot;?&quot; and may include multiple commands. Commands begin with a command identifier, followed either by a terminating &#8216;;&#8217; or by an equal sign &quot;=&quot; and a JSON object treated as an argument. Any &#8216;;&#8217; or newline indication (either LF or CR-LF) after the end of a command is ignored. All request lines must be composed of US-ASCII characters and may be no more than 80 characters in length, exclusive of the trailing newline. </p>
<p> Responses are JSON objects all of which have a &quot;class&quot; attribute the value of which is either the name of the invoking command. There are reports (including but not limited to as &quot;TPV&quot;, &quot;SKY&quot;, &quot;DEVICE&quot;, and &quot;ERROR&quot;) which are not direct responses to commands. </p>
<p> The order of JSON attributes within a response object is never significant, and you may specify attributes in commands in any order. Responses never contain the special JSON value null; instead, attributes with empty or undefined values are omitted. The length limit for responses and reports is 1536 characters, including trailing newline; longer responses will be truncated, so client code must be prepared for the possibility of invalid JSON fragments. </p>
<p> In JSON reports, if an attribute is present only if the parent attribute is present or has a particular range, then the parent attribute is emitted first. </p>
<p> There is one constraint on the order in which attributes will be omitted. If an optional attribute is present only when a parent attribute has a specified value or range of values, the parent attribute will be emitted first to make parsing easier. </p>
<p> The next subsection section documents the core GPSD protocol. Extensions are documented in the following subsections. The extensions may not be supported in your gpsd instance if it has been compiled with a restricted feature set.</p>
<h2>Core Socket Protocol</h2>
<p>Here are the core-protocol responses: </p>
<p> TPV</p>
<dl>
<dd>A TPV object is a time-position-velocity report. The &quot;class&quot; and &quot;mode&quot; fields will reliably be present. The &quot;mode&quot; field will be emitted before optional fields that may be absent when there is no fix. Error estimates will be emitted after the fix components they&#8217;re associated with. Others may be reported or not depending on the fix quality. </p>
<p> <code>Table 1. TPV object</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Always? </code></td>
<td><code> Type </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> class </td>
<td> Yes </td>
<td> string </td>
<td> Fixed: &quot;TPV&quot;
</td>
</tr>
<tr VALIGN=top>
<td> tag </td>
<td> No </td>
<td> string </td>
<td> Type tag associated with this GPS sentence; from an NMEA <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>device this is just the NMEA sentence type.</p>
</td>
</tr>
<tr VALIGN=top>
<td> device </td>
<td> No </td>
<td> string </td>
<td> Name of originating device.
</td>
</tr>
<tr VALIGN=top>
<td> mode </td>
<td> Yes </td>
<td> numeric </td>
<td> NMEA mode: %d, 0=no mode value yet seen, 1=no fix, 2=2D, 3=3D.
</td>
</tr>
<tr VALIGN=top>
<td> time </td>
<td> No </td>
<td> string </td>
<td> Time/date stamp in ISO8601 format, UTC. May have a <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fractional part of up to .001sec precision. May be absent if mode </p>
<p>&nbsp;<wbr>&nbsp;<wbr>is not 2 or 3.
</td>
</tr>
<tr VALIGN=top>
<td> ept </td>
<td> No </td>
<td> numeric </td>
<td> Estimated timestamp error (%f, seconds, 95% confidence).<br />
&nbsp;<wbr>&nbsp;<wbr>Present if time is present.
</td>
</tr>
<tr VALIGN=top>
<td> lat </td>
<td> No </td>
<td> numeric </td>
<td> Latitude in degrees: +/- signifies North/South. Present<br />
&nbsp;<wbr>&nbsp;<wbr>when mode is 2 or 3.
</td>
</tr>
<tr VALIGN=top>
<td> lon </td>
<td> No </td>
<td> numeric </td>
<td> Longitude in degrees: +/- signifies East/West. Present<br />
&nbsp;<wbr>&nbsp;<wbr>when mode is 2 or 3.
</td>
</tr>
<tr VALIGN=top>
<td> alt </td>
<td> No </td>
<td> numeric </td>
<td> Altitude in meters. Present if mode is 3.
</td>
</tr>
<tr VALIGN=top>
<td> epx </td>
<td> No </td>
<td> numeric </td>
<td> Longitude error estimate in meters, 95% confidence. Present<br />
&nbsp;<wbr>&nbsp;<wbr>if mode is 2 or 3 and DOPs can be calculated from the satellite&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>view.
</td>
</tr>
<tr VALIGN=top>
<td> epy </td>
<td> No </td>
<td> numeric </td>
<td> Latitude error estimate in meters, 95% confidence. Present<br />
&nbsp;<wbr>&nbsp;<wbr>if mode is 2 or 3 and DOPs can be calculated from the satellite&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>view.
</td>
</tr>
<tr VALIGN=top>
<td> epv </td>
<td> No </td>
<td> numeric </td>
<td> Estimated vertical error in meters, 95% confidence. Present<br />
&nbsp;<wbr>&nbsp;<wbr>if mode is 3 and DOPs can be calculated from the satellite&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>view.
</td>
</tr>
<tr VALIGN=top>
<td> track </td>
<td> No </td>
<td> numeric </td>
<td> Course over ground, degrees from true north.
</td>
</tr>
<tr VALIGN=top>
<td> speed </td>
<td> No </td>
<td> numeric </td>
<td> Speed over ground, meters per second.
</td>
</tr>
<tr VALIGN=top>
<td> climb </td>
<td> No </td>
<td> numeric </td>
<td> Climb (positive) or sink (negative) rate, meters per <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>second.</p>
</td>
</tr>
<tr VALIGN=top>
<td> epd </td>
<td> No </td>
<td> numeric </td>
<td> Direction error estimate in degrees, 95% confidence.
</td>
</tr>
<tr VALIGN=top>
<td> eps </td>
<td> No </td>
<td> numeric </td>
<td> Speed error estinmate in meters/sec, 95% confidence.
</td>
</tr>
<tr VALIGN=top>
<td> epc </td>
<td> No </td>
<td> numeric </td>
<td> Climb/sink error estimate in meters/sec, 95% confidence.
</td>
</tr>
</table>
<p> When the C client library parses a response of this kind, it will assert validity bits in the top-level set member for each field actually received; see gps.h for bitmask names and values. </p>
<p> Here&#8217;s an example: </p>
<dl>
<dd>
<pre>{&quot;class&quot;:&quot;TPV&quot;,&quot;tag&quot;:&quot;MID2&quot;,&quot;device&quot;:&quot;/dev/pts/1&quot;,
 &quot;time&quot;:&quot;2005-06-08T10:34:48.283Z&quot;,&quot;ept&quot;:0.005,
 &quot;lat&quot;:46.498293369,&quot;lon&quot;:7.567411672,&quot;alt&quot;:1343.127,
 &quot;eph&quot;:36.000,&quot;epv&quot;:32.321,
 &quot;track&quot;:10.3788,&quot;speed&quot;:0.091,&quot;climb&quot;:-0.085,&quot;mode&quot;:3}</pre>
</dl>
</dl>
<p> SKY</p>
<dl>
<dd>A SKY object reports a sky view of the GPS satellite positions. If there is no GPS device available, or no skyview has been reported yet, only the &quot;class&quot; field will reliably be present. </p>
<p> <code>Table 2. SKY object</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Always? </code></td>
<td><code> Type </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> class </td>
<td> Yes </td>
<td> string </td>
<td> Fixed: &quot;SKY&quot;
</td>
</tr>
<tr VALIGN=top>
<td> tag </td>
<td> No </td>
<td> string </td>
<td> Type tag associated with this GPS sentence; from an NMEA <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>device this is just the NMEA sentence type.</p>
</td>
</tr>
<tr VALIGN=top>
<td> device </td>
<td> No </td>
<td> string </td>
<td> Name of originating device
</td>
</tr>
<tr VALIGN=top>
<td> time </td>
<td> No </td>
<td> numeric </td>
<td> Time/date stamp in ISO8601 format, UTC. May have a <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fractional part of up to .001sec precision.</p>
</td>
</tr>
<tr VALIGN=top>
<td> xdop </td>
<td> No </td>
<td> numeric </td>
<td> Longitudinal dilution of precision, a dimensionless <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>factor which should be multiplied by a base UERE to get an<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>error estimate.</p>
</td>
</tr>
<tr VALIGN=top>
<td> ydop </td>
<td> No </td>
<td> numeric </td>
<td> Latitudinal dilution of precision, a dimensionless <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>factor which should be multiplied by a base UERE to get an<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>error estimate.</p>
</td>
</tr>
<tr VALIGN=top>
<td> vdop </td>
<td> No </td>
<td> numeric </td>
<td> Altitude dilution of precision, a dimensionless <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>factor which should be multiplied by a base UERE to get an<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>error estimate.</p>
</td>
</tr>
<tr VALIGN=top>
<td> tdop </td>
<td> No </td>
<td> numeric </td>
<td> Time dilution of precision, a dimensionless <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>factor which should be multiplied by a base UERE to get an<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>error estimate.</p>
</td>
</tr>
<tr VALIGN=top>
<td> hdop </td>
<td> No </td>
<td> numeric </td>
<td> Horizontal dilution of precision, a dimensionless <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>factor which should be multiplied by a base UERE to get a<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>circular error estimate.</p>
</td>
</tr>
<tr VALIGN=top>
<td> pdop </td>
<td> No </td>
<td> numeric </td>
<td> Spherical dilution of precision, a dimensionless <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>factor which should be multiplied by a base UERE to get an<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>error estimate.</p>
</td>
</tr>
<tr VALIGN=top>
<td> gdop </td>
<td> No </td>
<td> numeric </td>
<td> Hyperspherical dilution of precision, a dimensionless <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>factor which should be multiplied by a base UERE to get an<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>error estimate.</p>
</td>
</tr>
<tr VALIGN=top>
<td> satellites </td>
<td> Yes </td>
<td> list </td>
<td> List of satellite objects in skyview
</td>
</tr>
</table>
<p> Many devices compute dilution of precision factors but do not include them in their reports. Many that do report DOPs report only HDOP, two-dimensional circular error. gpsd always passes through whatever the device actually reports, then attempts to fill in other DOPs by calculating the appropriate determinants in a covariance matrix based on the satellite view. DOPs may be missing if some of these determinants are singular. It can even happen that the device reports an error estimate in meters when the corresponding DOP is unavailable; some devices use more sophisticated error modeling than the covariance calculation. </p>
<p> The satellite list objects have the following elements: </p>
<p> <code>Table 3. Satellite object</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Always? </code></td>
<td><code> Type </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> PRN </td>
<td> Yes </td>
<td> numeric </td>
<td> PRN ID of the satellite. 1-63 are GNSS satellites, <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>64-96 are GLONASS satellites, 100-164 are SBAS satellites</p>
</td>
</tr>
<tr VALIGN=top>
<td> az </td>
<td> Yes </td>
<td> numeric </td>
<td> Azimuth, degrees from true north.
</td>
</tr>
<tr VALIGN=top>
<td> el </td>
<td> Yes </td>
<td> numeric </td>
<td> Elevation in degrees.
</td>
</tr>
<tr VALIGN=top>
<td> ss </td>
<td> Yes </td>
<td> numeric </td>
<td> Signal strength in dB.
</td>
</tr>
<tr VALIGN=top>
<td> used </td>
<td> Yes </td>
<td> boolean </td>
<td> Used in current solution? (SBAS/WAAS/EGNOS satellites <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>may be flagged used if the solution has corrections from them,<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>but not all drivers make this information available.)</p>
</td>
</tr>
</table>
<p> Note that satellite objects do not have a &quot;class&quot; field, as they are never shipped outside of a SKY object. </p>
<p> When the C client library parses a SKY response, it will assert the SATELLITE_SET bit in the top-level set member. </p>
<p> Here&#8217;s an example: </p>
<dl>
<dd>
<pre>{&quot;class&quot;:&quot;SKY&quot;,&quot;tag&quot;:&quot;MID2&quot;,&quot;device&quot;:&quot;/dev/pts/1&quot;,
 &quot;time&quot;:&quot;2005-07-08T11:28:07.114Z&quot;,
 &quot;xdop&quot;:1.55,&quot;hdop&quot;:1.24,&quot;pdop&quot;:1.99,
 &quot;satellites&quot;:[
 {&quot;PRN&quot;:23,&quot;el&quot;:6,&quot;az&quot;:84,&quot;ss&quot;:0,&quot;used&quot;:false},
 {&quot;PRN&quot;:28,&quot;el&quot;:7,&quot;az&quot;:160,&quot;ss&quot;:0,&quot;used&quot;:false},
 {&quot;PRN&quot;:8,&quot;el&quot;:66,&quot;az&quot;:189,&quot;ss&quot;:44,&quot;used&quot;:true},
 {&quot;PRN&quot;:29,&quot;el&quot;:13,&quot;az&quot;:273,&quot;ss&quot;:0,&quot;used&quot;:false},
 {&quot;PRN&quot;:10,&quot;el&quot;:51,&quot;az&quot;:304,&quot;ss&quot;:29,&quot;used&quot;:true},
 {&quot;PRN&quot;:4,&quot;el&quot;:15,&quot;az&quot;:199,&quot;ss&quot;:36,&quot;used&quot;:true},
 {&quot;PRN&quot;:2,&quot;el&quot;:34,&quot;az&quot;:241,&quot;ss&quot;:43,&quot;used&quot;:true},
 {&quot;PRN&quot;:27,&quot;el&quot;:71,&quot;az&quot;:76,&quot;ss&quot;:43,&quot;used&quot;:true}]}</pre>
</dl>
</dl>
<p> GST</p>
<dl>
<dd>A GST object is a pseudorange noise report. </p>
<p> <code>Table 4. GST object</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Always? </code></td>
<td><code> Type </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> class </td>
<td> Yes </td>
<td> string </td>
<td> Fixed: &quot;GST&quot;
</td>
</tr>
<tr VALIGN=top>
<td> tag </td>
<td> No </td>
<td> string </td>
<td> Type tag associated with this GPS sentence; from an NMEA device this is just the NMEA sentence type.
</td>
</tr>
<tr VALIGN=top>
<td> device </td>
<td> No </td>
<td> string </td>
<td> Name of originating device
</td>
</tr>
<tr VALIGN=top>
<td> time </td>
<td> No </td>
<td> numeric </td>
<td> Seconds since the Unix epoch, UTC. May have a fractional part of up to .001sec precision.
</td>
</tr>
<tr VALIGN=top>
<td> rms </td>
<td> No </td>
<td> numeric </td>
<td> Value of the standard deviation of the range inputs to the navigation process (range inputs include pseudoranges and DGPS corrections).
</td>
</tr>
<tr VALIGN=top>
<td> major </td>
<td> No </td>
<td> numeric </td>
<td> Standard deviation of semi-major axis of error ellipse, in meters.
</td>
</tr>
<tr VALIGN=top>
<td> minor </td>
<td> No </td>
<td> numeric </td>
<td> Standard deviation of semi-minor axis of error ellipse, in meters.
</td>
</tr>
<tr VALIGN=top>
<td> orient </td>
<td> No </td>
<td> numeric </td>
<td> Orientation of semi-major axis of error ellipse, in degrees from true north.
</td>
</tr>
<tr VALIGN=top>
<td> lat </td>
<td> No </td>
<td> numeric </td>
<td> Standard deviation of latitude error, in meters.
</td>
</tr>
<tr VALIGN=top>
<td> lon </td>
<td> No </td>
<td> numeric </td>
<td> Standard deviation of longitude error, in meters.
</td>
</tr>
<tr VALIGN=top>
<td> alt </td>
<td> No </td>
<td> numeric </td>
<td> Standard deviation of altitude error, in meters.
</td>
</tr>
</table>
<p> Here&#8217;s an example: </p>
<dl>
<dd>
<pre>{&quot;class&quot;:&quot;GST&quot;,&quot;tag&quot;:&quot;GST&quot;,&quot;device&quot;:&quot;/dev/ttyUSB0&quot;,
 &quot;time&quot;:&quot;2010-12-07T10:23:07.096Z&quot;,&quot;rms&quot;:2.440,
 &quot;major&quot;:1.660,&quot;minor&quot;:1.120,&quot;orient&quot;:68.989,
 &quot;lat&quot;:1.600,&quot;lon&quot;:1.200,&quot;alt&quot;:2.520}</pre>
</dl>
</dl>
<p> ATT</p>
<dl>
<dd>An ATT object is a vehicle-attitude report. It is returned by digital-compass and gyroscope sensors; depending on device, it may include: heading, pitch, roll, yaw, gyroscope, and magnetic-field readings. Because such sensors are often bundled as part of marine-navigation systems, the ATT response may also include water depth. </p>
<p> The &quot;class&quot;, &quot;mode&quot;, and &quot;tag&quot; fields will reliably be present. Others may be reported or not depending on the specific device type. </p>
<p> <code>Table 5. ATT object</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Always? </code></td>
<td><code> Type </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> class </td>
<td> Yes </td>
<td> string </td>
<td> Fixed: &quot;ATT&quot;
</td>
</tr>
<tr VALIGN=top>
<td> tag </td>
<td> Yes </td>
<td> string </td>
<td> Type tag associated with this GPS sentence; from an NMEA <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>device this is just the NMEA sentence type.</p>
</td>
</tr>
<tr VALIGN=top>
<td> device </td>
<td> Yes </td>
<td> string </td>
<td> Name of originating device
</td>
</tr>
<tr VALIGN=top>
<td> time </td>
<td> Yes </td>
<td> numeric </td>
<td> Seconds since the Unix epoch, UTC. May have a <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fractional part of up to .001sec precision.</p>
</td>
</tr>
<tr VALIGN=top>
<td> heading </td>
<td> No </td>
<td> numeric </td>
<td> Heading, degrees from true north.
</td>
</tr>
<tr VALIGN=top>
<td> mag_st </td>
<td> No </td>
<td> string </td>
<td> Magnetometer status.
</td>
</tr>
<tr VALIGN=top>
<td> pitch </td>
<td> No </td>
<td> numeric </td>
<td> Pitch in degrees.
</td>
</tr>
<tr VALIGN=top>
<td> pitch_st </td>
<td> No </td>
<td> string </td>
<td> Pitch sensor status.
</td>
</tr>
<tr VALIGN=top>
<td> yaw </td>
<td> No </td>
<td> numeric </td>
<td> Yaw in degrees
</td>
</tr>
<tr VALIGN=top>
<td> yaw_st </td>
<td> No </td>
<td> string </td>
<td> Yaw sensor status.
</td>
</tr>
<tr VALIGN=top>
<td> roll </td>
<td> No </td>
<td> numeric </td>
<td> Roll in degrees.
</td>
</tr>
<tr VALIGN=top>
<td> roll_st </td>
<td> No </td>
<td> string </td>
<td> Roll sensor status.
</td>
</tr>
<tr VALIGN=top>
<td> dip </td>
<td> No </td>
<td> numeric </td>
<td> Local magnetic inclination, degrees, positive when the magnetic field points downward (into the Earth).
</td>
</tr>
<tr VALIGN=top>
<td> mag_len </td>
<td> No </td>
<td> numeric </td>
<td> Scalar magnetic field strength.
</td>
</tr>
<tr VALIGN=top>
<td> mag_x </td>
<td> No </td>
<td> numeric </td>
<td> X component of magnetic field strength.
</td>
</tr>
<tr VALIGN=top>
<td> mag_y </td>
<td> No </td>
<td> numeric </td>
<td> Y component of magnetic field strength.
</td>
</tr>
<tr VALIGN=top>
<td> mag_z </td>
<td> No </td>
<td> numeric </td>
<td> Z component of magnetic field strength.
</td>
</tr>
<tr VALIGN=top>
<td> acc_len </td>
<td> No </td>
<td> numeric </td>
<td> Scalar acceleration.
</td>
</tr>
<tr VALIGN=top>
<td> acc_x </td>
<td> No </td>
<td> numeric </td>
<td> X component of acceleration.
</td>
</tr>
<tr VALIGN=top>
<td> acc_y </td>
<td> No </td>
<td> numeric </td>
<td> Y component of acceleration.
</td>
</tr>
<tr VALIGN=top>
<td> acc_z </td>
<td> No </td>
<td> numeric </td>
<td> Z component of acceleration.
</td>
</tr>
<tr VALIGN=top>
<td> gyro_x </td>
<td> No </td>
<td> numeric </td>
<td> X component of acceleration.
</td>
</tr>
<tr VALIGN=top>
<td> gyro_y </td>
<td> No </td>
<td> numeric </td>
<td> Y component of acceleration.
</td>
</tr>
<tr VALIGN=top>
<td> depth </td>
<td> No </td>
<td> numeric </td>
<td> Water depth in meters.
</td>
</tr>
<tr VALIGN=top>
<td> temperature </td>
<td> No </td>
<td> numeric </td>
<td> Temperature at sensor, degrees centigrade.
</td>
</tr>
</table>
<p> The heading, pitch, and roll status codes (if present) vary by device. For the TNT Revolution digital compasses, they are coded as follows: </p>
<p> <code>Table 6. Device flags</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Code </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> C </td>
<td> magnetometer calibration alarm
</td>
</tr>
<tr VALIGN=top>
<td> L </td>
<td> low alarm
</td>
</tr>
<tr VALIGN=top>
<td> M </td>
<td> low warning
</td>
</tr>
<tr VALIGN=top>
<td> N </td>
<td> normal
</td>
</tr>
<tr VALIGN=top>
<td> O </td>
<td> high warning
</td>
</tr>
<tr VALIGN=top>
<td> P </td>
<td> high alarm
</td>
</tr>
<tr VALIGN=top>
<td> V </td>
<td> magnetometer voltage level alarm
</td>
</tr>
</table>
<p> When the C client library parses a response of this kind, it will assert ATT_IS. </p>
<p> Here&#8217;s an example: </p>
<dl>
<dd>
<pre>{&quot;class&quot;:&quot;ATT&quot;,&quot;tag&quot;:&quot;PTNTHTM&quot;,&quot;time&quot;:1270938096.843,
 &quot;heading&quot;:14223.00,&quot;mag_st&quot;:&quot;N&quot;,
 &quot;pitch&quot;:169.00,&quot;pitch_st&quot;:&quot;N&quot;, &quot;roll&quot;:-43.00,&quot;roll_st&quot;:&quot;N&quot;,
 &quot;dip&quot;:13641.000,&quot;mag_x&quot;:2454.000}</pre>
</dl>
</dl>
<p> And here are the commands: </p>
<p> ?VERSION;</p>
<dl>
<dd>Returns an object with the following attributes: </p>
<p> <code>Table 7. VERSION object</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Always? </code></td>
<td><code> Type </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> class </td>
<td> Yes </td>
<td> string </td>
<td> Fixed: &quot;VERSION&quot;
</td>
</tr>
<tr VALIGN=top>
<td> release </td>
<td> Yes </td>
<td> string </td>
<td> Public release level
</td>
</tr>
<tr VALIGN=top>
<td> rev </td>
<td> Yes </td>
<td> string </td>
<td> Internal revision-control level.
</td>
</tr>
<tr VALIGN=top>
<td> proto_major </td>
<td> Yes </td>
<td> numeric </td>
<td> API major revision level.
</td>
</tr>
<tr VALIGN=top>
<td> proto_minor </td>
<td> Yes </td>
<td> numeric </td>
<td> API minor revision level.
</td>
</tr>
<tr VALIGN=top>
<td> remote </td>
<td> No </td>
<td> string </td>
<td> URL of the remote daemon reporting this version. If<br />
&nbsp;<wbr>&nbsp;<wbr>empty, this is the version of the local daemon.
</td>
</tr>
</table>
<p> The daemon ships a VERSION response to each client when the client first connects to it. </p>
<p> When the C client library parses a response of this kind, it will assert the VERSION_SET bit in the top-level set member. </p>
<p> Here&#8217;s an example: </p>
<dl>
<dd>
<pre>{&quot;class&quot;:&quot;VERSION&quot;,&quot;version&quot;:&quot;2.40dev&quot;,
 &quot;rev&quot;:&quot;06f62e14eae9886cde907dae61c124c53eb1101f&quot;,
 &quot;proto_major&quot;:3,&quot;proto_minor&quot;:1
}</pre>
</dl>
</dl>
<p> ?DEVICES;</p>
<dl>
<dd>Returns a device list object with the following elements: </p>
<p> <code>Table 8. DEVICES object</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Always? </code></td>
<td><code> Type </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> class </td>
<td> Yes </td>
<td> string </td>
<td> Fixed: &quot;DEVICES&quot;
</td>
</tr>
<tr VALIGN=top>
<td> devices </td>
<td> Yes </td>
<td> list </td>
<td> List of device descriptions
</td>
</tr>
<tr VALIGN=top>
<td> remote </td>
<td> No </td>
<td> string </td>
<td> URL of the remote daemon reporting the device set. If<br />
&nbsp;<wbr>&nbsp;<wbr>empty, this is a DEVICES response from the local daemon.
</td>
</tr>
</table>
<p> When the C client library parses a response of this kind, it will assert the DEVICELIST_SET bit in the top-level set member. </p>
<p> Here&#8217;s an example: </p>
<dl>
<dd>
<pre>{&quot;class&quot;=&quot;DEVICES&quot;,&quot;devices&quot;:[
 {&quot;class&quot;:&quot;DEVICE&quot;,&quot;path&quot;:&quot;/dev/pts/1&quot;,&quot;flags&quot;:1,&quot;driver&quot;:&quot;SiRF binary&quot;},
 {&quot;class&quot;:&quot;DEVICE&quot;,&quot;path&quot;:&quot;/dev/pts/3&quot;,&quot;flags&quot;:4,&quot;driver&quot;:&quot;AIVDM&quot;}]}</pre>
</dl>
<p> The daemon occasionally ships a bare DEVICE object to the client (that is, one not inside a DEVICES wrapper). The data content of these objects will be described later as a response to the ?DEVICE command.</dl>
<p> ?WATCH;</p>
<dl>
<dd>This command sets watcher mode. It also sets or elicits a report of per-subscriber policy and the raw bit. An argument WATCH object changes the subscriber&#8217;s policy. The response describes the subscriber&#8217;s policy. The response will also include a DEVICES object. </p>
<p> A WATCH object has the following elements: </p>
<p> <code>Table 9. WATCH object</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Always? </code></td>
<td><code> Type </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> class </td>
<td> Yes </td>
<td> string </td>
<td> Fixed: &quot;WATCH&quot;
</td>
</tr>
<tr VALIGN=top>
<td> enable </td>
<td> No </td>
<td> boolean </td>
<td> Enable (true) or disable (false) watcher mode. Default <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>is true.</p>
</td>
</tr>
<tr VALIGN=top>
<td> json </td>
<td> No </td>
<td> boolean </td>
<td> Enable (true) or disable (false) dumping of JSON reports. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Default is false.</p>
</td>
</tr>
<tr VALIGN=top>
<td> nmea </td>
<td> No </td>
<td> boolean </td>
<td> Enable (true) or disable (false) dumping of binary <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>packets as pseudo-NMEA. Default<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>is false.</p>
</td>
</tr>
<tr VALIGN=top>
<td> raw </td>
<td> No </td>
<td> integer </td>
<td> Controls &#8216;raw&#8217; mode. When this attribute is set to 1 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>for a channel, gpsd reports the<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>unprocessed NMEA or AIVDM data stream from whatever device is attached.<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Binary GPS packets are hex-dumped. RTCM2 and RTCM3</p>
<p>&nbsp;<wbr>&nbsp;<wbr>packets are not dumped in raw mode. When this attribute is set to <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>2 for a channel that processes binary data,<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gpsd reports the received data verbatim<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>without hex-dumping.</p>
</td>
</tr>
<tr VALIGN=top>
<td> scaled </td>
<td> No </td>
<td> boolean </td>
<td> If true, apply scaling divisors to output before <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>dumping; default is false.</p>
</td>
</tr>
<tr VALIGN=top>
<td> split24 </td>
<td> No </td>
<td> boolean </td>
<td> If true, aggregate AIS type24 sentence parts. If false,<br />
&nbsp;<wbr>&nbsp;<wbr>report each part as a separate JSON object, leaving the<br />
&nbsp;<wbr>&nbsp;<wbr>client to match MMSIs and aggregate.&nbsp;<wbr>&nbsp;<wbr>Default is<br />
&nbsp;<wbr>&nbsp;<wbr>false. Applies only to AIS reports.
</td>
</tr>
<tr VALIGN=top>
<td> pps </td>
<td> No </td>
<td> boolean </td>
<td> If true, emit a PPS bar when the device issues<br />
&nbsp;<wbr>&nbsp;<wbr>1PPS.&nbsp;<wbr>&nbsp;<wbr>Intended to be used with the&nbsp;<wbr>&quot;nmea&quot;&nbsp;<wbr>and&nbsp;<wbr>&quot;raw&quot;&nbsp;<wbr>modes.<br />
&nbsp;<wbr>&nbsp;<wbr>Default is false.&nbsp;<wbr><code>Note: this is an<br />
&nbsp;<wbr>&nbsp;<wbr>unstable experimental feature which may change or be removed<br />
&nbsp;<wbr>&nbsp;<wbr>without notice.</code>
</td>
</tr>
<tr VALIGN=top>
<td> device </td>
<td> No </td>
<td> string </td>
<td> If present, enable watching only of the specified device <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>rather than all devices. Useful with raw and NMEA modes<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>in which device responses aren&#8217;t tagged. Has no effect when<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>used with enable:false.</p>
</td>
</tr>
<tr VALIGN=top>
<td> remote </td>
<td> No </td>
<td> string </td>
<td> URL of the remote daemon reporting the watch set. If<br />
&nbsp;<wbr>&nbsp;<wbr>empty, this is a WATCH response from the local daemon.
</td>
</tr>
</table>
<p> There is an additional boolean &quot;timing&quot; attribute which is undocumented because that portion of the interface is considered unstable and for developer use only. </p>
<p> In watcher mode, GPS reports are dumped as TPV and SKY responses. AIS, Subframe and RTCM reporting is described in the next section. </p>
<p> When the C client library parses a response of this kind, it will assert the POLICY_SET bit in the top-level set member. </p>
<p> Here&#8217;s an example: </p>
<dl>
<dd>
<pre>{&quot;class&quot;:&quot;WATCH&quot;, &quot;raw&quot;:1,&quot;scaled&quot;:true}</pre>
</dl>
</dl>
<p> ?POLL;</p>
<dl>
<dd>The POLL command requests data from the last-seen fixes on all active GPS devices. Devices must previously have been activated by ?WATCH to be pollable. </p>
<p> Polling can lead to possibly surprising results when it is used on a device such as an NMEA GPS for which a complete fix has to be accumulated from several sentences. If you poll while those sentences are being emitted, the response will contain the last complete fix data and may be as much as one cycle time (typically 1 second) stale. </p>
<p> The POLL response will contain a timestamped list of TPV objects describing cached data, and a timestamped list of SKY objects describing satellite configuration. If a device has not seen fixes, it will be reported with a mode field of zero. </p>
<p> <code>Table 10. POLL object</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Always? </code></td>
<td><code> Type </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> class </td>
<td> Yes </td>
<td> string </td>
<td> Fixed: &quot;POLL&quot;
</td>
</tr>
<tr VALIGN=top>
<td> time </td>
<td> Yes </td>
<td> Numeric </td>
<td> Timestamp in ISO 8601 format. May have a <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>fractional part of up to .001sec precision.</p>
</td>
</tr>
<tr VALIGN=top>
<td> active </td>
<td> Yes </td>
<td> Numeric </td>
<td> Count of active devices.
</td>
</tr>
<tr VALIGN=top>
<td> fixes </td>
<td> Yes </td>
<td> JSON array </td>
<td> Comma-separated list of TPV objects.
</td>
</tr>
<tr VALIGN=top>
<td> skyviews </td>
<td> Yes </td>
<td> JSON array </td>
<td> Comma-separated list of SKY objects.
</td>
</tr>
</table>
<p> Here&#8217;s an example of a POLL response: </p>
<dl>
<dd>
<pre>{&quot;class&quot;:&quot;POLL&quot;,&quot;time&quot;:&quot;2010-06-04T10:31:00.289Z&quot;,&quot;active&quot;:1,
 &quot;tpv&quot;:[{&quot;class&quot;:&quot;TPV&quot;,&quot;tag&quot;:&quot;MID41&quot;,&quot;device&quot;:&quot;/dev/ttyUSB0&quot;,
 &quot;time&quot;:&quot;2010-09-08T13:33:06.095Z&quot;,
 &quot;ept&quot;:0.005,&quot;lat&quot;:40.035093060,
 &quot;lon&quot;:-75.519748733,&quot;track&quot;:99.4319,&quot;speed&quot;:0.123,&quot;mode&quot;:2}],
 &quot;sky&quot;:[{&quot;class&quot;:&quot;SKY&quot;,&quot;tag&quot;:&quot;MID41&quot;,&quot;device&quot;:&quot;/dev/ttyUSB0&quot;,
 &quot;time&quot;:1270517264.240,&quot;hdop&quot;:9.20,
 &quot;satellites&quot;:[{&quot;PRN&quot;:16,&quot;el&quot;:55,&quot;az&quot;:42,&quot;ss&quot;:36,&quot;used&quot;:true},
 {&quot;PRN&quot;:19,&quot;el&quot;:25,&quot;az&quot;:177,&quot;ss&quot;:0,&quot;used&quot;:false},
 {&quot;PRN&quot;:7,&quot;el&quot;:13,&quot;az&quot;:295,&quot;ss&quot;:0,&quot;used&quot;:false},
 {&quot;PRN&quot;:6,&quot;el&quot;:56,&quot;az&quot;:135,&quot;ss&quot;:32,&quot;used&quot;:true},
 {&quot;PRN&quot;:13,&quot;el&quot;:47,&quot;az&quot;:304,&quot;ss&quot;:0,&quot;used&quot;:false},
 {&quot;PRN&quot;:23,&quot;el&quot;:66,&quot;az&quot;:259,&quot;ss&quot;:0,&quot;used&quot;:false},
 {&quot;PRN&quot;:20,&quot;el&quot;:7,&quot;az&quot;:226,&quot;ss&quot;:0,&quot;used&quot;:false},
 {&quot;PRN&quot;:3,&quot;el&quot;:52,&quot;az&quot;:163,&quot;ss&quot;:32,&quot;used&quot;:true},
 {&quot;PRN&quot;:31,&quot;el&quot;:16,&quot;az&quot;:102,&quot;ss&quot;:0,&quot;used&quot;:false}
]}]}</pre>
</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 Client software should not assume the field inventory of the POLL response is fixed for all time. As gpsd collects and caches more data from more sensor types, those data are likely to find their way into this response. </p>
</dl>
</dl>
<p> PPS</p>
<dl>
<dd>This message is emitted each time the daemon sees a PPS (Pulse Per Second) strobe from a device. </p>
<p> A PPS object has the following elements: </p>
<p> <code>Table 11. PPS object</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Always? </code></td>
<td><code> Type </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> class </td>
<td> Yes </td>
<td> string </td>
<td> Fixed: &quot;PPS&quot;
</td>
</tr>
<tr VALIGN=top>
<td> device </td>
<td> Yes </td>
<td> string </td>
<td> Name of originating device
</td>
</tr>
<tr VALIGN=top>
<td> real_sec </td>
<td> Yes </td>
<td> numeric </td>
<td> seconds from the realtime clock
</td>
</tr>
<tr VALIGN=top>
<td> real_nsec </td>
<td> Yes </td>
<td> numeric </td>
<td> nanoseconds from the realtime clock
</td>
</tr>
<tr VALIGN=top>
<td> clock_sec </td>
<td> Yes </td>
<td> numeric </td>
<td> seconds from the system clock
</td>
</tr>
<tr VALIGN=top>
<td> clock_nsec </td>
<td> Yes </td>
<td> numeric </td>
<td> nanoseconds from the system clock
</td>
</tr>
</table>
<p> This message is emitted once per second to watchers of a device emitting PPS, and is intended to report the drift between the start of the GPS second and seconds as reported by the system clock (which may be NTP-corrected). </p>
<p> The message contains second/microsecond pairs for two clocks; the realtime clock without NTP correction (the result of clock_gettime(CLOCK_REALTIME), but only to microsecond precision) and the ordinary system clock (which may be NTP corrected). </p>
<p> There are various sources of error in the reported clock times. For PPS delivered via a real serial-line strobe, serial-interrupt latency plus processing time to the timer call should be bounded above by about 10 microseconds; USB-to-serial control-line emulation is known to add jitter of about 50 microseconds. (Both figures are for GPSD running in non-realtime mode on an x86 with a gigahertz clock and are estimates based on measured latency in other applications) </p>
<p> Here&#8217;s an example: </p>
<dl>
<dd>
<pre>{&quot;class&quot;:&quot;PPS&quot;,&quot;device&quot;:&quot;/dev/ttyUSB0&quot;,
 &quot;real_sec&quot;:1330212592, &quot;real_nsec&quot;:343182,
 &quot;clock_sec&quot;:1330212592,&quot;clock_nsec&quot;:343184}</pre>
</dl>
</dl>
<p> ?DEVICE</p>
<dl>
<dd>This command reports (when followed by &#8216;;&#8217;) the state of a device, or sets (when followed by &#8216;=&#8217; and a DEVICE object) device-specific control bits, notably the device&#8217;s speed and serial mode and the native-mode bit. The parameter-setting form will be rejected if more than one client is attached to the channel. </p>
<p> Pay attention to the response, because it is possible for this command to fail if the GPS does not support a speed-switching command or only supports some combinations of serial modes. In case of failure, the daemon and GPS will continue to communicate at the old speed. </p>
<p> Use the parameter-setting form with caution. On USB and Bluetooth GPSes it is also possible for serial mode setting to fail either because the serial adaptor chip does not support non-8N1 modes or because the device firmware does not properly synchronize the serial adaptor chip with the UART on the GPS chipset when the speed changes. These failures can hang your device, possibly requiring a GPS power cycle or (in extreme cases) physically disconnecting the NVRAM backup battery. </p>
<p> A DEVICE object has the following elements: </p>
<p> <code>Table 12. CONFIGCHAN object</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Always? </code></td>
<td><code> Type </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> class </td>
<td> Yes </td>
<td> string </td>
<td> Fixed: &quot;DEVICE&quot;
</td>
</tr>
<tr VALIGN=top>
<td> path </td>
<td> No </td>
<td> string </td>
<td> Name the device for which the control bits are <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>being reported, or for which they are to be applied. This</p>
<p>&nbsp;<wbr>&nbsp;<wbr>attribute may be omitted only when there is exactly one<br />
&nbsp;<wbr>&nbsp;<wbr>subscribed channel.
</td>
</tr>
<tr VALIGN=top>
<td> activated </td>
<td> No </td>
<td> string </td>
<td> Time the device was activated as an ISO8601<br />
&nbsp;<wbr>&nbsp;<wbr>timestamp. If the device is inactive this attribute is<br />
&nbsp;<wbr>&nbsp;<wbr>absent.
</td>
</tr>
<tr VALIGN=top>
<td> flags </td>
<td> No </td>
<td> integer </td>
<td> Bit vector of property flags. Currently defined flags are:<br />
&nbsp;<wbr>&nbsp;<wbr>describe packet types seen so far&nbsp;<wbr>(GPS, RTCM2, RTCM3, <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>AIS). Won&#8217;t be reported if empty, e.g. before<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gpsd has seen identifiable packets<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>from the device.</p>
</td>
</tr>
<tr VALIGN=top>
<td> driver </td>
<td> No </td>
<td> string </td>
<td> GPSD&#8217;s name for the device driver type. Won&#8217;t be reported before <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>gpsd has seen identifiable packets<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>from the device.</p>
</td>
</tr>
<tr VALIGN=top>
<td> subtype </td>
<td> When the daemon sees a delayed response to a probe for <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>subtype or firmware-version information.
 </td>
<td> string </td>
<td> Whatever version information the device returned.
</td>
</tr>
<tr VALIGN=top>
<td> bps </td>
<td> No </td>
<td> integer </td>
<td> Device speed in bits per second.
</td>
</tr>
<tr VALIGN=top>
<td> parity </td>
<td> Yes </td>
<td> string </td>
<td> N, O or E for no parity, odd, or even.
</td>
</tr>
<tr VALIGN=top>
<td> stopbits </td>
<td> Yes </td>
<td> string </td>
<td> Stop bits (1 or 2).
</td>
</tr>
<tr VALIGN=top>
<td> native </td>
<td> No </td>
<td> integer </td>
<td> 0 means NMEA mode and 1 means <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>alternate mode (binary if it has one, for SiRF and Evermore chipsets<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>in particular). Attempting to set this mode on a non-GPS<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>device will yield an error.</p>
</td>
</tr>
<tr VALIGN=top>
<td> cycle </td>
<td> No </td>
<td> real </td>
<td> Device cycle time in seconds.
</td>
</tr>
<tr VALIGN=top>
<td> mincycle </td>
<td> No </td>
<td> real </td>
<td> Device minimum cycle time in seconds. Reported from <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>?CONFIGDEV when (and only when) the rate is switchable. It is<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>read-only and not settable.</p>
</td>
</tr>
</table>
<p> The serial parameters will be omitted in a response describing a TCP/IP source such as an Ntrip, DGPSIP, or AIS feed. </p>
<p> The contents of the flags field should be interpreted as follows: </p>
<p> <code>Table 13. Device flags</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> C #define </code></td>
<td><code> Value </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> SEEN_GPS </td>
<td> 0x01 </td>
<td> GPS data has been seen on this device
</td>
</tr>
<tr VALIGN=top>
<td> SEEN_RTCM2 </td>
<td> 0x02 </td>
<td> RTCM2 data has been seen on this device
</td>
</tr>
<tr VALIGN=top>
<td> SEEN_RTCM3 </td>
<td> 0x04 </td>
<td> RTCM3 data has been seen on this device
</td>
</tr>
<tr VALIGN=top>
<td> SEEN_AIS </td>
<td> 0x08 </td>
<td> AIS data has been seen on this device
</td>
</tr>
</table>
<p> When the C client library parses a response of this kind, it will assert the DEVICE_SET bit in the top-level set member. </p>
<p> Here&#8217;s an example: </p>
<dl>
<dd>
<pre>{&quot;class&quot;:&quot;DEVICE&quot;,&quot;bps&quot;:4800,&quot;parity&quot;:&quot;N&quot;,&quot;stopbits&quot;:1,&quot;native&quot;:0}</pre>
</dl>
</dl>
<p> When a client is in watcher mode, the daemon will ship it DEVICE notifications when a device is added to the pool or deactivated. </p>
<p> When the C client library parses a response of this kind, it will assert the DEVICE_SET bit in the top-level set member. </p>
<p> Here&#8217;s an example: </p>
<dl>
<dd>
<pre>{&quot;class&quot;:&quot;DEVICE&quot;,&quot;path&quot;:&quot;/dev/pts1&quot;,&quot;activated&quot;:0}</pre>
</dl>
<p> The daemon may ship an error object in response to a syntactically invalid command line or unknown command. It has the following elements: </p>
<p> <code>Table 14. ERROR notification object</code> </p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Always? </code></td>
<td><code> Type </code></td>
<td><code> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> class </td>
<td> Yes </td>
<td> string </td>
<td> Fixed: &quot;ERROR&quot;
</td>
</tr>
<tr VALIGN=top>
<td> message </td>
<td> Yes </td>
<td> string </td>
<td> Textual error message
</td>
</tr>
</table>
<p> Here&#8217;s an example: </p>
<dl>
<dd>
<pre>{&quot;class&quot;:&quot;ERROR&quot;,&quot;message&quot;:&quot;Unrecognized request '?FOO'&quot;}</pre>
</dl>
<p> When the C client library parses a response of this kind, it will assert the ERR_SET bit in the top-level set member.</p>
<h2>Rtcm2</h2>
<p>RTCM-104 is a family of serial protocols used for broadcasting pseudorange corrections from differential-GPS reference stations. Many GPS receivers can accept these corrections to improve their reporting accuracy. </p>
<p> RTCM-104 comes in two major and incompatible flavors, 2.x and 3.x. Each major flavor has minor (compatible) revisions. </p>
<p> The applicable standard for RTCM Version 2.x is RTCM Recommended Standards for Differential NAVSTAR GPS Service RTCM Paper 194-93/SC 104-STD. For RTCM 3.1 it is RTCM Paper 177-2006-SC104-STD. Ordering instructions for both standards are accessible from the website of the m[blue]<code>Radio Technical Commission for Maritime Services</code>m[]<font SIZE="-2">[1]</font> under &quot;Publications&quot;.</p>
<h3>Rtcm Wire Transmissions</h3>
<p>Differential-GPS correction stations consist of a GPS reference receiver coupled to a low frequency (LF) transmitter. The GPS reference receiver is a survey-grade GPS that does GPS carrier tracking and can work out its own position to a few millimeters. It generates range and range-rate corrections and encodes them into RTCM104. It ships the RTCM104 to the LF transmitter over serial rs-232 signal at 100 baud or 200 baud depending on the requirements of the transmitter. </p>
<p> The LF transmitter broadcasts the approximately 300khz radio signal that differential-GPS radio receivers pick up. Transmitters that are meant to have a higher range will need to transmit at the slower rate. The higher the data rate the harder it will be for the remote radio receiver to receive with a good signal-to-noise ration. (Higher data rate signals can&#8217;t be averaged over as long a time frame, hence they appear noisier.)</p>
<h3>Rtcm Wire Formats</h3>
<p>An RTCM 2.x message consists of a sequence of up to 33 30-bit words. The 24 most significant bits of each word are data and the six least significant bits are parity. The parity algorithm used is the same ISGPS-2000 as that used on GPS satellite downlinks. Each RTCM 2.x message consists of two header words followed by zero or more data words, depending upon message type. </p>
<p> An RTCM 3.x message begins with a fixed leader byte 0xD3. That is followed by six bits of version information and 10 bits of payload length information. Following that is the payload; following the payload is a 3-byte checksum of the payload using the Qualcomm CRC-24Q algorithm.</p>
<h3>Rtcm2 Json Format</h3>
<p>Each RTCM2 message is dumped as a single JSON object per message, with the message fields as attributes of that object. Arrays of satellite, station, and constellation statistics become arrays of JSON sub-objects. Each sentence will normally also have a &quot;device&quot; field containing the pathname of the originating device. </p>
<p> All attributes other than the device field are mandatory. Header attributes are emitted before others. </p>
<p> <font SIZE="+1"> <code>Header portion</code></p>
<dl>
<dd><code>Table 15. SKY object</code> </font></p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Type </code></td>
<td><code> </p>
<p> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> class </td>
<td> string </td>
<td>
<p> Fixed: &quot;RTCM2&quot;.
</td>
</tr>
<tr VALIGN=top>
<td> type </td>
<td> integer </td>
<td>
<p> Message type (1-9).
</td>
</tr>
<tr VALIGN=top>
<td> station_id </td>
<td> integer </td>
<td>
<p> The id of the GPS reference receiver. The LF transmitters also have (different) id numbers.
</td>
</tr>
<tr VALIGN=top>
<td> zcount </td>
<td> real </td>
<td>
<p> The reference time of the corrections in the message in seconds within the current hour. Note that it is in GPS time, which is some seconds ahead of UTC (see the U.S. Naval Observatory&#8217;s m[blue]<code>table of leap second corrections</code>m[]<font SIZE="-2">[2]</font>).
</td>
</tr>
<tr VALIGN=top>
<td> seqnum </td>
<td> integer </td>
<td>
<p> Sequence number. Only 3 bits wide, wraps after 7.
</td>
</tr>
<tr VALIGN=top>
<td> length </td>
<td> integer </td>
<td>
<p> The number of words after the header that comprise the message.
</td>
</tr>
<tr VALIGN=top>
<td> station_health </td>
<td> integer </td>
<td>
<p> Station transmission status. Indicates the health of the beacon as a reference source. Any nonzero value means the satellite is probably transmitting bad data and should not be used in a fix. 6 means the transmission is unmonitored. 7 means the station is not working properly. Other values are defined by the beacon operator.
</td>
</tr>
</table>
<p> <font SIZE="+1"> </p>
<p> &lt;message type&gt; is one of </p>
<p> 1</p>
<dl>
<dd>full corrections &#8211; one message containing corrections for all GPS satellites in view. This is not common.</dl>
<p> 3</p>
<dl>
<dd>reference station parameters &#8211; the position of the reference station GPS antenna.</dl>
<p> 4</p>
<dl>
<dd>datum &#8212; the datum to which the DGPS data is referred.</dl>
<p> 5</p>
<dl>
<dd>constellation health &#8212; information about the satellites the beacon can see.</dl>
<p> 6</p>
<dl>
<dd>null message &#8212; just a filler.</dl>
<p> 7</p>
<dl>
<dd>radio beacon almanac &#8212; information about this or other beacons.</dl>
<p> 9</p>
<dl>
<dd>subset corrections &#8212; a message containing corrections for only a subset of the GPS satellites in view.</dl>
<p> 16</p>
<dl>
<dd>special message &#8212; a text message from the beacon operator.</dl>
<p> 31</p>
<dl>
<dd>GLONASS subset corrections &#8212; a message containing corrections for a set of the GLONASS satellites in view.</dl>
</dl>
<p> </font><font SIZE="+2"> <code>Type 1 and 9: Correction data</code></p>
<dl>
<dd>One or more satellite objects follow the header for type 1 or type 9 messages. Here is the format: </p>
<p> <code>Table 16. Satellite object</code> </font></p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Type </code></td>
<td><code> </p>
<p> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> ident </td>
<td> integer </td>
<td>
<p> The PRN number of the satellite for which this is correction data.
</td>
</tr>
<tr VALIGN=top>
<td> udre </td>
<td> integer </td>
<td>
<p> User Differential Range Error (0-3). See the table following for values.
</td>
</tr>
<tr VALIGN=top>
<td> iod </td>
<td> integer </td>
<td>
<p> Issue Of Data, matching the IOD for the current ephemeris of this satellite, as transmitted by the satellite. The IOD is a unique tag that identifies the ephemeris; the GPS using the DGPS correction and the DGPS generating the data must use the same orbital positions for the satellite.
</td>
</tr>
<tr VALIGN=top>
<td> prc </td>
<td> real </td>
<td>
<p> The pseudorange error in meters for this satellite as measured by the beacon reference receiver at the epoch indicated by the z_count in the parent record.
</td>
</tr>
<tr VALIGN=top>
<td> rrc </td>
<td> real </td>
<td>
<p> The rate of change of pseudorange error in meters/sec for this satellite as measured by the beacon reference receiver at the epoch indicated by the z_count field in the parent record. This is used to calculate pseudorange errors at other epochs, if required by the GPS receiver.
</td>
</tr>
</table>
<p> <font SIZE="+2"> </p>
<p> User Differential Range Error values are as follows: </p>
<p> <code>Table 17. UDRE values</code> </font></p>
<table BORDER>
<tr VALIGN=top>
<td> 0 </td>
<td> 1-sigma error<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;= 1m</p>
</td>
</tr>
<tr VALIGN=top>
<td> 1 </td>
<td> 1-sigma error<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;= 4m</p>
</td>
</tr>
<tr VALIGN=top>
<td> 2 </td>
<td> 1-sigma error<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;= 8m</p>
</td>
</tr>
<tr VALIGN=top>
<td> 3 </td>
<td> 1-sigma error<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&gt; 8m</p>
</td>
</tr>
</table>
<p> <font SIZE="+2"> </p>
<p> Here&#8217;s an example: </p>
<dl>
<dd></font></p>
<pre>{&quot;class&quot;:&quot;RTCM2&quot;,&quot;type&quot;:1,
 &quot;station_id&quot;:688,&quot;zcount&quot;:843.0,&quot;seqnum&quot;:5,&quot;length&quot;:19,&quot;station_health&quot;:6,
 &quot;satellites&quot;:[
 {&quot;ident&quot;:10,&quot;udre&quot;:0,&quot;iod&quot;:46,&quot;prc&quot;:-2.400,&quot;rrc&quot;:0.000},
 {&quot;ident&quot;:13,&quot;udre&quot;:0,&quot;iod&quot;:94,&quot;prc&quot;:-4.420,&quot;rrc&quot;:0.000},
 {&quot;ident&quot;:7,&quot;udre&quot;:0,&quot;iod&quot;:22,&quot;prc&quot;:-5.160,&quot;rrc&quot;:0.002},
 {&quot;ident&quot;:2,&quot;udre&quot;:0,&quot;iod&quot;:34,&quot;prc&quot;:-6.480,&quot;rrc&quot;:0.000},
 {&quot;ident&quot;:4,&quot;udre&quot;:0,&quot;iod&quot;:47,&quot;prc&quot;:-8.860,&quot;rrc&quot;:0.000},
 {&quot;ident&quot;:8,&quot;udre&quot;:0,&quot;iod&quot;:76,&quot;prc&quot;:-7.980,&quot;rrc&quot;:0.002},
 {&quot;ident&quot;:5,&quot;udre&quot;:0,&quot;iod&quot;:99,&quot;prc&quot;:-8.260,&quot;rrc&quot;:0.002},
 {&quot;ident&quot;:23,&quot;udre&quot;:0,&quot;iod&quot;:81,&quot;prc&quot;:-8.060,&quot;rrc&quot;:0.000},
 {&quot;ident&quot;:16,&quot;udre&quot;:0,&quot;iod&quot;:70,&quot;prc&quot;:-11.740,&quot;rrc&quot;:0.000},
 {&quot;ident&quot;:30,&quot;udre&quot;:0,&quot;iod&quot;:4,&quot;prc&quot;:-18.960,&quot;rrc&quot;:-0.006},
 {&quot;ident&quot;:29,&quot;udre&quot;:0,&quot;iod&quot;:101,&quot;prc&quot;:-24.960,&quot;rrc&quot;:-0.002}
]}</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Type 3: Reference Station Parameters</code></p>
<dl>
<dd>Here are the payload members of a type 3 (Reference Station Parameters) message: </p>
<p> <code>Table 18. Reference Station Parameters</code> </font></p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Type </code></td>
<td><code> </p>
<p> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> x </td>
<td> real </td>
<td>
<p> ECEF X coordinate.
</td>
</tr>
<tr VALIGN=top>
<td> y </td>
<td> real </td>
<td>
<p> ECEF Y coordinate.
</td>
</tr>
<tr VALIGN=top>
<td> z </td>
<td> real </td>
<td>
<p> ECEF Z coordinate.
</td>
</tr>
</table>
<p> <font SIZE="+1"> </p>
<p> The coordinates are the position of the station, in meters to two decimal places, in Earth Centred Earth Fixed coordinates. These are usually referred to the WGS84 reference frame, but may be referred to NAD83 in the US (essentially identical to WGS84 for all except geodesists), or to some other reference frame in other parts of the world. </p>
<p> An invalid reference message is represented by a type 3 header without payload fields. </p>
<p> Here&#8217;s an example: </p>
<dl>
<dd></font></p>
<pre>{&quot;class&quot;:&quot;RTCM2&quot;,&quot;type&quot;:3,
 &quot;station_id&quot;:652,&quot;zcount&quot;:1657.2,&quot;seqnum&quot;:2,&quot;length&quot;:4,&quot;station_health&quot;:6,
 &quot;x&quot;:3878620.92,&quot;y&quot;:670281.40,&quot;z&quot;:5002093.59
}</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Type 4: Datum</code></p>
<dl>
<dd>Here are the payload members of a type 4 (Datum) message: </p>
<p> <code>Table 19. Datum</code> </font></p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Type </code></td>
<td><code> </p>
<p> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> dgnss_type </td>
<td> string </td>
<td>
<p> Either &quot;GPS&quot;, &quot;GLONASS&quot;, &quot;GALILEO&quot;, or &quot;UNKNOWN&quot;.
</td>
</tr>
<tr VALIGN=top>
<td> dat </td>
<td> integer </td>
<td>
<p> 0 or 1 and indicates the sense of the offset shift given by dx, dy, dz. dat = 0 means that the station coordinates (in the reference message) are referred to a local datum and that adding dx, dy, dz to that position will render it in GNSS coordinates (WGS84 for GPS). If dat = 1 then the ref station position is in GNSS coordinates and adding dx, dy, dz will give it referred to the local datum.
</td>
</tr>
<tr VALIGN=top>
<td> datum_name </td>
<td> string </td>
<td>
<p> A standard name for the datum.
</td>
</tr>
<tr VALIGN=top>
<td> dx </td>
<td> real </td>
<td>
<p> X offset.
</td>
</tr>
<tr VALIGN=top>
<td> dy </td>
<td> real </td>
<td>
<p> Y offset.
</td>
</tr>
<tr VALIGN=top>
<td> dz </td>
<td> real </td>
<td>
<p> Z offset.
</td>
</tr>
</table>
<p> <font SIZE="+1"> </p>
<p> &lt;dx&gt; &lt;dy&gt; &lt;dz&gt; are offsets to convert from local datum to GNSS datum or vice versa. These fields are optional. </p>
<p> An invalid datum message is represented by a type 4 header without payload fields.</dl>
<p> </font><font SIZE="+2"> <code>Type 5: Constellation Health</code></p>
<dl>
<dd>One or more of these follow the header for type 5 messages &#8212; one for each satellite. </p>
<p> Here is the format: </p>
<p> <code>Table 20. Constellation health</code> </font></p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Type </code></td>
<td><code> </p>
<p> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> ident </td>
<td> integer </td>
<td>
<p> The PRN number of the satellite.
</td>
</tr>
<tr VALIGN=top>
<td> iodl </td>
<td> bool </td>
<td>
<p> True indicates that this information relates to the satellite information in an accompanying type 1 or type 9 message.
</td>
</tr>
<tr VALIGN=top>
<td> health </td>
<td> integer </td>
<td> 0 indicates that the satellite is healthy. Any other value <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>indicates a problem (coding is not known)..PP</p>
</td>
</tr>
<tr VALIGN=top>
<td> snr </td>
<td> integer </td>
<td>
<p> The carrier/noise ratio of the received signal in the range 25 to 55 dB(Hz).
</td>
</tr>
<tr VALIGN=top>
<td> health_en </td>
<td> bool </td>
<td>
<p> If set to True it indicates that the satellite is healthy even if the satellite navigation data says it is unhealthy.
</td>
</tr>
<tr VALIGN=top>
<td> new_data </td>
<td> bool </td>
<td> True indicates that the IOD for this satellite will<br />
&nbsp;<wbr>&nbsp;<wbr>soon be updated in type 1 or 9 messages..PP
</td>
</tr>
<tr VALIGN=top>
<td> los_warning </td>
<td> bool </td>
<td>
<p> Line-of-sight warning. True indicates that the satellite will shortly go unhealthy.
</td>
</tr>
<tr VALIGN=top>
<td> tou </td>
<td> integer </td>
<td>
<p> Healthy time remaining in seconds.
</td>
</tr>
</table>
<p> <font SIZE="+2"> </p>
</dl>
<p> </font><font SIZE="+3"> <code>Type 6: Null</code></p>
<dl>
<dd>This just indicates a null message. There are no payload fields.</dl>
<p> </font><font SIZE="+4"> <code>Unknown message</code></p>
<dl>
<dd>This format is used to dump message words in hexadecimal when the message type field doesn&#8217;t match any of the known ones. </p>
<p> Here is the format: </p>
<p> <code>Table 21. Unknown Message</code> </font></p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Type </code></td>
<td><code> </p>
<p> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> data </td>
<td> list </td>
<td>
<p> A list of strings.
</td>
</tr>
</table>
<p> <font SIZE="+4"> </p>
<p> Each string in the array is a hex literal representing 30 bits of information, after parity checks and inversion. The high two bits should be ignored.</dl>
<p> </font><font SIZE="+5"> <code>Type 7: Radio Beacon Almanac</code></p>
<dl>
<dd>Here is the format: </p>
<p> <code>Table 22. Contellation health</code> </font></p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Type </code></td>
<td><code> </p>
<p> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> lat </td>
<td> real </td>
<td>
<p> Latitude in degrees, of the LF transmitter antenna for the station for which this is an almanac. North is positive.
</td>
</tr>
<tr VALIGN=top>
<td> lon </td>
<td> real </td>
<td>
<p> Longitude in degrees, of the LF transmitter antenna for the station for which this is an almanac. East is positive.
</td>
</tr>
<tr VALIGN=top>
<td> range </td>
<td> integer </td>
<td> Published range of the station in km..PP
</td>
</tr>
<tr VALIGN=top>
<td> frequency </td>
<td> real </td>
<td>
<p> Station broadcast frequency in kHz.
</td>
</tr>
<tr VALIGN=top>
<td> health </td>
<td> integer </td>
<td>
<p> &lt;health&gt; is the health of the station for which this is an almanac. If it is non-zero, the station is issuing suspect data and should not be used for fixes. The ITU and RTCM104 standards differ about the mode detailed interpretation of the &lt;health&gt; field and even about its bit width.
</td>
</tr>
<tr VALIGN=top>
<td> station_id </td>
<td> integer </td>
<td>
<p> The id of the transmitter. This is not the same as the reference id in the header, the latter being the id of the reference receiver.
</td>
</tr>
<tr VALIGN=top>
<td> bitrate </td>
<td> integer </td>
<td>
<p> The transmitted bitrate.
</td>
</tr>
</table>
<p> <font SIZE="+5"> </p>
<p> Here&#8217;s an example: </p>
<dl>
<dd></font></p>
<pre>{&quot;class&quot;:&quot;RTCM2&quot;,&quot;type&quot;:9,&quot;station_id&quot;:268,&quot;zcount&quot;:252.6,
 &quot;seqnum&quot;:4,&quot;length&quot;:5,&quot;station_health&quot;:0,
 &quot;satellites&quot;:[
 {&quot;ident&quot;:13,&quot;udre&quot;:0,&quot;iod&quot;:3,&quot;prc&quot;:-25.940,&quot;rrc&quot;:0.066},
 {&quot;ident&quot;:2,&quot;udre&quot;:0,&quot;iod&quot;:73,&quot;prc&quot;:0.920,&quot;rrc&quot;:-0.080},
 {&quot;ident&quot;:8,&quot;udre&quot;:0,&quot;iod&quot;:22,&quot;prc&quot;:23.820,&quot;rrc&quot;:0.014}
]}</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Type 13: GPS Time of Week</code></p>
<dl>
<dd>Here are the payload members of a type 13 (Groumf Tramitter Parameters) message: </p>
<p> <code>Table 23. Grund Transmitter Parameters</code> </font></p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Type </code></td>
<td><code> </p>
<p> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> status </td>
<td> bool </td>
<td>
<p> If True, signals user to expect a type 16 explanatory message associated with this station. Probably indicates some sort of unusual event.
</td>
</tr>
<tr VALIGN=top>
<td> rangeflag </td>
<td> bool </td>
<td>
<p> If True, indicates that the estimated range is different from that found in the Type 7 message (which contains the beacon&#8217;s listed range). Generally indicates a range reduction due to causes such as poor ionospheric conditions or reduced transmission power.
</td>
</tr>
<tr VALIGN=top>
<td> lat </td>
<td> real </td>
<td>
<p> Degrees latitude, signed. Positive is N, negative is S.
</td>
</tr>
<tr VALIGN=top>
<td> lon </td>
<td> real </td>
<td>
<p> Degrees longitude, signed. Positive is E, negative is W.
</td>
</tr>
<tr VALIGN=top>
<td> range </td>
<td> integer </td>
<td>
<p> Transmission range in km (1-1024).
</td>
</tr>
</table>
<p> <font SIZE="+1"> </p>
<p> This message type replaces message type 3 (Reference Station Parameters) in RTCM 2.3.</dl>
<p> </font><font SIZE="+2"> <code>Type 14: GPS Time of Week</code></p>
<dl>
<dd>Here are the payload members of a type 14 (GPS Time of Week) message: </p>
<p> <code>Table 24. Reference Station Parameters</code> </font></p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Type </code></td>
<td><code> </p>
<p> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> week </td>
<td> integer </td>
<td>
<p> GPS week (0-123).
</td>
</tr>
<tr VALIGN=top>
<td> hour </td>
<td> integer </td>
<td>
<p> Hour of week (0-167).
</td>
</tr>
<tr VALIGN=top>
<td> leapsecs </td>
<td> integer </td>
<td>
<p> Leap Seconds (0-63).
</td>
</tr>
</table>
<p> <font SIZE="+2"> </p>
<p> Here&#8217;s an example: </p>
<dl>
<dd></font></p>
<pre>{&quot;class&quot;:&quot;RTCM2&quot;,&quot;type&quot;:14,&quot;station_id&quot;:652,&quot;zcount&quot;:1657.2,
 &quot;seqnum&quot;:3,&quot;length&quot;:1,&quot;station_health&quot;:6,&quot;week&quot;:601,&quot;hour&quot;:109,
 &quot;leapsecs&quot;:15}</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Type 16: Special Message</code></p>
<dl>
<dd><code>Table 25. Special Message</code> </font></p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Type </code></td>
<td><code> </p>
<p> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> message </td>
<td> string </td>
<td>
<p> A text message sent by the beacon operator.
</td>
</tr>
</table>
<p> <font SIZE="+1"> </p>
</dl>
<p> </font><font SIZE="+2"> <code>Type 31: Correction data</code></p>
<dl>
<dd>One or more GLONASS satellite objects follow the header for type 1 or type 9 messages. Here is the format: </p>
<p> <code>Table 26. Satellite object</code> </font></p>
<table BORDER>
<tr VALIGN=top>
<td><code> Name </code></td>
<td><code> Type </code></td>
<td><code> </p>
<p> Description </code>
</td>
</tr>
<tr VALIGN=top>
<td> ident </td>
<td> integer </td>
<td>
<p> The PRN number of the satellite for which this is correction data.
</td>
</tr>
<tr VALIGN=top>
<td> udre </td>
<td> integer </td>
<td>
<p> User Differential Range Error (0-3). See the table following for values.
</td>
</tr>
<tr VALIGN=top>
<td> change </td>
<td> boolean </td>
<td>
<p> Change-of-ephemeris bit.
</td>
</tr>
<tr VALIGN=top>
<td> tod </td>
<td> uinteger </td>
<td>
<p> Count of 30-second periods since the top of the hour.
</td>
</tr>
<tr VALIGN=top>
<td> prc </td>
<td> real </td>
<td>
<p> The pseudorange error in meters for this satellite as measured by the beacon reference receiver at the epoch indicated by the z_count in the parent record.
</td>
</tr>
<tr VALIGN=top>
<td> rrc </td>
<td> real </td>
<td>
<p> The rate of change of pseudorange error in meters/sec for this satellite as measured by the beacon reference receiver at the epoch indicated by the z_count field in the parent record. This is used to calculate pseudorange errors at other epochs, if required by the GPS receiver.
</td>
</tr>
</table>
<p> <font SIZE="+2"> </p>
<p> Here&#8217;s an example: </p>
<dl>
<dd></font></p>
<pre>{&quot;class&quot;:&quot;RTCM2&quot;,&quot;type&quot;:31,&quot;station_id&quot;:652,&quot;zcount&quot;:1642.2,
 &quot;seqnum&quot;:0,&quot;length&quot;:14,&quot;station_health&quot;:6,
 &quot;satellites&quot;:[
 {&quot;ident&quot;:5,&quot;udre&quot;:0,&quot;change&quot;:false,&quot;tod&quot;:0,&quot;prc&quot;:132.360,&quot;rrc&quot;:0.000},
 {&quot;ident&quot;:15,&quot;udre&quot;:0,&quot;change&quot;:false,&quot;tod&quot;:0,&quot;prc&quot;:134.840,&quot;rrc&quot;:0.002},
 {&quot;ident&quot;:14,&quot;udre&quot;:0,&quot;change&quot;:false,&quot;tod&quot;:0,&quot;prc&quot;:141.520,&quot;rrc&quot;:0.000},
 {&quot;ident&quot;:6,&quot;udre&quot;:0,&quot;change&quot;:false,&quot;tod&quot;:0,&quot;prc&quot;:127.000,&quot;rrc&quot;:0.000},
 {&quot;ident&quot;:21,&quot;udre&quot;:0,&quot;change&quot;:false,&quot;tod&quot;:0,&quot;prc&quot;:128.780,&quot;rrc&quot;:0.000},
 {&quot;ident&quot;:22,&quot;udre&quot;:0,&quot;change&quot;:false,&quot;tod&quot;:0,&quot;prc&quot;:125.260,&quot;rrc&quot;:0.002},
 {&quot;ident&quot;:20,&quot;udre&quot;:0,&quot;change&quot;:false,&quot;tod&quot;:0,&quot;prc&quot;:117.280,&quot;rrc&quot;:-0.004},
 {&quot;ident&quot;:16,&quot;udre&quot;:0,&quot;change&quot;:false,&quot;tod&quot;:17,&quot;prc&quot;:113.460,&quot;rrc&quot;:0.018}
]}</pre>
</dl>
</dl>
<h2>Rtcm3 Dump Format</h2>
<p>The support for RTCM104v3 dumping is incomplete and buggy. Do not attempt to use it for production! Anyone interested in it should read the source code.</p>
<h2>Ais Dump Formats</h2>
<p>AIS support is an extension. It may not be present if your instance of gpsd has been built with a restricted feature set. </p>
<p> AIS packets are dumped as JSON objects with class &quot;AIS&quot;. Each AIS report object contains a &quot;type&quot; field giving the AIS message type and a &quot;scaled&quot; field telling whether the remainder of the fields are dumped in scaled or unscaled form. (These will be emitted before any type-specific fields.) It will also contain a &quot;device&quot; field naming the data source. Other fields have names and types as specified in the AIVDM/AIVDO Protocol Decoding document on the GPSD project website; each message field table may be directly interpreted as a specification for the members of the corresponding JSON object type. </p>
<p> By default, certain scaling and conversion operations are performed for JSON output. Latitudes and longitudes are scaled to decimal degrees rather than the native AIS unit of 1/10000th of a minute of arc. Ship (but not air) speeds are scaled to knots rather than tenth-of-knot units. Rate of turn may appear as &quot;nan&quot; if is unavailable, or as one of the strings &quot;fastright&quot; or &quot;fastleft&quot; if it is out of the AIS encoding range; otherwise it is quadratically mapped back to the turn sensor number in degrees per minute. Vessel draughts are converted to decimal meters rather than native AIS decimeters. Various other scaling conversions are described in &quot;AIVDM/AIVDO Protocol Decoding&quot;.</p>
<h2>Subframe Dump Formats</h2>
<p>Subframe support is always compiled into gpsd but many GPSes do not output subframe data or the gpsd driver may not support subframes. </p>
<p> Subframe packets are dumped as JSON objects with class &quot;SUBFRAME&quot;. Each subframe report object contains a &quot;frame&quot; field giving the subframe number, a &quot;tSV&quot; field for the transmitting satellite number, a &quot;TOW17&quot; field containing the 17 MSBs of the start of the next 12-second message and a &quot;scaled&quot; field telling whether the remainder of the fields are dumped in scaled or unscaled form. It will also contain a &quot;device&quot; field naming the data source. Each SUBFRAME object will have a sub-object specific to that subframe page type. Those sub-object fields have names and types similar to those specified in the IS-GPS-200E document; each message field table may be directly interpreted as a specification for the members of the corresponding JSON object type.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3),</p>
<h2>Author</h2>
<p>The protocol was designed and documented by Eric S. Raymond.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Radio Technical Commission for Maritime Services</p>
<dl>
<dd><a rel="nofollow" href="http://www.rtcm.org/">http://www.rtcm.org/</a></dl>
<dt> 2.</p>
<dd>table of leap second corrections</p>
<dl>
<dd><a href="ftp://maia.usno.navy.mil/ser7/tai-utc.dat">ftp://maia.usno.navy.mil/ser7/tai-utc.dat</a></dl>
