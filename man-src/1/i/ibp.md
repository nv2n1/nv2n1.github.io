---
title: "ibp(1)"
name: "ibp"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ibp/"
description: "ibp – show which of the International Beacon Project beacons is transmitting"
---

<h2>NAME</h2>
<p> ibp &#8211; show which of the International Beacon Project beacons is transmitting</p>
<h2>SYNOPSIS</h2>
<p> <code>ibp</code> <i>[arguments]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>IBP</code> shows which of the beacons of the International Beacon Project is transmitting now. </p>
<p> The following arguments can be used: </p>
<p> a <code>band</code> expressed either in MHz (14, 18, 21, 24 or 28) or in meters (20, 17, 15, 12 or 10); if no band is specified, the program starts in multi-band mode. </p>
<p> a <code>Maidenhead locator</code> (like JO32KF), to be used for the calculation of distance and azimuth (both short and long path) to each beacon. </p>
<dl>
<dt><code>-c</code>, <code>&#8211;nocolour</code></p>
<dd> don&#8217;t use colour, even on a colour terminal. </p>
<dt><code>-m</code>, <code>&#8211;morse</code></p>
<dd> display callsign of active beacon in morse code (not in multi-band mode). </p>
<dt><code>-x</code>, <code>&#8211;nograph</code></p>
<dd> don&#8217;t open the X11 window (showing a world map with the beacon locations, and short and long paths) even if the DISPLAY environment variable is set. This option is only available if X11 support has been compiled in.</dl>
<p> Note: since each beacon transmission lasts only 10 seconds, your computer&#8217;s clock should be set reasonably accurately for the results to be valid. </p>
<h2>THE INTERNATIONAL BEACON PROJECT</h2>
<p> The International Beacon Project is a set of 18 amateur (ham) radio transmitters around the world, each of which transmit every 3 minutes on a set of 5 short-wave frequencies. This allows short-wave radio users to quickly assess the current worldwide propagation conditions. Much more information can be found on <i><a rel="nofollow" href="http://www.ncdxf.org/beacons.html">http://www.ncdxf.org/beacons.html</a></i> </p>
<h2>AUTHOR</h2>
<p> Pieter-Tjerk de Boer &lt;pa3fwm [at] amsat.org&gt;; via amateur packet-radio: PA3FWM @ PI8DAZ.#TWE.NLD.EU. </p>
<p> The X11 display code is heavily based on the &#8216;sunclock&#8217; program by John Mackin &lt;john [at] cs.su.oz.AU&gt;. </p>
<h2>Index</h2>
