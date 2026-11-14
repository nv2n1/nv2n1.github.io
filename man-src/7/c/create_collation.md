---
title: "create_collation(7)"
name: "create_collation"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_collation/"
description: "CREATE_COLLATION – define a new collation"
---

<p>CREATE_COLLATION &#8211; define a new collation</p>
<h2>Synopsis</h2>
<pre>CREATE COLLATION <i>name</i> (
 [ LOCALE = <i>locale</i>, ]
 [ LC_COLLATE = <i>lc_collate</i>, ]
 [ LC_CTYPE = <i>lc_ctype</i> ]
)
CREATE COLLATION <i>name</i> FROM <i>existing_collation</i></pre>
<h2>Description</h2>
<p><code>CREATE COLLATION</code> defines a new collation using the specified operating system locale settings, or by copying an existing collation. </p>
<p> To be able to create a collation, you must have CREATE privilege on the destination schema.</p>
<h2>Parameters</h2>
<p><i>name</i></p>
<dl>
<dd>The name of the collation. The collation name can be schema-qualified. If it is not, the collation is defined in the current schema. The collation name must be unique within that schema. (The system catalogs can contain collations with the same name for other encodings, but these are ignored if the database encoding does not match.)</dl>
<p> <i>locale</i></p>
<dl>
<dd>This is a shortcut for setting LC_COLLATE and LC_CTYPE at once. If you specify this, you cannot specify either of those parameters.</dl>
<p> <i>lc_collate</i></p>
<dl>
<dd>Use the specified operating system locale for the LC_COLLATE locale category. The locale must be applicable to the current database encoding. (See CREATE DATABASE (<code><a href="/docs/linux/man/7-create_database/">CREATE_DATABASE</a></code>(7)) for the precise rules.)</dl>
<p> <i>lc_ctype</i></p>
<dl>
<dd>Use the specified operating system locale for the LC_CTYPE locale category. The locale must be applicable to the current database encoding. (See CREATE DATABASE (<code><a href="/docs/linux/man/7-create_database/">CREATE_DATABASE</a></code>(7)) for the precise rules.)</dl>
<p> <i>existing_collation</i></p>
<dl>
<dd>The name of an existing collation to copy. The new collation will have the same properties as the existing one, but it will be an independent object.</dl>
<h2>Notes</h2>
<p>Use <code>DROP COLLATION</code> to remove user-defined collations. </p>
<p> See Section 22.2, &#8220;Collation Support&#8221;, in the documentation for more information about collation support in PostgreSQL.</p>
<h2>Examples</h2>
<p>To create a collation from the operating system locale fr_FR.utf8 (assuming the current database encoding is UTF8): </p>
<pre><code>CREATE COLLATION french (LOCALE = 'fr_FR.utf8');</code></pre>
<p> To create a collation from an existing collation:</p>
<dl>
<dd>
<pre>CREATE COLLATION german FROM &quot;de_DE&quot;;</pre>
</dl>
<p> This can be convenient to be able to use operating-system-independent collation names in applications.</p>
<h2>Compatibility</h2>
<p>There is a <code>CREATE COLLATION</code> statement in the SQL standard, but it is limited to copying an existing collation. The syntax to create a new collation is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>ALTER COLLATION (<code><a href="/docs/linux/man/7-alter_collation/">ALTER_COLLATION</a></code>(7)), DROP COLLATION (<code><a href="/docs/linux/man/7-drop_collation/">DROP_COLLATION</a></code>(7)) </p>
