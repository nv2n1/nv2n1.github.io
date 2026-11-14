---
title: "netsnmp_library(3)"
name: "netsnmp_library"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_library/"
description: "The Net-SNMP library –"
---

<p>The Net-SNMP library &#8211;</p>
<h3>Modules</h3>
<p><code>asn1 parsing and datatype manipulation routines.</code><br />
 <i>Note on. </i><br />
 <code>A generic callback mechanism</code> </p>
<p> <code>generic linked-list data handling with a string as a key.</code> </p>
<p> <code>storage space for defaults</code><br />
 <i>The purpose of the default storage is three-fold:. </i><br />
 <code>mib parsing and datatype manipulation routines.</code> </p>
<p> <code>Store and retrieve data referenced by an OID.</code><br />
 <i>This is essentially a way of storing data associated with a given OID. </i><br />
 <code>parsing various configuration files at run time</code><br />
 <i>The read_config related functions are a fairly extensible system of parsing various configuration files at the run time. </i><br />
 <code>generic library based alarm timers for various parts of an application</code> </p>
<p> <code>various PDU processing routines</code> </p>
<p> <code>generic logging for net-snmp</code> </p>
<p> <code>Memory Utility Routines</code></p>
<h3>Data Structures</h3>
<pre><code>struct snmp_internal_session



struct session_list



Defines
#define MIN(a, b)   (((a) &lt; (b)) ? (a) : (b))



#define MIB_CLIENTS_ARE_EVIL   1



#define _init_agent_callback_transport()



#define SNMP_NEED_REQUEST_LIST



#define timercmp(tvp, uvp, cmp)



#define timerclear(tvp)   (tvp)-&gt;tv_sec = (tvp)-&gt;tv_usec = 0



#define MAX_PACKET_LENGTH   (0x7fffffff)



#define NETSNMP_STREAM_QUEUE_LEN   5



#define BSD4_2



#define NFDBITS   (sizeof(fd_mask) * NBBY)



#define FD_SET(n, p)   ((p)-&gt;fds_bits[(n)/NFDBITS] |= (1 &lt;&lt; ((n) % NFDBITS)))



#define FD_CLR(n, p)   ((p)-&gt;fds_bits[(n)/NFDBITS] &amp;= ~(1 &lt;&lt; ((n) % NFDBITS)))



#define FD_ISSET(n, p)   ((p)-&gt;fds_bits[(n)/NFDBITS] &amp; (1 &lt;&lt; ((n) % NFDBITS)))



#define FD_ZERO(p)   memset((p), 0, sizeof(*(p)))



#define DEFAULT_COMMUNITY   'public'



#define DEFAULT_RETRIES   5



#define DEFAULT_TIMEOUT   1000000L



#define DEFAULT_REMPORT   SNMP_PORT



#define DEFAULT_ENTERPRISE   default_enterprise



#define DEFAULT_TIME   0



#define MAXIMUM_PACKET_SIZE   0x7fffffff



#define DEBUGPRINTPDUTYPE(token, type)   DEBUGDUMPSECTION(token, snmp_pdu_type(type))



#define ERROR_STAT_LENGTH   11



Typedefs</code></pre>
<p> typedef long <code>fd_mask</code></p>
<h3>Functions</h3>
<pre><code>int init_agent (const char *app)


Initialize the agent.


void shutdown_agent (void)



void add_to_init_list (char *module_list)



int should_init (const char *module_name)



int snmp_build (u_char **pkt, size_t *pkt_len, size_t *offset, netsnmp_session *pss, netsnmp_pdu *pdu)



int snmp_get_errno (void)



void snmp_synch_reset (netsnmp_session *notused)



void snmp_synch_setup (netsnmp_session *notused)



const char * strerror (int err)



const char * snmp_pdu_type (int type)



long snmp_get_next_reqid (void)



long snmp_get_next_msgid (void)



long snmp_get_next_sessid (void)



long snmp_get_next_transid (void)



void snmp_perror (const char *prog_string)



void snmp_set_detail (const char *detail_string)



const char * snmp_api_errstring (int snmp_errnumber)



void snmp_error (netsnmp_session *psess, int *p_errno, int *p_snmp_errno, char **p_str)



void snmp_sess_error (void *sessp, int *p_errno, int *p_snmp_errno, char **p_str)



void netsnmp_sess_log_error (int priority, const char *prog_string, netsnmp_session *ss)



void snmp_sess_perror (const char *prog_string, netsnmp_session *ss)



void snmp_sess_init (netsnmp_session *session)



void init_snmp (const char *type)


Calls the functions to do config file loading and mib module parsing in the correct order.


