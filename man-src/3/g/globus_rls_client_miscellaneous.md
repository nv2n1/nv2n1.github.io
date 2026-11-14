---
title: "globus_rls_client_miscellaneous(3)"
name: "globus_rls_client_miscellaneous"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rls_client_miscellaneous/"
description: "Miscellaneous –"
---

<h2 class="name">NAME</h2>
<p> Miscellaneous &#8211; </p>
<p> Miscellaneous functions and types.</p>
<h3>Data Structures</h3>
<p> struct <code>globus_rls_attribute_t</code><br />
 <i>Object (LFN or PFN) attribute type. </i><br />
 struct <code>globus_rls_stats_t</code><br />
 <i>Various configuration options and statistics about an RLS server returned in the following structures by </i><code>globus_rls_client_stats()</code>.</p>
<h3>Defines</h3>
<p> #define <code>RLS_LRCSERVER</code> 0x1 </p>
<p> #define <code>RLS_RLISERVER</code> 0x2 </p>
<p> #define <code>RLS_RCVLFNLIST</code> 0x4 </p>
<p> #define <code>RLS_RCVBLOOMFILTER</code> 0x8 </p>
<p> #define <code>RLS_SNDLFNLIST</code> 0x10 </p>
<p> #define <code>RLS_SNDBLOOMFILTER</code> 0x20 </p>
<p> #define <code>RLS_INITIALIZED</code> 0x40 </p>
<h3>Enumerations</h3>
<p> enum <code>globus_rls_pattern_t</code> { <code>rls_pattern_unix</code>, <code>rls_pattern_sql</code> } </p>
<p> enum <code>globus_rls_attr_type_t</code> { <code>globus_rls_attr_type_date</code>, <code>globus_rls_attr_type_flt</code>, <code>globus_rls_attr_type_int</code>, <code>globus_rls_attr_type_str</code> } </p>
<p> enum <code>globus_rls_obj_type_t</code> { <code>globus_rls_obj_lrc_lfn</code>, <code>globus_rls_obj_lrc_pfn</code>, <code>globus_rls_obj_rli_lfn</code>, <code>globus_rls_obj_rli_lrc</code> } </p>
<p> enum <code>globus_rls_attr_op_t</code> { <code>globus_rls_attr_op_all</code>, <code>globus_rls_attr_op_eq</code>, <code>globus_rls_attr_op_ne</code>, <code>globus_rls_attr_op_gt</code>, <code>globus_rls_attr_op_ge</code>, <code>globus_rls_attr_op_lt</code>, <code>globus_rls_attr_op_le</code>, <code>globus_rls_attr_op_btw</code>, <code>globus_rls_attr_op_like</code> } </p>
<p> enum <code>globus_rls_admin_cmd_t</code> { <code>globus_rls_admin_cmd_ping</code>, <code>globus_rls_admin_cmd_quit</code>, <code>globus_rls_admin_cmd_ssu</code> } </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_rls_client_admin</code> (<code>globus_rls_handle_t</code> *h, <code>globus_rls_admin_cmd_t</code> cmd) </p>
<p> globus_result_t <code>globus_rls_client_get_configuration</code> (<code>globus_rls_handle_t</code> *h, char *option, globus_list_t **conf_list) </p>
<p> globus_result_t <code>globus_rls_client_set_configuration</code> (<code>globus_rls_handle_t</code> *h, char *option, char *value) </p>
<p> globus_result_t <code>globus_rls_client_stats</code> (<code>globus_rls_handle_t</code> *h, <code>globus_rls_stats_t</code> *rlsstats) </p>
<p> char * <code>globus_rls_client_attr2s</code> (<code>globus_rls_attribute_t</code> *attr, char *buf, int buflen) </p>
<p> globus_result_t <code>globus_rls_client_s2attr</code> (<code>globus_rls_attr_type_t</code> type, char *sval, <code>globus_rls_attribute_t</code> *attr) </p>
<p> globus_result_t <code>globus_rls_client_error_info</code> (globus_result_t r, int *rc, char *buf, int buflen, globus_bool_t preserve) </p>
<p> int <code>globus_list_len</code> (globus_list_t *len) </p>
<p> char * <code>globus_rls_errmsg</code> (int rc, char *specificmsg, char *buf, int buflen) </p>
<h2>Detailed Description</h2>
<p> Miscellaneous functions and types.</p>
<h2>Define Documentation</h2>
<h3>#define RLS_LRCSERVER 0x1</h3>
<p> Server is LRC server.</p>
<h3>#define RLS_RLISERVER 0x2</h3>
<p> Server is RLI server.</p>
<h3>#define RLS_RCVLFNLIST 0x4</h3>
<p> RLI accepts LFN list updates.</p>
<h3>#define RLS_RCVBLOOMFILTER 0x8</h3>
<p> RLI accepts Bloom filter updates.</p>
<h3>#define RLS_SNDLFNLIST 0x10</h3>
<p> LRC sends LFN list updates.</p>
<h3>#define RLS_SNDBLOOMFILTER 0x20</h3>
<p> LRC sends Bloom filter updates.</p>
<h3>#define RLS_INITIALIZED 0x40</h3>
<p> RLC is fully initialized.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_rls_pattern_t</code></h3>
<p> Wildcard character style. </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>rls_pattern_unix </i></p>
<dd> Unix file globbing chars (*, ?).</p>
<dt><i>rls_pattern_sql </i></p>
<dd> SQL &#8216;like&#8217; wildcards (%, _).</dl>
<h3>enum <code>globus_rls_attr_type_t</code></h3>
<p> Attribute Value Types. </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>globus_rls_attr_type_date </i></p>
<dd> Date (time_t).</p>
<dt><i>globus_rls_attr_type_flt </i></p>
<dd> Floating point (double).</p>
<dt><i>globus_rls_attr_type_int </i></p>
<dd> Integer (int).</p>
<dt><i>globus_rls_attr_type_str </i></p>
<dd> String (char *).</dl>
<h3>enum <code>globus_rls_obj_type_t</code></h3>
<p> Object types in LRC and RLI databases. </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>globus_rls_obj_lrc_lfn </i></p>
<dd> LRC Logical File Name.</p>
<dt><i>globus_rls_obj_lrc_pfn </i></p>
<dd> LRC Physical File Name.</p>
<dt><i>globus_rls_obj_rli_lfn </i></p>
<dd> RLI Logical File Name.</p>
<dt><i>globus_rls_obj_rli_lrc </i></p>
<dd> RLI LRC URL.</dl>
<h3>enum <code>globus_rls_attr_op_t</code></h3>
<p> Attribute Value Query Operators. </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>globus_rls_attr_op_all </i></p>
<dd> All values returned.</p>
<dt><i>globus_rls_attr_op_eq </i></p>
<dd> Values matching operand 1 returned.</p>
<dt><i>globus_rls_attr_op_ne </i></p>
<dd> Values not matching operand 1.</p>
<dt><i>globus_rls_attr_op_gt </i></p>
<dd> Values greater than operand 1.</p>
<dt><i>globus_rls_attr_op_ge </i></p>
<dd> Values greater than or equal to op1.</p>
<dt><i>globus_rls_attr_op_lt </i></p>
<dd> Values less than operand 1.</p>
<dt><i>globus_rls_attr_op_le </i></p>
<dd> Values less than or equal to op1.</p>
<dt><i>globus_rls_attr_op_btw </i></p>
<dd> Values between operand1 and 2.</p>
<dt><i>globus_rls_attr_op_like </i></p>
<dd> Strings &#8216;like&#8217; operand1 (SQL like).</dl>
<h3>enum <code>globus_rls_admin_cmd_t</code></h3>
<p> <code>globus_rls_client_admin()</code> commands. </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>globus_rls_admin_cmd_ping </i></p>
<dd> Verify RLS server responding.</p>
<dt><i>globus_rls_admin_cmd_quit </i></p>
<dd> Tell RLS server to exit.</p>
<dt><i>globus_rls_admin_cmd_ssu </i></p>
<dd> Tell LRC server to do softstate update.</dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_rls_client_admin (<code>globus_rls_handle_t</code> * h, <code>globus_rls_admin_cmd_t</code> cmd)</h3>
<p> Miscellaneous administrative operations. Most operations require the admin privilege. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to RLS server.<br />
 <i>cmd</i> Command to be sent to RLS server.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Command succeeded.</dl>
