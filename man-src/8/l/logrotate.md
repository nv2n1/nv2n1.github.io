---
title: "logrotate(8)"
name: "logrotate"
section: "8"
letter: "l"
url: "/docs/linux/man/8-logrotate/"
description: "logrotate – rotates, compresses, and mails system logs"
---

<p>logrotate &#8211; rotates, compresses, and mails system logs</p>
<h2>Synopsis</h2>
<p><code>logrotate</code> [<code>&#8211;force</code>] [<code>&#8211;debug</code>] [<code>&#8211;state</code> <i>file</i>] [<code>&#8211;skip-state-lock</code>] [<code>&#8211;verbose</code>] [<code>&#8211;log</code> <i>file</i>] [<code>&#8211;mail</code> <i>command</i>] <i>config_file</i> [<i>config_file2 &#8230;</i>] </p>
<h2>Description</h2>
<p><code>logrotate</code> is designed to ease administration of systems that generate large numbers of log files. It allows automatic rotation, compression, removal, and mailing of log files. Each log file may be handled daily, weekly, monthly, or when it grows too large. Normally, <code>logrotate</code> is run as a daily cron job. It will not modify a log more than once in one day unless the criterion for that log is based on the log&#8217;s size and <code>logrotate</code> is being run more than once each day, or unless the <code>-f</code> or <code>&#8211;force</code> option is used. Any number of config files may be given on the command line. Later config files may override the options given in earlier files, so the order in which the <code>logrotate</code> config files are listed is important. Normally, a single config file which includes any other config files which are needed should be used. See below for more information on how to use the <code>include</code> directive to accomplish this. If a directory is given on the command line, every file in that directory is used as a config file. If no command line arguments are given, <code>logrotate</code> will print version and copyright information, along with a short usage summary. If any errors occur while rotating logs, <code>logrotate</code> will exit with non-zero status, although the state file will be updated. </p>
<h2>Options</h2>
<dl>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>Tells <code>logrotate</code> to force the rotation, even if it doesn&#8217;t think this is necessary. Sometimes this is useful after adding new entries to a <code>logrotate</code> config file, or if old log files have been removed by hand, as the new files will be created, and logging will continue correctly. </p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>Turn on debug mode, which means that no changes are made to the logs and the <code>logrotate</code> state file is not updated. Only debug messages are printed. </p>
<dt><code>-s</code>, <code>&#8211;state</code> <i>statefile</i></p>
<dd>Tells <code>logrotate</code> to use an alternate state file. This is useful if <code>logrotate</code> is being run as a different user for various sets of log files. To prevent parallel execution <code>logrotate</code> by default acquires a lock on the state file, if it cannot be acquired <code>logrotate</code> will exit with value 3. The default state file is <i>/var/lib/logrotate/status</i>. If <i>/dev/null</i> is given as the state file, then <code>logrotate</code> will not try to write the state file. </p>
<dt><code>&#8211;skip-state-lock</code></p>
<dd>Do not lock the state file, for example if locking is unsupported or prohibited. </p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Turns on verbose mode, for example to display messages during rotation. </p>
<dt><code>-l</code>, <code>&#8211;log</code> <i>file</i></p>
<dd>Tells <code>logrotate</code> to log verbose output into the log_file. The verbose output logged to that file is the same as when running <code>logrotate</code> with <code>-v</code> switch. The log file is overwritten on every <code>logrotate</code> execution. </p>
<dt><code>-m</code>, <code>&#8211;mail</code> <i>command</i></p>
<dd>Tells <code>logrotate</code> which command to use when mailing logs. This command should accept the following arguments:</p>
<dd>1) the subject of the message given with &#8216;-s subject&#8217;<br />
 2) the recipient.</p>
