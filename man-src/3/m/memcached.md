---
title: "memcached(3)"
name: "memcached"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memcached/"
description: "memcached – libmemcached Documentation"
---

<h2>NAME</h2>
<p> memcached &#8211; libmemcached Documentation</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;libmemcached-1.0/memcached.h&gt;</p>
<dl>
<dt><code>LIBMEMCACHED</code></p>
<dd>
<dt><code>memcached_st *memcached(const char</code><i>&nbsp;<wbr>*string</i>, size_t<i>&nbsp;<wbr>string_length</i>)</p>
<dd>
<dt><code>memcached_return_t libmemcached_check_configuration(const char</code><i>&nbsp;<wbr>*option_string</i>, size_t<i>&nbsp;<wbr>length</i>, char<i>&nbsp;<wbr>*error_buffer</i>, size_t<i>&nbsp;<wbr>error_buffer_size</i>)</p>
<dd>
<p> Compile and link with -lmemcached</dl>
<h2>DESCRIPTION</h2>
<p> Libmemcached implements a custom language for configuring and modifying servers. By passing in an option string you can generate a <code>memcached_st</code> object that you can use in your application directly.</p>
<dl>
<dt><code>&#8211;SERVER=&lt;servername&gt;:&lt;optional_port&gt;/?&lt;optional_weight&gt;</code></p>
<dd>
<p> Provide a servername to be used by the client. Providing a weight will cause weighting to occur with all hosts with each server getting a default weight of 1.</p>
<dt><code>&#8211;SOCKET=&lt;filepath&gt;/?&lt;optional_weight&gt;</code></p>
<dd>
<p> Provide a filepath to a UNIX socket file. Providing a weight will cause weighting to occur with all hosts with each server getting a default weight of 1.</p>
<dt><code>&#8211;VERIFY-KEY</code></p>
<dd>
<p> Verify that keys that are being used fit within the design of the protocol being used.</p>
<dt><code>&#8211;REMOVE_FAILED_SERVERS</code></p>
<dd>
<p> Enable the behavior <code>MEMCACHED_BEHAVIOR_REMOVE_FAILED_SERVERS</code>.</p>
<dt><code>&#8211;BINARY-PROTOCOL</code></p>
<dd>
<p> Force all connections to use the binary protocol.</p>
<dt><code>&#8211;BUFFER-REQUESTS</code></p>
<dd>
<p> Please see <code>MEMCACHED_BEHAVIOR_BUFFER_REQUESTS</code>.</p>
<dt><code>&#8211;CONFIGURE-FILE=</code></p>
<dd>
<p> Provide a configuration file to be used to load requests. Beware that by using a configuration file libmemcached will reset memcached_st based on information only contained in the file.</p>
<dt><code>&#8211;CONNECT-TIMEOUT=</code></p>
<dd>
<p> Please see <code>MEMCACHED_BEHAVIOR_CONNECT_TIMEOUT</code>.</p>
<dt><code>&#8211;DISTRIBUTION=</code></p>
<dd>
<p> Set the distribution model used by the client. See :manpage:&#8220; for more details.</p>
<dt><code>&#8211;HASH=</code></p>
<dd>
<p> Set the hashing alogrthm used for placing keys on servers.</p>
<dt><code>&#8211;HASH-WITH-NAMESPACE</code></p>
<dd>
<p> When enabled the prefix key will be added to the key when determining which server to store the data in.</p>
<dt><code>&#8211;NOREPLY</code></p>
<dd>
<p> Enable &quot;no reply&quot; for all calls that support this. It is highly recommended that you use this option with the binary protocol only.</p>
<dt><code>&#8211;NUMBER-OF-REPLICAS=</code></p>
<dd>
<p> Set the nummber of servers that keys will be replicated to.</p>
<dt><code>&#8211;RANDOMIZE-REPLICA-READ</code></p>
<dd>
<p> Select randomly the server within the replication pool to read from.</p>
<dt><code>&#8211;SORT-HOSTS</code></p>
<dd>
<p> When adding new servers always calculate their distribution based on sorted naming order.</p>
<dt><code>&#8211;SUPPORT-CAS</code></p>
<dd>
<p> See <i><a href="/docs/linux/man/3-memcached_behavior_set/">memcached_behavior_set</a>(3)</i> for <code>MEMCACHED_BEHAVIOR_SUPPORT_CAS</code></p>
<dt><code>&#8211;USE-UDP</code></p>
<dd>
<p> See <i><a href="/docs/linux/man/3-memcached_behavior_set/">memcached_behavior_set</a>(3)</i> for <code>MEMCACHED_BEHAVIOR_USE_UDP</code></p>
<dt><code>&#8211;NAMESPACE=</code></p>
<dd>
<p> A namespace is a container that provides context for keys, only other requests that know the namespace can access these values. This is accomplished by prepending the namespace value to all keys.</dl>
<h3>Mecached Pool Options:</h3>
<dl>
<dt><code>&#8211;POOL-MIN</code></p>
<dd>
<p> Initial size of pool.</p>
<dt><code>&#8211;POOL-MAX</code></p>
<dd>
<p> Maximize size of the pool.</dl>
<h3>I/O Options:</h3>
<dl>
<dt><code>&#8211;TCP-NODELAY</code></p>
<dd>
<p> See <i><a href="/docs/linux/man/3-memcached_behavior_set/">memcached_behavior_set</a>(3)</i> for MEMCACHED_BEHAVIOR_TCP_NODELAY</p>
<dt><code>&#8211;TCP-KEEPALIVE</code></p>
<dd>
<p> See <i><a href="/docs/linux/man/3-memcached_behavior_set/">memcached_behavior_set</a>(3)</i> for MEMCACHED_BEHAVIOR_TCP_KEEPALIVE</p>
<dt><code>&#8211;RETRY-TIMEOUT=</code></p>
<dd>
<p> See <i><a href="/docs/linux/man/3-memcached_behavior_set/">memcached_behavior_set</a>(3)</i> for MEMCACHED_BEHAVIOR_RETRY_TIMEOUT</p>
<dt><code>&#8211;SERVER-FAILURE-LIMIT=</code></p>
<dd>
<p> See <i><a href="/docs/linux/man/3-memcached_behavior_set/">memcached_behavior_set</a>(3)</i> for MEMCACHED_BEHAVIOR_SERVER_FAILURE_LIMIT</p>
<dt><code>&#8211;SND-TIMEOUT=</code></p>
<dd>
<p> See <i><a href="/docs/linux/man/3-memcached_behavior_set/">memcached_behavior_set</a>(3)</i> for MEMCACHED_BEHAVIOR_SND_TIMEOUT</p>
<dt><code>&#8211;SOCKET-RECV-SIZE=</code></p>
<dd>
<p> See <i><a href="/docs/linux/man/3-memcached_behavior_set/">memcached_behavior_set</a>(3)</i> for MEMCACHED_BEHAVIOR_SOCKET_RECV_SIZE</p>
<dt><code>&#8211;SOCKET-SEND-SIZE=</code></p>
<dd>
<p> See <i><a href="/docs/linux/man/3-memcached_behavior_set/">memcached_behavior_set</a>(3)</i> for MEMCACHED_BEHAVIOR_SOCKET_SEND_SIZE</p>
<dt><code>&#8211;POLL-TIMEOUT=</code></p>
<dd>
<p> That sets the value of the timeout used by :manpage: <i>poll()</i>.</p>
<dt><code>&#8211;IO-BYTES-WATERMARK=</code></p>
<dd>
<dt><code>&#8211;IO-KEY-PREFETCH=</code></p>
<dd>
<dt><code>&#8211;IO-MSG-WATERMARK=</code></p>
<dd>
<dt><code>&#8211;TCP-KEEPIDLE</code></p>
<dd>
<dt><code>&#8211;RCV-TIMEOUT=</code></p>
<dd></dl>
<h3>Other:</h3>
<dl>
<dt><code>INCLUDE</code></p>
<dd>
<p> Include a file in configuration. Unlike &#8211;CONFIGURE-FILE= this will not reset memcached_st</p>
<dt><code>RESET</code></p>
<dd>
<p> Reset memcached_st and continue to process.</p>
<dt><code>END</code></p>
<dd>
<p> End configutation processing.</p>
<dt><code>ERROR</code></p>
<dd>
<p> End configutation processing and throw an error.</dl>
<h2>RETURN</h2>
<p> <i>memcached()</i> returns a pointer to the memcached_st that was created (or initialized). On an allocation failure, it returns NULL.</p>
<h2>EXAMPLE</h2>
<pre><code>
const char *config_string= "--SERVER=host10.example.com --SERVER=host11.example.com --SERVER=host10.example.com"
memcached_st *memc= memcached(config_string, strlen(config_string);
{
 ...
}
memcached_free(memc);
</code></pre>
<h2>HOME</h2>
<p> To find out more information please check: <i><a rel="nofollow" href="http://libmemcached.org/">http://libmemcached.org/</a></i></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-memcached/">memcached</a>(1)</i> <i><a href="/docs/linux/man/3-libmemcached/">libmemcached</a>(3)</i> <i><a href="/docs/linux/man/3-memcached_strerror/">memcached_strerror</a>(3)</i></p>
<h2>AUTHOR</h2>
<p> Brian Aker</p>
<h2>COPYRIGHT</h2>
<p> 2011-2013, Brian Aker DataDifferential, <a rel="nofollow" href="http://datadifferential.com/">http://datadifferential.com/</a> </p>
<h2>Index</h2>
