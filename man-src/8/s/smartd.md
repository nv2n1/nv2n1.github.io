---
title: "smartd(8)"
name: "smartd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smartd/"
description: "smartd – SMART Disk Monitoring Daemon"
---

<p><code>smartd</code> &#8211; SMART Disk Monitoring Daemon</p>
<h2>Synopsis</h2>
<p><code>smartd [options]</code> </p>
<h2>Description</h2>
<p>[This man page is generated for the Linux version of smartmontools. It does not contain info specific to other platforms.] <code>smartd</code> is a daemon that monitors the Self-Monitoring, Analysis and Reporting Technology (SMART) system built into most ATA/SATA and SCSI/SAS hard drives and solid-state drives. The purpose of SMART is to monitor the reliability of the hard drive and predict drive failures, and to carry out different types of drive self-tests. This version of <code>smartd</code> is compatible with ACS-3, ACS-2, ATA8-ACS, ATA/ATAPI-7 and earlier standards (see <code>REFERENCES</code> below). <code>smartd</code> will attempt to enable SMART monitoring on ATA devices (equivalent to <code>smartctl -s on</code>) and polls these and SCSI devices every 30 minutes (configurable), logging SMART errors and changes of SMART Attributes via the SYSLOG interface. The default location for these SYSLOG notifications and warnings is system-dependent (typically <code>/var/log/messages</code> or <code>/var/log/syslog</code>). To change this default location, please see the <code>&#8216;-l&#8217;</code> command-line option described below. In addition to logging to a file, <code>smartd</code> can also be configured to send email warnings if problems are detected. Depending upon the type of problem, you may want to run self-tests on the disk, back up the disk, replace the disk, or use a manufacturer&#8217;s utility to force reallocation of bad or unreadable disk sectors. If disk problems are detected, please see the <code>smartctl</code> manual page and the <code>smartmontools</code> web page/FAQ for further guidance. If you send a <code>USR1</code> signal to <code>smartd</code> it will immediately check the status of the disks, and then return to polling the disks every 30 minutes. See the <code>&#8216;-i&#8217;</code> option below for additional details. <code>smartd</code> can be configured at start-up using the configuration file <code>/etc/smartd.conf</code> (Windows: <code>EXEDIR/smartd.conf</code>). If the configuration file is subsequently modified, <code>smartd</code> can be told to re-read the configuration file by sending it a <code>HUP</code> signal, for example with the command:<br />
 <code>killall -HUP smartd</code>.<br />
 On startup, if <code>smartd</code> finds a syntax error in the configuration file, it will print an error message and then exit. However if <code>smartd</code> is already running, then is told with a <code>HUP</code> signal to re-read the configuration file, and then find a syntax error in this file, it will print an error message and then continue, ignoring the contents of the (faulty) configuration file, as if the <code>HUP</code> signal had never been received. When <code>smartd</code> is running in debug mode, the <code>INT</code> signal (normally generated from a shell with CONTROL-C) is treated in the same way as a <code>HUP</code> signal: it makes <code>smartd</code> reload its configuration file. To exit <code>smartd</code> use CONTROL-\ On startup, in the absence of the configuration file <code>/etc/smartd.conf</code>, the <code>smartd</code> daemon first scans for all devices that support SMART. The scanning is done as follows:</p>
