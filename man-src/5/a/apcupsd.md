---
title: "apcupsd(5)"
name: "apcupsd"
section: "5"
letter: "a"
url: "/docs/linux/man/5-apcupsd/"
description: "apcupsd.conf –"
---

<p><code>apcupsd.conf </code> &#8211; </p>
<p><a href="/docs/linux/man/8-apcupsd/">apcupsd</a>(8) configuration file</p>
<h2>Description</h2>
<p>is the configuration file for the <a href="/docs/linux/man/8-apcupsd/">apcupsd</a>(8) program. The file is a plain ASCII text file which comprises a number of configuration directives which control how the apcupsd program behaves when controlling most American Power Conversion Corp (APC) UPSes. The configuration file is also used for the <a href="/docs/linux/man/8-apctest/">apctest</a>(8) program when bulk programming the EEPROM in a Smart-UPS model. It will almost certainly be necessary to customise the information in the configuration file to suit your particular configuration and operating requirements. The configuration file directives are explained in the subsections below.</p>
<h3>General Configuration Directives</h3>
<dt><code>UPSNAME &lt;string&gt;</code></dt>
<dd>Specify a name for the UPS for log files, status reports etc.</dd>
<dt><code>UPSCABLE [ simple | smart | ether | usb | 940-0119A | 940-0127A | 940-0128A | 940-0020B | 940-0020C | 940-0023A | 940-0024B | 940-0024C | 940-1524C | 940-0024G | 940-0095A | 940-0095B | 940-0095C | MAM-04-02-2000 ]</code></dt>
<dd>The type of cable used to connect the UPS to the computer.</dd>
<dt><code>UPSTYPE [ dumb | apcsmart | net | usb | snmp | pcnet | test ]</code></dt>
<dd>The type of APC UPS that you have.</dd>
<dt><code>DEVICE &lt;name&gt;</code></dt>
<dd>The name of the device used for communication between the UPS and the computer. For a USB UPS, you should leave the DEVICE directive blank and apcupsd will figure out where the device is located.  </dd>
<li> apcsmart : /dev/tty** (serial connection)
<li> usb : leave blank! (USB connection)
<li> net : hostname:port (NIS connection)
<li> snmp : hostname:port:vendor:community (SNMP connection)
<li> dumb : /dev/tty** (serial connection)
<li> pcnet : ipaddr:username:passphrase (AP9617 SmartSlot card) </ul>
<p> If you have problems, please see the apcupsd manual for more detailed information and comprehensive troubleshooting advice.</p>
<dt><code>POLLTIME &lt;seconds&gt;</code></dt>
<dd>The rate in seconds that the daemon polls the UPS for status. This rate is automatically set to 1 second when the UPS goes on battery and reset to the specified value when the utility power returns. This setting applies both to directly-attached UPSes and networked UPSes. A low setting will improve the daemon&#8217;s responsiveness to certain events at the cost of higher CPU utilisation. The default of 60 is appropriate for most situations.</dd>
<dt><code>LOCKFILE &lt;path&gt;</code></dt>
<dd>apcupsd creates a lockfile for the serial or USB port in the specified directory. It must be changed when running more than one copy of apcupsd on the same computer to control multiple UPSes.</dd>
<dt><code>SCRIPTDIR &lt;path&gt;</code></dt>
<dd>Directory in which apccontrol and event scripts are located. Defaults to /usr/local/etc/apcupsd It must be changed when running more than one copy of apcupsd on the same computer to control multiple UPSes.</dd>
<dt><code>PWRFAILDIR &lt;path&gt;</code></dt>
<dd>Directory in which apcupsd writes the powerfail flag file created when apcupsd initiates a system shutdown. The directory is checked in halt scripts to determine if turning off the UPS output power is required. Defaults to /var/run It must be changed when running more than one copy of apcupsd on the same computer to control multiple UPSes.</dd>
<dt><code>NOLOGINDIR &lt;path&gt;</code></dt>
<dd>Directory in which apcupsd writes the nologin file which tells the OS to disallow new logins. Defaults to /var/run It must be changed when running more than one copy of apcupsd on the same computer to control multiple UPSes.</dd></dl>
<h3>Nis Configuration Directives</h3>
<dt><code>NETSERVER [ on | off ]</code></dt>
<dd>Turns the network information server (NIS) on or off. When on, apcupsd serves status and event information over the network. This information is also used by the web-based CGI monitoring programs. The default is set to on.</dd>
<dt><code>NISIP &lt;IP address&gt;</code></dt>
<dd>Specifies the IP address of the network interface on which apcupsd will listen for incoming connections. The default value is 0.0.0.0 which means the NIS will listen for connections on all network interfaces. If the computer has more than one interface, you can specify the IP of a single interface to limit connections to that interface. Specifying the loopback address (127.0.0.1) will cause the NIS daemon to accept connections only from the local computer.</dd>
<dt><code>NISPORT &lt;port&gt;</code></dt>
<dd>Specifies the port to be used by the NIS daemon. The default is 3551 which has been received from IANA as the official apcupsd networking port. It must be changed when running more than one copy of apcupsd on the same computer to control multiple UPSes.</dd>
<dt><code>EVENTSFILE &lt;filename&gt;</code></dt>
<dd>If you want NIS to provide the last 10 events via the network, you must specify a file where apcupsd will save these events. The default is: /var/log/apcupsd.events apcupsd will save at most the last 50 events to this file. When more than 50 events are saved and a network request for the events arrives, apcupsd will truncate the file to the most recent 10 events. It must be changed when running more than one copy of apcupsd on the same computer to control multiple UPSes.</dd></dl>
<h3>Logging Configuration Directives</h3>
<dt><code>STATTIME &lt;seconds&gt;</code></dt>
<dd>Specifies the time interval between writes to the status file. If set to zero, the status file will not be written. The status file will disappear in a future apcupsd version as its functionality has been replaced by the Network Information Server and the <a href="/docs/linux/man/8-apcaccess/">apcaccess</a>(8) program.</dd>
<dt><code>STATFILE &lt;file&gt;</code></dt>
<dd>Specifies the file to be used when writing the status information. The default is /etc/apcupsd/apcupsd.status It must be changed when running more than one copy of apcupsd on the same computer to control multiple UPSes.</dd>
<dt><code>LOGSTATS [ on | off ]</code></dt>
<dd>Activate log file. This generates a lot of output, so if you turn this on, be sure that the file defined in syslog.conf5 for LOG_NOTICE is a named pipe.</dd>
<dt><code>DATATIME &lt;seconds&gt;</code></dt>
<dd>Specifies the time interval between writes of the APC PowerChute software-like data information to the log file.</dd>
<dt><code>FACILITY &lt;log-facility&gt;</code></dt>
<dd>Change the system logging (syslog) facility. The default is daemon. This parameter can be useful if you wish to direct the apcupsd system logging information to other than your system default files. See syslog.conf5 for details of other possible facilities and general system logging configuration. </dd>
<h3>Power Failure Configuration Directives</h3>
<dt><code>ONBATTERYDELAY &lt;seconds&gt;</code></dt>
<dd>The number of seconds from when a power failure is detected until apcupsd reacts with an onbattery event.</dd>
<dt><code>BATTERYLEVEL &lt;percentage&gt;</code></dt>
<dd>apcupsd will shutdown the system during a power failure when the remaining battery charge falls below the specified percentage. The default is 5.</dd>
<dt><code>MINUTES &lt;minutes&gt;</code></dt>
<dd>apcupsd will shutdown the system during a power failure when the remaining runtime on batteries as internally calculated by the UPS falls below the specified minutes. The default is 3.</dd>
<dt><code>TIMEOUT &lt;seconds&gt;</code></dt>
<dd>After a power failure occurs, apcupsd will shutdown the system after the specified number of seconds have expired. For a Smart-UPS, this should normally be set to zero so that the shutdown time will be determined by the battery level or remaining runtime (see above). This command is, however, useful for a Back-UPS or other simple signalling UPS which does not report battery level or the remaining runtime. It is also useful for testing apcupsd because you can force a rapid shutdown by setting a small value (eg 60) and turning off the power to the UPS. TIMEOUT, BATTERYLEVEL, and MINUTES can all be set without problems. apcupsd will initiate a shutdown when the first of these conditions becomes valid.</dd>
<dt><code>ANNOY &lt;seconds&gt;</code></dt>
<dd>Specifies the time in seconds between broadcast messages requesting logged in users to log off from the system. This timer starts only when the UPS is running on battery. The default is 300 seconds (5 minutes).</dd>
<dt><code>ANNOYDELAY &lt;seconds&gt;</code></dt>
<dd>Specifies the delay time in seconds before broadcast messages requesting logged in users to log off from the system. This timer starts only after the UPS is running on battery power. This timer is reset when the power returns. The default is 60 seconds (ie the first request to log off occurs after 60 seconds on battery power).</dd>
<dt><code>NOLOGON [ disable | timeout | percent | minutes | always ]</code></dt>
<dd>Specifies when apcupsd should create the nologon file to prevent users from logging on to the system. &quot;disable&quot; prevents apcupsd from creating the nologin file. &quot;timeout&quot; specifies a specific wait time before apcupsd creates the nologin file. &quot;percent&quot; specifies the percentage of battery charge remaining before apcupsd creates the nologin file. &quot;minutes&quot; specifies the battery runtime remaining before apcupsd creates the nologin file. &quot;always&quot; specifies that apcupsd should create the nologin file immediately after a power failure occurs. This directive is important for allowing systems with BIG UPSes to run normally until the system administrator determines the need for dumping users. It also allows the system administrator to hold the &quot;ANNOY&quot; factor until the /etc/nologin file is created.</dd>
<dt><code>KILLDELAY &lt;seconds&gt;</code></dt>
<dd>Specifies the number of seconds for which apcupsd will continue running after a shutdown has been requested. After the specified time, apcupsd will attempt to put the UPS into hibernate mode and kill the power to the computer. This is for use on operating systems where apcupsd cannot regain control after a shutdown (eg FreeBSD) to issue an apcupsd &#8211;killpower command. Setting the delay to 0 disables it.</dd></dl>
<h3>Share-Ups Configuration Directives</h3>
<dt><code>UPSCLASS [ standalone | shareslave | sharemaster ]</code></dt>
<dd>The default is &quot;standalone&quot; and should be used for all computers powered by the UPS, with a direct connection to the UPS and where there are no other computers dependent on power from the UPS. This is the &quot;normal&quot; case. Use &quot;shareslave&quot; if you are using a Share-UPS interface expander and connected to the BASIC port (simple signalling). Use &quot;sharemaster&quot;, if you are using a Share-UPS interface expander and connected to the ADVANCED port (smart signalling).</dd>
<dt><code>UPSMODE [ disable | share ]</code></dt>
<dd>Set to &quot;disable&quot; for normal standalone operation to indicate that you are disabling the Share-UPS interface expander support. Set to &quot;share&quot; for two to seven additional simple signalling ports on a Share-UPS interface expander. This code may not be fully tested in every new release.</dd></dl>
<h3>Apctest Eeprom Configuration Directives</h3>
<p>These directives have no effect on the operation of <a href="/docs/linux/man/8-apcupsd/">apcupsd</a>(8) but are reserved for use by <a href="/docs/linux/man/8-apctest/">apctest</a>(8) when bulk programming the values of the UPS EEPROM configuration variables in a Smart-UPS model. </p>
<dt><code>UPSNAME &lt;string&gt;</code></dt>
<dd>Name of UPS. Maximum of 8 characters.</dd>
<dt><code>BATTDATE [ mm/dd/yy | dd/mm/yy ]</code></dt>
<dd>Last battery replacement date. Maximum of 8 characters.</dd>
<dt><code>SENSITIVITY [ H | M | L ]</code></dt>
<dd>
</dd><dt><code>H : High (most sensitive setting)</code></dt>
<dd>
</dd><dt><code>M : Medium</code></dt>
<dd>
</dd><dt><code>L : Low (least sensitive setting)</code></dt>
<dd></dd></dl>
<dt><code>WAKEUP [ 000 | 060 | 180 | 300 ] </code></dt>
<dd>The time delay in seconds that the UPS waits after the return of utility power before &quot;waking up&quot; and restoring power to the connected equipment.</dd>
<dt><code>SLEEP [ 020 | 180 | 300 | 600 ]</code></dt>
<dd>The time delay in seconds for which the UPS waits or &quot;sleeps&quot; after it receives a request to power off the connected system.</dd>
<dt><code>LOTRANSFER &lt;voltage&gt;</code></dt>
<dd>Low line voltage causing transfer to battery power or activation of SmartBoost. Allowable values depend on the last letter of the firmware or APCMODEL. Typical values are:<br/>
&nbsp;<wbr>&nbsp;<wbr>D&nbsp;<wbr>&nbsp;<wbr>106&nbsp;<wbr>&nbsp;<wbr>103&nbsp;<wbr>&nbsp;<wbr>100&nbsp;<wbr>&nbsp;<wbr>097<br/>
&nbsp;<wbr>&nbsp;<wbr>M&nbsp;<wbr>&nbsp;<wbr>177&nbsp;<wbr>&nbsp;<wbr>172&nbsp;<wbr>&nbsp;<wbr>168&nbsp;<wbr>&nbsp;<wbr>182<br/>
&nbsp;<wbr>&nbsp;<wbr>A&nbsp;<wbr>&nbsp;<wbr>092&nbsp;<wbr>&nbsp;<wbr>090&nbsp;<wbr>&nbsp;<wbr>088&nbsp;<wbr>&nbsp;<wbr>086<br/>
&nbsp;<wbr>&nbsp;<wbr>I&nbsp;<wbr>&nbsp;<wbr>208&nbsp;<wbr>&nbsp;<wbr>204&nbsp;<wbr>&nbsp;<wbr>200&nbsp;<wbr>&nbsp;<wbr>196 where D = domestic (USA), M = Canada, A = Asia and I = International.</dd>
<dt><code>HITRANSFER &lt;voltage&gt;</code></dt>
<dd>High line voltage causing transfer to battery power or activation of SmartTrim. Allowable values depend on the last letter of the firmware or APCMODEL. Typical values are:<br/>
&nbsp;<wbr>&nbsp;<wbr>D&nbsp;<wbr>&nbsp;<wbr>127&nbsp;<wbr>&nbsp;<wbr>130&nbsp;<wbr>&nbsp;<wbr>133&nbsp;<wbr>&nbsp;<wbr>136<br/>
&nbsp;<wbr>&nbsp;<wbr>M&nbsp;<wbr>&nbsp;<wbr>229&nbsp;<wbr>&nbsp;<wbr>234&nbsp;<wbr>&nbsp;<wbr>239&nbsp;<wbr>&nbsp;<wbr>224<br/>
&nbsp;<wbr>&nbsp;<wbr>A&nbsp;<wbr>&nbsp;<wbr>108&nbsp;<wbr>&nbsp;<wbr>110&nbsp;<wbr>&nbsp;<wbr>112&nbsp;<wbr>&nbsp;<wbr>114<br/>
&nbsp;<wbr>&nbsp;<wbr>I&nbsp;<wbr>&nbsp;<wbr>253&nbsp;<wbr>&nbsp;<wbr>257&nbsp;<wbr>&nbsp;<wbr>261&nbsp;<wbr>&nbsp;<wbr>265 where D = domestic (USA), M = Canada, A = Asia and I = International.</dd>
<dt><code>RETURNCHARGE [ 00 | 15 | 50 | 90 ]</code></dt>
<dd>Percentage of battery charge needed for the UPS to restore power to the connected equipment.</dd>
<dt><code>BEEPSTATE [ 0 | T | L | N ]</code></dt>
<dd>Alarm delay. </dd>
<dt><code>0 : Zero delay after power fails.</code></dt>
<dd>
</dd><dt><code>T : When power fails plus 30 seconds.</code></dt>
<dd>
</dd><dt><code>L : When low battery occurs.</code></dt>
<dd>
</dd><dt><code>N : Never.</code></dt>
<dd></dd></dl>
<dt><code>LOWBATT &lt;minutes&gt;</code></dt>
<dd>Low battery warning occurs when the specified number of minutes remains before the UPS estimates battery power will be exhausted. There are four user-changeable settings: 2, 5, 7, or 10 minutes</dd>
<dt><code>OUTPUTVOLTS &lt;voltage&gt;</code></dt>
<dd>UPS nominal output voltage when running on battery. Allowable values depend on the last letter of the firmware or APCMODEL. Typical values are:<br/>
&nbsp;<wbr>&nbsp;<wbr>D&nbsp;<wbr>&nbsp;<wbr>115<br/>
&nbsp;<wbr>&nbsp;<wbr>M&nbsp;<wbr>&nbsp;<wbr>208<br/>
&nbsp;<wbr>&nbsp;<wbr>A&nbsp;<wbr>&nbsp;<wbr>100<br/>
&nbsp;<wbr>&nbsp;<wbr>I&nbsp;<wbr>&nbsp;<wbr>230&nbsp;<wbr>&nbsp;<wbr>240&nbsp;<wbr>&nbsp;<wbr>220&nbsp;<wbr>&nbsp;<wbr>225 where D = domestic (USA), M = Canada, A = Asia and I = International.</dd>
<dt><code>SELFTEST [ 336 | 168 | ON | OFF ]</code></dt>
<dd>Self test interval in hours (336 = 2 weeks, 168 = 1 week, ON = at power on, OFF = never). </dd>
<h2>Examples</h2>
<p>Note that in the following examples, the device names assume that you are using Linux. Device names for serial devices in *BSD and other operating systems will be different.</p>
<h3>Minimal USB Configuration for a USB UPS</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>UPSCABLE usb<br/>
&nbsp;<wbr>&nbsp;<wbr>UPSTYPE usb<br/>
&nbsp;<wbr>&nbsp;<wbr>DEVICE<br/>
&nbsp;<wbr>&nbsp;<wbr>LOCKFILE&nbsp;<wbr>/var/lock<br/>
&nbsp;<wbr>&nbsp;<wbr>UPSCLASS standalone<br/>
&nbsp;<wbr>&nbsp;<wbr>UPSMODE disable Notice no device name is specified. <a href="/docs/linux/man/8-apcupsd/">apcupsd</a>(8) will try all the well known USB ports. Only specify a specific USB device name if you know what you are doing. For detailed information on setting up a USB UPS, refer to the &quot;USB Configuration&quot; section of the apcupsd manual.</p>
<h3>Minimal Serial Configuration for a Smart UPS</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>UPSCABLE smart<br/>
&nbsp;<wbr>&nbsp;<wbr>UPSTYPE apcsmart<br/>
&nbsp;<wbr>&nbsp;<wbr>DEVICE&nbsp;<wbr>/dev/ttyS0<br/>
&nbsp;<wbr>&nbsp;<wbr>LOCKFILE&nbsp;<wbr>/var/lock<br/>
&nbsp;<wbr>&nbsp;<wbr>UPSCLASS standalone<br/>
&nbsp;<wbr>&nbsp;<wbr>UPSMODE disable Normally there would be more configuration directives to completely customise your installation, but this example shows the minimum required.</p>
<h3>Minimal Serial Configuration for a Dumb UPS</h3>
<p>&nbsp;<wbr>&nbsp;<wbr>UPSCABLE&nbsp;<wbr>&lt;number of the cable used&gt;<br/>
&nbsp;<wbr>&nbsp;<wbr>UPSTYPE dumb<br/>
&nbsp;<wbr>&nbsp;<wbr>DEVICE&nbsp;<wbr>/dev/ttyS0<br/>
&nbsp;<wbr>&nbsp;<wbr>LOCKFILE&nbsp;<wbr>/var/lock<br/>
&nbsp;<wbr>&nbsp;<wbr>UPSCLASS standalone<br/>
&nbsp;<wbr>&nbsp;<wbr>UPSMODE disable If your cable does not have low battery detection (eg such cables include the APC 940-0020B and 940-0023A), you will also need to define the TIMEOUT &lt;seconds&gt; configuration directive to set the number of seconds on battery during a power failure after which apcupsd will do a system shutdown. Normally there would be more configuration directives to completely customise your installation, but this example shows the minimum required. </p>
<h2>Files</h2>
<p>/etc/apcupsd/apcupsd.conf default configuration file</p>
<h2>See Also</h2>
<p>syslog.conf5, <a href="/docs/linux/man/8-apcupsd/">apcupsd</a>(8), <a href="/docs/linux/man/8-apctest/">apctest</a>(8). </p>
<p> The HTML apcupsd manual installed on your system or available online at <a rel="nofollow" href="http://www.apcupsd.org/">http://www.apcupsd.org/</a></p>
<h2>Authors</h2>
<p>An Trevor Roydhouse (current) An Andre M. Hedrick An Christopher J. Reimer</p>
