---
title: "nslcd-conf(5)"
name: "nslcd-conf"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nslcd-conf/"
description: "nslcd.conf – configuration file for LDAP nameservice daemon"
---

<p>nslcd.conf &#8211; configuration file for LDAP nameservice daemon</p>
<h2>Description</h2>
<p>The <i>nss-pam-ldapd</i> package allows LDAP directory servers to be used as a primary source of name service information. (Name service information typically includes users, hosts, groups, and other such data historically stored in flat files or NIS.) </p>
<p> The file <i>nslcd.conf</i> contains the configuration information for running <code>nslcd</code> (see <code><a href="/docs/linux/man/8-nslcd/">nslcd</a></code>(8)). The file contains options, one on each line, defining the way NSS lookups and PAM actions are mapped to LDAP lookups.</p>
<h2>Options</h2>
<h3>Runtime Options</h3>
<dl>
<dt><code>threads</code> <i>NUM</i></p>
<dd>Specifies the number of threads to start that can handle requests and perform LDAP queries. Each thread opens a separate connection to the LDAP server. The default is to start 5 threads.</p>
<dt><code>uid</code> <i>UID</i></p>
<dd>This specifies the user id with which the daemon should be run. This can be a numerical id or a symbolic value. If no uid is specified no attempt to change the user will be made. Note that you should use values that don&#8217;t need LDAP to resolve.</p>
<dt><code>gid</code> <i>GID</i></p>
<dd>This specifies the group id with which the daemon should be run. This can be a numerical id or a symbolic value. If no gid is specified no attempt to change the group will be made. Note that you should use values that don&#8217;t need LDAP to resolve.</dl>
<h3>General Connection Options</h3>
<dl>
<dt><code>uri</code> <i>URI</i></p>
<dd>Specifies the LDAP URI of the server to connect to. The URI scheme may be ldap, ldapi or ldaps, specifying LDAP over TCP, ICP or SSL respectively (if supported by the LDAP library). </p>
<p> Alternatively, the value DNS may be used to try to lookup the server using DNS SRV records. By default the current domain is used but another domain can be queried by using the DNS:<i>DOMAIN</i> syntax. </p>
<p> When using the ldapi scheme, %2f should be used to escape slashes (e.g. <a href="ldapi://%2fvar%2frun%2fslapd%2fldapi/">ldapi://%2fvar%2frun%2fslapd%2fldapi/</a>), although most of the time this should not be needed. </p>
<p> This option may be specified multiple times. Normally, only the first server will be used with the following servers as fall-back (see <code>bind_timelimit</code> below). </p>
<p> If LDAP lookups are used for host name resolution, any host names should be specified as an IP address or name that can be resolved without using LDAP.</p>
<dt><code>ldap_version</code> <i>VERSION</i></p>
<dd>Specifies the version of the LDAP protocol to use. The default is to use the maximum version supported by the LDAP library.</p>
<dt><code>binddn</code> <i>DN</i></p>
<dd>Specifies the distinguished name with which to bind to the directory server for lookups. The default is to bind anonymously.</p>
<dt><code>bindpw</code> <i>PASSWORD</i></p>
<dd>Specifies the credentials with which to bind. This option is only applicable when used with <code>binddn</code> above. If you set this option you should consider changing the permissions of the <i>nslcd.conf</i> file to only grant access to the root user.</p>
<dt><code>rootpwmoddn</code> <i>DN</i></p>
<dd>Specifies the distinguished name to use when the root user tries to modify a user&#8217;s password using the PAM module.</p>
<dt><code>rootpwmodpw</code> <i>PASSWORD</i></p>
<dd>Specifies the credentials with which to bind if the root user tries to change a user&#8217;s password. This option is only applicable when used with <code>rootpwmoddn</code> above. If this option is not specified the PAM module prompts the user for this password. If you set this option you should consider changing the permissions of the <i>nslcd.conf</i> file to only grant access to the root user.</dl>
<h3>Sasl Authentication Options</h3>
<dl>
<dt><code>sasl_mech</code> <i>MECHANISM</i></p>
<dd>Specifies the SASL mechanism to be used when performing SASL authentication.</p>
<dt><code>sasl_realm</code> <i>REALM</i></p>
<dd>Specifies the SASL realm to be used when performing SASL authentication.</p>
<dt><code>sasl_authcid</code> <i>AUTHCID</i></p>
<dd>Specifies the authentication identity to be used when performing SASL authentication.</p>
<dt><code>sasl_authzid</code> <i>AUTHZID</i></p>
<dd>Specifies the authorization identity to be used when performing SASL authentication. Must be specified in one of the formats: dn:&lt;distinguished name&gt; or u:&lt;username&gt;.</p>
<dt><code>sasl_secprops</code> <i>PROPERTIES</i></p>
<dd>Specifies Cyrus SASL security properties. Allowed values are described in the <code><a href="/docs/linux/man/5-ldap-conf/">ldap.conf</a></code>(5) manual page.</p>
<dt><code>sasl_canonicalize</code> yes|no</p>
<dd>Determines whether the LDAP server host name should be canonicalised. If this is set to yes the LDAP library will do a reverse host name lookup. By default, it is left up to the LDAP library whether this check is performed or not.</dl>
<h3>Kerberos Authentication Options</h3>
<dl>
<dt><code>krb5_ccname</code> <i>NAME</i></p>
<dd>Set the name for the GSS-API Kerberos credentials cache.</dl>
<h3>Search/Mapping Options</h3>
<dl>
<dt><code>base</code> [<i>MAP</i>] <i>DN</i></p>
<dd>Specifies the base distinguished name (DN) to use as search base. This option may be supplied multiple times and all specified bases will be searched. </p>
<p> A global search base may be specified or a MAP-specific one. If no MAP-specific search bases are defined the global ones are used. </p>
<p> If, instead of a DN, the value <i>DOMAIN</i> is specified, the host&#8217;s DNS domain is used to construct a search base. </p>
<p> If this value is not defined an attempt is made to look it up in the configured LDAP server. Note that if the LDAP server is unavailable during start-up <code>nslcd</code> will not start.</p>
<dt><code>scope</code> [<i>MAP</i>] sub[tree]|one[level]|base</p>
<dd>Specifies the search scope (subtree, one level or base object). The default scope is subtree; base scope is almost never useful for name service lookups.</p>
<dt><code>deref</code> never|searching|finding|always</p>
<dd>Specifies the policy for dereferencing aliases. The default policy is to never dereference aliases.</p>
<dt><code>referrals</code> yes|no</p>
<dd>Specifies whether automatic referral chasing should be enabled. The default behaviour is to chase referrals.</p>
<dt><code>filter</code> <i>MAP</i> <i>FILTER</i></p>
<dd>The <i>FILTER</i> is an LDAP search filter to use for a specific map. The default filter is a basic search on the objectClass for the map (e.g. (objectClass=posixAccount)).</p>
<dt><code>map</code> <i>MAP</i> <i>ATTRIBUTE</i> <i>NEWATTRIBUTE</i></p>
<dd>This option allows for custom attributes to be looked up instead of the default RFC 2307 attributes. The <i>MAP</i> may be one of the supported maps below. The <i>ATTRIBUTE</i> is the one as used in RFC 2307 (e.g. userPassword, ipProtocolNumber, macAddress, etc.). The <i>NEWATTRIBUTE</i> may be any attribute as it is available in the directory. </p>
<p> If the <i>NEWATTRIBUTE</i> is presented in quotes (&quot;) it is treated as an expression which will be evaluated to build up the actual value used. See the section on attribute mapping expressions below for more details. </p>
<p> Only some attributes for group, passwd and shadow entries may be mapped with an expression (because other attributes may be used in search filters). For group entries only the userPassword attribute may be mapped with an expression. For passwd entries the following attributes may be mapped with an expression: userPassword, gidNumber, gecos, homeDirectory and loginShell. For shadow entries the following attributes may be mapped with an expression: userPassword, shadowLastChange, shadowMin, shadowMax, shadowWarning, shadowInactive, shadowExpire and shadowFlag. </p>
<p> The uidNumber and gidNumber attributes in the passwd and group maps may be mapped to the objectSid followed by the domain SID to derive numeric user and group ids from the SID (e.g. objectSid:S-1-5-21-3623811015-3361044348-30300820). </p>
<p> By default all userPassword attributes are mapped to the unmatchable password (&quot;*&quot;) to avoid accidentally leaking password information.</dl>
<h3>Timing/Reconnect Options</h3>
<dl>
<dt><code>bind_timelimit</code> <i>SECONDS</i></p>
<dd>Specifies the time limit (in seconds) to use when connecting to the directory server. This is distinct from the time limit specified in <code>timelimit</code> and affects the set-up of the connection only. Note that not all LDAP client libraries have support for setting the connection time out. The default <code>bind_timelimit</code> is 10 seconds.</p>
<dt><code>timelimit</code> <i>SECONDS</i></p>
<dd>Specifies the time limit (in seconds) to wait for a response from the LDAP server. A value of zero (0), which is the default, is to wait indefinitely for searches to be completed.</p>
<dt><code>idle_timelimit</code> <i>SECONDS</i></p>
<dd>Specifies the period if inactivity (in seconds) after which the connection to the LDAP server will be closed. The default is not to time out connections.</p>
<dt><code>reconnect_sleeptime</code> <i>SECONDS</i></p>
<dd>Specifies the number of seconds to sleep when connecting to all LDAP servers fails. By default 1 second is waited between the first failure and the first retry.</p>
<dt><code>reconnect_retrytime</code> <i>SECONDS</i></p>
<dd>Specifies the time after which the LDAP server is considered to be permanently unavailable. Once this time is reached retries will be done only once per this time period. The default value is 10 seconds.</dl>
<p> Note that the reconnect logic as described above is the mechanism that is used between <code>nslcd</code> and the LDAP server. The mechanism between the NSS and PAM client libraries on one end and <code>nslcd</code> on the other is simpler with a fixed compiled-in time out of a 10 seconds for writing to <code>nslcd</code> and a time out of 60 seconds for reading answers. <code>nslcd</code> itself has a read time out of 0.5 seconds and a write time out of 60 seconds.</p>
<h3>Ssl/Tls Options</h3>
<dl>
<dt><code>ssl</code> on|off|start_tls</p>
<dd>Specifies whether to use SSL/TLS or not (the default is not to). If <i>start_tls</i> is specified then StartTLS is used rather than raw LDAP over SSL. Not all LDAP client libraries support both SSL, StartTLS and all related configuration options.</p>
<dt><code>tls_reqcert</code> never|allow|try|demand|hard</p>
<dd>Specifies what checks to perform on a server-supplied certificate. The meaning of the values is described in the <code><a href="/docs/linux/man/5-ldap-conf/">ldap.conf</a></code>(5) manual page. At least one of <code>tls_cacertdir</code> and <code>tls_cacertfile</code> is required if peer verification is enabled.</p>
<dt><code>tls_cacertdir</code> <i>PATH</i></p>
<dd>Specifies the directory containing X.509 certificates for peer authentication. This parameter is ignored when using GnuTLS. On Debian OpenLDAP is linked against GnuTLS.</p>
<dt><code>tls_cacertfile</code> <i>PATH</i></p>
<dd>Specifies the path to the X.509 certificate for peer authentication.</p>
<dt><code>tls_randfile</code> <i>PATH</i></p>
<dd>Specifies the path to an entropy source. This parameter is ignored when using GnuTLS. On Debian OpenLDAP is linked against GnuTLS.</p>
<dt><code>tls_ciphers</code> <i>CIPHERS</i></p>
<dd>Specifies the ciphers to use for TLS. See your TLS implementation&#8217;s documentation for further information.</p>
<dt><code>tls_cert</code> <i>PATH</i></p>
<dd>Specifies the path to the file containing the local certificate for client TLS authentication.</p>
<dt><code>tls_key</code> <i>PATH</i></p>
<dd>Specifies the path to the file containing the private key for client TLS authentication.</dl>
<h3>Other Options</h3>
<dl>
<dt><code>pagesize</code> <i>NUMBER</i></p>
<dd>Set this to a number greater than 0 to request paged results from the LDAP server in accordance with RFC2696. The default (0) is to not request paged results. </p>
<p> This is useful for LDAP servers that contain a lot of entries (e.g. more than 500) and limit the number of entries that are returned with one request. For OpenLDAP servers you may need to set <code>sizelimit size.prtotal=unlimited</code> for allowing more entries to be returned over multiple pages.</p>
<dt><code>nss_initgroups_ignoreusers</code> user1,user2,&#8230;</p>
<dd>This option prevents group membership lookups through LDAP for the specified users. This can be useful in case of unavailability of the LDAP server. This option may be specified multiple times. </p>
<p> Alternatively, the value ALLLOCAL may be used. With that value nslcd builds a full list of non-LDAP users on startup.</p>
<dt><code>nss_min_uid</code> <i>UID</i></p>
<dd>This option ensures that LDAP users with a numeric user id lower than the specified value are ignored. Also requests for users with a lower user id are ignored.</p>
<dt><code>validnames</code> <i>REGEX</i></p>
<dd>This option can be used to specify how user and group names are verified within the system. This pattern is used to check all user and group names that are requested and returned from LDAP. </p>
<p> The regular expression should be specified as a POSIX extended regular expression. The expression itself needs to be separated by slash (/) characters and the &#8216;i&#8217; flag may be appended at the end to indicate that the match should be case-insensetive. The default value is /^[a-z0-9._@$][a-z0-9._@$ \~-]*[a-z0-9._@$~-]$/i</p>
<dt><code>ignorecase</code> yes|no</p>
<dd>This specifies whether or not to perform searches for group, netgroup, passwd, protocols, rpc, services and shadow maps using case-insensitive matching. Setting this to yes could open up the system to authorisation vulnerabilities and introduce nscd cache poisoning vulnerabilities which allow denial of service. The default is to perform case-sensitve filtering of LDAP search results for the above maps.</p>
<dt><code>pam_authz_search</code> <i>FILTER</i></p>
<dd>This option allows flexible fine tuning of the authorisation check that should be performed. The search filter specified is executed and if any entries match, access is granted, otherwise access is denied. </p>
<p> The search filter can contain the following variable references: $username, $service, $ruser, $rhost, $tty, $hostname, $fqdn, $dn, and $uid. These references are substituted in the search filter using the same syntax as described in the section on attribute mapping expressions below. </p>
<p> For example, to check that the user has a proper authorizedService value if the attribute is present (this almost emulates the <code>pam_check_service_attr</code> option in PADL&#8217;s pam_ldap): </p>
<pre>(&amp;(objectClass=posixAccount)(uid=$username)(|(authorizedService=$service)(!(authorizedService=*))))</pre>
<p>The <code>pam_check_host_attr</code> option can be emulated with: </p>
<pre>(&amp;(objectClass=posixAccount)(uid=$username)(|(host=$hostname)(host=$fqdn)(host=\*)))</pre>
<p>This option may be specified multiple times and all specified searches should at least return one entry for access to be granted.</p>
<dt><code>pam_password_prohibit_message</code> &quot;<i>MESSAGE</i>&quot;</p>
<dd>If this option is set password modification using pam_ldap will be denied and the specified message will be presented to the user instead. The message can be used to direct the user to an alternative means of changing their password.</dl>
<h2>Supported Maps</h2>
<p>The following maps are supported. They are referenced as <i>MAP</i> in the options above.</p>
<dl>
<dt>alias[es]</p>
<dd>Mail aliases. Note that most mail servers do not use the NSS interface for requesting mail aliases and parse <i>/etc/aliases</i> on their own.</p>
<dt>ether[s]</p>
<dd>Ethernet numbers (mac addresses).</p>
<dt>group</p>
<dd>Posix groups.</p>
<dt>host[s]</p>
<dd>Host names.</p>
<dt>netgroup</p>
<dd>Host and user groups used for access control.</p>
<dt>network[s]</p>
<dd>Network numbers.</p>
<dt>passwd</p>
<dd>Posix users.</p>
<dt>protocol[s]</p>
<dd>Protocol definitions (like in <i>/etc/protocols</i>).</p>
<dt>rpc</p>
<dd>Remote procedure call names and numbers.</p>
<dt>service[s]</p>
<dd>Network service names and numbers.</p>
<dt>shadow</p>
<dd>Shadow user password information.</dl>
<h2>Attribute Mapping Expressions</h2>
<p>For some attributes a mapping expression may be used to construct the resulting value. This is currently only possible for attributes that do not need to be used in search filters. The expressions are a subset of the double quoted string expressions in the Bourne (POSIX) shell. Instead of variable substitution, attribute lookups are done on the current entry and the attribute value is substituted. The following expressions are supported:</p>
<dl>
<dt>${attr} (or $attr for short)</p>
<dd>will substitute the value of the attribute</p>
<dt>${attr:-word}</p>
<dd>(use default) will substitbute the value of the attribute or, if the attribute is not set or empty substitute the word</p>
<dt>${attr:+word}</p>
<dd>(use alternative) will substitbute word if attribute is set, otherwise substitute the empty string</dl>
<p> Quote (&quot;), dollar ($) or backslash (\) characters should be escaped with a backslash (\). </p>
<p> The <code>nslcd</code> daemon checks the expressions to figure out which attributes to fetch from LDAP. Some examples to demonstrate how these expressions may be used in attribute mapping:</p>
<dl>
<dt>&quot;${shadowFlag:-0}&quot;</p>
<dd>use the shadowFlag attribute, using the value 0 as default</p>
<dt>&quot;${homeDirectory:-/home/$uid}&quot;</p>
<dd>use the uid attribute to build a homeDirectory value if that attribute is missing</p>
<dt>&quot;${isDisabled:+100}&quot;</p>
<dd>if the isDisabled attribute is set, return 100, otherwise leave value empty</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/nslcd.conf</i></p>
<dd>the main configuration file</p>
<dt><i>/etc/nsswitch.conf</i></p>
<dd>Name Service Switch configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nslcd/">nslcd</a></code>(8), <code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5)</p>
<h2>Author</h2>
<p>This manual was written by Arthur de Jong &lt;arthur [at] arthurdejong.org&gt; and is based on the <code><a href="/docs/linux/man/5-nss_ldap/">nss_ldap</a></code>(5) manual developed by PADL Software Pty Ltd.</p>
