---
title: "alter_trigger(7)"
name: "alter_trigger"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_trigger/"
description: "ALTER TRIGGER – change the definition of a trigger"
---

<p>ALTER TRIGGER &#8211; change the definition of a trigger </p>
<h2>Synopsis</h2>
<pre>ALTER TRIGGER <i>name</i> ON <i>table</i> RENAME TO <i>newname</i></pre>
<h2>Description</h2>
<p><code>ALTER TRIGGER</code> changes properties of an existing trigger. The RENAME clause changes the name of the given trigger without otherwise changing the trigger definition. </p>
<p> You must own the table on which the trigger acts to be allowed to change its properties.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name of an existing trigger to alter.</p>
<dt><i>table</i></p>
<dd>The name of the table on which this trigger acts.</p>
<dt><i>newname</i></p>
<dd>The new name for the trigger.</dl>
<h2>Notes</h2>
<p>The ability to temporarily enable or disable a trigger is provided by ALTER TABLE [<code><a href="/docs/linux/man/7-alter_table/">alter_table</a></code>(7)], not by <code>ALTER TRIGGER</code>, because <code>ALTER TRIGGER</code> has no convenient way to express the option of enabling or disabling all of a table&#8217;s triggers at once.</p>
<h2>Examples</h2>
<p>To rename an existing trigger: </p>
<pre>ALTER TRIGGER emp_stamp ON emp RENAME TO emp_track_chgs;</pre>
<h2>Compatibility</h2>
<p><code>ALTER TRIGGER</code> is a PostgreSQL extension of the SQL standard.</p>
<h2>See Also</h2>
<p>ALTER TABLE [<code><a href="/docs/linux/man/7-alter_table/">alter_table</a></code>(7)] </p>
