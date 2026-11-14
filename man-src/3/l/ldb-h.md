---
title: "ldb-h(3)"
name: "ldb-h"
section: "3"
letter: "l"
url: "/docs/linux/man/3-ldb-h/"
description: "include/ldb.h – Samba’s ldb database."
---

<p>include/ldb.h &#8211; Samba&#8217;s ldb database.</p>
<h2>Synopsis</h2>
<p> #include &lt;stdbool.h&gt;<br />
 #include &lt;talloc.h&gt;<br />
 #include &lt;tevent.h&gt;<br />
 #include &lt;ldb_version.h&gt;<br />
 #include &lt;ldb_errors.h&gt; </p>
<h3>Data Structures</h3>
<p> struct <code>ldb_val</code><br />
 <i>Result value. </i><br />
 struct <code>ldb_message_element</code><br />
 <i>results are given back as arrays of </i><code>ldb_message_element</code><br />
 struct <code>ldb_message</code><br />
 <i>a </i><code>ldb_message</code> represents all or part of a record.<br />
 struct <code>ldb_ldif</code><br />
 <i>LDIF record. </i><br />
 struct <code>ldb_debug_ops</code><br />
 <i>the user can optionally supply a debug function. </i><br />
 struct <code>ldb_utf8_fns</code><br />
 <i>The user can optionally supply a custom utf8 functions, to handle comparisons and casefolding. </i><br />
 struct <code>ldb_parse_tree</code> </p>
<p> struct <code>ldb_schema_syntax</code> </p>
<p> struct <code>ldb_schema_attribute</code> </p>
<p> struct <code>ldb_dn_extended_syntax</code> </p>
<p> struct <code>ldb_sd_flags_control</code> </p>
<p> struct <code>ldb_search_options_control</code> </p>
<p> struct <code>ldb_paged_control</code> </p>
<p> struct <code>ldb_extended_dn_control</code> </p>
<p> struct <code>ldb_server_sort_control</code> </p>
<p> struct <code>ldb_sort_resp_control</code> </p>
<p> struct <code>ldb_asq_control</code> </p>
<p> struct <code>ldb_dirsync_control</code> </p>
<p> struct <code>ldb_vlv_req_control</code> </p>
<p> struct <code>ldb_vlv_resp_control</code> </p>
<p> struct <code>ldb_verify_name_control</code> </p>
<p> struct <code>ldb_control</code> </p>
<p> struct <code>ldb_extended</code> </p>
<p> struct <code>ldb_seqnum_request</code> </p>
<p> struct <code>ldb_seqnum_result</code> </p>
<p> struct <code>ldb_result</code> </p>
<p> struct <code>ldb_reply</code> </p>
<p> struct <code>ldb_search</code> </p>
<p> struct <code>ldb_add</code> </p>
<p> struct <code>ldb_modify</code> </p>
<p> struct <code>ldb_delete</code> </p>
<p> struct <code>ldb_rename</code> </p>
<p> struct <code>ldb_register_control</code> </p>
<p> struct <code>ldb_register_partition</code> </p>
<p> struct <code>ldb_request</code> </p>
<h3>Macros</h3>
<p> #define <code>LDB_FLAG_MOD_MASK</code> 0x3<br />
 <i>There are a number of flags that are used with ldap_modify() in ldb_message_element.flags fields. </i><br />
 #define <code>LDB_FLAG_MOD_TYPE</code>(flags) ((flags) &amp; <code>LDB_FLAG_MOD_MASK</code>)<br />
 <i>use this to extract the mod type from the operation </i><br />
 #define <code>LDB_FLAG_MOD_ADD</code> 1<br />
 <i>Flag value used in ldap_modify() to indicate that attributes are being added. </i><br />
 #define <code>LDB_FLAG_MOD_REPLACE</code> 2<br />
 <i>Flag value used in ldap_modify() to indicate that attributes are being replaced. </i><br />
 #define <code>LDB_FLAG_MOD_DELETE</code> 3<br />
 <i>Flag value used in ldap_modify() to indicate that attributes are being deleted. </i><br />
 #define <code>LDB_FLAG_INTERNAL_MASK</code> 0xFFFFFFF0<br />
 <i>flag bits on an element usable only by the internal implementation </i><br />
 #define <code>LDB_OID_COMPARATOR_AND</code> &#8216;1.2.840.113556.1.4.803&#8217;<br />
 <i>OID for logic AND comaprison. </i><br />
 #define <code>LDB_OID_COMPARATOR_OR</code> &#8216;1.2.840.113556.1.4.804&#8217;<br />
 <i>OID for logic OR comparison. </i><br />
 #define <code>LDB_FLG_RDONLY</code> 1<br />
 <i>Flag value for database connection mode. </i><br />
 #define <code>LDB_FLG_NOSYNC</code> 2<br />
 <i>Flag value for database connection mode. </i><br />
 #define <code>LDB_FLG_RECONNECT</code> 4<br />
 <i>Flag value to specify autoreconnect mode. </i><br />
 #define <code>LDB_FLG_NOMMAP</code> 8<br />
 <i>Flag to tell backends not to use mmap. </i><br />
 #define <code>LDB_FLG_SHOW_BINARY</code> 16<br />
 <i>Flag to tell ldif handlers not to force encoding of binary structures in base64. </i><br />
 #define <code>LDB_FLG_ENABLE_TRACING</code> 32<br />
 <i>Flags to enable ldb tracing. </i><br />
 #define <code>LDB_ATTR_FLAG_HIDDEN</code> (1&lt;&lt;0)<br />
 <i>The attribute is not returned by default. </i><br />
 #define <code>LDB_ATTR_FLAG_ALLOCATED</code> (1&lt;&lt;1) </p>
<p> #define <code>LDB_ATTR_FLAG_FIXED</code> (1&lt;&lt;2)<br />
 <i>The attribute is supplied by the application and should not be removed. </i><br />
 #define <code>LDB_ATTR_FLAG_UNIQUE_INDEX</code> (1&lt;&lt;3) </p>
<p> #define <code>LDB_ATTR_FLAG_SINGLE_VALUE</code> (1&lt;&lt;4) </p>
<p> #define <code>LDB_ATTR_FLAG_FORCE_BASE64_LDIF</code> (1&lt;&lt;5) </p>
<p> #define <code>LDB_SYNTAX_DN</code> &#8216;1.3.6.1.4.1.1466.115.121.1.12&#8217;<br />
 <i>LDAP attribute syntax for a DN. </i><br />
 #define <code>LDB_SYNTAX_DIRECTORY_STRING</code> &#8216;1.3.6.1.4.1.1466.115.121.1.15&#8217;<br />
 <i>LDAP attribute syntax for a Directory String. </i><br />
 #define <code>LDB_SYNTAX_INTEGER</code> &#8216;1.3.6.1.4.1.1466.115.121.1.27&#8217;<br />
 <i>LDAP attribute syntax for an integer. </i><br />
 #define <code>LDB_SYNTAX_BOOLEAN</code> &#8216;1.3.6.1.4.1.1466.115.121.1.7&#8217;<br />
 <i>LDAP attribute syntax for a boolean. </i><br />
 #define <code>LDB_SYNTAX_OCTET_STRING</code> &#8216;1.3.6.1.4.1.1466.115.121.1.40&#8217;<br />
 <i>LDAP attribute syntax for an octet string. </i><br />
 #define <code>LDB_SYNTAX_UTC_TIME</code> &#8216;1.3.6.1.4.1.1466.115.121.1.53&#8217;<br />
 <i>LDAP attribute syntax for UTC time. </i><br />
 #define <code>LDB_SYNTAX_GENERALIZED_TIME</code> &#8216;1.3.6.1.4.1.1466.115.121.1.24&#8217; </p>
<p> #define <code>LDB_SYNTAX_OBJECTCLASS</code> &#8216;LDB_SYNTAX_OBJECTCLASS&#8217; </p>
<p> #define <code>LDB_CONTROL_BYPASS_OPERATIONAL_OID</code> &#8216;1.3.6.1.4.1.7165.4.3.13&#8217;<br />
 <i>OID for getting and manipulating attributes from the ldb without interception in the operational module. </i><br />
 #define <code>LDB_CONTROL_BYPASS_OPERATIONAL_NAME</code> &#8216;bypassoperational&#8217; </p>
<p> #define <code>LDB_CONTROL_RECALCULATE_SD_OID</code> &#8216;1.3.6.1.4.1.7165.4.3.5&#8217;<br />
 <i>OID for recalculate SD control. </i><br />
 #define <code>LDB_CONTROL_RECALCULATE_SD_NAME</code> &#8216;recalculate_sd&#8217; </p>
<p> #define <code>LDB_CONTROL_REVEAL_INTERNALS</code> &#8216;1.3.6.1.4.1.7165.4.3.6&#8217;<br />
 <i>REVEAL_INTERNALS is used to reveal internal attributes and DN components which are not normally shown to the user. </i><br />
 #define <code>LDB_CONTROL_REVEAL_INTERNALS_NAME</code> &#8216;reveal_internals&#8217; </p>
<p> #define <code>LDB_CONTROL_AS_SYSTEM_OID</code> &#8216;1.3.6.1.4.1.7165.4.3.7&#8217;<br />
 <i>LDB_CONTROL_AS_SYSTEM is used to skip access checks on operations that are performed by the system, but with a user&#8217;s credentials, e.g. </i><br />
 #define <code>LDB_CONTROL_PROVISION_OID</code> &#8216;1.3.6.1.4.1.7165.4.3.16&#8217;<br />
 <i>LDB_CONTROL_PROVISION_OID is used to skip some constraint checks. </i><br />
 #define <code>LDB_CONTROL_PROVISION_NAME</code> &#8216;provision&#8217; </p>
<p> #define <code>LDB_CONTROL_PAGED_RESULTS_OID</code> &#8216;1.2.840.113556.1.4.319&#8217;<br />
 <i>OID for the paged results control. </i><br />
 #define <code>LDB_CONTROL_PAGED_RESULTS_NAME</code> &#8216;paged_results&#8217; </p>
<p> #define <code>LDB_CONTROL_SD_FLAGS_OID</code> &#8216;1.2.840.113556.1.4.801&#8217;<br />
 <i>OID for specifying the returned elements of the ntSecurityDescriptor. </i><br />
 #define <code>LDB_CONTROL_SD_FLAGS_NAME</code> &#8216;sd_flags&#8217; </p>
<p> #define <code>LDB_CONTROL_DOMAIN_SCOPE_OID</code> &#8216;1.2.840.113556.1.4.1339&#8217;<br />
 <i>OID for specifying an advanced scope for the search (one partition) </i><br />
 #define <code>LDB_CONTROL_DOMAIN_SCOPE_NAME</code> &#8216;domain_scope&#8217; </p>
<p> #define <code>LDB_CONTROL_SEARCH_OPTIONS_OID</code> &#8216;1.2.840.113556.1.4.1340&#8217;<br />
 <i>OID for specifying an advanced scope for a search. </i><br />
 #define <code>LDB_CONTROL_SEARCH_OPTIONS_NAME</code> &#8216;search_options&#8217; </p>
<p> #define <code>LDB_CONTROL_NOTIFICATION_OID</code> &#8216;1.2.840.113556.1.4.528&#8217;<br />
 <i>OID for notification. </i><br />
 #define <code>LDB_CONTROL_NOTIFICATION_NAME</code> &#8216;notification&#8217; </p>
<p> #define <code>LDB_CONTROL_TREE_DELETE_OID</code> &#8216;1.2.840.113556.1.4.805&#8217;<br />
 <i>OID for performing subtree deletes. </i><br />
 #define <code>LDB_CONTROL_TREE_DELETE_NAME</code> &#8216;tree_delete&#8217; </p>
<p> #define <code>LDB_CONTROL_SHOW_DELETED_OID</code> &#8216;1.2.840.113556.1.4.417&#8217;<br />
 <i>OID for getting deleted objects. </i><br />
 #define <code>LDB_CONTROL_SHOW_DELETED_NAME</code> &#8216;show_deleted&#8217; </p>
<p> #define <code>LDB_CONTROL_SHOW_RECYCLED_OID</code> &#8216;1.2.840.113556.1.4.2064&#8217;<br />
 <i>OID for getting recycled objects. </i><br />
 #define <code>LDB_CONTROL_SHOW_RECYCLED_NAME</code> &#8216;show_recycled&#8217; </p>
<p> #define <code>LDB_CONTROL_SHOW_DEACTIVATED_LINK_OID</code> &#8216;1.2.840.113556.1.4.2065&#8217;<br />
 <i>OID for getting deactivated linked attributes. </i><br />
 #define <code>LDB_CONTROL_SHOW_DEACTIVATED_LINK_NAME</code> &#8216;show_deactivated_link&#8217; </p>
<p> #define <code>LDB_CONTROL_EXTENDED_DN_OID</code> &#8216;1.2.840.113556.1.4.529&#8217;<br />
 <i>OID for extended DN. </i><br />
 #define <code>LDB_CONTROL_EXTENDED_DN_NAME</code> &#8216;extended_dn&#8217; </p>
