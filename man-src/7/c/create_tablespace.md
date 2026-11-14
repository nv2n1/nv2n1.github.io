---
title: "create_tablespace(7)"
name: "create_tablespace"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_tablespace/"
description: "CREATE TABLESPACE – define a new tablespace"
---

<p>CREATE TABLESPACE &#8211; define a new tablespace </p>
<h2>Synopsis</h2>
<pre>CREATE TABLESPACE <i>tablespacename</i> [ OWNER <i>username</i> ] LOCATION '<i>directory</i>'</pre>
<h2>Description</h2>
<p><code>CREATE TABLESPACE</code> registers a new cluster-wide tablespace. The tablespace name must be distinct from the name of any existing tablespace in the database cluster. </p>
<p> A tablespace allows superusers to define an alternative location on the file system where the data files containing database objects (such as tables and indexes) can reside. </p>
<p> A user with appropriate privileges can pass <i>tablespacename</i> to <code>CREATE DATABASE</code>, <code>CREATE TABLE</code>, <code>CREATE INDEX</code> or <code>ADD CONSTRAINT</code> to have the data files for these objects stored within the specified tablespace.</p>
<h2>Parameters</h2>
<dl>
<dt><i>tablespacename</i></p>
<dd>The name of a tablespace to be created. The name cannot begin with pg_, as such names are reserved for system tablespaces.</p>
<dt><i>username</i></p>
<dd>The name of the user who will own the tablespace. If omitted, defaults to the user executing the command. Only superusers can create tablespaces, but they can assign ownership of tablespaces to non-superusers.</p>
<dt><i>directory</i></p>
<dd>The directory that will be used for the tablespace. The directory must be empty and must be owned by the PostgreSQL system user. The directory must be specified by an absolute path name.</dl>
<h2>Notes</h2>
<p>Tablespaces are only supported on systems that support symbolic links. </p>
<p> <code>CREATE TABLESPACE</code> cannot be executed inside a transaction block.</p>
<h2>Examples</h2>
<p>Create a tablespace dbspace at /data/dbs: </p>
<pre>CREATE TABLESPACE dbspace LOCATION '/data/dbs';</pre>
<p>Create a tablespace indexspace at /data/indexes owned by user genevieve: </p>
<pre>CREATE TABLESPACE indexspace OWNER genevieve LOCATION '/data/indexes';</pre>
<h2>Compatibility</h2>
<p><code>CREATE TABLESPACE</code> is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>CREATE DATABASE [<code><a href="/docs/linux/man/7-create_database/">create_database</a></code>(7)], CREATE TABLE [<code><a href="/docs/linux/man/7-create_table/">create_table</a></code>(7)], CREATE INDEX [<code><a href="/docs/linux/man/7-create_index/">create_index</a></code>(7)], DROP TABLESPACE [<code><a href="/docs/linux/man/7-drop_tablespace/">drop_tablespace</a></code>(7)], ALTER TABLESPACE [<code><a href="/docs/linux/man/7-alter_tablespace/">alter_tablespace</a></code>(7)] </p>
