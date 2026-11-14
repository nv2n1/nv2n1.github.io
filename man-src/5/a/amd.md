---
title: "amd(5)"
name: "amd"
section: "5"
letter: "a"
url: "/docs/linux/man/5-amd/"
description: "amd.conf – Amd configuration file"
---

<p>amd.conf &#8211; Amd configuration file</p>
<h2>Synopsis</h2>
<p><code>amd.conf</code></p>
<h2>Description</h2>
<p>The <code>amd.conf</code> file is the configuration file for Amd, as part of the am-utils suite. <code>amd.conf</code> contains runtime configuration information for the <code>Amd</code> automounter program.</p>
<h2>File Format</h2>
<p>The file consists of sections and parameters. A section begins with the name of the section in square brackets and continues until the next section begins or the end the file is reached. Sections contain parameters of the form &#8216;name = value&#8217;. The file is line-based &#8211; that is, each newline-terminated line represents either a comment, a section name or a parameter. No line-continuation syntax is available. Section, parameter names and their values are case sensitive. Only the first equals sign in a parameter is significant. Whitespace before or after the first equals sign is discarded. Leading, trailing and internal whitespace in section and parameter names is irrelevant. Leading and trailing whitespace in a parameter value is discarded. Internal whitespace within a parameter value is not allowed, unless the whole parameter value is quoted with double quotes as in &#8216;name = &quot;some value&quot;&#8217;. Any line beginning with a pound sign (#) is ignored, as are lines containing only whitespace. The values following the equals sign in parameters are all either a string (no quotes needed if string does not include spaces) or a boolean, which may be given as yes/no. Case is significant in all values. Some items such as cache timeouts are numeric.</p>
<h2>Sections</h2>
<h3>The [global] section</h3>
<p>Parameters in this section either apply to Amd as a whole, or to all other regular map sections which follow. There should be only one global section defined in one configuration file. It is highly recommended that this section be specified first in the configuration file. If it is not, then regular map sections which precede it will not use global values defined later.</p>
<h3>Regular [/map] sections</h3>
<p>Parameters in regular (non-global) sections apply to a single map entry. For example, if the map section <code>[/homes]</code> is defined, then all parameters following it will be applied to the <i>/homes</i> Amd-managed mount point.</p>
<h2>Parameters</h2>
<h3>Parameters common to all sections</h3>
<p>These parameters can be specified either in the global or a map specific section. Entries specified in a map-specific section override the default value or one defined in the global section. If such a common parameter is specified only in the global section, it is applicable to all regular map sections that follow.</p>
<dl>
<dt><code>browsable_dirs</code> (string, default=no)</p>
<dd>If &quot;yes,&quot; then Amd&#8217;s top-level mount points will be browsable to <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3) calls. This means you could run for example <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) and see what keys are available to mount in that directory. Not all entries are made visible to <a href="/docs/linux/man/3-readdir/">readdir</a>(3): the &quot;/default&quot; entry, wildcard entries, and those with a &quot;/&quot; in them are not included. If you specify &quot;full&quot; to this option, all but &quot;/default&quot; will be visible. Note that if you run a command which will attempt to <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) the entries, such as often done by &quot;ls -l&quot; or &quot;ls -F,&quot; Amd will attempt to mount <i>every</i> entry in that map. This is often called a &#8220;mount storm.&#8221; </p>
<dt><code>map_defaults</code> (string, default to empty)</p>
<dd>This option sets a string to be used as the map&#8217;s /defaults entry, overriding any /defaults specified in the map. This allows local users to override map defaults without modifying maps globally. </p>
<dt><code>map_options</code> (string, default no options)</p>
<dd>This option is the same as specifying map options on the command line to Amd, such as &quot;cache:=all&quot;. </p>
<dt><code>map_type</code> (string, default search all map types)</p>
<dd>If specified, Amd will initialize the map only for the type given. This is useful to avoid the default map search type used by Amd which takes longer and can have undesired side-effects such as initializing NIS even if not used. Possible values are </p>
<pre><code>exec</code> executable maps
<code>file</code> plain files
<code>hesiod</code> Hesiod name service from MIT
<code>ldap</code> Lightweight Directory Access Protocol
<code>ndbm</code> (New) dbm style hash files
<code>nis</code> Network Information Services (version 2)
<code>nisplus</code> Network Information Services Plus (version 3)
<code>passwd</code> local password files
<code>union</code> union maps</pre>
<dt><code>mount_type</code> (string, default=nfs)</p>
<dd>All Amd mount types default to NFS. That is, Amd is an NFS server on the map mount points, for the local host it is running on. If &quot;autofs&quot; is specified, Amd will be an autofs server for those mount points. </p>
<dt><code>autofs_use_lofs</code> (string, default=yes)</p>
<dd>When set to &quot;yes&quot; and using Autofs, Amd will use lofs-type (loopback) mounts for type:=link mounts. This has the advantage of mounting in place, and users get to the see the same pathname that they chdir&#8217;ed into. If this option is set to &quot;no,&quot; then Amd will use symlinks instead: that code is more tested, but negates autofs&#8217;s big advantage of in-place mounts. </p>
<dt><code>search_path</code> (string, default no search path)</p>
<dd>This provides a (colon-delimited) search path for file maps. Using a search path, sites can allow for local map customizations and overrides, and can distributed maps in several locations as needed. </p>
<dt><code>selectors_in_defaults</code> (boolean, default=no)</p>
<dd>If &quot;yes,&quot; then the /defaults entry of maps will search for and process any selectors before setting defaults for all other keys in that map. Useful when you want to set different options for a complete map based on some parameters. For example, you may want to better the NFS performance over slow slip-based networks as follows: </p>
<pre>/defaults \
 wire==slip-net;opts:=intr,rsize=1024,wsize=1024 \
 wire!=slip-net;opts:=intr,rsize=8192,wsize=8192</pre>
