---
title: "ser2net(8)"
name: "ser2net"
section: "8"
letter: "s"
url: "/docs/linux/man/8-ser2net/"
description: "ser2net – Serial to network proxy"
---

<p>ser2net &#8211; Serial to network proxy</p>
<h2>Synopsis</h2>
<p><code>ser2net</code> [-c configfile] [-C configline] [-p controlport] [-n] [-d] [-b] [-v] [-P pidfile] </p>
<h2>Description</h2>
<p>The <code>ser2net</code> daemon allows telnet and tcp sessions to be established with a unit&#8217;s serial ports. The program comes up normally as a daemon, opens the TCP ports specified in the configuration file, and waits for connections. Once a connection occurs, the program attempts to set up the connection and open the serial port. If another user is already using the connection or serial port, the connection is refused with an error message. </p>
<h2>Options</h2>
<dl>
<dt><i>-c config-file</i></p>
<dd>Set the configuration file to one other than the default of <code>/etc/ser2net.conf</code></p>
<dt><i>-C config-line</i></p>
<dd>Handle a single configuration line. This may be specified multiple times for multiple lines. This is just like a line in the config file. This disables the default config file, you must specify a -c after the last -C to have it read a config file, too.</p>
<dt><i>-n</i></p>
<dd>Stops the daemon from forking and detaching from the controlling terminal. This is useful for running from init.</p>
<dt><i>-d</i></p>
<dd>Like -n, but also sends the system logs to standard output. This is most useful for debugging purposes.</p>
<dt><i>-P pidfile</i></p>
<dd>If specified, put the process id (pid) of ser2net in the pidfile, replacing whatever was in that file previously. A pidfile is not created by default, you must specify this to create one. Note also that this filename must be specific with the full path, as ser2net will change directory to &quot;/&quot; when it becomes a daemon. when it</p>
<dt><i>-u</i></p>
<dd>If UUCP locking is enabled, this will disable the use of UUCP locks.</p>
<dt><i>-b</i></p>
<dd>Cisco IOS uses a different mechanism for specifying the baud rates than the mechanism described in RFC2217. This option sets the IOS version of setting the baud rates. The default is RFC2217&#8217;s.</p>
<dt><i>-v</i></p>
<dd>Prints the version of the program and exits.</p>
<dt><i>-p controlport</i></p>
<dd>Enables the control port and sets the TCP port to listen to for the control port. A port number may be of the form [host,]port, such as 127.0.0.1,2000 or localhost,2000. If this is specified, it will only bind to the IP address specified for the port. Otherwise, it will bind to all the addresses on the machine. </p>
<p> If the port number is zero, that means that standard in/out will be used for the only input/output, and only one port should be specified in the config. This way, it can be used from inetd.</p>
<dt><i>-s signature</i></p>
<dd>Specifies the default RFC2217 signature. </p>
</dl>
<h2>Control Port</h2>
<p>The control port provides a simple interface for controlling the ports and viewing their status. To accomplish this, it has the following commands:</p>
<dl>
<dt><code>showport [&lt;TCP port&gt;]</code></p>
<dd>Show information about a port. If no port is given, all ports are displayed.</p>
<dt><code>showshortport [&lt;TCP port&gt;]</code></p>
<dd>Show information about a port, each port on one line. If no port is given, all ports are displayed. This can produce very wide output.</p>
<dt><code>help</code></p>
<dd>Display a short list and summary of commands.</p>
<dt><code>exit</code></p>
<dd>Disconnect from the control port.</p>
<dt><code>version</code></p>
<dd>Display the version of this program.</p>
<dt><code>monitor &lt;type&gt; &lt;tcp port&gt;</code></p>
<dd>Display all the input for a given port on the calling control port. Only one direction may be monitored at a time. The type field may be <i>tcp</i> or <i>term</i> and specifies whether to monitor data from the TCP port or from the serial port Note that data monitoring is best effort, if the controller port cannot keep up the data will be silently dropped. A controller may only monitor one thing and a port may only be monitored by one controller.</p>
<dt><code>monitor stop</code></p>
<dd>Stop the current monitor.</p>
<dt><code>disconnect &lt;tcp port&gt;</code></p>
<dd>Disconnect the tcp connection on the port.</p>
<dt><code>setporttimeout &lt;tcp port&gt; &lt;timeout&gt;</code></p>
<dd>Set the amount of time in seconds before the port connection will be shut down if no activity has been seen on the port.</p>
<dt><code>setportconfig &lt;tcp port&gt; &lt;config&gt;</code></p>
<dd>Set the port configuration as in the device configuration in the <code>/etc/ser2net.conf</code> file. If conflicting options are specified, the last option will be the one used. Note that these will not change until the port is disconnected and connected again. Options <i>300, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200</i> set the various baud rates. <i>EVEN, ODD, NONE</i> set the parity. <i>1STOPBIT, 2STOPBITS</i> set the number of stop bits. <i>7DATABITS, 8DATABITS</i> set the number of data bits. <i>[-]XONXOFF</i> turns on (- off) XON/XOFF support. <i>[-]RTSCTS</i> turns on (- off) hardware flow control. <i>[-]LOCAL</i> ignores (- checks) the modem control lines (DCD, DTR, etc.)</p>
<dt><code>setportcontrol &lt;tcp port&gt; &lt;controls&gt;</code></p>
<dd>Modify dynamic port controls. These do not stay between connections. Controls are: <i>DTRHI, DTRLO</i> Turns on and off the DTR line. <i>RTSHI, RTSLO</i> Turns on and off the RTS line.</p>
<dt><code>setportenable &lt;tcp port&gt; &lt;enable state&gt;</code></p>
<dd>Sets the port operation state. Valid states are: <i>off</i> to shut the TCP port down, <i>raw</i> to enable the TCP port transfer all I/O as-is, <i>rawlp</i> to enable the TCP port input and device output without termios setting, and <i>telnet</i> to enable the TCP port is up run the telnet negotiation protocol on the port. </p>
</dl>
<h2>Configuration</h2>
<p>Configuration is accomplished through the file <code>/etc/ser2net.conf</code>. A file with another name or path may be specified using the <i>-c</i> option, or individual config lines may be specified with the <i>-C</i> option. This file consists of one or more entries with the following format:</p>
<dl>
<dd>&lt;TCP port&gt;:&lt;state&gt;:&lt;timeout&gt;:&lt;device&gt;:&lt;options&gt;</dl>
<p> or</p>
<dl>
<dd>BANNER:&lt;banner name&gt;:&lt;banner text&gt;</dl>
<p> or</p>
<dl>
<dd>SIGNATURE:&lt;signature name&gt;:&lt;signature text&gt;</dl>
<p> or</p>
<dl>
<dd>OPENSTR:&lt;openstr name&gt;:&lt;openstr text&gt;</dl>
<p> or</p>
<dl>
<dd>CLOSESTR:&lt;closestr name&gt;:&lt;closestr text&gt;</dl>
<p> or</p>
<dl>
<dd>TRACEFILE:&lt;tracefile name&gt;:&lt;tracefile&gt;</dl>
<p> or</p>
<dl>
<dd>CONTROLPORT:&lt;port spec&gt;</dl>
<h3>Fields</h3>
<dl>
<dt><i>TCP port</i></p>
<dd>Name or number of the TCP/IP port to accept connections from for this device. A port number may be of the form [host,]port, such as 127.0.0.1,2000 or localhost,2000. If this is specified, it will only bind to the IP address specified for the port. Otherwise, it will bind to all the ports on the machine.</p>
<dt><i>state</i></p>
<dd>Either <code>raw</code> or <code>rawlp</code> or <code>telnet</code> or <code>off.</code> <i>off</i> disables the port from accepting connections. It can be turned on later from the control port. <i>raw</i> enables the port and transfers all data as-is between the port and the long. <i>rawlp</i> enables the port and transfers all input data to device, device is open without any termios setting. It allow to use /dev/lpX devices and printers connected to them. <i>telnet</i> enables the port and runs the telnet protocol on the port to set up telnet parameters. This is most useful for using telnet.</p>
<dt><i>timeout</i></p>
<dd>The time (in seconds) before the port will be disconnected if there is no activity on it. A zero value disables this function.</p>
<dt><i>device</i></p>
<dd>The name of the device to connect to. This must be in the form of <code>/dev/&lt;device&gt;</code>.</p>
<dt><i>device configuration options</i></p>
<dd>Sets operational parameters for the serial port. Values may be separated by spaces or commas. Options <i>300, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200</i> set the various baud rates. <i>EVEN, ODD, NONE</i> set the parity. <i>1STOPBIT, 2STOPBITS</i> set the number of stop bits. <i>7DATABITS, 8DATABITS</i> set the number of data bits. <i>[-]XONXOFF</i> turns on (- off) XON/XOFF support. <i>[-]RTSCTS</i> turns on (- off) hardware flow control. <i>[-]LOCAL</i> ignores (- checks) the modem control lines (DCD, DTR, etc.) <i>[-]HANGUP_WHEN_DONE</i> lowers (- does not lower) the modem control lines (DCD, DTR, etc.) when the connection closes. <i>NOBREAK</i> disables automatic clearing of the break setting of the port. <i>remctl</i> allows remote control of the serial port parameters via RFC 2217. See the README for more info. <i>&lt;banner name&gt;</i> displays the given banner when a user connects to the port. <i>&lt;signature name&gt;</i> sends RFC2217 signature on clients request. <i>&lt;openstr name&gt;</i> Send the given string to the device when the port is opened. <i>&lt;closestr name&gt;</i> Send the given string to the device when the port is closed. </p>
<p> <i>tr=&lt;filename&gt;</i> When the port is opened, open the given tracefile and store all data read from the physical device (and thus written to the user&#8217;s TCP port) in the file. The actual filename is specified in the TRACEFILE directive. If the file already exists, it is appended. The file is closed when the port is closed. </p>
<p> <i>tw=&lt;filename&gt;</i> Like tr, but traces data written to the device. </p>
<p> <i>tb=&lt;filename&gt;</i> trace both read and written data to the same file. Note that this is independent of tr and tw, so you may be tracing read, write, and both to different files. </p>
<p> <i>[-]hexdump</i> turns on (- turns off) hexdump output to all trace files. Each line in the trace file will be 8 (or less) bytes in canonical hex+ASCII format. This is useful for debugging a binary protocol. </p>
<p> <i>[-]timestamp</i> adds (- removes) a timestamp to all of the trace files. A timestamp is prepended to each line if hexdump is active for the trace file. A timestamped line is also recorded in the trace file when a remote client connects or disconnects from the port. </p>
<p> <i>[-][tr-|tw-|tb-]hexdump</i> turns on (- turns off) hexdump output for only one trace file. May be combined with [-]hexdump. Order is important. </p>
<p> <i>[-][tr-|tw-|tb-]timestamp</i> adds (- removes) a timestamp to only one the trace files May be combined with [-]timestamp. Order is important. </p>
<dt><i>banner name</i></p>
<dd>A name for the banner; this may be used in the options of a port.</p>
<dt><i>banner text</i></p>
<dd>The text to display as the banner. It takes escape sequences for substituting strings, see &quot;FILENAME, BANNER, AND STRING FORMATTING&quot; for details. </p>
<dt><i>tracefile name</i></p>
<dd>A name for the tracefile, this is used in the tw, tr, and tb options of a port.</p>
<dt><i>tracefile</i></p>
<dd>The file to send the trace into. Note that this takes escape sequences for substituting strings, see &quot;FILENAME, BANNER, AND STRING FORMATTING&quot; for details. Note that when using the time escape sequences, the time is read once at port startup, so if you use both tw and tr they will have the same date and time.</p>
<dt><i>port spec</i></p>
<dd>The control port specification as defined by the [-p] option on the command line. This lets the control port be specified in the configuration file. The command line will override this, and only the first port specified is used. </p>
</dl>
<p> Blank lines and lines starting with `#&#8217; are ignored.</p>
<h2>Filename, Banner, And String Formatting</h2>
<p>Filenames, banners, and open/close string may contain normal &quot;C&quot; escape sequences and a large number of other escape sequences, too: </p>
<dl>
<dd> &#8211; bell<br />
  &#8211; backspace<br />
  &#8211; form feed<br />
 
 &#8211; newline<br />
  &#8211; carriage return<br />
 	 &#8211; tab<br />
  &#8211; vertical tab<br />
 \ &#8211; \<br />
 \? &#8211; ?<br />
 \&#8217; &#8211; &#8216;<br />
 \&quot; &#8211; &quot;<br />
 
nn &#8211; octal value for nnn<br />
 
