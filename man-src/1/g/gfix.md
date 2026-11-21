---

title: "gfix(1)"
name: "gfix"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfix/"
description: "gfix — miscelenous Firebird database maintenance"
---

<p> <code>gfix</code> <i>command</i> [<i>option</i>&#8230;] <i>database</i></p>
<p> <code>gfix</code> is a program that allows the Firebird administrator or database owner to perform various maintenance tasks.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>-ac</code></dt>
<dd>
</dd><dt><code>-activate_shadow</code></dt>
<dd> Activate database shadow file.</dd>
<dt><code>-b</code> <i>number</i></dt>
<dd>
</dd><dt><code>-buffers</code> <i>number</i></dt>
<dd> Set database buffer size, in pages.</dd>
<dt><code>-co</code> <i>number</i>|&quot;all&quot;</dt>
<dd>
</dd><dt><code>-commit</code> <i>number</i>|&quot;all&quot;</dt>
<dd> Commit a limbo transaction with a given number or all limbo transactions.</dd>
<dt><code>-h</code> <i>number</i></dt>
<dd>
</dd><dt><code>-housekeeping</code> <i>number</i></dt>
<dd> Set the housekeeping interval. When the difference between the oldest interesting transaction and the current transaction exceeds <i>number</i>, an automatic garbage collection (sweep) process is started to make possible increasing of the oldest interesting transaction number. </dd>
<p> When <i>number</i> is <tt>0</tt>, there is no automatic sweep and <font SIZE="-1">OIT</font> advancement should be arranged by other means, e.g. <code>gfix -sweep</code> via <code>cron</code>(1).</p>
<dt><code>-icu</code></dt>
<dd> Fix the database to be usable with the available <font SIZE="-1">ICU</font> version. </dd>
<p> Some collations in Firebird are bound the the version of the <font SIZE="-1">ICU</font> library. When such a collation needs to be used in an environment with a different version of <font SIZE="-1">ICU,</font> an error occurs. <code>gfix -icu</code> is the remedy.</p>
<dt><code>-k</code></dt>
<dd>
</dd><dt><code>-kill_shadow</code></dt>
<dd> Kill unavailable database shadow files.</dd>
<dt><code>-l</code></dt>
<dd>
</dd><dt><code>-list</code></dt>
<dd> List limbo transactions.</dd>
<dl>
<dl>
<dt><code>-pr</code></dt>
<dd>
</dd><dt><code>-prompt</code></dt>
<dd> Prompt for commit/rollback for each transaction in limbo.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-me</code></dt>
<dd>
</dd><dt><code>-mend</code></dt>
<dd> Prepare corrupt database for backup.</dd>
<dt><code>-mo</code> <i>access</i></dt>
<dd>
</dd><dt><code>-mode</code> <i>access</i></dt>
<dd> Set database access mode. Possibla values are <tt>&quot;read_only&quot;</tt> and <tt>&quot;read_write&quot;</tt>.</dd>
<dt><code>-nol</code></dt>
<dd>
</dd><dt><code>-nolinger</code></dt>
<dd> Temporary remove linger setting of the database. </dd>
<p> Similar to the following <font SIZE="-1">SQL</font> statement: </p>
<pre>
 alter database drop linger;
</pre>
<p> but the next attachment to the database will restore the linger setting. </p>
<p> See <i>sql.extensions/README.linger</i>.</p>
<dt><code>-o</code> [<i>mode</i>]</dt>
<dd>
</dd><dt><code>-online</code> [<i>mode</i>]</dt>
<dd> Brings the database online. The reverse of <code>-shut</code>. </dd>
<p> <i>mode</i> can be:</p>
<dl>
<dl>
<dt><code>normal</code></dt>
<dd> This is the default. Brings the database fully online, all normal connections are permitted.</dd>
<dt><code>multi</code></dt>
<dd> Permits multiple connections from <font SIZE="-1">SYSDBA</font> and the database owner.</dd>
<dt><code>single</code></dt>
<dd> Permins only one connection from <font SIZE="-1">SYSDBA</font> or the database owner.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-v</code></dt>
<dd>
</dd><dt><code>-validate</code></dt>
<dd> Perform database validation. </dd>
<p> Validation options:</p>
<dl>
<dl>
<dt><code>-fu</code></dt>
<dd>
</dd><dt><code>-full</code></dt>
<dd> Full validation. Record fragments are verified.</dd>
<dt><code>-i</code></dt>
<dd>
</dd><dt><code>-ignore</code></dt>
<dd> Ignore record checksum errors.</dd>
<dt><code>-n</code></dt>
<dd>
</dd><dt><code>-no_update</code></dt>
<dd> Peform read-only validation.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-r</code> <i>number</i>|&quot;all&quot;</dt>
<dd>
</dd><dt><code>-rollback</code> <i>number</i>|&quot;all&quot;</dt>
<dd> Rollback given limbo transaction or all limbo transactions.</dd>
<dt><code>-sq</code> <i>number</i></dt>
<dd>
</dd><dt><code>-sql_dialect</code> <i>number</i></dt>
<dd> Change the <font SIZE="-1">SQL</font> dialect of the database.</dd>
<dt><code>-sw</code></dt>
<dd>
</dd><dt><code>-sweep</code></dt>
<dd> Perform immediate garbage collection on the database.</dd>
<dt><code>-sh</code> [<i>mode</i>] <i>option</i> <i>timeout</i></dt>
<dd>
</dd><dt><code>-shutdown</code> [<i>mode</i>] <i>option</i> <i>timeout</i></dt>
<dd> Shuts the database down. <i>mode</i> is either of</dd>
<dl>
<dl>
<dt><code>multi</code></dt>
<dd> Multiple connections from <font SIZE="-1">SYSDBA</font> and the database owner are allowed. Ordinary osers are denied any requests to the database. This is the default <i>mode</i>.</dd>
<dt><code>single</code></dt>
<dd> Only a single connection from <font SIZE="-1">SYSDBA</font> or the database owner is allowed.</dd>
<dt><code>full</code></dt>
<dd> No connections to the database are allowed.</dd>
<dt><code>-ca</code></dt>
<dd>
</dd><dt><code>-cache</code></dt>
<dd> Ignored. Equivalent to -multi.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> <i>option</i> is either of</p>
</dd><dl>
<dt><code>-at</code></dt>
<dd>
</dd><dt><code>-attach</code></dt>
<dd> Prevents new attachments (connections). Active connections continue to work.</dd>
<dt><code>-tra</code></dt>
<dd>
</dd><dt><code>-transaction</code></dt>
<dd> Prevents new transactions. Open transactions continue to work.</dd>
<dt><code>-fo</code></dt>
<dd>
</dd><dt><code>-force_shutdown</code></dt>
<dd> Force immediate database shutdown. All running statements, transactions and connections are aborted.</dd></dl>
</dl>
<dl>
</dl>
<dt><code>-tw</code></dt>
<dd>
</dd><dt><code>-two_phase</code></dt>
<dd> Perform two-phase recovery of limbo transactions.</dd>
<dt><code>-u</code> <i>mode</i></dt>
<dd>
</dd><dt><code>-use</code> <i>mode</i></dt>
<dd> Set the page allocation preference. When <i>mode</i> is <tt>&quot;reserve&quot;</tt> a certain amount of the page is kept aside for record versions. When <i>mode</i> is <tt>&quot;full&quot;</tt> database pages are used fully without such reservarions. </dd>
<p> Corresponds to the <code>-use_all</code> option of <code><a href="/docs/linux/man/1-gbak/">gbak</a></code>(1).</p>
<dt><code>-w</code> <i>mode</i></dt>
<dd>
</dd><dt><code>-write</code> <i>mode</i></dt>
<dd> Sets the synchronous writes flag. <tt>&quot;sync&quot;</tt> sets the synchronous mode flag (also known as <tt>&quot;forced writes&quot;</tt>). <tt>&quot;async&quot;</tt> clears the flag. </dd>
<p> When the flag is on, all writes to the database are synchronised via a call to the operating system to ensure that the data has reached stable storage.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-fe</code> <i>file</i></dt>
<dd>
</dd><dt><code>-fetch_password</code> <i>file</i></dt>
<dd> Read password from <i>file</i>.</dd>
<dt><code>-pas</code> <i>string</i></dt>
<dd>
</dd><dt><code>-password</code> <i>string</i></dt>
<dd> Password for the connection.</dd>
<dt><code>-ro</code> <i>string</i></dt>
<dd>
</dd><dt><code>-role</code> <i>string</i></dt>
<dd> Use supplied <font SIZE="-1">SQL</font> role for the connection.</dd>
<dt><code>-user</code> <i>string</i></dt>
<dd> Use supplied user name for the connection.</dd>
<dt><code>-z</code></dt>
<dd> Prints the <code>gfix</code> version number before anything else.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>ISC_USER</code></font></dt>
<dd> Default value for the -user option.</dd>
<dt><font SIZE="-1"><code>ISC_ROLE</code></font></dt>
<dd> Default value for the -role option.</dd>
<dt><font SIZE="-1"><code>ISC_PASSWORD</code></font></dt>
<dd> Default value for the -password option.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fbstat/">fbstat</a></code>(1). </p>
<p> Additional documentation about Firebird can be found on the Firebird Project website, &lt;<a rel="nofollow" href="http://www.firebirdsql.org">http://www.firebirdsql.org</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Damyan Ivanov dmn [at] debian.org for the Debian project. Permission is granted to use this document, with or without modifications, provided that this notice is retained. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return. </p>