<dd>The command must then read a message on standard input and mail it to the recipient. The default mail command is <i>/usr/bin/mail</i>. </p>
<dt><code>&#8211;usage</code></p>
<dd>Prints a short usage message. </p>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>Prints help message. </p>
<dt><code>&#8211;version</code></p>
<dd>Display version information. </p>
</dl>
<h2>Configuration File</h2>
<p><code>logrotate</code> reads everything about the log files it should be handling from the series of configuration files specified on the command line. Each configuration file can set global options (local definitions override global ones, and later definitions override earlier ones) and specify logfiles to rotate. Global options do not affect preceding include directives. A simple configuration file looks like this: </p>
<pre># sample logrotate configuration file
compress
/var/log/messages {
 rotate 5
 weekly
 postrotate
 /usr/bin/killall -HUP syslogd
 endscript
}
&quot;/var/log/httpd/access.log&quot; /var/log/httpd/error.log {
 rotate 5
 mail recipient [at] example.org
 size 100k
 sharedscripts
 postrotate
 /usr/bin/killall -HUP httpd
 endscript
}
/var/log/news/* {
 monthly
 rotate 2
 olddir /var/log/news/old
 missingok
 sharedscripts
 postrotate
 kill -HUP $(cat /var/run/inn.pid)
 endscript
 nocompress
}
~/log/*.log {}</pre>
<p>The first few lines set global options; in the example, logs are compressed after they are rotated. Note that comments may appear anywhere in the config file as long as the first non-whitespace character on the line is a <code>#</code>. </p>
<p> Values are separated from directives by whitespace and/or an optional =. Numbers must be specified in a format understood by <code><a href="/docs/linux/man/3-strtoul/">strtoul</a></code>(3). </p>
<p> The next section of the config file defines how to handle the log file <i>/var/log/messages</i>. The log will go through five weekly rotations before being removed. After the log file has been rotated (but before the old version of the log has been compressed), the command <i>/usr/bin/killall -HUP syslogd</i> will be executed. </p>
<p> The next section defines the parameters for both <i>/var/log/httpd/access.log</i> and <i>/var/log/httpd/error.log</i>. Each is rotated whenever it grows over 100 kilobytes in size, and the old logs files are mailed (uncompressed) to recipient [at] example.org after going through 5 rotations, rather than being removed. The <code>sharedscripts</code> means that the <code>postrotate</code> script will only be run once (after the old logs have been compressed), not once for each log which is rotated. Note that log file names may be enclosed in quotes (and that quotes are required if the name contains spaces). Normal shell quoting rules apply, with <code>&#8216;</code>, <code>&quot;</code>, and <code>\</code> characters supported. </p>
<p> The next section defines the parameters for all of the files in <i>/var/log/news</i>. Each file is rotated on a monthly basis. </p>
<p> The last section uses tilde expansion to rotate log files in the home directory of the current user. This is only available, if your glob library supports tilde expansion. GNU glob does support this. </p>
<p> Please use wildcards with caution. If you specify *, <code>logrotate</code> will rotate all files, including previously rotated ones. A way around this is to use the <code>olddir</code> directive or a more exact wildcard (such as *.log). </p>
<p> Please note, by default when using <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), the option <i>ProtectSystem=full</i> is set in the <i>logrotate.service</i> file. This prevents <code>logrotate</code> from modifying logs in <i>/etc</i> and <i>/usr</i>. </p>
<p> Here is more information on the directives which may be included in a <code>logrotate</code> configuration file:</p>
<h2>Configuration File Directives</h2>
<p>These directives may be included in a <code>logrotate</code> configuration file:</p>
<h3>Rotation</h3>
<dl>
<dt><code>rotate </code><i>count</i></p>
<dd>Log files are rotated <i>count</i> times before being removed or mailed to the address specified in a <code>mail</code> directive. If <i>count</i> is 0, old versions are removed rather than rotated. If <i>count</i> is -1, old logs are not removed at all, except they are affected by <code>maxage</code> (use with caution, may waste performance and disk space). Default is 0. </p>
<dt><code>olddir </code><i>directory</i></p>
<dd>Logs are moved into <i>directory</i> for rotation. The <i>directory</i> must be on the same physical device as the log file being rotated, unless <code>copy</code>, <code>copytruncate</code> or <code>renamecopy</code> option is used. The <i>directory</i> is assumed to be relative to the directory holding the log file unless an absolute path name is specified. When this option is used all old versions of the log end up in <i>directory</i>. This option may be overridden by the <code>noolddir</code> option. </p>
<dt><code>noolddir</code></p>
<dd>Logs are rotated in the directory they normally reside in (this overrides the <code>olddir</code> option). </p>
<dt><code>su </code><i>user</i> <i>group</i></p>
<dd>Rotate log files set under this user and group instead of using default user/group (usually root). <i>user</i> specifies the user used for rotation and <i>group</i> specifies the group used for rotation (see the section <code>USER AND GROUP</code> for details). If the user/group you specify here does not have sufficient privilege to make files with the ownership you&#8217;ve specified in a <code>create</code> directive, it will cause an error. If <code>logrotate</code> runs with root privileges, it is recommended to use the <code>su</code> directive to rotate files in directories that are directly or indirectly in control of non-privileged users. </p>
</dl>
<h3>Frequency</h3>
<dl>
<dt><code>hourly</code></p>
<dd>Log files are rotated every hour. Note that usually <code>logrotate</code> is configured to be run by cron daily (or by <i>logrotate.timer</i> when using <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1)). You have to change this configuration and run <code>logrotate</code> hourly to be able to really rotate logs hourly. </p>
<dt><code>daily</code></p>
<dd>Log files are rotated every day. </p>
<dt><code>weekly</code> [<i>weekday</i>]</p>
<dd>Log files are rotated once each <i>weekday</i>, or if the date is advanced by at least 7 days since the last rotation (while ignoring the exact time). The <i>weekday</i> interpretation is following: 0 means Sunday, 1 means Monday, &#8230;, 6 means Saturday; the special value 7 means each 7 days, irrespectively of weekday. Defaults to 0 if the <i>weekday</i> argument is omitted. </p>
<dt><code>monthly</code></p>
<dd>Log files are rotated the first time <code>logrotate</code> is run in a month (this is normally on the first day of the month). </p>
<dt><code>yearly</code></p>
<dd>Log files are rotated if the current year is not the same as the last rotation. </p>
<dt><code>size </code><i>size</i></p>
<dd>Log files are rotated only if they grow bigger than <i>size</i> bytes. If <i>size</i> is followed by <i>k</i>, the size is assumed to be in kilobytes. If <i>M</i> is used, the size is in megabytes, and if <i>G</i> is used, the size is in gigabytes. So <i>size 100</i>, <i>size 100k</i>, <i>size 100M</i> and <i>size 100G</i> are all valid. This option is mutually exclusive with the time interval options, and it causes log files to be rotated without regard for the last rotation time, if specified after the time criteria (the last specified option takes the precedence). </p>
</dl>
<h3>File selection</h3>
<dl>
<dt><code>missingok</code></p>
<dd>If the log file is missing, go on to the next one without issuing an error message. See also <code>nomissingok</code>. </p>
<dt><code>nomissingok</code></p>
<dd>If a log file does not exist, issue an error. This is the default. </p>
<dt><code>ifempty</code></p>
<dd>Rotate the log file even if it is empty, overriding the <code>notifempty</code> option (<code>ifempty</code> is the default). </p>
<dt><code>notifempty</code></p>
<dd>Do not rotate the log if it is empty (this overrides the <code>ifempty</code> option). </p>
<dt><code>minage</code> <i>count</i></p>
<dd>Do not rotate logs which are less than &lt;count&gt; days old. </p>
<dt><code>maxage</code> <i>count</i></p>
<dd>Remove rotated logs older than &lt;count&gt; days. The age is only checked if the logfile is to be rotated. <code>rotate -1</code> does not hinder removal. The files are mailed to the configured address if <code>maillast</code> and <code>mail</code> are configured. </p>
<dt><code>minsize</code> <i>size</i></p>
<dd>Log files are rotated when they grow bigger than <i>size</i> bytes, but not before the additionally specified time interval (<code>daily</code>, <code>weekly</code>, <code>monthly</code>, or <code>yearly</code>). The related <code>size</code> option is similar except that it is mutually exclusive with the time interval options, and it causes log files to be rotated without regard for the last rotation time, if specified after the time criteria (the last specified option takes the precedence). When <code>minsize</code> is used, both the size and timestamp of a log file are considered. </p>
<dt><code>maxsize</code> <i>size</i></p>
<dd>Log files are rotated when they grow bigger than <i>size</i> bytes even before the additionally specified time interval (<code>daily</code>, <code>weekly</code>, <code>monthly</code>, or <code>yearly</code>). The related <code>size</code> option is similar except that it is mutually exclusive with the time interval options, and it causes log files to be rotated without regard for the last rotation time, if specified after the time criteria (the last specified option takes the precedence). When <code>maxsize</code> is used, both the size and timestamp of a log file are considered. </p>
<dt><code>tabooext</code> [+] <i>list</i></p>
<dd>The current taboo extension list is changed (see the <code>include</code> directive for information on the taboo extensions). If a + precedes the list of extensions, the current taboo extension list is augmented, otherwise it is replaced. At startup, the taboo extension list <i>,v</i>, <i>.cfsaved</i>, <i>.disabled</i>, <i>.dpkg-bak</i>, <i>.dpkg-del</i>, <i>.dpkg-dist</i>, <i>.dpkg-new</i>, <i>.dpkg-old</i>, <i>.rhn-cfg-tmp-*</i>, <i>.rpmnew</i>, <i>.rpmorig</i>, <i>.rpmsave</i>, <i>.swp</i>, <i>.ucf-dist</i>, <i>.ucf-new</i>, <i>.ucf-old</i>, <i>~</i> </p>
<dt><code>taboopat</code> [+] <i>list</i></p>
<dd>The current taboo glob pattern list is changed (see the <code>include</code> directive for information on the taboo extensions and patterns). If a + precedes the list of patterns, the current taboo pattern list is augmented, otherwise it is replaced. At startup, the taboo pattern list is empty. </p>
</dl>
<h3>Files and Folders</h3>
<dl>
<dt><code>create </code><i>mode</i> <i>owner</i> <i>group</i>, <code>create </code><i>owner</i> <i>group</i></p>
<dd>Immediately after rotation (before the <code>postrotate</code> script is run) the log file is created (with the same name as the log file just rotated). <i>mode</i> specifies the mode for the log file in octal (the same as <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2)), <i>owner</i> specifies the user who will own the log file, and <i>group</i> specifies the group the log file will belong to (see the section <code>USER AND GROUP</code> for details). Any of the log file attributes may be omitted, in which case those attributes for the new file will use the same values as the original log file for the omitted attributes. This option can be disabled using the <code>nocreate</code> option. </p>
<dt><code>nocreate</code></p>
<dd>New log files are not created (this overrides the <code>create</code> option). </p>
<dt><code>createolddir </code><i>mode</i> <i>owner</i> <i>group</i></p>
<dd>If the directory specified by <code>olddir</code> directive does not exist, it is created. <i>mode</i> specifies the mode for the <code>olddir</code> directory in octal (the same as <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2)), <i>owner</i> specifies the user who will own the <code>olddir</code> directory, and <i>group</i> specifies the group the <code>olddir</code> directory will belong to (see the section <code>USER AND GROUP </code> for details). This option can be disabled using the <code>nocreateolddir</code> option. </p>
<dt><code>nocreateolddir</code></p>
<dd><code>olddir</code> directory is not created by <code>logrotate</code> when it does not exist. </p>
<dt><code>copy</code></p>
<dd>Make a copy of the log file, but don&#8217;t change the original at all. This option can be used, for instance, to make a snapshot of the current log file, or when some other utility needs to truncate or parse the file. When this option is used, the <code>create</code> option will have no effect, as the old log file stays in place. The <code>copy</code> option allows storing rotated log files on the different devices using <code>olddir</code> directive. </p>
<dt><code>nocopy</code></p>
<dd>Do not copy the original log file and leave it in place. (this overrides the <code>copy</code> option). </p>
<dt><code>copytruncate</code></p>
<dd>Truncate the original log file to zero size in place after creating a copy, instead of moving the old log file and optionally creating a new one. It can be used when some program cannot be told to close its logfile and thus might continue writing (appending) to the previous log file forever. Note that there is a very small time slice between copying the file and truncating it, so some logging data might be lost. When this option is used, the <code>create</code> option will have no effect, as the old log file stays in place. The <code>copytruncate</code> option allows storing rotated log files on the different devices using <code>olddir</code> directive. The <code>copytruncate</code> option implies <code>norenamecopy</code>. </p>
<dt><code>nocopytruncate</code></p>
<dd>Do not truncate the original log file in place after creating a copy (this overrides the <code>copytruncate</code> option). </p>
<dt><code>renamecopy</code></p>
<dd>Log file is renamed to temporary filename in the same directory by adding &quot;.tmp&quot; extension to it. After that, <code>postrotate</code> script is run and log file is copied from temporary filename to final filename. In the end, temporary filename is removed. The <code>renamecopy</code> option allows storing rotated log files on the different devices using <code>olddir</code> directive. The <code>renamecopy</code> option implies <code>nocopytruncate</code>. </p>
<dt><code>norenamecopy</code></p>
<dd>Do not rename and copy the original log file (this overrides the <code>renamecopy</code> option). </p>
<dt><code>shred</code></p>
<dd>Delete log files using <code>shred</code> -u instead of unlink(). This should ensure that logs are not readable after their scheduled deletion; this is off by default. See also <code>noshred</code>. </p>
<dt><code>noshred</code></p>
<dd>Do not use <code>shred</code> when deleting old log files. See also <code>shred</code>. </p>
<dt><code>shredcycles</code> <i>count</i></p>
<dd>Asks GNU <code><a href="/docs/linux/man/1-shred/">shred</a></code>(1) to overwrite log files <code>count</code> times before deletion. Without this option, <code>shred</code>&#8216;s default will be used. </p>
<dt><code>allowhardlink</code></p>
<dd>Rotate files with multiple hard links; this is off by default. The target file might get emptied, e.g. with <code>shred</code> or <code>copytruncate</code>. Use with caution, especially when the log files are rotated as root. </p>
<dt><code>noallowhardlink</code></p>
<dd>Do not rotate files with multiple hard links. See also <code>allowhardlink</code>. </p>
</dl>
<h3>Compression</h3>
<dl>
<dt><code>compress</code></p>
<dd>Old versions of log files are compressed with <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) by default. See also <code>nocompress</code>. </p>
<dt><code>nocompress</code></p>
<dd>Old versions of log files are not compressed. See also <code>compress</code>. </p>
<dt><code>compresscmd</code></p>
<dd>Specifies which command to use to compress log files. The default is <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1). See also <code>compress</code>. </p>
<dt><code>uncompresscmd</code></p>
<dd>Specifies which command to use to uncompress log files. The default is <code><a href="/docs/linux/man/1-gunzip/">gunzip</a></code>(1). </p>
<dt><code>compressext</code></p>
<dd>Specifies which extension to use on compressed logfiles, if compression is enabled. The default follows that of the configured compression command. </p>
<dt><code>compressoptions</code></p>
<dd>Command line options may be passed to the compression program, if one is in use. The default, for <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), is &quot;-6&quot; (biased towards high compression at the expense of speed). If you use a different compression command, you may need to change the <code>compressoptions</code> to match. </p>
<dt><code>delaycompress</code></p>
<dd>Postpone compression of the previous log file to the next rotation cycle. This only has effect when used in combination with <code>compress</code>. It can be used when some program cannot be told to close its logfile and thus might continue writing to the previous log file for some time. </p>
<dt><code>nodelaycompress</code></p>
<dd>Do not postpone compression of the previous log file to the next rotation cycle (this overrides the <code>delaycompress</code> option). </p>
</dl>
<h3>Filenames</h3>
<dl>
<dt><code>extension </code><i>ext</i></p>
<dd>Log files with <i>ext</i> extension can keep it after the rotation. If compression is used, the compression extension (normally <i>.gz</i>) appears after <i>ext</i>. For example you have a logfile named mylog.foo and want to rotate it to mylog.1.foo.gz instead of mylog.foo.1.gz. </p>
<dt><code>addextension </code><i>ext</i></p>
<dd>Log files are given the final extension <i>ext</i> after rotation. If the original file already ends with <i>ext</i>, the extension is not duplicated, but merely moved to the end, that is both <code>filename</code> and <code>filename</code><i>ext</i> would get rotated to filename.1<i>ext</i>. If compression is used, the compression extension (normally <code>.gz</code>) appears after <i>ext</i>. </p>
<dt><code>start </code><i>count</i></p>
<dd>This is the number to use as the base for rotation. For example, if you specify 0, the logs will be created with a .0 extension as they are rotated from the original log files. If you specify 9, log files will be created with a .9, skipping 0-8. Files will still be rotated the number of times specified with the <code>rotate</code> directive. </p>
<dt><code>dateext</code></p>
<dd>Archive old versions of log files adding a date extension like YYYYMMDD instead of simply adding a number. The extension may be configured using the <code>dateformat</code> and <code>dateyesterday</code> options. </p>
<dt><code>nodateext</code></p>
<dd>Do not archive old versions of log files with date extension (this overrides the <code>dateext</code> option). </p>
<dt><code>dateformat</code> <i>format_string</i></p>
<dd>Specify the extension for <code>dateext</code> using the notation similar to <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) function. Only %Y %m %d %H %M %S %V and %s specifiers are allowed. The default value is -%Y%m%d except hourly, which uses -%Y%m%d%H as default value. Note that also the character separating log name from the extension is part of the dateformat string. The system clock must be set past Sep 9th 2001 for %s to work correctly. Note that the datestamps generated by this format must be lexically sortable (that is first the year, then the month then the day. For example 2001/12/01 is ok, but 01/12/2001 is not, since 01/11/2002 would sort lower while it is later). This is because when using the <code>rotate</code> option, <code>logrotate</code> sorts all rotated filenames to find out which logfiles are older and should be removed. </p>
<dt><code>dateyesterday</code></p>
<dd>Use yesterday&#8217;s instead of today&#8217;s date to create the <code>dateext</code> extension, so that the rotated log file has a date in its name that is the same as the timestamps within it. </p>
<dt><code>datehourago</code></p>
<dd>Use hour ago instead of current date to create the <code>dateext</code> extension, so that the rotated log file has a hour in its name that is the same as the timestamps within it. Useful with rotate <code>hourly</code>. </p>
</dl>
<h3>Mail</h3>
<dl>
<dt><code>mail </code><i>address</i></p>
<dd>When a log is rotated out of existence, it is mailed to <i>address</i>. If no mail should be generated by a particular log, the <code>nomail</code> directive may be used. </p>
<dt><code>nomail</code></p>
<dd>Do not mail old log files to any address. </p>
<dt><code>mailfirst</code></p>
<dd>When using the <code>mail</code> command, mail the just-rotated file, instead of the about-to-expire file. </p>
<dt><code>maillast</code></p>
<dd>When using the <code>mail</code> command, mail the about-to-expire file, instead of the just-rotated file (this is the default). </p>
</dl>
<h3>Additional config files</h3>
<dl>
<dt><code>include </code><i>file_or_directory</i></p>
<dd>Reads the file given as an argument as if it was included inline where the <code>include</code> directive appears. If a directory is given, most of the files in that directory are read in alphabetic order before processing of the including file continues. The only files which are ignored are files which are not regular files (such as directories and named pipes) and files whose names end with one of the taboo extensions or patterns, as specified by the <code>tabooext</code> or <code>taboopat</code> directives, respectively. The given path may start with <code>~/</code> to make it relative to the home directory of the executing user. For security reasons configuration files must not be group-writable nor world-writable. </p>
</dl>
<h3>Scripts</h3>
<dl>
<dt><code>sharedscripts</code></p>
<dd>Normally, <code>prerotate</code> and <code>postrotate</code> scripts are run for each log which is rotated and the absolute path to the log file is passed as first argument to the script. That means a single script may be run multiple times for log file entries which match multiple files (such as the <i>/var/log/news/*</i> example). If <code>sharedscripts</code> is specified, the scripts are only run once, no matter how many logs match the wildcarded pattern, and whole pattern is passed to them. However, if none of the logs in the pattern require rotating, the scripts will not be run at all. If the scripts exit with error (or any log fails to rotate), the remaining actions will not be executed for any logs. This option overrides the <code>nosharedscripts</code> option. </p>
<dt><code>nosharedscripts</code></p>
<dd>Run <code>prerotate</code> and <code>postrotate</code> scripts for every log file which is rotated (this is the default, and overrides the <code>sharedscripts</code> option). The absolute path to the log file is passed as first argument to the script. The absolute path to the final rotated log file is passed as the second argument to the <code>postrotate</code> script. If the scripts exit with error, the remaining actions will not be executed for the affected log only. </p>
<dt> <code>firstaction</code></p>
<dd>
<dt> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>script</i></p>
<dd>
<dt> <code>endscript</code></p>
<dd>The <i>script</i> is executed once before all log files that match the wildcarded pattern are rotated, before the prerotate script is run and only if at least one log will actually be rotated. These directives may only appear inside a log file definition. The whole pattern is passed to the script as its first argument. If the script exits with an error, no further processing is done. See also <code>lastaction</code> and the <code>SCRIPTS</code> section. </p>
<dt> <code>lastaction</code></p>
<dd>
<dt> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>script</i></p>
<dd>
<dt> <code>endscript</code></p>
<dd>The <i>script</i> is executed once after all log files that match the wildcarded pattern are rotated, after the postrotate script is run and only if at least one log is rotated. These directives may only appear inside a log file definition. The whole pattern is passed to the script as its first argument. If the script exits with an error, just an error message is shown (as this is the last action). See also <code>firstaction</code> and the <code>SCRIPTS</code> section. </p>
<dt> <code>prerotate</code></p>
<dd>
<dt> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>script</i></p>
<dd>
<dt> <code>endscript</code></p>
<dd>The <i>script</i> is executed before the log file is rotated and only if the log will actually be rotated. These directives may only appear inside a log file definition. Normally, the absolute path to the log file is passed as the first argument to the script. If <code>sharedscripts</code> is specified, the whole pattern is passed to the script. See also <code>postrotate</code> and the <code>SCRIPTS</code> section. See <code>sharedscripts</code> and <code>nosharedscripts</code> for error handling. </p>
<dt> <code>postrotate</code></p>
<dd>
<dt> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>script</i></p>
<dd>
<dt> <code>endscript</code></p>
<dd>The <i>script</i> is executed after the log file is rotated. These directives may only appear inside a log file definition. Normally, the absolute path to the log file is passed as the first argument to the script and the absolute path to the final rotated log file is passed as the second argument to the script. If <code>sharedscripts</code> is specified, the whole pattern is passed as the first argument to the script, and the second argument is omitted. See also <code>prerotate</code> and the <code>SCRIPTS</code> section. See <code>sharedscripts</code> and <code>nosharedscripts</code> for error handling. </p>
<dt> <code>preremove</code></p>
<dd>
<dt> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>script</i></p>
<dd>
<dt> <code>endscript</code></p>
<dd>The <i>script</i> is executed once just before removal of a log file. <code>logrotate</code> will pass the name of file which is soon to be removed as the first argument to the script. See also <code>firstaction</code> and the <code>SCRIPTS</code> section. </p>
</dl>
<h2>Scripts</h2>
<p>The lines between the starting keyword (e.g. <code>prerotate</code>) and <code>endscript</code> (both of which must appear on lines by themselves) are executed (using <code>/bin/sh</code>). The script inherits some traits from the <code>logrotate</code> process, including stderr, stdout, the current directory, the environment, and the umask. Scripts are run as the invoking user and group, irrespective of any <code>su</code> directive. If the <code>&#8211;log</code> flag was specified, file descriptor 3 is the log file. The current working directory is unspecified.</p>
<h2>User And Group</h2>
<p>User and group identifiers are resolved first by trying the textual representation and, in case it fails, afterwards by the numeric value.</p>
<h2>Files</h2>
<table>
<tr VALIGN=top>
<td><i>/var/lib/logrotate/status</i></td>
<td>Default state file.</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><i>/etc/logrotate.conf</i></td>
<td>Configuration options.</td>
<td>
</td>
</tr>
</table>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/1-gunzip/">gunzip</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-mail/">mail</a></code>(1), <code><a href="/docs/linux/man/1-shred/">shred</a></code>(1), <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3), <code><a href="/docs/linux/man/3-strtoul/">strtoul</a></code>(3), &lt;<a rel="nofollow" href="https://github.com/logrotate/logrotate">https://github.com/logrotate/logrotate</a>&gt; </p>
<h2>Authors</h2>
<pre>Erik Troan, Preston Brown, Jan Kaluza.
&lt;<a rel="nofollow" href="https://github.com/logrotate/logrotate">https://github.com/logrotate/logrotate</a>&gt;</pre>
