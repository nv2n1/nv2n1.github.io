---
title: "globus_rsl_value_concatenation_get_left(3)"
name: "globus_rsl_value_concatenation_get_left"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rsl_value_concatenation_get_left/"
description: "RSL Accessor Functions –"
---

<h2 class="name">NAME</h2>
<p> RSL Accessor Functions &#8211; </p>
<h3>Functions</h3>
<p> int <code>globus_rsl_boolean_get_operator</code> (globus_rsl_t *ast_node)<br />
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
 int <code>globus_rsl_value_variable_get_size</code> (globus_rsl_value_t *variable_node)<br />
 <i>Get the size of the value list within an RSL variable reference node. </i><br />
 globus_rsl_value_t * <code>globus_rsl_value_concatenation_get_left</code> (globus_rsl_value_t *concatenation_node)<br />
 <i>Get the left side of a concatenation value. </i><br />
 globus_rsl_value_t * <code>globus_rsl_value_concatenation_get_right</code> (globus_rsl_value_t *concatenation_node)<br />
 <i>Get the right side of a concatenation value. </i><br />
 globus_list_t ** <code>globus_rsl_value_sequence_get_list_ref</code> (globus_rsl_value_t *sequence_node)<br />
 <i>Get a reference to the list of values in a sequence. </i></p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>globus_list_t* globus_rsl_boolean_get_operand_list (globus_rsl_t *ast_node)</h3>
