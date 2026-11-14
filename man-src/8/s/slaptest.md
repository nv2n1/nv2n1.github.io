---
title: "slaptest(8)"
name: "slaptest"
section: "8"
letter: "s"
url: "/docs/linux/man/8-slaptest/"
description: "slaptest – Check the suitability of the OpenLDAP slapd configuration"
---

<p>slaptest &#8211; Check the suitability of the OpenLDAP slapd configuration</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/slaptest</code> [<code>-d</code><i>&nbsp;<wbr>debug-level</i>] [<code>-f</code><i>&nbsp;<wbr>slapd.conf</i>] [<code>-F</code><i>&nbsp;<wbr>confdir</i>] [<code>-n</code><i>dbnum</i>] [<code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]] [<code>-Q</code>] [<code>-u</code>] [<code>-v</code>] </p>
<h2>Description</h2>
<p><code>Slaptest</code> is used to check the conformance of the <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) configuration. It opens the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) configuration file or the <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5) backend, and parses it according to the general and the backend-specific rules, checking its sanity. </p>
<h2>Options</h2>
<dl>
<dt><code>-d</code><i>&nbsp;<wbr>debug-level</i></p>
<dd>enable debugging messages as defined by the specified <i>debug-level</i>; see <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) for details.</p>
<dt><code>-f</code><i>&nbsp;<wbr>slapd.conf</i></p>
<dd>specify an alternative <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) file.</p>
<dt><code>-F</code><i>&nbsp;<wbr>confdir</i></p>
<dd>specify a config directory. If both <code>-f</code> and <code>-F</code> are specified, the config file will be read and converted to config directory format and written to the specified directory. If neither option is specified, slaptest will attempt to read the default config directory before trying to use the default config file. If a valid config directory exists then the default config file is ignored. If dry-run mode is also specified, no conversion will occur.</p>
<dt><code>-n</code><i>&nbsp;<wbr>dbnum</i></p>
<dd>Just open and test the <i>dbnum</i>-th database listed in the configuration file. To only test the config database <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), use <code>-n 0</code> as it is always the first database.</p>
<dt><code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]</p>
<dd>Specify an <i>option</i> with a(n optional) <i>value</i>. Possible generic options/values are:</dl>
<pre> syslog=&lt;subsystems&gt; (see `-s' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))
 syslog-level=&lt;level&gt; (see `-S' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))
 syslog-user=&lt;user&gt; (see `-l' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))</pre>
<dl>
<dt><code>-Q</code></p>
<dd>Be extremely quiet: only the exit code indicates success (0) or not (any other value).</p>
<dt><code>-u</code></p>
<dd>enable dry-run mode (i.e. don&#8217;t fail if databases cannot be opened, but config is fine).</p>
<dt><code>-v</code></p>
<dd>enable verbose mode.</dl>
<h2>Examples</h2>
<p>To check a <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) give the command: </p>
<pre> /usr/sbin/slaptest -f //etc/openldap/slapd.conf -v</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/8-slapdn/">slapdn</a></code>(8) </p>
<p> &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a></p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
