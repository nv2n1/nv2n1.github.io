---
title: "ncidd(8)"
name: "ncidd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ncidd/"
description: "ncidd – Network Caller ID Server"
---

<p><code>ncidd</code> &#8211; Network Caller ID Server</p>
<h2>Synopsis</h2>
<p><code>ncidd</code> [options] </p>
<p> <i>Options:</i> </p>
<pre>[-A &lt;aliasfile&gt; | --alias &lt;aliasfile&gt;]
[-C &lt;configfile&gt; | --config &lt;configfile&gt;]
[-c &lt;logfile&gt; | --cidlog &lt;logfile&gt;]
[-D | --debug]
[-d &lt;logfile&gt; | --datalog &lt;logfile&gt;]
[-e &lt;identifier&gt; | --lineid &lt;identifier&gt;]
[-h | --help]
[-I &lt;modemstr&gt; | --initstr &lt;modemstr&gt;]
[-i &lt;cidstr&gt; | --initcid &lt;cidstr&gt;]
[-L &lt;logfile&gt; | --logfile &lt;logfile&gt;]
[-l &lt;lockfile&gt; | --lockfile &lt;lockfile&gt;]
[-M &lt;MaxBytes&gt; | --cidlogmax &lt;MaxBytes&gt;]
[-N &lt;0|1&gt; | --noserial &lt;0|1]
[-n &lt;0|1&gt; | --nomodem &lt;0|1]
[-P &lt;pidfile&gt; | --pidfile &lt;pidfile&gt;]
[-p &lt;portnumber&gt; | --port &lt;portnumber&gt;]
[-S &lt;0|1&gt; | --ttyclocal &lt;0|1]
[-s &lt;datatype&gt; | --send &lt;datatype&gt;]
[-T &lt;ttyspeed&gt; | --ttyspeed &lt;ttyspeed&gt;]
[-t &lt;ttyport&gt; | --ttyport &lt;ttyport&gt;]
[-V | --version]
[-v &lt;1-9&gt; | --verbose &lt;1-9&gt;]</pre>
<h2>Description</h2>
<p><code>NCIDD</code> collects Caller ID data from: </p>
<pre> - a modem or CID device on a telephone line
 - a CID gateway on the network
 - or both</pre>
<p>It formats the data on a single text line, and then sends it to one or more <i>Network</i> <i>CallerID</i> (<i>NCID</i>) clients over TCP/IP. <code>NCIDD</code> also allows an alias for the number, an alias for the name, and an alias for the telephone line identifier. </p>
<p> The telephone company limits names to 15 upper case characters, so by using the alias function, you can display the name as you would like to view it, or correct a name that was truncated. You can even change or mask a telephone number. </p>
<p> <code>NCIDD</code> can be configured to send a CIDINFO line to clients at each ring and when ringing stops. It contains a LINE (called telephone line) indicator and a RING indicator. </p>
<p> If the Caller ID is obtained from a modem, and the modem supports it, the server will include a ring count in each CIDINFO line. When ringing stops, the ring count will be zero. This allows, for example, a client to send the call information to a pager or cell phone on a specific ring count. If the ring count is not reached, it is assumed the phone was answered and there is no need to send a page or cell phone notification. </p>
<p> If the Caller ID is obtained from a SIP Gateway the CIDINFO line is only sent at the begining and end of a call. At the end of a call, RING indicates either <i>Hangup Without Answer</i><code> or </code><i>Hangup after Answer</i> This allows a cell phone or pager to receive a message only if the phone was not answered. </p>
<p> <code>NCIDD</code> will accept a text message for a client, and then send it to all connected clients, including the one that sent it. </p>
<p> <code>NCIDD</code> will accept a CID message from a client. A CID message contains the Caller ID information from a CID client instead of a serial device or modem. </p>
<p> <code>NCIDD</code> will accept a CIDINFO message from a client. A SIP client will send a CIDINFO message when it receives a CANCEL command. The server will then send a ring count of -1 to its clients to indicate a hangup with no answer. </p>
<p> <code>NCIDD</code> will reload the alias file when sent a SIGHUP signal.</p>
<h2>Options</h2>
<dl>
<dt><code>-A &lt;file&gt; | &#8211;alias &lt;file&gt;</code></p>
<dd>Alias file.<br />
 Default: /etc/ncid/ncidd.alias</p>
