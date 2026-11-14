---
title: "slapo-sock(5)"
name: "slapo-sock"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-sock/"
description: "slapd-sock – Socket backend/overlay to slapd"
---

<p>slapd-sock &#8211; Socket backend/overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The Socket backend to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) uses an external program to handle queries, similarly to <code><a href="/docs/linux/man/5-slapd-shell/">slapd-shell</a></code>(5). However, in this case the external program listens on a Unix domain socket. This makes it possible to have a pool of processes, which persist between requests. This allows multithreaded operation and a higher level of efficiency. The external program must have been started independently; <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) itself will not start it. </p>
<p> This module may also be used as an overlay on top of some other database. Use as an overlay allows external actions to be triggered in response to operations on the main database.</p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> options apply to the SOCK backend database. That is, they must follow a &quot;database sock&quot; line and come before any subsequent &quot;backend&quot; or &quot;database&quot; lines. Other database options are described in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) manual page. </p>
<p> Alternatively, to use this module as an overlay, these directives must follow an &quot;overlay sock&quot; line within an existing database definition.</p>
<dl>
<dt><code>extensions [ binddn | peername | ssf | connid ]*</code></p>
<dd>Enables the sending of additional meta-attributes with each request. </p>
<pre>binddn: &lt;bound DN&gt;
peername: IP=&lt;address&gt;:&lt;port&gt;
ssf: &lt;SSF value&gt;
connid: &lt;connection ID&gt;</pre>
<dt><code>socketpath &lt;pathname&gt;</code></p>
<dd>Gives the path to a Unix domain socket to which the commands will be sent and from which replies are received. </p>
<p> When used as an overlay, these additional directives are defined:</p>
<dt><code>sockops<tt>&nbsp;<wbr></tt>[ bind | unbind | search | compare | modify | modrdn | add | delete ]*</code></p>
<dd>Specify which request types to send to the external program. The default is<br />
 empty (no requests are sent).</p>
