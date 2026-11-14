---
title: "upsmon(8)"
name: "upsmon"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upsmon/"
description: "upsmon – UPS monitor and shutdown controller"
---

<p>upsmon &#8211; UPS monitor and shutdown controller</p>
<h2>Synopsis</h2>
<p><code>upsmon</code> -h </p>
<p> <code>upsmon</code> -c <i>command</i> </p>
<p> <code>upsmon</code> [-D] [-K] [-p] [-u <i>user</i>]</p>
<h2>Description</h2>
<p><code>upsmon</code> is the client process that is responsible for the most important part of UPS monitoring&#8212;shutting down the system when the power goes out. It can call out to other helper programs for notification purposes during power events. </p>
<p> upsmon can monitor multiple systems using a single process. Every UPS that is defined in the <code><a href="/docs/linux/man/5-upsmon-conf/">upsmon.conf</a></code>(5) configuration file is assigned a power value and a type (<code>slave</code> or <code>master</code>).</p>
<h2>Options</h2>
<p><code>-h</code></p>
<dl>
<dd>Display the help message.</dl>
<p> <code>-c</code> <i>command</i></p>
<dl>
<dd>Send the command <i>command</i> to the existing upsmon process. Valid commands are: </p>
<p> <code>fsd</code></p>
<dl>
<dd>shutdown all master UPSes (use with caution)</dl>
<p> <code>stop</code></p>
<dl>
<dd>stop monitoring and exit</dl>
<p> <code>reload</code></p>
<dl>
<dd>reread <code><a href="/docs/linux/man/5-upsmon-conf/">upsmon.conf</a></code>(5) configuration file. See &quot;reloading nuances&quot; below if this doesn&#8217;t work.</dl>
</dl>
<p> <code>-D</code></p>
<dl>
<dd>Raise the debugging level. upsmon will run in the foreground and prints information on stdout about the monitoring process. Use this multiple times for more details.</dl>
<p> <code>-K</code></p>
<dl>
<dd>Test for the shutdown flag. If it exists and contains the magic string from upsmon, then upsmon will exit with EXIT_SUCCESS. Any other condition will make upsmon exit with EXIT_FAILURE. </p>
<p> You can test for a successful exit from upsmon -K in your shutdown scripts to know when to call <code><a href="/docs/linux/man/8-upsdrvctl/">upsdrvctl</a></code>(8) to shut down the UPS.</dl>
<p> <code>-p</code></p>
<dl>
<dd>Run privileged all the time. Normally upsmon will split into two processes. The majority of the code runs as an unprivileged user, and only a tiny stub runs as root. This switch will disable that mode, and run the old &quot;all root all the time&quot; system. </p>
<p> This is not the recommended mode, and you should not use this unless you have a very good reason.</dl>
<p> <code>-u</code> <i>user</i></p>
<dl>
<dd>Set the user for the unprivileged monitoring process. This has no effect when using -p. </p>
<p> The default user is set at configure time with <i>configure &#8211;with-user=&#8230;</i>. Typically this is <i>nobody</i>, but other distributions will probably have a specific <i>nut</i> user for this task. If your notification scripts need to run as a specific user, set it here. </p>
<p> You can also set this in the <code><a href="/docs/linux/man/5-upsmon-conf/">upsmon.conf</a></code>(5) file with the RUN_AS_USER directive.</dl>
<h2>Ups Definitions</h2>
<p>In the <code><a href="/docs/linux/man/5-upsmon-conf/">upsmon.conf</a></code>(5), you must specify at least one UPS that will be monitored. Use the MONITOR directive. </p>
<dl>
<dd>
<pre>MONITOR 'system' 'powervalue' 'username' 'password' 'type'</pre>
</dl>
<p> The <i>system</i> refers to a <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) server, in the form upsname[@hostname[:port]]. The default hostname is &quot;localhost&quot;. Some examples follow: </p>
<dl>
<dd>&bull; &quot;su700 [at] mybox&quot; means a UPS called &quot;su700&quot; on a system called &quot;mybox&quot;. This is the normal form.</dl>
<dl>
<dd>&bull; &quot;fenton [at] bigbox:5678&quot; is a UPS called &quot;fenton&quot; on a system called &quot;bigbox&quot; which runs <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) on port &quot;5678&quot;.</dl>
<p> The <i>powervalue</i> refers to how many power supplies on this system are being driven this UPS. This is typically set to 1, but see the section on power values below. </p>
<p> The <i>username</i> is a section in your <code><a href="/docs/linux/man/5-upsd-users/">upsd.users</a></code>(5) file. Whatever password you set in that section must match the <i>password</i> set in this file. </p>
<p> The type set in that section must also match the <i>type</i> here&#8211; <code>master</code> or <code>slave</code>. In general, a master process is one running on the system with the UPS actually plugged into a serial port, and a slave is drawing power from the UPS but can&#8217;t talk to it directly. See the section on UPS types for more.</p>
<h2>Notify Events</h2>
<p><code>upsmon</code> senses several events as it monitors each UPS. They are called notify events as they can be used to tell the users and admins about the change in status. See the additional NOTIFY-related sections below for information on customizing the delivery of these messages. </p>
<p> <code>ONLINE</code></p>
<dl>
<dd>The UPS is back on line.</dl>
<p> <code>ONBATT</code></p>
<dl>
<dd>The UPS is on battery.</dl>
<p> <code>LOWBATT</code></p>
<dl>
<dd>The UPS battery is low (as determined by the driver).</dl>
<p> <code>FSD</code></p>
<dl>
<dd>The UPS has been commanded into the &quot;forced shutdown&quot; mode.</dl>
<p> <code>COMMOK</code></p>
<dl>
<dd>Communication with the UPS has been established.</dl>
<p> <code>COMMBAD</code></p>
<dl>
<dd>Communication with the UPS was just lost.</dl>
<p> <code>SHUTDOWN</code></p>
<dl>
<dd>The local system is being shut down.</dl>
<p> <code>REPLBATT</code></p>
<dl>
<dd>The UPS needs to have its battery replaced.</dl>
<p> <code>NOCOMM</code></p>
<dl>
<dd>The UPS can&#8217;t be contacted for monitoring.</dl>
<h2>Notify Command</h2>
<p>In <code><a href="/docs/linux/man/5-upsmon-conf/">upsmon.conf</a></code>(5), you can configure a program called the NOTIFYCMD that will handle events that occur. </p>
<p> NOTIFYCMD &quot;<i>path to program</i>&quot; </p>
<p> NOTIFYCMD &quot;/usr/local/bin/notifyme&quot; </p>
<p> Remember to wrap the path in &quot;quotes&quot; if it contains any spaces. </p>
<p> The program you run as your NOTIFYCMD can use the environment variables NOTIFYTYPE and UPSNAME to know what has happened and on which UPS. It also receives the notification message (see below) as the first (and only) argument, so you can deliver a preformatted message too. </p>
<p> Note that the NOTIFYCMD will only be called for a given event when you set the EXEC flag by using the notify flags, below:</p>
<h2>Notify Flags</h2>
<p>By default, all notify events (see above) generate a global message (wall) to all users, plus they are logged via the syslog. You can change this with the NOTIFYFLAG directive in the configuration file: </p>
<p> NOTIFYFLAG <i>notifytype</i> <i>flags</i> </p>
<p> Examples: </p>
<dl>
<dd>&bull; </p>
<p> NOTIFYFLAG ONLINE SYSLOG</dl>
<dl>
<dd>&bull; </p>
<p> NOTIFYFLAG ONBATT SYSLOG+WALL</dl>
<dl>
<dd>&bull; </p>
<p> NOTIFYFLAG LOWBATT SYSLOG+WALL+EXEC</dl>
<p> The flags that can be set on a given notify event are: </p>
<p> <code>SYSLOG</code></p>
<dl>
<dd>Write this message to the syslog.</dl>
<p> <code>WALL</code></p>
<dl>
<dd>Send this message to all users on the system via <code><a href="/docs/linux/man/1-wall/">wall</a></code>(1).</dl>
<p> <code>EXEC</code></p>
<dl>
<dd>Execute the NOTIFYCMD.</dl>
<p> <code>IGNORE</code></p>
<dl>
<dd>Don&#8217;t do anything. If you use this, don&#8217;t use any of the other flags.</dl>
<p> You can mix these flags. &quot;SYSLOG+WALL+EXEC&quot; does all three for a given event.</p>
<h2>Notify Messages</h2>
<p>upsmon comes with default messages for each of the NOTIFY events. These can be changed with the NOTIFYMSG directive. </p>
<p> NOTIFYMSG <i>type</i> &quot;<i>message</i>&quot; </p>
<p> Examples: </p>
<dl>
<dd>&bull; </p>
<p> NOTIFYMSG ONLINE &quot;UPS %s is getting line power&quot;</dl>
<dl>
<dd>&bull; ` NOTIFYMSG ONBATT &quot;Someone pulled the plug on %s&quot;`</dl>
<p> The first instance of %s is replaced with the identifier of the UPS that generated the event. These messages are used when sending walls to the users directly from upsmon, and are also passed to the NOTIFYCMD.</p>
<h2>Power Values</h2>
<p>The &quot;current overall power value&quot; is the sum of all UPSes that are currently able to supply power to the system hosting upsmon. Any UPS that is either on line or just on battery contributes to this number. If a UPS is critical (on battery and low battery) or has been put into &quot;forced shutdown&quot; mode, it no longer contributes. </p>
<p> A &quot;power value&quot; on a MONITOR line in the config file is the number of power supplies that the UPS runs on the current system. </p>
<p> MONITOR <i>upsname</i> <i>powervalue</i> <i>username</i> <i>password</i> <i>type</i> </p>
<p> Normally, you only have one power supply, so it will be set to 1. </p>
<p> MONITOR myups [at] myhost 1 username mypassword master </p>
<p> On a large server with redundant power supplies, the power value for a UPS may be greater than 1. You may also have more than one of them defined. </p>
<p> MONITOR ups-alpha [at] myhost 2 username mypassword master </p>
<p> MONITOR ups-beta [at] myhost 2 username mypassword master </p>
<p> You can also set the power value for a UPS to 0 if it does not supply any power to that system. This is generally used when you want to use the upsmon notification features for a UPS even though it&#8217;s not actually running the system that hosts upsmon. Don&#8217;t set this to &quot;master&quot; unless you really want to power this UPS off when this instance of upsmon needs to shut down for its own reasons. </p>
<p> MONITOR faraway [at] anotherbox 0 username mypassword slave </p>
<p> The &quot;minimum power value&quot; is the number of power supplies that must be receiving power in order to keep the computer running. </p>
<p> MINSUPPLIES <i>value</i> </p>
<p> Typical PCs only have 1, so most users will leave this at the default. </p>
<p> MINSUPPLIES 1 </p>
<p> If you have a server or similar system with redundant power, then this value will usually be set higher. One that requires three power supplies to be running at all times would simply set it to 3. </p>
<p> MINSUPPLIES 3 </p>
<p> When the current overall power value drops below the minimum power value, upsmon starts the shutdown sequence. This design allows you to lose some of your power supplies in a redundant power environment without bringing down the entire system while still working properly for smaller systems.</p>
<h2>Ups Types</h2>
<p><code>upsmon</code> and <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) don&#8217;t always run on the same system. When they do, any UPSes that are directly attached to the upsmon host should be monitored in &quot;master&quot; mode. This makes upsmon take charge of that equipment, and it will wait for slaves to disconnect before shutting down the local system. This allows the distant systems (monitoring over the network) to shut down cleanly before upsdrvctl shutdown runs and turns them all off. </p>
<p> When upsmon runs as a slave, it is relying on the distant system to tell it about the state of the UPS. When that UPS goes critical (on battery and low battery), it immediately invokes the local shutdown command. This needs to happen quickly. Once it disconnects from the distant <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) server, the master upsmon will start its own shutdown process. Your slaves must all shut down before the master turns off the power or filesystem damage may result. </p>
<p> upsmon deals with slaves that get wedged, hang, or otherwise fail to disconnect from <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8) in a timely manner with the HOSTSYNC timer. During a shutdown situation, the master upsmon will give up after this interval and it will shut down anyway. This keeps the master from sitting there forever (which would endanger that host) if a slave should break somehow. This defaults to 15 seconds. </p>
<p> If your master system is shutting down too quickly, set the FINALDELAY interval to something greater than the default 15 seconds. Don&#8217;t set this too high, or your UPS battery may run out of power before the master upsmon process shuts down that system.</p>
<h2>Timed Shutdowns</h2>
<p>For those rare situations where the shutdown process can&#8217;t be completed between the time that low battery is signalled and the UPS actually powers off the load, use the <code><a href="/docs/linux/man/8-upssched/">upssched</a></code>(8) helper program. You can use it along with upsmon to schedule a shutdown based on the &quot;on battery&quot; event. upssched can then come back to upsmon to initiate the shutdown once it has run on battery too long. </p>
<p> This can be complicated and messy, so stick to the default critical UPS handling if you can.</p>
<h2>Redundant Power Supplies</h2>
<p>If you have more than one power supply for redundant power, you may also have more than one UPS feeding your computer. upsmon can handle this. Be sure to set the UPS power values appropriately and the MINSUPPLIES value high enough so that it keeps running until it really does need to shut down. </p>
<p> For example, the HP NetServer LH4 by default has 3 power supplies installed, with one bay empty. It has two power cords, one per side of the box. This means that one power cord powers two power supply bays, and that you can only have two UPSes supplying power. </p>
<p> Connect UPS &quot;alpha&quot; to the cord feeding two power supplies, and UPS &quot;beta&quot; to the cord that feeds the third and the empty slot. Define alpha as a powervalue of 2, and beta as a powervalue of 1. Set the MINSUPPLIES to 2. </p>
<p> When alpha goes on battery, your current overall power value will stay at 3, as it&#8217;s still supplying power. However, once it goes critical (on battery and low battery), it will stop contributing to the current overall power value. That means the value will be 1 (beta alone), which is less than 2. That is insufficient to run the system, and upsmon will invoke the shutdown sequence. </p>
<p> However, if beta goes critical, subtracting its contribution will take the current overall value from 3 to 2. This is just high enough to satisfy the minimum, so the system will continue running as before. If beta returns later, it will be re-added and the current value will go back to 3. This allows you to swap out UPSes, change a power configuration, or whatever, as long as you maintain the minimum power value at all times.</p>
<h2>Mixed Operations</h2>
<p>Besides being able to monitor multiple UPSes, upsmon can also monitor them as different roles. If you have a system with multiple power supplies serviced by separate UPS batteries, it&#8217;s possible to be a master on one and a slave on the other. This usually happens when you run out of serial ports and need to do the monitoring through another system nearby. </p>
<p> This is also complicated, especially when it comes time to power down a UPS that has gone critical but doesn&#8217;t supply the local system. You can do this with some scripting magic in your notify command script, but it&#8217;s beyond the scope of this manual.</p>
<h2>Forced Shutdowns</h2>
<p>When upsmon is forced to bring down the local system, it sets the &quot;FSD&quot; (forced shutdown) flag on any UPSes that it is running in master mode. This is used to synchronize slaves in the event that a master UPS that is otherwise OK needs to be brought down due to some pressing event on the master. </p>
<p> You can manually invoke this mode on the master upsmon by starting another copy with -c fsd. This is useful when you want to initiate a shutdown before the critical stage through some external means, such as <code><a href="/docs/linux/man/8-upssched/">upssched</a></code>(8).</p>
<h2>Dead Upses</h2>
<p>In the event that upsmon can&#8217;t reach <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8), it declares that UPS &quot;dead&quot; after some interval controlled by DEADTIME in the <code><a href="/docs/linux/man/5-upsmon-conf/">upsmon.conf</a></code>(5). If this happens while that UPS was last known to be on battery, it is assumed to have gone critical and no longer contributes to the overall power value. </p>
<p> upsmon will alert you to a UPS that can&#8217;t be contacted for monitoring with a &quot;NOCOMM&quot; notifier by default every 300 seconds. This can be changed with the NOCOMMWARNTIME setting.</p>
<h2>Reloading Nuances</h2>
<p>upsmon usually gives up root powers for the process that does most of the work, including handling signals like SIGHUP to reload the configuration file. This means your <code><a href="/docs/linux/man/8-upsmon-conf/">upsmon.conf</a></code>(8) file must be readable by the non-root account that upsmon switches to. </p>
<p> If you want reloads to work, upsmon must run as some user that has permissions to read the configuration file. I recommend making a new user just for this purpose, as making the file readable by &quot;nobody&quot; (the default user) would be a bad idea. </p>
<p> See the RUN_AS_USER section in <code><a href="/docs/linux/man/8-upsmon-conf/">upsmon.conf</a></code>(8) for more on this topic. </p>
<p> Additionally, you can&#8217;t change the SHUTDOWNCMD or POWERDOWNFLAG definitions with a reload due to the split-process model. If you change those values, you <code>must</code> stop upsmon and start it back up. upsmon will warn you in the syslog if you make changes to either of those values during a reload.</p>
<h2>Simulating Power Failures</h2>
<p>To test a synchronized shutdown without pulling the plug on your UPS(es), you need only set the forced shutdown (FSD) flag on them. You can do this by calling upsmon again to set the flag, i.e.: </p>
<p> upsmon -c fsd </p>
<p> After that, the master and the slaves will do their usual shutdown sequence as if the battery had gone critical. This is much easier on your UPS equipment, and it beats crawling under a desk to find the plug.</p>
<h2>Files</h2>
<p><code><a href="/docs/linux/man/5-upsmon-conf/">upsmon.conf</a></code>(5)</p>
<h2>See Also</h2>
<h3>Server:</h3>
<p><code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8)</p>
<h3>Clients:</h3>
<p><code><a href="/docs/linux/man/8-upsc/">upsc</a></code>(8), <code><a href="/docs/linux/man/8-upscmd/">upscmd</a></code>(8), <code><a href="/docs/linux/man/8-upsrw/">upsrw</a></code>(8), <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8)</p>
<h3>CGI programs:</h3>
<p><code><a href="/docs/linux/man/8-upsset-cgi/">upsset.cgi</a></code>(8), <code><a href="/docs/linux/man/8-upsstats-cgi/">upsstats.cgi</a></code>(8), <code><a href="/docs/linux/man/8-upsimage-cgi/">upsimage.cgi</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
