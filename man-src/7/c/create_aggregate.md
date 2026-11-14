---
title: "create_aggregate(7)"
name: "create_aggregate"
section: "7"
letter: "c"
url: "/docs/linux/man/7-create_aggregate/"
description: "CREATE AGGREGATE – define a new aggregate function"
---

<p>CREATE AGGREGATE &#8211; define a new aggregate function </p>
<h2>Synopsis</h2>
<pre>CREATE AGGREGATE <i>name</i> ( <i>input_data_type</i> [ , ... ] ) (
 SFUNC = <i>sfunc</i>,
 STYPE = <i>state_data_type</i>
 [ , FINALFUNC = <i>ffunc</i> ]
 [ , INITCOND = <i>initial_condition</i> ]
 [ , SORTOP = <i>sort_operator</i> ]
)
or the old syntax
CREATE AGGREGATE <i>name</i> (
 BASETYPE = <i>base_type</i>,
 SFUNC = <i>sfunc</i>,
 STYPE = <i>state_data_type</i>
 [ , FINALFUNC = <i>ffunc</i> ]
 [ , INITCOND = <i>initial_condition</i> ]
 [ , SORTOP = <i>sort_operator</i> ]
)</pre>
<h2>Description</h2>
<p><code>CREATE AGGREGATE</code> defines a new aggregate function. Some basic and commonly-used aggregate functions are included with the distribution; they are documented in in the documentation. If one defines new types or needs an aggregate function not already provided, then <code>CREATE AGGREGATE</code> can be used to provide the desired features. </p>
<p> If a schema name is given (for example, CREATE AGGREGATE myschema.myagg &#8230;) then the aggregate function is created in the specified schema. Otherwise it is created in the current schema. </p>
<p> An aggregate function is identified by its name and input data type(s). Two aggregates in the same schema can have the same name if they operate on different input types. The name and input data type(s) of an aggregate must also be distinct from the name and input data type(s) of every ordinary function in the same schema. </p>
<p> An aggregate function is made from one or two ordinary functions: a state transition function <i>sfunc</i>, and an optional final calculation function <i>ffunc</i>. These are used as follows: </p>
<pre><i>sfunc</i>( internal-state, next-data-values ) ---&gt; next-internal-state
<i>ffunc</i>( internal-state ) ---&gt; aggregate-value</pre>
<p>PostgreSQL creates a temporary variable of data type <i>stype</i> to hold the current internal state of the aggregate. At each input row, the aggregate argument value(s) are calculated and the state transition function is invoked with the current state value and the new argument value(s) to calculate a new internal state value. After all the rows have been processed, the final function is invoked once to calculate the aggregate&#8217;s return value. If there is no final function then the ending state value is returned as-is. </p>
<p> An aggregate function can provide an initial condition, that is, an initial value for the internal state value. This is specified and stored in the database as a value of type <code>text</code>, but it must be a valid external representation of a constant of the state value data type. If it is not supplied then the state value starts out null. </p>
<p> If the state transition function is declared &#8220;strict&#8221;, then it cannot be called with null inputs. With such a transition function, aggregate execution behaves as follows. Rows with any null input values are ignored (the function is not called and the previous state value is retained). If the initial state value is null, then at the first row with all-nonnull input values, the first argument value replaces the state value, and the transition function is invoked at subsequent rows with all-nonnull input values. This is handy for implementing aggregates like <code>max</code>. Note that this behavior is only available when <i>state_data_type</i> is the same as the first <i>input_data_type</i>. When these types are different, you must supply a nonnull initial condition or use a nonstrict transition function. </p>
<p> If the state transition function is not strict, then it will be called unconditionally at each input row, and must deal with null inputs and null transition values for itself. This allows the aggregate author to have full control over the aggregate&#8217;s handling of null values. </p>
<p> If the final function is declared &#8220;strict&#8221;, then it will not be called when the ending state value is null; instead a null result will be returned automatically. (Of course this is just the normal behavior of strict functions.) In any case the final function has the option of returning a null value. For example, the final function for <code>avg</code> returns null when it sees there were zero input rows. </p>
<p> Aggregates that behave like <code>MIN</code> or <code>MAX</code> can sometimes be optimized by looking into an index instead of scanning every input row. If this aggregate can be so optimized, indicate it by specifying a <i>sort operator</i>. The basic requirement is that the aggregate must yield the first element in the sort ordering induced by the operator; in other words: </p>
<pre>SELECT agg(col) FROM tab;</pre>
<p>must be equivalent to: </p>
<pre>SELECT col FROM tab ORDER BY col USING sortop LIMIT 1;</pre>
<p>Further assumptions are that the aggregate ignores null inputs, and that it delivers a null result if and only if there were no non-null inputs. Ordinarily, a data type&#8217;s &lt; operator is the proper sort operator for <code>MIN</code>, and &gt; is the proper sort operator for <code>MAX</code>. Note that the optimization will never actually take effect unless the specified operator is the &#8220;less than&#8221; or &#8220;greater than&#8221; strategy member of a B-tree index operator class.</p>
<h2>Parameters</h2>
<dl>
<dt><i>name</i></p>
<dd>The name (optionally schema-qualified) of the aggregate function to create.</p>
<dt><i>input_data_type</i></p>
<dd>An input data type on which this aggregate function operates. To create a zero-argument aggregate function, write * in place of the list of input data types. (An example of such an aggregate is <code>count(*)</code>.)</p>
<dt><i>base_type</i></p>
<dd>In the old syntax for <code>CREATE AGGREGATE</code>, the input data type is specified by a basetype parameter rather than being written next to the aggregate name. Note that this syntax allows only one input parameter. To define a zero-argument aggregate function, specify the basetype as &quot;ANY&quot; (not *).</p>
<dt><i>sfunc</i></p>
<dd>The name of the state transition function to be called for each input row. For an <i>N</i>-argument aggregate function, the <i>sfunc</i> must take <i>N</i>+1 arguments, the first being of type <i>state_data_type</i> and the rest matching the declared input data type(s) of the aggregate. The function must return a value of type <i>state_data_type</i>. This function takes the current state value and the current input data value(s), and returns the next state value.</p>
<dt><i>state_data_type</i></p>
<dd>The data type for the aggregate&#8217;s state value.</p>
<dt><i>ffunc</i></p>
<dd>The name of the final function called to compute the aggregate&#8217;s result after all input rows have been traversed. The function must take a single argument of type <i>state_data_type</i>. The return data type of the aggregate is defined as the return type of this function. If <i>ffunc</i> is not specified, then the ending state value is used as the aggregate&#8217;s result, and the return type is <i>state_data_type</i>.</p>
<dt><i>initial_condition</i></p>
<dd>The initial setting for the state value. This must be a string constant in the form accepted for the data type <i>state_data_type</i>. If not specified, the state value starts out null.</p>
<dt><i>sort_operator</i></p>
<dd>The associated sort operator for a <code>MIN</code>&#8211; or <code>MAX</code>-like aggregate. This is just an operator name (possibly schema-qualified). The operator is assumed to have the same input data types as the aggregate (which must be a single-argument aggregate).</dl>
<p> The parameters of <code>CREATE AGGREGATE</code> can be written in any order, not just the order illustrated above.</p>
<h2>Examples</h2>
<p>See in the documentation.</p>
<h2>Compatibility</h2>
<p><code>CREATE AGGREGATE</code> is a PostgreSQL language extension. The SQL standard does not provide for user-defined aggregate functions.</p>
<h2>See Also</h2>
<p>ALTER AGGREGATE [<code><a href="/docs/linux/man/7-alter_aggregate/">alter_aggregate</a></code>(7)], DROP AGGREGATE [<code><a href="/docs/linux/man/7-drop_aggregate/">drop_aggregate</a></code>(7)] </p>