void snmp_store (const char *type)



void snmp_shutdown (const char *type)


Shuts down the application, saving any needed persistent storage, and appropriate clean up.


netsnmp_session * snmp_open (netsnmp_session *session)



netsnmp_session * snmp_open_ex (netsnmp_session *session, int(*fpre_parse)(netsnmp_session *, netsnmp_transport *, void *, int), int(*fparse)(netsnmp_session *, netsnmp_pdu *, u_char *, size_t), int(*fpost_parse)(netsnmp_session *, netsnmp_pdu *, int), int(*fbuild)(netsnmp_session *, netsnmp_pdu *, u_char *, size_t *), int(*frbuild)(netsnmp_session *, netsnmp_pdu *, u_char **, size_t *, size_t *), int(*fcheck)(u_char *, size_t))



int snmpv3_engineID_probe (struct session_list *slp, netsnmp_session *in_session)


probe for peer engineID


netsnmp_session * snmp_add (netsnmp_session *in_session, netsnmp_transport *transport, int(*fpre_parse)(netsnmp_session *, netsnmp_transport *, void *, int), int(*fpost_parse)(netsnmp_session *, netsnmp_pdu *, int))



netsnmp_session * snmp_add_full (netsnmp_session *in_session, netsnmp_transport *transport, int(*fpre_parse)(netsnmp_session *, netsnmp_transport *, void *, int), int(*fparse)(netsnmp_session *, netsnmp_pdu *, u_char *, size_t), int(*fpost_parse)(netsnmp_session *, netsnmp_pdu *, int), int(*fbuild)(netsnmp_session *, netsnmp_pdu *, u_char *, size_t *), int(*frbuild)(netsnmp_session *, netsnmp_pdu *, u_char **, size_t *, size_t *), int(*fcheck)(u_char *, size_t), netsnmp_pdu *(*fcreate_pdu)(netsnmp_transport *, void *, size_t))



void * snmp_sess_add_ex (netsnmp_session *in_session, netsnmp_transport *transport, int(*fpre_parse)(netsnmp_session *, netsnmp_transport *, void *, int), int(*fparse)(netsnmp_session *, netsnmp_pdu *, u_char *, size_t), int(*fpost_parse)(netsnmp_session *, netsnmp_pdu *, int), int(*fbuild)(netsnmp_session *, netsnmp_pdu *, u_char *, size_t *), int(*frbuild)(netsnmp_session *, netsnmp_pdu *, u_char **, size_t *, size_t *), int(*fcheck)(u_char *, size_t), netsnmp_pdu *(*fcreate_pdu)(netsnmp_transport *, void *, size_t))



void * snmp_sess_add (netsnmp_session *in_session, netsnmp_transport *transport, int(*fpre_parse)(netsnmp_session *, netsnmp_transport *, void *, int), int(*fpost_parse)(netsnmp_session *, netsnmp_pdu *, int))



void * snmp_sess_open (netsnmp_session *pss)



int create_user_from_session (netsnmp_session *session)



int snmp_sess_close (void *sessp)



int snmp_close (netsnmp_session *session)



int snmp_close_sessions (void)



int snmpv3_packet_build (netsnmp_session *session, netsnmp_pdu *pdu, u_char *packet, size_t *out_length, u_char *pdu_data, size_t pdu_data_len)



u_char * snmp_pdu_build (netsnmp_pdu *pdu, u_char *cp, size_t *out_length)



int snmpv3_parse (netsnmp_pdu *pdu, u_char *data, size_t *length, u_char **after_header, netsnmp_session *sess)



int snmpv3_make_report (netsnmp_pdu *pdu, int error)



int snmpv3_get_report_type (netsnmp_pdu *pdu)



int snmp_pdu_parse (netsnmp_pdu *pdu, u_char *data, size_t *length)



u_char * snmpv3_scopedPDU_parse (netsnmp_pdu *pdu, u_char *cp, size_t *length)



int snmp_send (netsnmp_session *session, netsnmp_pdu *pdu)



int snmp_sess_send (void *sessp, netsnmp_pdu *pdu)



int snmp_async_send (netsnmp_session *session, netsnmp_pdu *pdu, snmp_callback callback, void *cb_data)



int snmp_sess_async_send (void *sessp, netsnmp_pdu *pdu, snmp_callback callback, void *cb_data)



void snmp_free_var (netsnmp_variable_list *var)



void snmp_free_varbind (netsnmp_variable_list *var)



void snmp_free_pdu (netsnmp_pdu *pdu)



netsnmp_pdu * snmp_create_sess_pdu (netsnmp_transport *transport, void *opaque, size_t olength)



