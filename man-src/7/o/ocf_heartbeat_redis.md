---
title: "ocf_heartbeat_redis(7)"
name: "ocf_heartbeat_redis"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_redis/"
description: "ocf_heartbeat_redis – Redis server"
---

<p>ocf_heartbeat_redis &#8211; Redis server</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>redis</code> [start | stop | status | monitor | promote | demote | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource agent script for redis server. </p>
<p> This resource fully supports master/slave replication. The master preference of a node is determined by the &#8216;slave_priority&#8217; parameter of the redis config. When taking the resource from &#8216;unmanaged&#8217; to &#8216;managed&#8217;, the currently active master will be given a priority of 1000 (plus 1 for each active connection). The default &#8216;slave_priority&#8217; is 100, so the master will stay master. For a slave to become master after converting the resource to managed, set a slave_priority greater than 1000.</p>
<h2>Supported Parameters</h2>
<p><code>bin</code></p>
<dl>
<dd>Path to `redis-server` </p>
<p> (optional, string, default &quot;/usr/bin/redis-server&quot;)</dl>
<p> <code>client_bin</code></p>
<dl>
<dd>Path to `redis-cli` </p>
<p> (optional, string, default &quot;/usr/bin/redis-cli&quot;)</dl>
<p> <code>config</code></p>
<dl>
<dd>Path to &#8216;redis.conf&#8217; </p>
<p> (unique, optional, string, default &quot;/etc/redis/redis.conf&quot;)</dl>
<p> <code>user</code></p>
<dl>
<dd>User to run redis as </p>
<p> (optional, string, default &quot;redis&quot;)</dl>
<p> <code>rundir</code></p>
<dl>
<dd>Directory to store socket and pid file in </p>
<p> (unique, optional, string, default &quot;/var/run/redis&quot;)</dl>
<p> <code>pidfile_name</code></p>
<dl>
<dd>The filename to use for the pidfile. Will be created in the rundir. Should only be a basename, not a full path. </p>
<p> (optional, string, default &quot;redis-server.pid&quot;)</dl>
<p> <code>socket_name</code></p>
<dl>
<dd>The filename to use for the socket. Will be crated in the rundir. Should only be a basename, not a full path. </p>
<p> (optional, string, default &quot;redis.sock&quot;)</dl>
<p> <code>port</code></p>
<dl>
<dd>Port for replication client to connect to on remote server </p>
<p> (optional, string, default &quot;6379&quot;)</dl>
<p> <code>wait_last_known_master</code></p>
<dl>
<dd>During redis cluster bootstrap, wait for the last known master to be promoted before allowing any other instances in the cluster to be promoted. This lessens the risk of data loss when persistent data is in use. </p>
<p> (optional, boolean, default false)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 120.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 120.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 60.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 60. Suggested interval: 45.</dl>
<p> <code>monitor (Master role)</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 60. Suggested interval: 20.</dl>
<p> <code>monitor (Slave role)</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 60. Suggested interval: 60.</dl>
<p> <code>promote</code></p>
<dl>
<dd>Promotes the resource to the Master role. Suggested minimum timeout: 120.</dl>
<p> <code>demote</code></p>
<dl>
<dd>Demotes the resource to the Slave role. Suggested minimum timeout: 120.</dl>
<p> <code>notify</code></p>
<dl>
<dd>Suggested minimum timeout: 90.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a redis resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_redis ocf:heartbeat:redis \
 op monitor depth=&quot;0&quot; timeout=&quot;60&quot; interval=&quot;45&quot; \
 op monitor role=&quot;Master&quot; depth=&quot;0&quot; timeout=&quot;60&quot; interval=&quot;20&quot; \
 op monitor role=&quot;Slave&quot; depth=&quot;0&quot; timeout=&quot;60&quot; interval=&quot;60&quot; </pre>
</dl>
<dl>
<dd>
<pre>ms ms_redis p_redis \
 meta notify=&quot;true&quot; interleave=&quot;true&quot;</pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a redis resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_redis ocf:heartbeat:redis \
 op monitor depth=&quot;0&quot; timeout=&quot;60&quot; interval=&quot;45&quot; \
 op monitor role=&quot;Master&quot; depth=&quot;0&quot; timeout=&quot;60&quot; interval=&quot;20&quot; \
 op monitor role=&quot;Slave&quot; depth=&quot;0&quot; timeout=&quot;60&quot; interval=&quot;60&quot; --master</pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/redis_(resource_agent)">http://www.linux-ha.org/wiki/redis_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
