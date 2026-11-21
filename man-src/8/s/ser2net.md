---
title: "ser2net(8)"
name: "ser2net"
section: "8"
letter: "s"
url: "/docs/linux/man/8-ser2net/"
description: "ser2net – Serial to network proxy"
---
<p>ser2net &#8211; Serial to network proxy  </p>
<h2>SYNOPSIS</h2>
<p> <code>ser2net</code> [-c configfile] [-C configline] [-p controlport] [-n] [-d] [-b] [-v] [-P pidfile] </p>
<h2>DESCRIPTION</h2>
<p> The <code>ser2net</code> daemon allows telnet and tcp sessions to be established with a unit&#8217;s serial ports. </p>
<p>The program comes up normally as a daemon, opens the TCP ports specified in the configuration file, and waits for connections. Once a connection occurs, the program attempts to set up the connection and open the serial port. If another user is already using the connection or serial port, the connection is refused with an error message. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-c config-file</i></dt>
<dd> <p> Set the configuration file to one other than the default of <code>/etc/ser2net.conf</code> </p>
 </dd>
<dt><i>-C config-line</i></dt>
<dd> <p> Handle a single configuration line. This may be specified multiple times for multiple lines. This is just like a line in the config file. This disables the default config file, you must specify a -c after the last -C to have it read a config file, too. </p>
 </dd>
<dt><i>-n</i></dt>
<dd> <p> Stops the daemon from forking and detaching from the controlling terminal. This is useful for running from init. </p>
 </dd>
<dt><i>-d</i></dt>
<dd> <p> Like -n, but also sends the system logs to standard output. This is most useful for debugging purposes. </p>
 </dd>
<dt><i>-P pidfile</i></dt>
<dd> <p> If specified, put the process id (pid) of ser2net in the pidfile, replacing whatever was in that file previously. A pidfile is not created by default, you must specify this to create one. Note also that this filename must be specific with the full path, as ser2net will change directory to &quot;/&quot; when it becomes a daemon. when it </p>
 </dd>
<dt><i>-u</i></dt>
<dd> <p> If UUCP locking is enabled, this will disable the use of UUCP locks. </p>
 </dd>
<dt><i>-b</i></dt>
<dd> <p> Cisco IOS uses a different mechanism for specifying the baud rates than the mechanism described in RFC2217. This option sets the IOS version of setting the baud rates. The default is RFC2217&#8217;s. </p>
 </dd>
<dt><i>-v</i></dt>
<dd> <p> Prints the version of the program and exits. </p>
 </dd>
<dt><i>-p controlport</i></dt>
<dd> <p> Enables the control port and sets the TCP port to listen to for the control port. A port number may be of the form [host,]port, such as 127.0.0.1,2000 or localhost,2000. If this is specified, it will only bind to the IP address specified for the port. Otherwise, it will bind to all the addresses on the machine. </p>
<p>If the port number is zero, that means that standard in/out will be used for the only input/output, and only one port should be specified in the config. This way, it can be used from inetd. </p>
 </dd>
<dt><i>-s signature</i></dt>
<dd> <p> Specifies the default RFC2217 signature. </p>
 </dd></dl>
<h2>CONTROL PORT</h2>
<p> The control port provides a simple interface for controlling the ports and viewing their status. To accomplish this, it has the following commands: </p>
<dl>
<dt><code>showport [&lt;TCP port&gt;]</code></dt>
<dd> <p> Show information about a port. If no port is given, all ports are displayed. </p>
 </dd>
<dt><code>showshortport [&lt;TCP port&gt;]</code></dt>
<dd> <p> Show information about a port, each port on one line. If no port is given, all ports are displayed. This can produce very wide output. </p>
 </dd>
<dt><code>help</code></dt>
<dd> <p> Display a short list and summary of commands. </p>
 </dd>
<dt><code>exit</code></dt>
<dd> <p> Disconnect from the control port. </p>
 </dd>
<dt><code>version</code></dt>
<dd> <p> Display the version of this program. </p>
 </dd>
<dt><code>monitor &lt;type&gt; &lt;tcp port&gt;</code></dt>
<dd> <p> Display all the input for a given port on the calling control port. Only one direction may be monitored at a time. The type field may be <i>tcp</i> or <i>term</i> and specifies whether to monitor data from the TCP port or from the serial port Note that data monitoring is best effort, if the controller port cannot keep up the data will be silently dropped. A controller may only monitor one thing and a port may only be monitored by one controller. </p>
 </dd>
