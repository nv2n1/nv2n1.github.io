---
title: "sssd-ad(5)"
name: "sssd-ad"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sssd-ad/"
description: "sssd-ad – SSSD Active Directory provider"
---

<p>sssd-ad &#8211; SSSD Active Directory provider</p>
<h2>Description</h2>
<p>This manual page describes the configuration of the AD provider for <code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8). For a detailed syntax reference, refer to the &#8220;FILE FORMAT&#8221; section of the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page. </p>
<p> The AD provider is a back end used to connect to an Active Directory server. This provider requires that the machine be joined to the AD domain and a keytab is available. </p>
<p> The AD provider supports connecting to Active Directory 2008 R2 or later. Earlier versions may work, but are unsupported. </p>
<p> The AD provider can be used to get user information and authenticate users from trusted domains. Currently only trusted domains in the same forest are recognized. In addition servers from trusted domains are always auto-discovered. </p>
<p> The AD provider enables SSSD to use the <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5) identity provider and the <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5) authentication provider with optimizations for Active Directory environments. The AD provider accepts the same options used by the sssd-ldap and sssd-krb5 providers with some exceptions. However, it is neither necessary nor recommended to set these options. </p>
<p> The AD provider primarily copies the traditional ldap and krb5 provider default options with some exceptions, the differences are listed in the &#8220;MODIFIED DEFAULT OPTIONS&#8221; section. </p>
<p> The AD provider can also be used as an access, chpass, sudo and autofs provider. No configuration of the access provider is required on the client side. </p>
<p> By default, the AD provider will map UID and GID values from the objectSID parameter in Active Directory. For details on this, see the &#8220;ID MAPPING&#8221; section below. If you want to disable ID mapping and instead rely on POSIX attributes defined in Active Directory, you should set </p>
<dl>
<dd>
<pre>ldap_id_mapping = False</pre>
</dl>
<p> In order to retrieve users and groups using POSIX attributes from trusted domains, the AD administrator must make sure that the POSIX attributes are replicated to the Global Catalog. </p>
<p> Users, groups and other entities served by SSSD are always treated as case-insensitive in the AD provider for compatibility with Active Directory&#8217;s LDAP implementation.</p>
<h2>Configuration Options</h2>
<p>Refer to the section &#8220;DOMAIN SECTIONS&#8221; of the <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5) manual page for details on the configuration of an SSSD domain. </p>
<p> ad_domain (string)</p>
<dl>
<dd>Specifies the name of the Active Directory domain. This is optional. If not provided, the configuration domain name is used. </p>
<p> For proper operation, this option should be specified as the lower-case version of the long version of the Active Directory domain. </p>
<p> The short domain name (also known as the NetBIOS or the flat name) is autodetected by the SSSD.</dl>
<p> ad_enabled_domains (string)</p>
<dl>
<dd>A comma-separated list of enabled Active Directory domains. If provided, SSSD will ignore any domains not listed in this option. If left unset, all domains from the AD forest will be available. </p>
<p> For proper operation, this option must be specified in all lower-case and as the fully qualified domain name of the Active Directory domain. For example: </p>
<dl>
<dd>
<pre>ad_enabled_domains = sales.example.com, eng.example.com</pre>
</dl>
<p> The short domain name (also known as the NetBIOS or the flat name) will be autodetected by SSSD. </p>
<p> Default: Not set</dl>
<p> ad_server, ad_backup_server (string)</p>
<dl>
<dd>The comma-separated list of hostnames of the AD servers to which SSSD should connect in order of preference. For more information on failover and server redundancy, see the &#8220;FAILOVER&#8221; section. </p>
<p> This is optional if autodiscovery is enabled. For more information on service discovery, refer to the &#8220;SERVICE DISCOVERY&#8221; section. </p>
<p> Note: Trusted domains will always auto-discover servers even if the primary server is explicitly defined in the ad_server option.</dl>
<p> ad_hostname (string)</p>
<dl>
<dd>Optional. May be set on machines where the <a href="/docs/linux/man/5-hostname/">hostname</a>(5) does not reflect the fully qualified name used in the Active Directory domain to identify this host. </p>
<p> This field is used to determine the host principal in use in the keytab. It must match the hostname for which the keytab was issued.</dl>
<p> ad_enable_dns_sites (boolean)</p>
<dl>
<dd>Enables DNS sites &#8211; location based service discovery. </p>
<p> If true and service discovery (see Service Discovery paragraph at the bottom of the man page) is enabled, the SSSD will first attempt to discover the Active Directory server to connect to using the Active Directory Site Discovery and fall back to the DNS SRV records if no AD site is found. The DNS SRV configuration, including the discovery domain, is used during site discovery as well. </p>
<p> Default: true</dl>
<p> ad_access_filter (string)</p>
<dl>
<dd>This option specifies LDAP access control filter that the user must match in order to be allowed access. Please note that the &#8220;access_provider&#8221; option must be explicitly set to &#8220;ad&#8221; in order for this option to have an effect. </p>
<p> The option also supports specifying different filters per domain or forest. This extended filter would consist of: &#8220;KEYWORD:NAME:FILTER&#8221;. The keyword can be either &#8220;DOM&#8221;, &#8220;FOREST&#8221; or missing. </p>
<p> If the keyword equals to &#8220;DOM&#8221; or is missing, then &#8220;NAME&#8221; specifies the domain or subdomain the filter applies to. If the keyword equals to &#8220;FOREST&#8221;, then the filter equals to all domains from the forest specified by &#8220;NAME&#8221;. </p>
<p> Multiple filters can be separated with the &#8220;?&#8221; character, similarly to how search bases work. </p>
<p> Nested group membership must be searched for using a special OID &#8220;:1.2.840.113556.1.4.1941:&#8221; in addition to the full DOM:domain.example.org: syntax to ensure the parser does not attempt to interpret the colon characters associated with the OID. If you do not use this OID then nested group membership will not be resolved. See usage example below and refer here for further information about the OID: m[blue]<code>[MS-ADTS] section LDAP extensions</code>m[]<font SIZE="-2">[1]</font> </p>
<p> The most specific match is always used. For example, if the option specified filter for a domain the user is a member of and a global filter, the per-domain filter would be applied. If there are more matches with the same specification, the first one is used. </p>
<p> Examples: </p>
<dl>
<dd>
<pre># apply filter on domain called dom1 only:
dom1:(memberOf=cn=admins,ou=groups,dc=dom1,dc=com)
# apply filter on domain called dom2 only:
DOM:dom2:(memberOf=cn=admins,ou=groups,dc=dom2,dc=com)
# apply filter on forest called EXAMPLE.COM only:
FOREST:EXAMPLE.COM:(memberOf=cn=admins,ou=groups,dc=example,dc=com)
# apply filter for a member of a nested group in dom1:
DOM:dom1:(memberOf:1.2.840.113556.1.4.1941:=cn=nestedgroup,ou=groups,dc=example,dc=com)</pre>
</dl>
<p> Default: Not set</dl>
<p> ad_site (string)</p>
<dl>
<dd>Specify AD site to which client should try to connect. If this option is not provided, the AD site will be auto-discovered. </p>
<p> Default: Not set</dl>
<p> ad_enable_gc (boolean)</p>
<dl>
<dd>By default, the SSSD connects to the Global Catalog first to retrieve users from trusted domains and uses the LDAP port to retrieve group memberships or as a fallback. Disabling this option makes the SSSD only connect to the LDAP port of the current AD server. </p>
<p> Please note that disabling Global Catalog support does not disable retrieving users from trusted domains. The SSSD would connect to the LDAP port of trusted domains instead. However, Global Catalog must be used in order to resolve cross-domain group memberships. </p>
<p> Default: true</dl>
<p> ad_gpo_access_control (string)</p>
<dl>
<dd>This option specifies the operation mode for GPO-based access control functionality: whether it operates in disabled mode, enforcing mode, or permissive mode. Please note that the &#8220;access_provider&#8221; option must be explicitly set to &#8220;ad&#8221; in order for this option to have an effect. </p>
<p> GPO-based access control functionality uses GPO policy settings to determine whether or not a particular user is allowed to logon to a particular host. </p>
<p> NOTE: If the operation mode is set to enforcing, it is possible that users that were previously allowed logon access will now be denied logon access (as dictated by the GPO policy settings). In order to facilitate a smooth transition for administrators, a permissive mode is available that will not enforce the access control rules, but will evaluate them and will output a syslog message if access would have been denied. By examining the logs, administrators can then make the necessary changes before setting the mode to enforcing. </p>
<p> There are three supported values for this option: </p>
<dl>
<dd>&bull; disabled: GPO-based access control rules are neither evaluated nor enforced.</dl>
<dl>
<dd>&bull; enforcing: GPO-based access control rules are evaluated and enforced.</dl>
<dl>
<dd>&bull; permissive: GPO-based access control rules are evaluated, but not enforced. Instead, a syslog message will be emitted indicating that the user would have been denied access if this option&#8217;s value were set to enforcing.</dl>
<p> Default: permissive</dl>
<p> ad_gpo_cache_timeout (integer)</p>
<dl>
<dd>The amount of time between lookups of GPO policy files against the AD server. This will reduce the latency and load on the AD server if there are many access-control requests made in a short period. </p>
<p> Default: 5 (seconds)</dl>
<p> ad_gpo_map_interactive (string)</p>
<dl>
<dd>A comma-separated list of PAM service names for which GPO-based access control is evaluated based on the InteractiveLogonRight and DenyInteractiveLogonRight policy settings. </p>
<p> Note: Using the Group Policy Management Editor this value is called &quot;Allow log on locally&quot; and &quot;Deny log on locally&quot;. </p>
<p> It is possible to add another PAM service name to the default set by using &#8220;+service_name&#8221; or to explicitly remove a PAM service name from the default set by using &#8220;-service_name&#8221;. For example, in order to replace a default PAM service name for this logon right (e.g. &#8220;login&#8221;) with a custom pam service name (e.g. &#8220;my_pam_service&#8221;), you would use the following configuration: </p>
<dl>
<dd>
<pre>ad_gpo_map_interactive = +my_pam_service, -login</pre>
</dl>
<p> Default: the default set of PAM service names includes: </p>
<dl>
<dd>&bull; login</dl>
<dl>
<dd>&bull; su</dl>
<dl>
<dd>&bull; su-l</dl>
<dl>
<dd>&bull; gdm-fingerprint</dl>
<dl>
<dd>&bull; gdm-password</dl>
<dl>
<dd>&bull; gdm-smartcard</dl>
<dl>
<dd>&bull; kdm</dl>
<dl>
<dd>&bull; lightdm</dl>
<dl>
<dd>&bull; lxdm</dl>
<dl>
<dd>&bull; sddm</dl>
<dl>
<dd>&bull; unity</dl>
<dl>
<dd>&bull; xdm</dl>
</dl>
<p> ad_gpo_map_remote_interactive (string)</p>
<dl>
<dd>A comma-separated list of PAM service names for which GPO-based access control is evaluated based on the RemoteInteractiveLogonRight and DenyRemoteInteractiveLogonRight policy settings. </p>
<p> Note: Using the Group Policy Management Editor this value is called &quot;Allow log on through Remote Desktop Services&quot; and &quot;Deny log on through Remote Desktop Services&quot;. </p>
<p> It is possible to add another PAM service name to the default set by using &#8220;+service_name&#8221; or to explicitly remove a PAM service name from the default set by using &#8220;-service_name&#8221;. For example, in order to replace a default PAM service name for this logon right (e.g. &#8220;sshd&#8221;) with a custom pam service name (e.g. &#8220;my_pam_service&#8221;), you would use the following configuration: </p>
<dl>
<dd>
<pre>ad_gpo_map_remote_interactive = +my_pam_service, -sshd</pre>
</dl>
<p> Default: the default set of PAM service names includes: </p>
<dl>
<dd>&bull; sshd</dl>
<dl>
<dd>&bull; cockpit</dl>
</dl>
<p> ad_gpo_map_network (string)</p>
<dl>
<dd>A comma-separated list of PAM service names for which GPO-based access control is evaluated based on the NetworkLogonRight and DenyNetworkLogonRight policy settings. </p>
<p> Note: Using the Group Policy Management Editor this value is called &quot;Access this computer from the network&quot; and &quot;Deny access to this computer from the network&quot;. </p>
<p> It is possible to add another PAM service name to the default set by using &#8220;+service_name&#8221; or to explicitly remove a PAM service name from the default set by using &#8220;-service_name&#8221;. For example, in order to replace a default PAM service name for this logon right (e.g. &#8220;ftp&#8221;) with a custom pam service name (e.g. &#8220;my_pam_service&#8221;), you would use the following configuration: </p>
<dl>
<dd>
<pre>ad_gpo_map_network = +my_pam_service, -ftp</pre>
</dl>
<p> Default: the default set of PAM service names includes: </p>
<dl>
<dd>&bull; ftp</dl>
<dl>
<dd>&bull; samba</dl>
</dl>
<p> ad_gpo_map_batch (string)</p>
<dl>
<dd>A comma-separated list of PAM service names for which GPO-based access control is evaluated based on the BatchLogonRight and DenyBatchLogonRight policy settings. </p>
<p> Note: Using the Group Policy Management Editor this value is called &quot;Allow log on as a batch job&quot; and &quot;Deny log on as a batch job&quot;. </p>
<p> It is possible to add another PAM service name to the default set by using &#8220;+service_name&#8221; or to explicitly remove a PAM service name from the default set by using &#8220;-service_name&#8221;. For example, in order to replace a default PAM service name for this logon right (e.g. &#8220;crond&#8221;) with a custom pam service name (e.g. &#8220;my_pam_service&#8221;), you would use the following configuration: </p>
<dl>
<dd>
<pre>ad_gpo_map_batch = +my_pam_service, -crond</pre>
</dl>
<p> Default: the default set of PAM service names includes: </p>
<dl>
<dd>&bull; crond</dl>
</dl>
<p> ad_gpo_map_service (string)</p>
<dl>
<dd>A comma-separated list of PAM service names for which GPO-based access control is evaluated based on the ServiceLogonRight and DenyServiceLogonRight policy settings. </p>
<p> Note: Using the Group Policy Management Editor this value is called &quot;Allow log on as a service&quot; and &quot;Deny log on as a service&quot;. </p>
<p> It is possible to add a PAM service name to the default set by using &#8220;+service_name&#8221;. Since the default set is empty, it is not possible to remove a PAM service name from the default set. For example, in order to add a custom pam service name (e.g. &#8220;my_pam_service&#8221;), you would use the following configuration: </p>
<dl>
<dd>
<pre>ad_gpo_map_service = +my_pam_service</pre>
</dl>
<p> Default: not set</dl>
<p> ad_gpo_map_permit (string)</p>
<dl>
<dd>A comma-separated list of PAM service names for which GPO-based access is always granted, regardless of any GPO Logon Rights. </p>
<p> It is possible to add another PAM service name to the default set by using &#8220;+service_name&#8221; or to explicitly remove a PAM service name from the default set by using &#8220;-service_name&#8221;. For example, in order to replace a default PAM service name for unconditionally permitted access (e.g. &#8220;sudo&#8221;) with a custom pam service name (e.g. &#8220;my_pam_service&#8221;), you would use the following configuration: </p>
<dl>
<dd>
<pre>ad_gpo_map_permit = +my_pam_service, -sudo</pre>
</dl>
<p> Default: the default set of PAM service names includes: </p>
<dl>
<dd>&bull; polkit-1</dl>
<dl>
<dd>&bull; sudo</dl>
<dl>
<dd>&bull; sudo-i</dl>
<dl>
<dd>&bull; systemd-user</dl>
</dl>
<p> ad_gpo_map_deny (string)</p>
<dl>
<dd>A comma-separated list of PAM service names for which GPO-based access is always denied, regardless of any GPO Logon Rights. </p>
<p> It is possible to add a PAM service name to the default set by using &#8220;+service_name&#8221;. Since the default set is empty, it is not possible to remove a PAM service name from the default set. For example, in order to add a custom pam service name (e.g. &#8220;my_pam_service&#8221;), you would use the following configuration: </p>
<dl>
<dd>
<pre>ad_gpo_map_deny = +my_pam_service</pre>
</dl>
<p> Default: not set</dl>
<p> ad_gpo_default_right (string)</p>
<dl>
<dd>This option defines how access control is evaluated for PAM service names that are not explicitly listed in one of the ad_gpo_map_* options. This option can be set in two different manners. First, this option can be set to use a default logon right. For example, if this option is set to &#8216;interactive&#8217;, it means that unmapped PAM service names will be processed based on the InteractiveLogonRight and DenyInteractiveLogonRight policy settings. Alternatively, this option can be set to either always permit or always deny access for unmapped PAM service names. </p>
<p> Supported values for this option include: </p>
<dl>
<dd>&bull; interactive</dl>
<dl>
<dd>&bull; remote_interactive</dl>
<dl>
<dd>&bull; network</dl>
<dl>
<dd>&bull; batch</dl>
<dl>
<dd>&bull; service</dl>
<dl>
<dd>&bull; permit</dl>
<dl>
<dd>&bull; deny</dl>
<p> Default: deny</dl>
<p> ad_maximum_machine_account_password_age (integer)</p>
<dl>
<dd>SSSD will check once a day if the machine account password is older than the given age in days and try to renew it. A value of 0 will disable the renewal attempt. </p>
<p> Default: 30 days</dl>
<p> ad_machine_account_password_renewal_opts (string)</p>
<dl>
<dd>This option should only be used to test the machine account renewal task. The option expect 2 integers seperated by a colon (&#8216;:&#8217;). The first integer defines the interval in seconds how often the task is run. The second specifies the inital timeout in seconds before the task is run for the first time after startup. </p>
<p> Default: 86400:750 (24h and 15m)</dl>
<p> dyndns_update (boolean)</p>
<dl>
<dd>Optional. This option tells SSSD to automatically update the Active Directory DNS server with the IP address of this client. The update is secured using GSS-TSIG. As a consequence, the Active Directory administrator only needs to allow secure updates for the DNS zone. The IP address of the AD LDAP connection is used for the updates, if it is not otherwise specified by using the &#8220;dyndns_iface&#8221; option. </p>
<p> NOTE: On older systems (such as RHEL 5), for this behavior to work reliably, the default Kerberos realm must be set properly in /etc/krb5.conf </p>
<p> Default: true</dl>
<p> dyndns_ttl (integer)</p>
<dl>
<dd>The TTL to apply to the client DNS record when updating it. If dyndns_update is false this has no effect. This will override the TTL serverside if set by an administrator. </p>
<p> Default: 3600 (seconds)</dl>
<p> dyndns_iface (string)</p>
<dl>
<dd>Optional. Applicable only when dyndns_update is true. Choose the interface or a list of interfaces whose IP addresses should be used for dynamic DNS updates. Special value &#8220;*&#8221; implies that IPs from all interfaces should be used. </p>
<p> Default: Use the IP addresses of the interface which is used for AD LDAP connection </p>
<p> Example: dyndns_iface = em1, vnet1, vnet2</dl>
<p> dyndns_refresh_interval (integer)</p>
<dl>
<dd>How often should the back end perform periodic DNS update in addition to the automatic update performed when the back end goes online. This option is optional and applicable only when dyndns_update is true. Note that the lowest possible value is 60 seconds in-case if value is provided less than 60, parameter will assume lowest value only. </p>
<p> Default: 86400 (24 hours)</dl>
<p> dyndns_update_ptr (bool)</p>
<dl>
<dd>Whether the PTR record should also be explicitly updated when updating the client&#8217;s DNS records. Applicable only when dyndns_update is true. </p>
<p> Default: True</dl>
<p> dyndns_force_tcp (bool)</p>
<dl>
<dd>Whether the nsupdate utility should default to using TCP for communicating with the DNS server. </p>
<p> Default: False (let nsupdate choose the protocol)</dl>
<p> dyndns_auth (string)</p>
<dl>
<dd>Whether the nsupdate utility should use GSS-TSIG authentication for secure updates with the DNS server, insecure updates can be sent by setting this option to &#8216;none&#8217;. </p>
<p> Default: GSS-TSIG</dl>
<p> dyndns_server (string)</p>
<dl>
<dd>The DNS server to use when performing a DNS update. In most setups, it&#8217;s recommended to leave this option unset. </p>
<p> Setting this option makes sense for environments where the DNS server is different from the identity server. </p>
<p> Please note that this option will be only used in fallback attempt when previous attempt using autodetected settings failed. </p>
<p> Default: None (let nsupdate choose the server)</dl>
<p> override_homedir (string)</p>
<dl>
<dd>Override the user&#8217;s home directory. You can either provide an absolute value or a template. In the template, the following sequences are substituted: </p>
<p> %u</p>
<dl>
<dd>login name</dl>
<p> %U</p>
<dl>
<dd>UID number</dl>
<p> %d</p>
<dl>
<dd>domain name</dl>
<p> %f</p>
<dl>
<dd>fully qualified user name (user [at] domain)</dl>
<p> %l</p>
<dl>
<dd>The first letter of the login name.</dl>
<p> %P</p>
<dl>
<dd>UPN &#8211; User Principal Name (name [at] REALM)</dl>
<p> %o</p>
<dl>
<dd>The original home directory retrieved from the identity provider.</dl>
<p> %H</p>
<dl>
<dd>The value of configure option <i>homedir_substring</i>.</dl>
<p> %%</p>
<dl>
<dd>a literal &#8216;%&#8217;</dl>
<p> This option can also be set per-domain. </p>
<p> example: </p>
<dl>
<dd>
<pre>override_homedir = /home/%u</pre>
</dl>
<p> Default: Not set (SSSD will use the value retrieved from LDAP)</dl>
<p> homedir_substring (string)</p>
<dl>
<dd>The value of this option will be used in the expansion of the <i>override_homedir</i> option if the template contains the format string <i>%H</i>. An LDAP directory entry can directly contain this template so that this option can be used to expand the home directory path for each client machine (or operating system). It can be set per-domain or globally in the [nss] section. A value specified in a domain section will override one set in the [nss] section. </p>
<p> Default: /home</dl>
<p> krb5_confd_path (string)</p>
<dl>
<dd>Absolute path of a directory where SSSD should place Kerberos configuration snippets. </p>
<p> To disable the creation of the configuration snippets set the parameter to &#8216;none&#8217;. </p>
<p> Default: not set (krb5.include.d subdirectory of SSSD&#8217;s pubconf directory)</dl>
<h2>Modified Default Options</h2>
<p>Certain option defaults do not match their respective backend provider defaults, these option names and AD provider-specific defaults are listed below:</p>
<h3>KRB5 Provider</h3>
<dl>
<dd>&bull; krb5_validate = true</dl>
<dl>
<dd>&bull; krb5_use_enterprise_principal = true</dl>
<h3>LDAP Provider</h3>
<dl>
<dd>&bull; ldap_schema = ad</dl>
<dl>
<dd>&bull; ldap_force_upper_case_realm = true</dl>
<dl>
<dd>&bull; ldap_id_mapping = true</dl>
<dl>
<dd>&bull; ldap_sasl_mech = gssapi</dl>
<dl>
<dd>&bull; ldap_referrals = false</dl>
<dl>
<dd>&bull; ldap_account_expire_policy = ad</dl>
<dl>
<dd>&bull; ldap_use_tokengroups = true</dl>
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
<h2>Id Mapping</h2>
<p>The ID-mapping feature allows SSSD to act as a client of Active Directory without requiring administrators to extend user attributes to support POSIX attributes for user and group identifiers. </p>
<p> NOTE: When ID-mapping is enabled, the uidNumber and gidNumber attributes are ignored. This is to avoid the possibility of conflicts between automatically-assigned and manually-assigned values. If you need to use manually-assigned values, ALL values must be manually-assigned. </p>
<p> Please note that changing the ID mapping related configuration options will cause user and group IDs to change. At the moment, SSSD does not support changing IDs, so the SSSD database must be removed. Because cached passwords are also stored in the database, removing the database should only be performed while the authentication servers are reachable, otherwise users might get locked out. In order to cache the password, an authentication must be performed. It is not sufficient to use <code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8) to remove the database, rather the process consists of: </p>
<dl>
<dd>&bull; Making sure the remote servers are reachable</dl>
<dl>
<dd>&bull; Stopping the SSSD service</dl>
<dl>
<dd>&bull; Removing the database</dl>
<dl>
<dd>&bull; Starting the SSSD service</dl>
<p> Moreover, as the change of IDs might necessitate the adjustment of other system properties such as file and directory ownership, it&#8217;s advisable to plan ahead and test the ID mapping configuration thoroughly.</p>
<h3>Mapping Algorithm</h3>
<p>Active Directory provides an objectSID for every user and group object in the directory. This objectSID can be broken up into components that represent the Active Directory domain identity and the relative identifier (RID) of the user or group object. </p>
<p> The SSSD ID-mapping algorithm takes a range of available UIDs and divides it into equally-sized component sections &#8211; called &quot;slices&quot;-. Each slice represents the space available to an Active Directory domain. </p>
<p> When a user or group entry for a particular domain is encountered for the first time, the SSSD allocates one of the available slices for that domain. In order to make this slice-assignment repeatable on different client machines, we select the slice based on the following algorithm: </p>
<p> The SID string is passed through the murmurhash3 algorithm to convert it to a 32-bit hashed value. We then take the modulus of this value with the total number of available slices to pick the slice. </p>
<p> NOTE: It is possible to encounter collisions in the hash and subsequent modulus. In these situations, we will select the next available slice, but it may not be possible to reproduce the same exact set of slices on other machines (since the order that they are encountered will determine their slice). In this situation, it is recommended to either switch to using explicit POSIX attributes in Active Directory (disabling ID-mapping) or configure a default domain to guarantee that at least one is always consistent. See &#8220;Configuration&#8221; for details.</p>
<h3>Configuration</h3>
<p>Minimum configuration (in the &#8220;[domain/DOMAINNAME]&#8221; section): </p>
<dl>
<dd>
<pre>ldap_id_mapping = True
ldap_schema = ad</pre>
</dl>
<p> The default configuration results in configuring 10,000 slices, each capable of holding up to 200,000 IDs, starting from 200,000 and going up to 2,000,200,000. This should be sufficient for most deployments. </p>
<p> <font SIZE="+1"> <code>Advanced Configuration</code></p>
<dl>
<dd>ldap_idmap_range_min (integer)</p>
<dl>
<dd>Specifies the lower bound of the range of POSIX IDs to use for mapping Active Directory user and group SIDs. </p>
<p> NOTE: This option is different from &#8220;min_id&#8221; in that &#8220;min_id&#8221; acts to filter the output of requests to this domain, whereas this option controls the range of ID assignment. This is a subtle distinction, but the good general advice would be to have &#8220;min_id&#8221; be less-than or equal to &#8220;ldap_idmap_range_min&#8221; </p>
<p> Default: 200000</dl>
<p> ldap_idmap_range_max (integer)</p>
<dl>
<dd>Specifies the upper bound of the range of POSIX IDs to use for mapping Active Directory user and group SIDs. </p>
<p> NOTE: This option is different from &#8220;max_id&#8221; in that &#8220;max_id&#8221; acts to filter the output of requests to this domain, whereas this option controls the range of ID assignment. This is a subtle distinction, but the good general advice would be to have &#8220;max_id&#8221; be greater-than or equal to &#8220;ldap_idmap_range_max&#8221; </p>
<p> Default: 2000200000</dl>
<p> ldap_idmap_range_size (integer)</p>
<dl>
<dd>Specifies the number of IDs available for each slice. If the range size does not divide evenly into the min and max values, it will create as many complete slices as it can. </p>
<p> NOTE: The value of this option must be at least as large as the highest user RID planned for use on the Active Directory server. User lookups and login will fail for any user whose RID is greater than this value. </p>
<p> For example, if your most recently-added Active Directory user has objectSid=S-1-5-21-2153326666-2176343378-3404031434-1107, &#8220;ldap_idmap_range_size&#8221; must be at least 1108 as range size is equal to maximal SID minus minimal SID plus one (e.g. 1108 = 1107 &#8211; 0 + 1). </p>
<p> It is important to plan ahead for future expansion, as changing this value will result in changing all of the ID mappings on the system, leading to users with different local IDs than they previously had. </p>
<p> Default: 200000</dl>
<p> ldap_idmap_default_domain_sid (string)</p>
<dl>
<dd>Specify the domain SID of the default domain. This will guarantee that this domain will always be assigned to slice zero in the ID map, bypassing the murmurhash algorithm described above. </p>
<p> Default: not set</dl>
<p> ldap_idmap_default_domain (string)</p>
<dl>
<dd>Specify the name of the default domain. </p>
<p> Default: not set</dl>
<p> ldap_idmap_autorid_compat (boolean)</p>
<dl>
<dd>Changes the behavior of the ID-mapping algorithm to behave more similarly to winbind&#8217;s &#8220;idmap_autorid&#8221; algorithm. </p>
<p> When this option is configured, domains will be allocated starting with slice zero and increasing monatomically with each additional domain. </p>
<p> NOTE: This algorithm is non-deterministic (it depends on the order that users and groups are requested). If this mode is required for compatibility with machines running winbind, it is recommended to also use the &#8220;ldap_idmap_default_domain_sid&#8221; option to guarantee that at least one domain is consistently allocated to slice zero. </p>
<p> Default: False</dl>
<p> ldap_idmap_helper_table_size (integer)</p>
<dl>
<dd>Maximal number of secondary slices that is tried when performing mapping from UNIX id to SID. </p>
<p> Note: Additional secondary slices might be generated when SID is being mapped to UNIX id and RID part of SID is out of range for secondary slices generated so far. If value of ldap_idmap_helper_table_size is equal to 0 then no additional secondary slices are generated. </p>
<p> Default: 10</dl>
</dl>
<p> </font></p>
<h3>Well-Known SIDs</h3>
<p>SSSD supports to look up the names of Well-Known SIDs, i.e. SIDs with a special hardcoded meaning. Since the generic users and groups related to those Well-Known SIDs have no equivalent in a Linux/UNIX environment no POSIX IDs are available for those objects. </p>
<p> The SID name space is organized in authorities which can be seen as different domains. The authorities for the Well-Known SIDs are </p>
<dl>
<dd>&bull; Null Authority</dl>
<dl>
<dd>&bull; World Authority</dl>
<dl>
<dd>&bull; Local Authority</dl>
<dl>
<dd>&bull; Creator Authority</dl>
<dl>
<dd>&bull; NT Authority</dl>
<dl>
<dd>&bull; Built-in</dl>
<p> The capitalized version of these names are used as domain names when returning the fully qualified name of a Well-Known SID. </p>
<p> Since some utilities allow to modify SID based access control information with the help of a name instead of using the SID directly SSSD supports to look up the SID by the name as well. To avoid collisions only the fully qualified names can be used to look up Well-Known SIDs. As a result the domain names &#8220;NULL AUTHORITY&#8221;, &#8220;WORLD AUTHORITY&#8221;, &#8221; LOCAL AUTHORITY&#8221;, &#8220;CREATOR AUTHORITY&#8221;, &#8220;NT AUTHORITY&#8221; and &#8220;BUILTIN&#8221; should not be used as domain names in sssd.conf.</p>
<h2>Example</h2>
<p>The following example assumes that SSSD is correctly configured and example.com is one of the domains in the <i>[sssd]</i> section. This example shows only the AD provider-specific options.</p>
<dl>
<dd>
<pre>[domain/EXAMPLE]
id_provider = ad
auth_provider = ad
access_provider = ad
chpass_provider = ad
ad_server = dc1.example.com
ad_hostname = client.example.com
ad_domain = example.com</pre>
</dl>
<h2>Notes</h2>
<p>The AD access control provider checks if the account is expired. It has the same effect as the following configuration of the LDAP provider:</p>
<dl>
<dd>
<pre>access_provider = ldap
ldap_access_order = expire
ldap_account_expire_policy = ad</pre>
</dl>
<p> However, unless the &#8220;ad&#8221; access control provider is explicitly configured, the default access provider is &#8220;permit&#8221;. Please note that if you configure an access provider other than &#8220;ad&#8221;, you need to set all the connection parameters (such as LDAP URIs and encryption details) manually. When the autofs provider is set to &#8220;ad&#8221;, the RFC2307 schema attribute mapping (nisMap, nisObject, &#8230;) is used, because these attributes are included in the default Active Directory schema. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code><a href="/docs/linux/man/5-sssd-conf/">sssd.conf</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/5-sssd-secrets/">sssd-secrets</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_authorizedkeys/">sss_ssh_authorizedkeys</a></code>(8), <code><a href="/docs/linux/man/8-sss_ssh_knownhostsproxy/">sss_ssh_knownhostsproxy</a></code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)</p>
<h2>Authors</h2>
<p><code>The SSSD upstream &#8211; <a rel="nofollow" href="https://pagure.io/SSSD/sssd/">https://pagure.io/SSSD/sssd/</a></code></p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>[MS-ADTS] section LDAP extensions</p>
<dl>
<dd><a rel="nofollow" href="https://msdn.microsoft.com/en-us/library/cc223367.aspx">https://msdn.microsoft.com/en-us/library/cc223367.aspx</a></dl>
