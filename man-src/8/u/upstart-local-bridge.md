---
title: "upstart-local-bridge(8)"
name: "upstart-local-bridge"
section: "8"
letter: "u"
url: "/docs/linux/man/8-upstart-local-bridge/"
description: "upstart-local-bridge – Bridge between Upstart and a local client socket connection."
---

<p>upstart-local-bridge &#8211; Bridge between Upstart and a local client socket connection.</p>
<h2>Synopsis</h2>
<p><code>upstart-local-bridge</code> [<i>OPTIONS</i>]&#8230;</p>
<h2>Description</h2>
<p><code>upstart-local-bridge</code> listens on a local domain socket for name=value pairs and creates <code><a href="/docs/linux/man/8-init/">init</a></code>(8) events for them. </p>
<p> The local unix domain socket can be either named or abstract.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;any-user</code></p>
<dd>By default the bridge will only accept connections from clients running under the same user ID as the bridge itself. This option allows connections from any user.</p>
<dt><code>&#8211;daemon</code></p>
<dd>Detach and run in the background.</p>
<dt><code>&#8211;debug</code></p>
<dd>Enable debugging output.</p>
<dt><code>&#8211;event </code><i>event</i></p>
<dd>Specify name of event to emit on receipt of a name=value pair.</p>
<dt><code>&#8211;help</code></p>
<dd>Show brief usage summary.</p>
<dt><code>&#8211;path </code><i>path</i></p>
<dd>Specify path for local/abstract socket to listen on. If the first byte of <i>path</i> is an &#8216;<i>@</i>&#8216;, the socket will be created as an abstract socket.</p>
<dt><code>&#8211;verbose</code></p>
<dd>Enable verbose output.</dl>
<h2>Event Details</h2>
<p>The following environment variables are added automatically to the event to be emitted, with the name=value pair being added as the last variable. </p>
<dl>
<dt>&bull;</p>
<dd>SOCKET_TYPE=unix</p>
<dt>&bull;</p>
<dd>SOCKET_VARIANT=[<i>named</i>|<i>abstract</i>] Sub-type of socket.</p>
<dt>&bull;</p>
<dd>CLIENT_UID=<i>UID</i> User ID of connected client.</p>
<dt>&bull;</p>
<dd>CLIENT_GID=<i>GID</i> Group ID of connected client.</p>
<dt>&bull;</p>
<dd>CLIENT_PID=<i>PID</i> Process ID of connected client.</p>
<dt>&bull;</p>
<dd>SOCKET_PATH=<i>PATH</i></dl>
<h2>Examples</h2>
<dl>
<dt>upstart-local-bridge &#8211;event=foo &#8211;path=/var/foo/bar</p>
<dd>Listen on local socket <i>/var/foo/bar</i> and when a name=value pair is read, emit an event of the form: </p>
<dl>
<dd>
<pre>foo SOCKET_TYPE=unix SOCKET_VARIANT=named SOCKET_PATH=/var/foo/bar name=value</pre>
</dl>
<dt>upstart-local-bridge &#8211;event=bar &#8211;path=@/var/foo/bar</p>
<dd>Listen on abstract socket <i>@/var/foo/bar</i> and when a name=value pair is read, emit an event of the form: </p>
<dl>
<dd>
<pre>bar SOCKET_TYPE=unix SOCKET_VARIANT=abstract SOCKET_PATH=@/var/foo/bar name=value</pre>
</dl>
</dl>
<h2>Notes</h2>
<dl>
<dt>&bull;</p>
<dd>If a named local socket is specified, all path elements except for the last must already exist before the bridge starts.</dl>
<h2>Limitations</h2>
<dl>
<dt>&bull;</p>
<dd>Only a single client connection is serviced at any one time.</dl>
<h2>Author</h2>
<p>Written by James Hunt &lt;<code>james.hunt [at] canonical.com</code>&gt;</p>
<h2>Bugs</h2>
<p>Report bugs at &lt;<code><a rel="nofollow" href="https://launchpad.net/ubuntu/+source/upstart/+bugs">https://launchpad.net/ubuntu/+source/upstart/+bugs</a></code>&gt;</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2013 Canonical Ltd. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-init/">init</a></code>(5) <code><a href="/docs/linux/man/8-init/">init</a></code>(8) </p>
