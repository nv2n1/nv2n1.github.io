---
title: "digitemp(1)"
name: "digitemp"
section: "1"
letter: "d"
url: "/docs/linux/man/1-digitemp/"
description: "digitemp – program to read from 1-wire temperature sensors."
---

<h2 class="name">NAME</h2>
<p> digitemp &#8211; program to read from 1-wire temperature sensors. </p>
<h2>SYNOPSIS</h2>
<p> <code>digitemp</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> DigiTemp uses the Dallas 1-wire bus to read temperatures from digital sensors attached to a serial port adapter. It handles initializing the bus, searching for attached devices, reading devices and custom log strings. It suports the following temperature devices: DS1820, DS18S20, DS18B20, DS1822 </p>
<p> It also handles the DS2406 1-wire hub switches, and DS2422 and DS2423 counters. </p>
<p> DigiTemp uses either the DS9097 passive serial port adapter, or the DS2480B based DS9097U adapter. 1-wire adapters from ibuttonlink.com, such as the Link45 are also supported.</p>
<h2>OPTIONS</h2>
<p> At least 1 action must be given, along with some optional arguments. Actions are one (and only on) of the <code>-w -t -a -w </code> options</p>
<dl>
<dt><code>-h, -?</code></p>
<dd> Show summary of options.</p>
<dt><code>-v</code></p>
<dd> Show verbose output.</p>
<dt><code>-i </code></p>
<dd> Initialize .digitemprc file, search the bus for all supported devices.</p>
<dt><code>-I</code></p>
<dd> Initialize .digitemprc file, search the bus for all supported devices, store devices in sorted serial # order.</p>
<dt><code>-w</code></p>
<dd> Walk the full device tree and display the serial number and type of all devices detected on the bus.</p>
<dt><code>-s /dev/ttyS0</code></p>
<dd> Set serial port to use. Make sure you have permission to access this port. For USB operation pass USB instead of /dev/ttySX</p>
<dt><code>-l /var/log/temperature</code></p>
<dd> Send output to logfile, the output format is defined by the .B -o command</p>
<dt><code>-c digitemp.conf</code></p>
<dd> Set digitemp configuration file. The default is .digitemprc in the current directory.</p>
<dt><code>-r 1000</code></p>
<dd> Read delay in ms. This sets the amount of time to wait between sending the temperature conversion command and reading the result. The DS18S20 takes about 750mS to do the temperature conversion. Default is 1000mS (1 sec).</p>
<dt><code>-t #</code></p>
<dd> Read sensor number #, the # depends on the order of the sensors in the .digitemprc file.</p>
<dt><code>-q</code></p>
<dd> Quiet output, no copyright banner.</p>
<dt><code>-a</code></p>
<dd> Read all sensors.</p>
<dt><code>-A</code></p>
<dd> Treat DS2438 as A/D converter, output raw voltages and currents.</p>
<dt><code>-d 5</code></p>
<dd> Delay between samples (in seconds).</p>
<dt><code>-n 50</code></p>
<dd> Number of times to repeat the command.</p>
<dt><code>-Ocounter format string</code></p>
<dd> See Counter Format below.</p>
<dt><code>-o [1..3] [output format string]</code></p>
<dd> See Temperature Format below.</p>
<dt><code>-HHumidity format string</code></p>
<dd> See Humidity Format below.</dl>
<h2>Temperature Format</h2>
<p> The temperature format can be either a numeric value, or a string. The numeric values select pre-configured output formats: </p>
<p>&nbsp;<wbr>1&nbsp;<wbr>=&nbsp;<wbr>One line per sensor, time, C, F&nbsp;<wbr>(default)&nbsp;<wbr><br />
&nbsp;<wbr>2&nbsp;<wbr>=&nbsp;<wbr>One line per sample, elapsed time, temperature in C<br />
&nbsp;<wbr>3&nbsp;<wbr>=&nbsp;<wbr>Same as&nbsp;<wbr>#2, except temperature is in F </p>
<p> #2 and #3 have the data seperated by tabs, suitable for import into a spreadsheet or other graphing software. </p>
<p> The format string uses strftime tokens plus 5 special ones for DigiTemp:</p>
<dl>
<dt><code>%s</code></p>
<dd> for sensor #</p>
<dt><code>%C</code></p>
<dd> for centigrade</p>
<dt><code>%F</code></p>
<dd> for fahrenheit</p>
<dt><code>%R</code></p>
<dd> to output the hex serial number</p>
<dt><code>%N</code></p>
<dd> for seconds since Epoch.</dl>
<p> The case of the token is important! The default format string is: &quot;%b %d %H:%M:%S Sensor %s C: %.2C F: %.2F&quot; which gives you an output of: May 24 21:25:43 Sensor 0 C: 23.66 F: 74.59 </p>
<p> The DS2438 sensor can be used for a variety of things. It includes a temperature sensor and A/D converter. DigiTemp defaults to using it as a humidity sensor. The raw voltages and currents can be displayed by passing the -A argument </p>
<p> When the -o2 or -o3 log options are used the attached DS2438&#8217;s temperatures will be output without the humidity. </p>
<h2>Counter Format String</h2>
<p> The counter format string is similar, adding these tokens:</p>
<dl>
<dt><code>%n</code></p>
<dd> is the counter #, which depends on its position in the .digitemprc file</p>
<dt><code>%C</code></p>
<dd> is the count in decimal.</dl>
<h2>Humidity Format String</h2>
<p> The Humidity format string is the same as the temperature format string with the addition of this format specifier:</p>
<dl>
<dt><code>%h</code></p>
<dd> is the humidity in 0-100%</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Jes&uacute;s Roncero &lt;jesus [at] roncero.org&gt;, for the Debian project (but may be used by others). Modifications by Brian C. Lane &lt;bcl [at] brianlane.com&gt;</p>
<h2>UPDATES</h2>
<p> DigiTemp updates can be found on the <a rel="nofollow" href="http://www.digitemp.com">http://www.digitemp.com</a> website. </p>
<h2>Index</h2>