<p>Deprecated form: selectors_on_default </p>
</dl>
<h3>Parameters applicable to the global section only</h3>
<dl>
<dt><code>arch</code> (string, default to compiled in value)</p>
<dd>Same as the <code>-A</code> option to Amd. Allows you to override the value of the <i>arch</i> Amd variable. </p>
<dt><code>auto_attrcache</code> (numeric, default=0)</p>
<dd>Specify in seconds (or units of 0.1 seconds, depending on the OS), what is the (kernel-side) NFS attribute cache timeout for @i{Amd}&#8217;s own automount points. A value of 0 is supposed to turn off attribute caching, meaning that @i{Amd} will be consulted via a kernel-RPC each time someone stat()&#8217;s the mount point (which could be abused as a denial-of-service attack). Warning: some OSs are incapable of turning off the NFS attribute cache reliably. On such systems, Amd may not work reliably under heavy load. See the README.attrcache document in the Am-utils distribution for more details. </p>
<dt><code>auto_dir</code> (string, default=/a)</p>
<dd>Same as the <code>-a</code> option to Amd. This sets the private directory where Amd will create sub-directories for its real mount points. </p>
<dt><code>cache_duration</code> (numeric, default=300)</p>
<dd>Same as the <code>-c</code> option to Amd. Sets the duration in seconds that looked-up or mounted map entries remain in the cache. </p>
<dt><code>cluster</code> (string, default no cluster)</p>
<dd>Same as the <code>-C</code> option to Amd. Specifies the alternate HP-UX cluster to use. </p>
<dt><code>debug_mtab_file</code> (string, default=/tmp/mnttab)</p>
<dd>Path to mtab file that is used by Amd to store a list of mounted file systems during debug-mtab mode. This option only applies to systems that store mtab information on disk.</p>
<dd>
<dt><code>debug_options</code> (string, default no debug options)</p>
<dd>Same as the <code>-D</code> option to Amd. Specify any debugging options for Amd. Works only if am-utils was configured for debugging using the &#8211;enable-debug option. The &quot;mem&quot; option, as well as all other options, can be turned on via &#8211;enable-debug=mem. Otherwise debugging options are ignored. Options are comma delimited, and can be preceded by the string &quot;no&quot; to negate their meaning. You can get the list of supported debugging options by running Amd -H. Possible values are: </p>
<pre><code>all</code> all options
<code>amq</code> register for amq
<code>daemon</code> enter daemon mode
<code>fork</code> fork server
<code>full</code> program trace
<code>hrtime</code> print high resolution time stamps (only if <a href="//www.systutorials.com/docs/linux/man/3-syslog/">syslog</a>(3) is not used)
<code>info</code> info service specific debugging (hesiod, nis, etc.)
<code>mem</code> trace memory allocations
<code>mtab</code> use local &quot;./mtab&quot; file
<code>readdir</code> show browsable_dirs progress
<code>str</code> debug string munging
<code>test</code> full debug but no daemon
<code>trace</code> trace protocol and NFS mount arguments
<code>xdrtrace</code> trace XDR routines</pre>
<dt><code>dismount_interval</code> (numeric, default=120)</p>
<dd>Same as the <code>-w</code> option to Amd. Specify in seconds, the time between attempts to dismount file systems that have exceeded their cached times. </p>
<dt><code>domain_strip</code> (boolean, default=yes)</p>
<dd>If &quot;yes,&quot; then the domain name part referred to by ${rhost} is stripped off. This is useful to keep logs and smaller. If &quot;no,&quot; then the domain name part is left changed. This is useful when using multiple domains with the same maps (as you may have hosts whose domain-stripped name is identical). </p>
<dt><code>exec_map_timeout</code> (numeric, default=10)</p>
<dd>The timeout in seconds that <i>Amd</i> will wait for an executable map program before an answer is returned from that program (or script). This value should be set to as small as possible while still allowing normal replies to be returned before the timer expires, because during the time that the executable map program is queried, <i>Amd</i> is essentially waiting and is thus not responding to any other queries. </p>
<dt><code>forced_unmounts</code> (boolean, default=no)</p>
<dd>If set to &quot;yes,&quot; and the client OS supports forced or lazy unmounts, then <i>Amd</i> will attempt to use them if it gets any of three serious error conditions when trying to unmount an existing mount point or mount on top of one: EIO, ESTALE, or EBUSY. </p>
<p> This could be useful to recover from serious conditions such as hardware failure of mounted disks, or NFS servers which are down permanently, were migrated, or changed their IP address. Only &quot;type:=toplvl&quot; mounts hung with EBUSY are forcibly unmounted using this option, which is useful to recover from a hung <i>Amd</i>). </p>
<dt><code>full_os</code> (string, default to compiled in value)</p>
<dd>The full name of the operating system, along with its version. Allows you to override the compiled-in full name and version of the operating system. Useful when the compiled-in name is not desired. For example, the full operating system name on linux comes up as &#8220;linux&#8221;, but you can override it to &#8220;linux-2.2.5.&#8221; </p>
<dt><code>fully_qualified_hosts</code> (string, default=no)</p>
<dd>If &quot;yes,&quot; <i>Amd</i> will perform RPC authentication using fully-qualified host names. This is necessary for some systems, and especially when performing cross-domain mounting. For this function to work, the <i>Amd</i> variable ${hostd} is used, requiring that ${domain} not be null. </p>
<dt><code>hesiod_base</code> (string, default=automount)</p>
<dd>Specify the base name for hesiod maps. </p>
<dt><code>karch</code> (string, default to karch of the system)</p>
<dd>Same as the <code>-k</code> option to Amd. Allows you to override the kernel-architecture of your system. Useful for example on Sun (Sparc) machines, where you can build one Amd binary, and run it on multiple machines, yet you want each one to get the correct <i>karch</i> variable set (for example, sun4c, sun4m, sun4u, etc.) Note that if not specified, Amd will use <a href="/docs/linux/man/3-uname/">uname</a>(3) to figure out the kernel architecture of the machine. </p>
<dt><code>ldap_base</code> (string, default not set)</p>
<dd>Specify the base name for LDAP. This often includes LDAP-specific values such as country and organization. </p>
<dt><code>ldap_cache_maxmem</code> (numeric, default=131072)</p>
<dd>Specify the maximum memory Amd should use to cache LDAP entries. </p>
<dt><code>ldap_cache_seconds</code> (numeric, default=0)</p>
<dd>Specify the number of seconds to keep entries in the cache. </p>
<dt><code>ldap_hostports</code> (string, default not set)</p>
<dd>Specify the LDAP host and port values. </p>
<dt><code>ldap_proto_version</code> (numeric, default=2)</p>
<dd>Specify the version of the LDAP protocol to use. </p>
<dt><code>local_domain</code> (string, default no sub-domain)</p>
<dd>Same as the <code>-d</code> option to Amd. Specify the local domain name. If this option is not given the domain name is determined from the hostname, by removing the first component of the fully-qualified host name. </p>
<dt><code>localhost_address</code> (string, default to localhost or 127.0.0.1)</p>
<dd>Specify the name or IP address for Amd to use when connecting the sockets for the local NFS server and the RPC server. This defaults to 127.0.0.1 or whatever the host reports as its local address. This parameter is useful on hosts with multiple addresses where you want to force Amd to connect to a specific address. </p>
<dt><code>log_file</code> (string, default=/dev/stderr)</p>
<dd>Same as the <code>-l</code> option to Amd. Specify a file name to log Amd events to. If the string <code>/dev/stderr</code> is specified, Amd will send its events to the standard error file descriptor. If the string <code>syslog</code> is given, Amd will record its events with the system logger <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8). The default syslog facility used is LOG_DAEMON. If you wish to change it, append its name to the log file name, delimited by a single colon. For example, if <i>logfile</i> is the string <code>syslog:local7</code> then Amd will log messages via <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3) using the LOG_LOCAL7 facility (if it exists on the system). </p>
<dt><code>log_options</code> (string, default no logging options)</p>
<dd>Same as the <code>-x</code> option to Amd. Specify any logging options for Amd. Options are comma delimited, and can be preceded by the string &quot;no&quot; to negate their meaning. The &quot;debug&quot; logging option is only available if am-utils was configured with &#8211;enable-debug. You can get the list of supported debugging and logging options by running <code>amd</code> <code>-H</code>. Possible values are: </p>
<pre><code>all</code> all messages
<code>debug</code> debug messages
<code>error</code> non-fatal system errors
<code>fatal</code> fatal errors
<code>info</code> information
<code>map</code> map errors
<code>stats</code> additional statistical information
<code>user</code> non-fatal user errors
<code>warn</code> warnings
<code>warning</code> warnings</pre>
<dt><code>map_reload_interval</code> (numeric, default=3600)</p>
<dd>The number of seconds that Amd will wait before it checks to see if any maps have changed at their source (NIS servers, LDAP servers, files, etc.). Amd will reload only those maps that have changed. </p>
<dt><code>nfs_allow_any_interface</code> (string, default=no)</p>
<dd>Normally Amd accepts local NFS packets only from 127.0.0.1. If this parameter is set to &quot;yes&quot; then Amd will accept local NFS packets from any local interface; this is useful on hosts that may have multiple interfaces where the system is forced to send all outgoing packets (even those bound to the same host) via an address other than 127.0.0.1. </p>
<dt><code>nfs_allow_insecure_port</code> (string, default=no)</p>
<dd>Normally Amd will refuse requests coming from unprivileged ports (i.e. ports &gt;= 1024 on Unix systems), so that only privileged users and the kernel can send NFS requests to it. However, some kernels (certain versions of Darwin, MacOS X, and Linux) have bugs that cause them to use unprivileged ports in certain situations, which causes Amd to stop dead in its tracks. This parameter allows Amd to operate normally even on such systems, at the expense of a slight decrease in the security of its operations. If you see messages like &quot;ignoring request from foo:1234, port not reserved&quot; in your Amd log, try enabling this parameter and give it another go. </p>
<dt><code>nfs_proto</code> (string, default to trying version tcp then udp)</p>
<dd>By default, Amd tries TCP and then UDP. This option forces the overall NFS protocol used to TCP or UDP. It overrides what is in the Amd maps, and is useful when Amd is compiled with NFSv3 support that may not be stable. With this option you can turn off the complete usage of NFSv3 dynamically (without having to recompile Amd) until such time as NFSv3 support is desired again. </p>
<dt><code>nfs_retransmit_counter</code> (numeric, default=11)</p>
<dd>Same as the <i>retransmit</i> part of the <code>-t</code><i> timeout.retransmit</i> option to Amd. Specifies the number of NFS retransmissions that the kernel will use to communicate with Amd. </p>
<dt><code>nfs_retransmit_counter_udp</code> (numeric, default=11)</p>
<dd>Same as the <code>nfs_retransmit_counter</code> option, but for all UDP mounts only. </p>
<dt><code>nfs_retransmit_counter_tcp</code> (numeric, default=11)</p>
<dd>Same as the <code>nfs_retransmit_counter</code> option, but for all TCP mounts only. </p>
<dt><code>nfs_retransmit_counter_toplvl</code> (numeric, default=11)</p>
<dd>Same as the <code>nfs_retransmit_counter</code> option, but only for Amd&#8217;s top-level UDP mounts. </p>
<dt><code>nfs_retry_interval</code> (numeric, default=8)</p>
<dd>Same as the <i>timeout</i> part of the <code>-t</code><i> timeout.retransmit</i> option to Amd. Specifies the NFS timeout interval, in <i>tenths</i> of seconds, between NFS/RPC retries (for UDP and TCP). This is the value that the kernel will use to communicate with Amd. </p>
<p> Amd relies on the kernel RPC retransmit mechanism to trigger mount retries. The values of the <code>nfs_retransmit_counter</code> and the <code>nfs_retry_interval</code> parameters change the overall retry interval. Too long an interval gives poor interactive response; too short an interval causes excessive retries. </p>
<dt><code>nfs_retry_interval_udp</code> (numeric, default=8)</p>
<dd>Same as the <code>nfs_retry_interval</code> option, but for all UDP mounts only. </p>
<dt><code>nfs_retry_interval_tcp</code> (numeric, default=8)</p>
<dd>Same as the <code>nfs_retry_interval</code> option, but for all TCP mounts only. </p>
<dt><code>nfs_retry_interval_toplvl</code> (numeric, default=8)</p>
<dd>Same as the <code>nfs_retry_interval</code> option, but only for Amd&#8217;s top-level UDP mounts. </p>
<dt><code>nfs_vers</code> (numeric, default to trying version 3 then 2)</p>
<dd>By default, Amd tries version 3 and then version 2. This option forces the overall NFS protocol used to version 3 or 2. It overrides what is in the Amd maps, and is useful when Amd is compiled with NFSv3 support that may not be stable. With this option you can turn off the complete usage of NFSv3 dynamically (without having to recompile Amd) until such time as NFSv3 support is desired again. </p>
<dt><code>nis_domain</code> (string, default to local NIS domain name)</p>
<dd>Same as the <code>-y</code> option to Amd. Specify an alternative NIS domain from which to fetch the NIS maps. The default is the system domain name. This option is ignored if NIS support is not available. </p>
<dt><code>normalize_hostnames</code> (boolean, default=no)</p>
<dd>Same as the <code>-n</code> option to Amd. If &quot;yes,&quot; then the name refereed to by ${rhost} is normalized relative to the host database before being used. The effect is to translate aliases into &#8220;official&#8221; names. </p>
<dt><code>normalize_slashes</code> (boolean, default=yes)</p>
<dd>If &quot;yes,&quot; then Amd will condense all multiple &#8220;/&#8221; (slash) characters into one and remove all trailing slashes. If &quot;no,&quot; then Amd will not touch strings that may contain repeated or trailing slashes. The latter is sometimes useful with SMB mounts, which often require multiple slash characters in pathnames. </p>
<dt><code>os</code> (string, default to compiled in value)</p>
<dd>Same as the <code>-O</code> option to Amd. Allows you to override the compiled-in name of the operating system. Useful when the built-in name is not desired for backward compatibility reasons. For example, if the build in name is &#8220;sunos5&#8221;, you can override it to &#8220;sos5&#8221;, and use older maps which were written with the latter in mind. </p>
<dt><code>osver</code> (string, default to compiled in value)</p>
<dd>Same as the <code>-o</code> option to Amd. Overrides the compiled-in version number of the operating system. Useful when the built in version is not desired for backward compatibility reasons. For example, if the build in version is &#8220;2.5.1&#8221;, you can override it to &#8220;5.5.1&#8221;, and use older maps that were written with the latter in mind. </p>
<dt><code>pid_file</code> (string, default=/dev/stdout)</p>
<dd>Specify a file to store the process ID of the running daemon into. If not specified, Amd will print its process id onto the standard output. Useful for killing Amd after it had run. Note that the PID of a running Amd can also be retrieved via <code>amq</code> <code>-p</code>. This file is used only if the print_pid option is on. </p>
<dt><code>plock</code> (boolean, default=yes)</p>
<dd>Same as the <code>-S</code> option to Amd. If &quot;yes,&quot; lock the running executable pages of Amd into memory. To improve Amd&#8217;s performance, systems that support the <code><a href="/docs/linux/man/3-plock/">plock</a></code>(3) or <code><a href="/docs/linux/man/2-mlockall/">mlockall</a></code>(2) call can lock the Amd process into memory. This way there is less chance it the operating system will schedule, page out, and swap the Amd process as needed. This improves Amd&#8217;s performance, at the cost of reserving the memory used by the Amd process (making it unavailable for other processes). </p>
<dt><code>portmap_program</code> (numeric, default=300019)</p>
<dd>Specify an alternate Port-mapper RPC program number, other than the official number. This is useful when running multiple Amd processes. For example, you can run another Amd in &quot;test&quot; mode, without affecting the primary Amd process in any way. For safety reasons, the alternate program numbers that can be specified must be in the range 300019-300029, inclusive. Amq has an option <code>-P</code> which can be used to specify an alternate program number of an Amd to contact. In this way, amq can fully control any number of Amd processes running on the same host. </p>
<dt><code>preferred_amq_port</code> (numeric, default=0)</p>
<dd>Specify an alternate Port-mapper RPC port number for Amd&#8217;s Amq service. This is used for both UDP and TCP. Setting this value to 0 (or not defining it) will cause Amd to select an arbitrary port number. Setting the Amq RPC service port to a specific number is useful in firewalled or NAT&#8217;ed environments, where you need to know which port Amd will listen on. </p>
<dt><code>print_pid</code> (boolean, default=no)</p>
<dd>Same as the <code>-p</code> option to Amd. If &quot;yes,&quot; Amd will print its process ID upon starting. </p>
<dt><code>print_version</code> (boolean, default=no)</p>
<dd>Same as the <code>-v</code> option to Amd, but the version prints and Amd continues to run. If &quot;yes,&quot; Amd will print its version information string, which includes some configuration and compilation values. </p>
<dt><code>restart_mounts</code> (boolean, default=no)</p>
<dd>Same as the <code>-r</code> option to Amd. If &quot;yes&quot; Amd will scan the mount table to determine which file systems are currently mounted. Whenever one of these would have been auto-mounted, Amd inherits it. </p>
<dt><code>show_statfs_entries</code> (boolean), default=no)</p>
<dd>If &quot;yes,&quot; then all maps which are browsable will also show the number of entries (keys) they have when &quot;df&quot; runs. (This is accomplished by returning non-zero values to the <a href="/docs/linux/man/2-statfs/">statfs</a>(2) system call). </p>
<dt><code>truncate_log</code> (boolean), default=no)</p>
<dd>If &quot;yes,&quot; then the log file (if it is a regular file), will be truncated upon startup. </p>
<dt><code>unmount_on_exit</code> (boolean), default=no)</p>
<dd>If &quot;yes,&quot; then Amd will attempt to unmount all file systems which it knows about. Normally Amd leaves all (esp. NFS) mounted file systems intact. Note that Amd does not know about file systems mounted before it starts up, unless the restart_mounts option or <code>-r</code> flag are used. </p>
<dt><code>use_tcpwrappers</code> (boolean), default=yes)</p>
<dd>If &quot;yes,&quot; then Amd will use the tcpd/librwap tcpwrappers library (if available) to control access to Amd via the /etc/hosts.allow and /etc/hosts.deny files. </p>
<dt><code>vendor</code> (string, default to compiled in value)</p>
<dd>The name of the vendor of the operating system. Overrides the compiled-in vendor name. Useful when the compiled-in name is not desired. For example, most Intel based systems set the vendor name to &#8220;unknown&#8221;, but you can set it to &#8220;redhat.&#8221; </p>
</dl>
<h3>Parameters applicable to regular map sections</h3>
<dl>
<dt><code>map_name</code> (string, must be specified)</p>
<dd>Name of the map where the keys are located. </p>
<dt><code>tag</code> (string, default no tag)</p>
<dd>Each map entry in the configuration file can be tagged. If no tag is specified, that map section will always be processed by Amd. If it is specified, then Amd will process the map if the <code>-T</code> option was given to Amd, and the value given to that command-line option matches that in the map section. </p>
</dl>
<h2>Examples</h2>
<p>Here is a real Amd configuration file I use daily. </p>
<pre># GLOBAL OPTIONS SECTION
[ global ]
normalize_hostnames = no
print_pid = no
restart_mounts = yes
auto_dir = /n
log_file = /var/log/amd
log_options = all
#debug_options = all
plock = no
selectors_in_defaults = yes
# config.guess picks up &quot;sunos5&quot; and I don't want to edit my maps yet
os = sos5
# if you print_version after setting up &quot;os,&quot; it will show it.
print_version = no
map_type = file
search_path = /etc/amdmaps:/usr/lib/amd:/usr/local/AMD/lib
browsable_dirs = yes
# DEFINE AN AMD MOUNT POINT
[ /u ]
map_name = amd.u
[ /proj ]
map_name = amd.proj
[ /src ]
map_name = amd.src
[ /misc ]
map_name = amd.misc
[ /import ]
map_name = amd.import
[ /tftpboot/.amd ]
tag = tftpboot
map_name = amd.tftpboot</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amd/">amd</a></code>(8), <code><a href="/docs/linux/man/8-amq/">amq</a></code>(8), <code><a href="/docs/linux/man/8-ctl-amd/">ctl-amd</a></code>(8), <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5). </p>
<p> &#8220;am-utils&#8221; <code><a href="/docs/linux/man/1-info/">info</a></code>(1) entry. </p>
<p> <i>Linux NFS and Automounter Administration</i> by Erez Zadok, ISBN 0-7821-2739-8, (Sybex, 2001). </p>
<p> <i><a rel="nofollow" href="http://www.am-utils.org">http://www.am-utils.org</a></i> </p>
<p> <i>Amd &#8211; The 4.4 BSD Automounter</i></p>
<h2>Authors</h2>
<p>Erez Zadok &lt;ezk [at] cs.sunysb.edu&gt;, Computer Science Department, Stony Brook University, Stony Brook, New York, USA. Other authors and contributors to am-utils are listed in the <code>AUTHORS</code> file distributed with am-utils.</p>
