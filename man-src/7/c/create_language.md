---
title: "create_language(7)"
name: "create_language"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_language/"
description: "CREATE LANGUAGE – define a new procedural language"
---

<p>CREATE LANGUAGE &#8211; define a new procedural language </p>
<h2>Synopsis</h2>
<pre>CREATE [ PROCEDURAL ] LANGUAGE <i>name</i>
CREATE [ TRUSTED ] [ PROCEDURAL ] LANGUAGE <i>name</i>
 HANDLER <i>call_handler</i> [ VALIDATOR <i>valfunction</i> ]</pre>
<h2>Description</h2>
<p>Using <code>CREATE LANGUAGE</code>, a PostgreSQL user can register a new procedural language with a PostgreSQL database. Subsequently, functions and trigger procedures can be defined in this new language. </p>
<p> <code>CREATE LANGUAGE</code> effectively associates the language name with a call handler that is responsible for executing functions written in the language. Refer to in the documentation for more information about language call handlers. </p>
<p> There are two forms of the <code>CREATE LANGUAGE</code> command. In the first form, the user supplies just the name of the desired language, and the PostgreSQL server consults the <code>pg_pltemplate</code> system catalog to determine the correct parameters. In the second form, the user supplies the language parameters along with the language name. The second form can be used to create a language that is not defined in <code>pg_pltemplate</code>, but this approach is considered obsolescent. </p>
<p> When the server finds an entry in the <code>pg_pltemplate</code> catalog for the given language name, it will use the catalog data even if the command includes language parameters. This behavior simplifies loading of old dump files, which are likely to contain out-of-date information about language support functions. </p>
<p> Ordinarily, the user must have the PostgreSQL superuser privilege to register a new language. However, the owner of a database can register a new language within that database if the language is listed in the <code>pg_pltemplate</code> catalog and is marked as allowed to be created by database owners (<code>tmpldbacreate</code> is true). The default is that trusted languages can be created by database owners, but this can be adjusted by superusers by modifying the contents of <code>pg_pltemplate</code>. The creator of a language becomes its owner and can later drop it, rename it, or assign it to a new owner.</p>
<h2>Parameters</h2>
<dl>
<dt><code>TRUSTED</code></p>
<dd>TRUSTED specifies that the call handler for the language is safe, that is, it does not offer an unprivileged user any functionality to bypass access restrictions. If this key word is omitted when registering the language, only users with the PostgreSQL superuser privilege can use this language to create new functions.</p>
<dt><code>PROCEDURAL</code></p>
<dd>This is a noise word.</p>
<dt><i>name</i></p>
<dd>The name of the new procedural language. The language name is case insensitive. The name must be unique among the languages in the database. </p>
<p> For backward compatibility, the name can be enclosed by single quotes.</p>
<dt><code>HANDLER </code><i>call_handler</i></p>
<dd><i>call_handler</i> is the name of a previously registered function that will be called to execute the procedural language functions. The call handler for a procedural language must be written in a compiled language such as C with version 1 call convention and registered with PostgreSQL as a function taking no arguments and returning the <code>language_handler</code> type, a placeholder type that is simply used to identify the function as a call handler.</p>
<dt><code>VALIDATOR </code><i>valfunction</i></p>
<dd><i>valfunction</i> is the name of a previously registered function that will be called when a new function in the language is created, to validate the new function. If no validator function is specified, then a new function will not be checked when it is created. The validator function must take one argument of type <code>oid</code>, which will be the OID of the to-be-created function, and will typically return <code>void</code>. </p>
<p> A validator function would typically inspect the function body for syntactical correctness, but it can also look at other properties of the function, for example if the language cannot handle certain argument types. To signal an error, the validator function should use the <code>ereport()</code> function. The return value of the function is ignored.</dl>
<p> The TRUSTED option and the support function name(s) are ignored if the server has an entry for the specified language name in <code>pg_pltemplate</code>.</p>
<h2>Notes</h2>
<p>The <code><a href="/docs/linux/man/1-createlang/">createlang</a></code>(1) program is a simple wrapper around the <code>CREATE LANGUAGE</code> command. It eases installation of procedural languages from the shell command line. </p>
<p> Use DROP LANGUAGE [<code><a href="/docs/linux/man/7-drop_language/">drop_language</a></code>(7)], or better yet the <code><a href="/docs/linux/man/1-droplang/">droplang</a></code>(1) program, to drop procedural languages. </p>
<p> The system catalog <code>pg_language</code> (see in the documentation) records information about the currently installed languages. Also, <code>createlang</code> has an option to list the installed languages. </p>
<p> To create functions in a procedural language, a user must have the USAGE privilege for the language. By default, USAGE is granted to PUBLIC (i.e., everyone) for trusted languages. This can be revoked if desired. </p>
<p> Procedural languages are local to individual databases. However, a language can be installed into the template1 database, which will cause it to be available automatically in all subsequently-created databases. </p>
<p> The call handler function and the validator function (if any) must already exist if the server does not have an entry for the language in <code>pg_pltemplate</code>. But when there is an entry, the functions need not already exist; they will be automatically defined if not present in the database. (This might result in <code>CREATE LANGUAGE</code> failing, if the shared library that implements the language is not available in the installation.) </p>
<p> In PostgreSQL versions before 7.3, it was necessary to declare handler functions as returning the placeholder type <code>opaque</code>, rather than <code>language_handler</code>. To support loading of old dump files, <code>CREATE LANGUAGE</code> will accept a function declared as returning <code>opaque</code>, but it will issue a notice and change the function&#8217;s declared return type to <code>language_handler</code>.</p>
<h2>Examples</h2>
<p>The preferred way of creating any of the standard procedural languages is just: </p>
<pre>CREATE LANGUAGE plpgsql;</pre>
<p>For a language not known in the <code>pg_pltemplate</code> catalog, a sequence such as this is needed: </p>
<pre>CREATE FUNCTION plsample_call_handler() RETURNS language_handler
 AS '$libdir/plsample'
 LANGUAGE C;
CREATE LANGUAGE plsample
 HANDLER plsample_call_handler;</pre>
<h2>Compatibility</h2>
<p><code>CREATE LANGUAGE</code> is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>ALTER LANGUAGE [<code><a href="/docs/linux/man/7-alter_language/">alter_language</a></code>(7)], CREATE FUNCTION [<code><a href="/docs/linux/man/7-create_function/">create_function</a></code>(7)], DROP LANGUAGE [<code><a href="/docs/linux/man/7-drop_language/">drop_language</a></code>(7)], GRANT [<code><a href="/docs/linux/man/7-grant/">grant</a></code>(7)], REVOKE [<code><a href="/docs/linux/man/7-revoke/">revoke</a></code>(7)], createlang [<code><a href="/docs/linux/man/1-createlang/">createlang</a></code>(1)], droplang [<code><a href="/docs/linux/man/1-droplang/">droplang</a></code>(1)] </p>
