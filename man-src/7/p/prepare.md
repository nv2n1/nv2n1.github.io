---
title: "prepare(7)"
name: "prepare"
section: "7"
letter: "p"
url: "/docs/linux/man/7-prepare/"
description: "PREPARE – prepare a statement for execution"
---

<p>PREPARE &#8211; prepare a statement for execution </p>
<h2>Synopsis</h2>
<pre>PREPARE <i>name</i> [ ( <i>datatype</i> [, ...] ) ] AS <i>statement</i></pre>
<h2>Description</h2>
<p><code>PREPARE</code> creates a prepared statement. A prepared statement is a server-side object that can be used to optimize performance. When the <code>PREPARE</code> statement is executed, the specified statement is parsed, rewritten, and planned. When an <code>EXECUTE</code> command is subsequently issued, the prepared statement need only be executed. Thus, the parsing, rewriting, and planning stages are only performed once, instead of every time the statement is executed. </p>
<p> Prepared statements can take parameters: values that are substituted into the statement when it is executed. When creating the prepared statement, refer to parameters by position, using $1, $2, etc. A corresponding list of parameter data types can optionally be specified. When a parameter&#8217;s data type is not specified or is declared as unknown, the type is inferred from the context in which the parameter is used (if possible). When executing the statement, specify the actual values for these parameters in the <code>EXECUTE</code> statement. Refer to EXECUTE [<code><a href="/docs/linux/man/7-execute/">execute</a></code>(7)] for more information about that. </p>
<p> Prepared statements only last for the duration of the current database session. When the session ends, the prepared statement is forgotten, so it must be recreated before being used again. This also means that a single prepared statement cannot be used by multiple simultaneous database clients; however, each client can create their own prepared statement to use. The prepared statement can be manually cleaned up using the DEALLOCATE [<code><a href="/docs/linux/man/7-deallocate/">deallocate</a></code>(7)] command. </p>
<p> Prepared statements have the largest performance advantage when a single session is being used to execute a large number of similar statements. The performance difference will be particularly significant if the statements are complex to plan or rewrite, for example, if the query involves a join of many tables or requires the application of several rules. If the statement is relatively simple to plan and rewrite but relatively expensive to execute, the performance advantage of prepared statements will be less noticeable.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>An arbitrary name given to this particular prepared statement. It must be unique within a single session and is subsequently used to execute or deallocate a previously prepared statement.</p>
<dt><i>datatype</i></p>
<dd>The data type of a parameter to the prepared statement. If the data type of a particular parameter is unspecified or is specified as unknown, it will be inferred from the context in which the parameter is used. To refer to the parameters in the prepared statement itself, use $1, $2, etc.</p>
<dt><i>statement</i></p>
<dd>Any <code>SELECT</code>, <code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>, or <code>VALUES</code> statement.</dl>
<h2>Notes</h2>
<p>In some situations, the query plan produced for a prepared statement will be inferior to the query plan that would have been chosen if the statement had been submitted and executed normally. This is because when the statement is planned and the planner attempts to determine the optimal query plan, the actual values of any parameters specified in the statement are unavailable. PostgreSQL collects statistics on the distribution of data in the table, and can use constant values in a statement to make guesses about the likely result of executing the statement. Since this data is unavailable when planning prepared statements with parameters, the chosen plan might be suboptimal. To examine the query plan PostgreSQL has chosen for a prepared statement, use EXPLAIN [<code><a href="/docs/linux/man/7-explain/">explain</a></code>(7)]. </p>
<p> For more information on query planning and the statistics collected by PostgreSQL for that purpose, see the ANALYZE [<code><a href="/docs/linux/man/7-analyze/">analyze</a></code>(7)] documentation. </p>
<p> You can see all available prepared statements of a session by querying the <code>pg_prepared_statements</code> system view.</p>
<h2>Examples</h2>
<p>Create a prepared statement for an <code>INSERT</code> statement, and then execute it: </p>
<pre>PREPARE fooplan (int, text, bool, numeric) AS
 INSERT INTO foo VALUES($1, $2, $3, $4);
EXECUTE fooplan(1, 'Hunter Valley', 't', 200.00);</pre>
<p>Create a prepared statement for a <code>SELECT</code> statement, and then execute it: </p>
<pre>PREPARE usrrptplan (int) AS
 SELECT * FROM users u, logs l WHERE u.usrid=$1 AND u.usrid=l.usrid
 AND l.date = $2;
EXECUTE usrrptplan(1, current_date);</pre>
<p>Note that the data type of the second parameter is not specified, so it is inferred from the context in which $2 is used.</p>
<h2>Compatibility</h2>
<p>The SQL standard includes a <code>PREPARE</code> statement, but it is only for use in embedded SQL. This version of the <code>PREPARE</code> statement also uses a somewhat different syntax.</p>
<h2>See Also</h2>
<p>DEALLOCATE [<code><a href="/docs/linux/man/7-deallocate/">deallocate</a></code>(7)], EXECUTE [<code><a href="/docs/linux/man/7-execute/">execute</a></code>(7)] </p>
