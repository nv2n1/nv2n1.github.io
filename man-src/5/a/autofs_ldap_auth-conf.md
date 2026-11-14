---
title: "autofs_ldap_auth-conf(5)"
name: "autofs_ldap_auth-conf"
section: "5"
letter: "a"
url: "/docs/linux/man/5-autofs_ldap_auth-conf/"
description: "autofs_ldap_auth.conf – autofs LDAP authentication configuration"
---

<p>autofs_ldap_auth.conf &#8211; autofs LDAP authentication configuration</p>
<h2>Description</h2>
<p>LDAP authenticated binds, TLS encrypted connections and certification may be used by setting appropriate values in the autofs authentication configuration file and configuring the LDAP client with appropriate settings. The default location of this file is <code>/etc/autofs_ldap_auth.conf</code>. If this file exists it will be used to establish whether TLS or authentication should be used. </p>
<p> An example of this file is: </p>
<dl>
<dd>
<pre>&lt;?xml version=&quot;1.0&quot; ?&gt;
&lt;autofs_ldap_sasl_conf
 usetls=&quot;yes&quot;
 tlsrequired=&quot;no&quot;
 authrequired=&quot;no&quot;
 authtype=&quot;DIGEST-MD5&quot;
 user=&quot;xyz&quot;
 secret=&quot;abc&quot;
/&gt;</pre>
</dl>
<p> If TLS encryption is to be used the location of the Certificate Authority certificate must be set within the LDAP client configuration in order to validate the server certificate. If, in addition, a certified connection is to be used then the client certificate and private key file locations must also be configured within the LDAP client.</p>
<h2>Options</h2>
<p>This files contains a single XML element, as shown in the example above, with several attributes.</p>
<dl>
<dt>The possible attributes are:</p>
<dd>
<dt><code>usetls=&quot;yes&quot;|&quot;no&quot;</code></p>
<dd>Determines whether an encrypted connection to the ldap server should be attempted.</p>
<dt><code>tlsrequired=&quot;yes&quot;|&quot;no&quot;</code></p>
<dd>This flag tells whether the ldap connection must be encrypted. If set to &quot;yes&quot;, the automounter will fail to start if an encrypted connection cannot be established.</p>
<dt><code>authrequired=&quot;yes&quot;|&quot;no&quot;|&quot;autodetect&quot;|&quot;simple&quot;</code></p>
<dd>This option tells whether an authenticated connection to the ldap server is required in order to perform ldap queries. If the flag is set to yes, only sasl authenticated connections will be allowed. If it is set to no then authentication is not needed for ldap server connections. If it is set to autodetect then the ldap server will be queried to establish a suitable sasl authentication mechanism. If no suitable mechanism can be found, connections to the ldap server are made without authentication. Finally, if it is set to simple, then simple authentication will be used instead of SASL.</p>
<dt><code>authtype=&quot;GSSAPI&quot;|&quot;LOGIN&quot;|&quot;PLAIN&quot;|&quot;ANONYMOUS&quot;|&quot;DIGEST-MD5|EXTERNAL&quot;</code></p>
<dd>This attribute can be used to specify a preferred authentication mechanism. In normal operations, the automounter will attempt to authenticate to the ldap server using the list of supportedSASLmechanisms obtained from the directory server. Explicitly setting the authtype will bypass this selection and only try the mechanism specified. The EXTERNAL mechanism may be used to authenticate using a client certificate and requires that authrequired set to &quot;yes&quot; if using SSL or usetls, tlsrequired and authrequired all set to &quot;yes&quot; if using TLS, in addition to authtype being set to EXTERNAL. </p>
<p> If using authtype EXTERNAL two additional configuration entries are required: </p>
<p> <code>external_cert=&quot;&lt;client certificate path&gt;&quot;</code> </p>
<p> This specifies the path of the file containing the client certificate. </p>
<p> <code>external_key=&quot;&lt;client certificate key path&gt;&quot;</code> </p>
<p> This specifies the path of the file containing the client certificate key. </p>
<p> These two configuration entries are mandatory when using the EXTERNAL method as the HOME environment variable cannot be assumed to be set or, if it is, to be set to the location we expect.</p>
<dt><code>user=&quot;&lt;username&gt;&quot;</code></p>
<dd>This attribute holds the authentication identity used by authentication mechanisms that require it. Legal values for this attribute include any printable characters that can be used by the selected authentication mechanism.</p>
<dt><code>secret=&quot;&lt;password&gt;&quot;</code></p>
<dd>This attribute holds the secret used by authentication mechanisms that require it. Legal values for this attribute include any printable characters that can be used by the selected authentication mechanism.</p>
<dt><code>encoded_secret=&quot;&lt;base64 encoded password&gt;&quot;</code></p>
<dd>This attribute holds the base64 encoded secret used by authentication mechanisms that require it. If this entry is present as well as the secret entry this value will take precedence.</p>
<dt>
<dt><code>clientprinc=&quot;&lt;GSSAPI client principal&gt;&quot;</code></p>
<dd>
<dd>When using GSSAPI authentication, this attribute is consulted to determine the principal name to use when authenticating to the directory server. By default, this will be set to &quot;autofsclient/&lt;fqdn&gt;@&lt;REALM&gt;.</p>
<dt><code>credentialcache=&quot;&lt;external credential cache path&gt;&quot;</code></p>
<dd>When using GSSAPI authentication, this attribute can be used to specify an externally configured credential cache that is used during authentication. By default, autofs will setup a memory based credential cache.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-auto-master/">auto.master</a></code>(5), <code><a href="/docs/linux/man/5-autofs-conf/">autofs.conf</a></code>(5),</p>
<h2>Author</h2>
<p>This manual page was written by Ian Kent &lt;raven [at] themaw.net&gt;.</p>
