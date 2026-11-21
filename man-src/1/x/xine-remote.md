---

title: "xine-remote(1)"
name: "xine-remote"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xine-remote/"
description: "xine-remote – a small tool to connect xine remote control server."
---

<p> xine-remote &#8211; a small tool to connect xine remote control server.</p>
<h2>SYNOPSIS</h2>
<p> <code>xine-remote</code> <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>xine-remote</code> tool. </p>
<p> <code>xine-remote</code> can replace a <i>raw</i> telnet connection to a xine remote control server. It use the <code>readline</code> facilities (completion, vi/emacs shortcuts, command history, etc&#8230;). By default, it try to connect the localhost, using the default port (see <i><a href="/docs/linux/man/1-xine/">xine</a></i>(1)).</p>
<h2>OPTIONS</h2>
<p> The program follow the usual GNU command line syntax, with long ioptions starting with two dashes (`-&#8216;). A summary of options are included below.</p>
<dl>
<dt><code>-H, &#8211;host&nbsp;<wbr></code>&lt;hostname&gt;</dt>
<dd> Try to connect &lt;<code>hostname</code>&gt;.</dd>
<dt><code>-P, &#8211;port&nbsp;<wbr></code>&lt;port&gt;</dt>
<dd> Try to connect the host using &lt;<code>port</code>&gt;.</dd>
<dt><code>-c, &#8211;command&nbsp;<wbr></code>&lt;command&gt;</dt>
<dd> Send &lt;<code>command</code>&gt; to server then quit. The command should be single quoted if it contain spaces or special characters.</dd>
<dt><code>-n, &#8211;noconnect</code></dt>
<dd> Do not initiate the connection on startup.</dd>
<dt><code>-v, &#8211;version</code></dt>
<dd> Display version.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display options summary.
</dd></dl>
<h2>COMMANDS</h2>
<p> Few commands are available, which are used to open or close a connection:</p>
<dl>
<dt><code>?</code></dt>
<dd> Display available commands (the xine-remote ones + server ones when connection is established).</dd>
<dt><code>help&nbsp;<wbr></code>&lt;command&gt;</dt>
<dd> Display the purpose of &lt;<code>command</code>&gt;, if that is omitted, display available commands.</dd>
<dt><code>syntax&nbsp;<wbr></code>&lt;command&gt;</dt>
<dd> Display the usage of &lt;<code>command</code>&gt;.</dd>
<dt><code>version</code></dt>
<dd> Display version.</dd>
<dt><code>open&nbsp;<wbr></code>&lt;server[:port]&gt;</dt>
<dd> Open connection to <code>server</code>. A <code>port</code> can be optionally specified, using colon (<code>:</code>) separator.</dd>
<dt><code>close</code></dt>
<dd> Close connection.</dd>
<dt><code>quit</code></dt>
<dd> Leaving xine-remote.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xine/">xine</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Daniel Caujolle-Bert &lt;f1rmb [at] users.sourceforge.net&gt; for the xine project. </p>