void snmp_read (fd_set *fdset)



int _sess_read (void *sessp, fd_set *fdset)



int snmp_sess_read (void *sessp, fd_set *fdset)



int snmp_select_info (int *numfds, fd_set *fdset, struct timeval *timeout, int *block)



int snmp_sess_select_info (void *sessp, int *numfds, fd_set *fdset, struct timeval *timeout, int *block)



void snmp_timeout (void)



void snmp_sess_timeout (void *sessp)



int snmp_oid_ncompare (const oid *in_name1, size_t len1, const oid *in_name2, size_t len2, size_t max_len)



int snmp_oid_compare (const oid *in_name1, size_t len1, const oid *in_name2, size_t len2)


lexicographical compare two object identifiers.


int netsnmp_oid_compare_ll (const oid *in_name1, size_t len1, const oid *in_name2, size_t len2, size_t *offpt)


lexicographical compare two object identifiers and return the point where they differ


int snmp_oidtree_compare (const oid *in_name1, size_t len1, const oid *in_name2, size_t len2)


Compares 2 OIDs to determine if they are equal up until the shortest length.


int snmp_oidsubtree_compare (const oid *in_name1, size_t len1, const oid *in_name2, size_t len2)



int netsnmp_oid_equals (const oid *in_name1, size_t len1, const oid *in_name2, size_t len2)


Compares 2 OIDs to determine if they are exactly equal.


int netsnmp_oid_is_subtree (const oid *in_name1, size_t len1, const oid *in_name2, size_t len2)


Identical to netsnmp_oid_equals, except only the length up to len1 is compared.


int netsnmp_oid_find_prefix (const oid *in_name1, size_t len1, const oid *in_name2, size_t len2)


Given two OIDs, determine the common prefix to them both.


netsnmp_variable_list * snmp_pdu_add_variable (netsnmp_pdu *pdu, const oid *name, size_t name_length, u_char type, const u_char *value, size_t len)



netsnmp_variable_list * snmp_varlist_add_variable (netsnmp_variable_list **varlist, const oid *name, size_t name_length, u_char type, const u_char *value, size_t len)



int snmp_add_var (netsnmp_pdu *pdu, const oid *name, size_t name_length, char type, const char *value)



void * snmp_sess_pointer (netsnmp_session *session)



netsnmp_session * snmp_sess_session (void *sessp)



netsnmp_transport * snmp_sess_transport (void *sessp)



void snmp_sess_transport_set (void *sp, netsnmp_transport *t)



oid * snmp_duplicate_objid (const oid *objToCopy, size_t objToCopyLen)



u_int snmp_increment_statistic (int which)



u_int snmp_increment_statistic_by (int which, int count)



u_int snmp_get_statistic (int which)



void snmp_init_statistics (void)



Variables
module_init_list * initlist = NULL



module_init_list * noinitlist = NULL



netsnmp_subtree * subtrees



long long_return



u_char return_buf [258]



timeval starttime



int callback_master_num = -1



oid nullOid [] = { 0, 0 }



int nullOidLen = sizeof(nullOid)



session_list * Sessions = NULL



