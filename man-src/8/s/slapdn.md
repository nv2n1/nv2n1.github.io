---
title: "slapdn(8)"
name: "slapdn"
section: "8"
letter: "s"
url: "/docs/linux/man/8-slapdn/"
description: "slapdn – Check a list of string-represented LDAP DNs based on schema syntax"
---

<p>slapdn &#8211; Check a list of string-represented LDAP DNs based on schema syntax</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/slapdn</code> [<code>-d</code><i>&nbsp;<wbr>debug-level</i>] [<code>-f</code><i>&nbsp;<wbr>slapd.conf</i>] [<code>-F</code><i>&nbsp;<wbr>confdir</i>] [<code>-N</code>|<code>-P</code>] [<code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]] [<code>-v</code>] <i>DN</i>&nbsp;<wbr>[&#8230;] </p>
<h2>Description</h2>
<p><code>Slapdn</code> is used to check the conformance of a DN based on the schema defined in <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) and that loaded via <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5). It opens the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) configuration file or the slapd-config (5) backend, reads in the schema definitions, and then parses the <i>DN</i> list given on the command-line. </p>
<h2>Options</h2>
<dl>
<dt><code>-d</code><i>&nbsp;<wbr>debug-level</i></p>
<dd>enable debugging messages as defined by the specified <i>debug-level</i>; see <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) for details.</p>
<dt><code>-f</code><i>&nbsp;<wbr>slapd.conf</i></p>
<dd>specify an alternative <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) file.</p>
<dt><code>-F</code><i>&nbsp;<wbr>confdir</i></p>
<dd>specify a config directory. If both <code>-f</code> and <code>-F</code> are specified, the config file will be read and converted to config directory format and written to the specified directory. If neither option is specified, an attempt to read the default config directory will be made before trying to use the default config file. If a valid config directory exists then the default config file is ignored.</p>
<dt><code>-N</code></p>
<dd>only output a normalized form of the <i>DN</i>, suitable to be used in a normalization tool; incompatible with <code>-P</code>.</p>
<dt><code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]</p>
<dd>Specify an <i>option</i> with a(n optional) <i>value</i>. Possible generic options/values are:</dl>
<pre> syslog=&lt;subsystems&gt; (see `-s' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))
 syslog-level=&lt;level&gt; (see `-S' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))
 syslog-user=&lt;user&gt; (see `-l' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))</pre>
<dl>
<dt><code>-P</code></p>
<dd>only output a prettified form of the <i>DN</i>, suitable to be used in a check and beautification tool; incompatible with <code>-N</code>.</p>
<dt><code>-v</code></p>
<dd>enable verbose mode.</dl>
<h2>Examples</h2>
<p>To check a <code>DN</code> give the command: </p>
<pre> /usr/sbin/slapdn -f //etc/openldap/slapd.conf -v DN</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/8-slaptest/">slaptest</a></code>(8) </p>
<p> &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a></p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
