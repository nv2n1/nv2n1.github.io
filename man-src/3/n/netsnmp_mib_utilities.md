---
title: "netsnmp_mib_utilities(3)"
name: "netsnmp_mib_utilities"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_mib_utilities/"
description: "mib parsing and datatype manipulation routines. –"
---

<p>mib parsing and datatype manipulation routines. &#8211;</p>
<h3>Data Structures</h3>
<pre><code>struct _PrefixList



struct parse_hints



Typedefs</code></pre>
<p> typedef <code>_PrefixList</code> * <code>PrefixListPtr</code> </p>
<p> typedef <code>_PrefixList</code> <code>PrefixList</code></p>
<h3>Enumerations</h3>
<p>enum inet_address_type { IPV4 =  1, IPV6 =  2, IPV4Z =  3, IPV6Z =  4, DNS =  16 }</p>
<p>Functions<br />
 int <code>_sprint_hexstring_line</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const u_char *cp, size_t line_len)<br />
 <i>Prints a hexadecimal string into a buffer. </i><br />
 int <code>sprint_realloc_hexstring</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const u_char *cp, size_t len) </p>
<p> int <code>sprint_realloc_asciistring</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const u_char *cp, size_t len)<br />
 <i>Prints an ascii string into a buffer. </i><br />
 int <code>sprint_realloc_octet_string</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)<br />
 <i>Prints an octet string into a buffer. </i><br />
 int <code>sprint_realloc_counter64</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)<br />
 <i>Prints a counter into a buffer. </i><br />
 int <code>sprint_realloc_opaque</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)<br />
 <i>Prints an object identifier into a buffer. </i><br />
 int <code>sprint_realloc_object_identifier</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)<br />
 <i>Prints an object identifier into a buffer. </i><br />
 int <code>sprint_realloc_timeticks</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)<br />
 <i>Prints a timetick variable into a buffer. </i><br />
 int <code>sprint_realloc_hinted_integer</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, long val, const char decimaltype, const char *hint, const char *units)<br />
 <i>Prints an integer according to the hint into a buffer. </i><br />
 int <code>sprint_realloc_integer</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)<br />
 <i>Prints an integer into a buffer. </i><br />
 int <code>sprint_realloc_uinteger</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)<br />
 <i>Prints an unsigned integer into a buffer. </i><br />
 int <code>sprint_realloc_gauge</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)<br />
 <i>Prints a gauge value into a buffer. </i><br />
 int <code>sprint_realloc_counter</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)<br />
 <i>Prints a counter value into a buffer. </i><br />
 int <code>sprint_realloc_networkaddress</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)<br />
 <i>Prints a network address into a buffer. </i><br />
 int <code>sprint_realloc_ipaddress</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)<br />
 <i>Prints an ip-address into a buffer. </i><br />
 int <code>sprint_realloc_null</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)<br />
 <i>Prints a null value into a buffer. </i><br />
 int <code>sprint_realloc_bitstring</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)<br />
 <i>Prints a bit string into a buffer. </i><br />
 int <code>sprint_realloc_nsapaddress</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>sprint_realloc_badtype</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)<br />
 <i>Fallback routine for a bad type, prints &#8216;Variable has bad type&#8217; into a buffer. </i><br />
 int <code>sprint_realloc_by_type</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)<br />
 <i>Universal print routine, prints a variable into a buffer according to the variable type. </i><br />
 <code>tree</code> * <code>get_tree_head</code> (void)<br />
 <i>Retrieves the tree head. </i><br />
 char * <code>snmp_out_toggle_options</code> (char *options) </p>
<p> void <code>snmp_out_toggle_options_usage</code> (const char *lead, FILE *outf) </p>
<p> char * <code>snmp_in_options</code> (char *optarg, int argc, char *const *argv) </p>
<p> char * <code>snmp_in_toggle_options</code> (char *options) </p>
<p> void <code>snmp_in_toggle_options_usage</code> (const char *lead, FILE *outf)<br />
 <i>Prints out a help usage for the in* toggle options. </i><br />
 void <code>register_mib_handlers</code> (void) </p>
