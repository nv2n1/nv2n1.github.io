---
title: "bestups(8)"
name: "bestups"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bestups/"
description: "bestups – Driver for Best Power / SOLA (Phoenixtec protocol) UPS equipment"
---

<p>bestups &#8211; Driver for Best Power / SOLA (Phoenixtec protocol) UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the bestups driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p><code>bestups</code> was designed to monitor Best Power UPS hardware like the Fortress, Fortress Telecom, Axxium Rackmount and Patriot Pro. It also recognizes and supports SOLA units such as the 325, 520 and 620. In addition, the Best 610 is supported using the &#8216;ID&#8217; option. </p>
<p> Other UPS hardware using the Phoenixtec protocol should also work, but they will generate a warning since their battery information is not known. </p>
<p> This driver does not support some older Best/SOLA units.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> <code>nombattvolt=</code><i>num</i></p>
<dl>
<dd>Override the battery float voltage which is normally determined by asking the hardware. This is useful if your UPS constantly reports battery.charge values just below 100% even when it&#8217;s completely charged. </p>
<p> If you have this problem, set this to whatever battery.voltage reports when the UPS is known to be completely charged with a good battery. </p>
<p> The author&#8217;s Best Fortress 750 uses nombattvolt=27.4.</dl>
<p> <code>battvoltmult=</code><i>num</i></p>
<dl>
<dd>Multiply the reported battery voltage by this number. Some devices report only a fraction of the total battery voltage. </p>
<p> For example, the SOLA 610 700VA UPS (with a 24V battery) reports the single cell voltage (about 2.27V when fully charged). In this particular case you can set battvoltmult = 12 in <code><a href="/docs/linux/man/8-ups-conf/">ups.conf</a></code>(8) to fix this.</dl>
<p> <code>ID=</code><i>string</i></p>
<dl>
<dd>Set the Identification response string. This should only be used with hardware that supports the Phoenixtec protocol status inquiry commands, but not the &quot;ID&quot; command, such as the Best/SOLA 610. Format of the ID string is: AAA,BBBB,CCC,DDD,EE.E,FF.F </p>
<p> AAA is the three-character identification for the UPS model. </p>
<p> BBBB is the output power in VA (volt amperes). B is an integer number ranging from 0 to 9. </p>
<p> CCC is the Nominal Input Voltage. C is an integer number ranging from 0 to 9. The unit is Volts AC. </p>
<p> DDD is the Nominal Output Voltage. D is an integer number ranging from 0 to 9. The unit is Volts AC. </p>
<p> EE.E is the Battery Voltage that will cause the UPS to shut itself off. E is an integer number ranging from 0 to 9. Then unit is Volts DC and a decimal point is present. </p>
<p> FF.F or FFF.F is the Battery Voltage at full charge. F is an integer number ranging from 0 to 9. Then unit is Volts DC. Typically, for 700VA, 1KVA and 1.5KVA units, the format is FF.F. For 2KVA and 3KVA units, the format is FFF.F. </p>
<p> Example: a Best 610 1.5KVA unit would use the string &quot;610,1500,120,120,10.0,48.0&quot;.</dl>
<h2>Bugs</h2>
<p>The battery charge percentage value (in battery.charge) is derived from the voltage data that the UPS returns, since the UPS doesn&#8217;t return that value directly. On some hardware, the charge will remain at 100% for a long time and then drops quickly shortly before the battery runs out. You can confirm from the battery.voltage readings that this is a problem with the UPS and not this driver. </p>
<p> Similarly, the float from the charger in some models forces the battery charge percentage back up to 100% immedately after the UPS goes back on-line, so you can&#8217;t tell when it is really recharged. </p>
<p> Finally, some models give one value for the battery&#8217;s nominal voltage and yet actually have a nominal voltage slightly below that. This leads to things such as the perpetual 98.7% charge on the author&#8217;s Fortress 750, even when it&#8217;s been charging for weeks. You can use nombattvolt= in <code><a href="/docs/linux/man/8-ups-conf/">ups.conf</a></code>(8) to fix this.</p>
<h2>Author</h2>
<p>Russell Kroll, Jason White</p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
