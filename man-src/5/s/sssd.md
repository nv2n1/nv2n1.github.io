---
title: "sssd(5)"
name: "sssd"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sssd/"
description: "sssd.conf – the configuration file for SSSD"
---
<p>sssd.conf &#8211; the configuration file for SSSD </p>
<h2>FILE FORMAT</h2>
<p>The file has an ini-style syntax and consists of sections and parameters. A section begins with the name of the section in square brackets and continues until the next section begins. An example of section with single and multi-valued parameters: </p>
<dl>
<dd> <pre><code> [section]  key  = value  key2  = value2,value3 
</code></pre>
 </dd></dl>
<p>The data types used are string (no quotes needed), integer and bool (with values of "TRUE/FALSE"). </p>
<p>A line comment starts with a hash sign ("#") or a semicolon (";"). Inline comments are not supported. </p>
<p>All sections can have an optional <i>description</i> parameter. Its function is only as a label for the section. </p>
<p>sssd.conf must be a regular file, owned by root and only root may read from or write to the file.  </p>
<h2>GENERAL OPTIONS</h2>
<p>Following options are usable in more than one configuration sections.  </p>
<h3>Options usable in all sections</h3>
<p>debug_level (integer) </p>
<dl>
<dd> <p> SSSD supports two representations for specifying the debug level. The simplest is to specify a decimal value from 0-9, which represents enabling that level and all lower-level debug messages. The more comprehensive option is to specify a hexadecimal bitmask to enable or disable specific levels (such as if you wish to suppress a level). </p>
<p>Currently supported debug levels: </p>
<p> <i>0</i>, <i>0x0010</i>: Fatal failures. Anything that would prevent SSSD from starting up or causes it to cease running. </p>
<p> <i>1</i>, <i>0x0020</i>: Critical failures. An error that doesn&#8217;t kill the SSSD, but one that indicates that at least one major feature is not going to work properly. </p>
<p> <i>2</i>, <i>0x0040</i>: Serious failures. An error announcing that a particular request or operation has failed. </p>
<p> <i>3</i>, <i>0x0080</i>: Minor failures. These are the errors that would percolate down to cause the operation failure of 2. </p>
<p> <i>4</i>, <i>0x0100</i>: Configuration settings. </p>
<p> <i>5</i>, <i>0x0200</i>: Function data. </p>
<p> <i>6</i>, <i>0x0400</i>: Trace messages for operation functions. </p>
<p> <i>7</i>, <i>0x1000</i>: Trace messages for internal control functions. </p>
<p> <i>8</i>, <i>0x2000</i>: Contents of function-internal variables that may be interesting. </p>
<p> <i>9</i>, <i>0x4000</i>: Extremely low-level tracing information. </p>
<p>To log required bitmask debug levels, simply add their numbers together as shown in following examples: </p>
<p> <i>Example</i>: To log fatal failures, critical failures, serious failures and function data use 0x0270. </p>
<p> <i>Example</i>: To log fatal failures, configuration settings, function data, trace messages for internal control functions use 0x1310. </p>
<p> <i>Note</i>: The bitmask format of debug levels was introduced in 1.7.0. </p>
<p> <i>Default</i>: 0 </p>
 </dd></dl>
<p>debug_timestamps (bool) </p>
<dl>
<dd> <p> Add a timestamp to the debug messages </p>
<p>Default: true </p>
 </dd></dl>
<p>debug_microseconds (bool) </p>
<dl>
<dd> <p> Add microseconds to the timestamp in debug messages </p>
<p>Default: false </p>
 </dd></dl>
<h3>Options usable in SERVICE and DOMAIN sections</h3>
<p>timeout (integer) </p>
<dl>
<dd> <p> Timeout in seconds between heartbeats for this service. This is used to ensure that the process is alive and capable of answering requests. </p>
<p>Default: 10 </p>
 </dd></dl>
<h2>SPECIAL SECTIONS</h2>
<h3>The [sssd] section</h3>
<p>Individual pieces of SSSD functionality are provided by special SSSD services that are started and stopped together with SSSD. The services are managed by a special service frequently called "monitor". The "[sssd]" section is used to configure the monitor as well as some other important options like the identity domains. </p>
<p> <code>Section parameters</code> </p>
<p>config_file_version (integer) </p>
<dl>
<dd> <p> Indicates what is the syntax of the config file. SSSD 0.6.0 and later use version 2. </p>
 </dd></dl>
<p>services </p>
<dl>
<dd> <p> Comma separated list of services that are started when sssd itself starts. </p>
<p>Supported services: nss, pam , sudo, autofs, ssh, pac, ifp </p>
 </dd></dl>
<p>reconnection_retries (integer) </p>
<dl>
<dd> <p> Number of times services should attempt to reconnect in the event of a Data Provider crash or restart before they give up </p>
<p>Default: 3 </p>
 </dd></dl>
<p>domains </p>
<dl>
<dd> <p> A domain is a database containing user information. SSSD can use more domains at the same time, but at least one must be configured or SSSD won&#8217;t start. This parameter described the list of domains in the order you want them to be queried. A domain name should only consist of alphanumeric ASCII characters, dashes and underscores. </p>
 </dd></dl>
<p>re_expression (string) </p>
<dl>
<dd> <p> Default regular expression that describes how to parse the string containing user name and domain into these components. </p>
<p>Each domain can have an individual regular expression configured. For some ID providers there are also default regular expressions. See DOMAIN SECTIONS for more info on these regular expressions. </p>
 </dd></dl>
<p>full_name_format (string) </p>
<dl>
<dd> <p> A <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3)-compatible format that describes how to compose a fully qualified name from user name and domain name components. </p>
<p>The following expansions are supported: </p>
<p>%1$s </p>
 </dd>
<dl>
<dd> <p> user name </p>
 </dd></dl>
<p>%2$s </p>
<dl>
<dd> <p> domain name as specified in the SSSD config file. </p>
 </dd></dl>
