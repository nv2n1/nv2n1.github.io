---
title: "ffmpeg-protocols(1)"
name: "ffmpeg-protocols"
section: "1"
letter: "f"
url: "/docs/linux/man/1-ffmpeg-protocols/"
description: "ffmpeg-protocols – FFmpeg protocols"
---

<h2 class="name">NAME</h2>
<p> ffmpeg-protocols &#8211; FFmpeg protocols </p>
<h2>DESCRIPTION</h2>
<p> This document describes the input and output protocols provided by the libavformat library.</p>
<h2>PROTOCOL OPTIONS</h2>
<p> The libavformat library provides some generic global options, which can be set on all the protocols. In addition each protocol may support so-called private options, which are specific for that component. </p>
<p> Options may be set by specifying &#8211;<i>option</i> <i>value</i> in the FFmpeg tools, or by setting the value explicitly in the <tt>&quot;AVFormatContext&quot;</tt> options or using the <i>libavutil/opt.h</i> <font SIZE="-1">API</font> for programmatic use. </p>
<p> The list of supported options follows:</p>
<dl>
<dt><code>protocol_whitelist</code> <i>list</i> <code>(</code><i>input</i><code>)</code></p>
<dd> Set a &#8220;,&#8221;-separated list of allowed protocols. &#8220;<font SIZE="-1">ALL&#8221;</font> matches all protocols. Protocols prefixed by &#8220;-&#8221; are disabled. All protocols are allowed by default but protocols used by an another protocol (nested protocols) are restricted to a per protocol subset.</dl>
<h2>PROTOCOLS</h2>
<p> Protocols are configured elements in FFmpeg that enable access to resources that require specific protocols. </p>
<p> When you configure your FFmpeg build, all the supported protocols are enabled by default. You can list all available ones using the configure option &#8220;&#8211;list-protocols&#8221;. </p>
<p> You can disable all the protocols using the configure option &#8220;&#8211;disable-protocols&#8221;, and selectively enable a protocol using the option &quot;&#8211;enable-protocol=<i></i><font SIZE="-1"><i>PROTOCOL</i></font><i></i>&#8220;, or you can disable a particular protocol using the option &#8221;&#8211;disable-protocol=<i></i><font SIZE="-1"><i>PROTOCOL</i></font><i></i>&quot;. </p>
<p> The option &#8220;-protocols&#8221; of the ff* tools will display the list of supported protocols. </p>
<p> All protocols accept the following options:</p>
<dl>
<dt><code>rw_timeout</code></p>
<dd> Maximum time to wait for (network) read/write operations to complete, in microseconds.</dl>
<p> A description of the currently available protocols follows.</p>
<h3>amqp</h3>
<p> Advanced Message Queueing Protocol (<font SIZE="-1">AMQP</font>) version 0-9-1 is a broker based publish-subscribe communication protocol. </p>
<p> FFmpeg must be compiled with &#8211;enable-librabbitmq to support <font SIZE="-1">AMQP. A</font> separate <font SIZE="-1">AMQP</font> broker must also be run. An example open-source <font SIZE="-1">AMQP</font> broker is RabbitMQ. </p>
<p> After starting the broker, an FFmpeg client may stream data to the broker using the command: </p>
<pre><code>
ffmpeg - re - i input - f mpegts amqp: //[[user]:[password]@]hostname[:port][/vhost]
</code></pre>
<p> Where hostname and port (default is 5672) is the address of the broker. The client may also set a user/password for authentication. The default for both fields is &#8220;guest&#8221;. Name of virtual host on broker can be set with vhost. The default value is &#8220;/&#8221;. </p>
<p> Muliple subscribers may stream from the broker using the command: </p>
<p>ffplay amqp: //[[user]:[password]@]hostname[:port][/vhost]</p>
<p> In RabbitMQ all data published to the broker flows through a specific exchange, and each subscribing client has an assigned queue/buffer. When a packet arrives at an exchange, it may be copied to a client&#8217;s queue depending on the exchange and routing_key fields. </p>
<p> The following options are supported:</p>
<dl>
<dt><code>exchange</code></p>
<dd> Sets the exchange to use on the broker. RabbitMQ has several predefined exchanges: &#8220;amq.direct&#8221; is the default exchange, where the publisher and subscriber must have a matching routing_key; &#8220;amq.fanout&#8221; is the same as a broadcast operation (i.e. the data is forwarded to all queues on the fanout exchange independent of the routing_key); and &#8220;amq.topic&#8221; is similar to &#8220;amq.direct&#8221;, but allows for more complex pattern matching (refer to the RabbitMQ documentation).</p>
<dt><code>routing_key</code></p>
<dd> Sets the routing key. The default value is &#8220;amqp&#8221;. The routing key is used on the &#8220;amq.direct&#8221; and &#8220;amq.topic&#8221; exchanges to decide whether packets are written to the queue of a subscriber.</p>
<dt><code>pkt_size</code></p>
<dd> Maximum size of each packet sent/received to the broker. Default is 131072. Minimum is 4096 and max is any large value (representable by an int). When receiving packets, this sets an internal buffer size in FFmpeg. It should be equal to or greater than the size of the published packets to the broker. Otherwise the received message may be truncated causing decoding errors.</p>
<dt><code>connection_timeout</code></p>
<dd> The timeout in seconds during the initial connection to the broker. The default value is rw_timeout, or 5 seconds if rw_timeout is not set.</p>
<dt><code>delivery_mode</code> <i>mode</i></p>
<dd> Sets the delivery mode of each message sent to broker. The following values are accepted:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>persistent</code></p>
<dd> Delivery mode set to &#8220;persistent&#8221; (2). This is the default value. Messages may be written to the broker&#8217;s disk depending on its setup.</p>
<dt><code>non-persistent</code></p>
<dd> Delivery mode set to &#8220;non-persistent&#8221; (1). Messages will stay in broker&#8217;s memory unless the broker is under memory pressure.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h3>async</h3>
<p> Asynchronous data filling wrapper for input stream. </p>
<p> Fill data in a background thread, to decouple I/O operation from demux thread. </p>
<pre>
        async:&lt;URL&gt;
        async:<a rel="nofollow" href="http://host/resource">http://host/resource</a>
        async:cache:<a rel="nofollow" href="http://host/resource">http://host/resource</a>