<p> #define <code>LDB_CONTROL_SERVER_SORT_OID</code> &#8216;1.2.840.113556.1.4.473&#8217;<br />
 <i>OID for LDAP server sort result extension. </i><br />
 #define <code>LDB_CONTROL_SERVER_SORT_NAME</code> &#8216;server_sort&#8217; </p>
<p> #define <code>LDB_CONTROL_SORT_RESP_OID</code> &#8216;1.2.840.113556.1.4.474&#8217;<br />
 <i>OID for LDAP server sort result response extension. </i><br />
 #define <code>LDB_CONTROL_SORT_RESP_NAME</code> &#8216;server_sort_resp&#8217; </p>
<p> #define <code>LDB_CONTROL_ASQ_OID</code> &#8216;1.2.840.113556.1.4.1504&#8217;<br />
 <i>OID for LDAP Attribute Scoped Query extension. </i><br />
 #define <code>LDB_CONTROL_ASQ_NAME</code> &#8216;asq&#8217; </p>
<p> #define <code>LDB_CONTROL_DIRSYNC_OID</code> &#8216;1.2.840.113556.1.4.841&#8217;<br />
 <i>OID for LDAP Directory Sync extension. </i><br />
 #define <code>LDB_CONTROL_DIRSYNC_NAME</code> &#8216;dirsync&#8217; </p>
<p> #define <code>LDB_CONTROL_DIRSYNC_EX_OID</code> &#8216;1.2.840.113556.1.4.2090&#8217; </p>
<p> #define <code>LDB_CONTROL_DIRSYNC_EX_NAME</code> &#8216;dirsync_ex&#8217; </p>
<p> #define <code>LDB_CONTROL_VLV_REQ_OID</code> &#8216;2.16.840.1.113730.3.4.9&#8217;<br />
 <i>OID for LDAP Virtual List View Request extension. </i><br />
 #define <code>LDB_CONTROL_VLV_REQ_NAME</code> &#8216;vlv&#8217; </p>
<p> #define <code>LDB_CONTROL_VLV_RESP_OID</code> &#8216;2.16.840.1.113730.3.4.10&#8217;<br />
 <i>OID for LDAP Virtual List View Response extension. </i><br />
 #define <code>LDB_CONTROL_VLV_RESP_NAME</code> &#8216;vlv_resp&#8217; </p>
<p> #define <code>LDB_CONTROL_PERMISSIVE_MODIFY_OID</code> &#8216;1.2.840.113556.1.4.1413&#8217;<br />
 <i>OID to let modifies don&#8217;t give an error when adding an existing attribute with the same value or deleting an nonexisting one attribute. </i><br />
 #define <code>LDB_CONTROL_PERMISSIVE_MODIFY_NAME</code> &#8216;permissive_modify&#8217; </p>
<p> #define <code>LDB_CONTROL_SERVER_LAZY_COMMIT</code> &#8216;1.2.840.113556.1.4.619&#8217;<br />
 <i>OID to allow the server to be more &#8216;fast and loose&#8217; with the data being added. </i><br />
 #define <code>LDB_CONTROL_RODC_DCPROMO_OID</code> &#8216;1.2.840.113556.1.4.1341&#8217;<br />
 <i>Control for RODC join -see [MS-ADTS] section 3.1.1.3.4.1.23. </i><br />
 #define <code>LDB_CONTROL_RODC_DCPROMO_NAME</code> &#8216;rodc_join&#8217; </p>
<p> #define <code>LDB_CONTROL_RELAX_OID</code> &#8216;1.3.6.1.4.1.4203.666.5.12&#8217;<br />
 <i>OID for the allowing client to request temporary relaxed enforcement of constraints of the x.500 model. </i><br />
 #define <code>LDB_CONTROL_RELAX_NAME</code> &#8216;relax&#8217; </p>
<p> #define <code>LDB_CONTROL_VERIFY_NAME_OID</code> &#8216;1.2.840.113556.1.4.1338&#8217;<br />
 <i>OID for the allowing some kind of relax check for attributes with DNs. </i><br />
 #define <code>LDB_CONTROL_VERIFY_NAME_NAME</code> &#8216;verify_name&#8217; </p>
<p> #define <code>LDB_EXTENDED_SEQUENCE_NUMBER</code> &#8216;1.3.6.1.4.1.7165.4.4.3&#8217;<br />
 <i>OID for LDAP Extended Operation SEQUENCE_NUMBER. </i><br />
 #define <code>LDB_EXTENDED_PASSWORD_CHANGE_OID</code> &#8216;1.3.6.1.4.1.4203.1.11.1&#8217;<br />
 <i>OID for LDAP Extended Operation PASSWORD_CHANGE. </i><br />
 #define <code>LDB_EXTENDED_FAST_BIND_OID</code> &#8216;1.2.840.113556.1.4.1781&#8217;<br />
 <i>OID for LDAP Extended Operation FAST_BIND. </i><br />
 #define <code>LDB_EXTENDED_START_TLS_OID</code> &#8216;1.3.6.1.4.1.1466.20037&#8217;<br />
 <i>OID for LDAP Extended Operation START_TLS. </i><br />
 #define <code>LDB_EXTENDED_DYNAMIC_OID</code> &#8216;1.3.6.1.4.1.1466.101.119.1&#8217;<br />
 <i>OID for LDAP Extended Operation DYNAMIC_REFRESH. </i><br />
 #define <code>LDB_SEARCH_OPTION_DOMAIN_SCOPE</code> 0x00000001 </p>
<p> #define <code>LDB_SEARCH_OPTION_PHANTOM_ROOT</code> 0x00000002 </p>
<p> #define <code>LDB_SEQ_GLOBAL_SEQUENCE</code> 0x01 </p>
<p> #define <code>LDB_SEQ_TIMESTAMP_SEQUENCE</code> 0x02 </p>
<p> #define <code>ldb_attr_cmp</code>(a, b) strcasecmp(a, b)<br />
 <i>Compare two attributes. </i><br />
 #define <code>discard_const</code>(ptr) ((void *)((uintptr_t)(ptr))) </p>
<p> #define <code>LDB_TYPESAFE_QSORT</code>(base, numel, opaque, comparison) </p>
<p> #define <code>TYPESAFE_QSORT</code>(base, numel, comparison) </p>
<p> #define <code>LDB_REQ_SET_LOCATION</code>(req) ldb_req_set_location(req, __location__) </p>
<h3>Typedefs</h3>
<p> typedef int(* <code>ldb_attr_handler_t</code> )(struct <code>ldb_context</code> *, TALLOC_CTX *mem_ctx, const struct <code>ldb_val</code> *, struct <code>ldb_val</code> *) </p>
<p> typedef int(* <code>ldb_attr_comparison_t</code> )(struct <code>ldb_context</code> *, TALLOC_CTX *mem_ctx, const struct <code>ldb_val</code> *, const struct <code>ldb_val</code> *) </p>
<p> typedef int(* <code>ldb_attr_operator_t</code> )(struct <code>ldb_context</code> *, enum ldb_parse_op operation, const struct <code>ldb_schema_attribute</code> *a, const struct <code>ldb_val</code> *, const struct <code>ldb_val</code> *, bool *matched) </p>
<p> typedef int(* <code>ldb_qsort_cmp_fn_t</code> )(void *v1, void *v2, void *opaque) </p>
<p> typedef int(* <code>ldb_request_callback_t</code> )(struct <code>ldb_request</code> *, struct <code>ldb_reply</code> *) </p>
<p> typedef void(* <code>ldb_async_timeout_fn</code> )(void *) </p>
<p> typedef bool(* <code>ldb_async_callback_fn</code> )(void *) </p>
<p> typedef int(* <code>ldb_async_ctx_add_op_fn</code> )(void *, time_t, void *, ldb_async_timeout_fn, ldb_async_callback_fn) </p>
<p> typedef int(* <code>ldb_async_ctx_wait_op_fn</code> )(void *) </p>
<h3>Enumerations</h3>
<p> enum <code>ldb_changetype</code> { <code>LDB_CHANGETYPE_NONE</code> =0, <code>LDB_CHANGETYPE_ADD</code>, <code>LDB_CHANGETYPE_DELETE</code>, <code>LDB_CHANGETYPE_MODIFY</code>, <code>LDB_CHANGETYPE_MODRDN</code> } </p>
<p> enum <code>ldb_scope</code> { <code>LDB_SCOPE_DEFAULT</code> =-1, <code>LDB_SCOPE_BASE</code> =0, <code>LDB_SCOPE_ONELEVEL</code> =1, <code>LDB_SCOPE_SUBTREE</code> =2 } </p>
<p> enum <code>ldb_debug_level</code> { <code>LDB_DEBUG_FATAL</code>, <code>LDB_DEBUG_ERROR</code>, <code>LDB_DEBUG_WARNING</code>, <code>LDB_DEBUG_TRACE</code> } </p>
<p> enum <code>ldb_parse_op</code> { <code>LDB_OP_AND</code> =1, <code>LDB_OP_OR</code> =2, <code>LDB_OP_NOT</code> =3, <code>LDB_OP_EQUALITY</code> =4, <code>LDB_OP_SUBSTRING</code> =5, <code>LDB_OP_GREATER</code> =6, <code>LDB_OP_LESS</code> =7, <code>LDB_OP_PRESENT</code> =8, <code>LDB_OP_APPROX</code> =9, <code>LDB_OP_EXTENDED</code> =10 } </p>
<p> enum <code>ldb_request_type</code> { <code>LDB_SEARCH</code>, <code>LDB_ADD</code>, <code>LDB_MODIFY</code>, <code>LDB_DELETE</code>, <code>LDB_RENAME</code>, <code>LDB_EXTENDED</code>, <code>LDB_REQ_REGISTER_CONTROL</code>, <code>LDB_REQ_REGISTER_PARTITION</code> } </p>
<p> enum <code>ldb_reply_type</code> { <code>LDB_REPLY_ENTRY</code>, <code>LDB_REPLY_REFERRAL</code>, <code>LDB_REPLY_DONE</code> } </p>
<p> enum <code>ldb_wait_type</code> { <code>LDB_WAIT_ALL</code>, <code>LDB_WAIT_NONE</code> } </p>
<p> enum <code>ldb_state</code> { <code>LDB_ASYNC_INIT</code>, <code>LDB_ASYNC_PENDING</code>, <code>LDB_ASYNC_DONE</code> } </p>
<p> enum <code>ldb_sequence_type</code> { <code>LDB_SEQ_HIGHEST_SEQ</code>, <code>LDB_SEQ_HIGHEST_TIMESTAMP</code>, <code>LDB_SEQ_NEXT</code> } </p>
<h3>Functions</h3>
<p> struct <code>ldb_parse_tree</code> * <code>ldb_parse_tree</code> (TALLOC_CTX *mem_ctx, const char *s) </p>
<p> char * <code>ldb_filter_from_tree</code> (TALLOC_CTX *mem_ctx, const struct <code>ldb_parse_tree</code> *tree) </p>
<p> char * <code>ldb_binary_encode</code> (TALLOC_CTX *mem_ctx, struct <code>ldb_val</code> val)<br />
 <i>Encode a binary blob. </i><br />
 char * <code>ldb_binary_encode_string</code> (TALLOC_CTX *mem_ctx, const char *string)<br />
 <i>Encode a string. </i><br />
 struct <code>ldb_schema_attribute</code> * <code>ldb_schema_attribute_by_name</code> (struct <code>ldb_context</code> *ldb, const char *name) </p>
<p> struct <code>ldb_dn_extended_syntax</code> * <code>ldb_dn_extended_syntax_by_name</code> (struct <code>ldb_context</code> *ldb, const char *name) </p>
<p> int <code>ldb_request</code> (struct <code>ldb_context</code> *ldb, struct <code>ldb_request</code> *request) </p>
<p> int <code>ldb_request_done</code> (struct <code>ldb_request</code> *req, int status) </p>
<p> bool <code>ldb_request_is_done</code> (struct <code>ldb_request</code> *req) </p>
<p> int <code>ldb_modules_wait</code> (struct <code>ldb_handle</code> *handle) </p>
<p> int <code>ldb_wait</code> (struct <code>ldb_handle</code> *handle, enum ldb_wait_type type) </p>
<p> int <code>ldb_set_timeout</code> (struct <code>ldb_context</code> *ldb, struct <code>ldb_request</code> *req, int timeout) </p>
<p> int <code>ldb_set_timeout_from_prev_req</code> (struct <code>ldb_context</code> *ldb, struct <code>ldb_request</code> *oldreq, struct <code>ldb_request</code> *newreq) </p>
<p> void <code>ldb_set_create_perms</code> (struct <code>ldb_context</code> *ldb, unsigned int perms) </p>
<p> void <code>ldb_set_modules_dir</code> (struct <code>ldb_context</code> *ldb, const char *path) </p>
<p> void <code>ldb_set_event_context</code> (struct <code>ldb_context</code> *ldb, struct tevent_context *ev) </p>
<p> struct tevent_context * <code>ldb_get_event_context</code> (struct <code>ldb_context</code> *ldb) </p>
<p> int <code>ldb_global_init</code> (void)<br />
 <i>Initialise ldbs&#8217; global information. </i><br />
 struct <code>ldb_context</code> * <code>ldb_init</code> (TALLOC_CTX *mem_ctx, struct tevent_context *ev_ctx)<br />
 <i>Initialise an ldb context. </i><br />
 void <code>ldb_async_ctx_set_private_data</code> (struct <code>ldb_context</code> *ldb, void *private_data) </p>
