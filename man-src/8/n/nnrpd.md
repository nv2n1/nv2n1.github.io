---
title: "nnrpd(8)"
name: "nnrpd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nnrpd/"
description: "nnrpd – NNTP server for reader clients"
---

<p>nnrpd &#8211; NNTP server for reader clients</p>
<h2>Synopsis</h2>
<p><code>nnrpd</code> [<code>-DfnoSt</code>] [<code>-4</code> <i>address</i>] [<code>-6</code> <i>address</i>] [<code>-b</code> <i>address</i>] [<code>-c</code> <i>configfile</i>] [<code>-i</code> <i>initial</i>] [<code>-I</code> <i>instance</i>] [<code>-p</code> <i>port</i>] [<code>-P</code> <i>prefork</i>] [<code>-r</code> <i>reason</i>] [<code>-s</code> <i>padding</i>]</p>
<h2>Description</h2>
<p><code>nnrpd</code> is an <font SIZE="-1">NNTP</font> server for newsreaders. It accepts commands on its standard input and responds on its standard output. It is normally invoked by <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8) with those descriptors attached to a remote client connection. <code>nnrpd</code> also supports running as a standalone daemon. </p>
<p> Unlike <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <code>nnrpd</code> supports all <font SIZE="-1">NNTP</font> commands for user-oriented reading and posting. <code>nnrpd</code> uses the <i>readers.conf</i> file to control who is authorized to access the Usenet database. </p>
<p> On exit, <code>nnrpd</code> will report usage statistics through <i><a href="/docs/linux/man/3-syslog/">syslog</a></i>(3). </p>
<p> <code>nnrpd</code> only reads config files (both <i>readers.conf</i> and <i>inn.conf</i>) when it is spawned. You can therefore never change the behavior of a client that&#8217;s already connected. If <code>nnrpd</code> is run from <code>innd</code> (the default) or from <i><a href="/docs/linux/man/8-inetd/">inetd</a></i>(8), <i><a href="/docs/linux/man/8-xinetd/">xinetd</a></i>(8), or some equivalent, a new <code>nnrpd</code> process is spawned for every connection and therefore any changes to configuration files will be immediately effective for all new connections. If you are instead running <code>nnrpd</code> with the <code>-D</code> option, any configuration changes won&#8217;t take effect until <code>nnrpd</code> is restarted. </p>
<p> The <i>inn.conf</i> setting <i>nnrpdflags</i> can be used to pass any of the options below to instances of <code>nnrpd</code> that are spawned directly from <code>innd</code>. Many options only make sense when <code>-D</code> is used, so these options should not be used with <i>nnrpdflags</i>. See also the discussion of <i>nnrpdflags</i> in <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5). </p>
<p> When <i>nnrpdloadlimit</i> in <i>inn.conf</i> is not <tt>0</tt>, it will also reject connections if the load average is greater than that value (typically <tt>16</tt>). <code>nnrpd</code> can also prevent high-volume posters from abusing your resources. See the discussion of exponential backoff in <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5).</p>
<h2>Options</h2>
<dl>
<dt><code>-4</code> <i>address</i></p>
<dd>The <code>-4</code> parameter instructs <code>nnrpd</code> to bind to the specified IPv4 address when started as a standalone daemon using the <code>-D</code> flag. This has to be a valid IPv4 address belonging to an interface of the local host. It can also be <tt>0.0.0.0</tt>, saying to bind to all addresses (this is the default).</p>
<dt><code>-6</code> <i>address</i></p>
<dd>The <code>-6</code> parameter instructs <code>nnrpd</code> to bind to the specified IPv6 address when started as a standalone daemon using the <code>-D</code> flag. This has to be a valid IPv6 address belonging to an interface of the local host. It can also be <tt>&quot;::0&quot;</tt>, saying to bind to all IPv6 addresses. </p>
<p> By default, <code>nnrpd</code> in daemon mode listens to both IPv4 and IPv6 addresses. With this option, it will listen only to the specified IPv6 addresses. On some systems however, a value of <tt>&quot;::0&quot;</tt> will cause it to listen to all IPv4 addresses as well.</p>
<dt><code>-b</code> <i>address</i></p>
<dd>Similar to the <code>-4</code> flag. <code>-b</code> is kept for backwards compatibility.</p>
<dt><code>-c</code> <i>configfile</i></p>
<dd>By default, <code>nnrpd</code> reads the <i>readers.conf</i> to determine how to authenticate connections. The <code>-c</code> flag specifies an alternate file for this purpose. If the file name isn&#8217;t fully qualified, it is taken to be relative to <i>pathetc</i> in <i>inn.conf</i>. (This is useful to have several instances of <code>nnrpd</code> running on different ports or <font SIZE="-1">IP</font> addresses with different settings.)</p>
<dt><code>-D</code></p>
<dd>If specified, this parameter causes <code>nnrpd</code> to operate as a daemon. That is, it detaches itself and runs in the background, forking a process for every connection. By default, <code>nnrpd</code> listens on the <font SIZE="-1">NNTP</font> port (119), so either <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8) has to be started on another port or the <code>-p</code> parameter used. Note that with this parameter, <code>nnrpd</code> continues running until killed. This means that it reads <i>inn.conf</i> once on startup and never again until restarted. <code>nnrpd</code> should therefore be restarted if <i>inn.conf</i> is changed. </p>
<p> When started in daemon mode, <code>nnrpd</code> will write its <font SIZE="-1">PID</font> into a file in the <i>pathrun</i> directory. The file will be named <i>nnrpd.pid</i> if <code>nnrpd</code> listens on port 119 (default), or <i>nnrpd-%d.pid</i>, where <tt>%d</tt> is replaced with the port that <code>nnrpd</code> is configured to listen on (<code>-p</code> option is given and its argument is not <tt>119</tt>).</p>
<dt><code>-f</code></p>
<dd>If specified, <code>nnrpd</code> does not detach itself and runs in the foreground when started as a standalone daemon using the <code>-D</code> flag.</p>
<dt><code>-i</code> <i>initial</i></p>
<dd>Specify an initial command to <code>nnrpd</code>. When used, <i>initial</i> is taken as if it were the first command received by <code>nnrpd</code>. After having responded, <code>nnrpd</code> will close the connection.</p>
<dt><code>-I</code> <i>instance</i></p>
<dd>If specified, <i>instance</i> is used as an additional static portion within message-IDs generated by <code>nnrpd</code>; typically this option would be used where a cluster of machines exist with the same virtual hostname and must be disambiguated during posts.</p>
<dt><code>-n</code></p>
<dd>The <code>-n</code> flag turns off resolution of <font SIZE="-1">IP</font> addresses to names. If you only use IP-based restrictions in <i>readers.conf</i> and can handle <font SIZE="-1">IP</font> addresses in your logs, using this flag may result in some additional speed.</p>
<dt><code>-o</code></p>
<dd>The <code>-o</code> flag causes all articles to be spooled instead of sending them to <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8). <code>rnews</code> with the <code>-U</code> flag should be invoked from cron on a regular basis to take care of these articles. This flag is useful if <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8) is accepting articles and <code>nnrpd</code> is started standalone or using <i><a href="/docs/linux/man/8-inetd/">inetd</a></i>(8).</p>
<dt><code>-p</code> <i>port</i></p>
<dd>The <code>-p</code> parameter instructs <code>nnrpd</code> to listen on <i>port</i> when started as a standalone daemon using the <code>-D</code> flag.</p>
<dt><code>-P</code> <i>prefork</i></p>
<dd>The <code>-P</code> parameter instructs <code>nnrpd</code> to prefork <i>prefork</i> children awaiting connections when started as a standalone daemon using the <code>-D</code> flag.</p>
<dt><code>-r</code> <i>reason</i></p>
<dd>If the <code>-r</code> flag is used, then <code>nnrpd</code> will reject the incoming connection giving <i>reason</i> as the text. This flag is used by <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8) when it is paused or throttled. <i>reason</i> should be encoded in <font SIZE="-1">UTF-8</font>.</p>
<dt><code>-s</code> <i>padding</i></p>
<dd>As each command is received, <code>nnrpd</code> tries to change its <tt>&quot;argv&quot;</tt> array so that <i><a href="/docs/linux/man/1-ps/">ps</a></i>(1) will print out the command being executed. To get a full display, the <code>-s</code> flag may be used with a long string as its argument, which will be overwritten when the program changes its title.</p>
<dt><code>-S</code></p>
<dd>If specified, <code>nnrpd</code> will start a negotiation for a <font SIZE="-1">TLS</font> session as soon as connected. To use this flag, <code>&#8211;with-openssl</code> must have been specified at configure time. For more information on running <code>nnrpd</code> with <font SIZE="-1">TLS</font> support, see &#8220;<font SIZE="-1">TLS</font> <font SIZE="-1">SUPPORT</font>&#8221;.</p>
<dt><code>-t</code></p>
<dd>If the <code>-t</code> flag is used, then all client commands and initial responses will be traced by reporting them in syslog. This flag is set by <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8) under the control of the <i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8) <tt>&quot;trace&quot;</tt> command, and is toggled upon receipt of a <font SIZE="-1">SIGHUP</font>; see <i><a href="/docs/linux/man/2-signal/">signal</a></i>(2).</dl>
<h2>Tls Support</h2>
<p>If <font SIZE="-1">INN</font> is built with <code>&#8211;with-openssl</code>, <code>nnrpd</code> will support news reading over <font SIZE="-1">TLS</font> (also known as <font SIZE="-1">SSL</font>). For clients that use the <font SIZE="-1">STARTTLS</font> command, no special configuration is needed beyond creating a <font SIZE="-1">TLS/SSL</font> certificate for the server. You should do this in exactly the same way that you would generate a certificate for a web server. </p>
<p> If you&#8217;re happy with a self-signed certificate (which will generate warnings with some news reader clients), you can create and install one in the default path by running <tt>&quot;make cert&quot;</tt> after <tt>&quot;make install&quot;</tt> when installing <font SIZE="-1">INN</font>, or by running the following commands: </p>
<pre> umask 077
 openssl req -new -x509 -nodes -out &lt;pathetc&gt;/cert.pem \
 -days 366 -keyout &lt;pathetc&gt;/key.pem
 chown news:news &lt;pathetc&gt;/cert.pem
 chmod 640 &lt;pathetc&gt;/cert.pem
 chown news:news &lt;pathetc&gt;/key.pem
 chmod 600 &lt;pathetc&gt;/key.pem</pre>
