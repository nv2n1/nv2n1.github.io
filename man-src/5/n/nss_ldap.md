---
title: "nss_ldap(5)"
name: "nss_ldap"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nss_ldap/"
description: "nss_ldap – LDAP nameservice provider"
---

<p>nss_ldap &#8211; LDAP nameservice provider</p>
<h2>Description</h2>
<p>The <code>nss_ldap</code> module is a set of C library extensions which allows X.500 and LDAP directory servers to be used as a primary source of name service information. (Name service information typically includes users, hosts, groups, and other such data historically stored in flat files or NIS.) </p>
<p> Features of the PADL nss_ldap module include support for both the RFC 2307 and RFC 2307bis schema, a common implementation across multiple platforms, Kerberos and SSL security, configurable schema mapping, and configuration file compatibility with the <code><a href="/docs/linux/man/5-pam_ldap/">pam_ldap</a></code>(5) module. </p>
<p> Because LDAP is a hierarchical directory service, one can distribute the information in a manner which reflects organizational structure. This contrasts with the flat, single domain policy of NIS. LDAP has many of the advantages of NIS+ (security and scalability) without the complexity. </p>
<p> <code>nss_ldap</code> will work alongside existing NIS, NIS+, DNS and flat file name services. More importantly, because it builds as a shared library, it is not necessary to recompile any applications to take advantage of LDAP. </p>
<p> The present version of <code>nss_ldap</code> supports AIX 4.3.3 and above, FreeBSD 5.1, HP-UX 11i, Linux and Solaris 2.6 and above. Many vendors provide their own LDAP nameservice providers, often also called nss_ldap. This manual page applies to the PADL <code>nss_ldap</code> module only. If you are using a vendor provided module, consult the relevant documentation instead. </p>
<p> The features supported by the version of <code>nss_ldap</code> depend on which flags were enabled when the software was built. Most features are enabled in the configuration file, described below. (The location of the configuration file is configurable at compile time; the default path is /etc/ldap.conf.) Also, some features may be unavailable on certain operating systems or with certain LDAP libraries. For more information, consult your vendor.</p>
<h2>Configuration</h2>
<p><code>nss_ldap</code> stores its configuration in the <code>ldap.conf</code> file, the location of which is configurable at compile time. (It should be noted that some LDAP client libraries, such as OpenLDAP, also use a configuration file of the same name. <code>nss_ldap</code> supports many of the same configuration file options as OpenLDAP, but it adds several that are specific to the functionality it provides. Additionally, it is not guaranteed that <code>nss_ldap</code> will continue to match the configuration file semantics of OpenLDAP. You may wish to use different files.) </p>
<p> Configuration file options consist of a keyword followed by a space and any arguments. The following options are supported by both <code>nss_ldap</code> and the PADL <code>pam_ldap</code> module: <code></p>
<dl>
<dt>host &lt;name:port &#8230;&gt;</code></p>
<dd>Specifies the name(s) or IP address(es) of the <i>LDAP</i> server(s) to connect to. In the case that <code>nss_ldap</code> is used for host name resolution, each server should be specified as an IP address or name that can be resolved without using <i>LDAP.</i> Multiple servers may be specified, each separated by a space. The failover time depends on whether the <i>LDAP</i> client library supports configurable network or connect timeouts (see <code>bind_timelimit</code> below).</p>
<dt><code>base &lt;base&gt;</code></p>
<dd>Specifies the default base distinguished name (DN) to use for searches.</p>
<dt><code>uri &lt;ldap[is]://[name[:port]] &#8230;&gt;</code></p>
<dd>For <i>LDAP</i> client libraries that support it, specifies the URI(s) of the LDAP server(s) to connect to. The URI scheme may be <code>ldap,</code> <code>ldapi,</code> or <code>ldaps,</code> specifying LDAP over TCP, IPC and SSL respectively. If applicable, a port number can be specified; the default port number for the selected protocol is used if omitted. This option takes precedence over the <code>host</code> option; it is not possible to combine the two.</p>
<dt><code>ldap_version &lt;version&gt;</code></p>
<dd>Specifies the version of the <i>LDAP</i> protocol to use. Presently <code>version</code> must be 2 or 3. The default is to use the maximum version supported by the client library.</p>
<dt><code>binddn &lt;binddn&gt;</code></p>
<dd>Specifies the distinguished name with which to bind to the directory server(s). This option is optional; the default is to bind anonymously.</p>
<dt><code>bindpw &lt;bindpw&gt;</code></p>
<dd>Specifies the cleartext credentials with which to bind. This option is only applicable when used with <code>binddn</code> above. The default is no credential (anonymous bind). When binding to the directory using <i>SASL</i> or other authentication mechanisms apart from simple binds, this option is not used.</p>
<dt><code>rootbinddn &lt;binddn&gt;</code></p>
<dd>This option has the same syntax and effect as the <code>binddn</code> option above, except it applies when the effective user ID is zero. If not specified, then the identity specified in <code>binddn</code> is used instead. Because the configuration file may be readable by many users, the root bind DN credentials are stored in the <code>ldap.secret</code> file instead. This file is usually in the same directory as the configuration file.</p>
<dt><code>port &lt;port&gt;</code></p>
<dd>Specifies the port to connect to; this option is used with the <code>host</code> option, and is ignored with the <code>uri</code> option.</p>
<dt><code>scope &lt;sub|one|base&gt;</code></p>
<dd>Specifies the search scope (subtree, one level or base object). The default scope is subtree; base scope is almost never useful for nameservice lookups.</p>
<dt><code>deref &lt;never|searching|finding|always&gt;</code></p>
<dd>Specifies the policy for dereferencing aliases. The default policy is to never dereference aliases.</p>
<dt><code>timelimit &lt;timelimit&gt;</code></p>
<dd>Specifies the time limit (in seconds) to use when performing searches. A value of zero (0), which is the default, is to wait indefinitely for searches to be completed.</p>
<dt><code>bind_timelimit &lt;timelimit&gt;</code></p>
<dd>Specifies the time limit (in seconds) to use when connecting to the directory server. This is distinct from the time limit specified in <code>timelimit</code> and affects the initial server connection only. (Server connections are otherwise cached.) Only some <i>LDAP</i> client libraries have the underlying functionality necessary to support this option. The default bind timelimit is 30 seconds.</p>
<dt><code>referrals &lt;yes|no&gt;</code></p>
<dd>Specifies whether automatic referral chasing should be enabled. The default behaviour is specifed by the <i>LDAP</i> client library.</p>
<dt><code>restart &lt;yes|no&gt;</code></p>
<dd>Specifies whether the <i>LDAP</i> client library should restart the <code><a href="/docs/linux/man/2-select/">select</a>(2)</code> system call when interrupted. This feature is not supported by all client libraries.</p>
<dt><code>logdir &lt;directory&gt;</code></p>
<dd>Specifies the directory used for logging by the <i>LDAP</i> client library. This feature is not supported by all client libraries.</p>
<dt><code>debug &lt;level&gt;</code></p>
<dd>Specifies the debug level used for logging by the <i>LDAP</i> client library. This feature is not supported by all client libraries, and does not apply to the <code>nss_ldap</code> and <code>pam_ldap</code> modules themselves (debugging, if any, is configured separately and usually at compile time).</p>
<dt><code>ssl &lt;on|off|start_tls&gt;</code></p>
<dd>Specifies whether to use SSL/TLS or not (the default is not to). If <code>start_tls</code> is specified then StartTLS is used rather than raw LDAP over SSL. Not all <i>LDAP</i> client libraries support both SSL and StartTLS, and all related configuration options.</p>
<dt><code>sslpath &lt;cert7_path&gt;</code></p>
<dd>For the Netscape and Mozilla <i>LDAP</i> client libraries only, this specifies the path to the X.509 certificate database.</p>
<dt><code>tls_checkpeer &lt;yes|no&gt;</code></p>
<dd>Specifies whether to require and verify the server certificate or not, when using SSL/TLS with the OpenLDAP client library. The default is to use the default behaviour of the client library; for OpenLDAP 2.0 and earlier it is &quot;no&quot;, for OpenLDAP 2.1 and later it is &quot;yes&quot;. At least one of <code>tls_cacertdir</code> and <code>tls_cacertfile</code> is required if peer verification is enabled.</p>
<dt><code>tls_cacertdir &lt;certificate_dir&gt;</code></p>
<dd>Specifies the directory containing X.509 certificates for peer authentication.</p>
<dt><code>tls_cacertfile &lt;certificate_file&gt;</code></p>
<dd>Specifies the path to the X.509 certificate for peer authentication.</p>
<dt><code>tls_randfile &lt;entropy_file&gt;</code></p>
<dd>Specifies the path to an entropy source.</p>
<dt><code>tls_ciphers &lt;ciphers&gt;</code></p>
<dd>Specifies the ciphers to use for TLS. See your TLS implementation&#8217;s documentation for further information.</p>
<dt><code>tls_cert &lt;certificate_file&gt;</code></p>
<dd>Specifies the path to the file containing the local certificate for client TLS authentication.</p>
<dt><code>tls_key &lt;key_file&gt;</code></p>
<dd>Specifies the path to the file containing the private key for client TLS authentication.</p>
<dt>The following configuration options apply to nss_ldap only:</p>
<dd>
<dt><code>bind_policy &lt;hard_open|hard_init|soft&gt;</code></p>
<dd>Specifies the policy to use for reconnecting to an unavailable <i>LDAP</i> server. The default is <code>hard_open,</code> which reconnects if opening the connection to the directory server failed. By contrast, <code>hard_init</code> reconnects if initializing the connection failed. Initializing may not actually contact the directory server, and it is possible that a malformed configuration file will trigger reconnection. If <code>soft</code> is specified, then <code>nss_ldap</code> will return immediately on server failure. All &quot;hard&quot; reconnect policies block with exponential backoff before retrying.</p>
<dt><code>nss_connect_policy &lt;persist|oneshot&gt;</code></p>
<dd>Determines whether nss_ldap persists connections. The default is for the connection to the LDAP server to remain open after the first request.</p>
<dt><code>idle_timelimit &lt;timelimit&gt;</code></p>
<dd>Specifies the time (in seconds) after which <code>nss_ldap</code> will close connections to the directory server. The default is not to time out connections.</p>
<dt><code>sasl_authid &lt;authid&gt;</code></p>
<dd>Specifies the authorization identity to be used when performing SASL authentication.</p>
<dt><code>rootsasl_auth_id &lt;authid&gt;</code></p>
<dd>Specifies the authorization identity to be used when performing SASL authentication as root (when the effective user ID is zero).</p>
<dt><code>sasl_secprops &lt;properties&gt;</code></p>
<dd>Specifies Cyrus SASL security properties. Allowed values are described in the <code><a href="/docs/linux/man/5-ldap-conf/">ldap.conf</a>(5)</code> manual page.</p>
<dt><code>rootuse_sasl &lt;yes|no&gt;</code></p>
<dd>Specifies whether SASL authentication should be used when the effective user ID is zero.</p>
<dt><code>krb5_ccname &lt;PREFIX:args&gt;</code></p>
<dd>If <code>nss_ldap</code> is built with configurable GSS-API credentials cache name support, specifies the Kerberos credentials cache to use.</p>
<dt><code>nss_paged_results &lt;yes|no&gt;</code></p>
<dd><code>Enables</code>support<code>for</code>paged<code>results.</code></p>
<dt><code>pagesize &lt;pagesize&gt;</code></p>
<dd>When paged results are enabled (see above), specifies the number of entries to return in a single page. The default is 1000.</p>
<dt><code>nss_base_&lt;map&gt; &lt;basedn?scope?filter&gt;</code></p>
<dd>Specify the search base, scope and filter to be used for specific maps. (Note that <code>map</code> forms part of the configuration file keyword and is one of passwd, shadow, group, hosts, services, networks, protocols, rpc, ethers, netmasks, bootparams, aliases and netgroup.) The syntax of <code>basedn</code> and <code>scope</code> are the same as for the configuration file options of the same name, with the addition of being able to omit the trailing suffix of the base DN (in which case the global base DN will be appended instead). The <code>filter</code> is a search filter to be added to the default search filter for a specific map, such that the effective filter is the logical intersection of the two. The base DN, scope and filter are separated with literal question marks (?) as given above; this is for compatibility with the DUA configuration profile schema and the <code>ldapprofile</code> tool. This option may be specified multiple times.</p>
<dt><code>nss_map_attribute &lt;from_attribute&gt; &lt;to_attribute&gt;</code></p>
<dd>This option may be specified multiple times, and directs <code>nss_ldap</code> to use the attribute <code>to_attribute</code> instead of the RFC 2307 attribute <code>from_attribute</code> in all lookups. If <code>nss_ldap</code> was built without schema mapping support, then this option is ignored.</p>
<dt><code>nss_map_objectclass &lt;from_objectclass&gt; &lt;to_objectclass&gt;</code></p>
<dd>This option may be specified multiple times, and directs <code>nss_ldap</code> to use the object class <code>to_objectclass</code> instead of the RFC 2307 object class <code>from_objectclass</code> in all lookups. If <code>nss_ldap</code> was built without schema mapping support, then this option is ignored.</p>
<dt><code>nss_default_attribute_value &lt;attribute&gt; &lt;value&gt;</code></p>
<dd>Specifies the default value to use for entries that lack the specified attribute. This option may be specified multiple times, for different attributes. If <code>nss_ldap</code> was built without schema mapping support, then this option is ignored.</p>
<dt><code>nss_override_attribute_value &lt;attribute&gt; &lt;value&gt;</code></p>
<dd>Specifies a value to use for the specified attribute in preference to that contained in the actual entry. This option may be specified multiple times, for different attributes. If <code>nss_ldap</code> was built without schema mapping support, then this option is ignored.</p>
<dt><code>nss_schema &lt;rfc2307bis|rfc2307&gt;</code></p>
<dd>If the value of this option is <code>rfc2307bis</code> then support for the RFC2307bis schema (distinguished names in groups) will be enabled.</p>
<dt><code>nss_initgroups &lt;backlink&gt;</code></p>
<dd>This option directs the <code>nss_ldap</code> implementation of <code><a href="/docs/linux/man/3-initgroups/">initgroups</a>(3)</code> to determine a user&#8217;s group membership by reading the memberOf attribute of their directory entry (and of any nested groups), rather than querying on uniqueMember. This may provide increased performance with certain directory servers that have peculiar indexing configurations. If RFC2307bis support is disabled, then this option is ignored.</p>
<dt><code>nss_initgroups_ignoreusers &lt;user1,user2,&#8230;,userN&gt;</code></p>
<dd>This option directs the <code>nss_ldap</code> implementation of <code><a href="/docs/linux/man/3-initgroups/">initgroups</a>(3)</code> to return NSS_STATUS_NOTFOUND if called with a listed users as its argument.</p>
<dt><code>nss_initgroups_minimum_uid &lt;uid&gt;</code></p>
<dd>This option directs the <code>nss_ldap</code> implementation of <code><a href="/docs/linux/man/3-initgroups/">initgroups</a>(3)</code> to return NSS_STATUS_NOTFOUND if called with a user whose UID is below the value given as the argument.</p>
<dt><code>nss_getgrent_skipmembers &lt;yes|no&gt;</code></p>
<dd>Specifies whether or not to populate the members list in the group structure for group lookups. If very large groups are present, enabling this option will greatly increase perforance, at the cost of some lost functionality. You should verify no local applications rely on this information before enabling this on a production system.</p>
<dt><code>nss_srv_domain &lt;domain&gt;</code></p>
<dd>This option determines the DNS domain used for performing SRV lookups.</dl>
<h2>Author</h2>
<p>The <code>nss_ldap</code> module was developed by PADL Software Pty Ltd (<a rel="nofollow" href="http://www.padl.com">www.padl.com</a>).</p>
<h2>Files</h2>
<dl>
<dt>/etc/ldap.conf, /etc/ldap.secret, /etc/nsswitch.conf</p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5) </p>
