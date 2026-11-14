---
title: "globus_rsl_is_boolean_or(3)"
name: "globus_rsl_is_boolean_or"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rsl_is_boolean_or/"
description: "RSL Predicates –"
---

<h2 class="name">NAME</h2>
<p> RSL Predicates &#8211; </p>
<h3>Functions</h3>
<p> int <code>globus_rsl_is_relation</code> (globus_rsl_t *ast)<br />
 <i>RSL relation test. </i><br />
 int <code>globus_rsl_is_boolean</code> (globus_rsl_t *ast)<br />
 <i>RSL boolean test. </i><br />
 int <code>globus_rsl_is_relation_eq</code> (globus_rsl_t *ast)<br />
 <i>RSL equality operation test. </i><br />
 int <code>globus_rsl_is_relation_lessthan</code> (globus_rsl_t *ast)<br />
 <i>RSL less than operation test. </i><br />
 int <code>globus_rsl_is_relation_attribute_equal</code> (globus_rsl_t *ast, char *attribute)<br />
 <i>RSL attribute name test. </i><br />
 int <code>globus_rsl_is_boolean_and</code> (globus_rsl_t *ast)<br />
 <i>RSL boolean and test. </i><br />
 int <code>globus_rsl_is_boolean_or</code> (globus_rsl_t *ast)<br />
 <i>RSL boolean or test. </i><br />
 int <code>globus_rsl_is_boolean_multi</code> (globus_rsl_t *ast)<br />
 <i>RSL boolean multi test. </i><br />
 int <code>globus_rsl_value_is_literal</code> (globus_rsl_value_t *ast)<br />
 <i>RSL literal string test. </i><br />
 int <code>globus_rsl_value_is_sequence</code> (globus_rsl_value_t *ast)<br />
 <i>RSL value sequence test. </i><br />
 int <code>globus_rsl_value_is_variable</code> (globus_rsl_value_t *ast)<br />
 <i>RSL value variable test. </i><br />
 int <code>globus_rsl_value_is_concatenation</code> (globus_rsl_value_t *ast)<br />
 <i>RSL value concatenation test. </i></p>
