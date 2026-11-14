---
title: "genericups(8)"
name: "genericups"
section: "8"
letter: "g"
url: "/docs/linux/man/8-genericups/"
description: "genericups – Driver for contact-closure UPS equipment"
---

<p>genericups &#8211; Driver for contact-closure UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the specific features of the genericups driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h2>Supported Hardware</h2>
<p>This driver supports hardware from many different manufacturers as it only uses the very simplest of signaling schemes. Contact closure refers to a kind of interface where basic high/low signals are provided to indicate status. This kind of UPS can only report line power and battery status. </p>
<p> This means that you will only get the essentials in ups.status: OL, OB, and LB. Anything else requires a smarter UPS.</p>
<h2>Cabling</h2>
<p>Cabling is different for every kind of UPS. See the table below for information on what is known to work with a given UPS type.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5): </p>
<p> upstype=<i>type</i></p>
<dl>
<dd>Required. Configures the driver for a specific kind of UPS. See the UPS Types section below for more information on which entries are available.</dl>
<p> mfr=<i>string</i></p>
<dl>
<dd>Optional. The very nature of a generic UPS driver sometimes means that the stock manufacturer data has no relation to the actual hardware that is attached. With the mfr setting, you can change the value that is seen by clients that monitor this UPS.</dl>
<p> model=<i>string</i></p>
<dl>
<dd>Optional. This is like mfr above, but it overrides the model string instead.</dl>
<p> serial=<i>string</i></p>
<dl>
<dd>Optional. This is like mfr above and intended to record the identification string of the UPS. It is titled &quot;serial&quot; because usually this string is referred to as the serial number.</dl>
<p> sdtime=<i>value</i></p>
<dl>
<dd>Optional. The driver will sleep for this many seconds after setting the shutdown signal. This is necessary for some hardware which requires a sustained level to activate the shutdown sequence. </p>
<p> The default behavior of the driver is to exit immediately. If this doesn&#8217;t reliably trigger a shutdown in your UPS hardware, use this setting to give it more time to react.</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> very large values for sdtime may create warnings from upsdrvctl if it gets tired of waiting for the driver to return. </p>
</dl>
<h2>Custom Configurations</h2>
<p>You may override the values for CP, OL, LB, and SD by defining them in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5) after the upstype setting. </p>
<p> For example, to set the cable power to DTR and the low battery value to DCD, it would look like this: </p>
<dl>
<dd>
<pre>CP = DTR</pre>
</dl>
<dl>
<dd>
<pre>LB = DCD</pre>
</dl>
<p> Recognized values for input lines are CTS, DCD, and RNG. Recognized values for output lines are DTR, RTS, and ST. See below for more about what these signals mean. </p>
<p> These values may be negated for active low signals. That is, &quot;LB=-DCD&quot; recognizes a low battery condition when DCD is not held high.</p>
<h2>Type Information</h2>
<p>The essence of a UPS definition in this driver is how it uses the serial lines that are available. These are the abbreviations you will see below: </p>
<p> OL</p>
<dl>
<dd>On line (no power failure) (opposite of OB &#8211; on battery)</dl>
<p> LB</p>
<dl>
<dd>Low battery</dl>
<p> SD</p>
<dl>
<dd>Shutdown load</dl>
<p> CP</p>
<dl>
<dd>Cable power (must be present for cable to have valid reading)</dl>
<p> CTS</p>
<dl>
<dd>Clear to Send. Received from the UPS.</dl>
<p> RTS</p>
<dl>
<dd>Ready to Send. Sent by the PC.</dl>
<p> DCD</p>
<dl>
<dd>Data Carrier Detect. Received from the UPS.</dl>
<p> RNG</p>
<dl>
<dd>Ring indicate. Received from the UPS.</dl>
<p> DTR</p>
<dl>
<dd>Data Terminal Ready. Sent by the PC.</dl>
<p> ST</p>
<dl>
<dd>Send a BREAK on the transmit data line</dl>
<p> A &quot;-&quot; in front of a signal name (like -RNG) means that the indicated condition is signaled with an active low signal. For example, [LB=-RNG] means the battery is low when the ring indicate line goes low, and that the battery is OK when that line is held high.</p>
<h2>Ups Types</h2>
<p>0 = UPSonic LAN Saver 600 </p>
<dl>
<dd>
<pre>[CP=DTR+RTS] [OL=-CTS] [LB=DCD] [SD=DTR]</pre>
</dl>
<p> 1 = APC Back-UPS/Back-UPS Pro/Smart-UPS with 940-0095A/C cable </p>
<dl>
<dd>
<pre>[CP=DTR] [OL=-RNG] [LB=DCD] [SD=RTS]</pre>
</dl>
<p> 2 = APC Back-UPS/Back-UPS Pro/Smart-UPS with 940-0020B cable </p>
<dl>
<dd>
<pre>[CP=RTS] [OL=-CTS] [LB=DCD] [SD=DTR+RTS]</pre>
</dl>
<dl>
<dd>
<pre>Type 2 has also been reported to work with the 940-0020C cable.</pre>
</dl>
<p> 3 = PowerTech Comp1000 with DTR cable power </p>
<dl>
<dd>
<pre>[CP=DTR] [OL=CTS] [LB=DCD] [SD=DTR+RTS]</pre>
</dl>
<p> 4 = Generic RUPS Model </p>
<dl>
<dd>
<pre>[CP=RTS] [OL=CTS] [LB=-DCD] [SD=-RTS]</pre>
</dl>
<p> 5 = Tripp Lite UPS with Lan2.2 interface (black 73-0844 cable) </p>
<dl>
<dd>
<pre>[CP=DTR] [OL=CTS] [LB=-DCD] [SD=DTR+RTS]</pre>
</dl>
<p> 6 = Best Patriot with INT51 cable </p>
<dl>
<dd>
<pre>[CP=DTR] [OL=CTS] [LB=-DCD] [SD=RTS]</pre>
</dl>
<p> 7 = CyberPower Power99 Also Upsonic Power Guardian PG-500, Belkin Belkin Home Office, F6H350-SER, F6H500-SER, F6H650-SER, Eaton Management Card Contact &#8211; Config3 with cable 66033 (shutdown does not work) </p>
<dl>
<dd>
<pre>[CP=RTS] [OL=CTS] [LB=-DCD] [SD=DTR]</pre>
</dl>
<p> 8 = Nitram Elite 500 </p>
<dl>
<dd>
<pre>[CP=DTR] [OL=CTS] [LB=-DCD] [SD=???]</pre>
</dl>
<p> 9 = APC Back-UPS/Back-UPS Pro/Smart-UPS with 940-0023A cable </p>
<dl>
<dd>
<pre>[CP=none] [OL=-DCD] [LB=CTS] [SD=RTS]</pre>
</dl>
<p> 10 = Victron Lite with crack cable </p>
<dl>
<dd>
<pre>[CP=RTS] [OL=CTS] [LB=-DCD] [SD=DTR]</pre>
</dl>
<p> 11 = Powerware 3115 </p>
<dl>
<dd>
<pre>[CP=DTR] [OL=-CTS] [LB=-DCD] [SD=ST]</pre>
</dl>
<p> 12 = APC Back-UPS Office with 940-0119A cable </p>
<dl>
<dd>
<pre>[CP=RTS] [OL=-CTS] [LB=DCD] [SD=DTR]</pre>
</dl>
<p> 13 = RPT Repoteck RPT-800A/RPT-162A </p>
<dl>
<dd>
<pre>[CP=DTR+RTS] [OL=DCD] [LB=-CTS] [SD=ST]</pre>
</dl>
<p> 14 = Online P-series </p>
<dl>
<dd>
<pre>[CP=DTR] [OL=DCD] [LB=-CTS] [SD=RTS]</pre>
</dl>
<p> 15 = Powerware 5119, 5125 </p>
<dl>
<dd>
<pre>[CP=DTR] [OL=CTS] [LB=-DCD] [SD=ST]</pre>
</dl>
<p> 16 = Nitram Elite 2002 </p>
<dl>
<dd>
<pre>[CP=DTR+RTS] [OL=CTS] [LB=-DCD] [SD=???]</pre>
</dl>
<p> 17 = PowerKinetics 9001 </p>
<dl>
<dd>
<pre>[CP=DTR] [OL=CTS] [LB=-DCD] [SD=???]</pre>
</dl>
<p> 18 = TrippLite Omni 450LAN with Martin&#8217;s cabling </p>
<dl>
<dd>
<pre>[CP=DTR] [OL=CTS] [LB=DCD] [SD=none]</pre>
</dl>
<p> 19 = Fideltronic Ares Series </p>
<dl>
<dd>
<pre>[CP=DTR] [OL=CTS] [LB=-DCD] [SD=RTS]</pre>
</dl>
<p> 20 = Powerware 5119 RM </p>
<dl>
<dd>
<pre>[CP=DTR] [OL=-CTS] [LB=DCD] [SD=ST]</pre>
</dl>
<dl>
<dd>
<pre>Check docs/cables/powerware.txt</pre>
</dl>
<p> 21 = Generic RUPS 2000 (Megatec M2501 cable) </p>
<dl>
<dd>
<pre>[CP=RTS] [OL=CTS] [LB=-DCD] [SD=RTS+DTR]</pre>
</dl>
<p> 22 = Gamatronic All models with alarm interface (also CyberPower SL series) </p>
<dl>
<dd>
<pre>[CP=RTS] [OL=CTS] [LB=-DCD] [SD=DTR]</pre>
</dl>
<h2>Similar Models</h2>
<p>Many different UPS companies make models with similar interfaces. The RUPS cable seems to be especially popular in the &quot;power strip&quot; variety of UPS found in office supply stores. If your UPS works with an entry in the table above, but the model or manufacturer information don&#8217;t match, don&#8217;t despair. You can fix that easily by using the mfr and model variables documented above in your <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5).</p>
<h2>Testing Compatibility</h2>
<p>If your UPS isn&#8217;t listed above, you can try going through the list until you find one that works. There is a lot of cable and interface reuse in the UPS world, and you may find a match. </p>
<p> To do this, first make sure nothing important is plugged into the outlets on the UPS, as you may inadvertently switch it off. Definitely make sure that the computer you&#8217;re using is not plugged into that UPS. Plug in something small like a lamp so you know when power is being supplied to the outlets. </p>
<p> Now, you can either attempt to make an educated guess based on the documentation your manufacturer has provided (if any), or just start going down the list.</p>
<h3>Step 1</h3>
<p>Pick a driver to try from the list (genericups -h) and go to step 2.</p>
<h3>Step 2</h3>
<p>Start the driver with the type you want to try &#8211; </p>
<dl>
<dd>
<pre>genericups -x upstype=n /dev/port</pre>
</dl>
<p> Let upsd sync up (watch the syslog), and then run upsc to see what it found. If the STATUS is right (should be OL for on line), continue to Step 3, otherwise go back to step 1. </p>
<p> Alternatively, you can run genericups in debug mode &#8211; </p>
<dl>
<dd>
<pre>genericups -DDDDD -x upstype=n /dev/port</pre>
</dl>
<p> In this mode it will be running in the foreground and continuously display the line and battery status of the UPS.</p>
<h3>Step 3</h3>
<p>Disconnect the UPS from the wall/mains power. This is easiest if you have a switched outlet in between it and the wall, but you can also just pull the plug to test. The lamp should stay lit, and the status should switch to &quot;OB&quot;. If the lamp went out or the status didn&#8217;t go to &quot;OB&quot; within about 15 seconds, go to Step 1. Otherwise, continue to Step 4.</p>
<h3>Step 4</h3>
<p>At this point, we know that OL and OB work. If nothing else beyond this point works, you at least know what your OL/OB value should be. </p>
<p> Wait for the UPS to start complaining about a low battery. Depending on the size of your UPS battery and the lamp&#8217;s bulb, this could take awhile. It should start complaining audibly at some point. When this happens, STATUS should show &quot;OB LB&quot; within 15 seconds. If not, go to Step 1, otherwise continue to Step 5.</p>
<h3>Step 5</h3>
<p>So far: OL works, OB works, and LB works. </p>
<p> With the UPS running on battery, run the genericups driver with the -k switch to shut it down. </p>
<dl>
<dd>
<pre>genericups -x upstype=n -k /dev/port</pre>
</dl>
<p> If the UPS turns off the lamp, you&#8217;re done. At this point, you have verified that the shutdown sequence actually does what you want. You can start using the genericups driver with this type number for normal operations. </p>
<p> You should use your findings to add a section to your ups.conf. Here is a quick example: </p>
<dl>
<dd>
<pre>[myups]
 driver = genericups
 port = /dev/ttyS0
 upstype = 1</pre>
</dl>
<p> Change the port and upstype values to match your system.</p>
<h2>New Support</h2>
<p>If the above testing sequence fails, you will probably need to create a new entry to support your hardware. All UPS types are determined from the table in the genericups.h file in the source tree. </p>
<p> On a standard 9 pin serial port, there are 6 lines that are used as the standard &quot;high/low&quot; signal levels. 4 of them are incoming (to the PC, from the UPS), and the other 2 are outgoing (to the UPS, from the PC). The other 3 are the receive/transmit lines and the ground. </p>
<p> Be aware that many manufacturers remap pins within the cable. If you have any doubts, a quick check with a multimeter should confirm whether the cable is straight-through or not. Another thing to keep in mind is that some cables have electronics in them to do special things. Some have resistors and transistors on board to change behavior depending on what&#8217;s being supplied by the PC.</p>
<h2>Specific Model Notes</h2>
<p>These have been contributed by users of this driver. </p>
<p> The Centralion CL series may power down the load if the driver starts up with the UPS running on battery as the default line settings contain the shutdown sequence. &#8211; Neil Muller </p>
<p> The Tripp-Lite Internet Office 700 must be used with the black 73-0844 cable instead of the gray 73-0743 cable. This entry should work with any of their models with the Lan 2.2 interface &#8211; see the sticker by the DB9 connector on the UPS. &#8211; Stephen Brown </p>
<p> Type 5 should work with the Tripp-Lite Lan 2.1 interface and the 73-0724 cable. This was tested with the OmniSmart 675 PNP on Red Hat 7.2. &#8211; Q Giese </p>
<p> Types 7 and 10 should both work with the PhoenixTec A1000.</p>
<h2>Bugs</h2>
<p>There is no way to reliably detect a contact-closure UPS. This means the driver will start up happily even if no UPS is detected. It also means that if the connection between the UPS and computer is interrupted, you may not be able to sense this in software. </p>
<p> Most contact-closure UPSes will not power down the load if the line power is present. This can create a race when using slave <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) systems. See the <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) man page for more information. </p>
<p> The solution to both of these problems is to upgrade to a smart protocol UPS of some kind that allows detection and proper load cycling on command.</p>
<h2>See Also</h2>
<h3>The core driver</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
