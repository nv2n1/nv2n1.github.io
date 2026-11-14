---
title: "notify(7)"
name: "notify"
section: "7"
letter: "n"
url: "/docs/linux/man/7-notify/"
description: "NOTIFY – generate a notification"
---

<p>NOTIFY &#8211; generate a notification </p>
<h2>Synopsis</h2>
<pre>NOTIFY <i>name</i> </pre>
<h2>Description</h2>
<p>The <code>NOTIFY</code> command sends a notification event to each client application that has previously executed <code>LISTEN </code><i>name</i> for the specified notification name in the current database. </p>
<p> <code>NOTIFY</code> provides a simple form of signal or interprocess communication mechanism for a collection of processes accessing the same PostgreSQL database. Higher-level mechanisms can be built by using tables in the database to pass additional data (beyond a mere notification name) from notifier to listener(s). </p>
<p> The information passed to the client for a notification event includes the notification name and the notifying session&#8217;s server process PID. It is up to the database designer to define the notification names that will be used in a given database and what each one means. </p>
<p> Commonly, the notification name is the same as the name of some table in the database, and the notify event essentially means, &#8220;I changed this table, take a look at it to see what&#8217;s new&#8221;. But no such association is enforced by the <code>NOTIFY</code> and <code>LISTEN</code> commands. For example, a database designer could use several different notification names to signal different sorts of changes to a single table. </p>
<p> When <code>NOTIFY</code> is used to signal the occurrence of changes to a particular table, a useful programming technique is to put the <code>NOTIFY</code> in a rule that is triggered by table updates. In this way, notification happens automatically when the table is changed, and the application programmer cannot accidentally forget to do it. </p>
<p> <code>NOTIFY</code> interacts with SQL transactions in some important ways. Firstly, if a <code>NOTIFY</code> is executed inside a transaction, the notify events are not delivered until and unless the transaction is committed. This is appropriate, since if the transaction is aborted, all the commands within it have had no effect, including <code>NOTIFY</code>. But it can be disconcerting if one is expecting the notification events to be delivered immediately. Secondly, if a listening session receives a notification signal while it is within a transaction, the notification event will not be delivered to its connected client until just after the transaction is completed (either committed or aborted). Again, the reasoning is that if a notification were delivered within a transaction that was later aborted, one would want the notification to be undone somehow &#8212; but the server cannot &#8220;take back&#8221; a notification once it has sent it to the client. So notification events are only delivered between transactions. The upshot of this is that applications using <code>NOTIFY</code> for real-time signaling should try to keep their transactions short. </p>
<p> <code>NOTIFY</code> behaves like Unix signals in one important respect: if the same notification name is signaled multiple times in quick succession, recipients might get only one notification event for several executions of <code>NOTIFY</code>. So it is a bad idea to depend on the number of notifications received. Instead, use <code>NOTIFY</code> to wake up applications that need to pay attention to something, and use a database object (such as a sequence) to keep track of what happened or how many times it happened. </p>
<p> It is common for a client that executes <code>NOTIFY</code> to be listening on the same notification name itself. In that case it will get back a notification event, just like all the other listening sessions. Depending on the application logic, this could result in useless work, for example, reading a database table to find the same updates that that session just wrote out. It is possible to avoid such extra work by noticing whether the notifying session&#8217;s server process PID (supplied in the notification event message) is the same as one&#8217;s own session&#8217;s PID (available from <code>libpq</code>). When they are the same, the notification event is one&#8217;s own work bouncing back, and can be ignored. (Despite what was said in the preceding paragraph, this is a safe technique. PostgreSQL keeps self-notifications separate from notifications arriving from other sessions, so you cannot miss an outside notification by ignoring your own notifications.)</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>Name of the notification to be signaled (any identifier).</dl>
<h2>Examples</h2>
<p>Configure and execute a listen/notify sequence from <code>psql</code>: </p>
<pre>LISTEN virtual;
NOTIFY virtual;
Asynchronous notification &quot;virtual&quot; received from server process with PID 8448.</pre>
<h2>Compatibility</h2>
<p>There is no <code>NOTIFY</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>LISTEN [<code><a href="/docs/linux/man/7-listen/">listen</a></code>(7)], UNLISTEN [<code><a href="/docs/linux/man/7-unlisten/">unlisten</a></code>(7)] </p>