<h3>globus_result_t globus_rls_client_get_configuration (<code>globus_rls_handle_t</code> * h, char * option, globus_list_t ** conf_list)</h3>
<p> Get server configuration. Client needs admin privilege. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to RLS server.<br />
 <i>option</i> Configuration option to get. If NULL all options are retrieved.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>conf_list</i> List of configuration options.<br />
 <i>GLOBUS_SUCCESS</i> List of retrieved config options returned in <i>conf_list</i>, each datum is of type <code>globus_rls_string2_t</code>. <i>conf_list</i> should be freed with <code>globus_rls_client_free_list()</code>. There may be multiple &#8216;acl&#8217; entries in the list, since the access control list can include more than one entry. Each acl configuration value is consists of a regular expression (matched against grid-mapfile users or DNs), a colon, and space separated list of permissions the matching users are granted.</dl>
<h3>globus_result_t globus_rls_client_set_configuration (<code>globus_rls_handle_t</code> * h, char * option, char * value)</h3>
<p> Set server configuration option. Client needs admin privilege. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to RLS server.<br />
 <i>option</i> Configuration option to set.<br />
 <i>value</i> New value for option.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Option set on server.</dl>
<h3>globus_result_t globus_rls_client_stats (<code>globus_rls_handle_t</code> * h, <code>globus_rls_stats_t</code> * rlsstats)</h3>
<p> Retrieve various statistics from RLS server. Requires stats privilege. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to RLS server.<br />
 <i>rlsstats</i> Stats returned here.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Stats returned in <i>rlsstats</i>.</dl>
