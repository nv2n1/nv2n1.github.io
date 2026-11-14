---
title: "git-remote-ext(1)"
name: "git-remote-ext"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-remote-ext/"
description: "git-remote-ext – Bridge smart transport to external command."
---

<h2 class="name">NAME</h2>
<p> git-remote-ext &#8211; Bridge smart transport to external command. </p>
<h2>SYNOPSIS</h2>
<pre>
git remote add &lt;nick&gt; &quot;ext::&lt;command&gt;[ &lt;arguments&gt;...]&quot;
</pre>
<h2>DESCRIPTION</h2>
<p> This remote helper uses the specified <i>&lt;command&gt;</i> to connect to a remote Git server. </p>
<p> Data written to stdin of the specified <i>&lt;command&gt;</i> is assumed to be sent to a git:// server, git-upload-pack, git-receive-pack or git-upload-archive (depending on situation), and data read from stdout of &lt;command&gt; is assumed to be received from the same service. </p>
<p> Command and arguments are separated by an unescaped space. </p>
<p> The following sequences have a special meaning: </p>
<p> &#8216;% &#8216;</p>
<dl>
<dt>
<dd> Literal space in command or argument.</dl>
<p> <i>%%</i></p>
<dl>
<dt>
<dd> Literal percent sign.</dl>
<p> <i>%s</i></p>
<dl>
<dt>
<dd> Replaced with name (receive-pack, upload-pack, or upload-archive) of the service Git wants to invoke.</dl>
<p> <i>%S</i></p>
<dl>
<dt>
<dd> Replaced with long name (git-receive-pack, git-upload-pack, or git-upload-archive) of the service Git wants to invoke.</dl>
<p> <i>%G</i> (must be the first characters in an argument)</p>
<dl>
<dt>
<dd> This argument will not be passed to <i>&lt;command&gt;</i>. Instead, it will cause the helper to start by sending git:// service requests to the remote side with the service field set to an appropriate value and the repository field set to rest of the argument. Default is not to send such a request. </p>
<p> This is useful if remote side is git:// server accessed over some tunnel.</dl>
<p> <i>%V</i> (must be first characters in argument)</p>
<dl>
<dt>
<dd> This argument will not be passed to <i>&lt;command&gt;</i>. Instead it sets the vhost field in the git:// service request (to rest of the argument). Default is not to send vhost in such request (if sent).</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> GIT_TRANSLOOP_DEBUG</p>
<dl>
<dt>
<dd> If set, prints debugging information about various reads/writes.</dl>
<h2>ENVIRONMENT VARIABLES PASSED TO COMMAND</h2>
<p> GIT_EXT_SERVICE</p>
<dl>
<dt>
<dd> Set to long name (git-upload-pack, etc&#8230;) of service helper needs to invoke.</dl>
<p> GIT_EXT_SERVICE_NOPREFIX</p>
<dl>
<dt>
<dd> Set to long name (upload-pack, etc&#8230;) of service helper needs to invoke.</dl>
<h2>EXAMPLES</h2>
<p> This remote helper is transparently used by Git when you use commands such as &quot;git fetch &lt;URL&gt;&quot;, &quot;git clone &lt;URL&gt;&quot;, , &quot;git push &lt;URL&gt;&quot; or &quot;git remote add &lt;nick&gt; &lt;URL&gt;&quot;, where &lt;URL&gt; begins with <code>ext::</code>. Examples: </p>
<p> &quot;ext::ssh -i /home/foo/.ssh/somekey user [at] host.example %S <i>foo/repo</i>&quot;</p>
<dl>
<dt>
<dd> Like host.example:foo/repo, but use /home/foo/.ssh/somekey as keypair and user as user on remote side. This avoids needing to edit .ssh/config.</dl>
<p> &quot;ext::socat -t3600 &#8211; ABSTRACT-CONNECT:/git-server %G/somerepo&quot;</p>
<dl>
<dt>
<dd> Represents repository with path /somerepo accessible over git protocol at abstract namespace address /git-server.</dl>
<p> &quot;ext::git-server-alias foo %G/repo&quot;</p>
<dl>
<dt>
<dd> Represents a repository with path /repo accessed using the helper program &quot;git-server-alias foo&quot;. The path to the repository and type of request are not passed on the command line but as part of the protocol stream, as usual with git:// protocol.</dl>
<p> &quot;ext::git-server-alias foo %G/repo %Vfoo&quot;</p>
<dl>
<dt>
<dd> Represents a repository with path /repo accessed using the helper program &quot;git-server-alias foo&quot;. The hostname for the remote server passed in the protocol stream will be &quot;foo&quot; (this allows multiple virtual Git servers to share a link-level address).</dl>
<p> &quot;ext::git-server-alias foo %G/repo% with% spaces %Vfoo&quot;</p>
<dl>
<dt>
<dd> Represents a repository with path <code>/repo with spaces</code> accessed using the helper program &quot;git-server-alias foo&quot;. The hostname for the remote server passed in the protocol stream will be &quot;foo&quot; (this allows multiple virtual Git servers to share a link-level address).</dl>
<p> &quot;ext::git-ssl foo.example /bar&quot;</p>
<dl>
<dt>
<dd> Represents a repository accessed using the helper program &quot;git-ssl foo.example /bar&quot;. The type of request can be determined by the helper using environment variables (see above).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-gitremote-helpers/">gitremote-helpers</a></code>(7)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