<p> void <code>netsnmp_set_mib_directory</code> (const char *dir) </p>
<p> char * <code>netsnmp_get_mib_directory</code> (void) </p>
<p> void <code>netsnmp_fixup_mib_directory</code> (void) </p>
<p> void <code>netsnmp_init_mib</code> (void)<br />
 <i>Initialises the mib reader. </i><br />
 void <code>init_mib</code> (void) </p>
<p> void <code>shutdown_mib</code> (void)<br />
 <i>Unloads all mibs. </i><br />
 void <code>print_mib</code> (FILE *fp)<br />
 <i>Prints the MIBs to the file fp. </i><br />
 void <code>print_ascii_dump</code> (FILE *fp) </p>
<p> void <code>set_function</code> (struct <code>tree</code> *subtree)<br />
 <i>Set&#8217;s the printing function printomat in a subtree according it&#8217;s type. </i><br />
 int <code>read_objid</code> (const char *input, oid *output, size_t *out_len)<br />
 <i>Reads an object identifier from an input string into internal OID form. </i><br />
 void <code>netsnmp_sprint_realloc_objid</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, int *buf_overflow, const oid *objid, size_t objidlen) </p>
<p> <code>tree</code> * <code>netsnmp_sprint_realloc_objid_tree</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, int *buf_overflow, const oid *objid, size_t objidlen) </p>
<p> int <code>sprint_realloc_objid</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const oid *objid, size_t objidlen) </p>
<p> int <code>snprint_objid</code> (char *buf, size_t buf_len, const oid *objid, size_t objidlen) </p>
<p> void <code>print_objid</code> (const oid *objid, size_t objidlen)<br />
 <i>Prints an oid to stdout. </i><br />
 void <code>fprint_objid</code> (FILE *f, const oid *objid, size_t objidlen)<br />
 <i>Prints an oid to a file descriptor. </i><br />
 int <code>sprint_realloc_variable</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const oid *objid, size_t objidlen, const <code>netsnmp_variable_list</code> *<code>variable</code>) </p>
<p> int <code>snprint_variable</code> (char *buf, size_t buf_len, const oid *objid, size_t objidlen, const <code>netsnmp_variable_list</code> *<code>variable</code>) </p>
<p> void <code>print_variable</code> (const oid *objid, size_t objidlen, const <code>netsnmp_variable_list</code> *<code>variable</code>)<br />
 <i>Prints a variable to stdout. </i><br />
 void <code>fprint_variable</code> (FILE *f, const oid *objid, size_t objidlen, const <code>netsnmp_variable_list</code> *<code>variable</code>)<br />
 <i>Prints a variable to a file descriptor. </i><br />
 int <code>sprint_realloc_value</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, const oid *objid, size_t objidlen, const <code>netsnmp_variable_list</code> *<code>variable</code>) </p>
<p> int <code>snprint_value</code> (char *buf, size_t buf_len, const oid *objid, size_t objidlen, const <code>netsnmp_variable_list</code> *<code>variable</code>) </p>
<p> void <code>print_value</code> (const oid *objid, size_t objidlen, const <code>netsnmp_variable_list</code> *<code>variable</code>) </p>
<p> void <code>fprint_value</code> (FILE *f, const oid *objid, size_t objidlen, const <code>netsnmp_variable_list</code> *<code>variable</code>) </p>
<p> int <code>build_oid_segment</code> (<code>netsnmp_variable_list</code> *var)<br />
 <i>Takes the value in VAR and turns it into an OID segment in var-&gt;name. </i><br />
 int <code>build_oid_noalloc</code> (oid *in, size_t in_len, size_t *out_len, oid *prefix, size_t prefix_len, <code>netsnmp_variable_list</code> *indexes) </p>
