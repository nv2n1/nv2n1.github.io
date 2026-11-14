---
title: "systemd-tmpfiles-clean-timer(8)"
name: "systemd-tmpfiles-clean-timer"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-tmpfiles-clean-timer/"
description: "systemd-tmpfiles, systemd-tmpfiles-setup.service, systemd-tmpfiles-setup-dev.service, systemd-tmpfiles-clean.service, systemd-tmpfiles-clean.timer – Creates, deletes and cleans up volatile and temp..."
---

<p>systemd-tmpfiles, systemd-tmpfiles-setup.service, systemd-tmpfiles-setup-dev.service, systemd-tmpfiles-clean.service, systemd-tmpfiles-clean.timer &#8211; Creates, deletes and cleans up volatile and temporary files and directories</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>systemd-tmpfiles</code> [OPTIONS&#8230;] [<i>CONFIGFILE</i>&#8230;]</dl>
<dd>System units: </p>
<pre>systemd-tmpfiles-setup.service
systemd-tmpfiles-setup-dev.service
systemd-tmpfiles-clean.service
systemd-tmpfiles-clean.timer</pre>
<p>User units: </p>
<pre>systemd-tmpfiles-setup.service
systemd-tmpfiles-clean.service
systemd-tmpfiles-clean.timer</pre>
<h2>Description</h2>
<p><code>systemd-tmpfiles</code> creates, deletes, and cleans up volatile and temporary files and directories, using the configuration file format and location specified in <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5). It must be invoked with one or more options <code>&#8211;create</code>, <code>&#8211;remove</code>, and <code>&#8211;clean</code>, to select the respective subset of operations. </p>
<p> By default, directives from all configuration files are applied. When invoked with <code>&#8211;replace=</code><i>PATH</i>, arguments specified on the command line are used instead of the configuration file <i>PATH</i>. Otherwise, if one or more absolute filenames are passed on the command line, only the directives in these files are applied. If &quot;-&quot; is specified instead of a filename, directives are read from standard input. If only the basename of a configuration file is specified, all configuration directories as specified in <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5) are searched for a matching file and the file found that has the highest priority is executed. </p>
<p> System services (systemd-tmpfiles-setup.service, systemd-tmpfiles-setup-dev.service, systemd-tmpfiles-clean.service) invoke <code>systemd-tmpfiles</code> to create system files and to perform system wide cleanup. Those services read administrator-controlled configuration files in tmpfiles.d/ directories. User services (systemd-tmpfiles-setup.service, systemd-tmpfiles-clean.service) also invoke <code>systemd-tmpfiles</code>, but it reads a separate set of files, which includes user-controlled files under ~/.config/user-tmpfiles.d/ and ~/.local/share/user-tmpfiles.d/, and administrator-controlled files under /usr/share/user-tmpfiles.d/. Users may use this to create and clean up files under their control, but the system instance performs global cleanup and is not influenced by user configuration. Note that this means a time-based cleanup configured in the system instance, such as the one typically configured for /tmp/, will thus also affect files created by the user instance if they are placed in /tmp/, even if the user instance&#8217;s time-based cleanup is turned off. </p>
<p> To re-apply settings after configuration has been modified, simply restart systemd-tmpfiles-clean.service, which will apply any settings which can be safely executed at runtime. To debug <code>systemd-tmpfiles</code>, it may be useful to invoke it directly from the command line with increased log level (see <i>$SYSTEMD_LOG_LEVEL</i> below).</p>
<h2>Options</h2>
<p>The following options are understood: </p>
<p> <code>&#8211;create</code></p>
<dl>
<dd>If this option is passed, all files and directories marked with <i>f</i>, <i>F</i>, <i>w</i>, <i>d</i>, <i>D</i>, <i>v</i>, <i>p</i>, <i>L</i>, <i>c</i>, <i>b</i>, <i>m</i> in the configuration files are created or written to. Files and directories marked with <i>z</i>, <i>Z</i>, <i>t</i>, <i>T</i>, <i>a</i>, and <i>A</i> have their ownership, access mode and security labels set.</dl>
<p> <code>&#8211;clean</code></p>
<dl>
<dd>If this option is passed, all files and directories with an age parameter configured will be cleaned up.</dl>
<p> <code>&#8211;remove</code></p>
<dl>
<dd>If this option is passed, the contents of directories marked with <i>D</i> or <i>R</i>, and files or directories themselves marked with <i>r</i> or <i>R</i> are removed.</dl>
<p> <code>&#8211;user</code></p>
<dl>
<dd>Execute &quot;user&quot; configuration, i.e. tmpfiles.d files in user configuration directories.</dl>
<p> <code>&#8211;boot</code></p>
<dl>
<dd>Also execute lines with an exclamation mark.</dl>
<p> <code>&#8211;prefix=</code><i>path</i></p>
<dl>
<dd>Only apply rules with paths that start with the specified prefix. This option can be specified multiple times.</dl>
<p> <code>&#8211;exclude-prefix=</code><i>path</i></p>
<dl>
<dd>Ignore rules with paths that start with the specified prefix. This option can be specified multiple times.</dl>
<p> <code>-E</code></p>
<dl>
<dd>A shortcut for &quot;&#8211;exclude-prefix=/dev &#8211;exclude-prefix=/proc &#8211;exclude-prefix=/run &#8211;exclude-prefix=/sys&quot;, i.e. exclude the hierarchies typically backed by virtual or memory file systems. This is useful in combination with <code>&#8211;root=</code>, if the specified directory tree contains an OS tree without these virtual/memory file systems mounted in, as it is typically not desirable to create any files and directories below these subdirectories if they are supposed to be overmounted during runtime.</dl>
<p> <code>&#8211;root=</code><i>root</i></p>
<dl>
<dd>Takes a directory path as an argument. All paths will be prefixed with the given alternate <i>root</i> path, including config search paths. </p>
<p> When this option is used, the libc Name Service Switch (NSS) is bypassed for resolving users and groups. Instead the files /etc/passwd and /etc/group inside the alternate root are read directly. This means that users/groups not listed in these files will not be resolved, i.e. LDAP NIS and other complex databases are not considered. </p>
<p> Consider combining this with <code>-E</code> to ensure the invocation does not create files or directories below mount points in the OS image operated on that are typically overmounted during runtime.</dl>
<p> <code>&#8211;image=</code><i>image</i></p>
<dl>
<dd>Takes a path to a disk image file or block device node. If specified all operations are applied to file system in the indicated disk image. This is similar to <code>&#8211;root=</code> but operates on file systems stored in disk images or block devices. The disk image should either contain just a file system or a set of file systems within a GPT partition table, following the m[blue]<code>Discoverable Partitions Specification</code>m[]<font SIZE="-2">[1]</font>. For further information on supported disk images, see <code><a href="/docs/linux/man/1-systemd-nspawn/">systemd-nspawn</a></code>(1)&#8217;s switch of the same name. </p>
<p> Implies <code>-E</code>.</dl>
<p> <code>&#8211;replace=</code><i>PATH</i></p>
<dl>
<dd>When this option is given, one ore more positional arguments must be specified. All configuration files found in the directories listed in <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5) will be read, and the configuration given on the command line will be handled instead of and with the same priority as the configuration file <i>PATH</i>. </p>
<p> This option is intended to be used when package installation scripts are running and files belonging to that package are not yet available on disk, so their contents must be given on the command line, but the admin configuration might already exist and should be given higher priority.</dl>
<p> <code>&#8211;cat-config</code></p>
<dl>
<dd>Copy the contents of config files to standard output. Before each file, the filename is printed as a comment.</dl>
<p> <code>&#8211;no-pager</code></p>
<dl>
<dd>Do not pipe output into a pager.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<p> It is possible to combine <code>&#8211;create</code>, <code>&#8211;clean</code>, and <code>&#8211;remove</code> in one invocation (in which case removal and cleanup are executed before creation of new files). For example, during boot the following command line is executed to ensure that all temporary and volatile directories are removed and created according to the configuration file: </p>
<dl>
<dd>
<pre>systemd-tmpfiles --remove --create</pre>
</dl>
<h2>Environment</h2>
<p><i>$SYSTEMD_LOG_LEVEL</i></p>
<dl>
<dd>The maximum log level of emitted messages (messages with a higher log level, i.e. less important ones, will be suppressed). Either one of (in order of decreasing importance) <code>emerg</code>, <code>alert</code>, <code>crit</code>, <code>err</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, <code>debug</code>, or an integer in the range 0&#8230;7. See <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) for more information.</dl>
<p> <i>$SYSTEMD_LOG_COLOR</i></p>
<dl>
<dd>A boolean. If true, messages written to the tty will be colored according to priority. </p>
<p> This setting is only useful when messages are written directly to the terminal, because <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) and other tools that display logs will color messages based on the log level on their own.</dl>
<p> <i>$SYSTEMD_LOG_TIME</i></p>
<dl>
<dd>A boolean. If true, console log messages will be prefixed with a timestamp. </p>
<p> This setting is only useful when messages are written directly to the terminal or a file, because <code><a href="/docs/linux/man/1-journalctl/">journalctl</a></code>(1) and other tools that display logs will attach timestamps based on the entry metadata on their own.</dl>
<p> <i>$SYSTEMD_LOG_LOCATION</i></p>
<dl>
<dd>A boolean. If true, messages will be prefixed with a filename and line number in the source code where the message originates. </p>
<p> Note that the log location is often attached as metadata to journal entries anyway. Including it directly in the message text can nevertheless be convenient when debugging programs.</dl>
<p> <i>$SYSTEMD_LOG_TARGET</i></p>
<dl>
<dd>The destination for log messages. One of <code>console</code> (log to the attached tty), <code>console-prefixed</code> (log to the attached tty but with prefixes encoding the log level and &quot;facility&quot;, see <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3), <code>kmsg</code> (log to the kernel circular log buffer), <code>journal</code> (log to the journal), <code>journal-or-kmsg</code> (log to the journal if available, and to kmsg otherwise), <code>auto</code> (determine the appropriate log target automatically, the default), <code>null</code> (disable log output).</dl>
<p> <i>$SYSTEMD_PAGER</i></p>
<dl>
<dd>Pager to use when <code>&#8211;no-pager</code> is not given; overrides <i>$PAGER</i>. If neither <i>$SYSTEMD_PAGER</i> nor <i>$PAGER</i> are set, a set of well-known pager implementations are tried in turn, including <code><a href="/docs/linux/man/1-less/">less</a></code>(1) and <code><a href="/docs/linux/man/1-more/">more</a></code>(1), until one is found. If no pager implementation is discovered no pager is invoked. Setting this environment variable to an empty string or the value &quot;cat&quot; is equivalent to passing <code>&#8211;no-pager</code>.</dl>
<p> <i>$SYSTEMD_LESS</i></p>
<dl>
<dd>Override the options passed to <code>less</code> (by default &quot;FRSXMK&quot;). </p>
<p> Users might want to change two options in particular: </p>
<p> <code>K</code></p>
<dl>
<dd>This option instructs the pager to exit immediately when Ctrl+C is pressed. To allow <code>less</code> to handle Ctrl+C itself to switch back to the pager command prompt, unset this option. </p>
<p> If the value of <i>$SYSTEMD_LESS</i> does not include &quot;K&quot;, and the pager that is invoked is <code>less</code>, Ctrl+C will be ignored by the executable, and needs to be handled by the pager.</dl>
<p> <code>X</code></p>
<dl>
<dd>This option instructs the pager to not send termcap initialization and deinitialization strings to the terminal. It is set by default to allow command output to remain visible in the terminal even after the pager exits. Nevertheless, this prevents some pager functionality from working, in particular paged output cannot be scrolled with the mouse.</dl>
<p> See <code><a href="/docs/linux/man/1-less/">less</a></code>(1) for more discussion.</dl>
<p> <i>$SYSTEMD_LESSCHARSET</i></p>
<dl>
<dd>Override the charset passed to <code>less</code> (by default &quot;utf-8&quot;, if the invoking terminal is determined to be UTF-8 compatible).</dl>
<p> <i>$SYSTEMD_PAGERSECURE</i></p>
<dl>
<dd>Takes a boolean argument. When true, the &quot;secure&quot; mode of the pager is enabled; if false, disabled. If <i>$SYSTEMD_PAGERSECURE</i> is not set at all, secure mode is enabled if the effective UID is not the same as the owner of the login session, see <code><a href="/docs/linux/man/2-geteuid/">geteuid</a></code>(2) and <code><a href="/docs/linux/man/3-sd_pid_get_owner_uid/">sd_pid_get_owner_uid</a></code>(3). In secure mode, <code>LESSSECURE=1</code> will be set when invoking the pager, and the pager shall disable commands that open or create new files or start new subprocesses. When <i>$SYSTEMD_PAGERSECURE</i> is not set at all, pagers which are not known to implement secure mode will not be used. (Currently only <code><a href="/docs/linux/man/1-less/">less</a></code>(1) implements secure mode.) </p>
<p> Note: when commands are invoked with elevated privileges, for example under <code><a href="/docs/linux/man/8-sudo/">sudo</a></code>(8) or <code><a href="/docs/linux/man/1-pkexec/">pkexec</a></code>(1), care must be taken to ensure that unintended interactive features are not enabled. &quot;Secure&quot; mode for the pager may be enabled automatically as describe above. Setting <i>SYSTEMD_PAGERSECURE=0</i> or not removing it from the inherited environment allows the user to invoke arbitrary commands. Note that if the <i>$SYSTEMD_PAGER</i> or <i>$PAGER</i> variables are to be honoured, <i>$SYSTEMD_PAGERSECURE</i> must be set too. It might be reasonable to completely disable the pager using <code>&#8211;no-pager</code> instead.</dl>
<p> <i>$SYSTEMD_COLORS</i></p>
<dl>
<dd>Takes a boolean argument. When true, <code>systemd</code> and related utilities will use colors in their output, otherwise the output will be monochrome. Additionally, the variable can take one of the following special values: &quot;16&quot;, &quot;256&quot; to restrict the use of colors to the base 16 or 256 ANSI colors, respectively. This can be specified to override the automatic decision based on <i>$TERM</i> and what the console is connected to.</dl>
<p> <i>$SYSTEMD_URLIFY</i></p>
<dl>
<dd>The value must be a boolean. Controls whether clickable links should be generated in the output for terminal emulators supporting this. This can be specified to override the decision that <code>systemd</code> makes based on <i>$TERM</i> and other conditions.</dl>
<h2>Unprivileged &#8211;Cleanup Operation</h2>
<p><code>systemd-tmpfiles</code> tries to avoid changing the access and modification times on the directories it accesses, which requires <code>CAP_FOWNER</code> privileges. When running as non-root, directories which are checked for files to clean up will have their access time bumped, which might prevent their cleanup.</p>
<h2>Exit Status</h2>
<p>On success, 0 is returned. If the configuration was syntactically invalid (syntax errors, missing arguments, &#8230;), so some lines had to be ignored, but no other errors occurred, <code>65</code> is returned (<code>EX_DATAERR</code> from /usr/include/sysexits.h). If the configuration was syntactically valid, but could not be executed (lack of permissions, creation of files in missing directories, invalid contents when writing to /sys/ values, &#8230;), <code>73</code> is returned (<code>EX_CANTCREAT</code> from /usr/include/sysexits.h). Otherwise, <code>1</code> is returned (<code>EXIT_FAILURE</code> from /usr/include/stdlib.h). </p>
<p> Note: when creating items, if the target already exists, but is of the wrong type or otherwise does not match the requested state, and forced operation has not been requested with &quot;+&quot;, a message is emitted, but the failure is otherwise ignored.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-tmpfiles-d/">tmpfiles.d</a></code>(5)</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>Discoverable Partitions Specification</p>
<dl>
<dd><a rel="nofollow" href="https://systemd.io/DISCOVERABLE_PARTITIONS">https://systemd.io/DISCOVERABLE_PARTITIONS</a></dl>
