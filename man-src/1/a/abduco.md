---
title: "abduco(1)"
name: "abduco"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abduco/"
description: "abduco – terminal session manager"
---

<h2 class="name">NAME</h2>
<p> abduco &#8211; terminal session manager </p>
<h2>SYNOPSIS</h2>
<p> <code>abduco</code> [<code>-e</code> <i>detachkey</i>] [<code>-r</code>] [<code>-f</code>] -c name command [<i>args</i>&nbsp;<wbr>&#8230;<i></i>]<br />
 <code>abduco</code> [<code>-e</code> <i>detachkey</i>] [<code>-r</code>] [<code>-f</code>] -n name command [<i>args</i>&nbsp;<wbr>&#8230;<i></i>]<br />
 <code>abduco</code> [<code>-e</code> <i>detachkey</i>] [<code>-r</code>] [<code>-f</code>] [<code>-l</code>] -A name command [<i>args</i>&nbsp;<wbr>&#8230;<i></i>]<br />
 <code>abduco</code> [<code>-e</code> <i>detachkey</i>] [<code>-r</code>] [<code>-l</code>] -a name </p>
<h2>DESCRIPTION</h2>
<p> <code>abduco</code> provides a way to disconnect a given application from its controlling terminal, thus it provides roughly the same session attach/detach support as <code><a href="/docs/linux/man/1-screen/">screen</a>(1)</code>,<code> <a href="/docs/linux/man/1-tmux/">tmux</a>(1)</code> or<code> dtach(1).</code> </p>
<p> If the <code>command</code> to execute is not specified, the environment variable <code>$ABDUCO_CMD</code> is examined, if it is not set <code>dvtm(1)</code> is executed. </p>
<p> All session related information is stored in the following directories (first to succeed is used):</p>
<dl>
<dt>
</dt><dd>
<pre>
<code>$ABDUCO_SOCKET_DIR/abduco</code>
<code>$HOME/.abduco</code>
<code>$TMPDIR/abduco/$USER</code>
<code>/tmp/abduco/$USER</code>
</pre>
</dd></dl>
<p> However if a given session name represents either a relative or absolute path it is used unmodified. </p>
<p> If for some reason the <code><a href="/docs/linux/man/7-unix/">unix</a>(7)</code> domain socket representing a session is deleted, sending <code>SIGUSR1</code> to the server process will recreate it.</p>
<h2>OPTIONS</h2>
<p> If no command line arguments are given all currently active sessions are printed sorted by their respective creation date. Lines starting with an asterik <code>*</code> indicate that at least one client is connected. A plus sign <code>+</code> indicates that the command terminated while no client was connected, attach to get its exit status.</p>
<dl>
<dt><code>-v</code></dt>
<dd> Print version information to standard output and exit.</dd>
<dt><code>-r</code></dt>
<dd> Readonly session, i.e. user input is ignored.</dd>
<dt><code>-e </code><i>detachkey</i></dt>
<dd> Set the key to detach which by default is set to CTRL+\ i.e. ^\ to detachkey.</dd>
<dt><code>-f</code></dt>
<dd> Force creation of session when there is an already terminated session of the same name, after showing its exit status.</dd>
<dt><code>-c</code></dt>
<dd> Create a new session and attach immediately to it.</dd>
<dt><code>-n</code></dt>
<dd> Create a new session but do not attach to it.</dd>
<dt><code>-A</code></dt>
<dd> Try to connect to an existing session, upon failure create said session and attach immediately to it.</dd>
<dt><code>-a</code></dt>
<dd> Attach to an existing session.</dd>
<dt><code>-l</code></dt>
<dd> Attach with the lowest priority, meaning this client will be the last to control the size.</dd></dl>
<h2>EXAMPLE</h2>
<p> Start a new session (assuming <code>dvtm(1)</code> is in <code>$PATH</code>) with </p>
<pre>
<code>abduco -c my-session</code>
</pre>
<p> do some work, then detach by pressing <code>CTRL+\</code> and later reattach with </p>
<pre>
<code>abduco -a my-session</code>
</pre>
<h2>AUTHOR</h2>
<p> abduco is written by Marc André Tanner &lt;mat at brain-dump.org&gt; </p>