<p>%3$s </p>
<dl>
<dd> <p> domain flat name. Mostly usable for Active Directory domains, both directly configured or discovered via IPA trusts. </p>
 </dd></dl>
<p>Each domain can have an individual format string configured. see DOMAIN SECTIONS for more info on this option. </dl>
 </p>
<p>try_inotify (boolean) </p>
<dl>
<dd> <p> SSSD monitors the state of resolv.conf to identify when it needs to update its internal DNS resolver. By default, we will attempt to use inotify for this, and will fall back to polling resolv.conf every five seconds if inotify cannot be used. </p>
<p>There are some limited situations where it is preferred that we should skip even trying to use inotify. In these rare cases, this option should be set to &#8216;false&#8217; </p>
<p>Default: true on platforms where inotify is supported. False on other platforms. </p>
<p>Note: this option will have no effect on platforms where inotify is unavailable. On these platforms, polling will always be used. </p>
 </dd></dl>
<p>krb5_rcache_dir (string) </p>
<dl>
<dd> <p> Directory on the filesystem where SSSD should store Kerberos replay cache files. </p>
<p>This option accepts a special value __LIBKRB5_DEFAULTS__ that will instruct SSSD to let libkrb5 decide the appropriate location for the replay cache. </p>
<p>Default: Distribution-specific and specified at build-time. (__LIBKRB5_DEFAULTS__ if not configured) </p>
 </dd></dl>
<p>default_domain_suffix (string) </p>
<dl>
<dd> <p> This string will be used as a default domain name for all names without a domain name component. The main use case is environments where the primary domain is intended for managing host policies and all users are located in a trusted domain. The option allows those users to log in just with their user name without giving a domain name as well. </p>
<p>Please note that if this option is set all users from the primary domain have to use their fully qualified name, e.g. user [at] domain.name, to log in. </p>
<p>Default: not set </p>
 </dd></dl>
<p>override_space (string) </p>
<dl>
<dd> <p> This parameter will replace spaces (space bar) with the given character for user and group names. e.g. (_). User name &quot;john doe&quot; will be &quot;john_doe&quot; This feature was added to help compatibility with shell scripts that have difficulty handling spaces, due to the default field separator in the shell. </p>
<p>Please note it is a configuration error to use a replacement character that might be used in user or group names. If a name contains the replacement character SSSD tries to return the unmodified name but in general the result of a lookup is undefined. </p>
<p>Default: not set (spaces will not be replaced) </p>
 </dd></dl>
<h2>SERVICES SECTIONS</h2>
<p>Settings that can be used to configure different services are described in this section. They should reside in the [<i>$NAME</i>] section, for example, for NSS service, the section would be "[nss]"  </p>
<h3>General service configuration options</h3>
<p>These options can be used to configure any service. </p>
<p>reconnection_retries (integer) </p>
<dl>
<dd> <p> Number of times services should attempt to reconnect in the event of a Data Provider crash or restart before they give up </p>
<p>Default: 3 </p>
 </dd></dl>
<p>fd_limit </p>
<dl>
<dd> <p> This option specifies the maximum number of file descriptors that may be opened at one time by this SSSD process. On systems where SSSD is granted the CAP_SYS_RESOURCE capability, this will be an absolute setting. On systems without this capability, the resulting value will be the lower value of this or the limits.conf &quot;hard&quot; limit. </p>
<p>Default: 8192 (or limits.conf &quot;hard&quot; limit) </p>
 </dd></dl>
<p>client_idle_timeout </p>
<dl>
<dd> <p> This option specifies the number of seconds that a client of an SSSD process can hold onto a file descriptor without communicating on it. This value is limited in order to avoid resource exhaustion on the system. </p>
<p>Default: 60 </p>
 </dd></dl>
<p>force_timeout (integer) </p>
<dl>
<dd> <p> If a service is not responding to ping checks (see the "timeout" option), it is first sent the SIGTERM signal that instructs it to quit gracefully. If the service does not terminate after "force_timeout" seconds, the monitor will forcibly shut it down by sending a SIGKILL signal. </p>
<p>Default: 60 </p>
 </dd></dl>
<p>offline_timeout (integer) </p>
<dl>
<dd> <p> When SSSD switches to offline mode the amount of time before it tries to go back online will increase based upon the time spent disconnected. This value is in seconds and calculated by the following: </p>
<p>offline_timeout + random_offset </p>
<p>The random offset can increment up to 30 seconds. After each unsuccessful attempt to go online, the new interval is recalculated by the following: </p>
<p>new_interval = old_interval*2 + random_offset </p>
<p>Note that the maximum length of each interval is currently limited to one hour. If the calculated length of new_interval is greater than an hour, it will be forced to one hour. </p>
<p>Default: 60 </p>
 </dd></dl>
<h3>NSS configuration options</h3>
<p>These options can be used to configure the Name Service Switch (NSS) service. </p>
<p>enum_cache_timeout (integer) </p>
<dl>
<dd> <p> How many seconds should nss_sss cache enumerations (requests for info about all users) </p>
<p>Default: 120 </p>
 </dd></dl>
<p>entry_cache_nowait_percentage (integer) </p>
<dl>
<dd> <p> The entry cache can be set to automatically update entries in the background if they are requested beyond a percentage of the entry_cache_timeout value for the domain. </p>
<p>For example, if the domain&#8217;s entry_cache_timeout is set to 30s and entry_cache_nowait_percentage is set to 50 (percent), entries that come in after 15 seconds past the last cache update will be returned immediately, but the SSSD will go and update the cache on its own, so that future requests will not need to block waiting for a cache update. </p>
<p>Valid values for this option are 0-99 and represent a percentage of the entry_cache_timeout for each domain. For performance reasons, this percentage will never reduce the nowait timeout to less than 10 seconds. (0 disables this feature) </p>
<p>Default: 50 </p>
 </dd></dl>
