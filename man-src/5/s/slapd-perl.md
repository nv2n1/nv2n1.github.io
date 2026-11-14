---
title: "slapd-perl(5)"
name: "slapd-perl"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-perl/"
description: "slapd-perl – Perl backend to slapd"
---

<p>slapd-perl &#8211; Perl backend to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The Perl backend to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) works by embedding a <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1) interpreter into <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8). Any perl database section of the configuration file <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) must then specify what Perl module to use. <code>Slapd</code> then creates a new Perl object that handles all the requests for that particular instance of the backend. </p>
<p> You will need to create a method for each one of the following actions: </p>
<pre> * new # creates a new object,
 * search # performs the ldap search,
 * compare # does a compare,
 * modify # modifies an entry,
 * add # adds an entry to backend,
 * modrdn # modifies an entry's rdn,
 * delete # deletes an ldap entry,
 * config # module-specific config directives,
 * init # called after backend is initialized.</pre>
<p>Unless otherwise specified, the methods return the result code which will be returned to the client. Unimplemented actions can just return unwillingToPerform (53).</p>
<dl>
<dt><code>new</code></p>
<dd>This method is called when the configuration file encounters a <code>perlmod</code> line. The module in that line is then effectively `use&#8217;d into the perl interpreter, then the <code>new</code> method is called to create a new object. Note that multiple instances of that object may be instantiated, as with any perl object. The <code>new</code> method receives the class name as argument.</p>
<dt><code>search</code></p>
<dd>This method is called when a search request comes from a client. It arguments are as follows: </p>
<pre> * object reference
 * base DN
 * scope
 * alias dereferencing policy
 * size limit
 * time limit
 * filter string
 * attributes only flag (1 for yes)
 * list of attributes to return (may be empty)</pre>
</dl>
<p> Return value: (resultcode, ldif-entry, ldif-entry, &#8230;)</p>
<dl>
<dt><code>compare</code></p>
<dd>This method is called when a compare request comes from a client. Its arguments are as follows. </p>
<pre> * object reference
 * dn
 * attribute assertion string</pre>
</dl>
<dl>
<dt><code>modify</code></p>
<dd>This method is called when a modify request comes from a client. Its arguments are as follows. </p>
<pre> * object reference
 * dn
 * a list formatted as follows
 ({ &quot;ADD&quot; | &quot;DELETE&quot; | &quot;REPLACE&quot; },
 attributetype, value...)...</pre>
</dl>
<dl>
<dt><code>add</code></p>
<dd>This method is called when a add request comes from a client. Its arguments are as follows. </p>
<pre> * object reference
 * entry in string format</pre>
</dl>
<dl>
<dt><code>modrdn</code></p>
<dd>This method is called when a modrdn request comes from a client. Its arguments are as follows. </p>
<pre> * object reference
 * dn
 * new rdn
 * delete old dn flag (1 means yes)</pre>
</dl>
<dl>
<dt><code>delete</code></p>
<dd>This method is called when a delete request comes from a client. Its arguments are as follows. </p>
<pre> * object reference
 * dn</pre>
</dl>
<dl>
<dt><code>config</code></p>
<dd>This method is called once for each perlModuleConfig line in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) configuration file. Its arguments are as follows. </p>
<pre> * object reference
 * array of arguments on line</pre>
</dl>
<p> Return value: nonzero if this is not a valid option.</p>
<dl>
<dt><code>init</code></p>
<dd>This method is called after backend is initialized. Its argument is as follows. </p>
<pre> * object reference</pre>
</dl>
<p> Return value: nonzero if initialization failed.</p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> options apply to the PERL backend database. That is, they must follow a &quot;database perl&quot; line and come before any subsequent &quot;backend&quot; or &quot;database&quot; lines. Other database options are described in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) manual page.</p>
<dl>
<dt><code>perlModulePath /path/to/libs</code></p>
<dd>Add the path to the @INC variable.</p>
<dt><code>perlModule ModName</code></p>
<dd>`Use&#8217; the module name ModName from ModName.pm</p>
<dt><code>filterSearchResults</code></p>
<dd>Search results are candidates that need to be filtered (with the filter in the search request), rather than search results to be returned directly to the client.</p>
<dt><code>perlModuleConfig &lt;arguments&gt;</code></p>
<dd>Invoke the module&#8217;s config method with the given arguments.</dl>
<h2>Example</h2>
<p>There is an example Perl module `SampleLDAP&#8217; in the slapd/back-perl/ directory in the OpenLDAP source tree.</p>
<h2>Access Control</h2>
<p>The <code>perl</code> backend does not honor any of the access control semantics described in <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5); all access control is delegated to the underlying PERL scripting. Only <code>read (=r)</code> access to the <code>entry</code> pseudo-attribute and to the other attribute values of the entries returned by the <code>search</code> operation is honored, which is performed by the frontend.</p>
<h2>Warning</h2>
<p>The interface of this backend to the perl module MAY change. Any suggestions would greatly be appreciated. </p>
<p> Note: in previous versions, any unrecognized lines in the slapd.conf file were passed to the perl module&#8217;s config method. This behavior is deprecated (but still allowed for backward compatibility), and the perlModuleConfig directive should instead be used to invoke the module&#8217;s config method. This compatibility feature will be removed at some future date.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/1-perl/">perl</a></code>(1). </p>