<dl>
<dt><code>LINUX:</code></p>
<dd>Examine all entries <code>&quot;/dev/hd[a-t]&quot;</code> for IDE/ATA devices, and <code>&quot;/dev/sd[a-z]&quot;</code>, <code>&quot;/dev/sd[a-c][a-z]&quot;</code> for ATA/SATA or SCSI/SAS devices. Disks behind RAID controllers are not included. [NEW EXPERIMENTAL SMARTD FEATURE] If directive &#8216;-d nvme&#8217; is specified, examine all entries <code>&quot;/dev/nvme[0-99]&quot;</code> for NVMe devices.</dl>
<p> <code>smartd</code> then monitors for <i>all</i> possible SMART errors (corresponding to the <code>&#8216;-a&#8217;</code> Directive in the configuration file; see the <code><a href="/docs/linux/man/5-smartd-conf/">smartd.conf</a></code>(5) man page). </p>
<h2>Options</h2>
<dl>
<dt><code>-A PREFIX, &#8211;attributelog=PREFIX</code></p>
<dd>Writes <code>smartd</code> attribute information (normalized and raw attribute values) to files &#8216;PREFIX&#8221;MODEL-SERIAL.ata.csv&#8217; or &#8216;PREFIX&#8221;VENDOR-MODEL-SERIAL.scsi.csv&#8217;. At each check cycle attributes are logged as a line of semicolon separated triplets of the form &quot;attribute-ID;attribute-norm-value;attribute-raw-value;&quot;. For SCSI devices error counters and temperature recorded in the form &quot;counter-name;counter-value;&quot; Each line is led by a date string of the form &quot;yyyy-mm-dd HH:MM:SS&quot; (in UTC). </p>
<p> If this option is not specified, attribute information is written to files &#8216;/var/lib/smartmontools/attrlog.MODEL-SERIAL.ata.csv&#8217;. To disable attribute log files, specify this option with an empty string argument: &#8216;-A &quot;&quot;&#8217;. MODEL and SERIAL are build from drive identify information, invalid characters are replaced by underline. </p>
<p> If the PREFIX has the form &#8216;/path/dir/&#8217; (e.g. &#8216;/var/lib/smartd/&#8217;), then files &#8216;MODEL-SERIAL.ata.csv&#8217; are created in directory &#8216;/path/dir&#8217;. If the PREFIX has the form &#8216;/path/name&#8217; (e.g. &#8216;/var/lib/misc/attrlog-&#8216;), then files &#8216;nameMODEL-SERIAL.ata.csv&#8217; are created in directory &#8216;/path/&#8217;. The path must be absolute, except if debug mode is enabled.</p>
<dt><code>-B [+]FILE, &#8211;drivedb=[+]FILE</code></p>
<dd>[ATA only] Read the drive database from FILE. The new database replaces the built in database by default. If &#8216;+&#8217; is specified, then the new entries prepend the built in entries. Please see the <code><a href="/docs/linux/man/8-smartctl/">smartctl</a></code>(8) man page for further details.</p>
<dt><code>-c FILE, &#8211;configfile=FILE</code></p>
<dd>Read <code>smartd</code> configuration Directives from FILE, instead of from the default location <code>/etc/smartd.conf</code> (Windows: <code>EXEDIR/smartd.conf</code>). If FILE does <code>not</code> exist, then <code>smartd</code> will print an error message and exit with nonzero status. Thus, &#8216;-c /etc/smartd.conf&#8217; can be used to verify the existence of the default configuration file. </p>
<p> By using &#8216;-&#8216; for FILE, the configuration is read from standard input. This is useful for commands like: </p>
<pre><code>echo /dev/sdb -m user [at] home -M test | smartd -c - -q onecheck</code></pre>
<p>to perform quick and simple checks without a configuration file.</p>
<dt><code>-C, &#8211;capabilities</code></p>
<dd>[Linux only] Use libcap-ng to drop unneeded Linux process <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7). The following capabilities are kept: CAP_SYS_ADMIN, CAP_SYS_RAWIO, CAP_MKNOD. </p>
<p> Warning: Mail notification does not work when used.</p>
<dt><code>-d, &#8211;debug</code></p>
<dd>Runs <code>smartd</code> in &quot;debug&quot; mode. In this mode, it displays status information to STDOUT rather than logging it to SYSLOG and does not <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) into the background and detach from the controlling terminal. In this mode, <code>smartd</code> also prints more verbose information about what it is doing than when operating in &quot;daemon&quot; mode. In this mode, the <code>INT</code> signal (normally generated from a terminal with CONTROL-C) makes <code>smartd</code> reload its configuration file. Please use CONTROL-\ to exit</p>
<dt><code>-D, &#8211;showdirectives</code></p>
<dd>Prints a list (to STDOUT) of all the possible Directives which may appear in the configuration file /etc/smartd.conf, and then exits. These Directives are described in the <code><a href="/docs/linux/man/5-smartd-conf/">smartd.conf</a></code>(5) man page. They may appear in the configuration file following the device name.</p>
<dt><code>-h, &#8211;help, &#8211;usage</code></p>
<dd>Prints usage message to STDOUT and exits.</p>
<dt><code>-i N, &#8211;interval=N</code></p>
<dd>Sets the interval between disk checks to <i>N</i> seconds, where <i>N</i> is a decimal integer. The minimum allowed value is ten and the maximum is the largest positive integer that can be represented on your system (often 2^31-1). The default is 1800 seconds. </p>
<p> Note that the superuser can make <code>smartd</code> check the status of the disks at any time by sending it the <code>SIGUSR1</code> signal, for example with the command: </p>
<pre><code>kill -SIGUSR1 &lt;pid&gt;</code></pre>
<p>where <code>&lt;pid&gt;</code> is the process id number of <code>smartd</code>. One may also use: </p>
<pre><code>killall -USR1 smartd</code></pre>
<p>for the same purpose. </p>
<dt><code>-l FACILITY, &#8211;logfacility=FACILITY</code></p>
<dd>Uses syslog facility FACILITY to log the messages from <code>smartd</code>. Here FACILITY is one of <i>local0</i>, <i>local1</i>, &#8230;, <i>local7</i>, or <i>daemon</i> [default]. If this command-line option is not used, then by default messages from <code>smartd</code> are logged to the facility <i>daemon</i>. </p>
<p> If you would like to have <code>smartd</code> messages logged somewhere other than the default location, include (for example) &#8216;-l local3&#8217; in its start up argument list. Tell the syslog daemon to log all messages from facility <code>local3</code> to (for example) &#8216;/var/log/smartd.log&#8217;. </p>
<p> For more detailed information, please refer to the man pages for the local syslog daemon, typically <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8), <code><a href="/docs/linux/man/8-syslog-ng/">syslog-ng</a></code>(8) or <code><a href="/docs/linux/man/8-rsyslogd/">rsyslogd</a></code>(8).</p>
<dt><code>-n, &#8211;no-fork</code></p>
<dd>Do not fork into background; this is useful when executed from modern init methods like initng, minit, supervise or systemd.</p>
<dt><code>-p NAME, &#8211;pidfile=NAME</code></p>
<dd>Writes pidfile <i>NAME</i> containing the <code>smartd</code> Process ID number (PID). To avoid symlink attacks make sure the directory to which pidfile is written is only writable for root. Without this option, or if the &#8211;debug option is given, no PID file is written on startup. If <code>smartd</code> is killed with a maskable signal then the pidfile is removed.</p>
<dt><code>-q WHEN, &#8211;quit=WHEN</code></p>
<dd>Specifies when, if ever, <code>smartd</code> should exit. The valid arguments are to this option are: </p>
<p> <i>nodev</i> &#8211; Exit if there are no devices to monitor, or if any errors are found at startup in the configuration file. This is the default. </p>
<p> <i>errors</i> &#8211; Exit if there are no devices to monitor, or if any errors are found in the configuration file /etc/smartd.conf at startup or whenever it is reloaded. </p>
<p> <i>nodevstartup</i> &#8211; Exit if there are no devices to monitor at startup. But continue to run if no devices are found whenever the configuration file is reloaded. </p>
<p> <i>never</i> &#8211; Only exit if a fatal error occurs (no remaining system memory, invalid command line arguments). In this mode, even if there are no devices to monitor, or if the configuration file <code>/etc/smartd.conf</code> has errors, <code>smartd</code> will continue to run, waiting to load a configuration file listing valid devices. </p>
<p> <i>onecheck</i> &#8211; Start <code>smartd</code> in debug mode, then register devices, then check device&#8217;s SMART status once, and then exit with zero exit status if all of these steps worked correctly. </p>
<p> This last option is intended for &#8216;distribution-writers&#8217; who want to create automated scripts to determine whether or not to automatically start up <code>smartd</code> after installing smartmontools. After starting <code>smartd</code> with this command-line option, the distribution&#8217;s install scripts should wait a reasonable length of time (say ten seconds). If <code>smartd</code> has not exited with zero status by that time, the script should send <code>smartd</code> a SIGTERM or SIGKILL and assume that <code>smartd</code> will not operate correctly on the host. Conversely, if <code>smartd</code> exits with zero status, then it is safe to run <code>smartd</code> in normal daemon mode. If <code>smartd</code> is unable to monitor any devices or encounters other problems then it will return with non-zero exit status. </p>
<p> <i>showtests</i> &#8211; Start <code>smartd</code> in debug mode, then register devices, then write a list of future scheduled self tests to stdout, and then exit with zero exit status if all of these steps worked correctly. Device&#8217;s SMART status is not checked. </p>
<p> This option is intended to test whether the &#8216;-s REGEX&#8217; directives in smartd.conf will have the desired effect. The output lists the next test schedules, limited to 5 tests per type and device. This is followed by a summary of all tests of each device within the next 90 days.</p>
<dt><code>-r TYPE, &#8211;report=TYPE</code></p>
<dd>Intended primarily to help <code>smartmontools</code> developers understand the behavior of <code>smartmontools</code> on non-conforming or poorly-conforming hardware. This option reports details of <code>smartd</code> transactions with the device. The option can be used multiple times. When used just once, it shows a record of the ioctl() transactions with the device. When used more than once, the detail of these ioctl() transactions are reported in greater detail. The valid arguments to this option are: </p>
<p> <i>ioctl</i> &#8211; report all ioctl() transactions. </p>
<p> <i>ataioctl</i> &#8211; report only ioctl() transactions with ATA devices. </p>
<p> <i>scsiioctl</i> &#8211; report only ioctl() transactions with SCSI devices. </p>
<p> <i>nvmeioctl</i> &#8211; [FreeBSD, Linux, Windows and Cygwin only] [NEW EXPERIMENTAL SMARTD FEATURE] report only ioctl() transactions with NVMe devices. </p>
<p> Any argument may include a positive integer to specify the level of detail that should be reported. The argument should be followed by a comma then the integer with no spaces. For example, <i>ataioctl,2</i> The default level is 1, so &#8216;-r ataioctl,1&#8217; and &#8216;-r ataioctl&#8217; are equivalent.</p>
<dt><code>-s PREFIX, &#8211;savestates=PREFIX</code></p>
<dd>Reads/writes <code>smartd</code> state information from/to files &#8216;PREFIX&#8221;MODEL-SERIAL.ata.state&#8217; or &#8216;PREFIX&#8221;VENDOR-MODEL-SERIAL.scsi.state&#8217;. This preserves SMART attributes, drive min and max temperatures (-W directive), info about last sent warning email (-m directive), and the time of next check of the self-test REGEXP (-s directive) across boot cycles. </p>
<p> If this option is not specified, state information is maintained in files &#8216;/var/lib/smartmontools/smartd.MODEL-SERIAL.ata.state&#8217; for ATA devices and &#8216;/var/lib/smartmontools/smartd.VENDOR-MODEL-SERIAL.scsi.state&#8217; for SCSI devices. To disable state files, specify this option with an empty string argument: &#8216;-s &quot;&quot;&#8217;. MODEL and SERIAL are build from drive identify information, invalid characters are replaced by underline. </p>
<p> If the PREFIX has the form &#8216;/path/dir/&#8217; (e.g. &#8216;/var/lib/smartd/&#8217;), then files &#8216;MODEL-SERIAL.ata.state&#8217; are created in directory &#8216;/path/dir&#8217;. If the PREFIX has the form &#8216;/path/name&#8217; (e.g. &#8216;/var/lib/misc/smartd-&#8216;), then files &#8216;nameMODEL-SERIAL.ata.state&#8217; are created in directory &#8216;/path/&#8217;. The path must be absolute, except if debug mode is enabled. </p>
<p> The state information files are read on smartd startup. The files are always (re)written after reading the configuration file, before rereading the configuration file (SIGHUP), before smartd shutdown, and after a check forced by SIGUSR1. After a normal check cycle, a file is only rewritten if an important change (which usually results in a SYSLOG output) occurred.</p>
<dt><code>-w PATH, &#8211;warnexec=PATH</code></p>
<dd>Run the executable PATH instead of the default script when smartd needs to send warning messages. PATH must point to an executable binary file or script. The default script is <code>/usr/share/smartmontools/smartd_warning.sh</code>.</p>
<dt><code>-V, &#8211;version, &#8211;license, &#8211;copyright</code></p>
<dd>Prints version, copyright, license, home page and SVN revision information for your copy of <code>smartd</code> to STDOUT and then exits. Please include this information if you are reporting bugs or problems. </p>
</dl>
<h2>Examples</h2>
<p><code>smartd</code><br />
 Runs the daemon in forked mode. This is the normal way to run <code>smartd</code>. Entries are logged to SYSLOG. <code>smartd -d -i 30</code><br />
 Run in foreground (debug) mode, checking the disk status every 30 seconds. <code>smartd -q onecheck</code><br />
 Registers devices, and checks the status of the devices exactly once. The exit status (the shell <code>$?</code> variable) will be zero if all went well, and nonzero if no devices were detected or some other problem was encountered. </p>
