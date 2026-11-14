---
title: "zarafa-gateway-cfg(5)"
name: "zarafa-gateway-cfg"
section: "5"
letter: "z"
url: "/docs/linux/man/5-zarafa-gateway-cfg/"
description: "zarafa-gateway.cfg – The Zarafa gateway configuration file"
---

<p>zarafa-gateway.cfg &#8211; The Zarafa gateway configuration file</p>
<h2>Synopsis</h2>
<p><code>gateway.cfg</code></p>
<h2>Description</h2>
<p>The gateway.cfg is a configuration file for the Zarafa Gateway. gateway.cfg contains instructions for the software to set up the logging system and to enable or disable the POP3, POP3S, IMAP or IMAPS part of the service.</p>
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
<h2>Explanation Of Each Parameter</h2>
<p><code>server_bind</code></p>
<dl>
<dd>IP address to bind to. 0.0.0.0 for any address. </p>
<p> Default: <i>0.0.0.0</i></dl>
<p> <code>server_hostname</code></p>
<dl>
<dd>Hostname of the server to print to a client in the logon greeting. Leave empty to use DNS to find the hostname. </p>
<p> Default:</dl>
<p> <code>server_hostname_greeting</code></p>
<dl>
<dd>Whether to show the hostname in the logon greeting to clients. This config option is reloadable using the HUP signal. </p>
<p> Default: <i>no</i></dl>
<p> <code>pop3_enable</code></p>
<dl>
<dd>Enable POP3 service with value yes. All other values disable the service. </p>
<p> Default: <i>yes</i></dl>
<p> <code>pop3_port</code></p>
<dl>
<dd>The POP3 service will listen on this port for incoming connections. </p>
<p> Default: <i>110</i></dl>
<p> <code>pop3s_enable</code></p>
<dl>
<dd>Enable POP3S service with value yes. All other values disable the service. </p>
<p> Default: <i>yes</i></dl>
<p> <code>pop3s_port</code></p>
<dl>
<dd>The POP3S service will listen on this port for incoming connections. </p>
<p> Default: <i>995</i></dl>
<p> <code>imap_enable</code></p>
<dl>
<dd>Enable IMAP service with value yes. All other values disable the service. </p>
<p> Default: <i>yes</i></dl>
<p> <code>imap_port</code></p>
<dl>
<dd>The IMAP service will listen on this port for incoming connections. </p>
<p> Default: <i>143</i></dl>
<p> <code>imaps_enable</code></p>
<dl>
<dd>Enable IMAPS service with value yes. All other values disable the service. </p>
<p> Default: <i>yes</i></dl>
<p> <code>imaps_port</code></p>
<dl>
<dd>The IMAPS service will listen on this port for incoming connections. </p>
<p> Default: <i>993</i></dl>
<p> <code>server_socket</code></p>
<dl>
<dd>The http address of the Zarafa server. </p>
<p> Default: <i><a rel="nofollow" href="http://localhost:236/zarafa">http://localhost:236/zarafa</a></i> </p>
<p> It is not advised to specify the UNIX socket here, but the http address instead. In default configuration the gateway will then be trusted by the Zarafa server (as set in its local_admin_users configuration setting). Unless is run as an untrusted user, by specifying the <code>run_as_user</code>, the gateway always authenticates users even if they provide no or wrong credentials!</dl>
<p> <code>run_as_user</code></p>
<dl>
<dd>After correctly starting, the gateway process will become this user, dropping root privileges. Note that the log file needs to be writeable by this user, and the directory too to create new logfiles after logrotation. This can also be achieved by setting the correct group and permissions. </p>
<p> Default value is empty, not changing the user after starting.</dl>
<p> <code>run_as_group</code></p>
<dl>
<dd>After correctly starting, the gateway process will become this group, dropping root privileges. </p>
<p> Default value is empty, not changing the group after starting.</dl>
<p> <code>pid_file</code></p>
<dl>
<dd>Write the process ID number to this file. This is used by the init.d script to correctly stop/restart the service. </p>
<p> Default: <i>/var/run/zarafa-gateway.pid</i></dl>
<p> <code>running_path</code></p>
<dl>
<dd>Change directory to this path when running in daemonize mode. When using the -F switch to run in the foreground the directory will not be changed. </p>
<p> Default: <i>/</i></dl>
<p> <code>process_model</code></p>
<dl>
<dd>You can change the process model between <i>fork</i> and <i>thread</i>. The forked model uses somewhat more resources, but if a crash is triggered, this will only affect one user. In the threaded model, a crash means all users are affected, and will not be able to use the service. </p>
<p> Default: <i>fork</i></dl>
<p> <code>imap_only_mailfolders</code></p>
<dl>
<dd>Enable the IMAP and IMAPS service to only show the mailfolders. This is the default behaviour. When this option is set to &#8216;no&#8217;, you will also be able to select you calendar and contacts and such. These views will not contain all information, since these items cannot be converted to a rfc-822 mail item. </p>
<p> Default: <i>yes</i></dl>
<p> <code>imap_public_folders</code></p>
<dl>
<dd>Enable the IMAP and IMAPS service to also show the public store with subfolders. This is the default behaviour. When this option is set to &#8216;no&#8217;, IMAP clients will only see the users&#8217; folder. </p>
<p> Default: <i>yes</i></dl>
<p> <code>imap_capability_idle</code></p>
<dl>
<dd>Allow IMAP clients to issue the IDLE command. When an IMAP client is idle, it may receive notifications from the server about changes of the selected folder. This may increase load on the server when many users are using the IMAP service. </p>
<p> Default: <i>yes</i></dl>
<p> <code>imap_generate_utf8</code></p>
<dl>
<dd>Normally e-mails specify the correct charset for their contents. This may be altered to make it always UTF-8. This will only happen on e-mails that do not have the extra imap data properties, which is true for users without the &#8216;imap&#8217; feature enabled. </p>
<p> Default: <i>no</i></dl>
<p> <code>imap_max_messagesize</code></p>
<dl>
<dd>Limit the maximum message size (in bytes) which can be created by an IMAP client. The maximum of this value is 4GB although this is not recommended. If the value is too high it will cause a segmentation fault. This value may contain a k, m or g multiplier. </p>
<p> Default: <i>128M</i></dl>
<p> <code>imap_expunge_on_delete</code></p>
<dl>
<dd>Normally when you delete an e-mail in an IMAP client, it will only be marked as deleted, and not removed from the folder. The client should send the EXPUNGE command to actually remove the item from the folder (where Zarafa will place it in the soft-delete system). When this option is set to <i>yes</i>, the zarafa-gateway will issue the expunge command itself directly after a &#8216;mark as delete&#8217; command was received. </p>
<p> Default: <i>no</i></dl>
<p> <code>imap_store_rfc822</code></p>
<dl>
<dd>Store the rfc822 data with the message in MAPI. The Zarafa Gateway stores the original rfc822 data of an APPENDed message in the database for later retrieval. This makes sure that the exact message that was delivered into the Zarafa gateway is available for retrieval later, which is the behaviour when set to <i>yes</i>. If set to no, the zarafa-gateway will not store the original rfc822 text. This means that the rfc822 data must be re-created when retrieved. This may cause changes in encoding or charset and some loss of fidelity. This will also invalidate any signatures in the stored messages. </p>
<p> Default: <i>yes</i></dl>
<p> <code>imap_max_fail_commands</code></p>
<dl>
<dd>Maximum of failed commands before forcibly closing connection of client. This makes sure that a client which does repeatedly fails on a specific connection (like opening folders over and over again which do not exist) does not affect the overall performance of the gateway process. With the default value set to <i>10</i>, normal operation will work for most productionenvironments. With IMAP migrations, this value should be set higher as many traditional IMAP migration tools try to fetch folders which do not necessarily exist before, so in a migration scenario this value should be set higher, at minimum to the number of folders to be migrated from the largest mailbox. </p>
<p> Default: <i>10</i></dl>
<p> <code>disable_plaintext_auth</code></p>
<dl>
<dd>Disable all plaintext POP3 and IMAP authentications unless SSL/TLS is used (except for connections originating from <i>127.0.0.1</i> to allow saslauthd with rimap). Obviously enabling this configuration option requires at least <i>ssl_private_key_file</i> and <i>ssl_certificate_file</i> to take effect. </p>
<p> Default: <i>no</i></dl>
<p> <code>ssl_private_key_file</code></p>
<dl>
<dd>The gateway will use this file as private key for SSL TLS. This file can be created with: <code>openssl genrsa -out /etc/zarafa/gateway/privkey.pem 2048</code>. </p>
<p> Default: <i>/etc/zarafa/gateway/privkey.pem</i></dl>
<p> <code>ssl_certificate_file</code></p>
<dl>
<dd>The gateway will use this file as certificate for SSL TLS. A self-signed certificate can be created with: <code>openssl req -new -x509 -key /etc/zarafa/gateway/privkey.pem -out /etc/zarafa/gateway/cert.pem -days 1095</code>. </p>
<p> Default: <i>/etc/zarafa/gateway/cert.pem</i></dl>
<p> <code>ssl_verify_client</code></p>
<dl>
<dd>Enable client certificate verification with value yes. All other values disable the verification. </p>
<p> Default: <i>no</i></dl>
<p> <code>ssl_verify_file</code></p>
<dl>
<dd>The file to verify the clients certificates with. </p>
<p> Default: value not set.</dl>
<p> <code>ssl_verify_path</code></p>
<dl>
<dd>The path with the files to verify the clients certificates with. </p>
<p> Default: value not set.</dl>
<p> <code>ssl_protocols</code></p>
<dl>
<dd>Disabled or enabled protocol names. Supported protocol names are <i>SSLv2</i>, <i>SSLv3</i> and <i>TLSv1</i>. If Zarafa was linked against OpenSSL 1.0.1 or later there is additional support for the new protocols <i>TLSv1.1</i> and <i>TLSv1.2</i>. To exclude both, SSLv2 and SSLv3 set <code>ssl_protocols</code> to <i>!SSLv2 !SSLv3</i>. SSLv2 is considered unsafe and these connections should not be accepted. </p>
<p> Default: <i>!SSLv2</i></dl>
<p> <code>ssl_ciphers</code></p>
<dl>
<dd>SSL ciphers to use, set to <i>ALL</i> for backward compatibility. </p>
<p> Default: <i>ALL:!LOW:!SSLv2:!EXP:!aNULL</i></dl>
<p> <code>ssl_prefer_server_ciphers</code></p>
<dl>
<dd>Prefer the server&#8217;s order of SSL ciphers over client&#8217;s. </p>
<p> Default: <i>no</i></dl>
<p> <code>log_method</code></p>
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
<p> Default: <i>/var/log/zarafa/gateway.log</i></dl>
<p> <code>log_level</code></p>
<dl>
<dd>The level of output for logging in the range from 0 to 5. 0=no logging, 5=full logging. </p>
<p> Default: <i>2</i></dl>
<p> <code>log_timestamp</code></p>
<dl>
<dd>Specify whether to prefix each log line with a timestamp in &#8216;file&#8217; logging mode. </p>
<p> Default: <i>1</i></dl>
<h2>Reloading</h2>
<p>The following options are reloadable by sending the zarafa-gateway process a HUP signal: </p>
<p> log_level</p>
<dl>
<dd></dl>
<h2>Files</h2>
<p>/etc/zarafa/gateway.cfg</p>
<dl>
<dd>The Zarafa gateway configuration file.</dl>
<h2>Author</h2>
<p>Written by Zarafa.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-zarafa-gateway/">zarafa-gateway</a></code>(1) </p>
