---
title: "drop_trigger(7)"
name: "drop_trigger"
section: "7"
letter: "d"
url: "/docs/linux/man/7-drop_trigger/"
description: "DROP TRIGGER – remove a trigger"
---

<p>DROP TRIGGER &#8211; remove a trigger </p>
<h2>Synopsis</h2>
<pre>DROP TRIGGER [ IF EXISTS ] <i>name</i> ON <i>table</i> [ CASCADE | RESTRICT ]</pre>
<h2>Description</h2>
<p><code>DROP TRIGGER</code> removes an existing trigger definition. To execute this command, the current user must be the owner of the table for which the trigger is defined.</p>
<h2>Parameters</h2>
<dl>
<dt><code>IF EXISTS</code></p>
<dd>Do not throw an error if the trigger does not exist. A notice is issued in this case.</p>
<dt><i>name</i></p>
<dd>The name of the trigger to remove.</p>
<dt><i>table</i></p>
<dd>The name (optionally schema-qualified) of the table for which the trigger is defined.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the trigger.</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the trigger if any objects depend on it. This is the default.</dl>
<h2>Examples</h2>
<p>Destroy the trigger if_dist_exists on the table films: </p>
<pre>DROP TRIGGER if_dist_exists ON films;</pre>
<h2>Compatibility</h2>
<p>The <code>DROP TRIGGER</code> statement in PostgreSQL is incompatible with the SQL standard. In the SQL standard, trigger names are not local to tables, so the command is simply DROP TRIGGER <i>name</i>.</p>
<h2>See Also</h2>
<p>CREATE TRIGGER [<code><a href="/docs/linux/man/7-create_trigger/">create_trigger</a></code>(7)] </p>
