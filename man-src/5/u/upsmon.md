---
title: "upsmon(5)"
name: "upsmon"
section: "5"
letter: "u"
url: "/docs/linux/man/5-upsmon/"
description: "upsmon.conf – Configuration for Network UPS Tools upsmon"
---

<p>upsmon.conf &#8211; Configuration for Network UPS Tools upsmon </p>
<h2>Description</h2>
<p>This file&#8217;s primary job is to define the systems that <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) will monitor and to tell it how to shut down the system when necessary. It will contain passwords, so keep it secure. Ideally,only the upsmon process should be able to read it. Additionally, other optional configuration values can be set in this file. </p>
<h2>Configuration Directives</h2>
<dl>
<dt>DEADTIME <i>seconds</i></p>
<dd>upsmon allows a UPS to go missing for this many seconds before declaring it &quot;dead&quot;. The default is 15 seconds. </p>
<p> upsmon requires a UPS to provide status information every few seconds (see POLLFREQ and POLLFREQALERT) to keep things updated. If the status fetch fails, the UPS is marked stale. If it stays stale for more than DEADTIME seconds, the UPS is marked dead. </p>
<p> A dead UPS that was last known to be on battery is assumed to have changed to a low battery condition. This may force a shutdown if it is providing a critical amount of power to your system. This seems disruptive, but the alternative is barreling ahead into oblivion and crashing when you run out of power. </p>
<p> Note: DEADTIME should be a multiple of POLLFREQ and POLLFREQALERT. Otherwise, you&#8217;ll have &quot;dead&quot; UPSes simply because upsmon isn&#8217;t polling them quickly enough. Rule of thumb: take the larger of the two POLLFREQ values, and multiply by 3. </p>
<dt>FINALDELAY <i>seconds</i></p>
<dd>When running in master mode, upsmon waits this long after sending the NOTIFY_SHUTDOWN to warn the users. After the timer elapses, it then runs your SHUTDOWNCMD. By default this is set to 5 seconds. </p>
<p> If you need to let your users do something in between those events, increase this number. Remember, at this point your UPS battery is almost depleted, so don&#8217;t make this too big. </p>
<p> Alternatively, you can set this very low so you don&#8217;t wait around when it&#8217;s time to shut down. Some UPSes don&#8217;t give much warning for low battery and will require a value of 0 here for a safe shutdown. </p>
<p> Note: If FINALDELAY on the slave is greater than HOSTSYNC on the master, the master will give up waiting for the slave to disconnect. </p>
<dt>HOSTSYNC <i>seconds</i></p>
<dd>upsmon will wait up to this many seconds in master mode for the slaves to disconnect during a shutdown situation. By default, this is 15 seconds. </p>
<p> When a UPS goes critical (on battery + low battery, or &quot;FSD&quot; &#8211; forced shutdown), the slaves are supposed to disconnect and shut down right away. The HOSTSYNC timer keeps the master upsmon from sitting there forever if one of the slaves gets stuck. </p>
<p> This value is also used to keep slave systems from getting stuck if the master fails to respond in time. After a UPS becomes critical, the slave will wait up to HOSTSYNC seconds for the master to set the FSD flag. If that timer expires, the slave will assume that the master is broken and will shut down anyway. </p>
<p> This keeps the slaves from shutting down during a short-lived status change to &quot;OB LB&quot; that the slaves see but the master misses. </p>
<dt>MINSUPPLIES <i>num</i></p>
<dd>Set the number of power supplies that must be receiving power to keep this system running. Normal computers have just one power supply, so the default value of 1 is acceptable. </p>
<p> Large/expensive server type systems usually have more, and can run with a few missing. The HP NetServer LH4 can run with 2 out of 4, for example, so you&#8217;d set it to 2. The idea is to keep the box running as long as possible, right? </p>
<p> Obviously you have to put the redundant supplies on different UPS circuits for this to make sense! See big-servers.txt in the docs subdirectory for more information and ideas on how to use this feature. </p>
<p> Also see the section on &quot;power values&quot; in <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8). </p>
<dt>MONITOR <i>system</i> <i>powervalue</i> <i>username</i> <i>password</i> <i>type</i></p>
<dd>Each UPS that you need to be monitor should have a MONITOR line. Not all of these need supply power to the system that is running upsmon. You may monitor other systems if you want to be able to send notifications about status changes on them. </p>
<p> You must have at least one MONITOR directive in this file. </p>
<p> <i>system</i> is a UPS identifier. It is in this form: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;upsname&gt;[@&lt;hostname&gt;[:&lt;port&gt;]]</p>
<p> The default hostname is &quot;localhost&quot;. Some examples: </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr>&quot;su700 [at] mybox&quot;&nbsp;<wbr>means a UPS called&nbsp;<wbr>&quot;su700&quot;&nbsp;<wbr>on a system called&nbsp;<wbr>&quot;mybox&quot;. This is the normal form. </p>
<p>&nbsp;<wbr>&#8211;&nbsp;<wbr>&quot;fenton [at] bigbox:5678&quot;&nbsp;<wbr>is a UPS called&nbsp;<wbr>&quot;fenton&quot;&nbsp;<wbr>on a system called &quot;bigbox&quot; which runs <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) on port &quot;5678&quot;. </p>
<p> <i>powervalue</i> is an integer representing the number of power supplies that the UPS feeds on this system. Most normal computers have one power supply, and the UPS feeds it, so this value will be 1. You need a very large or special system to have anything higher here. </p>
<p> You can set the <i>powervalue</i> to 0 if you want to monitor a UPS that doesn&#8217;t actually supply power to this system. This is useful when you want to have upsmon do notifications about status changes on a UPS without shutting down when it goes critical. </p>
<p> The <i>username</i> and <i>password</i> on this line must match an entry in that system&#8217;s <code><a href="/docs/linux/man/5-upsd-users/">upsd.users</a></code>(5). If your username is &quot;monmaster&quot; and your password is &quot;blah&quot;, the MONITOR line might look like this: </p>
<p> MONITOR myups [at] bigserver 1 monmaster blah master </p>
<p> Meanwhile, the upsd.users on &#8216;bigserver&#8217; would look like this: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[monmaster]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>password = blah</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>upsmon master (or slave)</p>
<p> The <i>type</i> refers to the relationship with <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8). It can be either &quot;master&quot; or &quot;slave&quot;. See <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) for more information on the meaning of these modes. The mode you pick here also goes in the upsd.users file, as seen in the example above. </p>
<dt>NOCOMMWARNTIME <i>seconds</i></p>
<dd>upsmon will trigger a NOTIFY_NOCOMM after this many seconds if it can&#8217;t reach any of the UPS entries in this configuration file. It keeps warning you until the situation is fixed. By default this is 300 seconds. </p>
<dt>NOTIFYCMD <i>command</i></p>
<dd>upsmon calls this to send messages when things happen. </p>
<p> This command is called with the full text of the message as one argument. The environment string NOTIFYTYPE will contain the type string of whatever caused this event to happen. </p>
<p> If you need to use <code><a href="/docs/linux/man/8-upssched/">upssched</a></code>(8), then you must make it your NOTIFYCMD by listing it here. </p>
<p> Note that this is only called for NOTIFY events that have EXEC set with NOTIFYFLAG. See NOTIFYFLAG below for more details. </p>
<p> Making this some sort of shell script might not be a bad idea. For more information and ideas, see pager.txt in the docs directory. </p>
<p> Remember, this also needs to be one element in the configuration file, so if your command has spaces, then wrap it in quotes. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>NOTIFYCMD &quot;/path/to/script &#8211;foo &#8211;bar&quot;</p>
<p> This script is run in the background &#8211; that is, upsmon forks before it calls out to start it. This means that your NOTIFYCMD may have multiple instances running simultaneously if a lot of stuff happens all at once. Keep this in mind when designing complicated notifiers. </p>
<dt>NOTIFYMSG <i>type</i> <i>message</i></p>
<dd>upsmon comes with a set of stock messages for various events. You can change them if you like. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>NOTIFYMSG ONLINE &quot;UPS %s is getting line power&quot;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>NOTIFYMSG ONBATT &quot;Someone pulled the plug on %s&quot;</p>
<p> Note that %s is replaced with the identifier of the UPS in question. </p>
<p> Possible values for <i>type</i>: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ONLINE &#8211; UPS is back online</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>ONBATT &#8211; UPS is on battery</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>LOWBATT &#8211; UPS is on battery and has a low battery (is critical)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>FSD &#8211; UPS is being shutdown by the master (FSD = &quot;Forced Shutdown&quot;)</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>COMMOK &#8211; Communications established with the UPS</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>COMMBAD &#8211; Communications lost to the UPS</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>SHUTDOWN &#8211; The system is being shutdown</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>REPLBATT &#8211; The UPS battery is bad and needs to be replaced</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>NOCOMM &#8211; A UPS is unavailable (can&#8217;t be contacted for monitoring) </p>
<p> The message must be one element in the configuration file, so if it contains spaces, you must wrap it in quotes. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>NOTIFYMSG NOCOMM &quot;Someone stole UPS %s&quot;</p>
<dt>NOTIFYFLAG <i>type</i> <i>flag</i>[+<i>flag</i>][+<i>flag</i>]&#8230;</p>
<dd>By default, upsmon sends walls global messages to all logged in users) via /bin/wall and writes to the syslog when things happen. You can change this. </p>
<p> Examples: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>NOTIFYFLAG ONLINE SYSLOG</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>NOTIFYFLAG ONBATT SYSLOG+WALL+EXEC</p>
<p> Possible values for the flags: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>SYSLOG &#8211; Write the message to the syslog</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>WALL &#8211; Write the message to all users with /bin/wall</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>EXEC &#8211; Execute NOTIFYCMD (see above) with the message</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>IGNORE &#8211; Don&#8217;t do anything</p>
<p> If you use IGNORE, don&#8217;t use any other flags on the same line. </p>
<dt>POLLFREQ <i>seconds</i></p>
<dd>Normally upsmon polls the <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) server every 5 seconds. If this is flooding your network with activity, you can make it higher. You can also make it lower to get faster updates in some cases. </p>
<p> There are some catches. First, if you set the POLLFREQ too high, you may miss short-lived power events entirely. You also risk triggering the DEADTIME (see above) if you use a very large number. </p>
<p> Second, there is a point of diminishing returns if you set it too low. While upsd normally has all of the data available to it instantly, most drivers only refresh the UPS status once every 2 seconds. Polling any more than that usually doesn&#8217;t get you the information any faster. </p>
<dt>POLLFREQALERT <i>seconds</i></p>
<dd>This is the interval that upsmon waits between polls if any of its UPSes are on battery. You can use this along with POLLFREQ above to slow down polls during normal behavior, but get quicker updates when something bad happens. </p>
<p> This should always be equal to or lower than the POLLFREQ value. By default it is also set 5 seconds. </p>
<p> The warnings from the POLLFREQ entry about too-high and too-low values also apply here. </p>
<dt>POWERDOWNFLAG <i>filename</i></p>
<dd>upsmon creates this file when running in master mode when the UPS needs to be powered off. You should check for this file in your shutdown scripts and call <code>upsdrvctl shutdown</code> if it exists. </p>
<p> This is done to forcibly reset the slaves, so they don&#8217;t get stuck at the &quot;halted&quot; stage even if the power returns during the shutdown process. This usually does not work well on contact-closure UPSes that use the genericups driver. </p>
<p> See the shutdown.txt file in the docs subdirectory for more information. </p>
<dt>RBWARNTIME <i>seconds</i></p>
<dd>When a UPS says that it needs to have its battery replaced, upsmon will generate a NOTIFY_REPLBATT event. By default this happens every 43200 seconds &#8211; 12 hours. </p>
<p> If you need another value, set it here. </p>
<dt>RUN_AS_USER <i>username</i></p>
<dd>upsmon normally runs the bulk of the monitoring duties under another user ID after dropping root privileges. On most systems this means it runs as &quot;nobody&quot;, since that&#8217;s the default from compile-time. </p>
<p> The catch is that &quot;nobody&quot; can&#8217;t read your upsmon.conf, since by default it is installed so that only root can open it. This means you won&#8217;t be able to reload the configuration file, since it will be unavailable. </p>
<p> The solution is to create a new user just for upsmon, then make it run as that user. I suggest &quot;nutmon&quot;, but you can use anything that isn&#8217;t already taken on your system. Just create a regular user with no special privileges and an impossible password. </p>
<p> Then, tell upsmon to run as that user, and make upsmon.conf readable by it. Your reloads will work, and your config file will stay secure. </p>
<p> This file should not be writable by the upsmon user, as it would be possible to exploit a hole, change the SHUTDOWNCMD to something malicious, then wait for upsmon to be restarted. </p>
<dt>SHUTDOWNCMD <i>command</i></p>
<dd>upsmon runs this command when the system needs to be brought down. If it is a slave, it will do that immediately whenever the current overall power value drops below the MINSUPPLIES value above. </p>
<p> When upsmon is a master, it will allow any slaves to log out before starting the local shutdown procedure. </p>
<p> Note that the command needs to be one element in the config file. If your shutdown command includes spaces, then put it in quotes to keep it together, i.e.: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>SHUTDOWNCMD &quot;/sbin/shutdown -h +0&quot;</p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8), <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8), <code><a href="/docs/linux/man/8-nutupsdrv/">nutupsdrv</a></code>(8).</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
