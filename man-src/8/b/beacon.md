---
title: "beacon(8)"
name: "beacon"
section: "8"
letter: "b"
url: "/docs/linux/man/8-beacon/"
description: "beacon – transmit periodic messages on an AX.25 port."
---

<p>beacon &#8211; transmit periodic messages on an AX.25 port.</p>
<h2>Synopsis</h2>
<p><code>beacon [-c &lt;src_call&gt;] [-d &lt;dest_call&gt;[digi ..]] [-l] [-m] [-s] [-t interval] [-v] port lqmessagerq</code></p>
<h2>Description</h2>
<p><code>Beacon</code> transmits the message text on an AX.25 port every thirty minutes. The message is addressed to lqIDENTrq and is sent using the AX.25 callsign of the port specified on the command line. Typically the message text will contain spaces and/or other characters, therefore the message text should be enclosed in quotes to ensure they are passed to the <code>beacon</code> program untranslated.</p>
<h2>Options</h2>
<dl>
<dt><code>-c</code></dt>
<dd>Configure the source callsign for beacons. The default is to use the interface callsign.</dd>
<dt><code>-d</code></dt>
<dd>Configure the destination callsign for beacons. The default is lqIDENTrq. Optional: Digipeaters may follow, separated with spaces. Use -d &quot;DEST DIGI1 DIGI2 ..&quot;</dd>
<dt><code>-l</code></dt>
<dd>Enables the logging of errors to the system log, the default is off.</dd>
<dt><code>-m</code></dt>
<dd>Changes the destination address to lqMAILrq and sends the message text once only. This option overrides any destination callsign given with the -d option.</dd>
<dt><code>-s</code></dt>
<dd>Sends the message text once only.</dd>
<dt><code>-t interval</code></dt>
<dd>The time interval between messages, the interval is given in minutes and the default is thirty minutes.</dd>
<dt><code>-v</code></dt>
<dd>Display the version.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4), <code><a href="/docs/linux/man/5-axports/">axports</a></code>(5).</p>
<h2>Authors</h2>
<pre>Alan Cox GW4PTS &lt;alan [at] cymru.net&gt;
<br>
Jonathan Naylor G4KLX &lt;g4klx [at] g4klx.demon.co.uk&gt;
<br>
David Brooke G6GZH &lt;db [at] fusk.demon.co.uk&gt;</pre>