<p>entry_negative_timeout (integer) </p>
<dl>
<dd> <p> Specifies for how many seconds nss_sss should cache negative cache hits (that is, queries for invalid database entries, like nonexistent ones) before asking the back end again. </p>
<p>Default: 15 </p>
 </dd></dl>
<p>filter_users, filter_groups (string) </p>
<dl>
<dd> <p> Exclude certain users from being fetched from the sss NSS database. This is particularly useful for system accounts. This option can also be set per-domain or include fully-qualified names to filter only users from the particular domain. </p>
<p>Default: root </p>
 </dd></dl>
<p>filter_users_in_groups (bool) </p>
<dl>
<dd> <p> If you want filtered user still be group members set this option to false. </p>
<p>Default: true </p>
 </dd></dl>
<p>override_homedir (string) </p>
<dl>
<dd> <p> Override the user&#8217;s home directory. You can either provide an absolute value or a template. In the template, the following sequences are substituted: </p>
<p>%u </p>
 </dd>
<dl>
<dd> <p> login name </p>
 </dd></dl>
<p>%U </p>
<dl>
<dd> <p> UID number </p>
 </dd></dl>
<p>%d </p>
<dl>
<dd> <p> domain name </p>
 </dd></dl>
<p>%f </p>
<dl>
<dd> <p> fully qualified user name (user [at] domain) </p>
 </dd></dl>
<p>%P </p>
<dl>
<dd> <p> UPN - User Principal Name (name [at] REALM) </p>
 </dd></dl>
<p>%o </p>
<dl>
<dd> <p> The original home directory retrieved from the identity provider. </p>
 </dd></dl>
<p>%H </p>
<dl>
<dd> <p> The value of configure option <i>homedir_substring</i>. </p>
 </dd></dl>
<p>%% </p>
<dl>
<dd> <p> a literal &#8216;%&#8216; </p>
 </dd></dl>
<p>This option can also be set per-domain. </p>
<p>example: </p>
<dl>
<dd> <pre><code>override_homedir = /home/%u
</code></pre>
 </dd></dl>
<p>Default: Not set (SSSD will use the value retrieved from LDAP) </dl>
 </p>
<p>homedir_substring (string) </p>
<dl>
<dd> <p> The value of this option will be used in the expansion of the <i>override_homedir</i> option if the template contains the format string <i>%H</i>. An LDAP directory entry can directly contain this template so that this option can be used to expand the home directory path for each client machine (or operating system). It can be set per-domain or globally in the [nss] section. A value specified in a domain section will override one set in the [nss] section. </p>
<p>Default: /home </p>
 </dd></dl>
<p>fallback_homedir (string) </p>
<dl>
<dd> <p> Set a default template for a user&#8217;s home directory if one is not specified explicitly by the domain&#8217;s data provider. </p>
<p>The available values for this option are the same as for override_homedir. </p>
<p>example: </p>
 </dd>
<dl>
<dd> <pre><code>fallback_homedir = /home/%u
</code></pre>
 </dd></dl>
<p>Default: not set (no substitution for unset home directories) </dl>
 </p>
<p>override_shell (string) </p>
<dl>
<dd> <p> Override the login shell for all users. This option supersedes any other shell options if it takes effect and can be set either in the [nss] section or per-domain. </p>
<p>Default: not set (SSSD will use the value retrieved from LDAP) </p>
 </dd></dl>
<p>allowed_shells (string) </p>
<dl>
<dd> <p> Restrict user shell to one of the listed values. The order of evaluation is: </p>
<p>1. If the shell is present in "/etc/shells", it is used. </p>
<p>2. If the shell is in the allowed_shells list but not in "/etc/shells", use the value of the shell_fallback parameter. </p>
<p>3. If the shell is not in the allowed_shells list and not in "/etc/shells", a nologin shell is used. </p>
<p>An empty string for shell is passed as-is to libc. </p>
<p>The "/etc/shells" is only read on SSSD start up, which means that a restart of the SSSD is required in case a new shell is installed. </p>
<p>Default: Not set. The user shell is automatically used. </p>
 </dd></dl>
<p>vetoed_shells (string) </p>
<dl>
<dd> <p> Replace any instance of these shells with the shell_fallback </p>
 </dd></dl>
<p>shell_fallback (string) </p>
<dl>
<dd> <p> The default shell to use if an allowed shell is not installed on the machine. </p>
<p>Default: /bin/sh </p>
 </dd></dl>
<p>default_shell </p>
<dl>
<dd> <p> The default shell to use if the provider does not return one during lookup. This option can be specified globally in the [nss] section or per-domain. </p>
<p>Default: not set (Return NULL if no shell is specified and rely on libc to substitute something sensible when necessary, usually /bin/sh) </p>
 </dd></dl>
<p>get_domains_timeout (int) </p>
<dl>
<dd> <p> Specifies time in seconds for which the list of subdomains will be considered valid. </p>
<p>Default: 60 </p>
 </dd></dl>
<p>memcache_timeout (int) </p>
<dl>
<dd> <p> Specifies time in seconds for which records in the in-memory cache will be valid </p>
<p>Default: 300 </p>
 </dd></dl>
<h3>PAM configuration options</h3>
<p>These options can be used to configure the Pluggable Authentication Module (PAM) service. </p>
<p>offline_credentials_expiration (integer) </p>
<dl>
<dd> <p> If the authentication provider is offline, how long should we allow cached logins (in days since the last successful online login). </p>
<p>Default: 0 (No limit) </p>
 </dd></dl>
<p>offline_failed_login_attempts (integer) </p>
<dl>
<dd> <p> If the authentication provider is offline, how many failed login attempts are allowed. </p>
<p>Default: 0 (No limit) </p>
 </dd></dl>
<p>offline_failed_login_delay (integer) </p>
<dl>
<dd> <p> The time in minutes which has to pass after offline_failed_login_attempts has been reached before a new login attempt is possible. </p>
<p>If set to 0 the user cannot authenticate offline if offline_failed_login_attempts has been reached. Only a successful online authentication can enable offline authentication again. </p>
<p>Default: 5 </p>
 </dd></dl>
