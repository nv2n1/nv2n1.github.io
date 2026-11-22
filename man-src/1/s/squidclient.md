---

title: "squidclient(1)"
name: "squidclient"
section: "1"
letter: "s"
url: "/docs/linux/man/1-squidclient/"
description: "squidclient – A simple HTTP web client tool"
---

<p> squidclient &#8211; A simple HTTP web client tool </p>
<h2>SYNOPSIS</h2>
<p> <code>squidclient</code> <code>[ -aknNrsv ] </code> <code>[ &#8211;ping [ping-options] ] </code> <code>[ &#8211;https] [tls-options] [ -A</code> string <code>] [ -h | &#8211;host</code> remote host <code>] [ -H &#8216;</code> string <code>&#8216; ] [ -i</code> IMS <code>] [ -j &#8216;</code> Host header <code>&#8216; ] [ -l | &#8211;local</code> host <code>] [ -m</code> method <code>] [ -p | &#8211;port</code> port <code>] [ -P</code> file <code>] [ -t</code> count <code>] [ -T</code> timeout <code>] [ -u</code> user <code>] [ -U</code> user <code>] [ -V</code> version <code>] [ -w</code> password <code>] [ -W</code> password <code>] </code> url </p>
<p> <code>Ping options: [ -g</code> count <code>] [ -I</code> interval <code>] </code> </p>
<p> <code>TLS options: [ &#8211;anonymous-tls ] [ &#8211;trusted-ca</code> CA certificates file <code>&#8230;] [ &#8211;cert</code> client X.509 certificate file <code>] [ &#8211;params</code> TLS session parameters <code>] </code></p>
<h2>DESCRIPTION</h2>
<p> <code>squidclient</code> is a tool providing a command line interface for retrieving URLs. Designed for testing any HTTP 0.9, 1.0, or 1.1 web server or proxy. This tool can be combined with scripts to perform any basic HTTP operation. Some additional features for access to the <code>squid</code> proxy object cache and management information are provided.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></dt>
<dd> Do NOT include Accept: header.</dd>
<dt><code>-A &#8216;string&#8217;</code></dt>
<dd> Send <code>string</code> as User-Agent: header. To omit the header completely set string to empty (&#8221;).</dd>
<dt><code>-h | &#8211;host host</code></dt>
<dd> Retrieve URL from server host. Default is <code>localhost</code></dd>
<dt><code>-H &#8216;string&#8217;</code></dt>
<dd> Extra headers to send. Use <code>&#8216;
&#8217;</code> for new lines.</dd>
<dt><code>-i time</code></dt>
<dd> If-Modified-Since time (in Epoch seconds).</dd>
<dt><code>-j hosthdr</code></dt>
<dd> Host header content</dd>
<dt><code>-k</code></dt>
<dd> Keep the connection active. Default is to do only one request then close.</dd>
<dt><code>-l | &#8211;local host</code></dt>
<dd> Specify a local IP address to bind to. Default is none.</dd>
<dt><code>-m method</code></dt>
<dd> Request method, default is <i>GET.</i> Squid also supports a non-standard method called <i>PURGE.</i> You can use that to purge a specific URL from the cache. You need to have <i>purge</i> access setup in <code>squid.conf</code> similar to <i>manager</i> access. Here is an example: </dd>
<pre>
      acl purge method PURGE      http_access deny purge !localhost</pre>
<dt><code>-n</code></dt>
<dd> Proxy Negotiate(Kerberos) authentication. </dd>
<pre><code>
Use kinit username[at] DOMAIN first to get initial TGS.- N
                                                             WWW
                                                             Negotiate(Kerberos) authentication.Use kinit username[at] DOMAIN first to get initial TGS.
</code></pre>
<dt><code>-p port</code></dt>
<dd> Port number of cache. Default is 3128.</dd>
<dt><code>-P file</code></dt>
<dd> Request body. Using the named file as data.</dd>
<dt><code>-r</code></dt>
<dd> Force cache to reload URL.</dd>
<dt><code>-s</code></dt>
<dd> Silent. Do not print data to stdout.</dd>
<dt><code>-t count</code></dt>
<dd> Trace <i>count</i> HTTP relay or proxy hops</dd>
<dt><code>-T timeout</code></dt>
<dd> Timeout value (seconds) for read/write operations.</dd>
<dt><code>-u user</code></dt>
<dd> Proxy authentication username</dd>
<dt><code>-U user</code></dt>
<dd> WWW authentication username</dd>
<dt><code>-v</code></dt>
<dd> Verbose. Print outgoing message to stderr.</dd>
<dt><code>-V version</code></dt>
<dd> HTTP Version. Use &#8216;-&#8216; for HTTP/0.9 omitted case</dd>
<dt><code>-w password</code></dt>
<dd> Proxy authentication password</dd>
<dt><code>-W password</code></dt>
<dd> WWW authentication password</dd>
<dt><code>&#8211;https</code></dt>
<dd> Use Transport Layer Security on the HTTP connection.</dd>
<dt><code>&#8211;anonymous-tls</code></dt>
<dd> Use TLS with unauthenticated (anonymous) certificate.</dd>
<dt><code>&#8211;cert file</code></dt>
<dd> File containing client X.509 certificate in PEM format. May be repeated to load several client certificates.</dd>
<dt><code>&#8211;trusted-ca file</code></dt>
<dd> File containing trusted Certificate Authority (CA) certificates in PEM format. May be repeated to load any number of files.</dd>
<dt><code>&#8211;params values</code></dt>
<dd> TLS library specific parameters for the communication session. See the library documentation for details on valid parameters. <i>GnuTLS: <a rel="nofollow" href="http://gnutls.org/manual/html_node/Priority-Strings.html">http://gnutls.org/manual/html_node/Priority-Strings.html</a></i> If repeated only the last value will have effect.</dd>
<dt><code>&#8211;ping [options]</code></dt>
<dd> Enable ping mode. Optional -g and -I parameters must follow immediately if used. Repeated use resets to default ping settings.</dd>
<dt><code>-g count</code></dt>
<dd> Ping mode, perform<i>count</i> iterations (default is to loop until interrupted).</dd>
<dt><code>-I interval</code></dt>
<dd> Ping interval in seconds (default 1 second).</dd></dl>
<h2>AUTHOR</h2>
<p> This program and manual was written by <i>Amos Jeffries &lt;amosjeffries [at] squid-cache.org&gt;</i> </p>
<p> Based on original code derived from Harvest and further developed by numerous individuals from the internet community.</p>
<h2>COPYRIGHT</h2>
<p>&nbsp;<wbr>*&nbsp;<wbr>Copyright&nbsp;<wbr>(C)&nbsp;<wbr>1996-2016 The Squid Software Foundation and contributors<br/>
&nbsp;<wbr>*<br/>
&nbsp;<wbr>*&nbsp;<wbr>Squid software is distributed under GPLv2+&nbsp;<wbr>license and includes<br/>
&nbsp;<wbr>*&nbsp;<wbr>contributions from numerous individuals and organizations.<br/>
&nbsp;<wbr>*&nbsp;<wbr>Please see the COPYING and CONTRIBUTORS files for details.</p>
<h2>QUESTIONS</h2>
<p> Questions on the usage of this program can be sent to the <i>Squid Users mailing list</i> &lt;squid-users [at] squid-cache.org&gt;</p>
<h2>REPORTING BUGS</h2>
<p> See <a rel="nofollow" href="http://wiki.squid-cache.org/SquidFaq/BugReporting">http://wiki.squid-cache.org/SquidFaq/BugReporting</a> for details of what you need to include with your bug report. </p>
<p> Report bugs or bug fixes using <a rel="nofollow" href="http://bugs.squid-cache.org/">http://bugs.squid-cache.org/</a> </p>
<p> Report serious security bugs to <i>Squid Bugs &lt;squid-bugs [at] squid-cache.org&gt;</i> </p>
<p> Report ideas for new improvements to the <i>Squid Developers mailing list</i> &lt;squid-dev [at] squid-cache.org&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-squid/">squid</a></code>(8), <code><a href="/docs/linux/man/8-cachemgr-cgi/">cachemgr.cgi</a></code>(8) </p>
