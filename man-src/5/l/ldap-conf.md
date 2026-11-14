---
title: "ldap-conf(5)"
name: "ldap-conf"
section: "5"
letter: "l"
url: "/docs/linux/man/5-ldap-conf/"
description: "ldap.conf, .ldaprc – LDAP configuration file/environment variables"
---

<p>ldap.conf, .ldaprc &#8211; LDAP configuration file/environment variables</p>
<h2>Synopsis</h2>
<p>/etc/ldap/ldap.conf, ldaprc, .ldaprc, $LDAP&lt;option-name&gt;</p>
<h2>Description</h2>
<p>If the environment variable <code>LDAPNOINIT</code> is defined, all defaulting is disabled. </p>
<p> The <i>ldap.conf</i> configuration file is used to set system-wide defaults to be applied when running <i>ldap</i> clients. </p>
<p> Users may create an optional configuration file, <i>ldaprc</i> or <i>.ldaprc</i>, in their home directory which will be used to override the system-wide defaults file. The file <i>ldaprc</i> in the current working directory is also used. </p>
<p> Additional configuration files can be specified using the <code>LDAPCONF</code> and <code>LDAPRC</code> environment variables. <code>LDAPCONF</code> may be set to the path of a configuration file. This path can be absolute or relative to the current working directory. The <code>LDAPRC</code>, if defined, should be the basename of a file in the current working directory or in the user&#8217;s home directory. </p>
<p> Environmental variables may also be used to augment the file based defaults. The name of the variable is the option name with an added prefix of <code>LDAP</code>. For example, to define <code>BASE</code> via the environment, set the variable <code>LDAPBASE</code> to the desired value. </p>
<p> Some options are user-only. Such options are ignored if present in the <i>ldap.conf</i> (or file specified by <code>LDAPCONF</code>). </p>
<p> Thus the following files and variables are read, in order: </p>
<pre> variable $LDAPNOINIT, and if that is not set:
 system file /etc/ldap/ldap.conf,
 user files $HOME/ldaprc, $HOME/.ldaprc, ./ldaprc,
 system file $LDAPCONF,
 user files $HOME/$LDAPRC, $HOME/.$LDAPRC, ./$LDAPRC,
 variables $LDAP&lt;uppercase option name&gt;.</pre>
