---
title: "poundctl(8)"
name: "poundctl"
section: "8"
letter: "p"
url: "/docs/linux/man/8-poundctl/"
description: "poundctl – control the pound(8) daemon"
---

<p>poundctl &#8211; control the <a href="/docs/linux/man/8-pound/">pound</a>(8) daemon</p>
<h2>Synopsis</h2>
<dl>
<dt><code>poundctl </code><i>-c /path/to/socket</i> [<i>-L/-l</i>] [<i>-S/-s</i>] [<i>-B/-b</i>] [<i>-N/-n</i>] [<i>-H</i>] [<i>-X</i>]</p>
<dd></dl>
<h2>Description</h2>
<p><code>Poundctl</code> controls various aspects of the operation of the <i><a href="/docs/linux/man/8-pound/">pound</a>(8)</i> program.</p>
<h2>Options</h2>
<p>Options available:</p>
<dl>
<dt><code>-c /path/to/socket</code></p>
<dd>The path to the (Unix-domain) socket <code>Pound</code> was configured to listen on for control. Your <code>Pound</code> configuration file must contain the directive <i>Control /path/to/socket</i> for <code>poundctl</code> to work.</p>
<dt><code>-L/-l n</code></p>
<dd>Enable/disable a listener. A disabled listener will stop accepting connection requests.</p>
<dt><code>-S/-s n m</code></p>
<dd>Enable/disable a service. A disabled service will not be used by <code>Pound</code> to answer requests.</p>
<dt><code>-B/-b n m r</code></p>
<dd>Enable/disable a back-end. A disabled back-end will not be passed requests to answer. Note however that existing sessions may still cause requests to be sent their way.</p>
<dt><code>-N n m k r</code></p>
<dd>Add a session to service m in listener n. The session key is k and it points to back-end r.</p>
<dt><code>-n n m k</code></p>
<dd>Remove a session from service m in listener n. The session key is k.</dl>
<p> The parameters n, m and r refer to the number assigned to a particular listener, service and back-end in the listings. A listener number of -1 refers by convention to the global context.</p>
<dl>
<dt><code>-H</code></p>
<dd>Try to resolve the addresses to symbolic names. Depending on your configuration, this may require an active DNS.</p>
<dt><code>-X</code></p>
<dd>Show the results in XML format.</dl>
<p> When called without flags <code>poundctl</code> will print out a listing of the <code>Pound</code> internal state.</p>
<h2>Author</h2>
<p>Written by Robert Segall, Apsis GmbH.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;roseg [at] apsis.ch&gt;.</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2002-2010 Apsis GmbH.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
