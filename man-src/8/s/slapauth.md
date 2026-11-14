---
title: "slapauth(8)"
name: "slapauth"
section: "8"
letter: "s"
url: "/docs/linux/man/8-slapauth/"
description: "slapauth – Check a list of string-represented IDs for LDAP authc/authz"
---

<p>slapauth &#8211; Check a list of string-represented IDs for LDAP authc/authz</p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/slapauth</code> [<code>-d</code><i>&nbsp;<wbr>debug-level</i>] [<code>-f</code><i>&nbsp;<wbr>slapd.conf</i>] [<code>-F</code><i>&nbsp;<wbr>confdir</i>] [<code>-M</code><i>&nbsp;<wbr>mech</i>] [<code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]] [<code>-R</code><i>&nbsp;<wbr>realm</i>] [<code>-U</code><i>&nbsp;<wbr>authcID</i>] [<code>-v</code>] [<code>-X</code><i>&nbsp;<wbr>authzID</i>] <i>ID</i>&nbsp;<wbr>[<i>&#8230;</i>] </p>
<h2>Description</h2>
<p><code>Slapauth</code> is used to check the behavior of the slapd in mapping identities for authentication and authorization purposes, as specified in <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5). It opens the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) configuration file or the <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5) backend, reads in the <code>authz-policy</code>/<code>olcAuthzPolicy</code> and <code>authz-regexp</code>/<code>olcAuthzRegexp</code> directives, and then parses the <i>ID</i> list given on the command-line. </p>
<h2>Options</h2>
<dl>
<dt><code>-d</code><i>&nbsp;<wbr>debug-level</i></p>
<dd>enable debugging messages as defined by the specified <i>debug-level</i>; see <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) for details.</p>
<dt><code>-f</code><i>&nbsp;<wbr>slapd.conf</i></p>
<dd>specify an alternative <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) file.</p>
<dt><code>-F</code><i>&nbsp;<wbr>confdir</i></p>
<dd>specify a config directory. If both <code>-f</code> and <code>-F</code> are specified, the config file will be read and converted to config directory format and written to the specified directory. If neither option is specified, an attempt to read the default config directory will be made before trying to use the default config file. If a valid config directory exists then the default config file is ignored.</p>
<dt><code>-M</code><i>&nbsp;<wbr>mech</i></p>
<dd>specify a mechanism.</p>
<dt><code>-o</code><i>&nbsp;<wbr>option</i>[<code>=</code><i>value</i>]</p>
<dd>Specify an <i>option</i> with a(n optional) <i>value</i>. Possible generic options/values are:</dl>
<pre> syslog=&lt;subsystems&gt; (see `-s' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))
 syslog-level=&lt;level&gt; (see `-S' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))
 syslog-user=&lt;user&gt; (see `-l' in <a href="//www.systutorials.com/docs/linux/man/8-slapd/">slapd</a>(8))</pre>
<dl>
<dt><code>-R</code><i>&nbsp;<wbr>realm</i></p>
<dd>specify a realm.</p>
<dt><code>-U</code><i>&nbsp;<wbr>authcID</i></p>
<dd>specify an ID to be used as <i>authcID</i> throughout the test session. If present, and if no <i>authzID</i> is given, the IDs in the ID list are treated as <i>authzID</i>.</p>
<dt><code>-X</code><i>&nbsp;<wbr>authzID</i></p>
<dd>specify an ID to be used as <i>authzID</i> throughout the test session. If present, and if no <i>authcID</i> is given, the IDs in the ID list are treated as <i>authcID</i>. If both <i>authcID </i> and <i>authzID</i> are given via command line switch, the ID list cannot be present.</p>
<dt><code>-v</code></p>
<dd>enable verbose mode.</dl>
<h2>Examples</h2>
<p>The command </p>
<pre> /usr/sbin/slapauth -f //etc/openldap/slapd.conf -v \
 -U bjorn -X u:bjensen</pre>
<p>tests whether the user <i>bjorn</i> can assume the identity of the user <i>bjensen</i> provided the directives </p>
<pre> authz-policy from
 authz-regexp &quot;^uid=([^,]+).*,cn=auth$&quot;
 &quot;<a href="ldap:///dc=example,dc=net??sub?uid=$1">ldap:///dc=example,dc=net??sub?uid=$1</a>&quot;</pre>
<p>are defined in <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/8-slaptest/">slaptest</a></code>(8) </p>
<p> &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a></p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