<p>pam_verbosity (integer) </p>
<dl>
<dd> <p> Controls what kind of messages are shown to the user during authentication. The higher the number to more messages are displayed. </p>
<p>Currently sssd supports the following values: </p>
<p> <i>0</i>: do not show any message </p>
<p> <i>1</i>: show only important messages </p>
<p> <i>2</i>: show informational messages </p>
<p> <i>3</i>: show all messages and debug information </p>
<p>Default: 1 </p>
 </dd></dl>
<p>pam_id_timeout (integer) </p>
<dl>
<dd> <p> For any PAM request while SSSD is online, the SSSD will attempt to immediately update the cached identity information for the user in order to ensure that authentication takes place with the latest information. </p>
<p>A complete PAM conversation may perform multiple PAM requests, such as account management and session opening. This option controls (on a per-client-application basis) how long (in seconds) we can cache the identity information to avoid excessive round-trips to the identity provider. </p>
<p>Default: 5 </p>
 </dd></dl>
<p>pam_pwd_expiration_warning (integer) </p>
<dl>
<dd> <p> Display a warning N days before the password expires. </p>
<p>Please note that the backend server has to provide information about the expiration time of the password. If this information is missing, sssd cannot display a warning. </p>
<p>If zero is set, then this filter is not applied, i.e. if the expiration warning was received from backend server, it will automatically be displayed. </p>
<p>This setting can be overridden by setting <i>pwd_expiration_warning</i> for a particular domain. </p>
<p>Default: 0 </p>
 </dd></dl>
<p>get_domains_timeout (int) </p>
<dl>
<dd> <p> Specifies time in seconds for which the list of subdomains will be considered valid. </p>
<p>Default: 60 </p>
 </dd></dl>
<p>pam_trusted_users (string) </p>
<dl>
<dd> <p> Specifies the comma-separated list of UID values or user names that are allowed to access the PAM responder. User names are resolved to UIDs at startup. </p>
<p>Default: all (All users are allowed to access the PAM responder) </p>
<p>Please note that UID 0 is always allowed to access the PAM responder even in case it is not in the pam_trusted_users list. </p>
<p>Also please note that if there is a user name in pam_trusted_users list which fails to be resolved it will cause that SSSD will not be started. </p>
 </dd></dl>
<p>pam_public_domains (string) </p>
<dl>
<dd> <p> Specifies the comma-separated list of domain names that are accessible even to untrusted users. </p>
<p>Two special values for pam_public_domains option are defined: </p>
<p>all (Untrusted users are allowed to access all domains in PAM responder.) </p>
<p>none (Untrusted users are not allowed to access any domains PAM in responder.) </p>
<p>Default: none </p>
 </dd></dl>
<h3>SUDO configuration options</h3>
<p>These options can be used to configure the sudo service. The detailed instructions for configuration of <code><a href="/docs/linux/man/8-sudo/">sudo</a></code>(8) to work with <code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8) are in the manual page <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5). </p>
<p>sudo_timed (bool) </p>
<dl>
<dd> <p> Whether or not to evaluate the sudoNotBefore and sudoNotAfter attributes that implement time-dependent sudoers entries. </p>
<p>Default: false </p>
 </dd></dl>
<h3>AUTOFS configuration options</h3>
<p>These options can be used to configure the autofs service. </p>
<p>autofs_negative_timeout (integer) </p>
<dl>
<dd> <p> Specifies for how many seconds should the autofs responder negative cache hits (that is, queries for invalid map entries, like nonexistent ones) before asking the back end again. </p>
<p>Default: 15 </p>
 </dd></dl>
<p>Please note that the automounter only reads the master map on startup, so if any autofs-related changes are made to the sssd.conf, you typically also need to restart the automounter daemon after restarting the SSSD.  </p>
<h3>SSH configuration options</h3>
<p>These options can be used to configure the SSH service. </p>
<p>ssh_hash_known_hosts (bool) </p>
<dl>
<dd> <p> Whether or not to hash host names and addresses in the managed known_hosts file. </p>
<p>Default: true </p>
 </dd></dl>
<p>ssh_known_hosts_timeout (integer) </p>
<dl>
<dd> <p> How many seconds to keep a host in the managed known_hosts file after its host keys were requested. </p>
<p>Default: 180 </p>
 </dd></dl>
<h3>PAC responder configuration options</h3>
<p>The PAC responder works together with the authorization data plugin for MIT Kerberos sssd_pac_plugin.so and a sub-domain provider. The plugin sends the PAC data during a GSSAPI authentication to the PAC responder. The sub-domain provider collects domain SID and ID ranges of the domain the client is joined to and of remote trusted domains from the local domain controller. If the PAC is decoded and evaluated some of the following operations are done: </p>
<dl>
<dd> <p> &bull; If the remote user does not exist in the cache, it is created. The uid is determined with the help of the SID, trusted domains will have UPGs and the gid will have the same value as the uid. The home directory is set based on the subdomain_homedir parameter. The shell will be empty by default, i.e. the system defaults are used, but can be overwritten with the default_shell parameter. </p>
 </dd></dl>
<dl>
<dd> <p> &bull; If there are SIDs of groups from domains sssd knows about, the user will be added to those groups. </p>
 </dd></dl>
<p>These options can be used to configure the PAC responder. </p>
<p>allowed_uids (string) </p>
<dl>
<dd> <p> Specifies the comma-separated list of UID values or user names that are allowed to access the PAC responder. User names are resolved to UIDs at startup. </p>
<p>Default: 0 (only the root user is allowed to access the PAC responder) </p>
<p>Please note that although the UID 0 is used as the default it will be overwritten with this option. If you still want to allow the root user to access the PAC responder, which would be the typical case, you have to add 0 to the list of allowed UIDs as well. </p>
 </dd></dl>
