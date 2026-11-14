---
title: "upsd-users(5)"
name: "upsd-users"
section: "5"
letter: "u"
url: "/docs/linux/man/5-upsd-users/"
description: "upsd.users – Administrative user definitions for NUT upsd"
---

<p>upsd.users &#8211; Administrative user definitions for NUT upsd</p>
<h2>Description</h2>
<p>Administrative commands such as setting variables and the instant commands are powerful, and access to them needs to be restricted. This file defines who may access them, and what is available. </p>
<p> Each user gets its own section. The fields in that section set the parameters associated with that user&#8217;s privileges. The section begins with the name of the user in brackets, and continues until the next user name in brackets or EOF. These users are independent of /etc/passwd. </p>
<p> Here are some examples to get you started: </p>
<dl>
<dd>
<pre>[admin]
 password = mypass
 actions = set
 actions = fsd
 instcmds = all</pre>
</dl>
<dl>
<dd>
<pre>[pfy]
 password = duh
 instcmds = test.panel.start
 instcmds = test.panel.stop</pre>
</dl>
<dl>
<dd>
<pre>[monmaster]
 password = blah
 upsmon master</pre>
</dl>
<dl>
<dd>
<pre>[monslave]
 password = abcd
 upsmon slave</pre>
</dl>
<h2>Fields</h2>
<p><code>password</code></p>
<dl>
<dd>Set the password for this user.</dl>
<p> <code>actions</code></p>
<dl>
<dd>Allow the user to do certain things with upsd. To specify multiple actions, use multiple instances of the <code>actions</code> field. Valid actions are: </p>
<p> SET</p>
<dl>
<dd>change the value of certain variables in the UPS</dl>
<p> FSD</p>
<dl>
<dd>set the forced shutdown flag in the UPS. This is equivalent to an &quot;on battery + low battery&quot; situation for the purposes of monitoring.</dl>
</dl>
<p> The list of actions is expected to grow in the future. </p>
<p> <code>instcmds</code></p>
<dl>
<dd>Let a user initiate specific instant commands. Use &quot;ALL&quot; to grant all commands automatically. To specify multiple commands, use multiple instances of the <code>instcmds</code> field. For the full list of what your UPS supports, use &quot;upscmd -l&quot;. </p>
<p> The cmdvartab file supplied with the distribution contains a list of most of the known command names.</dl>
<p> <code>upsmon</code></p>
<dl>
<dd>Add the necessary actions for a upsmon process to work. This is either set to &quot;master&quot; or &quot;slave&quot;. </p>
<p> Do not attempt to assign actions to upsmon by hand, as you may miss something important. This method of designating a &quot;upsmon user&quot; was created so internal capabilities could be changed later on without breaking existing installations.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8), <code><a href="/docs/linux/man/5-upsd-conf/">upsd.conf</a></code>(5)</p>
<h2>Internet Resources</h2>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a></p>
