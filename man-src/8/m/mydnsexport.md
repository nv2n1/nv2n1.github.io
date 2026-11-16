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
<dt><code>-b</code>, <code>&#8211;bind</code></dt>
<dd>Output the specified zone(s) in BIND zone file format.</dd>
<dt><code>-t</code>, <code>&#8211;tinydns-data</code></dt>
<dd>Output the specified zone(s) in tinydns-data format.</dd>
<dt><code>-D</code>, <code>&#8211;database</code>=<i>dbname</i></dt>
<dd>Use the database called <i>dbname</i>.</dd>
<dt><code>-h</code>, <code>&#8211;host</code>=<i>hostname</i></dt>
<dd>Connect to database server at <i>hostname</i>.</dd>
<dt><code>-p</code>, <code>&#8211;pass</code>=<i>password</i></dt>
<dd>Supply <i>password</i> when connecting to the database server. If the <i>password</i> argument is omitted, it will be prompted on the tty.</dd>
<dt><code>-u</code>, <code>&#8211;user</code>=<i>username</i></dt>
<dd>Use <i>username</i> when connecting to the database server.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd>Enable verbose output while running.</dd>
<dt><code>&#8211;help</code></dt>
<dd>Display program help and exit.</dd>
<dt><code>&#8211;version</code></dt>
<dd>Output version number and exit.</dd></dl>
<h2>Author</h2>
<p>Don Moore &lt;bboy [at] bboy.net&gt; Howard Wilkinson &lt;howard [at] cohtech.com&gt;</p>
<h2>Homepage</h2>
<p><a rel="nofollow" href="http://mydns.bboy.net">http://mydns.bboy.net</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mydns/">mydns</a></code>(8), <code>mydns.conf</code>(5), <code><a href="/docs/linux/man/8-mydnscheck/">mydnscheck</a></code>(8), <code><a href="/docs/linux/man/8-mydnsimport/">mydnsimport</a></code>(8) </p>