<h2>DOMAIN SECTIONS</h2>
<p>These configuration options can be present in a domain configuration section, that is, in a section called "[domain/<i>NAME</i>]" </p>
<p>min_id,max_id (integer) </p>
<dl>
<dd> <p> UID and GID limits for the domain. If a domain contains an entry that is outside these limits, it is ignored. </p>
<p>For users, this affects the primary GID limit. The user will not be returned to NSS if either the UID or the primary GID is outside the range. For non-primary group memberships, those that are in range will be reported as expected. </p>
<p>These ID limits affect even saving entries to cache, not only returning them by name or ID. </p>
<p>Default: 1 for min_id, 0 (no limit) for max_id </p>
 </dd></dl>
<p>enumerate (bool) </p>
<dl>
<dd> <p> Determines if a domain can be enumerated. This parameter can have one of the following values: </p>
<p>TRUE = Users and groups are enumerated </p>
<p>FALSE = No enumerations for this domain </p>
<p>Default: FALSE </p>
<p>Note: Enabling enumeration has a moderate performance impact on SSSD while enumeration is running. It may take up to several minutes after SSSD startup to fully complete enumerations. During this time, individual requests for information will go directly to LDAP, though it may be slow, due to the heavy enumeration processing. Saving a large number of entries to cache after the enumeration completes might also be CPU intensive as the memberships have to be recomputed. </p>
<p>While the first enumeration is running, requests for the complete user or group lists may return no results until it completes. </p>
<p>Further, enabling enumeration may increase the time necessary to detect network disconnection, as longer timeouts are required to ensure that enumeration lookups are completed successfully. For more information, refer to the man pages for the specific id_provider in use. </p>
<p>For the reasons cited above, enabling enumeration is not recommended, especially in large environments. </p>
 </dd></dl>
<p>subdomain_enumerate (string) </p>
<dl>
<dd> <p> Whether any of autodetected trusted domains should be enumerated. The supported values are: </p>
<p>all </p>
 </dd>
<dl>
<dd> <p> All discovered trusted domains will be enumerated </p>
 </dd></dl>
<p>none </p>
<dl>
<dd> <p> No discovered trusted domains will be enumerated </p>
 </dd></dl>
<p>Optionally, a list of one or more domain names can enable enumeration just for these trusted domains. </p>
<p>Default: none </dl>
 </p>
<p>force_timeout (integer) </p>
<dl>
<dd> <p> If a service is not responding to ping checks (see the "timeout" option), it is first sent the SIGTERM signal that instructs it to quit gracefully. If the service does not terminate after "force_timeout" seconds, the monitor will forcibly shut it down by sending a SIGKILL signal. </p>
<p>Default: 60 </p>
 </dd></dl>
<p>entry_cache_timeout (integer) </p>
<dl>
<dd> <p> How many seconds should nss_sss consider entries valid before asking the backend again </p>
<p>The cache expiration timestamps are stored as attributes of individual objects in the cache. Therefore, changing the cache timeout only has effect for newly added or expired entries. You should run the <code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8) tool in order to force refresh of entries that have already been cached. </p>
<p>Default: 5400 </p>
 </dd></dl>
<p>entry_cache_user_timeout (integer) </p>
<dl>
<dd> <p> How many seconds should nss_sss consider user entries valid before asking the backend again </p>
<p>Default: entry_cache_timeout </p>
 </dd></dl>
<p>entry_cache_group_timeout (integer) </p>
<dl>
<dd> <p> How many seconds should nss_sss consider group entries valid before asking the backend again </p>
<p>Default: entry_cache_timeout </p>
 </dd></dl>
<p>entry_cache_netgroup_timeout (integer) </p>
<dl>
<dd> <p> How many seconds should nss_sss consider netgroup entries valid before asking the backend again </p>
<p>Default: entry_cache_timeout </p>
 </dd></dl>
<p>entry_cache_service_timeout (integer) </p>
<dl>
<dd> <p> How many seconds should nss_sss consider service entries valid before asking the backend again </p>
<p>Default: entry_cache_timeout </p>
 </dd></dl>
<p>entry_cache_sudo_timeout (integer) </p>
<dl>
<dd> <p> How many seconds should sudo consider rules valid before asking the backend again </p>
<p>Default: entry_cache_timeout </p>
 </dd></dl>
<p>entry_cache_autofs_timeout (integer) </p>
<dl>
<dd> <p> How many seconds should the autofs service consider automounter maps valid before asking the backend again </p>
<p>Default: entry_cache_timeout </p>
 </dd></dl>
<p>entry_cache_ssh_host_timeout (integer) </p>
<dl>
<dd> <p> How many seconds to keep a host ssh key after refresh. IE how long to cache the host key for. </p>
<p>Default: entry_cache_timeout </p>
 </dd></dl>
<p>refresh_expired_interval (integer) </p>
<dl>
<dd> <p> Specifies how many seconds SSSD has to wait before triggering a background refresh task which will refresh all expired or nearly expired records. </p>
<p>Currently only refreshing expired netgroups is supported. </p>
<p>You can consider setting this value to 3/4 * entry_cache_timeout. </p>
<p>Default: 0 (disabled) </p>
 </dd></dl>
<p>cache_credentials (bool) </p>
<dl>
<dd> <p> Determines if user credentials are also cached in the local LDB cache </p>
<p>User credentials are stored in a SHA512 hash, not in plaintext </p>
<p>Default: FALSE </p>
 </dd></dl>
<p>account_cache_expiration (integer) </p>
<dl>
<dd> <p> Number of days entries are left in cache after last successful login before being removed during a cleanup of the cache. 0 means keep forever. The value of this parameter must be greater than or equal to offline_credentials_expiration. </p>
<p>Default: 0 (unlimited) </p>
 </dd></dl>
