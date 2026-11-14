---
title: "mosquitto(8)"
name: "mosquitto"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mosquitto/"
description: "mosquitto – an MQTT broker"
---

<p>mosquitto &#8211; an MQTT broker</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>mosquitto</code> [-c&nbsp;<wbr><i>config file</i>] [-d | &#8211;daemon] [-p&nbsp;<wbr><i>port number</i>] [-v]</dl>
<h2>Description</h2>
<p><code>mosquitto</code></p>
<dd>is a broker for the MQTT protocol version 3.1.</p>
<h2>Options</h2>
<p><code>-c</code>, <code>&#8211;config-file</code></p>
<dl>
<dd>Load configuration from a file. If not given, the default values as described in <code><a href="/docs/linux/man/5-mosquitto-conf/">mosquitto.conf</a></code>(5) are used.</dl>
<p> <code>-d</code>, <code>&#8211;daemon</code></p>
<dl>
<dd>Run <code>mosquitto</code> in the background as a daemon. All other behaviour remains the same.</dl>
<p> <code>-p</code>, <code>&#8211;port</code></p>
<dl>
<dd>Listen on the port specified instead of the default 1883. This acts in addition to the port setting in the config file. May be specified multiple times to open multiple sockets listening on different ports. This socket will be bound to all network interfaces.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Use verbose logging. This is equivalent to setting <code>log_type</code> to <code>all</code> in the configuration file. This overrides and logging options given in the configuration file.</dl>
<h2>Configuration</h2>
<p>The broker can be configured using a configuration file as described in <code><a href="/docs/linux/man/5-mosquitto-conf/">mosquitto.conf</a></code>(5) and this is the main point of information for mosquitto. The files required for SSL/TLS support are described in <code><a href="/docs/linux/man/7-mosquitto-tls/">mosquitto-tls</a></code>(7).</p>
<h2>Broker Status</h2>
<p>Clients can find information about the broker by subscribing to topics in the $SYS hierarchy as follows. Topics marked as static are only sent once per client on subscription. All other topics are updated every <code>sys_interval</code> seconds. If <code>sys_interval</code> is 0, then updates are not sent. </p>
<p> Note that if you are using a command line client to interact with the $SYS topics and your shell interprets $ as an environment variable, you need to place the topic in single quotes &#8216;$SYS/&#8230;&#8217; or to escape the dollar symbol: \$SYS/&#8230; otherwise the $SYS will be treated as an environment variable. </p>
<p> <code>$SYS/broker/bytes/received</code></p>
<dl>
<dd>The total number of bytes received since the broker started.</dl>
<p> <code>$SYS/broker/bytes/sent</code></p>
<dl>
<dd>The total number of bytes sent since the broker started.</dl>
<p> <code>$SYS/broker/clients/connected</code>, <code>$SYS/broker/clients/active</code> (deprecated)</p>
<dl>
<dd>The number of currently connected clients.</dl>
<p> <code>$SYS/broker/clients/expired</code></p>
<dl>
<dd>The number of disconnected persistent clients that have been expired and removed through the persistent_client_expiration option.</dl>
<p> <code>$SYS/broker/clients/disconnected</code>, <code>$SYS/broker/clients/inactive</code> (deprecated)</p>
<dl>
<dd>The total number of persistent clients (with clean session disabled) that are registered at the broker but are currently disconnected.</dl>
<p> <code>$SYS/broker/clients/maximum</code></p>
<dl>
<dd>The maximum number of clients that have been connected to the broker at the same time.</dl>
<p> <code>$SYS/broker/clients/total</code></p>
<dl>
<dd>The total number of active and inactive clients currently connected and registered on the broker.</dl>
<p> <code>$SYS/broker/connection/#</code></p>
<dl>
<dd>When bridges are configured to/from the broker, common practice is to provide a status topic that indicates the state of the connection. This is provided within $SYS/broker/connection/ by default. If the value of the topic is 1 the connection is active, if 0 then it is not active. See the Bridges section below for more information on bridges.</dl>
<p> <code>$SYS/broker/heap/current size</code></p>
<dl>
<dd>The current size of the heap memory in use by mosquitto. Note that this topic may be unavailable depending on compile time options.</dl>
<p> <code>$SYS/broker/heap/maximum size</code></p>
<dl>
<dd>The largest amount of heap memory used by mosquitto. Note that this topic may be unavailable depending on compile time options.</dl>
<p> <code>$SYS/broker/load/connections/+</code></p>
<dl>
<dd>The moving average of the number of CONNECT packets received by the broker over different time intervals. The final &quot;+&quot; of the hierarchy can be 1min, 5min or 15min. The value returned represents the number of connections received in 1 minute, averaged over 1, 5 or 15 minutes.</dl>
<p> <code>$SYS/broker/load/bytes/received/+</code></p>
<dl>
<dd>The moving average of the number of bytes received by the broker over different time intervals. The final &quot;+&quot; of the hierarchy can be 1min, 5min or 15min. The value returned represents the number of bytes received in 1 minute, averaged over 1, 5 or 15 minutes.</dl>
<p> <code>$SYS/broker/load/bytes/sent/+</code></p>
<dl>
<dd>The moving average of the number of bytes sent by the broker over different time intervals. The final &quot;+&quot; of the hierarchy can be 1min, 5min or 15min. The value returned represents the number of bytes sent in 1 minute, averaged over 1, 5 or 15 minutes.</dl>
<p> <code>$SYS/broker/load/messages/received/+</code></p>
<dl>
<dd>The moving average of the number of all types of MQTT messages received by the broker over different time intervals. The final &quot;+&quot; of the hierarchy can be 1min, 5min or 15min. The value returned represents the number of messages received in 1 minute, averaged over 1, 5 or 15 minutes.</dl>
<p> <code>$SYS/broker/load/messages/sent/+</code></p>
<dl>
<dd>The moving average of the number of all types of MQTT messages sent by the broker over different time intervals. The final &quot;+&quot; of the hierarchy can be 1min, 5min or 15min. The value returned represents the number of messages send in 1 minute, averaged over 1, 5 or 15 minutes.</dl>
<p> <code>$SYS/broker/load/publish/dropped/+</code></p>
<dl>
<dd>The moving average of the number of publish messages dropped by the broker over different time intervals. This shows the rate at which durable clients that are disconnected are losing messages. The final &quot;+&quot; of the hierarchy can be 1min, 5min or 15min. The value returned represents the number of messages dropped in 1 minute, averaged over 1, 5 or 15 minutes.</dl>
<p> <code>$SYS/broker/load/publish/received/+</code></p>
<dl>
<dd>The moving average of the number of publish messages received by the broker over different time intervals. The final &quot;+&quot; of the hierarchy can be 1min, 5min or 15min. The value returned represents the number of publish messages received in 1 minute, averaged over 1, 5 or 15 minutes.</dl>
<p> <code>$SYS/broker/load/publish/sent/+</code></p>
<dl>
<dd>The moving average of the number of publish messages sent by the broker over different time intervals. The final &quot;+&quot; of the hierarchy can be 1min, 5min or 15min. The value returned represents the number of publish messages sent in 1 minute, averaged over 1, 5 or 15 minutes.</dl>
<p> <code>$SYS/broker/load/sockets/+</code></p>
<dl>
<dd>The moving average of the number of socket connections opened to the broker over different time intervals. The final &quot;+&quot; of the hierarchy can be 1min, 5min or 15min. The value returned represents the number of socket connections in 1 minute, averaged over 1, 5 or 15 minutes.</dl>
<p> <code>$SYS/broker/messages/inflight</code></p>
<dl>
<dd>The number of messages with QoS&gt;0 that are awaiting acknowledgments.</dl>
<p> <code>$SYS/broker/messages/received</code></p>
<dl>
<dd>The total number of messages of any type received since the broker started.</dl>
<p> <code>$SYS/broker/messages/sent</code></p>
<dl>
<dd>The total number of messages of any type sent since the broker started.</dl>
<p> <code>$SYS/broker/messages/stored</code></p>
<dl>
<dd>The number of messages currently held in the message store. This includes retained messages and messages queued for durable clients.</dl>
<p> <code>$SYS/broker/publish/messages/dropped</code></p>
<dl>
<dd>The total number of publish messages that have been dropped due to inflight/queuing limits. See the max_inflight_messages and max_queued_messages options in <code><a href="/docs/linux/man/5-mosquitto-conf/">mosquitto.conf</a></code>(5) for more information.</dl>
<p> <code>$SYS/broker/publish/messages/received</code></p>
<dl>
<dd>The total number of PUBLISH messages received since the broker started.</dl>
<p> <code>$SYS/broker/publish/messages/sent</code></p>
<dl>
<dd>The total number of PUBLISH messages sent since the broker started.</dl>
<p> <code>$SYS/broker/retained messages/count</code></p>
<dl>
<dd>The total number of retained messages active on the broker.</dl>
<p> <code>$SYS/broker/subscriptions/count</code></p>
<dl>
<dd>The total number of subscriptions active on the broker.</dl>
<p> <code>$SYS/broker/timestamp</code></p>
<dl>
<dd>The timestamp at which this particular build of the broker was made. Static.</dl>
<p> <code>$SYS/broker/uptime</code></p>
<dl>
<dd>The amount of time in seconds the broker has been online.</dl>
<p> <code>$SYS/broker/version</code></p>
<dl>
<dd>The version of the broker. Static.</dl>
<h2>Wildcard Topic Subscriptions</h2>
<p>In addition to allowing clients to subscribe to specific topics, mosquitto also allows the use of two wildcards in subscriptions. <code>+</code> is the wildcard used to match a single level of hierarchy. For example, for a topic of &quot;a/b/c/d&quot;, the following example subscriptions will match: </p>
<dl>
<dd>&bull; a/b/c/d</dl>
<dl>
<dd>&bull; +/b/c/d</dl>
<dl>
<dd>&bull; a/+/c/d</dl>
<dl>
<dd>&bull; a/+/+/d</dl>
<dl>
<dd>&bull; +/+/+/+</dl>
<p> The following subscriptions will not match: </p>
<dl>
<dd>&bull; a/b/c</dl>
<dl>
<dd>&bull; b/+/c/d</dl>
<dl>
<dd>&bull; +/+/+</dl>
<p> The second wildcard is <code>#</code> and is used to match all subsequent levels of hierarchy. With a topic of &quot;a/b/c/d&quot;, the following example subscriptions will match: </p>
<dl>
<dd>&bull; a/b/c/d</dl>
<dl>
<dd>&bull; #</dl>
<dl>
<dd>&bull; a/#</dl>
<dl>
<dd>&bull; a/b/#</dl>
<dl>
<dd>&bull; a/b/c/#</dl>
<dl>
<dd>&bull; +/b/c/#</dl>
<p> The $SYS hierarchy does not match a subscription of &quot;#&quot;. If you want to observe the entire $SYS hierarchy, subscribe to $SYS/#. </p>
<p> Note that the wildcards must be only ever used on their own, so a subscription of &quot;a/b+/c&quot; is not valid use of a wildcard. The <code>#</code> wildcard must only ever be used as the final character of a subscription.</p>
<h2>Bridges</h2>
<p>Multiple brokers can be connected together with the bridging functionality. This is useful where it is desirable to share information between locations, but where not all of the information needs to be shared. An example could be where a number of users are running a broker to help record power usage and for a number of other reasons. The power usage could be shared through bridging all of the user brokers to a common broker, allowing the power usage of all users to be collected and compared. The other information would remain local to each broker. </p>
<p> For information on configuring bridges, see <code><a href="/docs/linux/man/5-mosquitto-conf/">mosquitto.conf</a></code>(5).</p>
<h2>Signals</h2>
<p>SIGHUP</p>
<dl>
<dd>Upon receiving the SIGHUP signal, mosquitto will attempt to reload configuration file data, assuming that the <code>-c</code> argument was provided when mosquitto was started. Not all configuration parameters can be reloaded without restarting. See <code><a href="/docs/linux/man/5-mosquitto-conf/">mosquitto.conf</a></code>(5) for details.</dl>
<p> SIGUSR1</p>
<dl>
<dd>Upon receiving the SIGUSR1 signal, mosquitto will write the persistence database to disk. This signal is only acted upon if persistence is enabled.</dl>
<p> SIGUSR2</p>
<dl>
<dd>The SIGUSR2 signal causes mosquitto to print out the current subscription tree, along with information about where retained messages exist. This is intended as a testing feature only and may be removed at any time.</dl>
<h2>Files</h2>
<p>/etc/mosquitto/mosquitto.conf</p>
<dl>
<dd>Configuration file. See <code><a href="/docs/linux/man/5-mosquitto-conf/">mosquitto.conf</a></code>(5).</dl>
<p> /var/lib/mosquitto/mosquitto.db</p>
<dl>
<dd>Persistent message data storage location if persist enabled.</dl>
<p> /etc/hosts.allow, /etc/hosts.deny</p>
<dl>
<dd>Host access control via tcp-wrappers as described in <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5).</dl>
<h2>Bugs</h2>
<p><code>mosquitto</code> bug information can be found at <a rel="nofollow" href="https://bugs.eclipse.org/bugs/describecomponents.cgi?product=Mosquitto">https://bugs.eclipse.org/bugs/describecomponents.cgi?product=Mosquitto</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-mqtt/">mqtt</a></code>(7), <code><a href="/docs/linux/man/7-mosquitto-tls/">mosquitto-tls</a></code>(7), <code><a href="/docs/linux/man/5-mosquitto-conf/">mosquitto.conf</a></code>(5), <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5), <code><a href="/docs/linux/man/1-mosquitto_passwd/">mosquitto_passwd</a></code>(1), <code><a href="/docs/linux/man/1-mosquitto_pub/">mosquitto_pub</a></code>(1), <code><a href="/docs/linux/man/1-mosquitto_sub/">mosquitto_sub</a></code>(1), <code><a href="/docs/linux/man/3-libmosquitto/">libmosquitto</a></code>(3)</p>
<h2>Thanks</h2>
<p>Thanks to Andy Stanford-Clark for being one of the people who came up with MQTT in the first place. Thanks to Andy and Nicholas O&#8217;Leary for providing clarifications of the protocol. </p>
<p> Thanks also to everybody at the Ubuntu UK Podcast and Linux Outlaws for organising OggCamp, where Andy gave a talk that inspired mosquitto.</p>
<h2>Author</h2>
<p>Roger Light &lt;roger [at] atchoo.org&gt;</p>
