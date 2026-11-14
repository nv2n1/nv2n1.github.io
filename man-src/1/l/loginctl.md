---
title: "loginctl(1)"
name: "loginctl"
section: "1"
letter: "l"
url: "/docs/linux/man/1-loginctl/"
description: "loginctl – Control the systemd login manager"
---

<h2 class="name">NAME</h2>
<p> loginctl &#8211; Control the systemd login manager </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>loginctl</code> [OPTIONS&#8230;] {COMMAND} [NAME&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>loginctl</code></p>
<dd>may be used to introspect and control the state of the <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) login manager <code><a href="/docs/linux/man/8-systemd-logind-service/">systemd-logind.service</a></code>(8).</p>
<h2>COMMANDS</h2>
<p> The following commands are understood:</p>
<h3>Session Commands</h3>
<p> <code>list-sessions</code></p>
<dl>
<dt>
<dd> List current sessions.</dl>
<p> <code>session-status</code> [<i>ID</i>&#8230;]</p>
<dl>
<dt>
<dd> Show terse runtime status information about one or more sessions, followed by the most recent log data from the journal. Takes one or more session identifiers as parameters. If no session identifiers are passed, the status of the caller&#8217;s session is shown. This function is intended to generate human-readable output. If you are looking for computer-parsable output, use <code>show-session</code> instead.</dl>
<p> <code>show-session</code> [<i>ID</i>&#8230;]</p>
<dl>
<dt>
<dd> Show properties of one or more sessions or the manager itself. If no argument is specified, properties of the manager will be shown. If a session ID is specified, properties of the session are shown. By default, empty properties are suppressed. Use <code>&#8211;all</code> to show those too. To select specific properties to show, use <code>&#8211;property=</code>. This command is intended to be used whenever computer-parsable output is required. Use <code>session-status</code> if you are looking for formatted human-readable output.</dl>
<p> <code>activate</code> [<i>ID</i>]</p>
<dl>
<dt>
<dd> Activate a session. This brings a session into the foreground if another session is currently in the foreground on the respective seat. Takes a session identifier as argument. If no argument is specified, the session of the caller is put into foreground.</dl>
<p> <code>lock-session</code> [<i>ID</i>&#8230;], <code>unlock-session</code> [<i>ID</i>&#8230;]</p>
<dl>
<dt>
<dd> Activates/deactivates the screen lock on one or more sessions, if the session supports it. Takes one or more session identifiers as arguments. If no argument is specified, the session of the caller is locked/unlocked.</dl>
<p> <code>lock-sessions</code>, <code>unlock-sessions</code></p>
<dl>
<dt>
<dd> Activates/deactivates the screen lock on all current sessions supporting it.</dl>
<p> <code>terminate-session</code> <i>ID</i>&#8230;</p>
<dl>
<dt>
<dd> Terminates a session. This kills all processes of the session and deallocates all resources attached to the session. If the argument is specified as empty string the session invoking the command is terminated.</dl>
<p> <code>kill-session</code> <i>ID</i>&#8230;</p>
<dl>
<dt>
<dd> Send a signal to one or more processes of the session. Use <code>&#8211;kill-who=</code> to select which process to kill. Use <code>&#8211;signal=</code> to select the signal to send. If the argument is specified as empty string the signal is sent to the session invoking the command.</dl>
<h3>User Commands</h3>
<p> <code>list-users</code></p>
<dl>
<dt>
<dd> List currently logged in users.</dl>
<p> <code>user-status</code> [<i>USER</i>&#8230;]</p>
<dl>
<dt>
<dd> Show terse runtime status information about one or more logged in users, followed by the most recent log data from the journal. Takes one or more user names or numeric user IDs as parameters. If no parameters are passed, the status is shown for the user of the session of the caller. This function is intended to generate human-readable output. If you are looking for computer-parsable output, use <code>show-user</code> instead.</dl>
<p> <code>show-user</code> [<i>USER</i>&#8230;]</p>
<dl>
<dt>
<dd> Show properties of one or more users or the manager itself. If no argument is specified, properties of the manager will be shown. If a user is specified, properties of the user are shown. By default, empty properties are suppressed. Use <code>&#8211;all</code> to show those too. To select specific properties to show, use <code>&#8211;property=</code>. This command is intended to be used whenever computer-parsable output is required. Use <code>user-status</code> if you are looking for formatted human-readable output.</dl>
<p> <code>enable-linger</code> [<i>USER</i>&#8230;], <code>disable-linger</code> [<i>USER</i>&#8230;]</p>
<dl>
<dt>
<dd> Enable/disable user lingering for one or more users. If enabled for a specific user, a user manager is spawned for the user at boot and kept around after logouts. This allows users who are not logged in to run long-running services. Takes one or more user names or numeric UIDs as argument. If no argument is specified, enables/disables lingering for the user of the session of the caller. </p>
<p> See also <i>KillUserProcesses=</i> setting in <code><a href="/docs/linux/man/5-logind-conf/">logind.conf</a></code>(5).</dl>
<p> <code>terminate-user</code> <i>USER</i>&#8230;</p>
<dl>
<dt>
<dd> Terminates all sessions of a user. This kills all processes of all sessions of the user and deallocates all runtime resources attached to the user. If the argument is specified as empty string the sessions of the user invoking the command are terminated.</dl>
<p> <code>kill-user</code> <i>USER</i>&#8230;</p>
<dl>
<dt>
<dd> Send a signal to all processes of a user. Use <code>&#8211;signal=</code> to select the signal to send. If the argument is specified as empty string the signal is sent to the sessions of the user invoking the command.</dl>
<h3>Seat Commands</h3>
<p> <code>list-seats</code></p>
<dl>
<dt>
<dd> List currently available seats on the local system.</dl>
<p> <code>seat-status</code> [<i>NAME</i>&#8230;]</p>
<dl>
<dt>
<dd> Show terse runtime status information about one or more seats. Takes one or more seat names as parameters. If no seat names are passed the status of the caller&#8217;s session&#8217;s seat is shown. This function is intended to generate human-readable output. If you are looking for computer-parsable output, use <code>show-seat</code> instead.</dl>
<p> <code>show-seat</code> [<i>NAME</i>&#8230;]</p>
<dl>
<dt>
<dd> Show properties of one or more seats or the manager itself. If no argument is specified, properties of the manager will be shown. If a seat is specified, properties of the seat are shown. By default, empty properties are suppressed. Use <code>&#8211;all</code> to show those too. To select specific properties to show, use <code>&#8211;property=</code>. This command is intended to be used whenever computer-parsable output is required. Use <code>seat-status</code> if you are looking for formatted human-readable output.</dl>
<p> <code>attach</code> <i>NAME</i> <i>DEVICE</i>&#8230;</p>
<dl>
<dt>
<dd> Persistently attach one or more devices to a seat. The devices should be specified via device paths in the /sys/ file system. To create a new seat, attach at least one graphics card to a previously unused seat name. Seat names may consist only of a-z, A-Z, 0-9, &quot;-&quot; and &quot;_&quot; and must be prefixed with &quot;seat&quot;. To drop assignment of a device to a specific seat, just reassign it to a different seat, or use <code>flush-devices</code>.</dl>
<p> <code>flush-devices</code></p>
<dl>
<dt>
<dd> Removes all device assignments previously created with <code>attach</code>. After this call, only automatically generated seats will remain, and all seat hardware is assigned to them.</dl>
<p> <code>terminate-seat</code> <i>NAME</i>&#8230;</p>
<dl>
<dt>
<dd> Terminates all sessions on a seat. This kills all processes of all sessions on the seat and deallocates all runtime resources attached to them.</dl>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;no-ask-password</code></p>
<dl>
<dt>
<dd> Do not query the user for authentication for privileged operations.</dl>
<p> <code>-p</code>, <code>&#8211;property=</code></p>
<dl>
<dt>
<dd> When showing session/user/seat properties, limit display to certain properties as specified as argument. If not specified, all set properties are shown. The argument should be a property name, such as &quot;Sessions&quot;. If specified more than once, all properties with the specified names are shown.</dl>
<p> <code>&#8211;value</code></p>
<dl>
<dt>
<dd> When showing session/user/seat properties, only print the value, and skip the property name and &quot;=&quot;.</dl>
<p> <code>-a</code>, <code>&#8211;all</code></p>
<dl>
<dt>
<dd> When showing session/user/seat properties, show all properties regardless of whether they are set or not.</dl>
<p> <code>-l</code>, <code>&#8211;full</code></p>
<dl>
<dt>
<dd> Do not ellipsize process tree entries.</dl>
<p> <code>&#8211;kill-who=</code></p>
<dl>
<dt>
<dd> When used with <code>kill-session</code>, choose which processes to kill. Must be one of <code>leader</code>, or <code>all</code> to select whether to kill only the leader process of the session or all processes of the session. If omitted, defaults to <code>all</code>.</dl>
<p> <code>-s</code>, <code>&#8211;signal=</code></p>
<dl>
<dt>
<dd> When used with <code>kill-session</code> or <code>kill-user</code>, choose which signal to send to selected processes. Must be one of the well known signal specifiers, such as <code>SIGTERM</code>, <code>SIGINT</code> or <code>SIGSTOP</code>. If omitted, defaults to <code>SIGTERM</code>. </p>
<p> The special value &quot;help&quot; will list the known values and the program will exit immediately, and the special value &quot;list&quot; will list known values along with the numerical signal numbers and the program will exit immediately.</dl>
<p> <code>-n</code>, <code>&#8211;lines=</code></p>
<dl>
<dt>
<dd> When used with <code>user-status</code> and <code>session-status</code>, controls the number of journal lines to show, counting from the most recent ones. Takes a positive integer argument. Defaults to 10.</dl>
<p> <code>-o</code>, <code>&#8211;output=</code></p>
<dl>
<dt>
<dd> When used with <code>user-status</code> and <code>session-status</code>, controls the formatting of the journal entries that are shown. For the available choices, see <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1). Defaults to &quot;short&quot;.</dl>
<p> <code>-H</code>, <code>&#8211;host=</code></p>
<dl>
<dt>
<dd> Execute the operation remotely. Specify a hostname, or a username and hostname separated by &quot;@&quot;, to connect to. The hostname may optionally be suffixed by a port ssh is listening on, separated by &quot;:&quot;, and then a container name, separated by &quot;/&quot;, which connects directly to a specific container on the specified host. This will use SSH to talk to the remote machine manager instance. Container names may be enumerated with <code>machinectl -H </code><i>HOST</i>. Put IPv6 addresses in brackets.</dl>
<p> <code>-M</code>, <code>&#8211;machine=</code></p>
<dl>
<dt>
<dd> Execute operation on a local container. Specify a container name to connect to, optionally prefixed by a user name to connect as and a separating &quot;@&quot; character. If the special string &quot;.host&quot; is used in place of the container name, a connection to the local system is made (which is useful to connect to a specific user&#8217;s user bus: &quot;&#8211;user &#8211;machine=lennart [at] .host&quot;). If the &quot;@&quot; syntax is not used, the connection is made as root user. If the &quot;@&quot; syntax is used either the left hand side or the right hand side may be omitted (but not both) in which case the local user name and &quot;.host&quot; are implied.</dl>
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
<p> On success, 0 is returned, a non-zero failure code otherwise.</p>
<h2>EXAMPLES</h2>
<p> <code>Example 1. Querying user status</code> </p>
<dl>
<dt>
<dd>
<pre><code>
$ loginctl user - status fatima(1005) Since : Sat 2016 - 04 - 09 14 : 23 : 31 EDT; 54min ago
           State: active
        Sessions: 5 *3
            Unit: user-1005.slice
                  ├─user [at] 1005.service
                    ...
                  ├─session-3.scope
                    ...
                  └─session-5.scope
                    ├─3473 login -- fatima
                    └─3515 -zsh
Apr 09 14:40:30 laptop login[2325]: pam_unix(login:session):
                       session opened for user fatima by LOGIN(uid=0)
Apr 09 14:40:30 laptop login[2325]: LOGIN ON tty3 BY fatima
</code></pre>
</dl>
<p> There are two sessions, 3 and 5. Session 3 is a graphical session, marked with a star. The tree of processing including the two corresponding scope units and the user manager unit are shown.</p>
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
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/1-systemctl/">systemctl</a></code>(1), <code><a href="/docs/linux/man/8-systemd-logind-service/">systemd-logind.service</a></code>(8), <code><a href="/docs/linux/man/5-logind-conf/">logind.conf</a></code>(5) </p>
<h2>Index</h2>