<dt><code>-C &lt;file&gt; | &#8211;config &lt;file&gt;</code></p>
<dd>Config file.<br />
 Default: /etc/ncid/ncidd.conf</p>
<dt><code>-c &lt;file&gt; | &#8211;cidlog &lt;file&gt;</code></p>
<dd>Call log data file.<br />
 Default: /var/log/cidcall.log</p>
<dt><code>-D | &#8211;debug</code></p>
<dd>Debug mode.</p>
<dt><code>-d &lt;file&gt; | &#8211;datalog &lt;file&gt;</code></p>
<dd>Data log data file, usually from a modem.<br />
 Default: /var/log/datalog.log</p>
<dt><code>-e &lt;identifier&gt; | &#8211;lineid &lt;identifier&gt;</code></p>
<dd>The telephone line identifier is for a modem. It is normally 1 to 4 characters. The default indicator is not displayed, but for one POTS line, you could change it to <i>POTS</i>. For multiple lines you should use a identifier. You could change it to the 4 digit extension for an exchange. For example, if the telephone number is 321-555-1212 the identifier whould be 1212.<br />
 Default: &#8211;</p>
<dt><code>-h | &#8211;help</code></p>
<dd>Display a help message.</p>
<dt><code>-I string | &#8211;initstr string</code></p>
<dd>Modem initialization string<br />
 Default: ATE1V1Q0</p>
<dt><code>-i string | &#8211;initcid string</code></p>
<dd>CID initialization string<br />
 Default: AT+VCID=1<br />
 if it fails: AT#CID=1</p>
<dt><code>-L &lt;file&gt; | &#8211;logfile &lt;file&gt;</code></p>
<dd>Server logfile.<br />
 Default: /var/log/ncidd.log</p>
<dt><code>-l &lt;file&gt; | &#8211;lockfile &lt;file&gt;</code></p>
<dd>Modem lockfile.<br />
 Default: /var/lock/LCK..modem</p>
<dt><code>-M &lt;MaxBytes&gt; | &#8211;cidlogmax &lt;MaxBytes&gt;</code></p>
<dd>Set the maximum CID call log file size in bytes.<br />
 Maximum size is 100000000<br />
 Default: cidlogmax = 110000</p>
<dt><code>-N &lt;0|1&gt; | &#8211;noserial &lt;0|1&gt;</code></p>
<dd>serial device (0) or no serial device (1)<br />
 Default: noserial = 0</p>
<dt><code>-n &lt;0|1&gt; | &#8211;nomodem &lt;0|1&gt;</code></p>
<dd>modem (0) or no modem (1)<br />
 Default: nomodem = 0</p>
<dt><code>-P &lt;pidfile&gt; | &#8211;pidfile &lt;pidfile&gt;</code></p>
<dd>Server PID file. Set to <i>/var/run/ncidd.pid</i><code> in a rc or init script when used as a service. The program will still run if it does not have permission to write a pidfile. There is no default. If pidfile is not set, no pid file will be used.</p>
<dt>-p &lt;port&gt; | &#8211;port &lt;port&gt;</code></p>
<dd>Server port.<br />
 Default: 3333</p>
<dt><code>-S &lt;0|1&gt; | &#8211;ttyclocal &lt;0|1&gt;</code></p>
<dd>Enable (0) or disable (1) modem control signals.<br />
 Default: modem control signals disabled</p>
<dt><code>-s &lt;datatype&gt; | &#8211;send &lt;datatype&gt;</code></p>
<dd>Send optional CID data to a client. Where <i>datatype</i> is:<br />
 <i>cidlog</i>: sent when the client connects. If the CID call log gets too big, it will not be sent.<br />
 <i>cidinfo</i>: sent on each ring, to all clients, gives the current ring count.<br />
 Default: Optional CID DATA is not sent</p>
