---
title: "gpscorrelate(1)"
name: "gpscorrelate"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpscorrelate/"
description: "gpscorrelate – correlates digital images with GPS data filling EXIF fields"
---

<h2 class="name">NAME</h2>
<p> gpscorrelate &#8211; correlates digital images with GPS data filling EXIF fields </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gpscorrelate</code> [-z | &#8211;timeadd&nbsp;<wbr>+/-<i>HH</i>[:<i>MM</i>]] [-O | &#8211;photooffset&nbsp;<wbr><i>seconds</i>] [-i | &#8211;no-interpolation] [-v | &#8211;verbose] [-d | &#8211;datum&nbsp;<wbr><i>datum</i>] [-n | &#8211;no-write] [-m | &#8211;max-dist&nbsp;<wbr><i>time</i>] [-t | &#8211;ignore-tracksegs] [-M | &#8211;no-mtime] [-f | &#8211;fix-timestamps] [-p | &#8211;degmins] -g&nbsp;<wbr><i>file.gpx</i> <i>image.jpg</i>&#8230;</p>
<dt> <code>gpscorrelate</code> -s | &#8211;show | -o | &#8211;machine <i>image.jpg</i>&#8230;</p>
<dt> <code>gpscorrelate</code> [-M | &#8211;no-mtime] {-r | &#8211;remove} <i>image.jpg</i>&#8230;</p>
<dt> <code>gpscorrelate</code> -V | &#8211;version | -h | &#8211;help</p>
<dt> <code>gpscorrelate-gui</code></dl>
<h2>DESCRIPTION</h2>
<dd>This manual page documents briefly the <code>gpscorrelate</code> and <code>gpscorrelate-gui</code> commands. </p>
<p> There is an extended documenation available in HTML format; see below. </p>
<p> <code>gpscorrelate</code> is a program that acts on digital images in JPEG format filling EXIF (Exchangeable Image File Format) fields related to GPS (Global Positioning System) information. Source for the GPS data is a record of GPS information encoded in GPX (GPS Exchange Format) Format. The act of filling those fields is referred to as <i>correlation</i>. </p>
<p> If GPS data are available at the precise moment the image was taken (with a 1-second granularity) the GPS data are stored unmodified in EXIF fields. If they are not linear interpolation of GPS data available at moments before and after the image was taken can be used. </p>
<p> <code>gpscorrelate</code> is a command line tool implementing correlation whereas <code>gpscorrelate-gui</code> is the corresponding GTK+ graphical user interface.</p>
<h2>OPTIONS</h2>
<p> These programs follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below. For a complete description, see the HTML documentation. </p>
<p> <code>-g</code>, <code>&#8211;gps</code> <i>file.gpx</i></p>
<dl>
<dt>
<dd> correlate using the specified GPX file with GPS data</dl>
<p> <code>-s</code>, <code>&#8211;show</code></p>
<dl>
<dt>
<dd> only show the GPS data of the given images</dl>
<p> <code>-o</code>, <code>&#8211;machine</code></p>
<dl>
<dt>
<dd> only show the GPS data of the given images in a machine readable output, if there is any</dl>
<p> <code>-r</code>, <code>&#8211;remove</code></p>
<dl>
<dt>
<dd> only remove GPS EXIF data from the given images</dl>
<p> <code>-z</code>, <code>&#8211;timeadd</code> <code>+/-</code><i>XX</i>[<code>:</code><i>XX</i>]</p>
<dl>
<dt>
<dd> time to add to GPS data to make it match the timestamps of the images. GPS data is in UTC; images are not likely to be in UTC. Enter the timezone used when taking the images: eg, <code>+8</code> for Perth</dl>
<p> <code>-O</code>, <code>&#8211;photooffset</code> <i>seconds</i></p>
<dl>
<dt>
<dd> time in seconds to add to the photo timestamp to make it match the GPS timestamp. To determine the amount of seconds needed, just create a picture of your GPS device showing the current time and compare it with the timestamp of your photo file.</dl>
<p> <code>-i</code>, <code>&#8211;no-interpolation</code></p>
<dl>
<dt>
<dd> disable interpolation between points. Interpolation is linear, points are rounded if disabled</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> show which GPS data has been selected for each image</dl>
<p> <code>-d</code>, <code>&#8211;datum</code> <i>datum</i></p>
<dl>
<dt>
<dd> specify measurement datum. If not set, WGS-84 used</dl>
<p> <code>-n</code>, <code>&#8211;no-write</code></p>
<dl>
<dt>
<dd> do not write the exif data. Useful with <code>&#8211;verbose</code></dl>
<p> <code>-m</code>, <code>&#8211;max-dist</code> <i>time</i></p>
<dl>
<dt>
<dd> max time outside points that image will be matched. Time is in seconds</dl>
<p> <code>-t</code>, <code>&#8211;ignore-tracksegs</code></p>
<dl>
<dt>
<dd> Interpolate between track segments, too</dl>
<p> <code>-M</code>, <code>&#8211;no-mtime</code></p>
<dl>
<dt>
<dd> Do not change mtime of modified files</dl>
<p> <code>-f</code>, <code>&#8211;fix-timestamps</code></p>
<dl>
<dt>
<dd> Fix broken GPS datestamps written with versions &lt; 1.5.2</dl>
<p> <code>-p</code>, <code>&#8211;degmins</code></p>
<dl>
<dt>
<dd> Write location as DD MM.MM as was default before &lt; 1.5.3</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Only show summary of options</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Only print the version</dl>
<h2>SEE ALSO</h2>
<p> gpsd (1), gpsbabel (1), gpxlogger (1), cgpxlogger (1). </p>
<p> The documentation of gpscorrelate and gpscorrelate-gui in HTML format are available on the filesystem at /usr/share/doc/gpscorrelate-1.6.0.</p>
<h2>AUTHOR</h2>
<p> This manual page was initially written by Stefano Zacchiroli zack [at] debian.org for the Debian(TM) system. It was extended by Till Maas opensource [at] till.name. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 any later version published by the Free Software Foundation. </p>
<p> On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>AUTHOR</h2>
<p> <code>Stefano Zacchiroli</code></p>
<dl>
<dt>
<dd> Author.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006, 2008 Stefano Zacchiroli zack [at] debian.org, Till Maas </p>
<h2>Index</h2>
