---
title: "nutupsdrv(8)"
name: "nutupsdrv"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nutupsdrv/"
description: "nutupsdrv – generic manual for unified NUT drivers"
---

<p>nutupsdrv &#8211; generic manual for unified NUT drivers</p>
<h2>Synopsis</h2>
<p><code>nutupsdrv</code> <i>-h</i> </p>
<p> <code>nutupsdrv</code> [OPTIONS]</p>
<h2>Description</h2>
<p><code>nutupsdrv</code> is not actually a driver. This is a combined man page for the shared code that is the core of many drivers within the Network UPS Tools package. For information on the specific drivers, see their individual man pages. UPS drivers provide a communication channel between the physical UPS hardware and the <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) server. The driver is responsible for translating the native protocol of the UPS to the common format used by the rest of this package. The core has two modes of operation which are determined by the command line switches. In the normal mode, the driver will periodically poll the UPS for its state and parameters. The results of this command is presented to upsd. The driver will also handle setting variables and instant commands if available. The driver can also instruct the UPS to shut down the load, possibly after some delay. This mode of operation is intended for cases when it is known that the UPS is running out of battery power and the systems attached must be turned off to ensure a proper reboot when power returns.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 You probably don&#8217;t want to use any of these options directly. You should use <code><a href="/docs/linux/man/8-upsdrvctl/">upsdrvctl</a></code>(8) to control your drivers, and <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5) to configure them. The rest of this manual describes options and parameters that generally are not needed by normal users. </p>
<h2>Options</h2>
<p><code>-h</code></p>
<dl>
<dd>Display a help message without doing anything else. This will also list possible values for <i>-x</i> in that driver, and other help text that the driver&#8217;s author may have provided.</dl>
<p> <code>-a</code> <i>id</i></p>
<dl>
<dd>Autoconfigure this driver using the <i>id</i> section of <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5). <code>This argument is mandatory when calling the driver directly.</code></dl>
<p> <code>-D</code></p>
<dl>
<dd>Raise the debugging level. Use this multiple times to see more details. Running a driver in debug mode will prevent it from backgrounding after startup. It will keep on logging information to the console until it receives a SIGINT (usually Ctrl-C) or SIGTERM signal. </p>
<p> The level of debugging needed depends both on the driver and the problem you&#8217;re trying to diagnose. Therefore, first explain the problem you have with a driver to a developer/maintainer, before sending them debugging output. More often than not, if you just pick a level, the output may be either too limited or too verbose to be of any use.</dl>
<p> <code>-q</code></p>
<dl>
<dd>Raise log level threshold. Use this multiple times to log more details. </p>
<p> The debugging comment above also applies here.</dl>
<p> <code>-i</code> <i>interval</i></p>
<dl>
<dd>Set the poll interval for the device.</dl>
<p> <code>-V</code></p>
<dl>
<dd>Print only version information, then exit.</dl>
<p> <code>-L</code></p>
<dl>
<dd>Print a parseable list of driver variables. Mostly useful for configuration wizard programs.</dl>
<p> <code>-k</code></p>
<dl>
<dd>(&quot;Kill&quot; power) Forced shutdown mode. The UPS will power off the attached load, if possible. </p>
<p> You should use upsdrvctl shutdown whenever possible instead of calling this directly.</dl>
<p> <code>-r</code> <i>directory</i></p>
<dl>
<dd>The driver will <a href="/docs/linux/man/2-chroot/">chroot</a>(2) to <i>directory</i> during initialization. This can be useful when securing systems. </p>
<p> In addition to the state path, many systems will require /dev/null to exist within <i>directory</i> for this to work. The serial ports are opened before the chroot call, so you do not need to create them inside the jail. In fact, it is somewhat safer if you do not.</dl>
<p> <code>-u</code> <i>username</i></p>
<dl>
<dd>If started as root, the driver will <a href="/docs/linux/man/2-setuid/">setuid</a>(2) to the user id associated with <i>username</i>. </p>
<p> If you do not specify this value and start it as root, the driver will switch to the default value that was compiled into the code. This is typically <i>nobody</i>, and is far from ideal.</dl>
<p> <code>-x</code> <i>var</i>=<i>val</i></p>
<dl>
<dd>Define a variable called <i>var</i> with the value of <i>var</i> in the driver. This varies from driver to driver &#8211; see the specific man pages for more information. </p>
<p> This is like setting <i>var</i>=<i>val</i> in <code><a href="/docs/linux/man/5-ups-conf/">ups.conf</a></code>(5), but <code>-x</code> overrides any settings from that file.</dl>
<h2>Diagnostics</h2>
<p>Information about the startup process is printed to stdout. Additional messages after that point are available in the syslog. After <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) starts, the UPS clients such as <code><a href="/docs/linux/man/8-upsc/">upsc</a></code>(8) can be used to query the status of an UPS.</p>
<h2>Program Control</h2>
<p>You should always use <code><a href="/docs/linux/man/8-upsdrvctl/">upsdrvctl</a></code>(8) to control the drivers. While drivers can be started by hand for testing purposes, it is not recommended for production use.</p>
<h2>Files</h2>
<p>ups.conf</p>
<dl>
<dd>Required configuration file. This contains all details on which drivers to start and where the hardware is attached.</dl>
<h2>Bugs</h2>
<p>Some of the drivers may have bugs. See their manuals for more information.</p>
<h2>See Also</h2>
<p>Server: <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) Clients: <code><a href="/docs/linux/man/8-upsc/">upsc</a></code>(8), <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8), <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8), <code><a href="/docs/linux/man/8-upslog/">upslog</a></code>(8), <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) CGI programs: <code><a href="/docs/linux/man/8-upsset-cgi/">upsset.cgi</a></code>(8), <code><a href="/docs/linux/man/8-upsstats-cgi/">upsstats.cgi</a></code>(8), <code><a href="/docs/linux/man/8-upsimage-cgi/">upsimage.cgi</a></code>(8) Driver control: <code><a href="/docs/linux/man/8-upsdrvctl/">upsdrvctl</a></code>(8) Drivers: <code><a href="/docs/linux/man/8-al175/">al175</a></code>(8) <code><a href="/docs/linux/man/8-apcsmart/">apcsmart</a></code>(8), <code><a href="/docs/linux/man/8-bcmxcp/">bcmxcp</a></code>(8), <code><a href="/docs/linux/man/8-bcmxcp_usb/">bcmxcp_usb</a></code>(8), <code><a href="/docs/linux/man/8-belkin/">belkin</a></code>(8), <code><a href="/docs/linux/man/8-belkinunv/">belkinunv</a></code>(8), <code><a href="/docs/linux/man/8-bestfcom/">bestfcom</a></code>(8), <code><a href="/docs/linux/man/8-bestuferrups/">bestuferrups</a></code>(8), <code><a href="/docs/linux/man/8-bestups/">bestups</a></code>(8), <code><a href="/docs/linux/man/8-blazer_ser/">blazer_ser</a></code>(8), <code><a href="/docs/linux/man/8-blazer_usb/">blazer_usb</a></code>(8), <code><a href="/docs/linux/man/8-cyberpower/">cyberpower</a></code>(8), <code><a href="/docs/linux/man/8-dummy-ups/">dummy-ups</a></code>(8), <code><a href="/docs/linux/man/8-etapro/">etapro</a></code>(8), <code><a href="/docs/linux/man/8-everups/">everups</a></code>(8), <code><a href="/docs/linux/man/8-gamatronic/">gamatronic</a></code>(8), <code><a href="/docs/linux/man/8-genericups/">genericups</a></code>(8), <code><a href="/docs/linux/man/8-isbmex/">isbmex</a></code>(8), <code><a href="/docs/linux/man/8-liebert/">liebert</a></code>(8), <code><a href="/docs/linux/man/8-masterguard/">masterguard</a></code>(8), <code><a href="/docs/linux/man/8-metasys/">metasys</a></code>(8), <code><a href="/docs/linux/man/8-mge-shut/">mge-shut</a></code>(8), <code><a href="/docs/linux/man/8-mge-utalk/">mge-utalk</a></code>(8), <code><a href="/docs/linux/man/8-mge-xml/">mge-xml</a></code>(8), <code><a href="/docs/linux/man/8-newmge-shut/">newmge-shut</a></code>(8), <code><a href="/docs/linux/man/8-nitram/">nitram</a></code>(8), <code><a href="/docs/linux/man/8-nutdrv_qx/">nutdrv_qx</a></code>(8), <code><a href="/docs/linux/man/8-oneac/">oneac</a></code>(8), <code><a href="/docs/linux/man/8-optiups/">optiups</a></code>(8), <code><a href="/docs/linux/man/8-powercom/">powercom</a></code>(8), <code><a href="/docs/linux/man/8-powerman-pdu/">powerman-pdu</a></code>(8), <code><a href="/docs/linux/man/8-powerpanel/">powerpanel</a></code>(8), <code><a href="/docs/linux/man/8-rhino/">rhino</a></code>(8), <code><a href="/docs/linux/man/8-richcomm_usb/">richcomm_usb</a></code>(8), <code><a href="/docs/linux/man/8-safenet/">safenet</a></code>(8), <code><a href="/docs/linux/man/8-snmp-ups/">snmp-ups</a></code>(8), <code><a href="/docs/linux/man/8-solis/">solis</a></code>(8), <code><a href="/docs/linux/man/8-tripplite/">tripplite</a></code>(8), <code><a href="/docs/linux/man/8-tripplitesu/">tripplitesu</a></code>(8), <code><a href="/docs/linux/man/8-tripplite_usb/">tripplite_usb</a></code>(8), <code><a href="/docs/linux/man/8-usbhid-ups/">usbhid-ups</a></code>(8), <code><a href="/docs/linux/man/8-upscode2/">upscode2</a></code>(8), <code><a href="/docs/linux/man/8-victronups/">victronups</a></code>(8) Internet resources: The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
