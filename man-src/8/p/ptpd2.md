---
title: "ptpd2(8)"
name: "ptpd2"
section: "8"
letter: "p"
url: "/docs/linux/man/8-ptpd2/"
description: "ptpd2 – Precision Time Protocol daemon (1588-2008)"
---

<p>ptpd2 &#8211; Precision Time Protocol daemon (1588-2008)</p>
<h2>Synopsis</h2>
<p><code>ptpd2</code> <code>[ -?hH ]</code> <code>[ -e </code><i>SETTING</i><code> ]</code> <code>[ -kvOLAl ]</code> <code>[ -smMyEPanCV ]</code> <code>[ -c </code><i>FILE</i><code> ]</code> <code>[ -R </code><i>DIR</i><code> ]</code> <code>[ -f </code><i>FILE</i><code> ]</code> <code>[ -S </code><i>FILE</i><code> ]</code> <code>[ -d </code><i>DOMAIN</i><code> ]</code> <code>[ -u </code><i>ADDRESS</i><code> ]</code> <code>[ -r </code><i>NUMBER</i><code> ]</code> <code>-i </code><i>INTERFACE</i></p>
<h2>Description</h2>
<p>PTPd is a daemon that implements the Precision Time Protocol (PTP) Version 2 as defined by the IEEE 1588-2008 standard. PTP was developed to provide very precise time coordination of LAN connected computers. The daemon must run as <code>root</code> in order to be able to manipluate the system clock and use low port numbers. PTPd is feature rich, supports IPv4 multicast, unicast and hybrid mode (mixed) operation, as well as Ethernet mode. Even without hardware assistance, PTPd is able to achieve and maintain sub-microsecond level timing precision and is able to withstand PTP Grandmaster failovers, link failures and restarts with minimal impact to timing performance. PTPd is lightweight, portable and currently supports Linux, FreeBSD and Mac OS X and runs on multiple CPU architectures, 32-bit and 64-bit, including x86 and ARM.</p>
<h2>Command-Line Configuration</h2>
<p>As of version 2.3.0, configuration file is the preferred mechanism for configuring PTPd, therefore the options available as short (<i>-x</i>) and long options (<i>&#8211;xxxxx</i>) mostly provide basic control over the daemon operation, and only provide the very basic PTP protocol settings. The rest of the settings (see <code><a href="/docs/linux/man/5-ptpd2-conf/">ptpd2.conf</a>(5)</code>) can also be specified as command-line options, but they take the long <i>&#8211;key:section=&quot;value&quot;</i> form.</p>
<h2>Basic Daemon Options</h2>
<dl>
<dt><code>-c &#8211;config-file </code><i>PATH</i></p>
<dd>Path to configuration file (see <code><a href="/docs/linux/man/5-ptpd2-conf/">ptpd2.conf</a>(5)</code>)</p>
<dt><code>-k &#8211;check-config</code></p>
<dd>Check configuration and exit &#8211; return 0 if configuration is correct.</p>
<dt><code>-v &#8211;version</code></p>
<dd>Print version string and exit</p>
<dt><code>-h &#8211;help</code></p>
<dd>Show help screen</p>
<dt><code>-H &#8211;long-help</code></p>
<dd>Show detailed help for all settings and behaviours</p>
<dt><code>-e &#8211;explain </code><i>SETTING</i></p>
<dd>Show help for a single setting (<i>section:key</i>)</p>
<dt><code>-O &#8211;default-config</code></p>
<dd>Show default configuration and exit (output usable as a configuration file)</p>
<dt><code>-L &#8211;ignore-lock</code></p>
<dd>Skip lock file checks and locking (also <i>global:ignore_lock</i>)</p>
<dt><code>-A &#8211;auto-lock</code></p>
<dd>Use preset / port mode specific lock file names &#8211; useful when running multiple instances</p>
<dt><code>-l &#8211;lockfile</code></p>
<dd>Specify lock file path (also <i>global:lock_file</i>)</p>
<dt><code>-p &#8211;print-lockfile</code></p>
<dd>Print path to lock file and exit (useful for init scripts in combination with auto lock files)</p>
<dt><code>-R &#8211;lock-directory </code><i>DIR</i></p>
<dd>Directory to store lock files (also <i>global:lock_directory</i>)</p>
<dt><code>-f &#8211;log-file </code><i>PATH</i></p>
<dd>Path to log file (also <i>global:logfile</i>)</p>
<dt><code>-S &#8211;statistics-file </code><i>PATH</i></p>
<dd>Path to statistics file (also <i>global:statistics_file</i>)</dl>
<h2>Basic Ptp Protocol Options</h2>
<dl>
<dt><code>-i &#8211;interface </code><i>DEV</i></p>
<dd><i>REQUIRED:</i>Interface to use &#8211; eth0, etc (also <i>ptpengine:interface</i>)</p>
<dt><code>-d &#8211;domain </code><i>NUMBER</i></p>
<dd>PTP domain number to become part of (also <i>ptpengine:domain</i>)</p>
<dt><code>-s &#8211;slaveonly</code></p>
<dd>Slave only mode (also <i>ptpengine:preset=slaveonly</i>)</p>
<dt><code>-m &#8211;masterslave</code></p>
<dd>Full IEEE 1588 implementation: master, slave when not best GM (also <i>ptpengine:preset=masterslave</i>)</p>
<dt><code>-M &#8211;masteronly</code></p>
<dd>Master only mode: passive when not best GM (also <i>ptpengine:preset=masteronly</i>)</p>
<dt><code>-y &#8211;hybrid</code></p>
<dd>Hybrid mode &#8211; mixed multicast and unicast operation (multicast for sync and announce, unicast for delay request and response (also <i>ptpengine:ip_mode=hybrid</i>)</p>
<dt><code>-U &#8211;unicast</code></p>
<dd>Unicast operation &#8211; (<i>also ptpengine:ip_mode=unicast</i>). For a GM, unicast destinations must be specified (<i>-u, &#8211;unicast-destinations, ptpengine:unicast_destinations</i>) unless using unicast negotiation (<i>-g, &#8211;unicast-negotiation, ptpengine:unicast_negotiation=y</i>) for delay request and response (also <i>ptpengine:ip_mode=hybrid</i>). For a slave, unicast destinations must be specified if not using unicast negotiation.</p>
<dt><code>-g &#8211;unicast-negotiation</code></p>
<dd>Enable unicast message delivery and interval negotiation usin signaling messages, as used by the Telecom profile (also enables <i>ptpengine:ip_mode=unicast</i>)</p>
<dt><code>-u &#8211;unicast-destinations </code><i>ip/host, ip/host, &#8230;</i></p>
<dd>List of unicast destinations &#8211; see <i>&#8211;unicast</i> (also <i>ptpengine:ip_mode=unicast</i> + <i>ptpengine:unicast_destinations</i>) <code>-E &#8211;e2e</code> End to end delay mechanism (also <i>ptpengine:delay_mechanism=E2E</i>)</p>
<dt><code>-E &#8211;p2p</code></p>
<dd>Peer to peer delay mechanism (also <i>ptpengine:delay_mechanism=P2P</i>)</p>
<dt><code>-a &#8211;delay-override</code></p>
<dd>In slave state, override delay request interval announced by master (also <i>ptpengine:log_delayreq_override</i>) &#8211; the value of <i>ptpengine:log_delayreq_interval</i> is used</p>
<dt><code>-r &#8211;delay-interval </code><i>NUMBER</i></p>
<dd>Specify delay request message interval (log 2) &#8211; (also <i>ptpengine:log_delayreq_interval</i>)</p>
<dt><code>-n &#8211;clock:no_adjust</code></p>
<dd>Do not adjust the clock (also <i>clock:no_adjust</i>)</p>
<dt><code>-D&lt;DD&#8230;&gt; &#8211;debug</code></p>
<dd>Debug level (also <i>global:debug_level</i>) &#8211; only if compiled with RUNTIME_DEBUG</p>
<dt><code>-C &#8211;foreground</code></p>
<dd>Don&#8217;t run in background (also <i>global:foreground=Y</i>)</p>
<dt><code>-V &#8211;verbose</code></p>
<dd>Run in foreground, log all the messages to standard output (also <i>global:verbose_foreground=Y</i>) </p>
</dl>
<h2>Compatibility Options</h2>
<dl>
<dt>PTPd supports the following options compatible with versions before 2.3.0:</p>
<dd>
<dl>
<dd>
<dl>
<dt><code>-b </code><i>DEV</i></p>
<dd>Network interface to use</p>
<dt><code>-i </code><i>NUMBER</i></p>
<dd>PTP domain number</p>
<dt><code>-g</code></p>
<dd>Slave only mode</p>
<dt><code>-G</code></p>
<dd>&#8216;Master mode with NTP&#8217; (master only mode)</p>
<dt><code>-W</code></p>
<dd>&#8216;Master mode without NTP&#8217; (master / slave mode)</p>
<dt><code>-U</code></p>
<dd>Hybrid mode (mixed unicast + multicast operation)</p>
<dt><code>-Y </code><i>NUMBER</i></p>
<dd>Delay request interval (log 2)</p>
<dt><code>-t</code></p>
<dd>Do not adjust the clock</dl>
</dl>
<dt><code>NOTE:</code> the above options are deprecated and will be removed in subsequent versions. Until then, their use will issue a warning.</p>
<dd></dl>
<h2>Ptpd Port States</h2>
<dl>
<dd>
<dl>
<dt><i>init</i></p>
<dd>INITIALIZING</p>
<dt><i>flt</i></p>
<dd>FAULTY</p>
<dt><i>lstn_init</i></p>
<dd>LISTENING (first time)</p>
<dt><i>lstn_reset</i></p>
<dd>LISTENING (subsequent reset)</p>
<dt><i>pass</i></p>
<dd>PASSIVE (not best master, not announcing)</p>
<dt><i>uncl</i></p>
<dd>UNCALIBRATED</p>
<dt><i>slv</i></p>
<dd>SLAVE</p>
<dt><i>pmst</i></p>
<dd>PRE-MASTER</p>
<dt><i>mst</i></p>
<dd>MASTER (active)</p>
<dt><i>dsbl</i></p>
<dd>DISABLED</p>
<dt><i>? (unk)</i></p>
<dd>UNKNOWN state</dl>
</dl>
<h2>Statistics Log File Format</h2>
<p>When the statistics log is enabled (<i>ptpengine:log_statistics</i>, verbose foreground mode or log file &#8211; <i>ptpengine:statistics_file</i>), a PTPd slave will log clock sync information upon the receipt of every Sync and Delay Response message. When PTPd starts up or flushes the log, a comment line (starting with #) will be logged, containing the names of all columns. The format of this log is a series of comma-separated values (CSV) and can be easily imported into statistics tools and most spreadsheet software packages for analysis and graphing. This log can get very large when running PTPd for longer periods of time and with high message rates, therefore to reduce the number of messages logged, the <i>global:statistics_log_interval</i> setting can be used, to limit the log output to one message per configured interval only. The size and maximum number of the statistics log can also be controlled &#8211; (see <code><a href="/docs/linux/man/5-ptpd2-conf/">ptpd2.conf</a>(5)</code>).</p>
<dl>
<dt>The meaning of the columns is as follows:</p>
<dd>
<dl>
<dd>
<dl>
<dt><code>Timestamp</code></p>
<dd>Time when message received. This can take the form of text date / time or Unix timestamp (with fractional seconds), or both (in which case an exra field is added), depending onthe <i>global:statistics_timestamp_format</i> setting (see <code><a href="/docs/linux/man/5-ptpd2-conf/">ptpd2.conf</a>(5)</code>). When importing the log into plotting software, if the software can understand Unix time, it is best to set the timestamp format to unix or both, as some software will not properly deal with the fractional part of the second when converting the date and time from text.</p>
<dt><code>State</code></p>
<dd>Port state (see <code>PTP PORT STATES</code>).</p>
<dt><code>Clock ID</code></p>
<dd>Port identity of the current best master, as defined by IEEE 1588. This will be the local clock&#8217;s ID if the local clock is the best master. Displayed as <i>clock_id/port(host)</i> Port is the PTP clock port number, not to be confused with UDP ports. The clock ID is an EUI-64 64-bit ID, usually converted from the 48-bit MAC address, by inserting 0xfffe between the lower and upper half of the MAC address. PTPd will attempt to convert the clock ID back to MAC address and look up the hostname from <i>/etc/ethers</i> (see <code><a href="/docs/linux/man/5-ethers/">ethers</a>(5)</code>). Populating the ethers file will help the administrator recognise the masters by familiar hostnames.</p>
<dt><code>One Way Delay</code></p>
<dd>Current value of one-way delay (or mean path delay) in seconds, calculated by PTPd in slave state from the Delay Request &#8211; Delay Response message exchange. <i>Note:</i> if this value remains at zero, this usually means that no Delay Response messages are being received, likely due to a network issue.</p>
<dt><code>Offset From Master</code></p>
<dd>Current value of offset from master in seconds &#8211; this is the main output of the PTP engine in slave state, which is the input of the clock servo for clock corrections. This is the value typically observed when estimating the slave performance.</p>
<dt><code>Slave to Master</code></p>
<dd>Intermediate offset value (seconds) extracted from the Delay Request &#8211; Delay Response message exchange, used for computing one-way delay. If the last value was rejected by a filter, the previous value will be shown in the log. This value will also be zero if no Delay Response messages are being received.</p>
<dt><code>Master to Slave</code></p>
<dd>Intermediate offset value (seconds) extracted from the Sync messages, used for computing the offset from master. If the last value was rejected by a filter, the previous value will be shown in the log.</p>
<dt><code>Observed Drift</code></p>
<dd>The integral accumulator of the clock control PI servo model &#8211; frequency difference between the slave clock and master clock. This value becomes stable when the clock offset has stabilised, and can be used (and is) to detect clock stability.</p>
<dt><code>Last Packet Received</code></p>
<dd>This field shows what message was received last &#8211; this will be S for Sync and D for Delay Response. If a slave logs no D entries, this means it&#8217;s not receiving Delay Response messages, which could be a network issue.</p>
<dt><code>One Way Delay Mean</code></p>
<dd>One-way delay mean computed over the last sampling window.</p>
<dt><code>One Way Delay Std Dev</code></p>
<dd>One-way delay standard deviation computed over the last sampling window.</p>
<dt><code>Offset From Master Mean</code></p>
<dd>Offset from master mean computed over the last sampling window.</p>
<dt><code>Offset From Master Std Dev</code></p>
<dd>Offset from master standard deviation computed over the last sampling window.</p>
<dt><code>Observed Drift Mean</code></p>
<dd>Observed drift / local clock frequency adjustment mean computed over the last sampling window.</p>
<dt><code>Observed Drift Std Dev</code></p>
<dd>Observed drift / local clock frequency adjustment standard deviation computed over the last sampling window. The lower the value, the less aggressively the clock is being controlled and therefore the more stable it is.</p>
<dt><code>raw delayMS</code></p>
<dd>Raw (unfiltered) delayMS value &#8211; useful for evaluating outliers and filter performance.</p>
<dt><code>raw delaySM</code></p>
<dd>Raw (unfiltered) delaySM value &#8211; useful for evaluating outliers and filter performance.</dl>
</dl>
<p> <code>NOTE:</code> All the statistical measures (mean and std dev) will only be computed and displayed if PTPd was built without &#8211;disable-statistics. The duration of the sampling period is controlled with the <i>global:statistics_update_interval</i> setting &#8211; (see <code><a href="/docs/linux/man/5-ptpd2-conf/">ptpd2.conf</a>(5)</code>). </p>
</dl>
<h2>Handled Signals</h2>
<dl>
<dt><code>PTPd handles the following signals:</code></p>
<dd>
<dl>
<dd>
<dl>
<dt><i>SIGHUP</i></p>
<dd>Reload configuration file (if used) and reopen log files</p>
<dt><i>SIGUSR1</i></p>
<dd>When in slave state, force clock step to current Offset from Master value</p>
<dt><i>SIGUSR2</i></p>
<dd>Dump all PTP protocol counters to current log target (and clear if <i>ptpengine:sigusr2_clears_counters</i> set)</p>
<dt><i>SIGINT|SIGTERM</i></p>
<dd>Clean exit &#8211; close logs and other open files, clean up lock file and exit.</p>
<dt><i>SIGKILL</i></p>
<dd>Force an unclean exit.</dl>
</dl>
</dl>
<h2>Exit Codes</h2>
<p>Upon exit, ptpd2 returns <code>0</code> on success &#8211; either successfully started in daemon mode, or otherwise exited cleanly. <code>0</code> is also returned when the <i>-k</i> (<i>&#8211;check-config</i>) option is used and the configuration was correct. A non-zero exit code is returned on errors. <code>3</code> is returned on lock file errors and when ptpd2 could not be started as daemon. <code>2</code> is returned on memory allocation errors during startup. For all other error conditions such as configuration errors, running ptpd2 in help mode or with no parameters, on self shutdown, network startup errors and when attempting to run ptpd2 as non-root &#8211; <code>1</code> is returned.</p>
<h2>Supported Platforms And Architectures</h2>
<p>PTPd is fully supported on Linux and FreeBSD as this is what the core developers focus on. OpenBSD and NetBSD are also supported, but get less developers&#8217; attention. So is Max OS X, and as of PTPd 2.3.1 also OpenSolaris (11) derivatives (tested on OmniOS). Sun&#8217;s / Oracle&#8217;s Solaris 11 has not been tested but in essence, it should work as intended. Solaris 10 is NOT supported because it does not provide the SO_TIMESTAMP socket option. It should theoretically be possible to use Solaris 10 using the <i>pf</i> facility as used by <i>snoop</i>, but there is currently no ongoing effort to acheive this. Patches for QNX/Neutrino have been provided, but cannot yet officially be merged because of no availability of QNX to the developers. Some users have ported PTPd to other RTOS, but this has not been merged either. </p>
<p> As of 2.3.1, PTPd runs entirely in software and only relies on kernel and OS APIs, so there are no hardware dependencies. Any little-endian or big-endian port of modern versions of the supported OSes should work, but only x86 and ARM are actively tested. The only dependencies close to hardware can be NIC drivers and how and if they impact software timestamping.</p>
<h2>Hardware Timestamping Support</h2>
<p>As of 2.3.1, PTPd still does not support hardware timestamping. This functionality will appear in the upcoming version 2.4 &#8211; potentially an interim version of 2.3.x may be delivered that will support hardware clocks and timestamping on Linux. This is very much OS-specific and to a large extent, hardware-specific. Linux has a PTP kernel API but not all hardware supports it. Because PTPd supports multiple OS platforms, where hardware timestamping may use different mechanisms on every platform, it has to be re-written in a modular way to allow this without unnecessarily increasing code complexity, which already is a problem.</p>
<h2>Bugs</h2>
<p>As of ptpd 2.3.1, the (Open)Solaris (11) OS family is supported, but libpcap functionality is currently broken &#8211; IPv4/pcap and Ethernet transports cannot be used on those systems. PTPd will compile and run,<br />
&nbsp;<wbr>but will not receive any data. Please report any bugs using the bug tracker on the SourceForge page: <a rel="nofollow" href="http://sourceforge.net/projects/ptpd/">http://sourceforge.net/projects/ptpd/</a> </p>
<h2>See Also</h2>
<p>ptpd2.conf5 <a href="/docs/linux/man/5-ptpd2-conf/">ptpd2.conf</a>(5)</p>
<h2>Authors</h2>
<p>Gael Mace &lt;gael_mace [at] users.sourceforge.net&gt; </p>
<p> Alexandre Van Kempen </p>
<p> Steven Kreuzer &lt;skreuzer [at] freebsd.org&gt; </p>
<p> George Neville-Neil &lt;gnn [at] freebsd.org&gt; </p>
<p> Wojciech Owczarek &lt;wojciech [at] owczarek.co.uk&gt; </p>
<p> <code><a href="/docs/linux/man/8-ptpd2/">ptpd2</a>(8)</code> man page was written by Wojciech Owczarek for ptpd 2.3.0 in November 2013</p>
