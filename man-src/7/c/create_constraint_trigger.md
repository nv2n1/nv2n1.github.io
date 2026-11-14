---
title: "create_constraint_trigger(7)"
name: "create_constraint_trigger"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_constraint_trigger/"
description: "CREATE CONSTRAINT TRIGGER – define a new constraint trigger"
---

<p>CREATE CONSTRAINT TRIGGER &#8211; define a new constraint trigger </p>
<h2>Synopsis</h2>
<pre>CREATE CONSTRAINT TRIGGER <i>name</i>
 AFTER <i>event</i> [ OR ... ]
 ON <i>table_name</i>
 [ FROM <i>referenced_table_name</i> ]
 { NOT DEFERRABLE | [ DEFERRABLE ] { INITIALLY IMMEDIATE | INITIALLY DEFERRED } }
 FOR EACH ROW
 EXECUTE PROCEDURE <i>funcname</i> ( <i>arguments</i> )</pre>
<h2>Description</h2>
<p><code>CREATE CONSTRAINT TRIGGER</code> creates a <i>constraint trigger</i>. This is the same as a regular trigger except that the timing of the trigger firing can be adjusted using SET CONSTRAINTS [<code><a href="/docs/linux/man/7-set_constraints/">set_constraints</a></code>(7)]. Constraint triggers must be AFTER ROW triggers. They can be fired either at the end of the statement causing the triggering event, or at the end of the containing transaction; in the latter case they are said to be <i>deferred</i>. A pending deferred-trigger firing can also be forced to happen immediately by using <code>SET CONSTRAINTS</code>.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of the constraint trigger. This is also the name to use when modifying the trigger&#8217;s behavior using <code>SET CONSTRAINTS</code>. The name cannot be schema-qualified &#8212; the trigger inherits the schema of its table.</p>
<dt><i>event</i></p>
<dd>One of INSERT, UPDATE, or DELETE; this specifies the event that will fire the trigger. Multiple events can be specified using OR.</p>
<dt><i>table_name</i></p>
<dd>The (possibly schema-qualified) name of the table in which the triggering events occur.</p>
<dt><i>referenced_table_name</i></p>
<dd>The (possibly schema-qualified) name of another table referenced by the constraint. This option is used for foreign-key constraints and is not recommended for general use.</p>
<dt><code>DEFERRABLE</code></p>
<dd>
<dt><code>NOT DEFERRABLE</code></p>
<dd>
<dt><code>INITIALLY IMMEDIATE</code></p>
<dd>
<dt><code>INITIALLY DEFERRED</code></p>
<dd>The default timing of the trigger. See the CREATE TABLE [<code><a href="/docs/linux/man/7-create_table/">create_table</a></code>(7)] documentation for details of these constraint options.</p>
<dt><i>funcname</i></p>
<dd>The function to call when the trigger is fired. See CREATE TRIGGER [<code><a href="/docs/linux/man/7-create_trigger/">create_trigger</a></code>(7)] for details.</p>
<dt><i>arguments</i></p>
<dd>Optional argument strings to pass to the trigger function. See CREATE TRIGGER [<code><a href="/docs/linux/man/7-create_trigger/">create_trigger</a></code>(7)] for details.</dl>
<h2>Compatibility</h2>
<p><code>CREATE CONSTRAINT TRIGGER</code> is a PostgreSQL extension of the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE TRIGGER [<code><a href="/docs/linux/man/7-create_trigger/">create_trigger</a></code>(7)], DROP TRIGGER [<code><a href="/docs/linux/man/7-drop_trigger/">drop_trigger</a></code>(7)], SET CONSTRAINTS [<code><a href="/docs/linux/man/7-set_constraints/">set_constraints</a></code>(7)] </p>