<p> void <code>ldb_async_ctx_set_add_op</code> (struct <code>ldb_context</code> *ldb, ldb_async_ctx_add_op_fn add_op) </p>
<p> void <code>ldb_async_ctx_set_wait_op</code> (struct <code>ldb_context</code> *ldb, ldb_async_ctx_wait_op_fn wait_op) </p>
<p> int <code>ldb_connect</code> (struct <code>ldb_context</code> *ldb, const char *url, unsigned int flags, const char *options[])<br />
 <i>Connect to a database. </i><br />
 struct ldb_dn * <code>ldb_get_root_basedn</code> (struct <code>ldb_context</code> *ldb) </p>
<p> struct ldb_dn * <code>ldb_get_config_basedn</code> (struct <code>ldb_context</code> *ldb) </p>
<p> struct ldb_dn * <code>ldb_get_schema_basedn</code> (struct <code>ldb_context</code> *ldb) </p>
<p> struct ldb_dn * <code>ldb_get_default_basedn</code> (struct <code>ldb_context</code> *ldb) </p>
<p> int <code>ldb_search_default_callback</code> (struct <code>ldb_request</code> *req, struct <code>ldb_reply</code> *ares)<br />
 <i>The default async search callback function. </i><br />
 int <code>ldb_op_default_callback</code> (struct <code>ldb_request</code> *req, struct <code>ldb_reply</code> *ares)<br />
 <i>The default async extended operation callback function. </i><br />
 int <code>ldb_modify_default_callback</code> (struct <code>ldb_request</code> *req, struct <code>ldb_reply</code> *ares) </p>
<p> int <code>ldb_build_search_req</code> (struct <code>ldb_request</code> **ret_req, struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, struct ldb_dn *base, enum ldb_scope scope, const char *expression, const char *const *attrs, struct <code>ldb_control</code> **controls, void *context, ldb_request_callback_t callback, struct <code>ldb_request</code> *parent)<br />
 <i>Helper function to build a search request. </i><br />
 int <code>ldb_build_search_req_ex</code> (struct <code>ldb_request</code> **ret_req, struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, struct ldb_dn *base, enum ldb_scope scope, struct <code>ldb_parse_tree</code> *tree, const char *const *attrs, struct <code>ldb_control</code> **controls, void *context, ldb_request_callback_t callback, struct <code>ldb_request</code> *parent) </p>
