---
title: "upssched(5)"
name: "upssched"
section: "5"
letter: "u"
url: "/docs/linux/man/5-upssched/"
description: "upssched.conf – Configuration for upssched timer program"
---

<p>upssched.conf &#8211; Configuration for upssched timer program </p>
<h2>Description</h2>
<p>This file controls the operations of <code><a href="/docs/linux/man/8-upssched/">upssched</a></code>(8), the timer-based helper program for <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8). </p>
<h2>Configuration Directives</h2>
<dl>
<dt>CMDSCRIPT <i>scriptname</i></p>
<dd>Required. This must be above any AT lines. This script is used to invoke commands when your timers are triggered. It receives a single argument which is the name of the timer that caused it to trigger. </p>
<dt>PIPEFN <i>filename</i></p>
<dd>Required. This sets the file name of the socket which will be used for interprocess communications. This should be in a directory where normal users can&#8217;t create the file, due to the possibility of symlinking and other evil.</p>
<dd>Note: if you are running Solaris or similar, the permissions that upssched sets on this file <code>are not enough</code> to keep you safe. If your OS ignores the permissions on a FIFO, then you MUST put this in a protected directory!</p>
<dd>Note 2: by default, <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8) will run upssched as whatever user you have defined with RUN_AS_USER in <code><a href="/docs/linux/man/8-upsmon-conf/">upsmon.conf</a></code>(8). Make sure that user can create files and write to files in the path you use for PIPEFN and LOCKFN.</p>
<dd>My recommendation: create a special directory for upssched, make it owned by your upsmon user, then use it for both.</p>
<dd>The stock version of the upssched.conf ships with PIPEFN disabled to make you visit this portion of the documentation and think about how your system works before potentially opening a security hole. </p>
<dt>LOCKFN <i>filename</i></p>
<dd>Required. upssched attempts to create this file in order to avoid a race condition when two events are dispatched from upsmon at nearly the same time. This file will only exist briefly. It must not be created by any other process.</p>
<dd>You should put this in the same directory as PIPEFN. </p>
<dt>AT <i>notifytype</i> <i>upsname</i> <i>command</i></p>
<dd>Define a handler for a specific event <i>notifytype</i> on UPS <i>upsname</i>. <i>upsname</i> can be the special value * to apply this handler to every UPS.</p>
<dd>This will perform the command <i>command</i> when the <i>notifytype</i> and <i>upsname</i> match the current activity. Possible values for <i>command</i> are:</p>
<dd>START-TIMER <i>timername</i> <i>interval</i></p>
<dd>
<pre> Start a timer of <i>interval</i> seconds. When it triggers, it
 will pass the argument <i>timername</i> as an argument to your
 CMDSCRIPT.</pre>
</dl>
<dl>
<dd>Example:</p>
<dd>
<pre> Start a timer that'll execute when any UPS (*) has been
 gone for 10 seconds
 AT COMMBAD * START-TIMER upsgone 10</pre>
</dl>
<dl>
<dd>CANCEL-TIMER <i>timername</i> [cmd]</p>
<dd>
<pre> Cancel a running timer called &lt;timername&gt;, if possible.
 If the timer has passed then pass the optional argument
 &lt;cmd&gt; to CMDSCRIPT.</pre>
</dl>
<dl>
<dd>Example:</p>
<dd>
<pre> If a specific UPS (myups [at] localhost) comes back online, then
 stop the timer before it triggers
 AT COMMOK myups [at] localhost CANCEL-TIMER upsgone</pre>
</dl>
<dl>
<dd>EXECUTE <i>command</i></p>
<dd>
<pre> Immediately pass &lt;command&gt; as an argument to CMDSCRIPT.</pre>
</dl>
<dl>
<dd>Example:</p>
<dd>
<pre> If any UPS (*) reverts to utility power, then execute
 'ups-back-on-line' via CMDSCRIPT.
 AT ONLINE * EXECUTE ups-back-on-line</pre>
</dl>
<dl>
<dd>Note that any AT that matches both the <i>notifytype</i> and the <i>upsname</i> for the current event will be used. </p>
<p> For a complete list of <i>notifytype</i> possible values, refer to the section NOTIFY EVENTS in <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8). </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-upssched/">upssched</a></code>(8), <code><a href="/docs/linux/man/8-upsmon/">upsmon</a></code>(8)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
