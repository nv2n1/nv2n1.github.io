---
title: "rotctl(1)"
name: "rotctl"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rotctl/"
description: "rotctl – control antenna rotators"
---

<h2 class="name">NAME</h2>
<p> rotctl &#8211; control antenna rotators </p>
<h2>SYNOPSIS</h2>
<p> <code>rotctl</code> [<i>OPTION</i>]&#8230; [<i>COMMAND</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Control antenna rotators. <code>rotctl</code> accepts <i>commands</i> from the command line as well as in interactive mode if none are provided on the command line. </p>
<p> Keep in mind that <code>Hamlib</code> is BETA level software. While a lot of backend libraries lack complete rig support, the basic functions are usually well supported. The API may change without publicized notice, while an advancement of the minor version (e.g. 1.1.x to 1.2.x) indicates such a change. </p>
<p> Please report bugs and provide feedback at the e-mail address given in the REPORTING BUGS section. Patches and code enhancements are also welcome.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). </p>
<p> Here is s summary of the supported options:</p>
<dl>
<dt><code>-m, &#8211;model=id</code></p>
<dd> Select rotator model number. See model list (use &#8216;rotctl -l&#8217;). </p>
<p> NB: <code>rotctl</code> (or third party software) will use rig model 1901 when using <code>rpc.rotd</code> or rig model 2 for NET rotctl (rotctld).</p>
<dt><code>-r, &#8211;rot-file=device</code></p>
<dd> Use <i>device</i> as the file name of the port the rotator is connected. Often a serial port, but could be a USB to serial adapter or USB port device. Typically /dev/ttyS0, /dev/ttyS1, /dev/ttyUSB0, etc. on Linux or COM1, COM2, etc. on Win32. </p>
<p> Also used to specify the host and port to connect to a listening rotctld daemon on POSIX: </p>
<p> -r localhost:4533 </p>
<p> and on Win32: </p>
<p> -r 127.0.0.1:4533</p>
<dt><code>-s, &#8211;serial-speed=baud</code></p>
<dd> Set serial speed to <i>baud</i> rate. Uses maximum serial speed from rotator backend capabilities as default.</p>
<dt><code>-t, &#8211;send-cmd-term=char</code></p>
<dd> Change the termination <i>char</i> for text protocol when using the <i>send_cmd</i> command. The default value is &lt;CR&gt;. Non ASCII printable characters can be specified as an ASCII number, in hexadecimal format, prepended with 0x. You may pass an empty string for no termination char. The string -1 tells rotctl to switch to binary protocol. See the <i>send_cmd</i> command for further explanation.</p>
<dt><code>-L, &#8211;show-conf</code></p>
<dd> List all config parameters for the rotor defined with -m above.</p>
<dt><code>-C, &#8211;set-conf=parm=val[,parm=val]*</code></p>
<dd> Set config parameter. e.g. &#8211;set_conf=stop_bits=2 </p>
<p> Use -L option for a list.</p>
<dt><code>-u, &#8211;dump-caps</code></p>
<dd> Dump capabilities for the rotor defined with -m above and exit.</p>
<dt><code>-l, &#8211;list</code></p>
<dd> List all model numbers defined in <code>Hamlib</code> and exit. As of 1.2.15.1 the list is sorted by model number. </p>
<p> <code>N.B.</code> In Linux the list can be scrolled back using Shift-PageUp/ Shift-PageDown, or using the scrollbars of a virtual terminal in X or the cmd window in Windows. The output can be piped to &#8216;more&#8217; or &#8216;less&#8217;, e.g. &#8216;rotctl -l | more&#8217;.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Set verbose mode, cumulative (see DIAGNOSTICS below).</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of these options and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show version of <code>rotctl</code> and exit.</dl>
<p> <code>N.B.</code> Some options may not be implemented by a given backend and will return an error. This is most likely to occur with the <i>&#8211;set-conf</i> and <i>&#8211;show-conf</i> options. </p>
<p> Please note that the backend for the rotator to be controlled, or the rotator itself may not support some commands. In that case, the operation will fail with a <code>Hamlib</code> error code.</p>
<h2>COMMANDS</h2>
<p> Commands can be entered either as a single char, or as a long command name. Basically, the commands do not take a dash in front of them, as the options do. They may be typed in when in interactive mode or provided as argument(s) in command line interface mode. </p>
<p> Since most of the <code>Hamlib</code> operations have a <i>set</i> and a <i>get</i> method, an upper case letter will be used for <i>set</i> method whereas the corresponding lower case letter refers to the <i>get</i> method. Each operation also has a long name; in interactive mode, prepend a backslash to enter a long command name. </p>
<p> Example: Use &quot;\get_info&quot; to see the rotor&#8217;s info. </p>
<p> Please note that the backend for the rotator to be controlled, or the rotator itself may not support some commands. In that case, the operation will fail with a <code>Hamlib</code> error message. </p>
<p> A summary of commands is included below (In the case of &quot;set&quot; commands the quoted string is replaced by the value in the description. In the case of &quot;get&quot; commands the quoted string is the key name of the value returned.):</p>
<dl>
<dt><code>Q|q, exit rotctl</code></p>
<dd> Exit rotctl in interactive mode. </p>
<p> When rotctl is controlling the rotor directly, will close the rotor backend and port. When rotctl is connected to rotctld (rotor model 2), the TCP/IP connection to rotctld is closed and rotctld remains running, available for another TCP/IP network connection.</p>
<dt><code>P, set_pos &#8216;Azimuth&#8217; &#8216;Elevation&#8217;</code></p>
<dd> Set position: Azimuth and Elevation as double precision floating point values.</p>
<dt><code>p, get_pos</code></p>
<dd> Get position: &#8216;Azimuth&#8217; and &#8216;Elevation&#8217; as double precision floating point values.</p>
<dt><code>M, move &#8216;Direction&#8217; &#8216;Speed&#8217;</code></p>
<dd> Move the rotator in a specific direction at the given rate. </p>
<p> Values are integers where Direction is defined as 2 = Up, 4 = Down, 8 = Left, and 16 = Right. Speed is an integer between 1 and 100. Not all backends that implement the move command use the Speed value. At this time only the gs232a utilizes the Speed parameter.</p>
<dt><code>S, stop</code></p>
<dd> Stop the rotator.</p>
<dt><code>K, park</code></p>
<dd> Park the antenna.</p>
<dt><code>C, set_conf &#8216;Token&#8217; &#8216;Value&#8217;</code></p>
<dd> Set a configuration parameter. It is safe to give &quot;Token&quot; a value of &#8216;0&#8217; (zero). &quot;Value&quot; may be a string up to 20 characters.<br />
 See -L output</p>
<dt><code>R, reset &#8216;Reset&#8217;</code></p>
<dd> Reset the rotator. </p>
<p> Integer value of &#8216;1&#8217; for Reset All.</p>
<dt><code>_, get_info</code></p>
<dd> Get misc information on the rotator. </p>
<p> At the moment returns &#8216;Model Name&#8217;.</p>
<dt><code>w, send_cmd &#8216;Cmd&#8217;</code></p>
<dd> Send raw command string to the rotator.<br />
 &lt;CR&gt; (or send-cmd-term, see <i>-t</i> option) is appended automatically at the end of the command for text protocols. For binary protocols, enter values as ��</dl>
<p> <code>Locator Commands</code> </p>
<p> These commands offer conversions of Degrees Minutes Seconds to other formats, Maidenhead square locator conversions and distance and azimuth conversions.</p>
<dl>
<dt><code>L, lonlat2loc &#8216;Longitude&#8217; &#8216;Latitude&#8217; &#8216;Loc Len [2-12]&#8217;</code></p>
<dd> Returns the Maidenhead locator for the given &#8216;Longitude&#8217; and &#8216;Latitude&#8217;. </p>
<p> Both are floating point values. The precision of the returned square is controlled by &#8216;Loc Len&#8217; which should be an even numbered integer value between 2 and 12. </p>
<p> For example, &quot;+L -170.000000 -85.000000 12
&quot; returns &quot;Locator: AA55AA00AA00
&quot;.</p>
<dt><code>l, loc2lonlat &#8216;Locator&#8217;</code></p>
<dd> Returns &#8216;Longitude&#8217; and &#8216;Latitude&#8217; in decimal degrees at the approximate center of the requested grid square (despite the use of double precision variables internally, some rounding error occurs). West longitude is expressed as a negative value. South latitude is expressed as a negative value. Locator can be from 2 to 12 characters in length. </p>
<p> For example, &quot;+l AA55AA00AA00
&quot; returns &quot;Longitude: -169.999983
Latitude: -84.999991
&quot;.</p>
<dt><code>D, dms2dec &#8216;Degrees&#8217; &#8216;Minutes&#8217; &#8216;Seconds&#8217; &#8216;S/W&#8217;</code></p>
<dd> Returns &#8216;Dec Degrees&#8217;, a signed floating point value. </p>
<p> Degrees and Minutes are integer values and Seconds is a floating point value. S/W is a flag with &#8216;1&#8217; indicating South latitude or West longitude and &#8216;0&#8217; North or East (the flag is needed as computers don&#8217;t recognize a signed zero even though only the Degrees value only is typically signed in DMS notation).</p>
<dt><code>d, dec2dms &#8216;Dec Degrees&#8217;</code></p>
<dd> Returns &#8216;Degrees&#8217; &#8216;Minutes&#8217; &#8216;Seconds&#8217; &#8216;S/W&#8217;. </p>
<p> Values are as in dms2dec above.</p>
<dt><code>E, dmmm2dec &#8216;Degrees&#8217; &#8216;Dec Minutes&#8217; &#8216;S/W&#8217;</code></p>
<dd> Returns &#8216;Dec Degrees&#8217;, a signed floating point value. </p>
<p> Degrees is an integer value and Minutes is a floating point value. S/W is a flag with &#8216;1&#8217; indicating South latitude or West longitude and &#8216;0&#8217; North or East (the flag is needed as computers don&#8217;t recognize a signed zero even though only the Degrees value only is typically signed in DMS notation).</p>
<dt><code>e, dec2dmmm &#8216;Dec Deg&#8217;</code></p>
<dd> Returns &#8216;Degrees&#8217; &#8216;Minutes&#8217; &#8216;S/W&#8217;. </p>
<p> Values are as in dmmm2dec above.</p>
<dt><code>B, qrb &#8216;Lon 1&#8217; &#8216;Lat 1&#8217; &#8216;Lon 2&#8217; &#8216;Lat 2&#8217;</code></p>
<dd> Returns &#8216;Distance&#8217; &#8216;Azimuth&#8217; where Distance is in km and Azimuth is in degrees. </p>
<p> All Lon/Lat values are signed floating point numbers.</p>
<dt><code>A, a_sp2a_lp &#8216;Short Path Deg&#8217;</code></p>
<dd> Returns &#8216;Long Path Deg&#8217; or -RIG_EINVAL upon input error.. </p>
<p> Both are floating point values within the range 0.00 to 360.00.</p>
<dt><code>a, d_sp2d_lp &#8216;Short Path km&#8217;</code></p>
<dd> Returns &#8216;Long Path km&#8217;. </p>
<p> Both are floating point values.</dl>
<h2>EXAMPLES</h2>
<p> Start <code>rotctl</code> for RotorEZ using the first serial port on Linux: </p>
<p> $ rotctl -m 401 -r /dev/ttyS0 </p>
<p> Start <code>rotctl</code> for RotorEZ using COM2 on Win32: </p>
<p> C:\&gt; rotctl -m 401 -r COM2 </p>
<p> Start <code>rotctl</code> using <code>rpc.rotd</code> and querying the position: </p>
<p> $ rotctl -m 101 -r localhost \get_pos </p>
<p> Connect to a running <code>rotctld</code> with rotor model 2 (&quot;NET rotctl&quot;) on the local host and specifying the TCP port on POSIX: </p>
<p> $ rotctl -m 2 -r localhost:4533 </p>
<p> and on Win32: </p>
<p> C:\&gt; rotctl -m 2 -r 127.0.0.1:4533</p>
<h2>DIAGNOSTICS</h2>
<p> The <code>-v</code>, <code>&#8211;version</code> option allows different levels of diagnostics to be output to <code>stderr</code> and correspond to -v for BUG, -vv for ERR, -vvv for WARN, -vvvv for VERBOSE, or -vvvvv for TRACE. </p>
<p> A given verbose level is useful for providing needed debugging information to the email address below. For example, TRACE output shows all of the values sent to and received from the radio which is very useful for radio backend library development and may be requested by the developers.</p>
<h2>EXIT STATUS</h2>
<p> <code>rotctl</code> exits with:<br />
 0 if all operations completed normally;<br />
 1 if there was an invalid command line option or argument;<br />
 2 if an error was returned by <code>Hamlib</code>.</p>
<h2>BUGS</h2>
<p> This suspiciously empty section&#8230;</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;hamlib-developer [at] lists.sourceforge.net&gt;. </p>
<p> We are already aware of the bug in the previous section :-)</p>
<h2>AUTHOR</h2>
<p> Written by Stephane Fillod, Nate Bargmann, and the Hamlib Group </p>
<p> &lt;<a rel="nofollow" href="http://www.hamlib.org">http://www.hamlib.org</a>&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2010 Stephane Fillod<br />
 Copyright &#169; 2011-2012 Nate Bargmann<br />
 Copyright &#169; 2000-2010 the Hamlib Group </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-hamlib/">hamlib</a></code>(3), <code><a href="/docs/linux/man/8-rpc-rotd/">rpc.rotd</a></code>(8) <code><a href="/docs/linux/man/8-rotctld/">rotctld</a></code>(8) </p>
<h2>Index</h2>
