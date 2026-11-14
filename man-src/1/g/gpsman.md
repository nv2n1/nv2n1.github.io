---
title: "gpsman(1)"
name: "gpsman"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpsman/"
description: "gpsman – a (graphical) manager of GPS data"
---

<h2>NAME</h2>
<p> gpsman &#8211; a (graphical) manager of GPS data</p>
<h2>SYNOPSIS</h2>
<p> <code>gpsman</code> [<code>-dev</code> <i>[usb=]DEVICE</i>]<br />
 <code>gpsman</code> [<i>OPTIONS</i>] <i>COMMAND</i> [<i>COMMAND_ARGS</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>gpsman</code> GPS Manager (GPSMan) is a graphical manager of GPS data that makes possible the preparation, inspection and edition of GPS data in a friendly environment. GPSMan supports communication and real-time logging with Garmin, Lowrance and Magellan receivers and accepts real-time logging information in NMEA 0183 from any GPS receiver. </p>
<p> To comunicate with the GPS port the user must have been granted read/write permissions for the corresponding device. </p>
<p> For use in graphical mode GPSMan must be invoked as in the first form above, where the <code>usb=</code> prefix to the device path enforces the use of the Garmin USB protocol. The use in this mode is not further described here, a full description being given in the User Manual available along with the GPSMan distribution. </p>
<p> GPSMan can also be used in command line mode (with no graphical interface), in which case it must be invoked as in the second form above. The sections below address this mode.</p>
<h2>EXIT STATUS</h2>
<p> In non-graphical mode GPSMan exits with either a 0 if <i>COMMAND</i> was successfully executed, or a 1 if not. Some commands will write information to the standard output channel. Error messages can possibly be written to the standard error channel, but most of the errors will not be explained. In case of doubt the graphical mode should be used to see if there are problems with files or the receiver.</p>
<h2>OPTIONS</h2>
<p> Apart from the <code>-dev</code> option all other options are only for use in non-graphical mode.</p>
<dl>
<dt><code>-dev</code> <i>DEVICE</i> gives the device path.</p>
<dd>
<dt><code>-log</code> creates a log file of the serial communication</p>
<dd> under the name <code>logfile</code> in the GPSMan user directory.</p>
<dt><code>-rec Garmin | Lowrance | Magellan</code></p>
<dd> changes the brand of the receiver (NOTE: at present will only work with <code>Garmin</code>); this option can be useful to override the options in the preferences file; cannot be used with the <code>readput</code> command, nor with the <code>-prefs</code> option, and cannot occur after the <code>-prot</code> option.</p>
<dt><code>-prefs</code> <i>PREFSFILE</i></p>
<dd> gives the path for an alternative preferences file (read after the user preferences file); cannot be used with the <code>-rec</code> option.</p>
<dt><code>-prot</code> <i>PROTOCOL</i></p>
<dd> selects the protocol to be used for connecting to the receiver; cannot occur before the <code>-rec</code> option; the <code>show protocols</code> command can be used to find out which protocols are available.</dl>
<p> Options not related with <i>COMMAND</i> will be silently ignored.</p>
<h2>NAME=VALUE ARGUMENTS</h2>
<p> Some commands accept parameters in the form <i>NAME=VALUE</i>. The term <i>PARAM</i> when used here referring to arguments of a command has always this meaning. Care should be taken if the value part is a string with spaces (or other characters with special meaning for the shell or system command interpreter) in which case quotes or some other form of quoting should be used.</p>
<h2>GPSMAN COMMAND SUMMARY</h2>
<p> There is no room in a manual page to describe in detail the available commands. The following list gives a synopsis for all of them:</p>
<dl>
<dt><code>is available</code> exits with 0.</p>
<dd>
<dt><code>is connected</code></p>
<dd> exits with 0 if a connection check with the receiver succeeds.</p>
<dt><code>show </code><i>WHAT</i> writes help information to the standard output; <i>WHAT</i> is one of: <code>datums</code>, <code>formats</code> (data file formats), <code>help</code>, <code>projections</code>, <code>protocols</code>, <code>symbols</code> (waypoint symbols), <code>transfs</code></p>
<dd> (coordinates transformations).</p>
<dt><code>haslib</code> <i>LIBRARY</i> checks availability of library</p>
<dd>
<dt><code>getwrite</code> <i>INTYPES</i> <i>FORMAT</i> [<i>OUTTYPES</i>] [<i>OUTPARAMS</i>] <i>PATH</i> transfers data from the receiver to a file.</p>
<dd>
<dt><code>readput</code> <i>FORMAT</i> [<i>INPARAMS</i>] [<i>INTYPES</i>] <i>PATH</i> [<i>OUTTYPES</i>] transfers data from a file to the receiver.</p>
<dd>
<dt><code>getrtimelog</code> <i>PATH</i> [<i>INTERVAL</i>] gets the real-time log from the receiver and saves it to a file.</p>
<dd>
<dt><code>getfix</code> <i>PATH</i> [<i>TIMEOUT</i>] gets the current fix data from the receiver and saves it to a file.</p>
<dd>
<dt><code>getalmanac</code> <i>PATH</i> gets the current almanac data from the receiver and saves it to a file.</p>
<dd>
<dt><code>read</code> <i>IN-FORMAT</i> [<i>PARAMS</i>] [<i>TYPES</i>] <i>PATH</i> reads a data file and launches the graphical interface (in GPSMan scripts the behaviour is different; see the <code>exec</code> command in the user manual).</p>
<dd>
<dt><code>start travel</code> [<i>INTERVAL</i>] launches the graphical interface and starts real-time logging, animation and travelling.</p>
<dd>
<dt><code>translate</code> <i>FORMAT</i> [<i>INPARAMS</i>] [<i>INTYPES</i>] <i>PATH</i> [<i>HOWPARAMS</i>] <i>FORMAT</i> [<i>OUTPARAMS</i>] [<i>OUTTYPES</i>] <i>PATH</i> translates from a file format to another.</p>
<dd>
<dt><code>project</code> <i>LATD</i> <i>LONGD</i> <i>DATUM</i> <i>PROJECTION</i> <i>[PARAMS]</i> writes to the standard output the projection of a point.</p>
<dd>
<dt><code>georef</code> <i>IMGPATH</i> <i>TRANSF</i> <i>LATD</i> <i>LONGD</i> <i>LATD</i> <i>LONGD</i> <i>[LATD LONGD]</i> <i>DATUM</i> <i>X</i> <i>Y</i> <i>X</i> <i>Y</i> <i>[X Y]</i> <i>PROJECTION</i> <i>[PARAMS]</i> writes to the standard output a map information file.</p>
<dd>
<dt><code>geopicts</code> <i>FORMAT</i> [<i>INPARAMS</i>] <i>INTYPE</i> <i>PATH</i> [<i>PROCPARAMS</i>] [<i>FORMAT</i>] [<i>OUTPARAMS</i>] <i>PATH</i> <i>PICTPATHS</i> geo-references files either based on their time-stamps and a given track, or by using the sequence of waypoints in a group.</p>
<dd>
<dt><code>source</code> <i>PATH</i> executes a Tcl/Tk script.</p>
<dd>
<dt><code>exec</code> <i>PATH</i> executes a GPSMan script.</p>
<dd></dl>
<h2>AUTHORS</h2>
<p> This manual page was written by Miguel Filgueiras &lt;mig [at] ncc.up.pt&gt; using a previous version by Rogerio Reis &lt;rvr [at] ncc.up.pt&gt;. </p>
<p> GPSMan: developed and maintained by Miguel Filgueiras, with contributions by Brian Baulch, Rogerio Reis, Andreas Lange, Alessandro Palmas, Niki Hammler, Martin Ostermann, Valere Robin, David Wolfskill, Rob Buitenhuis, Frank Kujawski, Tri Agus Prayitno, Matt Martin, Stefan Heinen, Heiko Thede, Sabine Broda, Alberto Morales, Martin Buck, David Kaplan, Jean H. Theoret, Paul Scorer, Nigel Orr, David Gardner, Nikolai Kosyakoff, Benoit Steiner.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;mig_AT_ncc.up.pt&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1998-2008 Miguel Filgueiras and Rogerio Reis<br />
 LIACC &amp; DCC Faculdade de Ciencias/ University of Porto </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> Miguel Filgueiras, <code>GPSMan User Manual</code>, Version 6.4, September 2008<br />
 This manual, in both PDF and HTML, is part of the distribution of GPSMan and can be retrieved from the GPSMan site at <code><a rel="nofollow" href="http://www.ncc.up.pt/gpsman">http://www.ncc.up.pt/gpsman</a></code>. </p>
<h2>Index</h2>
