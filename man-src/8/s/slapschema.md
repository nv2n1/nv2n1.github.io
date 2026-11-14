---
title: "slapschema(8)"
name: "slapschema"
section: "8"
letter: "s"
url: "/docs/linux/man/8-slapschema/"
description: "slapschema – SLAPD in-database schema checking utility"
---

<p>slapschema &#8211; SLAPD in-database schema checking utility</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/slapschema</code> [<code>-a</code><i>filter</i>] [<code>-b</code><i>suffix</i>] [<code>-c</code>] [<code>-d</code><i>debug-level</i>] [<code>-f</code><i>slapd.conf</i>] [<code>-F</code><i>confdir</i>] [<code>-g</code>] [<code>-H</code><i>URI</i>] [<code>-l</code><i>error-file</i>] [<code>-n</code><i>dbnum</i>] [<code>-o</code><i>option</i>[<code>=</code><i>value</i>]] [<code>-s</code><i>subtree-dn</i>] [<code>-v</code>] </p>
<h2>Description</h2>
<p><code>Slapschema</code> is used to check schema compliance of the contents of a <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) database. It opens the given database determined by the database number or suffix and checks the compliance of its contents with the corresponding schema. Errors are written to standard output or the specified file. Databases configured as <code>subordinate</code> of this one are also output, unless <code>-g</code> is specified. </p>
<p> Administrators may need to modify existing schema items, including adding new required attributes to objectClasses, removing existing required or allowed attributes from objectClasses, entirely removing objectClasses, or any other change that may result in making perfectly valid entries no longer compliant with the modified schema. The execution of the <code>slapschema</code> tool after modifying the schema can point out inconsistencies that would otherwise surface only when inconsistent entries need to be modified. </p>
<p> The entry records are checked in database order, not superior first order. The entry records will be checked considering all (user and operational) attributes stored in the database. Dynamically generated attributes (such as subschemaSubentry) will not be considered.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code><i>&nbsp;<wbr>filter</i></p>
<dd>Only check entries matching the asserted filter. For example </p>
<p> slapschema -a \<br />
&nbsp;<wbr>&quot;(!(entryDN:dnSubtreeMatch:=ou=People,dc=example,dc=com))&quot; </p>
<p> will check all but the &quot;ou=People,dc=example,dc=com&quot; subtree of the &quot;dc=example,dc=com&quot; database. Deprecated; use <code>-H</code> <i><a href="ldap:///???(filter)">ldap:///???(filter)</a></i> instead.</p>
<dt><code>-b</code><i>&nbsp;<wbr>suffix</i></p>
<dd>Use the specified <i>suffix</i> to determine which database to check. The <code>-b</code> cannot be used in conjunction with the <code>-n</code> option.</p>
<dt><code>-c</code></p>
<dd>Enable continue (ignore errors) mode.</p>
<dt><code>-d</code><i>&nbsp;<wbr>debug-level</i></p>
<dd>Enable debugging messages as defined by the specified <i>debug-level</i>; see <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) for details.</p>
<dt><code>-f</code><i>&nbsp;<wbr>slapd.conf</i></p>
<dd>Specify an alternative <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) file.</p>
<dt><code>-F</code><i>&nbsp;<wbr>confdir</i></p>
<dd>specify a config directory. If both <code>-f</code> and <code>-F</code> are specified, the config file will be read and converted to config directory format and written to the specified directory. If neither option is specified, an attempt to read the default config directory will be made before trying to use the default config file. If a valid config directory exists then the default config file is ignored.</p>
<dt><code>-g</code></p>
<dd>disable subordinate gluing. Only the specified database will be processed, and not its glued subordinates (if any).</p>
<dt><code>-H &nbsp;<wbr>URI</code></p>
<dd>use dn, scope and filter from URI to only handle matching entries.</p>
<dt><code>-l</code><i>&nbsp;<wbr>error-file</i></p>
<dd>Write errors to specified file instead of standard output.</p>
<dt><code>-n</code><i>&nbsp;<wbr>dbnum</i></p>
<dd>Check the <i>dbnum</i>-th database listed in the configuration file. The config database <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), is always the first database, so use <code>-n 0</code> </p>
<p> The <code>-n</code> cannot be used in conjunction with the <code>-b</code> option.</p>
<dt><code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]</p>
<dd>Specify an <i>option</i> with a(n optional) <i>value</i>. Possible generic options/values are:</dl>
<pre> syslog=&lt;subsystems&gt; (see `-s' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))
 syslog-level=&lt;level&gt; (see `-S' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))
 syslog-user=&lt;user&gt; (see `-l' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))</pre>
<dl>
<dt><code>-s</code><i>&nbsp;<wbr>subtree-dn</i></p>
<dd>Only check entries in the subtree specified by this DN. Implies <code>-b</code> <i>subtree-dn</i> if no <code>-b</code> nor <code>-n</code> option is given. Deprecated; use <code>-H</code> <i><a href="ldap:///subtree-dn">ldap:///subtree-dn</a></i> instead.</p>
<dt><code>-v</code></p>
<dd>Enable verbose mode.</dl>
<h2>Limitations</h2>
<p>For some backend types, your <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) should not be running (at least, not in read-write mode) when you do this to ensure consistency of the database. It is always safe to run <code>slapschema</code> with the <code><a href="/docs/linux/man/5-slapd-bdb/">slapd-bdb</a></code>(5), <code><a href="/docs/linux/man/5-slapd-hdb/">slapd-hdb</a></code>(5), and <code><a href="/docs/linux/man/5-slapd-null/">slapd-null</a></code>(5) backends.</p>
<h2>Examples</h2>
<p>To check the schema compliance of your SLAPD database after modifications to the schema, and put any error in a file called <code>errors.ldif</code>, give the command: </p>
<pre> /usr/sbin/slapschema -l errors.ldif</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/5-ldif/">ldif</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) </p>
<p> &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a></p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
