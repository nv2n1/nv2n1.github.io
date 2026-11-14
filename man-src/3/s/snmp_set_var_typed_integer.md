---
title: "snmp_set_var_typed_integer(3)"
name: "snmp_set_var_typed_integer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-snmp_set_var_typed_integer/"
description: "snmp_pdu_add_variable, snmp_varlist_add_variable, snmp_add_null_var, snmp_clone_varbind, snmp_set_var_objid, snmp_set_var_value, snmp_set_var_typed_value, snmp_set_var_typed_integer, print_variable..."
---

<p>snmp_pdu_add_variable, snmp_varlist_add_variable, snmp_add_null_var, snmp_clone_varbind, snmp_set_var_objid, snmp_set_var_value, snmp_set_var_typed_value, snmp_set_var_typed_integer, print_variable, fprint_variable, snprint_variable, print_value, fprint_value, snprint_value, snmp_free_var, snmp_free_varbind &#8211; netsnmp_varbind_api functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;net-snmp/varbind_api.h&gt;


Creation</code></pre>
<p> <code>netsnmp_variable_list *snmp_pdu_add_variable(</code><br />
 <code> netsnmp_pdu *</code><i>pdu</i><code>,</code><br />
 <code> const oid *</code><i>objid</i><code>, size_t </code><i>objidlen</i><code>,</code><br />
 <code> u_char </code><i>type</i><code>, const void *</code><i>value</i><code>, size_t </code><i>len</i><code>);</code><br />
 <code>netsnmp_variable_list *snmp_varlist_add_variable(</code><br />
 <code> netsnmp_variable_list *</code><i>varlist</i><code>,</code><br />
 <code> const oid *</code><i>objid</i><code>, size_t </code><i>objidlen</i><code>,</code><br />
 <code> u_char </code><i>type</i><code>, const void *</code><i>value</i><code>, size_t </code><i>len</i><code>);</code><br />
 <code>netsnmp_variable_list *snmp_add_null_var(</code><br />
 <code> netsnmp_pdu *</code><i>pdu</i><code>,</code><br />
 <code> const oid *</code><i>objid</i><code>, size_t </code><i>objidlen</i><code>);</code> <code>netsnmp_variable_list *snmp_clone_varbind(</code><br />
 <code> netsnmp_variable_list *</code><i>varlist</i><code>);</code></p>
<h3>Setting Values</h3>
<p><code>int snmp_set_var_objid( netsnmp_variable_list* </code><i>variable</i><code>,</code><br />
 <code> const oid * </code><i>objid</i><code>, size_t </code><i>objidlen</i><code>);</code><br />
 <code>int snmp_set_var_value( netsnmp_variable_list* </code><i>variable</i><code>,</code><br />
 <code> const void * </code><i>value</i><code>, size_t </code><i>vallen</i><code>);</code><br />
 <code>int snmp_set_var_typed_value( netsnmp_variable_list* </code><i>variable</i><code>,</code><br />
 <code> u_char </code><i>type</i><code>,</code><br />
 <code> const void * </code><i>value</i><code>, size_t </code><i>vallen</i><code>);</code><br />
 <code>int snmp_set_var_typed_integer( netsnmp_variable_list* </code><i>variable</i><code>,</code><br />
 <code> u_char </code><i>type</i><code>, long </code><i>value</i><code>);</code></p>
<h3>Output</h3>
<p>void print_variable(const oid *objid, size_t objidlen,</p>
<p>                    const netsnmp_variable_list *variable);</p>
<p>void fprint_variable(FILE *fp,</p>
<p>                     const oid *objid, size_t objidlen,</p>
<p>                     const netsnmp_variable_list *variable);</p>
<p>int snprint_variable(char *buf, size_t len,</p>
<p>                     const oid *objid, size_t objidlen,</p>
<p>                     const netsnmp_variable_list *variable); <code>void print_value(const oid *</code><i>objid</i><code>, size_t </code><i>objidlen</i><code>,</code><br />
 <code> const netsnmp_variable_list *</code><i>variable</i><code>);</code><br />
 <code>void fprint_value(FILE *</code><i>fp</i><code>,</code><br />
 <code> const oid *</code><i>objid</i><code>, size_t </code><i>objidlen</i><code>,</code><br />
 <code> const netsnmp_variable_list *</code><i>variable</i><code>);</code><br />
 <code>int snprint_value(char *</code><i>buf</i><code>, size_t </code><i>len</i><code>,</code><br />
 <code> const oid *</code><i>objid</i><code>, size_t </code><i>objidlen</i><code>,</code><br />
 <code> const netsnmp_variable_list *</code><i>variable</i><code>);</code></p>
