---
title: "isdnlog(8)"
name: "isdnlog"
section: "8"
letter: "i"
url: "/docs/linux/man/8-isdnlog/"
description: "isdnlog – isdn log system (and more)"
---

<p>isdnlog &#8211; isdn log system (and more)</p>
<h2>Description</h2>
<p>Isdnlog gets information from your isdn card, decodes this information, and can do anything with it, such as logging, starting programs, and more. All options to isdnlog can be given as command line flags, or you can specify a file with options (recommended). </p>
<h2>Restriction</h2>
<p>Isdnlog only works with the HiSax isdn driver. Other cards with their own driver are not supported. Additionally you need to enable d-channel logging (you can use &quot;hisaxctrl &lt;DriverId&gt; 1 4&quot; to do that, e.g. &quot;hisaxctrl line0 1 4&quot;). Isdnlog can only log outgoing calls that originate from your isdn card, and incoming calls. To get information about outgoing calls from other isdn devices (e.g. telephones), you need a second Teles isdn card, with crossed lines. Such a card is not usable for communicating, but can log outgoing calls from any device (see dual option below).</p>
<h2>General Options</h2>
<dl>
<dt><code>-V</code></p>
<dd>show version information and exit. </p>
<dt><code>-f</code><i>FILE</i></p>
<dd>read options from the config file <i>FILE</i>. This file is also called the parameter file of isdnlog. The first line should be &quot;[options]&quot;. You may use blank lines and comments (starting with a #). All config files for isdnlog have the format described in <a href="/docs/linux/man/5-isdn-conf/">isdn.conf</a>(5). Debug options must be given on the command line, they cannot be stored in a file. </p>
<dt><code>/dev/DEVICE</code></p>
<dd>isdnlog will read from this device and from /dev/isdninfo. You should give /dev/isdnctrl0 for the first isdn card (or /dev/isdnctrl2 for the second). </p>
<p> Isdnlog has a replay mode for debugging, where you can simulate previous recorded events. In that case use &quot;-&quot; instead of a device. </p>
<dt><code>-A</code><i>x</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>amt=value</code></p>
<dd>Set digits necessary to get an outside line, when connected through a PABX.<br />
 You can give several codes padded with a &quot;:&quot; (e.g. -A0:80:81:82). </p>
<dd>(There is no commandline option for this.) Overwrite area code from isdn.conf. A machine connected to subscriber lines with different area codes and thus several isdnlogs running requires this non global setting. </p>
<dt><code>-B</code><i>vbn</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>vbn=value</code></p>
<dd>Set the provider preselection to the given value. More prefixes may be separated<br />
 by a &quot;:&quot;.<br />
 Values are e.g. &quot;010&quot; for DE, &quot;10&quot; for AT, &quot;16:17&quot; for NL, &quot;9&quot; for FR. </p>
<dt><code>-R</code><i>prefix</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>preselected=value</code></p>
<dd>Set the preselected (i.e the provider chosen, if no prefix is dialed)<br />
 provider to value. Value should be without <i>vbn</i>. </p>
<dt><code>skipProv=</code><i>skiplist</i></p>
<dd>(There is no commandline option for this.) Ignore certain providers from the rate-file. The format of <i>skiplist</i> is the same as for Q: tags in rate.conf and described in <a href="/docs/linux/man/5-rate-conf/">rate.conf</a>(5). </p>
<dt><code>-0</code><i>x:y</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>trim=value[:value]</code></p>
<dd>Suppress leading digits. If isdnlog is connected through a PABX, it is<br />
 sometimes not possible to let isdnlog distinguish between a national and an international call, even with help of the <code>-A</code> option.<br />
 This option requires two values separated with &quot;:&quot; as an argument. These values tell isdnlog how many leading digits to remove from incoming and outgoing calls respectively. If only one value is given, it is used for both incoming and outgoing calls.<br />
 Don&#8217;t use this in combination with the <code>-A</code> option! This will confuse the system (and possibly you). </p>
<p> Example: a PABX in Germany shows the number of an incoming call from Hamburg as &quot;00040&#8230;&quot;. When calling out to Hamburg, it shows the number as &quot;0040&#8230;&quot;. This means that on incoming calls, three zeroes must be removed, and on outgoing calls two zeroes must be removed (the number must be normalized to be without any leading zeroes in the case of a national number; international numbers must have one leading zero). So, in this case, the option <code>-03:2</code> would be correct. </p>
<dt><code>-i</code><i>x</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>internS0=value</code></p>
<dd>Telephone numbers shorter then<br />
 <i>value</i> are considered to be internal numbers on your PABX. </p>
<dt><code>-o<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>other={yes|no}</code></p>
<dd>Normally &quot;causes&quot; (e.g. &quot;non-selected user clearing&quot;) for other connected<br />
 ISDN devices are not displayed, only those which are related to the connection will be shown. With this option the causes for the other devices are also displayed. </p>
<dt><code>-Hx watchdog</code></p>
<dd>
<dt><code>-N use new config</code></p>
<dd>
<dt><code>-Q sqldump</code></p>
<dd>
<dt><code>-a any</code></p>
<dd>
<dt><code>-u</code><i>x</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ignoreRR=value</code></p>
<dd>Ignore &quot;housekeeping&quot; frames.<br />
 <i>x</i> may be 1 (ignore RR=Receiver ready) or 2 (ignore EMP=Euracom Management Protokoll) frames. </p>
<dt><code>-U</code><i>x[:y]</i><code><tt>&nbsp;<wbr></tt>ignoreCOLP=value[:value]</code></p>
<dd>Ignore COLP/CLIP frames when value is 1 or greater.<br />
 Value 0 is default, and tells isdnlog to not ignore COLP/CLIP frames. With value 2 the ignored COLP/CLIP number is displayed.<br />
 The first value applies to COLP the second to CLIP. If only one value is given, it applies to COLP and CLIP.<br />
 Sometimes the COLP number is a number in a different areacode to the number that was dialled, and then the cost calculation would be wrong. </p>
<dd>(There is no commandline option for this.) A PABX may cause numerous messages like &quot;Unexpected discriminator 0x47 &#8212; ignored!&quot; resulting from protocol discriminator values in layer 3 not known to isdnlog. Set ignoreUPD to yes to suppress this messages. </p>
<dt><code>-2</code><i>x</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>dual=value</code></p>
<dd>Enable dual mode. You need this if you have a second isdn card attached with<br />
 crossed lines so it can listen to what other isdn devices like telephones are doing. With <i>x</i>=2 you can increase the debug output &#8211; every single digit will be displayed. </p>
<p> Some setups may require workarounds for reliable logging. These workarounds are enabled by addition of the following numbers to the dual value. They are intended for the dualmode but may also be useful without. In this case, specify only the sum of the following numbers without 1 or 2 for the dual mode. </p>
<dl>
<dd>
<dl>
<dt>0x100</p>
<dd>Enable this when the destination number of an outgoing call contains the number of the previous call, e.g. calling 222 after calling 111 before results in 111222 for the second call. </p>
<p> This may also help in situations where an unanswered incoming call causes incorrect logging of the following outgoing call. </p>
<dt>0x200</p>
<dd>Enable this when outgoing calls are logged without a source number (own MSN). </p>
<dt>0x400</p>
<dd>Enable this when unanswered incoming calls are logged multiple times (revealed by isdnrep -E).</dl>
</dl>
<dt><code>-1</code></p>
<dd>A HFC-based card is used for echo mode. Enable echo mode for the HFC card with<br />
 <i>hisaxctrl id 10 1</i><br />
 <i>hisaxctrl id 12 1</i> </p>
</dl>
<h2>Debug Module</h2>
<dl>
<dt><code>-r</code></p>
<dd>Replay a debug file (e.g. /tmp/isdnctrl0) to find bugs. With this flag you should give a filename with the debug information instead of a device. It will also work with files not created by isdnlog (e.g. &quot;cat /dev/isdnctrl0&quot;). </p>
<dt><code>-n<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>newline={yes|no}</code></p>
<dd>Display throughput messages on the same line (only useful with logging to<br />
 stderr or a console device). </p>
<dt><code>-W</code><i>X</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>width=value</p>
<dd>Limit all messages to X characters per line.</p>
<dt><code>-v</code><i>X</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>log=X</p>
<dd>Isdnlog can copy all information to /tmp/DEVICE (e.g. /tmp/isdnctrl0 if<br />
 you started isdnlog with /dev/isdnctrl0). Choose what debugging you want from the following list, add the corresponding numbers together and use that for X: </p>
<dl>
<dd>
<dl>
<dt>1</p>
<dd>copy all &quot;HEX:&quot; lines from the hisax isdn device driver.</p>
<dt>2</p>
<dd>copy /dev/isdnctrl output (or whatever device you specified).</p>
<dt>4</p>
<dd>copy /dev/isdninfo output</p>
<dt>8</p>
<dd>copy transfer values (&quot;ibyte&quot;,&quot;obyte&quot;). </p>
<p> Isdnlog will close and reopen this file after a &quot;kill -HUP&quot;.</dl>
</dl>
<dt><code>-s<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>flush={yes|no}</code></p>
<dd>Isdnlog will flush the debug file /tmp/DEVICE (e.g. /tmp/isdnctrl0) after<br />
 each write access. </p>
<dt><code>-P<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>pipe={yes|no}</code></p>
<dd>Copy the debug information to stdout. This way you can run isdnlog as the<br />
 source of a pipe like &quot;isdnlog -P /dev/isdnctrl0 |prog &#8230; &quot;. </p>
<dt><code>-D<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>daemon={yes|no}</code></p>
<dd>Start isdnlog as daemon: it will fork into the background, and use syslog<br />
 as the default logging method (if you did not specify -m). </p>
<dt><code>-T</code></p>
<dd>Trace mode: isdnlog will wait for a key after processing a line from /dev/isdnctrl0 (or whatever device you specified). </p>
<dt><code>-K</code></p>
<dd>Print for every pressed key the thruput. Can not used together with option -d. </p>
<dt><code>-b</code></p>
<dd>If you are using a bilingual network terminator (NT), you must give this flag, or isdnlog will show the own MSN&#8217;s incorrectly. </p>
</dl>
<h2>Number Rewrite Module</h2>
<p>You can define aliases for telephone numbers (see <a href="/docs/linux/man/5-callerid-conf/">callerid.conf</a>(5) and <a href="/docs/linux/man/5-isdn-conf/">isdn.conf</a>(5) for more information). Isdnlog will compare all numbers to the list of aliases, and when a match is found, the alias is displayed instead of the number.</p>
<h2>Log Module</h2>
<p>Isdnlog can log information via syslog, to stdout, and send information to x11 clients. Calculate a code from these numbers by adding them, and activate logging with -s, -m or -x. You can use normal numbers or hex numbers. Default is stderr mode -m, unless daemon mode is enabled; then it&#8217;s syslog mode -l. </p>
<dl>
<dt>0x1</p>
<dd>Errors </p>
<dt>0x2</p>
<dd>Warnings </p>
<dt>0x4</p>
<dd>Notice </p>
<dt>0x8</p>
<dd>Log messages to /tmp/DEVICE (e.g. /tmp/isdnctrl0 if isdnlog is started with /dev/isdnctrl0) </p>
<dt>0x10</p>
<dd>Show telephone numbers immediately. </p>
<dt>0x20</p>
<dd>Show charge int and telephone costs with every charge signal (in Germany, and perhaps other countries, you have to pay to get these signals). </p>
<dt>0x40</p>
<dd>Show connect messages. </p>
<dt>0x80</p>
<dd>Show hang up messages. </p>
<dt>0x100</p>
<dd>Show cause message on hang up. </p>
<dt>0x200</p>
<dd>Show time messages. </p>
<dt>0x400</p>
<dd>Show throughput in bytes (every -wX seconds). </p>
<dt>0x800</p>
<dd>Show state of B-channels (use with -M monitor). </p>
<dt>0x1000</p>
<dd>Show service indicator.<br />
 You should log at least 0x7 (errors, warnings, notice) messages. </p>
<dt>0x2000</p>
<dd>Log estimated time till next charge signal. </p>
<dt>0x4000</p>
<dd>Show chargemax. </p>
<dt>0x8000</p>
<dd>Enable <i>core</i> file on SIGSEGV. </p>
<dt>0x10000 &#8230; 0x800000, show more diagnostic and debug messages.</p>
<dd>
<dt><code>-m</code><i>X</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>stdout=value</code></p>
<dd>Log to stderr.</p>
<dt><code>-O</code><i>X</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>outfile=path</code></p>
<dd>Log to file <i>X</i> instead of stderr. Isdnlog will close this device when it<br />
 gets a signal -SIGHUP (-1). Only valid with -m option.<br />
 If the name starts with a &quot;+&quot;, new data will be appended to the existing file. Default behaviour is to truncate the file when isdnlog opens it. </p>
<dt><code>-C </code><i>X</i><code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>console=path</code></p>
<dd>Log to console <i>X</i> instead of stderr. You can use -O and -C together,<br />
 so that isdnlog copies output to both. Specify a full pathname. Beware: you must put a space between -C and X ! </p>
<dt><code>-M<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>monitor={yes|no}</code></p>
<dd>With this flag, isdnlog will generate output for monitor programs like<br />
 imon, imontty or isdnmon. You must also give -m with 0x800 enabled. </p>
<dt><code>-l</code><i>X</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>syslog=value</code></p>
<dd>Log to syslog. <i>X</i> is the log code. You can log to syslog and to stdout at<br />
 the same time. </p>
<dt><code>-x</code><i>X</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>xisdn=value</code></p>
<dd>Pass information to x11 client. X is the log code. You can pass<br />
 information to x11 clients and log to syslog and/or stdout at the same time. </p>
<dt><code>-p</code><i>PORT</i><code> port=value</code></p>
<dd>Pass information to x11 client on this <i>PORT</i>. </p>
<dt><code>-c</code><i>X</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>calls=value</code></p>
<dd>Only with -x<i>X</i> : save the last <i>X</i> calls and pass this information to an<br />
 x11 client. Default value is 100. </p>
<dt><code>-L</code><i>X</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>xlog=value</code></p>
<dd>Only with -x<i>X</i> : save the last <i>X</i> messages and pass this information to an<br />
 x11 client. Default value is 500. </p>
<dt><code>-w</code><i>X</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>thruput=value</code></p>
<dd>If you enabled throughput logging (0x400), isdnlog will log the throughput<br />
 every <i>X</i> seconds. </p>
<dt><code>-I</code><i>x:y</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ciinterval=value[:value]</code></p>
<dd>Interval for printing of charge messages (0x20).</p>
<p> The first value is the interval for the calculated CI, the second value for the EH (AOC-D) messages. If only one value is given, both intervals are set to this value. </p>
</dl>
<h2>Lcr</h2>
<dl>
<dt><code>-d</code><i>x</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>abclcr=value</code></p>
<dd>Value is a bitmap:</p>
<p> 0 &#8230; off<br />
 1 &#8230; calls to different area / country<br />
 2 &#8230; local calls too<br />
 4 &#8230; special numbers e.g. ISP<br />
 This needs a kernel patch to work. If the kernel patch is not found a simulation is done.<br />
 Note: depending on your telephone provider local area calls may or may not be routed to alternate providers. For changing the ISP a script is called. s. next option &#8216;providerchange&#8217; </p>
<dd>(There is no commandline option for this.) This script is called with 3 parameters, the new provider number (from rate-CC.dat), the number, which would be dialed, and the servicename. The script should adjust routing, name resolution and so on to connect to the ISP. If the script returns non zero, LCR will not be done. </p>
</dl>
<h2>Time Module</h2>
<dl>
<dt><code>-t</code><i>X</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>time={0|1|2}</code></p>
<dd>Isdnlog will set your local system time to the time transmitted by your<br />
 isdn service provider: -t1 = once, -t2 = every time. </p>
</dl>
<h2>Chargehup Module</h2>
<dl>
<dt><code>-h</code><i>X</i><code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>hangup=value</code></p>
<dd>The isdn kernel system has a chargehup system, so it will hang up a few<br />
 seconds before the next charge signal. If you don&#8217;t get a charge signal from your phone company, isdnlog can emulate it. </p>
<p> On every outgoing connection, isdnlog will calculate the charge time from day of week, time of day and the distance zone of the connection. </p>
<p> The kernel needs to know how long the charge time is, and how many seconds before the next charge signal it should hang up. You have to set the second parameter with X in the form number:number (hang up seconds before next charge signal for charge times greater than or equal to 20 seconds : for charge times of less than 20 seconds). </p>
<p> With this information, isdnlog will call &quot;isdnctrl chargeint &lt;device&gt; &lt;charge time&gt;&quot; and &quot;isdnctrl huptimeout &lt;device&gt; &lt;seconds before charge signal&gt;&quot; (it actually communicates directly with isdn, without calling isdnctrl, but this would have the same effect). </p>
<p> You should run isdnlog with -t1 or better with -t2, so isdnlog sets the local time in sync with telephone switching office. </p>
<p> If there is a third number in value, this is the minimum connection time for providers charging a basic rate per connection.<br />
 e.g. hangup 3:5:60 </p>
</dl>
<h2>Start Module</h2>
<p>isdnlog can react on any event and start programs. This feature is disabled unless you activate it with: </p>
<dl>
<dt><code>-S<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>start={yes|no}</code></p>
<dd>active &quot;START&quot; feature. Please read <a href="/docs/linux/man/5-callerid-conf/">callerid.conf</a>(5) for more<br />
 information. </p>
<dd>(There is no commandline option for this.) If set to yes, isdnlog will close all unnecessarily opened file descriptors before a &quot;START&quot; program is executed. This closing will also take place at isdnlog&#8217;s restart after SIGHUP. Default is no. </p>
</dl>
<h2>Connection Log Module</h2>
<p>isdnlog will log all connections in /var/log/isdn.log. isdnrep can parse this file and calculate costs.</p>
<h2>Several Isdn Cards</h2>
<p>If you have more than one isdn card, you need to run one isdnlog for each card. And every process must have a different name, so you should create a symbolic link isdnlog1 -&gt; isdnlog, and start isdnlog1 for the second card.</p>
<h2>Unloading Kernel Modules</h2>
<p>You cannot unload isdn kernel modules while an isdn device is in use, e.g. a PPP interface is defined or isdnlog is running. Look at /var/run for a file isdnlog.DEVICE.pid with the process id of isdnlog, and kill that. After that you should be able to unload your isdn kernel modules.</p>
<h2>Files</h2>
<dl>
<dt><code>/dev/DEVICE</code></p>
<dd>isdnlog requires a device as a parameter to read from (e.g. /dev/isdnctrl0 for the 1st isdn card). </p>
<dt><code>/tmp/DEVICE</code></p>
<dd>isdnlog can copy everything it reads to this file as debug information (e.g. /tmp/isdnctrl0 if you started isdnlog with /dev/isdnctrl0). </p>
<dt><code>/var/run/isdnlog.DEVICE.pid</code></p>
<dd>isdnlog creates this file with its process id. Useful to see if isdnlog is running. </p>
<dt><code>/var/lock/LCK..DEVICE</code></p>
<dd>isdnlog creates a lock file for the device, so no other processes will access that device. </p>
<dt><code>/etc/isdn/isdn.conf</code></p>
<dd>isdnlog config file. Options to isdnlog can be given on the command line, can be stored in this file in [options] (with command line option -f/etc/isdn/isdn.conf), or in a different config file, but isdnlog will look at this file for sections [global] [variables] [isdnlog]. </p>
</dl>
<h2>Signals</h2>
<dl>
<dt><code>SIGHUP (-1)</code></p>
<dd>On SIGHUP isdnlog restarts, and does therefore reread it&#8217;s config files. </p>
<dt><code>SIGINT (-2), SIGTERM (-15), SIGQUIT (-3)</code></p>
<dd>Isdnlog quits gracefully on receiving these termination signals. </p>
<dt><code>SIGSEGV (-11)</code></p>
<dd>If the log level contains 0x8000 (and your ulimits permit this) isdnlog will generate a <i>core</i> file before terminating. </p>
</dl>
<h2>Example</h2>
<p>I start isdnlog with &quot;isdnlog -f/etc/isdn/isdn.conf /dev/isdnctrl0&quot;. This file contains a [options] section: </p>
<pre>[options]
#newline=no # show all throughput messages in one line.
#width=80 # limit log messages to 80 characters per line
#amt=0:80:81 # digits to get a line through your PABX
log=15 # maximum debug mode
flush=no # flush logfile after every write
pipe=no # pipe log messages to stderr
daemon=yes # run isdnlog as daemon
stdout=0x1ff7 # stderr logging level
outfile=+/var/log/isdn.log # log to file
#console= # log to a console
monitor=yes # emulate output for imon/imontty/...
syslog=0x1ff7 # syslog logging level
#xisdn=0x07ff # x11 output level
#calls= # store call information for x11 client
#xlog= # store messages for x11 client
thruput=60 # if throughput logging is enabled: log every X seconds
time=2 # set time: 0 = never; 1 = once; 2 = every time
#hangup= # simulate charge signals
start=yes # enable starting programs</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-isdnconf/">isdnconf</a>(1) <a href="/docs/linux/man/5-isdn-conf/">isdn.conf</a>(5) <a href="/docs/linux/man/5-callerid-conf/">callerid.conf</a>(5)</code><br />
 <code><a href="/docs/linux/man/5-rate-files/">rate-files</a>(5) <a href="/docs/linux/man/5-rate-conf/">rate.conf</a>(5)</code><br />
 <code><a href="/docs/linux/man/5-isdnlog/">isdnlog</a>(5) <a href="/docs/linux/man/1-isdnrep/">isdnrep</a>(1) <a href="/docs/linux/man/1-isdnrate/">isdnrate</a>(1)</code> </p>
<h2>Author</h2>
<p>This manual page was written by Andreas Jellinghaus &lt;aj [at] dungeon.inka.de&gt;, for Debian GNU/Linux and isdn4linux, updated by Leopold Toetsch &lt;lt [at] toetsch.at&gt;.</p>
