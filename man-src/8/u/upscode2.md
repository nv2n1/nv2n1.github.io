---
title: "upscode2(8)"
name: "upscode2"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upscode2/"
description: "upscode2 – Driver for UPScode II compatible UPS equipment"
---

<p>upscode2 &#8211; Driver for UPScode II compatible UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the upscode2 driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver supports UPS equipment which can be controlled via the UPScode II protocol. This is mainly Fiskars, Powerware equipment, but also some (probably OEM&#8217;ed) products from Compaq.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> <code>manufacturer</code>=<i>value</i></p>
<dl>
<dd>Autodetection of this parameter is not possible yet (and it probably never will be). Therefore, this user-defined string accepts any name. The default is <i>unknown</i>.</dl>
<p> <code>input_timeout</code>=<i>value</i></p>
<dl>
<dd>The timeout waiting for a response from the UPS. Some UPS models have shown to be rather slow, resulting in frequent messages about empty responses from the UPS. If you see this, try increasing this value.</dl>
<p> <code>output_pace</code>=<i>value</i></p>
<dl>
<dd>Delay between characters sent to the UPS. This was added for completeness with the above parameter. It has not shown to be needed yet.</dl>
<p> <code>baudrate</code>=<i>value</i></p>
<dl>
<dd>The default baudrate is 1200, which is the standard for the UPScode II protocol.</dl>
<p> <code>full_update_timer</code>=<i>value</i></p>
<dl>
<dd>Number of seconds between collection of normative values.</dl>
<p> <code>use_crlf</code></p>
<dl>
<dd>Flag to set if commands towards to UPS need to be terminated with CR-LF, and not just CR.</dl>
<p> <code>use_pre_lf</code></p>
<dl>
<dd>Flag to set if commands towards to UPS need to be introduced with an LF. A Compaq T1500h is known to need this.</dl>
<h2>Commands</h2>
<p>The driver supports the following commands for those UPSen that support them. The available commands are autodetected during initialization, so you should check availability with <i>upscmd -l</i>. </p>
<dl>
<dd>&bull; test.panel.start &#8211; Start UPS self test</dl>
<dl>
<dd>&bull; test.battery.start &#8211; Start battery self test</dl>
<dl>
<dd>&bull; beeper.enable &#8211; Enable UPS beeper</dl>
<dl>
<dd>&bull; beeper.disable &#8211; Disable UPS beeper</dl>
<dl>
<dd>&bull; shutdown.return &#8211; Shut down in 1 second and wait for power to return</dl>
<dl>
<dd>&bull; shutdown.stayoff &#8211; Shut down in 1 seconds</dl>
<dl>
<dd>&bull; shutdown.reboot &#8211; Shut down in 1 seconds and reboot after 1 minute</dl>
<dl>
<dd>&bull; shutdown.reboot.graceful &#8211; Shut down in 20 seconds and reboot after 1 minute</dl>
<h2>Notes</h2>
<p>The Powerware UPS models that this driver has been tested against until now have not returned a value for <i>battery.charge</i>. Therefore, the driver will guestimate a value based on the nominal battery min/max and the current battery voltage.</p>
<h2>Author</h2>
<p>Håvard Lygre &lt;hklygre [at] online.no&gt;, Niels Baggesen &lt;niels [at] baggesen.net&gt;</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
