---
title: "drop_foreign_table(7)"
name: "drop_foreign_table"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_foreign_table/"
description: "DROP_FOREIGN_TABLE – remove a foreign table"
---

<p>DROP_FOREIGN_TABLE &#8211; remove a foreign table</p>
<h2>Synopsis</h2>
<pre>DROP FOREIGN TABLE [ IF EXISTS ] <i>name</i> [, ...] [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP FOREIGN TABLE</code> removes a foreign table. Only the owner of a foreign table can remove it.</p>
<h2>Parameters</h2>
<p>IF EXISTS</p>
<dl>
<dd>Do not throw an error if the foreign table does not exist. A notice is issued in this case.</dl>
<p> <i>name</i></p>
<dl>
<dd>The name (optionally schema-qualified) of the foreign table to drop.</dl>
<p> CASCADE</p>
<dl>
<dd>Automatically drop objects that depend on the foreign table (such as views).</dl>
<p> RESTRICT</p>
<dl>
<dd>Refuse to drop the foreign table if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>To destroy two foreign tables, films and distributors: </p>
<dl>
<dd>
<pre>DROP FOREIGN TABLE films, distributors;</pre>
</dl>
<h2>Compatibility</h2>
<p>This command conforms to the ISO/IEC 9075-9 (SQL/MED), except that the standard only allows one foreign table to be dropped per command, and apart from the IF EXISTS option, which is a PostgreSQL extension.</p>
<h2>See Also</h2>
<p>ALTER FOREIGN TABLE (<code><a href="/docs/linux/man/7-alter_foreign_table/">ALTER_FOREIGN_TABLE</a></code>(7)), CREATE FOREIGN TABLE (<code><a href="/docs/linux/man/7-create_foreign_table/">CREATE_FOREIGN_TABLE</a></code>(7)) </p>