<p> int <code>ldb_build_add_req</code> (struct <code>ldb_request</code> **ret_req, struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const struct <code>ldb_message</code> *message, struct <code>ldb_control</code> **controls, void *context, ldb_request_callback_t callback, struct <code>ldb_request</code> *parent)<br />
 <i>Helper function to build an add request. </i><br />
 int <code>ldb_build_mod_req</code> (struct <code>ldb_request</code> **ret_req, struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const struct <code>ldb_message</code> *message, struct <code>ldb_control</code> **controls, void *context, ldb_request_callback_t callback, struct <code>ldb_request</code> *parent)<br />
 <i>Helper function to build a modify request. </i><br />
 int <code>ldb_build_del_req</code> (struct <code>ldb_request</code> **ret_req, struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, struct ldb_dn *dn, struct <code>ldb_control</code> **controls, void *context, ldb_request_callback_t callback, struct <code>ldb_request</code> *parent)<br />
 <i>Helper function to build a delete request. </i><br />
 int <code>ldb_build_rename_req</code> (struct <code>ldb_request</code> **ret_req, struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, struct ldb_dn *olddn, struct ldb_dn *newdn, struct <code>ldb_control</code> **controls, void *context, ldb_request_callback_t callback, struct <code>ldb_request</code> *parent)<br />
 <i>Helper function to build a rename request. </i><br />
 int <code>ldb_request_add_control</code> (struct <code>ldb_request</code> *req, const char *oid, bool critical, void *data)<br />
 <i>Add a </i><code>ldb_control</code> to a <code>ldb_request</code>.<br />
 int <code>ldb_request_replace_control</code> (struct <code>ldb_request</code> *req, const char *oid, bool critical, void *data)<br />
 <i>replace a </i><code>ldb_control</code> in a <code>ldb_request</code><br />
 struct <code>ldb_control</code> * <code>ldb_request_get_control</code> (struct <code>ldb_request</code> *req, const char *oid)<br />
 <i>check if a control with the specified &#8216;oid&#8217; exist and return it </i><br />
 struct <code>ldb_control</code> * <code>ldb_reply_get_control</code> (struct <code>ldb_reply</code> *rep, const char *oid)<br />
 <i>check if a control with the specified &#8216;oid&#8217; exist and return it </i><br />
 int <code>ldb_search</code> (struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, struct <code>ldb_result</code> **result, struct ldb_dn *base, enum ldb_scope scope, const char *const *attrs, const char *exp_fmt,&#8230;) PRINTF_ATTRIBUTE(7<br />
 <i>Search the database. </i><br />
 int int <code>ldb_add</code> (struct <code>ldb_context</code> *ldb, const struct <code>ldb_message</code> *message)<br />
 <i>Add a record to the database. </i><br />
 int <code>ldb_modify</code> (struct <code>ldb_context</code> *ldb, const struct <code>ldb_message</code> *message)<br />
 <i>Modify the specified attributes of a record. </i><br />
 int <code>ldb_rename</code> (struct <code>ldb_context</code> *ldb, struct ldb_dn *olddn, struct ldb_dn *newdn)<br />
 <i>Rename a record in the database. </i><br />
 int <code>ldb_delete</code> (struct <code>ldb_context</code> *ldb, struct ldb_dn *dn)<br />
 <i>Delete a record from the database. </i><br />
 int <code>ldb_extended_default_callback</code> (struct <code>ldb_request</code> *req, struct <code>ldb_reply</code> *ares)<br />
 <i>The default async extended operation callback function. </i><br />
 int <code>ldb_build_extended_req</code> (struct <code>ldb_request</code> **ret_req, struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const char *oid, void *data, struct <code>ldb_control</code> **controls, void *context, ldb_request_callback_t callback, struct <code>ldb_request</code> *parent)<br />
 <i>Helper function to build a extended request. </i><br />
 int <code>ldb_extended</code> (struct <code>ldb_context</code> *ldb, const char *oid, void *data, struct <code>ldb_result</code> **res)<br />
 <i>call an extended operation </i><br />
 int <code>ldb_sequence_number</code> (struct <code>ldb_context</code> *ldb, enum ldb_sequence_type type, uint64_t *seq_num)<br />
 <i>Obtain current/next database sequence number. </i><br />
 int <code>ldb_transaction_start</code> (struct <code>ldb_context</code> *ldb)<br />
 <i>start a transaction </i><br />
 int <code>ldb_transaction_prepare_commit</code> (struct <code>ldb_context</code> *ldb)<br />
 <i>first phase of two phase commit </i><br />
 int <code>ldb_transaction_commit</code> (struct <code>ldb_context</code> *ldb)<br />
 <i>commit a transaction </i><br />
 int <code>ldb_transaction_cancel</code> (struct <code>ldb_context</code> *ldb)<br />
 <i>cancel a transaction </i><br />
 int <code>ldb_transaction_cancel_noerr</code> (struct <code>ldb_context</code> *ldb) </p>
<p> const char * <code>ldb_errstring</code> (struct <code>ldb_context</code> *ldb)<br />
 <i>return extended error information from the last call </i><br />
 const char * <code>ldb_strerror</code> (int ldb_err)<br />
 <i>return a string explaining what a ldb error constant meancs </i><br />
 void <code>ldb_set_utf8_default</code> (struct <code>ldb_context</code> *ldb)<br />
 <i>setup the default utf8 functions FIXME: these functions do not yet handle utf8 </i><br />
 char * <code>ldb_casefold</code> (struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const char *s, size_t n)<br />
 <i>Casefold a string. </i><br />
 int <code>ldb_valid_attr_name</code> (const char *s)<br />
 <i>Check the attribute name is valid according to rfc2251. </i><br />
 int <code>ldb_ldif_write</code> (struct <code>ldb_context</code> *ldb, int(*fprintf_fn)(void *, const char *,&#8230;) PRINTF_ATTRIBUTE(2, 3), void *private_data, const struct <code>ldb_ldif</code> *ldif)<br />
 <i>Write an LDIF message. </i><br />
 void <code>ldb_ldif_read_free</code> (struct <code>ldb_context</code> *ldb, struct <code>ldb_ldif</code> *msg)<br />
 <i>Clean up an LDIF message. </i><br />
 struct <code>ldb_ldif</code> * <code>ldb_ldif_read</code> (struct <code>ldb_context</code> *ldb, int(*fgetc_fn)(void *), void *private_data)<br />
 <i>Read an LDIF message. </i><br />
 struct <code>ldb_ldif</code> * <code>ldb_ldif_read_file</code> (struct <code>ldb_context</code> *ldb, FILE *f)<br />
 <i>Read an LDIF message from a file. </i><br />
 struct <code>ldb_ldif</code> * <code>ldb_ldif_read_string</code> (struct <code>ldb_context</code> *ldb, const char **s)<br />
 <i>Read an LDIF message from a string. </i><br />
 int <code>ldb_ldif_parse_modrdn</code> (struct <code>ldb_context</code> *ldb, const struct <code>ldb_ldif</code> *ldif, TALLOC_CTX *mem_ctx, struct ldb_dn **olddn, struct ldb_dn **newrdn, bool *deleteoldrdn, struct ldb_dn **newsuperior, struct ldb_dn **newdn)<br />
 <i>Parse a modrdn LDIF message from a struct </i><code>ldb_message</code>.<br />
 int <code>ldb_ldif_write_file</code> (struct <code>ldb_context</code> *ldb, FILE *f, const struct <code>ldb_ldif</code> *msg)<br />
 <i>Write an LDIF message to a file. </i><br />
 char * <code>ldb_ldif_write_string</code> (struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const struct <code>ldb_ldif</code> *msg)<br />
 <i>Write an LDIF message to a string. </i><br />
 char * <code>ldb_ldif_message_string</code> (struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, enum ldb_changetype changetype, const struct <code>ldb_message</code> *msg) </p>
<p> char * <code>ldb_base64_encode</code> (TALLOC_CTX *mem_ctx, const char *buf, int len)<br />
 <i>Base64 encode a buffer. </i><br />
 int <code>ldb_base64_decode</code> (char *s)<br />
 <i>Base64 decode a buffer. </i><br />
 const char * <code>ldb_dn_get_linearized</code> (struct ldb_dn *dn)<br />
 <i>Get the linear form of a DN (without any extended components) </i><br />
 char * <code>ldb_dn_alloc_linearized</code> (TALLOC_CTX *mem_ctx, struct ldb_dn *dn)<br />
 <i>Allocate a copy of the linear form of a DN (without any extended components) onto the supplied memory context. </i><br />
 char * <code>ldb_dn_get_extended_linearized</code> (TALLOC_CTX *mem_ctx, struct ldb_dn *dn, int mode)<br />
 <i>Get the linear form of a DN (with any extended components) </i><br />
 struct <code>ldb_val</code> * <code>ldb_dn_get_extended_component</code> (struct ldb_dn *dn, const char *name) </p>
<p> int <code>ldb_dn_set_extended_component</code> (struct ldb_dn *dn, const char *name, const struct <code>ldb_val</code> *val) </p>
<p> void <code>ldb_dn_extended_filter</code> (struct ldb_dn *dn, const char *const *accept_list) </p>
<p> void <code>ldb_dn_remove_extended_components</code> (struct ldb_dn *dn) </p>
<p> bool <code>ldb_dn_has_extended</code> (struct ldb_dn *dn) </p>
<p> int <code>ldb_dn_extended_add_syntax</code> (struct <code>ldb_context</code> *ldb, unsigned flags, const struct <code>ldb_dn_extended_syntax</code> *syntax) </p>
<p> struct ldb_dn * <code>ldb_dn_new</code> (TALLOC_CTX *mem_ctx, struct <code>ldb_context</code> *ldb, const char *dn)<br />
 <i>Allocate a new DN from a string. </i><br />
 struct ldb_dn * <code>ldb_dn_new_fmt</code> (TALLOC_CTX *mem_ctx, struct <code>ldb_context</code> *ldb, const char *new_fmt,&#8230;) PRINTF_ATTRIBUTE(3<br />
 <i>Allocate a new DN from a printf style format string and arguments. </i><br />
 struct ldb_dn struct ldb_dn * <code>ldb_dn_from_ldb_val</code> (TALLOC_CTX *mem_ctx, struct <code>ldb_context</code> *ldb, const struct <code>ldb_val</code> *strdn)<br />
 <i>Allocate a new DN from a struct </i><code>ldb_val</code> (useful to avoid buffer overrun)<br />
 bool <code>ldb_dn_validate</code> (struct ldb_dn *dn)<br />
 <i>Determine if this DN is syntactically valid. </i><br />
 char * <code>ldb_dn_escape_value</code> (TALLOC_CTX *mem_ctx, struct <code>ldb_val</code> value) </p>
<p> const char * <code>ldb_dn_get_casefold</code> (struct ldb_dn *dn) </p>
<p> char * <code>ldb_dn_alloc_casefold</code> (TALLOC_CTX *mem_ctx, struct ldb_dn *dn) </p>
<p> int <code>ldb_dn_compare_base</code> (struct ldb_dn *base, struct ldb_dn *dn) </p>
<p> int <code>ldb_dn_compare</code> (struct ldb_dn *edn0, struct ldb_dn *edn1) </p>
<p> bool <code>ldb_dn_add_base</code> (struct ldb_dn *dn, struct ldb_dn *base) </p>
<p> bool <code>ldb_dn_add_base_fmt</code> (struct ldb_dn *dn, const char *base_fmt,&#8230;) PRINTF_ATTRIBUTE(2 </p>
<p> bool bool <code>ldb_dn_add_child</code> (struct ldb_dn *dn, struct ldb_dn *child) </p>
<p> bool <code>ldb_dn_add_child_fmt</code> (struct ldb_dn *dn, const char *child_fmt,&#8230;) PRINTF_ATTRIBUTE(2 </p>
<p> bool bool <code>ldb_dn_remove_base_components</code> (struct ldb_dn *dn, unsigned int num) </p>
<p> bool <code>ldb_dn_remove_child_components</code> (struct ldb_dn *dn, unsigned int num) </p>
<p> struct ldb_dn * <code>ldb_dn_copy</code> (TALLOC_CTX *mem_ctx, struct ldb_dn *dn) </p>
<p> struct ldb_dn * <code>ldb_dn_get_parent</code> (TALLOC_CTX *mem_ctx, struct ldb_dn *dn) </p>
<p> char * <code>ldb_dn_canonical_string</code> (TALLOC_CTX *mem_ctx, struct ldb_dn *dn) </p>
<p> char * <code>ldb_dn_canonical_ex_string</code> (TALLOC_CTX *mem_ctx, struct ldb_dn *dn) </p>
<p> int <code>ldb_dn_get_comp_num</code> (struct ldb_dn *dn) </p>
<p> int <code>ldb_dn_get_extended_comp_num</code> (struct ldb_dn *dn) </p>
<p> const char * <code>ldb_dn_get_component_name</code> (struct ldb_dn *dn, unsigned int num) </p>
<p> struct <code>ldb_val</code> * <code>ldb_dn_get_component_val</code> (struct ldb_dn *dn, unsigned int num) </p>
<p> const char * <code>ldb_dn_get_rdn_name</code> (struct ldb_dn *dn) </p>
<p> struct <code>ldb_val</code> * <code>ldb_dn_get_rdn_val</code> (struct ldb_dn *dn) </p>
<p> int <code>ldb_dn_set_component</code> (struct ldb_dn *dn, int num, const char *name, const struct <code>ldb_val</code> val) </p>
<p> bool <code>ldb_dn_is_valid</code> (struct ldb_dn *dn) </p>
<p> bool <code>ldb_dn_is_special</code> (struct ldb_dn *dn) </p>
<p> bool <code>ldb_dn_check_special</code> (struct ldb_dn *dn, const char *check) </p>
<p> bool <code>ldb_dn_is_null</code> (struct ldb_dn *dn) </p>
<p> int <code>ldb_dn_update_components</code> (struct ldb_dn *dn, const struct ldb_dn *ref_dn) </p>
<p> char * <code>ldb_attr_casefold</code> (TALLOC_CTX *mem_ctx, const char *s) </p>
<p> int <code>ldb_attr_dn</code> (const char *attr) </p>
<p> struct <code>ldb_message</code> * <code>ldb_msg_new</code> (TALLOC_CTX *mem_ctx)<br />
 <i>Create an empty message. </i><br />
 struct <code>ldb_message_element</code> * <code>ldb_msg_find_element</code> (const struct <code>ldb_message</code> *msg, const char *attr_name)<br />
 <i>Find an element within an message. </i><br />
 int <code>ldb_val_equal_exact</code> (const struct <code>ldb_val</code> *v1, const struct <code>ldb_val</code> *v2)<br />
 <i>Compare two </i><code>ldb_val</code> values.<br />
 struct <code>ldb_val</code> * <code>ldb_msg_find_val</code> (const struct <code>ldb_message_element</code> *el, struct <code>ldb_val</code> *val)<br />
 <i>find a value within an </i><code>ldb_message_element</code><br />
 int <code>ldb_msg_add_empty</code> (struct <code>ldb_message</code> *msg, const char *attr_name, int flags, struct <code>ldb_message_element</code> **return_el)<br />
 <i>add a new empty element to a </i><code>ldb_message</code><br />
 int <code>ldb_msg_add</code> (struct <code>ldb_message</code> *msg, const struct <code>ldb_message_element</code> *el, int flags)<br />
 <i>add a element to a </i><code>ldb_message</code><br />
 int <code>ldb_msg_add_value</code> (struct <code>ldb_message</code> *msg, const char *attr_name, const struct <code>ldb_val</code> *val, struct <code>ldb_message_element</code> **return_el) </p>
<p> int <code>ldb_msg_add_steal_value</code> (struct <code>ldb_message</code> *msg, const char *attr_name, struct <code>ldb_val</code> *val) </p>
<p> int <code>ldb_msg_add_steal_string</code> (struct <code>ldb_message</code> *msg, const char *attr_name, char *str) </p>
<p> int <code>ldb_msg_add_string</code> (struct <code>ldb_message</code> *msg, const char *attr_name, const char *str) </p>
<p> int <code>ldb_msg_add_linearized_dn</code> (struct <code>ldb_message</code> *msg, const char *attr_name, struct ldb_dn *dn) </p>
<p> int <code>ldb_msg_add_fmt</code> (struct <code>ldb_message</code> *msg, const char *attr_name, const char *fmt,&#8230;) PRINTF_ATTRIBUTE(3 </p>
<p> int int <code>ldb_msg_element_compare</code> (struct <code>ldb_message_element</code> *el1, struct <code>ldb_message_element</code> *el2)<br />
 <i>compare two message elements &#8211; return 0 on match </i><br />
 int <code>ldb_msg_element_compare_name</code> (struct <code>ldb_message_element</code> *el1, struct <code>ldb_message_element</code> *el2) </p>
<p> struct <code>ldb_val</code> * <code>ldb_msg_find_ldb_val</code> (const struct <code>ldb_message</code> *msg, const char *attr_name)<br />
 <i>Find elements in a message. </i><br />
 int <code>ldb_msg_find_attr_as_int</code> (const struct <code>ldb_message</code> *msg, const char *attr_name, int default_value) </p>
<p> unsigned int <code>ldb_msg_find_attr_as_uint</code> (const struct <code>ldb_message</code> *msg, const char *attr_name, unsigned int default_value) </p>
<p> int64_t <code>ldb_msg_find_attr_as_int64</code> (const struct <code>ldb_message</code> *msg, const char *attr_name, int64_t default_value) </p>
<p> uint64_t <code>ldb_msg_find_attr_as_uint64</code> (const struct <code>ldb_message</code> *msg, const char *attr_name, uint64_t default_value) </p>
<p> double <code>ldb_msg_find_attr_as_double</code> (const struct <code>ldb_message</code> *msg, const char *attr_name, double default_value) </p>
<p> int <code>ldb_msg_find_attr_as_bool</code> (const struct <code>ldb_message</code> *msg, const char *attr_name, int default_value) </p>
<p> const char * <code>ldb_msg_find_attr_as_string</code> (const struct <code>ldb_message</code> *msg, const char *attr_name, const char *default_value) </p>
<p> struct ldb_dn * <code>ldb_msg_find_attr_as_dn</code> (struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const struct <code>ldb_message</code> *msg, const char *attr_name) </p>
<p> void <code>ldb_msg_sort_elements</code> (struct <code>ldb_message</code> *msg) </p>
<p> struct <code>ldb_message</code> * <code>ldb_msg_copy_shallow</code> (TALLOC_CTX *mem_ctx, const struct <code>ldb_message</code> *msg) </p>
<p> struct <code>ldb_message</code> * <code>ldb_msg_copy</code> (TALLOC_CTX *mem_ctx, const struct <code>ldb_message</code> *msg) </p>
<p> struct <code>ldb_message</code> * <code>ldb_msg_canonicalize</code> (struct <code>ldb_context</code> *ldb, const struct <code>ldb_message</code> *msg) _DEPRECATED_ </p>
<p> int <code>ldb_msg_normalize</code> (struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const struct <code>ldb_message</code> *msg, struct <code>ldb_message</code> **_msg_out) </p>
<p> struct <code>ldb_message</code> * <code>ldb_msg_diff</code> (struct <code>ldb_context</code> *ldb, struct <code>ldb_message</code> *msg1, struct <code>ldb_message</code> *msg2) _DEPRECATED_ </p>
<p> int <code>ldb_msg_difference</code> (struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, struct <code>ldb_message</code> *msg1, struct <code>ldb_message</code> *msg2, struct <code>ldb_message</code> **_msg_out)<br />
 <i>return a </i><code>ldb_message</code> representing the differences between msg1 and msg2.<br />
 int <code>ldb_msg_check_string_attribute</code> (const struct <code>ldb_message</code> *msg, const char *name, const char *value)<br />
 <i>Tries to find a certain string attribute in a message. </i><br />
 int <code>ldb_msg_sanity_check</code> (struct <code>ldb_context</code> *ldb, const struct <code>ldb_message</code> *msg)<br />
 <i>Integrity check an </i><code>ldb_message</code>.<br />
 struct <code>ldb_val</code> <code>ldb_val_dup</code> (TALLOC_CTX *mem_ctx, const struct <code>ldb_val</code> *v)<br />
 <i>Duplicate an </i><code>ldb_val</code> structure.<br />
 int <code>ldb_set_debug</code> (struct <code>ldb_context</code> *ldb, void(*debug)(void *context, enum ldb_debug_level level, const char *fmt, va_list ap) PRINTF_ATTRIBUTE(3, 0), void *context)<br />
 <i>this allows the user to set a debug function for error reporting </i><br />
 void <code>ldb_set_utf8_fns</code> (struct <code>ldb_context</code> *ldb, void *context, char *(*casefold)(void *, void *, const char *, size_t n))<br />
 <i>this allows the user to set custom utf8 function for error reporting </i><br />
 int <code>ldb_set_debug_stderr</code> (struct <code>ldb_context</code> *ldb)<br />
 <i>this sets up debug to print messages on stderr </i><br />
 int <code>ldb_set_opaque</code> (struct <code>ldb_context</code> *ldb, const char *name, void *value) </p>
<p> void * <code>ldb_get_opaque</code> (struct <code>ldb_context</code> *ldb, const char *name) </p>
<p> const char ** <code>ldb_attr_list_copy</code> (TALLOC_CTX *mem_ctx, const char *const *attrs) </p>
<p> const char ** <code>ldb_attr_list_copy_add</code> (TALLOC_CTX *mem_ctx, const char *const *attrs, const char *new_attr) </p>
<p> int <code>ldb_attr_in_list</code> (const char *const *attrs, const char *attr) </p>
<p> int <code>ldb_msg_rename_attr</code> (struct <code>ldb_message</code> *msg, const char *attr, const char *replace) </p>
<p> int <code>ldb_msg_copy_attr</code> (struct <code>ldb_message</code> *msg, const char *attr, const char *replace) </p>
<p> void <code>ldb_msg_remove_attr</code> (struct <code>ldb_message</code> *msg, const char *attr) </p>
<p> void <code>ldb_msg_remove_element</code> (struct <code>ldb_message</code> *msg, struct <code>ldb_message_element</code> *el) </p>
<p> void <code>ldb_parse_tree_attr_replace</code> (struct <code>ldb_parse_tree</code> *tree, const char *attr, const char *replace) </p>
<p> struct <code>ldb_parse_tree</code> * <code>ldb_parse_tree_copy_shallow</code> (TALLOC_CTX *mem_ctx, const struct <code>ldb_parse_tree</code> *ot) </p>
<p> char * <code>ldb_timestring</code> (TALLOC_CTX *mem_ctx, time_t t)<br />
 <i>Convert a time structure to a string. </i><br />
 time_t <code>ldb_string_to_time</code> (const char *s)<br />
 <i>Convert a string to a time structure. </i><br />
 int <code>ldb_val_to_time</code> (const struct <code>ldb_val</code> *v, time_t *t)<br />
 <i>convert a LDAP GeneralizedTime string in </i><code>ldb_val</code> format to a time_t.<br />
 char * <code>ldb_timestring_utc</code> (TALLOC_CTX *mem_ctx, time_t t)<br />
 <i>Convert a time structure to a string. </i><br />
 time_t <code>ldb_string_utc_to_time</code> (const char *s)<br />
 <i>Convert a string to a time structure. </i><br />
 void <code>ldb_qsort</code> (void *const pbase, size_t total_elems, size_t size, void *opaque, ldb_qsort_cmp_fn_t cmp) </p>
<p> char * <code>ldb_control_to_string</code> (TALLOC_CTX *mem_ctx, const struct <code>ldb_control</code> *control)<br />
 <i>Convert a control into its string representation. </i><br />
 struct <code>ldb_control</code> * <code>ldb_parse_control_from_string</code> (struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const char *control_strings)<br />
 <i>Convert a string representing a control into a </i><code>ldb_control</code> structure.<br />
 struct <code>ldb_control</code> ** <code>ldb_parse_control_strings</code> (struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const char **control_strings)<br />
 <i>Convert an array of string represention of a control into an array of </i><code>ldb_control</code> structures.<br />
 unsigned int <code>ldb_get_flags</code> (struct <code>ldb_context</code> *ldb)<br />
 <i>return the ldb flags </i><br />
 void <code>ldb_set_flags</code> (struct <code>ldb_context</code> *ldb, unsigned flags) </p>
<p> struct ldb_dn * <code>ldb_dn_binary_from_ldb_val</code> (TALLOC_CTX *mem_ctx, struct <code>ldb_context</code> *ldb, const struct <code>ldb_val</code> *strdn) </p>
<p> int <code>ldb_dn_get_binary</code> (struct ldb_dn *dn, struct <code>ldb_val</code> *val) </p>
<p> int <code>ldb_dn_set_binary</code> (struct ldb_dn *dn, struct <code>ldb_val</code> *val) </p>
<p> void <code>ldb_req_set_location</code> (struct <code>ldb_request</code> *req, const char *location) </p>
<p> const char * <code>ldb_req_location</code> (struct <code>ldb_request</code> *req) </p>
<p> bool <code>ldb_dn_minimise</code> (struct ldb_dn *dn) </p>
<p> int <code>ldb_val_string_cmp</code> (const struct <code>ldb_val</code> *v, const char *str) </p>
<h2>Detailed Description</h2>
<p> Samba&#8217;s ldb database. </p>
<p> This header file provides the main API for ldb.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define ldb_attr_cmp(a, b) strcasecmp(a, b)</h3>
<p> Compare two attributes. This function compares to attribute names. Note that this is a case-insensitive comparison. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>a</i> the first attribute name to compare<br />
 <i>b</i> the second attribute name to compare</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> 0 if the attribute names are the same, or only differ in case; non-zero if there are any differences</dl>
<p> attribute names are restricted by rfc2251 so using strcasecmp and toupper here is ok. return 0 for match</p>
<h3>#define LDB_ATTR_FLAG_FIXED (1&lt;&lt;2)</h3>
<p> The attribute is supplied by the application and should not be removed.</p>
<h3>#define LDB_ATTR_FLAG_HIDDEN (1&lt;&lt;0)</h3>
<p> The attribute is not returned by default.</p>
<h3>#define LDB_CONTROL_AS_SYSTEM_OID &#8216;1.3.6.1.4.1.7165.4.3.7&#8217;</h3>
<p> LDB_CONTROL_AS_SYSTEM is used to skip access checks on operations that are performed by the system, but with a user&#8217;s credentials, e.g. updating prefix map</p>
<h3>#define LDB_CONTROL_ASQ_OID &#8216;1.2.840.113556.1.4.1504&#8217;</h3>
<p> OID for LDAP Attribute Scoped Query extension. This control is included in SearchRequest or SearchResponse messages as part of the controls field of the LDAPMessage.</p>
<h3>#define LDB_CONTROL_BYPASS_OPERATIONAL_OID &#8216;1.3.6.1.4.1.7165.4.3.13&#8217;</h3>
<p> OID for getting and manipulating attributes from the ldb without interception in the operational module. It can be used to access attribute that used to be stored in the sam and that are now calculated.</p>
<h3>#define LDB_CONTROL_DIRSYNC_OID &#8216;1.2.840.113556.1.4.841&#8217;</h3>
<p> OID for LDAP Directory Sync extension. This control is included in SearchRequest or SearchResponse messages as part of the controls field of the LDAPMessage.</p>
<h3>#define LDB_CONTROL_DOMAIN_SCOPE_OID &#8216;1.2.840.113556.1.4.1339&#8217;</h3>
<p> OID for specifying an advanced scope for the search (one partition) </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> Microsoft documentation of this OID</dl>
<h3>#define LDB_CONTROL_EXTENDED_DN_OID &#8216;1.2.840.113556.1.4.529&#8217;</h3>
<p> OID for extended DN. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> Microsoft documentation of this OID</dl>
<h3>#define LDB_CONTROL_NOTIFICATION_OID &#8216;1.2.840.113556.1.4.528&#8217;</h3>
<p> OID for notification. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> Microsoft documentation of this OID</dl>
<h3>#define LDB_CONTROL_PAGED_RESULTS_OID &#8216;1.2.840.113556.1.4.319&#8217;</h3>
<p> OID for the paged results control. This control is included in the searchRequest and searchResultDone messages as part of the controls field of the LDAPMessage, as defined in Section 4.1.12 of LDAP v3. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> RFC 2696.</dl>
<h3>#define LDB_CONTROL_PERMISSIVE_MODIFY_OID &#8216;1.2.840.113556.1.4.1413&#8217;</h3>
<p> OID to let modifies don&#8217;t give an error when adding an existing attribute with the same value or deleting an nonexisting one attribute. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> Microsoft documentation of this OID</dl>
<h3>#define LDB_CONTROL_PROVISION_OID &#8216;1.3.6.1.4.1.7165.4.3.16&#8217;</h3>
<p> LDB_CONTROL_PROVISION_OID is used to skip some constraint checks. It&#8217;s is mainly thought to be used for the provisioning.</p>
<h3>#define LDB_CONTROL_RECALCULATE_SD_OID &#8216;1.3.6.1.4.1.7165.4.3.5&#8217;</h3>
<p> OID for recalculate SD control. This control force the dsdb code to recalculate the SD of the object as if the object was just created.</p>
<h3>#define LDB_CONTROL_RELAX_OID &#8216;1.3.6.1.4.1.4203.666.5.12&#8217;</h3>
<p> OID for the allowing client to request temporary relaxed enforcement of constraints of the x.500 model. Mainly used for the OpenLDAP backend. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> draft managedit.</dl>
<h3>#define LDB_CONTROL_REVEAL_INTERNALS &#8216;1.3.6.1.4.1.7165.4.3.6&#8217;</h3>
<p> REVEAL_INTERNALS is used to reveal internal attributes and DN components which are not normally shown to the user.</p>
<h3>#define LDB_CONTROL_RODC_DCPROMO_OID &#8216;1.2.840.113556.1.4.1341&#8217;</h3>
<p> Control for RODC join -see [MS-ADTS] section 3.1.1.3.4.1.23. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> Microsoft documentation of this OID</dl>
<h3>#define LDB_CONTROL_SD_FLAGS_OID &#8216;1.2.840.113556.1.4.801&#8217;</h3>
<p> OID for specifying the returned elements of the ntSecurityDescriptor. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> Microsoft documentation of this OID</dl>
<h3>#define LDB_CONTROL_SEARCH_OPTIONS_OID &#8216;1.2.840.113556.1.4.1340&#8217;</h3>
<p> OID for specifying an advanced scope for a search. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> Microsoft documentation of this OID</dl>
<h3>#define LDB_CONTROL_SERVER_LAZY_COMMIT &#8216;1.2.840.113556.1.4.619&#8217;</h3>
<p> OID to allow the server to be more &#8216;fast and loose&#8217; with the data being added. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> Microsoft documentation of this OID</dl>
<h3>#define LDB_CONTROL_SERVER_SORT_OID &#8216;1.2.840.113556.1.4.473&#8217;</h3>
<p> OID for LDAP server sort result extension. This control is included in the searchRequest message as part of the controls field of the LDAPMessage, as defined in Section 4.1.12 of LDAP v3. The controlType is set to &#8216;1.2.840.113556.1.4.473&#8217;. The criticality MAY be either TRUE or FALSE (where absent is also equivalent to FALSE) at the client&#8217;s option. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> RFC 2891.</dl>
<h3>#define LDB_CONTROL_SHOW_DEACTIVATED_LINK_OID &#8216;1.2.840.113556.1.4.2065&#8217;</h3>
<p> OID for getting deactivated linked attributes. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> Microsoft documentation of this OID</dl>
<h3>#define LDB_CONTROL_SHOW_DELETED_OID &#8216;1.2.840.113556.1.4.417&#8217;</h3>
<p> OID for getting deleted objects. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> Microsoft documentation of this OID</dl>
<h3>#define LDB_CONTROL_SHOW_RECYCLED_OID &#8216;1.2.840.113556.1.4.2064&#8217;</h3>
<p> OID for getting recycled objects. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> Microsoft documentation of this OID</dl>
<h3>#define LDB_CONTROL_SORT_RESP_OID &#8216;1.2.840.113556.1.4.474&#8217;</h3>
<p> OID for LDAP server sort result response extension. This control is included in the searchResultDone message as part of the controls field of the LDAPMessage, as defined in Section 4.1.12 of LDAP v3. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> RFC 2891.</dl>
<h3>#define LDB_CONTROL_TREE_DELETE_OID &#8216;1.2.840.113556.1.4.805&#8217;</h3>
<p> OID for performing subtree deletes. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> Microsoft documentation of this OID</dl>
<h3>#define LDB_CONTROL_VERIFY_NAME_OID &#8216;1.2.840.113556.1.4.1338&#8217;</h3>
<p> OID for the allowing some kind of relax check for attributes with DNs. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> 3.1.1.3.4.1.16 in [MS-ADTS].pdf</dl>
<h3>#define LDB_CONTROL_VLV_REQ_OID &#8216;2.16.840.1.113730.3.4.9&#8217;</h3>
<p> OID for LDAP Virtual List View Request extension. This control is included in SearchRequest messages as part of the controls field of the LDAPMessage.</p>
<h3>#define LDB_CONTROL_VLV_RESP_OID &#8216;2.16.840.1.113730.3.4.10&#8217;</h3>
<p> OID for LDAP Virtual List View Response extension. This control is included in SearchResponse messages as part of the controls field of the LDAPMessage.</p>
<h3>#define LDB_EXTENDED_DYNAMIC_OID &#8216;1.3.6.1.4.1.1466.101.119.1&#8217;</h3>
<p> OID for LDAP Extended Operation DYNAMIC_REFRESH. This Extended operation is used to create and maintain objects which exist only a specific time, e.g. when a certain client or a certain person is logged in. Data refreshes have to be periodically sent in a specific interval. Otherwise the entry is going to be removed.</p>
<h3>#define LDB_EXTENDED_FAST_BIND_OID &#8216;1.2.840.113556.1.4.1781&#8217;</h3>
<p> OID for LDAP Extended Operation FAST_BIND. This Extended operations is used to perform a fast bind.</p>
<h3>#define LDB_EXTENDED_PASSWORD_CHANGE_OID &#8216;1.3.6.1.4.1.4203.1.11.1&#8217;</h3>
<p> OID for LDAP Extended Operation PASSWORD_CHANGE. This Extended operation is used to allow user password changes by the user itself.</p>
<h3>#define LDB_EXTENDED_SEQUENCE_NUMBER &#8216;1.3.6.1.4.1.7165.4.4.3&#8217;</h3>
<p> OID for LDAP Extended Operation SEQUENCE_NUMBER. This extended operation is used to retrieve the extended sequence number.</p>
<h3>#define LDB_EXTENDED_START_TLS_OID &#8216;1.3.6.1.4.1.1466.20037&#8217;</h3>
<p> OID for LDAP Extended Operation START_TLS. This Extended operation is used to start a new TLS channel on top of a clear text channel.</p>
<h3>#define LDB_FLAG_INTERNAL_MASK 0xFFFFFFF0</h3>
<p> flag bits on an element usable only by the internal implementation</p>
<h3>#define LDB_FLAG_MOD_ADD 1</h3>
<p> Flag value used in ldap_modify() to indicate that attributes are being added. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> <code>LDB_FLAG_MOD_MASK</code></dl>
<h3>#define LDB_FLAG_MOD_DELETE 3</h3>
<p> Flag value used in ldap_modify() to indicate that attributes are being deleted. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> <code>LDB_FLAG_MOD_MASK</code></dl>
<h3>#define LDB_FLAG_MOD_MASK 0x3</h3>
<p> There are a number of flags that are used with ldap_modify() in ldb_message_element.flags fields. The LDB_FLAG_MOD_ADD, LDB_FLAG_MOD_DELETE and LDB_FLAG_MOD_REPLACE flags are used in ldap_modify() calls to specify whether attributes are being added, deleted or modified respectively.</p>
<h3>#define LDB_FLAG_MOD_REPLACE 2</h3>
<p> Flag value used in ldap_modify() to indicate that attributes are being replaced. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> <code>LDB_FLAG_MOD_MASK</code></dl>
<h3>#define LDB_FLAG_MOD_TYPE(flags) ((flags) &amp; <code>LDB_FLAG_MOD_MASK</code>)</h3>
<p> use this to extract the mod type from the operation</p>
<h3>#define LDB_FLG_ENABLE_TRACING 32</h3>
<p> Flags to enable ldb tracing.</p>
<h3>#define LDB_FLG_NOMMAP 8</h3>
<p> Flag to tell backends not to use mmap.</p>
<h3>#define LDB_FLG_NOSYNC 2</h3>
<p> Flag value for database connection mode. If LDB_FLG_NOSYNC is used in ldb_connect, then the database will be opened without synchronous operations, if possible.</p>
<h3>#define LDB_FLG_RDONLY 1</h3>
<p> Flag value for database connection mode. If LDB_FLG_RDONLY is used in ldb_connect, then the database will be opened read-only, if possible. </p>
<p> <code>Examples: </code> <code>ldbreader.c</code>.</p>
<h3>#define LDB_FLG_RECONNECT 4</h3>
<p> Flag value to specify autoreconnect mode. If LDB_FLG_RECONNECT is used in ldb_connect, then the backend will be opened in a way that makes it try to auto reconnect if the connection is dropped (actually make sense only with ldap).</p>
<h3>#define LDB_FLG_SHOW_BINARY 16</h3>
<p> Flag to tell ldif handlers not to force encoding of binary structures in base64.</p>
<h3>#define LDB_OID_COMPARATOR_AND &#8216;1.2.840.113556.1.4.803&#8217;</h3>
<p> OID for logic AND comaprison. This is the well known object ID for a logical AND comparitor.</p>
<h3>#define LDB_OID_COMPARATOR_OR &#8216;1.2.840.113556.1.4.804&#8217;</h3>
<p> OID for logic OR comparison. This is the well known object ID for a logical OR comparitor.</p>
<h3>#define LDB_SYNTAX_BOOLEAN &#8216;1.3.6.1.4.1.1466.115.121.1.7&#8217;</h3>
<p> LDAP attribute syntax for a boolean. This is the well-known LDAP attribute syntax for a boolean. </p>
<p> See RFC 2252, Section 4.3.2</p>
<h3>#define LDB_SYNTAX_DIRECTORY_STRING &#8216;1.3.6.1.4.1.1466.115.121.1.15&#8217;</h3>
<p> LDAP attribute syntax for a Directory String. This is the well-known LDAP attribute syntax for a Directory String. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> RFC 2252, Section 4.3.2</dl>
<h3>#define LDB_SYNTAX_DN &#8216;1.3.6.1.4.1.1466.115.121.1.12&#8217;</h3>
<p> LDAP attribute syntax for a DN. This is the well-known LDAP attribute syntax for a DN. </p>
<p> See RFC 2252, Section 4.3.2</p>
<h3>#define LDB_SYNTAX_INTEGER &#8216;1.3.6.1.4.1.1466.115.121.1.27&#8217;</h3>
<p> LDAP attribute syntax for an integer. This is the well-known LDAP attribute syntax for an integer. </p>
<p> See RFC 2252, Section 4.3.2</p>
<h3>#define LDB_SYNTAX_OCTET_STRING &#8216;1.3.6.1.4.1.1466.115.121.1.40&#8217;</h3>
<p> LDAP attribute syntax for an octet string. This is the well-known LDAP attribute syntax for an octet string. </p>
<p> See RFC 2252, Section 4.3.2</p>
<h3>#define LDB_SYNTAX_UTC_TIME &#8216;1.3.6.1.4.1.1466.115.121.1.53&#8217;</h3>
<p> LDAP attribute syntax for UTC time. This is the well-known LDAP attribute syntax for a UTC time. </p>
<p> See RFC 2252, Section 4.3.2</p>
<h3>#define LDB_TYPESAFE_QSORT(base, numel, opaque, comparison)</h3>
<p> <code>Value:</code> </p>
<pre>
do {     if (numel &gt; 1) {         ldb_qsort(base, numel, sizeof((base)[0]), discard_const(opaque), (ldb_qsort_cmp_fn_t)comparison);         comparison(&amp;((base)[0]), &amp;((base)[1]), opaque);         } } while (0)
</pre>
<h3>#define TYPESAFE_QSORT(base, numel, comparison)</h3>
<p> <code>Value:</code> </p>
<pre>
do {     if (numel &gt; 1) {         qsort(base, numel, sizeof((base)[0]), (int (*)(const void *, const void *))comparison);         comparison(&amp;((base)[0]), &amp;((base)[1]));     } } while (0)
</pre>
<h2>Function Documentation</h2>
<h3>int int <code>ldb_add</code> (struct <code>ldb_context</code> *ldb, const struct <code>ldb_message</code> *message)</h3>
<p> Add a record to the database. This function adds a record to the database. This function will fail if a record with the specified class and key already exists in the database. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the context associated with the database (from <code>ldb_init()</code>)<br />
 <i>message</i> the message containing the record to add.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS if the record was added, otherwise a failure code)</dl>
<h3>int ldb_base64_decode (char *s)</h3>
<p> Base64 decode a buffer. This function decodes a base64 encoded string in place. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>s</i> the string to decode.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the length of the returned (decoded) string.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dt>
<dd> the string is null terminated, but the null terminator is not included in the length.</dl>
<h3>char* ldb_base64_encode (TALLOC_CTX *mem_ctx, const char *buf, intlen)</h3>
<p> Base64 encode a buffer. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>mem_ctx</i> the memory context that the result is allocated from.<br />
 <i>buf</i> pointer to the array that is to be encoded<br />
 <i>len</i> the number of elements in the array to be encoded</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> pointer to an array containing the encoded data</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dt>
<dd> The caller is responsible for freeing the result</dl>
<h3>char* ldb_binary_encode (TALLOC_CTX *mem_ctx, struct <code>ldb_val</code>val)</h3>
<p> Encode a binary blob. This function encodes a binary blob using the encoding rules in RFC 2254 (Section 4). This function also escapes any non-printable characters. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>mem_ctx</i> the memory context to allocate the return string in.<br />
 <i>val</i> the (potentially) binary data to be encoded</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the encoded data as a null terminated string</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> RFC 2252.</dl>
<h3>char* ldb_binary_encode_string (TALLOC_CTX *mem_ctx, const char *string)</h3>
<p> Encode a string. This function encodes a string using the encoding rules in RFC 2254 (Section 4). This function also escapes any non-printable characters. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>mem_ctx</i> the memory context to allocate the return string in.<br />
 <i>string</i> the string to be encoded</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the encoded data as a null terminated string</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> RFC 2252.</dl>
<h3>int ldb_build_add_req (struct <code>ldb_request</code> **ret_req, struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const struct <code>ldb_message</code> *message, struct <code>ldb_control</code> **controls, void *context, ldb_request_callback_tcallback, struct <code>ldb_request</code> *parent)</h3>
<p> Helper function to build an add request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ret_req</i> the request structure is returned here (talloced on mem_ctx)<br />
 <i>ldb</i> the context associated with the database (from <code>ldb_init()</code>)<br />
 <i>mem_ctx</i> a talloc memory context (used as parent of ret_req)<br />
 <i>message</i> contains the entry to be added<br />
 <i>controls</i> an array of controls<br />
 <i>context</i> the callback function context<br />
 <i>the</i> callback function to handle the async replies<br />
 <i>the</i> parent request if any</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS on success, or a failure code)</dl>
<h3>int ldb_build_del_req (struct <code>ldb_request</code> **ret_req, struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, struct ldb_dn *dn, struct <code>ldb_control</code> **controls, void *context, ldb_request_callback_tcallback, struct <code>ldb_request</code> *parent)</h3>
<p> Helper function to build a delete request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ret_req</i> the request structure is returned here (talloced on mem_ctx)<br />
 <i>ldb</i> the context associated with the database (from <code>ldb_init()</code>)<br />
 <i>mem_ctx</i> a talloc memory context (used as parent of ret_req)<br />
 <i>dn</i> the DN to be deleted<br />
 <i>controls</i> an array of controls<br />
 <i>context</i> the callback function context<br />
 <i>the</i> callback function to handle the async replies<br />
 <i>the</i> parent request if any</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS on success, or a failure code)</dl>
<h3>int ldb_build_extended_req (struct <code>ldb_request</code> **ret_req, struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const char *oid, void *data, struct <code>ldb_control</code> **controls, void *context, ldb_request_callback_tcallback, struct <code>ldb_request</code> *parent)</h3>
<p> Helper function to build a extended request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ret_req</i> the request structure is returned here (talloced on mem_ctx)<br />
 <i>ldb</i> the context associated with the database (from <code>ldb_init()</code>)<br />
 <i>mem_ctx</i> a talloc memory context (used as parent of ret_req)<br />
 <i>oid</i> the OID of the extended operation.<br />
 <i>data</i> a void pointer a the extended operation specific parameters, it needs to be NULL or a valid talloc pointer! talloc_get_type() will be used on it<br />
 <i>controls</i> an array of controls<br />
 <i>context</i> the callback function context<br />
 <i>the</i> callback function to handle the async replies<br />
 <i>the</i> parent request if any</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS on success, or a failure code)</dl>
<h3>int ldb_build_mod_req (struct <code>ldb_request</code> **ret_req, struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const struct <code>ldb_message</code> *message, struct <code>ldb_control</code> **controls, void *context, ldb_request_callback_tcallback, struct <code>ldb_request</code> *parent)</h3>
<p> Helper function to build a modify request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ret_req</i> the request structure is returned here (talloced on mem_ctx)<br />
 <i>ldb</i> the context associated with the database (from <code>ldb_init()</code>)<br />
 <i>mem_ctx</i> a talloc memory context (used as parent of ret_req)<br />
 <i>message</i> contains the entry to be modified<br />
 <i>controls</i> an array of controls<br />
 <i>context</i> the callback function context<br />
 <i>the</i> callback function to handle the async replies<br />
 <i>the</i> parent request if any</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS on success, or a failure code)</dl>
<h3>int ldb_build_rename_req (struct <code>ldb_request</code> **ret_req, struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, struct ldb_dn *olddn, struct ldb_dn *newdn, struct <code>ldb_control</code> **controls, void *context, ldb_request_callback_tcallback, struct <code>ldb_request</code> *parent)</h3>
<p> Helper function to build a rename request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ret_req</i> the request structure is returned here (talloced on mem_ctx)<br />
 <i>ldb</i> the context associated with the database (from <code>ldb_init()</code>)<br />
 <i>mem_ctx</i> a talloc memory context (used as parent of ret_req)<br />
 <i>olddn</i> the old DN<br />
 <i>newdn</i> the new DN<br />
 <i>controls</i> an array of controls<br />
 <i>context</i> the callback function context<br />
 <i>the</i> callback function to handle the async replies<br />
 <i>the</i> parent request if any</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS on success, or a failure code)</dl>
<h3>int ldb_build_search_req (struct <code>ldb_request</code> **ret_req, struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, struct ldb_dn *base, enum ldb_scopescope, const char *expression, const char *const *attrs, struct <code>ldb_control</code> **controls, void *context, ldb_request_callback_tcallback, struct <code>ldb_request</code> *parent)</h3>
<p> Helper function to build a search request. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ret_req</i> the request structure is returned here (talloced on mem_ctx)<br />
 <i>ldb</i> the context associated with the database (from <code>ldb_init()</code>)<br />
 <i>mem_ctx</i> a talloc memory context (used as parent of ret_req)<br />
 <i>base</i> the Base Distinguished Name for the query (use <code>ldb_dn_new()</code> for an empty one)<br />
 <i>scope</i> the search scope for the query<br />
 <i>expression</i> the search expression to use for this query<br />
 <i>attrs</i> the search attributes for the query (pass NULL if none required)<br />
 <i>controls</i> an array of controls<br />
 <i>context</i> the callback function context<br />
 <i>the</i> callback function to handle the async replies<br />
 <i>the</i> parent request if any</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS on success, or a failure code)</dl>
