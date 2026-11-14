---
title: "alter_table(7)"
name: "alter_table"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_table/"
description: "ALTER TABLE – change the definition of a table"
---

<p>ALTER TABLE &#8211; change the definition of a table </p>
<h2>Synopsis</h2>
<pre>ALTER TABLE [ ONLY ] <i>name</i> [ * ]
 <i>action</i> [, ... ]
ALTER TABLE [ ONLY ] <i>name</i> [ * ]
 RENAME [ COLUMN ] <i>column</i> TO <i>new_column</i>
ALTER TABLE <i>name</i>
 RENAME TO <i>new_name</i>
ALTER TABLE <i>name</i>
 SET SCHEMA <i>new_schema</i>
where <i>action</i> is one of:
 ADD [ COLUMN ] <i>column</i> <i>type</i> [ <i>column_constraint</i> [ ... ] ]
 DROP [ COLUMN ] <i>column</i> [ RESTRICT | CASCADE ]
 ALTER [ COLUMN ] <i>column</i> [ SET DATA ] TYPE <i>type</i> [ USING <i>expression</i> ]
 ALTER [ COLUMN ] <i>column</i> SET DEFAULT <i>expression</i>
 ALTER [ COLUMN ] <i>column</i> DROP DEFAULT
 ALTER [ COLUMN ] <i>column</i> { SET | DROP } NOT NULL
 ALTER [ COLUMN ] <i>column</i> SET STATISTICS <i>integer</i>
 ALTER [ COLUMN ] <i>column</i> SET STORAGE { PLAIN | EXTERNAL | EXTENDED | MAIN }
 ADD <i>table_constraint</i>
 DROP CONSTRAINT <i>constraint_name</i> [ RESTRICT | CASCADE ]
 DISABLE TRIGGER [ <i>trigger_name</i> | ALL | USER ]
 ENABLE TRIGGER [ <i>trigger_name</i> | ALL | USER ]
 ENABLE REPLICA TRIGGER <i>trigger_name</i>
 ENABLE ALWAYS TRIGGER <i>trigger_name</i>
 DISABLE RULE <i>rewrite_rule_name</i>
 ENABLE RULE <i>rewrite_rule_name</i>
 ENABLE REPLICA RULE <i>rewrite_rule_name</i>
 ENABLE ALWAYS RULE <i>rewrite_rule_name</i>
 CLUSTER ON <i>index_name</i>
 SET WITHOUT CLUSTER
 SET WITH OIDS
 SET WITHOUT OIDS
 SET ( <i>storage_parameter</i> = <i>value</i> [, ... ] )
 RESET ( <i>storage_parameter</i> [, ... ] )
 INHERIT <i>parent_table</i>
 NO INHERIT <i>parent_table</i>
 OWNER TO <i>new_owner</i>
 SET TABLESPACE <i>new_tablespace</i></pre>
