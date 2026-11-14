---
title: "create_sequence(7)"
name: "create_sequence"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_sequence/"
description: "CREATE SEQUENCE – define a new sequence generator"
---

<p>CREATE SEQUENCE &#8211; define a new sequence generator </p>
<h2>Synopsis</h2>
<pre>CREATE [ TEMPORARY | TEMP ] SEQUENCE <i>name</i> [ INCREMENT [ BY ] <i>increment</i> ]
 [ MINVALUE <i>minvalue</i> | NO MINVALUE ] [ MAXVALUE <i>maxvalue</i> | NO MAXVALUE ]
 [ START [ WITH ] <i>start</i> ] [ CACHE <i>cache</i> ] [ [ NO ] CYCLE ]
 [ OWNED BY { <i>table</i>.<i>column</i> | NONE } ]</pre>
<h2>Description</h2>
<p><code>CREATE SEQUENCE</code> creates a new sequence number generator. This involves creating and initializing a new special single-row table with the name <i>name</i>. The generator will be owned by the user issuing the command. </p>
<p> If a schema name is given then the sequence is created in the specified schema. Otherwise it is created in the current schema. Temporary sequences exist in a special schema, so a schema name cannot be given when creating a temporary sequence. The sequence name must be distinct from the name of any other sequence, table, index, or view in the same schema. </p>
<p> After a sequence is created, you use the functions <code>nextval</code>, <code>currval</code>, and <code>setval</code> to operate on the sequence. These functions are documented in in the documentation. </p>
<p> Although you cannot update a sequence directly, you can use a query like: </p>
<pre>SELECT * FROM <i>name</i>;</pre>
<p>to examine the parameters and current state of a sequence. In particular, the last_value field of the sequence shows the last value allocated by any session. (Of course, this value might be obsolete by the time it&#8217;s printed, if other sessions are actively doing <code>nextval</code> calls.)</p>
<h2>Parameters</h2>
<dl>
<dt><code>TEMPORARY or TEMP</code></p>
<dd>If specified, the sequence object is created only for this session, and is automatically dropped on session exit. Existing permanent sequences with the same name are not visible (in this session) while the temporary sequence exists, unless they are referenced with schema-qualified names.</p>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of the sequence to be created.</p>
<dt><i>increment</i></p>
<dd>The optional clause INCREMENT BY <i>increment</i> specifies which value is added to the current sequence value to create a new value. A positive value will make an ascending sequence, a negative one a descending sequence. The default value is 1.</p>
<dt><i>minvalue</i></p>
<dd>
<dt><code>NO MINVALUE</code></p>
<dd>The optional clause MINVALUE <i>minvalue</i> determines the minimum value a sequence can generate. If this clause is not supplied or <code>NO MINVALUE</code> is specified, then defaults will be used. The defaults are 1 and -263-1 for ascending and descending sequences, respectively.</p>
<dt><i>maxvalue</i></p>
<dd>
<dt><code>NO MAXVALUE</code></p>
<dd>The optional clause MAXVALUE <i>maxvalue</i> determines the maximum value for the sequence. If this clause is not supplied or <code>NO MAXVALUE</code> is specified, then default values will be used. The defaults are 263-1 and -1 for ascending and descending sequences, respectively.</p>
<dt><i>start</i></p>
<dd>The optional clause START WITH <i>start</i> allows the sequence to begin anywhere. The default starting value is <i>minvalue</i> for ascending sequences and <i>maxvalue</i> for descending ones.</p>
<dt><i>cache</i></p>
<dd>The optional clause CACHE <i>cache</i> specifies how many sequence numbers are to be preallocated and stored in memory for faster access. The minimum value is 1 (only one value can be generated at a time, i.e., no cache), and this is also the default.</p>
<dt><code>CYCLE</code></p>
<dd>
<dt><code>NO CYCLE</code></p>
<dd>The CYCLE option allows the sequence to wrap around when the <i>maxvalue</i> or <i>minvalue</i> has been reached by an ascending or descending sequence respectively. If the limit is reached, the next number generated will be the <i>minvalue</i> or <i>maxvalue</i>, respectively. </p>
<p> If NO CYCLE is specified, any calls to <code>nextval</code> after the sequence has reached its maximum value will return an error. If neither CYCLE or NO CYCLE are specified, NO CYCLE is the default.</p>
<dt><code>OWNED BY </code><i>table</i><code>.</code><i>column</i></p>
<dd>
<dt><code>OWNED BY NONE</code></p>
<dd>The OWNED BY option causes the sequence to be associated with a specific table column, such that if that column (or its whole table) is dropped, the sequence will be automatically dropped as well. The specified table must have the same owner and be in the same schema as the sequence. OWNED BY NONE, the default, specifies that there is no such association.</dl>
<h2>Notes</h2>
<p>Use <code>DROP SEQUENCE</code> to remove a sequence. </p>
<p> Sequences are based on <code>bigint</code> arithmetic, so the range cannot exceed the range of an eight-byte integer (-9223372036854775808 to 9223372036854775807). On some older platforms, there might be no compiler support for eight-byte integers, in which case sequences use regular <code>integer</code> arithmetic (range -2147483648 to +2147483647). </p>
<p> Unexpected results might be obtained if a <i>cache</i> setting greater than one is used for a sequence object that will be used concurrently by multiple sessions. Each session will allocate and cache successive sequence values during one access to the sequence object and increase the sequence object&#8217;s last_value accordingly. Then, the next <i>cache</i>-1 uses of <code>nextval</code> within that session simply return the preallocated values without touching the sequence object. So, any numbers allocated but not used within a session will be lost when that session ends, resulting in &#8220;holes&#8221; in the sequence. </p>
<p> Furthermore, although multiple sessions are guaranteed to allocate distinct sequence values, the values might be generated out of sequence when all the sessions are considered. For example, with a <i>cache</i> setting of 10, session A might reserve values 1..10 and return <code>nextval</code>=1, then session B might reserve values 11..20 and return <code>nextval</code>=11 before session A has generated nextval=2. Thus, with a <i>cache</i> setting of one it is safe to assume that <code>nextval</code> values are generated sequentially; with a <i>cache</i> setting greater than one you should only assume that the <code>nextval</code> values are all distinct, not that they are generated purely sequentially. Also, last_value will reflect the latest value reserved by any session, whether or not it has yet been returned by <code>nextval</code>. </p>
<p> Another consideration is that a <code>setval</code> executed on such a sequence will not be noticed by other sessions until they have used up any preallocated values they have cached.</p>
<h2>Examples</h2>
<p>Create an ascending sequence called serial, starting at 101: </p>
<pre>CREATE SEQUENCE serial START 101;</pre>
<p>Select the next number from this sequence: </p>
<pre>SELECT nextval('serial');
 nextval
---------
 101</pre>
<p>Select the next number from this sequence: </p>
<pre>SELECT nextval('serial');
 nextval
---------
 102</pre>
<p>Use this sequence in an <code>INSERT</code> command: </p>
<pre>INSERT INTO distributors VALUES (nextval('serial'), 'nothing');</pre>
<p>Update the sequence value after a <code>COPY FROM</code>: </p>
<pre>BEGIN;
COPY distributors FROM 'input_file';
SELECT setval('serial', max(id)) FROM distributors;
END;</pre>
<h2>Compatibility</h2>
<p><code>CREATE SEQUENCE</code> conforms to the SQL standard, with the following exceptions:</p>
<dl>
<dt>*</p>
<dd>The standard&#8217;s AS &lt;data type&gt; expression is not supported.</p>
<dt>*</p>
<dd>Obtaining the next value is done using the <code>nextval()</code> function instead of the standard&#8217;s <code>NEXT VALUE FOR</code> expression.</p>
<dt>*</p>
<dd>The OWNED BY clause is a PostgreSQL extension.</dl>
<h2>See Also</h2>
<p>ALTER SEQUENCE [<code><a href="/docs/linux/man/7-alter_sequence/">alter_sequence</a></code>(7)], DROP SEQUENCE [<code><a href="/docs/linux/man/7-drop_sequence/">drop_sequence</a></code>(7)] </p>
