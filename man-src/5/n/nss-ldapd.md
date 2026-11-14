---
title: "nss-ldapd(5)"
name: "nss-ldapd"
section: "5"
letter: "n"
url: "/docs/linux/man/5-nss-ldapd/"
description: "nss-ldapd.conf – configuration file for LDAP nameservice provider"
---

<p>nss-ldapd.conf &#8211; configuration file for LDAP nameservice provider</p>
<h2>Description</h2>
<p>The <i>nss-ldapd</i> module allows LDAP directory servers to be used as a primary source of name service information. (Name service information typically includes users, hosts, groups, and other such data historically stored in flat files or NIS.) </p>
<p> The file <i>nss-ldapd.conf</i> contains the configuration information for running <code>nslcd</code> (see <code><a href="/docs/linux/man/8-nslcd/">nslcd</a></code>(8)). The file contains options, one on each line, defining the way NSS lookups are mapped onto LDAP lookups.</p>
<h2>Options</h2>
<h3>Runtime Options</h3>
<dl>
<dt><code>threads</code> <i>NUM</i></p>
<dd>Specifies the number of threads to start that can handle requests and perform LDAP queries. The default is to start 5 threads.</p>
<dt><code>uid</code> <i>UID</i></p>
<dd>This specifies which user id with which the daemon should be run. This can be a numerical id or a symbolic value. If no uid is specified no attempt to change the user will be made. Note that you should use values that don&#8217;t need LDAP to resolve.</p>
<dt><code>gid</code> <i>GID</i></p>
<dd>This specifies which group id with which the daemon should be run. This can be a numerical id or a symbolic value. If no gid is specified no attempt to change the group will be made. Note that you should use values that don&#8217;t need LDAP to resolve.</dl>
<h3>General Connection Options</h3>
<dl>
<dt><code>uri</code> <i>URI</i></p>
<dd>Specifies the LDAP URI of the server to connect to. The URI scheme may be <i>ldap</i>, <i>ldapi</i> or <i>ldaps</i>, specifying LDAP over TCP, ICP or SSL respectively (if supported by the LDAP library). Alternatively, the value <i>DNS</i> may be used to try to lookup the server using DNS SRV records. </p>
<p> When using the ldapi scheme, %2f should be used to escape slashes (e.g. <a href="ldapi://%2fvar%2frun%2fslapd%2fldapi/">ldapi://%2fvar%2frun%2fslapd%2fldapi/</a>), although most of the time this should not be needed. </p>
<p> This option may be specified multiple times. Normally, only the first server will be used with the following servers as fall-back (see <code>bind_timelimit</code> below). </p>
<p> If LDAP lookups are used for host name resolution, any host names should be specified as an IP address or name that can be resolved without using LDAP.</p>
<dt><code>ldap_version</code> <i>VERSION</i></p>
<dd>Specifies the version of the LDAP protocol to use. The default is to use the maximum version supported by the LDAP library.</p>
<dt><code>binddn</code> <i>DN</i></p>
<dd>Specifies the distinguished name with which to bind to the directory server for lookups. The default is to bind anonymously.</p>
<dt><code>bindpw</code> <i>PASSWORD</i></p>
<dd>Specifies the clear text credentials with which to bind. This option is only applicable when used with <code>binddn</code> above. If you set this option you should consider changing the permissions of the <i>nss-ldapd.conf</i> file to only grant access to the root user.</dl>
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
<dd>This option allows for custom attributes to be looked up instead of the default RFC 2307 attributes. The <i>MAP</i> may be one of the supported maps below. The <i>ATTRIBUTE</i> is the one as used in RFC 2307 (e.g. userPassword, ipProtocolNumber or macAddress). The <i>NEWATTRIBUTE</i> may be any attribute as it is available in the directory.</dl>
<h3>Timing/Reconnect Options</h3>
<dl>
<dt><code>bind_timelimit</code> <i>SECONDS</i></p>
<dd>Specifies the time limit (in seconds) to use when connecting to the directory server. This is distinct from the time limit specified in <code>timelimit</code> and affects the setup of the connection only. Note that not all LDAP client libraries have support for setting the connection time out. The default <code>bind_timelimit</code> is 30 seconds.</p>
<dt><code>timelimit</code> <i>SECONDS</i></p>
<dd>Specifies the time limit (in seconds) to wait for a response from the LDAP server. A value of zero (0), which is the default, is to wait indefinitely for searches to be completed.</p>
<dt><code>idle_timelimit</code> <i>SECONDS</i></p>
<dd>Specifies the period if inactivity (in seconds) after which the connection to the LDAP server will be closed. The default is not to time out connections.</p>
<dt><code>reconnect_sleeptime</code> <i>SECONDS</i></p>
<dd>Specifies the number of seconds to sleep when connecting to all LDAP servers fails. By default 1 second is waited between the first failure and the first retry.</p>
<dt><code>reconnect_maxsleeptime</code> <i>SECONDS</i></p>
<dd>Specified the time after the last successful operation from which the LDAP server is considered permanently unavailable. Retries will be done only once in this time period. The default value is 30 seconds.</dl>
<p> Note that the reconnect logic as described above is the mechanism that is used between <code>nslcd</code> and the LDAP server. The mechanism between the NSS client library and <code>nslcd</code> is simpler with a fixed compiled-in time out of a 10 seconds for writing to <code>nslcd</code> and a time out of 60 seconds for reading answers. <code>nslcd</code> itself has a read time out of 0.5 seconds and a write time out of 60 seconds.</p>
<h3>Ssl/Tls Options</h3>
<dl>
<dt><code>ssl</code> on|off|start_tls</p>
<dd>Specifies whether to use SSL/TLS or not (the default is not to). If <i>start_tls</i> is specified then StartTLS is used rather than raw LDAP over SSL. Not all LDAP client libraries support both SSL, StartTLS and all related configuration options.</p>
<dt><code>tls_reqcert</code> never|allow|try|demand|hard</p>
<dd>Specifies what checks to perform on a server-supplied certificate. The meaning of the values is described in the <code><a href="/docs/linux/man/5-ldap-conf/">ldap.conf</a></code>(5) manual page. At least one of <code>tls_cacertdir</code> and <code>tls_cacertfile</code> is required if peer verification is enabled.</p>
<dt><code>tls_cacertdir</code> <i>PATH</i></p>
<dd>Specifies the directory containing X.509 certificates for peer authentication.</p>
<dt><code>tls_cacertfile</code> <i>PATH</i></p>
<dd>Specifies the path to the X.509 certificate for peer authentication.</p>
<dt><code>tls_randfile</code> <i>PATH</i></p>
<dd>Specifies the path to an entropy source.</p>
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
<p> This is useful for LDAP servers that contain a lot of entries (e.g. more than 500) and limit the number of entries that are returned with one request. For OpenLDAP servers you may need to set <code>sizelimit size.prtotal=unlimited</code> for allowing more entries to be returned over multiple pages.</dl>
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
<h2>Files</h2>
<dl>
<dt><i>/etc/nss-ldapd.conf</i></p>
<dd>the main configuration file</p>
<dt><i>/etc/nsswitch.conf</i></p>
<dd>Name Service Switch configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-nslcd/">nslcd</a></code>(8), <code><a href="/docs/linux/man/5-nsswitch-conf/">nsswitch.conf</a></code>(5)</p>
<h2>Author</h2>
<p>This manual was written by Arthur de Jong &lt;arthur [at] arthurdejong.org&gt; and is based on the <code><a href="/docs/linux/man/5-nss_ldap/">nss_ldap</a></code>(5) manual developed by PADL Software Pty Ltd.</p>
