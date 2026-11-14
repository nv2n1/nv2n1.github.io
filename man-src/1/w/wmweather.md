---
title: "wmweather(1)"
name: "wmweather"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wmweather/"
description: "wmweather – dockable weather monitor"
---

<h2>NAME</h2>
<p> wmweather &#8211; dockable weather monitor</p>
<h2>SYNOPSIS</h2>
<p> <code>wmweather</code> -s&nbsp;<wbr><i>&lt;4-char ICAO location indicator&gt;&nbsp;<wbr></i>[<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>wmweather</code> monitors local weather conditions: temperature, dew point, pressure, humidity and wind direction and speed. The user needs to specify a 4-character `ICAO location indicator&#8217;. The standardized METAR station designations and current weather reports are designed for use by the aviation community. Since most major cities have at least one airport, there is usually one or more METAR stations in a given city. You&#8211;obviously&#8211;need to be connected to the internet and you also need to have libcurl installed. <code>wmweather</code> will then attempt to download the latest METAR report for the station of your choice from the National Weather Sevice run by NOAA. </p>
<p> You can toggle back and forth between imperial and metric units, i.e. between degrees Fahrenheit, inches of Mercury, and miles per hour&#8211;and&#8211;degrees Celsius, hectoPascal, and kilometers per hour. A middle click will do this. </p>
<p> Also, a left click will bring up the fully decoded METAR report in xmessage. And a right click will force an immediate update, i.e. <code>wmweather</code> will attempt to grab weather information.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s&nbsp;<wbr></code><i>id</i><code>, &#8211;station=</code><i>id</i></p>
<dd> This option tells <code>wmweather</code> which METAR station to show data for. <i>id</i> can be any four-letter ICAO location indicator, which can be found at <i><a rel="nofollow" href="http://www.nws.noaa.gov/tg/siteloc.shtml">http://www.nws.noaa.gov/tg/siteloc.shtml</a></i>.</p>
<dt><code>-c, &#8211;compat</code></p>
<dd> Switch into compatibility mode. The old monitor style will be used, default metric pressure units are millimeters of Mercury instead of hectoPascal, and the colorization options are enabled. When the time turns red, this means that the weather report is older than 24 hours. When the wind speed turns red, this means that the wind is gusty and the listed value is an average only. Similarly, a red direction indicates a variable wind direction and the value given is the average direction. The symbolic link <i>wmWeather</i> is functionally equivalent to <i>wmweather &#8211;compat</i>.</p>
<dt><code>-d&nbsp;<wbr></code><i>[@]min</i><code>, &#8211;delay=</code><i>[@]min</i></p>
<dd> Set the time (in minutes) between updates, default is 15 minutes. Use <i>@</i> to specify minutes past the hour.</p>
<dt><code>-m, &#8211;metric</code></p>
<dd> Display metric values: temperatures in degrees Celsius rather than degrees Fahrenheit, pressure in hectoPascal rather than inches of Mercury, and wind speed in kilometers per hour rather than miles per hour. This option can be toggled at runtime using a middle click.</p>
<dt><code>-w, &#8211;chill, -W</code></p>
<dd> Display wind chill&#8211;if available&#8211;instead of dew point temperature.</p>
<dt><code>-e, &#8211;heat</code></p>
<dd> Display wind heat index&#8211;if available&#8211;instead of temperature.</p>
<dt><code>-b, &#8211;beaufort</code></p>
<dd> Display wind speed on the `Beaufort scale&#8217;.</p>
<dt><code>-n, &#8211;knots</code></p>
<dd> Display wind speed in units of knots, i.e. sea miles per hour.</p>
<dt><code>-u, &#8211;utc</code></p>
<dd> Display update time in UTC instead of localtime. This is equivalent to &#8211;time=+0000.</p>
<dt><code>-t&nbsp;<wbr></code><i>offset</i><code>, &#8211;time=</code><i>offset</i></p>
<dd> Convert update time according to (RFC 822 compliant) time <i>offset</i> rather than to localtime, e.g. &#8211;time=+0100 for MET.</p>
<dt><code>-x&nbsp;<wbr></code><i>host[:port]</i><code>, &#8211;proxy=</code><i>host[:port]</i></p>
<dd> Proxy specification, this option is passed to libcurl.</p>
<dt><code>-U&nbsp;<wbr></code><i>username[:password]</i><code>, &#8211;proxy-user=</code><i>username[:password]</i></p>
<dd> Proxy authentication, this option is passed to libcurl. Please don&#8217;t specify this option, use the file <code>~/.netrc</code> for authentication instead.</p>
<dt><code>&#8211;lcd</code></p>
<dd> Use LCD style display.</p>
<dt><code>&#8211;display=</code><i>id</i></p>
<dd> Set the display to use, e.g. &#8211;display=:0.0.</p>
<dt><code>&#8211;geometry=</code><i>pos</i></p>
<dd> Set the position of the dock app. Note that the size (64&#215;64) is hard-coded and cannot be changed.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display a list of command-line options.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Display the program version.</p>
<dt><code>-a, &#8211;hPa</code></p>
<dd> When toggled to metric, display pressure in units of hectoPascals, i.e. milliBars.</p>
<dt><code>-k, &#8211;kPa</code></p>
<dd> When toggled to metric, display pressure in units of kiloPascals.</p>
<dt><code>-g, &#8211;mmHg</code></p>
<dd> When toggled to metric, display pressure in units of millimeters of Mercury.</p>
<dt><code>-p, &#8211;mps</code></p>
<dd> When toggled to metric, display wind speed in units of meters per second.</p>
<dt><code>&#8211;bc=</code><i>color</i></p>
<dd> When toggled to compatibility mode, set the background color (#8e8e69 is LCD-ish).</p>
<dt><code>&#8211;lc=</code><i>color</i></p>
<dd> When toggled to compatibility mode, set the color of the labels, e.g. &#8211;lc=red or &#8211;lc=salmon or &#8211;lc=#4523ff.</p>
<dt><code>&#8211;dc=</code><i>color</i></p>
<dd> When toggled to compatibility mode, set the color of the data entries.</p>
<dt><code>&#8211;wgc=</code><i>color</i></p>
<dd> When toggled to compatibility mode, set the gusty-wind/variable-direction color. The wind speed indicator will turn this color when the wind speed is gusty. The value shown in this case is the average speed. Similarly, the wind direction indicator with change to this color when the wind direction is variable. The value shown in this case is the average direction.</p>
<dt><code>&#8211;tc=</code><i>color</i></p>
<dd> When toggled to compatibility mode, set the color of the ICAO location indicator and update time header.</dl>
<h2>FILES</h2>
<dl>
<dt><code>/etc/wmweather.conf</code></p>
<dd> The system-wide configuration file. Specify one long option per line, e.g. <code>station=EDDC</code> or <code>metric</code>. Whitespace, empty lines, and lines beginning with a <code>#</code> will be ignored.</p>
<dt><code>~/.wmweather/config</code></p>
<dd> The user configuration file.</p>
<dt><code>~/.wmweather/????</code></p>
<dd> These files contain the latest downloaded weather records in decoded METAR format.</p>
<dt><code>~/.netrc</code></p>
<dd> These file contains authentication information and should be used in preference to <code>&#8211;proxy-user</code>.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>http_proxy</code></p>
<dd> The HTTP proxy to be used, see also <code>&#8211;proxy</code>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-netrc/">netrc</a></code>(5) </p>
<p> To find out more about NOAA&#8217;s National Weather Service, have a look at <i><a rel="nofollow" href="http://www.nws.noaa.gov/">http://www.nws.noaa.gov/</a></i>.</p>
<h2>BUGS</h2>
<p> Please report any bugs to &lt;martin [at] godisch.de&gt;. Debian users are encouraged to use the Debian Bug Tracking System at <i><a rel="nofollow" href="http://bugs.debian.org/wmweather">http://bugs.debian.org/wmweather</a></i>.</p>
<h2>AUTHORS</h2>
<dl>
<dt>Version 1:</p>
<dd> Michael G. Henderson &lt;mghenderson [at] lanl.gov&gt;</p>
<dt>Version 2:</p>
<dd> Martin A. Godisch &lt;martin [at] godisch.de&gt;</p>
<dt>Contributors:</p>
<dd> Athanasius, Pablo Castellazzi, Avtar Gill, Adam Lackorzynski, Jon Larabee, Jordi Mallach, Paul Martin, HIROSE Masaaki, Michael P&ouml;tters </p>
</dl>
<h2>Index</h2>
