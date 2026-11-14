---
title: "mongoc_uri_t(3)"
name: "mongoc_uri_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_uri_t/"
description: "mongoc_uri_t – mongoc_uri_t provides an abstraction on top of the MongoDB connection URI format. It provides standardized parsing as well as convenience methods for extracting useful information su..."
---

<p>mongoc_uri_t &#8211; mongoc_uri_t provides an abstraction on top of the MongoDB connection URI format. It provides standardized parsing as well as convenience methods for extracting useful information such as replica hosts or authorization information.</p>
<h2>Synopsis</h2>
<pre>typedef struct _mongoc_uri_t mongoc_uri_t;</pre>
<h2>Description</h2>
<p><code>mongoc_uri_t</code> provides an abstraction on top of the MongoDB connection URI format. It provides standardized parsing as well as convenience methods for extracting useful information such as replica hosts or authorization information. </p>
<p> See <code>Connection String URI Reference</code> on the MongoDB website for more information. </p>
<h2>Format</h2>
<pre>mongodb:// &lt;1&gt;
 [username:password@] &lt;2&gt;
 host1 &lt;3&gt;
 [:port1] &lt;4&gt;
 [,host2[:port2],...[,hostN[:portN]]] &lt;5&gt;
 [/[database] &lt;6&gt;
 [?options]] &lt;7&gt;</pre>
