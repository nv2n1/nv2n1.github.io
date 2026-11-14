---
title: "proxymap(8)"
name: "proxymap"
section: "8"
letter: "p"
url: "/docs/linux/man/8-proxymap/"
description: "proxymap – Postfix lookup table proxy server"
---

<p>proxymap &#8211; Postfix lookup table proxy server</p>
<h2>Synopsis</h2>
<pre><code>proxymap</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) server provides read-only or read-write table lookup service to Postfix processes. These services are implemented with distinct service names: <code>proxymap</code> and <code>proxywrite</code>, respectively. The purpose of these services is:</p>
<dl>
<dt>&bull;</p>
<dd>To overcome chroot restrictions. For example, a chrooted SMTP server needs access to the system passwd file in order to reject mail for non-existent local addresses, but it is not practical to maintain a copy of the passwd file in the chroot jail. The solution: </p>
<pre>local_recipient_maps =
 proxy:unix:passwd.byname $alias_maps</pre>
<dt>&bull;</p>
<dd>To consolidate the number of open lookup tables by sharing one open table among multiple processes. For example, making mysql connections from every Postfix daemon process results in &quot;too many connections&quot; errors. The solution: </p>
<pre>virtual_alias_maps =
 proxy:mysql:/etc/postfix/virtual_alias.cf</pre>
<p>The total number of connections is limited by the number of proxymap server processes.</p>
<dt>&bull;</p>
<dd>To provide single-updater functionality for lookup tables that do not reliably support multiple writers (i.e. all file-based tables).</dl>
<p> The <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) server implements the following requests:</p>
<dl>
<dt><code>open</code> <i>maptype:mapname flags</i></p>
<dd>Open the table with type <i>maptype</i> and name <i>mapname</i>, as controlled by <i>flags</i>. The reply includes the <i>maptype</i> dependent flags (to distinguish a fixed string table from a regular expression table).</p>
<dt><code>lookup</code> <i>maptype:mapname flags key</i></p>
<dd>Look up the data stored under the requested key. The reply is the request completion status code and the lookup result value. The <i>maptype:mapname</i> and <i>flags</i> are the same as with the <code>open</code> request.</p>
<dt><code>update</code> <i>maptype:mapname flags key value</i></p>
<dd>Update the data stored under the requested key. The reply is the request completion status code. The <i>maptype:mapname</i> and <i>flags</i> are the same as with the <code>open</code> request. </p>
<p> To implement single-updater maps, specify a process limit of 1 in the master.cf file entry for the <code>proxywrite</code> service. </p>
<p> This request is supported in Postfix 2.5 and later.</p>
<dt><code>delete</code> <i>maptype:mapname flags key</i></p>
<dd>Delete the data stored under the requested key. The reply is the request completion status code. The <i>maptype:mapname</i> and <i>flags</i> are the same as with the <code>open</code> request. </p>
<p> This request is supported in Postfix 2.5 and later.</p>
<dt><code>sequence</code> <i>maptype:mapname flags function</i></p>
<dd>Iterate over the specified database. The <i>function</i> is one of DICT_SEQ_FUN_FIRST or DICT_SEQ_FUN_NEXT. The reply is the request completion status code and a lookup key and result value, if found. </p>
<p> This request is supported in Postfix 2.9 and later.</dl>
<p> The request completion status is one of OK, RETRY, NOKEY (lookup failed because the key was not found), BAD (malformed request) or DENY (the table is not approved for proxy read or update access). </p>
<p> There is no <code>close</code> command, nor are tables implicitly closed when a client disconnects. The purpose is to share tables among multiple client processes.</p>
<h2>Server Process Management</h2>
<p><code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) servers run under control by the Postfix <code><a href="/docs/linux/man/8-master/">master</a></code>(8) server. Each server can handle multiple simultaneous connections. When all servers are busy while a client connects, the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) creates a new <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) server process, provided that the process limit is not exceeded. Each server terminates after serving at least <code>$max_use</code> clients or after <code>$max_idle</code> seconds of idle time.</p>
<h2>Security</h2>
<p>The <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) server opens only tables that are approved via the <code>proxy_read_maps</code> or <code>proxy_write_maps</code> configuration parameters, does not talk to users, and can run at fixed low privilege, chrooted or not. However, running the proxymap server chrooted severely limits usability, because it can open only chrooted tables. </p>
<p> The <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) server is not a trusted daemon process, and must not be used to look up sensitive information such as UNIX user or group IDs, mailbox file/directory names or external commands. </p>
<p> In Postfix version 2.2 and later, the proxymap client recognizes requests to access a table for security-sensitive purposes, and opens the table directly. This allows the same main.cf setting to be used by sensitive and non-sensitive processes. </p>
<p> Postfix-writable data files should be stored under a dedicated directory that is writable only by the Postfix mail system, such as the Postfix-owned <code>data_directory</code>. </p>
<p> In particular, Postfix-writable files should never exist in root-owned directories. That would open up a particular type of security hole where ownership of a file or directory does not match the provider of its content.</p>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8).</p>
<h2>Bugs</h2>
<p>The <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) server provides service to multiple clients, and must therefore not be used for tables that have high-latency lookups. </p>
<p> The <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) read-write service does not explicitly close lookup tables (even if it did, this could not be relied on, because the process may be terminated between table updates). The read-write service should therefore not be used with tables that leave persistent storage in an inconsistent state between updates (for example, CDB). Tables that support &quot;sync on update&quot; should be safe (for example, Berkeley DB) as should tables that are implemented by a real DBMS.</p>
<h2>Configuration Parameters</h2>
<p>On busy mail systems a long time may pass before <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) relevant changes to <code>main.cf</code> are picked up. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>data_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The directory with Postfix-writable data files (for example: caches, pseudo-random numbers).</p>
<dt><code>daemon_timeout (18000s)</code></p>
<dd>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer.</p>
<dt><code>ipc_timeout (3600s)</code></p>
<dd>The time limit for sending or receiving information over an internal communication channel.</p>
<dt><code>max_idle (100s)</code></p>
<dd>The maximum amount of time that an idle Postfix daemon process waits for an incoming connection before terminating voluntarily.</p>
<dt><code>max_use (100)</code></p>
<dd>The maximal number of incoming connections that a Postfix daemon process will service before terminating voluntarily.</p>
<dt><code>process_id (read-only)</code></p>
<dd>The process ID of a Postfix command or daemon process.</p>
<dt><code>process_name (read-only)</code></p>
<dd>The process name of a Postfix command or daemon process.</p>
<dt><code>proxy_read_maps (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The lookup tables that the <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) server is allowed to access for the read-only service.</dl>
<p> Available in Postfix 2.5 and later:</p>
<dl>
<dt><code>data_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The directory with Postfix-writable data files (for example: caches, pseudo-random numbers).</p>
<dt><code>proxy_write_maps (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The lookup tables that the <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) server is allowed to access for the read-write service.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-master/">master</a>(5), generic daemon options</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>DATABASE_README, Postfix lookup table overview</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<p>The proxymap service was introduced with Postfix 2.0.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
