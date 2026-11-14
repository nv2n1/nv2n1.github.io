---
title: "upssched(8)"
name: "upssched"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upssched/"
description: "upssched – Timer helper for scheduling events from upsmon"
---

<p>upssched &#8211; Timer helper for scheduling events from upsmon</p>
<h2>Synopsis</h2>
<p><code>upssched</code></p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 <code>upssched</code> should be run from <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) via the NOTIFYCMD. You should never run it directly during normal operations. </p>
<h2>Description</h2>
<p><code>upssched</code> was created to allow users to execute programs at times relative to events being monitored by <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8). The original purpose was to allow for a shutdown to occur after some fixed period on battery, but there are other uses that are possible.</p>
<h2>Integration</h2>
<p>upssched needs to be called as the NOTIFYCMD in your <code><a href="/docs/linux/man/5-upsmon-conf/">upsmon.conf</a></code>(5). It determines what is happening based on the UPSNAME and NOTIFYTYPE environment variables. You should never have to deal with them directly. </p>
<p> Set the EXEC flag on the events that you want to see in upssched. For example, to make sure that upssched hears about ONLINE, ONBATT and LOWBATT events, the flags would look like this: </p>
<dl>
<dd>
<pre>NOTIFYFLAG ONLINE EXEC
NOTIFYFLAG ONBATT EXEC
NOTIFYFLAG LOWBATT EXEC</pre>
</dl>
<p> If you also want to continue writing to the syslog, just add it in: </p>
<dl>
<dd>
<pre>NOTIFYFLAG ONLINE SYSLOG+EXEC
NOTIFYFLAG ONBATT SYSLOG+EXEC
NOTIFYFLAG LOWBATT SYSLOG+EXEC</pre>
</dl>
<p> For a full list of notify flags, see the <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) documentation.</p>
<h2>Configuration</h2>
<p>See <code><a href="/docs/linux/man/5-upssched-conf/">upssched.conf</a></code>(5) for information on configuring this program.</p>
<h2>Early Shutdowns</h2>
<p>To shut down the system early, define a timer that starts due to an ONBATT condition. When it triggers, make your CMDSCRIPT call your shutdown routine. It should finish by calling upsmon -c fsd so that upsmon gets to shut down the slaves in a controlled manner. </p>
<p> Be sure you cancel the timer if power returns (ONLINE).</p>
<h2>Debouncing Events</h2>
<p>If your UPS goes on and off battery frequently, you can use this program to reduce the number of pager messages that are sent out. Rather than sending pages directly from <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8), use a short timer here. If the timer triggers with the UPS still on battery, then send the page. If the power returns before then, the timer can be cancelled and no page is necessary.</p>
<h2>Background</h2>
<p>This program was written primarily to fulfill the requests of users for the early shutdown scenario. The &quot;outboard&quot; design of the program (relative to upsmon) was intended to reduce the load on the average system. Most people don&#8217;t have the requirement of shutting down after <i>N</i> seconds on battery, since the usual OB+LB testing is sufficient. </p>
<p> This program was created separately so those people don&#8217;t have to spend CPU time and RAM on something that will never be used in their environments. </p>
<p> The design of the timer handler is also geared towards minimizing impact. It will come and go from the process list as necessary. When a new timer is started, a process will be forked to actually watch the clock and eventually start the CMDSCRIPT. When a timer triggers, it is removed from the queue. Cancelling a timer will also remove it from the queue. When no timers are present in the queue, the background process exits. </p>
<p> This means that you will only see upssched running when one of two things is happening: </p>
<dl>
<dd>&bull; There&#8217;s a timer of some sort currently running</dl>
<dl>
<dd>&bull; upsmon just called it, and you managed to catch the brief instance</dl>
<p> The final optimization handles the possibility of trying to cancel a timer when there are none running. If the timer daemon isn&#8217;t running, there are no timers to cancel, and furthermore there is no need to start a clock-watcher. So, it skips that step and exits sooner.</p>
<h2>Files</h2>
<p><code><a href="/docs/linux/man/5-upssched-conf/">upssched.conf</a></code>(5)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
