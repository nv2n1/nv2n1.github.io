---
title: "logrotate(5)"
name: "logrotate"
section: "5"
letter: "l"
url: "/docs/linux/man/5-logrotate/"
description: "logrotate – rotates, compresses, and mails system logs"
---

<p>logrotate &#8211; rotates, compresses, and mails system logs</p>
<h2>Synopsis</h2>
<p><code>logrotate</code> [<code>-dv</code>] [<code>-f</code>|<code>&#8211;force</code>] [<code>-s</code>|<code>&#8211;state </code><i>file</i>] <i>config_file</i> ..</p>
<h2>Description</h2>
<p><code>logrotate</code> is designed to ease administration of systems that generate large numbers of log files. It allows automatic rotation, compression, removal, and mailing of log files. Each log file may be handled daily, weekly, monthly, or when it grows too large. Normally, <code>logrotate</code> is run as a daily cron job. It will not modify a log multiple times in one day unless the criterion for that log is based on the log&#8217;s size and <code>logrotate</code> is being run multiple times each day, or unless the <code>-f</code> or <code>&#8211;force</code> option is used. Any number of config files may be given on the command line. Later config files may override the options given in earlier files, so the order in which the <code>logrotate</code> config files are listed is important. Normally, a single config file which includes any other config files which are needed should be used. See below for more information on how to use the <code>include</code> directive to accomplish this. If a directory is given on the command line, every file in that directory is used as a config file. If no command line arguments are given, <code>logrotate</code> will print version and copyright information, along with a short usage summary. If any errors occur while rotating logs, <code>logrotate</code> will exit with non-zero status. </p>
<h2>Options</h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>Prints help message. </p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>Turns on debug mode and implies <code>-v</code>. In debug mode, no changes will be made to the logs or to the <code>logrotate</code> state file. </p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd>Tells <code>logrotate</code> to force the rotation, even if it doesn&#8217;t think this is necessary. Sometimes this is useful after adding new entries to a <code>logrotate</code> config file, or if old log files have been removed by hand, as the new files will be created, and logging will continue correctly. </p>
<dt><code>-m</code>, <code>&#8211;mail &lt;command&gt;</code></p>
<dd>Tells <code>logrotate</code> which command to use when mailing logs. This command should accept two arguments: 1) the subject of the message, and 2) the recipient. The command must then read a message on standard input and mail it to the recipient. The default mail command is <code>/bin/mail -s</code>. </p>
<dt><code>-s</code>, <code>&#8211;state &lt;statefile&gt;</code></p>
<dd>Tells <code>logrotate</code> to use an alternate state file. This is useful if logrotate is being run as a different user for various sets of log files. The default state file is <i>/var/lib/logrotate.status</i>. </p>
<dt><code>&#8211;usage</code></p>
<dd>Prints a short usage message. </p>
<dt>+<code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Turns on verbose mode. </p>
</dl>
<h2>Configuration File</h2>
<p><code>logrotate</code> reads everything about the log files it should be handling from the series of configuration files specified on the command line. Each configuration file can set global options (local definitions override global ones, and later definitions override earlier ones) and specify logfiles to rotate. A simple configuration file looks like this: </p>
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
 mail www [at] my.org
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
 postrotate
 kill -HUP `cat /var/run/inn.pid`
 endscript
 nocompress
}
~/log/*.log {}</pre>
<p>The first few lines set global options; in the example, logs are compressed after they are rotated. Note that comments may appear anywhere in the config file as long as the first non-whitespace character on the line is a #. </p>
<p> The next section of the config files defined how to handle the log file <i>/var/log/messages</i>. The log will go through five weekly rotations before being removed. After the log file has been rotated (but before the old version of the log has been compressed), the command <i>/sbin/killall -HUP syslogd</i> will be executed. </p>
<p> The next section defines the parameters for both <i>/var/log/httpd/access.log</i> and <i>/var/log/httpd/error.log</i>. They are rotated whenever it grows over 100k in size, and the old logs files are mailed (uncompressed) to www [at] my.org after going through 5 rotations, rather than being removed. The <code>sharedscripts</code> means that the <code>postrotate</code> script will only be run once (after the old logs have been compressed), not once for each log which is rotated. Note that the double quotes around the first filename at the beginning of this section allows logrotate to rotate logs with spaces in the name. Normal shell quoting rules apply, with &#8216;, &quot;, and \ characters supported. </p>
<p> The next section defines the parameters for all of the files in <i>/var/log/news</i>. Each file is rotated on a monthly basis. This is considered a single rotation directive and if errors occur for more than one file, the log files are not compressed. </p>
<p> The last section uses tilde expansion to rotate log files in the home directory of the current user. This is only available, if your glob library supports tilde expansion. GNU glob does support this. </p>
<p> Please use wildcards with caution. If you specify *, <code>logrotate</code> will rotate all files, including previously rotated ones. A way around this is to use the <code>olddir</code> directive or a more exact wildcard (such as *.log). </p>
<p> Here is more information on the directives which may be included in a <code>logrotate</code> configuration file: </p>
<dl>
<dt><code>compress</code></p>
<dd>Old versions of log files are compressed with <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) by default. See also <code>nocompress</code>. </p>
<dt><code>compresscmd</code></p>
<dd>Specifies which command to use to compress log files. The default is <code>gzip</code>. See also <code>compress</code>. </p>
<dt><code>uncompresscmd</code></p>
<dd>Specifies which command to use to uncompress log files. The default is <code>gunzip</code>. </p>
<dt><code>compressext</code></p>
<dd>Specifies which extension to use on compressed logfiles, if compression is enabled. The default follows that of the configured compression command. </p>
<dt><code>compressoptions</code></p>
<dd>Command line options may be passed to the compression program, if one is in use. The default, for <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), is &quot;-6&quot; (biased towards high compression at the expense of speed). If you use a different compression command, you may need to change the <code>compressoptions</code> to match. </p>
<dt><code>copy</code></p>
<dd>Make a copy of the log file, but don&#8217;t change the original at all. This option can be used, for instance, to make a snapshot of the current log file, or when some other utility needs to truncate or parse the file. When this option is used, the <code>create</code> option will have no effect, as the old log file stays in place. </p>
<dt><code>copytruncate</code></p>
<dd>Truncate the original log file in place after creating a copy, instead of moving the old log file and optionally creating a new one. It can be used when some program cannot be told to close its logfile and thus might continue writing (appending) to the previous log file forever. Note that there is a very small time slice between copying the file and truncating it, so some logging data might be lost. When this option is used, the <code>create</code> option will have no effect, as the old log file stays in place. </p>
<dt><code>create </code><i>mode</i> <i>owner</i> <i>group</i>, <code>create </code><i>owner</i> <i>group</i></p>
<dd>Immediately after rotation (before the <code>postrotate</code> script is run) the log file is created (with the same name as the log file just rotated). <i>mode</i> specifies the mode for the log file in octal (the same as <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2)), <i>owner</i> specifies the user name who will own the log file, and <i>group</i> specifies the group the log file will belong to. Any of the log file attributes may be omitted, in which case those attributes for the new file will use the same values as the original log file for the omitted attributes. This option can be disabled using the <code>nocreate</code> option. </p>
<dt><code>daily</code></p>
<dd>Log files are rotated every day. </p>
<dt><code>dateext</code></p>
<dd>Archive old versions of log files adding a date extension like YYYYMMDD instead of simply adding a number. The extension may be configured using the <code>dateformat</code> and <code>dateyesterday</code> options. </p>
<dt><code>dateformat</code> <i>format_string</i></p>
<dd>Specify the extension for <code>dateext</code> using the notation similar to <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3) function. Only %Y %m %d and %s specifiers are allowed. The default value is -%Y%m%d. Note that also the character separating log name from the extension is part of the dateformat string. The system clock must be set past Sep 9th 2001 for %s to work correctly. Note that the datestamps generated by this format must be lexically sortable (i.e., first the year, then the month then the day. e.g., 2001/12/01 is ok, but 01/12/2001 is not, since 01/11/2002 would sort lower while it is later). This is because when using the <code>rotate</code> option, logrotate sorts all rotated filenames to find out which logfiles are older and should be removed. </p>
<dt><code>dateyesterday</code></p>
<dd>Use yesterday&#8217;s instead of today&#8217;s date to create the <code>dateext</code> extension, so that the rotated log file has a date in its name that is the same as the timestamps within it. </p>
<dt><code>delaycompress</code></p>
<dd>Postpone compression of the previous log file to the next rotation cycle. This only has effect when used in combination with <code>compress</code>. It can be used when some program cannot be told to close its logfile and thus might continue writing to the previous log file for some time. </p>
<dt><code>extension </code><i>ext</i></p>
<dd>Log files with <i>ext</i> extension can keep it after the rotation. If compression is used, the compression extension (normally <code>.gz</code>) appears after <i>ext</i>. For example you have a logfile named mylog.foo and want to rotate it to mylog.1.foo.gz instead of mylog.foo.1.gz. </p>
<dt><code>hourly</code></p>
<dd>Log files are rotated every hour. Note that usually <i>logrotate</i> is configured to be run by cron daily. You have to change this configuration and run <i>logrotate</i> hourly to be able to really rotate logs hourly. </p>
<dt><code>ifempty</code></p>
<dd>Rotate the log file even if it is empty, overriding the <code>notifempty</code> option (<code>ifempty</code> is the default). </p>
<dt><code>include </code><i>file_or_directory</i></p>
<dd>Reads the file given as an argument as if it was included inline where the <code>include</code> directive appears. If a directory is given, most of the files in that directory are read in alphabetic order before processing of the including file continues. The only files which are ignored are files which are not regular files (such as directories and named pipes) and files whose names end with one of the taboo extensions, as specified by the <code>tabooext</code> directive. </p>
<dt><code>mail </code><i>address</i></p>
<dd>When a log is rotated out-of-existence, it is mailed to <i>address</i>. If no mail should be generated by a particular log, the <code>nomail</code> directive may be used. </p>
<dt><code>mailfirst</code></p>
<dd>When using the <code>mail</code> command, mail the just-rotated file, instead of the about-to-expire file. </p>
<dt><code>maillast</code></p>
<dd>When using the <code>mail</code> command, mail the about-to-expire file, instead of the just-rotated file (this is the default). </p>
<dt><code>maxage</code> <i>count</i></p>
<dd>Remove rotated logs older than &lt;count&gt; days. The age is only checked if the logfile is to be rotated. The files are mailed to the configured address if <code>maillast</code> and <code>mail</code> are configured. </p>
<dt><code>maxsize</code> <i>size</i></p>
<dd>Log files are rotated when they grow bigger than <i>size</i> bytes even before the additionally specified time interval (<code>daily</code>, <code>weekly</code>, <code>monthly</code>, or <code>yearly</code>). The related <code>size</code> option is similar except that it is mutually exclusive with the time interval options, and it causes log files to be rotated without regard for the last rotation time. When <code>maxsize</code> is used, both the size and timestamp of a log file are considered. </p>
<dt><code>minsize</code> <i>size</i></p>
<dd>Log files are rotated when they grow bigger than <i>size</i> bytes, but not before the additionally specified time interval (<code>daily</code>, <code>weekly</code>, <code>monthly</code>, or <code>yearly</code>). The related <code>size</code> option is similar except that it is mutually exclusive with the time interval options, and it causes log files to be rotated without regard for the last rotation time. When <code>minsize</code> is used, both the size and timestamp of a log file are considered. </p>
<dt><code>missingok</code></p>
<dd>If the log file is missing, go on to the next one without issuing an error message. See also <code>nomissingok</code>. </p>
<dt><code>monthly</code></p>
<dd>Log files are rotated the first time <code>logrotate</code> is run in a month (this is normally on the first day of the month). </p>
<dt><code>nocompress</code></p>
<dd>Old versions of log files are not compressed. See also <code>compress</code>. </p>
<dt><code>nocopy</code></p>
<dd>Do not copy the original log file and leave it in place. (this overrides the <code>copy</code> option). </p>
<dt><code>nocopytruncate</code></p>
<dd>Do not truncate the original log file in place after creating a copy (this overrides the <code>copytruncate</code> option). </p>
<dt><code>nocreate</code></p>
<dd>New log files are not created (this overrides the <code>create</code> option). </p>
<dt><code>nodelaycompress</code></p>
<dd>Do not postpone compression of the previous log file to the next rotation cycle (this overrides the <code>delaycompress</code> option). </p>
<dt><code>nodateext</code></p>
<dd>Do not archive old versions of log files with date extension (this overrides the <code>dateext</code> option). </p>
<dt><code>nomail</code></p>
<dd>Don&#8217;t mail old log files to any address. </p>
<dt><code>nomissingok</code></p>
<dd>If a log file does not exist, issue an error. This is the default. </p>
<dt><code>noolddir</code></p>
<dd>Logs are rotated in the same directory the log normally resides in (this overrides the <code>olddir</code> option). </p>
<dt><code>nosharedscripts</code></p>
<dd>Run <code>prerotate</code> and <code>postrotate</code> scripts for every log file which is rotated (this is the default, and overrides the <code>sharedscripts</code> option). The absolute path to the log file is passed as first argument to the script. If the scripts exit with error, the remaining actions will not be executed for the affected log only. </p>
<dt><code>noshred</code></p>
<dd>Do not use <code>shred</code> when deleting old log files. See also <code>shred</code>. </p>
<dt><code>notifempty</code></p>
<dd>Do not rotate the log if it is empty (this overrides the <code>ifempty</code> option). </p>
<dt><code>olddir </code><i>directory</i></p>
<dd>Logs are moved into <i>directory</i> for rotation. The <i>directory</i> must be on the same physical device as the log file being rotated, and is assumed to be relative to the directory holding the log file unless an absolute path name is specified. When this option is used all old versions of the log end up in <i>directory</i>. This option may be overridden by the <code>noolddir</code> option. </p>
<dt><code>postrotate</code>/<code>endscript</code></p>
<dd>The lines between <code>postrotate</code> and <code>endscript</code> (both of which must appear on lines by themselves) are executed (using <code>/bin/sh</code>) after the log file is rotated. These directives may only appear inside a log file definition. Normally, the absolute path to the log file is passed as first argument to the script. If <code>sharedscripts</code> is specified, whole pattern is passed to the script. See also <code>prerotate</code>. See <code>sharedscripts</code> and <code>nosharedscripts</code> for error handling. </p>
<dt><code>prerotate</code>/<code>endscript</code></p>
<dd>The lines between <code>prerotate</code> and <code>endscript</code> (both of which must appear on lines by themselves) are executed (using <code>/bin/sh</code>) before the log file is rotated and only if the log will actually be rotated. These directives may only appear inside a log file definition. Normally, the absolute path to the log file is passed as first argument to the script. If <code>sharedscripts</code> is specified, whole pattern is passed to the script. See also <code>postrotate</code>. See <code>sharedscripts</code> and <code>nosharedscripts</code> for error handling. </p>
<dt><code>firstaction</code>/<code>endscript</code></p>
<dd>The lines between <code>firstaction</code> and <code>endscript</code> (both of which must appear on lines by themselves) are executed (using <code>/bin/sh</code>) once before all log files that match the wildcarded pattern are rotated, before prerotate script is run and only if at least one log will actually be rotated. These directives may only appear inside a log file definition. Whole pattern is passed to the script as first argument. If the script exits with error, no further processing is done. See also <code>lastaction</code>. </p>
<dt><code>lastaction</code>/<code>endscript</code></p>
<dd>The lines between <code>lastaction</code> and <code>endscript</code> (both of which must appear on lines by themselves) are executed (using <code>/bin/sh</code>) once after all log files that match the wildcarded pattern are rotated, after postrotate script is run and only if at least one log is rotated. These directives may only appear inside a log file definition. Whole pattern is passed to the script as first argument. If the script exits with error, just an error message is shown (as this is the last action). See also <code>firstaction</code>. </p>
<dt><code>preremove</code>/<code>endscript</code></p>
<dd>The lines between <code>preremove</code> and <code>endscript</code> (both of which must appear on lines by themselves) are executed (using <code>/bin/sh</code>) once just before removal of a log file. The logrotate will pass the name of file which is soon to be removed. See also <code>firstaction</code>. </p>
<dt><code>rotate </code><i>count</i></p>
<dd>Log files are rotated <i>count</i> times before being removed or mailed to the address specified in a <code>mail</code> directive. If <i>count</i> is 0, old versions are removed rather than rotated. </p>
<dt><code>size </code><i>size</i></p>
<dd>Log files are rotated only if they grow bigger then <i>size</i> bytes. If <i>size</i> is followed by <i>k</i>, the size is assumed to be in kilobytes. If the <i>M</i> is used, the size is in megabytes, and if <i>G</i> is used, the size is in gigabytes. So <i>size 100</i>, <i>size 100k</i>, <i>size 100M</i> and <i>size 100G</i> are all valid. </p>
<dt><code>sharedscripts</code></p>
<dd>Normally, <code>prerotate</code> and <code>postrotate</code> scripts are run for each log which is rotated and the absolute path to the log file is passed as first argument to the script. That means a single script may be run multiple times for log file entries which match multiple files (such as the <i>/var/log/news/*</i> example). If <code>sharedscripts</code> is specified, the scripts are only run once, no matter how many logs match the wildcarded pattern, and whole pattern is passed to them. However, if none of the logs in the pattern require rotating, the scripts will not be run at all. If the scripts exit with error, the remaining actions will not be executed for any logs. This option overrides the <code>nosharedscripts</code> option and implies <code>create</code> option. </p>
<dt><code>shred</code></p>
<dd>Delete log files using <code>shred</code> -u instead of unlink(). This should ensure that logs are not readable after their scheduled deletion; this is off by default. See also <code>noshred</code>. </p>
<dt><code>shredcycles</code> <i>count</i></p>
<dd>Asks GNU <code><a href="/docs/linux/man/1-shred/">shred</a></code>(1) to overwrite log files <code>count</code> times before deletion. Without this option, <code>shred</code>&#8216;s default will be used. </p>
<dt><code>start </code><i>count</i></p>
<dd>This is the number to use as the base for rotation. For example, if you specify 0, the logs will be created with a .0 extension as they are rotated from the original log files. If you specify 9, log files will be created with a .9, skipping 0-8. Files will still be rotated the number of times specified with the <code>rotate</code> directive. </p>
<dt><code>su </code><i>user</i> <i>group</i></p>
<dd>Rotate log files set under this user and group instead of using default user/group (usually root). <i>user</i> specifies the user name used for rotation and <i>group</i> specifies the group used for rotation. </p>
<dt><code>tabooext</code> [+] <i>list</i></p>
<dd>The current taboo extension list is changed (see the <code>include</code> directive for information on the taboo extensions). If a + precedes the list of extensions, the current taboo extension list is augmented, otherwise it is replaced. At startup, the taboo extension list contains .rpmsave, .rpmorig, ~, .disabled, .dpkg-old, .dpkg-dist, .dpkg-new, .cfsaved, .ucf-old, .ucf-dist, .ucf-new, .rpmnew, .swp, .cfsaved, .rhn-cfg-tmp-* </p>
<dt><code>weekly</code></p>
<dd>Log files are rotated if the current weekday is less than the weekday of the last rotation or if more than a week has passed since the last rotation. This is normally the same as rotating logs on the first day of the week, but it works better if <i>logrotate</i> is not run every night. </p>
<dt><code>yearly</code></p>
<dd>Log files are rotated if the current year is not the same as the last rotation. </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/var/lib/logrotate.status</i></p>
<dd>Default state file.</p>
<dt><i>/etc/logrotate.conf</i></p>
<dd>Configuration options. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1) &lt;<a rel="nofollow" href="http://fedorahosted.org/logrotate/">http://fedorahosted.org/logrotate/</a>&gt; </p>
<h2>Authors</h2>
<pre>Erik Troan, Preston Brown, Jan Kaluza.
&lt;logrotate-owner [at] fedoraproject.org&gt;</pre>
