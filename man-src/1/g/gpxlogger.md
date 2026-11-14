---
title: "gpxlogger(1)"
name: "gpxlogger"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpxlogger/"
description: "gps, xgps, xgpsspeed, cgps, lcdgps, cgpxlogger – test clients for gpsd"
---

<h2 class="name">NAME</h2>
<p> gps, xgps, xgpsspeed, cgps, lcdgps, cgpxlogger &#8211; test clients for gpsd </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xgps</code> [<i>X-options</i>] [-h] [-V] [-j] [-speedunits&nbsp;<wbr>{[mph]&nbsp;<wbr>|&nbsp;<wbr>[kph]&nbsp;<wbr>|&nbsp;<wbr>[knots]}] [-altunits&nbsp;<wbr>{[feet]&nbsp;<wbr>|&nbsp;<wbr>[meters]}] [-l&nbsp;<wbr>[[d]&nbsp;<wbr>|&nbsp;<wbr>[m]&nbsp;<wbr>|&nbsp;<wbr>[s]]] [<i>server</i> [<i>:port</i> [<i>:device</i>]]]</p>
<dt> <code>xgpsspeed</code> [-rv] [<i>X-options</i>] [-h] [-V] [-nc&nbsp;<wbr><i>X-color</i>] [-speedunits&nbsp;<wbr>{[mph]&nbsp;<wbr>|&nbsp;<wbr>[kph]&nbsp;<wbr>|&nbsp;<wbr>[knots]}] [<i>server</i> [<i>:port</i> [<i>:device</i>]]]</p>
<dt> <code>cgps</code> [-h] [-V] [-j] [-speedunits&nbsp;<wbr>{[mph]&nbsp;<wbr>|&nbsp;<wbr>[kph]&nbsp;<wbr>|&nbsp;<wbr>[knots]}] [-altunits&nbsp;<wbr>{[feet]&nbsp;<wbr>|&nbsp;<wbr>[meters]}] [-l&nbsp;<wbr>[[d]&nbsp;<wbr>|&nbsp;<wbr>[m]&nbsp;<wbr>|&nbsp;<wbr>[s]]] [-m] [-s] [<i>server</i> [<i>:port</i> [<i>:device</i>]]]</p>
<dt> <code>lcdgps</code> [-h] [-V] [-j] [-l&nbsp;<wbr>[[d]&nbsp;<wbr>|&nbsp;<wbr>[m]&nbsp;<wbr>|&nbsp;<wbr>[s]]] [-u&nbsp;<wbr>[[i]&nbsp;<wbr>|&nbsp;<wbr>[n]&nbsp;<wbr>|&nbsp;<wbr>[m]]] [<i>server</i> [<i>:port</i> [<i>:device</i>]]]</p>
<dt> <code>gpxlogger</code></p>
<dt> <code>gpxlogger</code> [-h] [-V] [-j] [-i&nbsp;<wbr><i>track timeout</i>] [<i>server</i> [<i>:port</i> [<i>:device</i>]]]</dl>
<h2>DESCRIPTION</h2>
<dd>These are the demonstration clients shipped with gpsd. They have some common options: </p>
<p> The <code>-h</code> option causes each client to emit a summary of its options and then exit. </p>
<p> The <code>-V</code> option causes each client to dump the package version and exit. </p>
<p> The <code>-j</code> option, where present, tells the daemon to hold fix data across cycles, eliminating jitter from NMEA devices that emit several partial reports. The downside is that with this switch on the client will occasionally report stale or invalid data held over from a previous cycle. This option is ineffective, and not needed, on SiRFs and most other non-NMEA GPSes. See also the discussion of the J command in <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8). </p>
<p> The <code>-l</code> option, when present, sets the format of latitude and longitude reports. The value &#8216;d&#8217; produces decimal degrees and is the default. The value &#8216;m&#8217; produces degrees and decimal minutes. The value &#8216;s&#8217; produces degrees, minutes, and decimal seconds. </p>
<p> An optional argument to any client may specify a server to get data from; a colon-separated suffix is taken as a port number. If there is a second colon-separated suffix, that is taken as a device name to be handed to the daemon in an F= command (or equivalent). </p>
<p> Not all clients shipped with GPSD are documented here. See also the separate manual pages for <code><a href="/docs/linux/man/1-gpspipe/">gpspipe</a></code>(1) and <code><a href="/docs/linux/man/1-gpsmon/">gpsmon</a></code>(1).</p>
<h3>xgps</h3>
<p> xgps is a simple test client for gpsd with an X interface. It displays current GPS position/time/velocity information and (for GPSes that support the feature) the locations of accessible satellites. </p>
<p> In the sky view, satellites are color-coded to indicate quality of signal; consult the data display to the left for exact figures in dB. Diamond icons indicate WAAS/EGNOS satellites, circles indicate ordinary GPS satellites. Filled icons were used in the last fix, outline icons were not. </p>
<p> The <code>-speedunits</code> option can be used to set the speed units for display; follow the keyword with knots for nautical miles per hour, kph for kilometres per hour, or mph for miles per hour. The default is miles per hour. This option can also be set as the X resource &#8216;speedunits&#8217;. </p>
<p> The <code>-altunits</code> option can be used to set the altitude units for display; follow the keyword with &#8216;meters&#8217; or &#8216;feet&#8217;. The default is feet. This option can also be set as the X resource &#8216;altunits&#8217;. </p>
<p> There is a known bug in xgps; it assumes the default font size is no more than 18 pixels. If this is not the case, the satellite data display will show fewer than 12 satellites.</p>
<h3>xgpsspeed</h3>
<p> xgpsspeed is a speedometer that uses position information from the GPS. It accepts an -h option and optional argument as for gps, or a -V option to dump the package version and exit. Additionally, it accepts -rv (reverse video) and -nc (needle color) options. </p>
<p> The -speedunits option can be used to set the speed units for display; follow the keyword with knots for nautical miles per hour, kph for kilometres per hour, or mph for miles per hour. The default is miles per hour. This option can also be set as the X resource &#8216;speedunits&#8217;.</p>
<h3>cgps</h3>
<p> cgps is a client resembling xgps, but without the pictorial satellite display and able to run on a serial terminal or terminal emulator. </p>
<p> The <code>-s</code> option prevents cgps from displaying the raw data. This display can also be toggled with the s command. </p>
<p> The <code>-m</code> option will display your magnetic heading (as opposed to your true heading). This is a calculated value, not a measured value, and is subject to a potential error of up to two degrees in the areas for which the calculation is valid (currently Western Europe, Alaska, and Lower 48 in the USA). The formulas used are those found in the Aviation Formulary v1.43. </p>
<p> Rather than use X resources to determine which units to use, cgps looks at variables in its environment. Here are the variables and values it checks: </p>
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
<p> cgps terminates when you send it a SIGHUP or SIGINT; given default terminal settings this will happen when you type Ctl-C at it. It will also terminate on &#8216;q&#8217;</p>
<h3>lcdgps</h3>
<p> A client that passes gpsd data to lcdproc, turning your car computer into a very expensive and nearly feature-free GPS receiver. Currently assumes a 4&#215;40 LCD and writes data formatted to fit that size screen. Also displays 4- or 6-character Maidenhead grid square output. </p>
<p> Options are as for cgps, except: The <code>-u</code> sets the display format the units used for altitude and speed. The options are: lqirq for Imperial units (feet/miles-per-hour); lqnrq for nautical (feet/knots); &#8216;m&#8217; for metric (meters/kilometers-per-hour).</p>
<h3>gpxlogger</h3>
<p> This program collects fixes from gpsd and logs them to standard output in GPX, an XML profile for track logging. </p>
<p> The output may be composed of multiple tracks. A new track is created if there&#8217;s no fix for an interval specified by the <code>-i</code> and defaulting to 5 seconds. </p>
<p> If D-Bus support is available on the host and GPSD is configured to use it, this program listens to DBUS broadcasts from gpsd. (org.gpsd.fix). Otherwise, it uses a conventional socket connection. </p>
<p> The <code>-j</code> option is only meaningful in socket mode and when collecting fixes from an NMEA device. Presence of a server-port-device specification forces use of sockets even on a D-Bus capable system, though this is unlikely to be of interest to anyone except GPSD developers.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-gpsd/">gpsd</a></code>(8), <code><a href="/docs/linux/man/3-libgps/">libgps</a></code>(3), <code><a href="/docs/linux/man/3-libgpsd/">libgpsd</a></code>(3), <code><a href="/docs/linux/man/1-gpsfake/">gpsfake</a></code>(1), <code><a href="/docs/linux/man/1-gpsctl/">gpsctl</a></code>(1), <code><a href="/docs/linux/man/1-gpscat/">gpscat</a></code>(1), <code><a href="/docs/linux/man/1-gpsprof/">gpsprof</a></code>(1). <code><a href="/docs/linux/man/1-gpspipe/">gpspipe</a></code>(1). <code><a href="/docs/linux/man/1-gpsmon/">gpsmon</a></code>(1).</p>
<h2>AUTHORS</h2>
<p> Remco Treffcorn, Derrick Brashear, Russ Nelson &amp; Eric S. Raymond, Jeff Francis (cgps). Amaury Jacquot sxpert [at] sxpert.org &amp; Petter Reinholdtsen pere [at] hungry.com (gpxlogger). Chris Kuethe chris.kuethe [at] gmail.com (cgpxlogger). </p>
<p> This manual page by Eric S. Raymond esr [at] thyrsus.com. There is a project page, with xgps screenshots, at m[blue]<code>berlios.de</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> berlios.de</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://gpsd.berlios.de/">http://gpsd.berlios.de/</a></dl>
</dl>
<h2>Index</h2>
