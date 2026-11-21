---
title: "redis-benchmark(1)"
name: "redis-benchmark"
section: "1"
letter: "r"
url: "/docs/linux/man/1-redis-benchmark/"
description: "redis-benchmark – Redis benchmark"
---

<h2>NAME</h2>
<p> redis-benchmark &#8211; Redis benchmark </p>
<h2>SYNOPSIS</h2>
<p> <code>redis-benchmark</code> [ options ] </p>
<h2>DESCRIPTION</h2>
<p> <code>Redis</code> is an open source (BSD licensed), in-memory data structure store, used as database, cache and message broker, found at <code><a rel="nofollow" href="http://redis.io/">http://redis.io/</a></code> </p>
<p> The <code>redis-benchmark</code> command is a command to benchmark redis-server. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h </code><i>hostname</i></dt>
<dd> Server hostname (default: 127.0.0.1).</dd>
<dt><code>-p </code><i>port</i></dt>
<dd> Server port (default: 6379).</dd>
<dt><code>-s </code><i>socket</i></dt>
<dd> Server socket (overrides hostname and port).</dd>
<dt><code>-a </code><i>password</i></dt>
<dd> Password to use when connecting to the server.</dd>
<dt><code>-c </code><i>clients</i></dt>
<dd> Number of parallel connections (default 50)</dd>
<dt><code>-dnnum </code><i>db</i></dt>
<dd> SELECT the specified db number (default 0)</dd>
<dt><code>-k </code><i>boolean</i></dt>
<dd> 1=keep alive 0=reconnect (default 1)</dd>
<dt><code>-r </code><i>keyspacelen</i></dt>
<dd> Use random keys for SET/GET/INCR, random values for SADD Using this option the benchmark will expand the string __rand_int__ inside an argument with a 12 digits number in the specified range from 0 to keyspacelen-1. The substitution changes every time a command is executed. Default tests use this to hit random keys in the specified range.</dd>
<dt><code>-P </code><i>numreq</i></dt>
<dd> Pipeline &lt;numreq&gt; requests. Default 1 (no pipeline).</dd>
<dt><code>-e</code></dt>
<dd> If server replies with errors, show them on stdout. (no more than 1 error per second is displayed)</dd>
<dt><code>-q</code></dt>
<dd> Quiet. Just show query/sec values</dd>
<dt><code>&#8211;csv</code></dt>
<dd> Output in CSV format</dd>
<dt><code>-l</code></dt>
<dd> Loop. Run the tests forever</dd>
<dt><code>-t </code><i>tests</i></dt>
<dd> Only run the comma separated list of tests. The test names are the same as the ones produced as output.</dd>
<dt><code>-I</code></dt>
<dd> Idle mode. Just open N idle connections and wait. </dd>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Run the benchmark with the default configuration against 127.0.0.1:6379:</dt>
<dd> $ redis-benchmark</dd>
<dt>Use 20 parallel clients, for a total of 100k requests, against 192.168.1.1:</dt>
<dd> $ redis-benchmark -h 192.168.1.1 -p 6379 -n 100000 -c 20</dd>
<dt>Fill 127.0.0.1:6379 with about 1 million keys only using the SET test:</dt>
<dd> $ redis-benchmark -t set -n 1000000 -r 100000000</dd>
<dt>Benchmark 127.0.0.1:6379 for a few commands producing CSV output:</dt>
<dd> $ redis-benchmark -t ping,set,get -n 100000 &#8211;csv</dd>
<dt>Benchmark a specific command line:</dt>
<dd> $ redis-benchmark -r 10000 -n 10000 eval &#8216;return redis.call(&quot;ping&quot;)&#8217; 0</dd>
<dt>Fill a list with 10000 random elements:</dt>
<dd> $ redis-benchmark -r 10000 -n 10000 lpush mylist __rand_int__</dd>
<dt>On user specified command lines __rand_int__ is replaced with a random integer</dt>
<dd> with a range of values selected by the -r option. </dd>
</dl>
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
