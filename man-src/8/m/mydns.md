---
title: "mydns(8)"
name: "mydns"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mydns/"
description: "mydns – SQL-based Internet name daemon."
---

<p>mydns &#8211; SQL-based Internet name daemon.</p>
<h2>Synopsis</h2>
<p><code>mydns</code> [<code>-b</code>, <code>&#8211;background</code>] [<code>-c</code>, <code>&#8211;conf=</code><i>filename</i>] [<code>-d</code>, <code>&#8211;debug</code>] [<code>-D</code>, <code>&#8211;database=</code><i>dbname</i>] [<code>-h</code>, <code>&#8211;host=</code><i>hostname</i>] [<code>-p</code>, <code>&#8211;password[=</code><i>password</i>]] [<code>-u</code>, <code>&#8211;user=</code><i>username</i>] [<code>-v</code>, <code>&#8211;verbose</code>] [<code>&#8211;create-tables</code>] [<code>&#8211;dump-config</code>] [<code>&#8211;debug-&lt;module&gt;</code>[=<i>&lt;debug_level&gt;</i>]] [<code>&#8211;help</code>] [<code>&#8211;version</code>]</p>
<h2>Description</h2>
<p><code>mydns</code> is a SQL-based DNS server.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;background</code></p>
<dd>Run in the background, as a daemon.</p>
<dt><code>-c</code>, <code>&#8211;conf</code>=<i>filename</i></p>
<dd>Read configuration from <i>filename</i> instead of the default (<code>/etc/mydns.conf</code>). Consult <code><a href="/docs/linux/man/5-mydns-conf/">mydns.conf</a></code>(5) for information about configuring <code>mydns</code>.</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>Output huge amounts of diagnostic text while running. This option is only available if MyDNS was configured with the <code>&#8211;enable-debug</code> option.</p>
<dt><code>-D</code>, <code>&#8211;database</code>=<i>dbname</i></p>
<dd>Use the database called <i>dbname</i>.</p>
<dt><code>-h</code>, <code>&#8211;host</code>=<i>hostname</i></p>
<dd>Connect to database server at <i>hostname</i>.</p>
<dt><code>-p</code>, <code>&#8211;pass</code>=<i>password</i></p>
<dd>Supply <i>password</i> when connecting to the database server. If the <i>password</i> argument is omitted, it will be prompted on the tty.</p>
<dt><code>-u</code>, <code>&#8211;user</code>=<i>username</i></p>
<dd>Use <i>username</i> when connecting to the database server.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Enable verbose output while running.</p>
<dt><code>&#8211;create-tables</code></p>
<dd>Write CREATE TABLE statements suitable for creating the tables used by <code>mydns</code> to the standard output and exit.</p>
<dt><code>&#8211;dump-config</code></p>
<dd>Read the current configuration (if any). Dump all possible configuration options to the standard output, with current values filled in. For options not presently configured, the internal defaults will be used. Output is in <code>mydns.conf</code> format, which is handy for creating a <code>mydns.conf</code> template.</p>
<dt><code>&#8211;debug-&lt;module&gt;</code>[=<i>&lt;debug-level&gt;</i></p>
<dd>Switch on debug for a particular module and set the debug level if given.</p>
<dt><code>&#8211;help</code></p>
<dd>Display program help and exit.</p>
<dt><code>&#8211;version</code></p>
<dd>Output version number and exit.</dl>
<h2>Files</h2>
<p><i>/etc/mydns.conf</i></p>
<dl>
<dd>The default location of the configuration file. (See <code><a href="/docs/linux/man/5-mydns-conf/">mydns.conf</a></code>(5))</dl>
<h2>Author</h2>
<p>Don Moore &lt;bboy [at] bboy.net&gt; Howard Wilkinson &lt;howard [at] cohtech.com&gt;</p>
<h2>Homepage</h2>
<p><a rel="nofollow" href="http://mydns.bboy.net">http://mydns.bboy.net</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-mydns-conf/">mydns.conf</a></code>(5), <code><a href="/docs/linux/man/8-mydnscheck/">mydnscheck</a></code>(8), <code><a href="/docs/linux/man/8-mydnsexport/">mydnsexport</a></code>(8), <code><a href="/docs/linux/man/8-mydnsimport/">mydnsimport</a></code>(8) This man page is a quick reference. For detailed documentation, see the MyDNS user&#8217;s manual, available from <a rel="nofollow" href="http://mydns.bboy.net.">http://mydns.bboy.net.</a> </p>
