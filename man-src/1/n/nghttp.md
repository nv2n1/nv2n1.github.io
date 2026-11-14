---
title: "nghttp(1)"
name: "nghttp"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nghttp/"
description: "nghttp – HTTP/2 client"
---

<h2>NAME</h2>
<p> nghttp &#8211; HTTP/2 client</p>
<h2>SYNOPSIS</h2>
<p> <code>nghttp</code> [OPTIONS]&#8230; &lt;URI&gt;&#8230;</p>
<h2>DESCRIPTION</h2>
<p> HTTP/2 client</p>
<dl>
<dt><code>&lt;URI&gt;</code></p>
<dd> Specify URI to access.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Print debug information such as reception and transmission of frames and name/value pairs. Specifying this option multiple times increases verbosity.</p>
<dt><code>-n, &#8211;null-out</code></p>
<dd> Discard downloaded data.</p>
<dt><code>-O, &#8211;remote-name</code></p>
<dd> Save download data in the current directory. The filename is derived from URI. If URI ends with &#8216;<i>/</i>&#8216;, &#8216;index.html&#8217; is used as a filename. Not implemented yet.</p>
<dt><code>-t, &#8211;timeout=&lt;DURATION&gt;</code></p>
<dd> Timeout each request after &lt;DURATION&gt;. Set 0 to disable timeout.</p>
<dt><code>-w, &#8211;window-bits=&lt;N&gt;</code></p>
<dd> Sets the stream level initial window size to 2**&lt;N&gt;-1.</p>
<dt><code>-W, &#8211;connection-window-bits=&lt;N&gt;</code></p>
<dd> Sets the connection level initial window size to 2**&lt;N&gt;-1.</p>
<dt><code>-a, &#8211;get-assets</code></p>
<dd> Download assets such as stylesheets, images and script files linked from the downloaded resource. Only links whose origins are the same with the linking resource will be downloaded. nghttp prioritizes resources using HTTP/2 dependency based priority. The priority order, from highest to lowest, is html itself, css, javascript and images.</p>
<dt><code>-s, &#8211;stat</code></p>
<dd> Print statistics.</p>
<dt><code>-H, &#8211;header=&lt;HEADER&gt;</code></p>
<dd> Add a header to the requests. Example: <i>-H</i>&#8216;:method: PUT&#8217;</p>
<dt><code>&#8211;trailer=&lt;HEADER&gt;</code></p>
<dd> Add a trailer header to the requests. &lt;HEADER&gt; must not include pseudo header field (header field name starting with &#8216;:&#8217;). To send trailer, one must use <i>-d</i> option to send request body. Example: <i>&#8211;trailer</i> &#8216;foo: bar&#8217;.</p>
<dt><code>&#8211;cert=&lt;CERT&gt;</code></p>
<dd> Use the specified client certificate file. The file must be in PEM format.</p>
<dt><code>&#8211;key=&lt;KEY&gt;</code></p>
<dd> Use the client private key file. The file must be in PEM format.</p>
<dt><code>-d, &#8211;data=&lt;PATH&gt;</code></p>
<dd> Post FILE to server. If &#8216;-&#8216; is given, data will be read from stdin.</p>
<dt><code>-m, &#8211;multiply=&lt;N&gt;</code></p>
<dd> Request each URI &lt;N&gt; times. By default, same URI is not requested twice. This option disables it too.</p>
<dt><code>-u, &#8211;upgrade</code></p>
<dd> Perform HTTP Upgrade for HTTP/2. This option is ignored if the request URI has https scheme. If <i>-d</i> is used, the HTTP upgrade request is performed with OPTIONS method.</p>
<dt><code>-p, &#8211;weight=&lt;WEIGHT&gt;</code></p>
<dd> Sets priority group weight. The valid value range is [1, 256], inclusive. </p>
<p> Default: <code>16</code></p>
<dt><code>-M, &#8211;peer-max-concurrent-streams=&lt;N&gt;</code></p>
<dd> Use &lt;N&gt; as SETTINGS_MAX_CONCURRENT_STREAMS value of remote endpoint as if it is received in SETTINGS frame. </p>
<p> Default: <code>100</code></p>
<dt><code>-c, &#8211;header-table-size=&lt;SIZE&gt;</code></p>
<dd> Specify decoder header table size. If this option is used multiple times, and the minimum value among the given values except for last one is strictly less than the last value, that minimum value is set in SETTINGS frame payload before the last value, to simulate multiple header table size change.</p>
<dt><code>-b, &#8211;padding=&lt;N&gt;</code></p>
<dd> Add at most &lt;N&gt; bytes to a frame payload as padding. Specify 0 to disable padding.</p>
<dt><code>-r, &#8211;har=&lt;PATH&gt;</code></p>
<dd> Output HTTP transactions &lt;PATH&gt; in HAR format. If &#8216;-&#8216; is given, data is written to stdout.</p>
<dt><code>&#8211;color</code></p>
<dd> Force colored log output.</p>
<dt><code>&#8211;continuation</code></p>
<dd> Send large header to test CONTINUATION.</p>
<dt><code>&#8211;no-content-length</code></p>
<dd> Don&#8217;t send content-length header field.</p>
<dt><code>&#8211;no-dep</code></p>
<dd> Don&#8217;t send dependency based priority hint to server.</p>
<dt><code>&#8211;hexdump</code></p>
<dd> Display the incoming traffic in hexadecimal (Canonical hex+ASCII display). If SSL/TLS is used, decrypted data are used.</p>
<dt><code>&#8211;no-push</code></p>
<dd> Disable server push.</p>
<dt><code>&#8211;max-concurrent-streams=&lt;N&gt;</code></p>
<dd> The number of concurrent pushed streams this client accepts.</p>
<dt><code>&#8211;version</code></p>
<dd> Display version information and exit.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Display this help and exit. </p>
<p> The &lt;SIZE&gt; argument is an integer and an optional unit (e.g., 10K is 10 * 1024). Units are K, M and G (powers of 1024). </p>
<p> The &lt;DURATION&gt; argument is an integer and an optional unit (e.g., 1s is 1 second and 500ms is 500 milliseconds). Units are h, m, s or ms (hours, minutes, seconds and milliseconds, respectively). If a unit is omitted, a second is used as unit.</dl>
<h2>DEPENDENCY BASED PRIORITY</h2>
<p> nghttp sends priority hints to server by default unless <i>&#8211;no-dep</i> is used. nghttp mimics the way Firefox employs to manages dependency using idle streams. We follows the behaviour of Firefox Nightly as of April, 2015, and nghttp&#8217;s behaviour is very static and could be different from Firefox in detail. But reproducing the same behaviour of Firefox is not our goal. The goal is provide the easy way to test out the dependency priority in server implementation. </p>
<p> When connection is established, nghttp sends 5 PRIORITY frames to idle streams 3, 5, 7, 9 and 11 to create &quot;anchor&quot; nodes in dependency tree: </p>
<pre><code>
+ -- -- -+ | id = 0 |
                  +-- -- -+^^^w = 201 / |    \ w = 1 / |
                                                   / w = 101 |
                                                         +-- -- -+ +-- -- -+ +-- -- -+ | id = 3 | | id = 5 | | id = 7 |
                                                                                                                    +-- -- -+ +-- -- -+ +-- -- -+^^w = 1 | w = 1 |
                                                                                                                                                               | |
                                                                                                                                                               +-- -- -+ +-- -- -+ | id = 11 | | id = 9 |
                                                                                                                                                                                                      +-- -- -+ +-- -- -+
</code></pre>
<p> In the above figure, <code>id</code> means stream ID, and <code>w</code> means weight. The stream 0 is non-existence stream, and forms the root of the tree. The stream 7 and 9 are not used for now. </p>
<p> The URIs given in the command-line depend on stream 11 with the weight given in <i>-p</i> option, which defaults to 16. </p>
<p> If <i>-a</i> option is used, nghttp parses the resource pointed by URI given in command-line as html, and extracts resource links from it. When requesting those resources, nghttp uses dependency according to its resource type. </p>
<p> For CSS, and Javascript files inside &quot;head&quot; element, they depend on stream 3 with the weight 2. The Javascript files outside &quot;head&quot; element depend on stream 5 with the weight 2. The mages depend on stream 11 with the weight 12. The other resources (e.g., icon) depend on stream 11 with the weight 2.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-nghttpd/">nghttpd</a>(1)</i>, <i><a href="/docs/linux/man/1-nghttpx/">nghttpx</a>(1)</i>, <i><a href="/docs/linux/man/1-h2load/">h2load</a>(1)</i></p>
<h2>AUTHOR</h2>
<p> Tatsuhiro Tsujikawa</p>
<h2>COPYRIGHT</h2>
<p> 2012, 2015, 2016, Tatsuhiro Tsujikawa </p>
<h2>Index</h2>
