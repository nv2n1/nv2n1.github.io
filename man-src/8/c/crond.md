---
title: "crond(8)"
name: "crond"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crond/"
description: "crond – daemon to execute scheduled commands"
---

<p>crond &#8211; daemon to execute scheduled commands</p>
<h2>Synopsis</h2>
<p><code>crond</code> [<code>-c</code> | <code>-h</code> | <code>-i</code> | <code>-n</code> | <code>-p</code> | <code>-P</code> | <code>-s</code> | <code>-m</code><i>&lt;mail</i><code>command&gt;</code>]<br />
 <code>crond</code> <code>-x</code> [ext,sch,proc,pars,load,misc,test,bit]</p>
<h2>Description</h2>
<p><i>Cron</i> is started from <i>/etc/rc.d/init.d</i> or <i>/etc/init.d</i> when classical sysvinit scripts are used. In case systemd is enabled, then unit file is installed into <i>/lib/systemd/system/crond.service</i> and daemon is started by <i>systemctl start crond.service</i> command. It returns immediately, thus, there is no need to need to start it with the &#8216;&amp;&#8217; parameter. </p>
<p> <i>Cron</i> searches <i>/var/spool/cron</i> for crontab files which are named after accounts in <i>/etc/passwd;</i> The found crontabs are loaded into the memory. <i>Cron</i> also searches for <i>/etc/anacrontab</i> and any files in the <i>/etc/cron.d</i> directory, which have a different format (see <code><a href="/docs/linux/man/5-crontab/">crontab</a></code>(5)). <i>Cron</i> examines all stored crontabs and checks each job to see if it needs to be run in the current minute. When executing commands, any output is mailed to the owner of the crontab (or to the user specified in the <i>MAILTO</i> environment variable in the crontab, if such exists). Any job output can also be sent to syslog by using the <code>-s</code> option. </p>
<p> There are two ways how changes in crontables are checked. The first method is checking the modtime of a file. The second method is using the inotify support. Using of inotify is logged in the <i>/var/log/cron</i> log after the daemon is started. The inotify support checks for changes in all crontables and accesses the hard disk only when a change is detected. </p>
<p> When using the modtime option, <i>Cron</i> checks its crontables&#8217; modtimes every minute to check for any changes and reloads the crontables which have changed. There is no need to restart <i>Cron</i> after some of the crontables were modified. The modtime option is also used when inotify can not be initialized. </p>
<p> <i>Cron</i> checks these files and directories:</p>
<dl>
<dt><i>/etc/crontab</i></p>
<dd>system crontab. Nowadays the file is empty by default. Originally it was usually used to run daily, weekly, monthly jobs. By default these jobs are now run through anacron which reads <i>/etc/anacrontab</i> configuration file. See <code><a href="/docs/linux/man/5-anacrontab/">anacrontab</a></code>(5) for more details.</p>
<dt><i>/etc/cron.d/</i></p>
<dd>directory that contains system cronjobs stored for different users.</p>
<dt><i>/var/spool/cron</i></p>
<dd>directory that contains user crontables created by the <i>crontab</i> command.</dl>
<p> Note that the <code><a href="/docs/linux/man/1-crontab/">crontab</a></code>(1) command updates the modtime of the spool directory whenever it changes a crontab.</p>
<h3>Daylight Saving Time and other time changes</h3>
<p>Local time changes of less than three hours, such as those caused by the Daylight Saving Time changes, are handled in a special way. This only applies to jobs that run at a specific time and jobs that run with a granularity greater than one hour. Jobs that run more frequently are scheduled normally. </p>
<p> If time was adjusted one hour forward, those jobs that would have run in the interval that has been skipped will be run immediately. Conversely, if time was adjusted backward, running the same job twice is avoided. </p>
<p> Time changes of more than 3 hours are considered to be corrections to the clock or the timezone, and the new time is used immediately. </p>
<p> It is possible to use different time zones for crontables. See <code><a href="/docs/linux/man/5-crontab/">crontab</a></code>(5) for more information.</p>
<h3>PAM Access Control</h3>
<p><i>Cron</i> supports access control with PAM if the system has PAM installed. For more information, see <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8). A PAM configuration file for <i>crond</i> is installed in <i>/etc/pam.d/crond</i>. The daemon loads the PAM environment from the pam_env module. This can be overridden by defining specific settings in the appropriate crontab file.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code></p>
<dd>Prints a help message and exits.</p>
<dt><code>-i</code></p>
<dd>Disables inotify support.</p>
<dt><code>-m</code></p>
<dd>This option allows you to specify a shell command to use for sending <i>Cron</i> mail output instead of using <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8) This command must accept a fully formatted mail message (with headers) on standard input and send it as a mail message to the recipients specified in the mail headers. Specifying the string <i>off</i> (i.e., crond -m off) will disable the sending of mail.</p>
<dt><code>-n</code></p>
<dd>Tells the daemon to run in the foreground. This can be useful when starting it out of init. With this option is needed to change pam setting. <i>/etc/pam.d/crond</i> must not enable <i>pam_loginuid.so</i> module.</p>
<dt><code>-p</code></p>
<dd>Allows <i>Cron</i> to accept any user set crontables.</p>
<dt><code>-P</code></p>
<dd>Don&#8217;t set PATH. PATH is instead inherited from the environment.</p>
<dt><code>-c</code></p>
<dd>This option enables clustering support, as described below.</p>
<dt><code>-s</code></p>
<dd>This option will direct <i>Cron</i> to send the job output to the system log using <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3). This is useful if your system does not have <code><a href="/docs/linux/man/8-sendmail/">sendmail</a></code>(8), installed or if mail is disabled.</p>
<dt><code>-x</code></p>
<dd>This option allows you to set debug flags.</dl>
<h2>Signals</h2>
<p>When the <i>SIGHUP</i> is received, the <i>Cron</i> daemon will close and reopen its log file. This proves to be useful in scripts which rotate and age log files. Naturally, this is not relevant if <i>Cron</i> was built to use <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3).</p>
<h2>Clustering Support</h2>
<p>In this version of <i>Cron</i> it is possible to use a network-mounted shared <i>/var/spool/cron</i> across a cluster of hosts and specify that only one of the hosts should run the crontab jobs in this directory at any one time. This is done by starting <i>Cron</i> with the <code>-c</code> option, and have the <i>/var/spool/cron/.cron.hostname</i> file contain just one line, which represents the hostname of whichever host in the cluster should run the jobs. If this file does not exist, or the hostname in it does not match that returned by <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2), then all crontab files in this directory are ignored. This has no effect on cron jobs specified in the <i>/etc/crontab</i> file or on files in the <i>/etc/cron.d</i> directory. These files are always run and considered host-specific. </p>
<p> Rather than editing <i>/var/spool/cron/.cron.hostname</i> directly, use the <code>-n</code> option of <code><a href="/docs/linux/man/1-crontab/">crontab</a></code>(1) to specify the host. </p>
<p> You should ensure that all hosts in a cluster, and the file server from which they mount the shared crontab directory, have closely synchronised clocks, e.g., using <code><a href="/docs/linux/man/8-ntpd/">ntpd</a></code>(8), otherwise the results will be very unpredictable. </p>
<p> Using cluster sharing automatically disables inotify support, because inotify cannot be relied on with network-mounted shared file systems.</p>
<h2>Caveats</h2>
<p>All <code>crontab</code> files have to be regular files or symlinks to regular files, they must not be executable or writable for anyone else but the owner. This requirement can be overridden by using the <code>-p</code> option on the crond command line. If inotify support is in use, changes in the symlinked crontabs are not automatically noticed by the cron daemon. The cron daemon must receive a SIGHUP signal to reload the crontabs. This is a limitation of the inotify API. </p>
<p> The syslog output will be used instead of mail, when sendmail is not installed.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-crontab/">crontab</a></code>(1), <code><a href="/docs/linux/man/5-crontab/">crontab</a></code>(5), <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<h2>Author</h2>
<p>Paul Vixie<br />
 Marcela Mašláňová<br />
 Colin Dean</p>
