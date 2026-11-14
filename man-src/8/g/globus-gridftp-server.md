---
title: "globus-gridftp-server(8)"
name: "globus-gridftp-server"
section: "8"
letter: "g"
url: "/docs/linux/man/8-globus-gridftp-server/"
description: "globus-gridftp-server – The Globus GridFTP server daemon"
---

<p>globus-gridftp-server &#8211; The Globus GridFTP server daemon</p>
<h2>Synopsis</h2>
<p>globus-gridftp-server OPTIONS</p>
<h2>Description</h2>
<p>The <code>globus-gridftp-server</code> program is a ftp server with support for GridFTP protocol extensions, including strong authentication, parallel data transfers, and parallel data layouts.</p>
<h2>Options</h2>
<p>The list below contains the command-line options for the server, and also the name of the configuration file entry that implements that option. Note that any boolean option can be negated on the command line by preceding the specified option with <i>-no-</i> or <i>-n</i>. example: -no-cas or -nf.</p>
<h3>Informational Options</h3>
<p><code>-h,-help</code></p>
<dl>
<dd>Show usage information and exit. </p>
<p> This option can also be set in the configuration file as help. The default value of this option is FALSE.</dl>
<p> <code>-hh,-longhelp</code></p>
<dl>
<dd>Show more usage information and exit. </p>
<p> This option can also be set in the configuration file as longhelp. The default value of this option is FALSE.</dl>
<p> <code>-v,-version</code></p>
<dl>
<dd>Show version information for the server and exit. </p>
<p> This option can also be set in the configuration file as version. The default value of this option is FALSE.</dl>
<p> <code>-V,-versions</code></p>
<dl>
<dd>Show version information for all loaded globus libraries and exit. </p>
<p> This option can also be set in the configuration file as versions. The default value of this option is FALSE.</dl>
<h3>Modes of Operation</h3>
<p><code>-i,-inetd</code></p>
<dl>
<dd>Run under an inetd service. </p>
<p> This option can also be set in the configuration file as inetd. The default value of this option is FALSE.</dl>
<p> <code>-s,-daemon</code></p>
<dl>
<dd>Run as a daemon. All connections will fork off a new process and setuid if allowed. </p>
<p> This option can also be set in the configuration file as daemon. The default value of this option is TRUE.</dl>
<p> <code>-S,-detach</code></p>
<dl>
<dd>Run as a background daemon detached from any controlling terminals. </p>
<p> This option can also be set in the configuration file as detach. The default value of this option is FALSE.</dl>
<p> <code>-ssh</code></p>
<dl>
<dd>Run over a connected ssh session. </p>
<p> This option can also be set in the configuration file as ssh. The default value of this option is FALSE.</dl>
<p> <code>-exec string</code></p>
<dl>
<dd>For statically compiled or non-GLOBUS_LOCATION standard binary locations, specify the full path of the server binary here. Only needed when run in daemon mode. </p>
<p> This option can also be set in the configuration file as exec.</dl>
<p> <code>-chdir</code></p>
<dl>
<dd>Change directory when the server starts. This will change directory to the dir specified by the chdir_to option. </p>
<p> This option can also be set in the configuration file as chdir. The default value of this option is TRUE.</dl>
<p> <code>-chdir-to string</code></p>
<dl>
<dd>Directory to chdir to after starting. Will use / if not set. Note that this is the directory of the process, not the client&#8217;s home directory. </p>
<p> This option can also be set in the configuration file as chdir_to.</dl>
<p> <code>-threads number</code></p>
<dl>
<dd>Enable threaded operation and set the number of threads. The default is 0, which is non-threaded. When threading is required, a thread count of 1 or 2 should be sufficient. </p>
<p> This option can also be set in the configuration file as threads.</dl>
<p> <code>-f,-fork</code></p>
<dl>
<dd>Server will fork for each new connection. Disabling this option is only recommended when debugging. Note that non-forked servers running as <i>root</i> will only accept a single connection, and then exit. </p>
<p> This option can also be set in the configuration file as fork. The default value of this option is TRUE.</dl>
<p> <code>-1,-single</code></p>
<dl>
<dd>Exit after a single connection. </p>
<p> This option can also be set in the configuration file as single. The default value of this option is FALSE.</dl>
<p> <code>-chroot-path string</code></p>
<dl>
<dd>Path to become the new root after authentication. This path must contain a valid certificate structure, /etc/passwd, and /etc/group. The command globus-gridftp-server-setup-chroot can help create a suitable directory structure. </p>
<p> This option can also be set in the configuration file as chroot_path.</dl>
<h3>Authentication, Authorization, and Security Options</h3>
<p><code>-auth-level number</code></p>
<dl>
<dd>Add levels together to use more than one. </p>
<dl>
<dd>
<pre> 0 = Disables all authorization checks.
 1 = Authorize identity.
 2 = Authorize all file/resource accesses.
 4 = Disable changing process uid to authenticated user (no setuid) -- DO NOT use this when process is started as root.