</pre>
<h3>bluray</h3>
<p> Read BluRay playlist. </p>
<p> The accepted options are:</p>
<dl>
<dt><code>angle</code></p>
<dd> BluRay angle</p>
<dt><code>chapter</code></p>
<dd> Start chapter (1&#8230;N)</p>
<dt><code>playlist</code></p>
<dd> Playlist to read (<font SIZE="-1">BDMV/PLAYLIST/</font>?????.mpls)</dl>
<p> Examples: </p>
<p> Read longest playlist from BluRay mounted to /mnt/bluray: </p>
<pre>
        bluray:/mnt/bluray
</pre>
<p> Read angle 2 of playlist 4 from BluRay mounted to /mnt/bluray, start from chapter 2: </p>
<pre>
        -playlist 4 -angle 2 -chapter 2 bluray:/mnt/bluray
</pre>
<h3>cache</h3>
<p> Caching wrapper for input stream. </p>
<p> Cache the input stream to temporary file. It brings seeking capability to live streams. </p>
<p> The accepted options are:</p>
<dl>
<dt><code>read_ahead_limit</code></p>
<dd> Amount in bytes that may be read ahead when seeking isn&#8217;t supported. Range is -1 to <font SIZE="-1">INT_MAX.</font> -1 for unlimited. Default is 65536.</dl>
<p> <font SIZE="-1">URL</font> Syntax is </p>
<pre>
        cache:&lt;URL&gt;
</pre>
<h3>concat</h3>
<p> Physical concatenation protocol. </p>
<p> Read and seek from many resources in sequence as if they were a unique resource. </p>
<p> A <font SIZE="-1">URL</font> accepted by this protocol has the syntax: </p>
<pre>
        concat:&lt;URL1&gt;|&lt;URL2&gt;|...|&lt;URLN&gt;
</pre>
<p> where <i></i><font SIZE="-1"><i>URL1</i></font><i></i>, <i></i><font SIZE="-1"><i>URL2</i></font><i></i>, &#8230;, <i></i><font SIZE="-1"><i>URLN</i></font><i></i> are the urls of the resource to be concatenated, each one possibly specifying a distinct protocol. </p>
<p> For example to read a sequence of files <i>split1.mpeg</i>, <i>split2.mpeg</i>, <i>split3.mpeg</i> with <code>ffplay</code> use the command: </p>
<pre>
        ffplay concat:split1.mpeg\|split2.mpeg\|split3.mpeg
</pre>
<p> Note that you may need to escape the character &#8220;|&#8221; which is special for many shells.</p>
<h3>crypto</h3>
<p> AES-encrypted stream reading protocol. </p>
<p> The accepted options are:</p>
<dl>
<dt><code>key</code></p>
<dd> Set the <font SIZE="-1">AES</font> decryption key binary block from given hexadecimal representation.</p>
<dt><code>iv</code></p>
<dd> Set the <font SIZE="-1">AES</font> decryption initialization vector binary block from given hexadecimal representation.</dl>
<p> Accepted <font SIZE="-1">URL</font> formats: </p>
<pre>
        crypto:&lt;URL&gt;
        crypto+&lt;URL&gt;
</pre>
<h3>data</h3>
<p> Data in-line in the <font SIZE="-1">URI.</font> See &lt;<code><a rel="nofollow" href="http://en.wikipedia.org/wiki/Data_URI_scheme">http://en.wikipedia.org/wiki/Data_URI_scheme</a></code>&gt;. </p>
<p> For example, to convert a <font SIZE="-1">GIF</font> file given inline with <code>ffmpeg</code>: </p>
<pre>
        ffmpeg -i &quot;data:image/gif;base64,R0lGODdhCAAIAMIEAAAAAAAA//8AAP//AP///////////////ywAAAAACAAIAAADF0gEDLojDgdGiJdJqUX02iB4E8Q9jUMkADs=&quot; smiley.png
</pre>
<h3>file</h3>
<p> File access protocol. </p>
<p> Read from or write to a file. </p>
<p> A file <font SIZE="-1">URL</font> can have the form: </p>
<pre>
        file:&lt;filename&gt;
</pre>
<p> where <i>filename</i> is the path of the file to read. </p>
<p> An <font SIZE="-1">URL</font> that does not have a protocol prefix will be assumed to be a file <font SIZE="-1">URL.</font> Depending on the build, an <font SIZE="-1">URL</font> that looks like a Windows path with the drive letter at the beginning will also be assumed to be a file <font SIZE="-1">URL</font> (usually not the case in builds for unix-like systems). </p>
<p> For example to read from a file <i>input.mpeg</i> with <code>ffmpeg</code> use the command: </p>
<pre>
        ffmpeg -i file:input.mpeg output.mpeg
</pre>
<p> This protocol accepts the following options:</p>
<dl>
<dt><code>truncate</code></p>
<dd> Truncate existing files on write, if set to 1. A value of 0 prevents truncating. Default value is 1.</p>
<dt><code>blocksize</code></p>
<dd> Set I/O operation maximum block size, in bytes. Default value is <tt>&quot;INT_MAX&quot;</tt>, which results in not limiting the requested block size. Setting this value reasonably low improves user termination request reaction time, which is valuable for files on slow medium.</p>
<dt><code>follow</code></p>
<dd> If set to 1, the protocol will retry reading at the end of the file, allowing reading files that still are being written. In order for this to terminate, you either need to use the rw_timeout option, or use the interrupt callback (for <font SIZE="-1">API</font> users).</p>
<dt><code>seekable</code></p>
<dd> Controls if seekability is advertised on the file. 0 means non-seekable, -1 means auto (seekable for normal files, non-seekable for named pipes). </p>
<p> Many demuxers handle seekable and non-seekable resources differently, overriding this might speed up opening certain files at the cost of losing some features (e.g. accurate seeking).</dl>
<h3>ftp</h3>
<p> <font SIZE="-1">FTP</font> (File Transfer Protocol). </p>
<p> Read from or write to remote resources using <font SIZE="-1">FTP</font> protocol. </p>
<p> Following syntax is required. </p>
<p>ftp: //[user[:password]@]server[:port]/path/to/remote/resource.mpeg</p>
<p> This protocol accepts the following options.</p>
<dl>
<dt><code>timeout</code></p>
<dd> Set timeout in microseconds of socket I/O operations used by the underlying low level operation. By default it is set to -1, which means that the timeout is not specified.</p>
<dt><code>ftp-user</code></p>
<dd> Set a user to be used for authenticating to the <font SIZE="-1">FTP</font> server. This is overridden by the user in the <font SIZE="-1">FTP URL.</font></p>
<dt><code>ftp-password</code></p>
<dd> Set a password to be used for authenticating to the <font SIZE="-1">FTP</font> server. This is overridden by the password in the <font SIZE="-1">FTP URL,</font> or by <code>ftp-anonymous-password</code> if no user is set.</p>
<dt><code>ftp-anonymous-password</code></p>
<dd> Password used when login as anonymous user. Typically an e-mail address should be used.</p>
<dt><code>ftp-write-seekable</code></p>
<dd> Control seekability of connection during encoding. If set to 1 the resource is supposed to be seekable, if set to 0 it is assumed not to be seekable. Default value is 0.</dl>
<p> <font SIZE="-1">NOTE:</font> Protocol can be used as output, but it is recommended to not do it, unless special care is taken (tests, customized server configuration etc.). Different <font SIZE="-1">FTP</font> servers behave in different way during seek operation. ff* tools may produce incomplete content due to server limitations.</p>
<h3>gopher</h3>
<p> Gopher protocol.</p>
<h3>gophers</h3>
<p> Gophers protocol. </p>
<p> The Gopher protocol with <font SIZE="-1">TLS</font> encapsulation.</p>
<h3>hls</h3>
<p> Read Apple <font SIZE="-1">HTTP</font> Live Streaming compliant segmented stream as a uniform one. The M3U8 playlists describing the segments can be remote <font SIZE="-1">HTTP</font> resources or local files, accessed using the standard file protocol. The nested protocol is declared by specifying &quot;+<i>proto</i>&quot; after the hls <font SIZE="-1">URI</font> scheme name, where <i>proto</i> is either &#8220;file&#8221; or &#8220;http&#8221;. </p>
<pre>
        hls+<a rel="nofollow" href="http://host/path/to/remote/resource.m3u8">http://host/path/to/remote/resource.m3u8</a>
        hls+file://path/to/local/resource.m3u8
</pre>
<p> Using this protocol is discouraged &#8211; the hls demuxer should work just as well (if not, please report the issues) and is more complete. To use the hls demuxer instead, simply use the direct URLs to the m3u8 files.</p>
<h3>http</h3>
<p> <font SIZE="-1">HTTP</font> (Hyper Text Transfer Protocol). </p>
<p> This protocol accepts the following options:</p>
<dl>
<dt><code>seekable</code></p>
<dd> Control seekability of connection. If set to 1 the resource is supposed to be seekable, if set to 0 it is assumed not to be seekable, if set to -1 it will try to autodetect if it is seekable. Default value is -1.</p>
<dt><code>chunked_post</code></p>
<dd> If set to 1 use chunked Transfer-Encoding for posts, default is 1.</p>
<dt><code>content_type</code></p>
<dd> Set a specific content type for the <font SIZE="-1">POST</font> messages or for listen mode.</p>
<dt><code>http_proxy</code></p>
<dd> set <font SIZE="-1">HTTP</font> proxy to tunnel through e.g. <a rel="nofollow" href="http://example.com:1234">http://example.com:1234</a></p>
<dt><code>headers</code></p>
<dd> Set custom <font SIZE="-1">HTTP</font> headers, can override built in default headers. The value must be a string encoding the headers.</p>
<dt><code>multiple_requests</code></p>
<dd> Use persistent connections if set to 1, default is 0.</p>
<dt><code>post_data</code></p>
<dd> Set custom <font SIZE="-1">HTTP</font> post data.</p>
<dt><code>referer</code></p>
<dd> Set the Referer header. Include &#8216;Referer: <font SIZE="-1">URL</font>&#8216; header in <font SIZE="-1">HTTP</font> request.</p>
<dt><code>user_agent</code></p>
<dd> Override the User-Agent header. If not specified the protocol will use a string describing the libavformat build. (&#8220;Lavf/&lt;version&gt;&#8221;)</p>
<dt><code>user-agent</code></p>
<dd> This is a deprecated option, you can use user_agent instead it.</p>
<dt><code>reconnect_at_eof</code></p>
<dd> If set then eof is treated like an error and causes reconnection, this is useful for live / endless streams.</p>
<dt><code>reconnect_streamed</code></p>
<dd> If set then even streamed/non seekable streams will be reconnected on errors.</p>
<dt><code>reconnect_on_network_error</code></p>
<dd> Reconnect automatically in case of <font SIZE="-1">TCP/TLS</font> errors during connect.</p>
<dt><code>reconnect_on_http_error</code></p>
<dd> A comma separated list of <font SIZE="-1">HTTP</font> status codes to reconnect on. The list can include specific status codes (e.g. &#8216;503&#8217;) or the strings &#8216;4xx&#8217; / &#8216;5xx&#8217;.</p>
<dt><code>reconnect_delay_max</code></p>
<dd> Sets the maximum delay in seconds after which to give up reconnecting</p>
<dt><code>mime_type</code></p>
<dd> Export the <font SIZE="-1">MIME</font> type.</p>
<dt><code>http_version</code></p>
<dd> Exports the <font SIZE="-1">HTTP</font> response version number. Usually &#8220;1.0&#8221; or &#8220;1.1&#8221;.</p>
<dt><code>icy</code></p>
<dd> If set to 1 request <font SIZE="-1">ICY</font> (SHOUTcast) metadata from the server. If the server supports this, the metadata has to be retrieved by the application by reading the <code>icy_metadata_headers</code> and <code>icy_metadata_packet</code> options. The default is 1.</p>
<dt><code>icy_metadata_headers</code></p>
<dd> If the server supports <font SIZE="-1">ICY</font> metadata, this contains the ICY-specific <font SIZE="-1">HTTP</font> reply headers, separated by newline characters.</p>
<dt><code>icy_metadata_packet</code></p>
<dd> If the server supports <font SIZE="-1">ICY</font> metadata, and <code>icy</code> was set to 1, this contains the last non-empty metadata packet sent by the server. It should be polled in regular intervals by applications interested in mid-stream metadata updates.</p>
<dt><code>cookies</code></p>
<dd> Set the cookies to be sent in future requests. The format of each cookie is the same as the value of a Set-Cookie <font SIZE="-1">HTTP</font> response field. Multiple cookies can be delimited by a newline character.</p>
<dt><code>offset</code></p>
<dd> Set initial byte offset.</p>
<dt><code>end_offset</code></p>
<dd> Try to limit the request to bytes preceding this offset.</p>
<dt><code>method</code></p>
<dd> When used as a client option it sets the <font SIZE="-1">HTTP</font> method for the request. </p>
<p> When used as a server option it sets the <font SIZE="-1">HTTP</font> method that is going to be expected from the client(s). If the expected and the received <font SIZE="-1">HTTP</font> method do not match the client will be given a Bad Request response. When unset the <font SIZE="-1">HTTP</font> method is not checked for now. This will be replaced by autodetection in the future.</p>
<dt><code>listen</code></p>
<dd> If set to 1 enables experimental <font SIZE="-1">HTTP</font> server. This can be used to send data when used as an output option, or read data from a client with <font SIZE="-1">HTTP POST</font> when used as an input option. If set to 2 enables experimental multi-client <font SIZE="-1">HTTP</font> server. This is not yet implemented in ffmpeg.c and thus must not be used as a command line option. </p>
<pre>
        # Server side (sending):
        ffmpeg -i somefile.ogg -c copy -listen 1 -f ogg http://&lt;server&gt;:&lt;port&gt;
        
        # Client side (receiving):
        ffmpeg -i http://&lt;server&gt;:&lt;port&gt; -c copy somefile.ogg
        
        # Client can also be done with wget:
        wget http://&lt;server&gt;:&lt;port&gt; -O somefile.ogg
        
        # Server side (receiving):
        ffmpeg -listen 1 -i http://&lt;server&gt;:&lt;port&gt; -c copy somefile.ogg
        
        # Client side (sending):
        ffmpeg -i somefile.ogg -chunked_post 0 -c copy -f ogg http://&lt;server&gt;:&lt;port&gt;
        
        # Client can also be done with wget:
        wget --post-file=somefile.ogg http://&lt;server&gt;:&lt;port&gt;
</pre>
<dt><code>send_expect_100</code></p>
<dd> Send an Expect: 100-continue header for <font SIZE="-1">POST.</font> If set to 1 it will send, if set to 0 it won&#8217;t, if set to -1 it will try to send if it is applicable. Default value is -1.</p>
<dt><code>auth_type</code></p>
<dd> Set <font SIZE="-1">HTTP</font> authentication type. No option for Digest, since this method requires getting nonce parameters from the server first and can&#8217;t be used straight away like Basic.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none</code></p>
<dd> Choose the <font SIZE="-1">HTTP</font> authentication type automatically. This is the default.</p>
<dt><code>basic</code></p>
<dd> Choose the <font SIZE="-1">HTTP</font> basic authentication. </p>
<p> Basic authentication sends a Base64-encoded string that contains a user name and password for the client. Base64 is not a form of encryption and should be considered the same as sending the user name and password in clear text (Base64 is a reversible encoding). If a resource needs to be protected, strongly consider using an authentication scheme other than basic authentication. <font SIZE="-1">HTTPS/TLS</font> should be used with basic authentication. Without these additional security enhancements, basic authentication should not be used to protect sensitive or valuable information.</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<p> <i></i><font SIZE="-1"><i>HTTP</i></font><i> Cookies</i> </p>
<p> Some <font SIZE="-1">HTTP</font> requests will be denied unless cookie values are passed in with the request. The <code>cookies</code> option allows these cookies to be specified. At the very least, each cookie must specify a value along with a path and domain. <font SIZE="-1">HTTP</font> requests that match both the domain and path will automatically include the cookie value in the <font SIZE="-1">HTTP</font> Cookie header field. Multiple cookies can be delimited by a newline. </p>
<p> The required syntax to play a stream specifying a cookie is: </p>
<pre>
        ffplay -cookies &quot;nlqptid=nltid=tsn; path=/; domain=somedomain.com;&quot; <a rel="nofollow" href="http://somedomain.com/somestream.m3u8">http://somedomain.com/somestream.m3u8</a>
</pre>
<h3>Icecast</h3>
<p> Icecast protocol (stream to Icecast servers) </p>
<p> This protocol accepts the following options:</p>
<dl>
<dt><code>ice_genre</code></p>
<dd> Set the stream genre.</p>
<dt><code>ice_name</code></p>
<dd> Set the stream name.</p>
<dt><code>ice_description</code></p>
<dd> Set the stream description.</p>
<dt><code>ice_url</code></p>
<dd> Set the stream website <font SIZE="-1">URL.</font></p>
<dt><code>ice_public</code></p>
<dd> Set if the stream should be public. The default is 0 (not public).</p>
<dt><code>user_agent</code></p>
<dd> Override the User-Agent header. If not specified a string of the form &#8220;Lavf/&lt;version&gt;&#8221; will be used.</p>
<dt><code>password</code></p>
<dd> Set the Icecast mountpoint password.</p>
<dt><code>content_type</code></p>
<dd> Set the stream content type. This must be set if it is different from audio/mpeg.</p>
<dt><code>legacy_icecast</code></p>
<dd> This enables support for Icecast versions &lt; 2.4.0, that do not support the <font SIZE="-1">HTTP PUT</font> method but the <font SIZE="-1">SOURCE</font> method.</p>
<dt><code>tls</code></p>
<dd> Establish a <font SIZE="-1">TLS</font> (<font SIZE="-1">HTTPS</font>) connection to Icecast.</dl>
<p>icecast: //[&lt;username&gt;[:&lt;password&gt;]@]&lt;server&gt;:&lt;port&gt;/&lt;mountpoint&gt;</p>
<h3>mmst</h3>
<p> <font SIZE="-1">MMS</font> (Microsoft Media Server) protocol over <font SIZE="-1">TCP.</font></p>
<h3>mmsh</h3>
<p> <font SIZE="-1">MMS</font> (Microsoft Media Server) protocol over <font SIZE="-1">HTTP.</font> </p>
<p> The required syntax is: </p>
<p>mmsh: //&lt;server&gt;[:&lt;port&gt;][/&lt;app&gt;][/&lt;playpath&gt;]</p>
<h3>md5</h3>
<p> <font SIZE="-1">MD5</font> output protocol. </p>
<p> Computes the <font SIZE="-1">MD5</font> hash of the data to be written, and on close writes this to the designated output or stdout if none is specified. It can be used to test muxers without writing an actual file. </p>
<p> Some examples follow. </p>
<pre>
        # Write the MD5 hash of the encoded AVI file to the file output.avi.md5.
        ffmpeg -i input.flv -f avi -y md5:output.avi.md5
        
        # Write the MD5 hash of the encoded AVI file to stdout.
        ffmpeg -i input.flv -f avi -y md5:
</pre>
<p> Note that some formats (typically <font SIZE="-1">MOV</font>) require the output protocol to be seekable, so they will fail with the <font SIZE="-1">MD5</font> output protocol.</p>
<h3>pipe</h3>
<p> <font SIZE="-1">UNIX</font> pipe access protocol. </p>
<p> Read and write from <font SIZE="-1">UNIX</font> pipes. </p>
<p> The accepted syntax is: </p>
<pre>
        pipe:[&lt;number&gt;]
</pre>
<p> <i>number</i> is the number corresponding to the file descriptor of the pipe (e.g. 0 for stdin, 1 for stdout, 2 for stderr). If <i>number</i> is not specified, by default the stdout file descriptor will be used for writing, stdin for reading. </p>
<p> For example to read from stdin with <code>ffmpeg</code>: </p>
<pre>
        cat test.wav | ffmpeg -i pipe:0
        # ...this is the same as...
        cat test.wav | ffmpeg -i pipe:
</pre>
<p> For writing to stdout with <code>ffmpeg</code>: </p>
<pre>
        ffmpeg -i test.wav -f avi pipe:1 | cat &gt; test.avi
        # ...this is the same as...
        ffmpeg -i test.wav -f avi pipe: | cat &gt; test.avi
</pre>
<p> This protocol accepts the following options:</p>
<dl>
<dt><code>blocksize</code></p>
<dd> Set I/O operation maximum block size, in bytes. Default value is <tt>&quot;INT_MAX&quot;</tt>, which results in not limiting the requested block size. Setting this value reasonably low improves user termination request reaction time, which is valuable if data transmission is slow.</dl>
<p> Note that some formats (typically <font SIZE="-1">MOV</font>), require the output protocol to be seekable, so they will fail with the pipe output protocol.</p>
<h3>prompeg</h3>
<p> Pro-MPEG Code of Practice #3 Release 2 <font SIZE="-1">FEC</font> protocol. </p>
<p> The Pro-MPEG CoP#3 <font SIZE="-1">FEC</font> is a 2D parity-check forward error correction mechanism for <font SIZE="-1">MPEG-2</font> Transport Streams sent over <font SIZE="-1">RTP.</font> </p>
<p> This protocol must be used in conjunction with the <tt>&quot;rtp_mpegts&quot;</tt> muxer and the <tt>&quot;rtp&quot;</tt> protocol. </p>
<p> The required syntax is: </p>
<pre>
        -f rtp_mpegts -fec prompeg=&lt;option&gt;=&lt;val&gt;... rtp://&lt;hostname&gt;:&lt;port&gt;
</pre>
<p> The destination <font SIZE="-1">UDP</font> ports are <tt>&quot;port + 2&quot;</tt> for the column <font SIZE="-1">FEC</font> stream and <tt>&quot;port + 4&quot;</tt> for the row <font SIZE="-1">FEC</font> stream. </p>
<p> This protocol accepts the following options:</p>
<dl>
<dt><code>l=</code><i>n</i></p>
<dd> The number of columns (4-20, LxD &lt;= 100)</p>
<dt><code>d=</code><i>n</i></p>
<dd> The number of rows (4-20, LxD &lt;= 100)</dl>
<p> Example usage: </p>
<pre>
        -f rtp_mpegts -fec prompeg=l=8:d=4 rtp://&lt;hostname&gt;:&lt;port&gt;
</pre>
<h3>rist</h3>
<p> Reliable Internet Streaming Transport protocol </p>
<p> The accepted options are:</p>
<dl>
<dt><code>rist_profile</code></p>
<dd> Supported values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>simple</code></p>
<dd>
<dt><code>main</code></p>
<dd> This one is default.</p>
<dt><code>advanced</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>buffer_size</code></p>
<dd> Set internal <font SIZE="-1">RIST</font> buffer size in milliseconds for retransmission of data. Default value is 0 which means the librist default (1 sec). Maximum value is 30 seconds.</p>
<dt><code>pkt_size</code></p>
<dd> Set maximum packet size for sending data. 1316 by default.</p>
<dt><code>log_level</code></p>
<dd> Set loglevel for <font SIZE="-1">RIST</font> logging messages. You only need to set this if you explicitly want to enable debug level messages or packet loss simulation, otherwise the regular loglevel is respected.</p>
<dt><code>secret</code></p>
<dd> Set override of encryption secret, by default is unset.</p>
<dt><code>encryption</code></p>
<dd> Set encryption type, by default is disabled. Acceptable values are 128 and 256.</dl>
<h3>rtmp</h3>
<p> Real-Time Messaging Protocol. </p>
<p> The Real-Time Messaging Protocol (<font SIZE="-1">RTMP</font>) is used for streaming multimedia content across a <font SIZE="-1">TCP/IP</font> network. </p>
<p> The required syntax is: </p>
<p>rtmp: //[&lt;username&gt;:&lt;password&gt;@]&lt;server&gt;[:&lt;port&gt;][/&lt;app&gt;][/&lt;instance&gt;][/&lt;playpath&gt;]</p>
<p> The accepted parameters are:</p>
<dl>
<dt><code>username</code></p>
<dd> An optional username (mostly for publishing).</p>
<dt><code>password</code></p>
<dd> An optional password (mostly for publishing).</p>
<dt><code>server</code></p>
<dd> The address of the <font SIZE="-1">RTMP</font> server.</p>
<dt><code>port</code></p>
<dd> The number of the <font SIZE="-1">TCP</font> port to use (by default is 1935).</p>
<dt><code>app</code></p>
<dd> It is the name of the application to access. It usually corresponds to the path where the application is installed on the <font SIZE="-1">RTMP</font> server (e.g. <i>/ondemand/</i>, <i>/flash/live/</i>, etc.). You can override the value parsed from the <font SIZE="-1">URI</font> through the <tt>&quot;rtmp_app&quot;</tt> option, too.</p>
<dt><code>playpath</code></p>
<dd> It is the path or name of the resource to play with reference to the application specified in <i>app</i>, may be prefixed by &#8220;mp4:&#8221;. You can override the value parsed from the <font SIZE="-1">URI</font> through the <tt>&quot;rtmp_playpath&quot;</tt> option, too.</p>
<dt><code>listen</code></p>
<dd> Act as a server, listening for an incoming connection.</p>
<dt><code>timeout</code></p>
<dd> Maximum time to wait for the incoming connection. Implies listen.</dl>
<p> Additionally, the following parameters can be set via command line options (or in code via <tt>&quot;AVOption&quot;</tt>s):</p>
<dl>
<dt><code>rtmp_app</code></p>
<dd> Name of application to connect on the <font SIZE="-1">RTMP</font> server. This option overrides the parameter specified in the <font SIZE="-1">URI.</font></p>
<dt><code>rtmp_buffer</code></p>
<dd> Set the client buffer time in milliseconds. The default is 3000.</p>
<dt><code>rtmp_conn</code></p>
<dd> Extra arbitrary <font SIZE="-1">AMF</font> connection parameters, parsed from a string, e.g. like <tt>&quot;B:1 S:authMe O:1 NN:code:1.23 NS:flag:ok O:0&quot;</tt>. Each value is prefixed by a single character denoting the type, B for Boolean, N for number, S for string, O for object, or Z for null, followed by a colon. For Booleans the data must be either 0 or 1 for <font SIZE="-1">FALSE</font> or <font SIZE="-1">TRUE,</font> respectively. Likewise for Objects the data must be 0 or 1 to end or begin an object, respectively. Data items in subobjects may be named, by prefixing the type with &#8216;N&#8217; and specifying the name before the value (i.e. <tt>&quot;NB:myFlag:1&quot;</tt>). This option may be used multiple times to construct arbitrary <font SIZE="-1">AMF</font> sequences.</p>
<dt><code>rtmp_flashver</code></p>
<dd> Version of the Flash plugin used to run the <font SIZE="-1">SWF</font> player. The default is <font SIZE="-1">LNX 9,0,124,2.</font> (When publishing, the default is <font SIZE="-1">FMLE/3.0</font> (compatible; &lt;libavformat version&gt;).)</p>
<dt><code>rtmp_flush_interval</code></p>
<dd> Number of packets flushed in the same request (<font SIZE="-1">RTMPT</font> only). The default is 10.</p>
<dt><code>rtmp_live</code></p>
<dd> Specify that the media is a live stream. No resuming or seeking in live streams is possible. The default value is <tt>&quot;any&quot;</tt>, which means the subscriber first tries to play the live stream specified in the playpath. If a live stream of that name is not found, it plays the recorded stream. The other possible values are <tt>&quot;live&quot;</tt> and <tt>&quot;recorded&quot;</tt>.</p>
<dt><code>rtmp_pageurl</code></p>
<dd> <font SIZE="-1">URL</font> of the web page in which the media was embedded. By default no value will be sent.</p>
<dt><code>rtmp_playpath</code></p>
<dd> Stream identifier to play or to publish. This option overrides the parameter specified in the <font SIZE="-1">URI.</font></p>
<dt><code>rtmp_subscribe</code></p>
<dd> Name of live stream to subscribe to. By default no value will be sent. It is only sent if the option is specified or if rtmp_live is set to live.</p>
<dt><code>rtmp_swfhash</code></p>
<dd> <font SIZE="-1">SHA256</font> hash of the decompressed <font SIZE="-1">SWF</font> file (32 bytes).</p>
<dt><code>rtmp_swfsize</code></p>
<dd> Size of the decompressed <font SIZE="-1">SWF</font> file, required for SWFVerification.</p>
<dt><code>rtmp_swfurl</code></p>
<dd> <font SIZE="-1">URL</font> of the <font SIZE="-1">SWF</font> player for the media. By default no value will be sent.</p>
<dt><code>rtmp_swfverify</code></p>
<dd> <font SIZE="-1">URL</font> to player swf file, compute hash/size automatically.</p>
<dt><code>rtmp_tcurl</code></p>
<dd> <font SIZE="-1">URL</font> of the target stream. Defaults to <a href="proto://host[:port]/app.">proto://host[:port]/app.</a></dl>
<p> For example to read with <code>ffplay</code> a multimedia resource named &#8220;sample&#8221; from the application &#8220;vod&#8221; from an <font SIZE="-1">RTMP</font> server &#8220;myserver&#8221;: </p>
<pre>
        ffplay <a href="rtmp://myserver/vod/sample">rtmp://myserver/vod/sample</a>
</pre>
<p> To publish to a password protected server, passing the playpath and app names separately: </p>
<pre>
        ffmpeg -re -i &lt;input&gt; -f flv -rtmp_playpath some/long/path -rtmp_app long/app/name <a href="rtmp://username:password@myserver/">rtmp://username:password@myserver/</a>
</pre>
<h3>rtmpe</h3>
<p> Encrypted Real-Time Messaging Protocol. </p>
<p> The Encrypted Real-Time Messaging Protocol (<font SIZE="-1">RTMPE</font>) is used for streaming multimedia content within standard cryptographic primitives, consisting of Diffie-Hellman key exchange and <font SIZE="-1">HMACSHA256,</font> generating a pair of <font SIZE="-1">RC4</font> keys.</p>
<h3>rtmps</h3>
<p> Real-Time Messaging Protocol over a secure <font SIZE="-1">SSL</font> connection. </p>
<p> The Real-Time Messaging Protocol (<font SIZE="-1">RTMPS</font>) is used for streaming multimedia content across an encrypted connection.</p>
<h3>rtmpt</h3>
<p> Real-Time Messaging Protocol tunneled through <font SIZE="-1">HTTP.</font> </p>
<p> The Real-Time Messaging Protocol tunneled through <font SIZE="-1">HTTP</font> (<font SIZE="-1">RTMPT</font>) is used for streaming multimedia content within <font SIZE="-1">HTTP</font> requests to traverse firewalls.</p>
<h3>rtmpte</h3>
<p> Encrypted Real-Time Messaging Protocol tunneled through <font SIZE="-1">HTTP.</font> </p>
<p> The Encrypted Real-Time Messaging Protocol tunneled through <font SIZE="-1">HTTP</font> (<font SIZE="-1">RTMPTE</font>) is used for streaming multimedia content within <font SIZE="-1">HTTP</font> requests to traverse firewalls.</p>
<h3>rtmpts</h3>
<p> Real-Time Messaging Protocol tunneled through <font SIZE="-1">HTTPS.</font> </p>
<p> The Real-Time Messaging Protocol tunneled through <font SIZE="-1">HTTPS</font> (<font SIZE="-1">RTMPTS</font>) is used for streaming multimedia content within <font SIZE="-1">HTTPS</font> requests to traverse firewalls.</p>
<h3>libsmbclient</h3>
<p> libsmbclient permits one to manipulate <font SIZE="-1">CIFS/SMB</font> network resources. </p>
<p> Following syntax is required. </p>
<p>smb: //[[domain:]user[:password@]]server[/share[/path[/file]]]</p>
<p> This protocol accepts the following options.</p>
<dl>
<dt><code>timeout</code></p>
<dd> Set timeout in milliseconds of socket I/O operations used by the underlying low level operation. By default it is set to -1, which means that the timeout is not specified.</p>
<dt><code>truncate</code></p>
<dd> Truncate existing files on write, if set to 1. A value of 0 prevents truncating. Default value is 1.</p>
<dt><code>workgroup</code></p>
<dd> Set the workgroup used for making connections. By default workgroup is not specified.</dl>
<p> For more information see: &lt;<code><a rel="nofollow" href="http://www.samba.org/">http://www.samba.org/</a></code>&gt;.</p>
<h3>libssh</h3>
<p> Secure File Transfer Protocol via libssh </p>
<p> Read from or write to remote resources using <font SIZE="-1">SFTP</font> protocol. </p>
<p> Following syntax is required. </p>
<p>sftp: //[user[:password]@]server[:port]/path/to/remote/resource.mpeg</p>
<p> This protocol accepts the following options.</p>
<dl>
<dt><code>timeout</code></p>
<dd> Set timeout of socket I/O operations used by the underlying low level operation. By default it is set to -1, which means that the timeout is not specified.</p>
<dt><code>truncate</code></p>
<dd> Truncate existing files on write, if set to 1. A value of 0 prevents truncating. Default value is 1.</p>
<dt><code>private_key</code></p>
<dd> Specify the path of the file containing private key to use during authorization. By default libssh searches for keys in the <i>~/.ssh/</i> directory.</dl>
<p> Example: Play a file stored on remote server. </p>
<pre>
        ffplay <a href="sftp://user:password@server_address:22/home/user/resource.mpeg">sftp://user:password@server_address:22/home/user/resource.mpeg</a>
</pre>
<h3>librtmp rtmp, rtmpe, rtmps, rtmpt, rtmpte</h3>
<p> Real-Time Messaging Protocol and its variants supported through librtmp. </p>
<p> Requires the presence of the librtmp headers and library during configuration. You need to explicitly configure the build with &#8220;&#8211;enable-librtmp&#8221;. If enabled this will replace the native <font SIZE="-1">RTMP</font> protocol. </p>
<p> This protocol provides most client functions and a few server functions needed to support <font SIZE="-1">RTMP, RTMP</font> tunneled in <font SIZE="-1">HTTP</font> (<font SIZE="-1">RTMPT</font>), encrypted <font SIZE="-1">RTMP</font> (<font SIZE="-1">RTMPE</font>), <font SIZE="-1">RTMP</font> over <font SIZE="-1">SSL/TLS</font> (<font SIZE="-1">RTMPS</font>) and tunneled variants of these encrypted types (<font SIZE="-1">RTMPTE, RTMPTS</font>). </p>
<p> The required syntax is: </p>
<p>        &lt;rtmp_proto&gt;://&lt;server&gt;[:&lt;port&gt;][/&lt;app&gt;][/&lt;playpath&gt;] &lt;options&gt;</p>
<p> where <i>rtmp_proto</i> is one of the strings &#8220;rtmp&#8221;, &#8220;rtmpt&#8221;, &#8220;rtmpe&#8221;, &#8220;rtmps&#8221;, &#8220;rtmpte&#8221;, &#8220;rtmpts&#8221; corresponding to each <font SIZE="-1">RTMP</font> variant, and <i>server</i>, <i>port</i>, <i>app</i> and <i>playpath</i> have the same meaning as specified for the <font SIZE="-1">RTMP</font> native protocol. <i>options</i> contains a list of space-separated options of the form <i>key</i>=<i>val</i>. </p>
<p> See the librtmp manual page (man 3 librtmp) for more information. </p>
<p> For example, to stream a file in real-time to an <font SIZE="-1">RTMP</font> server using <code>ffmpeg</code>: </p>
<pre>
        ffmpeg -re -i myfile -f flv <a href="rtmp://myserver/live/mystream">rtmp://myserver/live/mystream</a>
</pre>
<p> To play the same stream using <code>ffplay</code>: </p>
<pre>
        ffplay &quot;<a href="rtmp://myserver/live/mystream">rtmp://myserver/live/mystream</a> live=1&quot;
</pre>
<h3>rtp</h3>
<p> Real-time Transport Protocol. </p>
<p> The required syntax for an <font SIZE="-1">RTP URL</font> is: rtp://<i>hostname</i>[:<i>port</i>][?<i>option</i>=<i>val</i>&#8230;] </p>
<p> <i>port</i> specifies the <font SIZE="-1">RTP</font> port to use. </p>
<p> The following <font SIZE="-1">URL</font> options are supported:</p>
<dl>
<dt><code>ttl=</code><i>n</i></p>
<dd> Set the <font SIZE="-1">TTL</font> (Time-To-Live) value (for multicast only).</p>
<dt><code>rtcpport=</code><i>n</i></p>
<dd> Set the remote <font SIZE="-1">RTCP</font> port to <i>n</i>.</p>
<dt><code>localrtpport=</code><i>n</i></p>
<dd> Set the local <font SIZE="-1">RTP</font> port to <i>n</i>.</p>
<dt><code>localrtcpport=</code><i>n</i><code>&#8216;</code></p>
<dd> Set the local <font SIZE="-1">RTCP</font> port to <i>n</i>.</p>
<dt><code>pkt_size=</code><i>n</i></p>
<dd> Set max packet size (in bytes) to <i>n</i>.</p>
<dt><code>buffer_size=</code><i>size</i></p>
<dd> Set the maximum <font SIZE="-1">UDP</font> socket buffer size in bytes.</p>
<dt><code>connect=0|1</code></p>
<dd> Do a <tt>&quot;connect()&quot;</tt> on the <font SIZE="-1">UDP</font> socket (if set to 1) or not (if set to 0).</p>
<dt><code>sources=</code><i>ip</i><code>[,</code><i>ip</i><code>]</code></p>
<dd> List allowed source <font SIZE="-1">IP</font> addresses.</p>
<dt><code>block=</code><i>ip</i><code>[,</code><i>ip</i><code>]</code></p>
<dd> List disallowed (blocked) source <font SIZE="-1">IP</font> addresses.</p>
<dt><code>write_to_source=0|1</code></p>
<dd> Send packets to the source address of the latest received packet (if set to 1) or to a default remote address (if set to 0).</p>
<dt><code>localport=</code><i>n</i></p>
<dd> Set the local <font SIZE="-1">RTP</font> port to <i>n</i>.</p>
<dt><code>timeout=</code><i>n</i></p>
<dd> Set timeout (in microseconds) of socket I/O operations to <i>n</i>. </p>
<p> This is a deprecated option. Instead, <code>localrtpport</code> should be used.</dl>
<p> Important notes:</p>
<dl>
<dt>1.</p>
<dd> If <code>rtcpport</code> is not set the <font SIZE="-1">RTCP</font> port will be set to the <font SIZE="-1">RTP</font> port value plus 1.</p>
<dt>2.</p>
<dd> If <code>localrtpport</code> (the local <font SIZE="-1">RTP</font> port) is not set any available port will be used for the local <font SIZE="-1">RTP</font> and <font SIZE="-1">RTCP</font> ports.</p>
<dt>3.</p>
<dd> If <code>localrtcpport</code> (the local <font SIZE="-1">RTCP</font> port) is not set it will be set to the local <font SIZE="-1">RTP</font> port value plus 1.</dl>
<h3>rtsp</h3>
<p> Real-Time Streaming Protocol. </p>
<p> <font SIZE="-1">RTSP</font> is not technically a protocol handler in libavformat, it is a demuxer and muxer. The demuxer supports both normal <font SIZE="-1">RTSP</font> (with data transferred over <font SIZE="-1">RTP</font>; this is used by e.g. Apple and Microsoft) and Real-RTSP (with data transferred over <font SIZE="-1">RDT</font>). </p>
<p> The muxer can be used to send a stream using <font SIZE="-1">RTSP ANNOUNCE</font> to a server supporting it (currently Darwin Streaming Server and Mischa Spiegelmock&#8217;s &lt;<code><a rel="nofollow" href="https://github.com/revmischa/rtsp-server">https://github.com/revmischa/rtsp-server</a></code>&gt;). </p>
<p> The required syntax for a <font SIZE="-1">RTSP</font> url is: </p>
<pre>
        rtsp://&lt;hostname&gt;[:&lt;port&gt;]/&lt;path&gt;
</pre>
<p> Options can be set on the <code>ffmpeg</code>/<code>ffplay</code> command line, or set in code via <tt>&quot;AVOption&quot;</tt>s or in <tt>&quot;avformat_open_input&quot;</tt>. </p>
<p> The following options are supported.</p>
<dl>
<dt><code>initial_pause</code></p>
<dd> Do not start playing the stream immediately if set to 1. Default value is 0.</p>
<dt><code>rtsp_transport</code></p>
<dd> Set <font SIZE="-1">RTSP</font> transport protocols. </p>
<p> It accepts the following values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>udp</code></p>
<dd> Use <font SIZE="-1">UDP</font> as lower transport protocol.</p>
<dt><code>tcp</code></p>
<dd> Use <font SIZE="-1">TCP</font> (interleaving within the <font SIZE="-1">RTSP</font> control channel) as lower transport protocol.</p>
<dt><code>udp_multicast</code></p>
<dd> Use <font SIZE="-1">UDP</font> multicast as lower transport protocol.</p>
<dt><code>http</code></p>
<dd> Use <font SIZE="-1">HTTP</font> tunneling as lower transport protocol, which is useful for passing proxies.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Multiple lower transport protocols may be specified, in that case they are tried one at a time (if the setup of one fails, the next one is tried). For the muxer, only the <code>tcp</code> and <code>udp</code> options are supported.</dl>
<dt><code>rtsp_flags</code></p>
<dd> Set <font SIZE="-1">RTSP</font> flags. </p>
<p> The following values are accepted:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>filter_src</code></p>
<dd> Accept packets only from negotiated peer address and port.</p>
<dt><code>listen</code></p>
<dd> Act as a server, listening for an incoming connection.</p>
<dt><code>prefer_tcp</code></p>
<dd> Try <font SIZE="-1">TCP</font> for <font SIZE="-1">RTP</font> transport first, if <font SIZE="-1">TCP</font> is available as <font SIZE="-1">RTSP RTP</font> transport.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Default value is <code>none</code>.</dl>
<dt><code>allowed_media_types</code></p>
<dd> Set media types to accept from the server. </p>
<p> The following flags are accepted:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>video</code></p>
<dd>
<dt><code>audio</code></p>
<dd>
<dt><code>data</code></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> By default it accepts all media types.</dl>
<dt><code>min_port</code></p>
<dd> Set minimum local <font SIZE="-1">UDP</font> port. Default value is 5000.</p>
<dt><code>max_port</code></p>
<dd> Set maximum local <font SIZE="-1">UDP</font> port. Default value is 65000.</p>
<dt><code>timeout</code></p>
<dd> Set maximum timeout (in seconds) to wait for incoming connections. </p>
<p> A value of -1 means infinite (default). This option implies the <code>rtsp_flags</code> set to <code>listen</code>.</p>
<dt><code>reorder_queue_size</code></p>
<dd> Set number of packets to buffer for handling of reordered packets.</p>
<dt><code>stimeout</code></p>
<dd> Set socket <font SIZE="-1">TCP I/O</font> timeout in microseconds.</p>
<dt><code>user-agent</code></p>
<dd> Override User-Agent header. If not specified, it defaults to the libavformat identifier string.</dl>
<p> When receiving data over <font SIZE="-1">UDP,</font> the demuxer tries to reorder received packets (since they may arrive out of order, or packets may get lost totally). This can be disabled by setting the maximum demuxing delay to zero (via the <tt>&quot;max_delay&quot;</tt> field of AVFormatContext). </p>
<p> When watching multi-bitrate Real-RTSP streams with <code>ffplay</code>, the streams to display can be chosen with <tt>&quot;-vst&quot;</tt> <i>n</i> and <tt>&quot;-ast&quot;</tt> <i>n</i> for video and audio respectively, and can be switched on the fly by pressing <tt>&quot;v&quot;</tt> and <tt>&quot;a&quot;</tt>. </p>
<p> <i>Examples</i> </p>
<p> The following examples all make use of the <code>ffplay</code> and <code>ffmpeg</code> tools.</p>
<dl>
<dt>&bull;</p>
<dd> Watch a stream over <font SIZE="-1">UDP,</font> with a max reordering delay of 0.5 seconds: </p>
<pre>
        ffplay -max_delay 500000 -rtsp_transport udp <a href="rtsp://server/video.mp4">rtsp://server/video.mp4</a>
</pre>
<dt>&bull;</p>
<dd> Watch a stream tunneled over <font SIZE="-1">HTTP:</font> </p>
<pre>
        ffplay -rtsp_transport http <a href="rtsp://server/video.mp4">rtsp://server/video.mp4</a>
</pre>
<dt>&bull;</p>
<dd> Send a stream in realtime to a <font SIZE="-1">RTSP</font> server, for others to watch: </p>
<pre>
        ffmpeg -re -i &lt;input&gt; -f rtsp -muxdelay 0.1 <a href="rtsp://server/live.sdp">rtsp://server/live.sdp</a>
</pre>
<dt>&bull;</p>
<dd> Receive a stream in realtime: </p>
<pre>
        ffmpeg -rtsp_flags listen -i <a href="rtsp://ownaddress/live.sdp">rtsp://ownaddress/live.sdp</a> &lt;output&gt;
</pre>
</dl>
<h3>sap</h3>
<p> Session Announcement Protocol (<font SIZE="-1">RFC 2974</font>). This is not technically a protocol handler in libavformat, it is a muxer and demuxer. It is used for signalling of <font SIZE="-1">RTP</font> streams, by announcing the <font SIZE="-1">SDP</font> for the streams regularly on a separate port. </p>
<p> <i>Muxer</i> </p>
<p> The syntax for a <font SIZE="-1">SAP</font> url given to the muxer is: </p>
<p>sap: //&lt;destination&gt;[:&lt;port&gt;][?&lt;options&gt;]</p>
<p> The <font SIZE="-1">RTP</font> packets are sent to <i>destination</i> on port <i>port</i>, or to port 5004 if no port is specified. <i>options</i> is a <tt>&quot;&amp;&quot;</tt>-separated list. The following options are supported:</p>
<dl>
<dt><code>announce_addr=</code><i>address</i></p>
<dd> Specify the destination <font SIZE="-1">IP</font> address for sending the announcements to. If omitted, the announcements are sent to the commonly used <font SIZE="-1">SAP</font> announcement multicast address 224.2.127.254 (sap.mcast.net), or ff0e::2:7ffe if <i>destination</i> is an IPv6 address.</p>
<dt><code>announce_port=</code><i>port</i></p>
<dd> Specify the port to send the announcements on, defaults to 9875 if not specified.</p>
<dt><code>ttl=</code><i>ttl</i></p>
<dd> Specify the time to live value for the announcements and <font SIZE="-1">RTP</font> packets, defaults to 255.</p>
<dt><code>same_port=</code><i>0|1</i></p>
<dd> If set to 1, send all <font SIZE="-1">RTP</font> streams on the same port pair. If zero (the default), all streams are sent on unique ports, with each stream on a port 2 numbers higher than the previous. VLC/Live555 requires this to be set to 1, to be able to receive the stream. The <font SIZE="-1">RTP</font> stack in libavformat for receiving requires all streams to be sent on unique ports.</dl>
<p> Example command lines follow. </p>
<p> To broadcast a stream on the local subnet, for watching in <font SIZE="-1">VLC:</font> </p>
<pre>
        ffmpeg -re -i &lt;input&gt; -f sap <a href="sap://224.0.0.255?same_port=1">sap://224.0.0.255?same_port=1</a>
</pre>
<p> Similarly, for watching in <code>ffplay</code>: </p>
<pre>
        ffmpeg -re -i &lt;input&gt; -f sap <a href="sap://224.0.0.255">sap://224.0.0.255</a>
</pre>
<p> And for watching in <code>ffplay</code>, over IPv6: </p>
<pre>
        ffmpeg -re -i &lt;input&gt; -f sap <a href="sap://[ff0e::1:2:3:4]">sap://[ff0e::1:2:3:4]</a>
</pre>
<p> <i>Demuxer</i> </p>
<p> The syntax for a <font SIZE="-1">SAP</font> url given to the demuxer is: </p>
<pre><code>
sap: //[&lt;address&gt;][:&lt;port&gt;]
</code></pre>
<p> <i>address</i> is the multicast address to listen for announcements on, if omitted, the default 224.2.127.254 (sap.mcast.net) is used. <i>port</i> is the port that is listened on, 9875 if omitted. </p>
<p> The demuxers listens for announcements on the given address and port. Once an announcement is received, it tries to receive that particular stream. </p>
<p> Example command lines follow. </p>
<p> To play back the first stream announced on the normal <font SIZE="-1">SAP</font> multicast address: </p>
<pre>
        ffplay sap://
</pre>
<p> To play back the first stream announced on one the default IPv6 <font SIZE="-1">SAP</font> multicast address: </p>
<pre>
        ffplay <a href="sap://[ff0e::2:7ffe]">sap://[ff0e::2:7ffe]</a>
</pre>
<h3>sctp</h3>
<p> Stream Control Transmission Protocol. </p>
<p> The accepted <font SIZE="-1">URL</font> syntax is: </p>
<pre>
        sctp://&lt;host&gt;:&lt;port&gt;[?&lt;options&gt;]
</pre>
<p> The protocol accepts the following options:</p>
<dl>
<dt><code>listen</code></p>
<dd> If set to any value, listen for an incoming connection. Outgoing connection is done by default.</p>
<dt><code>max_streams</code></p>
<dd> Set the maximum number of streams. By default no limit is set.</dl>
<h3>srt</h3>
<p> Haivision Secure Reliable Transport Protocol via libsrt. </p>
<p> The supported syntax for a <font SIZE="-1">SRT URL</font> is: </p>
<pre>
        srt://&lt;hostname&gt;:&lt;port&gt;[?&lt;options&gt;]
</pre>
<p> <i>options</i> contains a list of &amp;-separated options of the form <i>key</i>=<i>val</i>. </p>
<p> or </p>
<pre>
        &lt;options&gt; srt://&lt;hostname&gt;:&lt;port&gt;
</pre>
<p> <i>options</i> contains a list of &#8216;-<i>key</i> <i>val</i>&#8216; options. </p>
<p> This protocol accepts the following options.</p>
<dl>
<dt><code>connect_timeout=</code><i>milliseconds</i></p>
<dd> Connection timeout; <font SIZE="-1">SRT</font> cannot connect for <font SIZE="-1">RTT</font> &gt; 1500 msec (2 handshake exchanges) with the default connect timeout of 3 seconds. This option applies to the caller and rendezvous connection modes. The connect timeout is 10 times the value set for the rendezvous mode (which can be used as a workaround for this connection problem with earlier versions).</p>
<dt><code>ffs=</code><i>bytes</i></p>
<dd> Flight Flag Size (Window Size), in bytes. <font SIZE="-1">FFS</font> is actually an internal parameter and you should set it to not less than <code>recv_buffer_size</code> and <code>mss</code>. The default value is relatively large, therefore unless you set a very large receiver buffer, you do not need to change this option. Default value is 25600.</p>
<dt><code>inputbw=</code><i>bytes/seconds</i></p>
<dd> Sender nominal input rate, in bytes per seconds. Used along with <code>oheadbw</code>, when <code>maxbw</code> is set to relative (0), to calculate maximum sending rate when recovery packets are sent along with the main media stream: <code>inputbw</code> * (100 + <code>oheadbw</code>) / 100 if <code>inputbw</code> is not set while <code>maxbw</code> is set to relative (0), the actual input rate is evaluated inside the library. Default value is 0.</p>
<dt><code>iptos=</code><i>tos</i></p>
<dd> <font SIZE="-1">IP</font> Type of Service. Applies to sender only. Default value is 0xB8.</p>
<dt><code>ipttl=</code><i>ttl</i></p>
<dd> <font SIZE="-1">IP</font> Time To Live. Applies to sender only. Default value is 64.</p>
<dt><code>latency=</code><i>microseconds</i></p>
<dd> Timestamp-based Packet Delivery Delay. Used to absorb bursts of missed packet retransmissions. This flag sets both <code>rcvlatency</code> and <code>peerlatency</code> to the same value. Note that prior to version 1.3.0 this is the only flag to set the latency, however this is effectively equivalent to setting <code>peerlatency</code>, when side is sender and <code>rcvlatency</code> when side is receiver, and the bidirectional stream sending is not supported.</p>
<dt><code>listen_timeout=</code><i>microseconds</i></p>
<dd> Set socket listen timeout.</p>
<dt><code>maxbw=</code><i>bytes/seconds</i></p>
<dd> Maximum sending bandwidth, in bytes per seconds. -1 infinite (<font SIZE="-1">CSRTCC</font> limit is 30mbps) 0 relative to input rate (see <code>inputbw</code>) &gt;0 absolute limit value Default value is 0 (relative)</p>
<dt><code>mode=</code><i>caller|listener|rendezvous</i></p>
<dd> Connection mode. <code>caller</code> opens client connection. <code>listener</code> starts server to listen for incoming connections. <code>rendezvous</code> use Rendez-Vous connection mode. Default value is caller.</p>
<dt><code>mss=</code><i>bytes</i></p>
<dd> Maximum Segment Size, in bytes. Used for buffer allocation and rate calculation using a packet counter assuming fully filled packets. The smallest <font SIZE="-1">MSS</font> between the peers is used. This is 1500 by default in the overall internet. This is the maximum size of the <font SIZE="-1">UDP</font> packet and can be only decreased, unless you have some unusual dedicated network settings. Default value is 1500.</p>
<dt><code>nakreport=</code><i>1|0</i></p>
<dd> If set to 1, Receiver will send `UMSG_LOSSREPORT` messages periodically until a lost packet is retransmitted or intentionally dropped. Default value is 1.</p>
<dt><code>oheadbw=</code><i>percents</i></p>
<dd> Recovery bandwidth overhead above input rate, in percents. See <code>inputbw</code>. Default value is 25%.</p>
<dt><code>passphrase=</code><i>string</i></p>
<dd> HaiCrypt Encryption/Decryption Passphrase string, length from 10 to 79 characters. The passphrase is the shared secret between the sender and the receiver. It is used to generate the Key Encrypting Key using <font SIZE="-1">PBKDF2</font> (Password-Based Key Derivation Function). It is used only if <code>pbkeylen</code> is non-zero. It is used on the receiver only if the received data is encrypted. The configured passphrase cannot be recovered (write-only).</p>
<dt><code>enforced_encryption=</code><i>1|0</i></p>
<dd> If true, both connection parties must have the same password set (including empty, that is, with no encryption). If the password doesn&#8217;t match or only one side is unencrypted, the connection is rejected. Default is true.</p>
<dt><code>kmrefreshrate=</code><i>packets</i></p>
<dd> The number of packets to be transmitted after which the encryption key is switched to a new key. Default is -1. -1 means auto (0x1000000 in srt library). The range for this option is integers in the 0 &#8211; <tt>&quot;INT_MAX&quot;</tt>.</p>
<dt><code>kmpreannounce=</code><i>packets</i></p>
<dd> The interval between when a new encryption key is sent and when switchover occurs. This value also applies to the subsequent interval between when switchover occurs and when the old encryption key is decommissioned. Default is -1. -1 means auto (0x1000 in srt library). The range for this option is integers in the 0 &#8211; <tt>&quot;INT_MAX&quot;</tt>.</p>
<dt><code>payload_size=</code><i>bytes</i></p>
<dd> Sets the maximum declared size of a packet transferred during the single call to the sending function in Live mode. Use 0 if this value isn&#8217;t used (which is default in file mode). Default is -1 (automatic), which typically means MPEG-TS; if you are going to use <font SIZE="-1">SRT</font> to send any different kind of payload, such as, for example, wrapping a live stream in very small frames, then you can use a bigger maximum frame size, though not greater than 1456 bytes.</p>
<dt><code>pkt_size=</code><i>bytes</i></p>
<dd> Alias for <code>payload_size</code>.</p>
<dt><code>peerlatency=</code><i>microseconds</i></p>
<dd> The latency value (as described in <code>rcvlatency</code>) that is set by the sender side as a minimum value for the receiver.</p>
<dt><code>pbkeylen=</code><i>bytes</i></p>
<dd> Sender encryption key length, in bytes. Only can be set to 0, 16, 24 and 32. Enable sender encryption if not 0. Not required on receiver (set to 0), key size obtained from sender in HaiCrypt handshake. Default value is 0.</p>
<dt><code>rcvlatency=</code><i>microseconds</i></p>
<dd> The time that should elapse since the moment when the packet was sent and the moment when it&#8217;s delivered to the receiver application in the receiving function. This time should be a buffer time large enough to cover the time spent for sending, unexpectedly extended <font SIZE="-1">RTT</font> time, and the time needed to retransmit the lost <font SIZE="-1">UDP</font> packet. The effective latency value will be the maximum of this options&#8217; value and the value of <code>peerlatency</code> set by the peer side. Before version 1.3.0 this option is only available as <code>latency</code>.</p>
<dt><code>recv_buffer_size=</code><i>bytes</i></p>
<dd> Set <font SIZE="-1">UDP</font> receive buffer size, expressed in bytes.</p>
<dt><code>send_buffer_size=</code><i>bytes</i></p>
<dd> Set <font SIZE="-1">UDP</font> send buffer size, expressed in bytes.</p>
<dt><code>timeout=</code><i>microseconds</i></p>
<dd> Set raise error timeouts for read, write and connect operations. Note that the <font SIZE="-1">SRT</font> library has internal timeouts which can be controlled separately, the value set here is only a cap on those.</p>
<dt><code>tlpktdrop=</code><i>1|0</i></p>
<dd> Too-late Packet Drop. When enabled on receiver, it skips missing packets that have not been delivered in time and delivers the following packets to the application when their time-to-play has come. It also sends a fake <font SIZE="-1">ACK</font> to the sender. When enabled on sender and enabled on the receiving peer, the sender drops the older packets that have no chance of being delivered in time. It was automatically enabled in the sender if the receiver supports it.</p>
<dt><code>sndbuf=</code><i>bytes</i></p>
<dd> Set send buffer size, expressed in bytes.</p>
<dt><code>rcvbuf=</code><i>bytes</i></p>
<dd> Set receive buffer size, expressed in bytes. </p>
<p> Receive buffer must not be greater than <code>ffs</code>.</p>
<dt><code>lossmaxttl=</code><i>packets</i></p>
<dd> The value up to which the Reorder Tolerance may grow. When Reorder Tolerance is &gt; 0, then packet loss report is delayed until that number of packets come in. Reorder Tolerance increases every time a &#8220;belated&#8221; packet has come, but it wasn&#8217;t due to retransmission (that is, when <font SIZE="-1">UDP</font> packets tend to come out of order), with the difference between the latest sequence and this packet&#8217;s sequence, and not more than the value of this option. By default it&#8217;s 0, which means that this mechanism is turned off, and the loss report is always sent immediately upon experiencing a &#8220;gap&#8221; in sequences.</p>
<dt><code>minversion</code></p>
<dd> The minimum <font SIZE="-1">SRT</font> version that is required from the peer. A connection to a peer that does not satisfy the minimum version requirement will be rejected. </p>
<p> The version format in hex is 0xXXYYZZ for x.y.z in human readable form.</p>
<dt><code>streamid=</code><i>string</i></p>
<dd> A string limited to 512 characters that can be set on the socket prior to connecting. This stream <font SIZE="-1">ID</font> will be able to be retrieved by the listener side from the socket that is returned from srt_accept and was connected by a socket with that set stream <font SIZE="-1">ID. SRT</font> does not enforce any special interpretation of the contents of this string. This option doesnXt make sense in Rendezvous connection; the result might be that simply one side will override the value from the other side and itXs the matter of luck which one would win</p>
<dt><code>smoother=</code><i>live|file</i></p>
<dd> The type of Smoother used for the transmission for that socket, which is responsible for the transmission and congestion control. The Smoother type must be exactly the same on both connecting parties, otherwise the connection is rejected.</p>
<dt><code>messageapi=</code><i>1|0</i></p>
<dd> When set, this socket uses the Message <font SIZE="-1">API,</font> otherwise it uses Buffer <font SIZE="-1">API.</font> Note that in live mode (see <code>transtype</code>) thereXs only message <font SIZE="-1">API</font> available. In File mode you can chose to use one of two modes: </p>
<p> Stream <font SIZE="-1">API</font> (default, when this option is false). In this mode you may send as many data as you wish with one sending instruction, or even use dedicated functions that read directly from a file. The internal facility will take care of any speed and congestion control. When receiving, you can also receive as many data as desired, the data not extracted will be waiting for the next call. There is no boundary between data portions in the Stream mode. </p>
<p> Message <font SIZE="-1">API.</font> In this mode your single sending instruction passes exactly one piece of data that has boundaries (a message). Contrary to Live mode, this message may span across multiple <font SIZE="-1">UDP</font> packets and the only size limitation is that it shall fit as a whole in the sending buffer. The receiver shall use as large buffer as necessary to receive the message, otherwise the message will not be given up. When the message is not complete (not all packets received or there was a packet loss) it will not be given up.</p>
<dt><code>transtype=</code><i>live|file</i></p>
<dd> Sets the transmission type for the socket, in particular, setting this option sets multiple other parameters to their default values as required for a particular transmission type. </p>
<p> live: Set options as for live transmission. In this mode, you should send by one sending instruction only so many data that fit in one <font SIZE="-1">UDP</font> packet, and limited to the value defined first in <code>payload_size</code> (1316 is default in this mode). There is no speed control in this mode, only the bandwidth control, if configured, in order to not exceed the bandwidth with the overhead transmission (retransmitted and control packets). </p>
<p> file: Set options as for non-live transmission. See <code>messageapi</code> for further explanations</p>
<dt><code>linger=</code><i>seconds</i></p>
<dd> The number of seconds that the socket waits for unsent data when closing. Default is -1. -1 means auto (off with 0 seconds in live mode, on with 180 seconds in file mode). The range for this option is integers in the 0 &#8211; <tt>&quot;INT_MAX&quot;</tt>.</dl>
<p> For more information see: &lt;<code><a rel="nofollow" href="https://github.com/Haivision/srt">https://github.com/Haivision/srt</a></code>&gt;.</p>
<h3>srtp</h3>
<p> Secure Real-time Transport Protocol. </p>
<p> The accepted options are:</p>
<dl>
<dt><code>srtp_in_suite</code></p>
<dd>
<dt><code>srtp_out_suite</code></p>
<dd> Select input and output encoding suites. </p>
<p> Supported values:</p>
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1"><code>AES_CM_128_HMAC_SHA1_80</code></font></p>
<dd>
<dt><font SIZE="-1"><code>SRTP_AES128_CM_HMAC_SHA1_80</code></font></p>
<dd>
<dt><font SIZE="-1"><code>AES_CM_128_HMAC_SHA1_32</code></font></p>
<dd>
<dt><font SIZE="-1"><code>SRTP_AES128_CM_HMAC_SHA1_32</code></font></p>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>srtp_in_params</code></p>
<dd>
<dt><code>srtp_out_params</code></p>
<dd> Set input and output encoding parameters, which are expressed by a base64-encoded representation of a binary block. The first 16 bytes of this binary block are used as master key, the following 14 bytes are used as master salt.</dl>
<h3>subfile</h3>
<p> Virtually extract a segment of a file or another stream. The underlying stream must be seekable. </p>
<p> Accepted options:</p>
<dl>
<dt><code>start</code></p>
<dd> Start offset of the extracted segment, in bytes.</p>
<dt><code>end</code></p>
<dd> End offset of the extracted segment, in bytes. If set to 0, extract till end of file.</dl>
<p> Examples: </p>
<p> Extract a chapter from a <font SIZE="-1">DVD VOB</font> file (start and end sectors obtained externally and multiplied by 2048): </p>
<pre>
        subfile,,start,153391104,end,268142592,,:/media/dvd/VIDEO_TS/VTS_08_1.VOB
</pre>
<p> Play an <font SIZE="-1">AVI</font> file directly from a <font SIZE="-1">TAR</font> archive: </p>
<pre>
        subfile,,start,183241728,end,366490624,,:archive.tar
</pre>
<p> Play a MPEG-TS file from start offset till end: </p>
<pre>
        subfile,,start,32815239,end,0,,:video.ts
</pre>
<h3>tee</h3>
<p> Writes the output to multiple protocols. The individual outputs are separated by | </p>
<pre>
        tee:file://path/to/local/this.avi|file://path/to/local/that.avi
</pre>
<h3>tcp</h3>
<p> Transmission Control Protocol. </p>
<p> The required syntax for a <font SIZE="-1">TCP</font> url is: </p>
<pre>
        tcp://&lt;hostname&gt;:&lt;port&gt;[?&lt;options&gt;]
</pre>
<p> <i>options</i> contains a list of &amp;-separated options of the form <i>key</i>=<i>val</i>. </p>
<p> The list of supported options follows.</p>
<dl>
<dt><code>listen=</code><i>2|1|0</i></p>
<dd> Listen for an incoming connection. 0 disables listen, 1 enables listen in single client mode, 2 enables listen in multi-client mode. Default value is 0.</p>
<dt><code>timeout=</code><i>microseconds</i></p>
<dd> Set raise error timeout, expressed in microseconds. </p>
<p> This option is only relevant in read mode: if no data arrived in more than this time interval, raise error.</p>
<dt><code>listen_timeout=</code><i>milliseconds</i></p>
<dd> Set listen timeout, expressed in milliseconds.</p>
<dt><code>recv_buffer_size=</code><i>bytes</i></p>
<dd> Set receive buffer size, expressed bytes.</p>
<dt><code>send_buffer_size=</code><i>bytes</i></p>
<dd> Set send buffer size, expressed bytes.</p>
<dt><code>tcp_nodelay=</code><i>1|0</i></p>
<dd> Set <font SIZE="-1">TCP_NODELAY</font> to disable Nagle&#8217;s algorithm. Default value is 0.</p>
<dt><code>tcp_mss=</code><i>bytes</i></p>
<dd> Set maximum segment size for outgoing <font SIZE="-1">TCP</font> packets, expressed in bytes.</dl>
<p> The following example shows how to setup a listening <font SIZE="-1">TCP</font> connection with <code>ffmpeg</code>, which is then accessed with <code>ffplay</code>: </p>
<pre>
        ffmpeg -i &lt;input&gt; -f &lt;format&gt; tcp://&lt;hostname&gt;:&lt;port&gt;?listen
        ffplay tcp://&lt;hostname&gt;:&lt;port&gt;
</pre>
<h3>tls</h3>
<p> Transport Layer Security (<font SIZE="-1">TLS</font>) / Secure Sockets Layer (<font SIZE="-1">SSL</font>) </p>
<p> The required syntax for a <font SIZE="-1">TLS/SSL</font> url is: </p>
<pre>
        tls://&lt;hostname&gt;:&lt;port&gt;[?&lt;options&gt;]
</pre>
<p> The following parameters can be set via command line options (or in code via <tt>&quot;AVOption&quot;</tt>s):</p>
<dl>
<dt><code>ca_file, cafile=</code><i>filename</i></p>
<dd> A file containing certificate authority (<font SIZE="-1">CA</font>) root certificates to treat as trusted. If the linked <font SIZE="-1">TLS</font> library contains a default this might not need to be specified for verification to work, but not all libraries and setups have defaults built in. The file must be in OpenSSL <font SIZE="-1">PEM</font> format.</p>
<dt><code>tls_verify=</code><i>1|0</i></p>
<dd> If enabled, try to verify the peer that we are communicating with. Note, if using OpenSSL, this currently only makes sure that the peer certificate is signed by one of the root certificates in the <font SIZE="-1">CA</font> database, but it does not validate that the certificate actually matches the host name we are trying to connect to. (With other backends, the host name is validated as well.) </p>
<p> This is disabled by default since it requires a <font SIZE="-1">CA</font> database to be provided by the caller in many cases.</p>
<dt><code>cert_file, cert=</code><i>filename</i></p>
<dd> A file containing a certificate to use in the handshake with the peer. (When operating as server, in listen mode, this is more often required by the peer, while client certificates only are mandated in certain setups.)</p>
<dt><code>key_file, key=</code><i>filename</i></p>
<dd> A file containing the private key for the certificate.</p>
<dt><code>listen=</code><i>1|0</i></p>
<dd> If enabled, listen for connections on the provided port, and assume the server role in the handshake instead of the client role.</p>
<dt><code>http_proxy</code></p>
<dd> The <font SIZE="-1">HTTP</font> proxy to tunnel through, e.g. <tt>&quot;<a rel="nofollow" href="http://example.com:1234">http://example.com:1234</a>&quot;</tt>. The proxy must support the <font SIZE="-1">CONNECT</font> method.</dl>
<p> Example command lines: </p>
<p> To create a <font SIZE="-1">TLS/SSL</font> server that serves an input stream. </p>
<pre>
        ffmpeg -i &lt;input&gt; -f &lt;format&gt; tls://&lt;hostname&gt;:&lt;port&gt;?listen&amp;cert=&lt;server.crt&gt;&amp;key=&lt;server.key&gt;
</pre>
<p> To play back a stream from the <font SIZE="-1">TLS/SSL</font> server using <code>ffplay</code>: </p>
<pre>
        ffplay tls://&lt;hostname&gt;:&lt;port&gt;
</pre>
<h3>udp</h3>
<p> User Datagram Protocol. </p>
<p> The required syntax for an <font SIZE="-1">UDP URL</font> is: </p>
<pre>
        udp://&lt;hostname&gt;:&lt;port&gt;[?&lt;options&gt;]
</pre>
<p> <i>options</i> contains a list of &amp;-separated options of the form <i>key</i>=<i>val</i>. </p>
<p> In case threading is enabled on the system, a circular buffer is used to store the incoming data, which allows one to reduce loss of data due to <font SIZE="-1">UDP</font> socket buffer overruns. The <i>fifo_size</i> and <i>overrun_nonfatal</i> options are related to this buffer. </p>
<p> The list of supported options follows.</p>
<dl>
<dt><code>buffer_size=</code><i>size</i></p>
<dd> Set the <font SIZE="-1">UDP</font> maximum socket buffer size in bytes. This is used to set either the receive or send buffer size, depending on what the socket is used for. Default is 32 <font SIZE="-1">KB</font> for output, 384 <font SIZE="-1">KB</font> for input. See also <i>fifo_size</i>.</p>
<dt><code>bitrate=</code><i>bitrate</i></p>
<dd> If set to nonzero, the output will have the specified constant bitrate if the input has enough packets to sustain it.</p>
<dt><code>burst_bits=</code><i>bits</i></p>
<dd> When using <i>bitrate</i> this specifies the maximum number of bits in packet bursts.</p>
<dt><code>localport=</code><i>port</i></p>
<dd> Override the local <font SIZE="-1">UDP</font> port to bind with.</p>
<dt><code>localaddr=</code><i>addr</i></p>
<dd> Local <font SIZE="-1">IP</font> address of a network interface used for sending packets or joining multicast groups.</p>
<dt><code>pkt_size=</code><i>size</i></p>
<dd> Set the size in bytes of <font SIZE="-1">UDP</font> packets.</p>
<dt><code>reuse=</code><i>1|0</i></p>
<dd> Explicitly allow or disallow reusing <font SIZE="-1">UDP</font> sockets.</p>
<dt><code>ttl=</code><i>ttl</i></p>
<dd> Set the time to live value (for multicast only).</p>
<dt><code>connect=</code><i>1|0</i></p>
<dd> Initialize the <font SIZE="-1">UDP</font> socket with <tt>&quot;connect()&quot;</tt>. In this case, the destination address can&#8217;t be changed with ff_udp_set_remote_url later. If the destination address isn&#8217;t known at the start, this option can be specified in ff_udp_set_remote_url, too. This allows finding out the source address for the packets with getsockname, and makes writes return with <font SIZE="-1">AVERROR</font>(<font SIZE="-1">ECONNREFUSED</font>) if &#8220;destination unreachable&#8221; is received. For receiving, this gives the benefit of only receiving packets from the specified peer address/port.</p>
<dt><code>sources=</code><i>address</i><code>[,</code><i>address</i><code>]</code></p>
<dd> Only receive packets sent from the specified addresses. In case of multicast, also subscribe to multicast traffic coming from these addresses only.</p>
<dt><code>block=</code><i>address</i><code>[,</code><i>address</i><code>]</code></p>
<dd> Ignore packets sent from the specified addresses. In case of multicast, also exclude the source addresses in the multicast subscription.</p>
<dt><code>fifo_size=</code><i>units</i></p>
<dd> Set the <font SIZE="-1">UDP</font> receiving circular buffer size, expressed as a number of packets with size of 188 bytes. If not specified defaults to 7*4096.</p>
<dt><code>overrun_nonfatal=</code><i>1|0</i></p>
<dd> Survive in case of <font SIZE="-1">UDP</font> receiving circular buffer overrun. Default value is 0.</p>
<dt><code>timeout=</code><i>microseconds</i></p>
<dd> Set raise error timeout, expressed in microseconds. </p>
<p> This option is only relevant in read mode: if no data arrived in more than this time interval, raise error.</p>
<dt><code>broadcast=</code><i>1|0</i></p>
<dd> Explicitly allow or disallow <font SIZE="-1">UDP</font> broadcasting. </p>
<p> Note that broadcasting may not work properly on networks having a broadcast storm protection.</dl>
<p> <i>Examples</i></p>
<dl>
<dt>&bull;</p>
<dd> Use <code>ffmpeg</code> to stream over <font SIZE="-1">UDP</font> to a remote endpoint: </p>
<pre>
        ffmpeg -i &lt;input&gt; -f &lt;format&gt; udp://&lt;hostname&gt;:&lt;port&gt;
</pre>
<dt>&bull;</p>
<dd> Use <code>ffmpeg</code> to stream in mpegts format over <font SIZE="-1">UDP</font> using 188 sized <font SIZE="-1">UDP</font> packets, using a large input buffer: </p>
<pre>
        ffmpeg -i &lt;input&gt; -f mpegts udp://&lt;hostname&gt;:&lt;port&gt;?pkt_size=188&amp;buffer_size=65535
</pre>
<dt>&bull;</p>
<dd> Use <code>ffmpeg</code> to receive over <font SIZE="-1">UDP</font> from a remote endpoint: </p>
<pre>
        ffmpeg -i <a href="udp://[">udp://[</a>&lt;multicast-address&gt;]:&lt;port&gt; ...
</pre>
</dl>
<h3>unix</h3>
<p> Unix local socket </p>
<p> The required syntax for a Unix socket <font SIZE="-1">URL</font> is: </p>
<pre>
        unix://&lt;filepath&gt;
</pre>
<p> The following parameters can be set via command line options (or in code via <tt>&quot;AVOption&quot;</tt>s):</p>
<dl>
<dt><code>timeout</code></p>
<dd> Timeout in ms.</p>
<dt><code>listen</code></p>
<dd> Create the Unix socket in listening mode.</dl>
<h3>zmq</h3>
<p> ZeroMQ asynchronous messaging using the libzmq library. </p>
<p> This library supports unicast streaming to multiple clients without relying on an external server. </p>
<p> The required syntax for streaming or connecting to a stream is: </p>
<pre>
        zmq:<a href="tcp://ip-address:port">tcp://ip-address:port</a>
</pre>
<p> Example: Create a localhost stream on port 5555: </p>
<pre>
        ffmpeg -re -i input -f mpegts zmq:<a href="tcp://127.0.0.1:5555">tcp://127.0.0.1:5555</a>
</pre>
<p> Multiple clients may connect to the stream using: </p>
<pre>
        ffplay zmq:<a href="tcp://127.0.0.1:5555">tcp://127.0.0.1:5555</a>
</pre>
<p> Streaming to multiple clients is implemented using a ZeroMQ Pub-Sub pattern. The server side binds to a port and publishes data. Clients connect to the server (via <font SIZE="-1">IP</font> address/port) and subscribe to the stream. The order in which the server and client start generally does not matter. </p>
<p> ffmpeg must be compiled with the &#8211;enable-libzmq option to support this protocol. </p>
<p> Options can be set on the <code>ffmpeg</code>/<code>ffplay</code> command line. The following options are supported:</p>
<dl>
<dt><code>pkt_size</code></p>
<dd> Forces the maximum packet size for sending/receiving data. The default value is 131,072 bytes. On the server side, this sets the maximum size of sent packets via ZeroMQ. On the clients, it sets an internal buffer size for receiving packets. Note that pkt_size on the clients should be equal to or greater than pkt_size on the server. Otherwise the received message may be truncated causing decoding errors.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ffmpeg/">ffmpeg</a></code>(1), <code><a href="/docs/linux/man/1-ffplay/">ffplay</a></code>(1), <code><a href="/docs/linux/man/1-ffprobe/">ffprobe</a></code>(1), <code><a href="/docs/linux/man/3-libavformat/">libavformat</a></code>(3)</p>
<h2>AUTHORS</h2>
<p> The FFmpeg developers. </p>
<p> For details about the authorship, see the Git history of the project (<a href="git://source.ffmpeg.org/ffmpeg">git://source.ffmpeg.org/ffmpeg</a>), e.g. by typing the command <code>git log</code> in the FFmpeg source directory, or browsing the online repository at &lt;<code><a rel="nofollow" href="http://source.ffmpeg.org">http://source.ffmpeg.org</a></code>&gt;. </p>
<p> Maintainers for the specific components are listed in the file <i></i><font SIZE="-1"><i>MAINTAINERS</i></font><i></i> in the source code tree. </p>
<h2>Index</h2>
