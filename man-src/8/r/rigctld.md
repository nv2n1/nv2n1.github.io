---
title: "rigctld(8)"
name: "rigctld"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rigctld/"
description: "rigctld – Hamlib TCP rig control daemon"
---

<p>rigctld &#8211; Hamlib TCP rig control daemon</p>
<h2>Synopsis</h2>
<p><code>rigctld</code> [<i>OPTION</i>]&#8230;</p>
<h2>Description</h2>
<p>The <code>rigctld</code> program is a NEW <code>Hamlib</code> rig control daemon ready for testing that handles client requests via TCP sockets. This allows multiple user programs to share one radio (this needs testing), except on Win32 where pthreads are not available. Multiple radios can be controlled on different TCP ports by use of multiple <code>rigctld</code> processes. The syntax of the commands are the same as <code>rigctl</code>. It is hoped that <code>rigctld</code> will be especially useful for client authors using languages such as Perl, Python, PHP, and others. </p>
<p> <code>rigctld</code> communicates to a client through a TCP socket using text commands shared with <code>rigctl</code>. The protocol is simple; commands are sent to <code>rigctld</code> on one line and <code>rigctld</code> responds to &quot;get&quot; commands with the requested values, one per line, when successful, otherwise, it responds with one line &quot;RPRT x&quot;, where x is a negative number indicating the error code. Commands that do not return values respond with the line &quot;RPRT x&quot;, where x is zero when successful, otherwise is a regative number indicating the error code. Each line is terminated with a newline &#8216;
&#8217; character. This protocol is primarily for use by the <i>NET rigctl</i> (rig model 2)backend. </p>
<p> A separate <code>Extended Response</code> protocol extends the above behavior by echoing the received command string as a header, any returned values as a key: value pair, and the &quot;RPRT x&quot; string as the end of response marker which includes the <code>Hamlib</code> success or failure value. See the <i>PROTOCOL</i> section for details. Consider using this protocol for clients that will interact with <code>rigctld</code> directly through a TCP socket. </p>
<p> Keep in mind that <code>Hamlib</code> is BETA level software. While a lot of backend libraries lack complete rig support, the basic functions are usually well supported. The API may change without publicized notice, while an advancement of the minor version (e.g. 1.1.x to 1.2.x) indicates such a change. </p>
<p> Please report bugs and provide feedback at the e-mail address given in the <i>REPORTING BUGS</i> section. Patches and code enhancements are also welcome.</p>
<h2>Options</h2>
<p>This program follows the usual GNU command line syntax, with long options starting with two dashes (&#8216;-&#8216;). </p>
<p> Here is a summary of the supported options:</p>
<dl>
<dt><code>-m, &#8211;model=id</code></p>
<dd>Select radio model number. See the -l, &#8211;list option below.</p>
<dt><code>-r, &#8211;rig-file=device</code></p>
<dd>Use <i>device</i> as the file name of the port the radio is connected. Often a serial port, but could be a USB to serial adapter or USB port device. Typically /dev/ttyS0, /dev/ttyS1, /dev/ttyUSB0, etc. on Linux or COM1, COM2, etc. on Win32.</p>
<dt><code>-p, &#8211;ptt-file=device</code></p>
<dd>Use <i>device</i> as the file name of the Push-To-Talk device using a device file as described above.</p>
<dt><code>-d, &#8211;dcd-file=device</code></p>
<dd>Use <i>device</i> as the file name of the Data Carrier Detect device using a device file as described above.</p>
<dt><code>-P, &#8211;ptt-type=type</code></p>
<dd>Use <i>type</i> of Push-To-Talk device. Supported types are RIG (CAT command), DTR, RTS, PARALLEL, NONE.</p>
<dt><code>-D, &#8211;dcd-type=type</code></p>
<dd>Use <i>type</i> of Data Carrier Detect device. Supported types are RIG (CAT command), DSR, CTS, CD, PARALLEL, NONE.</p>
<dt><code>-s, &#8211;serial-speed=baud</code></p>
<dd>Set serial speed to <i>baud</i> rate. Uses maximum serial speed from rig backend capabilities (set by -m above) as the default.</p>
<dt><code>-c, &#8211;civaddr=id</code></p>
<dd>Use <i>id</i> as the CI-V address to communicate with the rig. Only useful for Icom rigs. </p>
<p> <code>N.B.</code>: The <i>id</i> is in decimal notation, unless prefixed by <i>0x</i> for a hexadecimal value.</p>
<dt><code>-T, &#8211;listen-addr=IPADDR</code></p>
<dd>Use <i>IPADDR</i> as the listening IP address. The default is ANY. </p>
<p> N.B.: This option seems mandatory on Win32, eg: -T 127.0.0.1</p>
<dt><code>-t, &#8211;port=number</code></p>
<dd>Use <i>number</i> as the TCP listening port. The default is 4532. </p>
<p> <code>N.B.</code>: As <code>rotctld</code>&#8216;s default port is 4533, it is advisable to use even numbered ports for <code>rigctld</code>, e.g. 4532, 4534, 4536, etc. </p>
<p> N.B.: This option seems mandatory on Win32, eg: -t 4532</p>
<dt><code>-L, &#8211;show-conf</code></p>
<dd>List all config parameters for the radio defined with -m above.</p>
<dt><code>-C, &#8211;set-conf=parm=val[,parm=val]*</code></p>
<dd>Set config parameter. e.g. &#8211;set-conf=stop_bits=2 </p>
<p> Use -L option for a list.</p>
<dt><code>-l, &#8211;list</code></p>
<dd>List all model numbers defined in <code>Hamlib</code> and exit. As of 1.2.15.1 the list is sorted by model number. </p>
<p> <code>N.B.</code> In Linux the list can be scrolled back using Shift-PageUp/ Shift-PageDown, or using the scrollbars of a virtual terminal in X or the cmd window in Windows. The output can be piped to &#8216;more&#8217; or &#8216;less&#8217;, e.g. &#8216;rigctld -l | more&#8217;.</p>
<dt><code>-u, &#8211;dump-caps</code></p>
<dd>Dump capabilities for the radio defined with -m above and exit.</p>
<dt><code>-o, &#8211;vfo</code></p>
<dd>Set vfo mode, requiring an extra VFO argument in front of each appropriate command (except <i>\set_vfo</i>!). Otherwise, &#8216;currVFO&#8217; is assumed when this option is not set and an extra VFO argument is not used. See <i>