<h3>char* ldb_casefold (struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const char *s, size_tn)</h3>
<p> Casefold a string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the ldb context<br />
 <i>mem_ctx</i> the memory context to allocate the result string memory from.<br />
 <i>s</i> the string that is to be folded</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> a copy of the string, converted to upper case</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dt>
<dd> The default function is not yet UTF8 aware. Provide your own set of functions through <code>ldb_set_utf8_fns()</code></dl>
<h3>int ldb_connect (struct <code>ldb_context</code> *ldb, const char *url, unsigned intflags, const char *options[])</h3>
<p> Connect to a database. This is typically called soon after <code>ldb_init()</code>, and is required prior to any search or database modification operations. </p>
<p> The URL can be one of the following forms:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd> <a href="tdb://path">tdb://path</a></p>
<dt>&bull;</p>
<dd> <a href="ldapi://path">ldapi://path</a></p>
<dt>&bull;</p>
<dd> <a href="ldap://host">ldap://host</a></p>
<dt>&bull;</p>
<dd> <a href="sqlite://path">sqlite://path</a></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the context associated with the database (from <code>ldb_init()</code>)<br />
 <i>url</i> the URL of the database to connect to, as noted above<br />
 <i>flags</i> a combination of LDB_FLG_* to modify the connection behaviour<br />
 <i>options</i> backend specific options &#8211; passed uninterpreted to the backend</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS on success, or a failure code)</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dt>
