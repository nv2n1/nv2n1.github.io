---
title: "globus_rsl_parse(3)"
name: "globus_rsl_parse"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rsl_parse/"
description: "globus_rsl.h – Globus RSL Parsing."
---

<h2 class="name">NAME</h2>
<p> globus_rsl.h &#8211; Globus RSL Parsing.</p>
<h2>SYNOPSIS</h2>
<p> #include &#8216;globus_module.h&#8217;<br />
 #include &#8216;globus_list.h&#8217;<br />
 #include &#8216;globus_symboltable.h&#8217;<br />
 #include &#8216;globus_hashtable.h&#8217; </p>
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
 <i>RSL value concatenation test. </i><br />
 globus_rsl_t * <code>globus_rsl_make_boolean</code> (int my_operator, globus_list_t *children)<br />
 <i>RSL boolean constructor. </i><br />
 globus_rsl_t * <code>globus_rsl_make_relation</code> (int my_operator, char *attributename, globus_rsl_value_t *value_sequence)<br />
 <i>RSL relation constructor. </i><br />
 globus_rsl_value_t * <code>globus_rsl_value_make_literal</code> (char *string)<br />
 <i>RSL literal constructor. </i><br />
 globus_rsl_value_t * <code>globus_rsl_value_make_sequence</code> (globus_list_t *value_list)<br />
 <i>RSL value sequence constructor. </i><br />
 globus_rsl_value_t * <code>globus_rsl_value_make_variable</code> (globus_rsl_value_t *sequence)<br />
 <i>RSL variable reference constructor. </i><br />
 globus_rsl_value_t * <code>globus_rsl_value_make_concatenation</code> (globus_rsl_value_t *left_value, globus_rsl_value_t *right_value)<br />
 <i>RSL concatenation constructor. </i><br />
 globus_rsl_t * <code>globus_rsl_copy_recursive</code> (globus_rsl_t *globus_rsl_ptr)<br />
 <i>Create a deep copy of an RSL syntax tree. </i><br />
 globus_rsl_value_t * <code>globus_rsl_value_copy_recursive</code> (globus_rsl_value_t *globus_rsl_value_ptr)<br />
 <i>Create a deep copy of an RSL value. </i><br />
 int <code>globus_rsl_boolean_get_operator</code> (globus_rsl_t *ast_node)<br />
 <i>Get the RSL operator used in a boolean RSL composition. </i><br />
 globus_list_t * <code>globus_rsl_boolean_get_operand_list</code> (globus_rsl_t *ast_node)<br />
 <i>Get the RSL operand list from a boolean RSL composition. </i><br />
 globus_list_t ** <code>globus_rsl_boolean_get_operand_list_ref</code> (globus_rsl_t *boolean_node)<br />
 <i>Get a reference to the RSL operand list from a boolean RSL composition. </i><br />
 char * <code>globus_rsl_relation_get_attribute</code> (globus_rsl_t *ast_node)<br />
 <i>Get an RSL relation attribute name. </i><br />
 int <code>globus_rsl_relation_get_operator</code> (globus_rsl_t *ast_node)<br />
 <i>Get an RSL relation operator. </i><br />
 globus_rsl_value_t * <code>globus_rsl_relation_get_value_sequence</code> (globus_rsl_t *ast_node)<br />
 <i>Get the value of an RSL relation. </i><br />
 globus_rsl_value_t * <code>globus_rsl_relation_get_single_value</code> (globus_rsl_t *ast_node)<br />
 <i>Get the single value of an RSL relation. </i><br />
 char * <code>globus_rsl_value_literal_get_string</code> (globus_rsl_value_t *literal_node)<br />
 <i>Get the string value of an RSL literal. </i><br />
 globus_list_t * <code>globus_rsl_value_sequence_get_value_list</code> (globus_rsl_value_t *sequence_node)<br />
 <i>Get the value list from an RSL value sequence. </i><br />
 globus_rsl_value_t * <code>globus_rsl_value_variable_get_sequence</code> (globus_rsl_value_t *variable_node)<br />
 <i>Get the value sequence from an RSL variable reference. </i><br />
 char * <code>globus_rsl_value_variable_get_name</code> (globus_rsl_value_t *variable_node)<br />
 <i>Get the name of an RSL variable reference. </i><br />
 char * <code>globus_rsl_value_variable_get_default</code> (globus_rsl_value_t *variable_node)<br />
 <i>Get the default value of an RSL variable reference. </i><br />
 globus_rsl_value_t * <code>globus_rsl_value_concatenation_get_left</code> (globus_rsl_value_t *concatenation_node)<br />
 <i>Get the left side of a concatenation value. </i><br />
 globus_rsl_value_t * <code>globus_rsl_value_concatenation_get_right</code> (globus_rsl_value_t *concatenation_node)<br />
 <i>Get the right side of a concatenation value. </i><br />
 globus_list_t ** <code>globus_rsl_value_sequence_get_list_ref</code> (globus_rsl_value_t *sequence_node)<br />
 <i>Get a reference to the list of values in a sequence. </i><br />
 int <code>globus_rsl_value_concatenation_set_left</code> (globus_rsl_value_t *concatenate_node, globus_rsl_value_t *new_left_node)<br />
 <i>Set the left-hand value of a concatenation. </i><br />
 int <code>globus_rsl_value_concatenation_set_right</code> (globus_rsl_value_t *concatenate_node, globus_rsl_value_t *new_right_node)<br />
 <i>Set the right-hand value of a concatenation. </i><br />
 int <code>globus_rsl_value_eval</code> (globus_rsl_value_t *ast_node, globus_symboltable_t *symbol_table, char **string_value, int rsl_substitute_flag)<br />
 <i>Evaluate RSL substitions in an RSL value node. </i><br />
 int <code>globus_rsl_eval</code> (globus_rsl_t *ast_node, globus_symboltable_t *symbol_table)<br />
 <i>Evaluate an RSL syntax tree. </i><br />
 int <code>globus_rsl_value_free</code> (globus_rsl_value_t *val)<br />
 <i>Free an RSL value node. </i><br />
 int <code>globus_rsl_free</code> (globus_rsl_t *ast_node)<br />
 <i>Free an RSL syntax tree node. </i><br />
 int <code>globus_rsl_value_free_recursive</code> (globus_rsl_value_t *globus_rsl_value_ptr)<br />
 <i>Free an RSL value and all its child nodes. </i><br />
 int <code>globus_rsl_free_recursive</code> (globus_rsl_t *ast_node)<br />
 <i>Free an RSL syntax tree and all its child nodes. </i><br />
 int <code>globus_rsl_value_print_recursive</code> (globus_rsl_value_t *globus_rsl_value_ptr)<br />
 <i>Print the value of a globus_rsl_value_t to standard output. </i><br />
 int <code>globus_rsl_print_recursive</code> (globus_rsl_t *ast_node)<br />
 <i>Print the value of an RSL syntax tree to standard output. </i><br />
 int <code>globus_rsl_value_variable_get_size</code> (globus_rsl_value_t *variable_node)<br />
 <i>Get the size of the value list within an RSL variable reference node. </i><br />
 globus_list_t * <code>globus_list_copy_reverse</code> (globus_list_t *orig)<br />
 <i>Create a reverse-order copy of a list. </i><br />
 int <code>globus_rsl_value_list_literal_replace</code> (globus_list_t *value_list, char *string_value)<br />
 <i>Replace the first value in a value list with a literal. </i><br />
 int <code>globus_rsl_value_list_param_get</code> (globus_list_t *ast_node_list, int required_type, char ***value, int *value_ctr)<br />
 <i>Get the values of an RSL value list. </i><br />
 int <code>globus_rsl_param_get</code> (globus_rsl_t *ast_node, int required_type, char *param, char ***values)<br />
 <i>Get the value strings for an RSL attribute. </i><br />
 globus_list_t * <code>globus_rsl_param_get_values</code> (globus_rsl_t *ast_node, char *param)<br />
 <i>Get the list of values for an RSL attribute. </i><br />
 globus_rsl_t * <code>globus_rsl_parse</code> (char *rsl_spec)<br />
 <i>Parse an RSL string. </i><br />
 char * <code>globus_rsl_unparse</code> (globus_rsl_t *rsl_spec)<br />
 <i>Convert an RSL parse tree to a string. </i><br />
 char * <code>globus_rsl_value_unparse</code> (globus_rsl_value_t *rsl_value)<br />
 <i>Convert an RSL value pointer to a string. </i></p>
<h2>Detailed Description</h2>
<p> Globus RSL Parsing. </p>
<h2>Function Documentation</h2>
<h3>globus_rsl_t* globus_rsl_parse (char *buf)</h3>
<p> Parse an RSL string. The <code>globus_rsl_parse()</code> function parses the string pointed to by the <i>buf</i> parameter into an RSL syntax tree. The caller is responsible for freeing that tree by calling <code>globus_rsl_free_recursive()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>buf</i> A NULL-terminated string that contains an RSL relation or boolean composition.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, the <code>globus_rsl_parse()</code> function returns the parse tree generated by processing its input. If an error occurs, <code>globus_rsl_parse()</code> returns NULL.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_rsl from the source code. </p>
<h2>Index</h2>
