---

title: "digitemp(1)"
name: "digitemp"
section: "1"
letter: "d"
url: "/docs/linux/man/1-digitemp/"
description: "digitemp – program to read from 1-wire temperature sensors."
---

<p> <code>digitemp</code> [<i>options</i>]</p>
<p> DigiTemp uses the Dallas 1-wire bus to read temperatures from digital sensors attached to a serial port adapter. It handles initializing the bus, searching for attached devices, reading devices and custom log strings. It suports the following temperature devices: DS1820, DS18S20, DS18B20, DS1822 </p>
<p> It also handles the DS2406 1-wire hub switches, and DS2422 and DS2423 counters. </p>
<p> DigiTemp uses either the DS9097 passive serial port adapter, or the DS2480B based DS9097U adapter. 1-wire adapters from ibuttonlink.com, such as the Link45 are also supported.</p>
<h2>OPTIONS</h2>
<p> At least 1 action must be given, along with some optional arguments. Actions are one (and only on) of the <code>-w -t -a -w </code> options</p>
<dl>
<dt><code>-h, -?</code></dt>
<dd> Show summary of options.</dd>
<dt><code>-v</code></dt>
<dd> Show verbose output.</dd>
<dt><code>-i </code></dt>
<dd> Initialize .digitemprc file, search the bus for all supported devices.</dd>
<dt><code>-I</code></dt>
<dd> Initialize .digitemprc file, search the bus for all supported devices, store devices in sorted serial # order.</dd>
<dt><code>-w</code></dt>
<dd> Walk the full device tree and display the serial number and type of all devices detected on the bus.</dd>
<dt><code>-s /dev/ttyS0</code></dt>
<dd> Set serial port to use. Make sure you have permission to access this port. For USB operation pass USB instead of /dev/ttySX</dd>
<dt><code>-l /var/log/temperature</code></dt>
<dd> Send output to logfile, the output format is defined by the .B -o command</dd>
<dt><code>-c digitemp.conf</code></dt>
<dd> Set digitemp configuration file. The default is .digitemprc in the current directory.</dd>
<dt><code>-r 1000</code></dt>
<dd> Read delay in ms. This sets the amount of time to wait between sending the temperature conversion command and reading the result. The DS18S20 takes about 750mS to do the temperature conversion. Default is 1000mS (1 sec).</dd>
<dt><code>-t #</code></dt>
<dd> Read sensor number #, the # depends on the order of the sensors in the .digitemprc file.</dd>
<dt><code>-q</code></dt>
<dd> Quiet output, no copyright banner.</dd>
<dt><code>-a</code></dt>
<dd> Read all sensors.</dd>
<dt><code>-A</code></dt>
<dd> Treat DS2438 as A/D converter, output raw voltages and currents.</dd>
<dt><code>-d 5</code></dt>
<dd> Delay between samples (in seconds).</dd>
<dt><code>-n 50</code></dt>
<dd> Number of times to repeat the command.</dd>
<dt><code>-Ocounter format string</code></dt>
<dd> See Counter Format below.</dd>
<dt><code>-o [1..3] [output format string]</code></dt>
<dd> See Temperature Format below.</dd>
<dt><code>-HHumidity format string</code></dt>
<dd> See Humidity Format below.</dd></dl>
<h2>Temperature Format</h2>
<p> The temperature format can be either a numeric value, or a string. The numeric values select pre-configured output formats: </p>
<p>&nbsp;<wbr>1&nbsp;<wbr>=&nbsp;<wbr>One line per sensor, time, C, F&nbsp;<wbr>(default)&nbsp;<wbr><br />
&nbsp;<wbr>2&nbsp;<wbr>=&nbsp;<wbr>One line per sample, elapsed time, temperature in C<br />
&nbsp;<wbr>3&nbsp;<wbr>=&nbsp;<wbr>Same as&nbsp;<wbr>#2, except temperature is in F </p>
<p> #2 and #3 have the data seperated by tabs, suitable for import into a spreadsheet or other graphing software. </p>
<p> The format string uses strftime tokens plus 5 special ones for DigiTemp:</p>
<dl>
<dt><code>%s</code></dt>
<dd> for sensor #</dd>
<dt><code>%C</code></dt>
<dd> for centigrade</dd>
<dt><code>%F</code></dt>
<dd> for fahrenheit</dd>
<dt><code>%R</code></dt>
<dd> to output the hex serial number</dd>
<dt><code>%N</code></dt>
<dd> for seconds since Epoch.</dd></dl>
<p> The case of the token is important! The default format string is: &quot;%b %d %H:%M:%S Sensor %s C: %.2C F: %.2F&quot; which gives you an output of: May 24 21:25:43 Sensor 0 C: 23.66 F: 74.59 </p>
<p> The DS2438 sensor can be used for a variety of things. It includes a temperature sensor and A/D converter. DigiTemp defaults to using it as a humidity sensor. The raw voltages and currents can be displayed by passing the -A argument </p>
<p> When the -o2 or -o3 log options are used the attached DS2438&#8217;s temperatures will be output without the humidity. </p>
<h2>Counter Format String</h2>
<p> The counter format string is similar, adding these tokens:</p>
<dl>
<dt><code>%n</code></dt>
<dd> is the counter #, which depends on its position in the .digitemprc file</dd>
<dt><code>%C</code></dt>
<dd> is the count in decimal.</dd></dl>
<h2>Humidity Format String</h2>
<p> The Humidity format string is the same as the temperature format string with the addition of this format specifier:</p>
<dl>
<dt><code>%h</code></dt>
<dd> is the humidity in 0-100%</dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Jes&uacute;s Roncero &lt;jesus [at] roncero.org&gt;, for the Debian project (but may be used by others). Modifications by Brian C. Lane &lt;bcl [at] brianlane.com&gt;</p>
<h2>UPDATES</h2>
<p> DigiTemp updates can be found on the <a rel="nofollow" href="http://www.digitemp.com">http://www.digitemp.com</a> website. </p>