<p> int <code>build_oid</code> (oid **out, size_t *out_len, oid *prefix, size_t prefix_len, <code>netsnmp_variable_list</code> *indexes) </p>
<p> int <code>parse_oid_indexes</code> (oid *oidIndex, size_t oidLen, <code>netsnmp_variable_list</code> *data) </p>
<p> int <code>parse_one_oid_index</code> (oid **oidStart, size_t *oidLen, <code>netsnmp_variable_list</code> *data, int complete) </p>
<p> int <code>dump_realloc_oid_to_inetaddress</code> (const int addr_type, const oid *objid, size_t objidlen, u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, char quotechar) </p>
<p> int <code>dump_realloc_oid_to_string</code> (const oid *objid, size_t objidlen, u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, char quotechar) </p>
<p> <code>tree</code> * <code>get_tree</code> (const oid *objid, size_t objidlen, struct <code>tree</code> *subtree) </p>
<p> void <code>print_description</code> (oid *objid, size_t objidlen, int width)<br />
 <i>Prints on oid description on stdout. </i><br />
 void <code>fprint_description</code> (FILE *f, oid *objid, size_t objidlen, int width)<br />
 <i>Prints on oid description into a file descriptor. </i><br />
 int <code>snprint_description</code> (char *buf, size_t buf_len, oid *objid, size_t objidlen, int width) </p>
<p> int <code>sprint_realloc_description</code> (u_char **buf, size_t *buf_len, size_t *out_len, int allow_realloc, oid *objid, size_t objidlen, int width) </p>
<p> int <code>get_module_node</code> (const char *fname, const char *<code>module</code>, oid *objid, size_t *objidlen) </p>
<p> int <code>get_wild_node</code> (const char *name, oid *objid, size_t *objidlen)<br />
 <i></i><code>See also:</code></p>
<dl>
<dd>comments on find_best_tree_node for usage after first time.</dl>
<p> &quot;<br />
 int <code>get_node</code> (const char *name, oid *objid, size_t *objidlen) </p>
<p> void <code>clear_tree_flags</code> (register struct <code>tree</code> *tp) </p>
<p> void <code>print_oid_report</code> (FILE *fp) </p>
<p> void <code>print_oid_report_enable_labeledoid</code> (void) </p>
<p> void <code>print_oid_report_enable_oid</code> (void) </p>
<p> void <code>print_oid_report_enable_suffix</code> (void) </p>
<p> void <code>print_oid_report_enable_symbolic</code> (void) </p>
<p> void <code>print_oid_report_enable_mibchildoid</code> (void) </p>
<p> char * <code>uptime_string</code> (u_long timeticks, char *buf)<br />
 <i>Converts timeticks to hours, minutes, seconds string. </i><br />
 char * <code>uptime_string_n</code> (u_long timeticks, char *buf, size_t buflen) </p>
<p> oid * <code>snmp_parse_oid</code> (const char *argv, oid *root, size_t *rootlen)<br />
 <i>Given a string, parses an oid out of it (if possible). </i><br />
 const char * <code>parse_octet_hint</code> (const char *hint, const char *value, unsigned char **new_val, int *new_val_len) </p>
