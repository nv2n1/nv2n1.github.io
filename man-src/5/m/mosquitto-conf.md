---
title: "mosquitto-conf(5)"
name: "mosquitto-conf"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mosquitto-conf/"
description: "mosquitto.conf – the configuration file for mosquitto"
---

<p>mosquitto.conf &#8211; the configuration file for mosquitto</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>mosquitto.conf</code></dl>
<h2>Description</h2>
<p><code>mosquitto.conf</code></p>
<dd>is the configuration file for mosquitto. This file can reside anywhere as long as mosquitto can read it. By default, mosquitto does not need a configuration file and will use the default values listed below. See <code><a href="/docs/linux/man/8-mosquitto/">mosquitto</a></code>(8) for information on how to load a configuration file.</p>
<h2>File Format</h2>
<p>All lines with a # as the very first character are treated as a comment. </p>
<p> Configuration lines start with a variable name. The variable value is separated from the name by a single space.</p>
<h2>Authentication</h2>
<p>The authentication options described below allow a wide range of possibilities in conjunction with the listener options. This section aims to clarify the possibilities. </p>
<p> The simplest option is to have no authentication at all. This is the default if no other options are given. Unauthenticated encrypted support is provided by using the certificate based SSL/TLS based options cafile/capath, certfile and keyfile. </p>
<p> MQTT provides username/password authentication as part of the protocol. Use the password_file option to define the valid usernames and passwords. Be sure to use network encryption if you are using this option otherwise the username and password will be vulnerable to interception. </p>
<p> When using certificate based encryption there are two options that affect authentication. The first is require_certificate, which may be set to true or false. If false, the SSL/TLS component of the client will verify the server but there is no requirement for the client to provide anything for the server: authentication is limited to the MQTT built in username/password. If require_certificate is true, the client must provide a valid certificate in order to connect successfully. In this case, the second option, use_identity_as_username, becomes relevant. If set to true, the Common Name (CN) from the client certificate is used instead of the MQTT username for access control purposes. The password is not replaced because it is assumed that only authenticated clients have valid certificates. If use_identity_as_username is false, the client must authenticate as normal (if required by password_file) through the MQTT options. </p>
<p> When using pre-shared-key based encryption through the psk_hint and psk_file options, the client must provide a valid identity and key in order to connect to the broker before any MQTT communication takes place. If use_identity_as_username is true, the PSK identity is used instead of the MQTT username for access control purposes. If use_identity_as_username is false, the client may still authenticate using the MQTT username/password if using the password_file option. </p>
<p> Both certificate and PSK based encryption are configured on a per-listener basis. </p>
<p> Authentication plugins can be created to replace the password_file and psk_file options (as well as the ACL options) with e.g. SQL based lookups. </p>
<p> It is possible to support multiple authentication schemes at once. A config could be created that had a listener for all of the different encryption options described above and hence a large number of ways of authenticating.</p>
<h2>General Options</h2>
<p><code>acl_file</code> <i>file path</i></p>
<dl>
<dd>Set the path to an access control list file. If defined, the contents of the file are used to control client access to topics on the broker. </p>
<p> If this parameter is defined then only the topics listed will have access. Topic access is added with lines of the format: </p>
<p> topic [read|write|readwrite] &lt;topic&gt; </p>
<p> The access type is controlled using &quot;read&quot;, &quot;write&quot; or &quot;readwrite&quot;. This parameter is optional (unless &lt;topic&gt; includes a space character) &#8211; if not given then the access is read/write. &lt;topic&gt; can contain the + or # wildcards as in subscriptions. </p>
<p> The first set of topics are applied to anonymous clients, assuming <code>allow_anonymous</code> is true. User specific topic ACLs are added after a user line as follows: </p>
<p> user &lt;username&gt; </p>
<p> The username referred to here is the same as in <code>password_fil</code>e. It is not the clientid. </p>
<p> It is also possible to define ACLs based on pattern substitution within the topic. The form is the same as for the topic keyword, but using pattern as the keyword. </p>
<p> pattern [read|write|readwrite] &lt;topic&gt; </p>
<p> The patterns available for substition are: </p>
<dl>
<dd>&bull; %c to match the client id of the client</dl>
<dl>
<dd>&bull; %u to match the username of the client</dl>
<p> The substitution pattern must be the only text for that level of hierarchy. Pattern ACLs apply to all users even if the &quot;user&quot; keyword has previously been given. </p>
<p> Example: </p>
<p> pattern write sensor/%u/data </p>
<p> Allow access for bridge connection messages: </p>
<p> pattern write $SYS/broker/connection/%c/state </p>
<p> If the first character of a line of the ACL file is a # it is treated as a comment. </p>
<p> Reloaded on reload signal. The currently loaded ACLs will be freed and reloaded. Existing subscriptions will be affected after the reload.</dl>
<p> <code>allow_anonymous</code> [ true | false ]</p>
<dl>
<dd>Boolean value that determines whether clients that connect without providing a username are allowed to connect. If set to <i>false</i> then another means of connection should be created to control authenticated client access. Defaults to <i>true</i>. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>allow_duplicate_messages</code> [ true | false ]</p>
<dl>
<dd>If a client is subscribed to multiple subscriptions that overlap, e.g. foo/# and foo/+/baz , then MQTT expects that when the broker receives a message on a topic that matches both subscriptions, such as foo/bar/baz, then the client should only receive the message once. </p>
<p> Mosquitto keeps track of which clients a message has been sent to in order to meet this requirement. This option allows this behaviour to be disabled, which may be useful if you have a large number of clients subscribed to the same set of topics and want to minimise memory usage. </p>
<p> It can be safely set to <i>true</i> if you know in advance that your clients will never have overlapping subscriptions, otherwise your clients must be able to correctly deal with duplicate messages even when then have QoS=2. </p>
<p> Defaults to <i>true</i>. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>auth_opt_*</code> <i>value</i></p>
<dl>
<dd>Options to be passed to the auth plugin. See the specific plugin instructions.</dl>
<p> <code>auth_plugin</code> <i>file path</i></p>
<dl>
<dd>Specify an external module to use for authentication and access control. This allows custom username/password and access control functions to be created. </p>
<p> Not currently reloaded on reload signal.</dl>
<p> <code>autosave_interval</code> <i>seconds</i></p>
<dl>
<dd>The number of seconds that mosquitto will wait between each time it saves the in-memory database to disk. If set to 0, the in-memory database will only be saved when mosquitto exits or when receiving the SIGUSR1 signal. Note that this setting only has an effect if persistence is enabled. Defaults to 1800 seconds (30 minutes). </p>
<p> Reloaded on reload signal.</dl>
<p> <code>autosave_on_changes</code> [ true | false ]</p>
<dl>
<dd>If <i>true</i>, mosquitto will count the number of subscription changes, retained messages received and queued messages and if the total exceeds <code>autosave_interval</code> then the in-memory database will be saved to disk. If <i>false</i>, mosquitto will save the in-memory database to disk by treating <code>autosave_interval</code> as a time in seconds. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>clientid_prefixes</code> <i>prefix</i></p>
<dl>
<dd>If defined, only clients that have a clientid with a prefix that matches clientid_prefixes will be allowed to connect to the broker. For example, setting &quot;secure-&quot; here would mean a client &quot;secure-client&quot; could connect but another with clientid &quot;mqtt&quot; couldn&#8217;t. By default, all client ids are valid. </p>
<p> Reloaded on reload signal. Note that currently connected clients will be unaffected by any changes.</dl>
<p> <code>connection_messages</code> [ true | false ]</p>
<dl>
<dd>If set to <i>true</i>, the log will include entries when clients connect and disconnect. If set to <i>false</i>, these entries will not appear. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>include_dir</code> <i>dir</i></p>
<dl>
<dd>External configuration files may be included by using the include_dir option. This defines a directory that will be searched for config files. All files that end in &#8216;.conf&#8217; will be loaded as a configuration file. It is best to have this as the last option in the main file. This option will only be processed from the main configuration file. The directory specified must not contain the main configuration file.</dl>
<p> <code>log_dest</code> <i>destinations</i></p>
<dl>
<dd>Send log messages to a particular destination. Possible destinations are: <code>stdout</code> <code>stderr</code> <code>syslog</code> <code>topic</code>. </p>
<p> <code>stdout</code> and <code>stderr</code> log to the console on the named output. </p>
<p> <code>syslog</code> uses the userspace syslog facility which usually ends up in /var/log/messages or similar and topic logs to the broker topic &#8216;$SYS/broker/log/&lt;severity&gt;&#8217;, where severity is one of D, E, W, N, I, M which are debug, error, warning, notice, information and message. Message type severity is used by the subscribe and unsubscribe log_type options and publishes log messages at $SYS/broker/log/M/subscribe and $SYS/broker/log/M/unsubscribe. </p>
<p> The <code>file</code> destination requires an additional parameter which is the file to be logged to, e.g. &quot;log_dest file /var/log/mosquitto.log&quot;. The file will be closed and reopened when the broker receives a HUP signal. Only a single file destination may be configured. </p>
<p> Use &quot;log_dest none&quot; if you wish to disable logging. Defaults to stderr. This option may be specified multiple times. </p>
<p> Note that if the broker is running as a Windows service it will default to &quot;log_dest none&quot; and neither stdout nor stderr logging is available. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>log_facility</code> <i>local facility</i></p>
<dl>
<dd>If using syslog logging (not on Windows), messages will be logged to the &quot;daemon&quot; facility by default. Use the <code>log_facility</code> option to choose which of local0 to local7 to log to instead. The option value should be an integer value, e.g. &quot;log_facility 5&quot; to use local5.</dl>
<p> <code>log_timestamp</code> [ true | false ]</p>
<dl>
<dd>Boolean value, if set to <i>true</i> a timestamp value will be added to each log entry. The default is <i>true</i>. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>log_type</code> <i>types</i></p>
<dl>
<dd>Choose types of messages to log. Possible types are: <i>debug</i>, <i>error</i>, <i>warning</i>, <i>notice</i>, <i>information</i>, <i>subscribe</i>, <i>unsubscribe</i>, <i>websockets</i>, <i>none</i>, <i>all</i>. </p>
<p> Defaults to <i>error</i>, <i>warning</i>, <i>notice </i>and <i>information</i>. This option may be specified multiple times. Note that the <i>debug </i>type (used for decoding incoming/outgoing network packets) is never logged in topics. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>max_inflight_messages</code> <i>count</i></p>
<dl>
<dd>The maximum number of QoS 1 or 2 messages that can be in the process of being transmitted simultaneously. This includes messages currently going through handshakes and messages that are being retried. Defaults to 20. Set to 0 for no maximum. If set to 1, this will guarantee in-order delivery of messages. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>max_queued_messages</code> <i>count</i></p>
<dl>
<dd>The maximum number of QoS 1 or 2 messages to hold in the queue above those messages that are currently in flight. Defaults to 100. Set to 0 for no maximum (not recommended). See also the <code>queue_qos0_messages</code> option. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>message_size_limit</code> <i>limit</i></p>
<dl>
<dd>This option sets the maximum publish payload size that the broker will allow. Received messages that exceed this size will not be accepted by the broker. The default value is 0, which means that all valid MQTT messages are accepted. MQTT imposes a maximum payload size of 268435455 bytes.</dl>
<p> <code>password_file</code> <i>file path</i></p>
<dl>
<dd>Set the path to a password file. If defined, the contents of the file are used to control client access to the broker. The file can be created using the <code><a href="/docs/linux/man/1-mosquitto_passwd/">mosquitto_passwd</a></code>(1) utility. If mosquitto is compiled without TLS support (it is recommended that TLS support is included), then the password file should be a text file with each line in the format &quot;username:password&quot;, where the colon and password are optional but recommended. If <code>allow_anonymous</code> is set to <i>false</i>, only users defined in this file will be able to connect. Setting <code>allow_anonymous</code> to <i>true</i> when <i>password_file</i>is defined is valid and could be used with acl_file to have e.g. read only guest/anonymous accounts and defined users that can publish. </p>
<p> Reloaded on reload signal. The currently loaded username and password data will be freed and reloaded. Clients that are already connected will not be affected. </p>
<p> See also <code><a href="/docs/linux/man/1-mosquitto_passwd/">mosquitto_passwd</a></code>(1).</dl>
<p> <code>persistence</code> [ true | false ]</p>
<dl>
<dd>If <i>true</i>, connection, subscription and message data will be written to the disk in mosquitto.db at the location dictated by persistence_location. When mosquitto is restarted, it will reload the information stored in mosquitto.db. The data will be written to disk when mosquitto closes and also at periodic intervals as defined by autosave_interval. Writing of the persistence database may also be forced by sending mosquitto the SIGUSR1 signal. If <i>false</i>, the data will be stored in memory only. Defaults to <i>false</i>. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>persistence_file</code> <i>file name</i></p>
<dl>
<dd>The filename to use for the persistent database. Defaults to mosquitto.db. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>persistence_location</code> <i>path</i></p>
<dl>
<dd>The path where the persistence database should be stored. Must end in a trailing slash. If not given, then the current directory is used. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>persistent_client_expiration</code> <i>duration</i></p>
<dl>
<dd>This option allows persistent clients (those with clean session set to false) to be removed if they do not reconnect within a certain time frame. This is a non-standard option. As far as the MQTT spec is concerned, persistent clients persist forever. </p>
<p> Badly designed clients may set clean session to false whilst using a randomly generated client id. This leads to persistent clients that will never reconnect. This option allows these clients to be removed. </p>
<p> The expiration period should be an integer followed by one of h d w m y for hour, day, week, month and year respectively. For example: </p>
<dl>
<dd>&bull; persistent_client_expiration 2m</dl>
<dl>
<dd>&bull; persistent_client_expiration 14d</dl>
<dl>
<dd>&bull; persistent_client_expiration 1y</dl>
<p> As this is a non-standard option, the default if not set is to never expire persistent clients. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>pid_file</code> <i>file path</i></p>
<dl>
<dd>Write a pid file to the file specified. If not given (the default), no pid file will be written. If the pid file cannot be written, mosquitto will exit. This option only has an effect is mosquitto is run in daemon mode. </p>
<p> If mosquitto is being automatically started by an init script it will usually be required to write a pid file. This should then be configured as e.g. /var/run/mosquitto.pid </p>
<p> Not reloaded on reload signal.</dl>
<p> <code>psk_file</code> <i>file path</i></p>
<dl>
<dd>Set the path to a pre-shared-key file. This option requires a listener to be have PSK support enabled. If defined, the contents of the file are used to control client access to the broker. Each line should be in the format &quot;identity:key&quot;, where the key is a hexadecimal string with no leading &quot;0x&quot;. A client connecting to a listener that has PSK support enabled must provide a matching identity and PSK to allow the encrypted connection to proceed. </p>
<p> Reloaded on reload signal. The currently loaded identity and key data will be freed and reloaded. Clients that are already connected will not be affected.</dl>
<p> <code>queue_qos0_messages</code> [ true | false ]</p>
<dl>
<dd>Set to <i>true</i> to queue messages with QoS 0 when a persistent client is disconnected. These messages are included in the limit imposed by max_queued_messages. Defaults to <i>false</i>. </p>
<p> Note that the MQTT v3.1 spec states that only QoS 1 and 2 messages should be saved in this situation so this is a non-standard option. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>retained_persistence</code> [ true | false ]</p>
<dl>
<dd>This is a synonym of the <code>persistence</code> option. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>retry_interval</code> <i>seconds</i></p>
<dl>
<dd>The integer number of seconds after a QoS=1 or QoS=2 message has been sent that mosquitto will wait before retrying when no response is received. If unset, defaults to 20 seconds. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>store_clean_interval</code> <i>seconds</i></p>
<dl>
<dd>The integer number of seconds between the internal message store being cleaned of messages that are no longer referenced. Lower values will result in lower memory usage but more processor time, higher values will have the opposite effect. Setting a value of 0 means the unreferenced messages will be disposed of as quickly as possible. Defaults to 10 seconds. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>sys_interval</code> <i>seconds</i></p>
<dl>
<dd>The integer number of seconds between updates of the $SYS subscription hierarchy, which provides status information about the broker. If unset, defaults to 10 seconds. </p>
<p> Set to 0 to disable publishing the $SYS hierarchy completely. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>upgrade_outgoing_qos</code> [ true | false ]</p>
<dl>
<dd>The MQTT specification requires that the QoS of a message delivered to a subscriber is never upgraded to match the QoS of the subscription. Enabling this option changes this behaviour. If <code>upgrade_outgoing_qos</code> is set <i>true</i>, messages sent to a subscriber will always match the QoS of its subscription. This is a non-standard option not provided for by the spec. Defaults to <i>false</i>. </p>
<p> Reloaded on reload signal.</dl>
<p> <code>user</code> <i>username</i></p>
<dl>
<dd>When run as root, change to this user and its primary group on startup. If mosquitto is unable to change to this user and group, it will exit with an error. The user specified must have read/write access to the persistence database if it is to be written. If run as a non-root user, this setting has no effect. Defaults to mosquitto. </p>
<p> This setting has no effect on Windows and so you should run mosquitto as the user you wish it to run as. </p>
<p> Not reloaded on reload signal.</dl>
<h2>Listeners</h2>
<p>The network ports that mosquitto listens on can be controlled using listeners. The default listener options can be overridden and further listeners can be created.</p>
<h3>General Options</h3>
<p><code>bind_address</code> <i>address</i></p>
<dl>
<dd>Listen for incoming network connections on the specified IP address/hostname only. This is useful to restrict access to certain network interfaces. To restrict access to mosquitto to the local host only, use &quot;bind_address localhost&quot;. This only applies to the default listener. Use the listener variable to control other listeners. </p>
<p> Not reloaded on reload signal.</dl>
<p> <code>http_dir</code> <i>directory</i></p>
<dl>
<dd>When a listener is using the websockets protocol, it is possible to serve http data as well. Set <code>http_dir</code> to a directory which contains the files you wish to serve. If this option is not specified, then no normal http connections will be possible. </p>
<p> Not reloaded on reload signal.</dl>
<p> <code>listener</code> <i>port</i> <i>[bind address/host]</i></p>
<dl>
<dd>Listen for incoming network connection on the specified port. A second optional argument allows the listener to be bound to a specific ip address/hostname. If this variable is used and neither the global <code>bind_address</code> nor <code>port</code> options are used then the default listener will not be started. </p>
<p> The <code>bind address/host</code> option allows this listener to be bound to a specific IP address by passing an IP address or hostname. For websockets listeners, it is only possible to pass an IP address here. </p>
<p> This option may be specified multiple times. See also the <code>mount_point</code> option. </p>
<p> Not reloaded on reload signal.</dl>
<p> <code>max_connections</code> <i>count</i></p>
<dl>
<dd>Limit the total number of clients connected for the current listener. Set to -1 to have &quot;unlimited&quot; connections. Note that other limits may be imposed that are outside the control of mosquitto. See e.g. <code><a href="/docs/linux/man/5-limits-conf/">limits.conf</a></code>(5). </p>
<p> Not reloaded on reload signal.</dl>
<p> <code>mount_point</code> <i>topic prefix</i></p>
<dl>
<dd>This option is used with the listener option to isolate groups of clients. When a client connects to a listener which uses this option, the string argument is attached to the start of all topics for this client. This prefix is removed when any messages are sent to the client. This means a client connected to a listener with mount point <i>example</i> can only see messages that are published in the topic hierarchy <i>example</i> and above. </p>
<p> Not reloaded on reload signal.</dl>
<p> <code>port</code> <i>port number</i></p>
<dl>
<dd>Set the network port for the default listener to listen on. Defaults to 1883. </p>
<p> Not reloaded on reload signal.</dl>
<p> <code>protocol</code> <i>value</i></p>
<dl>
<dd>Set the protocol to accept for this listener. Can be <code>mqtt</code>, the default, or <code>websockets</code> if available. </p>
<p> Websockets support is currently disabled by default at compile time. Certificate based TLS may be used with websockets, except that only the <code>cafile</code>, <code>certfile</code>, <code>keyfile</code> and <code>ciphers</code> options are supported. </p>
<p> Not reloaded on reload signal.</dl>
<p> <code>use_username_as_clientid</code> [ true | false ]</p>
<dl>
<dd>Set <code>use_username_as_clientid</code> to true to replace the clientid that a client connected with with its username. This allows authentication to be tied to the clientid, which means that it is possible to prevent one client disconnecting another by using the same clientid. Defaults to false. </p>
<p> If a client connects with no username it will be disconnected as not authorised when this option is set to true. Do not use in conjunction with <code>clientid_prefixes</code>. </p>
<p> See also <code>use_identity_as_username</code>. </p>
<p> Not reloaded on reload signal.</dl>
<p> <code>websockets_log_level</code> <i>level</i></p>
<dl>
<dd>Change the websockets logging level. This is a global option, it is not possible to set per listener. This is an integer that is interpreted by libwebsockets as a bit mask for its lws_log_levels enum. See the libwebsockets documentation for more details. </p>
<p> To use this option, <code>log_type websockets</code> must also be enabled. Defaults to 0.</dl>
<h3>Certificate based SSL/TLS Support</h3>
<p>The following options are available for all listeners to configure certificate based SSL support. See also &quot;Pre-shared-key based SSL/TLS support&quot;. </p>
<p> <code>cafile</code> <i>file path</i></p>
<dl>
<dd>At least one of <code>cafile</code> or <code>capath</code> must be provided to allow SSL support. </p>
<p> <code>cafile</code> is used to define the path to a file containing the PEM encoded CA certificates that are trusted.</dl>
<p> <code>capath</code> <i>directory path</i></p>
<dl>
<dd>At least one of <code>cafile</code> or <code>capath</code> must be provided to allow SSL support. </p>
<p> <code>capath</code> is used to define a directory that contains PEM encoded CA certificates that are trusted. For <code>capath</code> to work correctly, the certificates files must have &quot;.pem&quot; as the file ending and you must run &quot;c_rehash &lt;path to capath&gt;&quot; each time you add/remove a certificate.</dl>
<p> <code>certfile</code> <i>file path</i></p>
<dl>
<dd>Path to the PEM encoded server certificate.</dl>
<p> <code>ciphers</code> <i>cipher:list</i></p>
<dl>
<dd>The list of allowed ciphers, each separated with a colon. Available ciphers can be obtained using the &quot;openssl ciphers&quot; command.</dl>
<p> <code>crlfile</code> <i>file path</i></p>
<dl>
<dd>If you have <code>require_certificate</code> set to <i>true</i>, you can create a certificate revocation list file to revoke access to particular client certificates. If you have done this, use crlfile to point to the PEM encoded revocation file.</dl>
<p> <code>keyfile</code> <i>file path</i></p>
<dl>
<dd>Path to the PEM encoded keyfile.</dl>
<p> <code>require_certificate</code> [ true | false ]</p>
<dl>
<dd>By default an SSL/TLS enabled listener will operate in a similar fashion to a https enabled web server, in that the server has a certificate signed by a CA and the client will verify that it is a trusted certificate. The overall aim is encryption of the network traffic. By setting <code>require_certificate</code> to <i>true</i>, the client must provide a valid certificate in order for the network connection to proceed. This allows access to the broker to be controlled outside of the mechanisms provided by MQTT.</dl>
<p> <code>tls_version</code> <i>version</i></p>
<dl>
<dd>Configure the version of the TLS protocol to be used for this listener. Possible values are <i>tlsv1.2</i>, <i>tlsv1.1</i> and <i>tlsv1</i>. If left unset, the default of allowing all of TLS v1.2, v1.1 and v1.0 is used.</dl>
<p> <code>use_identity_as_username</code> [ true | false ]</p>
<dl>
<dd>If <code>require_certificate</code> is <i>true</i>, you may set <code>use_identity_as_username</code> to <i>true</i> to use the CN value from the client certificate as a username. If this is <i>true</i>, the <code>password_file</code> option will not be used for this listener.</dl>
<h3>Pre-shared-key based SSL/TLS Support</h3>
<p>The following options are available for all listeners to configure pre-shared-key based SSL support. See also &quot;Certificate based SSL/TLS support&quot;. </p>
<p> <code>ciphers</code> <i>cipher:list</i></p>
<dl>
<dd>When using PSK, the encryption ciphers used will be chosen from the list of available PSK ciphers. If you want to control which ciphers are available, use this option. The list of available ciphers can be optained using the &quot;openssl ciphers&quot; command and should be provided in the same format as the output of that command.</dl>
<p> <code>psk_hint</code> <i>hint</i></p>
<dl>
<dd>The <code>psk_hint</code> option enables pre-shared-key support for this listener and also acts as an identifier for this listener. The hint is sent to clients and may be used locally to aid authentication. The hint is a free form string that doesn&#8217;t have much meaning in itself, so feel free to be creative. </p>
<p> If this option is provided, see <code>psk_file</code> to define the pre-shared keys to be used or create a security plugin to handle them.</dl>
<p> <code>tls_version</code> <i>version</i></p>
<dl>
<dd>Configure the version of the TLS protocol to be used for this listener. Possible values are <i>tlsv1.2</i>, <i>tlsv1.1</i> and <i>tlsv1</i>. If left unset, the default of allowing all of TLS v1.2, v1.1 and v1.0 is used.</dl>
<p> <code>use_identity_as_username</code> [ true | false ]</p>
<dl>
<dd>Set <code>use_identity_as_username</code> to have the psk identity sent by the client used as its username. The username will be checked as normal, so <code>password_file</code> or another means of authentication checking must be used. No password will be used.</dl>
<h2>Configuring Bridges</h2>
<p>Multiple bridges (connections to other brokers) can be configured using the following variables. </p>
<p> Bridges cannot currently be reloaded on reload signal. </p>
<p> <code>address</code> <i>address[:port]</i> <i>[address[:port]]</i>, <code>addresses</code> <i>address[:port]</i> <i>[address[:port]]</i></p>
<dl>
<dd>Specify the address and optionally the port of the bridge to connect to. This must be given for each bridge connection. If the port is not specified, the default of 1883 is used. </p>
<p> Multiple host addresses can be specified on the address config. See the <code>round_robin</code> option for more details on the behaviour of bridges with multiple addresses.</dl>
<p> <code>bridge_attempt_unsubscribe</code> [ true | false ]</p>
<dl>
<dd>If a bridge has topics that have &quot;out&quot; direction, the default behaviour is to send an unsubscribe request to the remote broker on that topic. This means that changing a topic direction from &quot;in&quot; to &quot;out&quot; will not keep receiving incoming messages. Sending these unsubscribe requests is not always desirable, setting <code>bridge_attempt_unsubscribe</code> to <i>false</i> will disable sending the unsubscribe request. Defaults to <i>true</i>.</dl>
<p> <code>bridge_protocol_version</code> <i>version</i></p>
<dl>
<dd>Set the version of the MQTT protocol to use with for this bridge. Can be one of <i>mqttv31</i> or <i>mqttv311</i>. Defaults to <i>mqttv31</i>.</dl>
<p> <code>cleansession</code> [ true | false ]</p>
<dl>
<dd>Set the clean session option for this bridge. Setting to <i>false</i> (the default), means that all subscriptions on the remote broker are kept in case of the network connection dropping. If set to <i>true</i>, all subscriptions and messages on the remote broker will be cleaned up if the connection drops. Note that setting to <i>true</i> may cause a large amount of retained messages to be sent each time the bridge reconnects. </p>
<p> If you are using bridges with <code>cleansession</code> set to <i>false</i> (the default), then you may get unexpected behaviour from incoming topics if you change what topics you are subscribing to. This is because the remote broker keeps the subscription for the old topic. If you have this problem, connect your bridge with <code>cleansession</code> set to <i>true</i>, then reconnect with cleansession set to <i>false</i> as normal.</dl>
<p> <code>connection</code> <i>name</i></p>
<dl>
<dd>This variable marks the start of a new bridge connection. It is also used to give the bridge a name which is used as the client id on the remote broker.</dl>
<p> <code>keepalive_interval</code> <i>seconds</i></p>
<dl>
<dd>Set the number of seconds after which the bridge should send a ping if no other traffic has occurred. Defaults to 60. A minimum value of 5 seconds is allowed.</dl>
<p> <code>idle_timeout</code> <i>seconds</i></p>
<dl>
<dd>Set the amount of time a bridge using the lazy start type must be idle before it will be stopped. Defaults to 60 seconds.</dl>
<p> <code>local_clientid</code> <i>id</i></p>
<dl>
<dd>Set the clientid to use on the local broker. If not defined, this defaults to <code>local.&lt;clientid&gt;</code>. If you are bridging a broker to itself, it is important that local_clientid and clientid do not match.</dl>
<p> <code>local_password</code> <i>password</i></p>
<dl>
<dd>Configure the password to be used when connecting this bridge to the local broker. This may be important when authentication and ACLs are being used.</dl>
<p> <code>local_username</code> <i>username</i></p>
<dl>
<dd>Configure the username to be used when connecting this bridge to the local broker. This may be important when authentication and ACLs are being used.</dl>
<p> <code>notifications</code> [ true | false ]</p>
<dl>
<dd>If set to <i>true</i>, publish notification messages to the local and remote brokers giving information about the state of the bridge connection. Retained messages are published to the topic $SYS/broker/connection/&lt;clientid&gt;/state unless otherwise set with <code>notification_topic</code>s. If the message is 1 then the connection is active, or 0 if the connection has failed. Defaults to <i>true</i>.</dl>
<p> <code>notification_topic</code> <i>topic</i></p>
<dl>
<dd>Choose the topic on which notifications will be published for this bridge. If not set the messages will be sent on the topic $SYS/broker/connection/&lt;clientid&gt;/state.</dl>
<p> <code>remote_clientid</code> <i>id</i></p>
<dl>
<dd>Set the client id for this bridge connection. If not defined, this defaults to &#8216;name.hostname&#8217;, where name is the connection name and hostname is the hostname of this computer. </p>
<p> This replaces the old &quot;clientid&quot; option to avoid confusion with local/remote sides of the bridge. &quot;clientid&quot; remains valid for the time being.</dl>
<p> <code>remote_password</code> <i>value</i></p>
<dl>
<dd>Configure a password for the bridge. This is used for authentication purposes when connecting to a broker that supports MQTT v3.1 and up and requires a username and/or password to connect. This option is only valid if a remote_username is also supplied. </p>
<p> This replaces the old &quot;password&quot; option to avoid confusion with local/remote sides of the bridge. &quot;password&quot; remains valid for the time being.</dl>
<p> <code>remote_username</code> <i>name</i></p>
<dl>
<dd>Configure a username for the bridge. This is used for authentication purposes when connecting to a broker that supports MQTT v3.1 and up and requires a username and/or password to connect. See also the <code>remote_password</code> option. </p>
<p> This replaces the old &quot;username&quot; option to avoid confusion with local/remote sides of the bridge. &quot;username&quot; remains valid for the time being.</dl>
<p> <code>restart_timeout</code> <i>value</i></p>
<dl>
<dd>Set the amount of time a bridge using the automatic start type will wait until attempting to reconnect. Defaults to 30 seconds.</dl>
<p> <code>round_robin</code> [ true | false ]</p>
<dl>
<dd>If the bridge has more than one address given in the address/addresses configuration, the round_robin option defines the behaviour of the bridge on a failure of the bridge connection. If round_robin is <i>false</i>, the default value, then the first address is treated as the main bridge connection. If the connection fails, the other secondary addresses will be attempted in turn. Whilst connected to a secondary bridge, the bridge will periodically attempt to reconnect to the main bridge until successful. </p>
<p> If round_robin is <i>true</i>, then all addresses are treated as equals. If a connection fails, the next address will be tried and if successful will remain connected until it fails.</dl>
<p> <code>start_type</code> [ automatic | lazy | once ]</p>
<dl>
<dd>Set the start type of the bridge. This controls how the bridge starts and can be one of three types: <i>automatic</i>, <i>lazy </i>and <i>once</i>. Note that RSMB provides a fourth start type &quot;manual&quot; which isn&#8217;t currently supported by mosquitto. </p>
<p> <i>automatic</i> is the default start type and means that the bridge connection will be started automatically when the broker starts and also restarted after a short delay (30 seconds) if the connection fails. </p>
<p> Bridges using the <i>lazy</i> start type will be started automatically when the number of queued messages exceeds the number set with the <code>threshold</code> option. It will be stopped automatically after the time set by the <code>idle_timeout</code> parameter. Use this start type if you wish the connection to only be active when it is needed. </p>
<p> A bridge using the <i>once</i> start type will be started automatically when the broker starts but will not be restarted if the connection fails.</dl>
<p> <code>threshold</code> <i>count</i></p>
<dl>
<dd>Set the number of messages that need to be queued for a bridge with lazy start type to be restarted. Defaults to 10 messages.</dl>
<p> <code>topic</code> <i>pattern</i> [[[ out | in | both ] qos-level] local-prefix remote-prefix]</p>
<dl>
<dd>Define a topic pattern to be shared between the two brokers. Any topics matching the pattern (which may include wildcards) are shared. The second parameter defines the direction that the messages will be shared in, so it is possible to import messages from a remote broker using <i>in</i>, export messages to a remote broker using <i>out</i> or share messages in both directions. If this parameter is not defined, the default of <i>out</i> is used. The QoS level defines the publish/subscribe QoS level used for this topic and defaults to 0. </p>
<p> The <i>local-prefix</i> and <i>remote-prefix</i> options allow topics to be remapped when publishing to and receiving from remote brokers. This allows a topic tree from the local broker to be inserted into the topic tree of the remote broker at an appropriate place. </p>
<p> For incoming topics, the bridge will prepend the pattern with the remote prefix and subscribe to the resulting topic on the remote broker. When a matching incoming message is received, the remote prefix will be removed from the topic and then the local prefix added. </p>
<p> For outgoing topics, the bridge will prepend the pattern with the local prefix and subscribe to the resulting topic on the local broker. When an outgoing message is processed, the local prefix will be removed from the topic then the remote prefix added. </p>
<p> When using topic mapping, an empty prefix can be defined using the place marker <i>&quot;&quot;</i>. Using the empty marker for the topic itself is also valid. The table below defines what combination of empty or value is valid. </p>
<table BORDER>
<tr VALIGN=top>
<td><code> &nbsp;<wbr> </code></td>
<td><code> <i>Topic</i> </code></td>
<td><code> <i>Local Prefix</i> </code></td>
<td><code> <i>Remote Prefix</i> </code></td>
<td><code> <i>Validity</i> </code>
</td>
</tr>
<tr VALIGN=top>
<td> 1 </td>
<td> value </td>
<td> value </td>
<td> value </td>
<td> valid
</td>
</tr>
<tr VALIGN=top>
<td> 2 </td>
<td> value </td>
<td> value </td>
<td> &quot;&quot; </td>
<td> valid
</td>
</tr>
<tr VALIGN=top>
<td> 3 </td>
<td> value </td>
<td> &quot;&quot; </td>
<td> value </td>
<td> valid
</td>
</tr>
<tr VALIGN=top>
<td> 4 </td>
<td> value </td>
<td> &quot;&quot; </td>
<td> &quot;&quot; </td>
<td> valid (no remapping)
</td>
</tr>
<tr VALIGN=top>
<td> 5 </td>
<td> &quot;&quot; </td>
<td> value </td>
<td> value </td>
<td> valid (remap single local topic to remote)
</td>
</tr>
<tr VALIGN=top>
<td> 6 </td>
<td> &quot;&quot; </td>
<td> value </td>
<td> &quot;&quot; </td>
<td> invalid
</td>
</tr>
<tr VALIGN=top>
<td> 7 </td>
<td> &quot;&quot; </td>
<td> &quot;&quot; </td>
<td> value </td>
<td> invalid
</td>
</tr>
<tr VALIGN=top>
<td> 8 </td>
<td> &quot;&quot; </td>
<td> &quot;&quot; </td>
<td> &quot;&quot; </td>
<td> invalid
</td>
</tr>
</table>
<p> To remap an entire topic tree, use e.g.: </p>
<dl>
<dd>
<pre>topic # both 2 local/topic/ remote/topic/</pre>
</dl>
<p> This option can be specified multiple times per bridge. </p>
<p> Care must be taken to ensure that loops are not created with this option. If you are experiencing high CPU load from a broker, it is possible that you have a loop where each broker is forever forwarding each other the same messages. </p>
<p> See also the <code>cleansession</code> option if you have messages arriving on unexpected topics when using incoming topics. </p>
<p> <code>Example Bridge Topic Remapping.&nbsp;<wbr></code> The configuration below connects a bridge to the broker at <code>test.mosquitto.org</code>. It subscribes to the remote topic <code>$SYS/broker/clients/total</code> and republishes the messages received to the local topic <code>test/mosquitto/org/clients/total</code> </p>
<dl>
<dd>
<pre>connection test-mosquitto-org
address test.mosquitto.org
cleansession true
topic clients/total in 0 test/mosquitto/org $SYS/broker/</pre>
</dl>
</dl>
<p> <code>try_private</code> [ true | false ]</p>
<dl>
<dd>If try_private is set to <i>true</i>, the bridge will attempt to indicate to the remote broker that it is a bridge not an ordinary client. If successful, this means that loop detection will be more effective and that retained messages will be propagated correctly. Not all brokers support this feature so it may be necessary to set <code>try_private</code> to <i>false</i> if your bridge does not connect properly. </p>
<p> Defaults to <i>true</i>.</dl>
<h3>SSL/TLS Support</h3>
<p>The following options are available for all bridges to configure SSL/TLS support. </p>
<p> <code>bridge_attempt_unsubscribe</code> [ true | false ]</p>
<dl>
<dd>If a bridge has topics that have &quot;out&quot; direction, the default behaviour is to send an unsubscribe request to the remote broker on that topic. This means that changing a topic direction from &quot;in&quot; to &quot;out&quot; will not keep receiving incoming messages. Sending these unsubscribe requests is not always desirable, setting <code>bridge_attempt_unsubscribe</code> to <i>false</i> will disable sending the unsubscribe request.</dl>
<p> <code>bridge_cafile</code> <i>file path</i></p>
<dl>
<dd>One of <code>bridge_cafile</code> or <code>bridge_capath</code> must be provided to allow SSL/TLS support. </p>
<p> bridge_cafile is used to define the path to a file containing the PEM encoded CA certificates that have signed the certificate for the remote broker.</dl>
<p> <code>bridge_capath</code> <i>file path</i></p>
<dl>
<dd>One of <code>bridge_capath</code> or <code>bridge_capath</code> must be provided to allow SSL/TLS support. </p>
<p> bridge_capath is used to define the path to a directory containing the PEM encoded CA certificates that have signed the certificate for the remote broker. For bridge_capath to work correctly, the certificate files must have &quot;.crt&quot; as the file ending and you must run &quot;c_rehash &lt;path to bridge_capath&gt;&quot; each time you add/remove a certificate.</dl>
<p> <code>bridge_certfile</code> <i>file path</i></p>
<dl>
<dd>Path to the PEM encoded client certificate for this bridge, if required by the remote broker.</dl>
<p> <code>bridge_identity</code> <i>identity</i></p>
<dl>
<dd>Pre-shared-key encryption provides an alternative to certificate based encryption. A bridge can be configured to use PSK with the <code>bridge_identity</code> and <code>bridge_psk</code> options. This is the client identity used with PSK encryption. Only one of certificate and PSK based encryption can be used on one bridge at once.</dl>
<p> <code>bridge_insecure</code> [ true | false ]</p>
<dl>
<dd>When using certificate based TLS, the bridge will attempt to verify the hostname provided in the remote certificate matches the host/address being connected to. This may cause problems in testing scenarios, so <code>bridge_insecure</code> may be set to <i>false</i> to disable the hostname verification. </p>
<p> Setting this option to <i>true</i> means that a malicious third party could potentially inpersonate your server, so it should always be set to <i>false</i> in production environments.</dl>
<p> <code>bridge_keyfile</code> <i>file path</i></p>
<dl>
<dd>Path to the PEM encoded private key for this bridge, if required by the remote broker.</dl>
<p> <code>bridge_psk</code> <i>key</i></p>
<dl>
<dd>Pre-shared-key encryption provides an alternative to certificate based encryption. A bridge can be configured to use PSK with the <code>bridge_identity</code> and <code>bridge_psk</code> options. This is the pre-shared-key in hexadecimal format with no &quot;0x&quot;. Only one of certificate and PSK based encryption can be used on one bridge at once.</dl>
<p> <code>bridge_tls_version</code> <i>version</i></p>
<dl>
<dd>Configure the version of the TLS protocol to be used for this bridge. Possible values are <i>tlsv1.2</i>, <i>tlsv1.1</i> and <i>tlsv1</i>. Defaults to <i>tlsv1.2</i>. The remote broker must support the same version of TLS for the connection to succeed.</dl>
<h2>Files</h2>
<p>mosquitto.conf</p>
<h2>Bugs</h2>
<p><code>mosquitto</code> bug information can be found at <a rel="nofollow" href="https://bugs.eclipse.org/bugs/describecomponents.cgi?product=Mosquitto">https://bugs.eclipse.org/bugs/describecomponents.cgi?product=Mosquitto</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mosquitto/">mosquitto</a></code>(8), <code><a href="/docs/linux/man/1-mosquitto_passwd/">mosquitto_passwd</a></code>(1), <code><a href="/docs/linux/man/7-mosquitto-tls/">mosquitto-tls</a></code>(7), <code><a href="/docs/linux/man/7-mqtt/">mqtt</a></code>(7), <code><a href="/docs/linux/man/5-limits-conf/">limits.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Roger Light &lt;roger [at] atchoo.org&gt;</p>
