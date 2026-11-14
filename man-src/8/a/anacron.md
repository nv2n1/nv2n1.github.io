---
title: "anacron(8)"
name: "anacron"
section: "8"
letter: "a"
url: "/docs/linux/man/8-anacron/"
description: "anacron – runs commands periodically"
---

<p>anacron &#8211; runs commands periodically</p>
<h2>Synopsis</h2>
<p><code>anacron </code>[<code>-s</code>] [<code>-f</code>] [<code>-n</code>] [<code>-d</code>] [<code>-q</code>] [<code>-t anacrontab</code>] [<code>-S spooldir</code>] [<i>job</i>] &#8230;<br />
 <code>anacron [-S spooldir</code>] -u [<code>-t anacrontab</code>] [<i>job</i>] &#8230;<br />
 <code>anacron </code>[<code>-V</code>|<code>-h</code>]<br />
 <code>anacron -T [-t anacrontab</code>]</p>
<h2>Description</h2>
<p>Anacron can be used to execute commands periodically, with a frequency specified in days. Unlike <code><a href="/docs/linux/man/8-cron/">cron</a>(8)</code>, it does not assume that the machine is running continuously. Hence, it can be used on machines that aren&#8217;t running 24 hours a day, to control daily, weekly, and monthly jobs that are usually controlled by <code>cron</code>. </p>
<p> When executed, Anacron reads a list of jobs from a configuration file, normally <i>/etc/anacrontab</i> (see <code><a href="/docs/linux/man/5-anacrontab/">anacrontab</a>(5)</code>). This file contains the list of jobs that Anacron controls. Each job entry specifies a period in days, a delay in minutes, a unique job identifier, and a shell command. </p>
<p> For each job, Anacron checks whether this job has been executed in the last n days, where n is the period specified for that job. If not, Anacron runs the job&#8217;s shell command, after waiting for the number of minutes specified as the delay parameter. </p>
<p> After the command exits, Anacron records the date in a special timestamp file for that job, so it can know when to execute it again. Only the date is used for the time calculations. The hour is not used. </p>
<p> When there are no more jobs to be run, Anacron exits. </p>
<p> Anacron only considers jobs whose identifier, as specified in the <i>anacrontab</i> matches any of the <i>job</i> command-line arguments. The <i>job</i> arguments can be shell wildcard patterns (be sure to protect them from your shell with adequate quoting). Specifying no <i>job</i> arguments, is equivalent to specifying &quot;*&quot; (That is, all jobs will be considered). </p>
<p> Unless the <code>-d</code> option is given (see below), Anacron forks to the background when it starts, and the parent process exits immediately. </p>
<p> Unless the <code>-s</code> or <code>-n</code> options are given, Anacron starts jobs immediately when their delay is over. The execution of different jobs is completely independent. </p>
<p> If a job generates any output on its standard output or standard error, the output is mailed to the user running Anacron (usually root), or to the address contained by the MAILTO environment variable in the crontab, if such exists. </p>
<p> Informative messages about what Anacron is doing are sent to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a>(8)</code> under facility <code>cron</code>, priority <code>notice</code>. Error messages are sent at priority <code>error</code>. </p>
<p> &quot;Active&quot; jobs (i.e. jobs that Anacron already decided to run and now wait for their delay to pass, and jobs that are currently being executed by Anacron), are &quot;locked&quot;, so that other copies of Anacron won&#8217;t run them at the same time.</p>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>Force execution of the jobs, ignoring the timestamps.</p>
<dt><code>-u</code></p>
<dd>Only update the timestamps of the jobs, to the current date, but don&#8217;t run anything.</p>
<dt><code>-s</code></p>
<dd>Serialize execution of jobs. Anacron will not start a new job before the previous one finished.</p>
<dt><code>-n</code></p>
<dd>Run jobs now. Ignore the delay specifications in the <i>/etc/anacrontab</i> file. This options implies <code>-s</code>.</p>
<dt><code>-d</code></p>
<dd>Don&#8217;t fork to the background. In this mode, Anacron will output informational messages to standard error, as well as to syslog. The output of jobs is mailed as usual.</p>
<dt><code>-q</code></p>
<dd>Suppress messages to standard error. Only applicable with <code>-d</code>.</p>
<dt><code>-t anacrontab</code></p>
<dd>Use specified anacrontab, rather than the default</p>
<dt><code>-T</code></p>
<dd>Anacrontab testing. The configuration file will be tested for validity. If there is an error in the file, an error will be shown and anacron will return 1. Valid anacrontabs will return 0.</p>
<dt><code>-S spooldir</code></p>
<dd>Use the specified spooldir to store timestamps in. This option is required for users who wish to run anacron themselves.</p>
<dt><code>-V</code></p>
<dd>Print version information, and exit.</p>
<dt><code>-h</code></p>
<dd>Print short usage message, and exit.</dl>
<h2>Signals</h2>
<p>After receiving a <code>SIGUSR1</code> signal, Anacron waits for running jobs, if any, to finish and then exits. This can be used to stop Anacron cleanly.</p>
<h2>Notes</h2>
<p>Make sure that the time-zone is set correctly before Anacron is started. (The time-zone affects the date). This is usually accomplished by setting the TZ environment variable, or by installing a <i>/usr/lib/zoneinfo/localtime</i> file. See <code><a href="/docs/linux/man/3-tzset/">tzset</a>(3)</code> for more information. </p>
<p> Timestamp files are created in the spool directory for each job in anacrontab. These are never removed automatically by anacron, and should be removed by hand if a job is no longer being scheduled.</p>
<h2>Debian-Specific Configuration</h2>
<p>On Debian-based systems, anacron will be activated hourly every day from 07:30 local time to 23:30 local time through cron job (on non-systemd systems where cron is installed and enabled) or systemd timer (on systemd-based systems). On activation, anacron will check if it missed some jobs. If yes, it will start those jobs after a short period of time. </p>
<p> By default, The hourly activation of anacron will not take place when the system is using battery and no AC power is connected to the computer. It is meant to reduce power usage and extend battery life, but such design might lead to unwanted results. Users may disable this feature and let anacron run regardless of power supply. Please read Debian-specific documentation in <i>/usr/share/doc/anacron/README.Debian</i> file for detailed instruction in now to change such behaviour.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/anacrontab</i></p>
<dd>Contains specifications of jobs. See <code><a href="/docs/linux/man/5-anacrontab/">anacrontab</a>(5)</code> for a complete description.</p>
<dt><i>/var/spool/anacron</i></p>
<dd>This directory is used by Anacron for storing timestamp files.</p>
<dt><i>/lib/systemd/system/anacron.service</i></p>
<dd>This file provides systemd service for anacron.</p>
<dt><i>/lib/systemd/system/anacron.timer</i></p>
<dd>This file provides systemd timer for anacron. Currently the service is triggered hourly through systemd timer.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-anacrontab/">anacrontab</a>(5), <a href="/docs/linux/man/8-cron/">cron</a>(8), <a href="/docs/linux/man/3-tzset/">tzset</a>(3)</code> </p>
<p> The Anacron <i>README</i> file. </p>
<p> For Debian-specific modifications, please read <i>/usr/share/doc/anacron/README.Debian</i> file for detailed information.</p>
<h2>Bugs</h2>
<p>Anacron never removes timestamp files. Remove unused files manually. </p>
<p> Anacron uses up to two file descriptors for each active job. It may run out of descriptors if there are more than about 125 active jobs (on normal kernels). </p>
<p> Mail comments, suggestions and bug reports to Sean &#8216;Shaleh&#8217; Perry &lt;shaleh@(debian.org|valinux.com)&gt;.</p>
<h2>Author</h2>
<p>Anacron was originally conceived and implemented by Christian Schwarz &lt;schwarz [at] monet.m.isar.de&gt;. The current implementation is a complete rewrite by Itai Tzur &lt;itzur [at] actcom.co.il&gt;. </p>
<p> The code base was maintained by Sean &#8216;Shaleh&#8217; Perry &lt;shaleh@(debian.org|valinux.com)&gt;. During 2004-2006, it was maintained by Pascal Hakim &lt;pasc@(debian.org|redellipse.net)&gt;. During 2009-2014, it was maintained by Peter Eisentraut &lt;petere [at] debian.org&gt;. </p>
<p> Nowadays anacron in Debian is co-maintained by various developers from Debian Project.</p>
