---
title: "listen(7)"
name: "listen"
section: "7"
letter: "l"
url: "/docs/linux/man/7-listen/"
description: "LISTEN – listen for a notification"
---

<p>LISTEN &#8211; listen for a notification </p>
<h2>Synopsis</h2>
<pre>LISTEN <i>name</i></pre>
<h2>Description</h2>
<p><code>LISTEN</code> registers the current session as a listener on the notification condition <i>name</i>. If the current session is already registered as a listener for this notification condition, nothing is done. </p>
<p> Whenever the command <code>NOTIFY </code><i>name</i> is invoked, either by this session or another one connected to the same database, all the sessions currently listening on that notification condition are notified, and each will in turn notify its connected client application. See the discussion of <code>NOTIFY</code> for more information. </p>
<p> A session can be unregistered for a given notify condition with the <code>UNLISTEN</code> command. A session&#8217;s listen registrations are automatically cleared when the session ends. </p>
<p> The method a client application must use to detect notification events depends on which PostgreSQL application programming interface it uses. With the <code>libpq</code> library, the application issues <code>LISTEN</code> as an ordinary SQL command, and then must periodically call the function <code>PQnotifies</code> to find out whether any notification events have been received. Other interfaces such as <code>libpgtcl</code> provide higher-level methods for handling notify events; indeed, with <code>libpgtcl</code> the application programmer should not even issue <code>LISTEN</code> or <code>UNLISTEN</code> directly. See the documentation for the interface you are using for more details. </p>
<p> NOTIFY [<code><a href="/docs/linux/man/7-notify/">notify</a></code>(7)] contains a more extensive discussion of the use of <code>LISTEN</code> and <code>NOTIFY</code>.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>Name of a notify condition (any identifier).</dl>
<h2>Examples</h2>
<p>Configure and execute a listen/notify sequence from <code>psql</code>: </p>
<pre>LISTEN virtual;
NOTIFY virtual;
Asynchronous notification &quot;virtual&quot; received from server process with PID 8448.</pre>
<h2>Compatibility</h2>
<p>There is no <code>LISTEN</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>NOTIFY [<code><a href="/docs/linux/man/7-notify/">notify</a></code>(7)], UNLISTEN [<code><a href="/docs/linux/man/7-unlisten/">unlisten</a></code>(7)] </p>
