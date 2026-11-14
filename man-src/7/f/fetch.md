---
title: "fetch(7)"
name: "fetch"
section: "7"
letter: "f"
url: "/docs/linux/man/7-fetch/"
description: "FETCH – retrieve rows from a query using a cursor"
---

<p>FETCH &#8211; retrieve rows from a query using a cursor </p>
<h2>Synopsis</h2>
<pre>FETCH [ <i>direction</i> { FROM | IN } ] <i>cursorname</i>
where <i>direction</i> can be empty or one of:
 NEXT
 PRIOR
 FIRST
 LAST
 ABSOLUTE <i>count</i>
 RELATIVE <i>count</i>
 <i>count</i>
 ALL
 FORWARD
 FORWARD <i>count</i>
 FORWARD ALL
 BACKWARD
 BACKWARD <i>count</i>
 BACKWARD ALL</pre>
<h2>Description</h2>
<p><code>FETCH</code> retrieves rows using a previously-created cursor. A cursor has an associated position, which is used by <code>FETCH</code>. The cursor position can be before the first row of the query result, on any particular row of the result, or after the last row of the result. When created, a cursor is positioned before the first row. After fetching some rows, the cursor is positioned on the row most recently retrieved. If <code>FETCH</code> runs off the end of the available rows then the cursor is left positioned after the last row, or before the first row if fetching backward. <code>FETCH ALL</code> or <code>FETCH BACKWARD ALL</code> will always leave the cursor positioned after the last row or before the first row. The forms NEXT, PRIOR, FIRST, LAST, ABSOLUTE, RELATIVE fetch a single row after moving the cursor appropriately. If there is no such row, an empty result is returned, and the cursor is left positioned before the first row or after the last row as appropriate. The forms using FORWARD and BACKWARD retrieve the indicated number of rows moving in the forward or backward direction, leaving the cursor positioned on the last-returned row (or after/before all rows, if the <i>count</i> exceeds the number of rows available). RELATIVE 0, FORWARD 0, and BACKWARD 0 all request fetching the current row without moving the cursor, that is, re-fetching the most recently fetched row. This will succeed unless the cursor is positioned before the first row or after the last row; in which case, no row is returned.</p>
<dl>
<dd><code>Note:</code> This page describes usage of cursors at the SQL command level. If you are trying to use cursors inside a <code>PL/pgSQL</code> function, the rules are different &#8212; see in the documentation.</dl>
<h2>Parameters</h2>
<dl>
<dt><i>direction</i></p>
<dd><i>direction</i> defines the fetch direction and number of rows to fetch. It can be one of the following:</p>
<dl>
<dd>
<dl>
<dt><code>NEXT</code></p>
<dd>Fetch the next row. This is the default if <i>direction</i> is omitted.</p>
<dt><code>PRIOR</code></p>
<dd>Fetch the prior row.</p>
<dt><code>FIRST</code></p>
<dd>Fetch the first row of the query (same as ABSOLUTE 1).</p>
<dt><code>LAST</code></p>
<dd>Fetch the last row of the query (same as ABSOLUTE -1).</p>
<dt><code>ABSOLUTE </code><i>count</i></p>
<dd>Fetch the <i>count</i>&#8216;th row of the query, or the abs(<i>count</i>)&#8217;th row from the end if <i>count</i> is negative. Position before first row or after last row if <i>count</i> is out of range; in particular, ABSOLUTE 0 positions before the first row.</p>
<dt><code>RELATIVE </code><i>count</i></p>
<dd>Fetch the <i>count</i>&#8216;th succeeding row, or the abs(<i>count</i>)&#8217;th prior row if <i>count</i> is negative. RELATIVE 0 re-fetches the current row, if any.</p>
<dt><i>count</i></p>
<dd>Fetch the next <i>count</i> rows (same as FORWARD <i>count</i>).</p>
<dt><code>ALL</code></p>
<dd>Fetch all remaining rows (same as FORWARD ALL).</p>
<dt><code>FORWARD</code></p>
<dd>Fetch the next row (same as NEXT).</p>
<dt><code>FORWARD </code><i>count</i></p>
<dd>Fetch the next <i>count</i> rows. FORWARD 0 re-fetches the current row.</p>
<dt><code>FORWARD ALL</code></p>
<dd>Fetch all remaining rows.</p>
<dt><code>BACKWARD</code></p>
<dd>Fetch the prior row (same as PRIOR).</p>
<dt><code>BACKWARD </code><i>count</i></p>
<dd>Fetch the prior <i>count</i> rows (scanning backwards). BACKWARD 0 re-fetches the current row.</p>
<dt><code>BACKWARD ALL</code></p>
<dd>Fetch all prior rows (scanning backwards).</dl>
</dl>
</dl>
<dl>
<dt><i>count</i></p>
<dd><i>count</i> is a possibly-signed integer constant, determining the location or number of rows to fetch. For FORWARD and BACKWARD cases, specifying a negative <i>count</i> is equivalent to changing the sense of FORWARD and BACKWARD.</p>
<dt><i>cursorname</i></p>
<dd>An open cursor&#8217;s name.</dl>
<h2>Outputs</h2>
<p>On successful completion, a <code>FETCH</code> command returns a command tag of the form </p>
<pre>FETCH <i>count</i></pre>
<p>The <i>count</i> is the number of rows fetched (possibly zero). Note that in <code>psql</code>, the command tag will not actually be displayed, since <code>psql</code> displays the fetched rows instead.</p>
<h2>Notes</h2>
<p>The cursor should be declared with the SCROLL option if one intends to use any variants of <code>FETCH</code> other than <code>FETCH NEXT</code> or <code>FETCH FORWARD</code> with a positive count. For simple queries PostgreSQL will allow backwards fetch from cursors not declared with SCROLL, but this behavior is best not relied on. If the cursor is declared with NO SCROLL, no backward fetches are allowed. </p>
<p> ABSOLUTE fetches are not any faster than navigating to the desired row with a relative move: the underlying implementation must traverse all the intermediate rows anyway. Negative absolute fetches are even worse: the query must be read to the end to find the last row, and then traversed backward from there. However, rewinding to the start of the query (as with FETCH ABSOLUTE 0) is fast. </p>
<p> DECLARE [<code><a href="/docs/linux/man/7-declare/">declare</a></code>(7)] is used to define a cursor. Use MOVE [<code><a href="/docs/linux/man/7-move/">move</a></code>(7)] to change cursor position without retrieving data.</p>
<h2>Examples</h2>
<p>The following example traverses a table using a cursor: </p>
<pre>BEGIN WORK;
-- Set up a cursor:
DECLARE liahona SCROLL CURSOR FOR SELECT * FROM films;
-- Fetch the first 5 rows in the cursor liahona:
FETCH FORWARD 5 FROM liahona;
 code | title | did | date_prod | kind | len
