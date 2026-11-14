---
title: "usbhid-ups(8)"
name: "usbhid-ups"
section: "8"
letter: "u"
url: "/docs/linux/man/8-usbhid-ups/"
description: "usbhid-ups – Driver for USB/HID UPS equipment"
---

<p>usbhid-ups &#8211; Driver for USB/HID UPS equipment</p>
<h2>Note</h2>
<p>This man page only documents the hardware-specific features of the usbhid-ups driver. For information about the core driver, see <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8). </p>
<p> This driver, formerly called <i>newhidups</i>, replaces the legacy <i>hidups</i> driver, which only supported Linux systems.</p>
<h2>Supported Hardware</h2>
<p><code>usbhid-ups</code> brings USB/HID UPS monitoring to NUT on all platform supporting USB through libusb. It should detect any UPS that uses the HID power device class, but the amount of data will vary depending on the manufacturer and model. </p>
<p> At the present time, usbhid-ups supports: </p>
<dl>
<dd>&bull; the newer Eaton USB models,</dl>
<dl>
<dd>&bull; all MGE USB models,</dl>
<dl>
<dd>&bull; all Dell USB models,</dl>
<dl>
<dd>&bull; some APC models,</dl>
<dl>
<dd>&bull; some Belkin models,</dl>
<dl>
<dd>&bull; some Cyber Power Systems models.</dl>
<dl>
<dd>&bull; some TrippLite models</dl>
<p> For a more complete list, refer to the NUT hardware compatibility list, available in the source distribution as data/drivers.list, or on the NUT website. You may use the &quot;explore&quot; driver option to gather information from HID UPSes which are not yet supported; see below for details. </p>
<p> This driver is known to work on: </p>
<dl>
<dd>&bull; most Linux systems,</dl>
<dl>
<dd>&bull; FreeBSD (beta stage) and maybe other *BSD,</dl>
<dl>
<dd>&bull; Darwin / Mac OS X,</dl>
<dl>
<dd>&bull; Solaris 10.</dl>
<h2>Extra Arguments</h2>
<p>This driver also supports the following optional settings: </p>
<p> <code>offdelay</code>=<i>num</i></p>
<dl>
<dd>Set the timer before the UPS is turned off after the kill power command is sent (via the <code>-k</code> switch). </p>
<p> The default value is 20 (in seconds). Usually this <code>must be lower</code> than <i>ondelay</i>, but the driver will <code>not</code> warn you upon startup if it isn&#8217;t.</dl>
<p> <code>ondelay</code>=<i>num</i></p>
<dl>
<dd>Set the timer for the UPS to switch on in case the power returns after the kill power command had been sent but before the actual switch off. This ensures the machines connected to the UPS are, in all cases, rebooted after a power failure. </p>
<p> The default value is 30 (in seconds). Usually this <code>must be greater</code> than offdelay, but the driver will <code>not</code> warn you upon startup if it isn&#8217;t. Some UPS&#8217;es will restart no matter what, even if the power is (still) out at the moment this timer elapses. In that case, you could try if setting <i>ondelay = -1</i> in <code>ups.conf</code> helps.</dl>
<p> <code>pollfreq</code>=<i>num</i></p>
<dl>
<dd>Set polling frequency, in seconds, to reduce the USB data flow. Between two polling requests, the driver will wait for interrupts (aka UPS notifications), which are data changes returned by the UPS by itself. This mechanism allow to avoid or reduce staleness message, due to the UPS being temporarily overloaded with too much polling requests. The default value is 30 (in seconds).</dl>
<p> <code>pollonly</code></p>
<dl>
<dd>If this flag is set, the driver will ignore interrupts it receives from the UPS (not recommended, but needed if these reports are broken on your UPS).</dl>
<p> <code>vendor</code>=<i>regex</i>, <code>product</code>=<i>regex</i>, <code>serial</code>=<i>regex</i>, <code>vendorid</code>=<i>regex</i>, <code>productid</code>=<i>regex</i></p>
<dl>
<dd>Select a specific UPS, in case there is more than one connected via USB Each option specifies an extended regular expression (see <a href="/docs/linux/man/7-regex/">regex</a>(7)) that must match the UPS&#8217;s entire vendor/product/serial string (minus any surrounding whitespace), or the whole 4-digit hexadecimal code for vendorid and productid. Try <code>-DD</code> for finding out the strings to match. </p>
<p> Examples: </p>
<dl>
<dd>&bull; </p>
<p> -x vendor=&quot;Foo.Corporation.*&quot;</dl>
<dl>
<dd>&bull; </p>
<p> -x vendorid=051d* (APC)</dl>
<dl>
<dd>&bull; </p>
<p> -x product=&quot;.*(Smart|Back)-?UPS.*&quot;</dl>
</dl>
<p> <code>bus</code>=<i>regex</i></p>
<dl>
<dd>Select a UPS on a specific USB bus or group of busses. The argument is a regular expression that must match the bus name where the UPS is connected (e.g. bus=&quot;002&quot;, bus=&quot;00[2-3]&quot;).</dl>
<p> <code>explore</code></p>
<dl>
<dd>With this option, the driver will connect to any device, including ones that are not yet supported. This must always be combined with the &quot;vendorid&quot; option. In this mode, the driver will not do anything useful except for printing debugging information (typically used with -DD).</dl>
<p> <code>maxreport</code></p>
<dl>
<dd>With this option, the driver activates a tweak to workaround buggy firmware returning invalid HID report length. Some APC Back-UPS units are known to have this bug.</dl>
<h2>Installation</h2>
<p>This driver is not built by default. You can build it by using &quot;configure &#8211;with-usb=yes&quot;. Note that it will also install other USB drivers. </p>
<p> You also need to install manually the legacy hotplug files (libhidups and libhid.usermap, generally in /etc/hotplug/usb/), or the udev file (nut-usbups.rules, generally in /etc/udev/rules.d/) to address the permission settings problem. For more information, refer to the README file in nut/scripts/hotplug or nut/scripts/udev. </p>
<p> On Linux with MGE equipment, you will need at least a 2.4.25 or 2.6.2 kernel as well as libusb-0.1.8 or later to disable hiddev support and avoid conflict.</p>
<h2>Implementation</h2>
<p>The driver ignores the &quot;port&quot; value in <code>ups.conf</code>. Unlike previous versions of this driver, it is now possible to control multiple UPS units simultaneously with this driver, provided they can be distinguished by setting some combination of the &quot;vendor&quot;, &quot;product&quot;, &quot;serial&quot;, &quot;vendorid&quot;, and &quot;productid&quot; options. For instance: </p>
<dl>
<dd>
<pre>[mge]
 driver = usbhid-ups
 port = auto
 vendorid = 0463
