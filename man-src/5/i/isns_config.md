---
title: "isns_config(5)"
name: "isns_config"
section: "5"
letter: "i"
url: "/docs/linux/man/5-isns_config/"
description: "isns_config – iSNS configuration file"
---

<p>isns_config &#8211; iSNS configuration file</p>
<h2>Synopsis</h2>
<p><code>/etc/isns/isnsadm.conf</code><br />
 <code>/etc/isns/isnsd.conf</code><br />
 <code>/etc/isns/isnsdd.conf</code> </p>
<h2>Description</h2>
<p>All Open-iSNS utilities read their configuration from a file in <code>/etc/isns</code>. There is a separate configuration file for each application, <code>isnsd</code>, <code>isnsadm</code>, and <code>isnsdd</code>. The syntax and the set of supported options is identical, even though some options are specific to e.g. the server. Unless indicated, options are applicable to all utilities. </p>
<p> An Open-iSNS configuration file contains keyword-argument pairs, one per line. All keywords are case insensitive. </p>
<p> A <code>#</code> character introduces a comment, which extends until the end of the line. Empty lines are ignored. </p>
<p> There are no line continuations, and you cannot use quotes around arguments. </p>
<p> Some options specify timeout values, which are given in units of seconds by default. You can specify an explicit unit, however, such as <code>d</code> (days), <code>h</code> (hours), <code>m</code> (minutes), or <code>s</code> (seconds).</p>
<h3>Generic Options</h3>
<dl>
<dt><code>HostName</code></p>
<dd>By default, Open-iSNS applications will retrieve the machine&#8217;s hostname using the <code><a href="/docs/linux/man/3-gethostname/">gethostname</a></code>(3) system call, and use a DNS lookup to look up the canonical name. Using the <code>HostName</code> option, you can overried this. This option is rarely needed.</p>
<dt><code>SourceName</code></p>
<dd>This option is mandatory for all Open-iSNS applications. This should be a name which identifies the client uniquely. There are two readings of RFC 4171; one requires that this is an iSCSI qualified name such as <code>iqn.2001-04.com.example.host</code>, whereas other language in the RFC suggests that this is pretty much a free-format string that just has to be unique (using e.g. the client&#8217;s fully qualified domain name).</p>
<dd>When using DSA authentication, Open-iSNS currently requires the source name to match the key identifier (SPI) of the client&#8217;s public key.</p>
<dd>If left empty, the source name is derived from the client&#8217;s hostname.</p>
<dt><code>ServerAddress</code> (client):</p>
<dd>This options specifies the host name or address of the iSNS server to talk to. It can optionally be followed by a colon, and a port number.</p>
<dd>Instead of a hostname, IPv4 or IPv6 addresses can be used. In order to avoid ambiguities, literal IPv6 addresses must be surrounded by square brackets, as in <code>[2001:4e5f::1]</code>.</p>
<dd>When specifying a port number, you can use either the numeric port, or a string name to be looked up in <code>/etc/services</code>. When the port is omitted, it defaults to 3205, the IANA assigned port number of iSNS.</p>
<dd>If the special string <code>SLP:</code> is used, the client will try to locate the iSNS server through SLP.</p>
<dt><code>SLPRegister</code> (server):</p>
<dd>If set to 1, the iSNS daemon will register itself will the SLP service. This allows clients to contact the server without having to configure its address statically.</p>
<dt><code>PIDFile</code> (server):</p>
<dd>This specifies the name of the server&#8217;s PID file, which is <code>/var/run/isnsd.pid</code> by default.</dl>
<h3>Database Related Options</h3>
<p>These options apply to the iSNS server only, and control operation of the iSNS database.</p>
<dl>
<dt><code>Database</code></p>
<dd>This option is used to specify how the database is stored. Setting this to an absolute path name will make <code>isnsd</code> keep its database in the specified directory.</p>
<dd>If you leave this empty, <code>isnsd</code> will keep its database in memory. This is also the default setting.</p>
<dt><code>DefaultDiscoveryDomain</code></p>
<dd>iSNS scopes visibility of other nodes using so-called Discovery Domains. A storage node A will only &quot;see&quot; storage node B, if both are members of the same discovery domain.</p>
<dd>So if a storage node is registered which is not part of any discovery domain, it will not see any other nodes.</p>
<dd>By setting <code>DefaultDiscoveryDomain=1</code>, you can tell isnsd to create a virtual &quot;default discovery domain&quot;, which holds all nodes that are not part of any administratively configured discovery domain.</p>
<dd>By default, there is no default discovery domain.</p>
<dt><code>RegistrationPeriod</code></p>
<dd>The iSNS server can purge registered entities after a certain period of inactivity. This is called the registration period. Clients who register objects are supposed to refresh their registration within this period.</p>
<dd>The default value is 1 hour. Setting it to 0 disables expiry of entities from the database.</p>
<dt><code>ESIRetries</code></p>
<dd>Open-iSNS is able to monitor the reachability of storage nodes and their portals by using a protocol feature called ESI (Entity status inquiry). Clients request ESI monitoring by registering an ESI port along with each portal. The server will send ESI messages to these portals at regular intervals. If the portal fails to reply several times in a row, it is considered dead, and will be removed from the database.</p>
<dd><code>ESIRetries</code> specifies the maximum number of attempts the server will make at contacting the portal before pronouncing it dead. If set to 0, the server will disable ESI and reject any registrations that specify an ESI port with an error code of &quot;ESI not supported&quot;.</p>
<dd>The default value is 3.</p>
<dt><code>ESIMinInterval</code></p>
<dd>This timeout value specifies the minimum ESI interval. If a client requests an ESI interval less than this value, it is silently rounded up.</p>
<dd>The default value is 60 seconds.</p>
<dt><code>ESIMaxInterval</code></p>
<dd>This timeout value specifies the maximum ESI interval. If a client requests an ESI interval greater than this value, it is silently rounded down.</p>
<dd>The default value is 10 minutes.</p>
<dd>The maximum ESI interval must not exceed half the value of the registration period.</p>
<dt><code>SCNRetries</code></p>
<dd>iSNS clients can register to receive State Change Notification (SCN) messages to learn about changes in the iSNS database. This value specifies how often the server will try to retransmit an SCN message until giving up.</p>
<dd>The default value is 3.</p>
<dt><code>SCNCallout</code></p>
<dd>This is the path name of a helper program that <code>isnsdd</code> will invoke whenever it processes a state change notification from the server. The helper program will be invoked with an argument indicating the type of event, being one of <code>add</code>, <code>update</code>, or <code>remove</code>. This is followed by a list of attributes in <i>name</i><code>=</code><i>value</i> notation, using the names and conventions described in <code><a href="/docs/linux/man/8-isnsadm/">isnsadm</a></code>(8).</dl>
<h3>Security Related Options</h3>
<p>The iSNS standard defines an authentication method based on the DSA algorithm. Participants in a message exchange authenticate messages by adding an &quot;authentication block&quot; containing a time stamp, a string identifying the key used, and a digital signature of the message. The same method is also used by SLP, the Service Location Protocol. </p>
<p> The string contained in the authentication block is referred to as the <i>Security Policy Index</i>(SPI). This string can be used by the server to look up the client&#8217;s public key by whatever mechanism; so the string could be used as the name of a public key file in a directory, or to retrieve an X509 certificate from LDAP. </p>
<p> From the perspective of Open-iSNS client applications, there are only two keys: the client&#8217;s own (private) key, used to sign the messages it sends to the server, and the server&#8217;s public key, used to verify the signatures of incoming server messages. </p>
<p> The iSNS server needs, in addition to its own private key, access to all public keys of clients that will communicate to it. The latter are kept in what is called a key store. Key stores and their operation will be discussed in section <code>Key Stores and Policy</code> below. </p>
<p> The following configuration options control authentication:</p>
<dl>
<dt><code>Security</code></p>
<dd>This enables or disables DSA authentication. When set to 1, the client will sign all messages, and expect all server messages to be signed.</p>
<dd>When enabling security in the server, incoming messages are checked for the presence of an auth block. If none is present, or if the server cannot find a public key corresponding to the SPI, the message is treated as originating from an anonymous source. If the SPI is known but the signature is incorrect, the message is dropped silently.</p>
<dd>Messages from an anonymous source will be assigned a very restrictive policy that allows database queries only.</p>
<dd>Setting this option to 0 will turn off authentication.</p>
<dd>The default value is -1, which tells iSNS to use authentication if the required keys are installed, and use unauthenticated iSNS otherwise.</p>
<dt><code>AuthName</code></p>
<dd>This is the string that will be used as the SPI in all outgoing messages that have an auth block. It defaults to the host name (please refer to option <code>HostName</code>).</p>
<dt><code>AuthKeyFile</code></p>
<dd>This is the path name of a file containing a PEM encoded DSA key. This key is used to sign outgoing messages. The default is <code>/etc/isns/auth_key</code>.</p>
<dt><code>ServerKeyFile</code></p>
<dd>This option is used by client applications only, and specifies the path name of a file containing a PEM encoded DSA key. This key is used to authenticate the server&#8217;s replies. The default is <code>/etc/isns/server_key.pub</code>.</p>
<dt><code>KeyStore</code></p>
<dd>This server-side option specifies the key store to use, described in the next section.</dl>
<p> The following two options control how iSNS will verify the time stamp contained in the authentication block, which is supposed to prevent replay attacks.</p>
<dl>
<dt><code>Auth.ReplayWindow</code></p>
<dd>In order to compensate for clock drift between two hosts exchanging iSNS messages, Open-iSNS will apply a little fuzz when comparing the time stamp contained in the message to the local system time. If the difference between time stamp and local system time is less than the number of seconds given by this option, the message is acceptable. Otherwise, it is rejected.</p>
<dd>The default value is <code>5m</code>.</p>
<dt><code>Auth.TimestampJitter</code></p>
<dd>When verifying incoming messages, Open-iSNS checks that the time stamps sent by the peer are increasing monotonically. In order to compensate for the reordering of messages by the network (eg when using UDP as transport), a certain time stamp jitter is accepted. If the time stamp of an incoming messages is no earlier than <code>TimestampJitter</code> seconds before the last time stamp received, then the message is acceptable. Otherwise, it is rejected.</p>
<dd>The default value is <code>1s</code>.</dl>
<h3>Key Stores and Policy</h3>
<p>The current implementation supports two types of key stores. </p>
<p> The simple key store uses a flat directory to store public keys, each key in a file of its own. The file is expected to hold the client&#8217;s PEM-encoded public key, and it must use the client&#8217;s SPI as the name. This type of key store is not really recommended, as it does not store any policy information. </p>
<p> A simple key store can be configured by setting the <code>KeyStore</code> option to the path name of the directory. </p>
<p> The recommended approach is to use the database as key store. This uses vendor-specific policy objects to tie SPI string, public key, entity name, source name and other bits of policy together, and store them in a persistent way. </p>
<p> The database key store is configured by setting the <code>KeyStore</code> option to the reserved value <code>DB:</code>, which is also the default. </p>
<p> Currently, Open-iSNS policy objects have the following attributes, besides the SPI:</p>
<dl>
<dt>Source:</p>
<dd>This is the source node name the client must use. It defaults to the SPI string.</p>
<dt>Functions:</p>
<dd>This is a bitmap detailing which functions the client is permitted to invoke. The bit names correspond to the shorthand names used in RFC 4711, such as <code>DevAttrReg</code>, <code>DevAttrQry</code>, etc. The default is to allow registration, query and deregistration, as well as SCNRegister.</p>
<dt>Entity name:</p>
<dd>This is the entity name assigned to the client. If set, a registration by the client is not permitted to use a different entity name. If the client sends a registration without Entity identifier, the server will assign the entity name given in the policy. The default is to not restrict the entity name.</p>
<dt>Object access:</p>
<dd>This is a bitfield describing access permissions for each object type. For each object type, you can grant Read and/or Write permissions. Read access applies to the Query and GetNext calls; all other operations require write permission. The default grants read and write access to objects of type Entity, Storage Node, Portal and Portal Group; and read access to Discovery Domains.</p>
<dt>Node types:</p>
<dd>This bitfield describes which types of storage nodes a client is allowed to register; the valid bit names are <code>target</code>, <code>initiator</code> and <code>control</code>. The default is to restrict nodes to register initiators only.</dl>
<h3>Network Related Options</h3>
<dl>
<dt><code>Network.MaxSockets</code></p>
<dd>This is the number of incoming connections accepted, and defaults to 1024. This usually applies to server side only, but is relevant if you create a passive TCP socket for ESI or SCN.</p>
<dt><code>Network.ConnectTimeout</code></p>
<dd>This is a timeout value, which specifies the time to wait for a TCP connection to be established. It defaults to <code>60s</code>.</p>
<dt><code>Network.ReconnectTimeout</code></p>
<dd>When a connection attempt failed, we wait for a short time before we try connecting again. This is intended to take the pressure off overloaded servers. The default value is <code>10s</code>.</p>
<dt><code>Network.CallTimeout</code></p>
<dd>Total amount of time to wait before timing out a call to the iSNS server. The default value is <code>60s</code>.</dl>
<h2>See Also</h2>
<p>RFC 4171, <code><a href="/docs/linux/man/8-isnsd/">isnsd</a></code>(8), <code><a href="/docs/linux/man/8-isnsadm/">isnsadm</a></code>(8).</p>
<h2>Authors</h2>
<p>Olaf Kirch &lt;olaf.kirch [at] oracle.com&gt;</p>
