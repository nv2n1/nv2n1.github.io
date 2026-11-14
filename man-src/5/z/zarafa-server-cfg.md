---
title: "zarafa-server-cfg(5)"
name: "zarafa-server-cfg"
section: "5"
letter: "z"
url: "/docs/linux/man/5-zarafa-server-cfg/"
description: "zarafa-server.cfg – The Zarafa configuration file"
---

<p>zarafa-server.cfg &#8211; The Zarafa configuration file</p>
<h2>Synopsis</h2>
<p><code>server.cfg</code></p>
<h2>Description</h2>
<p>The server.cfg is a configuration file for the zarafa-server process. server.cfg contains instructions for the software to set up the database environment, logging system and license.</p>
<h2>File Format</h2>
<p>The file consists of one big section, but parameters can be grouped by functionality. </p>
<p> The parameters are written in the form: </p>
<p> <code>name</code> = <i>value</i> </p>
<p> The file is line-based. Each newline-terminated line represents either a comment, nothing, a parameter or a directive. A line beginning with `#&#8217; is considered a comment, and will be ignored by Zarafa. Parameter names are case sensitive. Lines beginning with `!&#8217; are directives. </p>
<p> Directives are written in the form: </p>
<p> !<code>directive</code><i>[argument(s)] </i> </p>
<p> The following directives exist: </p>
<p> <code>include</code></p>
<dl>
<dd>Include and process <i>argument</i> </p>
<p> Example: !include common.cfg</dl>
<h2>Explanation Of The Server Settings Parameters</h2>
<p><code>server_bind</code></p>
<dl>
<dd>IP address to bind to. 0.0.0.0 for any address. Keep in mind that both Webaccess and Outlook should be able to connect. The Webaccess normally connects on 127.0.0.1, and Outlook over the network. </p>
<p> Default: <i>0.0.0.0</i></dl>
<p> <code>server_tcp_enabled</code></p>
<dl>
<dd>Enable direct TCP connections. </p>
<p> Default: <i>yes</i></dl>
<p> <code>server_tcp_port</code></p>
<dl>
<dd>Port to listen on. </p>
<p> Default: <i>236</i></dl>
<p> <code>server_pipe_enabled</code></p>
<dl>
<dd>Enable Unix pipe connections. Should not be disabled. </p>
<p> Default: <i>yes</i></dl>
<p> <code>server_recv_timeout</code></p>
<dl>
<dd>TCP and SSL receive timeout in seconds. This is the time that a TCP connection may be idle (between requests) before the TCP connection is closed from the server. Settings this high makes it less necessary for clients to re-connect, but increases the total number of concurrent open sockets in the server. You normally needn&#8217;t change the default value. </p>
<p> Default: <i>5</i></dl>
<p> <code>server_read_timeout</code></p>
<dl>
<dd>TCP and SSL read timeout in seconds. The read timeout is the amount of time that the server will wait to read more data from a socket, after processing of the request has started. This needn&#8217;t be changed in most cases. </p>
<p> Default: <i>60</i></dl>
<p> <code>server_send_timeout</code></p>
<dl>
<dd>TCP and SSL send timeout in seconds. The send timeout is the amount of time that the server will wait to write data to a socket, analogous to server_read_timeout. </p>
<p> Default: <i>60</i></dl>
<p> <code>server_max_keep_alive_requests</code></p>
<dl>
<dd>Limits the number of requests allowed per connection. </p>
<p> Default: <i>100</i></dl>
<p> <code>server_pipe_name</code></p>
<dl>
<dd>Unix socket to listen on. </p>
<p> Default: <i>/var/run/zarafa</i></dl>
<p> <code>server_pipe_priority</code></p>
<dl>
<dd>Priority unix socket to listen on. This socket is only used by the zarafa-licensed daemon. </p>
<p> Default: <i>/var/run/zarafa-prio</i></dl>
<p> <code>server_name</code></p>
<dl>
<dd>Unique name for identifying the server in a multi-server environment. </p>
<p> Default: <i>Zarafa</i></dl>
<p> <code>server_hostname</code></p>
<dl>
<dd>DNS name of the server. This is used for the Kerberos single sign-on environment. If empty (default), the FQDN or hostname will be used. </p>
<p> Default:</dl>
<p> <code>database_engine</code></p>
<dl>
<dd>The database engine to use. Values can be: </p>
<p> <i>mysql</i></p>
<dl>
<dd>Use MySQL.</dl>
<p> Default: <i>mysql</i></dl>
<p> <code>allow_local_users</code></p>
<dl>
<dd>Named Unix users which connect through the unix socket (server_pipe_name) which are added here, those users will become the internal SYSTEM user in Zarafa, and have administrative rights. Normally, this is only &#8216;root&#8217;, so the unix root user can use the zarafa-admin tool. You can add a generic user to be used by the zarafa-dagent here. This user is most likely called &#8216;vmail&#8217;. Note that the field is SPACE separated. </p>
<p> Default: <i>root</i></dl>
<p> <code>system_email_address</code></p>
<dl>
<dd>This is the e-mail address of the SYSTEM user. When people receive mail from the quota monitor, or receive fallback deliveries from the zarafa-dagent, the From email address is this field. You might want to change this field so people can reply to this address. </p>
<p> Default: <i>postmaster [at] localhost</i></dl>
<p> <code>run_as_user</code></p>
<dl>
<dd>After correctly starting, the server process will become this user, dropping root privileges. Note that the log file needs to be writeable by this user, and the directory too to create new logfiles after logrotation. This can also be achieved by setting the correct group and permissions. </p>
<p> Default value is empty, not changing the user after starting.</dl>
<p> <code>run_as_group</code></p>
<dl>
<dd>After correctly starting, the server process will become this group, dropping root privileges. </p>
<p> Default value is empty, not changing the group after starting.</dl>
<p> <code>pid_file</code></p>
<dl>
<dd>Write the process ID number to this file. This is used by the init.d script to correctly stop/restart the service. </p>
<p> Default: <i>/var/run/zarafa-server.pid</i></dl>
<p> <code>running_path</code></p>
<dl>
<dd>Change directory to this path when running in daemonize mode. When using the -F switch to run in the foreground the directory will not be changed. </p>
<p> Default: <i>/</i></dl>
<p> <code>coredump_enabled</code></p>
<dl>
<dd>When a segfault occurs, a coredump file will be written in the running_path directory. This file should be sent along with the crash report. </p>
<p> Default: <i>yes</i></dl>
<p> <code>session_timeout</code></p>
<dl>
<dd>The session timeout specifies how many seconds must elapse without any activity from a client before the server counts the session as dead. The client sends keepalive requests every 60 seconds, so the session timeout can never be below 60. In fact, if you specify a timeout below 300, 300 will be taken as the session timeout instead. This makes sure you can never timeout your session while the Zarafa client is running. </p>
<p> Setting the session timeout low will keep the session count and therefore the memory usage on the server low, but may also timeout sessions of client that have lost network connectivity temporarily. For example, some clients with powersaving modes will disable the ethernet card during the screensaver. When this happens, you must set the session_timeout to a value that is higher than the time that it takes for the network connection to come back. This could be anything ranging up to several hours. </p>
<p> Default: <i>300</i></dl>
<p> <code>session_ip_check</code></p>
<dl>
<dd>Normally, a session is linked to an IP-address, so this check is enabled. You may want to disable this check when you have laptop&#8217;s which can get multiple ip-adresses through wired and wireless networks. It is highly recommended to leave this check enabled, since the session id can be used by other machines, and thus introduces a large security risc. Since version 6.20, the session id is 64 bits. Older versions use a 32 bit session id, so then the session is easier guessable. </p>
<p> Default: <i>yes</i></dl>
<p> <code>hide_everyone</code></p>
<dl>
<dd>If this option is set to &#8216;yes&#8217;, the internal group Everyone (which always contains all users) will be hidden from the Global Addressbook. Thus, users will not be able to send e-mail to this group anymore, and also will not be able to set access rights on folders for this group. Administrators will still be able to see and use the group. </p>
<p> Default: <i>no</i></dl>
<p> <code>hide_system</code></p>
<dl>
<dd>If this option is set to &#8216;yes&#8217;, the internal user SYSTEM will be hidden from the Global Addressbook. Thus, users will not be able to send e-mail to this user anymore. Administrators will still be able to see and use the user. </p>
<p> Default: <i>yes</i></dl>
<p> <code>thread_stacksize</code></p>
<dl>
<dd>This setting might be usefull on 32bit system with a lot of users. This setting should not be set too small, or your server will crash. The value set is in Kb. </p>
<p> Default: <i>512</i></dl>
<p> <code>license_socket</code></p>
<dl>
<dd>Path to the <code><a href="/docs/linux/man/1-zarafa-licensed/">zarafa-licensed</a></code>(1) service. </p>
<p> Default: <i>/var/run/zarafa-licensed</i></dl>
<p> <code>license_timeout</code></p>
<dl>
<dd>Time (in seconds) to wait for a connection to the <code><a href="/docs/linux/man/1-zarafa-licensed/">zarafa-licensed</a></code>(1) before terminating the request. </p>
<p> Default: <i>10</i></dl>
<h2>Explanation Of The Logging Settings Parameters</h2>
<p><code>log_method</code></p>
<dl>
<dd>The method which should be used for logging. Valid values are: </p>
<p> <i>syslog</i></p>
<dl>
<dd>Use the Linux system log. All messages will be written to the mail facility. See also <code><a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a></code>(5).</dl>
<p> <i>file</i></p>
<dl>
<dd>Log to a file. The filename will be specified in <code>log_file</code>.</dl>
<p> Default: <i>file</i></dl>
<p> <code>log_file</code></p>
<dl>
<dd>When logging to a file, specify the filename in this parameter. Use <i>&#8211;</i> (minus sign) for stderr output. </p>
<p> Default: <i>/var/log/zarafa/server.log</i></dl>
<p> <code>log_level</code></p>
<dl>
<dd>The level of output for logging in the range from 0 to 5. 0 means no logging, 5 means full logging. </p>
<p> Default: <i>2</i></dl>
<p> <code>log_timestamp</code></p>
<dl>
<dd>Specify whether to prefix each log line with a timestamp in &#8216;file&#8217; logging mode. </p>
<p> Default: <i>1</i></dl>
<h2>Explanation Of The Security Logging Settings Parameters</h2>
<p><code>audit_log_enabled</code></p>
<dl>
<dd>Whether the security logging feature should be enabled. </p>
<p> Default: <i>no</i></dl>
<p> <code>audit_log_method</code></p>
<dl>
<dd>The method which should be used for logging. Valid values are: </p>
<p> <i>syslog</i></p>
<dl>
<dd>Use the Linux system log. All messages will be written to the authpriv facility. See also <code><a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a></code>(5).</dl>
<p> <i>file</i></p>
<dl>
<dd>Log to a file. The filename will be specified in <code>log_file</code>.</dl>
<p> Default: <i>syslog</i></dl>
<p> <code>audit_log_file</code></p>
<dl>
<dd>When logging to a file, specify the filename in this parameter. Use <i>&#8211;</i> (minus sign) for stderr output. </p>
<p> Default: <i>&#8211;</i></dl>
<p> <code>audit_log_level</code></p>
<dl>
<dd>The level of output for logging in the range from 0 to 1. 0 means no logging, 1 means full logging. </p>
<p> Default: <i>1</i></dl>
<p> <code>audit_log_timestamp</code></p>
<dl>
<dd>Specify whether to prefix each log line with a timestamp in &#8216;file&#8217; logging mode. </p>
<p> Default: <i>1</i></dl>
<h2>Explanation Of The Mysql Settings Parameters</h2>
<p><code>mysql_host</code></p>
<dl>
<dd>The hostname of the MySQL server to use. </p>
<p> Default: <i>localhost</i></dl>
<p> <code>mysql_port</code></p>
<dl>
<dd>The port of the MySQL server to use. </p>
<p> Default: <i>3306</i></dl>
<p> <code>mysql_user</code></p>
<dl>
<dd>The user under which we connect with MySQL. </p>
<p> Default: <i>root</i></dl>
<p> <code>mysql_password</code></p>
<dl>
<dd>The password to use for MySQL. Leave empty for no password. </p>
<p> Default:</dl>
<p> <code>mysql_socket</code></p>
<dl>
<dd>The socket of the MySQL server to use. This option can be used to override the default mysql socket. To use the socket, the mysql_host value must be empty or &#8216;localhost&#8217; </p>
<p> Default:</dl>
<p> <code>mysql_database</code></p>
<dl>
<dd>The MySQL database to connect to. </p>
<p> Default: <i>zarafa</i></dl>
<p> <code>mysql_group_concat_max_len</code></p>
<dl>
<dd>The group_concat_max_len used to set for MySQL. If you have large distribution lists (more than 150 members), it is useful to set this value higher. On the other hand, some MySQL versions are known to break with a value higher than 21844. </p>
<p> Default: <i>21844</i></dl>
<p> <code>attachment_storage</code></p>
<dl>
<dd>The location where attachments are stored. This can be in the MySQL database, or as separate files. The drawback of &#8216;database&#8217; is that the large data of attachment will push usefull data from the MySQL cache. The drawback of separate files is that a mysqldump is not enough for a full disaster recovery. </p>
<p> Default: <i>files</i></dl>
<p> <code>attachment_path</code></p>
<dl>
<dd>When the attachment_storage option is &#8216;files&#8217;, this option sets the location of the attachments on disk. Note that the server runs as the &#8216;run_as_user&#8217; user and &#8216;run_as_group&#8217; group, which will require write access to this directory. </p>
<p> Default: <i>/var/lib/zarafa/attachments</i></dl>
<p> <code>attachment_compression</code></p>
<dl>
<dd>When the attachment_storage option is &#8216;files&#8217;, this option controls the compression level for the attachments. Higher compression levels will compress data better, but at the cost of CPU usage. Lower compression levels will require less CPU but will compress data less. Setting the compression level to 0 will effectively disable compression completely. </p>
<p> Changing the compression level, or switching it on or off, will not affect any existing attachments, and will remain accessible as normal. </p>
<p> Set to <i>0</i> to disable compression completely. The maximum compression level is <i>9</i> </p>
<p> Default: <i>6</i></dl>
<h2>Explanation Of The Ssl Settings Parameters</h2>
<p><code>server_ssl_enabled</code></p>
<dl>
<dd>Enable direct SSL connections. When this option is enabled, you must set the following ssl options correctly, otherwise the server may or will not start. </p>
<p> Default: <i>no</i></dl>
<p> <code>server_ssl_port</code></p>
<dl>
<dd>The portnumber to accept SSL connections on. </p>
<p> Default: <i>237</i></dl>
<p> <code>server_ssl_key_file</code></p>
<dl>
<dd>The file containing the private key and certificate. Please read the SSL section in the <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1) manual on how to create this file. </p>
<p> Default: <i>/etc/zarafa/ssl/server.pem</i></dl>
<p> <code>server_ssl_key_pass</code></p>
<dl>
<dd>Enter you password here when your key file contains a password to be readable. </p>
<p> No default set.</dl>
<p> <code>server_ssl_ca_file</code></p>
<dl>
<dd>The CA file which was used to sign client SSL certificates. This CA will be trusted. This value must be set for clients to login with an SSL Key. Their public key must be present in the sslkeys_path directory. </p>
<p> No default set.</dl>
<p> <code>server_ssl_ca_path</code></p>
<dl>
<dd>When you have multiple CA&#8217;s to trust, you may use this option. Set this to a directory which contains all your trusted CA certificates. The name of the certificate needs to be the hash of the certificate. You can get the hash value of the certificate with the following command: </p>
<p> <code> openssl x509 -hash -noout -in cacert.pem </code> </p>
<p> Create a symbolic link to the certificate with the hashname like this: </p>
<p> <code> ln -s cacert.pem `openssl x509 -hash -noout -in cacert.pem`.0 </code> </p>
<p> If you have several certificates which result in the same hash, use .1, .2, etc. in the end of the filename. </p>
<p> No default set.</dl>
<p> <code>sslkeys_path</code></p>
<dl>
<dd>The path which contains public keys of clients which can login over SSL using their key. Please read the SSL section in the <code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1) manual on how to create these files. </p>
<p> Default: <i>/etc/zarafa/sslkeys</i></dl>
<p> <code>server_ssl_protocols</code></p>
<dl>
<dd>Disabled or enabled protocol names. Supported protocol names are <i>SSLv2</i>, <i>SSLv3</i> and <i>TLSv1</i>. If Zarafa was linked against OpenSSL 1.0.1 or later there is additional support for the new protocols <i>TLSv1.1</i> and <i>TLSv1.2</i>. To exclude both, SSLv2 and SSLv3 set <code>server_ssl_protocols</code> to <i>!SSLv2 !SSLv3</i>. SSLv2 is considered unsafe and these connections should not be accepted. </p>
<p> Default: <i>!SSLv2</i></dl>
<p> <code>server_ssl_ciphers</code></p>
<dl>
<dd>SSL ciphers to use, set to <i>ALL</i> for backward compatibility. </p>
<p> Default: <i>ALL:!LOW:!SSLv2:!EXP:!aNULL</i></dl>
<p> <code>server_ssl_prefer_server_ciphers</code></p>
<dl>
<dd>Prefer the server&#8217;s order of SSL ciphers over client&#8217;s. </p>
<p> Default: <i>no</i></dl>
<h2>Explanation Of The Threading Parameters</h2>
<p><code>threads</code></p>
<dl>
<dd>Number of server threads. </p>
<p> Default: <i>8</i></dl>
<p> <code>watchdog_frequency</code></p>
<dl>
<dd>Watchdog frequency. The number of watchdog checks per second. </p>
<p> Default: <i>1</i></dl>
<p> <code>watchdog_max_age</code></p>
<dl>
<dd>Watchdog max age. The maximum age in ms of a task before a new thread is started. </p>
<p> Default: <i>500</i></dl>
<p> <code>server_max_keep_alive_requests</code></p>
<dl>
<dd>Maximum SOAP keep_alive value. </p>
<p> Default: <i>100</i></dl>
<p> <code>server_recv_timeout</code></p>
<dl>
<dd>SOAP recv timeout value. </p>
<p> Default: <i>5</i></dl>
<p> <code>server_send_timeout</code></p>
<dl>
<dd>SOAP send timeout value. </p>
<p> Default: <i>60</i></dl>
<h2>Explanation Of The Other Settings Parameters</h2>
<p><code>softdelete_lifetime</code></p>
<dl>
<dd>Softdelete clean cycle, in days. 0 means never. Items older than this setting will be removed from the database. </p>
<p> Default: <i>0</i></dl>
<p> <code>sync_lifetime</code></p>
<dl>
<dd>Synchronization clean cycle, in days. 0 means never. Synchronizations older than this setting will be removed from the database. </p>
<p> Default: <i>90</i></dl>
<p> <code>sync_log_all_changes</code></p>
<dl>
<dd>Normally changes to messages inside folders which no user is syncing from are not logged to the database as optimization. In some scenarios (i.e. when using BlackBerry synchronization) it is important for all changes to be logged regardless of the number of listeners to these changes. </p>
<p> Setting this value to <i>yes</i> will cause slightly more database traffic and the value <i>no</i> will be the correct for most installations. </p>
<p> Default: <i>no</i></dl>
<p> <code>enable_sso</code></p>
<dl>
<dd>When you configured your system for single sign-on, you can enable this by setting the value to <i>yes</i>. The server can autodetect between NTLM and Kerberos. For NTLM authentication you will need the ntlm_auth program from Samba. Please see the server installation manual on howto enable your system for single sign-on. </p>
<p> Default: <i>no</i></dl>
<p> <code>enable_gab</code></p>
<dl>
<dd>Enables viewing of the Global Address Book (GAB) by users. Disabling the GAB will show an empty list in the GAB, which may be required for some installations. Resolving addresses is not affected by this option. </p>
<p> Users with administrator rights are also not affected by this option and always have access to the GAB. </p>
<p> Default: <i>yes</i></dl>
<p> <code>auth_method</code></p>
<dl>
<dd>Authentication is normally done in the user plugin. In case your plugin cannot provide the authentication, you may set this to pam, and set the pam_service to authenticate through pam. Another choice is kerberos. The user password will be verified using the kerberos service. Note that is not a single-signon method, since the server requires the user password. </p>
<p> Default: <i>plugin</i></dl>
<p> <code>restrict_admin_permissions</code></p>
<dl>
<dd>Normally, admin users are granted all permissions on all stores in the server, or for stores in the tenant&#8217;s company (in multi-tenant mode). Enabling this option restricts permissions to folder operations: Folder viewing, folder creation and importantly, folder permissions. This means that an administrator can grant himself full permissions on a folder. However, in combination with auditing, it provides an extra level of security protection against unwanted access. </p>
<p> Note that some applications may require full access to all stores, which would be restricted by this option. Also, this option cannot be reset by sending a HUP signal, so a full server restart is required to change the setting. </p>
<p> Default: <i>no</i></dl>
<p> <code>embedded_attachment_limit</code></p>
<dl>
<dd>Defines the number of attachment-in-attachment-in-attachment levels allowed when saving and replicating a MAPI object. This limit can be made higher if needed, but will also require you to increase the stack_size in mysql to allow for correct exporting for replication. </p>
<p> Default: <i>no</i></dl>
<p> <code>pam_service</code></p>
<dl>
<dd>This is the pam service name. Pam services can be found in /etc/pam.d/. </p>
<p> Default: <i>passwd</i></dl>
<p> <code>max_deferred_records</code></p>
<dl>
<dd>The server has a list of deferred writes to the tproperties table, to improve overall I/O performance. The number of deferred writes is kept below this value; setting it high will allow writes to be more efficient by grouping more writes together, but may slow down reading, and setting it low will force writes to complete directly, but speed up reading of tables. </p>
<p> Default: <i>0 (off)</i></dl>
<p> <code>max_deferred_records_folder</code></p>
<dl>
<dd>Same as the max_deferred_records variable, but per folder instead of total. </p>
<p> Default: <i>20</i></dl>
<p> <code>disabled_features</code></p>
<dl>
<dd>In this list you can disable certain features for users. Normally all features are enabled for all users, making it possible through the user plugin to disable specific features for specific users. To set the default of a feature to disabled, add it here to the list, making it possible through the user plugin to enable a specific user for specific users. </p>
<p> This list is space separated, and currently may contain the following features: imap, pop3. </p>
<p> Default: <i>imap pop3</i></dl>
<h2>Explanation Of The Cache Settings Parameters</h2>
<p><code>cache_cell_size</code></p>
<dl>
<dd>Size in bytes of the cell cache. This is the main cache used in Zarafa. It caches all data that comes into view in tables (ie the view of your inbox, or any other folder). In an ideal situation, all cells would be cached, so that the database does not need to be queried for data when browsing through folders, but this would require around 1.5K per message item (e-mail, appointment task, etc) in the entire server. If you can afford it, set this value as high as possible, up to 50% of your total RAM capacity. Make sure this doesn&#8217;t lead to swapping though. This value may contain a k, m or g multiplier. </p>
<p> Default: <i>256M</i></dl>
<p> <code>cache_object_size</code></p>
<dl>
<dd>This caches objects and their respective hierarchy of folders. You can calculate the size with a simple equation: </p>
<p> concurrent users * max items in a folder * 24 </p>
<p> This value may contain a k, m or g multiplier. </p>
<p> Default: <i>5M</i></dl>
<p> <code>cache_indexedobject_size</code></p>
<dl>
<dd>This cache contains unique id&#8217;s of objects. This cache is used twice, also by the index2 cache, which is the inverse of the index1 cache. This value may contain a k, m or g multiplier. </p>
<p> Default: <i>16M</i></dl>
<p> <code>cache_quota_size</code></p>
<dl>
<dd>This cache contains quota values of users. This value may contain a k, m or g multiplier. </p>
<p> Default: <i>1M</i></dl>
<p> <code>cache_quota_lifetime</code></p>
<dl>
<dd>This sets the lifetime for quota details inside the cache. If quota details weren&#8217;t queried during this period it is removed from the cache making room for more often requested quota details. Set to 0 to never expire, or -1 to disable this cache. </p>
<p> Default: <i>1</i> (1 minute)</dl>
<p> <code>cache_acl_size</code></p>
<dl>
<dd>This cache contains Access Control List values. Folders who are opened in other stores than your own are listed in the ACL table, and will be cached. This value may contain a k, m or g multiplier. </p>
<p> Default: <i>1M</i></dl>
<p> <code>cache_store_size</code></p>
<dl>
<dd>This cache contains store id values. This value may contain a k, m or g multiplier. </p>
<p> Default: <i>1M</i></dl>
<p> <code>cache_user_size</code></p>
<dl>
<dd>This cache contains user id values. This cache is used twice, also by the externid cache, which is the inverse of this cache. This value may contain a k, m or g multiplier. </p>
<p> Default: <i>1M</i></dl>
<p> <code>cache_userdetails_size</code></p>
<dl>
<dd>This cache contains the details of users. This value may contain a k, m or g multiplier. </p>
<p> Default: <i>3M</i></dl>
<p> <code>cache_userdetails_lifetime</code></p>
<dl>
<dd>This sets the lifetime for user details inside the cache. If user details weren&#8217;t queried during this period it is removed from the cache making room for more often requested user details. Set to 0 to never expire, or -1 to disable this cache. </p>
<p> Default: <i>0</i> (never expire)</dl>
<p> <code>cache_server_size</code></p>
<dl>
<dd>This cache contains server locations. This cache is only used in multiserver mode. This value may contain a k, m or g multiplier. </p>
<p> Default: <i>1M</i></dl>
<p> <code>cache_server_lifetime</code></p>
<dl>
<dd>This sets the lifetime for server location details inside the cache. If server details weren&#8217;t queried during this period it is removed from the cache making room for more often requested server details. Set to 0 to never expire, or -1 to disable this cache. </p>
<p> Default: <i>30</i> (30 minutes)</dl>
<h2>Explanation Of The Quota Settings Parameters</h2>
<p><code>quota_warn</code></p>
<dl>
<dd>Size in Mb of de default quota warning level. Use 0 to disable this quota level. </p>
<p> Default: <i>0</i></dl>
<p> <code>quota_soft</code></p>
<dl>
<dd>Size in Mb of de default quota soft level. Use 0 to disable this quota level. </p>
<p> Default: <i>0</i></dl>
<p> <code>quota_hard</code></p>
<dl>
<dd>Size in Mb of de default quota hard level. Use 0 to disable this quota level. </p>
<p> Default: <i>0</i></dl>
<p> <code>companyquota_warn</code></p>
<dl>
<dd>Size in Mb of de default quota warning level for multitenant public stores. Use 0 to disable this quota level. </p>
<p> Default: <i>0</i></dl>
<h2>Explanation Of The User Plugin Settings Parameters</h2>
<p><code>plugin_path</code></p>
<dl>
<dd>The location of the Zarafa plugin directory. </p>
<p> Default: <i>/usr/lib/zarafa</i></dl>
<p> <code>user_plugin</code></p>
<dl>
<dd>The source of the user base. Possible values are: </p>
<p> <i>db</i></p>
<dl>
<dd>Retrieve the users from the Zarafa database. Use the zarafa-admin tool to create users and groups. There are no additional settings for this plugin.</dl>
<p> <i>ldap</i></p>
<dl>
<dd>Retrieve the users and groups information from an LDAP server. All additional LDAP settings are set in a separate config file, which will be defined by the <code>user_plugin_config</code>. See also <code><a href="/docs/linux/man/5-zarafa-ldap-cfg/">zarafa-ldap.cfg</a></code>(5).</dl>
<p> <i>unix</i></p>
<dl>
<dd>Retrieve the users and groups information from the Linux password files. User information will be read the /etc/passwd file. Passwords will be checked agains /etc/shadow. Group information will read from /etc/group. Use the <code><a href="/docs/linux/man/1-zarafa-admin/">zarafa-admin</a></code>(1) tool to set Zarafa specific attributes on a user. </p>
<p> All additional Unix settings are set in a separate config file, which will be defined by the <code>user_plugin_config</code>. See also <code><a href="/docs/linux/man/5-zarafa-unix-cfg/">zarafa-unix.cfg</a></code>(5) .</dl>
<p> Default: <i>db</i></dl>
<p> <code>createuser_script</code>, <code>deleteuser_script</code>, <code>creategroup_script</code>, <code>deletegroup_script</code>, <code>createcompany_script</code>, <code>deletecompany_script</code></p>
<dl>
<dd>These scripts are called by the server when the external user source, like LDAP, is different from the users, groups and companies which are known to Zarafa. The script uses a environment variable to see which user, group or tenant is affected. The following parameter is used for the script: </p>
<p> <code>createuser_script</code></p>
<dl>
<dd><i>ZARAFA_USER</i> contains the new username. The script should at least call <code>zarafa-admin</code><i>&#8211;create-store</i><i>&quot;${ZARAFA_USER}&quot;</i> to correctly create the store for the new user. </p>
<p> Default: <i>/etc/zarafa/userscripts/createuser</i></dl>
<p> <code>deleteuser_script</code></p>
<dl>
<dd><i>ZARAFA_STOREID</i> contains the old id of the store of the removed user. </p>
<p> Default: <i>/etc/zarafa/userscripts/deleteuser</i></dl>
<p> <code>creategroup_script</code></p>
<dl>
<dd><i>ZARAFA_GROUP</i> contains the new groupname. No action is currently needed by the script. </p>
<p> Default: <i>/etc/zarafa/userscripts/creategroup</i></dl>
<p> <code>deletegroup_script</code></p>
<dl>
<dd><i>ZARAFA_GROUPID</i> contains the old id of the group. No action is currently needed by the script. </p>
<p> Default: <i>/etc/zarafa/userscripts/deletegroup</i></dl>
<p> <code>createcompany_script</code></p>
<dl>
<dd><i>ZARAFA_COMPANY</i> contains the new companyname. No action is currently needed by the script. </p>
<p> Default: <i>/etc/zarafa/userscripts/createcompany</i></dl>
<p> <code>deletecompany_script</code></p>
<dl>
<dd><i>ZARAFA_COMPANYID</i> contains the old id of the company. No action is currently needed by the script. </p>
<p> Default: <i>/etc/zarafa/userscripts/deletecompany</i></dl>
</dl>
<p> <code>user_safe_mode</code></p>
<dl>
<dd>If enabled, the zarafa server will only log when create, delete and move actions are done on an user object. This might be useful when you are testing changes to your plugin configuration. </p>
<p> Default: <i>no</i></dl>
<h2>Explanation Of Miscelleanious Parameters</h2>
<p><code>enable_hosted_zarafa</code></p>
<dl>
<dd>Enable multi-tenancy environment. </p>
<p> When set to true it is possible to create companies within the zarafa instance and assign all users and groups to particular companies. </p>
<p> When set to false, the normal single-tenancy environment is created. </p>
<p> Default: <i>false</i></dl>
<p> <code>enable_distributed_zarafa</code></p>
<dl>
<dd>Enable multi-server environment. </p>
<p> When set to true it is possible to place users and companies on specific servers. </p>
<p> When set to false, the normal single-server environment is created. </p>
<p> Default: <i>false</i></dl>
<p> <code>storename_format</code></p>
<dl>
<dd>Display format of store name. </p>
<p> Allowed variables: </p>
<p> <code>%u</code></p>
<dl>
<dd>Username</dl>
<p> <code>%f</code></p>
<dl>
<dd>Fullname</dl>
<p> <code>%c</code></p>
<dl>
<dd>Companyname</dl>
<p> Default: <i>%f</i></dl>
<p> <code>loginname_format</code></p>
<dl>
<dd>Loginname format (for multi-tenancy installations). When the user does not login through a system-wide unique username (like the email address) a unique name has created by combining the username and the tenancyname. With the this configuration option you can set how the loginname should be build up. </p>
<p> Allowed variables: </p>
<p> <code>%u</code></p>
<dl>
<dd>Username</dl>
<p> <code>%c</code></p>
<dl>
<dd>Companyname</dl>
<p> Default: <i>%u</i></dl>
<p> <code>client_update_enabled</code></p>
<dl>
<dd>Enable client updates. </p>
<p> You can place the Zarafa Outlook Client installer in the client_update_path directory, and enable this option. Windows clients which have the automatic updater program installed will be able to download the latest client from the Zarafa server. </p>
<p> Default: <i>false</i></dl>
<p> <code>client_update_path</code></p>
<dl>
<dd>This is the path where you will place the Zarafa Outlook Client MSI install program for Windows clients to download. You need the <code>client_update_enabled</code> option set to <i>true</i> for clients to actually download this file through the Zarafa server. </p>
<p> Default: <i>/var/lib/zarafa/client</i></dl>
<p> <code>client_update_log_level</code></p>
<dl>
<dd>Receive the log information from the client auto update service. </p>
<p> Options: 0 disable, 1 sent only with errors, 2 always sent </p>
<p> Default: <i>1</i></dl>
<p> <code>client_update_log_path</code></p>
<dl>
<dd>Log location for the client auto update files </p>
<p> You need the <code>client_update_log_level</code> option set to non-zero value to receive log files from the client. </p>
<p> Default: <i>/var/log/zarafa/autoupdate</i></dl>
<p> <code>search_enabled</code></p>
<dl>
<dd>Use the zarafa-search indexing service for faster searching. Enabling this option requires the <code><a href="/docs/linux/man/1-zarafa-search/">zarafa-search</a></code>(1) service to be running. </p>
<p> Default: <i>yes</i></dl>
<p> <code>search_socket</code></p>
<dl>
<dd>Path to the <code><a href="/docs/linux/man/1-zarafa-search/">zarafa-search</a></code>(1) service, this option is only required if the server is going to make use of the indexing service. </p>
<p> Default: <i>file:///var/run/zarafa-search</i></dl>
<p> <code>search_timeout</code></p>
<dl>
<dd>Time (in seconds) to wait for a connection to the <code><a href="/docs/linux/man/1-zarafa-search/">zarafa-search</a></code>(1) before terminating the indexed search request. </p>
<p> Default: <i>10</i></dl>
<p> <code>enable_enhanced_ics</code></p>
<dl>
<dd>Allow enhanced ICS operations to speedup synchronization with cached profiles. Only disable this option for debugging purposes. </p>
<p> Default: <i>yes</i></dl>
<p> <code>enable_sql_procedures</code></p>
<dl>
<dd>SQL Procedures allow for some optimized queries when streaming with enhanced ICS. This is default disabled because you must set &#8216;thread_stack = 256k&#8217; in your MySQL server config under the [mysqld] tag and restart your MySQL server. </p>
<p> Default: <i>no</i></dl>
<p> <code>folder_max_items</code></p>
<dl>
<dd>Limits the amount of items (messages or folders) in a single folder. This makes sure that the server will not attempt to load folders that are so large that it would require huge amounts of memory just to show the data. In practice, folders of over 1000000 items are usually created by runaway processes which are therefore useless anyway. </p>
<p> Default: <i>1000000</i></dl>
<p> <code>sync_gab_realtime</code></p>
<dl>
<dd>When set to &#8216;yes&#8217;, zarafa will synchronize the local user list whenever a list of users is requested (eg during zarafa-admin -l or when opening the addressbook). This was the default for zarafa 6.40.4 and earlier. When setting this value to &#8216;no&#8217;, synchronization will only occur during zarafa-admin &#8211;sync. This is useful for setups which have large addressbooks (more than 1000 entries in the addressbook). </p>
<p> This option is forced to &#8216;yes&#8217; when using the &#8216;db&#8217; plugin since synchronization is implicit in that case. </p>
<p> Default: <i>yes</i></dl>
<p> <code>counter_reset</code></p>
<dl>
<dd>The counter_reset option forces a recount of items in the folder each time a folder is opened. Although this is not strictly necessary, it is a precaution to make sure that counters are always correct. When enabled, this does incur a performance penalty, especially on large (&gt;50000 items) folders. Each time a counter_reset found an incorrect item count, it increments the system statistic counter_resyncs. If it is at 0 on your system, then this option has had no effect except for slowing it down. </p>
<p> Default: <i>yes</i></dl>
<p> <code>proxy_header</code></p>
<dl>
<dd>In normal operation, a cluster of zarafa-server nodes is served by sending redirections back to the clients requesting information. The redirection URL is built from the server&#8217;s information in the LDAP database. However, in some cases it is useful to place the zarafa-server instances behind a reverse HTTP proxy. In this case the redirected URL returned to the client cannot be the &#8216;normal&#8217; hostname, but must be a URL that is handled by the proxy. </p>
<p> However, internal (&#8216;behind&#8217; the proxy) redirections must *not* be redirected to the proxy since this is not necessary. The strategy is that zarafa-server will redirect to the proxy URL if the connection that initiated the redirect passed through a proxy. The way that this is detected is by examining an HTTP header. If the header specified by this option is found, then redirections will be to the proxy. If it is not, then redirections will be to the internal host. If the special value &#8216;*&#8217; is specified for this option, then the proxy URL will always be used. Specifying an empty value disables proxy detection. </p>
<p> Another effect of this option is that when a proxy connection is detected, zarafa-server attempts to use the &#8216;X-Forwarded-For&#8217; header to determine the originating IP address. This is used for logging and session binding (a session initiated on a certain IP address may not be accessed from another IP address). </p>
<p> Default:</dl>
<h2>Reloading</h2>
<p>The following options are reloadable by sending the zarafa-server process a HUP signal or reload the process by the initscript </p>
<p> system_email_address, local_admin_users, allow_local_users, hide_system, hide_everyone, auth_method, pam_service, enable_sso, enable_gab, sync_gab_realtime</p>
<dl>
<dd></dl>
<p> session_timeout, server_recv_timeout, server_read_timeout, server_send_timeout, sync_lifetime</p>
<dl>
<dd></dl>
<p> log_level, audit_log_level</p>
<dl>
<dd></dl>
<p> threads, watchdog_max_age, watchdog_frequency, max_deferred_records, max_deferred_records_folder</p>
<dl>
<dd></dl>
<p> counter_reset, user_safe_mode, enable_enhanced_ics, report_path, report_ca_path, client_update_log_level, client_update_path, client_update_log_path</p>
<dl>
<dd></dl>
<p> search_enabled, search_socket, search_timeout, disabled_features, mysql_group_concat_max_len, embedded_attachment_limit, proxy_header</p>
<dl>
<dd></dl>
<p> quota_warn, quota_soft, quota_hard, companyquota_warn</p>
<dl>
<dd></dl>
<p> createuser_script, deleteuser_script, creategroup_script, deletegroup_script, createcompany_script, deletecompany_script</p>
<dl>
<dd></dl>
<h2>Files</h2>
<p>/etc/zarafa/server.cfg</p>
<dl>
<dd>The server configuration file.</dl>
<p> /etc/zarafa/ldap.cfg</p>
<dl>
<dd>The Zarafa LDAP user plugin configuration file.</dl>
<p> /etc/zarafa/unix.cfg</p>
<dl>
<dd>The Zarafa Unix user plugin configuration file.</dl>
<h2>Author</h2>
<p>Written by Zarafa.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-zarafa-server/">zarafa-server</a></code>(1)<code><a href="/docs/linux/man/5-zarafa-ldap-cfg/">zarafa-ldap.cfg</a></code>(5)<code><a href="/docs/linux/man/5-zarafa-unix-cfg/">zarafa-unix.cfg</a></code>(5) </p>
