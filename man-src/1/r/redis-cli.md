---
title: "redis-cli(1)"
name: "redis-cli"
section: "1"
letter: "r"
url: "/docs/linux/man/1-redis-cli/"
description: "redis-cli – Redis client"
---

<h2>NAME</h2>
<p> redis-cli &#8211; Redis client </p>
<h2>SYNOPSIS</h2>
<p> <code>redis-cli</code> [ options ] [cmd [arg [arg &#8230;]]] </p>
<h2>DESCRIPTION</h2>
<p> <code>Redis</code> is an open source (BSD licensed), in-memory data structure store, used as database, cache and message broker, found at <code><a rel="nofollow" href="http://redis.io/">http://redis.io/</a></code> </p>
<p> The <code>redis-cli</code> command is a command line client to redis-server. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h </code><i>hostname</i></p>
<dd> Server hostname (default: 127.0.0.1).</p>
<dt><code>-p </code><i>port</i></p>
<dd> Server port (default: 6379).</p>
<dt><code>-s </code><i>socket</i></p>
<dd> Server socket (overrides hostname and port).</p>
<dt><code>-a </code><i>password</i></p>
<dd> Password to use when connecting to the server.</p>
<dt><code>-r </code><i>repeat</i></p>
<dd> Execute specified command N times.</p>
<dt><code>-i </code><i>interval</i></p>
<dd> When -r is used, waits <i>interval</i> seconds per command. It is possible to specify sub-second times like -i 0.1.</p>
<dt><code>-n </code><i>db</i></p>
<dd> Database number.</p>
<dt><code>-x</code></p>
<dd> Read last argument from STDIN.</p>
<dt><code>-d </code><i>delimiter</i></p>
<dd> Multi-bulk delimiter in for raw formatting (default: .</p>
<dt><code>-c</code></p>
<dd> Enable cluster mode (follow -ASK and -MOVED redirections).</p>
<dt><code>&#8211;raw</code></p>
<dd> Use raw formatting for replies (default when STDOUT is not a tty).</p>
<dt><code>&#8211;no-raw</code></p>
<dd> Force formatted output even when STDOUT is not a tty.</p>
<dt><code>&#8211;csv</code></p>
<dd> Output in CSV format.</p>
<dt><code>&#8211;stat</code></p>
<dd> Print rolling stats about server: mem, clients, &#8230;</p>
<dt><code>&#8211;latency</code></p>
<dd> Enter a special mode continuously sampling latency.</p>
<dt><code>&#8211;latency-history</code></p>
<dd> Like &#8211;latency but tracking latency changes over time. Default time interval is 15 sec. Change it using -i.</p>
<dt><code>&#8211;latency-dist</code></p>
<dd> Shows latency as a spectrum, requires xterm 256 colors. Default time interval is 1 sec. Change it using -i.</p>
<dt><code>&#8211;lru-test</code></p>
<dd> Simulate a cache workload with an 80-20 distribution.</p>
<dt><code>&#8211;slave</code></p>
<dd> Simulate a slave showing commands received from the master.</p>
<dt><code>&#8211;rdb </code><i>filename</i></p>
<dd> Transfer an RDB dump from remote server to local file.</p>
<dt><code>&#8211;pipe</code></p>
<dd> Transfer raw Redis protocol from stdin to server.</p>
<dt><code>&#8211;pipe-timeout </code><i>n</i></p>
<dd> In &#8211;pipe mode, abort with error if after sending all data. no reply is received within <i>n</i> seconds. Default timeout: 30. Use 0 to wait forever.</p>
<dt><code>&#8211;bigkeys</code></p>
<dd> Sample Redis keys looking for big keys.</p>
<dt><code>&#8211;scan</code></p>
<dd> List all keys using the SCAN command.</p>
<dt><code>&#8211;pattern </code><i>pat</i></p>
<dd> Useful with &#8211;scan to specify a SCAN pattern.</p>
<dt><code>&#8211;intrinsic-latency </code><i>sec</i></p>
<dd> Run a test to measure intrinsic system latency. The test will run for the specified amount of seconds.</p>
<dt><code>&#8211;eval </code><i>file</i></p>
<dd> Send an EVAL command using the Lua script at <i>file</i>.</p>
<dt><code>&#8211;ldb</code></p>
<dd> Used with &#8211;eval enable the Redis Lua debugger.</p>
<dt><code>&#8211;ldb-sync-mode</code></p>
<dd> Like &#8211;ldb but uses the synchronous Lua debugger, in this mode the server is blocked and script changes are are not rolled back from the server memory.</p>
<dt><code>&#8211;help</code></p>
<dd> Output this help and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Output version and exit. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>cat /etc/passwd | redis-cli -x set mypasswd</p>
<dd>
<dt>redis-cli get mypasswd</p>
<dd>
<dt>redis-cli -r 100 lpush mylist x</p>
<dd>
<dt>redis-cli -r 100 -i 1 info | grep used_memory_human:</p>
<dd>
<dt>redis-cli &#8211;eval myscript.lua key1 key2 , arg1 arg2 arg3</p>
<dd>
<dt>redis-cli &#8211;scan &#8211;pattern &#8216;*:12345*&#8217;</p>
<dd>
</dl>
<h2>BUGS</h2>
<p> See: <code><a rel="nofollow" href="http://redis.io/support">http://redis.io/support</a></code> and <code><a rel="nofollow" href="https://github.com/antirez/redis/issues">https://github.com/antirez/redis/issues</a></code> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006-2016 Salvatore Sanfilippo </p>
<p> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:</p>
<dl>
<dt>*</p>
<dd> Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.</p>
<dt>*</p>
<dd> Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.</p>
<dt>*</p>
<dd> Neither the name of Redis nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.</dl>
<p> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS &quot;AS IS&quot; AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. </p>
<h2>Index</h2>