<p>pwd_expiration_warning (integer) </p>
<dl>
<dd> <p> Display a warning N days before the password expires. </p>
<p>If zero is set, then this filter is not applied, i.e. if the expiration warning was received from backend server, it will automatically be displayed. </p>
<p>Please note that the backend server has to provide information about the expiration time of the password. If this information is missing, sssd cannot display a warning. Also an auth provider has to be configured for the backend. </p>
<p>Default: 7 (Kerberos), 0 (LDAP) </p>
 </dd></dl>
<p>id_provider (string) </p>
<dl>
<dd> <p> The identification provider used for the domain. Supported ID providers are: </p>
<p>"proxy": Support a legacy NSS provider </p>
<p>"local": SSSD internal provider for local users </p>
<p>"ldap": LDAP provider. See <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5) for more information on configuring LDAP. </p>
<p>"ipa": FreeIPA and Red Hat Enterprise Identity Management provider. See <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5) for more information on configuring FreeIPA. </p>
<p>"ad": Active Directory provider. See <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5) for more information on configuring Active Directory. </p>
 </dd></dl>
<p>use_fully_qualified_names (bool) </p>
<dl>
<dd> <p> Use the full name and domain (as formatted by the domain&#8217;s full_name_format) as the user&#8217;s login name reported to NSS. </p>
<p>If set to TRUE, all requests to this domain must use fully qualified names. For example, if used in LOCAL domain that contains a &quot;test&quot; user, <code>getent passwd test</code> wouldn&#8217;t find the user while <code>getent passwd test [at] LOCAL</code> would. </p>
<p>NOTE: This option has no effect on netgroup lookups due to their tendency to include nested netgroups without qualified names. For netgroups, all domains will be searched when an unqualified name is requested. </p>
<p>Default: FALSE </p>
 </dd></dl>
<p>ignore_group_members (bool) </p>
<dl>
<dd> <p> Do not return group members for group lookups. </p>
<p>If set to TRUE, the group membership attribute is not requested from the ldap server, and group members are not returned when processing group lookup calls. </p>
<p>Default: FALSE </p>
 </dd></dl>
<p>auth_provider (string) </p>
<dl>
<dd> <p> The authentication provider used for the domain. Supported auth providers are: </p>
<p>"ldap" for native LDAP authentication. See <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5) for more information on configuring LDAP. </p>
<p>"krb5" for Kerberos authentication. See <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5) for more information on configuring Kerberos. </p>
<p>"ipa": FreeIPA and Red Hat Enterprise Identity Management provider. See <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5) for more information on configuring FreeIPA. </p>
<p>"ad": Active Directory provider. See <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5) for more information on configuring Active Directory. </p>
<p>"proxy" for relaying authentication to some other PAM target. </p>
<p>"local": SSSD internal provider for local users </p>
<p>"none" disables authentication explicitly. </p>
<p>Default: "id_provider" is used if it is set and can handle authentication requests. </p>
 </dd></dl>
<p>access_provider (string) </p>
<dl>
<dd> <p> The access control provider used for the domain. There are two built-in access providers (in addition to any included in installed backends) Internal special providers are: </p>
<p>"permit" always allow access. It&#8217;s the only permitted access provider for a local domain. </p>
<p>"deny" always deny access. </p>
<p>"ldap" for native LDAP authentication. See <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5) for more information on configuring LDAP. </p>
<p>"ipa": FreeIPA and Red Hat Enterprise Identity Management provider. See <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5) for more information on configuring FreeIPA. </p>
<p>"ad": Active Directory provider. See <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5) for more information on configuring Active Directory. </p>
<p>"simple" access control based on access or deny lists. See <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5) for more information on configuring the simple access module. </p>
<p>Default: "permit" </p>
 </dd></dl>
<p>chpass_provider (string) </p>
<dl>
<dd> <p> The provider which should handle change password operations for the domain. Supported change password providers are: </p>
<p>"ldap" to change a password stored in a LDAP server. See <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5) for more information on configuring LDAP. </p>
<p>"krb5" to change the Kerberos password. See <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5) for more information on configuring Kerberos. </p>
<p>"ipa": FreeIPA and Red Hat Enterprise Identity Management provider. See <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5) for more information on configuring FreeIPA. </p>
<p>"ad": Active Directory provider. See <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5) for more information on configuring Active Directory. </p>
<p>"proxy" for relaying password changes to some other PAM target. </p>
<p>"none" disallows password changes explicitly. </p>
<p>Default: "auth_provider" is used if it is set and can handle change password requests. </p>
 </dd></dl>
<p>sudo_provider (string) </p>
<dl>
<dd> <p> The SUDO provider used for the domain. Supported SUDO providers are: </p>
<p>"ldap" for rules stored in LDAP. See <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5) for more information on configuring LDAP. </p>
<p>"ipa" the same as "ldap" but with IPA default settings. </p>
<p>"ad" the same as "ldap" but with AD default settings. </p>
<p>"none" disables SUDO explicitly. </p>
<p>Default: The value of "id_provider" is used if it is set. </p>
<p>The detailed instructions for configuration of sudo_provider are in the manual page <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5). There are many configuration options that can be used to adjust the behavior. Please refer to &quot;ldap_sudo_*&quot; in <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5). </p>
 </dd></dl>
<p>selinux_provider (string) </p>
<dl>
<dd> <p> The provider which should handle loading of selinux settings. Note that this provider will be called right after access provider ends. Supported selinux providers are: </p>
<p>"ipa" to load selinux settings from an IPA server. See <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5) for more information on configuring IPA. </p>
<p>"none" disallows fetching selinux settings explicitly. </p>
<p>Default: "id_provider" is used if it is set and can handle selinux loading requests. </p>
 </dd></dl>
<p>subdomains_provider (string) </p>
<dl>
<dd> <p> The provider which should handle fetching of subdomains. This value should be always the same as id_provider. Supported subdomain providers are: </p>
<p>"ipa" to load a list of subdomains from an IPA server. See <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5) for more information on configuring IPA. </p>
<p>"ad" to load a list of subdomains from an Active Directory server. See <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5) for more information on configuring the AD provider. </p>
<p>"none" disallows fetching subdomains explicitly. </p>
<p>Default: The value of "id_provider" is used if it is set. </p>
 </dd></dl>
