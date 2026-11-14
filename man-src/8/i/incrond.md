---
title: "incrond(8)"
name: "incrond"
section: "8"
letter: "i"
url: "/docs/linux/man/8-incrond/"
description: "incrond – inotify cron (incron) daemon"
---

<p>incrond &#8211; inotify cron (incron) daemon </p>
<h2>Synopsis</h2>
<p><code>incrond</code> [ -f <i>file</i> ] [ -n | -k ]</p>
<h2>Description</h2>
<p>The inotify cron daemon (<i>incrond</i>) is a daemon which monitors filesystem events and executes commands defined in system and user tables. It&#8217;s use is generally similar to <i><a href="/docs/linux/man/8-cron/">cron</a></i>(8). </p>
<p> <i>incrond</i> can be started from /etc/rc, /etc/rc.local and so on. It daemonizes itself (returns immediately) and doesn&#8217;t need to be started with &amp; and through <i><a href="/docs/linux/man/1-nohup/">nohup</a></i>(1). It can be run on foreground too. </p>
<p> <i>incrond</i> uses two categories of tables <i><a href="/docs/linux/man/5-incrontab/">incrontab</a></i>(5). System tables are usually located in /etc/incron.d and are maintained outside of incron (e.g. by various applications). These tables work on root rights level and thus any file may be watched and commands are executed with root privileges. </p>
<p> User tables are located in /var/spool/incron by default and have names based on user accounts. These tables use users&#8217; access rights, thus only files which the user may access are watched. Commands are executed with users&#8217; privileges. </p>
<p> If a table (incrontab) is changed <i>incrond</i> reacts immediately and reloads the table. Currently running child processes (commands) are not affected. </p>
<p> There are two files determining whether an user is allowed to use incron. These files have very simple syntax &#8211; one user name per line. If /etc/incron.allow exists the user must be noted there to be allowed to use incron. Otherwise if /etc/incron.deny exists the user must not be noted there to use incron. If none of these files exists there is no other restriction whether anybody may use incron. Location of these files can be changed in the configuration. </p>
<p> The daemon itself is currently not protected against looping. If a command executed due to an event causes the same event it leads to an infinite loop unless a flag mask containing IN_NO_LOOP is specified. Please beware of this and do not allow permission for use incron to unreliable users. </p>
<p> <code>-n</code> (or <code>&#8211;foreground</code>) option causes running on foreground. This is useful especially for testing, debugging and optimization. </p>
<p> <code>-k</code> (or <code>&#8211;kill</code>) option terminates a running instance of <code>incrond</code>. </p>
<p> <code>-f &lt;FILE&gt;</code> (or <code>&#8211;config=&lt;FILE&gt;</code>) option specifies another location for the configuration file (/etc/incron.conf is used by default). </p>
<p> <code>Environment variables:</code> For system tables, the default (the same as for incrond itself) environment variable set is used. The same applies to root&#8217;s table. For non-root user tables, the whole environment is cleared and then only these variables are set: LOGNAME, USER, USERNAME, SHELL, HOME and PATH. The variables (except PATH) take values from the user database (e.g. /etc/passwd). The PATH variable is set to /usr/local/bin:/usr/bin:/bin:/usr/X11R6/bin.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-incrontab/">incrontab</a>(1), <a href="/docs/linux/man/5-incrontab/">incrontab</a>(5), <a href="/docs/linux/man/5-incron-conf/">incron.conf</a>(5)</p>
<h2>Bugs</h2>
<p>incrond is currently not resistent against looping. Recursive monitoring (whole subtrees) has not been implemented yet.</p>
<h2>Author</h2>
<p>Lukas Jelinek &lt;lukas [at] aiken.cz&gt; (please report bugs to <a rel="nofollow" href="http://bts.aiken.cz">http://bts.aiken.cz</a> or &lt;bugs [at] aiken.cz&gt;).</p>
<h2>Copying</h2>
<p>This program is free software. It can be used, redistributed and/or modified under the terms of the GNU General Public License, version 2.</p>
