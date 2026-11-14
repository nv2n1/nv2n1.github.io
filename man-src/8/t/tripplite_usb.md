---
title: "tripplite_usb(8)"
name: "tripplite_usb"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tripplite_usb/"
description: "tripplite_usb – Driver for older Tripp Lite USB UPSes (not PDC HID)"
---

<p>tripplite_usb &#8211; Driver for older Tripp Lite USB UPSes (not PDC HID)</p>
<h2>Synopsis</h2>
<p><code>tripplite_usb</code> -h </p>
<p> <code>tripplite_usb</code> -a <i>UPS_NAME</i> [<i>OPTIONS</i>]</p>
<h2>Supported Hardware</h2>
<p>This driver should work with older Tripp Lite UPSes which are detected as USB HID-class devices, but are not true HID Power-Device Class devices. So far, the devices supported by tripplite_usb have product ID 0001, and the newer units (such as those with &quot;LCD&quot; in the model name) with product ID 2001 require the <code><a href="/docs/linux/man/8-usbhid-ups/">usbhid-ups</a></code>(8) driver instead. Please report success or failure to the nut-upsuser mailing list. A key piece of information is the protocol number, returned in ups.debug.0. Also, be sure to turn on debugging (<i>-DDD</i>) for more informative log messages. If your Tripp Lite UPS uses a serial port, you may wish to investigate the <code><a href="/docs/linux/man/8-tripplite/">tripplite</a></code>(8) or <code><a href="/docs/linux/man/8-tripplite_su/">tripplite_su</a></code>(8) driver. </p>
<p> This driver has been tested with the following models: </p>
<dl>
<dd>&bull; INTERNETOFFICE700</dl>
<dl>
<dd>&bull; OMNIVS1000</dl>
<dl>
<dd>&bull; OMNIVS1500XL (some warnings)</dl>
<dl>
<dd>&bull; SMART700USB</dl>
<dl>
<dd>&bull; SMART1500RM2U</dl>
<dl>
<dd>&bull; SMART2200RMXL2U</dl>
<dl>
<dd>&bull; SMART3000RM2U</dl>
<p> If you have used Tripp Lite&#8217;s PowerAlert software to connect to your UPS, there is a good chance that <i>tripplite_usb</i> will work if it uses one of the following protocols: </p>
<dl>
<dd>&bull; Protocol 0004</dl>
<dl>
<dd>&bull; Protocol 1001</dl>
<dl>
<dd>&bull; Protocol 2001</dl>
<dl>
<dd>&bull; Protocol 3003</dl>
<p> On the other hand, if the web page for your UPS on the Tripp-Lite website says &quot;HID-compliant USB port also enables direct integration with built-in power management and auto-shutdown features of Windows and MAC OS X&quot;, then you should use the <code><a href="/docs/linux/man/8-usbhid-ups/">usbhid-ups</a></code>(8) driver instead.</p>
<h2>Extra Arguments</h2>
<p>This driver supports the following optional settings in the <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5) file (or with <i>-x</i> on the command line): </p>
<p> <code>offdelay</code></p>
<dl>
<dd>This setting controls the delay between receiving the &quot;kill&quot; command (<i>-k</i>) and actually cutting power to the computer.</dl>
<p> <code>bus</code></p>
<dl>
<dd>This regular expression is used to match the USB bus (as seen in /proc/bus/usb/devices or <a href="/docs/linux/man/8-lsusb/">lsusb</a>(8); including leading zeroes).</dl>
<p> <code>product</code></p>
<dl>
<dd>A regular expression to match the product string for the UPS. This would be useful if you have two different Tripp Lite UPS models connected to the system, and you want to be sure that you shut them down in the correct order.</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font> </p>
<p> This regex is matched against the full USB product string as seen in <a href="/docs/linux/man/8-lsusb/">lsusb</a>(8). The ups.model in the <code><a href="/docs/linux/man/1-upsc/">upsc</a></code>(1) output only lists the name after TRIPP LITE, so to match a SMART2200RMXL2U, you could use the regex .*SMART2200.*. </p>
</dl>
<p> <code>productid</code></p>
<dl>
<dd>The productid is a regular expression which matches the UPS PID as four hexadecimal digits. So far, the only devices that work with this driver have PID 0001.</dl>
<p> <code>serial</code></p>
<dl>
<dd>It does not appear that these particular Tripp Lite UPSes use the iSerial descriptor field to return a serial number. However, in case your unit does, you may specify it here.</dl>
<p> For more information on regular expressions, see <a href="/docs/linux/man/7-regex/">regex</a>(7)</p>
<h2>Runtime Variables</h2>
<p><code>ups.delay.shutdown</code></p>
<dl>
<dd>This variable is the same as the <i>offdelay</i> setting, but it can be changed at runtime by <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8).</dl>
<p> <code>ups.id</code></p>
<dl>
<dd>Some SMARTPRO models feature an ID that can be set and retrieved. If your UPS supports this feature, this variable will be listed in the output of <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8).</dl>
<p> <code>outlet.1.switch</code></p>
<dl>
<dd>Some Tripp Lite units have a switchable outlet (usually outlet #1) which can be turned on and off by writing <i>1</i> or <i>0</i>, respectively, to outlet.1.switch with <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8). If your unit has multiple switchable outlets, substitute the outlet number for <i>1</i> in the variable name. Be sure to test this first &#8211; there is no other way to be certain that the number used by the driver matches the label on the unit.</dl>
<h2>Known Issues And Bugs</h2>
<p>The driver was not developed with any official documentation from Tripp Lite, so certain events may confuse the driver. If you observe any strange behavior, please re-run the driver with -DDD to increase the verbosity. </p>
<p> So far, the Tripp Lite UPSes do not seem to have a serial number or other globally unique identifier accessible through USB. Thus, when monitoring several Tripp Lite USB UPSes, you should use either the <i>bus</i> or <i>product</i> configuration options to uniquely specify which UPS a given driver instance should control. </p>
<p> For instance, you can easily monitor an OMNIVS1000 and a SMART1500RM2U at the same time, since they have different USB Product ID strings. If you have two SMART1500RM2U units, you would have to find which USB bus number each unit is on (via <a href="/docs/linux/man/8-lsusb/">lsusb</a>(8)), which may result in ambiguities if the available USB ports are on the same bus. </p>
<p> Some of the SMART*2U models have an ID number, but because this ID is not exposed as a USB string descriptor, there is no easy way to use this ID to distinguish between multiple UPS units on a single machine. The UPS would need to be claimed by the driver in order to read this ID.</p>
<h2>Author</h2>
<p>Written by Charles Lepple, based on the <code><a href="/docs/linux/man/8-tripplite/">tripplite</a></code>(8) driver by Rickard E. (Rik) Faith and Nicholas Kain. Please do not email the authors directly &#8211; use the nut-upsdev mailing list. </p>
<p> A Tripp Lite OMNIVS1000 was graciously donated to the NUT project by Bradley Feldman (<a rel="nofollow" href="http://www.bradleyloritheo.com)">http://www.bradleyloritheo.com)</a></p>
<h2>See Also</h2>
<h3>The core driver:</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Other drivers for Tripp-Lite hardware:</h3>
<p><code><a href="/docs/linux/man/8-tripplite/">tripplite</a></code>(8), <code><a href="/docs/linux/man/8-tripplitesu/">tripplitesu</a></code>(8), <code><a href="/docs/linux/man/8-usbhid-ups/">usbhid-ups</a></code>(8)</p>
<h3>Other tools:</h3>
<p><a href="/docs/linux/man/7-regex/">regex</a>(7), <a href="/docs/linux/man/8-lsusb/">lsusb</a>(8)</p>
<h2>Internet Resources</h2>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a></p>
