---

title: "mdb_stat(1)"
name: "mdb_stat"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdb_stat/"
description: "mdb_stat – LMDB environment status tool"
---

<p> <code>mdb_stat</code> [<code>-V</code>] [<code>-e</code>] [<code>-f</code>[<code>f</code>[<code>f</code>]]] [<code>-n</code>] [<code>-r</code>[<code>r</code>]] [<code>-a</code>&nbsp;<wbr>| <code>-s</code><i>&nbsp;<wbr>subdb</i>] <code>&nbsp;<wbr>envpath</code></p>
<p> The <code>mdb_stat</code> utility displays the status of an LMDB environment.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-V</code></dt>
<dd> Write the library version number to the standard output, and exit.</dd>
<dt><code>-e</code></dt>
<dd> Display information about the database environment.</dd>
<dt><code>-f</code></dt>
<dd> Display information about the environment freelist. If <code>-ff</code> is given, summarize each freelist entry. If <code>-fff</code> is given, display the full list of page IDs in the freelist.</dd>
<dt><code>-n</code></dt>
<dd> Display the status of an LMDB database which does not use subdirectories.</dd>
<dt><code>-r</code></dt>
<dd> Display information about the environment reader table. Shows the process ID, thread ID, and transaction ID for each active reader slot. The process ID and transaction ID are in decimal, the thread ID is in hexadecimal. The transaction ID is displayed as &quot;-&quot; if the reader does not currently have a read transaction open. If <code>-rr</code> is given, check for stale entries in the reader table and clear them. The reader table will be printed again after the check is performed.</dd>
<dt><code>-a</code></dt>
<dd> Display the status of all of the subdatabases in the environment.</dd>
<dt><code>-s</code>&nbsp;<wbr>subdb</dt>
<dd> Display the status of a specific subdatabase.</dd></dl>
<h2>DIAGNOSTICS</h2>
<p> Exit status is zero if no errors occur. Errors result in a non-zero exit status and a diagnostic message being written to standard error.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mdb_copy/">mdb_copy</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Howard Chu of Symas Corporation &lt;<a rel="nofollow" href="http://www.symas.com">http://www.symas.com</a>&gt; </p>
