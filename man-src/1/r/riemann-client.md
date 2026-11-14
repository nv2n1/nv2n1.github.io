---
title: "riemann-client(1)"
name: "riemann-client"
section: "1"
letter: "r"
url: "/docs/linux/man/1-riemann-client/"
description: "riemann-client – Riemann communication tool"
---

<h2 class="name">NAME</h2>
<p> <code>riemann-client</code> &#8211; Riemann communication tool</p>
<h2>SYNOPSIS</h2>
<p> <code>riemann-client</code> <code>query</code> [<i>OPTIONS</i>&#8230;] <i>QUERY</i> [<i>HOST</i>] [<i>PORT</i>]<br />
 <code>riemann-client</code> <code>send</code> [<i>OPTIONS</i>&#8230;] [<i>HOST</i>] [<i>PORT</i>]<br />
 <code>riemann-client</code> <code>&#8211;help</code>|<code>-?</code><br />
 <code>riemann-client</code> <code>&#8211;version</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>riemann-client</code> is a very simple tool to faciliate communication with a Riemann event stream processing server. It can be used both for sending events to one, and to query it too. </p>
<h2>OPTIONS</h2>
<p> In both <code>query</code> and <code>send</code> mode, <i>HOST</i> and <i>PORT</i> default to <i>localhost</i> and <i>5555</i>, respectively. </p>
<h3>Query mode</h3>
<p> In query mode, <code>riemann-client</code> takes one mandatory argument: the query itself. It must be a single argument, which will be sent to Riemann as-is, and the response dumped to the standard output, or, in case of an error, the error message will be written to the standard error. </p>
<p> See the Riemann documentation <i><a rel="nofollow" href="http://riemann.io/concepts.html">http://riemann.io/concepts.html</a></i> for more information about the query syntax. </p>
<p> Apart from the mandatory argument, the <code>riemann-client</code> accepts the following options in query mode: </p>
<dl>
<dt><code>-j</code>, <code>&#8211;json</code></p>
<dd> Print the result in JSON format, instead of the default, human-readable one. </p>
<dt><code>-T</code>, <code>&#8211;tcp</code></p>
<dd> Send the event via TCP (the default). </p>
<dt><code>-G</code>, <code>&#8211;tls</code></p>
<dd> Send the event via TLS. </p>
<dt><code>-o</code>, <code>&#8211;option</code> <i>option</i>=<i>value</i></p>
<dd> Set one client option to the given value. </p>
<p> Available client options are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cafile</code></p>
<dd> Path to the file containing trusted certificate authority certificates. Only used for TLS connections. </p>
<dt><code>certfile</code></p>
<dd> Path to the file containing the public client certificate. Only used for TLS connections. </p>
<dt><code>keyfile</code></p>
<dd> Path to the file containing the private client key. Only used for TLS connections.</dl>
</dl>
</dl>
<h3>Submit mode</h3>
<p> In submit mode, <code>riemann-client</code> accepts the following options: </p>
<dl>
<dt><code>-s</code>, <code>&#8211;state</code> <i>STATE</i></p>
<dd> The state the event should describe, free-form text, optional. </p>
<dt><code>-S</code>, <code>&#8211;service</code> <i>SERVICE</i></p>
<dd> The service the event is coming from. </p>
<dt><code>-h</code>, <code>&#8211;host</code> <i>HOST</i></p>
<dd> The host the event originates from. Not to be confused with the optional <i>HOST</i> parameter of <code>riemann-client</code> itself, which sets where to send the events to. </p>
<dt><code>-D</code>, <code>&#8211;description</code> <i>DESCRIPTION</i></p>
<dd> The description of the event, optional. </p>
<dt><code>-t</code>, <code>&#8211;tag</code> <i>TAG</i></p>
<dd> This option can be used multiple times to add tags to the event. </p>
<dt><code>-a</code>, <code>&#8211;attribute</code> <i>NAME</i>=<i>VALUE</i></p>
<dd> This option can be used multiple times to add custom attributes to the event. </p>
<dt><code>-i</code>, <code>&#8211;metric-sint64</code> <i>METRIC</i></p>
<dd> Sets the metric for the event, using integer precision. </p>
<dt><code>-d</code>, <code>&#8211;metric-d</code> <i>METRIC</i></p>
<dd> Sets the metric of the event, using double precision. </p>
<dt><code>-f</code>, <code>&#8211;metric-f</code> <i>METRIC</i></p>
<dd> Sets the metric of the event, using floating point precision. </p>
<dt><code>-L</code>, <code>&#8211;ttl</code> <i>TTL</i></p>
<dd> An optional time-to-live of the event, in seconds (floating point number). </p>
<dt><code>-T</code>, <code>&#8211;tcp</code></p>
<dd> Send the event via TCP (the default). </p>
<dt><code>-U</code>, <code>&#8211;udp</code></p>
<dd> Send the event via UDP. </p>
<dt><code>-G</code>, <code>&#8211;tls</code></p>
<dd> Send the event via TLS. </p>
<dt><code>-o</code>, <code>&#8211;option</code> <i>option</i>=<i>value</i></p>
<dd> Set one client option to the given value. </p>
<p> Available client options are: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>cafile</code></p>
<dd> Path to the file containing trusted certificate authority certificates. Only used for TLS connections. </p>
<dt><code>certfile</code></p>
<dd> Path to the file containing the public client certificate. Only used for TLS connections. </p>
<dt><code>keyfile</code></p>
<dd> Path to the file containing the private client key. Only used for TLS connections.</dl>
</dl>
</dl>
<h2>EXAMPLES</h2>
<h3>Sending an event</h3>
<pre><code>
$ riemann - client send-- state ok-- service "client-test" --host "my-host" --description "A message from the Manual" --tag tag - 1 --tag tag - 2 --attribute x - manual = best - friend --metric - sint64 1 --ttl 300.5 --tcp
</code></pre>
<h3>Querying Riemann</h3>
<pre>
$ riemann-client query 'host = &quot;my-host&quot;'
</pre>
<h2>AUTHOR</h2>
<p> Gergely Nagy <i>algernon [at] madhouse-project.org</i> </p>
<h2>Index</h2>
