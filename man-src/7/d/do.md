---
title: "do(7)"
name: "do"
section: "7"
letter: "d"
url: "/docs/linux/man/7-do/"
description: "DO – execute an anonymous code block"
---

<p>DO &#8211; execute an anonymous code block</p>
<h2>Synopsis</h2>
<pre>DO [ LANGUAGE <i>lang_name</i> ] <i>code</i></pre>
<h2>Description</h2>
<p><code>DO</code> executes an anonymous code block, or in other words a transient anonymous function in a procedural language. </p>
<p> The code block is treated as though it were the body of a function with no parameters, returning void. It is parsed and executed a single time. </p>
<p> The optional LANGUAGE clause can be written either before or after the code block.</p>
<h2>Parameters</h2>
<p><i>code</i></p>
<dl>
<dd>The procedural language code to be executed. This must be specified as a string literal, just as in <code>CREATE FUNCTION</code>. Use of a dollar-quoted literal is recommended.</dl>
<p> <i>lang_name</i></p>
<dl>
<dd>The name of the procedural language the code is written in. If omitted, the default is plpgsql.</dl>
<h2>Notes</h2>
<p>The procedural language to be used must already have been installed into the current database by means of <code>CREATE LANGUAGE</code>. plpgsql is installed by default, but other languages are not. </p>
<p> The user must have USAGE privilege for the procedural language, or must be a superuser if the language is untrusted. This is the same privilege requirement as for creating a function in the language.</p>
<h2>Examples</h2>
<p>Grant all privileges on all views in schema public to role webuser: </p>
<pre><code>DO $$DECLARE r record;
BEGIN
FOR r IN SELECT table_schema, table_name FROM information_schema.tables
WHERE table_type = 'VIEW' AND table_schema = 'public'
LOOP
EXECUTE 'GRANT ALL ON ' || quote_ident(r.table_schema) || '.' || quote_ident(r.table_name) || ' TO webuser';
END LOOP;
END$$;</code></pre>
<h2>Compatibility</h2>
<p>There is no <code>DO</code> statement in the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE LANGUAGE (<code><a href="/docs/linux/man/7-create_language/">CREATE_LANGUAGE</a></code>(7)) </p>