int snmp_errno = 0</code></pre>
<h2>Define Documentation</h2>
<h3>#define timercmp(tvp, uvp, cmp)</h3>
<p><code>Value:</code> </p>
<pre>/* CSTYLED */ ((tvp)-&gt;tv_sec cmp (uvp)-&gt;tv_sec || ((tvp)-&gt;tv_sec == (uvp)-&gt;tv_sec &amp;&amp; /* CSTYLED */ (tvp)-&gt;tv_usec cmp (uvp)-&gt;tv_usec))</pre>
<p>Definition at line 148 of file snmp_api.c. </p>
<p> Referenced by netsnmp_addrcache_add(), and snmp_sess_timeout().</p>
<h2>Function Documentation</h2>
<h3>int _sess_read (void * sessp, fd_set * fdset)</h3>
<p>Definition at line 5390 of file snmp_api.c. </p>
<p> References asn_check_packet(), snmp_session::callback, snmp_session::callback_magic, snmp_internal_session::check_packet, netsnmp_transport_s::f_accept, netsnmp_transport_s::f_close, netsnmp_transport_s::f_recv, FD_ISSET, netsnmp_transport_s::flags, snmp_internal_session::hook_build, snmp_internal_session::hook_create_pdu, snmp_internal_session::hook_parse, snmp_internal_session::hook_post, snmp_internal_session::hook_pre, snmp_internal_session::hook_realloc_build, session_list::internal, MAX_PACKET_LENGTH, MAXIMUM_PACKET_SIZE, session_list::next, NULL, snmp_internal_session::packet, snmp_internal_session::packet_len, snmp_internal_session::packet_size, snmp_session::s_errno, snmp_session::s_snmp_errno, session_list::session, Sessions, SNMP_FREE, snmp_log(), snmp_sess_add_ex(), snmp_set_detail(), netsnmp_transport_s::sock, strerror(), and session_list::transport. </p>
<p> Referenced by snmp_sess_read().</p>
<h3>int init_agent (const char * app)</h3>
<p>Initialize the agent. </p>
<p> Calls into init_agent_read_config to set tha app&#8217;s configuration file in the appropriate default storage space, NETSNMP_DS_LIB_APPTYPE. Need to call init_agent before calling init_snmp. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>app</i> the configuration file to be read in, gets stored in default storage</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>Returns non-zero on failure and zero on success.</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>init_snmp</code></dl>
<p> Definition at line 270 of file snmp_vars.c. </p>
<p> References _init_agent_callback_transport, init_traps(), netsnmp_ds_get_boolean(), netsnmp_ds_set_boolean(), netsnmp_init_helpers(), NULL, setup_tree(), snmp_log(), and starttime.</p>
<h3>void init_snmp (const char * type)</h3>
<p>Calls the functions to do config file loading and mib module parsing in the correct order. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>type</i> label for the config file &#8216;type&#8217;</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>void</dl>
<p> <code>See also:</code></p>
<dl>
<dd><code>init_agent</code></dl>
<p> Definition at line 766 of file snmp_api.c. </p>
<p> References init_callbacks(), init_snmp_alarm(), init_snmp_logging(), netsnmp_ds_get_string(), netsnmp_ds_set_string(), netsnmp_init_mib(), read_configs(), read_premib_configs(), register_mib_handlers(), and snmp_init_statistics().</p>
<h3>int netsnmp_oid_compare_ll (const oid * in_name1, size_t len1, const oid * in_name2, size_t len2, size_t * offpt)</h3>
<p>lexicographical compare two object identifiers and return the point where they differ </p>
<p> Caution: this method is called often by command responder applications (ie, agent). </p>
<p> <code>Returns:</code></p>
<dl>
<dd>-1 if name1 &lt; name2, 0 if name1 = name2, 1 if name1 &gt; name2 and offpt = len where name1 != name2</dl>
<p> Definition at line 6328 of file snmp_api.c. </p>
<p> Referenced by netsnmp_subtree_change_next(), netsnmp_subtree_change_prev(), and netsnmp_subtree_find_prev().</p>
<h3>int netsnmp_oid_equals (const oid * in_name1, size_t len1, const oid * in_name2, size_t len2)</h3>
<p>Compares 2 OIDs to determine if they are exactly equal. </p>
<p> This should be faster than doing a snmp_oid_compare for different length OIDs, since the length is checked first and if != returns immediately. Might be very slighly faster if lengths are ==. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>in_name1</i> A pointer to the first oid.<br />
 <i>len1</i> length of the first OID (in segments, not bytes)<br />
 <i>in_name2</i> A pointer to the second oid.<br />
 <i>len2</i> length of the second OID (in segments, not bytes)</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 if they are equal, 1 if they are not.</dl>
<p> Definition at line 6409 of file snmp_api.c. </p>
<p> Referenced by netsnmp_cache_find_by_oid(), netsnmp_subtree_free(), netsnmp_subtree_load(), netsnmp_unregister_mib_table_row(), and unregister_mib_context().</p>
<h3>int netsnmp_oid_find_prefix (const oid * in_name1, size_t len1, const oid * in_name2, size_t len2)</h3>
<p>Given two OIDs, determine the common prefix to them both. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>in_name1</i> A pointer to the first oid.<br />
 <i>len1</i> Length of the first oid.<br />
 <i>in_name2</i> A pointer to the second oid.<br />
 <i>len2</i> Length of the second oid.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>length of largest common index of commonality. 1 = first, 0 if none * or -1 on error.</dl>
<p> Definition at line 6465 of file snmp_api.c. </p>
<p> References SNMP_MIN. </p>
<p> Referenced by netsnmp_add_varbind_to_cache().</p>
<h3>int netsnmp_oid_is_subtree (const oid * in_name1, size_t len1, const oid * in_name2, size_t len2)</h3>
<p>Identical to netsnmp_oid_equals, except only the length up to len1 is compared. </p>
<p> Functionally, this determines if in_name2 is equal or a subtree of in_name1 </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>in_name1</i> A pointer to the first oid.<br />
 <i>len1</i> length of the first OID (in segments, not bytes)<br />
 <i>in_name2</i> A pointer to the second oid.<br />
 <i>len2</i> length of the second OID (in segments, not bytes)</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 if one is a common prefix of the other.</dl>
