---
title: "grig(1)"
name: "grig"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grig/"
description: "grig – graphical user interface for the Ham Radio Control Libraries (hamlib)"
---

<h2 class="name">NAME</h2>
<p> grig &#8211; graphical user interface for the Ham Radio Control Libraries (hamlib)</p>
<h2>SYNOPSIS</h2>
<p> <code>grig</code> [<i>OPTION</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> Grig is a simple Ham Radio control (CAT) program based on the Ham Radio Control Libraries. It is intended to be highly generic presenting the user to the same graphical user interface regardless of which radio is being controlled. </p>
<p> Grig does not store any radio configuration, instead it takes a number of command line options.</p>
<dl>
<dt><code>-m</code>, <code>&#8211;model</code>=<i>ID</i></p>
<dd> select radio model number; see <code>&#8211;list</code></p>
<dt><code>-r</code>, <code>&#8211;rig-file</code>=<i>DEVICE</i></p>
<dd> set device of the radio, eg. /dev/ttyS0</p>
<dt><code>-s</code>, <code>&#8211;speed</code>=<i>BAUD</i></p>
<dd> set transfer rate (serial port only)</p>
<dt><code>-c</code>, <code>&#8211;civ-addr</code>=<i>ID</i></p>
<dd> set CI-V address (decimal, ICOM only)</p>
<dt><code>-C</code>, <code>&#8211;set-conf</code>=<i>par=val[,par2=val2]</i></p>
<dd> set additiional configuration parameters</p>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>LEVEL</i></p>
<dd> set hamlib debug level (0..5)</p>
<dt><code>-D</code>, <code>&#8211;delay</code>=<i>VALUE</i></p>
<dd> set delay between commands in msec (see below)</p>
<dt><code>-n</code>, <code>&#8211;nothread</code></p>
<dd> use timeout calls instead of thread (see below)</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd> list supported radios and exit</p>
<dt><code>-p</code>, <code>&#8211;enable-ptt</code></p>
<dd> enable ptt control</p>
<dt><code>-P</code>, <code>&#8211;enable-pwr</code></p>
<dd> enable power status control</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show a brief help message and exit</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> show version information and exit</dl>
<p> <code>Example:</code> Start grig using YAESU FT-990 connected to the first serial port, using 4800 baud and debug level set to warning: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>grig -m 116 -r&nbsp;<wbr>/dev/ttyS0 -s 4800 -d 3 </p>
<p> or if you prefer the long options: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>grig &#8211;model=116 &#8211;rig-file=/dev/ttyS0 &#8211;speed=4800 &#8211;debug=3 </p>
<p> It is usually enough to specify the model ID and the DEVICE. </p>
<p> If you start grig without any options it will use the Dummy backend and set the debug level to 0 (RIG_DEBUG_NONE). If you do not specify the transfer rate for the serial port, the default serial speed will be used by the backend and even if you specify a value, it can be overridden by the backend. If you omit the radio device (port) grig will use <i>/dev/ttyS0</i> or <i>localhost</i> if the selected radio is RPC-rig. </p>
<h2>DEBUG LEVELS</h2>
<p> 0 No debug, keep quiet.<br />
 1 Serious bug.<br />
 2 Error case (e.g. protocol, memory allocation).<br />
 3 Warnings.<br />
 4 Verbose information.<br />
 5 Trace. </p>
<p> Grig has its own debug message handler, which will manage messages from hamlib too. The messages are printed to STDERR by default but they can be redirected to a file. In bash shell you would write something like: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>grig&nbsp;<wbr>[options]&nbsp;<wbr>2&gt;&nbsp;<wbr>grig.log </p>
<p> You can then use the Message Window in the View menu to view these messages. The debug messages printed by grig a formatted in a structured way with each line containing both time, source and level of the message. Each field is separated with ;; so you can also import the log file into a spread sheet for further analysis. </p>
<h2>FEATURES</h2>
<p> Grig 0.7.2 supports the most commonly used CAT command implemented by hamlib. These include frequency, mode, filter and various level settings. Please note that not all features have been thoroughly tested since I don&#8217;t have access to any modern high-end radios. Therefore, comments regarding success or failure in using grig will be highly appreciated. </p>
<h2>KNOWN BUGS AND LIMITATIONS</h2>
<dl>
<dt>Buffer Overflow in Radio</p>
<dd> By default, grig tries to execute rig commands as fast as possible in order to achieve an almost real-time remote control experience. This strategy has turned out to cause problems with some radios, probably because these radios acknowledge the reception of a command before executing them, whereby the next command will be sent before the previous one has terminated. To avoid any possible buffer overflow in these situations, one can try to experiment with the -D or &#8211;delay command line argument, which will put the specified delay in between each executed command. The default value is 10 milliseconds and the smallest possible value is 1 millisecond (if one specifies 0 millisecond on the command line, the default value will be<br />
&nbsp;<wbr>used). If you find a value which is better for your radio than the default value, please let us know about it.</p>
<dt>Daemon Never Starts on FreeBSD</p>
<dd> There have been reports on that the new, thread-based daemon process is never started on FreeBSD, while the old, timeout-based daemon worked fine. It is therefore possible to choose the two ways to run the daemon process. The default is the new thread based daemon, but if you use FreeBSD and nothing seems to work after start-up you can select the timout-based daemon with the -n or &#8211;nothread command line option.</p>
<dt>Connection Settings</p>
<dd> Once you have started grig you can not change the radio settings (model, device, speed). You will have to restart the program if you want to change any of these settings.</p>
<dt>Multiple Radios</p>
<dd> Grig can control only one radio at the time. There are, however, no problems in starting several instances of grig as long as they do not try to control the same radio. An exception to this is the RPC-rig backend in which case the rpc rig daemon will act as a server while grig or any other hamlib frontends will act as a clients.</p>
<dt>Power OFF State</p>
<dd> On some radios, grig does not cope very well with the power off state. It is yet not known whether this is a bug in the hamlib backend or in grig and we will definitely appreciate your input. The situation gets even more complicated due to the fact that different radios behave in a different ways when they are powered OFF; some of them will continue to respond to remote commands, while others will not. Even the same radio, like the FT-817, can behave differently depending on whether it is powered from internal batteries or external power supply. Grig tries to handle this mess by suspending all rig commands while in power OFF state. Only the power ON command will be sent to the rig. By default, the power status control is disabled and must explicitly be enabled using the -P or &#8211;enable-pwr command line switch.</p>
<dt>PTT Control</p>
<dd> Similar to the power state, the PTT has caused strange behaviour on some radios. Consequently, it has been disabled by default but can be enabled using the -p or &#8211;enable-ptt command line aguments. </p>
</dl>
<h2>AUTHOR</h2>
<p> Written by Alexandru Csete, OZ9AEC. </p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <code>&lt;groundstation-developer [at] lists.sourcforge.net&gt;</code>.<br />
 Bugs related to hamlib should be reported directly to the hamlib developers at <code>&lt;hamlib-developer [at] lists.sourceforge.net&gt;</code>. </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2006 Alexandru Csete.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rigctl/">rigctl</a></code>(1) </p>
<h2>Index</h2>
