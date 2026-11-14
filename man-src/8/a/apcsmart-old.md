---
title: "apcsmart-old(8)"
name: "apcsmart-old"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apcsmart-old/"
description: "apcsmart-old – Driver for American Power Conversion Smart Protocol UPS equipment"
---

<p>apcsmart-old &#8211; Driver for American Power Conversion Smart Protocol UPS equipment</p>
<h2>Synopsis</h2>
<p><code>apcsmart-old</code> -h <code>apcsmart-old</code> -a <i>UPS_NAME</i> [<i>OPTIONS</i>]</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 This man page only documents the hardware-specific features of the apcsmart-old driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8). </p>
<h2>Supported Hardware</h2>
<p>apcsmart-old should recognize all recent APC models that use a serial protocol at 2400 bps. This is primarily the Smart-UPS, Matrix-UPS and Back-UPS Pro lines. </p>
<p> The driver attempts to support every bell and whistle of the APC reporting interface, whether or not this is strictly sensible. </p>
<p> Some older hardware may only report a handful of variables. This is usually not a bug&#8212;they just don&#8217;t support anything else.</p>
<h2>Cabling</h2>
<p>This driver expects to see a 940-0024C cable or a clone by default. You can switch to the 940-0095B dual-mode cable support with the cable= definition described below. </p>
<p> If your 940-0024C cable is broken or missing, use this diagram to build a clone: </p>
<p> <a rel="nofollow" href="http://www.networkupstools.org/cables/940-0024C.jpg">http://www.networkupstools.org/cables/940-0024C.jpg</a></p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> <code>cable=940-0095B</code></p>
<dl>
<dd>Configure the serial port for the APC 940-0095B dual-mode cable.</dl>
<p> <code>sdtype=</code><i>num</i></p>
<dl>
<dd>Use shutdown type <i>num</i>, according to this table: </p>
<p> 0</p>
<dl>
<dd>soft shutdown or powerdown, depending on battery status</dl>
<p> 1</p>
<dl>
<dd>soft shutdown followed by powerdown</dl>
<p> 2</p>
<dl>
<dd>instant power off</dl>
<p> 3</p>
<dl>
<dd>power off with grace period</dl>
<p> 4</p>
<dl>
<dd>&quot;force OB&quot; hack method for CS 350</dl>
</dl>
<p> Modes 0 and 1 will power up the load when power returns. Modes 2 and 3 will keep the load turned off when the power returns. </p>
<p> Mode 4 exploits an oddity in the CS 350 models since they only seem to support the S command, but then only when running on battery. As a result, the driver will force the UPS to go on battery if necessary before sending the shutdown command. This ensures that the load gets reset.</p>
<h2>Bugs</h2>
<p>Some older APC UPS models return bogus data in the status register during a front panel test. This is usually detected and discarded, but some other unexpected values have occasionally slipped through. </p>
<p> APC UPS models with both USB and serial ports require a power cycle when switching from USB communication to serial, and perhaps vice versa.</p>
<h2>Author</h2>
<p>Nigel Metheringham &lt;Nigel.Metheringham [at] Intechnology.co.uk&gt; (drawing heavily on the original apcsmart driver by Russell Kroll). This driver was called newapc for a time and was renamed in the 1.5 series. In 2.6.2 the driver was renamed to apcsmart-old, being superseded by updated version with new features.</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