<p> Definition at line 6445 of file snmp_api.c.</p>
<h3>int snmp_oid_compare (const oid * in_name1, size_t len1, const oid * in_name2, size_t len2)</h3>
<p>lexicographical compare two object identifiers. </p>
<p> Caution: this method is called often by command responder applications (ie, agent). </p>
<p> <code>Returns:</code></p>
<dl>
<dd>-1 if name1 &lt; name2, 0 if name1 = name2, 1 if name1 &gt; name2</dl>
<p> Definition at line 6279 of file snmp_api.c. </p>
<p> Referenced by check_getnext_results(), convert_v2pdu_to_v1(), find_varbind_in_list(), lookup_cache_find(), netsnmp_bulk_to_next_fix_requests(), netsnmp_check_getnext_reply(), netsnmp_container_table_row_insert(), netsnmp_insert_iterator_context(), netsnmp_insert_table_row(), netsnmp_instance_helper_handler(), netsnmp_iterator_row_get_byoid(), netsnmp_iterator_row_next_byoid(), netsnmp_scalar_group_helper_handler(), netsnmp_scalar_helper_handler(), netsnmp_send_traps(), netsnmp_stash_to_next_helper(), netsnmp_subtree_compare(), netsnmp_subtree_find(), netsnmp_subtree_find_next(), netsnmp_subtree_find_prev(), netsnmp_subtree_load(), netsnmp_subtree_split(), netsnmp_table_data_add_row(), netsnmp_table_data_get_from_oid(), netsnmp_table_data_helper_handler(), netsnmp_table_data_row_next_byoid(), netsnmp_tdata_compare_oid(), netsnmp_watched_spinlock_handler(), netsnmp_watched_timestamp_handler(), netsnmp_watcher_helper_handler(), snmp_oidsubtree_compare(), snmp_oidtree_compare(), and table_helper_handler().</p>
<h3>int snmp_oidtree_compare (const oid * in_name1, size_t len1, const oid * in_name2, size_t len2)</h3>
<p>Compares 2 OIDs to determine if they are equal up until the shortest length. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>in_name1</i> A pointer to the first oid.<br />
 <i>len1</i> length of the first OID (in segments, not bytes)<br />
 <i>in_name2</i> A pointer to the second oid.<br />
 <i>len2</i> length of the second OID (in segments, not bytes)</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 if they are equal, 1 if in_name1 is &gt; in_name2, or -1 if &lt;.</dl>
<p> Definition at line 6381 of file snmp_api.c. </p>
<p> References snmp_oid_compare(). </p>
<p> Referenced by netsnmp_query_walk(), and netsnmp_tdata_compare_subtree_oid().</p>
<h3>void snmp_shutdown (const char * type)</h3>
<p>Shuts down the application, saving any needed persistent storage, and appropriate clean up. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>type</i> Label for the config file &#8216;type&#8217; used</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>void</dl>
<p> Definition at line 834 of file snmp_api.c. </p>
<p> References clear_callback(), netsnmp_ds_shutdown(), NULL, shutdown_mib(), shutdown_snmp_logging(), snmp_alarm_unregister_all(), snmp_call_callbacks(), snmp_close_sessions(), snmp_store(), and unregister_all_config_handlers().</p>
<h3>int snmpv3_engineID_probe (struct <code>session_list</code> * slp, <code>netsnmp_session</code> * in_session)</h3>
<p>probe for peer engineID </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>slp</i> session list pointer.<br />
 <i>in_session</i> session for errors</dl>
<p> <code>Note:</code></p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>called by _sess_open(), <code>snmp_sess_add_ex()</code></p>
<dt>*</p>
<dd>in_session is the user supplied session provided to those functions.</p>
<dt>*</p>
<dd>the first session in slp should the internal allocated copy of in_session</dl>
</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 : error </p>
<p> 1 : ok</dl>
<p> Definition at line 1254 of file snmp_api.c. </p>
<p> References create_user_from_session(), snmp_session::engineBoots, snmp_session::engineTime, snmp_session::flags, NULL, snmp_session::s_snmp_errno, snmp_session::securityEngineID, snmp_session::securityEngineIDLen, session_list::session, snmp_api_errstring(), snmp_errstring(), snmp_sess_synch_response(), TRUE, and snmp_session::version. </p>
<p> Referenced by snmp_sess_add_ex().</p>