<p>Replace the paths with something appropriate to your <font SIZE="-1">INN</font> installation. This will create a self-signed certificate that will expire in a year. The <code>openssl</code> program will ask you a variety of questions about your organization. Enter the fully qualified domain name of the server as the name the certificate is for. </p>
<p> You then have to set these <i>inn.conf</i> parameters with the right paths: </p>
<pre> tlscapath: &lt;pathetc&gt;
 tlscertfile: &lt;pathetc&gt;/cert.pem
 tlskeyfile: &lt;pathetc&gt;/key.pem</pre>
<p>In case you have a certificate authority root certificate, you can also set <i>tlscafile</i> to its path. </p>
<p> Most news clients currently do not use the <font SIZE="-1">STARTTLS</font> command, however, and instead expect to connect to a separate port (563) and start a <font SIZE="-1">TLS</font> negotiation immediately. <code>innd</code> does not, however, know how to listen for connections to that port and then spawn <code>nnrpd</code> the way that it does for regular reader connections. You will therefore need to arrange for <code>nnrpd</code> to listen on that port through some other means. This can be done with the <code>-D</code> flag along with <tt>&quot;-p 563&quot;</tt> and put into your init scripts: </p>
<pre> su news -s /bin/sh -c '&lt;pathbin&gt;/nnrpd -D -p 563 -S'</pre>
<p>but the easiest way is probably to add a line like: </p>
<pre> nntps stream tcp nowait news &lt;pathbin&gt;/nnrpd nnrpd -S</pre>
<p>to <i>/etc/inetd.conf</i> or the equivalent on your system and let <code>inetd</code> run <code>nnrpd</code>. (Change the path to <code>nnrpd</code> to match your installation.) You may need to replace <tt>&quot;nntps&quot;</tt> with <tt>563</tt> if <tt>&quot;nntps&quot;</tt> isn&#8217;t defined in <i>/etc/services</i> on your system. </p>
<p> Optionally, you may set the <i>tlsciphers</i>, <i>tlscompression</i>, <i>tlseccurve</i>, <i>tlspreferserverciphers</i>, and <i>tlsprotocols</i> parameters in <i>inn.conf</i> to fine-tune the behaviour of the <font SIZE="-1">SSL/TLS</font> negotiation whenever a new attack on the <font SIZE="-1">TLS</font> protocol or some supported cipher suite is discovered.</p>
<h2>Protocol Differences</h2>
<p><code>nnrpd</code> implements the <font SIZE="-1">NNTP</font> commands defined in <font SIZE="-1">RFC</font>&nbsp;<wbr>3977 (<font SIZE="-1">NNTP</font>), <font SIZE="-1">RFC</font>&nbsp;<wbr>4642 (<font SIZE="-1">TLS/NNTP</font>), <font SIZE="-1">RFC</font>&nbsp;<wbr>4643 (<font SIZE="-1">NNTP</font> authentication) and <font SIZE="-1">RFC</font>&nbsp;<wbr>6048 (<font SIZE="-1">NNTP</font> <font SIZE="-1">LIST</font> additions) with the following differences:</p>
<dl>
<dt>1.</p>
<dd>The <font SIZE="-1">XGTITLE</font> [<i>wildmat</i>] command is provided. This extension is used by ANU-News and documented in <font SIZE="-1">RFC</font>&nbsp;<wbr>2980. It returns a <tt>282</tt> reply code, followed by a one-line description of all newsgroups that match the pattern. The default is the current group. </p>
<p> Note that <font SIZE="-1">LIST</font> <font SIZE="-1">NEWSGROUPS</font> should be used instead of <font SIZE="-1">XGTITLE</font>.</p>
<dt>2.</p>
<dd>The <font SIZE="-1">XHDR</font> <i>header</i> [<i>message-ID</i>|<i>range</i>] command is implemented. It returns a <tt>221</tt> reply code, followed by specific headers for the specified range; the default is to return the data for the current article. See <font SIZE="-1">RFC</font>&nbsp;<wbr>2980. </p>
<p> Note that <font SIZE="-1">HDR</font> should be used instead of <font SIZE="-1">XHDR</font>.</p>
<dt>3.</p>
<dd>The <font SIZE="-1">XOVER</font> [<i>range</i>] command is provided. It returns a <tt>224</tt> reply code, followed by the overview data for the specified range; the default is to return the data for the current article. See <font SIZE="-1">RFC</font>&nbsp;<wbr>2980. </p>
<p> Note that <font SIZE="-1">OVER</font> should be used instead of <font SIZE="-1">XOVER</font>.</p>
<dt>4.</p>
<dd>A new command, <font SIZE="-1">XPAT</font> <i>header</i> <i>message-ID</i>|<i>range</i> <i>pattern</i> [<i>pattern</i> &#8230;], is provided. The first argument is the case-insensitive name of the header to be searched. The second argument is either an article range or a single message-ID, as specified in <font SIZE="-1">RFC</font>&nbsp;<wbr>2980. The third argument is a <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3)-style pattern; if there are additional arguments, they are joined together separated by a single space to form the complete pattern. This command is similar to the <font SIZE="-1">XHDR</font> command. It returns a <tt>221</tt> response code, followed by the text response of all article numbers that match the pattern.</p>
<dt>5.</p>
<dd>A newsgroup name is case-sensitive for <code>nnrpd</code>.</p>
<dt>6.</p>
<dd>If <font SIZE="-1">IHAVE</font> has been advertised, it will not necessarily be advertised for the entire session (contrary to section 3.4.1 of <font SIZE="-1">RFC</font>&nbsp;<wbr>3977). <code>nnrpd</code> only advertises the <font SIZE="-1">IHAVE</font> capability when it is really available.</p>
<dt>7.</p>
<dd><code>nnrpd</code> allows a wider syntax for wildmats and ranges (especially <tt>&quot;-&quot;</tt> and <tt>&quot;-</tt>article-number<tt>&quot;</tt>).</dl>
<h2>History</h2>
<p>Written by Rich <tt>$alz</tt> &lt;rsalz [at] uunet.uu.net&gt; for InterNetNews. Overview support added by Rob Robertston &lt;rob [at] violet.berkeley.edu&gt; and Rich in January, 1993. Exponential backoff (for posting) added by Dave Hayes in Febuary 1998. </p>
<p> <tt>$Id:</tt> nnrpd.pod 9753 2014-12-01 20:26:38Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ctlinnd/">ctlinnd</a></i>(8), <i><a href="/docs/linux/man/8-innd/">innd</a></i>(8), <i><a href="/docs/linux/man/5-inn-conf/">inn.conf</a></i>(5), <i><a href="/docs/linux/man/5-readers-conf/">readers.conf</a></i>(5), <i><a href="/docs/linux/man/2-signal/">signal</a></i>(2), <i><a href="/docs/linux/man/3-uwildmat/">uwildmat</a></i>(3). </p>