<p>autofs_provider (string) </p>
<dl>
<dd> <p> The autofs provider used for the domain. Supported autofs providers are: </p>
<p>"ldap" to load maps stored in LDAP. See <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5) for more information on configuring LDAP. </p>
<p>"ipa" to load maps stored in an IPA server. See <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5) for more information on configuring IPA. </p>
<p>"none" disables autofs explicitly. </p>
<p>Default: The value of "id_provider" is used if it is set. </p>
 </dd></dl>
<p>hostid_provider (string) </p>
<dl>
<dd> <p> The provider used for retrieving host identity information. Supported hostid providers are: </p>
<p>"ipa" to load host identity stored in an IPA server. See <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5) for more information on configuring IPA. </p>
<p>"none" disables hostid explicitly. </p>
<p>Default: The value of "id_provider" is used if it is set. </p>
 </dd></dl>
<p>re_expression (string) </p>
<dl>
<dd> <p> Regular expression for this domain that describes how to parse the string containing user name and domain into these components. The &quot;domain&quot; can match either the SSSD configuration domain name, or, in the case of IPA trust subdomains and Active Directory domains, the flat (NetBIOS) name of the domain. </p>
<p>Default for the AD and IPA provider: "(((?P&lt;domain&gt;[^\\]+)\\(?P&lt;name&gt;.+$))|((?P&lt;name&gt;[^@]+)@(?P&lt;domain&gt;.+$))|(^(?P&lt;name&gt;[^@\\]+)$))" which allows three different styles for user names: </p>
 </dd>
<dl>
<dd> <p> &bull; username </p>
 </dd></dl>
<dl>
<dd> <p> &bull; username [at] domain.name </p>
 </dd></dl>
<dl>
<dd> <p> &bull; domain\username </p>
 </dd></dl>
<p>While the first two correspond to the general default the third one is introduced to allow easy integration of users from Windows domains. </p>
<p>Default: "(?P&lt;name&gt;[^@]+)@?(?P&lt;domain&gt;[^@]*$)" which translates to &quot;the name is everything up to the "@" sign, the domain everything after that&quot; </p>
<p>PLEASE NOTE: the support for non-unique named subpatterns is not available on all platforms (e.g. RHEL5 and SLES10). Only platforms with libpcre version 7 or higher can support non-unique named subpatterns. </p>
<p>PLEASE NOTE ALSO: older version of libpcre only support the Python syntax (?P&lt;name&gt;) to label subpatterns. </dl>
 </p>
<p>full_name_format (string) </p>
<dl>
<dd> <p> A <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3)-compatible format that describes how to compose a fully qualified name from user name and domain name components. </p>
<p>The following expansions are supported: </p>
<p>%1$s </p>
 </dd>
<dl>
<dd> <p> user name </p>
 </dd></dl>
<p>%2$s </p>
<dl>
<dd> <p> domain name as specified in the SSSD config file. </p>
 </dd></dl>
<p>%3$s </p>
<dl>
<dd> <p> domain flat name. Mostly usable for Active Directory domains, both directly configured or discovered via IPA trusts. </p>
 </dd></dl>
<p>Default: "%1$s@%2$s". </dl>
 </p>
<p>lookup_family_order (string) </p>
<dl>
<dd> <p> Provides the ability to select preferred address family to use when performing DNS lookups. </p>
<p>Supported values: </p>
<p>ipv4_first: Try looking up IPv4 address, if that fails, try IPv6 </p>
<p>ipv4_only: Only attempt to resolve hostnames to IPv4 addresses. </p>
<p>ipv6_first: Try looking up IPv6 address, if that fails, try IPv4 </p>
<p>ipv6_only: Only attempt to resolve hostnames to IPv6 addresses. </p>
<p>Default: ipv4_first </p>
 </dd></dl>
<p>dns_resolver_timeout (integer) </p>
<dl>
<dd> <p> Defines the amount of time (in seconds) to wait for a reply from the DNS resolver before assuming that it is unreachable. If this timeout is reached, the domain will continue to operate in offline mode. </p>
<p>Default: 6 </p>
 </dd></dl>
<p>dns_discovery_domain (string) </p>
<dl>
<dd> <p> If service discovery is used in the back end, specifies the domain part of the service discovery DNS query. </p>
<p>Default: Use the domain part of machine&#8217;s hostname </p>
 </dd></dl>
<p>override_gid (integer) </p>
<dl>
<dd> <p> Override the primary GID value with the one specified. </p>
 </dd></dl>
<p>case_sensitive (string) </p>
<dl>
<dd> <p> Treat user and group names as case sensitive. At the moment, this option is not supported in the local provider. Possible option values are: </p>
<p>True </p>
 </dd>
<dl>
<dd> <p> Case sensitive. This value is invalid for AD provider. </p>
 </dd></dl>
<p>False </p>
<dl>
<dd> <p> Case insensitive. </p>
 </dd></dl>
<p>Preserving </p>
<dl>
<dd> <p> Same as False (case insensitive), but does not lowercase names in the output of getpwnam and getgrnam. </p>
 </dd></dl>
<p>Default: True (False for AD provider) </dl>
 </p>
<p>proxy_fast_alias (boolean) </p>
<dl>
<dd> <p> When a user or group is looked up by name in the proxy provider, a second lookup by ID is performed to &quot;canonicalize&quot; the name in case the requested name was an alias. Setting this option to true would cause the SSSD to perform the ID lookup from cache for performance reasons. </p>
<p>Default: false </p>
 </dd></dl>
<p>subdomain_homedir (string) </p>
<dl>
<dd> <p> Use this homedir as default value for all subdomains within this domain in IPA AD trust. See <i>override_homedir</i> for info about possible values. In addition to those, the expansion below can only be used with <i>subdomain_homedir</i>. </p>
<p>%F </p>
 </dd>