If not set uses level 2 for front ends and level 1 for data nodes. Note that levels 2 and 4 imply level 1 as well.</pre>
</dl>
<p> This option can also be set in the configuration file as auth_level.</dl>
<p> <code>-ipc-allow-from string</code></p>
<dl>
<dd>Only allow connections from these source ip addresses. Specify a comma separated list of ip address fragments. A match is any ip address that starts with the specified fragment. Example: <i>192.168.1.</i> will match and allow a connection from 192.168.1.45. Note that if this option is used any address not specifically allowed will be denied. </p>
<p> This option can also be set in the configuration file as ipc_allow_from.</dl>
<p> <code>-ipc-deny-from string</code></p>
<dl>
<dd>Deny connections from these source ip addresses. Specify a comma separated list of ip address fragments. A match is any ip address that starts with the specified fragment. Example: <i>192.168.2.</i> will match and deny a connection from 192.168.2.45. </p>
<p> This option can also be set in the configuration file as ipc_deny_from.</dl>
<p> <code>-allow-from string</code></p>
<dl>
<dd>Only allow connections from these source ip addresses. Specify a comma separated list of ip address fragments. A match is any ip address that starts with the specified fragment. Example: <i>192.168.1.</i> will match and allow a connection from 192.168.1.45. Note that if this option is used any address not specifically allowed will be denied. </p>
<p> This option can also be set in the configuration file as allow_from.</dl>
<p> <code>-deny-from string</code></p>
<dl>
<dd>Deny connections from these source ip addresses. Specify a comma separated list of ip address fragments. A match is any ip address that starts with the specified fragment. Example: <i>192.168.2.</i> will match and deny a connection from 192.168.2.45. </p>
<p> This option can also be set in the configuration file as deny_from.</dl>
<p> <code>-encrypt-data</code></p>
<dl>
<dd>Require encrypted data channels. This will cause an error and prevent all transfers in which the client does not request an authenticated and encrypted data channel. </p>
<p> This option can also be set in the configuration file as encrypt_data. The default value of this option is FALSE.</dl>
<p> <code>-si,-secure-ipc</code></p>
<dl>
<dd>Use GSI security on ipc channel. </p>
<p> This option can also be set in the configuration file as secure_ipc. The default value of this option is TRUE.</dl>
<p> <code>-ia string,-ipc-auth-mode string</code></p>
<dl>
<dd>Set GSI authorization mode for the ipc connection. Options are: none, host, self or subject:[subject]. </p>
<p> This option can also be set in the configuration file as ipc_auth_mode. The default value of this option is host.</dl>
<p> <code>-aa,-allow-anonymous</code></p>
<dl>
<dd>Allow clear text anonymous access. If server is running as root anonymous_user must also be set. Disables ipc security. </p>
<p> This option can also be set in the configuration file as allow_anonymous. The default value of this option is FALSE.</dl>
<p> <code>-anonymous-names-allowed string</code></p>
<dl>
<dd>Comma separated list of names to treat as anonymous users when allowing anonymous access. If not set, the default names of <i>anonymous</i> and <i>ftp</i> will be allowed. Use <i>*</i> to allow any username. </p>
<p> This option can also be set in the configuration file as anonymous_names_allowed.</dl>
<p> <code>-anonymous-user string</code></p>
<dl>
<dd>User to setuid to for an anonymous connection. Only applies when running as root. </p>
<p> This option can also be set in the configuration file as anonymous_user.</dl>
<p> <code>-anonymous-group string</code></p>
<dl>
<dd>Group to setgid to for an anonymous connection. If unset, the default group of anonymous_user will be used. </p>
<p> This option can also be set in the configuration file as anonymous_group.</dl>
<p> <code>-sharing-dn string</code></p>
<dl>
<dd>Allow sharing when using the supplied DN. A client connected with these credentials will be able to access any user for which sharing is enabled. </p>
<p> This option can also be set in the configuration file as sharing_dn.</dl>
<p> <code>-sharing-state-dir string</code></p>
<dl>
<dd>Full path to a directory that will contain files used by GridFTP to control sharing access for individual local accounts. The special variables <i>$HOME</i> and <i>$USER</i> can be used to create a dynamic path that is unique to each local account. This pathmust be writable by the associated account. The default path is <i>$HOME/.globus/sharing/</i>. This must refer to a path on the filesystem, not a path that is only accessible via a DSI plugin. </p>
<p> This option can also be set in the configuration file as sharing_state_dir.</dl>
<p> <code>-sharing-control</code></p>
<dl>
<dd>Allow a local user account to control its own sharing access via special GridFTP client commands. The user account must have filesystem write access to the sharing state dir. </p>
<p> This option can also be set in the configuration file as sharing_control. The default value of this option is TRUE.</dl>
<p> <code>-sharing-rp string</code></p>
<dl>
<dd>Sharing specific path restrictions. This completely replaces the normal path restrictions (-rp) when an account is being shared by a sharing-dn login.Follows normal path restriction semantics. </p>
<p> This option can also be set in the configuration file as sharing_rp.</dl>
<p> <code>-sharing-users-allow string</code></p>
<dl>
<dd>Comma separated list of usernames that are allowed to share unless matched in the user deny lists. If this list is set, users that are not included will be denied unless matched in the group allow list. </p>
<p> This option can also be set in the configuration file as sharing_users_allow.</dl>
<p> <code>-sharing-users-deny string</code></p>
<dl>
<dd>Comma separated list of usernames that are denied sharing even if matched in the user or group allow lists. </p>
<p> This option can also be set in the configuration file as sharing_users_deny.</dl>
<p> <code>-sharing-groups-allow string</code></p>
<dl>
<dd>Comma separated list of groups whose members are allowed to share unless matched in the user or group deny lists. If this list is set, groups that are not included will be denied unless matched in the user allow list. </p>
<p> This option can also be set in the configuration file as sharing_groups_allow.</dl>
<p> <code>-sharing-groups-deny string</code></p>
<dl>
<dd>Comma separated list of groups whose members will be denied sharing unless matched in the user allow list. </p>
<p> This option can also be set in the configuration file as sharing_groups_deny.</dl>
<p> <code>-allow-root</code></p>
<dl>
<dd>Allow clients to be mapped to the root account. </p>
<p> This option can also be set in the configuration file as allow_root. The default value of this option is FALSE.</dl>
<p> <code>-allow-disabled-login</code></p>
<dl>
<dd>Do not check if a user&#8217;s system account is disabled before allowing login. </p>
<p> This option can also be set in the configuration file as allow_disabled_login. The default value of this option is FALSE.</dl>
<p> <code>-password-file string</code></p>
<dl>
<dd>Enable clear text access and authenticate users against this /etc/passwd formatted file. </p>
<p> This option can also be set in the configuration file as pw_file.</dl>
<p> <code>-connections-max number</code></p>
<dl>
<dd>Maximum concurrent connections allowed. Only applies when running in daemon mode. Unlimited if not set. </p>
<p> This option can also be set in the configuration file as connections_max.</dl>
<p> <code>-connections-disabled</code></p>
<dl>
<dd>Disable all new connections. For daemon mode, issue a SIGHUP to the server process after changing the config file in order to not affect ongoing connections. </p>
<p> This option can also be set in the configuration file as connections_disabled. The default value of this option is FALSE.</dl>
<p> <code>-offline-msg string</code></p>
<dl>
<dd>Custom message to be displayed to clients when the server is offline via the connections_disabled or connections_max = 0 options. </p>
<p> This option can also be set in the configuration file as offline_msg.</dl>
<p> <code>-disable-command-list string</code></p>
<dl>
<dd>A comma separated list of client commands that will be disabled. </p>
<p> This option can also be set in the configuration file as disable_command_list.</dl>
<p> <code>-authz-callouts,-cas</code></p>
<dl>
<dd>Enable the GSI authorization callout framework, for callouts such as CAS. </p>
<p> This option can also be set in the configuration file as cas. The default value of this option is TRUE.</dl>
<p> <code>-use-home-dirs</code></p>
<dl>
<dd>Set the starting directory to the authenticated users home dir. Disabling this is the same as setting <i>-home-dir /</i>. </p>
<p> This option can also be set in the configuration file as use_home_dirs. The default value of this option is TRUE.</dl>
<p> <code>-home-dir string</code></p>
<dl>
<dd>Set a path to override the system defined home/starting directory for authenticated users. The special variable strings <i>$USER</i> and <i>$HOME</i> may be used. The authenticated username will be substituted for $USER, and the user&#8217;s real home dir will be substituted for $HOME. Be sure to escape the $ character if using these on the command line. </p>
<p> This option can also be set in the configuration file as home_dir.</dl>
<p> <code>-rp string,-restrict-paths string</code></p>
<dl>
<dd>A comma separated list of full paths that clients may access. Each path may be prefixed by R and/or W, denoting read or write access, otherwise full access is granted. If a given path is a directory, all contents and subdirectories will be given the same access. Order of paths does not matter &#8212; the permissions on the longest matching path will apply. The special character <i>~</i> will be replaced by the authenticated user&#8217;s home directory, or the <i>-home-dir</i> option, if used. Note that if the home directory is not accessible, <i>\~</i> will be set to <i>/</i>. By default all paths are allowed, and access control is handled by the OS. In a striped or split process configuration, this should be set on both the frontend and data nodes. </p>
<p> This option can also be set in the configuration file as restrict_paths.</dl>
<p> <code>-rp-follow-symlinks</code></p>
<dl>
<dd>Do not verify that a symlink points to an allowed path before following. By default, symlinks are followed only when they point to an allowed path. By enabling this option, symlinks will be followed even if they point to a path that is otherwise restricted. </p>
<p> This option can also be set in the configuration file as rp_follow_symlinks. The default value of this option is FALSE.</dl>
<p> <code>-em string,-acl string</code></p>
<dl>
<dd>A comma separated list of ACL or event modules to load. </p>
<p> This option can also be set in the configuration file as acl.</dl>
<h3>Logging Options</h3>
<p><code>-d string,-log-level string</code></p>
<dl>
<dd>Log level. A comma separated list of levels from: <i>ERROR, WARN, INFO, TRANSFER, DUMP, ALL</i>. TRANSFER includes the same statistics that are sent to the separate transfer log when -log-transfer is used. Example: error,warn,info. You may also specify a numeric level of 1-255. The default level is ERROR. </p>
<p> This option can also be set in the configuration file as log_level. The default value of this option is ERROR.</dl>
<p> <code>-log-module string</code></p>
<dl>
<dd>globus_logging module that will be loaded. If not set, the default <i>stdio</i> module will be used, and the logfile options apply. Built in modules are <i>stdio</i> and <i>syslog</i>. Log module options may be set by specifying module:opt1=val1:opt2=val2. Available options for the built in modules are <i>interval</i> and <i>buffer</i>, for buffer flush interval and buffer size, respectively. The default options are a 64k buffer size and a 5 second flush interval. A 0 second flush interval will disable periodic flushing, and the buffer will only flush when it is full. A value of 0 for buffer will disable buffering and all messages will be written immediately. Example: -log-module stdio:buffer=4096:interval=10 </p>
<p> This option can also be set in the configuration file as log_module.</dl>
<p> <code>-l string,-logfile string</code></p>
<dl>
<dd>Path of a single file to log all activity to. If neither this option or log_unique is set, logs will be written to stderr unless the execution mode is detached or inetd, in which case logging will be disabled. </p>
<p> This option can also be set in the configuration file as log_single.</dl>
<p> <code>-L string,-logdir string</code></p>
<dl>
<dd>Partial path to which <i>gridftp.(pid).log</i> will be appended to construct the log filename. Example: -L /var/log/gridftp/ will create a separate log ( /var/log/gridftp/grid<a href="ftp://ftp.xxxx.log">ftp.xxxx.log</a> ) for each process (which is normally each new client session). If neither this option or log_single is set, logs will be written to stderr unless the execution mode is detached or inetd, in which case logging will be disabled. </p>
<p> This option can also be set in the configuration file as log_unique.</dl>
<p> <code>-Z string,-log-transfer string</code></p>
<dl>
<dd>Log netlogger style info for each transfer into this file. You may also use the log-level of TRANSFER to include this info in the standard log. </p>
<p> This option can also be set in the configuration file as log_transfer.</dl>
<p> <code>-log-filemode string</code></p>
<dl>
<dd>File access permissions of log files. Should be an octal number such as 0644. </p>
<p> This option can also be set in the configuration file as log_filemode.</dl>
<p> <code>-disable-usage-stats</code></p>
<dl>
<dd>Disable transmission of per-transfer usage statistics. See the Usage Statistics section in the online documentation for more information. </p>
<p> This option can also be set in the configuration file as disable_usage_stats. The default value of this option is FALSE.</dl>
<p> <code>-usage-stats-target string</code></p>
<dl>
<dd>Comma separated list of contact strings (host:port) for usage statistics receivers. The usage stats sent to a particular receiver may be customized by configuring it with a taglist (host:port!taglist) The taglist is a list of characters that each correspond to a usage stats tag. When this option is unset, stats are reported to usage-stats.globus.org:4810. If you set your own receiver, and wish to continue reporting to the Globus receiver, you will need to add it manually. The list of available tags follow. Tags marked * are reported by default. </p>
<dl>
<dd>
<pre>*(e) START - start time of transfer
*(E) END - end time of transfer
*(v) VER - version string of GridFTP server
*(b) BUFFER - tcp buffer size used for transfer
*(B) BLOCK - disk blocksize used for transfer
*(N) NBYTES - number of bytes transferred
*(s) STREAMS - number of parallel streams used
*(S) STRIPES - number of stripes used
*(t) TYPE - transfer command: RETR, STOR, LIST, etc
*(c) CODE - ftp result code (226 = success, 5xx = fail)
*(D) DSI - DSI module in use
*(A) EM - event modules in use
*(T) SCHEME - ftp, gsiftp, sshftp, etc. (client supplied)
*(a) APP - guc, rft, generic library app, etc. (client supplied)
*(V) APPVER - version string of above. (client supplied)
(f) FILE - name of file/data transferred
(i) CLIENTIP - ip address of host running client (control channel)
(I) DATAIP - ip address of source/dest host of data (data channel)
(u) USER - local user name the transfer was performed as
(d) USERDN - DN that was mapped to user id
(C) CONFID - ID defined by -usage-stats-id config option
(U) SESSID - unique id that can be used to match transfers in a session and
 transfers across source/dest of a third party transfer. (client supplied)</pre>
