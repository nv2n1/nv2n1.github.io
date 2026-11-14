---
title: "memcache_table(5)"
name: "memcache_table"
section: "5"
letter: "m"
url: "/docs/linux/man/5-memcache_table/"
description: "memcache_table – Postfix memcache client configuration"
---

<p>memcache_table &#8211; Postfix memcache client configuration</p>
<h2>Synopsis</h2>
<pre><code>postmap -q &quot;</code><i>string</i><code>&quot; memcache:/etc/postfix/</code><i>filename</i>
<code>postmap -q - memcache:/etc/postfix/</code><i>filename</i><code> &lt;</code><i>inputfile</i></pre>
<h2>Description</h2>
<p>The Postfix mail system uses optional tables for address rewriting or mail routing. These tables are usually in <code>dbm</code> or <code>db</code> format. </p>
<p> Alternatively, lookup tables can be specified as memcache instances. To use memcache lookups, define a memcache source as a lookup table in main.cf, for example: </p>
<pre> virtual_alias_maps = memcache:/etc/postfix/memcache-aliases.cf</pre>
<p>The file /etc/postfix/memcache-aliases.cf has the same format as the Postfix main.cf file, and specifies the parameters described below. </p>
<p> The Postfix memcache client supports the lookup, update, delete and sequence (first/next) operations. The sequence operation requires a backup database that supports the operation.</p>
<h2>Memcache Main Parameters</h2>
<dl>
<dt><code>memcache (default: inet:localhost:11211)</code></p>
<dd>The memcache server (note: singular) that Postfix will try to connect to. For a TCP server specify &quot;inet:&quot; followed by a hostname or address, &quot;:&quot;, and a port name or number. Specify an IPv6 address inside &quot;[]&quot;. For a UNIX-domain server specify &quot;unix:&quot; followed by the socket pathname. Examples: </p>
<pre> memcache = inet:memcache.example.com:11211
 memcache = inet:127.0.0.1:11211
 memcache = inet:[fc00:8d00:189::3]:11211
 memcache = unix:/path/to/socket</pre>
<p>NOTE: to access a UNIX-domain socket with the <a href="/docs/linux/man/8-proxymap/">proxymap</a>(8) server, the socket must be accessible by the unprivileged postfix user.</p>
<dt><code>backup (default: undefined)</code></p>
<dd>An optional Postfix database that provides persistent backup for the memcache database. The Postfix memcache client will update the memcache database whenever it looks up or changes information in the persistent database. Specify a Postfix &quot;type:table&quot; database. Examples: </p>
<pre> # Non-shared postscreen cache.
 backup = btree:/var/lib/postfix/postscreen_cache_map
 # Shared postscreen cache for processes on the same host.
 backup = proxy:btree:/var/lib/postfix/postscreen_cache_map</pre>
<p>Access to remote proxymap servers is under development. </p>
<p> NOTE 1: When sharing a persistent <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) or <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) cache, disable automatic cache cleanup (set *_cache_cleanup_interval = 0) except with one Postfix instance that will be responsible for cache cleanup. </p>
<p> NOTE 2: When multiple tables share the same memcache database, each table should use the <code>key_format</code> feature (see below) to prepend its own unique string to the lookup key. Otherwise, automatic <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) or <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) cache cleanup may not work. </p>
<p> NOTE 3: When the backup database is accessed with &quot;proxy:&quot; lookups, the full backup database name (including the &quot;proxy:&quot; prefix) must be specified in the proxymap server&#8217;s proxy_read_maps or proxy_write_maps setting (depending on whether the access is read-only or read-write).</p>
<dt><code>flags (default: 0)</code></p>
<dd>Optional flags that should be stored along with a memcache update. The flags are ignored when looking up information.</p>
<dt><code>ttl (default: 3600)</code></p>
<dd>The expiration time in seconds of memcache updates. </p>
<p> NOTE 1: When using a memcache table as <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) or <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) cache without persistent backup, specify a zero *_cache_cleanup_interval value with all Postfix instances that use the memcache, and specify the largest <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) *_ttl value or <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) *_expire_time value as the memcache table&#8217;s <code>ttl</code> value. </p>
<p> NOTE 2: According to memcache protocol documentation, a value greater than 30 days (2592000 seconds) specifies absolute UNIX time. Smaller values are relative to the time of the update.</dl>
<h2>Memcache Key Parameters</h2>
<dl>
<dt><code>key_format (default: %s)</p>
<dd>Format of the lookup and update keys that the Postfix memcache client sends to the memcache server. By default, these are the same as the lookup and update keys that the memcache client receives from Postfix applications. </p>
<p> NOTE 1: The key_format</code> feature is not used for <code>backup</code> database requests. </p>
<p> NOTE 2: When multiple tables share the same memcache database, each table should prepend its own unique string to the lookup key. Otherwise, automatic <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) or <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) cache cleanup may not work. </p>
<p> Examples: </p>
<pre> key_format = aliases:%s
 key_format = verify:%s
 key_format = postscreen:%s</pre>
