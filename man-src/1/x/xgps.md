---
title: "xgps(1)"
name: "xgps"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xgps/"
description: "gps, xgps, xgpsspeed, cgps, lcdgps, gegps – test clients for gpsd"
---

<h2 class="name">NAME</h2>
<p> gps, xgps, xgpsspeed, cgps, lcdgps, gegps &#8211; test clients for gpsd </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xgps</code> [-D&nbsp;<wbr><i>debug-level</i>] [-h] [-V] [-l&nbsp;<wbr>[[d]&nbsp;<wbr>|&nbsp;<wbr>[m]&nbsp;<wbr>|&nbsp;<wbr>[s]]] [-u&nbsp;<wbr>[[i]&nbsp;<wbr>|&nbsp;<wbr>[n]&nbsp;<wbr>|&nbsp;<wbr>[m]]] [<i>server</i> [<i>:port</i> [<i>:device</i>]]]</p>
<dt> <code>xgpsspeed</code> [-D&nbsp;<wbr><i>debug-level</i>] [-h] [-V] [&#8211;speedunits&nbsp;<wbr>{[mph]&nbsp;<wbr>|&nbsp;<wbr>[kph]&nbsp;<wbr>|&nbsp;<wbr>[knots]}] [<i>server</i> [<i>:port</i> [<i>:device</i>]]]</p>
<dt> <code>cgps</code> [-D&nbsp;<wbr><i>debug-level</i>] [-h] [-V] [-l&nbsp;<wbr>[[d]&nbsp;<wbr>|&nbsp;<wbr>[m]&nbsp;<wbr>|&nbsp;<wbr>[s]]] [-m] [-s] [-u&nbsp;<wbr>[[i]&nbsp;<wbr>|&nbsp;<wbr>[n]&nbsp;<wbr>|&nbsp;<wbr>[m]]] [<i>server</i> [<i>:port</i> [<i>:device</i>]]]</p>
<dt> <code>lcdgps</code> [-h] [-V] [-l&nbsp;<wbr>[[d]&nbsp;<wbr>|&nbsp;<wbr>[m]&nbsp;<wbr>|&nbsp;<wbr>[s]]] [-u&nbsp;<wbr>[[i]&nbsp;<wbr>|&nbsp;<wbr>[n]&nbsp;<wbr>|&nbsp;<wbr>[m]]] [<i>server</i> [<i>:port</i> [<i>:device</i>]]]</p>
<dt> <code>gpxlogger</code> [-D&nbsp;<wbr><i>debug-level</i>] [-d] [-e&nbsp;<wbr><i>export-method</i>] [-f&nbsp;<wbr><i>filename</i>] [-l] [-m&nbsp;<wbr><i>minmove</i>] [-h] [-V] [-i&nbsp;<wbr><i>track timeout</i>] [<i>server</i> [<i>:port</i> [<i>:device</i>]]]</p>
<dt> <code>gegps</code> [-d&nbsp;<wbr><i>directory</i>] [-i]</dl>
<h2>DESCRIPTION</h2>
<dd>These are the demonstration clients shipped with gpsd. They have some common options: </p>
<p> The <code>-h</code> option causes each client to emit a summary of its options and then exit. </p>
<p> The <code>-V</code> option causes each client to dump the package version and exit. </p>
<p> The <code>-l</code> option, when present, sets the format of latitude and longitude reports. The value &#8216;d&#8217; produces decimal degrees and is the default. The value &#8216;m&#8217; produces degrees and decimal minutes. The value &#8216;s&#8217; produces degrees, minutes, and decimal seconds. </p>
<p> xgps, cgps, and lcdgps look at variables in the environment to figure out what units they should default to using for display &#8212; imperial, nautical, or metric. Here are the variables and values they check: </p>
<dl>
<dt>
<dd>
<pre><code>
GPSD_UNITS one of : imperial = miles / feet
                                           nautical = knots / feet
                                                                  metric = km / meters
                                                                                    LC_MEASUREMENT
                                                                                        en_US = miles / feet
                                                                                                            C = miles / feet
                                                                                                                            POSIX = miles / feet
                                                                                                                                                [other] = km / meters
                                                                                                                                                                   LANG
                                                                                                                                                                       en_US = miles / feet
                                                                                                                                                                                           C = miles / feet
                                                                                                                                                                                                           POSIX = miles / feet
                                                                                                                                                                                                                               [other] = km / meters
</code></pre>
</dl>
<p> These preferences may be overridden by the <code>-u</code> option. </p>
<p> Where present, the <code>-u</code> option can be used to set the system units for display; follow the keyword with &#8216;i&#8217; for &#8216;imperial&#8217; for American units (feet in altitude and error estimates, miles per hour in speeds), &#8216;n&#8217; for &#8216;nautical&#8217; (feet in altitude and error estimates, knots in speed) or &#8216;m&#8217; for &#8216;metric&#8217; (meters in altitude and error estimates, kilometers per hour in speeds). </p>
<p> The <code>-D</code> option, when present, sets a debug level; it is primarily for use by GPSD developers. It enables various progress messages to standard error. </p>
<p> By default, clients collect data from all compatible devices on localhost, using the default GPSD port 2947. An optional argument to any client may specify a server to get data from. A colon-separated suffix is taken as a port number. If there is a second colon-separated suffix, that is taken as a specific device name to be watched. However, if the server specification contains square brackets, the part inside them is taken as an IPv6 address and port/device suffixes are only parsed after the trailing bracket. Possible cases look like this: </p>
<p> localhost:/dev/ttyS1</p>
<dl>
<dt>
<dd> Look at the default port of localhost, trying both IPv4 and IPv6 and watching output from serial device 1.</dl>
<p> example.com:2317</p>
<dl>
<dt>
<dd> Look at port 2317 on example.com, trying both IPv4 and IPv6.</dl>
<p> 71.162.241.5:2317:/dev/ttyS3</p>
<dl>
<dt>
<dd> Look at port 2317 at the specified IPv4 address, collecting data from attached serial device 3.</dl>
<p> [FEDC:BA98:7654:3210:FEDC:BA98:7654:3210]:2317:/dev/ttyS5</p>
<dl>
<dt>
<dd> Look at port 2317 at the specified IPv6 address, collecting data from attached serial device 5.</dl>
<p> Not all clients shipped with GPSD are documented here. See also the separate manual pages for <code><a href="/docs/linux/man/1-gpspipe/">gpspipe</a></code>(1) and <code><a href="/docs/linux/man/1-gpsmon/">gpsmon</a></code>(1).</p>
<h3>xgps</h3>
<p> xgps is a simple test client for gpsd with an X interface. It displays current GPS position/time/velocity information and (for GPSes that support the feature) the locations of accessible satellites. </p>
<p> In the sky view, satellites are color-coded to indicate quality of signal; consult the data display to the left for exact figures in dB. Square icons indicate WAAS/EGNOS satellites, circles indicate ordinary GPS satellites. Filled icons were used in the last fix, outline icons were not.</p>
<h3>xgpsspeed</h3>
<p> xgpsspeed is a speedometer that uses position information from the GPS. It accepts an -h option and optional argument as for gps, or a -V option to dump the package version and exit. </p>
<p> The default display mode resembles a car speedometer. With the option &#8211;nautical you get a more elaborate speed and track presentation modeled after a marine navigation display. </p>
<p> The -speedunits option can be used to set the speed units for display; follow the keyword with knots for nautical miles per hour, kph for kilometres per hour, or mph for miles per hour. The default is miles per hour. </p>
<p> In the nautical mode only, &#8211;maxspeed sets the maximum on the speedometer.</p>
<h3>cgps</h3>
<p> cgps is a client resembling xgps, but without the pictorial satellite display and able to run on a serial terminal or terminal emulator. </p>
<p> The <code>-s</code> option prevents cgps from displaying the data coming from the daemon. This display can also be toggled with the s command. </p>
<p> The <code>-m</code> option will display your magnetic heading (as opposed to your true heading). This is a calculated value, not a measured value, and is subject to a potential error of up to two degrees in the areas for which the calculation is valid (currently Western Europe, Alaska, and Lower 48 in the USA). The formulas used are those found in the Aviation Formulary v1.43. </p>
<p> cgps terminates when you send it a SIGHUP or SIGINT; given default terminal settings this will happen when you type Ctrl-C at it. It will also terminate on &#8216;q&#8217;</p>
<h3>lcdgps</h3>
<p> A client that passes gpsd data to lcdproc, turning your car computer into a very expensive and nearly feature-free GPS receiver. Currently assumes a 4&#215;40 LCD and writes data formatted to fit that size screen. Also displays 4- or 6-character Maidenhead grid square output.</p>
<h3>gpxlogger</h3>
<p> This program collects fixes from gpsd and logs them to standard output in GPX, an XML profile for track logging. </p>
<p> The output may be composed of multiple tracks. A new track is created if there&#8217;s no fix for an interval specified by the <code>-i</code> and defaulting to 5 seconds. </p>
<p> The <code>-d</code> option tells gpxlogger to run as a daemon in background. It requires the <code>-f</code> option, which directs output to a specified logfile. </p>
<p> The <code>-m</code> option sets a minimum move distance in meters (it may include a fractional decimal part). Motions shorter than this will not be logged. </p>
<p> gpxlogger can use any of the export methods that gpsd supports. For a list of these methods, use the <code>-l</code>. To force the method, give the <code>-e</code> one of the colon-terminated method names from the <code>-l</code> table. </p>
<p> If D-Bus support is available on the host, GPSD is configured to use it, and <code>-e dbus</code> is specified, this program listens to DBUS broadcasts from gpsd via org.gpsd.fix. </p>
<p> With <code>-e sockets</code>, or if sockets is the method defaulted to, you may give a server-port-device specification as arguments.</p>
<h3>gegps</h3>
<p> This program collects fixes from gpsd and feeds them to a running instance of Google Earth for live location tracking. </p>
<p> The <code>-d</code> argument is the location of the Google Earth installation directory. If not specified, it defaults to the current directory. </p>
<p> If you have the free (non-subscription) version, start by running with the <code>-i</code> option to drop a clue in the Google Earth installation directory, as &#8216;Open_in_Google_Earth_RT_GPS.kml&#8217;, then open that file in Places (File &gt; Open&#8230;). Run gpsd in the normal way after that.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3), <code><a href="/docs/linux/man/1-gpsfake/">gpsfake</a></code>(1), <code><a href="/docs/linux/man/1-gpsctl/">gpsctl</a></code>(1), <code><a href="/docs/linux/man/1-gpscat/">gpscat</a></code>(1), <code><a href="/docs/linux/man/1-gpsprof/">gpsprof</a></code>(1). <code><a href="/docs/linux/man/1-gpspipe/">gpspipe</a></code>(1). <code><a href="/docs/linux/man/1-gpsmon/">gpsmon</a></code>(1).</p>
<h2>AUTHORS</h2>
<p> Remco Treffcorn, Derrick Brashear, Russ Nelson &amp; Eric S. Raymond, Jeff Francis (cgps). Amaury Jacquot &lt;sxpert [at] sxpert.org&gt; &amp; Petter Reinholdtsen &lt;pere [at] hungry.com&gt; (gpxlogger). Chris Kuethe &lt;chris.kuethe [at] gmail.com&gt; (gpxlogger), Chen Wei &lt;weichen302 [at] aol.com&gt; (gegps &amp; xgpsspeed), Robin Wittler &lt;real [at] the-real.org&gt; (xgpsspeed). </p>
<p> This manual page by Eric S. Raymond &lt;esr [at] thyrsus.com&gt; </p>
<h2>Index</h2>
