---
title: "qdrouterd-conf(5)"
name: "qdrouterd-conf"
section: "5"
letter: "q"
url: "/docs/linux/man/5-qdrouterd-conf/"
description: "qdrouterd.conf – dispatch router configuration"
---

<p>qdrouterd.conf &#8211; dispatch router configuration</p>
<h2>Synopsis</h2>
<p>qdroutered.conf is the configuration file for the dispatch router.</p>
<h2>Description</h2>
<p>The configuration file is made up of sections with this syntax: </p>
<pre>SECTION-NAME {
 ATTRIBUTE-NAME: ATTRIBUTE-VALUE
 ATTRIBUTE-NAME: ATTRIBUTE-VALUE
 ...
}</pre>
<p>There are two types of sections: </p>
<p> <i>Configuration sections</i> correspond to configuration entities. They can be queried and configured via management tools as well as via the configuration file. </p>
<p> <i>Annotation sections</i> define a group of attribute values that can be included in one or more entity sections. </p>
<p> For example you can define an &quot;ssl-profile&quot; annotation section with SSL credentials that can be included in multiple &quot;listener&quot; entities. Here&#8217;s an example, note how the &#8216;ssl-profile&#8217; attribute of &#8216;listener&#8217; sections references the &#8216;name&#8217; attribute of &#8216;ssl-profile&#8217; sections. </p>
<pre>ssl-profile {
 name: ssl-profile-one
 cert-db: ca-certificate-1.pem
 cert-file: server-certificate-1.pem
 key-file: server-private-key.pem
}
listener {
 ssl-profile: ssl-profile-one
 host: 0.0.0.0
 port: 20102
 sasl-mechanisms: ANONYMOUS
}</pre>
<h2>Annotation Sections</h2>
<h3>addrPort</h3>
<p>Attributes for internet address and port. </p>
<p> Used by: <code>listener</code>, <code>connector</code>.</p>
<dl>
<dt><i>addr</i> (string, default=&#8217;127.0.0.1&#8242;)</p>
<dd>(DEPRECATED)IP address: ipv4 or ipv6 literal or a host name. This attribute has been deprecated. Use host instead</p>
<dt><i>host</i> (string, default=&#8217;127.0.0.1&#8242;)</p>
<dd>IP address: ipv4 or ipv6 literal or a host name</p>
<dt><i>port</i> (string, default=&#8217;amqp&#8217;)</p>
<dd>Port number or symbolic service name.</p>
<dt><i>protocolFamily</i> (One of [&#8216;IPv4&#8217;, &#8216;IPv6&#8217;])</p>
<dd>[&#8216;IPv4&#8217;, &#8216;IPv6&#8217;] IPv4: Internet Protocol version 4; IPv6: Internet Protocol version 6. If not specified, the protocol family will be automatically determined from the address.</dl>
<h3>connectionRole</h3>
<p>Attribute for the role of a connection. </p>
<p> Used by: <code>listener</code>, <code>connector</code>.</p>
<dl>
<dt><i>role</i> (One of [&#8216;normal&#8217;, &#8216;inter-router&#8217;, &#8216;route-container&#8217;, &#8216;on-demand&#8217;], default=&#8217;normal&#8217;)</p>
<dd>The role of an established connection. In the normal role, the connection is assumed to be used for AMQP clients that are doing normal message delivery over the connection. In the inter-router role, the connection is assumed to be to another router in the network. Inter-router discovery and routing protocols can only be used over inter-router connections. route-container role can be used for router-container connections, for example, a router-broker connection. on-demand role has been deprecated.</p>
<dt><i>cost</i> (integer, default=&#8217;1&#8242;)</p>
<dd>For the &#8216;inter-router&#8217; role only. This value assigns a cost metric to the inter-router connection. The default (and minimum) value is one. Higher values represent higher costs. The cost is used to influence the routing algorithm as it attempts to use the path with the lowest total cost from ingress to egress.</dl>
<h3>sslProfile</h3>
<p>Attributes for setting TLS/SSL configuration for connections. </p>
<p> Used by: <code>listener</code>, <code>connector</code>.</p>
<dl>
<dt><i>certDb</i> (path)</p>
<dd>The path to the database that contains the public certificates of trusted certificate authorities (CA).</p>
<dt><i>certFile</i> (path)</p>
<dd>The path to the file containing the PEM-formatted public certificate to be used on the local end of any connections using this profile.</p>
<dt><i>keyFile</i> (path)</p>
<dd>The path to the file containing the PEM-formatted private key for the above certificate.</p>
<dt><i>passwordFile</i> (path)</p>
<dd>If the above private key is password protected, this is the path to a file containing the password that unlocks the certificate key.</p>
<dt><i>password</i> (string)</p>
<dd>An alternative to storing the password in a file referenced by passwordFile is to supply the password right here in the configuration file. This option can be used by supplying the password in the &#8216;password&#8217; option. Don&#8217;t use both password and passwordFile in the same profile.</p>
<dt><i>uidFormat</i> (string)</p>
<dd>A list of x509 client certificate fields that will be used to build a string that will uniquely identify the client certificate owner. For e.g. a value of &#8216;cou&#8217; indicates that the uid will consist of c &#8211; common name concatenated with o &#8211; organization-company name concatenated with u &#8211; organization unit; or a value of &#8216;o2&#8217; indicates that the uid will consist of o (organization name) concatenated with 2 (the sha256 fingerprint of the entire certificate) . Allowed values can be any combination of comma separated &#8216;c'( ISO3166 two character country code), &#8216;s'(state or province), &#8216;l'(Locality; generally &#8211; city), &#8216;o'(Organization &#8211; Company Name), &#8216;u'(Organization Unit &#8211; typically certificate type or brand), &#8216;n'(CommonName &#8211; typically a user name for client certificates) and &#8216;1&#8217;(sha1 certificate fingerprint, as displayed in the fingerprints section when looking at a certificate with say a web browser is the hash of the entire certificate) and 2 (sha256 certificate fingerprint) and 5 (sha512 certificate fingerprint).</p>
<dt><i>displayNameFile</i> (string)</p>
<dd>The path to the file containing the unique id to dispay name mapping</dl>
<h2>Configuration Sections</h2>
<h3>container</h3>
<p>(DEPRECATED)Attributes related to the AMQP container. This entity has been deprecated. Use the router entity instead.</p>
<dl>
<dt><i>containerName</i> (string)</p>
<dd>The name of the AMQP container. If not specified, the container name will be set to a value of the container&#8217;s choosing. The automatically assigned container name is not guaranteed to be persistent across restarts of the container.</p>
<dt><i>workerThreads</i> (integer, default=4)</p>
<dd>The number of threads that will be created to process message traffic and other application work (timers, non-amqp file descriptors, etc.) .</p>
<dt><i>debugDump</i> (path)</p>
<dd>A file to dump debugging information that can&#8217;t be logged normally.</p>
<dt><i>saslConfigPath</i> (path)</p>
<dd>Absolute path to the SASL configuration file.</p>
<dt><i>saslConfigName</i> (string)</p>
<dd>Name of the SASL configuration. This string + &#8216;.conf&#8217; is the name of the configuration file.</dl>
<h3>router</h3>
<p>Tracks peer routers and computes routes to destinations.</p>
<dl>
<dt><i>routerId</i> (string)</p>
<dd>(DEPRECATED) Router&#8217;s unique identity. This attribute has been deprecated. Use id instead</p>
<dt><i>id</i> (string)</p>
<dd>Router&#8217;s unique identity. One of id or routerId is required. The router will fail to start without id or routerId</p>
<dt><i>mode</i> (One of [&#8216;standalone&#8217;, &#8216;interior&#8217;], default=&#8217;standalone&#8217;)</p>
<dd>In standalone mode, the router operates as a single component. It does not participate in the routing protocol and therefore will not cooperate with other routers. In interior mode, the router operates in cooperation with other interior routers in an interconnected network.</p>
<dt><i>helloInterval</i> (integer, default=1)</p>
<dd>Interval in seconds between HELLO messages sent to neighbor routers.</p>
<dt><i>helloMaxAge</i> (integer, default=3)</p>
<dd>Time in seconds after which a neighbor is declared lost if no HELLO is received.</p>
<dt><i>raInterval</i> (integer, default=30)</p>
<dd>Interval in seconds between Router-Advertisements sent to all routers in a stable network.</p>
<dt><i>raIntervalFlux</i> (integer, default=4)</p>
<dd>Interval in seconds between Router-Advertisements sent to all routers during topology fluctuations.</p>
<dt><i>remoteLsMaxAge</i> (integer, default=60)</p>
<dd>Time in seconds after which link state is declared stale if no RA is received.</p>
<dt><i>mobileAddrMaxAge</i> (integer, default=60)</p>
<dd>(DEPRECATED) This value is no longer used in the router.</p>
<dt><i>workerThreads</i> (integer, default=4)</p>
<dd>The number of threads that will be created to process message traffic and other application work (timers, non-amqp file descriptors, etc.) .</p>
<dt><i>debugDump</i> (path)</p>
<dd>A file to dump debugging information that can&#8217;t be logged normally.</p>
<dt><i>saslConfigPath</i> (path)</p>
<dd>Absolute path to the SASL configuration file.</p>
<dt><i>saslConfigName</i> (string, default=&#8217;qdrouterd&#8217;)</p>
<dd>Name of the SASL configuration. This string + &#8216;.conf&#8217; is the name of the configuration file.</dl>
<h3>listener</h3>
<p>Listens for incoming connections to the router. </p>
<p> Annotations: <code>addrPort</code>, <code>connectionRole</code>, <code>sslProfile</code>.</p>
<dl>
<dt><i>addr</i> (string, default=&#8217;127.0.0.1&#8242;)</p>
<dd>(DEPRECATED)IP address: ipv4 or ipv6 literal or a host name. This attribute has been deprecated. Use host instead</p>
<dt><i>host</i> (string, default=&#8217;127.0.0.1&#8242;)</p>
<dd>IP address: ipv4 or ipv6 literal or a host name</p>
<dt><i>port</i> (string, default=&#8217;amqp&#8217;)</p>
<dd>Port number or symbolic service name.</p>
<dt><i>protocolFamily</i> (One of [&#8216;IPv4&#8217;, &#8216;IPv6&#8217;])</p>
<dd>[&#8216;IPv4&#8217;, &#8216;IPv6&#8217;] IPv4: Internet Protocol version 4; IPv6: Internet Protocol version 6. If not specified, the protocol family will be automatically determined from the address.</p>
<dt><i>role</i> (One of [&#8216;normal&#8217;, &#8216;inter-router&#8217;, &#8216;route-container&#8217;, &#8216;on-demand&#8217;], default=&#8217;normal&#8217;)</p>
<dd>The role of an established connection. In the normal role, the connection is assumed to be used for AMQP clients that are doing normal message delivery over the connection. In the inter-router role, the connection is assumed to be to another router in the network. Inter-router discovery and routing protocols can only be used over inter-router connections. route-container role can be used for router-container connections, for example, a router-broker connection. on-demand role has been deprecated.</p>
<dt><i>cost</i> (integer, default=&#8217;1&#8242;)</p>
<dd>For the &#8216;inter-router&#8217; role only. This value assigns a cost metric to the inter-router connection. The default (and minimum) value is one. Higher values represent higher costs. The cost is used to influence the routing algorithm as it attempts to use the path with the lowest total cost from ingress to egress.</p>
<dt><i>certDb</i> (path)</p>
<dd>The path to the database that contains the public certificates of trusted certificate authorities (CA).</p>
<dt><i>certFile</i> (path)</p>
<dd>The path to the file containing the PEM-formatted public certificate to be used on the local end of any connections using this profile.</p>
<dt><i>keyFile</i> (path)</p>
<dd>The path to the file containing the PEM-formatted private key for the above certificate.</p>
<dt><i>passwordFile</i> (path)</p>
<dd>If the above private key is password protected, this is the path to a file containing the password that unlocks the certificate key.</p>
<dt><i>password</i> (string)</p>
<dd>An alternative to storing the password in a file referenced by passwordFile is to supply the password right here in the configuration file. This option can be used by supplying the password in the &#8216;password&#8217; option. Don&#8217;t use both password and passwordFile in the same profile.</p>
<dt><i>uidFormat</i> (string)</p>
<dd>A list of x509 client certificate fields that will be used to build a string that will uniquely identify the client certificate owner. For e.g. a value of &#8216;cou&#8217; indicates that the uid will consist of c &#8211; common name concatenated with o &#8211; organization-company name concatenated with u &#8211; organization unit; or a value of &#8216;o2&#8217; indicates that the uid will consist of o (organization name) concatenated with 2 (the sha256 fingerprint of the entire certificate) . Allowed values can be any combination of comma separated &#8216;c'( ISO3166 two character country code), &#8216;s'(state or province), &#8216;l'(Locality; generally &#8211; city), &#8216;o'(Organization &#8211; Company Name), &#8216;u'(Organization Unit &#8211; typically certificate type or brand), &#8216;n'(CommonName &#8211; typically a user name for client certificates) and &#8216;1&#8217;(sha1 certificate fingerprint, as displayed in the fingerprints section when looking at a certificate with say a web browser is the hash of the entire certificate) and 2 (sha256 certificate fingerprint) and 5 (sha512 certificate fingerprint).</p>
<dt><i>displayNameFile</i> (string)</p>
<dd>The path to the file containing the unique id to dispay name mapping</p>
<dt><i>saslMechanisms</i> (string)</p>
<dd>Comma separated list of accepted SASL authentication mechanisms.</p>
<dt><i>authenticatePeer</i> (boolean)</p>
<dd>yes: Require the peer&#8217;s identity to be authenticated; no: Do not require any authentication.</p>
<dt><i>requireEncryption</i> (boolean)</p>
<dd>yes: Require the connection to the peer to be encrypted; no: Permit non-encrypted communication with the peer</p>
<dt><i>requireSsl</i> (boolean)</p>
<dd>yes: Require the use of SSL or TLS on the connection; no: Allow clients to connect without SSL or TLS.</p>
<dt><i>trustedCerts</i> (path)</p>
<dd>This optional setting can be used to reduce the set of available CAs for client authentication. If used, this setting must provide a path to a PEM file that contains the trusted certificates.</p>
<dt><i>maxFrameSize</i> (integer, default=16384)</p>
<dd>Defaults to 16384. If specified, it is the maximum frame size in octets that will be used in the connection-open negotiation with a connected peer. The frame size is the largest contiguous set of uninterrupted data that can be sent for a message delivery over the connection. Interleaving of messages on different links is done at frame granularity.</p>
<dt><i>idleTimeoutSeconds</i> (integer, default=16)</p>
<dd>The idle timeout, in seconds, for connections through this listener. If no frames are received on the connection for this time interval, the connection shall be closed.</p>
<dt><i>requirePeerAuth</i> (boolean)</p>
<dd>(DEPRECATED) This attribute is now controlled by the authenticatePeer attribute.</p>
<dt><i>allowUnsecured</i> (boolean)</p>
<dd>(DEPRECATED) This attribute is now controlled by the requireEncryption attribute.</p>
<dt><i>allowNoSasl</i> (boolean)</p>
<dd>(DEPRECATED) This attribute is now controlled by the authenticatePeer attribute.</p>
<dt><i>stripAnnotations</i> (One of [&#8216;in&#8217;, &#8216;out&#8217;, &#8216;both&#8217;, &#8216;no&#8217;], default=&#8217;both&#8217;)</p>
<dd>[&#8216;in&#8217;, &#8216;out&#8217;, &#8216;both&#8217;, &#8216;no&#8217;] in: Strip the dispatch router specific annotations only on ingress; out: Strip the dispatch router specific annotations only on egress; both: Strip the dispatch router specific annotations on both ingress and egress; no &#8211; do not strip dispatch router specific annotations</p>
<dt><i>linkCapacity</i> (integer)</p>
<dd>The capacity of links within this connection, in terms of message deliveries. The capacity is the number of messages that can be in-flight concurrently for each link.</dl>
<h3>connector</h3>
<p>Establishes an outgoing connection from the router. </p>
<p> Annotations: <code>addrPort</code>, <code>connectionRole</code>, <code>sslProfile</code>.</p>
<dl>
<dt><i>addr</i> (string, default=&#8217;127.0.0.1&#8242;)</p>
<dd>(DEPRECATED)IP address: ipv4 or ipv6 literal or a host name. This attribute has been deprecated. Use host instead</p>
<dt><i>host</i> (string, default=&#8217;127.0.0.1&#8242;)</p>
<dd>IP address: ipv4 or ipv6 literal or a host name</p>
<dt><i>port</i> (string, default=&#8217;amqp&#8217;)</p>
<dd>Port number or symbolic service name.</p>
<dt><i>protocolFamily</i> (One of [&#8216;IPv4&#8217;, &#8216;IPv6&#8217;])</p>
<dd>[&#8216;IPv4&#8217;, &#8216;IPv6&#8217;] IPv4: Internet Protocol version 4; IPv6: Internet Protocol version 6. If not specified, the protocol family will be automatically determined from the address.</p>
<dt><i>role</i> (One of [&#8216;normal&#8217;, &#8216;inter-router&#8217;, &#8216;route-container&#8217;, &#8216;on-demand&#8217;], default=&#8217;normal&#8217;)</p>
<dd>The role of an established connection. In the normal role, the connection is assumed to be used for AMQP clients that are doing normal message delivery over the connection. In the inter-router role, the connection is assumed to be to another router in the network. Inter-router discovery and routing protocols can only be used over inter-router connections. route-container role can be used for router-container connections, for example, a router-broker connection. on-demand role has been deprecated.</p>
<dt><i>cost</i> (integer, default=&#8217;1&#8242;)</p>
<dd>For the &#8216;inter-router&#8217; role only. This value assigns a cost metric to the inter-router connection. The default (and minimum) value is one. Higher values represent higher costs. The cost is used to influence the routing algorithm as it attempts to use the path with the lowest total cost from ingress to egress.</p>
<dt><i>certDb</i> (path)</p>
<dd>The path to the database that contains the public certificates of trusted certificate authorities (CA).</p>
<dt><i>certFile</i> (path)</p>
<dd>The path to the file containing the PEM-formatted public certificate to be used on the local end of any connections using this profile.</p>
<dt><i>keyFile</i> (path)</p>
<dd>The path to the file containing the PEM-formatted private key for the above certificate.</p>
<dt><i>passwordFile</i> (path)</p>
<dd>If the above private key is password protected, this is the path to a file containing the password that unlocks the certificate key.</p>
<dt><i>password</i> (string)</p>
<dd>An alternative to storing the password in a file referenced by passwordFile is to supply the password right here in the configuration file. This option can be used by supplying the password in the &#8216;password&#8217; option. Don&#8217;t use both password and passwordFile in the same profile.</p>
<dt><i>uidFormat</i> (string)</p>
<dd>A list of x509 client certificate fields that will be used to build a string that will uniquely identify the client certificate owner. For e.g. a value of &#8216;cou&#8217; indicates that the uid will consist of c &#8211; common name concatenated with o &#8211; organization-company name concatenated with u &#8211; organization unit; or a value of &#8216;o2&#8217; indicates that the uid will consist of o (organization name) concatenated with 2 (the sha256 fingerprint of the entire certificate) . Allowed values can be any combination of comma separated &#8216;c'( ISO3166 two character country code), &#8216;s'(state or province), &#8216;l'(Locality; generally &#8211; city), &#8216;o'(Organization &#8211; Company Name), &#8216;u'(Organization Unit &#8211; typically certificate type or brand), &#8216;n'(CommonName &#8211; typically a user name for client certificates) and &#8216;1&#8217;(sha1 certificate fingerprint, as displayed in the fingerprints section when looking at a certificate with say a web browser is the hash of the entire certificate) and 2 (sha256 certificate fingerprint) and 5 (sha512 certificate fingerprint).</p>
<dt><i>displayNameFile</i> (string)</p>
<dd>The path to the file containing the unique id to dispay name mapping</p>
<dt><i>saslMechanisms</i> (string)</p>
<dd>Comma separated list of accepted SASL authentication mechanisms.</p>
<dt><i>allowRedirect</i> (boolean, default=True)</p>
<dd>Allow the peer to redirect this connection to another address.</p>
<dt><i>maxFrameSize</i> (integer, default=65536)</p>
<dd>Maximum frame size in octets that will be used in the connection-open negotiation with a connected peer. The frame size is the largest contiguous set of uninterrupted data that can be sent for a message delivery over the connection. Interleaving of messages on different links is done at frame granularity.</p>
<dt><i>idleTimeoutSeconds</i> (integer, default=16)</p>
<dd>The idle timeout, in seconds, for connections through this connector. If no frames are received on the connection for this time interval, the connection shall be closed.</p>
<dt><i>stripAnnotations</i> (One of [&#8216;in&#8217;, &#8216;out&#8217;, &#8216;both&#8217;, &#8216;no&#8217;], default=&#8217;both&#8217;)</p>
<dd>[&#8216;in&#8217;, &#8216;out&#8217;, &#8216;both&#8217;, &#8216;no&#8217;] in: Strip the dispatch router specific annotations only on ingress; out: Strip the dispatch router specific annotations only on egress; both: Strip the dispatch router specific annotations on both ingress and egress; no &#8211; do not strip dispatch router specific annotations</p>
<dt><i>linkCapacity</i> (integer)</p>
<dd>The capacity of links within this connection, in terms of message deliveries. The capacity is the number of messages that can be in-flight concurrently for each link.</p>
<dt><i>verifyHostName</i> (boolean, default=True)</p>
<dd>yes: Ensures that when initiating a connection (as a client) the host name in the URL to which this connector connects to matches the host name in the digital certificate that the peer sends back as part of the SSL connection; no: Does not perform host name verification</p>
<dt><i>saslUsername</i> (string)</p>
<dd>The user name that the connector is using to connect to a peer.</p>
<dt><i>saslPassword</i> (string)</p>
<dd>The password that the connector is using to connect to a peer.</dl>
<h3>log</h3>
<p>Configure logging for a particular module. You can use the <i>UPDATE</i> operation to change log settings while the router is running.</p>
<dl>
<dt><i>module</i> (One of [&#8216;ROUTER&#8217;, &#8216;ROUTER_CORE&#8217;, &#8216;ROUTER_HELLO&#8217;, &#8216;ROUTER_LS&#8217;, &#8216;ROUTER_MA&#8217;, &#8216;MESSAGE&#8217;, &#8216;SERVER&#8217;, &#8216;AGENT&#8217;, &#8216;CONTAINER&#8217;, &#8216;CONFIG&#8217;, &#8216;ERROR&#8217;, &#8216;DISPATCH&#8217;, &#8216;POLICY&#8217;, &#8216;DEFAULT&#8217;], required)</p>
<dd>Module to configure. The special module &#8216;DEFAULT&#8217; specifies defaults for all modules.</p>
<dt><i>enable</i> (string, default=&#8217;default&#8217;, required)</p>
<dd>Levels are: trace, debug, info, notice, warning, error, critical. The enable string is a comma-separated list of levels. A level may have a trailing &#8216;+&#8217; to enable that level and above. For example &#8216;trace,debug,warning+&#8217; means enable trace, debug, warning, error and critical. The value &#8216;none&#8217; means disable logging for the module. The value &#8216;default&#8217; means use the value from the DEFAULT module.</p>
<dt><i>timestamp</i> (boolean)</p>
<dd>Include timestamp in log messages.</p>
<dt><i>source</i> (boolean)</p>
<dd>Include source file and line number in log messages.</p>
<dt><i>output</i> (string)</p>
<dd>Where to send log messages. Can be &#8216;stderr&#8217;, &#8216;syslog&#8217; or a file name.</dl>
<h3>fixedAddress</h3>
<p>(DEPRECATED) Establishes treatment for addresses starting with a prefix. This entity has been deprecated. Use address instead</p>
<dl>
<dt><i>prefix</i> (string, required)</p>
<dd>The address prefix (always starting with &#8216;/&#8217;).</p>
<dt><i>phase</i> (integer)</p>
<dd>The phase of a multi-hop address passing through one or more waypoints.</p>
<dt><i>fanout</i> (One of [&#8216;multiple&#8217;, &#8216;single&#8217;], default=&#8217;multiple&#8217;)</p>
<dd>One of &#8216;multiple&#8217; or &#8216;single&#8217;. Multiple fanout is a non-competing pattern. If there are multiple consumers using the same address, each consumer will receive its own copy of every message sent to the address. Single fanout is a competing pattern where each message is sent to only one consumer.</p>
<dt><i>bias</i> (One of [&#8216;closest&#8217;, &#8216;spread&#8217;], default=&#8217;closest&#8217;)</p>
<dd>Only if fanout is single. One of &#8216;closest&#8217; or &#8216;spread&#8217;. Closest bias means that messages to an address will always be delivered to the closest (lowest cost) subscribed consumer. Spread bias will distribute the messages across subscribers in an approximately even manner.</dl>
<h3>waypoint</h3>
<p>(DEPRECATED) A remote node that messages for an address pass through. This entity has been deprecated. Use autoLink instead</p>
<dl>
<dt><i>address</i> (string, required)</p>
<dd>The AMQP address of the waypoint.</p>
<dt><i>connector</i> (string, required)</p>
<dd>The name of the on-demand connector used to reach the waypoint&#8217;s container.</p>
<dt><i>inPhase</i> (integer, default=-1)</p>
<dd>The phase of the address as it is routed _to_ the waypoint.</p>
<dt><i>outPhase</i> (integer, default=-1)</p>
<dd>The phase of the address as it is routed _from_ the waypoint.</dl>
<h3>linkRoutePattern</h3>
<p>(DEPRECATED) An address pattern to match against link sources and targets to cause the router to link-route the attach across the network to a remote node. This entity has been deprecated. Use linkRoute instead</p>
<dl>
<dt><i>prefix</i> (string, required)</p>
<dd>An address prefix to match against target and source addresses. This pattern must be of the form &#8216;&lt;text&gt;.&lt;text1&gt;.&lt;textN&gt;&#8217; or &#8216;&lt;text&gt;&#8217; or &#8216;&lt;text&gt;.&#8217; and matches any address that contains that prefix. For example, if the prefix is set to org.apache (or org.apache.), any address that has the prefix &#8216;org.apache&#8217; (like org.apache.dev) will match. Note that a prefix must not start with a (.), can end in a (.) and can contain zero or more dots (.). Any characters between the dots are simply treated as part of the address</p>
<dt><i>dir</i> (One of [&#8216;in&#8217;, &#8216;out&#8217;, &#8216;both&#8217;], default=&#8217;both&#8217;)</p>
<dd>Link direction for match: &#8216;in&#8217; matches only links inbound to the client; &#8216;out&#8217; matches only links outbound from the client; &#8216;both&#8217; matches any link.</p>
<dt><i>connector</i> (string)</p>
<dd>The name of the on-demand connector used to reach the target node&#8217;s container. If this value is not provided, it means that the target container is expected to be connected to a different router in the network. This prevents links to a link-routable address from being misinterpreted as message-routing links when there is no route to a valid destination available.</dl>
<h3>address</h3>
<p>Entity type for address configuration. This is used to configure the treatment of message-routed deliveries within a particular address-space. The configuration controls distribution and address phasing.</p>
<dl>
<dt><i>prefix</i> (string, required)</p>
<dd>The address prefix for the configured settings</p>
<dt><i>distribution</i> (One of [&#8216;multicast&#8217;, &#8216;closest&#8217;, &#8216;balanced&#8217;], default=&#8217;balanced&#8217;)</p>
<dd>Treatment of traffic associated with the address</p>
<dt><i>waypoint</i> (boolean)</p>
<dd>Designates this address space as being used for waypoints. This will cause the proper address-phasing to be used.</p>
<dt><i>ingressPhase</i> (integer)</p>
<dd>Advanced &#8211; Override the ingress phase for this address</p>
<dt><i>egressPhase</i> (integer)</p>
<dd>Advanced &#8211; Override the egress phase for this address</dl>
<h3>linkRoute</h3>
<p>Entity type for link-route configuration. This is used to identify remote containers that shall be destinations for routed link-attaches. The link-routing configuration applies to an addressing space defined by a prefix.</p>
<dl>
<dt><i>prefix</i> (string, required)</p>
<dd>The address prefix for the configured settings</p>
<dt><i>containerId</i> (string)</p>
<dd>ContainerID for the target container</p>
<dt><i>connection</i> (string)</p>
<dd>The name from a connector or listener</p>
<dt><i>distribution</i> (One of [&#8216;linkBalanced&#8217;], default=&#8217;linkBalanced&#8217;)</p>
<dd>Treatment of traffic associated with the address</p>
<dt><i>dir</i> (One of [&#8216;in&#8217;, &#8216;out&#8217;], required)</p>
<dd>The permitted direction of links: &#8216;in&#8217; means client senders; &#8216;out&#8217; means client receivers</dl>
<h3>autoLink</h3>
<p>Entity type for configuring auto-links. Auto-links are links whose lifecycle is managed by the router. These are typically used to attach to waypoints on remote containers (brokers, etc.).</p>
<dl>
<dt><i>addr</i> (string, required)</p>
<dd>The address of the provisioned object</p>
<dt><i>dir</i> (One of [&#8216;in&#8217;, &#8216;out&#8217;], required)</p>
<dd>The direction of the link to be created. In means into the router, out means out of the router.</p>
<dt><i>phase</i> (integer)</p>
<dd>The address phase for this link. Defaults to &#8216;0&#8217; for &#8216;out&#8217; links and &#8216;1&#8217; for &#8216;in&#8217; links.</p>
<dt><i>containerId</i> (string)</p>
<dd>ContainerID for the target container</p>
<dt><i>connection</i> (string)</p>
<dd>The name from a connector or listener</dl>
<h3>console</h3>
<p>Start a websocket/tcp proxy and http file server to serve the web console</p>
<h3>policy</h3>
<p>Defines global connection limit</p>
<dl>
<dt><i>maximumConnections</i> (integer)</p>
<dd>Global maximum number of concurrent client connections allowed. Zero implies no limit. This limit is always enforced even if no other policy settings have been defined.</p>
<dt><i>enableAccessRules</i> (boolean)</p>
<dd>Enable user rule set processing and connection denial.</p>
<dt><i>policyFolder</i> (path)</p>
<dd>The path to a folder that holds policyRuleset definition .json files. For a small system the rulesets may all be defined in this file. At a larger scale it is better to have the policy files in their own folder and to have none of the rulesets defined here. All rulesets in all .json files in this folder are processed.</p>
<dt><i>defaultApplication</i> (string)</p>
<dd>Application policyRuleset to use for connections with no open.hostname or a hostname that does not match any existing policy. For users that don&#8217;t wish to use open.hostname or any multi-tennancy feature, this default policy can be the only policy in effect for the network.</p>
<dt><i>defaultApplicationEnabled</i> (boolean)</p>
<dd>Enable defaultApplication policy fallback logic.</dl>
<h3>policyRuleset</h3>
<p>Per application definition of the locations from which users may connect and the groups to which users belong.</p>
<dl>
<dt><i>maxConnections</i> (integer)</p>
<dd>Maximum number of concurrent client connections allowed. Zero implies no limit.</p>
<dt><i>maxConnPerUser</i> (integer)</p>
<dd>Maximum number of concurrent client connections allowed for any single user. Zero implies no limit.</p>
<dt><i>maxConnPerHost</i> (integer)</p>
<dd>Maximum number of concurrent client connections allowed for any remote host. Zero implies no limit.</p>
<dt><i>userGroups</i> (map)</p>
<dd>A map where each key is a user group name and the corresponding value is a CSV string naming the users in that group. Users who are assigned to one or more groups are deemed &#8216;restricted&#8217;. Restricted users are subject to connection ingress policy and are assigned policy settings based on the assigned user groups. Unrestricted users may be allowed or denied. If unrestricted users are allowed to connect then they are assigned to user group default.</p>
<dt><i>ingressHostGroups</i> (map)</p>
<dd>A map where each key is an ingress host group name and the corresponding value is a CSV string naming the IP addresses or address ranges in that group. IP addresses may be FQDN strings or numeric IPv4 or IPv6 host addresses. A host range is two host addresses of the same address family separated with a hyphen. The wildcard host address &#8216;*&#8217; represents any host address.</p>
<dt><i>ingressPolicies</i> (map)</p>
<dd>A map where each key is a user group name and the corresponding value is a CSV string naming the ingress host group names that restrict the ingress host for the user group. Users who are members of the user group are allowed to connect only from a host in one of the named ingress host groups.</p>
<dt><i>connectionAllowDefault</i> (boolean)</p>
<dd>Unrestricted users, those who are not members of a defined user group, are allowed to connect to this application. Unrestricted users are assigned to the &#8216;default&#8217; user group and receive &#8216;default&#8217; settings.</p>
<dt><i>settings</i> (map)</p>
<dd>A map where each key is a user group name and the value is a map of the corresponding settings for that group.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-qdrouterd/">qdrouterd</a>(8)</i>, <i><a href="/docs/linux/man/8-qdmanage/">qdmanage</a>(8)</i> </p>
<p> <i><a rel="nofollow" href="http://qpid.apache.org/components/dispatch-router">http://qpid.apache.org/components/dispatch-router</a></i></p>
<h2>Copyright</h2>
<p>2013, Apache Qpid &lt;<a rel="nofollow" href="http://qpid.apache.org/">http://qpid.apache.org/</a>&gt;</p>
