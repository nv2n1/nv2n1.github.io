---
title: "script-email(8)"
name: "script-email"
section: "8"
letter: "s"
url: "/docs/linux/man/8-script-email/"
description: "script-email – Amanda script to send email notifications"
---

<p>script-email &#8211; Amanda script to send email notifications</p>
<h2>Description</h2>
<p>script-email is an Amanda script implementing the Script API. It should not be run by users directly. It sends a notification email to the addresses specified in the MAILTO property.</p>
<h2>Properties</h2>
<p>This section lists the properties that control script-email&#8217;s functionality. See <code><a href="/docs/linux/man/7-amanda-scripts/">amanda-scripts</a></code>(7) for information on the Script API, script configuration. </p>
<p> MAILTO</p>
<dl>
<dd>List of email addresses that will receive an email on command execution. It is a multi-valued property: </p>
<pre> property &quot;MAILTO&quot; &quot;amanda [at] domain.com&quot; &quot;sysadmin [at] domain.com&quot; &quot;amandauser [at] domain.com&quot;</pre>
</dl>
<h2>Example</h2>
<p>In this example, script-email is scheduled to be run before the DLE, on the server. The unqualified email address <i>amanda</i> will be passed to the email system unchanged. The script is then attached to a dumptype, which can then be specified for any DLEs which require notification. </p>
<pre> define script-tool pre-email {
 comment &quot;email me before this DLE is backed up&quot;
 plugin &quot;script-email&quot;
 execute-on pre-dle-backup
 execute-where server
 property &quot;mailto&quot; &quot;amanda&quot;
 }
 define dumptype user-tar-email {
 user-tar
 script &quot;pre-email&quot;
 }</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/5-amanda-conf/">amanda.conf</a></code>(5), <code><a href="/docs/linux/man/5-amanda-client-conf/">amanda-client.conf</a></code>(5), <code><a href="/docs/linux/man/7-amanda-scripts/">amanda-scripts</a></code>(7) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>Jean-Louis Martineau</code> &lt;martineau [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
<p> <code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