<h3>Deletion</h3>
<p>void snmp_free_var(netsnmp_variable_list *variable);</p>
<p>void snmp_free_varbind(netsnmp_variable_list *variables);</p>
<h2>Description</h2>
<p>The functions dealing with variable bindings fall into four groups &#8211; dealing with the creation, setting of values, output and deletion of varbinds.</p>
<h3>Creation</h3>
<p><code>snmp_pdu_add_variable</code> will create a new varbind structure, initialised with the name ( <i>objid</i>, <i>objidlen</i> ), syntax ( <i>type</i> ) and value ( <i>value , len</i> ) provided. This varbind is then added to the end of the varbind list in the given PDU. </p>
<pre><code>snmp_varlist_add_variable

is similar, but appends the new varbind to the end of the
varbind list provided.
When adding the first varbind to an empty list, simply
pass the address of the head of the list:


netsnmp_variable_list *vl = NULL;
snmp_varlist_add_variable(
&amp;vl, name1, name1_len,
ASN_TYPE, &amp;val1, val1_len);
snmp_varlist_add_variable(
&amp;vl, name2, name2_len,
ASN_TYPE, &amp;val2, val2_len);</code></pre>
<p> In both cases, the routine will return a pointer to the new varbind structure (or NULL if the varbind creation fails). <code>snmp_add_null_var</code> is a convenience function to add an empty varbind to the PDU. without needing to specify the NULL value explicitly. This is the normal mechanism for constructing a GET (or similar) information retrieval request.<br />
 Again, this returns a pointer to the new varbind, or NULL. <code>snmp_clone_varbind</code> creates a copy of each varbind in the specified list, returning a pointer to the head of the new list (or NULL if the cloning fails).</p>
<h3>Setting of values</h3>
<p><code>snmp_set_var_objid</code> sets the name of the varbind structure to the specified OID.<br />
 <code>snmp_set_var_typed_value</code> sets the syntax type and value of the varbind structure.<br />
 <code>snmp_set_var_value</code> sets the value of the varbind structure, leaving the syntax type unchanged.<br />
 <code>snmp_set_var_typed_integer</code> is a convenience function to set the syntax type and value for a 32-bit integer-based varbind. All four of these return 0 if the assignment is successful, or 1 if it is not.</p>
<h3>Output</h3>
<p><code>print_variable</code> will take an object identifier (as returned by <code>read_objid</code>, <code>snmp_parse_oid</code> or <code>get_module_node</code>) and an instance of such a variable, and prints to the standard output the textual form of the object identifier together with the value of the variable. <code>fprint_variable</code> does the same, but prints to the FILE pointer specified by the initial parameter. <code>snprint_variable</code> prints the same information into the buffer pointed to by <i>buf</i> which is of length <i>len</i>. It returns the number of characters printed, or -1 if the buffer was not large enough. In the latter case, <i>buf</i> will typically contained a truncated version of the information (but this behaviour is not guaranteed). This function replaces the obsolete function <code>sprint_variable</code>. <code>print_value</code>, <code>fprint_value</code>, and <code>snprint_value</code> do the same as the equivalent <code>print_variable</code> routines, but only displaying the value of the variable, without the corresponding object identifier. For displaying the OID of a varbind, see <code><a href="/docs/linux/man/3-min_api/">min_api</a></code>(3).</p>
<h3>Deletion</h3>
<p><code>snmp_free_var</code> releases all memory used by the given varbind structure.<br />
 <code>snmp_free_varbind</code> releases all memory used by each varbind structure in the varbind list provided.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pdu_api/">pdu_api</a></code>(3) <code><a href="/docs/linux/man/3-mib_api/">mib_api</a></code>(3) </p>
