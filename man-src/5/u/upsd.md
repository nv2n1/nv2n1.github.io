---
title: "upsd(5)"
name: "upsd"
section: "5"
letter: "u"
url: "/docs/linux/man/5-upsd/"
description: "upsd.users – Administrative user definitions for NUT upsd"
---

<p>upsd.users &#8211; Administrative user definitions for NUT upsd </p>
<h2>Description</h2>
<p>Administrative commands such as setting variables and the instant commands are powerful, and access to them needs to be restricted. This file defines who may access them, and what is available. Each user gets its own section. The fields in that section set the parameters associated with that user&#8217;s privileges. The section begins with the name of the user in brackets, and continues until the next user name in brackets or EOF. Here are some examples to get you started:</p>
<dl>
<dd>
<pre> [admin]
 password = mypass
 actions = set
 instcmds = all
 [pfy]
 password = duh
 instcmds = test.panel.start
 [monmaster]
 password = blah
 upsmon master
 [monslave]
 password = abcd
 upsmon slave</pre>
</dl>
<h2>Fields</h2>
<dl>
<dt>password</p>
<dd>Set the password for this user. </p>
<dt>actions</p>
<dd>Allow the user to do certain things with upsd. Valid actions are: </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>SET &#8211; change the value of certain variables in the UPS</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>FSD &#8211; set the forced shutdown flag in the UPS. This is<br />
 equivalent to an &quot;on battery + low battery&quot; situation for the purposes of monitoring. </p>
<p> The list of actions is expected to grow in the future. </p>
<dt>instcmds</p>
<dd>Let a user initiate specific instant commands. Use &quot;ALL&quot; to grant all commands automatically. For the full list of what your UPS supports, use &quot;upscmd -l&quot;. </p>
<p> The <code>cmdvartab</code> file supplied with the distribution contains a list of most of the known command names. </p>
<dt>upsmon</p>
<dd>Add the necessary actions for a upsmon process to work. This is either set to &quot;master&quot; or &quot;slave&quot;. </p>
<p> Do not attempt to assign actions to upsmon by hand, as you may miss something important. This method of designating a &quot;upsmon user&quot; was created so internal capabilities could be changed later on without breaking existing installations. </p>
</dl>
<h2>Upgrading From Older Versions</h2>
<p>The <i>allowfrom</i> mechanism that existed in versions before nut-2.4.0 has been replaced by tcp-wrappers. Further details are described in <code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-upsd/">upsd</a></code>(8), <code><a href="/docs/linux/man/5-upsd-conf/">upsd.conf</a></code>(5)</p>
<h3>Internet resources:</h3>
<p>The NUT (Network UPS Tools) home page: <a rel="nofollow" href="http://www.networkupstools.org/">http://www.networkupstools.org/</a> </p>
