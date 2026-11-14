---
title: "alter_view(7)"
name: "alter_view"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_view/"
description: "ALTER VIEW – change the definition of a view"
---

<p>ALTER VIEW &#8211; change the definition of a view </p>
<h2>Synopsis</h2>
<pre>ALTER VIEW <i>name</i> ALTER [ COLUMN ] <i>column</i> SET DEFAULT <i>expression</i>
ALTER VIEW <i>name</i> ALTER [ COLUMN ] <i>column</i> DROP DEFAULT
ALTER VIEW <i>name</i> OWNER TO <i>new_owner</i>
ALTER VIEW <i>name</i> RENAME TO <i>new_name</i>
ALTER VIEW <i>name</i> SET SCHEMA <i>new_schema</i></pre>
<h2>Description</h2>
<p><code>ALTER VIEW</code> changes various auxiliary properties of a view. (If you want to modify the view&#8217;s defining query, use <code>CREATE OR REPLACE VIEW</code>.) </p>
<p> You must own the view to use <code>ALTER VIEW</code>. To change a view&#8217;s schema, you must also have CREATE privilege on the new schema. To alter the owner, you must also be a direct or indirect member of the new owning role, and that role must have CREATE privilege on the view&#8217;s schema. (These restrictions enforce that altering the owner doesn&#8217;t do anything you couldn&#8217;t do by dropping and recreating the view. However, a superuser can alter ownership of any view anyway.)</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of an existing view.</p>
<dt><code>SET/DROP DEFAULT</code></p>
<dd>These forms set or remove the default value for a column. A default value associated with a view column is inserted into <code>INSERT</code> statements on the view before the view&#8217;s ON INSERT rule is applied, if the <code>INSERT</code> does not specify a value for the column.</p>
<dt><i>new_owner</i></p>
<dd>The user name of the new owner of the view.</p>
<dt><i>new_name</i></p>
<dd>The new name for the view.</p>
<dt><i>new_schema</i></p>
<dd>The new schema for the view.</dl>
<h2>Notes</h2>
<p>For historical reasons, <code>ALTER TABLE</code> can be used with views too; but the only variants of <code>ALTER TABLE</code> that are allowed with views are equivalent to the ones shown above.</p>
<h2>Examples</h2>
<p>To rename the view foo to bar: </p>
<pre>ALTER VIEW foo RENAME TO bar;</pre>
<h2>Compatibility</h2>
<p><code>ALTER VIEW</code> is a PostgreSQL extension of the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE VIEW [<code><a href="/docs/linux/man/7-create_view/">create_view</a></code>(7)], DROP VIEW [<code><a href="/docs/linux/man/7-drop_view/">drop_view</a></code>(7)] </p>