<p> Get the RSL operand list from a boolean RSL composition. The <code>globus_rsl_boolean_get_operand_list()</code> function returns the list of RSL syntax tree nodes that is joined by a boolean composition. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast_node</i> The RSL syntax tree to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_boolean_get_operand_list()</code> returns a pointer to a list of RSL syntax tree nodes that are the operand of a boolean composition operation. If an error occurs, <code>globus_rsl_boolean_get_operand_list()</code> returns NULL.</dl>
<h3>globus_list_t** globus_rsl_boolean_get_operand_list_ref (globus_rsl_t *boolean_node)</h3>
<p> Get a reference to the RSL operand list from a boolean RSL composition. The <code>globus_rsl_boolean_get_operand_list_ref()</code> function returns a pointer to the list of RSL syntax tree nodes that is joined by a boolean composition. If this list is modified, then the value of boolean syntax tree is modified. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>boolean_node</i> The RSL syntax tree to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_boolean_get_operand_list_ref()</code> returns a pointer to the list pointer in the RSL syntax tree data structure. This list can be modified to change the oprands of the boolean operation. If an error occurs, <code>globus_rsl_boolean_get_operand_list_ref()</code> returns NULL.</dl>
<h3>int globus_rsl_boolean_get_operator (globus_rsl_t *ast_node)</h3>
<p> Get the RSL operator used in a boolean RSL composition. The <code>globus_rsl_boolean_get_operator()</code> function returns the operator that is used by the boolean RSL composition. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast_node</i> The RSL syntax tree to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_boolean_get_operator()</code> returns one of GLOBUS_RSL_AND, GLOBUS_RSL_OR, GLOBUS_RSL_MULTIREQ. If an error occurs, <code>globus_rsl_boolean_get_operator()</code> returns -1.</dl>
<h3>char* globus_rsl_relation_get_attribute (globus_rsl_t *ast_node)</h3>
<p> Get an RSL relation attribute name. The <code>globus_rsl_relation_get_attribute()</code> function returns a pointer to the name of the attribute in an RSL relation. This return value is a shallow reference to the attribute name. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast_node</i> The RSL relation node to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_relation_get_attribute()</code> returns a pointer to the name of the attribute of the relation. If an error occurs, <code>globus_rsl_relation_get_attribute()</code> returns NULL.</dl>
<h3>int globus_rsl_relation_get_operator (globus_rsl_t *ast_node)</h3>
<p> Get an RSL relation operator. The <code>globus_rsl_relation_get_operator()</code> function returns the operation type represented by the RSL relation node pointed to by the <i>ast_node</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast_node</i> The RSL relation node to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_relation_get_operator()</code> returns one of GLOBUS_RSL_EQ, GLOBUS_RSL_NEQ, GLOBUS_RSL_GT, GLOBUS_RSL_GTEQ, GLOBUS_RSL_LT, or GLOBUS_RSL_LTEQ. If an error occurs, <code>globus_rsl_relation_get_operator()</code> returns -1.</dl>
<h3>globus_rsl_value_t* globus_rsl_relation_get_single_value (globus_rsl_t *ast_node)</h3>
<p> Get the single value of an RSL relation. The <code>globus_rsl_relation_get_single_value()</code> function returns the value of an RSL relation node pointed to by the <i>ast_node</i> parameter if the value is a sequence of one value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast_node</i> The RSL relation node to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_relation_get_single_value()</code> returns the value pointer at the head of the RSL relation pointed to by the <i>ast_node</i> parameter. If the value sequence has more than one value or the <i>ast_node</i> points to an RSL syntax tree that is not a relation, <code>globus_rsl_relation_get_value_sequence()</code> returns NULL.</dl>
<h3>globus_rsl_value_t* globus_rsl_relation_get_value_sequence (globus_rsl_t *ast_node)</h3>
<p> Get the value of an RSL relation. The <code>globus_rsl_relation_get_value_sequence()</code> function returns the value of an RSL relation node pointed to by the <i>ast_node</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast_node</i> The RSL relation node to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_relation_get_value_sequence()</code> returns the value sequence pointer in the RSL relation pointed to by the <i>ast_node</i> parameter. If an error occurs, <code>globus_rsl_relation_get_value_sequence()</code> returns NULL.</dl>
<h3>globus_rsl_value_t* globus_rsl_value_concatenation_get_left (globus_rsl_value_t *concatenation_node)</h3>
<p> Get the left side of a concatenation value. The <code>globus_rsl_value_concatenation_get_left()</code> function returns the left side of an RSL value concatenation pointed to by the <i>concatenation_node</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>concatenation_node</i> The RSL concatenation node to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_value_concatenation_get_left()</code> returns a pointer to the left value of the concatenation values pointed to by the <i>concatenation_node</i> parameter. If an error occurs, <code>globus_rsl_value_concatenation_get_left()</code> returns NULL.</dl>
<h3>globus_rsl_value_t* globus_rsl_value_concatenation_get_right (globus_rsl_value_t *concatenation_node)</h3>
<p> Get the right side of a concatenation value. The <code>globus_rsl_value_concatenation_get_right()</code> function returns the right side of an RSL value concatenation pointed to by the <i>concatenation_node</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>concatenation_node</i> The RSL concatenation node to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_value_concatenation_get_right()</code> returns a pointer to the right value of the concatenation values pointed to by the <i>concatenation_node</i> parameter. If an error occurs, <code>globus_rsl_value_concatenation_get_right()</code> returns NULL.</dl>
<h3>char* globus_rsl_value_literal_get_string (globus_rsl_value_t *literal_node)</h3>
<p> Get the string value of an RSL literal. The <code>globus_rsl_value_literal_get_string()</code> function returns the string value of an RSL literal node pointed to by the <i>literal_node</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>literal_node</i> The RSL literal node to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_value_literal_get_string()</code> returns a pointer to the string value of the literal pointed to by the <i>literal_node</i> parameter. If the value is not a literal, <code>globus_rsl_value_literal_get_string()</code> returns NULL.</dl>
<h3>globus_list_t** globus_rsl_value_sequence_get_list_ref (globus_rsl_value_t *sequence_node)</h3>
<p> Get a reference to the list of values in a sequence. The <code>globus_rsl_value_sequence_get_list_ref()</code> function returns a reference to the list of values in a value sequence. Any changes to the elements of this list will affect the <i>sequence_node</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sequence_node</i> The RSL sequence node to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_value_sequence_get_list_ref()</code> returns a pointer to the list of the globus_rsl_value_t pointer values contained in the <i>sequence_node</i> parameter. If an error occurs, <code>globus_rsl_value_sequence_get_list_ref()</code> returns NULL.</dl>
<h3>globus_list_t* globus_rsl_value_sequence_get_value_list (globus_rsl_value_t *sequence_node)</h3>
<p> Get the value list from an RSL value sequence. The <code>globus_rsl_value_sequence_get_value_list()</code> function returns the list of globus_rsl_value_t pointer values associated with the RSL value sequence pointed to by the <i>sequence_node</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>sequence_node</i> The RSL sequence node to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_value_sequence_get_value_list()</code> returns a pointer to the list of values pointed to by the <i>sequence_node</i> parameter. If the value is not a sequence, <code>globus_rsl_value_literal_get_string()</code> returns NULL.</dl>
<h3>char* globus_rsl_value_variable_get_default (globus_rsl_value_t *variable_node)</h3>
<p> Get the default value of an RSL variable reference. The <code>globus_rsl_value_variable_get_default()</code> function returns a pointer to the default value of the RSL variable pointed to by the <i>variable_node</i> parameter to use if the variable&#8217;s name is not bound in the current evaluation context. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>variable_node</i> The RSL variable node to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_value_variable_get_default()</code> returns a pointer to the string containing the default value of the variable referenced by the <i>variable_node</i> parameter. If the node is not a variable reference or no default value exists in the RSL node, <code>globus_rsl_value_variable_get_default()</code> returns NULL.</dl>
<h3>char* globus_rsl_value_variable_get_name (globus_rsl_value_t *variable_node)</h3>
<p> Get the name of an RSL variable reference. The <code>globus_rsl_value_variable_get_name()</code> function returns a pointer to the name of the RSL variable name pointed to by the <i>variable_node</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>variable_node</i> The RSL variable node to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_value_variable_get_name()</code> returns a pointer to the string containing the name of the variable referenced by the <i>variable_node</i> parameter. If the node is not a variable reference, <code>globus_rsl_value_variable_get_sequence()</code> returns NULL.</dl>
<h3>globus_rsl_value_t* globus_rsl_value_variable_get_sequence (globus_rsl_value_t *variable_node)</h3>
<p> Get the value sequence from an RSL variable reference. The <code>globus_rsl_value_variable_get_sequence()</code> function returns the sequence value associated with the RSL variable reference pointed to by the <i>variable_node</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>variable_node</i> The RSL variable node to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_value_variable_get_sequence()</code> returns a pointer to the rsl value sequence pointed to by the <i>variable_node</i> parameter. If the value is not a variable reference, <code>globus_rsl_value_variable_get_sequence()</code> returns NULL.</dl>
<h3>int globus_rsl_value_variable_get_size (globus_rsl_value_t *variable_node)</h3>
<p> Get the size of the value list within an RSL variable reference node. The <code>globus_rsl_value_variable_get_size()</code> function returns the number of nodes in the RSL variable reference node pointed to by the <i>variable_node</i> parameter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>variable_node</i> The RSL variable node to inspect.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_value_variable_get_size()</code> returns the list of values within a RSL variable reference, or -1 if the node pointed to by <i>variable_node</i> is not a variable reference. If the return value is 1, then the variable has no default value included in the reference.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_rsl from the source code. </p>
<h2>Index</h2>
