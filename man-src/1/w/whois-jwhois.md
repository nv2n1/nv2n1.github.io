---
title: "whois-jwhois(1)"
name: "whois-jwhois"
section: "1"
letter: "w"
url: "/docs/linux/man/1-whois-jwhois/"
description: "jwhois – client for the whois service"
---

<p>jwhois &#8211; client for the whois service</p>
<h2>Synopsis</h2>
<p><code>jwhois</code> [ <i>OPTIONS</i> ]&#8230; [ <i>QUERY</i> ]</p>
<h2>Description</h2>
<p><i>jwhois</i> searches Whois servers for the object on the command line. </p>
<p> The host to query is taken from a global configuration file, a configuration file specified on the command line, or selected directly on the command line. </p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>&#8211;version</code></p>
<dd>display version, authors and licensing information.</p>
<dt><code>&#8211;help</code></p>
<dd>display a short help text.</p>
<dt><code>-c FILE &#8211;config=FILE</code></p>
<dd>uses FILE as a configuration file instead of the default.</p>
<dt><code>-h HOST &#8211;host=HOST</code></p>
<dd>overrides any hosts in the configuration file and queries HOST directly.</p>
<dt><code>-p PORT &#8211;port=PORT</code></p>
<dd>specifies a port number to use when querying a HOST.</p>
<dt><code>-f &#8211;force-lookup</code></p>
<dd>forces a query to be made to a host even if a current object is available from the cache.</p>
<dt><code>-v &#8211;verbose</code></p>
<dd>outputs verbose debugging information while running (use this before sending a bugreport to ensure that it&#8217;s indeed a bug and not a misconfiguration). You can increase the verbosity by giving several verbose commands to jwhois, such as -vv.</p>
<dt><code>-n &#8211;no-redirect</code></p>
<dd>disable features that redirect queries from one server to another.</p>
<dt><code>-s &#8211;no-whoisservers</code></p>
<dd>disable the built-in support for whois-servers.net.</p>
<dt><code>-a &#8211;raw</code></p>
<dd>send query verbatim to receiving hosts instead of rewriting them according to the configuration.</p>
<dt><code>-i &#8211;display-redirections</code></p>
<dd>display every step in a redirection (default is to display only the last answer).</p>
<dt><code>-d &#8211;disable-cache</code></p>
<dd>completely disable both reading and writing to cache.</p>
<dt><code>-r &#8211;rwhois</code></p>
<dd>force the query to use the rwhois protocoll instead of HTTP or whois.</p>
<dt><code>&#8211;rwhois-display=DISPLAY</code></p>
<dd>asks receiving rwhois servers to display the results in the DISPLAY display instead of the default dump display.</p>
<dt><code>&#8211;rwhois-limit=LIMIT</code></p>
<dd>asks receiving rwhois servers to limit their responses to LIMIT matches. </p>
</dl>
<h3>Ripe Extensions</h3>
<p>To use the options specified in <i>RIPE Document 157</i>, you need to change the format of the query slightly. If you were to search for all entries in the RIPE database which lists the <i>admin-c</i>, <i>tech-c</i> or <i>zone-c</i> as <i>CO19-RIPE</i>, you could use the following command syntax: </p>
<p> <code>jwhois -h whois.ripe.net &#8212; -i admin-c,tech-c,zone-c CO19-RIPE</code> </p>
<p> <code>&#8212;</code> is used to separate the RIPE options from the jwhois options. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-whois/">whois</a>(1)</p>
