---
title: "timedatectl(1)"
name: "timedatectl"
section: "1"
letter: "t"
url: "/docs/linux/man/1-timedatectl/"
description: "timedatectl – Control the system time and date"
---

<h2 class="name">NAME</h2>
<p> timedatectl &#8211; Control the system time and date </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>timedatectl</code> [OPTIONS&#8230;] {COMMAND}</dl>
<h2>DESCRIPTION</h2>
<p> <code>timedatectl</code></p>
<dd>may be used to query and change the system clock and its settings, and enable or disable time synchronization services. </p>
<p> Use <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1) to initialize the system time zone for mounted (but not booted) system images. </p>
<p> <code>timedatectl</code> may be used to show the current status of time synchronization services, for example <code><a href="/docs/linux/man/8-systemd-timesyncd-service/">systemd-timesyncd.service</a></code>(8).</p>
<h2>COMMANDS</h2>
<p> The following commands are understood: </p>
<p> <code>status</code></p>
<dl>
<dt>
<dd> Show current settings of the system clock and RTC, including whether network time synchronization is active. If no command is specified, this is the implied default.</dl>
<p> <code>show</code></p>
<dl>
<dt>
<dd> Show the same information as <code>status</code>, but in machine readable form. This command is intended to be used whenever computer-parsable output is required. Use <code>status</code> if you are looking for formatted human-readable output. </p>
<p> By default, empty properties are suppressed. Use <code>&#8211;all</code> to show those too. To select specific properties to show, use <code>&#8211;property=</code>.</dl>
<p> <code>set-time [TIME]</code></p>
<dl>
<dt>
<dd> Set the system clock to the specified time. This will also update the RTC time accordingly. The time may be specified in the format &quot;2012-10-30 18:17:16&quot;.</dl>
<p> <code>set-timezone [TIMEZONE]</code></p>
<dl>
<dt>
<dd> Set the system time zone to the specified value. Available timezones can be listed with <code>list-timezones</code>. If the RTC is configured to be in the local time, this will also update the RTC time. This call will alter the /etc/localtime symlink. See <code><a href="/docs/linux/man/5-localtime/">localtime</a></code>(5) for more information.</dl>
<p> <code>list-timezones</code></p>
<dl>
<dt>
<dd> List available time zones, one per line. Entries from the list can be set as the system timezone with <code>set-timezone</code>.</dl>
<p> <code>set-local-rtc [BOOL]</code></p>
<dl>
<dt>
<dd> Takes a boolean argument. If &quot;0&quot;, the system is configured to maintain the RTC in universal time. If &quot;1&quot;, it will maintain the RTC in local time instead. Note that maintaining the RTC in the local timezone is not fully supported and will create various problems with time zone changes and daylight saving adjustments. If at all possible, keep the RTC in UTC mode. Note that invoking this will also synchronize the RTC from the system clock, unless <code>&#8211;adjust-system-clock</code> is passed (see above). This command will change the 3rd line of /etc/adjtime, as documented in <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8).</dl>
<p> <code>set-ntp [BOOL]</code></p>
<dl>
<dt>
<dd> Takes a boolean argument. Controls whether network time synchronization is active and enabled (if available). If the argument is true, this enables and starts the first existing network synchronization service. If the argument is false, then this disables and stops the known network synchronization services. The way that the list of services is built is described in <code><a href="/docs/linux/man/8-systemd-timedated-service/">systemd-timedated.service</a></code>(8).</dl>
<h3>systemd-timesyncd Commands</h3>
<p> The following commands are specific to <code><a href="/docs/linux/man/8-systemd-timesyncd-service/">systemd-timesyncd.service</a></code>(8). </p>
<p> <code>timesync-status</code></p>
<dl>
<dt>
<dd> Show current status of <code><a href="/docs/linux/man/8-systemd-timesyncd-service/">systemd-timesyncd.service</a></code>(8). If <code>&#8211;monitor</code> is specified, then this will monitor the status updates.</dl>
<p> <code>show-timesync</code></p>
<dl>
<dt>
<dd> Show the same information as <code>timesync-status</code>, but in machine readable form. This command is intended to be used whenever computer-parsable output is required. Use <code>timesync-status</code> if you are looking for formatted human-readable output. </p>
<p> By default, empty properties are suppressed. Use <code>&#8211;all</code> to show those too. To select specific properties to show, use <code>&#8211;property=</code>.</dl>
<p> <code>ntp-servers </code><i>INTERFACE</i><i>SERVER</i><code>&#8230;</code></p>
<dl>
<dt>
<dd> Set the interface specific NTP servers. This command can be used only when the interface is managed by <code>systemd-networkd</code>.</dl>
<p> <code>revert </code><i>INTERFACE</i></p>
<dl>
<dt>
<dd> Revert the interface specific NTP servers. This command can be used only when the interface is managed by <code>systemd-networkd</code>.</dl>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;no-ask-password</code></p>
<dl>
<dt>
<dd> Do not query the user for authentication for privileged operations.</dl>
<p> <code>&#8211;adjust-system-clock</code></p>
<dl>
<dt>
<dd> If <code>set-local-rtc</code> is invoked and this option is passed, the system clock is synchronized from the RTC again, taking the new setting into account. Otherwise, the RTC is synchronized from the system clock.</dl>
<p> <code>&#8211;monitor</code></p>
<dl>
<dt>
<dd> If <code>timesync-status</code> is invoked and this option is passed, then <code>timedatectl</code> monitors the status of <code><a href="/docs/linux/man/8-systemd-timesyncd-service/">systemd-timesyncd.service</a></code>(8) and updates the outputs. Use Ctrl+C to terminate the monitoring.</dl>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dt>
<dd> When showing properties of <code><a href="/docs/linux/man/8-systemd-timesyncd-service/">systemd-timesyncd.service</a></code>(8), show all properties regardless of whether they are set or not.</dl>
<p> <code>-p</code>, <code>&#8211;property=</code></p>
<dl>
<dt>
<dd> When showing properties of <code><a href="/docs/linux/man/8-systemd-timesyncd-service/">systemd-timesyncd.service</a></code>(8), limit display to certain properties as specified as argument. If not specified, all set properties are shown. The argument should be a property name, such as &quot;ServerName&quot;. If specified more than once, all properties with the specified names are shown.</dl>
<p> <code>&#8211;value</code></p>
<dl>
<dt>
<dd> When printing properties with <code>show-timesync</code>, only print the value, and skip the property name and &quot;=&quot;.</dl>
<p> <code>-H</code>, <code>&#8211;host=</code></p>
<dl>
<dt>
<dd> Execute the operation remotely. Specify a hostname, or a username and hostname separated by &quot;@&quot;, to connect to. The hostname may optionally be suffixed by a port ssh is listening on, separated by &quot;:&quot;, and then a container name, separated by &quot;/&quot;, which connects directly to a specific container on the specified host. This will use SSH to talk to the remote machine manager instance. Container names may be enumerated with <code>machinectl -H </code><i>HOST</i>. Put IPv6 addresses in brackets.</dl>
<p> <code>-M</code>, <code>&#8211;machine=</code></p>
<dl>
<dt>
<dd> Execute operation on a local container. Specify a container name to connect to, optionally prefixed by a user name to connect as and a separating &quot;@&quot; character. If the special string &quot;.host&quot; is used in place of the container name, a connection to the local system is made (which is useful to connect to a specific user&#8217;s user bus: &quot;&#8211;user &#8211;machine=lennart [at] .host&quot;). If the &quot;@&quot; syntax is not used, the connection is made as root user. If the &quot;@&quot; syntax is used either the left hand side or the right hand side may be omitted (but not both) in which case the local user name and &quot;.host&quot; are implied.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
<dd> Do not pipe output into a pager.</dl>
<h2>EXIT STATUS</h2>
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>ENVIRONMENT</h2>
<p> <i>$SYSTEMD_LOG_LEVEL</i></p>
<dl>
<dt>
<dd> The maximum log level of emitted messages (messages with a higher log level, i.e. less important ones, will be suppressed). Either one of (in order of decreasing importance) <code>emerg</code>, <code>alert</code>, <code>crit</code>, <code>err</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, <code>debug</code>, or an integer in the range 0&#8230;7. See <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for more information.</dl>
<p> <i>$SYSTEMD_LOG_COLOR</i></p>
<dl>
<dt>
<dd> A boolean. If true, messages written to the tty will be colored according to priority. </p>
<p> This setting is only useful when messages are written directly to the terminal, because <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) and other tools that display logs will color messages based on the log level on their own.</dl>
<p> <i>$SYSTEMD_LOG_TIME</i></p>
<dl>
<dt>
<dd> A boolean. If true, console log messages will be prefixed with a timestamp. </p>
<p> This setting is only useful when messages are written directly to the terminal or a file, because <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) and other tools that display logs will attach timestamps based on the entry metadata on their own.</dl>
<p> <i>$SYSTEMD_LOG_LOCATION</i></p>
<dl>
<dt>
<dd> A boolean. If true, messages will be prefixed with a filename and line number in the source code where the message originates. </p>
<p> Note that the log location is often attached as metadata to journal entries anyway. Including it directly in the message text can nevertheless be convenient when debugging programs.</dl>
<p> <i>$SYSTEMD_LOG_TID</i></p>
<dl>
<dt>
<dd> A boolean. If true, messages will be prefixed with the current numerical thread ID (TID). </p>
<p> Note that the this information is attached as metadata to journal entries anyway. Including it directly in the message text can nevertheless be convenient when debugging programs.</dl>
<p> <i>$SYSTEMD_LOG_TARGET</i></p>
<dl>
<dt>
<dd> The destination for log messages. One of <code>console</code> (log to the attached tty), <code>console-prefixed</code> (log to the attached tty but with prefixes encoding the log level and &quot;facility&quot;, see <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code>kmsg</code> (log to the kernel circular log buffer), <code>journal</code> (log to the journal), <code>journal-or-kmsg</code> (log to the journal if available, and to kmsg otherwise), <code>auto</code> (determine the appropriate log target automatically, the default), <code>null</code> (disable log output).</dl>
<p> <i>$SYSTEMD_PAGER</i></p>
<dl>
<dt>
<dd> Pager to use when <code>&#8211;no-pager</code> is not given; overrides <i>$PAGER</i>. If neither <i>$SYSTEMD_PAGER</i> nor <i>$PAGER</i> are set, a set of well-known pager implementations are tried in turn, including <code><a href="/docs/linux/man/1-less/">less</a></code>(1) and <code><a href="/docs/linux/man/1-more/">more</a></code>(1), until one is found. If no pager implementation is discovered no pager is invoked. Setting this environment variable to an empty string or the value &quot;cat&quot; is equivalent to passing <code>&#8211;no-pager</code>.</dl>
<p> <i>$SYSTEMD_LESS</i></p>
<dl>
<dt>
<dd> Override the options passed to <code>less</code> (by default &quot;FRSXMK&quot;). </p>
<p> Users might want to change two options in particular: </p>
<p> <code>K</code></p>
<dl>
<dt>
<dd> This option instructs the pager to exit immediately when Ctrl+C is pressed. To allow <code>less</code> to handle Ctrl+C itself to switch back to the pager command prompt, unset this option. </p>
<p> If the value of <i>$SYSTEMD_LESS</i> does not include &quot;K&quot;, and the pager that is invoked is <code>less</code>, Ctrl+C will be ignored by the executable, and needs to be handled by the pager.</dl>
<p> <code>X</code></p>
<dl>
<dt>
<dd> This option instructs the pager to not send termcap initialization and deinitialization strings to the terminal. It is set by default to allow command output to remain visible in the terminal even after the pager exits. Nevertheless, this prevents some pager functionality from working, in particular paged output cannot be scrolled with the mouse.</dl>
<p> See <code><a href="/docs/linux/man/1-less/">less</a></code>(1) for more discussion.</dl>
<p> <i>$SYSTEMD_LESSCHARSET</i></p>
<dl>
<dt>
<dd> Override the charset passed to <code>less</code> (by default &quot;utf-8&quot;, if the invoking terminal is determined to be UTF-8 compatible).</dl>
<p> <i>$SYSTEMD_PAGERSECURE</i></p>
<dl>
<dt>
<dd> Takes a boolean argument. When true, the &quot;secure&quot; mode of the pager is enabled; if false, disabled. If <i>$SYSTEMD_PAGERSECURE</i> is not set at all, secure mode is enabled if the effective UID is not the same as the owner of the login session, see <code><a href="/docs/linux/man/2-geteuid/">geteuid</a></code>(2) and <code><a href="/docs/linux/man/3-sd_pid_get_owner_uid/">sd_pid_get_owner_uid</a></code>(3). In secure mode, <code>LESSSECURE=1</code> will be set when invoking the pager, and the pager shall disable commands that open or create new files or start new subprocesses. When <i>$SYSTEMD_PAGERSECURE</i> is not set at all, pagers which are not known to implement secure mode will not be used. (Currently only <code><a href="/docs/linux/man/1-less/">less</a></code>(1) implements secure mode.) </p>
<p> Note: when commands are invoked with elevated privileges, for example under <code><a href="/docs/linux/man/8-sudo/">sudo</a></code>(8) or <code><a href="/docs/linux/man/1-pkexec/">pkexec</a></code>(1), care must be taken to ensure that unintended interactive features are not enabled. &quot;Secure&quot; mode for the pager may be enabled automatically as describe above. Setting <i>SYSTEMD_PAGERSECURE=0</i> or not removing it from the inherited environment allows the user to invoke arbitrary commands. Note that if the <i>$SYSTEMD_PAGER</i> or <i>$PAGER</i> variables are to be honoured, <i>$SYSTEMD_PAGERSECURE</i> must be set too. It might be reasonable to completely disable the pager using <code>&#8211;no-pager</code> instead.</dl>
<p> <i>$SYSTEMD_COLORS</i></p>
<dl>
<dt>
<dd> Takes a boolean argument. When true, <code>systemd</code> and related utilities will use colors in their output, otherwise the output will be monochrome. Additionally, the variable can take one of the following special values: &quot;16&quot;, &quot;256&quot; to restrict the use of colors to the base 16 or 256 ANSI colors, respectively. This can be specified to override the automatic decision based on <i>$TERM</i> and what the console is connected to.</dl>
<p> <i>$SYSTEMD_URLIFY</i></p>
<dl>
<dt>
<dd> The value must be a boolean. Controls whether clickable links should be generated in the output for terminal emulators supporting this. This can be specified to override the decision that <code>systemd</code> makes based on <i>$TERM</i> and other conditions.</dl>
<h2>EXAMPLES</h2>
<p> Show current settings: </p>
<dl>
<dt>
<dd>
<pre>
$ timedatectl
               Local time: Thu 2017-09-21 16:08:56 CEST
           Universal time: Thu 2017-09-21 14:08:56 UTC
                 RTC time: Thu 2017-09-21 14:08:56
                Time zone: Europe/Warsaw (CEST, +0200)
System clock synchronized: yes
              NTP service: active
          RTC in local TZ: no
</pre>
</dl>
<p> Enable network time synchronization: </p>
<dl>
<dt>
<dd>
<pre><code>
$ timedatectl set - ntp true
==== AUTHENTICATING FOR org.freedesktop.timedate1.set-ntp ===
                    Authentication is required to control whether network time synchronization shall be enabled.Authenticating as : user
                                                                                                                                        Password : ********
==== AUTHENTICATION COMPLETE ===
</code></pre>
</dl>
<dl>
<dt>
<dd>
<pre>
$ systemctl status systemd-timesyncd.service
● systemd-timesyncd.service - Network Time Synchronization
   Loaded: loaded (/lib/systemd/system/systemd-timesyncd.service; enabled)
   Active: active (running) since Mo 2015-03-30 14:20:38 CEST; 5s ago
     Docs: <a href="//www.systutorials.com/docs/linux/man/8-man:systemd-timesyncd.service/">man:systemd-timesyncd.service</a>(8)
 Main PID: 595 (systemd-timesyn)
   Status: &quot;Using Time Server 216.239.38.15:123 (time4.google.com).&quot;
   CGroup: /system.slice/systemd-timesyncd.service
           └─595 /lib/systemd/systemd-timesyncd
...
</pre>
</dl>
<p> Show current status of <code><a href="/docs/linux/man/8-systemd-timesyncd-service/">systemd-timesyncd.service</a></code>(8): </p>
<dl>
<dt>
<dd>
<pre>
$ timedatectl timesync-status
       Server: 216.239.38.15 (time4.google.com)
Poll interval: 1min 4s (min: 32s; max 34min 8s)
         Leap: normal
      Version: 4
      Stratum: 1
    Reference: GPS
    Precision: 1us (-20)
Root distance: 335us (max: 5s)
       Offset: +316us
        Delay: 349us
       Jitter: 0
 Packet count: 1
    Frequency: -8.802ppm
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/8-hwclock/">hwclock</a></code>(8), <code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/5-localtime/">localtime</a></code>(5), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-timedated-service/">systemd-timedated.service</a></code>(8), <code><a href="/docs/linux/man/8-systemd-timesyncd-service/">systemd-timesyncd.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1) </p>
<h2>Index</h2>
