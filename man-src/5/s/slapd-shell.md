---
title: "slapd-shell(5)"
name: "slapd-shell"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-shell/"
description: "slapd-shell – Shell backend to slapd"
---

<p>slapd-shell &#8211; Shell backend to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The Shell backend to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) executes external programs to implement operations, and is designed to make it easy to tie an existing database to the <code>slapd</code> front-end. </p>
<p> This backend is primarily intended to be used in prototypes.</p>
<h2>Warning</h2>
<p>The <code>abandon</code> shell command has been removed since OpenLDAP 2.1.</p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> options apply to the SHELL backend database. That is, they must follow a &quot;database shell&quot; line and come before any subsequent &quot;backend&quot; or &quot;database&quot; lines. Other database options are described in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) manual page. </p>
<p> These options specify the pathname and arguments of the program to execute in response to the given LDAP operation. Each option is followed by the input lines that the program receives:</p>
<dl>
<dt><code>add &lt;pathname&gt; &lt;argument&gt;&#8230;</code></p>
<dd>
<pre>ADD
msgid: &lt;message id&gt;
&lt;repeat { &quot;suffix:&quot; &lt;database suffix DN&gt; }&gt;
&lt;entry in LDIF format&gt;</pre>
<dt><code>bind &lt;pathname&gt; &lt;argument&gt;&#8230;</code></p>
<dd>
<pre>BIND
msgid: &lt;message id&gt;
&lt;repeat { &quot;suffix:&quot; &lt;database suffix DN&gt; }&gt;
dn: &lt;DN&gt;
method: &lt;method number&gt;
credlen: &lt;length of &lt;credentials&gt;&gt;
cred: &lt;credentials&gt;</pre>
<dt><code>compare &lt;pathname&gt; &lt;argument&gt;&#8230;</code></p>
<dd>
<pre>COMPARE
msgid: &lt;message id&gt;
&lt;repeat { &quot;suffix:&quot; &lt;database suffix DN&gt; }&gt;
dn: &lt;DN&gt;
&lt;attribute&gt;: &lt;value&gt;</pre>
<dt><code>delete &lt;pathname&gt; &lt;argument&gt;&#8230;</code></p>
<dd>
<pre>DELETE
msgid: &lt;message id&gt;
&lt;repeat { &quot;suffix:&quot; &lt;database suffix DN&gt; }&gt;
dn: &lt;DN&gt;</pre>
<dt><code>modify &lt;pathname&gt; &lt;argument&gt;&#8230;</code></p>
<dd>
<pre>MODIFY
msgid: &lt;message id&gt;
&lt;repeat { &quot;suffix:&quot; &lt;database suffix DN&gt; }&gt;
dn: &lt;DN&gt;
&lt;repeat {
 &lt;&quot;add&quot;/&quot;delete&quot;/&quot;replace&quot;&gt;: &lt;attribute&gt;
 &lt;repeat { &lt;attribute&gt;: &lt;value&gt; }&gt;
 -
}&gt;</pre>
<dt><code>modrdn &lt;pathname&gt; &lt;argument&gt;&#8230;</code></p>
<dd>
<pre>MODRDN
msgid: &lt;message id&gt;
&lt;repeat { &quot;suffix:&quot; &lt;database suffix DN&gt; }&gt;
dn: &lt;DN&gt;
newrdn: &lt;new RDN&gt;
deleteoldrdn: &lt;0 or 1&gt;
&lt;if new superior is specified: &quot;newSuperior: &lt;DN&gt;&quot;&gt;</pre>
<dt><code>search &lt;pathname&gt; &lt;argument&gt;&#8230;</code></p>
<dd>
<pre>SEARCH
msgid: &lt;message id&gt;
&lt;repeat { &quot;suffix:&quot; &lt;database suffix DN&gt; }&gt;
base: &lt;base DN&gt;
scope: &lt;0-2, see ldap.h&gt;
deref: &lt;0-3, see ldap.h&gt;
sizelimit: &lt;size limit&gt;
timelimit: &lt;time limit&gt;
filter: &lt;filter&gt;
attrsonly: &lt;0 or 1&gt;
attrs: &lt;&quot;all&quot; or space-separated attribute list&gt;</pre>
<dt><code>unbind &lt;pathname&gt; &lt;argument&gt;&#8230;</code></p>
<dd>
<pre>UNBIND
msgid: &lt;message id&gt;
&lt;repeat { &quot;suffix:&quot; &lt;database suffix DN&gt; }&gt;
dn: &lt;bound DN&gt;</pre>
</dl>
<p> Note that you need only supply configuration lines for those commands you want the backend to handle. Operations for which a command is not supplied will be refused with an &quot;unwilling to perform&quot; error. </p>
<p> The <code>search</code> command should output the entries in LDIF format, each entry followed by a blank line, and after these the RESULT below. </p>
<p> All commands except <code>unbind</code> should then output:</p>
<dl>
<dd>
<pre>RESULT
code: &lt;integer&gt;
matched: &lt;matched DN&gt;
info: &lt;text&gt;</pre>
</dl>
<p> where only the RESULT line is mandatory. Lines starting with `#&#8217; or `DEBUG:&#8217; are ignored.</p>
<h2>Access Control</h2>
<p>The <code>shell</code> backend does not honor all ACL semantics as described in <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5). In general, access to objects is checked by using a dummy object that contains only the DN, so access rules that rely on the contents of the object are not honored. In detail: </p>
<p> The <code>add</code> operation does not require <code>write (=w)</code> access to the <code>children</code> pseudo-attribute of the parent entry. </p>
<p> The <code>bind</code> operation requires <code>auth (=x)</code> access to the <code>entry</code> pseudo-attribute of the entry whose identity is being assessed; <code>auth (=x)</code> access to the credentials is not checked, but rather delegated to the underlying shell script. </p>
<p> The <code>compare</code> operation requires <code>read (=r)</code> access (FIXME: wouldn&#8217;t <code>compare (=c)</code> be a more appropriate choice?) to the <code>entry</code> pseudo-attribute of the object whose value is being asserted; <code>compare (=c)</code> access to the attribute whose value is being asserted is not checked. </p>
<p> The <code>delete</code> operation does not require <code>write (=w)</code> access to the <code>children</code> pseudo-attribute of the parent entry. </p>
<p> The <code>modify</code> operation requires <code>write (=w)</code> access to the <code>entry </code> pseudo-attribute; <code>write (=w)</code> access to the specific attributes that are modified is not checked. </p>
<p> The <code>modrdn</code> operation does not require <code>write (=w)</code> access to the <code>children</code> pseudo-attribute of the parent entry, nor to that of the new parent, if different; <code>write (=w)</code> access to the distinguished values of the naming attributes is not checked. </p>
<p> The <code>search </code> operation does not require <code>search (=s)</code> access to the <code>entry</code> pseudo_attribute of the searchBase; <code>search (=s)</code> access to the attributes and values used in the filter is not checked.</p>
<h2>Example</h2>
<p>There is an example search script in the slapd/back-shell/ directory in the OpenLDAP source tree.</p>
<h2>Limitations</h2>
<p>The shell backend does not support threaded environments. When using the shell backend, <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) should be built <i>&#8211;without-threads</i>.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1). </p>