</dl>
<p> This option can also be set in the configuration file as usage_stats_target.</dl>
<p> <code>-usage-stats-id string</code></p>
<dl>
<dd>Identifying tag to include in usage statistics data. If this is set and usage-stats-target is unset, CONFID will be added to the default usage stats data. </p>
<p> This option can also be set in the configuration file as usage_stats_id.</dl>
<h3>Single and Striped Remote Data Node Options</h3>
<p><code>-r string,-remote-nodes string</code></p>
<dl>
<dd>Comma separated list of remote node contact strings. </p>
<p> This option can also be set in the configuration file as remote_nodes.</dl>
<p> <code>-hybrid</code></p>
<dl>
<dd>When a server is configured for striped operation with the <i>remote_nodes</i> option, both a frontend and backend process are started even if the client does not request multiple stripes. This option will start backend processes only when striped operation is requested by the client, while servicing non-striped requests with a single frontend process. </p>
<p> This option can also be set in the configuration file as hybrid. The default value of this option is FALSE.</dl>
<p> <code>-dn,-data-node</code></p>
<dl>
<dd>This server is a backend data node. </p>
<p> This option can also be set in the configuration file as data_node. The default value of this option is FALSE.</dl>
<p> <code>-sbs number,-stripe-blocksize number</code></p>
<dl>
<dd>Size in bytes of sequential data that each stripe will transfer. </p>
<p> This option can also be set in the configuration file as stripe_blocksize. The default value of this option is 1048576.</dl>
<p> <code>-stripe-count number</code></p>
<dl>
<dd>Number of number stripes to use per transfer when this server controls that number. If remote nodes are statically configured (via -r or remote_nodes), this will be set to that number of nodes, otherwise the default is 1. </p>
<p> This option can also be set in the configuration file as stripe_count.</dl>
<p> <code>-sl number,-stripe-layout number</code></p>
<dl>
<dd>Stripe layout. 1 = Partitioned 2 = Blocked. </p>
<p> This option can also be set in the configuration file as stripe_layout. The default value of this option is 2.</dl>
<p> <code>-stripe-blocksize-locked</code></p>
<dl>
<dd>Do not allow client to override stripe blocksize with the OPTS RETR command </p>
<p> This option can also be set in the configuration file as stripe_blocksize_locked. The default value of this option is FALSE.</dl>
<p> <code>-stripe-layout-locked</code></p>
<dl>
<dd>Do not allow client to override stripe layout with the OPTS RETR command </p>
<p> This option can also be set in the configuration file as stripe_layout_locked. The default value of this option is FALSE.</dl>
<h3>Disk Options</h3>
<p><code>-bs number,-blocksize number</code></p>
<dl>
<dd>Size in bytes of data blocks to read from disk before posting to the network. </p>
<p> This option can also be set in the configuration file as blocksize. The default value of this option is 262144.</dl>
<p> <code>-sync-writes</code></p>
<dl>
<dd>Flush disk writes before sending a restart marker. This attempts to ensure that the range specified in the restart marker has actually been committed to disk. This option will probably impact performance, and may result in different behavior on different storage systems. See the manpage for sync() for more information. </p>
<p> This option can also be set in the configuration file as sync_writes. The default value of this option is FALSE.</dl>
<p> <code>-perms string</code></p>
<dl>
<dd>Set the default permissions for created files. Should be an octal number such as 0644. The default is 0644. Note: If umask is set it will affect this setting &#8212; i.e. if the umask is 0002 and this setting is 0666, the resulting files will be created with permissions of 0664. </p>
<p> This option can also be set in the configuration file as perms.</dl>
<p> <code>-file-timeout number</code></p>
<dl>
<dd>Timeout in seconds for all disk accesses. A value of 0 disables the timeout. </p>
<p> This option can also be set in the configuration file as file_timeout.</dl>
<h3>Network Options</h3>
<p><code>-p number,-port number</code></p>
<dl>
<dd>Port on which a frontend will listen for client control channel connections, or on which a data node will listen for connections from a frontend. If not set a random port will be chosen and printed via the logging mechanism. </p>
<p> This option can also be set in the configuration file as port.</dl>
<p> <code>-control-interface string</code></p>
<dl>
<dd>Hostname or IP address of the interface to listen for control connections on. If not set will listen on all interfaces. </p>
<p> This option can also be set in the configuration file as control_interface.</dl>
<p> <code>-data-interface string</code></p>
<dl>
<dd>Hostname or IP address of the interface to use for data connections. If not set will use the current control interface. </p>
<p> This option can also be set in the configuration file as data_interface.</dl>
<p> <code>-ipc-interface string</code></p>
<dl>
<dd>Hostname or IP address of the interface to use for ipc connections. If not set will listen on all interfaces. </p>
<p> This option can also be set in the configuration file as ipc_interface.</dl>
<p> <code>-hostname string</code></p>
<dl>
<dd>Effectively sets the above control_interface, data_interface and ipc_interface options. </p>
<p> This option can also be set in the configuration file as hostname.</dl>
<p> <code>-ipc-port number</code></p>
<dl>
<dd>Port on which the frontend will listen for data node connections. </p>
<p> This option can also be set in the configuration file as ipc_port.</dl>
<p> <code>-control-preauth-timeout number</code></p>
<dl>
<dd>Time in seconds to allow a client to remain connected to the control channel without activity before authenticating. </p>
<p> This option can also be set in the configuration file as control_preauth_timeout. The default value of this option is 120.</dl>
<p> <code>-control-idle-timeout number</code></p>
<dl>
<dd>Time in seconds to allow a client to remain connected to the control channel without activity. </p>
<p> This option can also be set in the configuration file as control_idle_timeout. The default value of this option is 600.</dl>
<p> <code>-ipc-idle-timeout number</code></p>
<dl>
<dd>Idle time in seconds before an unused ipc connection will close. </p>
<p> This option can also be set in the configuration file as ipc_idle_timeout. The default value of this option is 900.</dl>
<p> <code>-ipc-connect-timeout number</code></p>
<dl>
<dd>Time in seconds before canceling an attempted ipc connection. </p>
<p> This option can also be set in the configuration file as ipc_connect_timeout. The default value of this option is 60.</dl>
<p> <code>-allow-udt</code></p>
<dl>
<dd>Enable protocol support for UDT with NAT traversal if the udt driver is available. Requires threads. </p>
<p> This option can also be set in the configuration file as allow_udt. The default value of this option is FALSE.</dl>
<p> <code>-port-range string</code></p>
<dl>
<dd>Port range to use for incoming connections. The format is &quot;startport,endport&quot;. This, along with -data-interface, can be used to enable operation behind a firewall and/or when NAT is involved. This is the same as setting the environment variable GLOBUS_TCP_PORT_RANGE. </p>
<p> This option can also be set in the configuration file as port_range.</dl>
<h3>User Messages</h3>
<p><code>-banner string</code></p>
<dl>
<dd>Message to display to the client before authentication. </p>
<p> This option can also be set in the configuration file as banner.</dl>
<p> <code>-banner-file string</code></p>
<dl>
<dd>File to read banner message from. </p>
<p> This option can also be set in the configuration file as banner_file.</dl>
<p> <code>-banner-terse</code></p>
<dl>
<dd>When this is set, the minimum allowed banner message will be displayed to unauthenticated clients. </p>
<p> This option can also be set in the configuration file as banner_terse. The default value of this option is FALSE.</dl>
<p> <code>-banner-append</code></p>
<dl>
<dd>When this is set, the message set in the <i>banner</i> or <i>banner_file</i> option will be appended to the default banner message rather than replacing it. </p>
<p> This option can also be set in the configuration file as banner_append. The default value of this option is FALSE.</dl>
<p> <code>-version-tag string</code></p>
<dl>
<dd>Add an identifying string to the existing toolkit version. This is displayed in the default banner message, the SITE VERSION command, and usage stats. </p>
<p> This option can also be set in the configuration file as version_tag.</dl>
<p> <code>-login-msg string</code></p>
<dl>
<dd>Message to display to the client after authentication. </p>
<p> This option can also be set in the configuration file as login_msg.</dl>
<p> <code>-login-msg-file string</code></p>
<dl>
<dd>File to read login message from. </p>
<p> This option can also be set in the configuration file as login_msg_file.</dl>
<h3>Module Options</h3>
<p><code>-dsi string</code></p>
<dl>
<dd>Data Storage Interface module to load. File and remote modules are defined by the server. If not set, the file module is loaded, unless the <i>remote</i> option is specified, in which case the remote module is loaded. An additional configuration string can be passed to the DSI using the format [module name]:[configuration string] to this option. The format of the configuration string is defined by the DSI being loaded. </p>
<p> This option can also be set in the configuration file as load_dsi_module.</dl>
<p> <code>-allowed-modules string</code></p>
<dl>
<dd>Comma separated list of ERET/ESTO modules to allow, and optionally specify an alias for. Example: module1,alias2:module2,module3 (module2 will be loaded when a client asks for alias2). </p>
<p> This option can also be set in the configuration file as allowed_modules.</dl>
<p> <code>-dc-whitelist string</code></p>
<dl>
<dd>A comma separated list of drivers allowed on the network stack. </p>
<p> This option can also be set in the configuration file as dc_whitelist.</dl>
<p> <code>-fs-whitelist string</code></p>
<dl>
<dd>A comma separated list of drivers allowed on the disk stack. </p>
<p> This option can also be set in the configuration file as fs_whitelist.</dl>
<p> <code>-popen-whitelist string</code></p>
<dl>
<dd>A comma separated list of programs that the popen driver is allowed to execute, when used on the network or disk stack. An alias may also be specified, so that a client does not need to specify the full path. Format is [alias:]prog,[alias:]prog. example: /bin/gzip,tar:/bin/tar </p>
<p> This option can also be set in the configuration file as popen_whitelist.</dl>
<p> <code>-xnetmgr string</code></p>
<dl>
<dd>An option string to pass to the XIO Network Manager Driver, which will then be loaded for all data channel connections. This must be in the form &quot;manager=module;option1=value;option2=value;&quot;. See the Network Manager documentation for more info. </p>
<p> This option can also be set in the configuration file as xnetmgr.</dl>
<p> <code>-dc-default string</code></p>
<dl>
<dd>A comma separated list of XIO drivers and options representing the default network stack. Format is of each driver entry is driver1[:opt1=val1;opt2=val2;&#8230;]. The bottom of the stack, the transport driver, is always first. </p>
<p> This option can also be set in the configuration file as dc_default.</dl>
<p> <code>-fs-default string</code></p>
<dl>
<dd>A comma separated list of XIO drivers and options representing the default disk stack. Format is of each driver entry is driver1[:opt1=val1;opt2=val2;&#8230;]. The bottom of the stack, the transport driver, is always first. </p>
<p> This option can also be set in the configuration file as fs_default.</dl>
<h3>Other</h3>
<p><code>-c string</code></p>
<dl>
<dd>Path to main configuration file that should be loaded. Otherwise will attempt to load $GLOBUS_LOCATION/etc/grid<a href="ftp://ftp.conf">ftp.conf</a> and /etc/grid-security/grid<a href="ftp://ftp.conf">ftp.conf</a>.</dl>
<p> <code>-C string</code></p>
<dl>
<dd>Path to directory holding configuration files that should be loaded. Files will be loaded in alphabetical order, and in the event of duplicate parameters the last loaded file will take precedence. Files with a <i>.</i> in the name (file.bak, file.rpmsave, etc.) will be ignored. Note that the main configuration file, if one exists, will always be loaded last. </p>
<p> This option can also be set in the configuration file as config_dir.</dl>
<p> <code>-config-base-path string</code></p>
<dl>
<dd>Base path to use when config and log path options are not full paths. By default this is the current directory when the process is started. </p>
<p> This option can also be set in the configuration file as config_base_path.</dl>
<p> <code>-debug</code></p>
<dl>
<dd>Sets options that make server easier to debug. Forces no-fork, no-chdir, and allows core dumps on bad signals instead of exiting cleanly. Not recommended for production servers. Note that non-forked servers running as <i>root</i> will only accept a single connection, and then exit. </p>
<p> This option can also be set in the configuration file as debug. The default value of this option is FALSE.</dl>
<p> <code>-pidfile string</code></p>
<dl>
<dd>This option can also be set in the configuration file as pidfile.</dl>
<h2>Exit Status</h2>
<p>0</p>
<dl>
<dd>Successful program execution.</dl>
