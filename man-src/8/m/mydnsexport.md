---
title: "mydnsexport(8)"
name: "mydnsexport"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mydnsexport/"
description: "mydnsexport – Output zone data in various foreign file formats"
---

<p>mydnsexport &#8211; Output zone data in various foreign file formats</p>
<h2>Synopsis</h2>
<p><code>mydnsexport</code> [<code>-b</code>, <code>&#8211;bind</code>] [<code>-t</code>, <code>&#8211;tinydns-data</code>] [<code>-D</code>, <code>&#8211;database=</code><i>dbname</i>] [<code>-h</code>, <code>&#8211;host=</code><i>hostname</i>] [<code>-p</code>, <code>&#8211;password[=</code><i>password</i>]] [<code>-u</code>, <code>&#8211;user=</code><i>username</i>] [<code>-v</code>, <code>&#8211;verbose</code>] [<code>&#8211;help</code>] [<code>&#8211;version</code>] [<code>ZONE</code>] [<code>&#8230;</code>]</p>
<h2>Description</h2>
<p><code>mydnsexport</code> outputs information about the zone(s) specified on the command line to the standard output, in the format specified. By default, it outputs BIND zone file format. Currently it can also output in <i>tinydns-data</i> format if the <code>-t</code>, <code>&#8211;tinydns-data</code> option is specified. If no zones are specified, all zones will be output.</p>
<h2>Options</h2>
<dl>
<dt><code>-b</code>, <code>&#8211;bind</code></p>
<dd>Output the specified zone(s) in BIND zone file format.</p>
<dt><code>-t</code>, <code>&#8211;tinydns-data</code></p>
<dd>Output the specified zone(s) in tinydns-data format.</p>
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
<dt><code>&#8211;help</code></p>
<dd>Display program help and exit.</p>
<dt><code>&#8211;version</code></p>
<dd>Output version number and exit.</dl>
<h2>Author</h2>
<p>Don Moore &lt;bboy [at] bboy.net&gt; Howard Wilkinson &lt;howard [at] cohtech.com&gt;</p>
<h2>Homepage</h2>
<p><a rel="nofollow" href="http://mydns.bboy.net">http://mydns.bboy.net</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mydns/">mydns</a></code>(8), <code><a href="/docs/linux/man/5-mydns-conf/">mydns.conf</a></code>(5), <code><a href="/docs/linux/man/8-mydnscheck/">mydnscheck</a></code>(8), <code><a href="/docs/linux/man/8-mydnsimport/">mydnsimport</a></code>(8) </p>