<h3>char* globus_rls_client_attr2s (<code>globus_rls_attribute_t</code> * attr, char * buf, int buflen)</h3>
<p> Map attribute value to string. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>attr</i> Attribute to convert. If <i>attr-&gt;type</i> is <code>globus_rls_attr_type_date</code> then the resulting string will be in the format MySQL uses by default, which is YYYYMMDDHHMMSS.<br />
 <i>buf</i> Buffer to write string value to. Note if <i>attr-&gt;type</i> is <code>globus_rls_attr_type_str</code> then <i>attr-&gt;val.s</i> is returned, and <i>buf</i> is unused.<br />
 <i>buflen</i> Size of <i>buf</i> in bytes.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>String Value</i> Attribute value converted to a string.</dl>
<h3>globus_result_t globus_rls_client_s2attr (<code>globus_rls_attr_type_t</code> type, char * sval, <code>globus_rls_attribute_t</code> * attr)</h3>
<p> Set <code>globus_rls_attribute_t</code> type and val fields from a type and string value. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>type</i> Attribute value type.<br />
 <i>sval</i> String value to convert to binary. If type is <code>globus_rls_attr_type_date</code> <i>sval</i> should be in the form YYYY-MM-DD HH:MM:SS.<br />
 <i>attr</i> Attribute whose type and val fields are to be set.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> <i>attr-&gt;type</i> and <i>attr-&gt;val</i> successfully set.</dl>
<h3>globus_result_t globus_rls_client_error_info (globus_result_t r, int * rc, char * buf, int buflen, globus_bool_t preserve)</h3>
<p> Get error code and message from globus_result_t returned by this API. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>r</i> Result returned by RLS API function. <i>r</i> is freed by this call and should not be referenced again. If <i>preserve</i> is set then a new globus_result_t is constructed with the same values and returned as the function value.<br />
 <i>rc</i> Address to store error code at. If NULL error code is not returned.<br />
 <i>buf</i> Address to store error message at. If NULL error message is not returned.<br />
 <i>preserve</i> If GLOBUS_TRUE then a new globus_result_t is contructed with the same values as the old and returned as the function value.<br />
 <i>buflen</i> Size of <i>buf</i>.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>globus_result_t</i> If <i>preserve</i> is set a new globus_result_t identical to <i>r</i> is returned, otherwise GLOBUS_SUCCESS.</dl>
<h3>int globus_list_len (globus_list_t * len)</h3>
<p> Compute length of list. globus_list_size() is implemented using recursion, besides being inefficient it can run out of stack space when the list is large.</p>
<h3>char* globus_rls_errmsg (int rc, char * specificmsg, char * buf, int buflen)</h3>
<p> Map RLS status code to error string. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>rc</i> Status code.<br />
 <i>specificmsg</i> If not NULL prepended (with a colon) to error string.<br />
 <i>buf</i> Buffer to write error message to.<br />
 <i>buflen</i> Length of <i>buf</i>. Message will be truncated to fit if too long.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>char</i> * Returns <i>buf</i>, error message written to <i>buf</i>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus rls client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAV">Function Documentation</a></p>
<dd>
<dt><a href="#lbBF">Author</a></p>
<dd></dl>
