---

title: "rigswr(1)"
name: "rigswr"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rigswr/"
description: "rigswr – measure VSWR vs frequency using Hamlib."
---

<p> rigswr &#8211; measure VSWR vs frequency using <code>Hamlib</code>. </p>
<p> <code>rigswr</code> [<i>OPTION</i>]&#8230; start_freq stop_freq [freq_step]</p>
<p> <code>rigswr</code> uses <code>Hamlib</code> to control a rig to measure VSWR vs frequency:<br />
 It scans frequencies from <i>start_freq</i> to <i>stop_freq</i> with a step of <i>freq_step</i>. For each frequency, it transmits at 25% of total POWER during 0.5 second in CW mode and reads VSWR. </p>
<p> Frequency and the corresponding VSWR are then printed on <code>stdout</code>. </p>
<p> To work correctly, <code>rigswr</code> needs a rig that can measure VSWR and a <code>Hamlib</code> backend that supports reading VSWR from the rig. </p>
<p> Keep in mind that <code>Hamlib</code> is BETA level software. While a lot of backend libraries lack complete rig support, the basic functions are usually well supported. The API may change without publicized notice, while an advancement of the minor version (e.g. 1.1.x to 1.2.x) indicates such a change. </p>
<p> Please report bugs and provide feedback at the e-mail address given in the REPORTING BUGS section. Patches and code enhancements are also welcome.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). </p>
<p> Here is a summary of the supported options:</p>
<dl>
<dt><code>-m, &#8211;model=id</code></dt>
<dd> Select radio model number. See model list (use &#8216;rigctl -l&#8217;).<br />
 NB: <code>rigswr</code> (or third party software) will use rig model 1901 when using <code>rpc.rigd</code>.</dd>
<dt><code>-r, &#8211;rig-file=device</code></dt>
<dd> Use <i>device</i> as the file name of the port the radio is connected. Often a serial port, but could be a USB to serial adapter. Typically /dev/ttyS0, /dev/ttyS1, /dev/ttyUSB0, etc.</dd>
<dt><code>-s, &#8211;serial-speed=baud</code></dt>
<dd> Set serial speed to <i>baud</i> rate. Uses maximum serial speed from rig backend capabilities as the default.</dd>
<dt><code>-c, &#8211;civaddr=id</code></dt>
<dd> Use <i>id</i> as the CI-V address to communicate with the rig. Only useful for Icom rigs.<br />
 NB: the <i>id</i> is in decimal notation, unless prefixed by <i>0x</i>, in which case it is hexadecimal.</dd>
<dt><code>-p, &#8211;ptt-file=device</code></dt>
<dd> Use <i>device</i> as the file name of the Push-To-Talk device using a device file as described above.<br />
 This is only needed if the radio doesn&#8217;t have legacy PTT control.</dd>
<dt><code>-p, &#8211;ptt-type=type</code></dt>
<dd> Use <i>type</i> of Push-To-Talk device. Supported types are RIG, DTR, RTS, PARALLEL, NONE.<br />
 This is only needed if the radio doesn&#8217;t have legacy PTT control.</dd>
<dt><code>-C, &#8211;set-conf=parm=val[,parm=val]*</code></dt>
<dd> Set config parameter. e.g. stop_bits=2<br />
 Use -L option of <code>rigctl</code> for a list.</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> Set verbose mode, cumulative (see DIAGNOSTICS below).</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show summary of these options and exit.</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Show version of <code>rigswr</code> and exit.</dd></dl>
<p> <code>NOTE!</code> Some options may not be implemented by a given backend and will return an error. This is most likely to occur with the <i>&#8211;set-conf</i> option.</p>
<h2>EXAMPLE</h2>
<p> rigswr -m 209 -r /dev/ttyS1 14000000 14290000 50000 &gt; cswr </p>
<p> Scans frequencies between 14.000 MHz and 14.200 MHz with 50 kHz step on a TS-850 and records VSWR measurements in file cswr. </p>
<p> After completion, cswr file contains the following lines: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>14000000 1.50 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>14050000 1.31 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>14100000 1.22 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>14150000 1.07 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>14200000 1.07</p>
<dl>
<dt>Result could then be plotted with <code>gnuplot</code>:</dt>
<dd>
 gnuplot<br />
 set data style linespoints<br />
 set grid<br />
 plot &quot;cswr&quot;</dd></dl>
<h2>DIAGNOSTICS</h2>
<p> The <code>-v</code>, <code>&#8211;version</code> option allows different levels of diagnostics to be output to <code>stderr</code> and correspond to -v for BUG, -vv for ERR, -vvv for WARN, -vvvv for VERBOSE, or -vvvvv for TRACE. </p>
<p> A given verbose level is useful for providing needed debugging information to the email address below. For example, TRACE output shows all of the values sent to and received from the radio which is very useful for radio backend library development and may be requested by the developers.</p>
<h2>EXIT STATUS</h2>
<p> <code>rigswr</code> exits with:<br />
 0 if all operations completed normally;<br />
 1 if there was an invalid command line option or argument;<br />
 2 if an error was returned by <code>Hamlib</code>;<br />
 3 if the rig doesn&#8217;t have the required capabilities.</p>
<h2>BUGS</h2>
<p> Depending on keyer/QSK setup, transmissions in CW mode may not be modulated thus possibly giving a wrong result. Please report this situation if it happens.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;hamlib-developer [at] lists.sourceforge.net&gt;.<br />
 We are already aware of the bug in the previous section :-)</p>
<h2>AUTHORS</h2>
<p> Written by Thierry Leconte, Stephane Fillod, and the Hamlib Group<br />
 &lt;<a rel="nofollow" href="http://www.hamlib.org">http://www.hamlib.org</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2004-2009 Thierry Leconte, Stephane Fillod, and the Hamlib Group.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rigctl/">rigctl</a></code>(1), <code><a href="/docs/linux/man/1-gnuplot/">gnuplot</a></code>(1), <code>hamlib</code>(3) </p>
