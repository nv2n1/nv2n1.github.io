---
title: "rtcm-104(5)"
name: "rtcm-104"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rtcm-104/"
description: "rtcm-104 – RTCM-104 dump format emitted by GPSD tools"
---

<p>rtcm-104 &#8211; RTCM-104 dump format emitted by GPSD tools</p>
<h2>Overview</h2>
<p>RTCM-104 is a family of serial protocols used for broadcasting pseudorange corrections from differential-GPS reference stations. This manual page describes some aspects of the RTCM protocol, mainly in order to explain the RTCM-104 dump format emitted by <code><a href="/docs/linux/man/1-gpsdecode/">gpsdecode</a></code>(1). It describes that dump format completely. </p>
<p> RTCM-104 comes in two major and incompatible flavors, 2.x and 3.x. Each major flavor has minor (compatible) revisions. </p>
<p> The applicable standard for RTCM Version 2.x is RTCM Recommended Standards for Differential NAVSTAR GPS Service RTCM Paper 194-93/SC 104-STD. For RTCM 3.1 it is RTCM Paper 177-2006-SC104-STD. Ordering instructions for both standards are accessible from the website of the <i>Radio Technical Commission for Maritime Services</i>[1] under &quot;Publications&quot;.</p>
<h2>Rtcm Wire Transmissions</h2>
<p>Differential-GPS correction stations consist of a GPS reference receiver coupled to a low frequency (LF) transmitter. The GPS reference receiver is a survey-grade GPS that does GPS carrier tracking and can work out its own position to a few millimeters. It generates range and range-rate corrections and encodes them into RTCM104. It ships the RTCM104 to the LF transmitter over serial rs-232 signal at 100 baud or 200 baud depending on the requirements of the transmitter. </p>
<p> The LF transmitter broadcasts the the approximately 300khz radio signal that differential-GPS radio receivers pick up. Transmitters that are meant to have a higher range will need to transmit at the slower rate. The higher the data rate the harder it will be for the remote radio receiver to receive with a good signal-to-noise ration. (Higher data rate signals can&#8217;t be averaged over as long a time frame, hence they appear noisier.)</p>
<h2>Rtcm Wire Formats</h2>
<p>An RTCM 2.x message consists of a sequence of up to 33 30-bit words. The 24 most significant bits of each word are data and the six least significant bits are parity. The parity algorithm used is the same ISGPS-2000 as that used on GPS satellite downlinks. Each RTCM 2.x message consists of two header words followed by zero or more data words, depending upon message type. </p>
<p> An RTCM 3.x message begins with a fixed leader byte 0xD3. That is followed by six bits of version information and 10 bits of payload length information. Following that is the payload; following the payload is a 3-byte checksum of the payload using the Qualcomm CRC-24Q algorithm.</p>
<h2>Rtcm2 Dump Format</h2>
<p>For each message, the header is listed first, followed by zero or more lines containing the specific data for that message, followed by a trailing sentinel line containing a single dot. The general format is a line beginning with a capital letter, followed by a tab, followed by the fields of the message separated by tabs, terminated by a newline.</p>
<h3>Header message (H)</h3>
<dl>
<dd>
<pre>H &lt;message type&gt; &lt;reference station id&gt; &lt;modified z_count&gt; &lt;sequence no&gt;
 &lt;message length&gt; &lt;station health&gt; [T &lt;useful length&gt;]</pre>
</dl>
<p> Here is an example: </p>
<dl>
<dd>
<pre>H 9 268 249.6 1 5 0
S 13 0 3 249.6 -26.120 0.068
S 2 0 73 249.6 1.220 -0.080
S 8 0 22 249.6 23.760 0.030
.</pre>
</dl>
<p> &lt;message type&gt; is one of </p>
<p> 1</p>
<dl>
<dd>full corrections &#8211; one message containing corrections for all satellites in view. This is not common.</dl>
<p> 3</p>
<dl>
<dd>reference station parameters &#8211; the position of the reference station GPS antenna.</dl>
<p> 4</p>
<dl>
<dd>datum &#8212; the datum to which the DGPS data is referred.</dl>
<p> 5</p>
<dl>
<dd>constellation health &#8212; information about the satellites the beacon can see</dl>
<p> 6</p>
<dl>
<dd>null message &#8212; just a filler.</dl>
<p> 7</p>
<dl>
<dd>radio beacon almanac &#8212; information about this or other beacons.</dl>
<p> 9</p>
<dl>
<dd>subset corrections &#8212; a message containing corrections for only a subset of the satellites in view.</dl>
<p> 16</p>
<dl>
<dd>special message &#8212; a text message from the beacon operator.</dl>
<p> &lt;reference station id&gt; is the id of the GPS reference receiver. The LF transmitters also have (different) id numbers. </p>
<p> &lt;modified z_count&gt; is the reference time of the corrections in the message in seconds within the current hour. Note that it is in GPS time, which is some seconds ahead of UTC (see the U.S. Naval Observatory&#8217;s <i>table of leap second corrections</i>[2]). </p>
<p> &lt;sequence no&gt; is a number which increments, modulo 8, for each message transmitted. </p>
<p> &lt;message length&gt; is the number of words after the header that comprise the message. </p>
<p> &lt;station health&gt; indicates the health of the beacon as a reference source. Any nonzero value means the satellite is probably transmitting bad data and should not be used in a fix. 6 means the transmission is unmonitored. 7 means the station is not working properly. Other values are defined by the beacon operator. </p>
<p> If the message contains a parity error after the header but before the end of the message, then the extra fields [T &lt;useful length&gt;] are appended to indicate a truncated message. </p>
<p> Here is an example: </p>
<dl>
<dd>
<pre>H 9 687 331.8 1 5 0 T 4</pre>
</dl>
<p> &lt;useful length&gt; indicates the number of useful words before the parity error. Depending on the message type, useful information may still be extracted.</p>
<h3>Correction data (S)</h3>
<p>One or more of these follow the header for type 1 or type 9 messages. Here is the format: </p>
<dl>
<dd>
<pre>S &lt;satellite&gt; &lt;udre&gt; &lt;iod&gt; &lt;modified z_count&gt; &lt;range error&gt;
 &lt;range error rate&gt;</pre>
</dl>
<p> Here is an example: </p>
<dl>
<dd>
<pre>S 7 0 199 331.8 -12.160 0.288</pre>
</dl>
<p> &lt;satellite&gt; is the PRN number of the satellite for which this is correction data. </p>
<p> &lt;udre&gt; is User Differential Range Error with the following values: </p>
<dl>
<dd>
<pre>0 1-sigma error &lt;= 1m
1 1-sigma error &lt;= 4m
2 1-sigma error &lt;= 8m
3 1-sigma error &gt; 8m</pre>
</dl>
<p> &lt;iod&gt; is Issue Of Data, matching the IOD for the current ephemeris of this satellite, as transmitted by the satellite. The IOD is a unique tag that identifies the ephemeris; the GPS using the DGPS correction and the DGPS generating the data must use the same orbital positions for the satellite. </p>
<p> &lt;modified z_count&gt; is just a copy of the same field from the header. </p>
<p> &lt;range error&gt; is the pseudorange error in meters for this satellite as measured by the beacon reference receiver at the epoch indicated by &lt;modified z_count&gt; </p>
<p> &lt;range error rate&gt; is the rate of change of pseudorange error in meters/sec for this satellite as measured by the beacon reference receiver at the epoch indicated by &lt;modified z_count&gt;. This is used to calculate pseudorange errors at other epochs, if required by the GPS receiver.</p>
<h3>Reference Station Parameters (R)</h3>
<p>Here is the format: </p>
<dl>
<dd>
<pre>R &lt;X-coordinate&gt; &lt;Y-coordinate&gt; &lt;Z-coordinate&gt;</pre>
</dl>
<p> Here is an example: </p>
<dl>
<dd>
<pre>R 3746729.40 -5086.23 5144450.67</pre>
</dl>
<p> The coordinates are the position of the station, in meters to two decimal places, in Earth Centred Earth Fixed coordinates. These are usually referred to the WGS84 reference frame, but may be referred to NAD83 in the US (essentially identical to WGS84 for all except geodesists), or to some other reference frame in other parts of the world.</p>
<h3>Datum (D)</h3>
<p>Here is the format: </p>
<dl>
<dd>
<pre>D &lt;dgnss type&gt; &lt;dat&gt; &lt;datum name&gt; [ &lt;dx&gt; &lt;dy&gt; &lt;dz&gt; ]</pre>
</dl>
<p> Here is an (artificial) example: </p>
<dl>
<dd>
<pre>D GPS 0 ABC12 25.8 30.5 33.0</pre>
</dl>
<p> &lt;dgnss type&gt; is either GPS or GLONASS. </p>
<p> &lt;dat&gt; is 0 or 1 and indicates the sense of the offset shift given by dx, dy, dz. dat = 0 means that the station coordinates (in the reference message) are referred to a local datum and that adding dx, dy, dz to that position will render it in GNSS coordinates (WGS84 for GPS). If dat = 1 then the ref station position is in GNSS coordinates and adding dx, dy, dz will give it referred to the local datum. </p>
<p> &lt;datum name&gt; is a standard name for the datum. </p>
<p> &lt;dx&gt; &lt;dy&gt; &lt;dz&gt; are offsets to convert from local datum to GNSS datum or vice versa. These fields are optional.</p>
<h3>Constellation Health (C)</h3>
<p>One or more of these follow the header for type 5 messages &#8212; one for each satellite. </p>
<p> Here is the format: </p>
<dl>
<dd>
<pre>C &lt;sat&gt; &lt;iodl&gt; &lt;health&gt; &lt;snr&gt; &lt;hlth en&gt; &lt;new data&gt; &lt;los warning&gt;
 &lt;time to unhealthy&gt;</pre>
</dl>
<p> Here is an example: </p>
<dl>
<dd>
<pre>C 29 0 0 53 0 0 0 0</pre>
</dl>
<p> &lt;sat&gt; is the PRN number of the satellite. </p>
<p> &lt;iodl&gt; is 1 bit. 0 indicates that this information relates to the satellite information in an accompanying type 1 or type 9 message. </p>
<p> &lt;health&gt; 0 indicates that the satellite is healthy. Any other value indicates a problem (coding is not known). </p>
<p> &lt;snr&gt; gives the carrier/noise ratio of the received signal in the range 25 to 55 dB(Hz). </p>
<p> &lt;health en&gt; is 1 bit. If set to 1 it indicates that the satellite is healthy even if the satellite navigation data says it is unhealthy. </p>
<p> &lt;new data&gt; is 1 bit. a 1 indicates that the IOD for this satellite will soon be updated in type 1 or 9 messages. </p>
<p> &lt;los warning&gt; is 1 bit. a 1 indicates that the satellite will shortly go unhealthy. The healthy time remaining is given in the &lt;time to unhealthy&gt; field.</p>
<h3>Radio Beacon Almanac (A)</h3>
<p>Here is the format: </p>
<dl>
<dd>
<pre>A &lt;latitude&gt; &lt;longitude&gt; &lt;range&gt; &lt;frequency&gt; &lt;health&gt; &lt;station id&gt;
 &lt;bitrate&gt;</pre>
</dl>
<p> Here is an example: </p>
<dl>
<dd>
<pre>A 54.1176 -0.0714 100 302.5 0 447 2</pre>
</dl>
<p> &lt;latitude&gt; and &lt;longitude&gt; give the position, in degrees, of the LF transmitter antenna for the station for which this is an almanac. North and East are positive. </p>
<p> &lt;range&gt; is the published range of the station in km. </p>
<p> &lt;frequency&gt; is the broadcast frequency in kHz. </p>
<p> &lt;health&gt; is the health of the station for which this is an almanac. If it is non-zero, the station is issuing suspect data and should not be used for fixes. The ITU and RTCM104 standards differ about the mode detailed interpretation of the &lt;health&gt; field and even about its bit width. </p>
<p> &lt;station id&gt; is the id of the transmitter. This is not the same as the reference id in the header, the latter being the id of the reference receiver. </p>
<p> &lt;bitrate&gt; indicates the transmitted bitrate.</p>
<h3>Special Message (T)</h3>
<p>Here is the format: </p>
<dl>
<dd>
<pre>T &lt;text&gt;</pre>
</dl>
<p> Here is an example: </p>
<dl>
<dd>
<pre>T THLS TRIAL SERVICE</pre>
</dl>
<p> &lt;text&gt; is just a text message sent by the beacon operator.</p>
<h3>Null (N)</h3>
<p>This just indicates a null message. There are no fields.</p>
<h3>Unknown message (U)</h3>
<p>This is used to dump message words in hexadecimal when the message type field doesn&#8217;t match any of the known ones. </p>
<p> Here is the format: </p>
<dl>
<dd>
<pre>U &lt;hex-literal&gt;</pre>
</dl>
<p> Here is an example: </p>
<dl>
<dd>
<pre>U 0x76423055</pre>
</dl>
<p> The &lt;hex-literal&gt; will represent 32 bits of information, after parity checks and inversion. The high two bits should be ignored.</p>
<h3>Null (N)</h3>
<p>This just indicates a null message. There are no fields.</p>
<h2>Rtcm3 Dump Format</h2>
<p>RTCM104v3 messages are too complex to be dumped in a fully invertible form without a structural markup at least as complex as XML or YAML. Accordingly, the dump format has been designed to be its own documentation at the expense of reparsability, and is not described here.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/1-gps/">gps</a></code>(1), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3), <code><a href="/docs/linux/man/1-gpsprof/">gpsprof</a></code>(1), <code><a href="/docs/linux/man/1-gpsfake/">gpsfake</a></code>(1).</p>
<h2>Compatibility Note</h2>
<p>In versions of the RTCM2 dump format prior to gpsd 2.28, there was no trailing sentinel line after each stanza of the dump.</p>
<h2>Author</h2>
<p>Much of the portion of this text describing RTCM2 was originally written by John Sager &lt;john.sager [at] btinternet.com&gt; in association with his RTCM decoder. Other material comes from the GPSD project. There is a project page for gpsd <i>here</i>[3].</p>
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
<dt> 3.</p>
<dd>here</p>
<dl>
<dd><a rel="nofollow" href="http://gpsd.berlios.de/">http://gpsd.berlios.de/</a></dl>
