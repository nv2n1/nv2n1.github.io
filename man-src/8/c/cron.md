---
title: "cron(8)"
name: "cron"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cron/"
description: "cron – daemon to execute scheduled commands (Vixie Cron)"
---

<p>cron &#8211; daemon to execute scheduled commands (Vixie Cron)</p>
<h2>Synopsis</h2>
<p>cron [<code>-f</code>] [<code>-l</code>] [<code>-L</code> <i>loglevel</i>]</p>
<h2>Description</h2>
<p><i>cron</i> is started automatically from /etc/init.d on entering multi-user runlevels.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Stay in foreground mode, don&#8217;t daemonize.</p>
<dt><code>-P</code></p>
<dd>Don&#8217;t set PATH for child processes. Let it inherit instead.</p>
<dt><code>-l</code></p>
<dd>Enable LSB compliant names for /etc/cron.d files. This setting, however, does not affect the parsing of files under /etc/cron.hourly, /etc/cron.daily, /etc/cron.weekly or /etc/cron.monthly.</p>
<dt><code>-n</code></p>
<dd>Include the FQDN in the subject when sending mails. By default, cron will abbreviate the hostname.</p>
<dt><code>-L loglevel</code></p>
<dd>Tell cron what to log about <code>jobs</code> (errors are logged regardless of this value) as the sum of the following values: </p>
<dl>
<dd>
<dl>
<dt><code>1</code></p>
<dd>will log the start of all cron jobs</p>
<dt><code>2</code></p>
<dd>will log the end of all cron jobs</p>
<dt><code>4</code></p>
<dd>will log all failed jobs (exit status != 0)</p>
<dt><code>8</code></p>
<dd>will log the process number of all cron jobs</dl>
</dl>
<dd>The default is to log the start of all jobs (1). Logging will be disabled if <i>levels</i> is set to zero (0). A value of fifteen (15) will select all options.</dl>
<h2>Notes</h2>
<p><i>cron</i> searches its spool area (/var/spool/cron/crontabs) for crontab files (which are named after accounts in /etc/passwd); crontabs found are loaded into memory. Note that crontabs in this directory should not be accessed directly &#8211; the <i>crontab</i> command should be used to access and update them. </p>
<p> <i>cron</i> also reads /etc/crontab, which is in a slightly different format (see <i><a href="/docs/linux/man/5-crontab/">crontab</a></i>(5)). In Debian, the content of /etc/crontab is predefined to run programs under /etc/cron.hourly, /etc/cron.daily, /etc/cron.weekly and /etc/cron.monthly. This configuration is specific to Debian, see the note under <code>DEBIAN SPECIFIC</code> below. </p>
<p> Additionally, in Debian, <i>cron</i> reads the files in the /etc/cron.d directory. <i>cron</i> treats the files in /etc/cron.d as in the same way as the /etc/crontab file (they follow the special format of that file, i.e. they include the <i>user</i> field). However, they are independent of /etc/crontab: they do not, for example, inherit environment variable settings from it. This change is specific to Debian see the note under <code>DEBIAN SPECIFIC</code> below. </p>
<p> Like /etc/crontab, the files in the /etc/cron.d directory are monitored for changes. In general, the system administrator should not use /etc/cron.d/, but use the standard system crontab /etc/crontab. </p>
<p> /etc/crontab and the files in /etc/cron.d must be owned by root, and must not be group- or other-writable. In contrast to the spool area, the files under /etc/cron.d or the files under /etc/cron.hourly, /etc/cron.daily, /etc/cron.weekly and /etc/cron.monthly may also be symlinks, provided that both the symlink and the file it points to are owned by root. The files under /etc/cron.d do not need to be executable, while the files under /etc/cron.hourly, /etc/cron.daily, /etc/cron.weekly and /etc/cron.monthly do, as they are run by <i>run-parts</i> (see <i><a href="/docs/linux/man/8-run-parts/">run-parts</a></i>(8) for more information). </p>
<p> <i>cron</i> then wakes up every minute, examining all stored crontabs, checking each command to see if it should be run in the current minute. When executing commands, any output is mailed to the owner of the crontab (or to the user named in the MAILTO environment variable in the crontab, if such exists) from the owner of the crontab (or from the email address given in the MAILFROM environment variable in the crontab, if such exists). The children copies of cron running these processes have their name coerced to uppercase, as will be seen in the syslog and ps output. </p>
<p> Additionally, <i>cron</i> checks each minute to see if its spool directory&#8217;s modtime (or the modtime on the <i>/etc/crontab</i> file) has changed, and if it has, <i>cron</i> will then examine the modtime on all crontabs and reload those which have changed. Thus <i>cron</i> need not be restarted whenever a crontab file is modified. Note that the <i><a href="/docs/linux/man/1-crontab/">crontab</a></i>(1) command updates the modtime of the spool directory whenever it changes a crontab. </p>
<p> Special considerations exist when the clock is changed by less than 3 hours, for example at the beginning and end of daylight savings time. If the time has moved forwards, those jobs which would have run in the time that was skipped will be run soon after the change. Conversely, if the time has moved backwards by less than 3 hours, those jobs that fall into the repeated time will not be re-run. </p>
<p> Only jobs that run at a particular time (not specified as @hourly, nor with &#8216;*&#8217; in the hour or minute specifier) are affected. Jobs which are specified with wildcards are run based on the new time immediately. </p>
<p> Clock changes of more than 3 hours are considered to be corrections to the clock, and the new time is used immediately. </p>
<p> <i>cron</i> logs its action to the syslog facility &#8216;cron&#8217;, and logging may be controlled using the standard <i><a href="/docs/linux/man/8-syslogd/">syslogd</a></i>(8) facility.</p>
<h2>Environment</h2>
<p>If configured in <i>/etc/default/cron</i> in Debian systems, the <i>cron</i> daemon localisation settings environment can be managed through the use of <i>/etc/environment</i> or through the use of <i>/etc/default/locale</i> with values from the latter overriding values from the former. These files are read and they will be used to setup the LANG, LC_ALL, and LC_CTYPE environment variables. These variables are then used to set the charset of mails, which defaults to &#8216;C&#8217;. </p>
<p> This does <code>NOT</code> affect the environment of tasks running under cron. For more information on how to modify the environment of tasks, consult <i><a href="/docs/linux/man/5-crontab/">crontab</a></i>(5). </p>
<p> The daemon will use, if present, the definition from <i>/etc/timezone</i> for the timezone. </p>
<p> The environment can be redefined in user&#8217;s crontab definitions but <i>cron</i> will only handle tasks in a single timezone.</p>
<h2>Debian Specific</h2>
<p>Debian introduces some changes to <i>cron</i> that were not originally available upstream. The most significant changes introduced are: </p>
<dl>
<dt>&#8212;</p>
<dd>Support for /etc/cron.{hourly,daily,weekly,monthly} via /etc/crontab,</p>
<dt>&#8212;</p>
<dd>Support for /etc/cron.d (drop-in dir for package crontabs),</p>
<dt>&#8212;</p>
<dd>PAM support,</p>
<dt>&#8212;</p>
<dd>SELinux support,</p>
<dt>&#8212;</p>
<dd>auditlog support,</p>
<dt>&#8212;</p>
<dd>DST and other time-related changes/fixes,</p>
<dt>&#8212;</p>
<dd>SGID <a href="/docs/linux/man/1-crontab/">crontab</a>(1) instead of SUID root,</p>
<dt>&#8212;</p>
<dd>Debian-specific file locations and commands,</p>
<dt>&#8212;</p>
<dd>Debian-specific configuration (/etc/default/cron),</p>
<dt>&#8212;</p>
<dd>numerous other smaller features and fixes. </p>
</dl>
<p> Support for /etc/cron.hourly, /etc/cron.daily, /etc/cron.weekly and /etc/cron.monthly is provided in Debian through the default setting of the /etc/crontab file (see the system-wide example in <i><a href="/docs/linux/man/5-crontab/">crontab</a></i>(5)). The default system-wide crontab contains four tasks: run every hour, every day, every week and every month. Each of these tasks will execute <code>run-parts</code> providing each one of the directories as an argument. These tasks are disabled if <code>anacron</code> is installed (except for the hourly task) to prevent conflicts between both daemons. </p>
<p> As described above, the files under these directories have to pass some sanity checks including the following: be executable, be owned by root, not be writable by group or other and, if symlinks, point to files owned by root. Additionally, the file names must conform to the filename requirements of <code>run-parts</code>: they must be entirely made up of letters, digits and can only contain the special signs underscores (&#8216;_&#8217;) and hyphens (&#8216;-&#8216;). Any file that does not conform to these requirements will not be executed by <code>run-parts</code>. For example, any file containing dots will be ignored. This is done to prevent cron from running any of the files that are left by the Debian package management system when handling files in /etc/cron.d/ as configuration files (i.e. files ending in .dpkg-dist, .dpkg-orig, .dpkg-old, and .dpkg-new). </p>
<p> This feature can be used by system administrators and packages to include tasks that will be run at defined intervals. Files created by packages in these directories should be named after the package that supplies them. </p>
<p> Support for /etc/cron.d is included in the <i>cron</i> daemon itself, which handles this location as the system-wide crontab spool. This directory can contain any file defining tasks following the format used in /etc/crontab, i.e. unlike the user cron spool, these files must provide the username to run the task as in the task definition. </p>
<p> Files in this directory have to be owned by root, do not need to be executable (they are configuration files, just like /etc/crontab) and must conform to the same naming convention as used by <i><a href="/docs/linux/man/8-run-parts/">run-parts</a></i>(8) : they must consist solely of upper- and lower-case letters, digits, underscores, and hyphens. This means that they <code>cannot</code> contain any dots. If the <code>-l</code> option is specified to <i>cron</i> (this option can be setup through /etc/default/cron, see below), then they must conform to the LSB namespace specification, exactly as in the <code>&#8211;lsbsysinit</code> option in <i>run-parts</i>. </p>
<p> The intended purpose of this feature is to allow packages that require finer control of their scheduling than the /etc/cron.{hourly,daily,weekly,monthly} directories to add a crontab file to /etc/cron.d. Such files should be named after the package that supplies them. </p>
<p> Also, the default configuration of <i>cron</i> is controlled by <i>/etc/default/cron</i> which is read by the init.d script that launches the <i>cron</i> daemon. This file determines whether <i>cron</i> will read the system&#8217;s environment variables and makes it possible to add additional options to the <i>cron</i> program before it is executed, either to configure its logging or to define how it will treat the files under /etc/cron.d.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-crontab/">crontab</a>(1), <a href="/docs/linux/man/5-crontab/">crontab</a>(5), <a href="/docs/linux/man/8-run-parts/">run-parts</a>(8)</p>
<h2>Author</h2>
<p>Paul Vixie &lt;paul [at] vix.com&gt; is the author of <i>cron</i> and original creator of this manual page. This page has also been modified for Debian by Steve Greenland, Javier Fernandez-Sanguino and Christian Kastner.</p>
