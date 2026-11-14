---
title: "mqtt(7)"
name: "mqtt"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mqtt/"
description: "mqtt – MQ Telemetry Transport"
---

<p>mqtt &#8211; MQ Telemetry Transport</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>MQTT</code></dl>
<h2>Description</h2>
<p><code>MQTT</code></p>
<dd>is a lightweight publish/subscribe messaging protocol. It is useful for use with low power sensors, but is applicable to many scenarios. </p>
<p> This manual describes some of the features of MQTT version 3.1, to assist end users in getting the most out of the protocol. For more complete information on MQTT, see <a rel="nofollow" href="http://mqtt.org/.">http://mqtt.org/.</a></p>
<h2>Publish/Subscribe</h2>
<p>The MQTT protocol is based on the principle of publishing messages and subscribing to topics, or &quot;pub/sub&quot;. Multiple clients connect to a broker and subscribe to topics that they are interested in. Clients also connect to the broker and publish messages to topics. Many clients may subscribe to the same topics and do with the information as they please. The broker and MQTT act as a simple, common interface for everything to connect to. This means that you if you have clients that dump subscribed messages to a database, to Twitter, Cosm or even a simple text file, then it becomes very simple to add new sensors or other data input to a database, Twitter or so on.</p>
<h2>Topics/Subscriptions</h2>
<p>Messages in MQTT are published on topics. There is no need to configure a topic, publishing on it is enough. Topics are treated as a hierarchy, using a slash (/) as a separator. This allows sensible arrangement of common themes to be created, much in the same way as a filesystem. For example, multiple computers may all publish their hard drive temperature information on the following topic, with their own computer and hard drive name being replaced as appropriate: </p>
<dl>
<dd>&bull; sensors/COMPUTER_NAME/temperature/HARDDRIVE_NAME</dl>
<p> Clients can receive messages by creating subscriptions. A subscription may be to an explicit topic, in which case only messages to that topic will be received, or it may include wildcards. Two wildcards are available, <code>+</code> or <code>#</code>. </p>
<p> <code>+</code> can be used as a wildcard for a single level of hierarchy. It could be used with the topic above to get information on all computers and hard drives as follows: </p>
<dl>
<dd>&bull; sensors/+/temperature/+</dl>
<p> As another example, for a topic of &quot;a/b/c/d&quot;, the following example subscriptions will match: </p>
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
<p> <code>#</code> can be used as a wildcard for all remaining levels of hierarchy. This means that it must be the final character in a subscription. With a topic of &quot;a/b/c/d&quot;, the following example subscriptions will match: </p>
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
<p> Zero length topic levels are valid, which can lead to some slightly non-obvious behaviour. For example, a topic of &quot;a//topic&quot; would correctly match against a subscription of &quot;a/+/topic&quot;. Likewise, zero length topic levels can exist at both the beginning and the end of a topic string, so &quot;/a/topic&quot; would match against a subscription of &quot;+/a/topic&quot;, &quot;#&quot; or &quot;/#&quot;, and a topic &quot;a/topic/&quot; would match against a subscription of &quot;a/topic/+&quot; or &quot;a/topic/#&quot;.</p>
<h2>Quality Of Service</h2>
<p>MQTT defines three levels of Quality of Service (QoS). The QoS defines how hard the broker/client will try to ensure that a message is received. Messages may be sent at any QoS level, and clients may attempt to subscribe to topics at any QoS level. This means that the client chooses the maximum QoS it will receive. For example, if a message is published at QoS 2 and a client is subscribed with QoS 0, the message will be delivered to that client with QoS 0. If a second client is also subscribed to the same topic, but with QoS 2, then it will receive the same message but with QoS 2. For a second example, if a client is subscribed with QoS 2 and a message is published on QoS 0, the client will receive it on QoS 0. </p>
<p> Higher levels of QoS are more reliable, but involve higher latency and have higher bandwidth requirements. </p>
<dl>
<dd>&bull; 0: The broker/client will deliver the message once, with no confirmation.</dl>
<dl>
<dd>&bull; 1: The broker/client will deliver the message at least once, with confirmation required.</dl>
<dl>
<dd>&bull; 2: The broker/client will deliver the message exactly once by using a four step handshake.</dl>
<h2>Retained Messages</h2>
<p>All messages may be set to be retained. This means that the broker will keep the message even after sending it to all current subscribers. If a new subscription is made that matches the topic of the retained message, then the message will be sent to the client. This is useful as a &quot;last known good&quot; mechanism. If a topic is only updated infrequently, then without a retained message, a newly subscribed client may have to wait a long time to receive an update. With a retained message, the client will receive an instant update.</p>
<h2>Clean Session / Durable Connections</h2>
<p>On connection, a client sets the &quot;clean session&quot; flag, which is sometimes also known as the &quot;clean start&quot; flag. If clean session is set to false, then the connection is treated as durable. This means that when the client disconnects, any subscriptions it has will remain and any subsequent QoS 1 or 2 messages will be stored until it connects again in the future. If clean session is true, then all subscriptions will be removed for the client when it disconnects.</p>
<h2>Wills</h2>
<p>When a client connects to a broker, it may inform the broker that it has a will. This is a message that it wishes the broker to send when the client disconnects unexpectedly. The will message has a topic, QoS and retain status just the same as any other message.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mosquitto/">mosquitto</a></code>(8), <code><a href="/docs/linux/man/1-mosquitto_pub/">mosquitto_pub</a></code>(1), <code><a href="/docs/linux/man/1-mosquitto_sub/">mosquitto_sub</a></code>(1)</p>
<h2>Author</h2>
<p>Roger Light &lt;roger [at] atchoo.org&gt;</p>
