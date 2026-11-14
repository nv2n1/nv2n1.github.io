---
title: "chronyc(1)"
name: "chronyc"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chronyc/"
description: "chronyc – command-line interface for chrony daemon"
---

<h2 class="name">NAME</h2>
<p> chronyc &#8211; command-line interface for chrony daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>chronyc</code> [<i>OPTION</i>]&#8230; [<i>COMMAND</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>chronyc</code> is a command-line interface program which can be used to monitor <code>chronyd</code>&#8216;s performance and to change various operating parameters whilst it is running. </p>
<p> If no commands are specified on the command line, <code>chronyc</code> will expect input from the user. The prompt <i>chronyc&gt;</i> will be displayed when it is being run from a terminal. If <code>chronyc</code>&#8216;s input or output are redirected from or to a file, the prompt is not shown. </p>
<p> There are two ways <code>chronyc</code> can access <code>chronyd</code>. One is the Internet Protocol (IPv4 or IPv6) and the other is a Unix domain socket, which is accessible locally by the root or <i>chrony</i> user. By default, <code>chronyc</code> first tries to connect to the Unix domain socket. The compiled-in default path is <i>/var/run/chrony/chronyd.sock</i>. If that fails (e.g. because <code>chronyc</code> is running under a non-root user), it will try to connect to 127.0.0.1 and then ::1. </p>
<p> Only the following monitoring commands, which do not affect the behaviour of <code>chronyd</code>, are allowed from the network: <code>activity</code>, <code>manual list</code>, <code>rtcdata</code>, <code>smoothing</code>, <code>sources</code>, <code>sourcestats</code>, <code>tracking</code>, <code>waitsync</code>. The set of hosts from which <code>chronyd</code> will accept these commands can be configured with the <code>cmdallow</code> directive in the <code>chronyd</code>&#8216;s configuration file or the <code>cmdallow</code> command in <code>chronyc</code>. By default, the commands are accepted only from localhost (127.0.0.1 or ::1). </p>
<p> All other commands are allowed only through the Unix domain socket. When sent over the network, <code>chronyd</code> will respond with a &#8216;Not authorised&#8217; error, even if it is from localhost. In chrony versions before 2.2 they were allowed from the network if they were authenticated with a password, but that is no longer supported. </p>
<p> Having full access to <code>chronyd</code> via <code>chronyc</code> is more or less equivalent to being able to modify the <code>chronyd</code>&#8216;s configuration file and restart it.</p>
<h2>OPTIONS</h2>
<p> <code>-4</code></p>
<dl>
<dt>
<dd> With this option hostnames will be resolved only to IPv4 addresses.</dl>
<p> <code>-6</code></p>
<dl>
<dt>
<dd> With this option hostnames will be resolved only to IPv6 addresses.</dl>
<p> <code>-n</code></p>
<dl>
<dt>
<dd> This option disables resolving of IP addresses to hostnames, e.g. to avoid slow DNS lookups. Long addresses will not be truncated to fit into the column.</dl>
<p> <code>-c</code></p>
<dl>
<dt>
<dd> This option enables printing of reports in a comma-separated values (CSV) format. IP addresses will not be resolved to hostnames, time will be printed as number of seconds since the epoch and values in seconds will not be converted to other units.</dl>
<p> <code>-d</code></p>
<dl>
<dt>
<dd> This option enables printing of debugging messages if <code>chronyc</code> was compiled with debugging support.</dl>
<p> <code>-m</code></p>
<dl>
<dt>
<dd> Normally, all arguments on the command line are interpreted as one command. With this option multiple commands can be specified. Each argument will be interpreted as a whole command.</dl>
<p> <code>-h</code> <i>host</i></p>
<dl>
<dt>
<dd> This option allows the user to specify which host (or comma-separated list of addresses) running the <code>chronyd</code> program is to be contacted. This allows for remote monitoring, without having to connect over SSH to the other host first. </p>
<p> The default is to contact <code>chronyd</code> running on the same host where <code>chronyc</code> is being run.</dl>
<p> <code>-p</code> <i>port</i></p>
<dl>
<dt>
<dd> This option allows the user to specify the UDP port number which the target <code>chronyd</code> is using for its monitoring connections. This defaults to 323; there would rarely be a need to change this.</dl>
<p> <code>-f</code> <i>file</i></p>
<dl>
<dt>
<dd> This option is ignored and is provided only for compatibility.</dl>
<p> <code>-a</code></p>
<dl>
<dt>
<dd> This option is ignored and is provided only for compatibility.</dl>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> With this option <code>chronyc</code> displays its version number on the terminal and exits.</dl>
<h2>COMMANDS</h2>
<p> This section describes each of the commands available within the <code>chronyc</code> program.</p>
<h3>System clock</h3>
<p> <code>tracking</code></p>
<dl>
<dt>
<dd> The <code>tracking</code> command displays parameters about the system&#8217;s clock performance. An example of the output is shown below. </p>
<dl>
<dt>
<dd>
<pre>
Reference ID    : CB00710F (foo.example.net)
Stratum         : 3
Ref time (UTC)  : Fri Jan 27 09:49:17 2017
System time     : 0.000006523 seconds slow of NTP time
Last offset     : -0.000006747 seconds
RMS offset      : 0.000035822 seconds
Frequency       : 3.225 ppm slow
Residual freq   : -0.000 ppm
Skew            : 0.129 ppm
Root delay      : 0.013639022 seconds
Root dispersion : 0.001100737 seconds
Update interval : 64.2 seconds
Leap status     : Normal
</pre>
</dl>
<p> The fields are explained as follows: </p>
<p> <code>Reference ID</code></p>
<dl>
<dt>
<dd> This is the reference ID and name (or IP address) of the server to which the computer is currently synchronised. For IPv4 addresses, the reference ID is equal to the address and for IPv6 addresses it is the first 32 bits of the MD5 sum of the address. </p>
<p> If the reference ID is <i>7F7F0101</i> and there is no name or IP address, it means the computer is not synchronised to any external source and that you have the <i>local</i> mode operating (via the <code>local</code> command in <code>chronyc</code>, or the <code>local</code> directive in the configuration file). </p>
<p> The reference ID is printed as a hexadecimal number. Note that in older versions it used to be printed in quad-dotted notation and could be confused with an IPv4 address.</dl>
<p> <code>Stratum</code></p>
<dl>
<dt>
<dd> The stratum indicates how many hops away from a computer with an attached reference clock we are. Such a computer is a stratum-1 computer, so the computer in the example is two hops away (i.e. <i>foo.example.net</i> is a stratum-2 and is synchronised from a stratum-1).</dl>
<p> <code>Ref time</code></p>
<dl>
<dt>
<dd> This is the time (UTC) at which the last measurement from the reference source was processed.</dl>
<p> <code>System time</code></p>
<dl>
<dt>
<dd> In normal operation, <code>chronyd</code> by default never steps the system clock, because any jump in the time can have adverse consequences for certain application programs. Instead, any error in the system clock is corrected by slightly speeding up or slowing down the system clock until the error has been removed, and then returning to the system clock&#8217;s normal speed. A consequence of this is that there will be a period when the system clock (as read by other programs) will be different from <code>chronyd</code>&#8216;s estimate of the current true time (which it reports to NTP clients when it is operating in server mode). The value reported on this line is the difference due to this effect.</dl>
<p> <code>Last offset</code></p>
<dl>
<dt>
<dd> This is the estimated local offset on the last clock update.</dl>
<p> <code>RMS offset</code></p>
<dl>
<dt>
<dd> This is a long-term average of the offset value.</dl>
<p> <code>Frequency</code></p>
<dl>
<dt>
<dd> The &#8216;frequency&#8217; is the rate by which the system&#8217;s clock would be wrong if <code>chronyd</code> was not correcting it. It is expressed in ppm (parts per million). For example, a value of 1 ppm would mean that when the system&#8217;s clock thinks it has advanced 1 second, it has actually advanced by 1.000001 seconds relative to true time.</dl>
<p> <code>Residual freq</code></p>
<dl>
<dt>
<dd> This shows the &#8216;residual frequency&#8217; for the currently selected reference source. This reflects any difference between what the measurements from the reference source indicate the frequency should be and the frequency currently being used. </p>
<p> The reason this is not always zero is that a smoothing procedure is applied to the frequency. Each time a measurement from the reference source is obtained and a new residual frequency computed, the estimated accuracy of this residual is compared with the estimated accuracy (see &#8216;skew&#8217; next) of the existing frequency value. A weighted average is computed for the new frequency, with weights depending on these accuracies. If the measurements from the reference source follow a consistent trend, the residual will be driven to zero over time.</dl>
<p> <code>Skew</code></p>
<dl>
<dt>
<dd> This is the estimated error bound on the frequency.</dl>
<p> <code>Root delay</code></p>
<dl>
<dt>
<dd> This is the total of the network path delays to the stratum-1 computer from which the computer is ultimately synchronised.</dl>
<p> <code>Root dispersion</code></p>
<dl>
<dt>
<dd> This is the total dispersion accumulated through all the computers back to the stratum-1 computer from which the computer is ultimately synchronised. Dispersion is due to system clock resolution, statistical measurement variations, etc. </p>
<p> An absolute bound on the computer&#8217;s clock accuracy (assuming the stratum-1 computer is correct) is given by: </p>
<dl>
<dt>
<dd>
<pre>
clock_error &lt;= root_dispersion + (0.5 * |root_delay|)
</pre>
</dl>
</dl>
<p> <code>Update interval</code></p>
<dl>
<dt>
<dd> This is the interval between the last two clock updates.</dl>
<p> <code>Leap status</code></p>
<dl>
<dt>
<dd> This is the leap status, which can be <i>Normal</i>, <i>Insert second</i>, <i>Delete second</i> or <i>Not synchronised</i>.</dl>
</dl>
<p> <code>makestep</code>, <code>makestep</code> <i>threshold</i> <i>limit</i></p>
<dl>
<dt>
<dd> Normally <code>chronyd</code> will cause the system to gradually correct any time offset, by slowing down or speeding up the clock as required. In certain situations, the system clock might be so far adrift that this slewing process would take a very long time to correct the system clock. </p>
<p> The <code>makestep</code> command can be used in this situation. There are two forms of the command. The first form has no parameters. It tells <code>chronyd</code> to cancel any remaining correction that was being slewed and jump the system clock by the equivalent amount, making it correct immediately. </p>
<p> The second form configures the automatic stepping, similarly to the <code>makestep</code> directive. It has two parameters, stepping threshold (in seconds) and number of future clock updates for which the threshold will be active. This can be used with the <code>burst</code> command to quickly make a new measurement and correct the clock by stepping if needed, without waiting for <code>chronyd</code> to complete the measurement and update the clock. </p>
<dl>
<dt>
<dd>
<pre>
makestep 0.1 1
burst 1/2
</pre>
</dl>
<p> BE WARNED: Certain software will be seriously affected by such jumps in the system time. (That is the reason why <code>chronyd</code> uses slewing normally.)</dl>
<p> <code>maxupdateskew</code> <i>skew-in-ppm</i></p>
<dl>
<dt>
<dd> This command has the same effect as the <code>maxupdateskew</code> directive in the configuration file.</dl>
<p> <code>waitsync</code> [<i>max-tries</i> [<i>max-correction</i> [<i>max-skew</i> [<i>interval</i>]]]]</p>
<dl>
<dt>
<dd> The <code>waitsync</code> command waits for <code>chronyd</code> to synchronise. </p>
<p> Up to four optional arguments can be specified. The first is the maximum number of tries before giving up and returning a non-zero error code. When 0 is specified, or there are no arguments, the number of tries will not be limited. </p>
<p> The second and third arguments are the maximum allowed remaining correction of the system clock and the maximum allowed skew (in ppm) as reported by the <code>tracking</code> command in the <code>System time</code> and <code>Skew</code> fields. If not specified or zero, the value will not be checked. </p>
<p> The fourth argument is the interval specified in seconds in which the check is repeated. The interval is 10 seconds by default. </p>
<p> An example is: </p>
<dl>
<dt>
<dd>
<pre>
waitsync 60 0.01
</pre>
</dl>
<p> which will wait up to about 10 minutes (60 times 10 seconds) for <code>chronyd</code> to synchronise to a source and the remaining correction to be less than 10 milliseconds.</dl>
<h3>Time sources</h3>
<p> <code>sources</code> [<code>-v</code>]</p>
<dl>
<dt>
<dd> This command displays information about the current time sources that <code>chronyd</code> is accessing. </p>
<p> The optional argument <code>-v</code> can be specified, meaning <i>verbose</i>. In this case, extra caption lines are shown as a reminder of the meanings of the columns. </p>
<dl>
<dt>
<dd>
<pre><code>
210 Number of sources = 3 MS Name / IP address Stratum Poll Reach LastRx Last sample == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
#* GPS0 0 4 377 11 - 479ns [- 621ns] + / - 134ns
                                                                                                                                                                                                              ^? foo.example.net 2 6 377 23 - 923us [-924us] + / -43ms ^ +bar.example.net 1 6 377 21 - 2629us [-2619us] + / -86ms
</code></pre>
</dl>
<p> The columns are as follows: </p>
<p> <code>M</code></p>
<dl>
<dt>
<dd> This indicates the mode of the source. <i>^</i> means a server, <i>=</i> means a peer and <i>#</i> indicates a locally connected reference clock.</dl>
<p> <code>S</code></p>
<dl>
<dt>
<dd> This column indicates the state of the source. </p>
<dl>
<dt>
<dd> &bull; <i>*</i> indicates the source to which <code>chronyd</code> is currently synchronised.</dl>
<dl>
<dt>
<dd> &bull; <i>+</i> indicates acceptable sources which are combined with the selected source.</dl>
<dl>
<dt>
<dd> &bull; <i>&#8211;</i> indicates acceptable sources which are excluded by the combining algorithm.</dl>
<dl>
<dt>
<dd> &bull; <i>?</i> indicates sources to which connectivity has been lost or whose packets do not pass all tests. It is also shown at start-up, until at least 3 samples have been gathered from it.</dl>
<dl>
<dt>
<dd> &bull; <i>x</i> indicates a clock which <code>chronyd</code> thinks is a falseticker (i.e. its time is inconsistent with a majority of other sources).</dl>
<dl>
<dt>
<dd> &bull; <i>~</i> indicates a source whose time appears to have too much variability.</dl>
</dl>
<p> <code>Name/IP address</code></p>
<dl>
<dt>
<dd> This shows the name or the IP address of the source, or reference ID for reference clocks.</dl>
<p> <code>Stratum</code></p>
<dl>
<dt>
<dd> This shows the stratum of the source, as reported in its most recently received sample. Stratum 1 indicates a computer with a locally attached reference clock. A computer that is synchronised to a stratum 1 computer is at stratum 2. A computer that is synchronised to a stratum 2 computer is at stratum 3, and so on.</dl>
<p> <code>Poll</code></p>
<dl>
<dt>
<dd> This shows the rate at which the source is being polled, as a base-2 logarithm of the interval in seconds. Thus, a value of 6 would indicate that a measurement is being made every 64 seconds. <code>chronyd</code> automatically varies the polling rate in response to prevailing conditions.</dl>
<p> <code>Reach</code></p>
<dl>
<dt>
<dd> This shows the source&#8217;s reachability register printed as an octal number. The register has 8 bits and is updated on every received or missed packet from the source. A value of 377 indicates that a valid reply was received for all from the last eight transmissions.</dl>
<p> <code>LastRx</code></p>
<dl>
<dt>
<dd> This column shows how long ago the last sample was received from the source. This is normally in seconds. The letters <i>m</i>, <i>h</i>, <i>d</i> or <i>y</i> indicate minutes, hours, days, or years.</dl>
<p> <code>Last sample</code></p>
<dl>
<dt>
<dd> This column shows the offset between the local clock and the source at the last measurement. The number in the square brackets shows the actual measured offset. This can be suffixed by <i>ns</i> (indicating nanoseconds), <i>us</i> (indicating microseconds), <i>ms</i> (indicating milliseconds), or <i>s</i> (indicating seconds). The number to the left of the square brackets shows the original measurement, adjusted to allow for any slews applied to the local clock since. The number following the <i>+/-</i> indicator shows the margin of error in the measurement. Positive offsets indicate that the local clock is ahead of the source.</dl>
</dl>
<p> <code>sourcestats</code> [<code>-v</code>]</p>
<dl>
<dt>
<dd> The <code>sourcestats</code> command displays information about the drift rate and offset estimation process for each of the sources currently being examined by <code>chronyd</code>. </p>
<p> The optional argument <code>-v</code> can be specified, meaning <i>verbose</i>. In this case, extra caption lines are shown as a reminder of the meanings of the columns. </p>
<p> An example report is: </p>
<dl>
<dt>
<dd>
210 Number of sources = 1 Name / IP Address NP NR Span Frequency Freq Skew Offset Std Dev == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =<br />
                                                                                                                                                                                                                   foo.example.net 11 5 46m &#8211; 0.001 0.045 1us 25us
</dl>
<p> The columns are as follows: </p>
<p> <code>Name/IP Address</code></p>
<dl>
<dt>
<dd> This is the name or IP address of the NTP server (or peer) or reference ID of the reference clock to which the rest of the line relates.</dl>
<p> <code>NP</code></p>
<dl>
<dt>
<dd> This is the number of sample points currently being retained for the server. The drift rate and current offset are estimated by performing a linear regression through these points.</dl>
<p> <code>NR</code></p>
<dl>
<dt>
<dd> This is the number of runs of residuals having the same sign following the last regression. If this number starts to become too small relative to the number of samples, it indicates that a straight line is no longer a good fit to the data. If the number of runs is too low, <code>chronyd</code> discards older samples and re-runs the regression until the number of runs becomes acceptable.</dl>
<p> <code>Span</code></p>
<dl>
<dt>
<dd> This is the interval between the oldest and newest samples. If no unit is shown the value is in seconds. In the example, the interval is 46 minutes.</dl>
<p> <code>Frequency</code></p>
<dl>
<dt>
<dd> This is the estimated residual frequency for the server, in parts per million. In this case, the computer&#8217;s clock is estimated to be running 1 part in 10^9 slow relative to the server.</dl>
<p> <code>Freq Skew</code></p>
<dl>
<dt>
<dd> This is the estimated error bounds on <code>Freq</code> (again in parts per million).</dl>
<p> <code>Offset</code></p>
<dl>
<dt>
<dd> This is the estimated offset of the source.</dl>
<p> <code>Std Dev</code></p>
<dl>
<dt>
<dd> This is the estimated sample standard deviation.</dl>
</dl>
<p> <code>reselect</code></p>
<dl>
<dt>
<dd> To avoid excessive switching between sources, <code>chronyd</code> can stay synchronised to a source even when it is not currently the best one among the available sources. </p>
<p> The <code>reselect</code> command can be used to force <code>chronyd</code> to reselect the best synchronisation source.</dl>
<p> <code>reselectdist</code> <i>distance</i></p>
<dl>
<dt>
<dd> The <code>reselectdist</code> command sets the reselection distance. It is equivalent to the <code>reselectdist</code> directive in the configuration file.</dl>
<h3>NTP sources</h3>
<p> <code>activity</code></p>
<dl>
<dt>
<dd> This command reports the number of servers and peers that are online and offline. If the <code>auto_offline</code> option is used in specifying some of the servers or peers, the <code>activity</code> command can be useful for detecting when all of them have entered the offline state after the network link has been disconnected. </p>
<p> The report shows the number of servers and peers in 5 states: </p>
<p> <code>online</code></p>
<dl>
<dt>
<dd> the server or peer is currently online (i.e. assumed by <code>chronyd</code> to be reachable)</dl>
<p> <code>offline</code></p>
<dl>
<dt>
<dd> the server or peer is currently offline (i.e. assumed by <code>chronyd</code> to be unreachable, and no measurements from it will be attempted.)</dl>
<p> <code>burst_online</code></p>
<dl>
<dt>
<dd> a burst command has been initiated for the server or peer and is being performed; after the burst is complete, the server or peer will be returned to the online state.</dl>
<p> <code>burst_offline</code></p>
<dl>
<dt>
<dd> a burst command has been initiated for the server or peer and is being performed; after the burst is complete, the server or peer will be returned to the offline state.</dl>
<p> <code>unresolved</code></p>
<dl>
<dt>
<dd> the name of the server or peer was not resolved to an address yet; this source is not visible in the <code>sources</code> and <code>sourcestats</code> reports.</dl>
</dl>
<p> <code>ntpdata</code> [<i>address</i>]</p>
<dl>
<dt>
<dd> The <code>ntpdata</code> command displays the last valid measurement and other NTP-specific information about the specified NTP source, or all NTP sources if no address was specified. An example of the output is shown below. </p>
<dl>
<dt>
<dd>
<pre>
Remote address  : 203.0.113.15 (CB00710F)
Remote port     : 123
Local address   : 203.0.113.74 (CB00714A)
Leap status     : Normal
Version         : 4
Mode            : Server
Stratum         : 1
Poll interval   : 10 (1024 seconds)
Precision       : -24 (0.000000060 seconds)
Root delay      : 0.000015 seconds
Root dispersion : 0.000015 seconds
Reference ID    : 47505300 (GPS)
Reference time  : Fri Nov 25 15:22:12 2016
Offset          : -0.000060878 seconds
Peer delay      : 0.000175634 seconds
Peer dispersion : 0.000000681 seconds
Response time   : 0.000053050 seconds
Jitter asymmetry: +0.00
NTP tests       : 111 111 1111
Interleaved     : No
Authenticated   : No
TX timestamping : Kernel
RX timestamping : Kernel
Total TX        : 24
Total RX        : 24
Total valid RX  : 24
</pre>
</dl>
<p> The fields are explained as follows: </p>
<p> <code>Remote address</code></p>
<dl>
<dt>
<dd> The IP address of the NTP server or peer, and the corresponding reference ID.</dl>
<p> <code>Remote port</code></p>
<dl>
<dt>
<dd> The UDP port number to which the request was sent. The standard NTP port is 123.</dl>
<p> <code>Local address</code></p>
<dl>
<dt>
<dd> The local IP address which received the response, and the corresponding reference ID.</dl>
<p> <code>Leap status</code>, <code>Version</code>, <code>Mode</code>, <code>Stratum</code>, <code>Poll interval</code>, <code>Precision</code>, <code>Root delay</code>, <code>Root dispersion</code>, <code>Reference ID</code>, <code>Reference time</code></p>
<dl>
<dt>
<dd> The NTP values from the last valid response.</dl>
<p> <code>Offset</code>, <code>Peer delay</code>, <code>Peer dispersion</code></p>
<dl>
<dt>
<dd> The measured values.</dl>
<p> <code>Response time</code></p>
<dl>
<dt>
<dd> The time the server or peer spent in processing of the request and waiting before sending the response.</dl>
<p> <code>Jitter asymmetry</code></p>
<dl>
<dt>
<dd> The estimated asymmetry of network jitter on the path to the source. The asymmetry can be between -0.5 and 0.5. A negative value means the delay of packets sent to the source is more variable than the delay of packets sent from the source back.</dl>
<p> <code>NTP tests</code></p>
<dl>
<dt>
<dd> Results of RFC 5905 tests 1 through 3, 5 through 7, and tests for maximum delay, delay ratio, delay dev ratio, and synchronisation loop.</dl>
<p> <code>Interleaved</code></p>
<dl>
<dt>
<dd> This shows if the response was in the interleaved mode.</dl>
<p> <code>Authenticated</code></p>
<dl>
<dt>
<dd> This shows if the response was authenticated.</dl>
<p> <code>TX timestamping</code></p>
<dl>
<dt>
<dd> The source of the local transmit timestamp. Valid values are <i>Daemon</i>, <i>Kernel</i>, and <i>Hardware</i>.</dl>
<p> <code>RX timestamping</code></p>
<dl>
<dt>
<dd> The source of the local receive timestamp.</dl>
<p> <code>Total TX</code></p>
<dl>
<dt>
<dd> The number of packets sent to the source.</dl>
<p> <code>Total RX</code></p>
<dl>
<dt>
<dd> The number of all packets received from the source.</dl>
<p> <code>Total valid RX</code></p>
<dl>
<dt>
<dd> The number of valid packets received from the source.</dl>
</dl>
<p> <code>add peer</code> <i>address</i> [<i>option</i>]&#8230;</p>
<dl>
<dt>
<dd> The <code>add peer</code> command allows a new NTP peer to be added whilst <code>chronyd</code> is running. </p>
<p> Following the words <code>add peer</code>, the syntax of the following parameters and options is similar to that for the <code>peer</code> directive in the configuration file. The following peer options can be set in the command: <code>port</code>, <code>minpoll</code>, <code>maxpoll</code>, <code>presend</code>, <code>maxdelayratio</code>, <code>maxdelay</code>, <code>key</code>. </p>
<p> An example of using this command is shown below. </p>
<dl>
<dt>
<dd>
<pre>
add peer foo.example.net minpoll 6 maxpoll 10 key 25
</pre>
</dl>
</dl>
<p> <code>add server</code> <i>address</i> [<i>option</i>]&#8230;</p>
<dl>
<dt>
<dd> The <code>add server</code> command allows a new NTP server to be added whilst <code>chronyd</code> is running. </p>
<p> Following the words <code>add server</code>, the syntax of the following parameters and options is similar to that for the <code>server</code> directive in the configuration file. The following server options can be set in the command: <code>port</code>, <code>minpoll</code>, <code>maxpoll</code>, <code>presend</code>, <code>maxdelayratio</code>, <code>maxdelay</code>, <code>key</code>. </p>
<p> An example of using this command is shown below: </p>
<dl>
<dt>
<dd>
<pre>
add server foo.example.net minpoll 6 maxpoll 10 key 25
</pre>
</dl>
</dl>
<p> <code>delete</code> <i>address</i></p>
<dl>
<dt>
<dd> The <code>delete</code> command allows an NTP server or peer to be removed from the current set of sources.</dl>
<p> <code>burst</code> <i>good</i>/<i>max</i> [<i>mask</i>/<i>masked-address</i>], <code>burst</code> <i>good</i>/<i>max</i> [<i>masked-address</i>/<i>masked-bits</i>], <code>burst</code> <i>good</i>/<i>max</i> [<i>address</i>]</p>
<dl>
<dt>
<dd> The <code>burst</code> command tells <code>chronyd</code> to make a set of measurements to each of its NTP sources over a short duration (rather than the usual periodic measurements that it makes). After such a burst, <code>chronyd</code> will revert to the previous state for each source. This might be either online, if the source was being periodically measured in the normal way, or offline, if the source had been indicated as being offline. (A source can be switched between the online and offline states with the <code>online</code> and <code>offline</code> commands.) </p>
<p> The <i>mask</i> and <i>masked-address</i> arguments are optional, in which case <code>chronyd</code> will initiate a burst for all of its currently defined sources. </p>
<p> The arguments have the following meaning and format: </p>
<p> <i>good</i></p>
<dl>
<dt>
<dd> This defines the number of good measurements that <code>chronyd</code> will want to obtain from each source. A measurement is good if it passes certain tests, for example, the round trip time to the source must be acceptable. (This allows <code>chronyd</code> to reject measurements that are likely to be bogus.)</dl>
<p> <i>max</i></p>
<dl>
<dt>
<dd> This defines the maximum number of measurements that <code>chronyd</code> will attempt to make, even if the required number of good measurements has not been obtained.</dl>
<p> <i>mask</i></p>
<dl>
<dt>
<dd> This is an IP address with which the IP address of each of <code>chronyd</code>&#8216;s sources is to be masked.</dl>
<p> <i>masked-address</i></p>
<dl>
<dt>
<dd> This is an IP address. If the masked IP address of a source matches this value then the burst command is applied to that source.</dl>
<p> <i>masked-bits</i></p>
<dl>
<dt>
<dd> This can be used with <i>masked-address</i> for CIDR notation, which is a shorter alternative to the form with mask.</dl>
<p> <i>address</i></p>
<dl>
<dt>
<dd> This is an IP address or a hostname. The burst command is applied only to that source.</dl>
</dl>
<dl>
<dt>
<dd>
<p> If no <i>mask</i> or <i>masked-address</i> arguments are provided, every source will be matched. </p>
<p> An example of the two-argument form of the command is: </p>
<dl>
<dt>
<dd>
<pre>
burst 2/10
</pre>
</dl>
<p> This will cause <code>chronyd</code> to attempt to get two good measurements from each source, stopping after two have been obtained, but in no event will it try more than ten probes to the source. </p>
<p> Examples of the four-argument form of the command are: </p>
<dl>
<dt>
<dd>
<pre>
burst 2/10 255.255.0.0/1.2.0.0
burst 2/10 2001:db8:789a::/48
</pre>
</dl>
<p> In the first case, the two out of ten sampling will only be applied to sources whose IPv4 addresses are of the form <i>1.2.x.y</i>, where <i>x</i> and <i>y</i> are arbitrary. In the second case, the sampling will be applied to sources whose IPv6 addresses have first 48 bits equal to <i>2001:db8:789a</i>. </p>
<p> Example of the three-argument form of the command is: </p>
<dl>
<dt>
<dd>
<pre>
burst 2/10 foo.example.net
</pre>
</dl>
</dl>
<p> <code>maxdelay</code> <i>address</i> <i>delay</i></p>
<dl>
<dt>
<dd> This allows the <code>maxdelay</code> option for one of the sources to be modified, in the same way as specifying the <code>maxdelay</code> option for the <code>server</code> directive in the configuration file.</dl>
<p> <code>maxdelaydevratio</code> <i>address</i> <i>ratio</i></p>
<dl>
<dt>
<dd> This allows the <code>maxdelaydevratio</code> option for one of the sources to be modified, in the same way as specifying the <code>maxdelaydevratio</code> option for the <code>server</code> directive in the configuration file.</dl>
<p> <code>maxdelayratio</code> <i>address</i> <i>ratio</i></p>
<dl>
<dt>
<dd> This allows the <code>maxdelayratio</code> option for one of the sources to be modified, in the same way as specifying the <code>maxdelayratio</code> option for the <code>server</code> directive in the configuration file.</dl>
<p> <code>maxpoll</code> <i>address</i> <i>maxpoll</i></p>
<dl>
<dt>
<dd> The <code>maxpoll</code> command is used to modify the maximum polling interval for one of the current set of sources. It is equivalent to the <code>maxpoll</code> option in the <code>server</code> directive in the configuration file. </p>
<p> Note that the new maximum polling interval only takes effect after the next measurement has been made.</dl>
<p> <code>minpoll</code> <i>address</i> <i>minpoll</i></p>
<dl>
<dt>
<dd> The <code>minpoll</code> command is used to modify the minimum polling interval for one of the current set of sources. It is equivalent to the <code>minpoll</code> option in the <code>server</code> directive in the configuration file. </p>
<p> Note that the new minimum polling interval only takes effect after the next measurement has been made.</dl>
<p> <code>minstratum</code> <i>address</i> <i>minstratum</i></p>
<dl>
<dt>
<dd> The <code>minstratum</code> command is used to modify the minimum stratum for one of the current set of sources. It is equivalent to the <code>minstratum</code> option in the <code>server</code> directive in the configuration file.</dl>
<p> <code>offline</code> [<i>address</i>], <code>offline</code> [<i>masked-address</i>/<i>masked-bits</i>], <code>offline</code> [<i>mask</i>/<i>masked-address</i>]</p>
<dl>
<dt>
<dd> The <code>offline</code> command is used to warn <code>chronyd</code> that the network connection to a particular host or hosts is about to be lost, e.g. on computers with intermittent connection to their time sources. </p>
<p> Another case where <code>offline</code> could be used is where a computer serves time to a local group of computers, and has a permanent connection to true time servers outside the organisation. However, the external connection is heavily loaded at certain times of the day and the measurements obtained are less reliable at those times. In this case, it is probably most useful to determine the gain or loss rate during the quiet periods and let the whole network coast through the loaded periods. The <code>offline</code> and <code>online</code> commands can be used to achieve this. </p>
<p> There are four forms of the <code>offline</code> command. The first form is a wildcard, meaning all sources. The second form allows an IP address mask and a masked address to be specified. The third form uses CIDR notation. The fourth form uses an IP address or a hostname. These forms are illustrated below. </p>
<dl>
<dt>
<dd>
<pre>
offline
offline 255.255.255.0/1.2.3.0
offline 2001:db8:789a::/48
offline foo.example.net
</pre>
</dl>
<p> The second form means that the <code>offline</code> command is to be applied to any source whose IPv4 address is in the <i>1.2.3</i> subnet. (The host&#8217;s address is logically and-ed with the mask, and if the result matches the <i>masked-address</i> the host is processed.) The third form means that the command is to be applied to all sources whose IPv6 addresses have their first 48 bits equal to <i>2001:db8:789a</i>. The fourth form means that the command is to be applied only to that one source. </p>
<p> The wildcard form of the address is equivalent to: </p>
<dl>
<dt>
<dd>
<pre>
offline 0.0.0.0/0.0.0.0
offline ::/0
</pre>
</dl>
</dl>
<p> <code>online</code> [<i>address</i>], <code>online</code> [<i>masked-address</i>/<i>masked-bits</i>], <code>online</code> [<i>mask</i>/<i>masked-address</i>]</p>
<dl>
<dt>
<dd> The <code>online</code> command is opposite in function to the <code>offline</code> command. It is used to advise <code>chronyd</code> that network connectivity to a particular source or sources has been restored. </p>
<p> The syntax is identical to that of the <code>offline</code> command.</dl>
<p> <code>polltarget</code> <i>address</i> <i>polltarget</i></p>
<dl>
<dt>
<dd> The <code>polltarget</code> command is used to modify the poll target for one of the current set of sources. It is equivalent to the <code>polltarget</code> option in the <code>server</code> directive in the configuration file.</dl>
<p> <code>refresh</code></p>
<dl>
<dt>
<dd> The <code>refresh</code> command can be used to force <code>chronyd</code> to resolve the names of configured sources to IP addresses again, e.g. after suspending and resuming the machine in a different network. </p>
<p> Sources that stop responding will be replaced with newly resolved addresses automatically after 8 polling intervals, but this command can still be useful to replace them immediately and not wait until they are marked as unreachable.</dl>
<h3>Manual time input</h3>
<p> <code>manual</code> <code>on</code>, <code>manual</code> <code>off</code>, <code>manual</code> <code>delete</code> <i>index</i>, <code>manual</code> <code>list</code>, <code>manual</code> <code>reset</code></p>
<dl>
<dt>
<dd> The manual command enables and disables use of the <code>settime</code> command, and is used to modify the behaviour of the manual clock driver. </p>
<p> The <code>on</code> form of the command enables use of the <code>settime</code> command. </p>
<p> The <code>off</code> form of the command disables use of the <code>settime</code> command. </p>
<p> The <code>list</code> form of the command lists all the samples currently stored in <code>chronyd</code>. The output is illustrated below. </p>
<dl>
<dt>
<dd>
210 n_samples = 1<br />
#Date Time(UTC) Slewed Original Residual<br />
                == == == == == == == == == == == == == == == == == == == == == == == == == ==<br />
                0 27Jan99 22 : 09 : 20 0.00 0.97 0.00
</dl>
<p> The columns are as as follows: </p>
<dl>
<dt>
<dd> 1. The sample index (used for the <code>manual delete</code> command).</dl>
<dl>
<dt>
<dd> 2. The date and time of the sample.</dl>
<dl>
<dt>
<dd> 3. The system clock error when the timestamp was entered, adjusted to allow for changes made to the system clock since.</dl>
<dl>
<dt>
<dd> 4. The system clock error when the timestamp was entered, as it originally was (without allowing for changes to the system clock since).</dl>
<dl>
<dt>
<dd> 5. The regression residual at this point, in seconds. This allows &#8216;outliers&#8217; to be easily spotted, so that they can be deleted using the <code>manual delete</code> command.</dl>
</dl>
<dl>
<dt>
<dd>
<p> The <code>delete</code> form of the command deletes a single sample. The parameter is the index of the sample, as shown in the first column of the output from <code>manual list</code>. Following deletion of the data point, the current error and drift rate are re-estimated from the remaining data points and the system clock trimmed if necessary. This option is intended to allow &#8216;outliers&#8217; to be discarded, i.e. samples where the administrator realises they have entered a very poor timestamp. </p>
<p> The <code>reset</code> form of the command deletes all samples at once. The system clock is left running as it was before the command was entered.</dl>
<p> <code>settime</code> <i>time</i></p>
<dl>
<dt>
<dd> The <code>settime</code> command allows the current time to be entered manually, if this option has been configured into <code>chronyd</code>. (It can be configured either with the <code>manual</code> directive in the configuration file, or with the <code>manual</code> command of <code>chronyc</code>.) </p>
<p> It should be noted that the computer&#8217;s sense of time will only be as accurate as the reference you use for providing this input (e.g. your watch), as well as how well you can time the press of the return key. </p>
<p> Providing your computer&#8217;s time zone is set up properly, you will be able to enter a local time (rather than UTC). </p>
<p> The response to a successful <code>settime</code> command indicates the amount that the computer&#8217;s clock was wrong. It should be apparent from this if you have entered the time wrongly, e.g. with the wrong time zone. </p>
<p> The rate of drift of the system clock is estimated by a regression process using the entered measurement and all previous measurements entered during the present run of <code>chronyd</code>. However, the entered measurement is used for adjusting the current clock offset (rather than the estimated intercept from the regression, which is ignored). Contrast what happens with the <code>manual delete</code> command, where the intercept is used to set the current offset (since there is no measurement that has just been entered in that case). </p>
<p> The time is parsed by the public domain <i>getdate</i> algorithm. Consequently, you can only specify time to the nearest second. </p>
<p> Examples of inputs that are valid are shown below: </p>
<dl>
<dt>
<dd>
<pre>
settime 16:30
settime 16:30:05
settime Nov 21, 2015 16:30:05
</pre>
</dl>
<p> For a full description of getdate, see the getdate documentation (bundled, for example, with the source for GNU tar).</dl>
<h3>NTP access</h3>
<p> <code>accheck</code> <i>address</i></p>
<dl>
<dt>
<dd> This command allows you to check whether client NTP access is allowed from a particular host. </p>
<p> Examples of use, showing a named host and a numeric IP address, are as follows: </p>
<dl>
<dt>
<dd>
<pre>
accheck foo.example.net
accheck 1.2.3.4
accheck 2001:db8::1
</pre>
</dl>
<p> This command can be used to examine the effect of a series of <code>allow</code>, <code>allow all</code>, <code>deny</code>, and <code>deny all</code> commands specified either via <code>chronyc</code>, or in <code>chronyd</code>&#8216;s configuration file.</dl>
<p> <code>clients</code></p>
<dl>
<dt>
<dd> This command shows a list of clients that have accessed the server, through either the NTP or command ports. It does not include accesses over the Unix domain command socket. There are no arguments. </p>
<p> An example of the output is: </p>
<dl>
<dt>
<dd>
Hostname NTP Drop Int IntL Last Cmd Drop Int Last == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =<br />
                                                                                                                                                                           localhost 2 0 2 &#8211; 133 15 0 &#8211; 1 7 foo.example.net 12 0 6 &#8211; 23 0 0 &#8211; &#8211;
</dl>
<p> Each row shows the data for a single host. Only hosts that have passed the host access checks (set with the <code>allow</code>, <code>deny</code>, <code>cmdallow</code> and <code>cmddeny</code> commands or configuration file directives) are logged. The intervals are displayed as a power of 2 in seconds. </p>
<p> The columns are as follows: </p>
<dl>
<dt>
<dd> 1. The hostname of the client.</dl>
<dl>
<dt>
<dd> 2. The number of NTP packets received from the client.</dl>
<dl>
<dt>
<dd> 3. The number of NTP packets dropped to limit the response rate.</dl>
<dl>
<dt>
<dd> 4. The average interval between NTP packets.</dl>
<dl>
<dt>
<dd> 5. The average interval between NTP packets after limiting the response rate.</dl>
<dl>
<dt>
<dd> 6. Time since the last NTP packet was received</dl>
<dl>
<dt>
<dd> 7. The number of command packets received from the client.</dl>
<dl>
<dt>
<dd> 8. The number of command packets dropped to limit the response rate.</dl>
<dl>
<dt>
<dd> 9. The average interval between command packets.</dl>
<dl>
<dt>
<dd> 10. Time since the last command packet was received.</dl>
</dl>
<p> <code>serverstats</code></p>
<dl>
<dt>
<dd> The <code>serverstats</code> command displays how many valid NTP and command requests <code>chronyd</code> as a server received from clients, how many of them were dropped to limit the response rate as configured by the <code>ratelimit</code> and <code>cmdratelimit</code> directives, and how many client log records were dropped due to the memory limit configured by the <code>clientloglimit</code> directive. An example of the output is shown below. </p>
<dl>
<dt>
<dd>
<pre>
NTP packets received       : 1598
NTP packets dropped        : 8
Command packets received   : 19
Command packets dropped    : 0
Client log records dropped : 0
</pre>
</dl>
</dl>
<p> <code>allow</code> [<code>all</code>] [<i>subnet</i>]</p>
<dl>
<dt>
<dd> The effect of the allow command is identical to the <code>allow</code> directive in the configuration file. </p>
<p> The syntax is illustrated in the following examples: </p>
<dl>
<dt>
<dd>
<pre>
allow foo.example.net
allow all 1.2
allow 3.4.5
allow 6.7.8/22
allow 6.7.8.9/22
allow 2001:db8:789a::/48
allow 0/0
allow ::/0
allow
allow all
</pre>
</dl>
</dl>
<p> <code>deny</code> [<code>all</code>] [<i>subnet</i>]</p>
<dl>
<dt>
<dd> The effect of the allow command is identical to the <code>deny</code> directive in the configuration file. </p>
<p> The syntax is illustrated in the following examples: </p>
<dl>
<dt>
<dd>
<pre>
deny foo.example.net
deny all 1.2
deny 3.4.5
deny 6.7.8/22
deny 6.7.8.9/22
deny 2001:db8:789a::/48
deny 0/0
deny ::/0
deny
deny all
</pre>
</dl>
</dl>
<p> <code>local</code> [<i>option</i>]&#8230;, <code>local</code> <code>off</code></p>
<dl>
<dt>
<dd> The <code>local</code> command allows <code>chronyd</code> to be told that it is to appear as a reference source, even if it is not itself properly synchronised to an external source. (This can be used on isolated networks, to allow one computer to be a master time server with the other computers slaving to it.) </p>
<p> The first form enables the local reference mode on the host. The syntax is identical to the <code>local</code> directive in the configuration file. </p>
<p> The second form disables the local reference mode.</dl>
<p> <code>smoothing</code></p>
<dl>
<dt>
<dd> The <code>smoothing</code> command displays the current state of the NTP server time smoothing, which can be enabled with the <code>smoothtime</code> directive. An example of the output is shown below. </p>
<dl>
<dt>
<dd>
<pre>
Active         : Yes
Offset         : +1.000268817 seconds
Frequency      : -0.142859 ppm
Wander         : -0.010000 ppm per second
Last update    : 17.8 seconds ago
Remaining time : 19988.4 seconds
</pre>
</dl>
<p> The fields are explained as follows: </p>
<p> <code>Active</code></p>
<dl>
<dt>
<dd> This shows if the server time smoothing is currently active. Possible values are <i>Yes</i> and <i>No</i>. If the <code>leaponly</code> option is included in the <code>smoothtime</code> directive, <i>(leap second only)</i> will be shown on the line.</dl>
<p> <code>Offset</code></p>
<dl>
<dt>
<dd> This is the current offset applied to the time sent to NTP clients. Positive value means the clients are getting time that&#8217;s ahead of true time.</dl>
<p> <code>Frequency</code></p>
<dl>
<dt>
<dd> The current frequency offset of the served time. Negative value means the time observed by clients is running slower than true time.</dl>
<p> <code>Wander</code></p>
<dl>
<dt>
<dd> The current frequency wander of the served time. Negative value means the time observed by clients is slowing down.</dl>
<p> <code>Last update</code></p>
<dl>
<dt>
<dd> This field shows how long ago the time smoothing process was updated, e.g. <code>chronyd</code> accumulated a new measurement.</dl>
<p> <code>Remaining time</code></p>
<dl>
<dt>
<dd> The time it would take for the smoothing process to get to zero offset and frequency if there were no more updates.</dl>
</dl>
<p> <code>smoothtime</code> <code>activate</code>, <code>smoothtime</code> <code>reset</code></p>
<dl>
<dt>
<dd> The <code>smoothtime</code> command can be used to activate or reset the server time smoothing process if it is configured with the <code>smoothtime</code> directive.</dl>
<h3>Monitoring access</h3>
<p> <code>cmdaccheck</code> <i>address</i></p>
<dl>
<dt>
<dd> This command is similar to the <code>accheck</code> command, except that it is used to check whether monitoring access is permitted from a named host. </p>
<p> Examples of use are as follows: </p>
<dl>
<dt>
<dd>
<pre>
cmdaccheck foo.example.net
cmdaccheck 1.2.3.4
cmdaccheck 2001:db8::1
</pre>
</dl>
</dl>
<p> <code>cmdallow</code> [<code>all</code>] [<i>subnet</i>]</p>
<dl>
<dt>
<dd> This is similar to the <code>allow</code> command, except that it is used to allow particular hosts or subnets to use <code>chronyc</code> to monitor with <code>chronyd</code> on the current host.</dl>
<p> <code>cmddeny</code> [<code>all</code>] [<i>subnet</i>]</p>
<dl>
<dt>
<dd> This is similar to the <code>deny</code> command, except that it is used to allow particular hosts or subnets to use <code>chronyc</code> to monitor <code>chronyd</code> on the current host.</dl>
<h3>Real-time clock (RTC)</h3>
<p> <code>rtcdata</code></p>
<dl>
<dt>
<dd> The <code>rtcdata</code> command displays the current RTC parameters. </p>
<p> An example output is shown below. </p>
<dl>
<dt>
<dd>
<pre>
RTC ref time (GMT) : Sat May 30 07:25:56 2015
Number of samples  : 10
Number of runs     : 5
Sample span period :  549
RTC is fast by     :    -1.632736 seconds
RTC gains time at  :  -107.623 ppm
</pre>
</dl>
<p> The fields have the following meaning: </p>
<p> <code>RTC ref time (GMT)</code></p>
<dl>
<dt>
<dd> This is the RTC reading the last time its error was measured.</dl>
<p> <code>Number of samples</code></p>
<dl>
<dt>
<dd> This is the number of previous measurements being used to determine the RTC gain or loss rate.</dl>
<p> <code>Number of runs</code></p>
<dl>
<dt>
<dd> This is the number of runs of residuals of the same sign following the regression fit for (RTC error) versus (RTC time). A value which is small indicates that the measurements are not well approximated by a linear model, and that the algorithm will tend to delete the older measurements to improve the fit.</dl>
<p> <code>Sample span period</code></p>
<dl>
<dt>
<dd> This is the period that the measurements span (from the oldest to the newest). Without a unit the value is in seconds; suffixes <i>m</i> for minutes, <i>h</i> for hours, <i>d</i> for days or <i>y</i> for years can be used.</dl>
<p> <code>RTC is fast by</code></p>
<dl>
<dt>
<dd> This is the estimate of how many seconds fast the RTC when it thought the time was at the reference time (above). If this value is large, you might (or might not) want to use the <code>trimrtc</code> command to bring the RTC into line with the system clock. (Note, a large error will not affect <code>chronyd</code>&#8216;s operation, unless it becomes so big as to start causing rounding errors.)</dl>
<p> <code>RTC gains time at</code></p>
<dl>
<dt>
<dd> This is the amount of time gained (positive) or lost (negative) by the real time clock for each second that it ticks. It is measured in parts per million. So if the value shown was +1, suppose the RTC was exactly right when it crosses a particular second boundary. Then it would be 1 microsecond fast when it crosses its next second boundary.</dl>
</dl>
<p> <code>trimrtc</code></p>
<dl>
<dt>
<dd> The <code>trimrtc</code> command is used to correct the system&#8217;s real-time clock (RTC) to the main system clock. It has no effect if the error between the two clocks is currently estimated at less than a second. </p>
<p> The command takes no arguments. It performs the following steps (if the RTC is more than 1 second away from the system clock): </p>
<dl>
<dt>
<dd> 1. Remember the currently estimated gain or loss rate of the RTC and flush the previous measurements.</dl>
<dl>
<dt>
<dd> 2. Step the real-time clock to bring it within a second of the system clock.</dl>
<dl>
<dt>
<dd> 3. Make several measurements to accurately determine the new offset between the RTC and the system clock (i.e. the remaining fraction of a second error).</dl>
<dl>
<dt>
<dd> 4. Save the RTC parameters to the RTC file (specified with the <code>rtcfile</code> directive in the configuration file).</dl>
</dl>
<dl>
<dt>
<dd>
<p> The last step is done as a precaution against the computer suffering a power failure before either the daemon exits or the <code>writertc</code> command is issued. </p>
<p> <code>chronyd</code> will still work perfectly well both whilst operating and across machine reboots even if the <code>trimrtc</code> command is never used (and the RTC is allowed to drift away from true time). The <code>trimrtc</code> command is provided as a method by which it can be corrected, in a manner compatible with <code>chronyd</code> using it to maintain accurate time across machine reboots. </p>
<p> The <code>trimrtc</code> command can be executed automatically by <code>chronyd</code> with the <code>rtcautotrim</code> directive in the configuration file.</dl>
<p> <code>writertc</code></p>
<dl>
<dt>
<dd> The <code>writertc</code> command writes the currently estimated error and gain or loss rate parameters for the RTC to the RTC file (specified with the <code>rtcfile</code> directive). This information is also written automatically when <code>chronyd</code> is killed (by the SIGHUP, SIGINT, SIGQUIT or SIGTERM signals) or when the <code>trimrtc</code> command is issued.</dl>
<h3>Other daemon commands</h3>
<p> <code>cyclelogs</code></p>
<dl>
<dt>
<dd> The <code>cyclelogs</code> command causes all of <code>chronyd</code>&#8216;s open log files to be closed and re-opened. This allows them to be renamed so that they can be periodically purged. An example of how to do this is shown below. </p>
<dl>
<dt>
<dd>
<pre><code>
#mv / var / log / chrony / measurements.log / var / log / chrony / measurements1.log
#chronyc cyclelogs
#ls - l / var / log / chrony
- rw - r-- r-- 1 root root 0 Jun 8 18:17 measurements.log - rw - r-- r-- 1 root root 12345 Jun 8 18:17 measurements1.log
#rm - f measurements1.log
</code></pre>
</dl>
</dl>
<p> <code>dump</code></p>
<dl>
<dt>
<dd> The <code>dump</code> command causes <code>chronyd</code> to write its current history of measurements for each of its sources to dump files, either for inspection or to support the <code>-r</code> option when <code>chronyd</code> is restarted. </p>
<p> The <code>dump</code> command is somewhat equivalent to the <code>dumponexit</code> directive in the configuration file. </p>
<p> To use the <code>dump</code> command, you might want to configure the name of the directory into which the dump files will be written. This can only be done in the configuration file with the <code>dumpdir</code> directive.</dl>
<p> <code>rekey</code></p>
<dl>
<dt>
<dd> The <code>rekey</code> command causes <code>chronyd</code> to re-read the key file specified in the configuration file by the <code>keyfile</code> directive.</dl>
<h3>Client commands</h3>
<p> <code>dns</code> <i>option</i></p>
<dl>
<dt>
<dd> The <code>dns</code> command configures how hostnames and IP addresses are resolved in <code>chronyc</code>. IP addresses can be resolved to hostnames when printing results of <code>sources</code>, <code>sourcestats</code>, <code>tracking</code> and <code>clients</code> commands. Hostnames are resolved in commands that take an address as argument. </p>
<p> There are five options: </p>
<p> <code>dns -n</code></p>
<dl>
<dt>
<dd> Disables resolving IP addresses to hostnames. Raw IP addresses will be displayed.</dl>
<p> <code>dns +n</code></p>
<dl>
<dt>
<dd> Enables resolving IP addresses to hostnames. This is the default unless <code>chronyc</code> was started with <code>-n</code> option.</dl>
<p> <code>dns -4</code></p>
<dl>
<dt>
<dd> Resolves hostnames only to IPv4 addresses.</dl>
<p> <code>dns -6</code></p>
<dl>
<dt>
<dd> Resolves hostnames only to IPv6 addresses.</dl>
<p> <code>dns -46</code></p>
<dl>
<dt>
<dd> Resolves hostnames to both address families. This is the default behaviour unless <code>chronyc</code> was started with the <code>-4</code> or <code>-6</code> option.</dl>
</dl>
<p> <code>timeout</code> <i>timeout</i></p>
<dl>
<dt>
<dd> The <code>timeout</code> command sets the initial timeout for <code>chronyc</code> requests in milliseconds. If no response is received from <code>chronyd</code>, the timeout is doubled and the request is resent. The maximum number of retries is configured with the <code>retries</code> command. </p>
<p> By default, the timeout is 1000 milliseconds.</dl>
<p> <code>retries</code> <i>retries</i></p>
<dl>
<dt>
<dd> The <code>retries</code> command sets the maximum number of retries for <code>chronyc</code> requests before giving up. The response timeout is controlled by the <code>timeout</code> command. </p>
<p> The default is 2.</dl>
<p> <code>keygen</code> [<i>id</i> [<i>type</i> [<i>bits</i>]]]</p>
<dl>
<dt>
<dd> The <code>keygen</code> command generates a key that can be added to the key file (specified with the <code>keyfile</code> directive) to allow NTP authentication between server and client, or peers. The key is generated from the <i>/dev/urandom</i> device and it is printed to standard output. </p>
<p> The command has three optional arguments. The first argument is the key number (by default 1), which will be specified with the <code>key</code> option of the <code>server</code> or <code>peer</code> directives in the configuration file. The second argument is the hash function (by default SHA1 or MD5 if SHA1 is not available) and the third argument is the number of bits the key should have, between 80 and 4096 bits (by default 160 bits). </p>
<p> An example is: </p>
<dl>
<dt>
<dd>
<pre>
keygen 73 SHA1 256
</pre>
</dl>
<p> which generates a 256-bit SHA1 key with number 73. The printed line should then be securely transferred and added to the key files on both server and client, or peers.</dl>
<p> <code>exit</code>, <code>quit</code></p>
<dl>
<dt>
<dd> The <code>exit</code> and <code>quit</code> commands exit from <code>chronyc</code> and return the user to the shell.</dl>
<p> <code>help</code></p>
<dl>
<dt>
<dd> The <code>help</code> command displays a summary of the commands and their arguments.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-chrony-conf/">chrony.conf</a>(5)</code>, <code><a href="/docs/linux/man/8-chronyd/">chronyd</a>(8)</code></p>
<h2>BUGS</h2>
<p> For instructions on how to report bugs, please visit &lt;URL: <a rel="nofollow" href="https://chrony.tuxfamily.org/">https://chrony.tuxfamily.org/</a> &gt;.</p>
<h2>AUTHORS</h2>
<p> chrony was written by Richard Curnow, Miroslav Lichvar, and others. </p>
<h2>Index</h2>
