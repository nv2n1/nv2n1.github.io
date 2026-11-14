---
title: "alter_sequence(7)"
name: "alter_sequence"
section: "7"
letter: "a"
url: "/docs/linux/man/7-alter_sequence/"
description: "ALTER SEQUENCE – change the definition of a sequence generator"
---

<p>ALTER SEQUENCE &#8211; change the definition of a sequence generator </p>
<h2>Synopsis</h2>
<pre>ALTER SEQUENCE <i>name</i> [ INCREMENT [ BY ] <i>increment</i> ]
 [ MINVALUE <i>minvalue</i> | NO MINVALUE ] [ MAXVALUE <i>maxvalue</i> | NO MAXVALUE ]
 [ START [ WITH ] <i>start</i> ]
 [ RESTART [ [ WITH ] <i>restart</i> ] ]
 [ CACHE <i>cache</i> ] [ [ NO ] CYCLE ]
 [ OWNED BY { <i>table</i>.<i>column</i> | NONE } ]
ALTER SEQUENCE <i>name</i> OWNER TO <i>new_owner</i>
ALTER SEQUENCE <i>name</i> RENAME TO <i>new_name</i>
ALTER SEQUENCE <i>name</i> SET SCHEMA <i>new_schema</i></pre>
<h2>Description</h2>
<p><code>ALTER SEQUENCE</code> changes the parameters of an existing sequence generator. Any parameters not specifically set in the <code>ALTER SEQUENCE</code> command retain their prior settings. </p>
<p> You must own the sequence to use <code>ALTER SEQUENCE</code>. To change a sequence&#8217;s schema, you must also have CREATE privilege on the new schema. To alter the owner, you must also be a direct or indirect member of the new owning role, and that role must have CREATE privilege on the sequence&#8217;s schema. (These restrictions enforce that altering the owner doesn&#8217;t do anything you couldn&#8217;t do by dropping and recreating the sequence. However, a superuser can alter ownership of any sequence anyway.)</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of a sequence to be altered.</p>
<dt><i>increment</i></p>
<dd>The clause INCREMENT BY <i>increment</i> is optional. A positive value will make an ascending sequence, a negative one a descending sequence. If unspecified, the old increment value will be maintained.</p>
<dt><i>minvalue</i></p>
<dd>
<dt><code>NO MINVALUE</code></p>
<dd>The optional clause MINVALUE <i>minvalue</i> determines the minimum value a sequence can generate. If NO MINVALUE is specified, the defaults of 1 and -263-1 for ascending and descending sequences, respectively, will be used. If neither option is specified, the current minimum value will be maintained.</p>
<dt><i>maxvalue</i></p>
<dd>
<dt><code>NO MAXVALUE</code></p>
<dd>The optional clause MAXVALUE <i>maxvalue</i> determines the maximum value for the sequence. If NO MAXVALUE is specified, the defaults are 263-1 and -1 for ascending and descending sequences, respectively, will be used. If neither option is specified, the current maximum value will be maintained.</p>
<dt><i>start</i></p>
<dd>The optional clause START WITH <i>start</i> changes the recorded start value of the sequence. This has no effect on the <code>current</code> sequence value; it simply sets the value that future <code>ALTER SEQUENCE RESTART</code> commands will use.</p>
<dt><i>restart</i></p>
<dd>The optional clause RESTART [ WITH <i>restart</i> ] changes the current value of the sequence. This is equivalent to calling the <code>setval</code> function with is_called = false: the specified value will be returned by the <code>next</code> call of <code>nextval</code>. Writing RESTART with no <i>restart</i> value is equivalent to supplying the start value that was recorded by <code>CREATE SEQUENCE</code> or last set by <code>ALTER SEQUENCE START WITH</code>.</p>
<dt><i>cache</i></p>
<dd>The clause CACHE <i>cache</i> enables sequence numbers to be preallocated and stored in memory for faster access. The minimum value is 1 (only one value can be generated at a time, i.e., no cache). If unspecified, the old cache value will be maintained.</p>
<dt><code>CYCLE</code></p>
<dd>The optional CYCLE key word can be used to enable the sequence to wrap around when the <i>maxvalue</i> or <i>minvalue</i> has been reached by an ascending or descending sequence respectively. If the limit is reached, the next number generated will be the <i>minvalue</i> or <i>maxvalue</i>, respectively.</p>
<dt><code>NO CYCLE</code></p>
<dd>If the optional NO CYCLE key word is specified, any calls to <code>nextval</code> after the sequence has reached its maximum value will return an error. If neither CYCLE or NO CYCLE are specified, the old cycle behavior will be maintained.</p>
<dt><code>OWNED BY </code><i>table</i><code>.</code><i>column</i></p>
<dd>
<dt><code>OWNED BY NONE</code></p>
<dd>The OWNED BY option causes the sequence to be associated with a specific table column, such that if that column (or its whole table) is dropped, the sequence will be automatically dropped as well. If specified, this association replaces any previously specified association for the sequence. The specified table must have the same owner and be in the same schema as the sequence. Specifying OWNED BY NONE removes any existing association, making the sequence &#8220;free-standing&#8221;.</p>
<dt><i>new_owner</i></p>
<dd>The user name of the new owner of the sequence.</p>
<dt><i>new_name</i></p>
<dd>The new name for the sequence.</p>
<dt><i>new_schema</i></p>
<dd>The new schema for the sequence.</dl>
<h2>Notes</h2>
<p>To avoid blocking of concurrent transactions that obtain numbers from the same sequence, <code>ALTER SEQUENCE</code>&#8216;s effects on the sequence generation parameters are never rolled back; those changes take effect immediately and are not reversible. However, the OWNED BY, OWNER TO, RENAME TO, and SET SCHEMA clauses cause ordinary catalog updates that can be rolled back. </p>
<p> <code>ALTER SEQUENCE</code> will not immediately affect <code>nextval</code> results in backends, other than the current one, that have preallocated (cached) sequence values. They will use up all cached values prior to noticing the changed sequence generation parameters. The current backend will be affected immediately. </p>
<p> <code>ALTER SEQUENCE</code> does not affect the <code>currval</code> status for the sequence. (Before PostgreSQL 8.3, it sometimes did.) </p>
<p> For historical reasons, <code>ALTER TABLE</code> can be used with sequences too; but the only variants of <code>ALTER TABLE</code> that are allowed with sequences are equivalent to the forms shown above.</p>
<h2>Examples</h2>
<p>Restart a sequence called serial, at 105: </p>
<pre>ALTER SEQUENCE serial RESTART WITH 105;</pre>
<h2>Compatibility</h2>
<p><code>ALTER SEQUENCE</code> conforms to the SQL standard, except for the START WITH, OWNED BY, OWNER TO, RENAME TO, and SET SCHEMA clauses, which are PostgreSQL extensions.</p>
<h2>See Also</h2>
<p>CREATE SEQUENCE [<code><a href="/docs/linux/man/7-create_sequence/">create_sequence</a></code>(7)], DROP SEQUENCE [<code><a href="/docs/linux/man/7-drop_sequence/">drop_sequence</a></code>(7)] </p>
