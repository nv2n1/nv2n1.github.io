---
title: "memcached_behavior_set(3)"
name: "memcached_behavior_set"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached_behavior_set/"
description: "memcached_behavior_set – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached_behavior_set &#8211; libmemcached Documentation </p>
<p> Manipulate the behavior of a memcached_st structure.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached/memcached.h&gt;</p>
<dl>
<dt><code>memcached_behavior_t</code></p>
<dd>
<dt><code>uint64_t memcached_behavior_get(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, <i>memcached_behavior_t</i><i>&nbsp;<wbr>flag</i>)</p>
<dd>
<dt><code>memcached_return_t memcached_behavior_set(memcached_st</code><i>&nbsp;<wbr>*ptr</i>, <i>memcached_behavior_t</i><i>&nbsp;<wbr>flag</i>, uint64_t<i>&nbsp;<wbr>data</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> behavior can be modified by using <i>memcached_behavior_set()</i>. Default behavior is the library strives to be quick and accurate. Some behavior, while being faster, can also result in not entirely accurate behavior (for instance, <code>memcached_set()</code> will always respond with <code>MEMCACHED_SUCCESS</code>). </p>
<p> <i>memcached_behavior_get()</i> takes a behavior flag and returns whether or not that behavior is currently enabled in the client. </p>
<p> <i>memcached_behavior_set()</i> changes the value of a particular option of the client. It takes both a flag (listed below) and a value. For simple on or off options you just need to pass in a value of 1. Calls to <i>memcached_behavior_set()</i> will flush and reset all connections.</p>
<dl>
<dt><code>MEMCACHED_BEHAVIOR_USE_UDP</code></p>
<dd>
<p> Causes <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> to use the UDP transport when communicating with a memcached server. Not all I/O operations are testsed when this behavior is enababled. The following operations will return <code>MEMCACHED_NOT_SUPPORTED</code> when executed with the <i>MEMCACHED_BEHAVIOR_USE_UDP</i> enabled: <code>memcached_version()</code>, <code>memcached_stat()</code>, <code>memcached_get()</code>, <code>memcached_get_by_key()</code>, <code>memcached_mget()</code>, <code>memcached_mget_by_key()</code>, <code>memcached_fetch()</code>, <code>memcached_fetch_result()</code>, <code>memcached_fetch_execute()</code>. </p>
<p> All other operations are testsed but are executed in a &#8216;fire-and-forget&#8217; mode, in which once the client has executed the operation, no attempt will be made to ensure the operation has been received and acted on by the server. </p>
<p> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> does not allow TCP and UDP servers to be shared within the same <a href="/docs/linux/man/3-libmemached/">libmemached</a>(3) client &#8216;instance&#8217;. An attempt to add a TCP server when this behavior is enabled will result in a <code>MEMCACHED_INVALID_HOST_PROTOCOL</code>, as will attempting to add a UDP server when this behavior has not been enabled.</p>
<dt><code>MEMCACHED_BEHAVIOR_NO_BLOCK</code></p>
<dd>
<p> Causes <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> to use asychronous IO. This is the fastest transport available for storage functions.</p>
<dt><code>MEMCACHED_BEHAVIOR_SND_TIMEOUT</code></p>
<dd>
<p> This sets the microsecond behavior of the socket against the SO_SNDTIMEO flag. In cases where you cannot use non-blocking IO this will allow you to still have timeouts on the sending of data.</p>
<dt><code>MEMCACHED_BEHAVIOR_RCV_TIMEOUT</code></p>
<dd>
<p> This sets the microsecond behavior of the socket against the SO_RCVTIMEO flag. </p>
<p> In cases where you cannot use non-blocking IO this will allow you to still have timeouts on the reading of data.</p>
<dt><code>MEMCACHED_BEHAVIOR_TCP_NODELAY</code></p>
<dd>
<p> Turns on the no-delay feature for connecting sockets (may be faster in some environments).</p>
<dt><code>MEMCACHED_BEHAVIOR_HASH</code></p>
<dd>
<p> Makes the default hashing algorithm for keys use MD5. The value can be set to either <code>MEMCACHED_HASH_DEFAULT</code>, <code>MEMCACHED_HASH_MD5</code>, <code>MEMCACHED_HASH_CRC</code>, <code>MEMCACHED_HASH_FNV1_64</code>, <code>MEMCACHED_HASH_FNV1A_64</code>, <code>MEMCACHED_HASH_FNV1_32</code>, <code>MEMCACHED_HASH_FNV1A_32</code>, <code>MEMCACHED_HASH_JENKINS</code>, <code>MEMCACHED_HASH_HSIEH</code>, and <code>MEMCACHED_HASH_MURMUR</code>. </p>
<p> Each hash has it&#8217;s advantages and it&#8217;s weaknesses. If you don&#8217;t know or don&#8217;t care, just go with the default. </p>
<p> Support for <code>MEMCACHED_HASH_HSIEH</code> is a compile time option that is disabled by default. To enable tests for this hashing algorithm, configure and build libmemcached with the &#8211;enable-hash_hsieh.</p>
<dt><code>MEMCACHED_BEHAVIOR_DISTRIBUTION</code></p>
<dd>
<p> Using this you can enable different means of distributing values to servers. </p>
<p> The default method is MEMCACHED_DISTRIBUTION_MODULA. You can enable consistent hashing by setting MEMCACHED_DISTRIBUTION_CONSISTENT. Consistent hashing delivers better distribution and allows servers to be added to the cluster with minimal cache losses. Currently MEMCACHED_DISTRIBUTION_CONSISTENT is an alias for the value MEMCACHED_DISTRIBUTION_CONSISTENT_KETAMA.</p>
<dt><code>MEMCACHED_BEHAVIOR_CACHE_LOOKUPS</code></p>
<dd>
<p> Deprecated since version 0.46(?): DNS lookups are now always cached until an error occurs with the server. </p>
<p> Memcached can cache named lookups so that DNS lookups are made only once. </p>
<dt><code>MEMCACHED_BEHAVIOR_SUPPORT_CAS</code></p>
<dd>
<p> Support CAS operations (this is not enabled by default at this point in the server since it imposes a slight performance penalty).</p>
<dt><code>MEMCACHED_BEHAVIOR_KETAMA</code></p>
<dd>
<p> Sets the default distribution to MEMCACHED_DISTRIBUTION_CONSISTENT_KETAMA and the hash to <code>MEMCACHED_HASH_MD5</code>.</p>
<dt><code>MEMCACHED_BEHAVIOR_KETAMA_WEIGHTED</code></p>
<dd> Sets the default distribution to MEMCACHED_DISTRIBUTION_CONSISTENT_KETAMA with the weighted tests. and the hash to MEMCACHED_HASH_MD5.</p>
<dt><code>MEMCACHED_BEHAVIOR_KETAMA_HASH</code></p>
<dd>
<p> Sets the hashing algorithm for host mapping on continuum. The value can be set to either <code>MEMCACHED_HASH_DEFAULT</code>, <code>MEMCACHED_HASH_MD5</code>, <code>MEMCACHED_HASH_CRC</code>, <code>MEMCACHED_HASH_FNV1_64</code>, <code>MEMCACHED_HASH_FNV1A_64</code>, <code>MEMCACHED_HASH_FNV1_32</code>, and <code>MEMCACHED_HASH_FNV1A_32</code>.</p>
<dt><code>MEMCACHED_BEHAVIOR_KETAMA_COMPAT</code></p>
<dd>
<p> Sets the compatibility mode. The value can be set to either MEMCACHED_KETAMA_COMPAT_LIBMEMCACHED (this is the default) or MEMCACHED_KETAMA_COMPAT_SPY to be compatible with the SPY Memcached client for Java.</p>
<dt><code>MEMCACHED_BEHAVIOR_POLL_TIMEOUT</code></p>
<dd>
<p> Modify the timeout value that is used by poll. The default value is -1. An signed int must be passed to memcached_behavior_set to change this value (this requires casting). For memcached_behavior_get a signed int value will be cast and returned as the unsigned long long.</p>
<dt><code>MEMCACHED_BEHAVIOR_USER_DATA</code></p>
<dd>
<p> Deprecated since version &lt;: 0.30</p>
<dt><code>MEMCACHED_BEHAVIOR_BUFFER_REQUESTS</code></p>
<dd>
<p> Enabling buffered IO causes commands to &quot;buffer&quot; instead of being sent. Any action that gets data causes this buffer to be be sent to the remote connection. Quiting the connection or closing down the connection will also cause the buffered data to be pushed to the remote connection.</p>
<dt><code>MEMCACHED_BEHAVIOR_VERIFY_KEY</code></p>
<dd>
<p> Enabling this will cause <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> to test all keys to verify that they are valid keys.</p>
<dt><code>MEMCACHED_BEHAVIOR_SORT_HOSTS</code></p>
<dd>
<p> Enabling this will cause hosts that are added to be placed in the host list in sorted order. This will defeat consisten hashing.</p>
<dt><code>MEMCACHED_BEHAVIOR_CONNECT_TIMEOUT</code></p>
<dd>
<p> In non-blocking mode this changes the value of the timeout during socket connection in milliseconds. Specifying -1 means an infinite time‐out.</p>
<dt><code>MEMCACHED_BEHAVIOR_BINARY_PROTOCOL</code></p>
<dd>
<p> Enable the use of the binary protocol. Please note that you cannot toggle this flag on an open connection.</p>
<dt><code>MEMCACHED_BEHAVIOR_SERVER_FAILURE_LIMIT</code></p>
<dd>
<p> Set this value to enable the server be removed after continuous MEMCACHED_BEHAVIOR_SERVER_FAILURE_LIMIT times connection failure.</p>
<dt><code>MEMCACHED_BEHAVIOR_IO_MSG_WATERMARK</code></p>
<dd>
<p> Set this value to tune the number of messages that may be sent before libmemcached should start to automatically drain the input queue. Setting this value to high, may cause libmemcached to deadlock (trying to send data, but the send will block because the input buffer in the kernel is full).</p>
<dt><code>MEMCACHED_BEHAVIOR_IO_BYTES_WATERMARK</code></p>
<dd>
<p> Set this value to tune the number of bytes that may be sent before libmemcached should start to automatically drain the input queue (need at least 10 IO requests sent without reading the input buffer). Setting this value to high, may cause libmemcached to deadlock (trying to send data, but the send will block because the input buffer in the kernel is full).</p>
<dt><code>MEMCACHED_BEHAVIOR_IO_KEY_PREFETCH</code></p>
<dd>
<p> The binary protocol works a bit different than the textual protocol in that a multiget is implemented as a pipe of single get-operations which are sent to the server in a chunk. If you are using large multigets from your application, you may improve the latency of the gets by setting this value so you send out the first chunk of requests when you hit the specified limit. It allows the servers to start processing the requests to send the data back while the rest of the requests are created and sent to the server.</p>
<dt><code>MEMCACHED_BEHAVIOR_NOREPLY</code></p>
<dd>
<p> Set this value to specify that you really don&#8217;t care about the result from your storage commands (set, add, replace, append, prepend).</p>
<dt><code>MEMCACHED_BEHAVIOR_NUMBER_OF_REPLICAS</code></p>
<dd>
<p> If you just want &quot;a poor mans HA&quot;, you may specify the numbers of replicas libmemcached should store of each item (on different servers). This replication does not dedicate certain memcached servers to store the replicas in, but instead it will store the replicas together with all of the other objects (on the &#8216;n&#8217; next servers specified in your server list).</p>
<dt><code>MEMCACHED_BEHAVIOR_RANDOMIZE_REPLICA_READ</code></p>
<dd>
<p> Allows randomizing the replica reads starting point. Normally the read is done from primary server and in case of miss the read is done from primary + 1, then primary + 2 all the way to &#8216;n&#8217; replicas. If this option is set on the starting point of the replica reads is randomized between the servers. This allows distributing read load to multiple servers with the expense of more write traffic.</p>
<dt><code>MEMCACHED_BEHAVIOR_CORK</code></p>
<dd>
<p> This open has been deprecated with the behavior now built and used appropriately on selected platforms.</p>
<dt><code>MEMCACHED_BEHAVIOR_KEEPALIVE</code></p>
<dd>
<p> Enable TCP_KEEPALIVE behavior.</p>
<dt><code>MEMCACHED_BEHAVIOR_KEEPALIVE_IDLE</code></p>
<dd>
<p> Specify time, in seconds, to mark a connection as idle. This is only available as an option Linux.</p>
<dt><code>MEMCACHED_BEHAVIOR_SOCKET_SEND_SIZE</code></p>
<dd>
<p> Find the current size of SO_SNDBUF. A value of 0 means either an error occured or no hosts were available. It is safe to assume system default if this occurs. If an error occurs you can checked the last cached errno statement to find the specific error.</p>
<dt><code>MEMCACHED_BEHAVIOR_SOCKET_RECV_SIZE</code></p>
<dd>
<p> Find the current size of SO_RCVBUF. A value of 0 means either an error occured or no hosts were available. It is safe to assume system default if this occurs. If an error occurs you can checked the last cached errno statement to find the specific error.</p>
<dt><code>MEMCACHED_BEHAVIOR_SERVER_FAILURE_LIMIT</code></p>
<dd>
<p> Deprecated since version 0.48: See <i>MEMCACHED_BEHAVIOR_REMOVE_FAILED_SERVERS</i> </p>
<p> This number of times a host can have an error before it is disabled. </p>
<dt><code>MEMCACHED_BEHAVIOR_AUTO_EJECT_HOSTS</code></p>
<dd>
<p> Deprecated since version 0.48: See <i>MEMCACHED_BEHAVIOR_REMOVE_FAILED_SERVERS</i> </p>
<p> If enabled any hosts which have been flagged as disabled will be removed from the list of servers in the memcached_st structure. This must be used in combination with MEMCACHED_BEHAVIOR_SERVER_FAILURE_LIMIT. </p>
<dt><code>MEMCACHED_BEHAVIOR_REMOVE_FAILED_SERVERS</code></p>
<dd> If enabled any hosts which have been flagged as disabled will be removed from the list of servers in the memcached_st structure.</p>
<dt><code>MEMCACHED_BEHAVIOR_RETRY_TIMEOUT</code></p>
<dd>
<p> When enabled a host which is problematic will only be checked for usage based on the amount of time set by this behavior. The value is in seconds.</p>
<dt><code>MEMCACHED_BEHAVIOR_HASH_WITH_PREFIX_KEY</code></p>
<dd>
<p> When enabled the prefix key will be added to the key when determining server by hash. See <code>MEMCACHED_CALLBACK_NAMESPACE</code> for additional information.</dl>
<h2>RETURN</h2>
<p> memcached_behavior_get returns either the current value of the get, or 0 or 1 on simple flag behaviors (1 being enabled). memcached_behavior_set returns failure or success.</p>
<h2>NOTES</h2>
<p> memcached_behavior_set in version .17 was changed from taking a pointer to data value, to taking a uin64_t.</p>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
