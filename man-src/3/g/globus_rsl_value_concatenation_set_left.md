---
title: "globus_rsl_value_concatenation_set_left(3)"
name: "globus_rsl_value_concatenation_set_left"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rsl_value_concatenation_set_left/"
description: "RSL Value Accessors –"
---

<h2 class="name">NAME</h2>
<p> RSL Value Accessors &#8211; </p>
<h3>Functions</h3>
<p> int <code>globus_rsl_value_concatenation_set_left</code> (globus_rsl_value_t *concatenation_node, globus_rsl_value_t *new_left_node)<br />
 <i>Set the left-hand value of a concatenation. </i><br />
 int <code>globus_rsl_value_concatenation_set_right</code> (globus_rsl_value_t *concatenation_node, globus_rsl_value_t *new_right_node)<br />
 <i>Set the right-hand value of a concatenation. </i><br />
 int <code>globus_rsl_value_list_param_get</code> (globus_list_t *ast_node_list, int required_type, char ***value, int *value_ctr)<br />
 <i>Get the values of an RSL value list. </i><br />
 globus_list_t * <code>globus_rsl_param_get_values</code> (globus_rsl_t *ast_node, char *param)<br />
 <i>Get the list of values for an RSL attribute. </i><br />
 int <code>globus_rsl_param_get</code> (globus_rsl_t *ast_node, int param_type, char *param, char ***values)<br />
 <i>Get the value strings for an RSL attribute. </i></p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>int globus_rsl_param_get (globus_rsl_t *ast_node, intparam_type, char *param, char ***values)</h3>
<p> Get the value strings for an RSL attribute. The <code>globus_rsl_param_get()</code> function searches the RSL parse tree pointed to by the <i>ast_node</i> parameter and returns an array of pointers to the strings bound to the attribute named by the <i>param</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast_node</i> A pointer to an RSL syntax tree that will be searched. This may be a relation or boolean RSL string.<br />
 <i>param_type</i> A flag indicating what type of values are expected for the RSL attribute named by the <i>param</i> parameter. This flag value may be <i>GLOBUS_RSL_PARAM_SINGLE_LITERAL</i>, <i>GLOBUS_RSL_PARAM_MULTI_LITERAL</i>, or <i>GLOBUS_RSL_PARAM_SEQUENCE</i>.<br />
 <i>param</i> A string pointing to the name of of the RSL attribute to search for.<br />
 <i>values</i> An output parameter pointing to an array of strings that will be allocated and contain pointers to the RSL value strings if they match the format specified by the <i>param_type</i> flag. The caller is responsible for freeing this array, but not the strings in the array.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_rsl_param_get()</code> function returns <i>GLOBUS_SUCCESS</i> and modifies the <i>values</i> parameter as described above. If an error occurs, <code>globus_rsl_param_get()</code> returns a non-zero value.</dl>
<h3>globus_list_t* globus_rsl_param_get_values (globus_rsl_t *ast_node, char *param)</h3>
<p> Get the list of values for an RSL attribute. The <code>globus_rsl_param_get_values()</code> function searches the RSL parse tree pointed to by the <i>ast_node</i> parameter and returns the value list that is bound to the attribute named by the <i>param</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast_node</i> A pointer to an RSL syntax tree that will be searched. This may be a relation or boolean RSL string.<br />
 <i>param</i> The name of the attribute to search for in the parse tree pointed to by the <i>ast_node</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_rsl_param_get_values()</code> function returns a pointer to the list of values associated with the attribute named by <i>param</i> in the RSL parse tree pointed to by <i>ast_node</i>. If an error occurs, <code>globus_rsl_param_get_values()</code> returns NULL.</dl>
<h3>int globus_rsl_value_concatenation_set_left (globus_rsl_value_t *concatenation_node, globus_rsl_value_t *new_left_node)</h3>
<p> Set the left-hand value of a concatenation. The <code>globus_rsl_value_concatenation_set_left()</code> sets the left hand side of a concatenation pointed to by <i>concatenation_node</i> to the value pointed to by <i>new_left_node</i>. If there was any previous value to the left hand side of the concatenation, it is discarded but not freed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>concatenation_node</i> A pointer to the RSL value concatenation node to modify.<br />
 <i>new_left_node</i> A pointer to the new left hand side of the concatenation.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_value_concatenation_set_left()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the value pointed to by the <i>concatenation_node</i> parameter to use the value pointed to by the <i>new_left_node</i> parameter as its left hand side value. If an error occurs, <code>globus_rsl_value_concatenation_set_left()</code> returns -1.</dl>
<h3>int globus_rsl_value_concatenation_set_right (globus_rsl_value_t *concatenation_node, globus_rsl_value_t *new_right_node)</h3>
<p> Set the right-hand value of a concatenation. The <code>globus_rsl_value_concatenation_set_right()</code> sets the right-hand side of a concatenation pointed to by <i>concatenation_node</i> to the value pointed to by <i>new_right_node</i>. If there was any previous value to the right-hand side of the concatenation, it is discarded but not freed. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>concatenation_node</i> A pointer to the RSL value concatenation node to modify.<br />
 <i>new_right_node</i> A pointer to the new right hand side of the concatenation.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_value_concatenation_set_right()</code> returns <i>GLOBUS_SUCCESS</i> and modifies the value pointed to by the <i>concatenation_node</i> parameter to use the value pointed to by the <i>new_right_node</i> parameter as its right hand side value. If an error occurs, <code>globus_rsl_value_concatenation_set_right()</code> returns -1.</dl>
<h3>int globus_rsl_value_list_param_get (globus_list_t *ast_node_list, intrequired_type, char ***value, int *value_ctr)</h3>
<p> Get the values of an RSL value list. The <code>globus_rsl_value_list_param_get()</code> function copies pointers to literal string values or string pairs associated with the list of globus_rsl_value_t pointers pointed to by the <i>ast_node_list</i> parameter to the output array pointed to by the <i>value</i> parameter. It modifies the value pointed to by the <i>value_ctr</i> parameter to be the number of strings copied into the array. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast_node_list</i> A pointer to a list of globus_rsl_value_t pointers whose values will be copied to the <i>value</i> parameter array.<br />
 <i>required_type</i> A flag indicating whether the list is expected to contain literal strings or string pairs. This value may be one of <i>GLOBUS_RSL_VALUE_LITERAL</i> or <i>GLOBUS_RSL_VALUE_SEQUENCE</i>.<br />
 <i>value</i> An output parameter pointing to an array of strings. This array must be at least as large as the number of elements in the list pointed to by <i>ast_node_list</i>.<br />
 <i>value_ctr</i> An output parameter pointing to an integer that will be incremented for each string copied into the <i>value</i> array.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_rsl_value_list_param_get()</code> function returns GLOBUS_SUCCESS and modifies the values pointed to by the <i>value</i> and <i>value_ctr</i> prameters as described above. If an error occurs, <code>globus_rsl_value_list_param_get()</code> returns a non-zero value.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_rsl from the source code. </p>
<h2>Index</h2>
