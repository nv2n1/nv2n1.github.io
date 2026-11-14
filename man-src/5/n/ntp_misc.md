---
title: "ntp_misc(5)"
name: "ntp_misc"
section: "5"
letter: "n"
url: "/docs/linux/man/5-ntp_misc/"
description: "ntp_misc – Miscellaneous Options"
---

<p>ntp_misc &#8211; Miscellaneous Options</p>
<h2>&nbsp;<wbr></h2>
<dl>
<dd>
<dl>
<dt><code>broadcastdelay </code><i>seconds</i></p>
<dd>The broadcast and multicast modes require a special calibration to determine the network delay between the local and remote servers. Ordinarily, this is done automatically by the initial protocol exchanges between the client and server. In some cases, the calibration procedure may fail due to network or server access controls, for example. This command specifies the default delay to be used under these circumstances. Typically (for Ethernet), a number between 0.003 and 0.007 seconds is appropriate.</p>
<dt><code>driftfile </code><i>driftfile</i><code> { </code><i>tolerance</i><code> ]</code></p>
<dd>This command specifies the complete path and name of the file used to record the frequency of the local clock oscillator. This is the same operation as the <code>-f</code> command linke option. If the file exists, it is read at startup in order to set the initial frequency and then updated once per hour or more with the current frequency computed by the daemon. If the file name is specified, but the file itself does not exist, the starts with an initial frequency of zero and creates the file when writing it for the first time. If this command is not given, the daemon will always start with an initial frequency of zero. The file format consists of a single line containing a single floating point number, which records the frequency offset measured in parts-per-million (PPM). The file is updated by first writing the current drift value into a temporary file and then renaming this file to replace the old version. This implies that <code>ntpd</code> must have write permission for the directory the drift file is located in, and that file system links, symbolic or otherwise, should be avoided. The parameter <code>tolerance</code> is the wander threshold to skip writing the new value. If the value of wander computed from recent frequency changes is greater than this threshold the file will be updated once per hour. If below the threshold, the file will not be written.</p>
<dt><code>enable [ auth | bclient | calibrate | kernel | monitor | ntp | pps | stats]</code></p>
<dd>
<dt><code>disable [ auth | bclient | calibrate | kernel | monitor | ntp | pps | stats ]</code></p>
<dd>Provides a way to enable or disable various system options. Flags not mentioned are unaffected. Note that all of these flags can be controlled remotely using the <code>ntpdc</code> utility program.</p>
<dl>
<dd>
<dl>
<dt><code>auth</code></p>
<dd>Enables the server to synchronize with unconfigured peers only if the peer has been correctly authenticated using either public key or private key cryptography. The default for this flag is enable.</p>
<dt><code>bclient</code></p>
<dd>Enables the server to listen for a message from a broadcast or multicast server, as in the <code>multicastclient</code> command with default address. The default for this flag is disable.</p>
<dt><code>calibrate</code></p>
<dd>Enables the calibrate feature for reference clocks. The default for this flag is disable.</p>
<dt><code>kernel</code></p>
<dd>Enables the kernel time discipline, if available. The default for this flag is enable if support is available, otherwise disable.</p>
<dt><code>monitor</code></p>
<dd>Enables the monitoring facility. See the <code>ntpdc</code> program and the <code>monlist</code> command or further information. The default for this flag is enable.</p>
<dt><code>ntp</code></p>
<dd>Enables time and frequency discipline. In effect, this switch opens and closes the feedback loop, which is useful for testing. The default for this flag is enable.</p>
<dt><code>stats</code></p>
<dd>Enables the statistics facility. See the Monitoring Options page for further information. The default for this flag is disable.</dl>
</dl>
<dt><code>includefile </code><i>includefile</i></p>
<dd>This command allows additional configuration commands to be included from a separate file. Include files may be nested to a depth of five; upon reaching the end of any include file, command processing resumes in the previous configuration file. This option is useful for sites that run <code>ntpd</code> on multiple hosts, with (mostly) common options (e.g., a restriction list).</p>
<dt><code>interface [listen | ignore | drop] [all | ipv4 | ipv6 | wildcard | </code><i>name</i><code> | </code><i>address</i><code>[/</code><i>prefixlen</i><code>]]</code></p>
<dd>This command controls which network addresses <code>ntpd</code> opens, and whether input is dropped without processing. The first parameter determines the action for addresses which match the second parameter. That parameter specifies a class of addresses, or a specific interface name, or an address. In the address case, <i>prefixlen</i> determines how many bits must match for this rule to apply. <code>ignore</code> prevents opening matching addresses, <code>drop</code> causes <code>ntpd</code> to open the address and drop all received packets without examination. Multiple <code>interface</code> commands can be used. The last rule which matches a particular address determines the action for it. <code>interface</code> commands are disabled if any <code>-I</code>, <code>&#8211;interface</code>, <code>-L</code>, or <code>&#8211;novirtualips</code> command-line options are used. If none of those options are used and no <code>interface</code> actions are specified in the configuration file, all available network addresses are opened. The <code>nic</code> command is an alias for <code>interface</code>46</p>
<dt><code>leapfile </code><i>leapfile</i></p>
<dd>This command loads the NIST leapseconds file and initializes the leapsecond values for the next leapsecond time, expiration time and TAI offset. The file can be obtained directly from NIST national time servers using <code>ftp</code> as the ASCII file <code>pub/leap-seconds</code>46 While not strictly a security function, the Autokey protocol provides means to securely retrieve the current or updated leapsecond values from a server.</p>
<dt><code>logconfig </code><i>configkeyword</i></p>
<dd>This command controls the amount and type of output written to the system <code>syslog</code> facility or the alternate <code>logfile</code> log file. All <i></i><code>configkeyword</code><i></i> keywords can be prefixed with <code>=</code>, <code>+</code> and <code>&#8211;</code>, where <code>=</code> sets the <code>syslogmask</code>, <code>+</code> adds and <code>&#8211;</code> removes messages. <code>syslog messages</code> can be controlled in four classes (<code>clock</code>, <code>peer</code>, <code>sys</code> and <code>sync</code>). Within these classes four types of messages can be controlled: informational messages (<code>info</code>), event messages (<code>events</code>), statistics messages (<code>statistics</code>) and status messages (<code>status</code>). Configuration keywords are formed by concatenating the message class with the event class. The <code>all</code> prefix can be used instead of a message class. A message class may also be followed by the <code>all</code> keyword to enable/disable all messages of the respective message class. By default, <code>logconfig</code> output is set to <code>=syncall +sysevents +sysstatus</code>46 Thus, a minimal log configuration could look like this: <code>logconfig =syncstatus +sysevents</code> This would just list the synchronizations state of <code>ntpd</code> and the major system events. For a simple reference server, the following minimum message configuration could be useful: <code>logconfig =syncall +clockall</code> This configuration will list all clock information and synchronization information. All other events and messages about peers, system events and so on is suppressed.</p>
<dt><code>logfile </code><i>logfile</i></p>
<dd>This command specifies the location of an alternate log file to be used instead of the default system <code>syslog</code> facility. This is the same operation as the <code>-l </code>command line option.</p>
<dt><code>phone </code><i>dial</i><code>1 </code><i>dial</i><code>2 &#8230;</code></p>
<dd>This command is used in conjunction with the ACTS modem driver (type 18). The arguments consist of a maximum of 10 telephone numbers used to dial USNO, NIST or European time services. The Hayes command ATDT is normally prepended to the number, which can contain other modem control codes as well.</p>
<dt><code>saveconfigdir </code><i>directory_path</i></p>
<dd>Specify the directory in which to write configuration snapshots requested with <code>ntpq</code>&#8216;s saveconfig command. If <code>saveconfigdir</code> does not appear in the configuration file, saveconfig requests are rejected by ntpd.</p>
<dt><code>setvar </code><i>variable</i><code> [default]</code></p>
<dd>This command adds an additional system variable. These variables can be used to distribute additional information such as the access policy. If the variable of the form <i>name</i><code> = </code><i>value</i> is followed by the <code>default</code> keyword, the variable will be listed as part of the default system variables (<code>ntpq rv</code> command). These additional variables serve informational purposes only. They are not related to the protocol other that they can be listed. The known protocol variables will always override any variables defined via the <code>setvar</code> mechanism. There are three special variables that contain the names of all variable of the same group. The <code>sys_var_list</code> holds the names of all system variables. The <code>peer_var_list</code> holds the names of all peer variables and the <code>clock_var_list</code> holds the names of the reference clock variables.</p>
<dt><code>tinker [ allan </code><i>allan</i><code> | dispersion </code><i>dispersion</i><code> | freq </code><i>freq</i><code> | huffpuff </code><i>huffpuff</i><code> | panic </code><i>panic</i><code> | step </code><i>step</i><code> | stepback </code><i>step</i><code> | stepfwd </code><i>step</i><code> | stepout </code><i>stepout</i><code> ]</code></p>
<dd>This command alters certain system variables used by the clock discipline algorithm. The default values of these variables have been carefully optimized for a wide range of network speeds and reliability expectations. Very rarely is it necessary to change the default values; but, some folks can&#8217;t resist twisting the knobs. The options are as follows:</p>
<dl>
<dd>
<dl>
<dt><code>allan </code><i>allan</i></p>
<dd>Spedifies the Allan intercept, which is a parameter of the PLL/FLL clock discipline algorithm, in seconds with default 1500 s.</p>
<dt><code>dispersion </code><i>dispersion</i></p>
<dd>Specifies the dispersion increase rate in parts-per-million (PPM) with default 15 PPM.</p>
<dt><code>freq </code><i>freq</i></p>
<dd>Spedifies the frequency offset in parts-per-million (PPM) with default the value in the frequency file.</p>
<dt><code>huffpuff </code><i>huffpuff</i></p>
<dd>Spedifies the huff-n&#8217;-puff filter span, which determines the most recent interval the algorithm will search for a minimum delay. The lower limit is 900 s (15 m), but a more reasonable value is 7200 (2 hours).</p>
<dt><code>panic </code><i>panic</i></p>
<dd>Spedifies the panic threshold in seconds with default 1000 s. If set to zero, the panic sanity check is disabled and a clock offset of any value will be accepted.</p>
<dt><code>step </code><i>step</i></p>
<dd>Spedifies the step threshold in seconds. The default without this command is 0.128 s. If set to zero, step adjustments will never occur. Note: The kernel time discipline is disabled if the step threshold is set to zero or greater than 0.5 s and the threshold is applied also to leap second corrections.</p>
<dt><code>stepback </code><i>step</i></p>
<dd>Specifies the step threshold, but only in the backward direction.</p>
<dt><code>stepfwd </code><i>step</i></p>
<dd>Specifies the step threshold, but only in the forward direction. To avoid problems with frequency stabilization after large slews it&#8217;s not recommended to set one direction to a value greater than 0.5 s without setting also the other direction to at least 0.5 s.</p>
<dt><code>stepout </code><i>stepout</i></p>
<dd>Specifies the stepout threshold in seconds. The default without this command is 900 s. If set to zero, popcorn spikes will not be suppressed.</dl>
</dl>
<dt><code>tos [ beacon </code><i>beacon</i><code> | ceiling </code><i>ceiling</i><code> | cohort {0 | 1} | floor </code><i>floor</i><code> | maxclock </code><i>maxclock </i><code>| maxdist </code><i>maxdist</i><code> | minclock </code><i>minclock</i><code> | mindist </code><i>mindist </i><code>| minsane </code><i>minsane</i><code> | orphan </code><i>stratum</i><code> ]</code></p>
<dd>This command alters certain system variables used by the the clock selection and clustering algorithms. The default values of these variables have been carefully optimized for a wide range of network speeds and reliability expectations. Very rarely is it necessary to change the default values; but, some folks can&#8217;t resist twisting the knobs. It can be used to select the quality and quantity of peers used to synchronize the system clock and is most useful in dynamic server discovery schemes. The options are as follows:</p>
<dl>
<dd>
<dl>
<dt><code>beacon </code><i>beacon</i></p>
<dd>The manycast server sends packets at intervals of 64 s if less than <code>maxclock</code> servers are available. Otherwise, it sends packets at the <i></i><code>beacon</code><i></i> interval in seconds. The default is 3600 s. See the Automatic Server Discovery page for further details.</p>
<dt><code>ceiling </code><i>ceiling</i></p>
<dd>Specify the maximum stratum (exclusive) for acceptable server packets. The default is 16. See the Automatic Server Discovery page for further details.</p>
<dt><code>cohort { 0 | 1 }</code></p>
<dd>Specify whether (1) or whether not (0) a server packet will be accepted for the same stratum as the client. The default is 0. See the Automatic Server Discovery page for further details.</p>
<dt><code>floor </code><i>floor</i></p>
<dd>Specify the minimum stratum (inclusive) for acceptable server packest. The default is 1. See the Automatic Server Discovery page for further details.</p>
<dt><code>maxclock </code><i>maxclock</i></p>
<dd>Specify the maximum number of servers retained by the server discovery schemes. The default is 10. See the Automatic Server Discovery page for further details.</p>
<dt><code>maxdist </code><i>maxdistance</i></p>
<dd>Specify the synchronization distance threshold used by the clock selection algorithm. The default is 1.5 s. This determines both the minimum number of packets to set the system clock and the maximum roundtrip delay. It can be decreased to improve reliability or increased to synchronize clocks on the Moon or planets.</p>
<dt><code>minclock </code><i>minclock</i></p>
<dd>Specify the number of servers used by the clustering algorithm as the minimum to include on the candidate list. The default is 3. This is also the number of servers to be averaged by the combining algorithm.</p>
<dt><code>mindist </code><i>mindistance</i></p>
<dd>Specify the minimum distance used by the selection and anticlockhop algorithm. Larger values increase the tolerance for outliers; smaller values increase the selectivity. The default is .001 s. In some cases, such as reference clocks with high jitter and a PPS signal, it is useful to increase the value to insure the intersection interval is always nonempty.</p>
<dt><code>minsane </code><i>minsane</i></p>
<dd>Specify the number of servers used by the selection algorithm as the minimum to set the system clock. The default is 1 for legacy purposes; however, for critical applications the value should be somewhat higher but less than <code>minclock</code>46</p>
<dt><code>orphan </code><i>stratum</i></p>
<dd>Specify the orphan stratum with default 16. If less than 16 this is the stratum assumed by the root servers. See the Association Management page for further details.</dl>
</dl>
<dt><code>trap </code><i>host_address</i><code> [port </code><i>port_number</i><code>] [interface </code><i>interfSace_address</i><code>]</code></p>
<dd>This command configures a trap receiver at the given host address and port number for sending messages with the specified local interface address. If the port number is unspecified, a value of 18447 is used. If the interface address is not specified, the message is sent with a source address of the local interface the message is sent through. Note that on a multihomed host the interface used may vary from time to time with routing changes. The trap receiver will generally log event messages and other information from the server in a log file. While such monitor programs may also request their own trap dynamically, configuring a trap receiver will ensure that no messages are lost when the server is started.</p>
<dt><code>ttl </code><i>hop</i><code> &#8230;</code></p>
<dd>This command specifies a list of TTL values in increasing order. up to 8 values can be specified. In manycast mode these values are used in turn in an expanding-ring search. The default is eight multiples of 32 starting at 31.</p>
<dt><code>dscp </code><i>dscp</i></p>
<dd>This command specifies the Differentiated Services Code Point (DSCP) value that is used in sent NTP packets. The default value is 48 for Class Selector 6 (CS6).</dl>
</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-ntp-conf/">ntp.conf</a>(5) The official HTML documentation. This file was automatically generated from HTML source. </p>
