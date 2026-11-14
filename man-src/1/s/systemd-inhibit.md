---
title: "systemd-inhibit(1)"
name: "systemd-inhibit"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-inhibit/"
description: "systemd-inhibit – Execute a program with an inhibition lock taken"
---

<h2 class="name">NAME</h2>
<p> systemd-inhibit &#8211; Execute a program with an inhibition lock taken </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-inhibit </code><code>[OPTIONS&#8230;]</code><code>[COMMAND]</code><code>[ARGUMENTS&#8230;]</code></p>
<dt> <code>systemd-inhibit </code><code>[OPTIONS&#8230;]</code><code> &#8211;list</code></dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-inhibit</code></p>
<dd>may be used to execute a program with a shutdown, sleep, or idle inhibitor lock taken. The lock will be acquired before the specified command line is executed and released afterwards. </p>
<p> Inhibitor locks may be used to block or delay system sleep and shutdown requests from the user, as well as automatic idle handling of the OS. This is useful to avoid system suspends while an optical disc is being recorded, or similar operations that should not be interrupted. </p>
<p> For more information see the m[blue]<code>Inhibitor Lock Developer Documentation</code>m[]<font SIZE="-2">[1]</font>.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;what=</code></p>
<dl>
<dt>
<dd> Takes a colon-separated list of one or more operations to inhibit: &quot;shutdown&quot;, &quot;sleep&quot;, &quot;idle&quot;, &quot;handle-power-key&quot;, &quot;handle-suspend-key&quot;, &quot;handle-hibernate-key&quot;, &quot;handle-lid-switch&quot;, for inhibiting reboot/power-off/halt/kexec, suspending/hibernating, the automatic idle detection, or the low-level handling of the power/sleep key and the lid switch, respectively. If omitted, defaults to &quot;idle:sleep:shutdown&quot;.</dl>
<p> <code>&#8211;who=</code></p>
<dl>
<dt>
<dd> Takes a short, human-readable descriptive string for the program taking the lock. If not passed, defaults to the command line string.</dl>
<p> <code>&#8211;why=</code></p>
<dl>
<dt>
<dd> Takes a short, human-readable descriptive string for the reason for taking the lock. Defaults to &quot;Unknown reason&quot;.</dl>
<p> <code>&#8211;mode=</code></p>
<dl>
<dt>
<dd> Takes either &quot;block&quot; or &quot;delay&quot; and describes how the lock is applied. If &quot;block&quot; is used (the default), the lock prohibits any of the requested operations without time limit, and only privileged users may override it. If &quot;delay&quot; is used, the lock can only delay the requested operations for a limited time. If the time elapses, the lock is ignored and the operation executed. The time limit may be specified in <code><a href="/docs/linux/man/5-logind-conf/">logind.conf</a></code>(5). Note that &quot;delay&quot; is only available for &quot;sleep&quot; and &quot;shutdown&quot;.</dl>
<p> <code>&#8211;list</code></p>
<dl>
<dt>
<dd> Lists all active inhibition locks instead of acquiring one.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dt>
<dd> Do not pipe output into a pager.</dl>
<p> <code>&#8211;no-legend</code></p>
<dl>
<dt>
<dd> Do not print the legend, i.e. column headers and the footer with hints.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>EXIT STATUS</h2>
<p> Returns the exit status of the executed program.</p>
<h2>EXAMPLE</h2>
<dl>
<dt>
<dd>
<pre>
# systemd-inhibit wodim foobar.iso
</pre>
</dl>
<p> This burns the ISO image foobar.iso on a CD using <code><a href="/docs/linux/man/1-wodim/">wodim</a></code>(1), and inhibits system sleeping, shutdown and idle while doing so.</p>
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
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-logind-conf/">logind.conf</a></code>(5)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Inhibitor Lock Developer Documentation</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://www.freedesktop.org/wiki/Software/systemd/inhibit">https://www.freedesktop.org/wiki/Software/systemd/inhibit</a></dl>
</dl>
<h2>Index</h2>