<dd> It is an error to connect to a database that does not exist in readonly mode (that is, with LDB_FLG_RDONLY). However in read-write mode, the database will be created if it does not exist.</dl>
<p> <code>Examples: </code> <code>ldbreader.c</code>.</p>
<h3>char* ldb_control_to_string (TALLOC_CTX *mem_ctx, const struct <code>ldb_control</code> *control)</h3>
<p> Convert a control into its string representation. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>mem_ctx</i> TALLOC context to return result on, and to allocate error_string on<br />
 <i>control</i> A struct <code>ldb_control</code> to convert</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> string representation of the control</dl>
<h3>int <code>ldb_delete</code> (struct <code>ldb_context</code> *ldb, struct ldb_dn *dn)</h3>
<p> Delete a record from the database. This function deletes a record from the database. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the context associated with the database (from <code>ldb_init()</code>)<br />
 <i>dn</i> the DN for the record to be deleted.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS if the record was deleted, otherwise a failure code)</dl>
<h3>char* ldb_dn_alloc_linearized (TALLOC_CTX *mem_ctx, struct ldb_dn *dn)</h3>
<p> Allocate a copy of the linear form of a DN (without any extended components) onto the supplied memory context. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>dn</i> The DN to linearize<br />
 <i>mem_ctx</i> TALLOC context to return result on</dl>
