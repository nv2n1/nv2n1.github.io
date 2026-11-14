---
title: "slapindex(8)"
name: "slapindex"
section: "8"
letter: "s"
url: "/docs/linux/man/8-slapindex/"
description: "slapindex – Reindex entries in a SLAPD database"
---

<p>slapindex &#8211; Reindex entries in a SLAPD database</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/slapindex</code> [<code>-b</code><i>&nbsp;<wbr>suffix</i>] [<code>-c</code>] [<code>-d</code><i>&nbsp;<wbr>debug-level</i>] [<code>-f</code><i>&nbsp;<wbr>slapd.conf</i>] [<code>-F</code><i>&nbsp;<wbr>confdir</i>] [<code>-g</code>] [<code>-n</code><i>&nbsp;<wbr>dbnum</i>] [<code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]] [<code>-q</code>] [<code>-t</code>] [<code>-v</code>] [<i>attr</i>[<i>&#8230;</i>]] <code> </p>
<h2>Description</h2>
<p><code>Slapindex</code> is used to regenerate <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) indices based upon the current contents of a database. It opens the given database determined by the database number or suffix and updates the indices for all values of all attributes of all entries. If a list of specific attributes is provided on the command line, only the indices for those attributes will be regenerated. Databases configured as <code>subordinate</code> of this one are also re-indexed, unless <code>-g</code> is specified. </p>
<p> All files eventually created by <code>slapindex</code> will belong to the identity <code>slapindex</code> is run as, so make sure you either run <code>slapindex</code> with the same identity <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) will be run as (see option <code>-u</code> in <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8)), or change file ownership before running <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8).</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code><i>&nbsp;<wbr>suffix</i></p>
<dd>Use the specified <i>suffix</i> to determine which database to generate output for. The <code>-b</code> cannot be used in conjunction with the <code>-n</code> option.</p>
<dt><code>-c</code></p>
<dd>enable continue (ignore errors) mode.</p>
<dt><code>-d</code><i>&nbsp;<wbr>debug-level</i></p>
<dd>enable debugging messages as defined by the specified <i>debug-level</i>; see <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) for details.</p>
<dt><code>-f</code><i>&nbsp;<wbr>slapd.conf</i></p>
<dd>specify an alternative <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) file.</p>
<dt><code>-F</code><i>&nbsp;<wbr>confdir</i></p>
<dd>specify a config directory. If both <code>-f</code> and <code>-F</code> are specified, the config file will be read and converted to config directory format and written to the specified directory. If neither option is specified, an attempt to read the default config directory will be made before trying to use the default config file. If a valid config directory exists then the default config file is ignored.</p>
<dt><code>-g</code></p>
<dd>disable subordinate gluing. Only the specified database will be processed, and not its glued subordinates (if any).</p>
<dt><code>-n</code><i>&nbsp;<wbr>dbnum</i></p>
<dd>Generate output for the <i>dbnum</i>-th database listed in the configuration file. The config database <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), is always the first database, so use <code>-n 0</code> </p>
<p> The <code>-n</code> cannot be used in conjunction with the <code>-b</code> option.</p>
<dt><code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]</p>
<dd>Specify an <i>option</i> with a(n optional) <i>value</i>. Possible generic options/values are:</dl>
<pre> syslog=&lt;subsystems&gt; (see `-s' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))
 syslog-level=&lt;level&gt; (see `-S' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))
 syslog-user=&lt;user&gt; (see `-l' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))</pre>
<dl>
<dt><code>-q</code></p>
<dd>enable quick (fewer integrity checks) mode. Performs no consistency checks when writing the database. Improves indexing time, <code>however</code> the database will most likely be unusable if any errors or interruptions occur.</p>
<dt><code>-t</code></p>
<dd>enable truncate mode. Truncates (empties) an index database before indexing any entries. May only be used with Quick mode.</p>
<dt><code>-v</code></p>
<dd>enable verbose mode.</dl>
<h2>Limitations</h2>
<p>Your <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) should not be running (at least, not in read-write mode) when you do this to ensure consistency of the database. </p>
<p> This command provides ample opportunity for the user to obtain and drink their favorite beverage.</p>
<h2>Examples</h2>
<p>To reindex your SLAPD database, give the command: </p>
<pre> /usr/sbin/slapindex</pre>
<p>To regenerate the index for only a specific attribute, e.g. &quot;uid&quot;, give the command: </p>
<pre> /usr/sbin/slapindex uid</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/5-ldif/">ldif</a></code>(5), <code><a href="/docs/linux/man/8-slapadd/">slapadd</a></code>(8), <code><a href="/docs/linux/man/1-ldapadd/">ldapadd</a></code>(1), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) </p>
<p> &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a></p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
