---
title: "globus_rsl_free(3)"
name: "globus_rsl_free"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rsl_free/"
description: "RSL Memory Management –"
---

<h2 class="name">NAME</h2>
<p> RSL Memory Management &#8211; </p>
<h3>Functions</h3>
<p> globus_rsl_t * <code>globus_rsl_copy_recursive</code> (globus_rsl_t *ast_node)<br />
 <i>Create a deep copy of an RSL syntax tree. </i><br />
 globus_rsl_value_t * <code>globus_rsl_value_copy_recursive</code> (globus_rsl_value_t *globus_rsl_value_ptr)<br />
 <i>Create a deep copy of an RSL value. </i><br />
 int <code>globus_rsl_value_free</code> (globus_rsl_value_t *val)<br />
 <i>Free an RSL value node. </i><br />
 int <code>globus_rsl_free</code> (globus_rsl_t *ast_node)<br />
 <i>Free an RSL syntax tree node. </i><br />
 int <code>globus_rsl_value_free_recursive</code> (globus_rsl_value_t *globus_rsl_value_ptr)<br />
 <i>Free an RSL value and all its child nodes. </i><br />
 int <code>globus_rsl_free_recursive</code> (globus_rsl_t *ast_node)<br />
 <i>Free an RSL syntax tree and all its child nodes. </i><br />
 int <code>globus_rsl_value_list_literal_replace</code> (globus_list_t *value_list, char *string_value)<br />
 <i>Replace the first value in a value list with a literal. </i><br />
 int <code>globus_rsl_value_eval</code> (globus_rsl_value_t *ast_node, globus_symboltable_t *symbol_table, char **string_value, int rsl_substitution_flag)<br />
 <i>Evaluate RSL substitions in an RSL value node. </i><br />
 int <code>globus_rsl_eval</code> (globus_rsl_t *ast_node, globus_symboltable_t *symbol_table)<br />
 <i>Evaluate an RSL syntax tree. </i></p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>globus_rsl_t* globus_rsl_copy_recursive (globus_rsl_t *ast_node)</h3>
<p> Create a deep copy of an RSL syntax tree. The <code>globus_rsl_copy_recursive()</code> function performs a deep copy of the RSL syntax tree pointed to by the <i>ast_node</i> parameter. All RSL nodes, value nodes, variable names, attributes, and literals will be copied to the return value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast_node</i> An RSL syntax tree to copy.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_copy_recursive()</code> function returns a copy of its input parameter that that can be used after the <i>ast_node</i> and its values have been freed. If an error occurs, <code>globus_rsl_copy_recursive()</code> returns NULL.</dl>
<h3>int globus_rsl_eval (globus_rsl_t *ast_node, globus_symboltable_t *symbol_table)</h3>
<p> Evaluate an RSL syntax tree. The <code>globus_rsl_eval()</code> function modifies the RSL parse tree pointed to by its <i>ast_node</i> parameter by replacing all RSL substitution variable reference nodes with the literal values those variables evaluate to based on the current scope of the symbol table pointed to by the <i>symbol_table</i> parameter. It also combines string concatenations into literal string values. Any nodes which are replaced by this function are freed using <code>globus_rsl_value_free_recursive()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast_node</i> A pointer to the RSL syntax tree to evaluate.<br />
 <i>symbol_table</i> A symbol table containing current definitions of the RSL substitutions which can occur in this evaluation scope.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_eval()</code> returns <i>GLOBUS_SUCCESS</i>, and replaces all RSL substitution values and concatenations in <i>ast_node</i> or its child nodes with the evaluated forms described above. If an error occurs, <code>globus_rsl_eval()</code> returns a non-zero value.</dl>
