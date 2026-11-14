---
title: "smtpctl(8)"
name: "smtpctl"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smtpctl/"
description: "smtpctl, mailq – control the Simple Mail Transfer Protocol daemon"
---

<p><code>smtpctl</code>, <code>mailq</code> &#8211; control the Simple Mail Transfer Protocol daemon</p>
<h2>Synopsis</h2>
<p><code>smtpctl</code> <i>command</i> [<i>argument</i> &#8230;]<br />
 <code>mailq</code></p>
<h2>Description</h2>
<p>The <code>smtpctl</code> program controls <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8). Commands may be abbreviated to the minimum unambiguous prefix; for example, <code>sh</code> ro for <code>show</code> routes. </p>
<p> The <code>mailq</code> command is provided for compatibility with other MTAs and is simply a shortcut for <code>show</code> queue. </p>
<p> The following commands are available:</p>
<dl>
<dd>
<dl>
<dt><code>discover</code> <i>envelope-id</i> | message-id</p>
<dd>Schedule a single envelope, or all envelopes with the same message ID that were manually moved to the queue.</p>
<dt><code>encrypt</code> [<i>string</i>]</p>
<dd>Encrypt the password <i>string</i> to a representation suitable for user credentials and print it to the standard output. If <i>string</i> is not provided, cleartext passwords are read from standard input.</dl>
<p> It is advised to avoid providing the password as a parameter as it will be visible from <code><a href="/docs/linux/man/1-top/">top</a></code>(1) and <code><a href="/docs/linux/man/1-ps/">ps</a></code>(1) output.</p>
<dl>
<dt><code>log</code> brief</p>
<dd>Disable verbose debug logging.</p>
<dt><code>log</code> verbose</p>
<dd>Enable verbose debug logging.</p>
<dt><code>monitor</code></p>
<dd>Display updates of some <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) internal counters in one second intervals. Each line reports the increment of all counters since the last update, except for some counters which are always absolute values. The first line reports the current value of each counter. The fields are:</dl>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Current number of active SMTP clients (absolute value).</p>
<dt>&bull;</p>
<dd>New SMTP clients.</p>
<dt>&bull;</p>
<dd>Disconnected clients.</p>
<dt>&bull;</p>
<dd>Current number of envelopes in the queue (absolute value).</p>
<dt>&bull;</p>
<dd>Newly enqueued envelopes.</p>
<dt>&bull;</p>
<dd>Dequeued envelopes.</p>
<dt>&bull;</p>
<dd>Successful deliveries.</p>
<dt>&bull;</p>
<dd>Temporary failures.</p>
<dt>&bull;</p>
<dd>Permanent failures.</p>
<dt>&bull;</p>
<dd>Message loops.</p>
<dt>&bull;</p>
<dd>Expired envelopes.</p>
<dt>&bull;</p>
<dd>Envelopes removed by the administrator.</p>
<dt>&bull;</p>
<dd>Generated bounces.</dl>
</dl>
<dl>
<dt><code>pause</code> envelope <i>envelope-id</i> | message-id</p>
<dd>Temporarily suspend scheduling for the envelope with the given ID, or all envelopes with the given message ID.</p>
<dt><code>pause</code> envelope all</p>
<dd>Temporarily suspend scheduling all the envelopes.</p>
<dt><code>pause</code> mda</p>
<dd>Temporarily stop deliveries to local users.</p>
<dt><code>pause</code> mta</p>
<dd>Temporarily stop relaying and deliveries to remote users.</p>
<dt><code>pause</code> smtp</p>
<dd>Temporarily stop accepting incoming sessions.</p>
<dt><code>profile</code> <i>subsystem</i></p>
<dd>Enables real-time profiling of <i>subsystem</i>. Supported subsystems are:</dl>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>queue, to profile cost of queue IO</p>
<dt>&bull;</p>
<dd>imsg, to profile cost of event handlers</dl>
</dl>
<dl>
<dt><code>remove</code> <i>envelope-id</i> | message-id</p>
<dd>Remove a single envelope, or all envelopes with the same message ID.</p>
<dt><code>remove</code> all</p>
<dd>Remove all envelopes.</p>
<dt><code>resume</code> envelope <i>envelope-id</i> | message-id</p>
<dd>Resume scheduling for the envelope with the given ID, or all envelopes with the given message ID.</p>
<dt><code>resume</code> envelope all</p>
<dd>Resume scheduling all the envelopes.</p>
<dt><code>resume</code> mda</p>
<dd>Resume deliveries to local users.</p>
<dt><code>resume</code> mta</p>
<dd>Resume relaying and deliveries to remote users.</p>
<dt><code>resume</code> route <i>route-id</i></p>
<dd>Resume routing on disabled route <i>route-id</i>.</p>
<dt><code>resume</code> smtp</p>
<dd>Resume accepting incoming sessions.</p>
<dt><code>schedule</code> all</p>
<dd>Mark all envelopes as ready for immediate delivery.</p>
<dt><code>schedule</code> <i>envelope-id</i> | message-id</p>
<dd>Mark a single envelope, or all envelopes with the same message ID, as ready for immediate delivery.</p>
<dt><code>show</code> envelope <i>envelope-id</i></p>
<dd>Display envelope content for the given ID.</p>
<dt><code>show</code> hosts</p>
<dd>Display the list of known remote MX hosts. For each of them, it shows the IP address, the canonical hostname, a reference count, the number of active connections to this host, and the elapsed time since the last connection.</p>
<dt><code>show</code> hoststats</p>
<dd>Display status of last delivery for domains that have been active in the last 4 hours. It consists of the following fields, separated by a &quot;|&quot;:</dl>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Domain.</p>
<dt>&bull;</p>
<dd>Ux timestamp of last delivery.</p>
<dt>&bull;</p>
<dd>Status of last delivery.</dl>
</dl>
<dl>
<dt><code>show</code> message <i>envelope-id</i></p>
<dd>Display message content for the given ID.</p>
<dt><code>show</code> queue</p>
<dd>Display information concerning envelopes that are currently in the queue. Each line of output describes a single envelope. It consists of the following fields, separated by a &quot;|&quot;:</dl>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>Envelope ID.</p>
<dt>&bull;</p>
<dd>Address family of the client which enqueued the mail.</p>
<dt>&bull;</p>
<dd>Type of delivery: one of &quot;mta&quot;, &quot;mda&quot; or &quot;bounce&quot;.</p>
<dt>&bull;</p>
<dd>Various flags on the envelope.</p>
<dt>&bull;</p>
<dd>Sender address (return path).</p>
<dt>&bull;</p>
<dd>The original recipient address.</p>
<dt>&bull;</p>
<dd>The destination address.</p>
<dt>&bull;</p>
<dd>Time of creation.</p>
<dt>&bull;</p>
<dd>Time of expiration.</p>
<dt>&bull;</p>
<dd>Time of last delivery or relaying attempt.</p>
<dt>&bull;</p>
<dd>Number of delivery or relaying attempts.</p>
<dt>&bull;</p>
<dd>Current runstate: either &quot;pending&quot; or &quot;inflight&quot; if <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) is running, or &quot;offline&quot; otherwise.</p>
<dt>&bull;</p>
<dd>Delay in seconds before the next attempt if pending, or time ellapsed if currently running. This field is blank if <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) is not running.</p>
<dt>&bull;</p>
<dd>Error string for the last failed delivery or relay attempt.</dl>
</dl>
<dl>
<dt><code>show</code> relays</p>
<dd>Display the list of currently active relays and associated connectors. For each relay, it shows a number of counters and information on its internal state on a single line. Then comes the list of connectors (source addresses to connect from for this relay).</p>
<dt><code>show</code> routes</p>
<dd>Display status of routes currently known by <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8). Each line consists of a route number, a source address, a destination address, a set of flags, the number of connections on this route, the current penalty level which determines the amount of time the route is disabled if an error occurs, and the delay before it gets reactivated. The following flags are defined:</dl>
<dl>
<dd>
<dl>
<dt>D</p>
<dd>The route is currently disabled.</p>
<dt>N</p>
<dd>The route is new. No SMTP session has been established yet.</p>
<dt>Q</p>
<dd>The route has a timeout registered to lower its penalty level and possibly reactivate or discard it.</dl>
</dl>
<dl>
<dt><code>show</code> stats</p>
<dd>Displays runtime statistics concerning <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8).</p>
<dt><code>show</code> status</p>
<dd>Shows if MTA, MDA and SMTP systems are currently running or paused.</p>
<dt><code>stop</code></p>
<dd>Stop the server.</p>
<dt><code>trace</code> <i>subsystem</i></p>
<dd>Enables real-time tracing of <i>subsystem</i>. Supported subsystems are:</dl>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>imsg</p>
<dt>&bull;</p>
<dd>io</p>
<dt>&bull;</p>
<dd>smtp (incoming sessions)</p>
<dt>&bull;</p>
<dd>filters</p>
<dt>&bull;</p>
<dd>mta (outgoing sessions)</p>
<dt>&bull;</p>
<dd>bounce</p>
<dt>&bull;</p>
<dd>scheduler</p>
<dt>&bull;</p>
<dd>expand (aliases/virtual/forward expansion)</p>
<dt>&bull;</p>
<dd>lookup (user/credentials lookups)</p>
<dt>&bull;</p>
<dd>stat</p>
<dt>&bull;</p>
<dd>rules (matched by incoming sessions)</p>
<dt>&bull;</p>
<dd>mproc</p>
<dt>&bull;</p>
<dd>all</dl>
</dl>
<dl>
<dt><code>uncorrupt</code> <i>message-id</i></p>
<dd>Move all envelopes with the given message ID from corrupt bucket back to queue.</p>
<dt><code>unprofile</code> <i>subsystem</i></p>
<dd>Disables real-time profiling of <i>subsystem</i>.</p>
<dt><code>untrace</code> <i>subsystem</i></p>
<dd>Disables real-time tracing of <i>subsystem</i>.</p>
<dt><code>update</code> table <i>name</i></p>
<dd>For table backends that provide caching, causes <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8) to update the cache.</dl>
</dl>
<p> When <code>smtpd</code> receives a message, it generates a <i>message-id</i> for the message, and one <i>envelope-id</i> per recipient. The <i>message-id</i> is a 32-bit random identifier that is guaranteed to be unique on the host system. The <i>envelope-id</i> is a 64-bit unique identifier that encodes the <i>message-id</i> in the 32 upper bits and a random envelope identifier in the 32 lower bits. </p>
<p> A command which specifies a <i>message-id</i> applies to all recipients of a message; a command which specifies an <i>envelope-id</i> applies to a specific recipient of a message.</p>
<h2>Files</h2>
<dl>
<dd>
<dl>
<dt><code>/var/run/smtpd.sock</code></p>
<dd>Ux -domain socket used for communication with <code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8).</dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-smtpd/">smtpd</a></code>(8)</p>
<h2>History</h2>
<p>The <code>smtpctl</code> program first appeared in OpenBSD 4.6.</p>
