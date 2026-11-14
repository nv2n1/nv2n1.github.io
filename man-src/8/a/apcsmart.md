---
title: "apcsmart(8)"
name: "apcsmart"
section: "8"
letter: "a"
url: "/docs/linux/man/8-apcsmart/"
description: "apcsmart – Driver for American Power Conversion Smart Protocol UPS equipment"
---

<p>apcsmart &#8211; Driver for American Power Conversion Smart Protocol UPS equipment</p>
<h2>Synopsis</h2>
<p><code>apcsmart</code> -h <code>apcsmart</code> -a &#8216;UPS_NAME&#8217; [-x option=value &#8230;]</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 This man page only documents the hardware-specific features of the apcsmart driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8). </p>
<h2>Supported Hardware</h2>
<p>The apcsmart driver should recognize (or at the very least work with) majority of Smart-UPS models &#8211; which includes Smart-UPS, Matrix-UPS and Back-UPS lineups, among few other ones. </p>
<p> Currently we can roughly divide APC hardware into 3 groups (note that the division isn&#8217;t strict by any means, and the borders between those are pretty fuzzy): </p>
<p> [very] &quot;old&quot; models</p>
<dl>
<dd>These models usually have old APC logo, white color and <i>no</i> programmable eeprom; You won&#8217;t find them listed anywhere on APC&#8217;s site either. The support for those will be usually based on driver&#8217;s compatibility tables, or if the model (firmware) is not listed in those &#8211; the driver will try to follow the very basic subset of features, while still trying to remain useful. Despite &quot;smart&quot; tagname, they often tend to behave in pretty dumb way (see the section below about shutdown behaviour). </p>
<p> <code>Example models:</code> </p>
<dl>
<dd>&bull; Smart-UPS 2000I</dl>
<dl>
<dd>&bull; Smart-UPS 900I</dl>
</dl>
<p> &quot;new&quot; models</p>
<dl>
<dd>These models usually come from late 1990s / pre-2009 times. They are often referred as &quot;3rd. gen&quot;. For the most part, they have programmable eeprom, report supported commands and capabilites, and should work just fine with the apcsmart driver.</dl>
<p> &quot;microlink&quot; models</p>
<dl>
<dd>WARNING: these are not <i>natively</i> supported by apcsmart (or apcupsd for that matter, if you&#8217;re wondering). Around 2007 APC (now APC Schneider) decided to go back to its proprietry roots and all the new models (SMT, SMX, SURTD) use completely different protocol and cables. If you purchased a new APC UPS, that uses cable with rj45 on the one end, and db-9 on the other &#8211; then you have such model. Your only option to support it through <code>NUT</code> is to purchase &quot;legacy communications card&quot; &#8211; part #AP9620 (google &#8216;AP9620&#8217; for more details). Or if that&#8217;s not an option, rely on official software.</dl>
<p> Another thing to remember is that Smart protocol is not USB protocol. If you have UPS with both USB and serial ports, then depending on how you connect it, you will need either apcsmart or usbhid-ups driver.</p>
<h2>Cabling</h2>
<p>This driver expects to see a 940-0024C cable or a clone by default. You can switch to the 940-0095B dual-mode cable support with the &#8216;cable=&#8217; definition described below. </p>
<p> If your 940-xx24X cable is broken or missing, use this diagram to build a clone: </p>
<p> <a rel="nofollow" href="http://www.networkupstools.org/cables.html#_940_0024c_clone">http://www.networkupstools.org/cables.html#_940_0024c_clone</a> </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> The &quot;xx&quot; is either &quot;00&quot; for a short cable, or the number of feet of a longer cable. The &quot;X&quot; is a letter representing the minor revision of the physical cable and its connectors (&quot;C&quot; and &quot;E&quot; are commonly found revisions). All minor revisions should use the same pin-outs and wiring. </p>
</dl>
<p> You can specify alternate cable in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> <code>cable</code>=940-0095B </p>
<p> Alternatively, you can also provide it on the command line using: </p>
<p> -x <code>cable</code>=940-0095B</p>
<h2>Tty Modes</h2>
<p>By default the driver works in canonical mode, but it showed to be a problem in windows systems. Furthermore there&#8217;s a possibility of some obscure serial cards or serial-usb convertes that could cause problems as well. You can use &#8216;ttymode=&#8217; option to force non-canonical discipline in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> <code>ttymode</code>=raw </p>
<p> Alternatively, you can also provide it on the command line using: </p>
<p> -x <code>ttymode</code>=raw </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Any other value will make the driver work in the canonical mode. </p>
</dl>
<h2>Explanation Of Shutdown Methods Supported By Apc Upses</h2>
<p>APC hardware supports a lot of shutdown methods, that themselves can differ in behaviour quite a bit, depending on the model. </p>
<p> <code>S</code> (soft hibernate)</p>
<dl>
<dd>This is most basic command present in probably all APC models. It will hibernate the UPS, and subsequently wake it up when the mains supply returns. <code>The command doesn&#8217;t work if UPS is running on mains.</code> </p>
<p> &quot;old&quot; models</p>
<dl>
<dd>The behaviour here is unfortunately pretty primitive &#8211; when the power returns, the UPS just wakes up. No grace periods, no min. battery charge condition, etc. This is probably not what you want.</dl>
<p> &quot;new&quot; models</p>
<dl>
<dd>The behaviour here is as expected &#8211; the power is cut off after the eeprom defined grace period. The UPS will wake up when the power returns, after the eeprom defined delay AND if the eeprom defined min. battery charge level is met. The delay is counted from the power&#8217;s return.</dl>
</dl>
<p> <code>CS</code> (aka &quot;force OB hack&quot;)</p>
<dl>
<dd>This is a trick to make UPS power down even if it&#8217;s running on mains. Immediately before issuing <code>S</code>, &quot;simulate power failure&quot; is issued. The remaining behaviour is as in <code>S</code> case. </p>
<p> The name came from APC CS models, where such trick was used to power down UPSes in consistent fashion using only <code>S</code>. It&#8217;s better to use <code>@nnn</code> command if your UPS supports it (and is not too old, see below).</dl>
<p> <code>@nnn</code> (hard hibernate)</p>
<dl>
<dd>This is basic command used to hibernate UPS regardless if it&#8217;s running on batteries or on mains. The option takes 3 digits argument which can be used to specify additional wakeup delay (in 6 minute units). </p>
<p> &quot;old&quot; models</p>
<dl>
<dd>The behaviour is &#8211; unfortunately &#8211; similary primitive to <code>S</code>. The UPS unconditionally wakes up after nnn*6 minutes &#8211; <code>it doesn&#8217;t care if the power returned !</code> If nnn = 000, then UPS will do precisely nothing. On those models you&#8217;re better specifying nnn &gt; 0, if you can estimate the kind of power problems that might be happening in your environment. Another thing to consider with &quot;old&quot; models &#8211; you might lose the connection with the UPS, until it wakes up (with <code>S</code>, the serial connection is kept alive).</dl>
<p> &quot;new&quot; models</p>
<dl>
<dd>All the usual variables defined in eeprom are respected (see <code>S</code>). Additionally, if nnn &gt; 0, the nnn*6 minutes are added to eeprom defined delay. UPS will not power up if it&#8217;s running on batteries, contrary to what &quot;old&quot; models used to do &#8211; the combined delay is counted from the moment of power return.</dl>
<p> Supposedly there exist models that take 2 digits instead of 3. Just in case, NUT also supports such variation. You have to provide exactly 2 digits to trigger it (<code>awd</code> option, or argument to one of the supported instant commands).</dl>
<p> <code>K</code> (delayed poweroff)</p>
<dl>
<dd>This is permanent poweroff &#8211; the UPS will not wake up automatically. On newer units, it will respect applicable eeprom variables.</dl>
<p> <code>Z</code> (instant poweroff)</p>
<dl>
<dd>This is also permanent poweroff &#8211; the UPS will not wake up automatically. The poweroff is executed immediately.</dl>
<h2>Shutdown Control By Nut</h2>
<p>There are three options used to control the shutdown behaviour. </p>
<p> <code>sdtype</code>=[0-5]</p>
<dl>
<dd>This option takes a single digit (0-5) as an argument. See below for details.</dl>
<p> <code>advorder</code>=no|[0-4]+</p>
<dl>
<dd>This option takes string of digits as an argument. Methods listed are tried in turn until one of them succeedes. Note that the meaning of digits is different from <code>sdtype</code>. See below for details.</dl>
<p> <code>awd</code>=[0-9]{1,3}</p>
<dl>
<dd>This option lets you specify additional wakeup delay used by <code>@</code>. If you provide exactly 2 digits, the driver will try 2 digits variation (see previous section for more info). Otherwise standard 3 digits variation is used. <code>Note: the time unit is 6 minutes !</code></dl>
<p> Keep in mind that <code>sdtype</code> and <code>advorder</code> are mutually exclusive. If <code>advorder</code> is provided, <code>sdtype</code> is ignored. If <code>advorder</code> is set to &#8216;no&#8217;, <code>sdtype</code> is used instead. </p>
<p> If nothing is provided, <code>NUT</code> will assume <code>sdtype</code>=0 &#8211; which is generally fine for anything not too ancient or not too quirky.</p>
<h3>Sdtype</h3>
<p>The values permitted are from 0 to 5. Only one can be specified. Anything else will cause apcsmart to exit. </p>
<p> 0</p>
<dl>
<dd>issue soft hibernate (<code>S</code>) if the UPS is running on batteries, otherwise issue hard hibernate (<code>@</code>)</dl>
<p> 1</p>
<dl>
<dd>issue soft hibernate (<code>S</code>) (if on batteries), and if it fails (or on mains) &#8211; try hard hibernate (<code>@</code>)</dl>
<p> 2</p>
<dl>
<dd>issue instant poweroff (<code>Z</code>)</dl>
<p> 3</p>
<dl>
<dd>issue delayed poweroff (<code>K</code>)</dl>
<p> 4</p>
<dl>
<dd>issue &quot;force OB hack&quot; (<code>CS</code>)</dl>
<p> 5</p>
<dl>
<dd>issue hard hibernate (<code>@</code>)</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Hard hibernate&#8217;s additional wakeup delay can be provided by <code>awd</code>. </p>
</dl>
<h3>Advorder</h3>
<p>The argument is either a word &#8216;no&#8217;, or a string of 1 &#8211; 5 digits in [0 &#8211; 4] range. Each digit maps to the one of shutdown methods supported by APC UPSes. Methods listed in this way are tried in order, until one of them succedes. </p>
<p> If <code>advorder</code> is undefined or set to &#8216;no&#8217;, <code>sdtype</code> is used instead. </p>
<p> The mapping is as follows: </p>
<table>
<tr VALIGN=top>
<td>
<p> 0 </td>
<td>
<p> soft hibernate (<code>S</code>)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 1 </td>
<td>
<p> hard hibernate (<code>@</code>)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 2 </td>
<td>
<p> delayed poweroff (<code>K</code>)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 3 </td>
<td>
<p> instant poweroff (<code>Z</code>)
</td>
</tr>
<tr VALIGN=top>
<td>
<p> 4 </td>
<td>
<p> &quot;force OB hack&quot; (<code>CS</code>)
</td>
</tr>
</table>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> Hard hibernate&#8217;s additional wakeup delay can be provided by <code>awd</code>. </p>
</dl>
<h2>Ignoring Lb State</h2>
<p>APC units &#8211; even if they report LB mode &#8211; will not go into shutdown automatically. This gives us even more control with reference to &quot;when to actually shutdown psu&quot;. Since version 2.6.2, NUT supports <code>ignorelb</code> option in driver&#8217;s section of <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5). When such option is in effect, the core driver will ignore LB state as reported by specific driver and start shutdown basing the decision <i>only</i> on two conditions: </p>
<p> battery.charge &lt; battery.charge.low </p>
<p> <code>OR</code> </p>
<p> battery.runtime &lt; battery.runtime.low </p>
<p> Of course &#8211; if any of the variables are not available, the appropriate condition is not checked. If you want to explicitly disable one of the conditions, simply override the right hand variable causing the condition to always evaluate to false (you can even provide negative numbers). </p>
<p> APC UPSes don&#8217;t have battery.charge.low &#8211; you will have to define it if you want to use such condition (prefix the variable with override. or default.). </p>
<p> &quot;New&quot; units have battery.runtime.low, but depending on battery quality, firmware version, calibration and UPS load &#8211; this variable can be underestimated quite a bit &#8211; especially right after going into OB state. This in turn can cause LB to be asserted, which under normal conditions will cause <code>NUT</code> to initiate the shutdown. You might want to disable this condition entirely, when relying on <code>ignorelb</code> option (this was actually the main motivation behind introduction of such feature). </p>
<p> Simple example: </p>
<dl>
<dd>
<pre>[apc]
 ignorelb
 override.battery.charge.low = 15
 override.battery.runtime.low = -1</pre>
</dl>
<p> This would cause apcsmart to go into shutdown <i>only</i> if detected battery charge &lt; 15%. Runtime condition is always false in this example. </p>
<p> You could ask &#8211; why bother ? Well, the reason is already hinted above. APC units can be very picky about the batteries, and their firmware can underestimate the remaining runtime (especially right after going into OB state). <code>ignorelb</code> option and <code>override.*</code> let you remain in control of the UPS, not UPS in control of you. </p>
<p> Furthermore, this allows to specify conditions similary to how it&#8217;s done in apcupsd daemon, so it should be welcome by people used to that software.</p>
<h2>Supported Instant Commands</h2>
<p>The apcsmart driver exposes following instant commands: </p>
<p> shutdown.return</p>
<dl>
<dd>executes soft hibernate</dl>
<p> shutdown.return cs</p>
<dl>
<dd>executes &quot;force OB hack&quot;</dl>
<p> shutdown.return at:&lt;nbr&gt;</p>
<dl>
<dd>executes &quot;hard hibernate&quot; with &lt;nbr&gt;*6 minutes additional wakeup delay (&lt;nbr&gt; format is the same as of <code>awd</code> option)</dl>
<p> shutdown.stayoff</p>
<dl>
<dd>executes &quot;delayed poweroff&quot;</dl>
<p> load.off</p>
<dl>
<dd>executes &quot;instant poweroff&quot;</dl>
<p> All the above commands must be issued 2nd time to have any effect (no less than 3 seconds, and no more than 15 seconds after the initial call). Those commands are mostly useful for manual testing, when your machine is not powered by the UPS you&#8217;re testing. </p>
<p> Other supported commands: </p>
<dl>
<dd>&bull; load.on</dl>
<dl>
<dd>&bull; test.panel.start</dl>
<dl>
<dd>&bull; test.failure.start</dl>
<dl>
<dd>&bull; test.battery.start</dl>
<dl>
<dd>&bull; test.battery.stop</dl>
<dl>
<dd>&bull; bypass.start</dl>
<dl>
<dd>&bull; bypass.stop</dl>
<dl>
<dd>&bull; calibrate.start</dl>
<dl>
<dd>&bull; calibrate.stop</dl>
<h2>Previous Driver Version</h2>
<p>Previous driver is still available as apcsmart-old &#8211; should there be any need to use earlier version (bugs, incompatiblities with new functionality, etc.). In due time apcsmart-old will be phased out completely, but this won&#8217;t happen until the new version gets solid exposure with no pending issues.</p>
<h2>Bugs</h2>
<p>Some older APC UPS models return bogus data in the status register during a front panel test. This is usually detected and discarded, but some other unexpected values have occasionally slipped through. </p>
<p> APC UPS models with both USB and serial ports require a power cycle when switching from USB communication to serial, and perhaps vice versa.</p>
<h2>Author</h2>
<p>Nigel Metheringham &lt;Nigel.Metheringham [at] Intechnology.co.uk&gt; (drawing heavily on the original apcsmart driver by Russell Kroll). This driver was called newapc for a time and was renamed in the 1.5 series. In 2.6.2 it was renamed to apcsmart-old, being superseded by updated version with new features, which is maintained by Michal Soltys &lt;soltys [at] ziu.info&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8), <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
