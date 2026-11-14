---
title: "sssd-krb5(5)"
name: "sssd-krb5"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sssd-krb5/"
description: "sssd-krb5 – SSSD Kerberos provider"
---

<p>sssd-krb5 &#8211; SSSD Kerberos provider</p>
<h2>Description</h2>
<p>This manual page describes the configuration of the Kerberos 5 authentication backend for <code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8). For a detailed syntax reference, please refer to the &#8220;FILE FORMAT&#8221; section of the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page. </p>
<p> The Kerberos 5 authentication backend contains auth and chpass providers. It must be paired with an identity provider in order to function properly (for example, id_provider = ldap). Some information required by the Kerberos 5 authentication backend must be provided by the identity provider, such as the user&#8217;s Kerberos Principal Name (UPN). The configuration of the identity provider should have an entry to specify the UPN. Please refer to the man page for the applicable identity provider for details on how to configure this. </p>
<p> This backend also provides access control based on the .k5login file in the home directory of the user. See <code><a href="/docs/linux/man/5--k5login/">.k5login</a></code>(5) for more details. Please note that an empty .k5login file will deny all access to this user. To activate this feature, use &#8216;access_provider = krb5&#8217; in your SSSD configuration. </p>
<p> In the case where the UPN is not available in the identity backend, <code>sssd</code> will construct a UPN using the format <i>username</i>@<i>krb5_realm</i>.</p>
<h2>Configuration Options</h2>
<p>If the auth-module krb5 is used in an SSSD domain, the following options must be used. See the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page, section &#8220;DOMAIN SECTIONS&#8221;, for details on the configuration of an SSSD domain. </p>
<p> krb5_server, krb5_backup_server (string)</p>
<dl>
<dd>Specifies the comma-separated list of IP addresses or hostnames of the Kerberos servers to which SSSD should connect, in the order of preference. For more information on failover and server redundancy, see the &#8220;FAILOVER&#8221; section. An optional port number (preceded by a colon) may be appended to the addresses or hostnames. If empty, service discovery is enabled; for more information, refer to the &#8220;SERVICE DISCOVERY&#8221; section. </p>
<p> When using service discovery for KDC or kpasswd servers, SSSD first searches for DNS entries that specify _udp as the protocol and falls back to _tcp if none are found. </p>
<p> This option was named &#8220;krb5_kdcip&#8221; in earlier releases of SSSD. While the legacy name is recognized for the time being, users are advised to migrate their config files to use &#8220;krb5_server&#8221; instead.</dl>
<p> krb5_realm (string)</p>
<dl>
<dd>The name of the Kerberos realm. This option is required and must be specified.</dl>
<p> krb5_kpasswd, krb5_backup_kpasswd (string)</p>
<dl>
<dd>If the change password service is not running on the KDC, alternative servers can be defined here. An optional port number (preceded by a colon) may be appended to the addresses or hostnames. </p>
<p> For more information on failover and server redundancy, see the &#8220;FAILOVER&#8221; section. NOTE: Even if there are no more kpasswd servers to try, the backend is not switched to operate offline if authentication against the KDC is still possible. </p>
<p> Default: Use the KDC</dl>
<p> krb5_ccachedir (string)</p>
<dl>
<dd>Directory to store credential caches. All the substitution sequences of krb5_ccname_template can be used here, too, except %d and %P. The directory is created as private and owned by the user, with permissions set to 0700. </p>
<p> Default: /tmp</dl>
<p> krb5_ccname_template (string)</p>
<dl>
<dd>Location of the user&#8217;s credential cache. Three credential cache types are currently supported: &#8220;FILE&#8221;, &#8220;DIR&#8221; and &#8220;KEYRING:persistent&#8221;. The cache can be specified either as <i>TYPE:RESIDUAL</i>, or as an absolute path, which implies the &#8220;FILE&#8221; type. In the template, the following sequences are substituted: </p>
<p> %u</p>
<dl>
<dd>login name</dl>
<p> %U</p>
<dl>
<dd>login UID</dl>
<p> %p</p>
<dl>
<dd>principal name</dl>
<p> %r</p>
<dl>
<dd>realm name</dl>
<p> %h</p>
<dl>
<dd>home directory</dl>
<p> %d</p>
<dl>
<dd>value of krb5_ccachedir</dl>
<p> %P</p>
<dl>
<dd>the process ID of the SSSD client</dl>
<p> %%</p>
<dl>
<dd>a literal &#8216;%&#8217;</dl>
<p> If the template ends with &#8216;XXXXXX&#8217; <a href="/docs/linux/man/3-mkstemp/">mkstemp</a>(3) is used to create a unique filename in a safe way. </p>
<p> When using KEYRING types, the only supported mechanism is &#8220;KEYRING:persistent:%U&#8221;, which uses the Linux kernel keyring to store credentials on a per-UID basis. This is also the recommended choice, as it is the most secure and predictable method. </p>
<p> The default value for the credential cache name is sourced from the profile stored in the system wide krb5.conf configuration file in the [libdefaults] section. The option name is default_ccache_name. See <a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a>(5)&#8217;s PARAMETER EXPANSION paragraph for additional information on the expansion format defined by krb5.conf. </p>
<p> NOTE: Please be aware that libkrb5 ccache expansion template from <code><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a></code>(5) uses different expansion sequences than SSSD. </p>
<p> Default: (from libkrb5)</dl>
<p> krb5_auth_timeout (integer)</p>
<dl>
<dd>Timeout in seconds after an online authentication request or change password request is aborted. If possible, the authentication request is continued offline. </p>
<p> Default: 6</dl>
<p> krb5_validate (boolean)</p>
<dl>
<dd>Verify with the help of krb5_keytab that the TGT obtained has not been spoofed. The keytab is checked for entries sequentially, and the first entry with a matching realm is used for validation. If no entry matches the realm, the last entry in the keytab is used. This process can be used to validate environments using cross-realm trust by placing the appropriate keytab entry as the last entry or the only entry in the keytab file. </p>
<p> Default: false</dl>
<p> krb5_keytab (string)</p>
<dl>
<dd>The location of the keytab to use when validating credentials obtained from KDCs. </p>
<p> Default: /etc/krb5.keytab</dl>
<p> krb5_store_password_if_offline (boolean)</p>
<dl>
<dd>Store the password of the user if the provider is offline and use it to request a TGT when the provider comes online again. </p>
<p> NOTE: this feature is only available on Linux. Passwords stored in this way are kept in plaintext in the kernel keyring and are potentially accessible by the root user (with difficulty). </p>
<p> Default: false</dl>
<p> krb5_renewable_lifetime (string)</p>
<dl>
<dd>Request a renewable ticket with a total lifetime, given as an integer immediately followed by a time unit: </p>
<p> <i>s</i> for seconds </p>
<p> <i>m</i> for minutes </p>
<p> <i>h</i> for hours </p>
<p> <i>d</i> for days. </p>
<p> If there is no unit given, <i>s</i> is assumed. </p>
<p> NOTE: It is not possible to mix units. To set the renewable lifetime to one and a half hours, use &#8217;90m&#8217; instead of &#8216;1h30m&#8217;. </p>
<p> Default: not set, i.e. the TGT is not renewable</dl>
<p> krb5_lifetime (string)</p>
<dl>
<dd>Request ticket with a lifetime, given as an integer immediately followed by a time unit: </p>
<p> <i>s</i> for seconds </p>
<p> <i>m</i> for minutes </p>
<p> <i>h</i> for hours </p>
<p> <i>d</i> for days. </p>
<p> If there is no unit given <i>s</i> is assumed. </p>
<p> NOTE: It is not possible to mix units. To set the lifetime to one and a half hours please use &#8217;90m&#8217; instead of &#8216;1h30m&#8217;. </p>
<p> Default: not set, i.e. the default ticket lifetime configured on the KDC.</dl>
<p> krb5_renew_interval (string)</p>
<dl>
<dd>The time in seconds between two checks if the TGT should be renewed. TGTs are renewed if about half of their lifetime is exceeded, given as an integer immediately followed by a time unit: </p>
<p> <i>s</i> for seconds </p>
<p> <i>m</i> for minutes </p>
<p> <i>h</i> for hours </p>
<p> <i>d</i> for days. </p>
<p> If there is no unit given, <i>s</i> is assumed. </p>
<p> NOTE: It is not possible to mix units. To set the renewable lifetime to one and a half hours, use &#8217;90m&#8217; instead of &#8216;1h30m&#8217;. </p>
<p> If this option is not set or is 0 the automatic renewal is disabled. </p>
<p> Default: not set</dl>
<p> krb5_use_fast (string)</p>
<dl>
<dd>Enables flexible authentication secure tunneling (FAST) for Kerberos pre-authentication. The following options are supported: </p>
<p> <i>never</i> use FAST. This is equivalent to not setting this option at all. </p>
<p> <i>try</i> to use FAST. If the server does not support FAST, continue the authentication without it. </p>
<p> <i>demand</i> to use FAST. The authentication fails if the server does not require fast. </p>
<p> Default: not set, i.e. FAST is not used. </p>
<p> NOTE: a keytab is required to use FAST. </p>
<p> NOTE: SSSD supports FAST only with MIT Kerberos version 1.8 and later. If SSSD is used with an older version of MIT Kerberos, using this option is a configuration error.</dl>
<p> krb5_fast_principal (string)</p>
<dl>
<dd>Specifies the server principal to use for FAST.</dl>
<p> krb5_canonicalize (boolean)</p>
<dl>
<dd>Specifies if the host and user principal should be canonicalized. This feature is available with MIT Kerberos 1.7 and later versions. </p>
<p> Default: false</dl>
<p> krb5_use_kdcinfo (boolean)</p>
<dl>
<dd>Specifies if the SSSD should instruct the Kerberos libraries what realm and which KDCs to use. This option is on by default, if you disable it, you need to configure the Kerberos library using the <code><a href="/docs/linux/man/5-krb5-conf/">krb5.conf</a></code>(5) configuration file. </p>
<p> See the <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8) manual page for more information on the locator plugin. </p>
<p> Default: true</dl>
<p> krb5_use_enterprise_principal (boolean)</p>
<dl>
<dd>Specifies if the user principal should be treated as enterprise principal. See section 5 of RFC 6806 for more details about enterprise principals. </p>
<p> Default: false (AD provider: true) </p>
<p> The IPA provider will set to option to &#8216;true&#8217; if it detects that the server is capable of handling enterprise principals and the option is not set explicitly in the config file.</dl>
<p> krb5_map_user (string)</p>
<dl>
<dd>The list of mappings is given as a comma-separated list of pairs &#8220;username:primary&#8221; where &#8220;username&#8221; is a UNIX user name and &#8220;primary&#8221; is a user part of a kerberos principal. This mapping is used when user is authenticating using &#8220;auth_provider = krb5&#8221;. </p>
<p> example: </p>
<dl>
<dd>
<pre>krb5_realm = REALM
krb5_map_user = joe:juser,dick:richard</pre>
</dl>
<p> &#8220;joe&#8221; and &#8220;dick&#8221; are UNIX user names and &#8220;juser&#8221; and &#8220;richard&#8221; are primaries of kerberos principals. For user &#8220;joe&#8221; resp. &#8220;dick&#8221; SSSD will try to kinit as &#8220;juser [at] REALM&#8221; resp. &#8220;richard [at] REALM&#8221;. </p>
<p> Default: not set</dl>
<h2>Failover</h2>
<p>The failover feature allows back ends to automatically switch to a different server if the current server fails.</p>
<h3>Failover Syntax</h3>
<p>The list of servers is given as a comma-separated list; any number of spaces is allowed around the comma. The servers are listed in order of preference. The list can contain any number of servers. </p>
<p> For each failover-enabled config option, two variants exist: <i>primary</i> and <i>backup</i>. The idea is that servers in the primary list are preferred and backup servers are only searched if no primary servers can be reached. If a backup server is selected, a timeout of 31 seconds is set. After this timeout SSSD will periodically try to reconnect to one of the primary servers. If it succeeds, it will replace the current active (backup) server.</p>
<h3>The Failover Mechanism</h3>
<p>The failover mechanism distinguishes between a machine and a service. The back end first tries to resolve the hostname of a given machine; if this resolution attempt fails, the machine is considered offline. No further attempts are made to connect to this machine for any other service. If the resolution attempt succeeds, the back end tries to connect to a service on this machine. If the service connection attempt fails, then only this particular service is considered offline and the back end automatically switches over to the next service. The machine is still considered online and might still be tried for another service. </p>
<p> Further connection attempts are made to machines or services marked as offline after a specified period of time; this is currently hard coded to 30 seconds. </p>
<p> If there are no more machines to try, the back end as a whole switches to offline mode, and then attempts to reconnect every 30 seconds.</p>
<h2>Service Discovery</h2>
<p>The service discovery feature allows back ends to automatically find the appropriate servers to connect to using a special DNS query. This feature is not supported for backup servers.</p>
<h3>Configuration</h3>
<p>If no servers are specified, the back end automatically uses service discovery to try to find a server. Optionally, the user may choose to use both fixed server addresses and service discovery by inserting a special keyword, &#8220;_srv_&#8221;, in the list of servers. The order of preference is maintained. This feature is useful if, for example, the user prefers to use service discovery whenever possible, and fall back to a specific server when no servers can be discovered using DNS.</p>
<h3>The domain name</h3>
<p>Please refer to the &#8220;dns_discovery_domain&#8221; parameter in the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page for more details.</p>
<h3>The protocol</h3>
<p>The queries usually specify _tcp as the protocol. Exceptions are documented in respective option description.</p>
<h3>See Also</h3>
<p>For more information on the service discovery mechanism, refer to RFC 2782.</p>
<h2>Example</h2>
<p>The following example assumes that SSSD is correctly configured and FOO is one of the domains in the <i>[sssd]</i> section. This example shows only configuration of Kerberos authentication; it does not include any identity provider.</p>
<dl>
<dd>
<pre>[domain/FOO]
auth_provider = krb5
krb5_server = 192.168.1.1
krb5_realm = EXAMPLE.COM</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/5-sssd-secrets/">sssd-secrets</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="https://pagure.io/SSSD/sssd/">https://pagure.io/SSSD/sssd/</a></code></p>