<h3>int globus_rsl_free (globus_rsl_t *ast_node)</h3>
<p> Free an RSL syntax tree node. The <code>globus_rsl_free()</code> function frees the RSL syntax tree node pointed to by the <i>ast_node</i> parameter. This only frees the RSL syntax tree node itself, and not any boolean operands, relation names, or values associated with the node. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast_node</i> The RSL syntax tree node to free.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_value_free()</code> function always returns GLOBUS_SUCCESS.</dl>
<h3>int globus_rsl_free_recursive (globus_rsl_t *ast_node)</h3>
<p> Free an RSL syntax tree and all its child nodes. The <code>globus_rsl_free_recursive()</code> function frees the RSL syntax tree pointed to by the <i>ast_node</i> parameter, including all boolean operands, attribute names, and values. Any pointers to these are no longer valid after <code>globus_rsl_free_recursive()</code> returns. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast_node</i> An RSL parse tree to free.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_value_free_recursive()</code> function always returns GLOBUS_SUCCESS.</dl>
<h3>globus_rsl_value_t* globus_rsl_value_copy_recursive (globus_rsl_value_t *globus_rsl_value_ptr)</h3>
<p> Create a deep copy of an RSL value. The <code>globus_rsl_value_copy_recursive()</code> function performs a deep copy of the RSL value pointed to by the <i>globus_rsl_value_ptr</i> parameter. All variable names, attributes, literals, and value lists will be copied to the return value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>globus_rsl_value_ptr</i> A pointer to an RSL value to copy.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_value_copy_recursive()</code> function returns a copy of its input parameter that that can be used after the <i>globus_rsl_value_ptr</i> and its values have been freed. If an error occurs, <code>globus_rsl_value_copy_recursive()</code> returns NULL.</dl>
<h3>int globus_rsl_value_eval (globus_rsl_value_t *ast_node, globus_symboltable_t *symbol_table, char **string_value, intrsl_substitution_flag)</h3>
<p> Evaluate RSL substitions in an RSL value node. The <code>globus_rsl_value_eval()</code> function modifies the value pointed to by its <i>ast_node</i> parameter by replacing all RSL substitution variable reference nodes with the literal values those variables evaluate to based on the current scope of the symbol table pointed to by the <i>symbol_table</i> parameter. It also combines string concatenations into literal string values. Any nodes which are replaced by this function are freed using <code>globus_rsl_value_free_recursive()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>ast_node</i> A pointer to the RSL value node to evaluate.<br />
 <i>symbol_table</i> A symbol table containing current definitions of the RSL substitutions which can occur in this evaluation scope.<br />
 <i>string_value</i> An output parameter which is set to point to the value of the string returned by evaluating the value node pointed to by <i>ast_node</i> if it evaluates to a literal value. list pointed to by the <i>value_list</i> parameter.<br />
 <i>rsl_substitution_flag</i> A flag indicating whether the node pointed to by the <i>ast_node</i> parameter defines RSL substition variables.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_value_eval()</code> returns <i>GLOBUS_SUCCESS</i>, and replaces any RSL substitution values in the node pointed to by the <i>ast_node</i> parameter. If the node evaluates to a single literal, the <i>string_value</i> parameter is modified to point to the value of that literal. If an error occurs, <code>globus_rsl_value_eval()</code> returns a non-zero value.</dl>
<h3>int globus_rsl_value_free (globus_rsl_value_t *val)</h3>
<p> Free an RSL value node. The <code>globus_rsl_value_free()</code> function frees the RSL value pointed to by the <i>val</i> parameter. This only frees the RSL value node itself, and not any sequence or string values associated with that node. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>val</i> The RSL value node to free.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_value_free()</code> function always returns GLOBUS_SUCCESS.</dl>
<h3>int globus_rsl_value_free_recursive (globus_rsl_value_t *globus_rsl_value_ptr)</h3>
<p> Free an RSL value and all its child nodes. The <code>globus_rsl_free_recursive()</code> function frees the RSL value node pointed to by the <i>globus_rsl_value_ptr</i>, including all literal strings, variable names, and value sequences. Any pointers to these are no longer valid after <code>globus_rsl_value_free_recursive()</code> returns. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>globus_rsl_value_ptr</i> An RSL value node to free.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> The <code>globus_rsl_value_free_recursive()</code> function always returns GLOBUS_SUCCESS.</dl>
<h3>int globus_rsl_value_list_literal_replace (globus_list_t *value_list, char *string_value)</h3>
<p> Replace the first value in a value list with a literal. The <code>globus_rsl_value_list_literal_replace()</code> function replaces the first value in the list pointed to by the <i>value_list</i> parameter with a new value node that is a literal string node pointing to the value of the <i>string_value</i> parameter, freeing the old value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>value_list</i> The RSL value list to modify by replacing its first element.<br />
 <i>string_value</i> The new string value to use as a literal first element of the list pointed to by the <i>value_list</i> parameter.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Upon success, <code>globus_rsl_value_list_literal_replace()</code> returns <i>GLOBUS_SUCCESS</i>, frees the current first value of <i>value_list</i> and replaces it with a new literal string node pointing to the value of the <i>string_value</i> parameter. If an error occurs, <code>globus_rsl_value_list_literal_replace()</code> returns 1.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_rsl from the source code. </p>
<h2>Index</h2>
