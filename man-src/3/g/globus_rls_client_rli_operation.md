---
title: "globus_rls_client_rli_operation(3)"
name: "globus_rls_client_rli_operation"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rls_client_rli_operation/"
description: "RLI Operations –"
---

<h2 class="name">NAME</h2>
<p> RLI Operations &#8211; </p>
<p> Functions to view and update data managed by a RLI server.</p>
<h3>Data Structures</h3>
<p> struct <code>globus_rls_sender_info_t</code><br />
 <i>Information about server sending updates to an rli, returned by </i><code>globus_rls_client_rli_sender_list()</code>.</p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_rls_client_rli_exists</code> (<code>globus_rls_handle_t</code> *h, char *key, <code>globus_rls_obj_type_t</code> objtype) </p>
<p> globus_result_t <code>globus_rls_client_rli_exists_bulk</code> (<code>globus_rls_handle_t</code> *h, globus_list_t *keylist, <code>globus_rls_obj_type_t</code> objtype, globus_list_t **str2bulk_list) </p>
<p> globus_result_t <code>globus_rls_client_rli_get_lrc</code> (<code>globus_rls_handle_t</code> *h, char *lfn, int *offset, int reslimit, globus_list_t **str2_list) </p>
<p> globus_result_t <code>globus_rls_client_rli_get_lrc_bulk</code> (<code>globus_rls_handle_t</code> *h, globus_list_t *lfnlist, globus_list_t **str2bulk_list) </p>
<p> globus_result_t <code>globus_rls_client_rli_get_lrc_wc</code> (<code>globus_rls_handle_t</code> *h, char *lfn_pattern, <code>globus_rls_pattern_t</code> type, int *offset, int reslimit, globus_list_t **str2_list) </p>
<p> globus_result_t <code>globus_rls_client_rli_sender_list</code> (<code>globus_rls_handle_t</code> *h, globus_list_t **senderinfo_list) </p>
<p> globus_result_t <code>globus_rls_client_rli_lrc_list</code> (<code>globus_rls_handle_t</code> *h, globus_list_t **lrcinfo_list) </p>
<p> globus_result_t <code>globus_rls_client_rli_mapping_exists</code> (<code>globus_rls_handle_t</code> *h, char *lfn, char *lrc) </p>
<p> globus_result_t <code>globus_rls_client_rli_rli_add</code> (<code>globus_rls_handle_t</code> *h, char *rli_url, char *pattern) </p>
<p> globus_result_t <code>globus_rls_client_rli_rli_delete</code> (<code>globus_rls_handle_t</code> *h, char *rli_url, char *pattern) </p>
<p> globus_result_t <code>globus_rls_client_rli_rli_get_part</code> (<code>globus_rls_handle_t</code> *h, char *rli_url, char *pattern, globus_list_t **str2_list) </p>
<p> globus_result_t <code>globus_rls_client_rli_rli_list</code> (<code>globus_rls_handle_t</code> *h, globus_list_t **rliinfo_list) </p>
<h2>Detailed Description</h2>
<p> Functions to view and update data managed by a RLI server.</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_rls_client_rli_exists (<code>globus_rls_handle_t</code> * h, char * key, <code>globus_rls_obj_type_t</code> objtype)</h3>
<p> Check if an object exists in the RLI database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>key</i> LFN or LRC that identifies object.<br />
 <i>objtype</i> Type of object <i>key</i> refers to (<code>globus_rls_obj_rli_lfn</code> or <code>globus_rls_obj_rli_lrc</code>).</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Object exists.</dl>
