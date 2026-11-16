---
title: "mydnsimport(8)"
name: "mydnsimport"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mydnsimport/"
description: "mydnsimport – Import zone data from external sources."
---

<p>mydnsimport &#8211; Import zone data from external sources.</p>
<h2>Synopsis</h2>
<p><code>mydnsimport</code> [<code>-a</code>, <code>&#8211;axfr=</code><i>host</i>] [<code>-D</code>, <code>&#8211;database=</code><i>dbname</i>] [<code>-h</code>, <code>&#8211;host=</code><i>hostname</i>] [<code>-o</code>, <code>&#8211;output</code>] [<code>-p</code>, <code>&#8211;password[=</code><i>password</i>]] [<code>-r</code>, <code>&#8211;replace</code>] [<code>-t</code>, <code>&#8211;tinydns=</code><i>file</i>] [<code>&#8211;notrim</code>] [<code>-u</code>, <code>&#8211;user=</code><i>username</i>] [<code>-v</code>, <code>&#8211;verbose</code>] [<code>&#8211;help</code>] [<code>&#8211;version</code>] <code>ZONE</code> [<code>&#8230;</code>]</p>
<h2>Description</h2>
<p><code>mydnsimport</code> imports zone data into MyDNS from an external source. If an import technique is specified (for example, via the <code>&#8211;axfr</code> option), the specified zone data will be loaded and <code>mydnsimport</code> will add the zone data to your database. Currently, <code>&#8211;axfr</code> and <code>&#8211;tinydns</code> are the only import techniques recognized.</p>
<h2>Options</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;axfr</code>=<i>hostname[:port]</i></dt>
<dd>Load <i>zone</i> information from the specified <i>hostname</i> via the DNS-based AXFR command.</dd>
<dt><code>-o</code>, <code>&#8211;output</code></dt>
<dd>If this option is specified, <code>mydnsimport</code> outputs zone data in a computer-friendly format instead of modifying the database. Each line of output consists of a <i>line type</i> (<code>soa</code>, <code>rr</code>, or <code>ptr</code>) followed by multiple fields. Fields within each line are separated by the <i>TAB</i> (ASCII 0x09) character. See <code>LINE SYNTAX</code>, below.</dd>
<dt><code>-r</code>, <code>&#8211;replace</code></dt>
<dd>When importing, if the <i>zone</i> specified already exists, <code>mydnsimport</code> will refuse to make changes to the database unless this flag is provided. When this flag is provided, if the <i>zone</i> already exists, its SOA record will be updated (from the external source), all resource records for that zone are purged, and a new set of resource records is loaded from the external source.</dd>
<dt><code>&#8211;notrim</code></dt>
<dd>Normally the zone origin is removed from labels when importing, in order to save space in the database. In other words, <code>host.example.com. becomes just host</code>. Using the <code>&#8211;notrim</code> option inhibits this behavior.</dd>
<dt><code>-D</code>, <code>&#8211;database</code>=<i>dbname</i></dt>
<dd>Use the database called <i>dbname</i>.</dd>
<dt><code>-h</code>, <code>&#8211;host</code>=<i>hostname</i></dt>
<dd>Connect to database server at <i>hostname</i>.</dd>
<dt><code>-p</code>, <code>&#8211;pass</code>=<i>password</i></dt>
<dd>Supply <i>password</i> when connecting to the database server. If the <i>password</i> argument is omitted, it will be prompted on the tty.</dd>
<dt><code>-t</code>, <code>&#8211;tinydns</code>=<i>file</i></dt>
<dd>Load <i>zone</i> information from the specified <i>file</i>, which is in tinydns-data format. When importing from a tinydns data file, <i>zone</i> may be omitted from the command line, in which case all zones found in the file are imported.</dd>
<dt><code>-u</code>, <code>&#8211;user</code>=<i>username</i></dt>
<dd>Use <i>username</i> when connecting to the database server.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd>Enable verbose output while running.</dd>
<dt><code>&#8211;help</code></dt>
<dd>Display program help and exit.</dd>
<dt><code>&#8211;version</code></dt>
<dd>Output version number and exit.</dd></dl>
<h2>Line Syntax</h2>
<p>When started with the <code>-o</code> (<code>&#8211;output</code>) option, <code>mydnsimport</code> outputs lines in the following format:</p>
<dl>
<dt>SOA</dt>
<dd>&quot;soa&quot; &lt;TAB&gt; origin &lt;TAB&gt; ns &lt;TAB&gt; mbox &lt;TAB&gt; serial &lt;TAB&gt; refresh &lt;TAB&gt; retry &lt;TAB&gt; expire &lt;TAB&gt; minimum &lt;TAB&gt; ttl</dd>
<dt>RR</dt>
<dd>&quot;rr&quot; &lt;TAB&gt; name &lt;TAB&gt; type &lt;TAB&gt; data &lt;TAB&gt; aux &lt;TAB&gt; ttl</dd>
<dt>PTR</dt>
<dd>&quot;ptr&quot; &lt;TAB&gt; address &lt;TAB&gt; name &lt;TAB&gt; ttl</dd></dl>
<h2>Author</h2>
<p>Don Moore &lt;bboy [at] bboy.net&gt; Howard Wilkinson &lt;howard [at] cohtech.com&gt;</p>
<h2>Homepage</h2>
<p><a rel="nofollow" href="http://mydns.bboy.net">http://mydns.bboy.net</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-mydns/">mydns</a></code>(8), <code>mydns.conf</code>(5), <code><a href="/docs/linux/man/8-mydnscheck/">mydnscheck</a></code>(8), <code><a href="/docs/linux/man/8-mydnsexport/">mydnsexport</a></code>(8) </p>