<dl COMPACT>
<dt>\[bu]</p>
<dd>mongodb is the specifier of the MongoDB protocol.</p>
<dt>\[bu]</p>
<dd>An optional username and password.</p>
<dt>\[bu]</p>
<dd>The only required part of the uri. This specifies either a hostname, IP address or UNIX domain socket.</p>
<dt>\[bu]</p>
<dd>An optional port number. Defaults to :27017.</p>
<dt>\[bu]</p>
<dd>Extra optional hosts and ports. You would specify multiple hosts, for example, for connections to replica sets.</p>
<dt>\[bu]</p>
<dd>The name of the database to authenticate if the connection string includes authentication credentials. If /database is not specified and the connection string includes credentials, defaults to the &#8216;admin&#8217; database.</p>
<dt>\[bu]</p>
<dd>Connection specific options. </p>
</dl>
<h2>Replica Set Example</h2>
<p>To describe a connection to a replica set named &#8216;test&#8217; with the following mongod hosts: </p>
<dl COMPACT>
<dt>\[bu]</p>
<dd><code>db1.example.com</code> on port <code>27017</code></p>
<dt>\[bu]</p>
<dd><code>db2.example.com</code> on port <code>2500</code> </p>
<p> You would use the connection string that resembles the following. </p>
<pre>mongodb://db1.example.com,db2.example.com:2500/?replicaSet=test</pre>
</dl>
<h2>Connection Options</h2>
<dl COMPACT>
<dt><code>ssl</code></p>
<dd>{true|false}, indicating if SSL must be used. (See also <code>mongoc_client_set_ssl_opts</code> and <code>mongoc_client_pool_set_ssl_opts</code> \&amp;.)</dl>
<dl COMPACT>
<dt><code>connectTimeoutMS</code></p>
<dd>A timeout in milliseconds to attempt a connection before timing out. This setting applies to server discovery and monitoring connections as well as to connections for application operations. The default is 10 seconds.</dl>
<dl COMPACT>
<dt><code>socketTimeoutMS</code></p>
<dd>The time in milliseconds to attempt to send or receive on a socket before the attempt times out. The default is 5 minutes.</dl>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>Setting any of the *TimeoutMS options above to <code>0</code> will be interpreted as &quot;use the default value&quot; </p>
</dl>
<h2>Server Discovery, Monitoring, And Selection Options</h2>
<p><code>NOTE</code></p>
<dl COMPACT>
<dd>Clients in a <code>mongoc_client_pool_t</code> share a topology scanner that runs on a background thread. The thread wakes every <code>heartbeatFrequencyMS</code> (default 10 seconds) to scan all MongoDB servers in parallel. Whenever an application operation requires a server that is not known&#8211;for example, if there is no known primary and your application attempts an insert&#8211;the thread rescans all servers every half-second. In this situation the pooled client waits up to <code>serverSelectionTimeoutMS</code> (default 30 seconds) for the thread to find a server suitable for the operation, then returns an error with domain <code>MONGOC_ERROR_SERVER_SELECTION</code> \&amp;. </p>
<p> Technically, the total time an operation may wait while a pooled client scans the topology is controlled both by <code>serverSelectionTimeoutMS</code> and <code>connectTimeoutMS</code> \&amp;. The longest wait occurs if the last scan begins just at the end of the selection timeout, and a slow or down server requires the full connection timeout before the client gives up. </p>
<p> A non-pooled client is single-threaded. Every <code>heartbeatFrequencyMS</code> , it blocks the next application operation while it does a parallel scan. This scan takes as long as needed to check the slowest server: roughly <code>connectTimeoutMS</code> \&amp;. Therefore the default <code>heartbeatFrequencyMS</code> for single-threaded clients is greater than for pooled clients: 60 seconds. </p>
<p> By default, single-threaded (non-pooled) clients scan only once when an operation requires a server that is not known. If you attempt an insert and there is no known primary, the client checks all servers once trying to find it, then succeeds or returns an error with domain <code>MONGOC_ERROR_SERVER_SELECTION</code> \&amp;. But if you set <code>serverSelectionTryOnce</code> to &quot;false&quot;, the single-threaded client loops, checking all servers every half-second, until <code>serverSelectionTimeoutMS</code> \&amp;. </p>
<p> The total time an operation may wait for a single-threaded client to scan the topology is determined by <code>connectTimeoutMS</code> in the try-once case, or <code>serverSelectionTimeoutMS</code> and <code>connectTimeoutMS</code> if <code>serverSelectionTryOnce</code> is set &quot;false&quot;. </p>
</dl>
<dl COMPACT>
<dt><code>heartbeatFrequencyMS</code></p>
<dd>The interval between server monitoring checks. Defaults to 10 seconds in pooled (multi-threaded) mode, 60 seconds in non-pooled mode (single-threaded).</dl>
<dl COMPACT>
<dt><code>serverSelectionTimeoutMS</code></p>
<dd>A timeout in milliseconds to block for server selection before throwing an exception. The default is 30 seconds.</dl>
<dl COMPACT>
<dt><code>serverSelectionTryOnce</code></p>
<dd>If &quot;true&quot;, the driver scans the topology exactly once after server selection fails, then either selects a server or returns an error. If it is false, then the driver repeatedly searches for a suitable server for up to <code>serverSelectionTimeoutMS</code> milliseconds (pausing a half second between attempts). The default for <code>serverSelectionTryOnce</code> is &quot;false&quot; for pooled clients, otherwise &quot;true&quot;. Pooled clients ignore serverSelectionTryOnce; they signal the thread to rescan the topology every half-second until serverSelectionTimeoutMS expires.</dl>
<dl COMPACT>
<dt><code>socketCheckIntervalMS</code></p>
<dd>Only applies to single threaded clients. If a socket has not been used within this time, its connection is checked with a quick &quot;isMaster&quot; call before it is used again. Defaults to 5 seconds.</dl>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd>Setting any of the *TimeoutMS options above to <code>0</code> will be interpreted as &quot;use the default value&quot; </p>
</dl>
<h2>Connection Pool Options</h2>
<dl COMPACT>
<dt><code>maxPoolSize</code></p>
<dd>The maximum number of connections in the pool. The default value is 100.</dl>
<dl COMPACT>
<dt><code>minPoolSize</code></p>
<dd>The minimum number of connections in the connection pool. Default value is 0. These are lazily created.</dl>
<dl COMPACT>
<dt><code>maxIdleTimeMS</code></p>
<dd>Not implemented.</dl>
<dl COMPACT>
<dt><code>waitQueueMultiple</code></p>
<dd>Not implemented.</dl>
<dl COMPACT>
<dt><code>waitQueueTimeoutMS</code></p>
<dd>Not implemented.</dl>
<h2>Write Concern Options</h2>
<dl COMPACT>
<dt><code>w</code></p>
<dd>
<dt><code>0</code></p>
<dd>The driver will not acknowledge write operations but will pass or handle any network and socket errors that it receives to the client. If you disable write concern but enable the getLastError command’s w option, w overrides the w option.</dl>
<dl COMPACT>
<dt><code>1</code></p>
<dd>Provides basic acknowledgment of write operations. By specifying 1, you require that a standalone mongod instance, or the primary for replica sets, acknowledge all write operations. For drivers released after the default write concern change, this is the default write concern setting.</dl>
<dl COMPACT>
<dt><code>majority</code></p>
<dd>For replica sets, if you specify the special majority value to w option, write operations will only return successfully after a majority of the configured replica set members have acknowledged the write operation.</dl>
<dl COMPACT>
<dt><code>n</code></p>
<dd>For replica sets, if you specify a number n greater than 1, operations with this write concern return only after n members of the set have acknowledged the write. If you set n to a number that is greater than the number of available set members or members that hold data, MongoDB will wait, potentially indefinitely, for these members to become available.</dl>
<dl COMPACT>
<dt><code>tags</code></p>
<dd>For replica sets, you can specify a tag set to require that all members of the set that have these tags configured return confirmation of the write operation.</dl>
<dl COMPACT>
<dt><code>wtimeoutMS</code></p>
<dd>The time in milliseconds to wait for replication to succeed, as specified in the w option, before timing out. When wtimeoutMS is 0, write operations will never time out.</dl>
<dl COMPACT>
<dt><code>journal</code></p>
<dd>Controls whether write operations will wait until the mongod acknowledges the write operations and commits the data to the on disk journal.</p>
<dt><code>true</code></p>
<dd>Enables journal commit acknowledgment write concern. Equivalent to specifying the getLastError command with the j option enabled.</dl>
<dl COMPACT>
<dt><code>false</code></p>
<dd>Does not require that mongod commit write operations to the journal before acknowledging the write operation. This is the default option for the journal parameter.</dl>
<h2>Read Concern Options</h2>
<dl COMPACT>
<dt><code>readConcernLevel</code></p>
<dd>The level of isolation for read operations. If the level is left unspecified, the server default will be used. See the <code>readConcern in the MongoDB Manual</code> for details.</dl>
<h2>Read Preference Options</h2>
<dl COMPACT>
<dt><code>readPreference</code></p>
<dd>Specifies the replica set read preference for this connection. This setting overrides any slaveOk value. The read preference values are the following:</p>
<dt>\[bu]</p>
<dd>primary</p>
<dt>\[bu]</p>
<dd>primaryPreferred</p>
<dt>\[bu]</p>
<dd>secondary</p>
<dt>\[bu]</p>
<dd>secondaryPreferred</p>
<dt>\[bu]</p>
<dd>nearest</dl>
<dl COMPACT>
<dt><code>readPreferenceTags</code></p>
<dd>Specifies a tag set as a comma-seperated list of colon-separted key-value pairs.</dl>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
