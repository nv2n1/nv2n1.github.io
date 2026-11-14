---
title: "slapd-null(5)"
name: "slapd-null"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-null/"
description: "slapd-null – Null backend to slapd"
---

<p>slapd-null &#8211; Null backend to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The Null backend to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) is surely the most useful part of <code>slapd</code>:<br />
 &#8211; Searches return success but no entries.<br />
 &#8211; Compares return compareFalse.<br />
 &#8211; Updates return success (unless readonly is on) but do nothing.<br />
 &#8211; Binds other than as the rootdn fail unless the database option &quot;bind on&quot; is given.<br />
 &#8211; The <code><a href="/docs/linux/man/8-slapadd/">slapadd</a></code>(8) and <code><a href="/docs/linux/man/8-slapcat/">slapcat</a></code>(8) tools are equally exciting.<br />
 Inspired by the /dev/null device.</p>
<h2>Configuration</h2>
<p>This <code>slapd.conf</code> option applies to the NULL backend database. That is, it must follow a &quot;database null&quot; line and come before any subsequent &quot;database&quot; lines. Other database options are described in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) manual page.</p>
<dl>
<dt><code>bind &lt;on/off&gt;</code></p>
<dd>Allow binds as any DN in this backend&#8217;s suffix, with any password. The default is &quot;off&quot;.</dl>
<h2>Example</h2>
<p>Here is a possible slapd.conf extract using the Null backend: </p>
<dl>
<dd>
<pre>database null
suffix &quot;cn=Nothing&quot;
bind on</pre>
</dl>
<h2>Access Control</h2>
<p>The <code>null</code> backend does not honor any of the access control semantics described in <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5).</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/8-slapadd/">slapadd</a></code>(8), <code><a href="/docs/linux/man/8-slapcat/">slapcat</a></code>(8). </p>
