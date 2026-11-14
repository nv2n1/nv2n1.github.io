---
title: "globus_rsl_value_make_concatenation(3)"
name: "globus_rsl_value_make_concatenation"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rsl_value_make_concatenation/"
description: "RSL Constructors –"
---

<h2 class="name">NAME</h2>
<p> RSL Constructors &#8211; </p>
<h3>Functions</h3>
<p> globus_rsl_t * <code>globus_rsl_make_boolean</code> (int operator, globus_list_t *children)<br />
 <i>RSL boolean constructor. </i><br />
 globus_rsl_t * <code>globus_rsl_make_relation</code> (int operator, char *attributename, globus_rsl_value_t *value_sequence)<br />
 <i>RSL relation constructor. </i><br />
 globus_rsl_value_t * <code>globus_rsl_value_make_literal</code> (char *string)<br />
 <i>RSL literal constructor. </i><br />
 globus_rsl_value_t * <code>globus_rsl_value_make_sequence</code> (globus_list_t *value_list)<br />
 <i>RSL value sequence constructor. </i><br />
 globus_rsl_value_t * <code>globus_rsl_value_make_variable</code> (globus_rsl_value_t *sequence)<br />
 <i>RSL variable reference constructor. </i><br />
 globus_rsl_value_t * <code>globus_rsl_value_make_concatenation</code> (globus_rsl_value_t *left_value, globus_rsl_value_t *right_value)<br />
 <i>RSL concatenation constructor. </i></p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>globus_rsl_t* globus_rsl_make_boolean (intoperator, globus_list_t *children)</h3>
<p> RSL boolean constructor. The <code>globus_rsl_make_boolean()</code> function creates a boolean composition of the RSL nodes in the list pointed to by <i>children</i>. The new RSL node which is returned contains a reference to the list, not a copy. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>operator</i> The boolean RSL operator to use to join the RSL parse tree list pointed to by the <i>children</i> parameter. This value must be one of GLOBUS_RSL_AND, GLOBUS_RSL_OR, GLOBUS_RSL_MULTIREQ in order to create a valid RSL tree.<br />
 <i>children</i> Pointer to a list of RSL syntax trees to combine with the boolean operation described by the <i>operator</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_make_boolean()</code> function returns a new RSL parse tree node that contains a shallow reference to the list of values pointed to by the <i>children</i> parameter joined by the operator value in the <i>operator</i> parameter. If an error occurs, <code>globus_rsl_make_boolean()</code> returns NULL.</dl>
<h3>globus_rsl_t* globus_rsl_make_relation (intoperator, char *attributename, globus_rsl_value_t *value_sequence)</h3>
<p> RSL relation constructor. The <code>globus_rsl_make_relation()</code> function creates a relation between the attribute named by the <i>attributename</i> parameter and the values pointed to by the <i>value_sequence</i> list. The new RSL relation node which is returned contains a reference to the <i>attributename</i> and <i>value_sequence</i> parameters, not a copy. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>operator</i> The RSL operator to use to relate the RSL attribute name pointed to by the <i>attributename</i> parameter and the values pointed to by the <i>value_sequence</i> parameter. This value must be one of GLOBUS_RSL_EQ, GLOBUS_RSL_NEQ, GLOBUS_RSL_GT, GLOBUS_RSL_GTEQ, GLOBUS_RSL_LT, or GLOBUS_RSL_LTEQ in order to create a valid RSL node.<br />
 <i>attributename</i> Pointer to a string naming the attribute of the new RSL relation.<br />
 <i>value_sequence</i> Pointer to a sequence of RSL values to use in the new RSL relation.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_make_relation()</code> function returns a new RSL parse tree node that contains a shallow reference to the attribute name pointed to by the <i>attributename</i> parameter and the RSL value sequence pointed to by the <i>value_sequence</i> parameter. If an error occurs, <code>globus_rsl_make_relation()</code> returns NULL.</dl>
<h3>globus_rsl_value_t* globus_rsl_value_make_concatenation (globus_rsl_value_t *left_value, globus_rsl_value_t *right_value)</h3>
<p> RSL concatenation constructor. The <code>globus_rsl_value_make_concatenation()</code> function creates a concatenation of the values pointed to by the <i>left_value</i> and <i>right_value</i> parameters. The new node returned by this function contains a reference to these parameters&#8217; values, not a copy. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>left_value</i> A pointer to a RSL value to act as the left side of the concatenation. This must be a string literal or variable reference.<br />
 <i>right_value</i> A pointer to a RSL value to act as the right side of the concatenation. This must be a string literal or variable reference.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_value_make_concatenation()</code> function returns a new RSL value node that contains a shallow reference to the values pointed to by the <i>left_value</i> and <i>right_value</i> parameters. If an error occurs, <code>globus_rsl_value_make_concatenation()</code> returns NULL.</dl>
<h3>globus_rsl_value_t* globus_rsl_value_make_literal (char *string)</h3>
<p> RSL literal constructor. The <code>globus_rsl_value_make_literal()</code> function creates a string literal RSL value node containing the value pointed to by the <i>string</i> parameter. The new RSL value node which is returned contains a reference to the <i>string</i> parameter, not a copy. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>string</i> The literal string to be used in the new value.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_value_make_literal()</code> function returns a new RSL value node that contains a shallow reference to the string pointed to by the <i>string</i> parameter. If an error occurs, <code>globus_rsl_value_make_literal()</code> returns NULL.</dl>
<h3>globus_rsl_value_t* globus_rsl_value_make_sequence (globus_list_t *value_list)</h3>
<p> RSL value sequence constructor. The <code>globus_rsl_value_make_sequence()</code> function creates a value sequence RSL node referring to the values pointed to by the <i>value_list</i> parameter. The new node returned by this function contains a reference to the <i>value_list</i> parameter, not a copy. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>value_list</i> A pointer to a list of globus_rsl_value_t pointers.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_value_make_sequence()</code> function returns a new RSL value node that contains a shallow reference to the list pointed to by the <i>value_list</i> parameter. If an error occurs, <code>globus_rsl_value_make_sequence()</code> returns NULL.</dl>
<h3>globus_rsl_value_t* globus_rsl_value_make_variable (globus_rsl_value_t *sequence)</h3>
<p> RSL variable reference constructor. The <code>globus_rsl_value_make_variable()</code> function creates a variable reference RSL node referring to the variable name contained in the value pointed to by <i>sequence</i> parameter. The new node returned by this function contains a reference to the <i>sequence</i> parameter, not a copy. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sequence</i> A pointer to a RSL value sequnce.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_value_make_variable()</code> function returns a new RSL value node that contains a shallow reference to the value sequence pointed to by the <i>sequence</i> parameter. If an error occurs, <code>globus_rsl_value_make_variable()</code> returns NULL.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_rsl from the source code. </p>
<h2>Index</h2>
