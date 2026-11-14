---
title: "rotctld(8)"
name: "rotctld"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rotctld/"
description: "rotctld – Hamlib TCP rotator control daemon"
---

<p>rotctld &#8211; Hamlib TCP rotator control daemon</p>
<h2>Synopsis</h2>
<p><code>rotctld</code> [<i>OPTION</i>]&#8230;</p>
<h2>Description</h2>
<p>The <code>rotctld</code> program is an NEW <code>Hamlib</code> rotator control daemon ready for testing that handles client requests via TCP sockets. This allows multiple user programs to share one rotator (this needs testing), except on Win32 where pthreads are not available. Multiple rotators can be controlled on different TCP ports by use of multiple <code>rotctld</code> processes. The syntax of the commands are the same as <code>rotctl</code>. It is hoped that <code>rotctld</code> will be especially useful for client authors using languages such as Perl, Python, PHP, and others. </p>
<p> <code>rotctld</code> communicates to a client through a TCP socket using text commands shared with <code>rotctl</code>. The protocol is simple, commands are sent to <code>rotctld</code> on one line and <code>rotctld</code> responds to &quot;get&quot; commands with the requested values, one per line, when successful, otherwise, it responds with one line &quot;RPRT x&quot;, where x is a negative number indicating the error code. Commands that do not return values respond with the line &quot;RPRT x&quot;, where x is zero when successful, otherwise is a regative number indicating the error code. Each line is terminated with a newline &#8216;
&#8217; character. This protocol is primarily for use by the <i>NET rotctl</i> (rot model 2) backend. </p>
<p> A separate <code>Extended Response</code> protocol extends the above behavior by echoing the received command string as a header, any returned values as a key: value pair, and the &quot;RPRT x&quot; string as the end of response marker which includes the <code>Hamlib</code> success or failure value. See the <i>PROTOCOL</i> section for details. Consider using this protocol for clients that will interact with <code>rotctld</code> directly through a TCP socket. </p>
<p> Keep in mind that <code>Hamlib</code> is BETA level software. While a lot of backend libraries lack complete rotator support, the basic functions are usually well supported. The API may change without publicized notice, while an advancement of the minor version (e.g. 1.1.x to 1.2.x) indicates such a change. </p>
<p> Please report bugs and provide feedback at the e-mail address given in the REPORTING BUGS section. Patches and code enhancements are also welcome.</p>
<h2>Options</h2>
<p>This program follows the usual GNU command line syntax, with long options starting with two dashes (&#8216;-&#8216;). </p>
<p> Here is a summary of the supported options:</p>
<dl>
<dt><code>-m, &#8211;model=id</code></p>
<dd>Select rotator model number. See -l, &quot;list&quot; option below.</p>
<dt><code>-r, &#8211;rot-file=device</code></p>
<dd>Use <i>device</i> as the file name of the port the rotator is connected. Often a serial port, but could be a USB to serial adapter or USB port device. Typically /dev/ttyS0, /dev/ttyS1, /dev/ttyUSB0, etc. on Linux or COM1, COM2, etc. on Win32.</p>
<dt><code>-s, &#8211;serial-speed=baud</code></p>
<dd>Set serial speed to <i>baud</i> rate. Uses maximum serial speed from rotor backend capabilities (set by -m above) as the default.</p>
<dt><code>-T, &#8211;listen-addr=IPADDR</code></p>
<dd>Use <i>IPADDR</i> as the listening IP address. The default is ANY. </p>
<p> N.B.: This option seems mandatory on Win32, eg: -T 127.0.0.1</p>
<dt><code>-t, &#8211;port=number</code></p>
<dd>Use <i>number</i> as the TCP listening port. The default is 4533. </p>
<p> <code>N.B.</code>: As <code>rigctld</code>&#8216;s default port is 4532, it is advisable to use odd numbered ports for <code>rotctld</code>, e.g. 4533, 4535, 4537, etc. </p>
<p> N.B.: This option seems mandatory on Win32, eg: -t 4533</p>
<dt><code>-L, &#8211;show-conf</code></p>
<dd>List all config parameters for the rotator defined with -m above.</p>
<dt><code>-C, &#8211;set-conf=parm=val[,parm=val]*</code></p>
<dd>Set config parameter. e.g. &#8211;set-conf=stop_bits=2 </p>
<p> Use -L option for a list.</p>
<dt><code>-l, &#8211;list</code></p>
<dd>List all model numbers defined in <code>Hamlib</code> and exit. As of 1.2.15.1 the list is sorted by model number. </p>
<p> <code>N.B.</code> In Linux the list can be scrolled back using Shift-PageUp/ Shift-PageDown, or using the scrollbars of a virtual terminal in X or the cmd window in Windows. The output can be piped to &#8216;more&#8217; or &#8216;less&#8217;, e.g. &#8216;rotctld -l | more&#8217;.</p>
<dt><code>-u, &#8211;dump-caps</code></p>
<dd>Dump capabilities for the radio defined with -m above and exit.</p>
<dt><code>-e, &#8211;end-marker</code></p>
<dd>Use END marker in rotctld protocol. </p>
<p> N.B.: This option should be considered obsolete. Please consider using the Extended Response protocol instead (see <i>PROTOCOL</i> below). This option will be removed in a future Hamlib release.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Set verbose mode, cumulative (see DIAGNOSTICS below).</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Show a summary of these options and exit.</p>
<dt><code>-V, &#8211;version</code></p>
<dd>Show the version of <code>rotctld</code> and exit.</dl>
<p> <code>N.B.</code> Some options may not be implemented by a given backend and will return an error. This is most likely to occur with the <i>&#8211;set-conf</i> and <i>&#8211;show-conf</i> options. </p>
<p> Please note that the backend for the rotator to be controlled, or the rotator itself may not support some commands. In that case, the operation will fail with a <code>Hamlib</code> error code.</p>
<h2>Commands</h2>
<p>Commands can be sent over the TCP socket either as a single char, or as a long command name plus the value(s) space separated on one &#8216;
&#8217; terminated line. See <i>PROTOCOL</i>. </p>
<p> Since most of the <code>Hamlib</code> operations have a <i>set</i> and a <i>get</i> method, an upper case letter will be used for <i>set</i> methods whereas the corresponding lower case letter refers to the <i>get</i> method. Each operation also has a long name; prepend a backslash to send a long command name. </p>
<p> Example (Perl): `print $socket &quot;\dump_caps
&quot;;&#8217; to see what the rotor&#8217;s backend can do (NOTE: In Perl and many other languages a &#8216;\&#8217; will need to be escaped with a preceding &#8216;\&#8217; so that even though two backslash characters appear in the code, only one will be passed to <code>rotctld</code>. This is a possible bug, beware!). </p>
<p> Please note that the backend for the rotator to be controlled, or the rotator itself may not support some commands. In that case, the operation will fail with a <code>Hamlib</code> error message. </p>
<p> Here is a summary of the supported commands (In the case of &quot;set&quot; commands the quoted string is replaced by the value in the description. In the case of &quot;get&quot; commands the quoted string is the key name of the value returned.):</p>
<dl>
<dt><code>P, set_pos &#8216;Azimuth&#8217; &#8216;Elevation&#8217;</code></p>
<dd>Set position: Azimuth and Elevation as double precision floating point values.</p>
<dt><code>p, get_pos</code></p>
<dd>Get position: &#8216;Azimuth&#8217; and &#8216;Elevation&#8217; as double precision floating point values.</p>
<dt><code>M, move &#8216;Direction&#8217; &#8216;Speed&#8217;</code></p>
<dd>Move the rotator in a specific direction at the given rate. </p>
<p> Values are integers where Direction is defined as 2 = Up, 4 = Down, 8 = Left, and 16 = Right. Speed is an integer between 1 and 100. Not all backends that implement the move command use the Speed value. At this time only the gs232a utilizes the Speed parameter.</p>
<dt><code>S, stop</code></p>
<dd>Stop the rotator.</p>
<dt><code>K, park</code></p>
<dd>Park the antenna.</p>
<dt><code>C, set_conf &#8216;Token&#8217; &#8216;Value&#8217;</code></p>
<dd>Set Token to Value. </p>
<p> Backend dependent. Needs testing.</p>
<dt><code>R, reset &#8216;Reset&#8217;</code></p>
<dd>Reset the rotator. </p>
<p> Integer value of &#8216;1&#8217; for Reset All.</p>
<dt><code>_, get_info</code></p>
<dd>Get misc information about the rotator. </p>
<p> At the moment returns &#8216;Model Name&#8217;.</p>
<dt><code>w, send_cmd &#8216;Cmd&#8217;</code></p>
<dd>Send raw command string to rotator. </p>
<p> For binary protocols enter values as ��. Expect a &#8216;Reply&#8217; from the rotator which will likely be a binary block or an ASCII string.</dl>
<p> <code>Locator Commands</code> </p>
<p> These commands offer conversions of Degrees Minutes Seconds to other formats, Maidenhead square locator conversions and distance and azimuth conversions.</p>
<dl>
<dt><code>L, lonlat2loc &#8216;Longitude&#8217; &#8216;Latitude&#8217; &#8216;Loc Len [2-12]&#8217;</code></p>
<dd>Returns the Maidenhead locator for the given &#8216;Longitude&#8217; and &#8216;Latitude&#8217;. </p>
<p> Both are floating point values. The precision of the returned square is controlled by &#8216;Loc Len&#8217; which should be an even numbered integer value between 2 and 12. </p>
<p> For example, &quot;+L -170.000000 -85.000000 12
&quot; returns &quot;Locator: AA55AA00AA00
&quot;.</p>
<dt><code>l, loc2lonlat &#8216;Locator&#8217;</code></p>
<dd>Returns &#8216;Longitude&#8217; and &#8216;Latitude&#8217; in decimal degrees at the approximate center of the requested grid square (despite the use of double precision variables internally, some rounding error occurs). West longitude is expressed as a negative value. South latitude is expressed as a negative value. Locator can be from 2 to 12 characters in length. </p>
<p> For example, &quot;+l AA55AA00AA00
&quot; returns &quot;Longitude: -169.999983
Latitude: -84.999991
&quot;.</p>
<dt><code>D, dms2dec &#8216;Degrees&#8217; &#8216;Minutes&#8217; &#8216;Seconds&#8217; &#8216;S/W&#8217;</code></p>
<dd>Returns &#8216;Dec Degrees&#8217;, a signed floating point value. </p>
<p> Degrees and Minutes are integer values and Seconds is a floating point value. S/W is a flag with &#8216;1&#8217; indicating South latitude or West longitude and &#8216;0&#8217; North or East (the flag is needed as computers don&#8217;t recognize a signed zero even though only the Degrees value only is typically signed in DMS notation).</p>
<dt><code>d, dec2dms &#8216;Dec Degrees&#8217;</code></p>
<dd>Returns &#8216;Degrees&#8217; &#8216;Minutes&#8217; &#8216;Seconds&#8217; &#8216;S/W&#8217;. </p>
<p> Values are as in dms2dec above.</p>
<dt><code>E, dmmm2dec &#8216;Degrees&#8217; &#8216;Dec Minutes&#8217; &#8216;S/W&#8217;</code></p>
<dd>Returns &#8216;Dec Degrees&#8217;, a signed floating point value. </p>
<p> Degrees is an integer value and Minutes is a floating point value. S/W is a flag with &#8216;1&#8217; indicating South latitude or West longitude and &#8216;0&#8217; North or East (the flag is needed as computers don&#8217;t recognize a signed zero even though only the Degrees value only is typically signed in DMS notation).</p>
<dt><code>e, dec2dmmm &#8216;Dec Deg&#8217;</code></p>
<dd>Returns &#8216;Degrees&#8217; &#8216;Minutes&#8217; &#8216;S/W&#8217;. </p>
<p> Values are as in dmmm2dec above.</p>
<dt><code>B, qrb &#8216;Lon 1&#8217; &#8216;Lat 1&#8217; &#8216;Lon 2&#8217; &#8216;Lat 2&#8217;</code></p>
<dd>Returns &#8216;Distance&#8217; &#8216;Azimuth&#8217; where Distance is in km and Azimuth is in degrees. </p>
<p> All Lon/Lat values are signed floating point numbers.</p>
<dt><code>A, a_sp2a_lp &#8216;Short Path Deg&#8217;</code></p>
<dd>Returns &#8216;Long Path Deg&#8217; or -RIG_EINVAL upon input error.. </p>
<p> Both are floating point values within the range 0.00 to 360.00.</p>
<dt><code>a, d_sp2d_lp &#8216;Short Path km&#8217;</code></p>
<dd>Returns &#8216;Long Path km&#8217;. </p>
<p> Both are floating point values.</dl>
<h2>Protocol</h2>
<p><code>Default Protocol</code> </p>
<p> The <code>rotctld</code> protocol is intentionally simple. Commands are entered on a single line with any needed values. In Perl, reliable results are obtained by terminating each command string with a newline character, &#8216;
&#8217;. </p>
<p> Example <i>set</i> (Perl code): </p>
<p> print $socket &quot;P 135 10
&quot;; </p>
<p> print $socket &quot;\set_pos 135 10
&quot;; # escape leading &#8216;\&#8217; </p>
<p> A one line response will be sent as a reply to <i>set</i> commands, &quot;RPRT <i>x</i>
&quot; where <i>x</i> is the Hamlib error code with &#8216;0&#8217; indicating success of the command. </p>
<p> Responses from <code>rotctld</code> <i>get</i> commands are text values and match the same tokens used in the <i>set</i> commands. Each value is returned on its own line. On error the string &quot;RPRT <i>x</i>
&quot; is returned where <i>x</i> is the Hamlib error code. </p>
<p> Example <i>get</i> (Perl code): </p>
<p> print $socket &quot;p
&quot;;<br />
 &quot;135&quot;<br />
 &quot;10&quot; </p>
<p> Most <i>get</i> functions return one to three values. A notable exception is the <i>\dump_caps</i> function which returns many lines of key:value pairs. </p>
<p> This protocol is primarily used by the <i>NET rotctl</i> (rotctl model 2) backend which allows applications already written for Hamlib&#8217;s C API to take advantage of <code>rotctld</code> without the need of rewriting application code. An application&#8217;s user can select rotor model 2 (&quot;NET rotctl&quot;) and then set rot_pathname to &quot;localhost:4533&quot; or other network host:port (set by the <i>-t</i> option above). </p>
<p> <code>Extended Response Protocol</code> </p>
<p> An <i>EXPERIMENTAL</i> Extended Response protocol has been introduced into <code>rotctld</code> as of February 10, 2010. This protocol adds several rules to the strings returned by <code>rotctld</code> and adds a rule for the command syntax. </p>
<p> 1. The command received by <code>rotctld</code> is echoed with its long command name followed by the value(s) (if any) received from the client terminated by the specified response separator as the first record of the response. </p>
<p> 2. The last record of each block is the string &quot;RPRT <i>x</i>
&quot; where <i>x</i> is the numeric return value of the Hamlib backend function that was called by the command. </p>
<p> 3. Any records consisting of data values returned by the rotor backend are prepended by a string immediately followed by a colon then a space and then the value terminated by the response separator. e.g. &quot;Azimuth: 90.000000
&quot; when the command was prepended by &#8216;+&#8217;. </p>
<p> 4. All commands received will be acknowledged by <code>rotctld</code> with records from rules 1 and 2. Records from rule 3 are only returned when data values must be returned to the client. </p>
<p> An example response to a <i>+P</i> command command sent from the shell prompt (note the prepended &#8216;+&#8217;): </p>
<p> $ echo &quot;+P 90 45&quot; | nc -w 1 localhost 4533<br />
 set_pos: 90 45<br />
 RPRT 0 </p>
<p> In this case the long command name and values are returned on the first line and the second line contains the end of block marker and the numeric rig backend return value indicating success. </p>
<p> An example response to a <i>+\get_pos</i> query: </p>
<p> $ echo &quot;+\get_pos&quot; | nc -w 1 localhost 4533<br />
 get_pos:<br />
 Azimuth: 90.000000<br />
 Elevation: 45.000000<br />
 RPRT 0 </p>
<p> In this case, as no value is passed to <code>rotctld</code>, the first line consists only of the long command name. The final line shows that the command was processed successfully by the rotor backend. </p>
<p> Invoking the Extended Response protocol requires prepending a command with a punctuation character. As shown in the examples above, prepending a &#8216;+&#8217; character to the command results in the responses being separated by a newline character (&#8216;
&#8217;). Any other punctuation character recognized by the C <i>ispunct()</i> function except &#8216;\&#8217;, &#8216;?&#8217;, or &#8216;_&#8217; will cause that character to become the response separator and the entire response will be on one line. </p>
<p> Separator character summary:</p>
<dl>
<dt><code>&#8216;+&#8217;</code></p>
<dd>Each record of the response is appended with a newline (&#8216;
&#8217;).</p>
<dt><code>&#8216;;&#8217;, &#8216;|&#8217;, or &#8216;,&#8217;</code></p>
<dd>Each record of the response is appended by the given character resulting in entire response on one line. </p>
<p> Common record separators for text representations of spreadsheet data, etc.</p>
<dt><code>&#8216;?&#8217;</code></p>
<dd>Reserved for &#8216;help&#8217; in rotctl short command</p>
<dt><code>&#8216;_&#8217;</code></p>
<dd>Reserved for \get_info short command</p>
<dt><code>&#8216;#&#8217;</code></p>
<dd>Reserved for comments when reading a command file script </p>
<p> Other punctuation characters have not been tested! Use at your own risk.</dl>
<p> For example, invoking a <i>;\get_pos</i> query with a leading &#8216;;&#8217; returns: </p>
<p> get_pos:;Azimuth: 90.000000;Elevation: 45.000000;RPRT 0 </p>
<p> Or, using the pipe character &#8216;|&#8217; returns: </p>
<p> get_pos:|Azimuth: 90.000000|Elevation: 45.000000|RPRT 0 </p>
<p> And a \set_pos command prepended with a &#8216;|&#8217; returns: </p>
<p> set_pos: 135 22.5|RPRT 0 </p>
<p> Such a format will allow reading a response as a single event using a preferred response separator. Other punctuation characters have not been tested! </p>
<p> All commands with the exception of <i>\set_conf</i> have been tested with the Extended Response protocol and the included <code>testrotctld.pl</code> script.</p>
<h2>Examples</h2>
<p>Start <code>rotctld</code> for a Ham IV rotor with the RotorEZ installed using a USB-to-serial adapter and backgrounding on Linux: </p>
<p> $ rotctld -m 401 -r /dev/ttyUSB1 &amp; </p>
<p> Start <code>rotctld</code> for RotorEZ using COM3 on Win32: </p>
<p> C:\&gt; rotctld -m 401 -r COM3 -T 127.0.0.1 -t 4533 </p>
<p> Connect to the already running <code>rotctld</code>, and set position to 135.0 degrees azimuth and 30.0 degrees elevation with a 1 second read timeout from the shell prompt: </p>
<p> $ echo &quot;\set_pos 135.0 30.0&quot; | nc -w 1 localhost 4533 </p>
<p> Connect to a running <code>rotctld</code> with <code>rotctl</code> on the local host on POSIX: </p>
<p> $ rotctl -m2 </p>
<p> and on Win32: </p>
<p> C:\&gt; rotctl -m 2 -r 127.0.0.1:4533</p>
<h2>Diagnostics</h2>
<p>The <code>-v</code>, <code>&#8211;version</code> option allows different levels of diagnostics to be output to <code>stderr</code> and correspond to -v for BUG, -vv for ERR, -vvv for WARN, -vvvv for VERBOSE, or -vvvvv for TRACE. </p>
<p> A given verbose level is useful for providing needed debugging information to the email address below. For example, TRACE output shows all of the values sent to and received from the rotator which is very useful for rotator backend library development and may be requested by the developers. See the <code>README.betatester</code> and <code>README.developer</code> files for more information.</p>
<h2>Security</h2>
<p>No authentication whatsoever; DO NOT leave this TCP port open wide to the Internet. Please ask if stronger security is needed or consider using an SSH tunnel. </p>
<p> As <code>rotctld</code> does not need any greater permissions than <code>rotctl</code>, it is advisable to not start <code>rotctld</code> as <i>root</i> or another system user account in order to limit any vulnerability.</p>
<h2>Bugs</h2>
<p>The daemon is not detaching and backgrounding itself. </p>
<p> Much testing needs to be done.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;hamlib-developer [at] lists.sourceforge.net&gt;. </p>
<p> We are already aware of the bugs in the previous section :-)</p>
<h2>Authors</h2>
<p>Written by Stephane Fillod, Nate Bargmann, and the Hamlib Group </p>
<p> &lt;<a rel="nofollow" href="http://www.hamlib.org">http://www.hamlib.org</a>&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2000-2009 Stephane Fillod<br />
 Copyright &#169; 2011-2012 Nate Bargmann<br />
 Copyright &#169; 2000-2009 the Hamlib Group. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-rotctl/">rotctl</a></code>(1), <code><a href="/docs/linux/man/3-hamlib/">hamlib</a></code>(3) </p>
