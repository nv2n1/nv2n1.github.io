---
title: "ntpq(8)"
name: "ntpq"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntpq/"
description: "ntpq – standard NTP query program"
---

<p>ntpq &#8211; standard NTP query program</p>
<h2>&nbsp;<wbr></h2>
<h2>Synopsis</h2>
<p><code>ntpq [-46dinp] [-c </code><i>command</i><code>] [</code><i>host</i><code>] [&#8230;]</code> </p>
<h2>Description</h2>
<p>The <code>ntpq</code> utility program is used to monitor NTP daemon <code>ntpd</code> operations and determine performance. It uses the standard NTP mode 6 control message formats defined in Appendix B of the NTPv3 specification RFC1305. The same formats are used in NTPv4, although some of the variable names have changed and new ones added. The description on this page is for the NTPv4 variables. The program can be run either in interactive mode or controlled using command line arguments. Requests to read and write arbitrary variables can be assembled, with raw and pretty-printed output options being available. The <code>ntpq</code> can also obtain and print a list of peers in a common format by sending multiple queries to the server. If one or more request options is included on the command line when <code>ntpq</code> is executed, each of the requests will be sent to the NTP servers running on each of the hosts given as command line arguments, or on localhost by default. If no request options are given, <code>ntpq</code> will attempt to read commands from the standard input and execute these on the NTP server running on the first host given on the command line, again defaulting to localhost when no other host is specified. <code>ntpq</code> will prompt for commands if the standard input is a terminal device. <code>ntpq</code> uses NTP mode 6 packets to communicate with the NTP server, and hence can be used to query any compatible server on the network which permits it. Note that since NTP is a UDP protocol this communication will be somewhat unreliable, especially over large distances in terms of network topology. <code>ntpq</code> makes one attempt to retransmit requests, and will time requests out if the remote host is not heard from within a suitable timeout time. Note that in contexts where a host name is expected, a <code>-4</code> qualifier preceding the host name forces DNS resolution to the IPv4 namespace, while a <code>-6</code> qualifier forces DNS resolution to the IPv6 namespace. For examples and usage, see the NTP Debugging Techniques page. Command line options are described following. Specifying a command line option other than <code>-i</code> or <code>-n</code> will cause the specified query (queries) to be sent to the indicated host(s) immediately. Otherwise, <code>ntpq</code> will attempt to read interactive format commands from the standard input.</p>
<dl>
<dd>
<dl>
<dt><code>-4</code></p>
<dd>Force DNS resolution of following host names on the command line to the IPv4 namespace.</p>
<dt><code>-6</code></p>
<dd>Force DNS resolution of following host names on the command line to the IPv6 namespace.</p>
<dt><code>-c</code></p>
<dd>The following argument is interpreted as an interactive format command and is added to the list of commands to be executed on the specified host(s). Multiple <code>-c</code> options may be given.</p>
<dt><code>-d</code></p>
<dd>Turn on debugging mode.</p>
<dt><code>-i</code></p>
<dd>Force <code>ntpq</code> to operate in interactive mode. Prompts will be written to the standard output and commands read from the standard input.</p>
<dt><code>-n</code></p>
<dd>Output all host addresses in dotted-quad numeric format rather than converting to the canonical host names.</p>
<dt><code>-p</code></p>
<dd>Print a list of the peers known to the server as well as a summary of their state. This is equivalent to the <code>peers</code> interactive command.</dl>
</dl>
<h2>Internal Commands</h2>
<p>Interactive format commands consist of a keyword followed by zero to four arguments. Only enough characters of the full keyword to uniquely identify the command need be typed. The output of a command is normally sent to the standard output, but optionally the output of individual commands may be sent to a file by appending a <code>&gt;</code>, followed by a file name, to the command line. A number of interactive format commands are executed entirely within the <code>ntpq</code> program itself and do not result in NTP mode-6 requests being sent to a server. These are described following. </p>
<dl>
<dd>
<dl>
<dt><code>? [</code><i>command_keyword</i><code>]</code></p>
<dd>
<dt><code>help [</code><i>command_keyword</i><code>]</code></p>
<dd>A <code>?</code> by itself will print a list of all the command keywords known to <code>ntpq</code>46 A <code>?</code> followed by a command keyword will print function and usage information about the command.</p>
<dt><code>addvars </code><i>name</i><code> [ = </code><i>value</i><code>] [&#8230;]</code></p>
<dd>
<dt><code>rmvars </code><i>name</i><code> [&#8230;]</code></p>
<dd>
<dt><code>clearvars</code></p>
<dd>The arguments to this command consist of a list of items of the form <i>name</i><code> = </code><i>value</i>, where the <code>= </code><i>value</i> is ignored, and can be omitted in read requests. <code>ntpq</code> maintains an internal list in which data to be included in control messages can be assembled, and sent using the <code>readlist</code> and <code>writelist</code> commands described below. The <code>addvars</code> command allows variables and optional values to be added to the list. If more than one variable is to be added, the list should be comma-separated and not contain white space. The <code>rmvars</code> command can be used to remove individual variables from the list, while the <code>clearlist</code> command removes all variables from the list.</p>
<dt><code>cooked</code></p>
<dd>Display server messages in prettyprint format.</p>
<dt><code>debug more | less | off</code></p>
<dd>Turns internal query program debugging on and off.</p>
<dt><code>delay </code><i>milliseconds</i></p>
<dd>Specify a time interval to be added to timestamps included in requests which require authentication. This is used to enable (unreliable) server reconfiguration over long delay network paths or between machines whose clocks are unsynchronized. Actually the server does not now require timestamps in authenticated requests, so this command may be obsolete.</p>
<dt><code>host </code><i>name</i></p>
<dd>Set the host to which future queries will be sent. The name may be either a DNS name or a numeric address.</p>
<dt><code>hostnames [yes | no]</code></p>
<dd>If <code>yes</code> is specified, host names are printed in information displays. If <code>no</code> is specified, numeric addresses are printed instead. The default is <code>yes</code>, unless modified using the command line <code>-n</code> switch.</p>
<dt><code>keyid </code><i>keyid</i></p>
<dd>This command specifies the key number to be used to authenticate configuration requests. This must correspond to a key number the server has been configured to use for this purpose.</p>
<dt><code>ntpversion 1 | 2 | 3 | 4</code></p>
<dd>Sets the NTP version number which <code>ntpq</code> claims in packets. Defaults to 2, Note that mode-6 control messages (and modes, for that matter) didn&#8217;t exist in NTP version 1.</p>
<dt><code>passwd</code></p>
<dd>This command prompts for a password to authenticate configuration requests. The password must correspond to the key configured for NTP server for this purpose.</p>
<dt><code>quit</code></p>
<dd>Exit <code>ntpq</code>46</p>
<dt><code>raw</code></p>
<dd>Display server messages as received and without reformatting.</p>
<dt><code>timeout </code><i>milliseconds</i></p>
<dd>Specify a timeout period for responses to server queries. The default is about 5000 milliseconds. Note that since <code>ntpq</code> retries each query once after a timeout, the total waiting time for a timeout will be twice the timeout value set.</dl>
</dl>
<h2>Control Message Commands</h2>
<p>Association IDs are used to identify system, peer and clock variables. System variables are assigned an association ID of zero and system name space, while each association is assigned a nonzero association ID and peer namespace. Most control commands send a single mode-6 message to the server and expect a single response message. The exceptions are the <code>peers</code> command, which sends a series of messages, and the <code>mreadlist</code> and <code>mreadvar</code> commands, which iterate over a range of associations. </p>
<dl>
<dd>
<dl>
<dt><code>associations</code></p>
<dd>Display a list of mobilized associations in the form <code>ind assid status conf reach auth condition last_event cnt</code> </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>Variable </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td><code>ind</code> </td>
<td> index on this list
</td>
</tr>
<tr VALIGN=top>
<td><code>assid</code> </td>
<td> association ID
</td>
</tr>
<tr VALIGN=top>
<td><code>status</code> </td>
<td> peer status word
</td>
</tr>
<tr VALIGN=top>
<td><code>conf</code> </td>
<td> <code>yes</code>: persistent, <code>no</code>: ephemeral
</td>
</tr>
<tr VALIGN=top>
<td><code>reach</code> </td>
<td> <code>yes</code>: reachable, <code>no</code>: unreachable
</td>
</tr>
<tr VALIGN=top>
<td><code>auth</code> </td>
<td> <code>ok</code>, <code>yes</code>, <code>bad</code> and <code>none</code>
</td>
</tr>
<tr VALIGN=top>
<td><code>condition</code> </td>
<td> selection status (see the <code>select</code> field of the peer status word)
</td>
</tr>
<tr VALIGN=top>
<td><code>last_event</code> </td>
<td> event report (see the <code>event</code> field of the peer status word)
</td>
</tr>
<tr VALIGN=top>
<td><code>cnt</code> </td>
<td> event count (see the <code>count</code> field of the peer status word)
</td>
</tr>
</table>
<dt><code>clockvar </code><i>assocID</i><code> [</code><i>name</i><code> [ = </code><i>value</i><code> [&#8230;]] [&#8230;]</code></p>
<dd>
<dt><code>cv </code><i>assocID</i><code> [</code><i>name</i><code> [ = </code><i>value</i><code> [&#8230;] ][&#8230;]</code></p>
<dd>Display a list of clock variables for those assocations supporting a reference clock.</p>
<dt><code>:config [&#8230;]</code></p>
<dd>Send the remainder of the command line, including whitespace, to the server as a run-time configuration command in the same format as the configuration file. This command is experimental until further notice and clarification. Authentication is of course required.</p>
<dt><code>config-from-file </code><i>filename</i></p>
<dd>Send the each line of <i>filename</i> to the server as run-time configuration commands in the same format as the configuration file. This command is experimental until further notice and clarification. Authentication is of course required.</p>
<dt><code>keyid</code></p>
<dd>Specify the key ID to use for write requests.</p>
<dt><code>lassociations</code></p>
<dd>Perform the same function as the associations command, execept display mobilized and unmobilized associations.</p>
<dt><code>mreadvar </code><i>assocID</i><i>assocID</i><code> [ </code><i>variable_name</i><code> [ = </code><i>value</i><code>[ &#8230; ]</code></p>
<dd>
<dt><code>mrv </code><i>assocID</i><i>assocID</i><code> [ </code><i>variable_name</i><code> [ = </code><i>value</i><code>[ &#8230; ]</code></p>
<dd>Perform the same function as the <code>readvar</code> command, except for a range of association IDs. This range is determined from the association list cached by the most recent <code>associations</code> command.</p>
<dt><code>passociations</code></p>
<dd>Perform the same function as the <code>associations command</code>, except that it uses previously stored data rather than making a new query.</p>
<dt><code>passwd</code></p>
<dd>Specify the password to use for write requests.</p>
<dt><code>peers</code></p>
<dd>Display a list of peers in the form <code>[tally]remote refid st t when pool reach delay offset jitter</code> </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>Variable </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td><code>[tally]</code> </td>
<td> single-character code indicating current value of the <code>select</code> field of the peer status word
</td>
</tr>
<tr VALIGN=top>
<td><code>remote</code> </td>
<td> host name (or IP number) of peer
</td>
</tr>
<tr VALIGN=top>
<td><code>refid</code> </td>
<td> association ID or kiss code
</td>
</tr>
<tr VALIGN=top>
<td><code>st</code> </td>
<td> stratum
</td>
</tr>
<tr VALIGN=top>
<td><code>t</code> </td>
<td> <code>u</code>: unicast, <code>b</code>: broadcast, <code>l</code>: local
</td>
</tr>
<tr VALIGN=top>
<td><code>when</code> </td>
<td> sec/min/hr since last received packet
</td>
</tr>
<tr VALIGN=top>
<td><code>poll</code> </td>
<td> poll interval (log2 s)
</td>
</tr>
<tr VALIGN=top>
<td><code>reach</code> </td>
<td> reach shift register (octal)
</td>
</tr>
<tr VALIGN=top>
<td><code>delay</code> </td>
<td> roundtrip delay
</td>
</tr>
<tr VALIGN=top>
<td><code>offset</code> </td>
<td> offset
</td>
</tr>
<tr VALIGN=top>
<td><code>jitter</code> </td>
<td> jitter
</td>
</tr>
</table>
<dt><code>readvar </code><i>assocID</i><i>name</i><code> [ = </code><i>value</i><code> ] [,&#8230;]</code></p>
<dd>
<dt><code>rv </code><i>assocID</i><code> [ </code><i>name</i><code> ] [,&#8230;]</code></p>
<dd>Display the specified variables. If <i>assocID</i> is zero, the variables are from the system variables name space, otherwise they are from the peer variables name space. The <i>assocID</i> is required, as the same name can occur in both spaces. If no <i>name</i> is included, all operative variables in the name space are displayed. In this case only, if the <i>assocID</i> is omitted, it is assumed zero. Multiple names are specified with comma separators and without whitespace. Note that time values are represented in milliseconds and frequency values in parts-per-million (PPM). Some NTP timestamps are represented in the format YYYYMMDDTTTT, where YYYY is the year, MM the month of year, DD the day of month and TTTT the time of day.</p>
<dt><code>saveconfig </code><i>filename</i></p>
<dd>Write the current configuration, including any runtime modifications given with <code>:config</code> or <code>config-from-file</code>, to the ntpd host&#8217;s file <i>filename</i>46 This command will be rejected by the server unless saveconfigdir appears in the <code>ntpd</code> configuration file. <i>filename</i> can use strftime() format specifiers to substitute the current date and time, for example, <code>saveconfig ntp-%Y%m%d-%H%M%S.conf</code>46 The filename used is stored in system variable <code>savedconfig</code>46 Authentication is required.</p>
<dt><code>writevar </code><i>assocID</i><i>name</i><code> = </code><i>value</i><code> [,&#8230;]</code></p>
<dd>Write the specified variables. If the <i>assocID</i> is zero, the variables are from the system variables name space, otherwise they are from the peer variables name space. The <i>assocID</i> is required, as the same name can occur in both spaces.</dl>
</dl>
<h2>Status Words And Kiss Codes</h2>
<p>The current state of the operating program is shown in a set of status words maintained by the system and each association separately. These words are displayed in the <code>rv</code> and <code>as</code> commands both in hexadecimal and decoded short tip strings. The codes, tips and short explanations are on the Event Messages and Status Words page. The page also includes a list of system and peer messages, the code for the latest of which is included in the status word. </p>
<p> Information resulting from protocol machine state transitions is displayed using an informal set of ASCII strings called kiss codes46 The original purpose was for kiss-o&#8217;-death (KoD) packets sent by the server to advise the client of an unusual condition. They are now displayed, when appropriate, in the reference identifier field in various billboards.</p>
<h2>System Variables</h2>
<p>The following system variables appear in the <code>rv</code> billboard. Not all variables are displayed in some configurations. </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>Variable </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td><code>status</code> </td>
<td> system status word
</td>
</tr>
<tr VALIGN=top>
<td><code>version</code> </td>
<td> NTP software version and build time
</td>
</tr>
<tr VALIGN=top>
<td><code>processor</code> </td>
<td> hardware platform and version
</td>
</tr>
<tr VALIGN=top>
<td><code>system</code> </td>
<td> operating system and version
</td>
</tr>
<tr VALIGN=top>
<td><code>leap</code> </td>
<td> leap warning indicator (0-3)
</td>
</tr>
<tr VALIGN=top>
<td><code>stratum</code> </td>
<td> stratum (1-15)
</td>
</tr>
<tr VALIGN=top>
<td><code>precision</code> </td>
<td> precision (log2 s)
</td>
</tr>
<tr VALIGN=top>
<td><code>rootdelay</code> </td>
<td> total roundtrip delay to the primary reference clock
</td>
</tr>
<tr VALIGN=top>
<td><code>rootdisp</code> </td>
<td> total dispersion to the primary reference clock
</td>
</tr>
<tr VALIGN=top>
<td><code>peer</code> </td>
<td> system peer association ID
</td>
</tr>
<tr VALIGN=top>
<td><code>tc</code> </td>
<td> time constant and poll exponent (log2 s) (3-17)
</td>
</tr>
<tr VALIGN=top>
<td><code>mintc</code> </td>
<td> minimum time constant (log2 s) (3-10)
</td>
</tr>
<tr VALIGN=top>
<td><code>clock</code> </td>
<td> date and time of day
</td>
</tr>
<tr VALIGN=top>
<td><code>refid</code> </td>
<td> reference ID or kiss code
</td>
</tr>
<tr VALIGN=top>
<td><code>reftime</code> </td>
<td> reference time
</td>
</tr>
<tr VALIGN=top>
<td><code>offset</code> </td>
<td> combined time offset
</td>
</tr>
<tr VALIGN=top>
<td><code>sys_jitter</code> </td>
<td> combined system jitter
</td>
</tr>
<tr VALIGN=top>
<td><code>frequency</code> </td>
<td> clock frequency offset (PPM)
</td>
</tr>
<tr VALIGN=top>
<td><code>clk_wander</code> </td>
<td> clock frequency wander (PPM)
</td>
</tr>
<tr VALIGN=top>
<td><code>clk_jitter</code> </td>
<td> clock jitter
</td>
</tr>
<tr VALIGN=top>
<td><code>tai</code> </td>
<td> TAI-UTC offset (s)
</td>
</tr>
<tr VALIGN=top>
<td><code>leapsec</code> </td>
<td> NTP seconds when the next leap second is/was inserted
</td>
</tr>
<tr VALIGN=top>
<td><code>expire</code> </td>
<td> NTP seconds when the NIST leapseconds file expires
</td>
</tr>
</table>
<dl>
<dd>
<dl>
<dt>The jitter and wander statistics are exponentially-weighted RMS averages. The system jitter is defined in the NTPv4 specification; the clock jitter statistic is computed by the clock discipline module.</p>
<dd>
<dt>When the NTPv4 daemon is compiled with the OpenSSL software library, additional system variables are displayed, including some or all of the following, depending on the particular Autokey dance:</p>
<dd></dl>
</dl>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>Variable </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td><code>host</code> </td>
<td> Autokey host name
</td>
</tr>
<tr VALIGN=top>
<td><code>group</code> </td>
<td> Autokey group name
</td>
</tr>
<tr VALIGN=top>
<td><code>flags</code> </td>
<td> host flags (see Autokey specification)
</td>
</tr>
<tr VALIGN=top>
<td><code>digest</code> </td>
<td> OpenSSL message digest algorithm
</td>
</tr>
<tr VALIGN=top>
<td><code>signature</code> </td>
<td> OpenSSL digest/signature scheme
</td>
</tr>
<tr VALIGN=top>
<td><code>update</code> </td>
<td> NTP seconds at last signature update
</td>
</tr>
<tr VALIGN=top>
<td><code>cert</code> </td>
<td> certificate subject, issuer and certificate flags
</td>
</tr>
<tr VALIGN=top>
<td><code>until</code> </td>
<td> NTP seconds when the certificate expires
</td>
</tr>
</table>
<h2>Peer Variables</h2>
<p>The following system variables apear in the <code>rv</code> billboard for each association. Not all variables are displayed in some configurations. </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>Variable </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td><code>associd</code> </td>
<td> association ID
</td>
</tr>
<tr VALIGN=top>
<td><code>status</code> </td>
<td> peer status word
</td>
</tr>
<tr VALIGN=top>
<td><code>srcadr srcport</code> </td>
<td> source (remote) IP address and port
</td>
</tr>
<tr VALIGN=top>
<td><code>dstadr dstport</code> </td>
<td> destination (local) IP address and port
</td>
</tr>
<tr VALIGN=top>
<td><code>leap</code> </td>
<td> leap indicator (0-3)
</td>
</tr>
<tr VALIGN=top>
<td><code>stratum</code> </td>
<td> stratum (0-15)
</td>
</tr>
<tr VALIGN=top>
<td><code>precision</code> </td>
<td> precision (log2 s)
</td>
</tr>
<tr VALIGN=top>
<td><code>rootdelay</code> </td>
<td> total roundtrip delay to the primary reference clock
</td>
</tr>
<tr VALIGN=top>
<td><code>rootdisp</code> </td>
<td> total root dispersion to the primary reference clock
</td>
</tr>
<tr VALIGN=top>
<td><code>refid</code> </td>
<td> reference ID or kiss code
</td>
</tr>
<tr VALIGN=top>
<td><code>reftime</code> </td>
<td> reference time
</td>
</tr>
<tr VALIGN=top>
<td><code>reach</code> </td>
<td> reach register (octal)
</td>
</tr>
<tr VALIGN=top>
<td><code>unreach</code> </td>
<td> unreach counter
</td>
</tr>
<tr VALIGN=top>
<td><code>hmode</code> </td>
<td> host mode (1-6)
</td>
</tr>
<tr VALIGN=top>
<td><code>pmode</code> </td>
<td> peer mode (1-5)
</td>
</tr>
<tr VALIGN=top>
<td><code>hpoll</code> </td>
<td> host poll exponent (log2 s) (3-17)
</td>
</tr>
<tr VALIGN=top>
<td><code>ppoll</code> </td>
<td> peer poll exponent (log2 s) (3-17)
</td>
</tr>
<tr VALIGN=top>
<td><code>headway</code> </td>
<td> headway (see Rate Management and the Kiss-o&#8217;-Death Packet)
</td>
</tr>
<tr VALIGN=top>
<td><code>flash</code> </td>
<td> flash status word
</td>
</tr>
<tr VALIGN=top>
<td><code>offset</code> </td>
<td> filter offset
</td>
</tr>
<tr VALIGN=top>
<td><code>delay</code> </td>
<td> filter delay
</td>
</tr>
<tr VALIGN=top>
<td><code>dispersion</code> </td>
<td> filter dispersion
</td>
</tr>
<tr VALIGN=top>
<td><code>jitter</code> </td>
<td> filter jitter
</td>
</tr>
<tr VALIGN=top>
<td><code>bias</code> </td>
<td> unicast/broadcast bias
</td>
</tr>
<tr VALIGN=top>
<td><code>xleave</code> </td>
<td> interleave delay (see NTP Interleaved Modes)
</td>
</tr>
</table>
<p> The bias vaqriable is calculated when the first broadcast packet is received after the calibration volley. It represents the offset of the broadcast subgraph relative to the unicast subgraph. The xleave variable appears only the interleaved symmetric and ingterleaved modes. It represents the internal queueing, buffering and transmission delays for the preceeding packet. </p>
<p> When the NTPv4 daemon is compiled with the OpenSSL software library, additional peer variables are displayed, including the following: </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>Variable </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td><code>flags</code> </td>
<td> peer flags (see Autokey specification)
</td>
</tr>
<tr VALIGN=top>
<td><code>host</code> </td>
<td> Autokey server name
</td>
</tr>
<tr VALIGN=top>
<td><code>flags</code> </td>
<td> peer flags (see Autokey specification)
</td>
</tr>
<tr VALIGN=top>
<td><code>signature</code> </td>
<td> OpenSSL digest/signature shceme
</td>
</tr>
<tr VALIGN=top>
<td><code>initsequence</code> </td>
<td> initial key ID
</td>
</tr>
<tr VALIGN=top>
<td><code>initkey</code> </td>
<td> initial key index
</td>
</tr>
<tr VALIGN=top>
<td><code>timestamp</code> </td>
<td> Autokey signature timestamp
</td>
</tr>
</table>
<h2>Clock Variables</h2>
<p>The following clock variables apear in the <code>cv</code> billboard for each association with a reference clock. Not all variables are displayed in some configurations. </p>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>Variable </td>
<td> Description
</td>
</tr>
<tr VALIGN=top>
<td><code>associd</code> </td>
<td> association ID
</td>
</tr>
<tr VALIGN=top>
<td><code>status</code> </td>
<td> clock status word
</td>
</tr>
<tr VALIGN=top>
<td><code>device</code> </td>
<td> device description
</td>
</tr>
<tr VALIGN=top>
<td><code>timecode</code> </td>
<td> ASCII timecode string (specific to device)
</td>
</tr>
<tr VALIGN=top>
<td><code>poll</code> </td>
<td> poll messages sent
</td>
</tr>
<tr VALIGN=top>
<td><code>noreply</code> </td>
<td> no reply
</td>
</tr>
<tr VALIGN=top>
<td><code>badformat</code> </td>
<td> bad format
</td>
</tr>
<tr VALIGN=top>
<td><code>baddata</code> </td>
<td> bad date or time
</td>
</tr>
<tr VALIGN=top>
<td><code>fudgetime1</code> </td>
<td> fudge time 1
</td>
</tr>
<tr VALIGN=top>
<td><code>fudgetime2</code> </td>
<td> fudge time 2
</td>
</tr>
<tr VALIGN=top>
<td><code>stratum</code> </td>
<td> driver stratum
</td>
</tr>
<tr VALIGN=top>
<td><code>refid</code> </td>
<td> driver reference ID
</td>
</tr>
<tr VALIGN=top>
<td><code>flags</code> </td>
<td> driver flags
</td>
</tr>
</table>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-ntp_decode/">ntp_decode</a>(5), <a href="/docs/linux/man/8-ntpd/">ntpd</a>(8), <a href="/docs/linux/man/8-ntpdc/">ntpdc</a>(8) The official HTML documentation. This file was automatically generated from HTML source. </p>
