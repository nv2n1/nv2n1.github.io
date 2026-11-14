---
title: "watchdog-conf(5)"
name: "watchdog-conf"
section: "5"
letter: "w"
url: "/docs/linux/man/5-watchdog-conf/"
description: "watchdog.conf – configuration file for the watchdog daemon"
---

<p>watchdog.conf &#8211; configuration file for the watchdog daemon</p>
<h2>Description</h2>
<p>This file carries all configuration options for the Linux watchdog daemon. Each option has to be written on a line for itself. Comments start with &#8216;#&#8217;. Blanks are ignored except after the &#8216;=&#8217; sign. An empty text after the &#8216;=&#8217; sign disables the feature as long as that makes sense.</p>
<h2>Options</h2>
<dl>
<dt>interval = &lt;interval&gt;</p>
<dd>Set the interval between two writes to the watchdog device. The kernel drivers expects a write command every minute. Otherwise the system will be rebooted. Default value is 1 second. An interval of more than a minute can only be used with the -f command-line option.</p>
<dt>logtick = &lt;logtick&gt;</p>
<dd>If you enable verbose logging, a message is written into the syslog or a logfile. While this is nice, it is not necessary to get a message every 10 seconds which really fills up disk and needs CPU. logtick allows adjustment of the number of intervals skipped before a log message is written. If you use logtick = 60 and interval = 10, only every 10 minutes (600 seconds) a message is written. This may make the exact time of a crash harder to find but greatly reduces disk usage and administrator nerves if you&#8217;re looking for a particular syslog entry in between of watchdog messages.</p>
<dt>max-load-1 = &lt;load1&gt;</p>
<dd>Set the maximal allowed load average for a 1 minute span. Once this load average is reached the system is rebooted. Default value is 0. That means the load average check is disabled. Be careful not to this parameter too low. To set a value less then the predefined minimal value of 2, you have to use the -f commandline option.</p>
<dt>max-load-5 = &lt;load5&gt;</p>
<dd>Set the maximal allowed load average for a 5 minute span. Once this load average is reached the system is rebooted. Default value is 3/4*max-load-1. Be careful not to this parameter too low. To set a value less then the predefined minimal value of 2, you have to use the -f commandline option.</p>
<dt>max-load-15 = &lt;load15&gt;</p>
<dd>Set the maximal allowed load average for a 15 minute span. Once this load average is reached the system is rebooted. Default value is 1/2*max-load-1. Be careful not to this parameter too low. To set a value less then the predefined minimal value of 2, you have to use the -f commandline option.</p>
<dt>min-memory = &lt;minpage&gt;</p>
<dd>Set the minimal amount of virtual memory that has to stay free. Note that this is in pages. Default value is 0 pages which means this test is disabled. The page size is taken from the system include files.</p>
<dt>max-temperature = &lt;temp&gt;</p>
<dd>Set the maximal allowed temperature. Once this temperature is reached the system is halted. Default value is 120. There is no unit conversion, so make sure you use the same unit as your hardware. Watchdog will issue warnings once the temperature increases 90%, 95% and 98% of this temperature.</p>
<dt>watchdog-device = &lt;device&gt;</p>
<dd>Set the watchdog device name. Default is to disable keep alive support.</p>
<dt>watchdog-timeout = &lt;timeout&gt;</p>
<dd>Set the watchdog device timeout during startup. If not set, the default is driver-dependent.</p>
<dt>temperature-device = &lt;temp-dev&gt;</p>
<dd>Set the temperature device name. Default is to disable temperature checking.</p>
<dt>file = &lt;filename&gt;</p>
<dd>Set file name for file mode. This option can be given as often as you like to check several files.</p>
<dt>change = &lt;mtime&gt;</p>
<dd>Set the change interval time for file mode. This options always belongs to the active filename, that is when finding a &#8216;change =&#8217; line watchdog assumes it belongs to the most recently read &#8216;file =&#8217; line. They don&#8217;t neccessarily have to follow each other directly. But you cannot specify a &#8216;change =&#8217; before a &#8216;file =&#8217;. The default is to only stat the file and don&#8217;t look for changes. Using this feature to monitor changes in /var/log/messages might require some special syslog daemon configuration, e.g. rsyslog needs &quot;$ActionWriteAllMarkMessages on&quot; to be set to make sure the marks are written no matter what.</p>
<dt>pidfile = &lt;pidfilename&gt;</p>
<dd>Set pidfile name for server test mode. This option can be given as often as you like to check several servers. See the Systemd section in watchdog (8) for more information.</p>
<dt>ping = &lt;ip-addr&gt;</p>
<dd>Set IP address for ping mode. This option can be used more than once to check different connections.</p>
<dt>interface = &lt;if-name&gt;</p>
<dd>Set interface name for network mode. This option can be used more than once to check different interfaces.</p>
<dt>test-binary = &lt;testbin&gt;</p>
<dd>Execute the given binary to do some user defined tests. With enforcing SELinux policy please use the /usr/libexec/watchdog/scripts/ for your test-binary configuration.</p>
<dt>test-timeout = &lt;timeout in seconds&gt;</p>
<dd>User defined tests may only run for &lt;timeout&gt; seconds. Set to 0 for unlimited.</p>
<dt>repair-binary = &lt;repbin&gt;</p>
<dd>Execute the given binary in case of a problem instead of shutting down the system. With enforcing SELinux policy please use the /usr/libexec/watchdog/scripts/ for your repair-binary configuration.</p>
<dt>repair-timeout = &lt;timeout in seconds&gt;</p>
<dd>repair command may only run for &lt;timeout&gt; seconds. Set to 0 for unlimited.</p>
<dt>admin = &lt;mail-address&gt;</p>
<dd>Email address to send admin mail to. That is, who shall be notified that the machine is being halted or rebooted. Default is &#8216;root&#8217;. If you want to disable notification via email just set admin to en empty string.</p>
<dt>realtime = &lt;yes|no&gt;</p>
<dd>If set to yes watchdog will lock itself into memory so it is never swapped out.</p>
<dt>priority = &lt;schedule priority&gt;</p>
<dd>Set the schedule priority for realtime mode.</p>
<dt>test-directory = &lt;test directory&gt;</p>
<dd>Set the directory to run user test/repair scripts. Default is &#8216;/etc/watchdog.d&#8217; The /etc/watchdog.d/ is recognized by SELinux policy. See the Test Directory section in <a href="/docs/linux/man/8-watchdog/">watchdog</a>(8) for more information.</p>
<dt>log-dir = &lt;log directory&gt;</p>
<dd>Set the log directory to capture the standard output and standard error from repair-binary and test-binary execution. Default is &#8216;/var/log/watchdog&#8217;.</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/watchdog.conf </i></p>
<dd>The watchdog configuration file</p>
<dt><i>/etc/watchdog.d</i></p>
<dd>A directory containing test-or-repair commands. See the Test Directory section in <a href="/docs/linux/man/8-watchdog/">watchdog</a>(8) for more information.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-watchdog/">watchdog</a></code>(8) </p>
