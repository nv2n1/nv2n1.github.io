---
title: "create_trigger(7)"
name: "create_trigger"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_trigger/"
description: "CREATE TRIGGER – define a new trigger"
---

<p>CREATE TRIGGER &#8211; define a new trigger </p>
<h2>Synopsis</h2>
<pre>CREATE TRIGGER <i>name</i> { BEFORE | AFTER } { <i>event</i> [ OR ... ] }
 ON <i>table</i> [ FOR [ EACH ] { ROW | STATEMENT } ]
 EXECUTE PROCEDURE <i>funcname</i> ( <i>arguments</i> )</pre>
<h2>Description</h2>
<p><code>CREATE TRIGGER</code> creates a new trigger. The trigger will be associated with the specified table and will execute the specified function <i>funcname</i> when certain events occur. </p>
<p> The trigger can be specified to fire either before the operation is attempted on a row (before constraints are checked and the <code>INSERT</code>, <code>UPDATE</code>, or <code>DELETE</code> is attempted) or after the operation has completed (after constraints are checked and the <code>INSERT</code>, <code>UPDATE</code>, or <code>DELETE</code> has completed). If the trigger fires before the event, the trigger can skip the operation for the current row, or change the row being inserted (for <code>INSERT</code> and <code>UPDATE</code> operations only). If the trigger fires after the event, all changes, including the last insertion, update, or deletion, are &#8220;visible&#8221; to the trigger. </p>
<p> A trigger that is marked FOR EACH ROW is called once for every row that the operation modifies. For example, a <code>DELETE</code> that affects 10 rows will cause any ON DELETE triggers on the target relation to be called 10 separate times, once for each deleted row. In contrast, a trigger that is marked FOR EACH STATEMENT only executes once for any given operation, regardless of how many rows it modifies (in particular, an operation that modifies zero rows will still result in the execution of any applicable FOR EACH STATEMENT triggers). </p>
<p> In addition, triggers may be defined to fire for a <code>TRUNCATE</code>, though only FOR EACH STATEMENT. </p>
<p> If multiple triggers of the same kind are defined for the same event, they will be fired in alphabetical order by name. </p>
<p> <code>SELECT</code> does not modify any rows so you cannot create <code>SELECT</code> triggers. Rules and views are more appropriate in such cases. </p>
<p> Refer to in the documentation for more information about triggers.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name to give the new trigger. This must be distinct from the name of any other trigger for the same table.</p>
<dt><code>BEFORE</code></p>
<dd>
<dt><code>AFTER</code></p>
<dd>Determines whether the function is called before or after the event.</p>
<dt><i>event</i></p>
<dd>One of <code>INSERT</code>, <code>UPDATE</code>, <code>DELETE</code>, or <code>TRUNCATE</code>; this specifies the event that will fire the trigger. Multiple events can be specified using OR.</p>
<dt><i>table</i></p>
<dd>The name (optionally schema-qualified) of the table the trigger is for.</p>
<dt><code>FOR EACH ROW</code></p>
<dd>
<dt><code>FOR EACH STATEMENT</code></p>
<dd>This specifies whether the trigger procedure should be fired once for every row affected by the trigger event, or just once per SQL statement. If neither is specified, FOR EACH STATEMENT is the default.</p>
<dt><i>funcname</i></p>
<dd>A user-supplied function that is declared as taking no arguments and returning type trigger, which is executed when the trigger fires.</p>
<dt><i>arguments</i></p>
<dd>An optional comma-separated list of arguments to be provided to the function when the trigger is executed. The arguments are literal string constants. Simple names and numeric constants can be written here, too, but they will all be converted to strings. Please check the description of the implementation language of the trigger function about how the trigger arguments are accessible within the function; it might be different from normal function arguments.</dl>
<h2>Notes</h2>
<p>To create a trigger on a table, the user must have the TRIGGER privilege on the table. </p>
<p> Use DROP TRIGGER [<code><a href="/docs/linux/man/7-drop_trigger/">drop_trigger</a></code>(7)] to remove a trigger. </p>
<p> In PostgreSQL versions before 7.3, it was necessary to declare trigger functions as returning the placeholder type <code>opaque</code>, rather than <code>trigger</code>. To support loading of old dump files, <code>CREATE TRIGGER</code> will accept a function declared as returning <code>opaque</code>, but it will issue a notice and change the function&#8217;s declared return type to <code>trigger</code>.</p>
<h2>Examples</h2>
<p>in the documentation contains a complete example.</p>
<h2>Compatibility</h2>
<p>The <code>CREATE TRIGGER</code> statement in PostgreSQL implements a subset of the SQL standard. The following functionality is currently missing:</p>
<dl>
<dt>*</p>
<dd>SQL allows triggers to fire on updates to specific columns (e.g., AFTER UPDATE OF col1, col2).</p>
<dt>*</p>
<dd>SQL allows you to define aliases for the &#8220;old&#8221; and &#8220;new&#8221; rows or tables for use in the definition of the triggered action (e.g., CREATE TRIGGER &#8230; ON tablename REFERENCING OLD ROW AS somename NEW ROW AS othername &#8230;). Since PostgreSQL allows trigger procedures to be written in any number of user-defined languages, access to the data is handled in a language-specific way.</p>
<dt>*</p>
<dd>PostgreSQL only allows the execution of a user-defined function for the triggered action. The standard allows the execution of a number of other SQL commands, such as <code>CREATE TABLE</code> as the triggered action. This limitation is not hard to work around by creating a user-defined function that executes the desired commands.</dl>
<p> SQL specifies that multiple triggers should be fired in time-of-creation order. PostgreSQL uses name order, which was judged to be more convenient. </p>
<p> SQL specifies that BEFORE DELETE triggers on cascaded deletes fire <code>after</code> the cascaded DELETE completes. The PostgreSQL behavior is for BEFORE DELETE to always fire before the delete action, even a cascading one. This is considered more consistent. There is also unpredictable behavior when BEFORE triggers modify rows that are later to be modified by referential actions. This can lead to constraint violations or stored data that does not honor the referential constraint. </p>
<p> The ability to specify multiple actions for a single trigger using OR is a PostgreSQL extension of the SQL standard. </p>
<p> The ability to fire triggers for <code>TRUNCATE</code> is a PostgreSQL extension of the SQL standard.</p>
<h2>See Also</h2>
<p>CREATE FUNCTION [<code><a href="/docs/linux/man/7-create_function/">create_function</a></code>(7)], ALTER TRIGGER [<code><a href="/docs/linux/man/7-alter_trigger/">alter_trigger</a></code>(7)], DROP TRIGGER [<code><a href="/docs/linux/man/7-drop_trigger/">drop_trigger</a></code>(7)] </p>
