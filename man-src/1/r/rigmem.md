---
title: "rigmem(1)"
name: "rigmem"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rigmem/"
description: "rigmem – backup and restore memory of radio transceivers and receivers"
---

<h2 class="name">NAME</h2>
<p> rigmem &#8211; backup and restore memory of radio transceivers and receivers </p>
<h2>SYNOPSIS</h2>
<p> <code>rigmem</code> [<i>OPTION</i>]&#8230; [<i>COMMAND</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Backup and restore memory of radio transceivers and receivers. <code>rigmem</code> accepts <i>commands</i> from the command line only. </p>
<p> Keep in mind that <code>Hamlib</code> is BETA level software. While a lot of backend libraries lack complete rig support, the basic functions are usually well supported. The API may change without publicized notice, while an advancement of the minor version (e.g. 1.1.x to 1.2.x) indicates such a change. </p>
<p> Please report bugs and provide feedback at the e-mail address given in the REPORTING BUGS section. Patches and code enhancements are also welcome.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). </p>
<p> Here is a summary of the supported options:</p>
<dl>
<dt><code>-m, &#8211;model=id</code></p>
<dd> Select radio model number. See model list (use &#8216;rigctl -l&#8217;).<br />
 NB: <code>rigmem</code> (or third party software) will use rig model 1901 when using <code>rpc.rigd</code>.</p>
<dt><code>-r, &#8211;rig-file=device</code></p>
<dd> Use <i>device</i> as the file name of the port the radio is connected. Often a serial port, but could be a USB to serial adapter. Typically /dev/ttyS0, /dev/ttyS1, /dev/ttyUSB0, etc.</p>
<dt><code>-s, &#8211;serial-speed=baud</code></p>
<dd> Set serial speed to <i>baud</i> rate. Uses maximum serial speed from rig backend capabilities as the default.</p>
<dt><code>-c, &#8211;civaddr=id</code></p>
<dd> Use <i>id</i> as the CI-V address to communicate with the rig. Only useful for Icom rigs.<br />
 NB: the <i>id</i> is in decimal notation, unless prefixed by <i>0x</i>, in which case it is hexadecimal.</p>
<dt><code>-C, &#8211;set-conf=parm=val[,parm=val]*</code></p>
<dd> Set config parameter. e.g. stop_bits=2<br />
 Use -L option of <code>rigctl</code> for a list.</p>
<dt><code>-x, &#8211;xml</code></p>
<dd> Use XML format instead of CSV, if libxml2 is available.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Set verbose mode, cumulative (see DIAGNOSTICS below).</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show a summary of these options and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show version of <code>rigmem</code> and exit.</dl>
<p> <code>NOTE!</code> Some options may not be implemented by a given backend and will return an error. This is most likely to occur with the <i>&#8211;set-conf</i> option.</p>
<h2>COMMANDS</h2>
<p> Backup and restore are supported for basic CSV file and XML format where available. </p>
<p> Please note that the backend for the radio to be controlled, or the radio itself may not support some commands. In that case, the operation will fail with a <code>Hamlib</code> error message. </p>
<p> Here is a summary of the supported commands:</p>
<dl>
<dt><code>save</code></p>
<dd> Save all the content of memory in a CSV (or XML) file given as an argument to the command.</p>
<dt><code>load</code></p>
<dd> Load the content into all the memory from a CSV (or XML) file given as an argument to the command.</p>
<dt><code>save_parm</code></p>
<dd> Save all the parameters of the radio in a CSV (or XML) file given as an argument to the command.</p>
<dt><code>load_parm</code></p>
<dd> Load the parameters of the radio from a CSV (or XML) file given as an argument to the command.</p>
<dt><code>clear</code></p>
<dd> This is a very <code>DANGEROUS</code> command, as it will completely clear out everything you have programmed in the memory of your radio. <code>ALL DATA WILL BE LOST</code>. Use at your own risk!</dl>
<h2>DIAGNOSTICS</h2>
<p> The <code>-v</code>, <code>&#8211;version</code> option allows different levels of diagnostics to be output to <code>stderr</code> and correspond to -v for BUG, -vv for ERR, -vvv for WARN, -vvvv for VERBOSE, or -vvvvv for TRACE. </p>
<p> A given verbose level is useful for providing needed debugging information to the email address below. For example, TRACE output shows all of the values sent to and received from the radio which is very useful for radio backend library development and may be requested by the developers.</p>
<h2>EXIT STATUS</h2>
<p> <code>rigmem</code> exits with:<br />
 0 if all operations completed normally;<br />
 1 if there was an invalid command line option or argument;<br />
 2 if an error was returned by <code>Hamlib</code>.<br />
 3 the <code>Hamlib</code> backend has no memory support implemented and/or<br />
&nbsp;<wbr>&nbsp;<wbr>the rig has no memory access available.</p>
<h2>BUGS</h2>
<p> This empty section&#8230;</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;hamlib-developer [at] lists.sourceforge.net&gt;.<br />
 We are already aware of the bug in the previous section :-)</p>
<h2>AUTHOR</h2>
<p> Written by Stephane Fillod and the Hamlib Group<br />
 &lt;<a rel="nofollow" href="http://www.hamlib.org">http://www.hamlib.org</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2009 Stephane Fillod and the Hamlib Group.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rigctl/">rigctl</a></code>(1), <code><a href="/docs/linux/man/3-hamlib/">hamlib</a></code>(3) </p>
<h2>Index</h2>
