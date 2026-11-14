---
title: "bannergrab(1)"
name: "bannergrab"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bannergrab/"
description: "bannergrab – a network service banner grabbing tool"
---

<h2>NAME</h2>
<p> bannergrab &#8211; a network service banner grabbing tool</p>
<h2>SYNOPSIS</h2>
<p> <code>bannergrab</code> [<i>options</i>]<i> host port</i></p>
<h2>DESCRIPTION</h2>
<p> bannergrab performs connection, trigger and basic service information collection. There are basic banner grabbing modes, the first mode (the default one) sends triggers to the services and performs basic information collection. The second mode (&#8211;no-triggers), only connects to the service and returns the connection banner.<br />
 By default, if bannergrab has a trigger for the port number that is specified, the trigger for that port is used. If no trigger is listed for a port, the default one is used. No attempt is made to determine the type of service operating on a port.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>
 Show summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version of program.</p>
<dt><code>&#8211;show-triggers</code></p>
<dd> Lists the triggers used by bannergrab.</p>
<dt><code>&#8211;trigger=&lt;trigger&gt;</code></p>
<dd> Specify the trigger to use. Specify DEFAULT to use the default trigger.</p>
<dt><code>&#8211;no-triggers</code></p>
<dd> Collect only the connection banner, no triggers are sent and no SSL.</p>
<dt><code>&#8211;udp</code></p>
<dd>
 Connect to a port using UDP. The default is to use TCP.</p>
<dt><code>&#8211;no-ssl</code></p>
<dd>
 Prevent SSL connection creation.</p>
<dt><code>&#8211;no-hex</code></p>
<dd> Output containing non-printable characters are converted to hex. This option prevents the conversion.</p>
<dt><code>&#8211;conn-time=&lt;secs&gt;</code></p>
<dd> Connection timeout (default is 5s).</p>
<dt><code>&#8211;read-time=&lt;secs&gt;</code></p>
<dd> Read timeout (default is 3s).</p>
<dt><code>&#8211;verbose</code></p>
<dd> Show additional program details such as any errors.
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>bannergrab 127.0.0.1 80</p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> bannergrab was written by Ian Ventura-Whiting &lt;fizz [at] titania.co.uk&gt;. </p>
<h2>Index</h2>