-------+-------------------------+-----+------------+----------+-------
 BL101 | The Third Man | 101 | 1949-12-23 | Drama | 01:44
 BL102 | The African Queen | 101 | 1951-08-11 | Romantic | 01:43
 JL201 | Une Femme est une Femme | 102 | 1961-03-12 | Romantic | 01:25
 P_301 | Vertigo | 103 | 1958-11-14 | Action | 02:08
 P_302 | Becket | 103 | 1964-02-03 | Drama | 02:28
-- Fetch the previous row:
FETCH PRIOR FROM liahona;
 code | title | did | date_prod | kind | len
-------+---------+-----+------------+--------+-------
 P_301 | Vertigo | 103 | 1958-11-14 | Action | 02:08
-- Close the cursor and end the transaction:
CLOSE liahona;
COMMIT WORK;</pre>
<h2>Compatibility</h2>
<p>The SQL standard defines <code>FETCH</code> for use in embedded SQL only. The variant of <code>FETCH</code> described here returns the data as if it were a <code>SELECT</code> result rather than placing it in host variables. Other than this point, <code>FETCH</code> is fully upward-compatible with the SQL standard. </p>
<p> The <code>FETCH</code> forms involving FORWARD and BACKWARD, as well as the forms FETCH <i>count</i> and FETCH ALL, in which FORWARD is implicit, are PostgreSQL extensions. </p>
<p> The SQL standard allows only FROM preceding the cursor name; the option to use IN is an extension.</p>
<h2>See Also</h2>
<p>CLOSE [<code><a href="/docs/linux/man/7-close/">close</a></code>(7)], DECLARE [<code><a href="/docs/linux/man/7-declare/">declare</a></code>(7)], MOVE [<code><a href="/docs/linux/man/7-move/">move</a></code>(7)] </p>