<dt><code>monitor stop</code></dt>
<dd> <p> Stop the current monitor. </p>
 </dd>
<dt><code>disconnect &lt;tcp port&gt;</code></dt>
<dd> <p> Disconnect the tcp connection on the port. </p>
 </dd>
<dt><code>setporttimeout &lt;tcp port&gt; &lt;timeout&gt;</code></dt>
<dd> <p> Set the amount of time in seconds before the port connection will be shut down if no activity has been seen on the port. </p>
 </dd>
<dt><code>setportconfig &lt;tcp port&gt; &lt;config&gt;</code></dt>
<dd> <p> Set the port configuration as in the device configuration in the <code>/etc/ser2net.conf</code> file. If conflicting options are specified, the last option will be the one used. Note that these will not change until the port is disconnected and connected again. Options <i>300, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200</i> set the various baud rates. <i>EVEN, ODD, NONE</i> set the parity. <i>1STOPBIT, 2STOPBITS</i> set the number of stop bits. <i>7DATABITS, 8DATABITS</i> set the number of data bits. <i>[-]XONXOFF</i> turns on (- off) XON/XOFF support. <i>[-]RTSCTS</i> turns on (- off) hardware flow control. <i>[-]LOCAL</i> ignores (- checks) the modem control lines (DCD, DTR, etc.) </p>
 </dd>
<dt><code>setportcontrol &lt;tcp port&gt; &lt;controls&gt;</code></dt>
<dd> <p> Modify dynamic port controls. These do not stay between connections. Controls are: <i>DTRHI, DTRLO</i> Turns on and off the DTR line. <i>RTSHI, RTSLO</i> Turns on and off the RTS line. </p>
 </dd>
<dt><code>setportenable &lt;tcp port&gt; &lt;enable state&gt;</code></dt>
<dd> <p> Sets the port operation state. Valid states are: <i>off</i> to shut the TCP port down, <i>raw</i> to enable the TCP port transfer all I/O as-is, <i>rawlp</i> to enable the TCP port input and device output without termios setting, and <i>telnet</i> to enable the TCP port is up run the telnet negotiation protocol on the port. </p>
 </dd></dl>
<h2>CONFIGURATION</h2>
<p> Configuration is accomplished through the file <code>/etc/ser2net.conf</code>. A file with another name or path may be specified using the <i>-c</i> option, or individual config lines may be specified with the <i>-C</i> option. This file consists of one or more entries with the following format: </p>
<dl>
<dd> <p> &lt;TCP port&gt;:&lt;state&gt;:&lt;timeout&gt;:&lt;device&gt;:&lt;options&gt; </p>
 </dd></dl>
<p>or </p>
<dl>
<dd> <p> BANNER:&lt;banner name&gt;:&lt;banner text&gt; </p>
 </dd></dl>
<p>or </p>
<dl>
<dd> <p> SIGNATURE:&lt;signature name&gt;:&lt;signature text&gt; </p>
 </dd></dl>
<p>or </p>
<dl>
<dd> <p> OPENSTR:&lt;openstr name&gt;:&lt;openstr text&gt; </p>
 </dd></dl>
<p>or </p>
<dl>
<dd> <p> CLOSESTR:&lt;closestr name&gt;:&lt;closestr text&gt; </p>
 </dd></dl>
<p>or </p>
<dl>
<dd> <p> TRACEFILE:&lt;tracefile name&gt;:&lt;tracefile&gt; </p>
 </dd></dl>
<p>or </p>
<dl>
<dd> <p> CONTROLPORT:&lt;port spec&gt; </p>
 </dd></dl>
<h3>FIELDS</h3>
<dl>
<dt><i>TCP port</i></dt>
<dd> <p> Name or number of the TCP/IP port to accept connections from for this device. A port number may be of the form [host,]port, such as 127.0.0.1,2000 or localhost,2000. If this is specified, it will only bind to the IP address specified for the port. Otherwise, it will bind to all the ports on the machine. </p>
 </dd>
