---
title: "ntpd(8)"
name: "ntpd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-ntpd/"
description: "ntpd – Network Time Protocol (NTP) daemon"
---

<p>ntpd &#8211; Network Time Protocol (NTP) daemon</p>
<h2>&nbsp;<wbr></h2>
<h2>Synopsis</h2>
<p><code>ntpd [ -46aAbdDgLmnNqx ] [ -c </code><i>conffile</i><code> ] [ -f </code><i>driftfile</i><code> ] [ -i </code><i>jaildir</i><code> ] [ -I </code><i>iface</i><code> ] [ -k </code><i>keyfile</i><code> ] [ -l </code><i>logfile</i><code> ] [ -p </code><i>pidfile</i><code> ] [ -P </code><i>priority</i><code> ] [ -r </code><i>broadcastdelay</i><code> ] [ -s </code><i>statsdir</i><code> ] [ -t </code><i>key</i><code> ] [ -u </code><i>user</i><code>[:</code><i>group</i><code>] ] [ -U </code><i>interface_update_interval</i><code> ] [ -v </code><i>variable</i><code> ] [ -V </code><i>variable</i><code> ]</code> </p>
<h2>Description</h2>
<p>The <code>ntpd</code> program is an operating system daemon that synchronises the system clock with remote NTP time servers or local reference clocks. It is a complete implementation of the Network Time Protocol (NTP) version 4, but also retains compatibility with version 3, as defined by RFC-1305, and version 1 and 2, as defined by RFC-1059 and RFC-1119, respectively. The program can operate in any of several modes, as described on the Association Management page, and with both symmetric key and public key cryptography, as described on the Authentication Options page. The <code>ntpd</code> program ordinarily requires a configuration file as described on the Configuration Commands and Options collection above. However a client can discover remote servers and configure them automatically. This makes it possible to deploy a fleet of workstations without specifying configuration details specific to the local environment. Further details are on the Automatic Server Discovery page. Once the NTP software distribution has been compiled and installed and the configuration file constructed, the next step is to verify correct operation and fix any bugs that may result. Usually, the command line that starts the daemon is included in the system startup file, so it is executed only at system boot time; however, the daemon can be stopped and restarted from root at any time. Once started, the daemon will begin sending and receiving messages, as specified in the configuration file. </p>
<h2>Setting The Time And Frequency</h2>
<p>The <code>ntpd</code> program operates by exchanging messages with one or more servers at designated intervals ranging from about one minute to about 17 minutes. When started, the program requires several exchanges while the algorithms accumulate and groom the data before setting the clock. The initial delay to set the clock can be reduced using options on the Server Options page. </p>
<p> Most computers today incorporate a time-of-year (TOY) chip to maintain the time during periods when the power is off. When the machine is booted, the chip is used to initialize the operating system time. In case there is no TOY chip or the TOY time is more than 1000 s from the server time, <code>ntpd</code> assumes something must be terribly wrong and exits with a panic message to the system operator. With the <code>-g</code> option the clock will be initially set to the server time regardless of the chip time. However, once the clock has been set, an error greater than 1000 s will cause <code>ntpd</code> to exit anyway. </p>
<p> Under ordinary conditions, <code>ntpd</code> slews the clock so that the time is effectively continuous and never runs backwards. If due to extreme network congestion an error spike exceeds the <i>step threshold</i>, by default 128 ms, the spike is discarded. However, if the error persists for more than the <i>stepout threshold</i>, by default 900 s, the system clock is stepped to the correct value. In practice the need for a step has is extremely rare and almost always the result of a hardware failure. With the <code>-x</code> option the step threshold is increased to 600 s. Other options are available using the <code>tinker</code> command on the Miscellaneous Options page. </p>
<p> The issues should be carefully considered before using these options. The maximum slew rate possible is limited to 500 parts-per-million (PPM) by the Unix kernel. As a result, the clock can take 2000 s for each second the clock is outside the acceptable range. During this interval the clock will not be consistent with any other network clock and the system cannot be used for distributed applications that require correctly synchronized network time. </p>
<p> The frequency file, usually called <code>ntp.drift</code>, contains the latest estimate of clock frequency. If this file does not exist when <code>ntpd</code> is started, it enters a special mode designed to measure the particular frequency directly. The measurement takes 15 minutes, after which the frequency is set and <code>ntpd</code> resumes normal mode where the time and frequency are continuously adjusted. The frequency file is updated at intervals of an hour or more depending on the measured clock stability.</p>
<h2>Operating Modes</h2>
<p>The <code>ntpd</code> program normally operates continuously while adjusting the time and frequency, but in some cases it may not be practical to run it continuously. With the <code>-q</code> option <code>ntpd</code> operates as in continous mode, but exits just after setting the clock for the first time with the configured servers. Most applications will probably want to specify the <code>iburst</code> option with the <code>server</code> command. With this option a volley of messages is exchanged to groom the data and set the clock in about 10 s. If nothing is heard after a few minutes, the daemon times out and exits.</p>
<h2>Poll Interval Control</h2>
<p>NTP uses an intricate heuristic algorithm to automatically control the poll interval for maximum accuracy consistent with minimum network overhead. The algorithm measures the incidental offset and jitter to determine the best poll interval. When <code>ntpd</code> starts, the interval is the default minimum 64 s. Under normal conditions when the clock discipline has stabilized, the interval increases in steps to the default maximum 1024 s. In addition, should a server become unreachable after some time, the interval increases in steps to the maximum in order to reduce network overhead. </p>
<p> The default poll interval range is suitable for most conditions, but can be changed using options on the Server Options and Miscellaneous Options pages. However, when using maximum intervals much larger than the default, the residual clock frequency error must be small enough for the discipline loop to capture and correct. The capture range is 500 PPM with a 64-s interval decreasing by a factor of two for each interval doubling. At a 36-hr interval, for example, the capture range is only 0.24 PPM.</p>
<h2>The Huff-N&#8217;-Puff Filter</h2>
<p>In scenarios where a considerable amount of data are to be downloaded or uploaded over telephone modems, timekeeping quality can be seriously degraded. This occurs because the differential delays on the two directions of transmission can be quite large. In many cases the apparent time errors are so large as to exceed the step threshold and a step correction can occur during and after the data transfer. </p>
<p> The huff-n&#8217;-puff filter is designed to correct the apparent time offset in these cases. It depends on knowledge of the propagation delay when no other traffic is present, such as during other than work hours. The filter remembers the minimum delay over the most recent interval measured usually in hours. Under conditions of severe delay, the filter corrects the apparent offset using the sign of the offset and the difference between the apparent delay and minimum delay. The name of the filter reflects the negative (huff) and positive (puff) correction, which depends on the sign of the offset. The filter is activated by the <code>tinker huffpuff</code> command, as described in the Miscellaneous Options page.</p>
<h2>Leap Second Processing</h2>
<p>As provided by international agreement, an extra second is sometimes inserted in Coordinated Universal Time (UTC) at the end of a selected month, usually June or December. The National Institutes of Standards and Technology (NIST) provides an historic leapseconds file at <code>time.nist.gov</code> for retrieval via FTP. When this file, usually called <code>ntp-leapseconds.list</code>, is copied and installed in a directory. The <code>leapfile</code> configuration command specifies the path to this file. At startup, <code>ntpd</code> reads it and initializes three leapsecond values: the NTP seconds at the next leap event, the offset of UTC relative to International Atomic Time (TAI) after the leap and the NTP seconds when the leapseconds file expires and should be retrieved again. </p>
<p> If a host does not have the leapsecond values, they can be obtained over the net using the Autokey security protocol. Ordinarily, the leapseconds file is installed on the primary servers and the values flow from them via secondary servers to the clients. When multiple servers are involved, the values with the latest expiration time are used. </p>
<p> If the latest leap is in the past, nothing further is done other than to install the TAI offset. If the leap is in the future less than 28 days, the leap warning bits are set. If in the future less than 23 hours, the kernel is armed to insert one second at the end of the current day. If the kernel is enabled, the leap is done automatically at that time; otherwise, the clock is effectively stopped for one second at the leap. Additional details are in the The NTP Timescale and Leap Seconds white paper </p>
<p> If none of the above provisions are available, dsependent servers and clients tally the leap warning bits of surviving servers and reference clocks. When a majority of the survivors show warning, a leap is programmed at the end of the current month. During the month and day of insertion, they operate as above. In this way the leap is propagated at all dependent servers and clients.</p>
<h2>Additional Features</h2>
<p>A new experimental feature called interleaved modes can be used in NTP symmetric or broadcast modes. It is designed to improve accuracy by avoiding kernel latency and queueing delay, as described on the NTP Interleaved Modes page. It is activated by the <code>xleave</code> option with the <code>peer</code> or <code>broadcast</code> configuration commands. The NTP protocol automatically reconfigures in normal or interleaved mode as required. Ordinary broadcast clients can use the same servers as interleaved clients at the same time. Further details are in the white paper NTP Interleaved On-Wire Protocol and the briefing Interleaved Synchronization Protocols for LANs and Space Data Links46 </p>
<p> If <code>ntpd</code>, is configured with NetInfo support, it will attempt to read its configuration from the NetInfo service if the default <code>ntp.conf</code> file cannot be read and no file is specified by the <code>-c</code> option. </p>
<p> In contexts where a host name is expected, a <code>-4</code> qualifier preceding the host name forces DNS resolution to the IPv4 namespace, while a <code>-6</code> qualifier forces DNS resolution to the IPv6 namespace. </p>
<p> Various internal <code>ntpd</code> variables can be displayed and configuration options altered while the <code>ntpd</code> is running using the <code>ntpq</code> and <code>ntpdc</code> utility programs. </p>
<p> When <code>ntpd</code> starts it looks at the value of <code>umask</code>, and if zero <code>ntpd</code> will set the <code>umask</code> to <code>022</code>46 </p>
<p> Unless the <code>-n</code>, <code>-d</code> or <code>-D</code> option is used, <code>ntpd</code> changes the current working directory to the root directory, so any options or commands specifying paths need to use an absolute path or a path relative to the root.</p>
<h2>Command Line Options</h2>
<dl>
<dd>
<dl>
<dt><code>-4</code></p>
<dd>Force DNS resolution of host names to the IPv4 namespace.</p>
<dt><code>-6</code></p>
<dd>Force DNS resolution of host names to the IPv6 namespace.</p>
<dt><code>-a</code></p>
<dd>Require cryptographic authentication for broadcast client, multicast client and symmetric passive associations. This is the same operation as the <code>enable auth</code> command and is the default.</p>
<dt><code>-A</code></p>
<dd>Do not require cryptographic authentication for broadcast client, multicast client and symmetric passive associations. This is the same operation as the <code>disable auth</code> command and almost never a good idea.</p>
<dt><code>-b</code></p>
<dd>Enable the client to synchronize to broadcast servers.</p>
<dt><code>-c </code><i>conffile</i></p>
<dd>Specify the name and path of the configuration file, default <code>/etc/ntp.conf</code>46</p>
<dt><code>-d</code></p>
<dd>Specify debugging mode. This option may occur more than once, with each occurrence indicating greater detail of display.</p>
<dt><code>-D </code><i>level</i></p>
<dd>Specify debugging level directly.</p>
<dt><code>-f </code><i>driftfile</i></p>
<dd>Specify the name and path of the frequency file. This is the same operation as the <code>driftfile </code><i>driftfile</i> command.</p>
<dt><code>-g</code></p>
<dd>Normally, <code>ntpd</code> exits with a message to the system log if the offset exceeds the panic threshold, which is 1000 s by default. This option allows the time to be set to any value without restriction; however, this can happen only once. If the threshold is exceeded after that, <code>ntpd</code> will exit with a message to the system log. This option can be used with the <code>-q</code> and <code>-x</code> options. See the <code>tinker</code> command for other options.</p>
<dt><code>-i </code><i>jaildir</i></p>
<dd>Chroot the server to the directory <i></i><code>jaildir</code><i></i>46 This option also implies that the server attempts to drop root privileges at startup (otherwise, chroot gives very little additional security), and it is only available if the OS supports to run the server without full root privileges. You may need to also specify a <code>-u</code> option.</p>
<dt><code>-I [</code><i>address</i><code> | </code><i>interface name</i><code>]</code></p>
<dd>Open the network address given, or all the addresses associated with the given interface name. This option may appear multiple times. This option also implies not opening other addresses, except wildcard and localhost. This option is deprecated. Please consider using the configuration file interface command, which is more versatile.</p>
<dt><code>-k </code><i>keyfile</i></p>
<dd>Specify the name and path of the symmetric key file. This is the same operation as the <code>keys </code><i>keyfile</i> command.</p>
<dt><code>-l </code><i>logfile</i></p>
<dd>Specify the name and path of the log file. The default is the system log file. This is the same operation as the <code>logfile </code><i>logfile</i> command.</p>
<dt><code>-L</code></p>
<dd>Do not listen to virtual interfaces, defined as those with names containing a colon. This option is deprecated. Please consider using the configuration file interface command, which is more versatile.</p>
<dt><code>-M</code></p>
<dd>Raise scheduler precision to its maximum (1 msec) using timeBeginPeriod. (Windows only)</p>
<dt><code>-m</code></p>
<dd>Lock memory.</p>
<dt><code>-n</code></p>
<dd>Don&#8217;t fork.</p>
<dt><code>-N</code></p>
<dd>To the extent permitted by the operating system, run the <code>ntpd</code> at the highest priority.</p>
<dt><code>-p </code><i>pidfile</i></p>
<dd>Specify the name and path of the file used to record the <code>ntpd</code> process ID. This is the same operation as the <code>pidfile </code><i>pidfile</i> command.</p>
<dt><code>-P </code><i>priority</i></p>
<dd>To the extent permitted by the operating system, run the <code>ntpd</code> at the specified priority.</p>
<dt><code>-q</code></p>
<dd>Exit the <code>ntpd</code> just after the first time the clock is set. This behavior mimics that of the <code>ntpdate</code> program, which is to be retired. The <code>-g</code> and <code>-x</code> options can be used with this option. Note: The kernel time discipline is disabled with this option.</p>
<dt><code>-r </code><i>broadcastdelay</i></p>
<dd>Specify the default propagation delay from the broadcast/multicast server to this client. This is necessary only if the delay cannot be computed automatically by the protocol.</p>
<dt><code>-s </code><i>statsdir</i></p>
<dd>Specify the directory path for files created by the statistics facility. This is the same operation as the <code>statsdir </code><i>statsdir</i> command.</p>
<dt><code>-t </code><i>key</i></p>
<dd>Add a key number to the trusted key list. This option can occur more than once. This is the same operation as the <code>trustedkey </code><i>key</i> command.</p>
<dt><code>-u </code><i>user[:group]</i></p>
<dd>Specify a user, and optionally a group, to switch to. This option is only available if the OS supports running the server without full root privileges. Currently, this option is supported under NetBSD (configure with <code>&#8211;enable-clockctl</code>) and Linux (configure with &#8212;<code>enable-linuxcaps</code>).</p>
<dt><code>-U </code><i>interface update interval</i></p>
<dd>Number of seconds to wait between interface list scans to pick up new and delete network interface. Set to 0 to disable dynamic interface list updating. The default is to scan every 5 minutes.</p>
<dt><code>-x</code></p>
<dd>Normally, the time is slewed if the offset is less than the step threshold, which is 128 ms by default, and stepped if above the threshold. This option sets the threshold to 600 s, which is well within the accuracy window to set the clock manually. Note: Since the slew rate of typical Unix kernels is limited to 0.5 ms/s, each second of adjustment requires an amortization interval of 2000 s. Thus, an adjustment as much as 600 s will take almost 14 days to complete. This option can be used with the <code>-g</code> and <code>-q</code> options. See the <code>tinker</code> command for other options. Note: The kernel time discipline is disabled with this option and the step threshold is applied also to leap second corrections.</dl>
</dl>
<h2>The Configuration File</h2>
<p>Ordinarily, <code>ntpd</code> reads the <code>ntp.conf</code> configuration file at startup in order to determine the synchronization sources and operating modes. It is also possible to specify a working, although limited, configuration entirely on the command line, obviating the need for a configuration file. This may be particularly useful when the local host is to be configured as a broadcast client, with servers determined by listening to broadcasts at run time. </p>
<p> Usually, the configuration file is installed as<code>/etc/ntp.conf</code>, but could be installed elsewhere (see the <code>-c </code><i>conffile</i> command line option). The file format is similar to other Unix configuration files &#8211; comments begin with a <code>#</code> character and extend to the end of the line; blank lines are ignored. </p>
<p> Configuration commands consist of an initial command keyword followed by a list of option keywords separated by whitespace. Commands may not be continued over multiple lines. Options may be host names, host addresses written in numeric, dotted-quad form, integers, floating point numbers (when specifying times in seconds) and text strings. Optional arguments are delimited by <code>[ ]</code> in the options pages, while alternatives are separated by <code>|</code>46 The notation <code>[ &#8230; ]</code> means an optional, indefinite repetition of the last item before the <code>[ &#8230; ]</code>46</p>
<h2>Files</h2>
<table BORDER WIDTH=100%>
<tr VALIGN=top>
<td>File </td>
<td> Default </td>
<td> Option </td>
<td> Command
</td>
</tr>
<tr VALIGN=top>
<td>configuration file </td>
<td> <code>/etc/ntp.conf</code> </td>
<td> <code>-c</code> </td>
<td> none
</td>
</tr>
<tr VALIGN=top>
<td>frequency file </td>
<td> none </td>
<td> <code>-f</code> </td>
<td> <code>driftfile</code>
</td>
</tr>
<tr VALIGN=top>
<td>leapseconds file </td>
<td> none </td>
<td> </td>
<td> <code>leapfile</code>
</td>
</tr>
<tr VALIGN=top>
<td>process ID file </td>
<td> none </td>
<td> <code>-p</code> </td>
<td> <code>pidfile</code>
</td>
</tr>
<tr VALIGN=top>
<td>log file </td>
<td> system log </td>
<td> <code>-l</code> </td>
<td> <code>logfile</code>
</td>
</tr>
<tr VALIGN=top>
<td>include file </td>
<td> none </td>
<td> none </td>
<td> <code>includefile</code>
</td>
</tr>
<tr VALIGN=top>
<td>statistics path </td>
<td> <code>/var/log/ntpstats/</code> </td>
<td> <code>-s</code> </td>
<td> <code>statsdir</code>
</td>
</tr>
<tr VALIGN=top>
<td>keys path </td>
<td> <code>/etc/ntp/crypto</code> </td>
<td> <code>none</code> </td>
<td> <code>keysdir</code>
</td>
</tr>
</table>
<h2>Exit Codes</h2>
<p>A non-zero exit code indicates an error. Any error messages are logged to the system log by default. </p>
<p> The exit code is 0 only when <code>ntpd</code> is terminated by a signal, or when the <code>-q</code> option is used and <code>ntpd</code> successfully sets the system clock.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-ntp-conf/">ntp.conf</a>(5), <a href="/docs/linux/man/8-ntpq/">ntpq</a>(8), <a href="/docs/linux/man/8-ntpdc/">ntpdc</a>(8) The official HTML documentation. This file was automatically generated from HTML source. </p>
