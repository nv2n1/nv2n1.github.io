---
title: "globus_rsl_value_print_recursive(3)"
name: "globus_rsl_value_print_recursive"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rsl_value_print_recursive/"
description: "RSL Display –"
---

<h2 class="name">NAME</h2>
<p> RSL Display &#8211; </p>
<h3>Functions</h3>
<p> int <code>globus_rsl_value_print_recursive</code> (globus_rsl_value_t *globus_rsl_value_ptr)<br />
 <i>Print the value of a globus_rsl_value_t to standard output. </i><br />
 char * <code>globus_rsl_get_operator</code> (int my_op)<br />
 <i>Get the string representation of an RSL operator. </i><br />
 int <code>globus_rsl_print_recursive</code> (globus_rsl_t *ast_node)<br />
 <i>Print the value of an RSL syntax tree to standard output. </i><br />
 char * <code>globus_rsl_unparse</code> (globus_rsl_t *rsl_spec)<br />
 <i>Convert an RSL parse tree to a string. </i><br />
 char * <code>globus_rsl_value_unparse</code> (globus_rsl_value_t *rsl_value)<br />
 <i>Convert an RSL value pointer to a string. </i></p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>char* globus_rsl_get_operator (intmy_op)</h3>
<p> Get the string representation of an RSL operator. The <code>globus_rsl_get_operator()</code> function returns a pointer to a static string that represents the RSL operator passed in via the <i>my_op</i> parameter. If the operator is not value, then <code>globus_rsl_get_operator()</code> returns a pointer to the string &#8216;??&#8217; </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>my_op</i> The RSL operator to return.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_get_operator()</code> function returns a pointer to the string representation of the <i>my_op</i> parameter, or &#8216;??&#8217; if that value is not a value RSL operator.</dl>
<h3>int globus_rsl_print_recursive (globus_rsl_t *ast_node)</h3>
<p> Print the value of an RSL syntax tree to standard output. The <code>globus_rsl_print_recursive()</code> function prints a string representation of the RSL syntax tree pointed to by the <i>ast_node</i> parameter to standard output. This function is not reentrant. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast_node</i> A pointer to the RSL syntax tree to display.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_print_recursive()</code> function always returns <i>GLOBUS_SUCCESS</i>.</dl>
<h3>char* globus_rsl_unparse (globus_rsl_t *rsl_spec)</h3>
<p> Convert an RSL parse tree to a string. The <code>globus_rsl_unparse()</code> function returns a new string which can be parsed into the RSL syntax tree passed as the <i>rsl_spec</i> parameter. The caller is responsible for freeing this string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>rsl_spec</i> A pointer to the RSL syntax tree to unparse.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_rsl_unparse()</code> function returns a new string which represents the RSL parse tree passed as the <i>rsl_spec</i> parameter. If an error occurs, <code>globus_rsl_unparse()</code> returns NULL.</dl>
<h3>int globus_rsl_value_print_recursive (globus_rsl_value_t *globus_rsl_value_ptr)</h3>
<p> Print the value of a globus_rsl_value_t to standard output. The <code>globus_rsl_value_print_recursive()</code> function prints a string representation of the RSL value node pointed to by the <i>globus_rsl_value_ptr</i> parameter to standard output. This function is not reentrant. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>globus_rsl_value_ptr</i> A pointer to the RSL value to display.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_value_print_recursive()</code> function always returns <i>GLOBUS_SUCCESS</i>.</dl>
<h3>char* globus_rsl_value_unparse (globus_rsl_value_t *rsl_value)</h3>
<p> Convert an RSL value pointer to a string. The <code>globus_rsl_value_unparse()</code> function returns a new string which can be parsed into the value of an RSL relation that has the same syntactic meaning as the <i>rsl_value</i> parameter. The caller is responsible for freeing this string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>rsl_value</i> A pointer to the RSL value node to unparse.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_rsl_value_unparse()</code> function returns a new string which represents the RSL value ndoe passed as the <i>rsl_value</i> parameter. If an error occurs, <code>globus_rsl_value_unparse()</code> returns NULL.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_rsl from the source code. </p>
<h2>Index</h2>