<h3>globus_result_t globus_rls_client_rli_exists_bulk (<code>globus_rls_handle_t</code> * h, globus_list_t * keylist, <code>globus_rls_obj_type_t</code> objtype, globus_list_t ** str2bulk_list)</h3>
<p> Bulk check if objects exist in the RLI database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>keylist</i> LFNs or LRCs that identify objects.<br />
 <i>objtype</i> Type of object <i>key</i> refers to (<code>globus_rls_obj_rli_lfn</code> or <code>globus_rls_obj_rli_lrc</code>).<br />
 <i>str2bulk_list</i> Results of existence check. Each list datum will be a <code>globus_rls_string2_bulk_t</code> structure. <code>str2.s1</code> will be the LFN or LRC, and <code>str2.s2</code> empty, and <code>rc</code> will be the result code indicating existence.</dl>
<h3>globus_result_t globus_rls_client_rli_get_lrc (<code>globus_rls_handle_t</code> * h, char * lfn, int * offset, int reslimit, globus_list_t ** str2_list)</h3>
<p> Return LRCs mapped to LFN in the RLI database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>lfn</i> LFN whose list of LRCs is desired.<br />
 <i>offset</i> Offset into result list. Used in conjunction with <i>reslimit</i> to retrieve results a few at a time. Use 0 to begin with first result.<br />
 <i>reslimit</i> Maximum number of results to return. Used in conjunction with <i>offset</i> to retrieve results a few at a time. Use 0 to retrieve all results.<br />
 <i>str2_list</i> List of LRCs that <i>lfn</i> maps to. Each list datum will be a <code>globus_rls_string2_t</code> structure. <code>s1</code> will be the LFN, and <code>s2</code> the LRC it maps to. <i>str2_list</i> should be freed with <code>globus_rls_client_free_list()</code>.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> List of LRCs that map to <i>lfn</i> in <i>str2_list</i>. See <code>Query Results</code>.</dl>
<h3>globus_result_t globus_rls_client_rli_get_lrc_bulk (<code>globus_rls_handle_t</code> * h, globus_list_t * lfnlist, globus_list_t ** str2bulk_list)</h3>
<p> Bulk return LRCs mapped to LFN in the RLI database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>lfnlist</i> LFNs to search for.<br />
 <i>str2bulk_list</i> Results of queries. Each list datum will be a <code>globus_rls_string2_bulk_t</code> structure. <code>str2.s1</code> will be the LFN, and <code>str2.s2</code> the LRC it maps to, and <code>rc</code> will be the result code from the query.</dl>
<h3>globus_result_t globus_rls_client_rli_get_lrc_wc (<code>globus_rls_handle_t</code> * h, char * lfn_pattern, <code>globus_rls_pattern_t</code> type, int * offset, int reslimit, globus_list_t ** str2_list)</h3>
<p> Return LRCs mapped to wildcarded LFN in the RLI database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>lfn_pattern</i> LFN pattern to search for.<br />
 <i>type</i> Identifies wildcard characters used in <i>lfn_pattern</i>. Wildcard chars can be Unix file globbing chars (* matches 0 or more characters, ? matches any single character) or SQL &#8216;like&#8217; wildcard characters (% matches 0 or more charactes, _ matches any single character).<br />
 <i>offset</i> Offset into result list. Used in conjunction with <i>reslimit</i> to retrieve results a few at a time. Use 0 to begin with first result.<br />
 <i>reslimit</i> Maximum number of results to return. Used in conjunction with <i>offset</i> to retrieve results a few at a time. Use 0 to retrieve all results.<br />
 <i>str2_list</i> List of LRCs that map to <i>lfn_pattern</i>. Each list datum will be a <code>globus_rls_string2_t</code>. <code>s1</code> will be the LFN, and <code>s2</code> the LRC it maps to. <i>str2_list</i> should be freed with <code>globus_rls_client_free_list()</code>.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> List of LRCs that map to <i>lfn_pattern</i> in <i>str2_list</i>. See <code>Query Results</code>.</dl>