<h3>struct ldb_dn struct ldb_dn* ldb_dn_from_ldb_val (TALLOC_CTX *mem_ctx, struct <code>ldb_context</code> *ldb, const struct <code>ldb_val</code> *strdn)</h3>
<p> Allocate a new DN from a struct <code>ldb_val</code> (useful to avoid buffer overrun) </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>mem_ctx</i> TALLOC context to return resulting ldb_dn structure on<br />
 <i>dn</i> The new DN</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dt>
<dd> The DN will not be parsed at this time. Use ldb_dn_validate to tell if the DN is syntacticly correct</dl>
<h3>char* ldb_dn_get_extended_linearized (TALLOC_CTX *mem_ctx, struct ldb_dn *dn, intmode)</h3>
<p> Get the linear form of a DN (with any extended components) </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>mem_ctx</i> TALLOC context to return result on<br />
 <i>dn</i> The DN to linearize<br />
 <i>mode</i> Style of extended DN to return (0 is HEX representation of binary form, 1 is a string form)</dl>
<h3>const char* ldb_dn_get_linearized (struct ldb_dn *dn)</h3>
<p> Get the linear form of a DN (without any extended components) </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>dn</i> The DN to linearize</dl>
<h3>struct ldb_dn* ldb_dn_new (TALLOC_CTX *mem_ctx, struct <code>ldb_context</code> *ldb, const char *dn)</h3>
<p> Allocate a new DN from a string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>mem_ctx</i> TALLOC context to return resulting ldb_dn structure on<br />
 <i>dn</i> The new DN</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dt>
<dd> The DN will not be parsed at this time. Use ldb_dn_validate to tell if the DN is syntacticly correct</dl>
<h3>struct ldb_dn* ldb_dn_new_fmt (TALLOC_CTX *mem_ctx, struct <code>ldb_context</code> *ldb, const char *new_fmt, &#8230;)</h3>
<p> Allocate a new DN from a printf style format string and arguments. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>mem_ctx</i> TALLOC context to return resulting ldb_dn structure on<br />
 <i>new_fms</i> The new DN as a format string (plus arguments)</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dt>
<dd> The DN will not be parsed at this time. Use ldb_dn_validate to tell if the DN is syntacticly correct</dl>
<h3>bool ldb_dn_validate (struct ldb_dn *dn)</h3>
<p> Determine if this DN is syntactically valid. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>dn</i> The DN to validate</dl>
<h3>const char* ldb_errstring (struct <code>ldb_context</code> *ldb)</h3>
<p> return extended error information from the last call</p>
<h3>int <code>ldb_extended</code> (struct <code>ldb_context</code> *ldb, const char *oid, void *data, struct <code>ldb_result</code> **res)</h3>
<p> call an extended operation </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the context associated with the database (from <code>ldb_init()</code>)<br />
 <i>oid</i> the OID of the extended operation.<br />
 <i>data</i> a void pointer a the extended operation specific parameters, it needs to be NULL or a valid talloc pointer! talloc_get_type() will be used on it<br />
 <i>res</i> the result of the extended operation</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS if the extended operation returned fine, otherwise a failure code)</dl>
<h3>int ldb_extended_default_callback (struct <code>ldb_request</code> *req, struct <code>ldb_reply</code> *ares)</h3>
<p> The default async extended operation callback function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>req</i> the request we are callback of<br />
 <i>ares</i> a single reply from the async core</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS on success, or a failure code)</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dt>
<dd> this function expects req-&gt;context to always be an struct <code>ldb_result</code> pointer AND a talloc context, this function will steal on the context each message from the ares reply passed on by the async core so that in the end all the messages will be in the context (<code>ldb_result</code>) memory tree. Freeing the passed context (<code>ldb_result</code> tree) will free all the resources (the request need to be freed separately and the result doe not depend on the request that can be freed as sson as the search request is finished)</dl>
<h3>unsigned int ldb_get_flags (struct <code>ldb_context</code> *ldb)</h3>
<p> return the ldb flags</p>
<h3>int ldb_global_init (void)</h3>
<p> Initialise ldbs&#8217; global information. This is required before any other LDB call </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> 0 if initialisation succeeded, -1 otherwise</dl>
<h3>struct <code>ldb_context</code>* ldb_init (TALLOC_CTX *mem_ctx, struct tevent_context *ev_ctx)</h3>
<p> Initialise an ldb context. This is required before any other LDB call. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>mem_ctx</i> pointer to a talloc memory context. Pass NULL if there is no suitable context available.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> pointer to <code>ldb_context</code> that should be free&#8217;d (using talloc_free()) at the end of the program.</dl>
<p> <code>Examples: </code> <code>ldbreader.c</code>, and <code>ldifreader.c</code>.</p>
<h3>int ldb_ldif_parse_modrdn (struct <code>ldb_context</code> *ldb, const struct <code>ldb_ldif</code> *ldif, TALLOC_CTX *mem_ctx, struct ldb_dn **olddn, struct ldb_dn **newrdn, bool *deleteoldrdn, struct ldb_dn **newsuperior, struct ldb_dn **newdn)</h3>
<p> Parse a modrdn LDIF message from a struct <code>ldb_message</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the ldb context (from <code>ldb_init()</code>)<br />
 <i>ldif</i> the preparsed LDIF chunk (from <code>ldb_ldif_read()</code>)<br />
 <i>mem_ctx</i> the memory context that&#8217;s used for return values<br />
 <i>olddn</i> the old dn as struct ldb_dn, if not needed pass NULL<br />
 <i>newrdn</i> the new rdn as struct ldb_dn, if not needed pass NULL<br />
 <i>deleteoldrdn</i> the deleteoldrdn value as bool, if not needed pass NULL<br />
 <i>newsuperior</i> the newsuperior dn as struct ldb_dn, if not needed pass NULL newsuperior can be NULL as it is optional in the LDIF<br />
 <i>newdn</i> the full constructed new dn as struct ldb_dn, if not needed pass NULL</dl>
<h3>struct <code>ldb_ldif</code>* ldb_ldif_read (struct <code>ldb_context</code> *ldb, int(*)(void *)fgetc_fn, void *private_data)</h3>
<p> Read an LDIF message. This function creates an LDIF message using a caller supplied read function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the ldb context (from <code>ldb_init()</code>)<br />
 <i>fgetc_fn</i> a function pointer for the read function. This must take a private data pointer, and must return a pointer to an integer corresponding to the next byte read (or EOF if there is no more data to be read).<br />
 <i>private_data</i> pointer that will be provided back to the read function. This is udeful for maintaining state or context.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the LDIF message that has been read in</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dt>
<dd> You must free the LDIF message when no longer required, using <code>ldb_ldif_read_free()</code>.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> <code>ldb_ldif_read_file</code> for a more convenient way to read from a file stream. </p>
<p> <code>ldb_ldif_read_string</code> for a more convenient way to read from a string (char array). </p>
<p> <code>ldb_ldif_write</code> for the writer equivalent to this function.</dl>
<h3>struct <code>ldb_ldif</code>* ldb_ldif_read_file (struct <code>ldb_context</code> *ldb, FILE *f)</h3>
<p> Read an LDIF message from a file. This function reads the next LDIF message from the contents of a file stream. If you want to get all of the LDIF messages, you will need to repeatedly call this function, until it returns NULL. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the ldb context (from <code>ldb_init()</code>)<br />
 <i>f</i> the file stream to read from (typically from fdopen())</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> <code>ldb_ldif_read_string</code> for an equivalent function that will read from a string (char array). </p>
