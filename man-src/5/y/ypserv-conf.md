---
title: "ypserv-conf(5)"
name: "ypserv-conf"
section: "5"
letter: "y"
url: "/docs/linux/man/5-ypserv-conf/"
description: "ypserv.conf – configuration file for ypserv and rpc.ypxfrd"
---

<p>ypserv.conf &#8211; configuration file for ypserv and rpc.ypxfrd</p>
<h2>Description</h2>
<p><i>ypserv.conf</i> is an ASCII file which contains some options for ypserv. It also contains a list of rules for special host and map access for ypserv and rpc.ypxfrd. This file will be read by ypserv and rpc.ypxfrd at startup, or when receiving a SIGHUP signal. </p>
<p> There is one entry per line. If the line is a option line, the format is: </p>
<dl>
<dd>
<pre> option: <i>argument</i></pre>
</dl>
<p> The line for an access rule has the format: </p>
<dl>
<dd>
<pre> host:domain:map:security</pre>
</dl>
<p> All rules are tried one by one. If no match is found, access to a map is allowed. </p>
<p> Following options exist:</p>
<dl>
<dt><code>files:</code> <i>30</i></p>
<dd>This option specifies, how many database files should be cached by <i>ypserv</i>. If 0 is specified, caching is disabled. Decreasing this number is only possible, if ypserv is restarted.</p>
<dt><code>trusted_master:</code> <i>server</i></p>
<dd>If this option is set on a slave server, new maps from the host <i>server</i> will be accepted as master. The default is, that no trusted master is set and new maps will not be accepted. </p>
<p> Example: </p>
<dl>
<dd>
<pre> trusted_master: ypmaster.example.org</pre>
</dl>
<dt><code>slp:</code> [<i>yes</i>|<i>&lt;no&gt;</i>|<i>domain</i>]</p>
<dd>If this option is enabled and SLP support compiled in, the NIS server registers itself on a SLP server. If the variable is set to <i>domain</i>, an attribute <i>domain</i> with a comma seperated list of supported domainnames is set. Else this attribute will not be set. The default is &quot;no&quot; (disabled).</p>
<dt><code>xfr_check_port:</code> [<i>&lt;yes&gt;</i>|<i>no</i>]</p>
<dd>With this option enabled, the NIS master server have to run on a port &lt; 1024. The default is &quot;yes&quot; (enabled).</dl>
<p> The field descriptions for the access rule lines are:</p>
<dl>
<dt><code>host</code></p>
<dd>IP address. Wildcards are allowed. </p>
<p> Examples: </p>
<dl>
<dd>
<pre> 131.234. = 131.234.0.0/255.255.0.0
 131.234.214.0/255.255.254.0</pre>
</dl>
<dt><code>domain</code></p>
<dd>specifies the domain, for which this rule should be applied. An asterix as wildcard is allowed.</p>
<dt><code>map</code></p>
<dd>name of the map, or asterisk for all maps.</p>
<dt><code>security</code></p>
<dd>one of <i>none</i>, <i>port</i>, <i>deny</i>:</p>
<dl>
<dd>
<dl>
<dt><i>none</i></p>
<dd>always allow access.</p>
<dt><i>port</i></p>
<dd>allow access if from port &lt; 1024. Otherwise do not allow access.</p>
<dt><i>deny</i></p>
<dd>deny access to this map.</dl>
</dl>
</dl>
<h2>Files</h2>
<p><i>/etc/ypserv.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8), <code><a href="/docs/linux/man/8-rpc-ypxfrd/">rpc.ypxfrd</a></code>(8)</p>
<h2>Warnings</h2>
<p>The access rules for special maps are no real improvement in security, but they make the life a little bit harder for a potential hacker. </p>
<p> Solaris clients don&#8217;t use privileged ports. All security options which depend on privileged ports cause big problems on Solaris clients.</p>
<h2>Author</h2>
<p>Thorsten Kukuk &lt;kukuk [at] thkukuk.de&gt;</p>