<h2>Detailed Description</h2>
<p> The functions in this group return boolean values indicating whether an RSL syntax tree is of a particular type.</p>
<h2>Function Documentation</h2>
<h3>int globus_rsl_is_boolean (globus_rsl_t *ast)</h3>
<p> RSL boolean test. The <code>globus_rsl_is_boolean()</code> function tests whether the the RSL pointed to by the <i>ast</i> parameter is a boolean composition of other RSL parse trees. The syntactically understood boolean compositions are &#8216;&amp;&#8217; (conjunction), &#8216;|&#8217; (disjunction), and &#8216;+&#8217; (multi-request). Some bexamples of RSL booleans are </p>
<pre>
&amp; ( &quot;queue&quot; = &quot;debug&quot;) ( &quot;max_time&quot; = &quot;10000&quot;)
| (&quot;count&quot; = &quot;1&quot;)(&quot;count&quot; = &quot;10&quot;)
+ ( &amp;(&quot;executable&quot; = &quot;1.exe&quot;) ) ( &amp; (&quot;executable&quot; = &quot;2.exe&quot; )
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast</i> Pointer to an RSL parse tree structure.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_is_boolean()</code> function returns GLOBUS_TRUE if the RSL parse tree pointed to by <i>ast</i> is a boolean composition; otherwise, it returns GLOBUS_FALSE.</dl>
<h3>int globus_rsl_is_boolean_and (globus_rsl_t *ast)</h3>
<p> RSL boolean and test. The <code>globus_rsl_is_boolean_and()</code> function tests whether the the RSL pointed to by the <i>ast</i> parameter is a boolean &#8216;and&#8217; composition of RSL trees. </p>
<p> An example of a boolean and relation is </p>
<pre>
&amp; ( &quot;queue&quot; = &quot;debug&quot; ) ( &quot;executable&quot; = &quot;a.out&quot; )
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast</i> Pointer to an RSL parse tree structure.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_is_boolean_and()</code> function returns GLOBUS_TRUE if the RSL parse tree pointed to by <i>ast</i> is a boolean and of RSL parse trees; otherwise, it returns GLOBUS_FALSE.</dl>
<h3>int globus_rsl_is_boolean_multi (globus_rsl_t *ast)</h3>
<p> RSL boolean multi test. The <code>globus_rsl_is_boolean_multi()</code> function tests whether the the RSL pointed to by the <i>ast</i> parameter is a boolean &#8216;multi-request&#8217; composition of RSL trees. </p>
<p> An example of a boolean multie-request relation is </p>
<pre>
+ ( &amp;( &quot;executable&quot; = &quot;exe.1&quot;) ( &quot;count&quot; = &quot;2&quot; ) )
  ( &amp;( &quot;executable&quot; =&quot; exe.2&quot;) ( &quot;count&quot; = &quot;2&quot; ) )
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast</i> Pointer to an RSL parse tree structure.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_is_boolean_multi()</code> function returns GLOBUS_TRUE if the RSL parse tree pointed to by <i>ast</i> is a boolean multi-request of RSL parse trees; otherwise, it returns GLOBUS_FALSE.</dl>
<h3>int globus_rsl_is_boolean_or (globus_rsl_t *ast)</h3>
<p> RSL boolean or test. The <code>globus_rsl_is_boolean_or()</code> function tests whether the the RSL pointed to by the <i>ast</i> parameter is a boolean &#8216;or&#8217; composition of RSL trees. </p>
<p> An example of a boolean or relation is </p>
<pre>
| ( &quot;count&quot; = &quot;2&quot; ) ( &quot;count&quot; = &quot;4&quot; )
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast</i> Pointer to an RSL parse tree structure.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_is_boolean_or()</code> function returns GLOBUS_TRUE if the RSL parse tree pointed to by <i>ast</i> is a boolean and of RSL parse trees; otherwise, it returns GLOBUS_FALSE.</dl>
<h3>int globus_rsl_is_relation (globus_rsl_t *ast)</h3>
<p> RSL relation test. The <code>globus_rsl_is_relation()</code> function tests whether the the RSL pointed to by the <i>ast</i> parameter is a relation. The RSL syntax supports the following relation operations:</p>
<dl>
<dt><code>= </code></p>
<dd> Equal</p>
<dt><code>!= </code></p>
<dd> Not Equal</p>
<dt><code>&gt; </code></p>
<dd> Greater Than</p>
<dt><code>&gt;= </code></p>
<dd> Greater Than or Equal</p>
<dt><code>&lt; </code></p>
<dd> Less Than</p>
<dt><code>&lt;= </code></p>
<dd> Less Than or Equal</p>
<dt><code>&lt;= </code></p>
<dd> Less Than or Equal</dl>
<p> Some examples of RSL relations are </p>
<pre>
&quot;queue&quot; = &quot;debug&quot;
&quot;queue&quot; != &quot;slow&quot;
&quot;min_memory&quot; &gt; &quot;1000&quot;
&quot;max_wall_time&quot; &gt;= &quot;60&quot;
&quot;count &lt; &quot;10&quot;
&quot;host_count&quot; &lt;= &quot;5&quot;
</pre>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> GRAM only supports equality relations.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast</i> Pointer to an RSL parse tree structure.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_is_relation()</code> function returns GLOBUS_TRUE if the RSL parse tree pointed to by <i>ast</i> is a relation; otherwise, it returns GLOBUS_FALSE.</dl>
<h3>int globus_rsl_is_relation_attribute_equal (globus_rsl_t *ast, char *attribute)</h3>
<p> RSL attribute name test. The <code>globus_rsl_is_relation_attribute_equal()</code> function tests whether the the RSL pointed to by the <i>ast</i> parameter is a relation with the attribute name which matches the string pointed to by the <i>attribute</i> parameter. This attribute name comparision is case-insensitive. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast</i> Pointer to an RSL parse tree structure.<br />
 <i>attribute</i> Name of the attribute to test</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_is_relation_attribute_equal()</code> function returns GLOBUS_TRUE if the RSL parse tree pointed to by <i>ast</i> is a relation and its attribute name matches the <i>attribute</i> parameter; otherwise, it returns GLOBUS_FALSE.</dl>
<h3>int globus_rsl_is_relation_eq (globus_rsl_t *ast)</h3>
<p> RSL equality operation test. The <code>globus_rsl_is_relation_eq()</code> function tests whether the the RSL pointed to by the <i>ast</i> parameter is an equality relation. An example of an equality relation is </p>
<pre>
&quot;queue&quot; = &quot;debug&quot;
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast</i> Pointer to an RSL parse tree structure.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_is_relation_eq()</code> function returns GLOBUS_TRUE if the RSL parse tree pointed to by <i>ast</i> is an equality relation; otherwise, it returns GLOBUS_FALSE.</dl>
<h3>int globus_rsl_is_relation_lessthan (globus_rsl_t *ast)</h3>
<p> RSL less than operation test. The <code>globus_rsl_is_relation_lessthan()</code> function tests whether the the RSL pointed to by the <i>ast</i> parameter is a less-than relation. An example of a less-than relation is </p>
<pre>
&quot;count&quot; = &quot;10&quot;
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast</i> Pointer to an RSL parse tree structure.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_is_relation_lessthan()</code> function returns GLOBUS_TRUE if the RSL parse tree pointed to by <i>ast</i> is a less-than relation; otherwise, it returns GLOBUS_FALSE.</dl>
<h3>int globus_rsl_value_is_concatenation (globus_rsl_value_t *ast)</h3>
<p> RSL value concatenation test. The <code>globus_rsl_value_is_concatenation()</code> function tests whether the the RSL value pointed to by the <i>ast</i> parameter is a concatenation of RSL values. An example of an RSL value concatenation is </p>
<pre>
$( &quot;GLOBUSRUN_GASS_URL&quot; ) # &quot;/input&quot;
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast</i> Pointer to an RSL value structure.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_value_is_concatenation()</code> function returns GLOBUS_TRUE if the RSL value pointed to by <i>ast</i> is a value concatenation; otherwise, it returns GLOBUS_FALSE.</dl>
<h3>int globus_rsl_value_is_literal (globus_rsl_value_t *ast)</h3>
<p> RSL literal string test. The <code>globus_rsl_value_is_literal()</code> function tests whether the the RSL value pointed to by the <i>ast</i> parameter is a literal string value. </p>
<p> An example of a literal string is </p>
<pre>
&quot;count&quot;
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast</i> Pointer to an RSL value structure.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_value_is_literal()</code> function returns GLOBUS_TRUE if the RSL value pointed to by <i>ast</i> is a literal string value; otherwise, it returns GLOBUS_FALSE.</dl>
<h3>int globus_rsl_value_is_sequence (globus_rsl_value_t *ast)</h3>
<p> RSL value sequence test. The <code>globus_rsl_value_is_sequence()</code> function tests whether the the RSL value pointed to by the <i>ast</i> parameter is a sequence of RSL values. An example of a sequence of values is </p>
<pre>
&quot;1&quot; &quot;2&quot; &quot;3&quot;
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast</i> Pointer to an RSL value structure.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_value_is_sequence()</code> function returns GLOBUS_TRUE if the RSL value pointed to by <i>ast</i> is a value sequnce; otherwise, it returns GLOBUS_FALSE.</dl>
<h3>int globus_rsl_value_is_variable (globus_rsl_value_t *ast)</h3>
<p> RSL value variable test. The <code>globus_rsl_value_is_variable()</code> function tests whether the the RSL value pointed to by the <i>ast</i> parameter is a variable reference. RSL values. An example of a variable reference is </p>
<pre>
$( &quot;GLOBUSRUN_GASS_URL&quot; )
</pre>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast</i> Pointer to an RSL value structure.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_value_is_sequence()</code> function returns GLOBUS_TRUE if the RSL value pointed to by <i>ast</i> is a value sequnce; otherwise, it returns GLOBUS_FALSE.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_rsl from the source code. </p>
<h2>Index</h2>
