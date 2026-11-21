---

title: "jwhois(1)"
name: "jwhois"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jwhois/"
description: "jwhois – client for the whois service"
---

<p> jwhois &#8211; client for the whois service</p>
<h2>SYNOPSIS</h2>
<p> <code>jwhois</code> [ <i>OPTIONS</i> ]&#8230; [ <i>QUERY</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>jwhois</i> searches Whois servers for the object on the command line. </p>
<p> The host to query is taken from a global configuration file, a configuration file specified on the command line, or selected directly on the command line. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> display version, authors and licensing information.</dd>
<dt><code>&#8211;help</code></dt>
<dd> display a short help text.</dd>
<dt><code>-c FILE &#8211;config=FILE</code></dt>
<dd> uses FILE as a configuration file instead of the default.</dd>
<dt><code>-h HOST &#8211;host=HOST</code></dt>
<dd> overrides any hosts in the configuration file and queries HOST directly.</dd>
<dt><code>-p PORT &#8211;port=PORT</code></dt>
<dd> specifies a port number to use when querying a HOST.</dd>
<dt><code>-f &#8211;force-lookup</code></dt>
<dd> forces a query to be made to a host even if a current object is available from the cache.</dd>
<dt><code>-v &#8211;verbose</code></dt>
<dd> outputs verbose debugging information while running (use this before sending a bugreport to ensure that it&#8217;s indeed a bug and not a misconfiguration). You can increase the verbosity by giving several verbose commands to jwhois, such as -vv.</dd>
<dt><code>-n &#8211;no-redirect</code></dt>
<dd> disable features that redirect queries from one server to another.</dd>
<dt><code>-s &#8211;no-whoisservers</code></dt>
<dd> disable the built-in support for whois-servers.net.</dd>
<dt><code>-a &#8211;raw</code></dt>
<dd> send query verbatim to receiving hosts instead of rewriting them according to the configuration.</dd>
<dt><code>-i &#8211;display-redirections</code></dt>
<dd> display every step in a redirection (default is to display only the last answer).</dd>
<dt><code>-d &#8211;disable-cache</code></dt>
<dd> completely disable both reading and writing to cache.</dd>
<dt><code>-r &#8211;rwhois</code></dt>
<dd> force the query to use the rwhois protocoll instead of HTTP or whois.</dd>
<dt><code>&#8211;rwhois-display=DISPLAY</code></dt>
<dd> asks receiving rwhois servers to display the results in the DISPLAY display instead of the default dump display.</dd>
<dt><code>&#8211;rwhois-limit=LIMIT</code></dt>
<dd> asks receiving rwhois servers to limit their responses to LIMIT matches. </dd>
</dl>
<h3>RIPE EXTENSIONS</h3>
<p> To use the options specified in <i>RIPE Document 157</i>, you need to change the format of the query slightly. If you were to search for all entries in the RIPE database which lists the <i>admin-c</i>, <i>tech-c</i> or <i>zone-c</i> as <i>CO19-RIPE</i>, you could use the following command syntax: </p>
<p> <code>jwhois -h whois.ripe.net &#8212; -i admin-c,tech-c,zone-c CO19-RIPE</code> </p>
<p> <code>&#8212;</code> is used to separate the RIPE options from the jwhois options. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-whois/">whois</a>(1) </p>