<p> u_char <code>mib_to_asn_type</code> (int mib_type) </p>
<p> int <code>netsnmp_str2oid</code> (const char *S, oid *O, int L)<br />
 <i>Converts a string to its OID form. </i><br />
 int <code>netsnmp_oid2chars</code> (char *C, int L, const oid *O)<br />
 <i>Converts an OID to its character form. </i><br />
 int <code>netsnmp_oid2str</code> (char *S, int L, oid *O)<br />
 <i>Converts an OID to its string form. </i><br />
 int <code>snprint_by_type</code> (char *buf, size_t buf_len, <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>snprint_hexstring</code> (char *buf, size_t buf_len, const u_char *cp, size_t len) </p>
<p> int <code>snprint_asciistring</code> (char *buf, size_t buf_len, const u_char *cp, size_t len) </p>
<p> int <code>snprint_octet_string</code> (char *buf, size_t buf_len, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>snprint_opaque</code> (char *buf, size_t buf_len, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>snprint_object_identifier</code> (char *buf, size_t buf_len, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>snprint_timeticks</code> (char *buf, size_t buf_len, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>snprint_hinted_integer</code> (char *buf, size_t buf_len, long val, const char *hint, const char *units) </p>
<p> int <code>snprint_integer</code> (char *buf, size_t buf_len, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>snprint_uinteger</code> (char *buf, size_t buf_len, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>snprint_gauge</code> (char *buf, size_t buf_len, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>snprint_counter</code> (char *buf, size_t buf_len, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>snprint_networkaddress</code> (char *buf, size_t buf_len, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>snprint_ipaddress</code> (char *buf, size_t buf_len, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>snprint_null</code> (char *buf, size_t buf_len, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>snprint_bitstring</code> (char *buf, size_t buf_len, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>snprint_nsapaddress</code> (char *buf, size_t buf_len, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>snprint_counter64</code> (char *buf, size_t buf_len, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units) </p>
<p> int <code>snprint_badtype</code> (char *buf, size_t buf_len, const <code>netsnmp_variable_list</code> *var, const struct <code>enum_list</code> *enums, const char *hint, const char *units)</p>
<h3>Variables</h3>
<pre><code>tree * tree_head



tree * Mib



oid RFC1213_MIB [] = { 1, 3, 6, 1, 2, 1 }



PrefixList mib_prefixes []</code></pre>
<h2>Function Documentation</h2>
<h3>int _sprint_hexstring_line (u_char ** buf, size_t * buf_len, size_t * out_len, int allow_realloc, const u_char * cp, size_t line_len)</h3>
<p>Prints a hexadecimal string into a buffer. </p>
<p> The characters pointed by *cp are encoded as hexadecimal string. </p>
<p> If allow_realloc is true the buffer will be (re)allocated to fit in the needed size. (Note: *buf may change due to this.) </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>buf</i> address of the buffer to print to.<br />
 <i>buf_len</i> address to an integer containing the size of buf.<br />
 <i>out_len</i> incremented by the number of characters printed.<br />
 <i>allow_realloc</i> if not zero reallocate the buffer to fit the needed size.<br />
 <i>cp</i> the array of characters to encode.<br />
 <i>line_len</i> the array length of cp.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>1 on success, or 0 on failure (out of memory, or buffer to small when not allowed to realloc.)</dl>
<p> Definition at line 271 of file mib.c. </p>
<p> References netsnmp_ds_get_boolean(), and snmp_realloc(). </p>
<p> Referenced by sprint_realloc_hexstring().</p>
<h3>int build_oid (oid ** out, size_t * out_len, oid * prefix, size_t prefix_len, <code>netsnmp_variable_list</code> * indexes)</h3>
<p>Definition at line 3578 of file mib.c. </p>
<p> References build_oid_noalloc(), tree::indexes, and snmp_clone_mem(). </p>
<p> Referenced by _netsnmp_tdata_generate_index_oid(), netsnmp_table_build_oid(), and netsnmp_table_data_generate_index_oid().</p>
<h3>int build_oid_segment (<code>netsnmp_variable_list</code> * var)</h3>
<p>Takes the value in VAR and turns it into an OID segment in var-&gt;name. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>var</i> The variable.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>SNMPERR_SUCCESS or SNMPERR_GENERR</dl>
<p> Definition at line 3442 of file mib.c. </p>
<p> References netsnmp_vardata::integer, variable_list::name, variable_list::name_length, variable_list::name_loc, NULL, netsnmp_vardata::objid, SNMP_FREE, netsnmp_vardata::string, variable_list::type, variable_list::val, and variable_list::val_len. </p>
<p> Referenced by build_oid_noalloc().</p>
<h3>void fprint_description (FILE * f, oid * objid, size_t objidlen, int width)</h3>
<p>Prints on oid description into a file descriptor. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>f</i> The file descriptor to print to.<br />
 <i>objid</i> The object identifier.<br />
 <i>objidlen</i> The object id length.<br />
 <i>width</i> Number of subidentifiers.</dl>
<p> Definition at line 4437 of file mib.c. </p>
<p> References NULL, SNMP_FREE, and sprint_realloc_description(). </p>
<p> Referenced by print_description().</p>
<h3>void fprint_objid (FILE * f, const oid * objid, size_t objidlen)</h3>
<p>Prints an oid to a file descriptor. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>f</i> The file descriptor to print to.<br />
 <i>objid</i> The oid to print<br />
 <i>objidlen</i> The length of oidid.</dl>
<p> Definition at line 3163 of file mib.c. </p>
<p> References netsnmp_sprint_realloc_objid_tree(), NULL, and SNMP_FREE. </p>
<p> Referenced by print_objid().</p>
<h3>void fprint_variable (FILE * f, const oid * objid, size_t objidlen, const <code>netsnmp_variable_list</code> * variable)</h3>
<p>Prints a variable to a file descriptor. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>f</i> The file descriptor to print to.<br />
 <i>objid</i> The object id.<br />
 <i>objidlen</i> The length of teh object id.<br />
 <i>variable</i> The variable to print.</dl>
<p> Definition at line 3317 of file mib.c. </p>
<p> References NULL, SNMP_FREE, and sprint_realloc_variable(). </p>
<p> Referenced by print_variable().</p>
<h3>struct <code>tree</code>* get_tree_head (void)</h3>
<p>Retrieves the tree head. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>the tree head.</dl>
<p> Definition at line 2017 of file mib.c. </p>
<p> References tree_head. </p>
<p> Referenced by netsnmp_config_parse_table_set(), and snmp_add_var().</p>
<h3>int get_wild_node (const char * name, oid * objid, size_t * objidlen)</h3>
<p><code>See also:</code></p>
<dl>
<dd>comments on find_best_tree_node for usage after first time.</dl>
<p> Definition at line 5457 of file mib.c. </p>
<p> References get_node(), tree::label, NULL, and tree_head. </p>
<p> Referenced by snmp_parse_oid().</p>
<h3>void netsnmp_fixup_mib_directory (void)</h3>
<p>Definition at line 2479 of file mib.c. </p>
<p> References netsnmp_get_mib_directory(), netsnmp_getenv(), netsnmp_set_mib_directory(), NULL, and SNMP_FREE. </p>
<p> Referenced by netsnmp_init_mib().</p>
<h3>char* netsnmp_get_mib_directory (void)</h3>
<p>Definition at line 2432 of file mib.c. </p>
<p> References netsnmp_ds_get_string(), netsnmp_getenv(), netsnmp_set_mib_directory(), and NULL. </p>
<p> Referenced by netsnmp_fixup_mib_directory(), and netsnmp_init_mib().</p>
<h3>void netsnmp_init_mib (void)</h3>
<p>Initialises the mib reader. </p>
<p> Reads in all settings from the environment. </p>
<p> Definition at line 2526 of file mib.c. </p>
<p> References tree::child_list, tree::label, _PrefixList::len, Mib, mib_prefixes, netsnmp_fixup_mib_directory(), netsnmp_get_mib_directory(), netsnmp_getenv(), NULL, SNMP_FREE, _PrefixList::str, and tree_head. </p>
<p> Referenced by init_mib(), and init_snmp().</p>
<h3>int netsnmp_oid2chars (char * C, int L, const oid * O)</h3>
<p>Converts an OID to its character form. </p>
<p> in example 5 . 1 . 2 . 3 . 4 . 5 = 12345 </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>C</i> The character buffer.<br />
 <i>L</i> The length of the buffer.<br />
 <i>O</i> The oid.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 on Sucess, 1 on failure.</dl>
<p> length </p>
<p> Definition at line 6244 of file mib.c. </p>
<p> Referenced by netsnmp_oid2str().</p>
<h3>int netsnmp_oid2str (char * S, int L, oid * O)</h3>
<p>Converts an OID to its string form. </p>
<p> in example 5 . &#8216;h&#8217; . &#8216;e&#8217; . &#8216;l&#8217; . &#8216;l&#8217; . &#8216;o&#8217; = &#8216;hello
