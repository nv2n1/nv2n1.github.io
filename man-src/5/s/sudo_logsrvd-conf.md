---
title: "sudo_logsrvd-conf(5)"
name: "sudo_logsrvd-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sudo_logsrvd-conf/"
description: "sudo_logsrvd.conf – configuration for sudo_logsrvd"
---

<p>Sudo 1.9.9</p>
<h2>Name</h2>
<p><code>sudo_logsrvd.conf</code> &#8211; configuration for sudo_logsrvd</p>
<h2>Description</h2>
<p>The <code>sudo_logsrvd.conf</code> file is used to configure the <code>sudo_logsrvd</code> log server. It uses an INI-style format made up of sections in square brackets and &#8220;key = value&#8221; pairs specific to each section below the section name. Depending on the key, values may be integers, booleans, or strings. Section and key names are not case sensitive, but values are. The pound sign (`#&#8217; ) is used to indicate a comment. Both the comment character and any text after it, up to the end of the line, are ignored. Lines beginning with a semi-colon (`;&#8217; ) are also ignored. Long lines can be continued with a backslash (`\&#8217; ) as the last character on the line. Note that leading white space is removed from the beginning of lines even when the continuation character is used. The Sx EXAMPLES section contains a copy of the default <code>sudo_logsrvd.conf</code> file. The following configuration sections are recognized:  </p>
<li> server
<li> relay
<li> iolog
<li> eventlog
<li> syslog
<li> logfile </ul>
<p> Each section is described in detail below.</p>
<h3>server</h3>
<p>The <i>server</i> section configures the address and port the server will listen on. The following keys are recognized:</p>
<dl>
<dt><code>listen_address = host </code>[: <code>port </code>[(tls)] ]</p>
<dd>The host name or IP address, optional port to listen on and an optional Transport Layer Security (TLS) flag in parentheses. The host may be a host name, an IPv4 address, an IPv6 address in square brackets or the wild card entry `*&#8217; A host setting of `*&#8217; will cause <code>sudo_logsrvd</code> to listen on all configured network interfaces. If the optional tls flag is present, <code>sudo_logsrvd</code> will secure the connection with TLS version 1.2 or 1.3. Versions of TLS prior to 1.2 are not supported. See sudo_logsrvd8 for details on generating TLS keys and certificates. If a port is specified, it may either be a port number or a known service name as defined by the system service name database. If no port is specified, port 30343 will be used for plaintext connections and port 30344 will be used for TLS connections. The default value is: </p>
<blockquote>
<pre>listen_address = *:30343
listen_address = *:30344(tls)</pre>
</blockquote>
<p> which will listen on all configured network interfaces for both plaintext and TLS connections. Multiple <i>listen_address</i> lines may be specified to listen on more than one port or interface.</p>
<dt><code>server_log = string</code></p>
<dd>Where to log server warning and error messages. Supported values are <i>none</i> <i>stderr</i> <i>syslog</i> or a path name beginning with the `/&#8217; character. Note that a value of <i>stderr</i> is only effective when used in conjunction with the &#8211;<code>n</code> option. The default value is <i>syslog</i></p>
<dt><code>pid_file = path</code></p>
<dd>The path to the file containing the process ID of the running <code>sudo_logsrvd</code> If set to an empty value, or if <code>sudo_logsrvd</code> is run with the &#8211;<code>n</code> option, no <i>pid_file</i> will be created. If <i>pid_file</i> refers to a symbolic link, it will be ignored. The default value is /run/sudo/sudo_logsrvd.pid</p>
<dt><code>tcp_keepalive = boolean</code></p>
<dd>If true, <code>sudo_logsrvd</code> will enable the TCP keepalive socket option on the client connection. This enables the periodic transmission of keepalive messages to the client. If the client does not respond to a message in time, the connection will be closed. Defaults to true.</p>
<dt><code>timeout = number</code></p>
<dd>The amount of time, in seconds, <code>sudo_logsrvd</code> will wait for the client to respond. A value of 0 will disable the timeout. The default value is 30.</p>
<dt><code>tls_cacert = path</code></p>
<dd>The path to a certificate authority bundle file, in PEM format, to use instead of the system&#8217;s default certificate authority database when authenticating clients. The default is to use /etc/ssl/sudo/cacert.pem if it exists, otherwise the system&#8217;s default certificate authority database is used.</p>
<dt><code>tls_cert = path</code></p>
<dd>The path to the server&#8217;s certificate file, in PEM format. The default value is /etc/ssl/sudo/certs/logsrvd_cert.pem</p>
<dt><code>tls_checkpeer = bool</code></p>
<dd>If true, client certificates will be validated by <code>sudo_logsrvd</code> clients without a valid certificate will be unable to connect. If false, no validation of client certificates will be performed. It true and client certificates are created using a private certificate authority, the <i>tls_cacert</i> setting must be set to a CA bundle that contains the CA certificate used to generate the client certificate. The default value is <code>false</code></p>
<dt><code>tls_ciphers_v12 = string</code></p>
<dd>A list of ciphers to use for connections secured by TLS version 1.2 only, separated by a colon `:&#8217; See the Sx CIPHER LIST FORMAT section in openssl-ciphers1 for full details. The default value is <code>HIGH:!aNULL</code> which consists of encryption cipher suites with key lengths larger than 128 bits, and some cipher suites with 128-bit keys. Cipher suites that offer no authentication are excluded.</p>
<dt><code>tls_ciphers_v13 = string</code></p>
<dd>A list of ciphers to use for connections secured by TLS version 1.3 only, separated by a colon `:&#8217; Supported cipher suites depend on the version of OpenSSL used, but should include the following: </p>
<dt><code>TLS_AES_128_GCM_SHA256</code></p>
<dd>
<dt><code>TLS_AES_256_GCM_SHA384</code></p>
<dd>
<dt><code>TLS_CHACHA20_POLY1305_SHA256</code></p>
<dd>
<dt><code>TLS_AES_128_CCM_SHA256</code></p>
<dd>
<dt><code>TLS_AES_128_CCM_8_SHA256</code></p>
<dd></dl>
<p> The default cipher suite is TLS_AES_256_GCM_SHA384.</p>
<dt><code>tls_dhparams = path</code></p>
<dd>The path to a file containing custom Diffie-Hellman parameters in PEM format. This file can be created with the following command: </p>
<pre>openssl dhparam -out /etc/sudo_logsrvd_dhparams.pem 2048</pre>
<p>By default, <code>sudo_logsrvd</code> will use the OpenSSL defaults for Diffie-Hellman key generation.</p>
<dt><code>tls_key = path</code></p>
<dd>The path to the server&#8217;s private key file, in PEM format. The default value is /etc/ssl/sudo/private/logsrvd_key.pem</p>
<dt><code>tls_verify = bool</code></p>
<dd>If true, <code>sudo_logsrvd.conf</code> will validate its own certificate at startup time or when the configuration is changed. If false, no verification is performed of the server certificate. When using self-signed certificates without a certificate authority, this setting should be set to false. The default value is true.</dl>
<h3>relay</h3>
<p>The <i>relay</i> section configures the optional logsrv relay host and port the server will connect to. The TLS configuration keys are optional, by default the corresponding keys in the Sx server section will be used. They are only present in this section to make it possible for the relay connection to use a different set of TLS parameters from the client-facing server. The following keys are recognized:</p>
<dl>
<dt><code>connect_timeout = number</code></p>
<dd>The amount of time, in seconds, <code>sudo_logsrvd</code> will wait for the connection to a <i>relay_host</i> (see below) to complete. Once the connection is complete, the <i>timeout</i> setting controls the amount of time <code>sudo_logsrvd</code> will wait for the relay to respond. A value of 0 will disable the timeout. The default value is 30.</p>
<dt><code>relay_dir = path</code></p>
<dd>The directory in which log messages are temporarily stored before they are sent to the relay host. Messages are stored in the wire format specified by sudo_logsrv.proto5 The default value is /var/log/sudo_logsrvd</p>
<dt><code>relay_host = host </code>[: <code>port </code>[(tls)] ]</p>
<dd>The relay host name or IP address, optional port to connect to and an optional Transport Layer Security (TLS) flag in parentheses. The syntax is identical to <i>listen_address</i> in the Sx server section with one exception: the wild card `*&#8217; syntax is not supported. When this setting is enabled, messages from the client will be forwarded to one of the specified relay hosts instead of being stored locally. The <i>host</i> could be running an instance of <code>sudo_logsrvd</code> or another server that supports the sudo_logsrv.proto5 protocol. If multiple <i>relay_host</i> lines are specified, the first available relay host will be used.</p>
<dt><code>retry_interval = number</code></p>
<dd>The number of seconds to wait after a connection error before making a new attempt to forward a message to a relay host. The default value is 30 seconds.</p>
<dt><code>store_first = boolean</code></p>
<dd>If true, <code>sudo_logsrvd</code> will store logs locally before relaying them. Once the log is complete, a connection to the relay host is opened and the log is relayed. If the network connection is interrupted before the log can be fully transferred, it will be retransmitted later. The default is to relay logs in real-time.</p>
<dt><code>tcp_keepalive = boolean</code></p>
<dd>If true, <code>sudo_logsrvd</code> will enable the TCP keepalive socket option on the relay connection. This enables the periodic transmission of keepalive messages to the relay server. If the relay does not respond to a message in time, the connection will be closed.</p>
<dt><code>timeout = number</code></p>
<dd>The amount of time, in seconds, <code>sudo_logsrvd</code> will wait for the relay server to respond after a connection has succeeded. A value of 0 will disable the timeout. The default value is 30.</p>
<dt><code>tls_cacert = path</code></p>
<dd>The path to a certificate authority bundle file, in PEM format, to use instead of the system&#8217;s default certificate authority database when authenticating clients. The default is to use the value specified in the Sx server section, or the system&#8217;s default certificate authority database if no value is set.</p>
<dt><code>tls_cert = path</code></p>
<dd>The path to the server&#8217;s certificate file, in PEM format. The default is to use the value specified in the Sx server section.</p>
<dt><code>tls_checkpeer = bool</code></p>
<dd>If true, the relay host&#8217;s certificate will be validated by <code>sudo_logsrvd</code> connections to a relay without a valid certificate will fail. If false, no validation of relay certificates will be performed. It true and relay certificates are created using a private certificate authority, the <i>tls_cacert</i> setting must be set to a CA bundle that contains the CA certificate used to generate the relay certificate. The default is to use the value specified in the Sx server section.</p>
<dt><code>tls_ciphers_v12 = string</code></p>
<dd>A list of ciphers to use for connections secured by TLS version 1.2 only, separated by a colon `:&#8217; See the Sx CIPHER LIST FORMAT section in openssl-ciphers1 for full details. The default is to use the value specified in the Sx server section.</p>
<dt><code>tls_ciphers_v13 = string</code></p>
<dd>A list of ciphers to use for connections secured by TLS version 1.3 only, separated by a colon `:&#8217; Supported cipher suites depend on the version of OpenSSL used, see the Sx server section for more information. The default is to use the value specified in the Sx server section.</p>
<dt><code>tls_dhparams = path</code></p>
<dd>The path to a file containing custom Diffie-Hellman parameters in PEM format. The default is to use the value specified in the Sx server section.</p>
<dt><code>tls_key = path</code></p>
<dd>The path to the server&#8217;s private key file, in PEM format. The default is to use the value specified in the Sx server section.</p>
<dt><code>tls_verify = bool</code></p>
<dd>If true, the server&#8217;s certificate used for relaying will be verified at startup. If false, no verification is performed of the server certificate. When using self-signed certificates without a certificate authority, this setting should be set to false. The default is to use the value specified in the Sx server section.</dl>
<h3>iolog</h3>
<p>The <i>iolog</i> section configures I/O log parameters. These settings are identical to the I/O configuration in <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5). The following keys are recognized:</p>
<dl>
<dt><code>iolog_compress = boolean</code></p>
<dd>If set, I/O logs will be compressed using <code>zlib</code> Enabling compression can make it harder to view the logs in real-time as the program is executing due to buffering. The default value is <code>false</code></p>
<dt><code>iolog_dir = path</code></p>
<dd>The top-level directory to use when constructing the path name for the I/O log directory. The session sequence number, if any, is stored in the directory. The default value is /var/log/sudo-io The following percent (`%&#8217; ) escape sequences are supported:</p>
<dl>
<dt><code>%{seq}</code></p>
<dd>expanded to a monotonically increasing base-36 sequence number, such as 0100A5, where every two digits are used to form a new directory, e.g., 01/00/A5</p>
<dt><code>%{user}</code></p>
<dd>expanded to the invoking user&#8217;s login name</p>
<dt><code>%{group}</code></p>
<dd>expanded to the name of the invoking user&#8217;s real group-ID</p>
<dt><code>%{runas_user}</code></p>
<dd>expanded to the login name of the user the command will be run as (e.g., root)</p>
<dt><code>%{runas_group}</code></p>
<dd>expanded to the group name of the user the command will be run as (e.g., wheel)</p>
<dt><code>%{hostname}</code></p>
<dd>expanded to the local host name without the domain name</p>
<dt><code>%{command}</code></p>
<dd>expanded to the base name of the command being run</dl>
<p> In addition, any escape sequences supported by the system&#8217;s <a href="/docs/linux/man/3-strftime/">strftime</a>(3) function will be expanded. To include a literal `%&#8217; character, the string `%%&#8217; should be used.</p>
<dt><code>iolog_file = path</code></p>
<dd>The path name, relative to <i>iolog_dir</i> in which to store I/O logs. Note that <i>iolog_file</i> may contain directory components. The default value is <code>%{seq}</code> See the <i>iolog_dir</i> setting above for a list of supported percent (`%&#8217; ) escape sequences. In addition to the escape sequences, path names that end in six or more <code>X s</code> will have the <code>X s</code> replaced with a unique combination of digits and letters, similar to the <a href="/docs/linux/man/3-mktemp/">mktemp</a>(3) function. If the path created by concatenating <i>iolog_dir</i> and <i>iolog_file</i> already exists, the existing I/O log file will be truncated and overwritten unless <i>iolog_file</i> ends in six or more <code>X s</code></p>
<dt><code>iolog_flush = boolean</code></p>
<dd>If set, I/O log data is flushed to disk after each write instead of buffering it. This makes it possible to view the logs in real-time as the program is executing but may significantly reduce the effectiveness of I/O log compression. I/O logs are always flushed before sending a commit point to the client regardless of this setting. The default value is <code>true</code></p>
<dt><code>iolog_group = name</code></p>
<dd>The group name to look up when setting the group-ID on new I/O log files and directories. If <i>iolog_group</i> is not set, the primary group-ID of the user specified by <i>iolog_user is used.</i> If neither <i>iolog_group</i> nor <i>iolog_user</i> are set, I/O log files and directories are created with group-ID 0.</p>
<dt><code>iolog_mode = mode</code></p>
<dd>The file mode to use when creating I/O log files. Mode bits for read and write permissions for owner, group, or other are honored, everything else is ignored. The file permissions will always include the owner read and write bits, even if they are not present in the specified mode. When creating I/O log directories, search (execute) bits are added to match the read and write bits specified by <i>iolog_mode</i> The default value is <code>0600</code></p>
<dt><code>iolog_user = name</code></p>
<dd>The user name to look up when setting the owner of new I/O log files and directories. If <i>iolog_group</i> is set, it will be used instead of the user&#8217;s primary group-ID. By default, I/O log files and directories are created with user and group-ID 0.</p>
<dt><code>maxseq = number</code></p>
<dd>The maximum sequence number that will be substituted for the &#8220;<code>%{seq}</code> &#8221; escape in the I/O log file (see the <i>iolog_dir</i> description above for more information). While the value substituted for &#8220;<code>%{seq}</code> &#8221; is in base 36, <i>maxseq</i> itself should be expressed in decimal. Values larger than 2176782336 (which corresponds to the base 36 sequence number &#8220;ZZZZZZ&#8221; will be silently truncated to 2176782336. The default value is 2176782336.</dl>
<h3>eventlog</h3>
<p>The <i>eventlog</i> section configures how (and if) security policy events are logged.</p>
<dl>
<dt><code>log_type = string</code></p>
<dd>Where to log accept, reject, and alert events reported by the policy. Supported values are <i>syslog</i> <i>logfile</i> and <i>none</i> The default value is <i>syslog</i></p>
<dt><code>log_exit = boolean</code></p>
<dd>If true, <code>sudo_logsrvd</code> will log an event when a command exits or is terminated by a signal. Defaults to false.</p>
<dt><code>log_format = string</code></p>
<dd>The event log format. Supported log formats are &#8220;sudo&#8221; for traditional sudo-style logs and &#8220;json&#8221; for JSON-format logs. The JSON log entries contain the full contents of the accept, reject, exit and alert messages. The default value is <i>sudo</i></dl>
<h3>syslog</h3>
<p>The <i>syslog</i> section configures how events are logged via <a href="/docs/linux/man/3-syslog/">syslog</a>(3).</p>
<dl>
<dt><code>facility = string</code></p>
<dd>Syslog facility if syslog is being used for logging. Defaults to <code>authpriv</code> The following syslog facilities are supported: <code>authpriv</code> (if your OS supports it), <code>auth</code> <code>daemon</code> <code>user</code> <code>local0</code> <code>local1</code> <code>local2</code> <code>local3</code> <code>local4</code> <code>local5</code> <code>local6</code> and <code>local7</code></p>
<dt><code>accept_priority = string</code></p>
<dd>Syslog priority to use when the user is allowed to run a command and authentication is successful. Defaults to <code>notice</code> The following syslog priorities are supported: <code>alert</code> <code>crit</code> <code>debug</code> <code>emerg</code> <code>err</code> <code>info</code> <code>notice</code> <code>warning</code> and <code>none</code> Setting it to a value of <code>none</code> will disable logging of successful commands.</p>
<dt><code>reject_priority = string</code></p>
<dd>Syslog priority to use when the user is not allowed to run a command or when authentication is unsuccessful. Defaults to <code>alert</code> See <i>accept_priority</i> for the list of supported syslog priorities.</p>
<dt><code>alert_priority = string</code></p>
<dd>Syslog priority to use for event log alert messages received from the client. Defaults to <code>alert</code> See <i>accept_priority</i> for the list of supported syslog priorities.</p>
<dt><code>maxlen = number</code></p>
<dd>On many systems, <a href="/docs/linux/man/3-syslog/">syslog</a>(3) has a relatively small log buffer. IETF RFC 5424 states that syslog servers must support messages of at least 480 bytes and should support messages up to 2048 bytes. By default, <code>sudo_logsrvd</code> creates log messages up to 960 bytes which corresponds to the historic BSD syslog implementation which used a 1024 byte buffer to store the message, date, hostname, and program name. To prevent syslog messages from being truncated, <code>sudo_logsrvd</code> will split up sudo-style log messages that are larger than <i>maxlen</i> bytes. When a message is split, additional parts will include the string &#8220;(command continued) &#8221; after the user name and before the continued command line arguments. JSON-format log entries are never split and are not affected by <i>maxlen</i></p>
<dt><code>server_facility = string</code></p>
<dd>Syslog facility if syslog is being used for server warning messages. See above for a list of supported facilities. Defaults to <code>daemon</code></dl>
<h3>logfile</h3>
<p>The <i>logfile</i> section consists of settings related to logging to a plain file (not syslog).</p>
<dl>
<dt><code>path = string</code></p>
<dd>The path to the file-based event log. This path must be fully-qualified and start with a `/&#8217; character. The default value is /var/log/sudo.log</p>
<dt><code>time_format = string</code></p>
<dd>The string used when formatting the date and time for file-based event logs. Formatting is performed via the system&#8217;s <a href="/docs/linux/man/3-strftime/">strftime</a>(3) function so any escape sequences supported by that function will be expanded. The default value is &#8220;<code>%h %e %T</code> &#8221; which produces dates like &#8220;Oct 3 07:15:24&#8221; in the C locale.</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/sudo_logsrvd.conf </code></p>
<dd>Sudo log server configuration file</dl>
<h2>Examples</h2>
<pre>#
# sudo logsrv daemon configuration
#
[server]
# The host name or IP address and port to listen on with an optional TLS
# flag. If no port is specified, port 30343 will be used for plaintext
# connections and port 30344 will be used to TLS connections.
# The following forms are accepted:
# listen_address = hostname(tls)
# listen_address = hostname:port(tls)
# listen_address = IPv4_address(tls)
# listen_address = IPv4_address:port(tls)
# listen_address = [IPv6_address](tls)
# listen_address = [IPv6_address]:port(tls)
#
# The (tls) suffix should be omitted for plaintext connections.
#
# Multiple listen_address settings may be specified.
# The default is to listen on all addresses.
#listen_address = *:30343
#listen_address = *:30344(tls)
# The file containing the ID of the running sudo_logsrvd process.
#pid_file = /run/sudo/sudo_logsrvd.pid
# Where to log server warnings: none, stderr, syslog, or a path name.
#server_log = syslog
# If true, enable the SO_KEEPALIVE socket option on client connections.
# Defaults to true.
#tcp_keepalive = true
# The amount of time, in seconds, the server will wait for the client to
# respond. A value of 0 will disable the timeout. The default value is 30.
#timeout = 30
# If true, the server will validate its own certificate at startup.
# Defaults to true.
#tls_verify = true
# If true, client certificates will be validated by the server;
# clients without a valid certificate will be unable to connect.
# By default, client certs are not checked.
#tls_checkpeer = false
# Path to a certificate authority bundle file in PEM format to use
# instead of the system's default certificate authority database.
#tls_cacert = /etc/ssl/sudo/cacert.pem
# Path to the server's certificate file in PEM format.
# Required for TLS connections.
#tls_cert = /etc/ssl/sudo/certs/logsrvd_cert.pem
# Path to the server's private key file in PEM format.
# Required for TLS connections.
#tls_key = /etc/ssl/sudo/private/logsrvd_key.pem
# TLS cipher list (see &quot;CIPHER LIST FORMAT&quot; in the openssl-ciphers manual).
# NOTE that this setting is only effective if the negotiated protocol
# is TLS version 1.2.
# The default cipher list is HIGH:!aNULL.
#tls_ciphers_v12 = HIGH:!aNULL
# TLS cipher list if the negotiated protocol is TLS version 1.3.
# The default cipher list is TLS_AES_256_GCM_SHA384.
#tls_ciphers_v13 = TLS_AES_256_GCM_SHA384
# Path to the Diffie-Hellman parameter file in PEM format.
# If not set, the server will use the OpenSSL defaults.
#tls_dhparams = /etc/ssl/sudo/logsrvd_dhparams.pem
[relay]
# The host name or IP address and port to send logs to in relay mode.
# The syntax is identical to listen_address with the exception of
# the wild card ('*') syntax. When this setting is enabled, logs will
# be relayed to the specified host instead of being stored locally.
# This setting is not enabled by default.
#relay_host = relayhost.dom.ain
#relay_host = relayhost.dom.ain(tls)
# The amount of time, in seconds, the server will wait for a connection
# to the relay server to complete. A value of 0 will disable the timeout.
# The default value is 30.
#connect_timeout = 30
# The directory to store messages in before they are sent to the relay.
# Messages are stored in wire format.
# The default value is /var/log/sudo_logsrvd.
#relay_dir = /var/log/sudo_logsrvd
# The number of seconds to wait after a connection error before
# making a new attempt to forward a message to a relay host.
# The default value is 30.
#retry_interval = 30
# Whether to store the log before relaying it. If true, enable store
# and forward mode. If false, the client connection is immediately
# relayed. Defaults to false.
#store_first = true
# If true, enable the SO_KEEPALIVE socket option on relay connections.
# Defaults to true.
#tcp_keepalive = true
# The amount of time, in seconds, the server will wait for the relay to
# respond. A value of 0 will disable the timeout. The default value is 30.
#timeout = 30
# If true, the server's relay certificate will be verified at startup.
# The default is to use the value in the [server] section.
#tls_verify = true
# Whether to verify the relay's certificate for TLS connections.
# The default is to use the value in the [server] section.
#tls_checkpeer = false
# Path to a certificate authority bundle file in PEM format to use
# instead of the system's default certificate authority database.
# The default is to use the value in the [server] section.
#tls_cacert = /etc/ssl/sudo/cacert.pem
# Path to the server's certificate file in PEM format.
# The default is to use the certificate in the [server] section.
#tls_cert = /etc/ssl/sudo/certs/logsrvd_cert.pem
# Path to the server's private key file in PEM format.
# The default is to use the key in the [server] section.
#tls_key = /etc/ssl/sudo/private/logsrvd_key.pem
# TLS cipher list (see &quot;CIPHER LIST FORMAT&quot; in the openssl-ciphers manual).
# NOTE that this setting is only effective if the negotiated protocol
# is TLS version 1.2.
# The default is to use the value in the [server] section.
#tls_ciphers_v12 = HIGH:!aNULL
# TLS cipher list if the negotiated protocol is TLS version 1.3.
# The default is to use the value in the [server] section.
#tls_ciphers_v13 = TLS_AES_256_GCM_SHA384
# Path to the Diffie-Hellman parameter file in PEM format.
# The default is to use the value in the [server] section.
#tls_dhparams = /etc/ssl/sudo/logsrvd_dhparams.pem
[iolog]
# The top-level directory to use when constructing the path name for the
# I/O log directory. The session sequence number, if any, is stored here.
#iolog_dir = /var/log/sudo-io
# The path name, relative to iolog_dir, in which to store I/O logs.
# Note that iolog_file may contain directory components.
#iolog_file = %{seq}
# If set, I/O logs will be compressed using zlib. Enabling compression can
# make it harder to view the logs in real-time as the program is executing.
#iolog_compress = false
# If set, I/O log data is flushed to disk after each write instead of
# buffering it. This makes it possible to view the logs in real-time
# as the program is executing but reduces the effectiveness of compression.
#iolog_flush = true
# The group to use when creating new I/O log files and directories.
# If iolog_group is not set, the primary group-ID of the user specified
# by iolog_user is used. If neither iolog_group nor iolog_user
# are set, I/O log files and directories are created with group-ID 0.
#iolog_group = wheel
# The user to use when setting the user-ID and group-ID of new I/O
# log files and directories. If iolog_group is set, it will be used
# instead of the user's primary group-ID. By default, I/O log files
# and directories are created with user and group-ID 0.
#iolog_user = root
# The file mode to use when creating I/O log files. The file permissions
# will always include the owner read and write bits, even if they are
# not present in the specified mode. When creating I/O log directories,
# search (execute) bits are added to match the read and write bits
# specified by iolog_mode.
#iolog_mode = 0600
# The maximum sequence number that will be substituted for the &quot;%{seq}&quot;
# escape in the I/O log file. While the value substituted for &quot;%{seq}&quot;
# is in base 36, maxseq itself should be expressed in decimal. Values
# larger than 2176782336 (which corresponds to the base 36 sequence
# number &quot;ZZZZZZ&quot;) will be silently truncated to 2176782336.
#maxseq = 2176782336
[eventlog]
# Where to log accept, reject, exit, and alert events.
# Accepted values are syslog, logfile, or none.
# Defaults to syslog
#log_type = syslog
# Whether to log an event when a command exits or is terminated by a signal.
# Defaults to false
#log_exit = true
# Event log format.
# Currently only sudo-style event logs are supported.
#log_format = sudo
[syslog]
# The maximum length of a syslog payload.
# On many systems, <a href="//www.systutorials.com/docs/linux/man/3-syslog/">syslog</a>(3) has a relatively small log buffer.
# IETF RFC 5424 states that syslog servers must support messages
# of at least 480 bytes and should support messages up to 2048 bytes.
# Messages larger than this value will be split into multiple messages.
#maxlen = 960
# The syslog facility to use for event log messages.
# The following syslog facilities are supported: authpriv (if your OS
# supports it), auth, daemon, user, local0, local1, local2, local3,
# local4, local5, local6, and local7.
#facility = authpriv
# Syslog priority to use for event log accept messages, when the command
# is allowed by the security policy. The following syslog priorities are
# supported: alert, crit, debug, emerg, err, info, notice, warning, none.
#accept_priority = notice
# Syslog priority to use for event log reject messages, when the command
# is not allowed by the security policy.
#reject_priority = alert
# Syslog priority to use for event log alert messages reported by the
# client.
#alert_priority = alert
# The syslog facility to use for server warning messages.
# Defaults to daemon.
#server_facility = daemon
[logfile]
# The path to the file-based event log.
# This path must be fully-qualified and start with a '/' character.
#path = /var/log/sudo
# The format string used when formatting the date and time for
# file-based event logs. Formatting is performed via <a href="//www.systutorials.com/docs/linux/man/3-strftime/">strftime</a>(3) so
# any format string supported by that function is allowed.
#time_format = %h %e %T</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-strftime/">strftime</a>(3), sudo.conf5, <a href="/docs/linux/man/5-sudoers/">sudoers</a>(5), <a href="/docs/linux/man/8-sudo/">sudo</a>(8), sudo_logsrvd8</p>
<h2>History</h2>
<p>See the HISTORY file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/history.html)">https://www.sudo.ws/history.html)</a> for a brief history of sudo.</p>
<h2>Authors</h2>
<p>Many people have worked on <code>sudo</code> over the years; this version consists of code written primarily by: </p>
<blockquote><p> An Todd C. Miller </p></blockquote>
<p> See the CONTRIBUTORS file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/contributors.html)">https://www.sudo.ws/contributors.html)</a> for an exhaustive list of people who have contributed to <code>sudo</code></p>
<h2>Bugs</h2>
<p>If you feel you have found a bug in <code>sudo</code> please submit a bug report at <a rel="nofollow" href="https://bugzilla.sudo.ws/">https://bugzilla.sudo.ws/</a></p>
<h2>Support</h2>
<p>Limited free support is available via the sudo-users mailing list, see <a rel="nofollow" href="https://www.sudo.ws/mailman/listinfo/sudo-users">https://www.sudo.ws/mailman/listinfo/sudo-users</a> to subscribe or search the archives.</p>
<h2>Disclaimer</h2>
<p><code>sudo</code> is provided &#8220;AS IS&#8221; and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. See the LICENSE file distributed with <code>sudo</code> or <a rel="nofollow" href="https://www.sudo.ws/license.html">https://www.sudo.ws/license.html</a> for complete details.</p>