<dt><code>sockresps [ result | search ]*</code></p>
<dd>Specify which response types to send to the external program. &quot;result&quot; sends just the results of an operation. &quot;search&quot; sends all entries that the database returned for a search request. The default is empty (no responses are sent). </p>
</dl>
<h2>Protocol</h2>
<p>The protocol is essentially the same as <code><a href="/docs/linux/man/5-slapd-shell/">slapd-shell</a></code>(5) with the addition of a newline to terminate the command parameters. The following commands are sent:</p>
<dl>
<dd>
<pre>ADD
msgid: &lt;message id&gt;
&lt;repeat { &quot;suffix:&quot; &lt;database suffix DN&gt; }&gt;
&lt;entry in LDIF format&gt;
&lt;blank line&gt;</pre>
</dl>
<dl>
<dd>
<pre>BIND
msgid: &lt;message id&gt;
&lt;repeat { &quot;suffix:&quot; &lt;database suffix DN&gt; }&gt;
dn: &lt;DN&gt;
method: &lt;method number&gt;
credlen: &lt;length of &lt;credentials&gt;&gt;
cred: &lt;credentials&gt;
&lt;blank line&gt;</pre>
</dl>
<dl>
<dd>
<pre>COMPARE
msgid: &lt;message id&gt;
&lt;repeat { &quot;suffix:&quot; &lt;database suffix DN&gt; }&gt;
dn: &lt;DN&gt;
&lt;attribute&gt;: &lt;value&gt;
&lt;blank line&gt;</pre>
</dl>
<dl>
<dd>
<pre>DELETE
msgid: &lt;message id&gt;
&lt;repeat { &quot;suffix:&quot; &lt;database suffix DN&gt; }&gt;
dn: &lt;DN&gt;
&lt;blank line&gt;</pre>
</dl>
<dl>
<dd>
<pre>MODIFY
msgid: &lt;message id&gt;
&lt;repeat { &quot;suffix:&quot; &lt;database suffix DN&gt; }&gt;
dn: &lt;DN&gt;
&lt;repeat {
 &lt;&quot;add&quot;/&quot;delete&quot;/&quot;replace&quot;&gt;: &lt;attribute&gt;
 &lt;repeat { &lt;attribute&gt;: &lt;value&gt; }&gt;
 -
}&gt;
&lt;blank line&gt;</pre>
</dl>
<dl>
<dd>
<pre>MODRDN
msgid: &lt;message id&gt;
&lt;repeat { &quot;suffix:&quot; &lt;database suffix DN&gt; }&gt;
dn: &lt;DN&gt;
newrdn: &lt;new RDN&gt;
deleteoldrdn: &lt;0 or 1&gt;
&lt;if new superior is specified: &quot;newSuperior: &lt;DN&gt;&quot;&gt;
&lt;blank line&gt;</pre>
</dl>
<dl>
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
attrs: &lt;&quot;all&quot; or space-separated attribute list&gt;
&lt;blank line&gt;</pre>
</dl>
<dl>
<dd>
<pre>UNBIND
msgid: &lt;message id&gt;
&lt;repeat { &quot;suffix:&quot; &lt;database suffix DN&gt; }&gt;
&lt;blank line&gt;</pre>
</dl>
<p> The commands &#8211; except <code>unbind</code> &#8211; should output:</p>
<dl>
<dd>
<pre>RESULT
code: &lt;integer&gt;
matched: &lt;matched DN&gt;
info: &lt;text&gt;</pre>
</dl>
<p> where only RESULT is mandatory, and then close the socket. The <code>search</code> RESULT should be preceded by the entries in LDIF format, each entry followed by a blank line. Lines starting with `#&#8217; or `DEBUG:&#8217; are ignored. </p>
<p> When used as an overlay, the external program should return a CONTINUE response if request processing should continue normally, or a regular RESULT response if the external program wishes to bypass the underlying database. </p>
<p> If the overlay is configured to send response messages to the external program, they will appear as an extended RESULT message or as an ENTRY message, defined below. The RESULT message is similar to the one above, but also includes the msgid and any configured extensions:</p>
<dl>
<dd>
<pre>RESULT
msgid: &lt;message id&gt;
code: &lt;integer&gt;
matched: &lt;matched DN&gt;
info: &lt;text&gt;
&lt;blank line&gt;</pre>
</dl>
<p> Typically both the msgid and the connid will be needed to match a result message to a request. The ENTRY message has the form</p>
<dl>
<dd>
<pre>ENTRY
msgid: &lt;message id&gt;
&lt;entry in LDIF format&gt;
&lt;blank line&gt;</pre>
</dl>
<h2>Access Control</h2>
<p>The <code>sock</code> backend does not honor all ACL semantics as described in <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5). In general, access to objects is checked by using a dummy object that contains only the DN, so access rules that rely on the contents of the object are not honored. In detail: </p>
<p> The <code>add</code> operation does not require <code>write (=w)</code> access to the <code>children</code> pseudo-attribute of the parent entry. </p>
<p> The <code>bind</code> operation requires <code>auth (=x)</code> access to the <code>entry</code> pseudo-attribute of the entry whose identity is being assessed; <code>auth (=x)</code> access to the credentials is not checked, but rather delegated to the underlying program. </p>
<p> The <code>compare</code> operation requires <code>compare (=c)</code> access to the <code>entry</code> pseudo-attribute of the object whose value is being asserted; <code>compare (=c)</code> access to the attribute whose value is being asserted is not checked. </p>
<p> The <code>delete</code> operation does not require <code>write (=w)</code> access to the <code>children</code> pseudo-attribute of the parent entry. </p>
<p> The <code>modify</code> operation requires <code>write (=w)</code> access to the <code>entry </code> pseudo-attribute; <code>write (=w)</code> access to the specific attributes that are modified is not checked. </p>
<p> The <code>modrdn</code> operation does not require <code>write (=w)</code> access to the <code>children</code> pseudo-attribute of the parent entry, nor to that of the new parent, if different; <code>write (=w)</code> access to the distinguished values of the naming attributes is not checked. </p>
<p> The <code>search </code> operation does not require <code>search (=s)</code> access to the <code>entry</code> pseudo_attribute of the searchBase; <code>search (=s)</code> access to the attributes and values used in the filter is not checked.</p>
<h2>Example</h2>
<p>There is an example script in the slapd/back-sock/ directory in the OpenLDAP source tree.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8).</p>
<h2>Author</h2>
<p>Brian Candler, with enhancements by Howard Chu</p>
