---
title: "git-upload-pack(1)"
name: "git-upload-pack"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-upload-pack/"
description: "git-upload-pack – Send objects packed back to git-fetch-pack"
---

<h2 class="name">NAME</h2>
<p> git-upload-pack &#8211; Send objects packed back to git-fetch-pack </p>
<h2>SYNOPSIS</h2>
<pre><code>
git - upload - pack[--[no - ] strict][--timeout = &lt;n&gt;][--stateless - rpc][--advertise - refs]&lt;directory&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> Invoked by <i>git fetch-pack</i>, learns what objects the other side is missing, and sends them after packing. </p>
<p> This command is usually not invoked directly by the end user. The UI for the protocol is on the <i>git fetch-pack</i> side, and the program pair is meant to be used to pull updates from a remote repository. For push operations, see <i>git send-pack</i>.</p>
<h2>OPTIONS</h2>
<p> &#8211;[no-]strict</p>
<dl>
<dt>
<dd> Do not try &lt;directory&gt;/.git/ if &lt;directory&gt; is no Git directory.</dl>
<p> &#8211;timeout=&lt;n&gt;</p>
<dl>
<dt>
<dd> Interrupt transfer after &lt;n&gt; seconds of inactivity.</dl>
<p> &#8211;stateless-rpc</p>
<dl>
<dt>
<dd> Perform only a single read-write cycle with stdin and stdout. This fits with the HTTP POST request processing model where a program may read the request, write a response, and must exit.</dl>
<p> &#8211;http-backend-info-refs</p>
<dl>
<dt>
<dd> Used by <code><a href="/docs/linux/man/1-git-http-backend/">git-http-backend</a></code>(1) to serve up <code>$GIT_URL/info/refs?service=git-upload-pack</code> requests. See &quot;Smart Clients&quot; in m[blue]<code>the HTTP transfer protocols</code>m[]<font SIZE="-2">[1]</font> documentation and &quot;HTTP Transport&quot; in m[blue]<code>the Git Wire Protocol, Version 2</code>m[]<font SIZE="-2">[2]</font> documentation. Also understood by <code><a href="/docs/linux/man/1-git-receive-pack/">git-receive-pack</a></code>(1).</dl>
<p> &lt;directory&gt;</p>
<dl>
<dt>
<dd> The repository to sync from.</dl>
<h2>ENVIRONMENT</h2>
<p> <code>GIT_PROTOCOL</code></p>
<dl>
<dt>
<dd> Internal variable used for handshaking the wire protocol. Server admins may need to configure some transports to allow this variable to be passed. See the discussion in <code><a href="/docs/linux/man/1-git/">git</a></code>(1).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gitnamespaces/">gitnamespaces</a></code>(7)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> the HTTP transfer protocols</p>
<dl>
<dt>
<dd> file:///usr/share/doc/git/html/technical/http-protocol.html</dl>
<dt> 2.</p>
<dd> the Git Wire Protocol, Version 2</p>
<dl>
<dt>
<dd> file:///usr/share/doc/git/html/technical/protocol-v2.html</dl>
</dl>
<h2>Index</h2>