<dt><i>state</i></dt>
<dd> <p> Either <code>raw</code> or <code>rawlp</code> or <code>telnet</code> or <code>off.</code> <i>off</i> disables the port from accepting connections. It can be turned on later from the control port. <i>raw</i> enables the port and transfers all data as-is between the port and the long. <i>rawlp</i> enables the port and transfers all input data to device, device is open without any termios setting. It allow to use /dev/lpX devices and printers connected to them. <i>telnet</i> enables the port and runs the telnet protocol on the port to set up telnet parameters. This is most useful for using telnet. </p>
 </dd>
<dt><i>timeout</i></dt>
<dd> <p> The time (in seconds) before the port will be disconnected if there is no activity on it. A zero value disables this function. </p>
 </dd>
<dt><i>device</i></dt>
<dd> <p> The name of the device to connect to. This must be in the form of <code>/dev/&lt;device&gt;</code>. </p>
 </dd>
<dt><i>device configuration options</i></dt>
<dd> <p> Sets operational parameters for the serial port. Values may be separated by spaces or commas. Options <i>300, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200</i> set the various baud rates. <i>EVEN, ODD, NONE</i> set the parity. <i>1STOPBIT, 2STOPBITS</i> set the number of stop bits. <i>7DATABITS, 8DATABITS</i> set the number of data bits. <i>[-]XONXOFF</i> turns on (- off) XON/XOFF support. <i>[-]RTSCTS</i> turns on (- off) hardware flow control. <i>[-]LOCAL</i> ignores (- checks) the modem control lines (DCD, DTR, etc.) <i>[-]HANGUP_WHEN_DONE</i> lowers (- does not lower) the modem control lines (DCD, DTR, etc.) when the connection closes. <i>NOBREAK</i> disables automatic clearing of the break setting of the port. <i>remctl</i> allows remote control of the serial port parameters via RFC 2217. See the README for more info. <i>&lt;banner name&gt;</i> displays the given banner when a user connects to the port. <i>&lt;signature name&gt;</i> sends RFC2217 signature on clients request. <i>&lt;openstr name&gt;</i> Send the given string to the device when the port is opened. <i>&lt;closestr name&gt;</i> Send the given string to the device when the port is closed. </p>
<p> <i>tr=&lt;filename&gt;</i> When the port is opened, open the given tracefile and store all data read from the physical device (and thus written to the user&#8217;s TCP port) in the file. The actual filename is specified in the TRACEFILE directive. If the file already exists, it is appended. The file is closed when the port is closed. </p>
<p> <i>tw=&lt;filename&gt;</i> Like tr, but traces data written to the device. </p>
<p> <i>tb=&lt;filename&gt;</i> trace both read and written data to the same file. Note that this is independent of tr and tw, so you may be tracing read, write, and both to different files. </p>
<p> <i>[-]hexdump</i> turns on (- turns off) hexdump output to all trace files. Each line in the trace file will be 8 (or less) bytes in canonical hex+ASCII format. This is useful for debugging a binary protocol. </p>
<p> <i>[-]timestamp</i> adds (- removes) a timestamp to all of the trace files. A timestamp is prepended to each line if hexdump is active for the trace file. A timestamped line is also recorded in the trace file when a remote client connects or disconnects from the port. </p>
<p> <i>[-][tr-|tw-|tb-]hexdump</i> turns on (- turns off) hexdump output for only one trace file. May be combined with [-]hexdump. Order is important. </p>
<p> <i>[-][tr-|tw-|tb-]timestamp</i> adds (- removes) a timestamp to only one the trace files May be combined with [-]timestamp. Order is important. </p>
 </dd>
<dt><i>banner name</i></dt>
<dd> <p> A name for the banner; this may be used in the options of a port. </p>
 </dd>
<dt><i>banner text</i></dt>
<dd> <p> The text to display as the banner. It takes escape sequences for substituting strings, see &quot;FILENAME, BANNER, AND STRING FORMATTING&quot; for details. </p>
 </dd>
<dt><i>tracefile name</i></dt>
<dd> <p> A name for the tracefile, this is used in the tw, tr, and tb options of a port. </p>
 </dd>
<dt><i>tracefile</i></dt>
<dd> <p> The file to send the trace into. Note that this takes escape sequences for substituting strings, see &quot;FILENAME, BANNER, AND STRING FORMATTING&quot; for details. Note that when using the time escape sequences, the time is read once at port startup, so if you use both tw and tr they will have the same date and time. </p>
 </dd>
<dt><i>port spec</i></dt>
<dd> <p> The control port specification as defined by the [-p] option on the command line. This lets the control port be specified in the configuration file. The command line will override this, and only the first port specified is used. </p>
 </dd></dl>
<p>Blank lines and lines starting with `#&#8216; are ignored. </p>
<h2>FILENAME, BANNER, AND STRING FORMATTING</h2>
<p> Filenames, banners, and open/close string may contain normal &quot;C&quot; escape sequences and a large number of other escape sequences, too: </p>
<dl>
<dd> <p> \a - bell <br />
 \b - backspace <br />
 \f - form feed <br />
 \n - newline <br />
 \r - carriage return <br />
 \t - tab <br />
 \v - vertical tab <br />
 \\ - \ <br />
 \? - ? <br />
 \&#8216; - &#8216; <br />
 \&quot; - &quot; <br />
 \nnn - octal value for nnn <br />
 \xXX - hex value for XX <br />
 \d - The device name (/dev/ttyS0, etc.) <br />
 \p - TCP port number <br />
 \B - The serial port parameters (eg 9600N81) <br />
 \Y -&gt; year <br />
 \y -&gt; day of the year (days since Jan 1) <br />
 \M -&gt; month (Jan, Feb, Mar, etc.) <br />
 \m -&gt; month (as a number) <br />
 \A -&gt; day of the week (Mon, Tue, etc.) <br />
 \D -&gt; day of the month <br />
 \e -&gt; epoc (seconds since Jan 1, 1970) <br />
 \U -&gt; microseconds in the current second <br />
 \p -&gt; local port number <br />
 \d -&gt; local device name <br />
 \I -&gt; remote IP address (in dot format) <br />
 \H -&gt; hour (24-hour time) <br />
 \h -&gt; hour (12-hour time) <br />
 \i -&gt; minute <br />
 \S -&gt; second <br />
 \q -&gt; am/pm <br />
 \P -&gt; AM/PM </p>
 </dd></dl>
<p>In addition, for backwards compatibility because filenames and banners used to have different formatting, \s is the serial port parameters if in a banner and seconds if in a filename. Use of this is discouraged as it may change in the future. </p>
<p>These sequences may be used to make the filename unique per open and identify which port/device the filename was for. Note that in filenames when using \d, everything up to and including last / in the device name is removed, because you can&#8217;t have a / in a filename. So in a filename /dev/ttyS0 would become just ttyS0. </p>
<h2>SECURITY</h2>
<p> ser2net uses the tcp wrappers interface to implement host-based security. See <a href="/docs/linux/man/5-hosts_access/">hosts_access</a>(5) for a description of the file setup. Two daemons are used by ser2net, &quot;ser2net&quot; is for the data ports and &quot;ser2net-control&quot; is for the control ports. </p>
<h2>SIGNALS</h2>
<dl>
<dt><code>SIGHUP</code></dt>
<dd> <p> If ser2net receives a SIGHUP, it will reread it configuration file and make the appropriate changes. If an inuse port is changed or deleted, the actual change will not occur until the port is disconnected. </p>
 </dd></dl>
<h2>Error</h2>
<p> Almost all error output goes to syslog, not standard output. </p>
<h2>FILES</h2>
<p> /etc/ser2net.conf </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-telnet/">telnet</a>(1), <a href="/docs/linux/man/5-hosts_access/">hosts_access</a>(5) </p>
<h2>KNOWN PROBLEMS</h2>
<p> None. </p>
<h2>AUTHOR</h2>
<p>Corey Minyard &lt;minyard [at] acm.org&gt; </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dt><a href="#lbAC">SYNOPSIS</a></dt>
<dd>  </dd>
<dt><a href="#lbAD">DESCRIPTION</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">OPTIONS</a></dt>
<dd>  </dd>
<dt><a href="#lbAF">CONTROL PORT</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">CONFIGURATION</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAH">FIELDS</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAI">FILENAME, BANNER, AND STRING FORMATTING</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">SECURITY</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">SIGNALS</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">Error</a></dt>
<dd>  </dd>
<dt><a href="#lbAM">FILES</a></dt>
<dd>  </dd>
<dt><a href="#lbAN">SEE ALSO</a></dt>
<dd>  </dd>
<dt><a href="#lbAO">KNOWN PROBLEMS</a></dt>
<dd>  </dd>
<dt><a href="#lbAP">AUTHOR</a></dt>
<dd>  </dd></dl>