<p>Settings late in the list override earlier ones.</p>
<h2>Syntax</h2>
<p>The configuration options are case-insensitive; their value, on a case by case basis, may be case-sensitive. </p>
<p> Blank lines are ignored.<br />
 Lines beginning with a hash mark (`#&#8217;) are comments, and ignored. </p>
<p> Valid lines are made of an option&#8217;s name (a sequence of non-blanks, conventionally written in uppercase, although not required), followed by a value. The value starts with the first non-blank character after the option&#8217;s name, and terminates at the end of the line, or at the last sequence of blanks before the end of the line. The tokenization of the value, if any, is delegated to the handler(s) for that option, if any. Quoting values that contain blanks may be incorrect, as the quotes would become part of the value. For example, </p>
<pre> # Wrong - erroneous quotes:
 URI &quot;ldap:// ldaps://&quot;
 # Right - space-separated list of URIs, without quotes:
 URI ldap:// ldaps://
 # Right - DN syntax needs quoting for Example, Inc:
 BASE ou=IT staff,o=&quot;Example, Inc&quot;,c=US
 # or:
 BASE ou=IT staff,o=Example\2C Inc,c=US
 # Wrong - comment on same line as option:
 DEREF never # Never follow aliases</pre>
<p>A line cannot be longer than LINE_MAX, which should be more than 2000 bytes on all platforms. There is no mechanism to split a long line on multiple lines, either for beautification or to overcome the above limit.</p>
<h2>Options</h2>
<p>The different configuration options are:</p>
<dl>
<dt><code>URI &lt;ldap[si]://[name[:port]] &#8230;&gt;</code></p>
<dd>Specifies the URI(s) of an LDAP server(s) to which the <i>LDAP </i> library should connect. The URI scheme may be any of <code>ldap</code>, <code>ldaps </code> or <code>ldapi</code>, which refer to LDAP over TCP, LDAP over SSL (TLS) and LDAP over IPC (UNIX domain sockets), respectively. Each server&#8217;s name can be specified as a domain-style name or an IP address literal. Optionally, the server&#8217;s name can followed by a &#8216;:&#8217; and the port number the LDAP server is listening on. If no port number is provided, the default port for the scheme is used (389 for <a href="ldap://,">ldap://,</a> 636 for <a href="ldaps://">ldaps://</a>). For LDAP over IPC, <code>name </code> is the name of the socket, and no <code>port</code> is required, nor allowed; note that directory separators must be URL-encoded, like any other characters that are special to URLs; so the socket </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>/usr/local/var/ldapi</p>
<p> must be specified as </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><a href="ldapi://%2Fusr%2Flocal%2Fvar%2Fldapi">ldapi://%2Fusr%2Flocal%2Fvar%2Fldapi</a></p>
<p> A space separated list of URIs may be provided.</p>
<dt><code>BASE &lt;base&gt;</code></p>
<dd>Specifies the default base DN to use when performing ldap operations. The base must be specified as a Distinguished Name in LDAP format.</p>
<dt><code>BINDDN &lt;dn&gt;</code></p>
<dd>Specifies the default bind DN to use when performing ldap operations. The bind DN must be specified as a Distinguished Name in LDAP format. <code>This is a user-only option.</code></p>
<dt><code>DEREF &lt;when&gt;</code></p>
<dd>Specifies how alias dereferencing is done when performing a search. The <code>&lt;when&gt;</code> can be specified as one of the following keywords:</p>
<dl>
<dd>
<dl>
<dt><code>never</code></p>
<dd>Aliases are never dereferenced. This is the default.</p>
<dt><code>searching</code></p>
<dd>Aliases are dereferenced in subordinates of the base object, but not in locating the base object of the search.</p>
<dt><code>finding</code></p>
<dd>Aliases are only dereferenced when locating the base object of the search.</p>
<dt><code>always</code></p>
<dd>Aliases are dereferenced both in searching and in locating the base object of the search.</dl>
</dl>
<dt>
<dt><code>HOST &lt;name[:port] &#8230;&gt;</code></p>
<dd>
<dd>Specifies the name(s) of an LDAP server(s) to which the <i>LDAP </i> library should connect. Each server&#8217;s name can be specified as a domain-style name or an IP address and optionally followed by a &#8216;:&#8217; and the port number the ldap server is listening on. A space separated list of hosts may be provided. <code>HOST</code> is deprecated in favor of <code>URI</code>.</p>
<dt><code>KEEPALIVE_IDLE</code></p>
<dd>Sets/gets the number of seconds a connection needs to remain idle before TCP starts sending keepalive probes. Linux only.</p>
<dt><code>KEEPALIVE_PROBES</code></p>
<dd>Sets/gets the maximum number of keepalive probes TCP should send before dropping the connection. Linux only.</p>
<dt><code>KEEPALIVE_INTERVAL</code></p>
<dd>Sets/gets the interval in seconds between individual keepalive probes. Linux only.</p>
<dt><code>NETWORK_TIMEOUT &lt;integer&gt;</code></p>
<dd>Specifies the timeout (in seconds) after which the <a href="/docs/linux/man/2-poll/">poll</a>(2)/<a href="/docs/linux/man/2-select/">select</a>(2) following a <a href="/docs/linux/man/2-connect/">connect</a>(2) returns in case of no activity.</p>
<dt><code>PORT &lt;port&gt;</code></p>
<dd>Specifies the default port used when connecting to LDAP servers(s). The port may be specified as a number. <code>PORT</code> is deprecated in favor of <code>URI.</code></p>
<dt><code>REFERRALS &lt;on/true/yes/off/false/no&gt;</code></p>
<dd>Specifies if the client should automatically follow referrals returned by LDAP servers. The default is on. Note that the command line tools <code><a href="/docs/linux/man/1-ldapsearch/">ldapsearch</a></code>(1) &amp;co always override this option.</p>
<dt><code>SIZELIMIT &lt;integer&gt;</code></p>
<dd>Specifies a size limit (number of entries) to use when performing searches. The number should be a non-negative integer. <i>SIZELIMIT</i> of zero (0) specifies a request for unlimited search size. Please note that the server may still apply any server-side limit on the amount of entries that can be returned by a search operation.</p>
<dt><code>SOCKET_BIND_ADDRESSES &lt;IP&gt;</code></p>
<dd>Specifies the source bind IP to be used for connecting to target LDAP server. Multiple IP addresses must be space separated. Only one valid IPv4 address and/or one valid IPv6 address are allowed in the list.</p>
<dt><code>TIMELIMIT &lt;integer&gt;</code></p>
<dd>Specifies a time limit (in seconds) to use when performing searches. The number should be a non-negative integer. <i>TIMELIMIT</i> of zero (0) specifies unlimited search time to be used. Please note that the server may still apply any server-side limit on the duration of a search operation.</p>
<dt><code>VERSION {2|3}</code></p>
<dd>Specifies what version of the LDAP protocol should be used.</p>
<dt><code>TIMEOUT &lt;integer&gt;</code></p>
<dd>Specifies a timeout (in seconds) after which calls to synchronous LDAP APIs will abort if no response is received. Also used for any <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3) calls where a NULL timeout parameter is supplied.</dl>
<h2>Sasl Options</h2>
<p>If OpenLDAP is built with Simple Authentication and Security Layer support, there are more options you can specify.</p>
<dl>
<dt><code>SASL_MECH &lt;mechanism&gt;</code></p>
<dd>Specifies the SASL mechanism to use.</p>
<dt><code>SASL_REALM &lt;realm&gt;</code></p>
<dd>Specifies the SASL realm.</p>
<dt><code>SASL_AUTHCID &lt;authcid&gt;</code></p>
<dd>Specifies the authentication identity. <code>This is a user-only option.</code></p>
<dt><code>SASL_AUTHZID &lt;authcid&gt;</code></p>
<dd>Specifies the proxy authorization identity. <code>This is a user-only option.</code></p>
<dt><code>SASL_SECPROPS &lt;properties&gt;</code></p>
<dd>Specifies Cyrus SASL security properties. The <code>&lt;properties&gt;</code> can be specified as a comma-separated list of the following:</p>
<dl>
<dd>
<dl>
<dt><code>none</code></p>
<dd>(without any other properties) causes the properties defaults (&quot;noanonymous,noplain&quot;) to be cleared.</p>
<dt><code>noplain</code></p>
<dd>disables mechanisms susceptible to simple passive attacks.</p>
<dt><code>noactive</code></p>
<dd>disables mechanisms susceptible to active attacks.</p>
<dt><code>nodict</code></p>
<dd>disables mechanisms susceptible to passive dictionary attacks.</p>
<dt><code>noanonymous</code></p>
<dd>disables mechanisms which support anonymous login.</p>
<dt><code>forwardsec</code></p>
<dd>requires forward secrecy between sessions.</p>
<dt><code>passcred</code></p>
<dd>requires mechanisms which pass client credentials (and allows mechanisms which can pass credentials to do so).</p>
<dt><code>minssf=&lt;factor&gt; </code></p>
<dd>specifies the minimum acceptable <i>security strength factor</i> as an integer approximate to effective key length used for encryption. 0 (zero) implies no protection, 1 implies integrity protection only, 128 allows RC4, Blowfish and other similar ciphers, 256 will require modern ciphers. The default is 0.</p>
<dt><code>maxssf=&lt;factor&gt; </code></p>
<dd>specifies the maximum acceptable <i>security strength factor</i> as an integer (see <code>minssf</code> description). The default is <code>INT_MAX</code>.</p>
<dt><code>maxbufsize=&lt;factor&gt; </code></p>
<dd>specifies the maximum security layer receive buffer size allowed. 0 disables security layers. The default is 65536.</dl>
</dl>
<dt><code>SASL_NOCANON &lt;on/true/yes/off/false/no&gt;</code></p>
<dd>Do not perform reverse DNS lookups to canonicalize SASL host names. The default is off.</p>
<dt><code>SASL_CBINDING &lt;none/tls-unique/tls-endpoint&gt;</code></p>
<dd>The channel-binding type to use, see also LDAP_OPT_X_SASL_CBINDING. The default is none.</dl>
<h2>Gssapi Options</h2>
<p>If OpenLDAP is built with Generic Security Services Application Programming Interface support, there are more options you can specify.</p>
<dl>
<dt><code>GSSAPI_SIGN &lt;on/true/yes/off/false/no&gt;</code></p>
<dd>Specifies if GSSAPI signing (GSS_C_INTEG_FLAG) should be used. The default is off.</p>
<dt><code>GSSAPI_ENCRYPT &lt;on/true/yes/off/false/no&gt;</code></p>
<dd>Specifies if GSSAPI encryption (GSS_C_INTEG_FLAG and GSS_C_CONF_FLAG) should be used. The default is off.</p>
<dt><code>GSSAPI_ALLOW_REMOTE_PRINCIPAL &lt;on/true/yes/off/false/no&gt;</code></p>
<dd>Specifies if GSSAPI based authentication should try to form the target principal name out of the ldapServiceName or dnsHostName attribute of the targets RootDSE entry. The default is off.</dl>
<h2>Tls Options</h2>
<p>If OpenLDAP is built with Transport Layer Security support, there are more options you can specify. These options are used when an <code>ldaps:// URI</code> is selected (by default or otherwise) or when the application negotiates TLS by issuing the LDAP StartTLS operation.</p>
<dl>
<dt><code>TLS_CACERT &lt;filename&gt;</code></p>
<dd>Specifies the file that contains certificates for all of the Certificate Authorities the client will recognize.</p>
<dt><code>TLS_CACERTDIR &lt;path&gt;</code></p>
<dd>Specifies the path of a directory that contains Certificate Authority certificates in separate individual files. The <code>TLS_CACERT</code> is always used before <code>TLS_CACERTDIR.</code></p>
<dt><code>TLS_CERT &lt;filename&gt;</code></p>
<dd>Specifies the file that contains the client certificate. <code>This is a user-only option.</code></p>
<dt><code>TLS_ECNAME &lt;name&gt;</code></p>
<dd>Specify the name of the curve(s) to use for Elliptic curve Diffie-Hellman ephemeral key exchange. This option is only used for OpenSSL. This option is not used with GnuTLS; the curves may be chosen in the GnuTLS ciphersuite specification.</p>
<dt><code>TLS_KEY &lt;filename&gt;</code></p>
<dd>Specifies the file that contains the private key that matches the certificate stored in the <code>TLS_CERT</code> file. Currently, the private key must not be protected with a password, so it is of critical importance that the key file is protected carefully. <code>This is a user-only option.</code></p>
<dt><code>TLS_CIPHER_SUITE &lt;cipher-suite-spec&gt;</code></p>
<dd>Specifies acceptable cipher suite and preference order. &lt;cipher-suite-spec&gt; should be a cipher specification for the TLS library in use (OpenSSL or GnuTLS). Example:</p>
<dl>
<dd>
<dl>
<dd>
<dl>
<dt><i>OpenSSL:</i></p>
<dd>TLS_CIPHER_SUITE HIGH:MEDIUM:+SSLv2</p>
<dt><i>GnuTLS:</i></p>
<dd>TLS_CIPHER_SUITE SECURE256:!AES-128-CBC</dl>
</dl>
<p> To check what ciphers a given spec selects in OpenSSL, use: </p>
<pre> openssl ciphers -v &lt;cipher-suite-spec&gt;</pre>
<p>With GnuTLS the available specs can be found in the manual page of <code><a href="/docs/linux/man/1-gnutls-cli/">gnutls-cli</a></code>(1) (see the description of the option <code>&#8211;priority</code>). </p>
<p> In older versions of GnuTLS, where gnutls-cli does not support the option &#8211;priority, you can obtain the &#8212; more limited &#8212; list of ciphers by calling: </p>
<pre> gnutls-cli -l</pre>
</dl>
<dt><code>TLS_PROTOCOL_MIN &lt;major&gt;[.&lt;minor&gt;]</code></p>
<dd>Specifies minimum SSL/TLS protocol version that will be negotiated. If the server doesn&#8217;t support at least that version, the SSL handshake will fail. To require TLS 1.x or higher, set this option to 3.(x+1), e.g., </p>
<pre> TLS_PROTOCOL_MIN 3.2</pre>
<p>would require TLS 1.1. Specifying a minimum that is higher than that supported by the OpenLDAP implementation will result in it requiring the highest level that it does support. This parameter is ignored with GnuTLS. On Debian openldap is linked against GnuTLS.</p>
<dt><code>TLS_RANDFILE &lt;filename&gt;</code></p>
<dd>Specifies the file to obtain random bits from when /dev/[u]random is not available. Generally set to the name of the EGD/PRNGD socket. The environment variable RANDFILE can also be used to specify the filename. This parameter is ignored with GnuTLS. On Debian openldap is linked against GnuTLS.</p>
<dt><code>TLS_REQCERT &lt;level&gt;</code></p>
<dd>Specifies what checks to perform on server certificates in a TLS session. The <code>&lt;level&gt;</code> can be specified as one of the following keywords:</p>
<dl>
<dd>
<dl>
<dt><code>never</code></p>
<dd>The client will not request or check any server certificate.</p>
<dt><code>allow</code></p>
<dd>The server certificate is requested. If a bad certificate is provided, it will be ignored and the session proceeds normally.</p>
<dt><code>try</code></p>
<dd>The server certificate is requested. If a bad certificate is provided, the session is immediately terminated.</p>
<dt><code>demand | hard</code></p>
<dd>These keywords are equivalent and the same as <code>try</code>. This is the default setting.</dl>
</dl>
<dt><code>TLS_REQSAN &lt;level&gt;</code></p>
<dd>Specifies what checks to perform on the subjectAlternativeName (SAN) extensions in a server certificate when validating the certificate name against the specified hostname of the server. The <code>&lt;level&gt;</code> can be specified as one of the following keywords:</p>
<dl>
<dd>
<dl>
<dt><code>never</code></p>
<dd>The client will not check any SAN in the certificate.</p>
<dt><code>allow</code></p>
<dd>The SAN is checked against the specified hostname. If a SAN is present but none match the specified hostname, the SANs are ignored and the usual check against the certificate DN is used. This is the default setting.</p>
<dt><code>try</code></p>
<dd>The SAN is checked against the specified hostname. If no SAN is present in the server certificate, the usual check against the certificate DN is used. If a SAN is present but doesn&#8217;t match the specified hostname, the session is immediately terminated. This setting may be preferred when a mix of certs with and without SANs are in use.</p>
<dt><code>demand | hard</code></p>
<dd>These keywords are equivalent. The SAN is checked against the specified hostname. If no SAN is present in the server certificate, or no SANs match, the session is immediately terminated. This setting should be used when only certificates with SANs are in use.</dl>
</dl>
<dt><code>TLS_CRLCHECK &lt;level&gt;</code></p>
<dd>Specifies if the Certificate Revocation List (CRL) of the CA should be used to verify if the server certificates have not been revoked. This requires <code>TLS_CACERTDIR</code> parameter to be set. This parameter is ignored with GnuTLS. On Debian openldap is linked against GnuTLS. <code>&lt;level&gt;</code> can be specified as one of the following keywords:</p>
<dl>
<dd>
<dl>
<dt><code>none</code></p>
<dd>No CRL checks are performed</p>
<dt><code>peer</code></p>
<dd>Check the CRL of the peer certificate</p>
<dt><code>all</code></p>
<dd>Check the CRL for a whole certificate chain</dl>
</dl>
<dt><code>TLS_CRLFILE &lt;filename&gt;</code></p>
<dd>Specifies the file containing a Certificate Revocation List to be used to verify if the server certificates have not been revoked. This parameter is only supported with GnuTLS.</dl>
<h2>Environment Variables</h2>
<dl>
<dt>LDAPNOINIT</p>
<dd>disable all defaulting</p>
<dt>LDAPCONF</p>
<dd>path of a configuration file</p>
<dt>LDAPRC</p>
<dd>basename of ldaprc file in $HOME or $CWD</p>
<dt>LDAP&lt;option-name&gt;</p>
<dd>Set &lt;option-name&gt; as from ldap.conf</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/ldap/ldap.conf</i></p>
<dd>system-wide ldap configuration file</p>
<dt><i>$HOME/ldaprc, $HOME/.ldaprc</i></p>
<dd>user ldap configuration file</p>
<dt><i>$CWD/ldaprc</i></p>
<dd>local ldap configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/3-ldap_set_option/">ldap_set_option</a></code>(3), <code><a href="/docs/linux/man/3-ldap_result/">ldap_result</a></code>(3), <code><a href="/docs/linux/man/1-openssl/">openssl</a></code>(1), <code><a href="/docs/linux/man/3-sasl/">sasl</a></code>(3)</p>
<h2>Author</h2>
<p>Kurt Zeilenga, The OpenLDAP Project</p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from the University of Michigan LDAP 3.3 Release.</p>
