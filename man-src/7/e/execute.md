---
title: "execute(7)"
name: "execute"
section: "7"
letter: "e"
url: "/docs/linux/man/7-execute/"
description: "EXECUTE – execute a prepared statement"
---

<p>EXECUTE &#8211; execute a prepared statement </p>
<h2>Synopsis</h2>
<pre>EXECUTE <i>name</i> [ ( <i>parameter</i> [, ...] ) ]</pre>
<h2>Description</h2>
<p><code>EXECUTE</code> is used to execute a previously prepared statement. Since prepared statements only exist for the duration of a session, the prepared statement must have been created by a <code>PREPARE</code> statement executed earlier in the current session. </p>
<p> If the <code>PREPARE</code> statement that created the statement specified some parameters, a compatible set of parameters must be passed to the <code>EXECUTE</code> statement, or else an error is raised. Note that (unlike functions) prepared statements are not overloaded based on the type or number of their parameters; the name of a prepared statement must be unique within a database session. </p>
<p> For more information on the creation and usage of prepared statements, see PREPARE [<code><a href="/docs/linux/man/7-prepare/">prepare</a></code>(7)].</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of the prepared statement to execute.</p>
<dt><i>parameter</i></p>
<dd>The actual value of a parameter to the prepared statement. This must be an expression yielding a value that is compatible with the data type of this parameter, as was determined when the prepared statement was created.</dl>
<h2>Outputs</h2>
<p>The command tag returned by <code>EXECUTE</code> is that of the prepared statement, and not EXECUTE.</p>
<h2>Examples</h2>
<p>Examples are given in the Examples [<code><a href="/docs/linux/man/7-prepare/">prepare</a></code>(7)] section of the PREPARE [<code><a href="/docs/linux/man/7-prepare/">prepare</a></code>(7)] documentation.</p>
<h2>Compatibility</h2>
<p>The SQL standard includes an <code>EXECUTE</code> statement, but it is only for use in embedded SQL. This version of the <code>EXECUTE</code> statement also uses a somewhat different syntax.</p>
<h2>See Also</h2>
<p>DEALLOCATE [<code><a href="/docs/linux/man/7-deallocate/">deallocate</a></code>(7)], PREPARE [<code><a href="/docs/linux/man/7-prepare/">prepare</a></code>(7)] </p>
