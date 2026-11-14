---
title: "move(7)"
name: "move"
section: "7"
letter: "m"
url: "/docs/linux/man/7-move/"
description: "MOVE – position a cursor"
---

<p>MOVE &#8211; position a cursor </p>
<h2>Synopsis</h2>
<pre>MOVE [ <i>direction</i> { FROM | IN } ] <i>cursorname</i></pre>
<h2>Description</h2>
<p><code>MOVE</code> repositions a cursor without retrieving any data. <code>MOVE</code> works exactly like the <code>FETCH</code> command, except it only positions the cursor and does not return rows. </p>
<p> The parameters for the <code>MOVE</code> command are identical to those of the <code>FETCH</code> command; refer to FETCH [<code><a href="/docs/linux/man/7-fetch/">fetch</a></code>(7)] for details on syntax and usage.</p>
<h2>Outputs</h2>
<p>On successful completion, a <code>MOVE</code> command returns a command tag of the form </p>
<pre>MOVE <i>count</i></pre>
<p>The <i>count</i> is the number of rows that a <code>FETCH</code> command with the same parameters would have returned (possibly zero).</p>
<h2>Examples</h2>
<pre>BEGIN WORK;
DECLARE liahona CURSOR FOR SELECT * FROM films;
-- Skip the first 5 rows:
MOVE FORWARD 5 IN liahona;
MOVE 5
-- Fetch the 6th row from the cursor liahona:
FETCH 1 FROM liahona;
 code | title | did | date_prod | kind | len
-------+--------+-----+------------+--------+-------
 P_303 | 48 Hrs | 103 | 1982-10-22 | Action | 01:37
(1 row)
-- Close the cursor liahona and end the transaction:
CLOSE liahona;
COMMIT WORK;</pre>
<h2>Compatibility</h2>
<p>There is no <code>MOVE</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CLOSE [<code><a href="/docs/linux/man/7-close/">close</a></code>(7)], DECLARE [<code><a href="/docs/linux/man/7-declare/">declare</a></code>(7)], FETCH [<code><a href="/docs/linux/man/7-fetch/">fetch</a></code>(7)] </p>
