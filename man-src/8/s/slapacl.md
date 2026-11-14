---
title: "slapacl(8)"
name: "slapacl"
section: "8"
letter: "s"
url: "/docs/linux/man/8-slapacl/"
description: "slapacl – Check access to a list of attributes."
---

<p>slapacl &#8211; Check access to a list of attributes.</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/slapacl</code> <code>-b</code><i>&nbsp;<wbr>DN</i> [<code>-d</code><i>&nbsp;<wbr>debug-level</i>] [<code>-D</code><i>&nbsp;<wbr>authcDN&nbsp;<wbr></i>| <code>-U</code><i>&nbsp;<wbr>authcID</i>] [<code>-f</code><i>&nbsp;<wbr>slapd.conf</i>] [<code>-F</code><i>&nbsp;<wbr>confdir</i>] [<code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]] [<code>-u</code>] [<code>-v</code>] [<code>-X</code><i>&nbsp;<wbr>authzID&nbsp;<wbr></i>| <code>-o &nbsp;<wbr>authzDN=</code><i>DN</i>] [<i>attr</i>[<code>/</code><i>access</i>][<code>:</code><i>value</i>]]&nbsp;<wbr>[&#8230;] </p>
<h2>Description</h2>
<p><code>slapacl</code> is used to check the behavior of <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) by verifying access to directory data according to the access control list directives defined in its configuration. It opens the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) configuration file or the <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5) backend, reads in the <code>access</code>/<code>olcAccess</code> directives, and then parses the <code>attr</code> list given on the command-line; if none is given, access to the <code>entry</code> pseudo-attribute is tested. </p>
<h2>Options</h2>
<dl>
<dt><code>-b</code><i>&nbsp;<wbr>DN</i></p>
<dd>specify the <i>DN </i> which access is requested to; the corresponding entry is fetched from the database, and thus it must exist. The <i>DN</i> is also used to determine what rules apply; thus, it must be in the naming context of a configured database. See also <code>-u</code>.</p>
<dt><code>-d</code><i>&nbsp;<wbr>debug-level</i></p>
<dd>enable debugging messages as defined by the specified <i>debug-level</i>; see <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) for details.</p>
<dt><code>-D</code><i>&nbsp;<wbr>authcDN</i></p>
<dd>specify a DN to be used as identity through the test session when selecting appropriate <code>&lt;by&gt; </code> clauses in access lists.</p>
<dt><code>-f</code><i>&nbsp;<wbr>slapd.conf</i></p>
<dd>specify an alternative <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) file.</p>
<dt><code>-F</code><i>&nbsp;<wbr>confdir</i></p>
<dd>specify a config directory. If both <code>-f</code> and <code>-F</code> are specified, the config file will be read and converted to config directory format and written to the specified directory. If neither option is specified, an attempt to read the default config directory will be made before trying to use the default config file. If a valid config directory exists then the default config file is ignored.</p>
<dt><code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]</p>
<dd>Specify an <i>option</i> with a(n optional) <i>value</i>. Possible generic options/values are:</dl>
<pre> syslog=&lt;subsystems&gt; (see `-s' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))
 syslog-level=&lt;level&gt; (see `-S' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))
 syslog-user=&lt;user&gt; (see `-l' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))</pre>
<dl>
<dd>Possible options/values specific to <code>slapacl</code> are:</dl>
<pre> authzDN
 domain
 peername
 sasl_ssf
 sockname
 sockurl
 ssf
 tls_ssf
 transport_ssf</pre>
<dl>
<dd>See the related fields in <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5) for details.</dl>
<dl>
<dt><code>-u</code></p>
<dd>do not fetch the entry from the database. In this case, if the entry does not exist, a fake entry with the <i>DN</i> given with the <code>-b</code> option is used, with no attributes. As a consequence, those rules that depend on the contents of the target object will not behave as with the real object. The <i>DN</i> given with the <code>-b</code> option is still used to select what rules apply; thus, it must be in the naming context of a configured database. See also <code>-b</code>.</p>
<dt><code>-U</code><i>&nbsp;<wbr>authcID</i></p>
<dd>specify an ID to be mapped to a <code>DN </code> as by means of <code>authz-regexp</code> or <code>authz-rewrite</code> rules (see <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) for details); mutually exclusive with <code>-D</code>.</p>
<dt><code>-v</code></p>
<dd>enable verbose mode.</p>
<dt><code>-X</code><i>&nbsp;<wbr>authzID</i></p>
<dd>specify an authorization ID to be mapped to a <code>DN</code> as by means of <code>authz-regexp</code> or <code>authz-rewrite</code> rules (see <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) for details); mutually exclusive with <code>-o</code> <code>authzDN=</code><i>DN</i>.</dl>
<h2>Examples</h2>
<p>The command </p>
<pre> /usr/sbin/slapacl -f /etc/openldap/slapd.conf -v \
 -U bjorn -b &quot;o=University of Michigan,c=US&quot; \
 &quot;o/read:University of Michigan&quot;</pre>
<p>tests whether the user <i>bjorn</i> can access the attribute <i>o</i> of the entry <i>o=University of Michigan,c=US</i> at <i>read</i> level.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/8-slaptest/">slaptest</a></code>(8), <code><a href="/docs/linux/man/8-slapauth/">slapauth</a></code>(8) </p>
<p> &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a></p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