<p>The <code>key_format</code> parameter supports the following &#8216;%&#8217; expansions:</p>
<dl>
<dd>
<dl>
<dt><code>%%</code></p>
<dd>This is replaced by a literal &#8216;%&#8217; character.</p>
<dt><code>%s</code></p>
<dd>This is replaced by the memcache client input key.</p>
<dt><code>%u</code></p>
<dd>When the input key is an address of the form user [at] domain, <code>%u</code> is replaced by the SQL quoted local part of the address. Otherwise, <code>%u</code> is replaced by the entire search string. If the localpart is empty, a lookup is silently suppressed and returns no results (an update is skipped with a warning).</p>
<dt><code>%d</code></p>
<dd>When the input key is an address of the form user [at] domain, <code>%d</code> is replaced by the domain part of the address. Otherwise, a lookup is silently suppressed and returns no results (an update is skipped with a warning).</p>
<dt><code>%[SUD]</code></p>
<dd>The upper-case equivalents of the above expansions behave in the <code>key_format</code> parameter identically to their lower-case counter-parts.</p>
<dt><code>%[1-9]</code></p>
<dd>The patterns %1, %2, &#8230; %9 are replaced by the corresponding most significant component of the input key&#8217;s domain. If the input key is <i>user [at] mail.example.com</i>, then %1 is <code>com</code>, %2 is <code>example</code> and %3 is <code>mail</code>. If the input key is unqualified or does not have enough domain components to satisfy all the specified patterns, a lookup is silently suppressed and returns no results (an update is skipped with a warning).</dl>
</dl>
<dt><code>domain (default: no domain list)</code></p>
<dd>This feature can significantly reduce database server load. Specify a list of domain names, paths to files, or &quot;type:table&quot; databases. When specified, only fully qualified search keys with a *non-empty* localpart and a matching domain are eligible for lookup or update: bare &#8216;user&#8217; lookups, bare domain lookups and &quot;@domain&quot; lookups are silently skipped (updates are skipped with a warning). Example: </p>
<pre> domain = example.com, hash:/etc/postfix/searchdomains</pre>
</dl>
<h2>Memcache Error Controls</h2>
<dl>
<dt><code>data_size_limit (default: 10240)</code></p>
<dd>The maximal memcache reply data length in bytes.</p>
<dt><code>line_size_limit (default: 1024)</code></p>
<dd>The maximal memcache reply line length in bytes.</p>
<dt><code>max_try (default: 2)</code></p>
<dd>The number of times to try a memcache command before giving up. The memcache client does not retry a command when the memcache server accepts no connection.</p>
<dt><code>retry_pause (default: 1)</code></p>
<dd>The time in seconds before retrying a failed memcache command.</p>
<dt><code>timeout (default: 2)</code></p>
<dd>The time limit for sending a memcache command and for receiving a memcache reply.</dl>
<h2>Bugs</h2>
<p>The Postfix memcache client cannot be used for security-sensitive tables such as <code>alias_maps</code> (these may contain &quot;<i>|command</i> and &quot;<i>/file/name</i>&quot; destinations), or <code>virtual_uid_maps</code>, <code>virtual_gid_maps</code> and <code>virtual_mailbox_maps</code> (these specify UNIX process privileges or &quot;<i>/file/name</i>&quot; destinations). In a typical deployment a memcache database is writable by any process that can talk to the memcache server; in contrast, security-sensitive tables must never be writable by the unprivileged Postfix user. </p>
<p> The Postfix memcache client requires additional configuration when used as <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) or <code><a href="/docs/linux/man/8-verify/">verify</a></code>(8) cache. For details see the <code>backup</code> and <code>ttl</code> parameter discussions in the MEMCACHE MAIN PARAMETERS section above.</p>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/1-postmap/">postmap</a>(1), Postfix lookup table manager
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>DATABASE_README, Postfix lookup table overview
MEMCACHE_README, Postfix memcache client guide</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<p>Memcache support was introduced with Postfix version 2.9.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA</pre>
