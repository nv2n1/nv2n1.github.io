---
title: "dnscrypt-proxy(8)"
name: "dnscrypt-proxy"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnscrypt-proxy/"
description: "dnscrypt-proxy – A DNSCrypt forwarder"
---

<p><code>dnscrypt-proxy</code> &#8211; A DNSCrypt forwarder</p>
<h2>Synopsis</h2>
<p><code>dnscrypt-proxy</code> [<i>options</i>]</p>
<h2>Description</h2>
<p><code>dnscrypt-proxy</code> accepts DNS requests, authenticates and encrypts them using dnscrypt and forwards them to a remote dnscrypt-enabled resolver. </p>
<p> Replies from the resolver are expected to be authenticated or else they will be discarded. </p>
<p> The proxy verifies the replies, decrypts them, and transparently forwards them to the local stub resolver. </p>
<p> <code>dnscrypt-proxy</code> listens to <code>127.0.0.1</code> / port <code>53</code> by default.</p>
<h2>Warning</h2>
<p><code>dnscrypt-proxy</code> is not a DNS cache. Unless your operating system already provides a decent built-in cache (and by default, most systems don&#8217;t), clients shouldn&#8217;t directly send requests to <code>dnscrypt-proxy</code>. </p>
<p> Intead, run a DNS cache like <code>Unbound</code>, and configure it to use <code>dnscrypt-proxy</code> as a forwarder. Both can safely run on the same machine as long as they use different IP addresses and/or different ports.</p>
<h2>Options</h2>
<dl>
<dt>&bull;</p>
<dd><code>-a</code>, <code>&#8211;local-address=&lt;ip&gt;[:port]</code>: what local IP the daemon will listen to, with an optional port. The default port is 53.</p>
<dt>&bull;</p>
<dd><code>-d</code>, <code>&#8211;daemonize</code>: detach from the current terminal and run the server in background.</p>
<dt>&bull;</p>
<dd><code>-E</code>, <code>&#8211;ephemeral-keys</code>: By default, queries are always sent with the same public key, allowing providers to link this public key to the different IP addresses you are using. This option requires extra CPU cycles, but mitigates this by computing an ephemeral key pair for every query.</p>
<dt>&bull;</p>
<dd><code>-e</code>, <code>&#8211;edns-payload-size=&lt;bytes&gt;</code>: transparently add an OPT pseudo-RR to outgoing queries in order to enable the EDNS0 extension mechanism. The payload size is the size of the largest response we accept from the resolver before retrying over TCP. This feature is enabled by default, with a payload size of 1252 bytes. Any value below 512 disables it.</p>
<dt>&bull;</p>
<dd><code>-h</code>, <code>&#8211;help</code>: show usage.</p>
<dt>&bull;</p>
<dd><code>-k</code>, <code>&#8211;provider-key=&lt;key&gt;</code>: specify the provider public key (see below).</p>
<dt>&bull;</p>
<dd><code>-K</code>, <code>&#8211;client-key=&lt;file&gt;</code>: use a static client secret key stored in <code>&lt;file&gt;</code>.</p>
<dt>&bull;</p>
<dd><code>-L</code>, <code>&#8211;resolvers-list=&lt;file&gt;</code>: path to the CSV file containing the list of available resolvers, and the parameters to use them.</p>
<dt>&bull;</p>
<dd><code>-l</code>, <code>&#8211;logfile=&lt;file&gt;</code>: log events to this file instead of the standard output.</p>
<dt>&bull;</p>
<dd><code>-m</code>, <code>&#8211;loglevel=&lt;level&gt;</code>: don&#8217;t log events with priority above this level after the service has been started up. Default is <code>6</code>, the value for <code>LOG_INFO</code>. Valid values are <code>0</code> (system is unusable), <code>1</code> (action must be taken immediately), <code>2</code> (critical conditions), <code>3</code> (error conditions), <code>4</code> (warning conditions), <code>5</code> (normal but significant condition), <code>6</code> (informational) and <code>7</code> (debug-level messages).</p>
<dt>&bull;</p>
<dd><code>-n</code>, <code>&#8211;max-active-requests=&lt;count&gt;</code>: set the maximum number of simultaneous active requests. The default value is 250.</p>
<dt>&bull;</p>
<dd><code>-p</code>, <code>&#8211;pidfile=&lt;file&gt;</code>: write the PID number to a file.</p>
<dt>&bull;</p>
<dd><code>-R</code>, <code>&#8211;resolver-name=&lt;name&gt;</code>: name of the resolver to use, from the list of available resolvers (see <code>-L</code>).</p>
<dt>&bull;</p>
<dd><code>-r</code>, <code>&#8211;resolver-address=&lt;ip&gt;[:port]</code>: a DNSCrypt-capable resolver IP address with an optional port. The default port is 443.</p>
<dt>&bull;</p>
<dd>-S, &#8211;syslog: if a log file hasn&#8217;t been set, log diagnostic messages to syslog instead of printing them. &#8211;daemonize implies &#8211;syslog.</p>
<dt>&bull;</p>
<dd><code>-t</code>, <code>&#8211;test=&lt;margin&gt;</code>: don&#8217;t actually start the proxy, but check that a valid certificate can be retrieved from the server and that it will remain valid for the next <i>margin</i> minutes. The exit code is 0 if a valid certificate can be used, 2 if no valid certificates can be used, 3 if a timeout occurred, and 4 if a currently valid certificate is going to expire before <i>margin</i>. The margin is always specificied in minutes.</p>
<dt>&bull;</p>
<dd><code>-u</code>, <code>&#8211;user=&lt;user name&gt;</code>: <a href="/docs/linux/man/2-chroot/">chroot</a>(2) to this user&#8217;s home directory and drop privileges.</p>
<dt>&bull;</p>
<dd><code>-N</code>, <code>&#8211;provider-name=&lt;FQDN&gt;</code>: the fully-qualified name of the dnscrypt certificate provider.</p>
<dt>&bull;</p>
<dd><code>-T</code>, <code>&#8211;tcp-only</code>: always use TCP. A connection made using UDP will get a truncated response, so that the (stub) resolver retries using TCP.</p>
<dt>&bull;</p>
<dd><code>-V</code>, <code>&#8211;version</code>: show version number.</p>
<dd></dl>
<p> A public key is 256-bit long, and it has to be specified as a hexadecimal string, with optional columns.</p>
<h2>Common Usage Example</h2>
<pre>$ dnscrypt-proxy --daemonize --resolver-name=...</pre>
<p>The resolver name is the first column (Name) in the CSV file.</p>
<h2>Usage Example With A Private Server</h2>
<pre>$ dnscrypt-proxy --daemonize --provider-key=... --provider-name=... --resolver-address=...</pre>
<h2>Bugs And Support</h2>
<p>Please report issues with DNSCrypt itself to <a rel="nofollow" href="https://dnscrypt.org/issues">https://dnscrypt.org/issues</a></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-hostip/">hostip</a>(8) </p>
