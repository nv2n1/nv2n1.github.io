---
title: "alter_type(7)"
name: "alter_type"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_type/"
---

ALTER TYPE - change the definition of a type 

<h2>Synopsis</h2>

<pre>ALTER TYPE <i>name</i> RENAME TO <i>new_name</i>
ALTER TYPE <i>name</i> OWNER TO <i>new_owner</i> 
ALTER TYPE <i>name</i> SET SCHEMA <i>new_schema</i></pre>

<h2>Description</h2>

<b>ALTER TYPE</b> changes the definition of an existing type. 

 You must own the type to use <b>ALTER TYPE</b>. To change the schema of a type, you must also have CREATE privilege on the new schema. To alter the owner, you must also be a direct or indirect member of the new owning role, and that role must have CREATE privilege on the type's schema. (These restrictions enforce that altering the owner doesn't do anything you couldn't do by dropping and recreating the type. However, a superuser can alter ownership of any type anyway.)

<h2>Parameters</h2>

<dl><dt><i>name</i>
<dd>The name (possibly schema-qualified) of an existing type to alter.
<dt><i>new_name</i>
<dd>The new name for the type.
<dt><i>new_owner</i>
<dd>The user name of the new owner of the type.
<dt><i>new_schema</i>
<dd>The new schema for the type.</dl>

<h2>Examples</h2>

To rename a data type: 

 <pre>ALTER TYPE electronic_mail RENAME TO email;</pre>To change the owner of the type email to joe: 

 <pre>ALTER TYPE email OWNER TO joe;</pre>To change the schema of the type email to customers: 

 <pre>ALTER TYPE email SET SCHEMA customers;</pre>

<h2>Compatibility</h2>

There is no <b>ALTER TYPE</b> statement in the SQL standard.
