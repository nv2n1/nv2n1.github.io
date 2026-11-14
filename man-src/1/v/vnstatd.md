---
title: "vnstatd(1)"
name: "vnstatd"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vnstatd/"
description: "vnstatd – daemon based database updating for vnStat"
---

<h2>NAME</h2>
<p> vnstatd &#8211; daemon based database updating for vnStat </p>
<h2>SYNOPSIS</h2>
<p> <code>vnstatd</code> [ <code>-Ddnpsv?</code> ] [ <code>&#8211;alwaysadd</code> ] [ <code>&#8211;config</code> <i>file</i> ] [ <code>&#8211;daemon</code> ] [ <code>&#8211;debug</code> ] [ <code>-g</code> <i>group</i> ] [ <code>&#8211;group</code> <i>group</i> ] [ <code>&#8211;help</code> ] [ <code>&#8211;noadd</code> ] [ <code>&#8211;nodaemon</code> ] [ <code>&#8211;pidfile</code> <i>file</i> ] [ <code>&#8211;sync</code> ] [ <code>&#8211;u</code> <i>user</i> ] [ <code>&#8211;user</code> <i>user</i> ] [ <code>&#8211;version</code> ] </p>
<h2>DESCRIPTION</h2>
<p> The purpose of <code>vnstatd</code> is to provide a more flexible and robust way for updating <code><a href="/docs/linux/man/1-vnstat/">vnstat</a></code>(1) databases than what using cron for updating can provide. The daemon makes possible updating databases more often but at the same time causes less disk access since data can be cached and written only later to disk at a user configurable interval. The availability of each interface is automatically tracked which removes the need for additional scripts to be implemented and called when an interface comes online or goes offline. </p>
<p> <code>vnstatd</code> is the command for starting the daemon. The daemon can either fork itself to run as a background process or stay attached to the terminal. It supports logging to a user selectable file or using syslog. </p>
<p> Once started, the daemon will read <code><a href="/docs/linux/man/5-vnstat-conf/">vnstat.conf</a></code>(5) if available and then check if there are any databases present in the database directory that has been specified in the configuration file. By default, if no databases are found, new databases will be created during startup for all available interfaces excluding pseudo interfaces lo, lo0 and sit0. This automatic database addition behaviour can be disabled using the <code>&#8211;noadd</code> option. Alternatively, it is possible to allow the daemon to create new databases whenever previously unseen interfaces become visible using the <code>&#8211;alwaysadd</code> option. </p>
<p> The daemon will proceed to track the availability of monitored interfaces, process the interface traffic statistics and write new values to databases at a configured interval. As a result, the daemon ends up spending most of the time sleeping between updates. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;alwaysadd</code></p>
<dd> Enable automatic creation of new databases for previously unseen interfaces even if the database directory already contains databases when the daemon is started. New databases will also get created for new interfaces seen while the daemon is running. Pseudo interfaces lo, lo0 and sit0 are excluded from getting added. </p>
<dt><code>&#8211;config </code><i>file</i></p>
<dd> Use <i>file</i> as configuration file instead of using normal configuration file search functionality. </p>
<dt><code>-d, &#8211;daemon</code></p>
<dd> Fork process to background and run as a daemon. </p>
<dt><code>-D, &#8211;debug</code></p>
<dd> Provide additional output for debug purposes. The process will stay attached to the terminal for output. </p>
<dt><code>-g, &#8211;group </code><i>group</i></p>
<dd> Set daemon process group to <i>group</i> during startup. <i>group</i> can be either the name of the group or a numerical group id. This option can only be used when the process is started as root. </p>
<dt><code>&#8211;noadd</code></p>
<dd> Disable automatic creation of new databases for all available interfaces if the daemon is started with zero database found. Pseudo interfaces lo, lo0 and sit0 are excluded from getting added. </p>
<dt><code>-n, &#8211;nodaemon</code></p>
<dd> Stay in foreground attached to the current terminal and start the update process. </p>
<dt><code>-p, &#8211;pidfile </code><i>file</i></p>
<dd> Write the process id to <i>file</i> and use it for locking so that another instance of the daemon cannot be started if the same <i>file</i> is specified. </p>
<dt><code>-s, &#8211;sync</code></p>
<dd> Synchronize internal counters in the database with interface counters for all available interfaces before starting traffic monitoring. Use this option if the traffic between the previous shutdown and the current startup of the daemon needs to be ignored. This option isn&#8217;t required in normal use because the daemon will automatically synchronize the internal counters after a system reboot, if enought time has passed since the daemon was previously running or if the internal counters are clearly out of sync. </p>
<dt><code>-u, &#8211;user </code><i>user</i></p>
<dd> Set daemon process user to <i>user</i> during startup. <i>user</i> can be either the login of the user or a numerical user id. This option can only be used when the process is started as root. </p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show current version of the daemon executable. </p>
<dt><code>-?, &#8211;help</code></p>
<dd> Show a command option summary. </p>
</dl>
<h2>CONFIGURATION</h2>
<p> The behaviour of the daemon is configured mainly using the configuration keywords <code>UpdateInterval, PollInterval</code> and <code>SaveInterval</code> in the configuration file. </p>
<p> <code>UpdateInterval</code> defines in seconds how often the interface data is fetched and updated. This is similar to the run interval for alternative cron based updating. However, the difference is that the data doesn&#8217;t directly get written to disk during updates. </p>
<p> <code>PollInterval</code> defines in seconds how often the list of available interfaces is checked for possible changes. The minimum value is 2 seconds and the maximum 60 seconds. <code>PollInterval</code> also defines the resolution for other intervals. </p>
<p> <code>SaveInterval</code> defines in minutes how often cached interface data is written to disk. A write can only occur during the updating of interface data. Therefore, the value should be a multiple of <code>UpdateInterval</code> with a maximum value of 60 minutes. </p>
<p> The default values of <code>UpdateInterval</code> 30, <code>SaveInterval</code> 5 and <code>PollInterval</code> 5 are usually suitable for most systems and provide a similar behaviour as cron based updating does but with a better resolution for interface changes and fast interfaces. </p>
<p> For embedded and/or low power systems more tuned configurations are possible. In such cases if the interfaces are mostly static the <code>PollInterval</code> can be increased to around 10-30 seconds and <code>UpdateInterval</code> set to 60 seconds. Higher values up to 300 seconds are possible if the interface speed is 10 Mbit or less. <code>SaveInterval</code> can be increased for example to 15, 30 or even 60 minutes depending on how often the data needs to be viewed. </p>
<h2>SIGNALS</h2>
<p> The daemon is listening to signals <code>SIGHUP, SIGINT</code> and <code>SIGTERM.</code> Sending the <code>SIGHUP</code> signal to the daemon will cause cached data to be written to disk, a rescan of the database directory and a reload of settings from the configuration file. However, the pid file location will not be changed even if it&#8217;s configuration setting has been modified. </p>
<p> <code>SIGTERM</code> and <code>SIGINT</code> signals will cause the daemon to write all cached data to disk and then exit. </p>
<h2>FILES</h2>
<dl>
<dt><i>/var/lib/vnstat/</i></p>
<dd> Default database directory. Files are named according to the monitored interfaces.</p>
<dt><i>/etc/vnstat.conf</i></p>
<dd> Config file that will be used unless <i>$HOME/.vnstatrc</i> exists. See the configuration chapter and <code><a href="/docs/linux/man/5-vnstat-conf/">vnstat.conf</a></code>(5) for more information.</p>
<dt><i>/var/log/vnstat.log</i></p>
<dd> Log file that will be used if logging to file is enable and no other file is specified in the config file.</p>
<dt><i>/var/run/vnstat.pid</i></p>
<dd> File used for storing the process id if no other file is specified in the configuration file or using the command line parameter. </p>
</dl>
<h2>RESTRICTIONS</h2>
<p> Updates needs to be executed at least as often as it is possible for the interface to generate enough traffic to overflow the kernel interface traffic counter. Otherwise, it is possible that some traffic won&#8217;t be seen. This isn&#8217;t an issue for 64-bit kernels but at least one update every hour is always required in order to provide proper input. With 32-bit kernels, the maximum time between two updates depends on how fast the interface can transfer 4 GiB. Calculated theoretical times are:</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td>10 Mbit: 54 minutes</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>100 Mbit: 5 minutes</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td>1000 Mbit: 30 seconds</td>
<td>
</td>
</tr>
</table>
</dl>
<p> However, for 1000 Mbit interfaces updating once every minute is usually a usable solution if faster updates can&#8217;t be used. </p>
<p> Virtual and aliased interfaces cannot be monitored because the kernel doesn&#8217;t provide traffic information for that type of interfaces. Such interfaces are usually named eth0:0, eth0:1, eth0:2 etc. where eth0 is the actual interface being aliased. </p>
<h2>AUTHOR</h2>
<p> Teemu Toivola &lt;tst at iki dot fi&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-vnstat/">vnstat</a></code>(1), <code><a href="/docs/linux/man/1-vnstati/">vnstati</a></code>(1), <code><a href="/docs/linux/man/5-vnstat-conf/">vnstat.conf</a></code>(5), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) </p>
<h2>Index</h2>
