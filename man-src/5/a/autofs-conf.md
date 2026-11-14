---
title: "autofs-conf(5)"
name: "autofs-conf"
section: "5"
letter: "a"
url: "/docs/linux/man/5-autofs-conf/"
description: "autofs.conf – autofs configuration"
---

<p>autofs.conf &#8211; autofs configuration</p>
<h2>Description</h2>
<p>Configuration settings used by <code><a href="/docs/linux/man/8-automount/">automount</a></code>(8) may be changed in the configuration file <code>/etc/autofs.conf</code>. </p>
<p> This file contains two primary sections, <code>autofs</code> and <code>amd</code>. </p>
<p> Configuration entries may be present at the beginning of the configuration file without a section header and are implicitly included as part of the <code>autofs</code> section. </p>
<p> Each section name is enclosed in square brackets with spaces between the brackets and the section name. The <code>amd</code> section may be followed by further sections, named by the top level mount point path, that contain per mount configuration settings.</p>
<h2>SECTION autofs CONFIGURATION OPTIONS</h2>
<p>Configuration settings available are:</p>
<dl>
<dt><code>timeout</code></p>
<dd>Sets the default mount timeout in seconds. The internal program default is 10 minutes, but the default installed configuration overrides this and sets the timeout to 5 minutes to be consistent with earlier autofs releases.</p>
<dt><code>master_wait</code></p>
<dd>sets the default maximum time to wait for the master map to become available if it cannot be read at program start (program default 10, wait for 10 seconds then continue).</p>
<dt><code>negative_timeout</code></p>
<dd>Set the default timeout for caching failed key lookups (program default 60). If the equivalent command line option is given it will override this setting.</p>
<dt><code>mount_wait</code></p>
<dd>Set the default time to wait for a response from a spawned <a href="/docs/linux/man/8-mount/">mount</a>(8) before sending it a SIGTERM. Note that we still need to wait for the RPC layer to timeout before the sub-process exits so this isn&#8217;t ideal but it is the best we can do. The default is to wait until <a href="/docs/linux/man/8-mount/">mount</a>(8) returns without intervention.</p>
<dt><code>umount_wait</code></p>
<dd>Set the default time to wait for a response from a spawned <a href="/docs/linux/man/8-umount/">umount</a>(8) before sending it a SIGTERM. Note that we still need to wait for the RPC layer to timeout before the sub-process exits so this isn&#8217;t ideal but it is the best we can do.</p>
<dt><code>browse_mode</code></p>
<dd>Maps are browsable by default (program default &quot;yes&quot;).</p>
<dt><code>mount_nfs_default_protocol</code></p>
<dd>Specify the default protocol used by <code><a href="/docs/linux/man/8-mount-nfs/">mount.nfs</a></code>(8) (program default 3). Since we can&#8217;t identify this default automatically we need to set it in the autofs configuration.</p>
<dt><code>append_options</code></p>
<dd>Determine whether global options, given on the command line or per mount in the master map, are appended to map entry options or if the map entry options replace the global options (program default &quot;yes&quot;, append options).</p>
<dt><code>logging</code></p>
<dd>set default log level &quot;none&quot;, &quot;verbose&quot; or &quot;debug&quot; (program default &quot;none&quot;).</p>
<dt><code>force_standard_program_map_env</code></p>
<dd>override the use of a prefix with standard environment variables when a program map is executed. Since program maps are run as the privileded user setting these standard environment variables opens <a href="/docs/linux/man/8-automount/">automount</a>(8) to potential user privilege escalation when the program map is written in a language that can load components from, for example, a user home directory (program default &quot;no&quot;).</p>
<dt><code>map_hash_table_size</code></p>
<dd>This configuration option may be used to change the number of hash table slots (default 1024). </p>
<p> This configuration option affects the overhead of searching the map entry cache for map entries when there are a large number of entries. It affects the number of entries that must be looked at to locate a map entry in the map entry cache. For example, the default of 1024 and a direct map with 8000 entries would result in each slot containing an average of 8 entries, which should be acceptable. </p>
<p> However, if excessive CPU usage is observed during automount lookups increasing this option can reduce the CPU overhead considerably becuase it reduces the length of the search chains. </p>
<p> Note that the number of entries in a map doesn&#8217;t necessarily relate to the number of entries used in the map entry cache. </p>
<p> There are three distinct cases, direct maps and indirect maps that use the &quot;browse&quot; option must be read in their entirity at program start so, in these two cases the map size does retate directly to the map entry cache size. </p>
<p> For indirect maps that do not use the &quot;browse&quot; option entries are added to the map entry cache at lookup so the number of active cache entries, in this case, is usually much less than the number of entries in the map. In this last case it would be unusual for the map entry cache to grow large enough to warrant increasing the default before an event that cleans stale entries, a map re-read for example.</p>
<dt><code>use_hostname_for_mounts</code></p>
<dd>NFS mounts where the host name resolves to more than one IP address are probed for availability and to establish the order in which mounts to them should be tried. To ensure that mount attempts are made only to hosts that are responding and are tried in the order of hosts with the quickest response the IP address of the host needs to be used for the mount. </p>
<p> If it is necessary to use the hostname given in the map entry for the mount regardless, then set this option to &quot;yes&quot;. </p>
<p> Be aware that if this is done there is no defense against the host name resolving to one that isn&#8217;t responding and while the number of attempts at a successful mount will correspond to the number of addresses the host name resolves to the order will also not correspond to fastest responding hosts.</p>
<dt><code>disable_not_found_message</code></p>
<dd>The original request to add this log message needed it to be unconditional. That produces, IMHO, unnecessary noise in the log so a configuration option has been added to provide the ability to turn it off. The default is &quot;no&quot; to maintain the current behaviour.</p>
<dt><code>sss_master_map_wait</code></p>
<dd>Set the time to wait and retry if sssd returns &quot;no such entry&quot; when starting up. When sssd is starting up it can sometimes return &quot;no such entry&quot; for a short time until it has read in the LDAP map information. Default is 0 seconds, don&#8217;t wait.</p>
<dt><code>use_mount_request_log_id</code></p>
<dd>Set whether to use a mount request log id so that log entries for specific mount requests can be easily identified in logs that have multiple conncurrent requests. Default is don&#8217;t use mount request log ids.</dl>
<h3>LDAP Configuration</h3>
<p>Configuration settings available are:</p>
<dl>
<dt><code>ldap_timeout</code></p>
<dd>Set the network response timeout (default 8). Set timeout value for the synchronous API calls. The default is the LDAP library default of an infinite timeout.</p>
<dt><code>ldap_network_timeout</code></p>
<dd>Set the network response timeout (default 8).</p>
<dt><code>ldap_uri</code></p>
<dd>A space seperated list of server uris of the form &lt;proto&gt;://&lt;server&gt;[/] where &lt;proto&gt; can be ldap or ldaps. The option can be given multiple times. Map entries that include a server name override this option and it is then not used. Default is an empty list in which case either the server given in a map entry or the LDAP configured default is used. This uri list is read at startup and whenever the daemon receives a HUP signal. </p>
<p> This configuration option can also be used to request autofs lookup SRV RRs for a domain of the form &lt;proto&gt;:///[&lt;domain dn&gt;]. Note that a trailing &quot;/&quot; is not allowed when using this form. If the domain dn is not specified the dns domain name (if any) is used to construct the domain dn for the SRV RR lookup. The server list returned from an SRV RR lookup is refreshed according to the minimum ttl found in the SRV RR records or after one hour, whichever is less.</p>
<dt><code>search_base</code></p>
<dd>The base dn to use when searching for amap base dn. This entry may be given multiple times and each will be checked for a map base dn in the order they occur in the configuration. The search base list is read at startup and whenever the daemon recieves a HUP signal.</p>
<dt><code>map_object_class</code></p>
<dd>The map object class. In the <code>nisMap</code> schema this corresponds to the class <code>nisMap</code> and in the <code>automountMap</code> schema it corresponds to the class <code>automountMap</code>.</p>
<dt><code>entry_object_class</code></p>
<dd>The map entry object class. In the <code>nisMap</code> schema this corresponds to the class <code>nisObject</code> and in the <code>automountMap</code> schema it corresponds to the class <code>automount</code>.</p>
<dt><code>map_attribute</code></p>
<dd>The attribute used to identify the name of the map to which this entry belongs. In the <code>nisMap</code> schema this corresponds to the attribute <code>nisMapName</code> and in the <code>automountMap</code> schema it corresponds to the attribute <code>ou</code> or <code>automountMapName</code>.</p>
<dt><code>entry_attribute</code></p>
<dd>The attribute used to identify a map key. In the <code>nisMap</code> schema this corresponds to the attribute <code>cn</code> and in the <code>automountMap</code> schema it corresponds to the attribute <code>automountKey</code>.</p>
<dt><code>value_attribute</code></p>
<dd>The attribute used to identify the value of the map entry. In the <code>nisMap</code> schema this corresponds to the attribute <code>nisMapEntry</code> and in the <code>automountMap</code> schema it corresponds to the attribute <code>automountInformation</code>.</p>
<dt><code>NOTE:</code></p>
<dd>It is essential that entries use class and attribute in a consistent manner for correct operation of autofs. For example mixing <code>cn</code> and <code>automountKey</code> attributes in <code>automount</code> schema will not work as expected.</p>
<dt><code>auth_conf_file</code></p>
<dd>This configuration option may be used to specify an alternate location for the ldap authentication configuration file. See <code><a href="/docs/linux/man/5-autofs_ldap_auth-conf/">autofs_ldap_auth.conf</a></code>(5) for more information.</dl>
<h2>SECTION amd CONFIGURATION OPTIONS</h2>
<p>A number of the amd configuration options are not used by autofs, some because they are not relevant within autofs, some because they are done differently in autofs and others that are not yet implemented. </p>
<p> Since <code>mount_type</code> is always autofs (because there&#8217;s no user space NFS server) the configuration entries relating to that aren&#8217;t used. Also, server availability is done differently within autofs so the options that relate to the amd server monitoring sub-system are also not used. </p>
<p> These options are <code>mount_type</code>, <code>auto_attrcache</code>, <code>portmap_program</code>, <code>nfs_vers_ping</code>, <code>nfs_allow_any_interface</code>, <code>nfs_allow_insecure_port</code>, <code>nfs_proto</code>, <code>nfs_retransmit_counter</code>, <code>nfs_retransmit_counter_udp</code>, <code>nfs_retransmit_counter_tcp</code>, <code>nfs_retransmit_counter_toplvl</code>, <code>nfs_retry_interval</code>, <code>nfs_retry_interval_udp</code>, <code>nfs_retry_interval_tcp</code>, <code>nfs_retry_interval_toplvl</code> and <code>nfs_vers</code>. </p>
<p> Other options that are not used within the autofs implementation:</p>
<dl>
<dt><code>log_file</code>, <code>truncate_log</code></p>
<dd>sends its output to syslog so an alternate log file (or truncating the log) can&#8217;t be used.</p>
<dt><code>print_pid</code></p>
<dd>There&#8217;s no corresponding option for this within autofs.</p>
<dt><code>use_tcpwrappers</code>, <code>show_statfs_entries</code></p>
<dd>There&#8217;s no user space NFS server to control access to so this option isn&#8217;t relevant. The show_statfs_entries can&#8217;t be implemented for the same reason.</p>
<dt><code>debug_mtab_file</code></p>
<dd>There&#8217;s no user space NFS server and autofs avoids using file based mtab whenever possible.</p>
<dt><code>sun_map_syntax</code></p>
<dd>Sun map format is handled by autofs itself.</p>
<dt><code>plock</code>, <code>show_statfs_entries</code>, <code>preferred_amq_port</code></p>
<dd>Are not supported by autofs.</p>
<dt><code>ldap_cache_maxmem</code>, <code>ldap_cache_seconds</code></p>
<dd>External ldap caching is not used by autofs.</p>
<dt><code>ldap_proto_version</code></p>
<dd>autofs always attempts to use the highest available ldap protocol version.</p>
<dt><code>cache_duration</code>, <code>map_reload_interval</code>, <code>map_options</code></p>
<dd>The map<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>entry cache is continually updated and stale entries<br />
 cleaned on re-load, which is done when map changes are detected so these configuration entries are not used by autofs. An exception to this is the case where the map is large. In this case it may be necessary to read the whole map at startup even if browsing is is not enabled. Adding the cache:=all option to map_options can be used to for this.</p>
<dt><code>localhost_address</code></p>
<dd>This is not used within autofs. This configuration option was only used in the amd user space server code and is not relevant within autofs.</dl>
<p> Options that are handled differently within autofs:</p>
<dl>
<dt><code>pid_file</code></p>
<dd>To specify a pid file name a command line option must be used on startup.</p>
<dt><code>print_version</code></p>
<dd>Program version and feature information is obtained by using the automount command line option &quot;-V&quot;.</p>
<dt><code>debug_options , log_options</code></p>
<dd>autofs has somewhat more limited logging and debug logging options. When the log_options options is encountered it is converted to the nearest matching autofs logging option. Since the configuration option debug_options would be handled the same way it is ignored.</p>
<dt><code>restart_mounts</code></p>
<dd>This option has no sensible meaning within autofs because autofs always tries to re-connect to existing mounts. While this has its own set of problems not re-connecting to existing mounts always results in a non-functional automount tree if mounts were busy at the last shutdown (as is also the case with amd when using mount_type autofs).</p>
<dt><code>forced_unmounts</code></p>
<dd>Detaching mounts often causes serious problems for users of existing mounts. It is used by autofs in some cases, either at the explicit request of the user (with a command line or init option) and in some special cases during program operation but is avoided whenever possible.</dl>
<p> A number of configuration options are not yet implemented:</p>
<dl>
<dt><code>search_path</code></p>
<dd>Always a little frustrating, the compiled in map location should be used to locate maps but isn&#8217;t in some cases. This requires work within autofs itself and that will (obviously) include implementing this configuration option for the amd map parser as well.</p>
<dt><code>fully_qualified_hosts</code></p>
<dd>Not yet implemented.</p>
<dt><code>unmount_on_exit</code></p>
<dd>Since autofs always tries to re-connect to mounts left mounted from a previous shutdown this is a sensible option to implement and that will be done.</p>
<dt><code>browsable_dirs</code></p>
<dd>Allow map keys to be shown in directory listings. This option can have values of &quot;yes&quot; or &quot;no&quot;. The default is &quot;no&quot;. A variation of this option, &quot;browsable&quot;, can be used as a pseudo mount option in type &quot;auto&quot; map entries to provide provide browsing funtionality in sub-mounts. The amd &quot;browsable_dirs = full&quot; option cannot be implemented within the current autofs framework and is not supported.</p>
<dt><code>exec_map_timeout</code></p>
<dd>A timeout is not currently used for for program maps, might be implemented.</p>
<dt><code>tag</code></p>
<dd>The tag option is not implemented within autofs.</dl>
<p> Supported options:</p>
<dl>
<dt><code>arch</code>, <code>karch</code>, <code>os</code>, <code>osver</code></p>
<dd>These options default to what is returned from <a href="/docs/linux/man/2-uname/">uname</a>(2) and can be overridden if required.</p>
<dt><code>full_os</code></p>
<dd>This option has no default and must be set in the configuration if used in maps.</p>
<dt><code>cluster</code></p>
<dd>If not set defaults to the host domain name. This option corresponds to the HP_UX cluster name (according to the amd source) and is probably not used in Linux but is set anyway.</p>
<dt><code>vendor</code></p>
<dd>This option has a default value of &quot;unknown&quot;, it must be set in the configuration if used in maps.</p>
<dt><code>auto_dir</code></p>
<dd>Is the base name of the mount tree used for external mounts that are sometimes needed by amd maps. Its default value is &quot;/a&quot;.</p>
<dt><code>map_type</code></p>
<dd>Specifies the autofs map source, such as file, nis, ldap etc. and has no default value set.</p>
<dt><code>map_defaults</code></p>
<dd>This option is used to override /defaults entries within maps and can be used to provide different defaults on specific machines without having to modify centrally managed maps. It is empty by default.</p>
<dt><code>search_path</code></p>
<dd>Colon seperated paths to search for maps that are not specified as a full path.</p>
<dt><code>dismount_interval</code></p>
<dd>Is equivalent to the autofs timeout option. It is only possible to use this with type &quot;auto&quot; mounts due to the way the autofs kernel module performs expiry. It takes its default value from the autofs internal defaulti of 600 seconds.</p>
<dt><code>autofs_use_lofs</code></p>
<dd>If set to &quot;yes&quot; autofs will attempt to use bind mounts for type &quot;auto&quot; when possible.</p>
<dt><code>nis_domain</code></p>
<dd>Allows setting of a domain name other than the system default.</p>
<dt><code>local_domain</code></p>
<dd>Is used to override (or set) the host domain name.</p>
<dt><code>normalize_hostnames</code></p>
<dd>If set to &quot;yes&quot; then the contents of ${rhost} is translated in its official host name.</p>
<dt><code>domain_strip</code></p>
<dd>If set to &quot;yes&quot; the domain name part of the host is strippped when normalizing hostnames. This can be useful when using of the same maps in a multiple domain environment.</p>
<dt><code>normalize_slashes</code></p>
<dd>This option is set to &quot;yes&quot; by default and will collapse multiple unescaped occurrences of &quot;/&quot; to a single &quot;/&quot;.</p>
<dt><code>selectors_in_defaults</code>, <code>selectors_on_default</code></p>
<dd>This option has a default value of &quot;no&quot;. If set to &quot;yes&quot; then any defaults entry will be checked for selectors to determine the values to be used. selectors_in_defaults is the preferred option to use.</p>
<dt><code>ldap_base</code></p>
<dd>iThis option has no default value. It must be set to the base dn that is used for queries if ldap is to be used as a map source.</p>
<dt><code>ldap_hostports</code></p>
<dd>This option has no default value set. It must be set to the URI of the LDAP server to be used for lookups wheni ldap is used a map source. It may contain a comma or space seperated list of LDAP URIs.</p>
<dt><code>hesiod_base</code></p>
<dd>Sets the base name used for hesiod map sources.</p>
<dt><code>linux_ufs_mount_type</code></p>
<dd>This is an aditional configuration option for the autofs amd format parser implementation. </p>
<p> There&#8217;s no simple way to determine what the system default filesystem is and am-utils needs to be continually updated to do this and can easily get it wrong ayway. So allow it to be set in the configuration.</dl>
<h2>Example</h2>
<dl>
<dd>
<pre>[ autofs ]
timeout = 300
browse_mode = no
[ amd ]
dismount_interval = 300
map_type = nis
autofs_use_lofs = no
[ /expamle/mount ]
dismount_interval = 60
map_type = file</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-automount/">automount</a></code>(8), <code><a href="/docs/linux/man/5-auto-master/">auto.master</a></code>(5), <code><a href="/docs/linux/man/5-autofs_ldap_auth-conf/">autofs_ldap_auth.conf</a></code>(5)</p>
<h2>Author</h2>
<p>This manual page was written by Ian Kent &lt;raven [at] themaw.net&gt;.</p>