<h2>Description</h2>
<p><code>ALTER TABLE</code> changes the definition of an existing table. There are several subforms:</p>
<dl>
<dt><code>ADD COLUMN</code></p>
<dd>This form adds a new column to the table, using the same syntax as CREATE TABLE [<code><a href="/docs/linux/man/7-create_table/">create_table</a></code>(7)].</p>
<dt><code>DROP COLUMN</code></p>
<dd>This form drops a column from a table. Indexes and table constraints involving the column will be automatically dropped as well. You will need to say CASCADE if anything outside the table depends on the column, for example, foreign key references or views.</p>
<dt><code>SET DATA TYPE</code></p>
<dd>This form changes the type of a column of a table. Indexes and simple table constraints involving the column will be automatically converted to use the new column type by reparsing the originally supplied expression. The optional USING clause specifies how to compute the new column value from the old; if omitted, the default conversion is the same as an assignment cast from old data type to new. A USING clause must be provided if there is no implicit or assignment cast from old to new type.</p>
<dt><code>SET/DROP DEFAULT</code></p>
<dd>These forms set or remove the default value for a column. The default values only apply to subsequent <code>INSERT</code> commands; they do not cause rows already in the table to change. Defaults can also be created for views, in which case they are inserted into <code>INSERT</code> statements on the view before the view&#8217;s ON INSERT rule is applied.</p>
<dt><code>SET/DROP NOT NULL</code></p>
<dd>These forms change whether a column is marked to allow null values or to reject null values. You can only use SET NOT NULL when the column contains no null values.</p>
<dt><code>SET STATISTICS</code></p>
<dd>This form sets the per-column statistics-gathering target for subsequent ANALYZE [<code><a href="/docs/linux/man/7-analyze/">analyze</a></code>(7)] operations. The target can be set in the range 0 to 10000; alternatively, set it to -1 to revert to using the system default statistics target (default_statistics_target). For more information on the use of statistics by the PostgreSQL query planner, refer to in the documentation. </p>
<dt><code>SET STORAGE</code></p>
<dd>This form sets the storage mode for a column. This controls whether this column is held inline or in a secondary TOAST table, and whether the data should be compressed or not. PLAIN must be used for fixed-length values such as <code>integer</code> and is inline, uncompressed. MAIN is for inline, compressible data. EXTERNAL is for external, uncompressed data, and EXTENDED is for external, compressed data. EXTENDED is the default for most data types that support non-PLAIN storage. Use of EXTERNAL will make substring operations on very large <code>text</code> and <code>bytea</code> values run faster, at the penalty of increased storage space. Note that SET STORAGE doesn&#8217;t itself change anything in the table, it just sets the strategy to be pursued during future table updates. See in the documentation for more information.</p>
<dt><code>ADD </code><i>table_constraint</i></p>
<dd>This form adds a new constraint to a table using the same syntax as CREATE TABLE [<code><a href="/docs/linux/man/7-create_table/">create_table</a></code>(7)].</p>
<dt><code>DROP CONSTRAINT</code></p>
<dd>This form drops the specified constraint on a table.</p>
<dt><code>DISABLE/ENABLE [ REPLICA | ALWAYS ] TRIGGER</code></p>
<dd>These forms configure the firing of trigger(s) belonging to the table. A disabled trigger is still known to the system, but is not executed when its triggering event occurs. For a deferred trigger, the enable status is checked when the event occurs, not when the trigger function is actually executed. One can disable or enable a single trigger specified by name, or all triggers on the table, or only user triggers (this option excludes triggers that are used to implement foreign key constraints). Disabling or enabling constraint triggers requires superuser privileges; it should be done with caution since of course the integrity of the constraint cannot be guaranteed if the triggers are not executed. The trigger firing mechanism is also affected by the configuration variable session_replication_role. Simply enabled triggers will fire when the replication role is &#8220;origin&#8221; (the default) or &#8220;local&#8221;. Triggers configured as ENABLE REPLICA will only fire if the session is in &#8220;replica&#8221; mode, and triggers configured as ENABLE ALWAYS will fire regardless of the current replication mode.</p>
<dt><code>DISABLE/ENABLE [ REPLICA | ALWAYS ] RULE</code></p>
<dd>These forms configure the firing of rewrite rules belonging to the table. A disabled rule is still known to the system, but is not applied during query rewriting. The semantics are as for disabled/enabled triggers. This configuration is ignored for ON SELECT rules, which are always applied in order to keep views working even if the current session is in a non-default replication role.</p>
<dt><code>CLUSTER</code></p>
<dd>This form selects the default index for future CLUSTER [<code><a href="/docs/linux/man/7-cluster/">cluster</a></code>(7)] operations. It does not actually re-cluster the table.</p>
<dt><code>SET WITHOUT CLUSTER</code></p>
<dd>This form removes the most recently used CLUSTER [<code><a href="/docs/linux/man/7-cluster/">cluster</a></code>(7)] index specification from the table. This affects future cluster operations that don&#8217;t specify an index.</p>
<dt><code>SET WITH OIDS</code></p>
<dd>This form adds an oid system column to the table (see in the documentation). It does nothing if the table already has OIDs. </p>
<p> Note that this is not equivalent to ADD COLUMN oid oid; that would add a normal column that happened to be named oid, not a system column.</p>
<dt><code>SET WITHOUT OIDS</code></p>
<dd>This form removes the oid system column from the table. This is exactly equivalent to DROP COLUMN oid RESTRICT, except that it will not complain if there is already no oid column.</p>
<dt><code>SET ( </code><i>storage_parameter</i><code> = </code><i>value</i><code> [, &#8230; ] )</code></p>
<dd>This form changes one or more storage parameters for the table. See Storage Parameters [<code><a href="/docs/linux/man/7-create_table/">create_table</a></code>(7)] for details on the available parameters. Note that the table contents will not be modified immediately by this command; depending on the parameter you might need to rewrite the table to get the desired effects. That can be done with CLUSTER [<code><a href="/docs/linux/man/7-cluster/">cluster</a></code>(7)] or one of the forms of <code>ALTER TABLE</code> that forces a table rewrite. </p>
<dl>
<dd><code>Note:</code> While <code>CREATE TABLE</code> allows OIDS to be specified in the WITH (<i>storage_parameter</i>) syntax, <code>ALTER TABLE</code> does not treat OIDS as a storage parameter. Instead use the SET WITH OIDS and SET WITHOUT OIDS forms to change OID status.</dl>
<dt><code>RESET ( </code><i>storage_parameter</i><code> [, &#8230; ] )</code></p>
<dd>This form resets one or more storage parameters to their defaults. As with SET, a table rewrite might be needed to update the table entirely.</p>
<dt><code>INHERIT </code><i>parent_table</i></p>
<dd>This form adds the target table as a new child of the specified parent table. Subsequently, queries against the parent will include records of the target table. To be added as a child, the target table must already contain all the same columns as the parent (it could have additional columns, too). The columns must have matching data types, and if they have NOT NULL constraints in the parent then they must also have NOT NULL constraints in the child. </p>
<p> There must also be matching child-table constraints for all CHECK constraints of the parent. Currently UNIQUE, PRIMARY KEY, and FOREIGN KEY constraints are not considered, but this might change in the future.</p>
<dt><code>NO INHERIT </code><i>parent_table</i></p>
<dd>This form removes the target table from the list of children of the specified parent table. Queries against the parent table will no longer include records drawn from the target table.</p>
<dt><code>OWNER</code></p>
<dd>This form changes the owner of the table, sequence, or view to the specified user.</p>
<dt><code>SET TABLESPACE</code></p>
<dd>This form changes the table&#8217;s tablespace to the specified tablespace and moves the data file(s) associated with the table to the new tablespace. Indexes on the table, if any, are not moved; but they can be moved separately with additional SET TABLESPACE commands. See also CREATE TABLESPACE [<code><a href="/docs/linux/man/7-create_tablespace/">create_tablespace</a></code>(7)].</p>
<dt><code>RENAME</code></p>
<dd>The RENAME forms change the name of a table (or an index, sequence, or view) or the name of an individual column in a table. There is no effect on the stored data.</p>
<dt><code>SET SCHEMA</code></p>
<dd>This form moves the table into another schema. Associated indexes, constraints, and sequences owned by table columns are moved as well.</dl>
<p> All the actions except RENAME and SET SCHEMA can be combined into a list of multiple alterations to apply in parallel. For example, it is possible to add several columns and/or alter the type of several columns in a single command. This is particularly useful with large tables, since only one pass over the table need be made. </p>
<p> You must own the table to use <code>ALTER TABLE</code>. To change the schema of a table, you must also have CREATE privilege on the new schema. To add the table as a new child of a parent table, you must own the parent table as well. To alter the owner, you must also be a direct or indirect member of the new owning role, and that role must have CREATE privilege on the table&#8217;s schema. (These restrictions enforce that altering the owner doesn&#8217;t do anything you couldn&#8217;t do by dropping and recreating the table. However, a superuser can alter ownership of any table anyway.)</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (possibly schema-qualified) of an existing table to alter. If ONLY is specified, only that table is altered. If ONLY is not specified, the table and any descendant tables are altered.</p>
<dt><i>column</i></p>
<dd>Name of a new or existing column.</p>
<dt><i>new_column</i></p>
<dd>New name for an existing column.</p>
<dt><i>new_name</i></p>
<dd>New name for the table.</p>
<dt><i>type</i></p>
<dd>Data type of the new column, or new data type for an existing column.</p>
<dt><i>table_constraint</i></p>
<dd>New table constraint for the table.</p>
<dt><i>constraint_name</i></p>
<dd>Name of an existing constraint to drop.</p>
<dt><code>CASCADE</code></p>
<dd>Automatically drop objects that depend on the dropped column or constraint (for example, views referencing the column).</p>
<dt><code>RESTRICT</code></p>
<dd>Refuse to drop the column or constraint if there are any dependent objects. This is the default behavior.</p>
<dt><i>trigger_name</i></p>
<dd>Name of a single trigger to disable or enable.</p>
<dt><code>ALL</code></p>
<dd>Disable or enable all triggers belonging to the table. (This requires superuser privilege if any of the triggers are for foreign key constraints.)</p>
<dt><code>USER</code></p>
<dd>Disable or enable all triggers belonging to the table except for foreign key constraint triggers.</p>
<dt><i>index_name</i></p>
<dd>The index name on which the table should be marked for clustering.</p>
<dt><i>storage_parameter</i></p>
<dd>The name of a table storage parameter.</p>
<dt><i>value</i></p>
<dd>The new value for a table storage parameter. This might be a number or a word depending on the parameter.</p>
<dt><i>parent_table</i></p>
<dd>A parent table to associate or de-associate with this table.</p>
<dt><i>new_owner</i></p>
<dd>The user name of the new owner of the table.</p>
<dt><i>new_tablespace</i></p>
<dd>The name of the tablespace to which the table will be moved.</p>
<dt><i>new_schema</i></p>
<dd>The name of the schema to which the table will be moved.</dl>
<h2>Notes</h2>
<p>The key word COLUMN is noise and can be omitted. </p>
<p> When a column is added with ADD COLUMN, all existing rows in the table are initialized with the column&#8217;s default value (NULL if no DEFAULT clause is specified). </p>
<p> Adding a column with a non-null default or changing the type of an existing column will require the entire table to be rewritten. This might take a significant amount of time for a large table; and it will temporarily require double the disk space. Adding or removing a system oid column likewise requires rewriting the entire table. </p>
<p> Adding a CHECK or NOT NULL constraint requires scanning the table to verify that existing rows meet the constraint. </p>
<p> The main reason for providing the option to specify multiple changes in a single <code>ALTER TABLE</code> is that multiple table scans or rewrites can thereby be combined into a single pass over the table. </p>
<p> The DROP COLUMN form does not physically remove the column, but simply makes it invisible to SQL operations. Subsequent insert and update operations in the table will store a null value for the column. Thus, dropping a column is quick but it will not immediately reduce the on-disk size of your table, as the space occupied by the dropped column is not reclaimed. The space will be reclaimed over time as existing rows are updated. (These statements do not apply when dropping the system oid column; that is done with an immediate rewrite.) </p>
<p> The fact that ALTER TYPE requires rewriting the whole table is sometimes an advantage, because the rewriting process eliminates any dead space in the table. For example, to reclaim the space occupied by a dropped column immediately, the fastest way is: </p>
<pre>ALTER TABLE table ALTER COLUMN anycol TYPE anytype;</pre>
<p>where anycol is any remaining table column and anytype is the same type that column already has. This results in no semantically-visible change in the table, but the command forces rewriting, which gets rid of no-longer-useful data. </p>
<p> The USING option of ALTER TYPE can actually specify any expression involving the old values of the row; that is, it can refer to other columns as well as the one being converted. This allows very general conversions to be done with the ALTER TYPE syntax. Because of this flexibility, the USING expression is not applied to the column&#8217;s default value (if any); the result might not be a constant expression as required for a default. This means that when there is no implicit or assignment cast from old to new type, ALTER TYPE might fail to convert the default even though a USING clause is supplied. In such cases, drop the default with DROP DEFAULT, perform the ALTER TYPE, and then use SET DEFAULT to add a suitable new default. Similar considerations apply to indexes and constraints involving the column. </p>
<p> If a table has any descendant tables, it is not permitted to add, rename, or change the type of a column in the parent table without doing the same to the descendants. That is, <code>ALTER TABLE ONLY</code> will be rejected. This ensures that the descendants always have columns matching the parent. </p>
<p> A recursive DROP COLUMN operation will remove a descendant table&#8217;s column only if the descendant does not inherit that column from any other parents and never had an independent definition of the column. A nonrecursive DROP COLUMN (i.e., <code>ALTER TABLE ONLY &#8230; DROP COLUMN</code>) never removes any descendant columns, but instead marks them as independently defined rather than inherited. </p>
<p> The TRIGGER, CLUSTER, OWNER, and TABLESPACE actions never recurse to descendant tables; that is, they always act as though ONLY were specified. Adding a constraint can recurse only for CHECK constraints, and is required to do so for such constraints. </p>
<p> Changing any part of a system catalog table is not permitted. </p>
<p> Refer to CREATE TABLE [<code><a href="/docs/linux/man/7-create_table/">create_table</a></code>(7)] for a further description of valid parameters. in the documentation has further information on inheritance.</p>
<h2>Examples</h2>
<p>To add a column of type <code>varchar</code> to a table: </p>
<pre>ALTER TABLE distributors ADD COLUMN address varchar(30);</pre>
<p>To drop a column from a table: </p>
<pre>ALTER TABLE distributors DROP COLUMN address RESTRICT;</pre>
<p>To change the types of two existing columns in one operation: </p>
<pre>ALTER TABLE distributors
 ALTER COLUMN address TYPE varchar(80),
 ALTER COLUMN name TYPE varchar(100);</pre>
<p>To change an integer column containing UNIX timestamps to <code>timestamp with time zone</code> via a USING clause: </p>
<pre>ALTER TABLE foo
 ALTER COLUMN foo_timestamp SET DATA TYPE timestamp with time zone
 USING
 timestamp with time zone 'epoch' + foo_timestamp * interval '1 second';</pre>
<p>The same, when the column has a default expression that won&#8217;t automatically cast to the new data type: </p>
<pre>ALTER TABLE foo
 ALTER COLUMN foo_timestamp DROP DEFAULT,
 ALTER COLUMN foo_timestamp TYPE timestamp with time zone
 USING
 timestamp with time zone 'epoch' + foo_timestamp * interval '1 second',
 ALTER COLUMN foo_timestamp SET DEFAULT now();</pre>
<p>To rename an existing column: </p>
<pre>ALTER TABLE distributors RENAME COLUMN address TO city;</pre>
<p>To rename an existing table: </p>
<pre>ALTER TABLE distributors RENAME TO suppliers;</pre>
<p>To add a not-null constraint to a column: </p>
<pre>ALTER TABLE distributors ALTER COLUMN street SET NOT NULL;</pre>
<p>To remove a not-null constraint from a column: </p>
<pre>ALTER TABLE distributors ALTER COLUMN street DROP NOT NULL;</pre>
<p>To add a check constraint to a table and all its children: </p>
<pre><code>ALTER TABLE distributors ADD CONSTRAINT zipchk CHECK (char_length(zipcode) = 5);</code></pre>
<p> To remove a check constraint from a table and all its children: </p>
<pre>ALTER TABLE distributors DROP CONSTRAINT zipchk;</pre>
<p>To remove a check constraint from a table only: </p>
<pre>ALTER TABLE ONLY distributors DROP CONSTRAINT zipchk;</pre>
<p>(The check constraint remains in place for any child tables.) To add a foreign key constraint to a table: </p>
<pre>ALTER TABLE distributors ADD CONSTRAINT distfk FOREIGN KEY (address) REFERENCES addresses (address) MATCH FULL;</pre>
<p>To add a (multicolumn) unique constraint to a table: </p>
<pre>ALTER TABLE distributors ADD CONSTRAINT dist_id_zipcode_key UNIQUE (dist_id, zipcode);</pre>
<p>To add an automatically named primary key constraint to a table, noting that a table can only ever have one primary key: </p>
<pre>ALTER TABLE distributors ADD PRIMARY KEY (dist_id);</pre>
<p>To move a table to a different tablespace: </p>
<pre>ALTER TABLE distributors SET TABLESPACE fasttablespace;</pre>
<p>To move a table to a different schema: </p>
<pre>ALTER TABLE myschema.distributors SET SCHEMA yourschema;</pre>
<h2>Compatibility</h2>
<p>The forms ADD, DROP, SET DEFAULT, and SET DATA TYPE (without USING) conform with the SQL standard. The other forms are PostgreSQL extensions of the SQL standard. Also, the ability to specify more than one manipulation in a single <code>ALTER TABLE</code> command is an extension. </p>
<p> <code>ALTER TABLE DROP COLUMN</code> can be used to drop the only column of a table, leaving a zero-column table. This is an extension of SQL, which disallows zero-column tables.</p>
