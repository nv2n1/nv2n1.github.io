---
title: "mydnscheck(8)"
name: "mydnscheck"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mydnscheck/"
description: "mydnscheck – Check zone data for consistency and syntax."
---

<p>mydnscheck &#8211; Check zone data for consistency and syntax.</p>
<h2>Synopsis</h2>
<p><code>mydnscheck</code> [<code>-c</code>, <code>&#8211;consistency</code>] [<code>-C</code>, <code>&#8211;consistency-only</code>] [<code>-D</code>, <code>&#8211;database=</code><i>dbname</i>] [<code>-h</code>, <code>&#8211;host=</code><i>hostname</i>] [<code>-p</code>, <code>&#8211;password[=</code><i>password</i>]] [<code>-u</code>, <code>&#8211;user=</code><i>username</i>] [<code>-v</code>, <code>&#8211;verbose</code>] [<code>&#8211;help</code>] [<code>&#8211;version</code>] [<code>ZONE</code>&#8230;]</p>
<h2>Description</h2>
<p><code>mydnscheck</code> scans the zones named on the command line for syntax. If no zones are specified, all zones are scanned. If the -c (or -C) option is specified, additional database consistency checks are performed. The program writes all results to stdout in a format that both humans and computers should be able to read. Each problem found is listed on a separate line, with a TAB character in between each field. The fields listed are: <code>MESSAGE</code> .. <code>SOA ID</code> .. <code>RR ID</code> .. <code>NAME</code> .. <code>TTL</code> .. <code>TYPE</code> .. <code>DATA</code> If stderr is a terminal, a progress meter is displayed if scanning all zones.</p>
<h2>Program Options</h2>
<dl>
<dt><code>-c</code>, <code>&#8211;consistency</code></p>
<dd>Perform database consistency checks in addition to the usual syntax checks</p>
<dt><code>-C</code>, <code>&#8211;consistency-only</code></p>
<dd>Skip the syntax checks and only perform the database consistency checks.</p>
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
<p><code><a href="/docs/linux/man/8-mydns/">mydns</a></code>(8), <code><a href="/docs/linux/man/5-mydns-conf/">mydns.conf</a></code>(5), <code><a href="/docs/linux/man/8-mydnsexport/">mydnsexport</a></code>(8), <code><a href="/docs/linux/man/8-mydnsimport/">mydnsimport</a></code>(8) </p>
