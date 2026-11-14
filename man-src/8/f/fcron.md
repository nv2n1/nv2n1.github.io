---
title: "fcron(8)"
name: "fcron"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fcron/"
description: "fcron – daemon to execute scheduled tasks"
---

<p>fcron &#8211; daemon to execute scheduled tasks</p>
<h2>Synopsis</h2>
<p><code>fcron</code> [ <code>-c </code><i>file</i> ] [ <code>-d</code> ] [ <code>-b</code> ] [ <code>-s </code><i>time</i> ] [ <code>-m </code><i>num</i> ] [ <code>-q </code><i>num</i> ] <code>fcron</code> [ <code>-c </code><i>file</i> ] [ <code>-d</code> ] [ <code>-f</code> ] [ <code>-o</code> ] [ <code>-y</code> ] [ <code>-l </code><i>time</i> ] <code>fcron</code> [ <code>-n </code><i>dir</i> ] <code>fcron</code> [ <code>-h</code> ] <code>fcron</code> [ <code>-V</code> ] </p>
<h2>Description</h2>
<p><code>Fcron</code> should be started from <i>/etc/rc</i> or <i>/etc/rc.local</i>. Unless the <code>-f</code> (or <code>&#8211;foreground</code>) option is given, it will return immediately, so you don&#8217;t need to start it with &#8216;&amp;&#8217;. </p>
<p> <code>Fcron</code> loads users <code>fcrontab</code>s (see <code><a href="/docs/linux/man/5-fcrontab/">fcrontab</a></code>(5)) files previously installed by <code>fcrontab</code> (see <code><a href="/docs/linux/man/1-fcrontab/">fcrontab</a></code>(1)). Then, <code>fcron</code> calculates the time and date of each job&#8217;s next execution, and determines how long it has to sleep, and sleeps for this amount of time. When it wakes up, it checks all jobs loaded and runs them if needed. When a job is executed, <code>fcron</code> forks, changes its user and group permissions to match those of the user the job is being done for, executes that job and mails the outputs to the user (this can be changed: see <code><a href="/docs/linux/man/5-fcrontab/">fcrontab</a></code>(5)). </p>
<p> Informative message about what <code>fcron</code> is doing are sent to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8) under facility <code>cron</code>, priority <code>notice</code>. Warning and error messages are sent respectively at priority <code>warning</code> and <code>error</code>. </p>
<dl>
<dd><code>Note:</code> <code>fcron</code> sleeps at least 20 seconds after it has been started before executing a job to avoid to use too much resources during system boot.</dl>
<h2>Options</h2>
<dl>
<dt><code>-f</code></p>
<dd>
<dt><code>&#8211;foreground</code></p>
<dd>Don&#8217;t fork to the background. In this mode, <code>fcron</code> will output informational message to standard error as well as to syslogd.</p>
<dt><code>-b</code></p>
<dd>
<dt><code>&#8211;background</code></p>
<dd>Force running in background, even if <code>fcron</code> has been compiled to run in foreground as default.</p>
<dt><code>-s </code><i>time</i></p>
<dd>
<dt><code>&#8211;savetime </code><i>time</i></p>
<dd>Save <code>fcrontab</code>s on disk every <i>time</i> sec (default is 1800).</p>
<dt><code>-m </code><i>num</i></p>
<dd>
<dt><code>&#8211;maxserial </code><i>num</i></p>
<dd>Set to <i>num</i> the maximum number of serial jobs which can run simultaneously. By default, this value is set to 1. </p>
<p> <code>See also</code>: option serial in <code><a href="/docs/linux/man/5-fcrontab/">fcrontab</a></code>(5).</p>
<dt><code>-q </code><i>num</i></p>
<dd>
<dt><code>&#8211;queuelen </code><i>num</i></p>
<dd>Set to n the number of jobs the serial queue and the lavg queue can contain.</p>
<dt><code>-c </code><i>file</i></p>
<dd>
<dt><code>&#8211;configfile </code><i>file</i></p>
<dd>Make <code>fcron</code> use config file <i>file</i> instead of default config file <i>/usr/local/etc/fcron.conf</i>. To interact with that running <code>fcron</code> process, <code>fcrontab</code> must use the same config file (which is defined by <code>fcrontab</code>&#8216;s option <code>-c</code>). That way, several <code>fcron</code> processes can run simultaneously on an only system (but each <code>fcron</code> process *must* have a different spool dir and pid file from the other processes).</p>
<dt><code>-o</code></p>
<dd>
<dt><code>&#8211;once</code></p>
<dd>Execute all jobs that need to be run at the time <code>fcron</code> was started, wait for them, then return. Sets <code>firstsleep</code> to 0. May be especially useful when used with options <code>-y</code> and <code>-f</code> in a script run, for instance, at dialup connection. </p>
<p> <code>See also</code>: fcrontab&#8217;s options volatile, stdout.</p>
<dt><code>-y</code></p>
<dd>
<dt><code>&#8211;nosyslog</code></p>
<dd>Don&#8217;t log to syslog at all. May be useful when running in foreground.</p>
<dt><code>-l </code><i>time</i></p>
<dd>
<dt><code>&#8211;firstsleep </code><i>time</i></p>
<dd>Sets the initial delay (in seconds) before any job is executed, default to 20 seconds.</p>
<dt><code>-n </code><i>dir</i></p>
<dd>
<dt><code>&#8211;newspooldir </code><i>dir</i></p>
<dd>Create <i>dir</i> as a new spool directory for <code>fcron</code>. Set correctly its mode and owner. Then, exit.</p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd>Display a brief description of the options.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd>Display an informational message about <code>fcron</code>, including its version and the license under which it is distributed.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;debug</code></p>
<dd>Run in debug mode (more details on stderr &#8212; if option <code>-f</code> is set &#8212; and in log file)</dl>
<h2>Return Values</h2>
<p><code>Fcron</code> returns 0 on normal exit, and 1 on error.</p>
<h2>Signals</h2>
<dl>
<dt><code>SIGTERM</code></p>
<dd>Save configuration (time remaining until next execution, time and date of next execution, etc), wait for all running jobs and exit.</p>
<dt><code>SIGUSR1</code></p>
<dd>Force <code>fcron</code> to reload its configuration.</p>
<dt><code>SIGUSR2</code></p>
<dd>Make <code>fcron</code> print its current schedule on syslog. It also toggles on/off the printing on debug info on syslog.</p>
<dt><code>SIGHUP</code></p>
<dd>Tell <code>fcron</code> to check if there is any configuration update (this signal is used by <code><a href="/docs/linux/man/5-fcrontab/">fcrontab</a></code>(5))</dl>
<h2>Conforming To</h2>
<p>Should be POSIX compliant.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/local/etc/fcron.conf</i></p>
<dd>Configuration file for <code>fcron</code>, <code>fcrontab</code> and <code>fcrondyn</code>: contains paths (spool dir, pid file) and default programs to use (editor, shell, etc). See <code><a href="/docs/linux/man/5-fcron-conf/">fcron.conf</a></code>(5) for more details.</p>
<dt><i>/usr/local/etc/fcron.allow</i></p>
<dd>Users allowed to use <code>fcrontab</code> and <code>fcrondyn</code> (one name per line, special name &quot;all&quot; acts for everyone)</p>
<dt><i>/usr/local/etc/fcron.deny</i></p>
<dd>Users who are not allowed to use <code>fcrontab</code> and <code>fcrondyn</code> (same format as allow file)</p>
<dt><i>/usr/local/etc/pam.d/fcron</i><code> (or </code><i>/usr/local/etc/pam.conf</i><code>)</code></p>
<dd>PAM configuration file for <code>fcron</code>. Take a look at <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8) for more details.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-fcrontab/">fcrontab</a></code>(1), </p>
<p> <code><a href="/docs/linux/man/1-fcrondyn/">fcrondyn</a></code>(1), </p>
<p> <code><a href="/docs/linux/man/5-fcrontab/">fcrontab</a></code>(5), </p>
<p> <code><a href="/docs/linux/man/5-fcron-conf/">fcron.conf</a></code>(5), </p>
<p> <code><a href="/docs/linux/man/8-fcron/">fcron</a></code>(8). </p>
<p> If you&#8217;re learning how to use fcron from scratch, I suggest that you read the HTML version of the documentation (if your are not reading it right now! :) ): the content is the same, but it is easier to navigate thanks to the hyperlinks.</p>
<h2>Author</h2>
<p>Thibault Godouet &lt;fcron [at] free.fr&gt;</p>
