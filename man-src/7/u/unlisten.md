---
title: "unlisten(7)"
name: "unlisten"
section: "7"
letter: "u"
url: "/docs/linux/man/7-unlisten/"
description: "UNLISTEN – stop listening for a notification"
---

<p>UNLISTEN &#8211; stop listening for a notification </p>
<h2>Synopsis</h2>
<pre>UNLISTEN { <i>name</i> | * }</pre>
<h2>Description</h2>
<p><code>UNLISTEN</code> is used to remove an existing registration for <code>NOTIFY</code> events. <code>UNLISTEN</code> cancels any existing registration of the current PostgreSQL session as a listener on the notification <i>name</i>. The special wildcard * cancels all listener registrations for the current session. </p>
<p> NOTIFY [<code><a href="/docs/linux/man/7-notify/">notify</a></code>(7)] contains a more extensive discussion of the use of <code>LISTEN</code> and <code>NOTIFY</code>.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>Name of a notification (any identifier).</p>
<dt><code>*</code></p>
<dd>All current listen registrations for this session are cleared.</dl>
<h2>Notes</h2>
<p>You can unlisten something you were not listening for; no warning or error will appear. </p>
<p> At the end of each session, <code>UNLISTEN *</code> is automatically executed.</p>
<h2>Examples</h2>
<p>To make a registration: </p>
<pre>LISTEN virtual;
NOTIFY virtual;
Asynchronous notification &quot;virtual&quot; received from server process with PID 8448.</pre>
<p>Once <code>UNLISTEN</code> has been executed, further <code>NOTIFY</code> commands will be ignored: </p>
<pre>UNLISTEN virtual;
NOTIFY virtual;
-- no NOTIFY event is received</pre>
<h2>Compatibility</h2>
<p>There is no <code>UNLISTEN</code> command in the SQL standard.</p>
<h2>See Also</h2>
<p>LISTEN [<code><a href="/docs/linux/man/7-listen/">listen</a></code>(7)], NOTIFY [<code><a href="/docs/linux/man/7-notify/">notify</a></code>(7)] </p>
