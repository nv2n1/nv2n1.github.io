---
title: "mheard(1)"
name: "mheard"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mheard/"
description: "mheard – display AX.25 calls recently heard."
---

<h2>NAME</h2>
<p> mheard &#8211; display AX.25 calls recently heard.</p>
<h2>SYNOPSIS</h2>
<p> <code>mheard [-d cmns] [-n] [-o cfpt] [-v] [port&#8230;]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Mheard</code> displays information about most recently heard AX.25 callsigns, the interface upon which they were heard, the total packets heard, the time at which the last one was heard and other information. <code>Mheard</code> displays different information, in different orders depending on the settings of the arguments. Information on specific ports can be displayed by giving the port names as arguments.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d cmns</code></p>
<dd> Sets the information that is displayed for each AX.25 callsign heard. The different arguments are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>c</code></p>
<dd> Display all the information with regard to callsigns, from-callsign, to-callsign, port name, and any digipeaters that may be in use.</p>
<dt><code>m</code></p>
<dd> Display miscellaneous information, the from-callsign, port name, no frames heard, the last type of frames heard, and which different PIDs have been heard from that station.</p>
<dt><code>n</code></p>
<dd> Display the default information. This is the from-callsign, port name, no frames heard and the date and time last heard.</p>
<dt><code>s</code></p>
<dd> Displays statistics about the station heard, the from-callsign, port name, no I frames, no S frames, no U frames, time first heard, and time last heard.</dl>
</dl>
<dt><code>-n</code></p>
<dd> Supress the displaying of titles.</p>
<dt><code>-o cfpt</code></p>
<dd> Sets the ordering of the information displayed. The meanings of the different arguments are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>c</code></p>
<dd> Sort list by from-callsign.</p>
<dt><code>f</code></p>
<dd> Sort list by number of frames heard.</p>
<dt><code>p</code></p>
<dd> Sort list by port name.</p>
<dt><code>t</code></p>
<dd> Sort list by the time last heard, this is the default.</dl>
</dl>
<dt><code>-v</code></p>
<dd> Display the version.</dl>
<h2>FILES</h2>
<p> /var/ax25/mheard/mheard.dat<br />
 /etc/ax25/axports</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4), <code><a href="/docs/linux/man/8-mheardd/">mheardd</a></code>(8).</p>
<h2>AUTHOR</h2>
<p> Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt; </p>
<h2>Index</h2>
