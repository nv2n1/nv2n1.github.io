---
title: "clamav-milter-conf(5)"
name: "clamav-milter-conf"
section: "5"
letter: "c"
url: "/docs/linux/man/5-clamav-milter-conf/"
description: "clamav-milter.conf – Configuration file for clamav-milter"
---

<p><code>clamav-milter.conf</code> &#8211; Configuration file for clamav-milter</p>
<h2>Description</h2>
<p>clamav-milter.conf contains the configuration options for <a href="/docs/linux/man/8-clamav-milter/">clamav-milter</a>(8).</p>
<h2>File Format</h2>
<p>The file consists of comments and options with arguments. Each line which starts with a hash (<code>#</code>) symbol is ignored by the parser. Options and arguments are case sensitive and of the form <code>Option Argument</code>. The arguments are of the following types:</p>
<dl>
<dt><code>BOOL</code></p>
<dd>Boolean value (yes/no or true/false or 1/0).</p>
<dt><code>STRING</code></p>
<dd>String without blank characters.</p>
<dt><code>SIZE</code></p>
<dd>Size in bytes. You can use &#8216;M&#8217; or &#8216;m&#8217; modifiers for megabytes and &#8216;K&#8217; or &#8216;k&#8217; for kilobytes.</p>
<dt><code>NUMBER</code></p>
<dd>Unsigned integer.</dl>
<h2>Main Options</h2>
<dl>
<dt><code>Example</code></p>
<dd>If this option is set clamav-milter will not run.</p>
<dt><code>MilterSocket STRING</code></p>
<dd>Define the interface through which we communicate with sendmail. This option is mandatory!<br />
 Possible formats are:<br />
 [[unix|local]:]/path/to/file &#8211; to specify a unix domain socket<br />
 inet:port@[hostname|ip-address] &#8211; to specify an ipv4 socket<br />
 inet6:port@[hostname|ip-address] &#8211; to specify an ipv6 socket<br />
 Default: unset</p>
<dt><code>MilterSocketGroup STRING</code></p>
<dd>Define the group ownership for the (unix) milter socket.<br />
 Default: disabled (the primary group of the user running clamd)</p>
<dt><code>MilterSocketMode STRING</code></p>
<dd>Sets the permissions on the (unix) milter socket to the specified mode.<br />
 Default: disabled (obey umask)</p>
<dt><code>FixStaleSocket BOOL</code></p>
<dd>Remove stale socket after unclean shutdown.<br />
 Default: yes</p>
<dt><code>User STRING</code></p>
<dd>Run as another user (clamav-milter must be started by root for this option to work)<br />
 Default: unset (don&#8217;t drop privileges)</p>
<dt><code>AllowSupplementaryGroups BOOL</code></p>
<dd>Initialize supplementary group access (clamav-milter must be started by root).<br />
 Default: no</p>
<dt><code>ReadTimeout NUMBER</code></p>
<dd>Waiting for data from clamd will timeout after this time (seconds).<br />
 Default: 120</p>
<dt><code>Foreground BOOL</code></p>
<dd>Don&#8217;t fork into background.<br />
 Default: no</p>
<dt><code>Chroot STRING</code></p>
<dd>Chroot to the specified directory. Chrooting is performed just after reading the config file and before dropping privileges.<br />
 Default: unset (don&#8217;t chroot)</p>
<dt><code>PidFile STRING</code></p>
<dd>Save the process identifier of a clamav-milter (main thread) to a specified file.<br />
 Default: disabled</p>
<dt><code>TemporaryDirectory STRING</code></p>
<dd>Optional path to the global temporary directory.<br />
 Default: system specific (usually /tmp or /var/tmp).</dl>
<h2>Clamd Options</h2>
<dl>
<dt><code>ClamdSocket STRING</code></p>
<dd>Define the clamd socket to connect to for scanning. This option is mandatory! Syntax:<br />
 ClamdSocket unix:path<br />
 ClamdSocket tcp:host:port<br />
 The first syntax specifies a local unix socket (needs an absolute path) e.g.:<br />
 ClamdSocket unix:/var/run/clamd/clamd.socket<br />
 The second syntax specifies a tcp local or remote tcp socket: the host can be a hostname or an ip address; the &quot;:port&quot; field is only required for IPv6 addresses, otherwise it defaults to 3310 e.g.:<br />
 ClamdSocket tcp:192.168.0.1<br />
 This option can be repeated several times with different sockets or even with the same socket: clamd servers will be selected in a round-robin fashion.<br />
 Default: no default</dl>
<h2>Exclusions</h2>
<dl>
<dt><code>LocalNet STRING</code></p>
<dd>Messages originating from these hosts/networks will not be scanned. This option takes a host(name)/mask pair in CIRD notation and can be repeated several times. If &quot;/mask&quot; is omitted, a host is assumed. To specify a locally orignated, non-smtp, email use the keyword &quot;local&quot;<br />
 Default: unset (scan everything regardless of the origin)</p>
<dt><code>Whitelist STRING</code></p>
<dd>This option specifies a file which contains a list of basic POSIX regular expressions. Addresses (sent to or from &#8211; see below) matching these regexes will not be scanned. Optionally each line can start with the string &quot;From:&quot; or &quot;To:&quot; (note: no whitespace after the colon) indicating if it is, respectively, the sender or recipient that is to be whitelisted. If the field is missing, &quot;To:&quot; is assumed. Lines starting with #, : or ! are ignored.<br />
 Default: unset (no exclusion applied)</p>
<dt><code>SkipAuthenticated STRING</code></p>
<dd>Messages from authenticated SMTP users matching this extended POSIX regular expression (egrep-like) will not be scanned. As an alternative, a file containing a plain (not regex) list of names (one per line) can be specified using the prefix &quot;file:&quot;. e.g. SkipAuthenticated file:/etc/good_guys. Note: this is the AUTH login name!<br />
 Default: unset (no whitelisting based on SMTP auth)</p>
<dt><code>MaxFileSize SIZE</code></p>
<dd>Messages larger than this value won&#8217;t be scanned. Make sure this value is lower or equal than StreamMaxLength in clamd.conf<br />
 Default: 25M</dl>
<h2>Actions</h2>
<p>The following group of options controls the delievery process under different circumstances. The following actions are available:<br />
 &#8211; Accept: The message is accepted for delievery<br />
 &#8211; Reject: Immediately refuse delievery (a 5xx error is returned to the peer)<br />
 &#8211; Defer: Return a temporary failure message (4xx) to the peer<br />
 &#8211; Blackhole (not available for OnFail): Like Accept but the message is sent to oblivion<br />
 &#8211; Quarantine (not available for OnFail): Like Accept but message is quarantined instead of being delivered. NOTE: In Sendmail the quarantine queue can be examined via mailq -qQ. For Postfix this causes the message to be placed on hold.</p>
<dl>
<dt><code>OnClean STRING</code></p>
<dd>Action to be performed on clean messages (mostly useful for testing)<br />
 Default: Accept</p>
<dt><code>OnInfected STRING</code></p>
<dd>Action to be performed on infected messages<br />
 Default: Quarantine</p>
<dt><code>OnFail STRING</code></p>
<dd>Action to be performed on error conditions (this includes failure to allocate data structures, no scanners available, network timeouts, unknown scanner replies and the like)<br />
 Default: Defer</p>
<dt><code>RejectMsg STRING</code></p>
<dd>This option allows you to set a specific rejection reason for infected messages and it&#8217;s therefore only useful together with &quot;OnInfected Reject&quot;. The string &quot;%v&quot;, if present, will be replaced with the virus name.<br />
 Default: MTA specific</p>
<dt><code>AddHeader STRING</code></p>
<dd>If this option is set to &quot;Replace&quot; (or &quot;Yes&quot;), an &quot;X-Virus-Scanned&quot; and an &quot;X-Virus-Status&quot; headers will be attached to each processed message, possibly replacing existing headers. If it is set to Add, the X-Virus headers are added possibly on top of the existing ones. Note that while &quot;Replace&quot; can potentially break DKIM signatures, &quot;Add&quot; may confuse procmail and similar filters.<br />
 Default: no</p>
<dt><code>ReportHostname STRING</code></p>
<dd>When AddHeader is in use, this option allows you to set the reported hostname. This may be desirable in order to avoid leaking internal names. If unset the real machine name is used.<br />
 Default: disabled</p>
<dt><code>VirusAction STRING</code></p>
<dd>Execute a command (possibly searching PATH) when an infected message is found. The following parameters are passed to the invoked program in this order: virus name, queue id, sender, destination, subject, message id, message date. Note #1: this requires MTA macroes to be available (see LogInfected below). Note #2: the process is invoked in the context of clamav-milter. Note #3: clamav-milter will wait for the process to exit. Be quick or fork to avoid unnecessary delays in email delievery.<br />
 Default: disabled</dl>
<h2>Logging Options</h2>
<dl>
<dt><code>LogFile STRING</code></p>
<dd>Enable logging to selected file.<br />
 Default: no</p>
<dt><code>LogFileUnlock BOOL</code></p>
<dd>Disable a system lock that protects against running clamd with the same configuration file multiple times.<br />
 Default: no</p>
<dt><code>LogFileMaxSize SIZE</code></p>
<dd>Limit the size of the log file. The logger will be automatically disabled if the file is greater than SIZE. Value of 0 disables the limit.<br />
 Default: 1M</p>
<dt><code>LogTime BOOL</code></p>
<dd>Log time for each message.<br />
 Default: no</p>
<dt><code>LogSyslog BOOL</code></p>
<dd>Use system logger (can work together with LogFile).<br />
 Default: no</p>
<dt><code>LogFacility STRING</code></p>
<dd>Specify the type of syslog messages &#8211; please refer to &#8216;man syslog&#8217; for facility names.<br />
 Default: LOG_LOCAL6</p>
<dt><code>LogVerbose BOOL</code></p>
<dd>Enable verbose logging.<br />
 Default: no</p>
<dt><code>LogInfected STRING</code></p>
<dd>This option allows you to tune what is logged when a message is infected. Possible values are Off (the default &#8211; nothing is logged), Basic (minimal info logged), Full (verbose info logged)<br />
 Note: For this to work properly in sendmail, make sure the msg_id, mail_addr, rcpt_addr and i macroes are available in eom. In other words add a line like: Milter.macros.eom={msg_id}, {mail_addr}, {rcpt_addr}, i to your .cf file. Alternatively use the macro: define(`confMILTER_MACROS_EOM&#8217;, `{msg_id}, {mail_addr}, {rcpt_addr}, i&#8217;)<br />
 Postfix should be working fine with the default settings.<br />
 Default: disabled</p>
<dt><code>LogClean STRING</code></p>
<dd>This option allows you to tune what is logged when no threat is found in a scanned message.<br />
 See LogInfected for possible values and caveats.<br />
 Useful in debugging but drastically increases the log size.<br />
 Default: disabled</p>
<dt><code>SupportMultipleRecipients BOOL</code></p>
<dd>This option affects the behaviour of LogInfected, LogClean and VirusAction when a message with multiple recipients is scanned:<br />
 If SupportMultipleRecipients is off (the default) then one single log entry is generated for the message and, in case the message is determined to be malicious, the command indicated by VirusAction is executed just once. In both cases only the last recipient is reported.<br />
 If SupportMultipleRecipients is on then one line is logged for each recipient and the command indicated by VirusAction is also executed once for each recipient.<br />
 Note: although it&#8217;s probably a good idea to enable this option, the default value is currently set to off for legacy reasons.<br />
 Default: no</dl>
<h2>Notes</h2>
<p>All options expressing a size are limited to max 4GB. Values in excess will be resetted to the maximum.</p>
<h2>Files</h2>
<p>/etc/clamav-milter.conf</p>
<h2>Author</h2>
<p>aCaB &lt;acab [at] clamav.net&gt;</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-clamav-milter/">clamav-milter</a>(8), <a href="/docs/linux/man/8-clamd/">clamd</a>(8), <a href="/docs/linux/man/5-clamd-conf/">clamd.conf</a>(5) </p>
