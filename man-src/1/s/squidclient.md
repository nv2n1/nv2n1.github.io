---
title: "squidclient(1)"
name: "squidclient"
section: "1"
letter: "s"
url: "/docs/linux/man/1-squidclient/"
description: "squidclient – A simple HTTP web client tool"
---

<h2 class="name">NAME</h2>
<p> squidclient &#8211; A simple HTTP web client tool </p>
<h2>SYNOPSIS</h2>
<p> <code>squidclient</code> <code>[ -aknNrsv ] </code> <code>[ &#8211;ping [ping-options] ] </code> <code>[ &#8211;https] [tls-options] [ -A</code> string <code>] [ -h | &#8211;host</code> remote host <code>] [ -H &#8216;</code> string <code>&#8216; ] [ -i</code> IMS <code>] [ -j &#8216;</code> Host header <code>&#8216; ] [ -l | &#8211;local</code> host <code>] [ -m</code> method <code>] [ -p | &#8211;port</code> port <code>] [ -P</code> file <code>] [ -t</code> count <code>] [ -T</code> timeout <code>] [ -u</code> user <code>] [ -U</code> user <code>] [ -V</code> version <code>] [ -w</code> password <code>] [ -W</code> password <code>] </code> url </p>
<p> <code>Ping options: [ -g</code> count <code>] [ -I</code> interval <code>] </code> </p>
<p> <code>TLS options: [ &#8211;anonymous-tls ] [ &#8211;trusted-ca</code> CA certificates file <code>&#8230;] [ &#8211;cert</code> client X.509 certificate file <code>] [ &#8211;params</code> TLS session parameters <code>] </code></p>
<h2>DESCRIPTION</h2>
<p> <code>squidclient</code> is a tool providing a command line interface for retrieving URLs. Designed for testing any HTTP 0.9, 1.0, or 1.1 web server or proxy. This tool can be combined with scripts to perform any basic HTTP operation. Some additional features for access to the <code>squid</code> proxy object cache and management information are provided.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Do NOT include Accept: header.</p>
<dt><code>-A &#8216;string&#8217;</code></p>
<dd> Send <code>string</code> as User-Agent: header. To omit the header completely set string to empty (&#8221;).</p>
<dt><code>-h | &#8211;host host</code></p>
<dd> Retrieve URL from server host. Default is <code>localhost</code></p>
<dt><code>-H &#8216;string&#8217;</code></p>
<dd> Extra headers to send. Use <code>&#8216;
&#8217;</code> for new lines.</p>
<dt><code>-i time</code></p>
<dd> If-Modified-Since time (in Epoch seconds).</p>
<dt><code>-j hosthdr</code></p>
<dd> Host header content</p>
<dt><code>-k</code></p>
<dd> Keep the connection active. Default is to do only one request then close.</p>
<dt><code>-l | &#8211;local host</code></p>
<dd> Specify a local IP address to bind to. Default is none.</p>
<dt><code>-m method</code></p>
<dd> Request method, default is <i>GET.</i> Squid also supports a non-standard method called <i>PURGE.</i> You can use that to purge a specific URL from the cache. You need to have <i>purge</i> access setup in <code>squid.conf</code> similar to <i>manager</i> access. Here is an example: </p>
<pre>
      acl purge method PURGE      http_access deny purge !localhost</pre>
<dt><code>-n</code></p>
<dd> Proxy Negotiate(Kerberos) authentication. </p>
<pre><code>
Use kinit username[at] DOMAIN first to get initial TGS.- N
                                                             WWW
                                                             Negotiate(Kerberos) authentication.Use kinit username[at] DOMAIN first to get initial TGS.
</code></pre>
<dt><code>-p port</code></p>
<dd> Port number of cache. Default is 3128.</p>
<dt><code>-P file</code></p>
<dd> Request body. Using the named file as data.</p>
<dt><code>-r</code></p>
<dd> Force cache to reload URL.</p>
<dt><code>-s</code></p>
<dd> Silent. Do not print data to stdout.</p>
<dt><code>-t count</code></p>
<dd> Trace <i>count</i> HTTP relay or proxy hops</p>
<dt><code>-T timeout</code></p>
<dd> Timeout value (seconds) for read/write operations.</p>
<dt><code>-u user</code></p>
<dd> Proxy authentication username</p>
<dt><code>-U user</code></p>
<dd> WWW authentication username</p>
<dt><code>-v</code></p>
<dd> Verbose. Print outgoing message to stderr.</p>
<dt><code>-V version</code></p>
<dd> HTTP Version. Use &#8216;-&#8216; for HTTP/0.9 omitted case</p>
<dt><code>-w password</code></p>
<dd> Proxy authentication password</p>
<dt><code>-W password</code></p>
<dd> WWW authentication password</p>
<dt><code>&#8211;https</code></p>
<dd> Use Transport Layer Security on the HTTP connection.</p>
<dt><code>&#8211;anonymous-tls</code></p>
<dd> Use TLS with unauthenticated (anonymous) certificate.</p>
<dt><code>&#8211;cert file</code></p>
<dd> File containing client X.509 certificate in PEM format. May be repeated to load several client certificates.</p>
<dt><code>&#8211;trusted-ca file</code></p>
<dd> File containing trusted Certificate Authority (CA) certificates in PEM format. May be repeated to load any number of files.</p>
<dt><code>&#8211;params values</code></p>
<dd> TLS library specific parameters for the communication session. See the library documentation for details on valid parameters. <i>GnuTLS: <a rel="nofollow" href="http://gnutls.org/manual/html_node/Priority-Strings.html">http://gnutls.org/manual/html_node/Priority-Strings.html</a></i> If repeated only the last value will have effect.</p>
<dt><code>&#8211;ping [options]</code></p>
<dd> Enable ping mode. Optional -g and -I parameters must follow immediately if used. Repeated use resets to default ping settings.</p>
<dt><code>-g count</code></p>
<dd> Ping mode, perform<i>count</i> iterations (default is to loop until interrupted).</p>
<dt><code>-I interval</code></p>
<dd> Ping interval in seconds (default 1 second).</dl>
<h2>AUTHOR</h2>
<p> This program and manual was written by <i>Amos Jeffries &lt;amosjeffries [at] squid-cache.org&gt;</i> </p>
<p> Based on original code derived from Harvest and further developed by numerous individuals from the internet community.</p>
<h2>COPYRIGHT</h2>
<p>&nbsp;<wbr>*&nbsp;<wbr>Copyright&nbsp;<wbr>(C)&nbsp;<wbr>1996-2016 The Squid Software Foundation and contributors<br />
&nbsp;<wbr>*<br />
&nbsp;<wbr>*&nbsp;<wbr>Squid software is distributed under GPLv2+&nbsp;<wbr>license and includes<br />
&nbsp;<wbr>*&nbsp;<wbr>contributions from numerous individuals and organizations.<br />
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
<h2>Index</h2>
