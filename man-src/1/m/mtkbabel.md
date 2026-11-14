---
title: "mtkbabel(1)"
name: "mtkbabel"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mtkbabel/"
description: "mtkbabel – Tool for managing GPS data loggers based on the MTK chip"
---

<h2>NAME</h2>
<p> mtkbabel &#8211; Tool for managing GPS data loggers based on the MTK chip</p>
<h2>SYNOPSIS</h2>
<p> <code>mtkbabel </code>[<code>-abcdEfhilmopRrstvwx</code>]</p>
<h2>DESCRIPTION</h2>
<p> <code>mtkbabel</code> is a command line program to operate GPS data loggers based on the MediaTek MTK chip. It was tested on the i-Blue 747, Qstarz BT-Q1000 and on the Holux M-241, it should work also with other GPS devices based on the same chip. </p>
<p> The main features are:<br />
&nbsp;<wbr>&#8211; Command line interface<br />
&nbsp;<wbr>&#8211; Save data log in GPX and raw binary format<br />
&nbsp;<wbr>&#8211; If required retrieve all the data, also the old one being overlapped<br />
&nbsp;<wbr>&#8211; Change logging criteria: time, distance, speed<br />
&nbsp;<wbr>&#8211; Change log format<br />
&nbsp;<wbr>&#8211; START/STOP logging<br />
&nbsp;<wbr>&#8211; Set OVERLAP or STOP method on memory full<br />
&nbsp;<wbr>&#8211; Erase the internal memory</p>
<h2>USAGE</h2>
<p> In order to use mtkbabel, please follow these instructions: </p>
<p> 1. Attach the GPS data logger device to your computer <code>via USB</code>. </p>
<p> 2. Now you have to switch the GPS device (at least the i-Blue 747) into <code>LOG or NAV mode</code>, otherwise the device will not be powered on, and no connection will be possible. Beware that in NAV mode the device goes into sleep mode if not connected to any Bluetooth device. </p>
<p> 3. In order to use mtkbabel you have to either be root (not recommended) and/or you must have read/write permissions for the USB device file, usually <code>/dev/ttyUSB0</code>. This device usually has permissions <code>&#8216;crw-rw&#8212;- 1 root dialout&#8217;</code>, so you can either add your user to the <code>dialout</code> group (in this example) by doing </p>
<p> <code> $ adduser USERNAME dialout</code> </p>
<p> or (not recommended) make the device world-readable/-writable by doing: </p>
<p> <code> $ chmod 666 /dev/ttyUSB0</code> </p>
<p> Another option is to write a udev rules file to change the owner and permissions of /dev/ttyUSB0 according to your requirements. </p>
<p> 4. You can now run mtkbabel. For example, if you want to download the track log and the list of waypoints you captured on the device, run: </p>
<p> <code> $ mtkbabel -s 115200 -l off -f foo -w -t</code> </p>
<p> The default speed of <code>115200</code> baud should work in most cases and you can omit it, for the Holux M-241 you must use <code>38400</code> instead. This will turn off the autolog function, which is always turned on when you switch on the device. The track log will be in the file <code>foo_trk.gpx</code>, the waypoints in the file <code>foo_wpt.gpx</code> (both in GPX format). The file <code>foo.bin</code> will contain the binary log file. Downloading the data from the GPS device can take several minutes, depending on how much data has to be transferred. </p>
<p> In order to delete all data from the GPS device, run: </p>
<p> <code> $ mtkbabel -s 115200 -E</code></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Read all the log memory (overlapped data).</p>
<dt><code>-b</code> filename.bin</p>
<dd> Do not read data from a GPS device, but rather read a previously saved .bin file. Ignore -f option.</p>
<dt><code>-c</code></p>
<dd> Create a GPX file with both tracks and waypoints.</p>
<dt><code>-d</code> debug_level</p>
<dd> Debug level: 0..7.</p>
<dt><code>-E</code></p>
<dd> Erase data log memory.</p>
<dt><code>-f</code></p>
<dd> Base name for saved files (.bin and .gpx). If you, for example, use <code>-f gpslog</code>, mtkbabel will create files which are called <code>gpslog.gpx</code>, <code>gpslog_trk.gpx</code>, <code>gpslog_wpt.gpx</code> and <code>gpslog.bin</code>.</p>
<dt><code>-h</code></p>
<dd> Show a help text and exit.</p>
<dt><code>-i</code></p>
<dd> Ignore some error conditions and try to extract as much data as possible from GPS.</p>
<dt><code>-l</code> {on|off}</p>
<dd> Turn logging ON/OFF.</p>
<dt><code>-m</code> {stop|overlap}</p>
<dd> Set STOP/OVERLAP recording method on memory full.</p>
<dt><code>-o</code> log_format</p>
<dd> Enable or disable log fields (FIELD1,-FIELD2,&#8230;), available fields: UTC, VALID, LATITUDE, LONGITUDE, HEIGHT, SPEED, HEADING, DSTA, DAGE, PDOP, HDOP, VDOP, NSAT, SID, ELEVATION, AZIMUTH, SNR, RCR, MILLISECOND, DISTANCE.</p>
<dt><code>-p</code> port</p>
<dd> Communication port, default: <code>/dev/ttyUSB0</code>.</p>
<dt><code>-R</code></p>
<dd> Recover from disabled log: erase data and reset recording criteria.</p>
<dt><code>-r</code> time:distance:speed</p>
<dd> Set logging criteria (zero to disable): every 0.10-9999999.90 seconds, every 0.10-9999999.90 meters, over 0.10-9999999.90 km/h. Not all the devices support such wide ranges, more reasonable values are 1-999 seconds, 10-9999 meters and 10-999 km/h.</p>
<dt><code>-s</code> speed</p>
<dd> Serial port speed, default <code>115200</code> baud.</p>
<dt><code>-t</code></p>
<dd> Create a GPX file with tracks.</p>
<dt><code>-v</code></p>
<dd> Show version information and exit.</p>
<dt><code>-w</code></p>
<dd> Create a GPX file with waypoints.</p>
<dt><code>-x</code></p>
<dd> Force reading Holux format. This is required to read-back the binary data produced by some Holux devices, which do not embed into the data itself the Holux identifier string.</dl>
<h2>BUGS</h2>
<p> Please report any bugs to Niccolo Rigacci &lt;niccolo [at] rigacci.org&gt;.</p>
<h2>LICENCE</h2>
<p> <code>mtkbabel</code> is covered by the GNU General Public License (GPL), version 2 or later.</p>
<h2>AUTHORS</h2>
<p> Niccolo Rigacci &lt;niccolo [at] rigacci.org&gt; </p>
<p> This manual page was written by Uwe Hermann &lt;uwe [at] hermann-uwe.de&gt;. It is licensed under the terms of the GNU GPL (version 2 or later). </p>
<h2>Index</h2>
