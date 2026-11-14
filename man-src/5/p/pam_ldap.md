---
title: "pam_ldap(5)"
name: "pam_ldap"
section: "5"
letter: "p"
url: "/docs/linux/man/5-pam_ldap/"
description: "pam_ldap – LDAP pluggable authentication module"
---

<p>pam_ldap &#8211; LDAP pluggable authentication module</p>
<h2>Description</h2>
<p>The <code>pam_ldap</code> module is a Pluggable Authentication Module (PAM) which provides for authentication, authorization and password changing against <i>LDAP</i> servers. </p>
<p> Features of the PADL pam_ldap module include support for transport layer security, SASL authentication, directory server-enforced password policy, and host- and group- based logon authorization. </p>
<p> The present version of <code>pam_ldap</code> supports AIX 5L, FreeBSD 3.x and above, HP-UX 11i, IRIX 6.x, Linux, Mac OS X 10.2 and above, and Solaris 2.6 and above. Many vendors provide their own LDAP authentication providers, often also called pam_ldap. This manual page applies to the PADL <code>pam_ldap</code> module only. If you are using a vendor provided module, consult the relevant documentation instead. </p>
<p> When authenticating or authorizing a user, <code>pam_ldap</code> first maps the user&#8217;s login name to a distinguished name by searching the directory server. This must be possible using the local system&#8217;s identity, specified in ldap.conf. (Note that presently only simple authentication is supported for authenticating in this initial step.) </p>
<p> To authenticate a user, <code>pam_ldap</code> attempts to bind to the directory server using the distinguished name of the user (retrieved previously). Both simple and SASL authentication mechanisms are supported; in the former case, one should take care to use transport security to prevent the user&#8217;s password being transmitted in the clear. </p>
<p> A variety of authorization primitives are supported by <code>pam_ldap,</code> discussed in the configuration section below. </p>
<p> Finally, <code>pam_ldap</code> supports a number of password change protocols used by directory servers from various vendors. (Some directory servers support more than one password change protocol.) </p>
<p> Whilst <code>pam_ldap</code> is generally configured in the system LDAP naming configuration file (ldap.conf), some options can be configured in the PAM configuration file, to allow for per-service granularity. These options include the path to the LDAP naming configuration file to use, so in effect all options can be configured on a per-service basis. Options are listed below under PAM Configuration.</p>
<h2>Configuration</h2>
<p><code>pam_ldap</code> stores its configuration in the <code>ldap.conf</code> file. (It should be noted that some LDAP client libraries, such as OpenLDAP, also use a configuration file of the same name. <code>pam_ldap</code> supports many of the same configuration file options as OpenLDAP, but it adds several that are specific to the functionality it provides. It is not guaranteed that <code>pam_ldap</code> will continue to match the configuration file semantics of OpenLDAP. You may wish to use different files.) </p>
<p> Configuration file options consist of a keyword followed by a space and any arguments. The following options are supported by both <code>pam_ldap</code> and the PADL <code>nss_ldap</code> module: <code></p>
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
<dt>The following configuration options apply to pam_ldap only:</p>
<dd>
<dt><code>pam_login_attribute &lt;attribute&gt;</code></p>
<dd>Specifies the attribute to use when constructing the attribute value assertion for retrieving a directory entry for a user&#8217;s login name. The default is &quot;uid&quot;, for compatibility with RFC 2307.</p>
<dt><code>pam_filter &lt;filter&gt;</code></p>
<dd>Specifies a filter to use when retrieving user information. The user entry must match the attribute value assertion of (pam_login_attribute=login_name) as well as any filter specified here. There is no default for this option.</p>
<dt><code>pam_lookup_policy &lt;yes|no&gt;</code></p>
<dd>Specifies whether to search the root DSE for password policy. The default is &quot;no&quot;.</p>
<dt><code>pam_check_host_attr &lt;yes|no&gt;</code></p>
<dd>Specifies whether the &quot;host&quot; attribute should be checked for logon authorization (&quot;account&quot; in the PAM stack). The default is not to. If set to &quot;yes&quot; and a user has no value for the &quot;host&quot; attribute, then the user will be unable to login.</p>
<dt><code>pam_check_service_attr &lt;yes|no&gt;</code></p>
<dd>Specifies whether the &quot;authorizedService&quot; attribute should be checked for logon authorization (&quot;account&quot; in the PAM stack). The default is not to. If set to &quot;yes&quot; and a user has no value for the &quot;authorizedService&quot; attribute, then the user will be unable to login.</p>
<dt><code>pam_groupdn &lt;groupdn&gt;</code></p>
<dd>Specifies the distinguished name of a group to which a user must belong for logon authorization to succeed. <code>pam_member_attribute &lt;attribute&gt;</code> Specifies the attribute to use when testing a user&#8217;s membership of a group specified in the <code>pam_groupdn</code> option.</p>
<dt><code>pam_nsrole &lt;role&gt;</code></p>
<dd>Specifies a value which the user&#8217;s entry&#8217;s &quot;nsRole&quot; attribute must match for logon authorization to succeed.</p>
<dt><code>pam_min_uid &lt;uid&gt;</code></p>
<dd>If specified, a user must have a POSIX user ID of at least <code>uid</code> in order for logon authorization to succeed.</p>
<dt><code>pam_max_uid &lt;uid&gt;</code></p>
<dd>If specified, a user must have a POSIX user ID of no greater than <code>uid</code> in order for logon authorization to succeed.</p>
<dt><code>pam_template_login_attribute &lt;attribute&gt;</code></p>
<dd>When using template users (not supported by all PAM applications), specifies the attribute containing the user&#8217;s actual login name. The <code>pam_ldap</code> module will set PAM_USER to the value of this attribute if present in the user&#8217;s entry, otherwise it defaults to the user specified in the <code>pam_template_login</code> option.</p>
<dt><code>pam_template_login &lt;user&gt;</code></p>
<dd>When using template users (not supported by all PAM applications), <code>pam_ldap</code> will set PAM_USER to the value of this option if the user does not contain a template login attribute.</p>
<dt><code>pam_password &lt;protocol&gt;</code></p>
<dd>Specifies the password change protocol to use. The following protocols are supported:</p>
<dl>
<dd>
<dl>
<dt><code>clear</code></p>
<dd>Change password using an LDAPModify request, replacing the userPassword value with the new cleartext password.</p>
<dt><code>clear_remove_old</code></p>
<dd>Change password using an LDAPModify request, first removing the userPassword value containing the old cleartext password, and then adding the userPassword value with the new cleartext password. This protocol is necessary for use with Novell NDS and IBM RACF.</p>
<dt><code>crypt</code></p>
<dd>Change password using an LDAPModify request, first generating a one way hash of the new password using <code><a href="/docs/linux/man/3-crypt/">crypt</a>(3)</code> and then replacing userPassword value with the new hashed password.</p>
<dt><code>md5</code></p>
<dd>Change password using an LDAPModify request, first generating a one way hash of the new password using MD5 and then replacing userPassword value with the new hashed password.</p>
<dt><code>nds</code></p>
<dd>This is an alias for <code>clear_remove_old.</code></p>
<dt><code>racf</code></p>
<dd>This is an alias for <code>clear_remove_old.</code></p>
<dt><code>ad</code></p>
<dd>Change password using an LDAPModify request, using the Active Directory Services Interface (ADSI) password change protocol.</p>
<dt><code>exop</code></p>
<dd>Change password using the RFC 3062 password modify extended operation (only the new password is sent).</p>
<dt><code>exop_send_old</code></p>
<dd>Change password using the RFC 3062 password modify extended operation (both the old and new passwords are sent).</dl>
</dl>
<dt><code>pam_password_prohibit_message &lt;message&gt;</code></p>
<dd>Specifies a message to send to users indicating that passwords cannot be changed. This could be used to redirect users to another means of changing passwords.</p>
<dt><code>pam_sasl_mech &lt;mechanism&gt;</code></p>
<dd>Specifies the SASL mechanism to use for PAM authentication. This requires SASL libraries be installed. Support for this functionality presently experimental and does not support password policy controls.</dl>
<h2>Pam Configuration</h2>
<p>It is possible to configure some aspects of <code>pam_ldap</code> on a per-service basis, in the PAM configuration file (this is usually /etc/pam.conf; for PAM implementations based on Linux-PAM, per-service files in /etc/pam.d are also supported). </p>
<p> The following options may be specified as arguments to the <code>pam_ldap</code> module:</p>
<dl>
<dt><code>config=&lt;path&gt;</code></p>
<dd>Specifies that <code>pam_ldap</code> should use the configuration file in <code>path</code> instead of ldap.conf to retrieve its global configuration. Configuring multiple instances of <code>pam_ldap</code> for the same service with different configuration files is not supported, because the configuration information is cached.</p>
<dt><code>use_first_pass</code></p>
<dd>Specifies that <code>pam_ldap</code> should always use the first password provided in the authentication stack.</p>
<dt><code>try_first_pass</code></p>
<dd>Specifies that <code>pam_ldap</code> should first try the first password provided in the authentication stack, and then prompt the user for their <i>LDAP</i> password if authentication fails.</p>
<dt><code>ignore_unknown_user</code></p>
<dd>Specifies that <code>pam_ldap</code> should return PAM_IGNORE for users that are not present in <i>LDAP.</i> This forces the PAM framework to ignore the <code>pam_ldap</code> module. This option is useful where certain accounts do not reside in <i>LDAP,</i> but one wishes to make <code>pam_ldap</code> &quot;required&quot; for all accounts in the directory. In this case one would make both <code>pam_ldap</code> and the other module (for example, pam_unix) &quot;required&quot; and enable the <code>ignore_unknown_user</code> option. (For this to work, the other module must behave similarly for users in the directory; in the case of a module such as pam_unix that uses the system accounts database, using <code><a href="/docs/linux/man/5-nss_ldap/">nss_ldap</a>(5)</code> should be sufficient to meet this requirement.)</p>
<dt><code>ignore_authinfo_unavail</code></p>
<dd>Specifies that <code>pam_ldap</code> should return PAM_IGNORE if it cannot contact the <i>LDAP</i> server. This option forces the PAM framework to ignore the <code>pam_ldap</code> module in this case.</p>
<dt><code>no_warn</code></p>
<dd>Specifies that warning messages should not be propagated to the PAM application.</p>
<dt><code>use_authtok</code></p>
<dd>Analogous to <code>use_first_pass</code> for password changing only.</p>
<dt><code>debug</code></p>
<dd>This option is recognized by <code>pam_ldap</code> but is presently ignored.</dl>
<h2>Author</h2>
<p>The <code>pam_ldap</code> module was developed by PADL Software Pty Ltd (<a rel="nofollow" href="http://www.padl.com">www.padl.com</a>).</p>
<h2>Files</h2>
<dl>
<dt>/etc/ldap.conf, /etc/ldap.secret, /etc/pam.conf</p>
<dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-pam/">pam</a></code>(8) </p>