<p> <code>ldb_ldif_write_file</code> for the writer equivalent to this function.</dl>
<p> <code>Examples: </code> <code>ldifreader.c</code>.</p>
<h3>void ldb_ldif_read_free (struct <code>ldb_context</code> *ldb, struct <code>ldb_ldif</code> *msg)</h3>
<p> Clean up an LDIF message. This function cleans up a LDIF message read using <code>ldb_ldif_read()</code> or related functions (such as <code>ldb_ldif_read_string()</code> and <code>ldb_ldif_read_file()</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the ldb context (from <code>ldb_init()</code>)<br />
 <i>msg</i> the message to clean up and free</dl>
<p> <code>Examples: </code> <code>ldifreader.c</code>.</p>
<h3>struct <code>ldb_ldif</code>* ldb_ldif_read_string (struct <code>ldb_context</code> *ldb, const char **s)</h3>
<p> Read an LDIF message from a string. This function reads the next LDIF message from the contents of a char array. If you want to get all of the LDIF messages, you will need to repeatedly call this function, until it returns NULL. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the ldb context (from <code>ldb_init()</code>)<br />
 <i>s</i> pointer to the char array to read from</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> <code>ldb_ldif_read_file</code> for an equivalent function that will read from a file stream. </p>
<p> <code>ldb_ldif_write</code> for a more general (arbitrary read function) version of this function.</dl>
<h3>int ldb_ldif_write (struct <code>ldb_context</code> *ldb, int(*)(void *, const char *,&#8230;) PRINTF_ATTRIBUTE fprintf_fn(2, 3), void *private_data, const struct <code>ldb_ldif</code> *ldif)</h3>
<p> Write an LDIF message. This function writes an LDIF message using a caller supplied write function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the ldb context (from <code>ldb_init()</code>)<br />
 <i>fprintf_fn</i> a function pointer for the write function. This must take a private data pointer, followed by a format string, and then a variable argument list.<br />
 <i>private_data</i> pointer that will be provided back to the write function. This is useful for maintaining state or context.<br />
 <i>ldif</i> the message to write out</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the total number of bytes written, or an error code as returned from the write function.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> <code>ldb_ldif_write_file</code> for a more convenient way to write to a file stream. </p>
<p> <code>ldb_ldif_read</code> for the reader equivalent to this function.</dl>
<p> <code>Examples: </code> <code>ldbreader.c</code>, and <code>ldifreader.c</code>.</p>
<h3>int ldb_ldif_write_file (struct <code>ldb_context</code> *ldb, FILE *f, const struct <code>ldb_ldif</code> *msg)</h3>
<p> Write an LDIF message to a file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the ldb context (from <code>ldb_init()</code>)<br />
 <i>f</i> the file stream to write to (typically from fdopen())<br />
 <i>msg</i> the message to write out</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the total number of bytes written, or a negative error code</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> <code>ldb_ldif_read_file</code> for the reader equivalent to this function.</dl>
<h3>char* ldb_ldif_write_string (struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const struct <code>ldb_ldif</code> *msg)</h3>
<p> Write an LDIF message to a string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the ldb context (from <code>ldb_init()</code>)<br />
 <i>mem_ctx</i> the talloc context on which to attach the string)<br />
 <i>msg</i> the message to write out</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the string containing the LDIF, or NULL on error</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dt>
<dd> <code>ldb_ldif_read_string</code> for the reader equivalent to this function.</dl>
<h3>int <code>ldb_modify</code> (struct <code>ldb_context</code> *ldb, const struct <code>ldb_message</code> *message)</h3>
<p> Modify the specified attributes of a record. This function modifies a record that is in the database. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the context associated with the database (from <code>ldb_init()</code>)<br />
 <i>message</i> the message containing the changes required.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS if the record was modified as requested, otherwise a failure code)</dl>
<h3>int ldb_msg_add (struct <code>ldb_message</code> *msg, const struct <code>ldb_message_element</code> *el, intflags)</h3>
<p> add a element to a <code>ldb_message</code></p>
<h3>int ldb_msg_add_empty (struct <code>ldb_message</code> *msg, const char *attr_name, intflags, struct <code>ldb_message_element</code> **return_el)</h3>
<p> add a new empty element to a <code>ldb_message</code></p>
<h3>int ldb_msg_check_string_attribute (const struct <code>ldb_message</code> *msg, const char *name, const char *value)</h3>
<p> Tries to find a certain string attribute in a message. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>msg</i> the message to check<br />
 <i>name</i> attribute name<br />
 <i>value</i> attribute value</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> 1 on match and 0 otherwise.</dl>
<h3>int ldb_msg_difference (struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, struct <code>ldb_message</code> *msg1, struct <code>ldb_message</code> *msg2, struct <code>ldb_message</code> **_msg_out)</h3>
<p> return a <code>ldb_message</code> representing the differences between msg1 and msg2. If you then use this in a <code>ldb_modify()</code> call, it can be used to save edits to a message </p>
<p> Result message is constructed as follows:</p>
<dl COMPACT>
<dt>&bull;</p>
<dd> LDB_FLAG_MOD_ADD &#8211; elements found only in msg2</p>
<dt>&bull;</p>
<dd> LDB_FLAG_MOD_REPLACE &#8211; elements in msg2 that have different value in msg1 Value for msg2 element is used</p>
<dt>&bull;</p>
<dd> LDB_FLAG_MOD_DELETE &#8211; elements found only in msg2</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> LDB_SUCCESS or LDB_ERR_OPERATIONS_ERROR</dl>
<h3>int int ldb_msg_element_compare (struct <code>ldb_message_element</code> *el1, struct <code>ldb_message_element</code> *el2)</h3>
<p> compare two message elements &#8211; return 0 on match</p>
<h3>struct <code>ldb_message_element</code>* ldb_msg_find_element (const struct <code>ldb_message</code> *msg, const char *attr_name)</h3>
<p> Find an element within an message.</p>
<h3>struct <code>ldb_val</code>* ldb_msg_find_ldb_val (const struct <code>ldb_message</code> *msg, const char *attr_name)</h3>
<p> Find elements in a message. This function finds elements and converts to a specific type, with a give default value if not found. Assumes that elements are single valued.</p>
<h3>struct <code>ldb_val</code>* ldb_msg_find_val (const struct <code>ldb_message_element</code> *el, struct <code>ldb_val</code> *val)</h3>
<p> find a value within an <code>ldb_message_element</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>el</i> the element to search<br />
 <i>val</i> the value to search for</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dt>
<dd> This search is case sensitive</dl>
<h3>struct <code>ldb_message</code>* ldb_msg_new (TALLOC_CTX *mem_ctx)</h3>
<p> Create an empty message. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>mem_ctx</i> the memory context to create in. You can pass NULL to get the top level context, however the ldb context (from <code>ldb_init()</code>) may be a better choice</dl>
<h3>int ldb_msg_sanity_check (struct <code>ldb_context</code> *ldb, const struct <code>ldb_message</code> *msg)</h3>
<p> Integrity check an <code>ldb_message</code>. This function performs basic sanity / integrity checks on an <code>ldb_message</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> context in which to perform the checks<br />
 <i>msg</i> the message to check</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> LDB_SUCCESS if the message is OK, or a non-zero error code (one of LDB_ERR_INVALID_DN_SYNTAX, LDB_ERR_ENTRY_ALREADY_EXISTS or LDB_ERR_INVALID_ATTRIBUTE_SYNTAX) if there is a problem with a message.</dl>
<h3>int ldb_op_default_callback (struct <code>ldb_request</code> *req, struct <code>ldb_reply</code> *ares)</h3>
<p> The default async extended operation callback function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>req</i> the request we are callback of<br />
 <i>ares</i> a single reply from the async core</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS on success, or a failure code)</dl>
<h3>struct <code>ldb_control</code>* ldb_parse_control_from_string (struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const char *control_strings)</h3>
<p> Convert a string representing a control into a <code>ldb_control</code> structure. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> LDB context<br />
 <i>mem_ctx</i> TALLOC context to return result on, and to allocate error_string on<br />
 <i>control_strings</i> A string-formatted control</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> a <code>ldb_control</code> element</dl>
<h3>struct <code>ldb_control</code>** ldb_parse_control_strings (struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, const char **control_strings)</h3>
<p> Convert an array of string represention of a control into an array of <code>ldb_control</code> structures. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> LDB context<br />
 <i>mem_ctx</i> TALLOC context to return result on, and to allocate error_string on<br />
 <i>control_strings</i> Array of string-formatted controls</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> array of <code>ldb_control</code> elements</dl>
<h3>int <code>ldb_rename</code> (struct <code>ldb_context</code> *ldb, struct ldb_dn *olddn, struct ldb_dn *newdn)</h3>
<p> Rename a record in the database. This function renames a record in the database. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the context associated with the database (from <code>ldb_init()</code>)<br />
 <i>olddn</i> the DN for the record to be renamed.<br />
 <i>newdn</i> the new DN</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS if the record was renamed as requested, otherwise a failure code)</dl>
<h3>struct <code>ldb_control</code>* ldb_reply_get_control (struct <code>ldb_reply</code> *rep, const char *oid)</h3>
<p> check if a control with the specified &#8216;oid&#8217; exist and return it </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>rep</i> the reply struct where to add the control<br />
 <i>oid</i> the object identifier of the control as string</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the control, NULL if not found</dl>
<h3>int ldb_request_add_control (struct <code>ldb_request</code> *req, const char *oid, boolcritical, void *data)</h3>
<p> Add a <code>ldb_control</code> to a <code>ldb_request</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>req</i> the request struct where to add the control<br />
 <i>oid</i> the object identifier of the control as string<br />
 <i>critical</i> whether the control should be critical or not<br />
 <i>data</i> a talloc pointer to the control specific data</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS on success, or a failure code)</dl>
<h3>struct <code>ldb_control</code>* ldb_request_get_control (struct <code>ldb_request</code> *req, const char *oid)</h3>
<p> check if a control with the specified &#8216;oid&#8217; exist and return it </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>req</i> the request struct where to add the control<br />
 <i>oid</i> the object identifier of the control as string</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the control, NULL if not found</dl>
<h3>int ldb_request_replace_control (struct <code>ldb_request</code> *req, const char *oid, boolcritical, void *data)</h3>
<p> replace a <code>ldb_control</code> in a <code>ldb_request</code> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>req</i> the request struct where to add the control<br />
 <i>oid</i> the object identifier of the control as string<br />
 <i>critical</i> whether the control should be critical or not<br />
 <i>data</i> a talloc pointer to the control specific data</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS on success, or a failure code)</dl>
<h3>int <code>ldb_search</code> (struct <code>ldb_context</code> *ldb, TALLOC_CTX *mem_ctx, struct <code>ldb_result</code> **result, struct ldb_dn *base, enum ldb_scopescope, const char *const *attrs, const char *exp_fmt, &#8230;)</h3>
<p> Search the database. This function searches the database, and returns records that match an LDAP-like search expression </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>ldb</i> the context associated with the database (from <code>ldb_init()</code>)<br />
 <i>mem_ctx</i> the memory context to use for the request and the results<br />
 <i>result</i> the return result<br />
 <i>base</i> the Base Distinguished Name for the query (use <code>ldb_dn_new()</code> for an empty one)<br />
 <i>scope</i> the search scope for the query<br />
 <i>attrs</i> the search attributes for the query (pass NULL if none required)<br />
 <i>exp_fmt</i> the search expression to use for this query (printf like)</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS on success, or a failure code)</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dt>
<dd> use talloc_free() to free the <code>ldb_result</code> returned</dl>
<p> <code>Examples: </code> <code>ldbreader.c</code>.</p>
<h3>int ldb_search_default_callback (struct <code>ldb_request</code> *req, struct <code>ldb_reply</code> *ares)</h3>
<p> The default async search callback function. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>req</i> the request we are callback of<br />
 <i>ares</i> a single reply from the async core</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> result code (LDB_SUCCESS on success, or a failure code)</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dt>
<dd> this function expects req-&gt;context to always be an struct <code>ldb_result</code> pointer AND a talloc context, this function will steal on the context each message from the ares reply passed on by the async core so that in the end all the messages will be in the context (<code>ldb_result</code>) memory tree. Freeing the passed context (<code>ldb_result</code> tree) will free all the resources (the request need to be freed separately and the result doe not depend on the request that can be freed as sson as the search request is finished)</dl>
<h3>int ldb_sequence_number (struct <code>ldb_context</code> *ldb, enum ldb_sequence_typetype, uint64_t *seq_num)</h3>
<p> Obtain current/next database sequence number.</p>
<h3>int ldb_set_debug (struct <code>ldb_context</code> *ldb, void(*)(void *context, enum ldb_debug_level level, const char *fmt, va_list ap) PRINTF_ATTRIBUTE debug(3, 0), void *context)</h3>
<p> this allows the user to set a debug function for error reporting</p>
<h3>int ldb_set_debug_stderr (struct <code>ldb_context</code> *ldb)</h3>
<p> this sets up debug to print messages on stderr</p>
<h3>void ldb_set_utf8_default (struct <code>ldb_context</code> *ldb)</h3>
<p> setup the default utf8 functions FIXME: these functions do not yet handle utf8</p>
<h3>void ldb_set_utf8_fns (struct <code>ldb_context</code> *ldb, void *context, char *(*)(void *, void *, const char *, size_t n)casefold)</h3>
<p> this allows the user to set custom utf8 function for error reporting</p>
<h3>const char* ldb_strerror (intldb_err)</h3>
<p> return a string explaining what a ldb error constant meancs</p>
<h3>time_t ldb_string_to_time (const char *s)</h3>
<p> Convert a string to a time structure. This function converts an LDAP formatted GeneralizedTime string to a time_t structure. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>s</i> the string to convert</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the time structure, or 0 if the string cannot be converted</dl>
<h3>time_t ldb_string_utc_to_time (const char *s)</h3>
<p> Convert a string to a time structure. This function converts an LDAP formatted UTCTime string to a time_t structure. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>s</i> the string to convert</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the time structure, or 0 if the string cannot be converted</dl>
<h3>char* ldb_timestring (TALLOC_CTX *mem_ctx, time_tt)</h3>
<p> Convert a time structure to a string. This function converts a time_t structure to an LDAP formatted GeneralizedTime string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>mem_ctx</i> the memory context to allocate the return string in<br />
 <i>t</i> the time structure to convert</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the formatted string, or NULL if the time structure could not be converted</dl>
<h3>char* ldb_timestring_utc (TALLOC_CTX *mem_ctx, time_tt)</h3>
<p> Convert a time structure to a string. This function converts a time_t structure to an LDAP formatted UTCTime string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>mem_ctx</i> the memory context to allocate the return string in<br />
 <i>t</i> the time structure to convert</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the formatted string, or NULL if the time structure could not be converted</dl>
<h3>int ldb_transaction_cancel (struct <code>ldb_context</code> *ldb)</h3>
<p> cancel a transaction</p>
<h3>int ldb_transaction_commit (struct <code>ldb_context</code> *ldb)</h3>
<p> commit a transaction</p>
<h3>int ldb_transaction_prepare_commit (struct <code>ldb_context</code> *ldb)</h3>
<p> first phase of two phase commit</p>
<h3>int ldb_transaction_start (struct <code>ldb_context</code> *ldb)</h3>
<p> start a transaction</p>
<h3>struct <code>ldb_val</code> ldb_val_dup (TALLOC_CTX *mem_ctx, const struct <code>ldb_val</code> *v)</h3>
<p> Duplicate an <code>ldb_val</code> structure. This function copies an ldb value structure. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>mem_ctx</i> the memory context that the duplicated value will be allocated from<br />
 <i>v</i> the <code>ldb_val</code> to be duplicated.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the duplicated <code>ldb_val</code> structure.</dl>
<h3>int ldb_val_equal_exact (const struct <code>ldb_val</code> *v1, const struct <code>ldb_val</code> *v2)</h3>
<p> Compare two <code>ldb_val</code> values. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>v1</i> first <code>ldb_val</code> structure to be tested<br />
 <i>v2</i> second <code>ldb_val</code> structure to be tested</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> 1 for a match, 0 if there is any difference</dl>
<h3>int ldb_val_to_time (const struct <code>ldb_val</code> *v, time_t *t)</h3>
<p> convert a LDAP GeneralizedTime string in <code>ldb_val</code> format to a time_t.</p>
<h3>int ldb_valid_attr_name (const char *s)</h3>
<p> Check the attribute name is valid according to rfc2251. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>s</i> the string to check</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> 1 if the name is ok</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LDB from the source code.</p>