<dt><code>-T &lt;ttyspeed&gt; | &#8211;ttyspeed &lt;ttyspeed&gt;</code></p>
<dd>Set the tty port speed to one of: 19200, 9600, 4800<br />
 Default: ttyspeed = 19200</p>
<dt><code>-t &lt;ttyport&gt; | &#8211;ttyport &lt;ttyport&gt;</code></p>
<dd>Modem device file, or serial port that provides Caller ID information.<br />
 Default: /dev/modem</p>
<dt><code>-V | &#8211;version</code></p>
<dd>Display the version number.</p>
<dt><code>-v &lt;1-9&gt; | &#8211;verbose &lt;1-9&gt;</code></p>
<dd>Output information, used for the logfile and the -D option. Set higher number for more information.<br />
 Default: verbose = 1<br />
 Most Useful: verbose = 3</dl>
<h2>Configuration</h2>
<p>The <a href="/docs/linux/man/5-ncidd-conf/">ncidd.conf</a>(5) file is used to set options. The syntax of the <a href="/docs/linux/man/5-ncidd-conf/">ncidd.conf</a>(5) file is discussed seperately, and should be consulted for detailed reference information. </p>
<p> The <a href="/docs/linux/man/5-ncidd-alias/">ncidd.alias</a>(5) file is used to create aliases. The syntax of the <a href="/docs/linux/man/5-ncidd-alias/">ncidd.alias</a>(5) file is discussed seperately, and should be consulted for detailed reference information.</p>
<h2>Data Line Format Examples</h2>
<p>These are five examples of the three types of lines sent to <i>NCID</i> clients. The first field is line identifier. </p>
<p> The <i>CID:</i> line gives the CID information of the current call. </p>
<p> The <i>CIDLOG:</i> line gives the CID information of a line in the CID log file. </p>
<p> The <i>MSG:</i> line gives messages from the server. </p>
<p> The <i>MSGLOG:</i> line gives a message logged in the CID log file. </p>
<p> The <i>CIDINFO:</i> line gives a line number and ring count from the server. The ring count starts at 1 and increases until ringing ends, at which time a count of 0 is sent. The line number default is 1, Distinctive Ring will add one of the letters: A B C D to indicate the virtual line called. Expect additional name/values pairs to be added in the future. </p>
<p> The <i>CID:</i> and <i>CIDLOG:</i> lines are identical, with data stored as name and value pairs. Clients should always locate the line identifier, and then scan for a field name and get its value. It&#8217;s possible that additional name/value pairs may be added in the future. </p>
<p> The <i>MSG:</i> and <i>MSGLOG:</i> lines are identical, </p>
<pre>CID: *DATE*mmddyyyy*TIME*hhmm*NMBR*number*MESG*NONE*NAME*name*
CIDLOG: *DATE*mmddyyyy*TIME*hhmm*NMBR*number*MESG*NONE*NAME*name*
CIDINFO: *LINE*line indicator*RING*ringcount*
MSG: Too many clients connected: 15
MSGLOG: Too many clients connected: 15</pre>
<h2>Log Files</h2>
<dl>
<dt><code>cidcall.log</code></p>
<dd>Contains CID and MSG lines</p>
<dt><code>ciddata.log</code></p>
<dd>Contains the output from the modem or CID device</p>
<dt><code>ncidd.log</code></p>
<dd>Server log file. Contents controlled by verbose.</dl>
<h2>Diagnostics</h2>
<pre> Return Code Meaning
 ----------- -------
 0 Successful
 -100 Usage
 -101 Invalid port number
 -102 TTY port is in use
 -103 Unable to set modem for Caller ID
 -104 Configuration file error
 -105 No modem found
 -106 Invalid data type.
 -107 Invalid number
 -108 Invalid tty port speed [set in config file]
 -109 Alias file error
 -110 PID file already exists
 -111 Cannot init TTY
 -112 Serial device error
 -113 string too long
 -? System error</pre>
<h2>See Also</h2>
<p>ncid.1, ncidtools.1, lcdncid.1, out2osd.1, ncidd.conf.5, ncidd.alias.5, ncid.conf.5 </p>
