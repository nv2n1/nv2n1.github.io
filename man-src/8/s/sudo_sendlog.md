---
title: "sudo_sendlog(8)"
name: "sudo_sendlog"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sudo_sendlog/"
description: "sudo_sendlog – send sudo I/O log to log server"
---

<p>Sudo 1.9.9</p>
<h2>Name</h2>
<p><code>sudo_sendlog</code> &#8211; send sudo I/O log to log server</p>
<h2>Synopsis</h2>
<p><code>sudo_sendlog</code> [-<code>AnV</code> ] [-<code>b </code><i>ca_bundle</i> ] [-<code>c </code><i>cert_file</i> ] [-<code>h </code><i>host</i> ] [-<code>i </code><i>iolog-id</i> ] [-<code>k </code><i>key_file</i> ] [-<code>p </code><i>port</i> ] [-<code>r </code><i>restart-point</i> ] [-<code>R </code><i>reject-reason</i> ] [-<code>s </code><i>stop-point</i> ] [-<code>t </code><i>number</i> ] <i>path</i></p>
<h2>Description</h2>
<p><code>sudo_sendlog</code> can be used to send the existing <code>sudoers</code> I/O log <i>path</i> to a remote log server such as sudo_logsrvd8 for central storage. </p>
<p> The options are as follows:</p>
<dl>
<dt><code>-A , -accept-only</code></p>
<dd>Only send the accept event, not the I/O associated with the log. This can be used to test the logging of accept events without any associated I/O.</p>
<dt><code>-b , -ca-bundle</code></p>
<dd>The path to a certificate authority bundle file, in PEM format, to use instead of the system&#8217;s default certificate authority database when authenticating the log server. The default is to use the system&#8217;s default certificate authority database.</p>
<dt><code>-c , -cert</code></p>
<dd>The path to the client&#8217;s certificate file in PEM format. This setting is required when the connection to the remote log server is secured with TLS.</p>
<dt><code>&#8211;help</code></p>
<dd>Display a short help message to the standard output and exit.</p>
<dt><code>-h , -host</code></p>
<dd>Connect to the specified <i>host</i> instead of localhost.</p>
<dt><code>-i , -iolog-id</code></p>
<dd>Use the specified <i>iolog-id</i> when restarting a log transfer. The <i>iolog-id</i> is reported by the server when it creates the remote I/O log. This option may only be used in conjunction with the &#8211;<code>r</code> option.</p>
<dt><code>-k , -key</code></p>
<dd>The path to the client&#8217;s private key file in PEM format. This setting is required when the connection to the remote log server is secured with TLS.</p>
<dt><code>-n , -no-verify</code></p>
<dd>If specified, the server&#8217;s certificate will not be verified during the TLS handshake. By default, <code>sudo_sendlog</code> verifies that the server&#8217;s certificate is valid and that it contains either the server&#8217;s host name or its IP address. This setting is only supported when the connection to the remote log server is secured with TLS.</p>
<dt><code>-p , -port</code></p>
<dd>Use the specified network <i>port</i> when connecting to the log server instead of the default, port 30344.</p>
<dt><code>-r , -restart</code></p>
<dd>Restart an interrupted connection to the log server. The specified <i>restart-point</i> is used to tell the server the point in time at which to continue the log. The <i>restart-point</i> is specified in the form &#8220;seconds,nanoseconds&#8221; and is usually the last commit point received from the server. The &#8211;<code>i</code> option must also be specified when restarting a transfer.</p>
<dt><code>-R , -reject</code></p>
<dd>Send a reject event for the command using the specified <i>reject-reason</i> even though it was actually accepted locally. This can be used to test the logging of reject events; no I/O will be sent.</p>
<dt><code>-s , -stop-after</code></p>
<dd>Stop sending log records and close the connection when <i>stop-point</i> is reached. This can be used for testing purposes to send a partial I/O log to the server. Partial logs can be restarted using the &#8211;<code>r</code> option. The <i>stop-point</i> is an elapsed time specified in the form &#8220;seconds,nanoseconds&#8221;</p>
<dt><code>-t , -test</code></p>
<dd>Open <i>number</i> simultaneous connections to the log server and send the specified I/O log file on each one. This option is useful for performance testing.</p>
<dt><code>-V , -version</code></p>
<dd>Print the <code>sudo_sendlog</code> version and exit.</dl>
<h3>Debugging sendlog</h3>
<p><code>sudo_sendlog</code> supports a flexible debugging framework that is configured via <code>Debug</code> lines in the sudo.conf5 file. </p>
<p> For more information on configuring sudo.conf5, please refer to its manual.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/sudo.conf </code></p>
<dd>Sudo front-end configuration</dl>
<h2>See Also</h2>
<p>sudo.conf5, <a href="/docs/linux/man/8-sudo/">sudo</a>(8), sudo_logsrvd8</p>
<h2>Authors</h2>
<p>Many people have worked on <code>sudo</code> over the years; this version consists of code written primarily by: </p>
<blockquote><p> An Todd C. Miller </p></blockquote>
<p> See the CONTRIBUTORS file in the <code>sudo</code> distribution (<a rel="nofollow" href="https://www.sudo.ws/contributors.html)">https://www.sudo.ws/contributors.html)</a> for an exhaustive list of people who have contributed to <code>sudo</code></p>
<h2>Bugs</h2>
<p>If you feel you have found a bug in <code>sudo_sendlog,</code> please submit a bug report at <a rel="nofollow" href="https://bugzilla.sudo.ws/">https://bugzilla.sudo.ws/</a></p>
<h2>Support</h2>
<p>Limited free support is available via the sudo-users mailing list, see <a rel="nofollow" href="https://www.sudo.ws/mailman/listinfo/sudo-users">https://www.sudo.ws/mailman/listinfo/sudo-users</a> to subscribe or search the archives.</p>
<h2>Disclaimer</h2>
<p><code>sudo_sendlog</code> is provided &#8220;AS IS&#8221; and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. See the LICENSE file distributed with <code>sudo</code> or <a rel="nofollow" href="https://www.sudo.ws/license.html">https://www.sudo.ws/license.html</a> for complete details.</p>
