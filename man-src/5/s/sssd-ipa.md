---
title: "sssd-ipa(5)"
name: "sssd-ipa"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sssd-ipa/"
description: "sssd-ipa – SSSD IPA provider"
---

<p>sssd-ipa &#8211; SSSD IPA provider</p>
<h2>Description</h2>
<p>This manual page describes the configuration of the IPA provider for <code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8). For a detailed syntax reference, refer to the &#8220;FILE FORMAT&#8221; section of the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page. </p>
<p> The IPA provider is a back end used to connect to an IPA server. (Refer to the freeipa.org web site for information about IPA servers.) This provider requires that the machine be joined to the IPA domain; configuration is almost entirely self-discovered and obtained directly from the server. </p>
<p> The IPA provider enables SSSD to use the <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5) identity provider and the <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5) authentication provider with optimizations for IPA environments. The IPA provider accepts the same options used by the sssd-ldap and sssd-krb5 providers with some exceptions. However, it is neither necessary nor recommended to set these options. </p>
<p> The IPA provider primarily copies the traditional ldap and krb5 provider default options with some exceptions, the differences are listed in the &#8220;MODIFIED DEFAULT OPTIONS&#8221; section. </p>
<p> As an access provider, the IPA provider uses HBAC (host-based access control) rules. Please refer to freeipa.org for more information about HBAC. No configuration of access provider is required on the client side. </p>
<p> The IPA provider will use the PAC responder if the Kerberos tickets of users from trusted realms contain a PAC. To make configuration easier the PAC responder is started automatically if the IPA ID provider is configured.</p>
<h2>Configuration Options</h2>
<p>Refer to the section &#8220;DOMAIN SECTIONS&#8221; of the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page for details on the configuration of an SSSD domain. </p>
<p> ipa_domain (string)</p>
<dl>
<dd>Specifies the name of the IPA domain. This is optional. If not provided, the configuration domain name is used.</dl>
<p> ipa_server, ipa_backup_server (string)</p>
<dl>
<dd>The comma-separated list of IP addresses or hostnames of the IPA servers to which SSSD should connect in the order of preference. For more information on failover and server redundancy, see the &#8220;FAILOVER&#8221; section. This is optional if autodiscovery is enabled. For more information on service discovery, refer to the &#8220;SERVICE DISCOVERY&#8221; section.</dl>
<p> ipa_hostname (string)</p>
<dl>
<dd>Optional. May be set on machines where the <a href="/docs/linux/man/5-hostname/">hostname</a>(5) does not reflect the fully qualified name used in the IPA domain to identify this host.</dl>
<p> dyndns_update (boolean)</p>
<dl>
<dd>Optional. This option tells SSSD to automatically update the DNS server built into FreeIPA with the IP address of this client. The update is secured using GSS-TSIG. The IP address of the IPA LDAP connection is used for the updates, if it is not otherwise specified by using the &#8220;dyndns_iface&#8221; option. </p>
<p> NOTE: On older systems (such as RHEL 5), for this behavior to work reliably, the default Kerberos realm must be set properly in /etc/krb5.conf </p>
<p> NOTE: While it is still possible to use the old <i>ipa_dyndns_update</i> option, users should migrate to using <i>dyndns_update</i> in their config file. </p>
<p> Default: false</dl>
<p> dyndns_ttl (integer)</p>
<dl>
<dd>The TTL to apply to the client DNS record when updating it. If dyndns_update is false this has no effect. This will override the TTL serverside if set by an administrator. </p>
<p> NOTE: While it is still possible to use the old <i>ipa_dyndns_ttl</i> option, users should migrate to using <i>dyndns_ttl</i> in their config file. </p>
<p> Default: 1200 (seconds)</dl>
<p> dyndns_iface (string)</p>
<dl>
<dd>Optional. Applicable only when dyndns_update is true. Choose the interface or a list of interfaces whose IP addresses should be used for dynamic DNS updates. Special value &#8220;*&#8221; implies that IPs from all interfaces should be used. </p>
<p> NOTE: While it is still possible to use the old <i>ipa_dyndns_iface</i> option, users should migrate to using <i>dyndns_iface</i> in their config file. </p>
<p> Default: Use the IP addresses of the interface which is used for IPA LDAP connection </p>
<p> Example: dyndns_iface = em1, vnet1, vnet2</dl>
<p> dyndns_auth (string)</p>
<dl>
<dd>Whether the nsupdate utility should use GSS-TSIG authentication for secure updates with the DNS server, insecure updates can be sent by setting this option to &#8216;none&#8217;. </p>
<p> Default: GSS-TSIG</dl>
<p> ipa_enable_dns_sites (boolean)</p>
<dl>
<dd>Enables DNS sites &#8211; location based service discovery. </p>
<p> If true and service discovery (see Service Discovery paragraph at the bottom of the man page) is enabled, then the SSSD will first attempt location based discovery using a query that contains &quot;_location.hostname.example.com&quot; and then fall back to traditional SRV discovery. If the location based discovery succeeds, the IPA servers located with the location based discovery are treated as primary servers and the IPA servers located using the traditional SRV discovery are used as back up servers </p>
<p> Default: false</dl>
<p> dyndns_refresh_interval (integer)</p>
<dl>
<dd>How often should the back end perform periodic DNS update in addition to the automatic update performed when the back end goes online. This option is optional and applicable only when dyndns_update is true. </p>
<p> Default: 0 (disabled)</dl>
<p> dyndns_update_ptr (bool)</p>
<dl>
<dd>Whether the PTR record should also be explicitly updated when updating the client&#8217;s DNS records. Applicable only when dyndns_update is true. </p>
<p> This option should be False in most IPA deployments as the IPA server generates the PTR records automatically when forward records are changed. </p>
<p> Default: False (disabled)</dl>
<p> dyndns_force_tcp (bool)</p>
<dl>
<dd>Whether the nsupdate utility should default to using TCP for communicating with the DNS server. </p>
<p> Default: False (let nsupdate choose the protocol)</dl>
<p> dyndns_server (string)</p>
<dl>
<dd>The DNS server to use when performing a DNS update. In most setups, it&#8217;s recommended to leave this option unset. </p>
<p> Setting this option makes sense for environments where the DNS server is different from the identity server. </p>
<p> Please note that this option will be only used in fallback attempt when previous attempt using autodetected settings failed. </p>
<p> Default: None (let nsupdate choose the server)</dl>
<p> ipa_hbac_search_base (string)</p>
<dl>
<dd>Optional. Use the given string as search base for HBAC related objects. </p>
<p> Default: Use base DN</dl>
<p> ipa_host_search_base (string)</p>
<dl>
<dd>Optional. Use the given string as search base for host objects. </p>
<p> See &#8220;ldap_search_base&#8221; for information about configuring multiple search bases. </p>
<p> Default: the value of <i>ldap_search_base</i></dl>
<p> ipa_selinux_search_base (string)</p>
<dl>
<dd>Optional. Use the given string as search base for SELinux user maps. </p>
<p> See &#8220;ldap_search_base&#8221; for information about configuring multiple search bases. </p>
<p> Default: the value of <i>ldap_search_base</i></dl>
<p> ipa_subdomains_search_base (string)</p>
<dl>
<dd>Optional. Use the given string as search base for trusted domains. </p>
<p> See &#8220;ldap_search_base&#8221; for information about configuring multiple search bases. </p>
<p> Default: the value of <i>cn=trusts,%basedn</i></dl>
<p> ipa_master_domain_search_base (string)</p>
<dl>
<dd>Optional. Use the given string as search base for master domain object. </p>
<p> See &#8220;ldap_search_base&#8221; for information about configuring multiple search bases. </p>
<p> Default: the value of <i>cn=ad,cn=etc,%basedn</i></dl>
<p> ipa_views_search_base (string)</p>
<dl>
<dd>Optional. Use the given string as search base for views containers. </p>
<p> See &#8220;ldap_search_base&#8221; for information about configuring multiple search bases. </p>
<p> Default: the value of <i>cn=views,cn=accounts,%basedn</i></dl>
<p> krb5_realm (string)</p>
<dl>
<dd>The name of the Kerberos realm. This is optional and defaults to the value of &#8220;ipa_domain&#8221;. </p>
<p> The name of the Kerberos realm has a special meaning in IPA &#8211; it is converted into the base DN to use for performing LDAP operations.</dl>
<p> krb5_confd_path (string)</p>
<dl>
<dd>Absolute path of a directory where SSSD should place Kerberos configuration snippets. </p>
<p> To disable the creation of the configuration snippets set the parameter to &#8216;none&#8217;. </p>
<p> Default: not set (krb5.include.d subdirectory of SSSD&#8217;s pubconf directory)</dl>
<p> ipa_hbac_refresh (integer)</p>
<dl>
<dd>The amount of time between lookups of the HBAC rules against the IPA server. This will reduce the latency and load on the IPA server if there are many access-control requests made in a short period. </p>
<p> Default: 5 (seconds)</dl>
<p> ipa_hbac_selinux (integer)</p>
<dl>
<dd>The amount of time between lookups of the SELinux maps against the IPA server. This will reduce the latency and load on the IPA server if there are many user login requests made in a short period. </p>
<p> Default: 5 (seconds)</dl>
<p> ipa_server_mode (boolean)</p>
<dl>
<dd>This option should only be set by the IPA installer. </p>
<p> The option denotes that the SSSD is running on IPA server and should perform lookups of users and groups from trusted domains differently. </p>
<p> Default: false</dl>
<p> ipa_automount_location (string)</p>
<dl>
<dd>The automounter location this IPA client will be using </p>
<p> Default: The location named &quot;default&quot; </p>
<p> Please note that the automounter only reads the master map on startup, so if any autofs-related changes are made to the sssd.conf, you typically also need to restart the automounter daemon after restarting the SSSD.</dl>
<h3>Views And Overrides</h3>
<p>SSSD can handle views and overrides which are offered by FreeIPA 4.1 and later version. Since all paths and objectclasses are fixed on the server side there is basically no need to configure anything. For completeness the related options are listed here with their default values. </p>
<p> ipa_view_class (string)</p>
<dl>
<dd>Objectclass of the view container. </p>
<p> Default: nsContainer</dl>
<p> ipa_view_name (string)</p>
<dl>
<dd>Name of the attribute holding the name of the view. </p>
<p> Default: cn</dl>
<p> ipa_overide_object_class (string)</p>
<dl>
<dd>Objectclass of the override objects. </p>
<p> Default: ipaOverrideAnchor</dl>
<p> ipa_anchor_uuid (string)</p>
<dl>
<dd>Name of the attribute containing the reference to the original object in a remote domain. </p>
<p> Default: ipaAnchorUUID</dl>
<p> ipa_user_override_object_class (string)</p>
<dl>
<dd>Name of the objectclass for user overrides. It is used to determine if the found override object is related to a user or a group. </p>
<p> User overrides can contain attributes given by </p>
<dl>
<dd>&bull; ldap_user_name</dl>
<dl>
<dd>&bull; ldap_user_uid_number</dl>
<dl>
<dd>&bull; ldap_user_gid_number</dl>
<dl>
<dd>&bull; ldap_user_gecos</dl>
<dl>
<dd>&bull; ldap_user_home_directory</dl>
<dl>
<dd>&bull; ldap_user_shell</dl>
<dl>
<dd>&bull; ldap_user_ssh_public_key</dl>
<p> Default: ipaUserOverride</dl>
<p> ipa_group_override_object_class (string)</p>
<dl>
<dd>Name of the objectclass for group overrides. It is used to determine if the found override object is related to a user or a group. </p>
<p> Group overrides can contain attributes given by </p>
<dl>
<dd>&bull; ldap_group_name</dl>
<dl>
<dd>&bull; ldap_group_gid_number</dl>
<p> Default: ipaGroupOverride</dl>
<h2>Modified Default Options</h2>
<p>Certain option defaults do not match their respective backend provider defaults, these option names and IPA provider-specific defaults are listed below:</p>
<h3>KRB5 Provider</h3>
<dl>
<dd>&bull; krb5_validate = true</dl>
<dl>
<dd>&bull; krb5_use_fast = try</dl>
<dl>
<dd>&bull; krb5_canonicalize = true</dl>
<h3>LDAP Provider &#8211; General</h3>
<dl>
<dd>&bull; ldap_schema = ipa_v1</dl>
<dl>
<dd>&bull; ldap_force_upper_case_realm = true</dl>
<dl>
<dd>&bull; ldap_sasl_mech = GSSAPI</dl>
<dl>
<dd>&bull; ldap_sasl_minssf = 56</dl>
<dl>
<dd>&bull; ldap_account_expire_policy = ipa</dl>
<dl>
<dd>&bull; ldap_use_tokengroups = true</dl>
<h3>LDAP Provider &#8211; User options</h3>
<dl>
<dd>&bull; ldap_user_member_of = memberOf</dl>
<dl>
<dd>&bull; ldap_user_uuid = ipaUniqueID</dl>
<dl>
<dd>&bull; ldap_user_ssh_public_key = ipaSshPubKey</dl>
<dl>
<dd>&bull; ldap_user_auth_type = ipaUserAuthType</dl>
<dl>
<dd>&bull; ldap_user_certificate = userCertificate;binary</dl>
<h3>LDAP Provider &#8211; Group options</h3>
<dl>
<dd>&bull; ldap_group_object_class = ipaUserGroup</dl>
<dl>
<dd>&bull; ldap_group_object_class_alt = posixGroup</dl>
<dl>
<dd>&bull; ldap_group_member = member</dl>
<dl>
<dd>&bull; ldap_group_uuid = ipaUniqueID</dl>
<dl>
<dd>&bull; ldap_group_objectsid = ipaNTSecurityIdentifier</dl>
<dl>
<dd>&bull; ldap_group_external_member = ipaExternalMember</dl>
<h2>Subdomains Provider</h2>
<p>The IPA subdomains provider behaves slightly differently if it is configured explicitly or implicitly. </p>
<p> If the option &#8216;subdomains_provider = ipa&#8217; is found in the domain section of sssd.conf, the IPA subdomains provider is configured explicitly, and all subdomain requests are sent to the IPA server if necessary. </p>
<p> If the option &#8216;subdomains_provider&#8217; is not set in the domain section of sssd.conf but there is the option &#8216;id_provider = ipa&#8217;, the IPA subdomains provider is configured implicitly. In this case, if a subdomain request fails and indicates that the server does not support subdomains, i.e. is not configured for trusts, the IPA subdomains provider is disabled. After an hour or after the IPA provider goes online, the subdomains provider is enabled again.</p>
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
<p>The following example assumes that SSSD is correctly configured and example.com is one of the domains in the <i>[sssd]</i> section. This examples shows only the ipa provider-specific options.</p>
<dl>
<dd>
<pre>[domain/example.com]
id_provider = ipa
ipa_server = ipaserver.example.com
ipa_hostname = myhost.example.com</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/5-sssd-secrets/">sssd-secrets</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="https://pagure.io/SSSD/sssd/">https://pagure.io/SSSD/sssd/</a></code></p>
