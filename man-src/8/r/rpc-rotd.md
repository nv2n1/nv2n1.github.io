---
title: "rpc-rotd(8)"
name: "rpc-rotd"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rpc-rotd/"
description: "rotd – Hamlib rotator service daemon"
---

<p>rotd &#8211; Hamlib rotator service daemon</p>
<h2>Synopsis</h2>
<p><code>rpc.rotd</code> [<i>OPTION</i>]&#8230;</p>
<h2>Description</h2>
<p>The <code>rotd</code> program is a <code>Hamlib</code> rotator daemon that handles RPC client requests. This allows multiple user programs to share one rotator. At this time multiple rotator support is not available (help needed!). </p>
<p> Keep in mind that <code>Hamlib</code> is BETA level software. While a lot of backend libraries lack complete rig support, the basic functions are usually well supported. The API may change without publicized notice, while an advancement of the minor version (e.g. 1.1.x to 1.2.x) indicates such a change. </p>
<p> Please report bugs and provide feedback at the e-mail address given in the REPORTING BUGS section. Patches and code enhancements are also welcome.</p>
<h2>Options</h2>
<p>This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). </p>
<p> Here is a summary of the supported options:</p>
<dl>
<dt><code>-m, &#8211;model=id</code></p>
<dd>Select rotator model number. See model list (use &#8216;rotctl -l&#8217;).<br />
 NB: <code>rotctl</code> (or third party software) will use rotor model 101 when using <code>rotd</code>.</p>
<dt><code>-r, &#8211;rot-file=device</code></p>
<dd>Use <i>device</i> as the file name of the port the rotator is connected. Often a serial port, but could be a USB to serial adapter. Typically /dev/ttyS0, /dev/ttyS1, /dev/ttyUSB0, etc.</p>
<dt><code>-s, &#8211;serial-speed=baud</code></p>
<dd>Set serial speed to <i>baud</i> rate. Uses maximum serial speed from rotor backend as the default.</p>
<dt><code>-C, &#8211;set-conf=parm=val[,parm=val]*</code></p>
<dd>Set config parameter. e.g. stop_bits=2<br />
 Use -L option of <code>rotctl</code> for a list.</p>
<dt><code>-t, &#8211;prog=number</code></p>
<dd>Use <i>number</i> as the RPC program number. The default is 536873369.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Set verbose mode, cumulative (see DIAGNOSTICS below).</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Show summary of these options and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Show version of <code>rpc.rotd</code> and exit.</dl>
<p> Please note that the backend for the rotator to be controlled, or the rotator itself may not support some commands. In that case, the operation will fail with a <code>Hamlib</code> error code.</p>
<h2>Examples</h2>
<p>Start <code>rotd</code> as root for a RotorEZ using a USB to serial adapter and backgrounding: </p>
<p> # rpc.rotd -m 401 -r /dev/ttyUSB1 &amp; </p>
<p> Start <code>rotd</code> as root for a RotorEZ using COM1 while generating TRACE output: </p>
<p> # rpc.rotd -m 401 -r /dev/ttyS0 -vvvvv </p>
<p> Start <code>rotd</code> as root for a RotorEZ using a USB to serial adapter while setting baud rate and stop bits and backgrounding: </p>
<p> # rpc.rotd -m 401 -r /dev/ttyUSB1 -s 4800 -C stop_bits=2 &amp;</p>
<h2>Diagnostics</h2>
<p>The <code>-v</code>, <code>&#8211;version</code> option allows different levels of diagnostics to be output to <code>stderr</code> and correspond to -v for BUG, -vv for ERR, -vvv for WARN, -vvvv for VERBOSE, or -vvvvv for TRACE. </p>
<p> A given verbose level is useful for providing needed debugging information to the email address below. For example, TRACE output shows all of the values sent to and received from the rotator which is very useful for rotator backend library development and may be requested by the developers.</p>
<h2>Security</h2>
<p>No authentication whatsoever; could be done through domain restriction, though. Please ask if stronger security is needed.</p>
<h2>Bugs</h2>
<p>Does not support more than one communication device for multiple rotor control. (e.g. for Single Operator 2 Radio) Help needed!</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;hamlib-developer [at] lists.sourceforge.net&gt;.<br />
 We are already aware of the bug in the previous section :-)</p>
<h2>Authors</h2>
<p>Written by Stephane Fillod and the Hamlib Group<br />
 &lt;<a rel="nofollow" href="http://www.hamlib.org">http://www.hamlib.org</a>&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2000-2007 Stephane Fillod and the Hamlib Group. Contributed by Francois Retief &lt;fgretief [at] sun.ac.za&gt;.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-rotctl/">rotctl</a></code>(1), <code><a href="/docs/linux/man/3-hamlib/">hamlib</a></code>(3) </p>