[tripplite]
 driver = usbhid-ups
 port = auto
 vendorid = 09ae</pre>
</dl>
<h2>Known Issues And Bugs</h2>
<h3>Repetitive timeout and staleness</h3>
<p>Some models tends to be unresponsive with the default polling frequency. The result is that your system log will have lots of messages like: </p>
<dl>
<dd>
<pre>usb 2-1: control timeout on ep0in
usb 2-1: usbfs: USBDEVFS_CONTROL failed cmd usbhid-ups rqt 128 rq 6 len 256
ret -110</pre>
</dl>
<p> In this case, simply modify the general parameter &quot;pollinterval&quot; to a higher value (like 10 for 10 seconds). This should solve the issue.</p>
<h3>Got EPERM: Operation not permitted upon driver startup</h3>
<p>You have forgotten to install the hotplug files, as explained in the INSTALLATION section above. Don&#8217;t forget to restart hotplug so that it applies these changes.</p>
<h3>Unattended shutdowns</h3>
<p>The hardware which was used for development of this driver is almost certainly different from what you have, and not all manufacturers follow the USB HID Power Device Class specifications to the letter. You don&#8217;t want to find out that yours has issues here when a power failure hits your server room and you&#8217;re not around to manually restart your servers. </p>
<p> If you rely on the UPS to shutdown your systems in case of mains failure and to restart them when the power returns, you <code>must</code> test this. You can do so by running <i>upsmon -c fsd</i>. With the mains present, this should bring your systems down and then cycle the power to restart them again. If you do the same without mains present, it should do the same, but in this case, the outputs shall remain off until mains power is applied again.</p>
<h2>Authors</h2>
<p>Originally sponsored by MGE UPS SYSTEMS. Now sponsored by Eaton <a rel="nofollow" href="http://opensource.eaton.com">http://opensource.eaton.com</a> Arnaud Quette, Peter Selinger, Arjen de Korte</p>
<h2>See Also</h2>
<h3>The core driver</h3>
<p><code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8)</p>
<h3>Internet resources</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