<h3>globus_result_t globus_rls_client_rli_sender_list (<code>globus_rls_handle_t</code> * h, globus_list_t ** senderinfo_list)</h3>
<p> Get list of servers updating this RLI server. Similar to globus_rls_client_rli_get_part() except no partition information is returned. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>senderinfo_list</i> Datums in senderinfo_list will be of type <code>globus_rls_sender_info_t</code>. <i>senderinfo_list</i> should be freed with <code>globus_rls_client_free_list()</code>.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> List of LRCs updating RLI added to <i>senderinfo_list</i>.</dl>
<h3>globus_result_t globus_rls_client_rli_lrc_list (<code>globus_rls_handle_t</code> * h, globus_list_t ** lrcinfo_list)</h3>
<p> Deprecated, use <code>globus_rls_client_rli_sender_list()</code>. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>lrcinfo_list</i> Datums in lrcinfo_list will be of type globus_rls_lrc_info_t. <i>lrcinfo_list</i> should be freed with <code>globus_rls_client_free_list()</code>.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> List of LRCs updating RLI added to <i>lrcinfo_list</i>.</dl>
<h3>globus_result_t globus_rls_client_rli_mapping_exists (<code>globus_rls_handle_t</code> * h, char * lfn, char * lrc)</h3>
<p> Check if a mapping exists in the RLI database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>lfn</i> LFN of mapping.<br />
 <i>lrc</i> LRC of mapping.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Mapping exists.</dl>
<h3>globus_result_t globus_rls_client_rli_rli_add (<code>globus_rls_handle_t</code> * h, char * rli_url, char * pattern)</h3>
<p> RLI servers send information about LFNs in their database to the the list of RLI servers in the database, added with the following function. Updates may be partitioned amongst multiple RLIs by specifying one or more patterns for an RLI. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>rli_url</i> URL of RLI server that LRC should send updates to.<br />
 <i>pattern</i> If not NULL used to filter which LFNs are sent to <i>rli_url</i>. Standard Unix wildcard characters (*, ?) may be used to do wildcard matches.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> RLI (with pattern if not NULL) added to RLI database.</dl>
<h3>globus_result_t globus_rls_client_rli_rli_delete (<code>globus_rls_handle_t</code> * h, char * rli_url, char * pattern)</h3>
<p> Delete an entry from the RLI rli/partition tables. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>rli_url</i> URL of RLI server to remove from RLI partition table.<br />
 <i>pattern</i> If not NULL then only the specific <i>rli_url/pattern</i> is removed, else all partition information for <i>rli_url</i> is removed.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> RLI and pattern (if specified) removed from LRC partition table.</dl>
<h3>globus_result_t globus_rls_client_rli_rli_get_part (<code>globus_rls_handle_t</code> * h, char * rli_url, char * pattern, globus_list_t ** str2_list)</h3>
<p> Get RLI update partitions from RLI server. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>rli_url</i> If not NULL identifies RLI that partition data will be retrieved for. If NULL then all RLIs are retrieved.<br />
 <i>pattern</i> If not NULL returns only partitions with matching patterns, otherwise all patterns are retrieved.<br />
 <i>str2_list</i> Results added to list. Datums in <i>str2_list</i> are of type <code>globus_rls_string2_t</code> structure. <code>s1</code> will be the rli url, <code>s2</code> an empty string or the pattern used to partition updates. See <code>Query Results</code>.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Partition data retrieved from server, written to <i>str2_list</i>.</dl>
<h3>globus_result_t globus_rls_client_rli_rli_list (<code>globus_rls_handle_t</code> * h, globus_list_t ** rliinfo_list)</h3>
<p> Return URLs of RLIs that RLI sends updates to. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>rliinfo_list</i> List of RLIs updated by this RLI returned in this list. Each list datum is of type <code>globus_rls_rli_info_t</code>. <i>rliinfo_list</i> should be freed with <code>globus_rls_client_free_list()</code> when no longer needed.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> List of RLIs updated by this LRC returned in <i>rliinfo_list</i>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus rls client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAS">Author</a></p>
<dd></dl>
