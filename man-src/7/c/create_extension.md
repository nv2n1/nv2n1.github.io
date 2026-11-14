---
title: "create_extension(7)"
name: "create_extension"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_extension/"
description: "CREATE_EXTENSION – install an extension"
---

<p>CREATE_EXTENSION &#8211; install an extension</p>
<h2>Synopsis</h2>
<pre>CREATE EXTENSION [ IF NOT EXISTS ] <i>extension_name</i>
 [ WITH ] [ SCHEMA <i>schema_name</i> ]
 [ VERSION <i>version</i> ]
 [ FROM <i>old_version</i> ]</pre>
<h2>Description</h2>
<p><code>CREATE EXTENSION</code> loads a new extension into the current database. There must not be an extension of the same name already loaded. </p>
<p> Loading an extension essentially amounts to running the extension&#8217;s script file. The script will typically create new SQL objects such as functions, data types, operators and index support methods. <code>CREATE EXTENSION</code> additionally records the identities of all the created objects, so that they can be dropped again if <code>DROP EXTENSION</code> is issued. </p>
<p> Loading an extension requires the same privileges that would be required to create its component objects. For most extensions this means superuser or database owner privileges are needed. The user who runs <code>CREATE EXTENSION</code> becomes the owner of the extension for purposes of later privilege checks, as well as the owner of any objects created by the extension&#8217;s script.</p>
<h2>Parameters</h2>
<p>IF NOT EXISTS</p>
<dl>
<dd>Do not throw an error if an extension with the same name already exists. A notice is issued in this case. Note that there is no guarantee that the existing extension is anything like the one that would have been created from the currently-available script file.</dl>
<p> <i>extension_name</i></p>
<dl>
<dd>The name of the extension to be installed. PostgreSQL will create the extension using details from the file SHAREDIR/extension/<i>extension_name</i>.control.</dl>
<p> <i>schema_name</i></p>
<dl>
<dd>The name of the schema in which to install the extension&#8217;s objects, given that the extension allows its contents to be relocated. The named schema must already exist. If not specified, and the extension&#8217;s control file does not specify a schema either, the current default object creation schema is used. </p>
<p> Remember that the extension itself is not considered to be within any schema: extensions have unqualified names that must be unique database-wide. But objects belonging to the extension can be within schemas.</dl>
<p> <i>version</i></p>
<dl>
<dd>The version of the extension to install. This can be written as either an identifier or a string literal. The default version is whatever is specified in the extension&#8217;s control file.</dl>
<p> <i>old_version</i></p>
<dl>
<dd>FROM<i>old_version</i> must be specified when, and only when, you are attempting to install an extension that replaces an &#8220;old style&#8221; module that is just a collection of objects not packaged into an extension. This option causes <code>CREATE EXTENSION</code> to run an alternative installation script that absorbs the existing objects into the extension, instead of creating new objects. Be careful that SCHEMA specifies the schema containing these pre-existing objects. </p>
<p> The value to use for <i>old_version</i> is determined by the extension&#8217;s author, and might vary if there is more than one version of the old-style module that can be upgraded into an extension. For the standard additional modules supplied with pre-9.1 PostgreSQL, use unpackaged for <i>old_version</i> when updating a module to extension style.</dl>
<h2>Notes</h2>
<p>Before you can use <code>CREATE EXTENSION</code> to load an extension into a database, the extension&#8217;s supporting files must be installed. Information about installing the extensions supplied with PostgreSQL can be found in Additional Supplied Modules. </p>
<p> The extensions currently available for loading can be identified from the pg_available_extensions or pg_available_extension_versions system views. </p>
<p> For information about writing new extensions, see Section 35.15, &#8220;Packaging Related Objects into an Extension&#8221;, in the documentation.</p>
<h2>Examples</h2>
<p>Install the hstore extension into the current database: </p>
<dl>
<dd>
<pre>CREATE EXTENSION hstore;</pre>
</dl>
<p> Update a pre-9.1 installation of hstore into extension style: </p>
<dl>
<dd>
<pre>CREATE EXTENSION hstore SCHEMA public FROM unpackaged;</pre>
</dl>
<p> Be careful to specify the schema in which you installed the existing hstore objects.</p>
<h2>Compatibility</h2>
<p><code>CREATE EXTENSION</code> is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>ALTER EXTENSION (<code><a href="/docs/linux/man/7-alter_extension/">ALTER_EXTENSION</a></code>(7)), DROP EXTENSION (<code><a href="/docs/linux/man/7-drop_extension/">DROP_EXTENSION</a></code>(7)) </p>
