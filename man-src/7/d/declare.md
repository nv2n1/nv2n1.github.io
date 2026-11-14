---
title: "declare(7)"
name: "declare"
section: "7"
letter: "d"
url: "/docs/linux/man/7-declare/"
description: "DECLARE – define a cursor"
---

<p>DECLARE &#8211; define a cursor </p>
<h2>Synopsis</h2>
<pre>DECLARE <i>name</i> [ BINARY ] [ INSENSITIVE ] [ [ NO ] SCROLL ]
 CURSOR [ { WITH | WITHOUT } HOLD ] FOR <i>query</i></pre>
<h2>Description</h2>
<p><code>DECLARE</code> allows a user to create cursors, which can be used to retrieve a small number of rows at a time out of a larger query. After the cursor is created, rows are fetched from it using FETCH [<code><a href="/docs/linux/man/7-fetch/">fetch</a></code>(7)].</p>
<dl>
<dd><code>Note:</code> This page describes usage of cursors at the SQL command level. If you are trying to use cursors inside a <code>PL/pgSQL</code> function, the rules are different &#8212; see in the documentation.</dl>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of the cursor to be created.</p>
<dt><code>BINARY</code></p>
<dd>Causes the cursor to return data in binary rather than in text format.</p>
<dt><code>INSENSITIVE</code></p>
<dd>Indicates that data retrieved from the cursor should be unaffected by updates to the table(s) underlying the cursor that occur after the cursor is created. In PostgreSQL, this is the default behavior; so this key word has no effect and is only accepted for compatibility with the SQL standard.</p>
<dt><code>SCROLL</code></p>
<dd>
<dt><code>NO SCROLL</code></p>
<dd>SCROLL specifies that the cursor can be used to retrieve rows in a nonsequential fashion (e.g., backward). Depending upon the complexity of the query&#8217;s execution plan, specifying SCROLL might impose a performance penalty on the query&#8217;s execution time. NO SCROLL specifies that the cursor cannot be used to retrieve rows in a nonsequential fashion. The default is to allow scrolling in some cases; this is not the same as specifying SCROLL. See Notes [<code><a href="/docs/linux/man/7-declare/">declare</a></code>(7)] for details.</p>
<dt><code>WITH HOLD</code></p>
<dd>
<dt><code>WITHOUT HOLD</code></p>
<dd>WITH HOLD specifies that the cursor can continue to be used after the transaction that created it successfully commits. WITHOUT HOLD specifies that the cursor cannot be used outside of the transaction that created it. If neither WITHOUT HOLD nor WITH HOLD is specified, WITHOUT HOLD is the default.</p>
<dt><i>query</i></p>
<dd>A SELECT [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] or VALUES [<code><a href="/docs/linux/man/7-values/">values</a></code>(7)] command which will provide the rows to be returned by the cursor.</dl>
<p> The key words BINARY, INSENSITIVE, and SCROLL can appear in any order.</p>
<h2>Notes</h2>
<p>Normal cursors return data in text format, the same as a <code>SELECT</code> would produce. The BINARY option specifies that the cursor should return data in binary format. This reduces conversion effort for both the server and client, at the cost of more programmer effort to deal with platform-dependent binary data formats. As an example, if a query returns a value of one from an integer column, you would get a string of 1 with a default cursor, whereas with a binary cursor you would get a 4-byte field containing the internal representation of the value (in big-endian byte order). </p>
<p> Binary cursors should be used carefully. Many applications, including <code>psql</code>, are not prepared to handle binary cursors and expect data to come back in the text format. </p>
<dl>
<dd><code>Note:</code> When the client application uses the &#8220;extended query&#8221; protocol to issue a <code>FETCH</code> command, the Bind protocol message specifies whether data is to be retrieved in text or binary format. This choice overrides the way that the cursor is defined. The concept of a binary cursor as such is thus obsolete when using extended query protocol &#8212; any cursor can be treated as either text or binary.</dl>
<p> Unless WITH HOLD is specified, the cursor created by this command can only be used within the current transaction. Thus, <code>DECLARE</code> without WITH HOLD is useless outside a transaction block: the cursor would survive only to the completion of the statement. Therefore PostgreSQL reports an error if such a command is used outside a transaction block. Use BEGIN [<code><a href="/docs/linux/man/7-begin/">begin</a></code>(7)] and COMMIT [<code><a href="/docs/linux/man/7-commit/">commit</a></code>(7)] (or ROLLBACK [<code><a href="/docs/linux/man/7-rollback/">rollback</a></code>(7)]) to define a transaction block. </p>
<p> If WITH HOLD is specified and the transaction that created the cursor successfully commits, the cursor can continue to be accessed by subsequent transactions in the same session. (But if the creating transaction is aborted, the cursor is removed.) A cursor created with WITH HOLD is closed when an explicit <code>CLOSE</code> command is issued on it, or the session ends. In the current implementation, the rows represented by a held cursor are copied into a temporary file or memory area so that they remain available for subsequent transactions. </p>
<p> WITH HOLD may not be specified when the query includes FOR UPDATE or FOR SHARE. </p>
<p> The SCROLL option should be specified when defining a cursor that will be used to fetch backwards. This is required by the SQL standard. However, for compatibility with earlier versions, PostgreSQL will allow backward fetches without SCROLL, if the cursor&#8217;s query plan is simple enough that no extra overhead is needed to support it. However, application developers are advised not to rely on using backward fetches from a cursor that has not been created with SCROLL. If NO SCROLL is specified, then backward fetches are disallowed in any case. </p>
<p> Backward fetches are also disallowed when the query includes FOR UPDATE or FOR SHARE; therefore SCROLL may not be specified in this case. </p>
<dl>
<dd><code>Caution:</code> Scrollable and WITH HOLD cursors may give unexpected results if they invoke any volatile functions (see in the documentation). When a previously fetched row is re-fetched, the functions might be re-executed, perhaps leading to results different from the first time. One workaround for such cases is to declare the cursor WITH HOLD and commit the transaction before reading any rows from it. This will force the entire output of the cursor to be materialized in temporary storage, so that volatile functions are executed exactly once for each row.</dl>
<p> If the cursor&#8217;s query includes FOR UPDATE or FOR SHARE, then returned rows are locked at the time they are first fetched, in the same way as for a regular SELECT [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] command with these options. In addition, the returned rows will be the most up-to-date versions; therefore these options provide the equivalent of what the SQL standard calls a &#8220;sensitive cursor&#8221;. (Specifying INSENSITIVE together with FOR UPDATE or FOR SHARE is an error.) </p>
<dl>
<dd><code>Caution:</code> </p>
<p> It is generally recommended to use FOR UPDATE if the cursor is intended to be used with <code>UPDATE &#8230; WHERE CURRENT OF</code> or <code>DELETE &#8230; WHERE CURRENT OF</code>. Using FOR UPDATE prevents other sessions from changing the rows between the time they are fetched and the time they are updated. Without FOR UPDATE, a subsequent WHERE CURRENT OF command will have no effect if the row was changed since the cursor was created. </p>
<p> Another reason to use FOR UPDATE is that without it, a subsequent WHERE CURRENT OF might fail if the cursor query does not meet the SQL standard&#8217;s rules for being &#8220;simply updatable&#8221; (in particular, the cursor must reference just one table and not use grouping or ORDER BY). Cursors that are not simply updatable might work, or might not, depending on plan choice details; so in the worst case, an application might work in testing and then fail in production. </p>
<p> The main reason not to use FOR UPDATE with WHERE CURRENT OF is if you need the cursor to be scrollable, or to be insensitive to the subsequent updates (that is, continue to show the old data). If this is a requirement, pay close heed to the caveats shown above.</dl>
<p> The SQL standard only makes provisions for cursors in embedded SQL. The PostgreSQL server does not implement an <code>OPEN</code> statement for cursors; a cursor is considered to be open when it is declared. However, <code>ECPG</code>, the embedded SQL preprocessor for PostgreSQL, supports the standard SQL cursor conventions, including those involving <code>DECLARE</code> and <code>OPEN</code> statements. </p>
<p> You can see all available cursors by querying the <code>pg_cursors</code> system view.</p>
<h2>Examples</h2>
<p>To declare a cursor: </p>
<pre>DECLARE liahona CURSOR FOR SELECT * FROM films;</pre>
<p>See FETCH [<code><a href="/docs/linux/man/7-fetch/">fetch</a></code>(7)] for more examples of cursor usage.</p>
<h2>Compatibility</h2>
<p>The SQL standard says that it is implementation-dependent whether cursors are sensitive to concurrent updates of the underlying data by default. In PostgreSQL, cursors are insensitive by default, and can be made sensitive by specifying FOR UPDATE. Other products may work differently. </p>
<p> The SQL standard allows cursors only in embedded SQL and in modules. PostgreSQL permits cursors to be used interactively. </p>
<p> Binary cursors are a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>CLOSE [<code><a href="/docs/linux/man/7-close/">close</a></code>(7)], FETCH [<code><a href="/docs/linux/man/7-fetch/">fetch</a></code>(7)], MOVE [<code><a href="/docs/linux/man/7-move/">move</a></code>(7)] </p>