<dl>
<dd> <p> flat (NetBIOS) name of a subdomain. </p>
 </dd></dl>
<p>The value can be overridden by <i>override_homedir</i> option. </p>
<p>Default: /home/%d/%u </dl>
 </p>
<p>realmd_tags (string) </p>
<dl>
<dd> <p> Various tags stored by the realmd configuration service for this domain. </p>
 </dd></dl>
<p>Options valid for proxy domains. </p>
<p>proxy_pam_target (string) </p>
<dl>
<dd> <p> The proxy target PAM proxies to. </p>
<p>Default: not set by default, you have to take an existing pam configuration or create a new one and add the service name here. </p>
 </dd></dl>
<p>proxy_lib_name (string) </p>
<dl>
<dd> <p> The name of the NSS library to use in proxy domains. The NSS functions searched for in the library are in the form of _nss_$(libName)_$(function), for example _nss_files_getpwent. </p>
 </dd></dl>
<h3>The local domain section</h3>
<p>This section contains settings for domain that stores users and groups in SSSD native database, that is, a domain that uses <i>id_provider=local</i>. </p>
<p> <code>Section parameters</code> </p>
<p>default_shell (string) </p>
<dl>
<dd> <p> The default shell for users created with SSSD userspace tools. </p>
<p>Default: /bin/bash </p>
 </dd></dl>
<p>base_directory (string) </p>
<dl>
<dd> <p> The tools append the login name to <i>base_directory</i> and use that as the home directory. </p>
<p>Default: /home </p>
 </dd></dl>
<p>create_homedir (bool) </p>
<dl>
<dd> <p> Indicate if a home directory should be created by default for new users. Can be overridden on command line. </p>
<p>Default: TRUE </p>
 </dd></dl>
<p>remove_homedir (bool) </p>
<dl>
<dd> <p> Indicate if a home directory should be removed by default for deleted users. Can be overridden on command line. </p>
<p>Default: TRUE </p>
 </dd></dl>
<p>homedir_umask (integer) </p>
<dl>
<dd> <p> Used by <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8) to specify the default permissions on a newly created home directory. </p>
<p>Default: 077 </p>
 </dd></dl>
<p>skel_dir (string) </p>
<dl>
<dd> <p> The skeleton directory, which contains files and directories to be copied in the user&#8217;s home directory, when the home directory is created by <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8) </p>
<p>Default: /etc/skel </p>
 </dd></dl>
<p>mail_dir (string) </p>
<dl>
<dd> <p> The mail spool directory. This is needed to manipulate the mailbox when its corresponding user account is modified or deleted. If not specified, a default value is used. </p>
<p>Default: /var/mail </p>
 </dd></dl>
<p>userdel_cmd (string) </p>
<dl>
<dd> <p> The command that is run after a user is removed. The command us passed the username of the user being removed as the first and only parameter. The return code of the command is not taken into account. </p>
<p>Default: None, no command is run </p>
 </dd></dl>
<h2>EXAMPLE</h2>
<p>The following example shows a typical SSSD config. It does not describe configuration of the domains themselves &#8211; refer to documentation on configuring domains for more details. </p>
<dl>
<dd> <pre><code>[sssd]
domains = LDAP
services = nss, pam
config_file_version = 2
[nss]
filter_groups = root
filter_users = root
[pam]
[domain/LDAP]
id_provider = ldap
ldap_uri =ldap://ldap.example.comldap_search_base = dc=example,dc=com
auth_provider = krb5
krb5_server = kerberos.example.com
krb5_realm = EXAMPLE.COM
cache_credentials = true
min_id = 10000
max_id = 20000
enumerate = False
</code></pre>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-sssd/">sssd</a></code>(8), <code>sssd.conf</code>(5), <code><a href="/docs/linux/man/5-sssd-ldap/">sssd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-sssd-krb5/">sssd-krb5</a></code>(5), <code><a href="/docs/linux/man/5-sssd-simple/">sssd-simple</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ipa/">sssd-ipa</a></code>(5), <code><a href="/docs/linux/man/5-sssd-ad/">sssd-ad</a></code>(5), <code><a href="/docs/linux/man/5-sssd-sudo/">sssd-sudo</a></code>(5),<code><a href="/docs/linux/man/8-sss_cache/">sss_cache</a></code>(8), <code><a href="/docs/linux/man/8-sss_debuglevel/">sss_debuglevel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupadd/">sss_groupadd</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupdel/">sss_groupdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupshow/">sss_groupshow</a></code>(8), <code><a href="/docs/linux/man/8-sss_groupmod/">sss_groupmod</a></code>(8), <code><a href="/docs/linux/man/8-sss_useradd/">sss_useradd</a></code>(8), <code><a href="/docs/linux/man/8-sss_userdel/">sss_userdel</a></code>(8), <code><a href="/docs/linux/man/8-sss_usermod/">sss_usermod</a></code>(8), <code><a href="/docs/linux/man/8-sss_obfuscate/">sss_obfuscate</a></code>(8), <code><a href="/docs/linux/man/8-sss_seed/">sss_seed</a></code>(8), <code><a href="/docs/linux/man/8-sssd_krb5_locator_plugin/">sssd_krb5_locator_plugin</a></code>(8), <code>sss_ssh_authorizedkeys</code>(8), <code>sss_ssh_knownhostsproxy</code>(8),<code><a href="/docs/linux/man/5-sssd-ifp/">sssd-ifp</a></code>(5),<code><a href="/docs/linux/man/8-pam_sss/">pam_sss</a></code>(8). <code><a href="/docs/linux/man/5-sss_rpcidmapd/">sss_rpcidmapd</a></code>(5)  </p>
<h2>AUTHORS</h2>
<p> <code>The SSSD upstream - <a rel="nofollow" href="http://fedorahosted.org/sssd">http://fedorahosted.org/sssd</a></code> </p>
