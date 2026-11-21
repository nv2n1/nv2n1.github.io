---

title: "redis-server(1)"
name: "redis-server"
section: "1"
letter: "r"
url: "/docs/linux/man/1-redis-server/"
description: "redis-server, redis-sentinel – Redis server"
---

<h2>NAME</h2>
<p> redis-server, redis-sentinel &#8211; Redis server </p>
<p> <code>redis-server</code> [ <i>configuration_file</i> ] [ options ] [ &#8211;sentinel ] </p>
<p> <code>redis-sentinel</code> [ <i>configuration_file</i> ] [ options ] </p>
<p> <code>Redis</code> is an open source (BSD licensed), in-memory data structure store, used as database, cache and message broker, found at <code><a rel="nofollow" href="http://redis.io/">http://redis.io/</a></code> </p>
<p> The <code>redis-server</code> command is a command line to launch a Redis server. </p>
<p> The <code>redis-sentinel</code> command is a symbolic link to the <code>redis-server</code> command which imply the <code>&#8211;sentionel</code> option. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;</code></dt>
<dd> Read configuration from stdin.</dd>
<dt>
</dt><dt><code>&#8211;sentinel</code></dt>
<dd>
</dd><dd> Run in sentinel mode</dd>
<dt><code>&#8211;test-memory </code><i>megabytes</i></dt>
<dd> Run a memory check and exit.</dd>
<dt>
</dt><dd> <code>&#8211;help</code></dd>
<dt>
</dt><dd> <code>-h</code> Output this help and exit.</dd>
<dt>
</dt><dd> <code>&#8211;version</code></dd>
<dt>
</dt><dd> <code>-v</code> Output version and exit.</dd></dl>
<p> All parameters described in <code>redis.conf</code> file can be passed as command line option, e.g. <code>&#8211;port</code> <i>port</i> </p>
<h2>EXAMPLES</h2>
<dl>
<dt>Run the server with default conf</dt>
<dd> redis-server</dd>
<dt>Run the server with a configuration file</dt>
<dd> redis-server /etc/redis/6379.conf</dd>
<dt>Run the server changing some default options</dt>
<dd> redis-server &#8211;port 7777 &#8211;slaveof 127.0.0.1 8888</dd>
<dt>Run the server with a configuration file and changing some options</dt>
<dd> redis-server /etc/myredis.conf &#8211;loglevel verbose</dd>
<dt>Run in sentinel mode</dt>
<dd> redis-server /etc/sentinel.conf &#8211;sentinel </dd>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-redis-conf/">redis.conf</a></code>(5) </p>
<h2>BUGS</h2>
<p> See: <code><a rel="nofollow" href="http://redis.io/support">http://redis.io/support</a></code> and <code><a rel="nofollow" href="https://github.com/antirez/redis/issues">https://github.com/antirez/redis/issues</a></code> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006-2016 Salvatore Sanfilippo </p>
<p> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:</p>
<dl>
<dt>*</dt>
<dd> Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.</dd>
<dt>*</dt>
<dd> Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.</dd>
<dt>*</dt>
<dd> Neither the name of Redis nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.</dd></dl>
<p> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS &quot;AS IS&quot; AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. </p>
