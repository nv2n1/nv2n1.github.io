---
title: "at(1)"
name: "at"
section: "1"
letter: "a"
url: "/docs/linux/man/1-at/"
description: "at, batch, atq, atrm – queue, examine or delete jobs for later execution"
---

<h2>NAME</h2>
<p> at, batch, atq, atrm &#8211; queue, examine or delete jobs for later execution</p>
<h2>SYNOPSIS</h2>
<p> <code>at</code> [<code>-V</code>] [<code>-q</code> <i>queue</i>] [<code>-f</code> <i>file</i>] [<code>-mMlv</code>] <i>timespec</i>&#8230;<br />
 <code>at</code> [<code>-V</code>] [<code>-q</code> <i>queue</i>] [<code>-f</code> <i>file</i>] [<code>-mMkv</code>] [<code>-t</code> <i>time</i>]<br />
 <code>at -c</code> <i>job</i> [<i>job&#8230;</i>]<br />
 <code>atq</code> [<code>-V</code>] [<code>-q</code> <i>queue</i>]<br />
 <code>at</code> [<code>-rd</code>] <i>job</i> [<i>job&#8230;</i>]<br />
 <code>atrm</code> [<code>-V</code>] <i>job</i> [<i>job&#8230;</i>]<br />
 <code>batch</code><br />
 <code>at -b</code></p>
<h2>DESCRIPTION</h2>
<p> <code>at</code> and <code>batch</code> read commands from standard input or a specified file which are to be executed at a later time, using <code>/bin/sh</code>.</p>
<dl>
<dt><code>at</code></p>
<dd> executes commands at a specified time.</p>
<dt><code>atq</code></p>
<dd> lists the user&#8217;s pending jobs, unless the user is the superuser; in that case, everybody&#8217;s jobs are listed. The format of the output lines (one for each job) is: Job number, date, hour, queue, and username.</p>
<dt><code>atrm</code></p>
<dd> deletes jobs, identified by their job number.</p>
<dt><code>batch</code></p>
<dd> executes commands when system load levels permit; in other words, when the load average drops below 0.8, or the value specified in the invocation of <code>atd</code>.</dl>
<p> <code>At</code> allows fairly complex time specifications, extending the POSIX.2 standard. It accepts times of the form <code>HH:MM</code> to run a job at a specific time of day. (If that time is already past, the next day is assumed.) You may also specify <code>midnight,</code> <code>noon,</code> or <code>teatime</code> (4pm) and you can have a time-of-day suffixed with <code>AM</code> or <code>PM</code> for running in the morning or the evening. You can also say what day the job will be run, by giving a date in the form <code>month-name</code> <code>day</code> with an optional <code>year,</code> or giving a date of the form <i>MMDD</i>[<i>CC</i>]<i>YY</i>, <i>MM</i>/<i>DD</i>/[<i>CC</i>]<i>YY</i>, <i>DD</i>.<i>MM</i>.[<i>CC</i>]<i>YY</i> or [<i>CC</i>]<i>YY</i>&#8211;<i>MM</i>&#8211;<i>DD</i>. The specification of a date <i>must</i> follow the specification of the time of day. You can also give times like <code>now</code> <code>+</code> <i>count</i> <i>time-units,</i> where the time-units can be <code>minutes,</code> <code>hours,</code> <code>days,</code> or <code>weeks</code> and you can tell <code>at</code> to run the job today by suffixing the time with <code>today</code> and to run the job tomorrow by suffixing the time with <code>tomorrow.</code> </p>
<p> For example, to run a job at 4pm three days from now, you would do <code>at 4pm + 3 days,</code> to run a job at 10:00am on July 31, you would do <code>at 10am Jul 31</code> and to run a job at 1am tomorrow, you would do <code>at 1am tomorrow.</code> </p>
<p> The definition of the time specification can be found in <i>/usr/share/doc/at-3.1.13/timespec</i>. </p>
<p> For both <code>at</code> and <code>batch</code>, commands are read from standard input or the file specified with the <code>-f</code> option and executed. The working directory, the environment (except for the variables <code>BASH_VERSINFO</code>, <code>DISPLAY</code>, <code>EUID</code>, <code>GROUPS</code>, <code>SHELLOPTS</code>, <code>TERM</code>, <code>UID</code>, and <code>_</code>) and the umask are retained from the time of invocation. </p>
<p> As <code>at</code> is currently implemented as a setuid program, other environment variables (e.g. <code>LD_LIBRARY_PATH</code> or <code>LD_PRELOAD</code>) are also not exported. This may change in the future. As a workaround, set these variables explicitly in your job. </p>
<p> An <code>at </code>&#8211; or <code>batch &#8211;</code> command invoked from a <code><a href="/docs/linux/man/1-su/">su</a>(1)</code> shell will retain the current userid. The user will be mailed standard error and standard output from his commands, if any. Mail will be sent using the command <code>/usr/sbin/sendmail</code>. If <code>at</code> is executed from a <code><a href="/docs/linux/man/1-su/">su</a>(1)</code> shell, the owner of the login shell will receive the mail. </p>
<p> The superuser may use these commands in any case. For other users, permission to use at is determined by the files <i>/etc/at.allow</i> and <i>/etc/at.deny</i>. See <code><a href="/docs/linux/man/5-at-allow/">at.allow</a></code>(5) for details.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code></p>
<dd> prints the version number to standard error and exit successfully.</p>
<dt><code>-q</code><i> queue</i></p>
<dd> uses the specified queue. A queue designation consists of a single letter; valid queue designations range from <code>a</code> to <code>z</code> and <code>A</code> to <code>Z</code>. The <code>a</code> queue is the default for <code>at</code> and the <code>b</code> queue for <code>batch</code>. Queues with higher letters run with increased niceness. The special queue &quot;=&quot; is reserved for jobs which are currently running. </p>
<p> If a job is submitted to a queue designated with an uppercase letter, the job is treated as if it were submitted to batch at the time of the job. Once the time is reached, the batch processing rules with respect to load average apply. If <code>atq</code> is given a specific queue, it will only show jobs pending in that queue.</p>
<dt><code>-m</code></p>
<dd> Send mail to the user when the job has completed even if there was no output.</p>
<dt><code>-M</code></p>
<dd> Never send mail to the user.</p>
<dt><code>-f</code><i> file</i></p>
<dd> Reads the job from <i>file</i> rather than standard input.</p>
<dt><code>-t</code><i> time</i></p>
<dd> run the job at <i>time</i>, given in the format [[CC]YY]MMDDhhmm[.ss]</p>
<dt><code>-l</code></p>
<dd> Is an alias for <code>atq.</code></p>
<dt><code>-r</code></p>
<dd> Is an alias for <code>atrm.</code></p>
<dt><code>-d</code></p>
<dd> Is an alias for <code>atrm.</code></p>
<dt><code>-b</code></p>
<dd> is an alias for <code>batch</code>.</p>
<dt><code>-v</code></p>
<dd> Shows the time the job will be executed before reading the job. </p>
<p> Times displayed will be in the format &quot;Thu Feb 20 14:50:00 1997&quot;.</p>
<dt><code>-c</code></p>
<dd> cats the jobs listed on the command line to standard output.</dl>
<h2>FILES</h2>
<p> <i>/var/spool/at</i><br />
 <i>/var/spool/at/spool</i><br />
 <i>/proc/loadavg</i><br />
 <i>/var/run/utmp</i><br />
 <i>/etc/at.allow</i><br />
 <i>/etc/at.deny</i></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-at-allow/">at.allow</a></code>(5), <code><a href="/docs/linux/man/5-at-deny/">at.deny</a></code>(5), <code><a href="/docs/linux/man/8-atd/">atd</a></code>(8), <code><a href="/docs/linux/man/1-cron/">cron</a></code>(1), <code><a href="/docs/linux/man/1-nice/">nice</a></code>(1), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2).</p>
<h2>BUGS</h2>
<p> The correct operation of <code>batch</code> for Linux depends on the presence of a <i>proc</i>&#8211; type directory mounted on <i>/proc</i>. </p>
<p> If the file <i>/var/run/utmp</i> is not available or corrupted, or if the user is not logged on at the time <code>at</code> is invoked, the mail is sent to the userid found in the environment variable <code>LOGNAME</code>. If that is undefined or empty, the current userid is assumed. </p>
<p> <code>At</code> and <code>batch</code> as presently implemented are not suitable when users are competing for resources. If this is the case for your site, you might want to consider another batch system, such as <code>nqs</code>.</p>
<h2>AUTHOR</h2>
<p> At was mostly written by Thomas Koenig, ig25 [at] rz.uni-karlsruhe.de. </p>
<h2>Index</h2>
