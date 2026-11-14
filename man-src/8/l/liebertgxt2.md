---
title: "liebertgxt2(8)"
name: "liebertgxt2"
section: "8"
letter: "l"
url: "/docs/linux/man/8-liebertgxt2/"
description: "liebertgxt2 – Driver for Liebert GXT2 UPS, using the ESP2 serial protocol"
---

<p>liebertgxt2 &#8211; Driver for Liebert GXT2 UPS, using the ESP2 serial protocol</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the liebertgxt2 driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>liebertgxt2 is experimental and will recognize only those models known to work. The driver will report the model it finds and abort if it is unknown. modelname= in ups.conf can be used to force the driver to accept the model as supported. </p>
<p> The driver is incomplete but supports the numerious information fields and fields necessary to make the driver useful. Potentially useful features that aren&#8217;t supported are shutdown and battery test &#8211; or any command that instructs the UPS to take some action.</p>
<h2>Cabling</h2>
<p>This driver expects to see 2400 baud serial data at the TX/RX pins. This driver was tested with an original cable.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<dl>
<dt>modelname=<i>model</i></p>
<dd>Force the model name of <i>model</i> to be a supported model, giving you the chance to try this driver with your Liebert UPS. </p>
</dl>
<h2>Bugs</h2>
<p>Action commands are not supported, that includes battery test and shutdown. </p>
<h2>Author</h2>
<p>Richard Gregory &lt;r.gregory liv ac uk&gt;. With additional information from Spiros Ioannou.</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> Partial description of the ESP2 protocol: <a rel="nofollow" href="http://www.csc.liv.ac.uk/~greg/projects/liebertserial/">http://www.csc.liv.ac.uk/~greg/projects/liebertserial/</a> </p>