<h2>Configuration</h2>
<p>The syntax of the <code><a href="/docs/linux/man/5-smartd-conf/">smartd.conf</a></code>(5) file is discussed separately.</p>
<h2>Notes</h2>
<p><code>smartd</code> will make log entries at loglevel <code>LOG_INFO</code> if the Normalized SMART Attribute values have changed, as reported using the <code>&#8216;-t&#8217;, &#8216;-p&#8217;,</code> or <code>&#8216;-u&#8217;</code> Directives. For example: </p>
<pre><code>'Device: /dev/sda, SMART Attribute: 194 Temperature_Celsius changed from 94 to 93'</code></pre>
<p>Note that in this message, the value given is the &#8216;Normalized&#8217; not the &#8216;Raw&#8217; Attribute value (the disk temperature in this case is about 22 Celsius). The <code>&#8216;-R&#8217;</code> and <code>&#8216;-r&#8217;</code> Directives modify this behavior, so that the information is printed with the Raw values as well, for example: </p>
<pre><code>'Device: /dev/sda, SMART Attribute: 194 Temperature_Celsius changed from 94 [Raw 22] to 93 [Raw 23]'</code></pre>
<p>Here the Raw values are the actual disk temperatures in Celsius. The way in which the Raw values are printed, and the names under which the Attributes are reported, is governed by the various <code>&#8216;-v Num,Description&#8217;</code> Directives described previously. Please see the <code>smartctl</code> manual page for further explanation of the differences between Normalized and Raw Attribute values. <code>smartd</code> will make log entries at loglevel <code>LOG_CRIT</code> if a SMART Attribute has failed, for example: </p>
<pre><code>'Device: /dev/sdc, Failed SMART Attribute: 5 Reallocated_Sector_Ct'</code></pre>
<p>&nbsp;This loglevel is used for reporting enabled by the <code>&#8216;-H&#8217;, -f&#8217;, &#8216;-l selftest&#8217;,</code> and <code>&#8216;-l error&#8217;</code> Directives. Entries reporting failure of SMART Prefailure Attributes should not be ignored: they mean that the disk is failing. Use the <code>smartctl</code> utility to investigate. </p>
<h2>Log Timestamp Timezone</h2>
<p>When <code>smartd</code> makes log entries, these are time-stamped. The time stamps are in the computer&#8217;s local time zone, which is generally set using either the environment variable &#8216;<code>TZ</code>&#8216; or using a time-zone file such as <code>/etc/localtime</code>. You may wish to change the timezone while <code>smartd</code> is running (for example, if you carry a laptop to a new time-zone and don&#8217;t reboot it). Due to a bug in the <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3) function of many unix standard C libraries, the time-zone stamps of <code>smartd</code> might not change. For some systems, <code>smartd</code> will work around this problem <i>if</i> the time-zone is set using <code>/etc/localtime</code>. The work-around <i>fails</i> if the time-zone is set using the &#8216;<code>TZ</code>&#8216; variable (or a file that it points to).</p>
<h2>Exit Status</h2>
<p>The exit status (return value) of <code>smartd</code> can have the following values:</p>
<dl>
<dt><code>0:</code></p>
<dd>Daemon startup successful, or <code>smartd</code> was killed by a SIGTERM (or in debug mode, a SIGQUIT).</p>
<dt><code>1:</code></p>
<dd>Commandline did not parse.</p>
<dt><code>2:</code></p>
<dd>There was a syntax error in the config file.</p>
<dt><code>3:</code></p>
<dd>Forking the daemon failed.</p>
<dt><code>4:</code></p>
<dd>Couldn&#8217;t create PID file.</p>
<dt><code>5:</code></p>
<dd>Config file does not exist (only returned in conjunction with the &#8216;-c&#8217; option).</p>
<dt><code>6:</code></p>
<dd>Config file exists, but cannot be read.</p>
<dt><code>8:</code></p>
<dd><code>smartd</code> ran out of memory during startup.</p>
<dt><code>10:</code></p>
<dd>An inconsistency was found in <code>smartd</code>&#8216;s internal data structures. This should never happen. It must be due to either a coding or compiler bug. <i>Please</i> report such failures to smartmontools developers, see REPORTING BUGS below.</p>
<dt><code>16:</code></p>
<dd>A device explicitly listed in <code>/etc/smartd.conf</code> can&#8217;t be monitored.</p>
<dt><code>17:</code></p>
<dd><code>smartd</code> didn&#8217;t find any devices to monitor.</p>
<dt><code>254:</code></p>
<dd>When in daemon mode, <code>smartd</code> received a SIGINT or SIGQUIT. (Note that in debug mode, SIGINT has the same effect as SIGHUP, and makes <code>smartd</code> reload its configuration file. SIGQUIT has the same effect as SIGTERM and causes <code>smartd</code> to exit with zero exit status.</p>
<dt><code>132 and above</code></p>
<dd><code>smartd</code> was killed by a signal that is not explicitly listed above. The exit status is then 128 plus the signal number. For example if <code>smartd</code> is killed by SIGKILL (signal 9) then the exit status is 137. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/usr/sbin/smartd</code></p>
<dd>full path of this executable.</p>
<dt><code>/etc/smartd.conf</code></p>
<dd>configuration file (see <code><a href="/docs/linux/man/5-smartd-conf/">smartd.conf</a></code>(5) man page).</p>
<dt><code>/usr/share/smartmontools/smartd_warning.sh</code></p>
<dd>script run on warnings (see &#8216;-M exec&#8217; directive on <code><a href="/docs/linux/man/5-smartd-conf/">smartd.conf</a></code>(5) man page).</p>
<dt><code>/etc/smartmontools/smartd_warning.d/</code></p>
<dd>plugin directory for smartd warning script (see &#8216;-m&#8217; directive on <code><a href="/docs/linux/man/5-smartd-conf/">smartd.conf</a></code>(5) man page).</p>
<dt><code>/var/lib/smartmontools/drivedb/drivedb.h</code></p>
<dd>drive database (see &#8216;-B&#8217; option).</p>
<dt><code>/etc/smart_drivedb.h</code></p>
<dd>optional local drive database (see &#8216;-B&#8217; option). </p>
</dl>
<h2>Authors</h2>
<p><code>Bruce Allen</code> (project initiator),<br />
 <code>Christian Franke</code> (project manager, Windows port and all sort of things),<br />
 <code>Douglas Gilbert</code> (SCSI subsystem),<br />
 <code>Volker Kuhlmann</code> (moderator of support and database mailing list),<br />
 <code>Gabriele Pohl</code> (wiki &amp; development team support),<br />
 <code>Alex Samorukov</code> (FreeBSD port and more, new Trac wiki). </p>
<p> Many other individuals have made contributions and corrections, see AUTHORS, ChangeLog and repository files. </p>
<p> The first smartmontools code was derived from the smartsuite package, written by Michael Cornwell and Andre Hedrick.</p>
<h2>Reporting Bugs</h2>
<p>To submit a bug report, create a ticket in smartmontools wiki:<br />
 &lt;<code><a rel="nofollow" href="http://www.smartmontools.org/">http://www.smartmontools.org/</a></code>&gt;.<br />
 Alternatively send the info to the smartmontools support mailing list:<br />
 &lt;<code><a rel="nofollow" href="https://lists.sourceforge.net/lists/listinfo/smartmontools-support">https://lists.sourceforge.net/lists/listinfo/smartmontools-support</a>&gt;. </p>
<p> </code></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-smartd-conf/">smartd.conf</a></code>(5), <code><a href="/docs/linux/man/8-smartctl/">smartctl</a></code>(8).<br />
 <code><a href="/docs/linux/man/8-update-smart-drivedb/">update-smart-drivedb</a></code>(8). </p>
<h2>References</h2>
<p>Please see the following web site for more info: <code><a rel="nofollow" href="http://www.smartmontools.org/">http://www.smartmontools.org/</a></code> </p>
<p> An introductory article about smartmontools is <i>Monitoring Hard Disks with SMART</i>, by Bruce Allen, Linux Journal, January 2004, pages 74-77. This is <code><a rel="nofollow" href="http://www.linuxjournal.com/article/6983">http://www.linuxjournal.com/article/6983</a></code> online. </p>
<p> If you would like to understand better how SMART works, and what it does, a good place to start is with Sections 4.8 and 6.54 of the first volume of the &#8216;AT Attachment with Packet Interface-7&#8217; (ATA/ATAPI-7) specification Revision 4b. This documents the SMART functionality which the <code>smartmontools</code> utilities provide access to. </p>
<p> The functioning of SMART was originally defined by the SFF-8035i revision 2 and the SFF-8055i revision 1.4 specifications. These are publications of the Small Form Factors (SFF) Committee. </p>
<p> Links to these and other documents may be found on the Links page of the <code>smartmontools</code> Wiki at <code><a rel="nofollow" href="http://www.smartmontools.org/wiki/Links">http://www.smartmontools.org/wiki/Links</a></code> .</p>
<h2>Package Version</h2>
<p>smartmontools-6.6 2016-05-31 r4324<br />
 $Id: smartd.8.in 4299 2016-04-16 19:45:57Z chrfranke $</p>
