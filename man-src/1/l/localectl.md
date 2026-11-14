---
title: "localectl(1)"
name: "localectl"
section: "1"
letter: "l"
url: "/docs/linux/man/1-localectl/"
description: "localectl – Control the system locale and keyboard layout settings"
---

<h2 class="name">NAME</h2>
<p> localectl &#8211; Control the system locale and keyboard layout settings </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>localectl</code> [OPTIONS&#8230;] {COMMAND}</dl>
<h2>DESCRIPTION</h2>
<p> <code>localectl</code></p>
<dd>may be used to query and change the system locale and keyboard layout settings. It communicates with <code><a href="/docs/linux/man/8-systemd-localed/">systemd-localed</a></code>(8) to modify files such as /etc/locale.conf and /etc/vconsole.conf. </p>
<p> The system locale controls the language settings of system services and of the UI before the user logs in, such as the display manager, as well as the default for users after login. </p>
<p> The keyboard settings control the keyboard layout used on the text console and of the graphical UI before the user logs in, such as the display manager, as well as the default for users after login. </p>
<p> Note that the changes performed using this tool might require the initramfs to be rebuilt to take effect during early system boot. The initramfs is not rebuilt automatically by localectl. </p>
<p> Note that <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1) may be used to initialize the system locale for mounted (but not booted) system images.</p>
<h2>COMMANDS</h2>
<p> The following commands are understood: </p>
<p> <code>status</code></p>
<dl>
<dt>
<dd> Show current settings of the system locale and keyboard mapping. If no command is specified, this is the implied default.</dl>
<p> <code>set-locale LOCALE</code>, <code>set-locale VARIABLE=LOCALE&#8230;</code></p>
<dl>
<dt>
<dd> Set the system locale. This takes one locale such as &quot;en_US.UTF-8&quot;, or takes one or more locale assignments such as &quot;LANG=de_DE.utf8&quot;, &quot;LC_MESSAGES=en_GB.utf8&quot;, and so on. If one locale without variable name is provided, then &quot;LANG=&quot; locale variable will be set. See <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7) for details on the available settings and their meanings. Use <code>list-locales</code> for a list of available locales (see below).</dl>
<p> <code>list-locales</code></p>
<dl>
<dt>
<dd> List available locales useful for configuration with <code>set-locale</code>.</dl>
<p> <code>set-keymap MAP [TOGGLEMAP]</code></p>
<dl>
<dt>
<dd> Set the system keyboard mapping for the console and X11. This takes a mapping name (such as &quot;de&quot; or &quot;us&quot;), and possibly a second one to define a toggle keyboard mapping. Unless <code>&#8211;no-convert</code> is passed, the selected setting is also applied as the default system keyboard mapping of X11, after converting it to the closest matching X11 keyboard mapping. Use <code>list-keymaps</code> for a list of available keyboard mappings (see below).</dl>
<p> <code>list-keymaps</code></p>
<dl>
<dt>
<dd> List available keyboard mappings for the console, useful for configuration with <code>set-keymap</code>.</dl>
<p> <code>set-x11-keymap LAYOUT [MODEL [VARIANT [OPTIONS]]]</code></p>
<dl>
<dt>
<dd> Set the system default keyboard mapping for X11 and the virtual console. This takes a keyboard mapping name (such as &quot;de&quot; or &quot;us&quot;), and possibly a model, variant, and options, see <code><a href="/docs/linux/man/4-kbd/">kbd</a></code>(4) for details. Unless <code>&#8211;no-convert</code> is passed, the selected setting is also applied as the system console keyboard mapping, after converting it to the closest matching console keyboard mapping.</dl>
<p> <code>list-x11-keymap-models</code>, <code>list-x11-keymap-layouts</code>, <code>list-x11-keymap-variants [LAYOUT]</code>, <code>list-x11-keymap-options</code></p>
<dl>
<dt>
<dd> List available X11 keymap models, layouts, variants and options, useful for configuration with <code>set-keymap</code>. The command <code>list-x11-keymap-variants</code> optionally takes a layout parameter to limit the output to the variants suitable for the specific layout.</dl>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;no-ask-password</code></p>
<dl>
<dt>
<dd> Do not query the user for authentication for privileged operations.</dl>
<p> <code>&#8211;no-convert</code></p>
<dl>
<dt>
<dd> If <code>set-keymap</code> or <code>set-x11-keymap</code> is invoked and this option is passed, then the keymap will not be converted from the console to X11, or X11 to console, respectively.</dl>
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
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/7-locale/">locale</a></code>(7), <code><a href="/docs/linux/man/5-locale-conf/">locale.conf</a></code>(5), <code><a href="/docs/linux/man/5-vconsole-conf/">vconsole.conf</a></code>(5), <code><a href="/docs/linux/man/1-loadkeys/">loadkeys</a></code>(1), <code><a href="/docs/linux/man/4-kbd/">kbd</a></code>(4), m[blue]<code>The XKB Configuration Guide</code>m[]<font SIZE="-2">[1]</font>, <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-localed-service/">systemd-localed.service</a></code>(8), <code><a href="/docs/linux/man/1-systemd-firstboot/">systemd-firstboot</a></code>(1), <code><a href="/docs/linux/man/8-mkinitrd/">mkinitrd</a></code>(8)</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> The XKB Configuration Guide</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.x.org/releases/current/doc/xorg-docs/input/XKB-Config.html">http://www.x.org/releases/current/doc/xorg-docs/input/XKB-Config.html</a></dl>
</dl>
<h2>Index</h2>
