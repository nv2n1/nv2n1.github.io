---
title: "gfix(1)"
name: "gfix"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfix/"
description: "gfix — miscelenous Firebird database maintenance"
---

<h2 class="name">NAME</h2>
<p> gfix &#8212; miscelenous Firebird database maintenance </p>
<h2>SYNOPSIS</h2>
<p> <code>gfix</code> <i>command</i> [<i>option</i>&#8230;] <i>database</i></p>
<h2>DESCRIPTION</h2>
<p> <code>gfix</code> is a program that allows the Firebird administrator or database owner to perform various maintenance tasks.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>-ac</code></p>
<dd>
<dt><code>-activate_shadow</code></p>
<dd> Activate database shadow file.</p>
<dt><code>-b</code> <i>number</i></p>
<dd>
<dt><code>-buffers</code> <i>number</i></p>
<dd> Set database buffer size, in pages.</p>
<dt><code>-co</code> <i>number</i>|&quot;all&quot;</p>
<dd>
<dt><code>-commit</code> <i>number</i>|&quot;all&quot;</p>
<dd> Commit a limbo transaction with a given number or all limbo transactions.</p>
<dt><code>-h</code> <i>number</i></p>
<dd>
<dt><code>-housekeeping</code> <i>number</i></p>
<dd> Set the housekeeping interval. When the difference between the oldest interesting transaction and the current transaction exceeds <i>number</i>, an automatic garbage collection (sweep) process is started to make possible increasing of the oldest interesting transaction number. </p>
<p> When <i>number</i> is <tt>0</tt>, there is no automatic sweep and <font SIZE="-1">OIT</font> advancement should be arranged by other means, e.g. <code>gfix -sweep</code> via <code><a href="/docs/linux/man/1-cron/">cron</a></code>(1).</p>
<dt><code>-icu</code></p>
<dd> Fix the database to be usable with the available <font SIZE="-1">ICU</font> version. </p>
<p> Some collations in Firebird are bound the the version of the <font SIZE="-1">ICU</font> library. When such a collation needs to be used in an environment with a different version of <font SIZE="-1">ICU,</font> an error occurs. <code>gfix -icu</code> is the remedy.</p>
<dt><code>-k</code></p>
<dd>
<dt><code>-kill_shadow</code></p>
<dd> Kill unavailable database shadow files.</p>
<dt><code>-l</code></p>
<dd>
<dt><code>-list</code></p>
<dd> List limbo transactions.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-pr</code></p>
<dd>
<dt><code>-prompt</code></p>
<dd> Prompt for commit/rollback for each transaction in limbo.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-me</code></p>
<dd>
<dt><code>-mend</code></p>
<dd> Prepare corrupt database for backup.</p>
<dt><code>-mo</code> <i>access</i></p>
<dd>
<dt><code>-mode</code> <i>access</i></p>
<dd> Set database access mode. Possibla values are <tt>&quot;read_only&quot;</tt> and <tt>&quot;read_write&quot;</tt>.</p>
<dt><code>-nol</code></p>
<dd>
<dt><code>-nolinger</code></p>
<dd> Temporary remove linger setting of the database. </p>
<p> Similar to the following <font SIZE="-1">SQL</font> statement: </p>
<pre>
 alter database drop linger;
</pre>
<p> but the next attachment to the database will restore the linger setting. </p>
<p> See <i>sql.extensions/README.linger</i>.</p>
<dt><code>-o</code> [<i>mode</i>]</p>
<dd>
<dt><code>-online</code> [<i>mode</i>]</p>
<dd> Brings the database online. The reverse of <code>-shut</code>. </p>
<p> <i>mode</i> can be:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>normal</code></p>
<dd> This is the default. Brings the database fully online, all normal connections are permitted.</p>
<dt><code>multi</code></p>
<dd> Permits multiple connections from <font SIZE="-1">SYSDBA</font> and the database owner.</p>
<dt><code>single</code></p>
<dd> Permins only one connection from <font SIZE="-1">SYSDBA</font> or the database owner.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-v</code></p>
<dd>
<dt><code>-validate</code></p>
<dd> Perform database validation. </p>
<p> Validation options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-fu</code></p>
<dd>
<dt><code>-full</code></p>
<dd> Full validation. Record fragments are verified.</p>
<dt><code>-i</code></p>
<dd>
<dt><code>-ignore</code></p>
<dd> Ignore record checksum errors.</p>
<dt><code>-n</code></p>
<dd>
<dt><code>-no_update</code></p>
<dd> Peform read-only validation.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-r</code> <i>number</i>|&quot;all&quot;</p>
<dd>
<dt><code>-rollback</code> <i>number</i>|&quot;all&quot;</p>
<dd> Rollback given limbo transaction or all limbo transactions.</p>
<dt><code>-sq</code> <i>number</i></p>
<dd>
<dt><code>-sql_dialect</code> <i>number</i></p>
<dd> Change the <font SIZE="-1">SQL</font> dialect of the database.</p>
<dt><code>-sw</code></p>
<dd>
<dt><code>-sweep</code></p>
<dd> Perform immediate garbage collection on the database.</p>
<dt><code>-sh</code> [<i>mode</i>] <i>option</i> <i>timeout</i></p>
<dd>
<dt><code>-shutdown</code> [<i>mode</i>] <i>option</i> <i>timeout</i></p>
<dd> Shuts the database down. <i>mode</i> is either of</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>multi</code></p>
<dd> Multiple connections from <font SIZE="-1">SYSDBA</font> and the database owner are allowed. Ordinary osers are denied any requests to the database. This is the default <i>mode</i>.</p>
<dt><code>single</code></p>
<dd> Only a single connection from <font SIZE="-1">SYSDBA</font> or the database owner is allowed.</p>
<dt><code>full</code></p>
<dd> No connections to the database are allowed.</p>
<dt><code>-ca</code></p>
<dd>
<dt><code>-cache</code></p>
<dd> Ignored. Equivalent to -multi.</dl>
</dl>
<dl>
<dt>
<dd>
<p> <i>option</i> is either of</p>
<dl>
<dt><code>-at</code></p>
<dd>
<dt><code>-attach</code></p>
<dd> Prevents new attachments (connections). Active connections continue to work.</p>
<dt><code>-tra</code></p>
<dd>
<dt><code>-transaction</code></p>
<dd> Prevents new transactions. Open transactions continue to work.</p>
<dt><code>-fo</code></p>
<dd>
<dt><code>-force_shutdown</code></p>
<dd> Force immediate database shutdown. All running statements, transactions and connections are aborted.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>-tw</code></p>
<dd>
<dt><code>-two_phase</code></p>
<dd> Perform two-phase recovery of limbo transactions.</p>
<dt><code>-u</code> <i>mode</i></p>
<dd>
<dt><code>-use</code> <i>mode</i></p>
<dd> Set the page allocation preference. When <i>mode</i> is <tt>&quot;reserve&quot;</tt> a certain amount of the page is kept aside for record versions. When <i>mode</i> is <tt>&quot;full&quot;</tt> database pages are used fully without such reservarions. </p>
<p> Corresponds to the <code>-use_all</code> option of <code><a href="/docs/linux/man/1-gbak/">gbak</a></code>(1).</p>
<dt><code>-w</code> <i>mode</i></p>
<dd>
<dt><code>-write</code> <i>mode</i></p>
<dd> Sets the synchronous writes flag. <tt>&quot;sync&quot;</tt> sets the synchronous mode flag (also known as <tt>&quot;forced writes&quot;</tt>). <tt>&quot;async&quot;</tt> clears the flag. </p>
<p> When the flag is on, all writes to the database are synchronised via a call to the operating system to ensure that the data has reached stable storage.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-fe</code> <i>file</i></p>
<dd>
<dt><code>-fetch_password</code> <i>file</i></p>
<dd> Read password from <i>file</i>.</p>
<dt><code>-pas</code> <i>string</i></p>
<dd>
<dt><code>-password</code> <i>string</i></p>
<dd> Password for the connection.</p>
<dt><code>-ro</code> <i>string</i></p>
<dd>
<dt><code>-role</code> <i>string</i></p>
<dd> Use supplied <font SIZE="-1">SQL</font> role for the connection.</p>
<dt><code>-user</code> <i>string</i></p>
<dd> Use supplied user name for the connection.</p>
<dt><code>-z</code></p>
<dd> Prints the <code>gfix</code> version number before anything else.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>ISC_USER</code></font></p>
<dd> Default value for the -user option.</p>
<dt><font SIZE="-1"><code>ISC_ROLE</code></font></p>
<dd> Default value for the -role option.</p>
<dt><font SIZE="-1"><code>ISC_PASSWORD</code></font></p>
<dd> Default value for the -password option.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-fbstat/">fbstat</a></code>(1). </p>
<p> Additional documentation about Firebird can be found on the Firebird Project website, &lt;<a rel="nofollow" href="http://www.firebirdsql.org">http://www.firebirdsql.org</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Damyan Ivanov dmn [at] debian.org for the Debian project. Permission is granted to use this document, with or without modifications, provided that this notice is retained. If we meet some day, and you think this stuff is worth it, you can buy me a beer in return. </p>
<h2>Index</h2>
