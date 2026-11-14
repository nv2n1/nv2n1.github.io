---
title: "globus_rls_client_lrc_operation(3)"
name: "globus_rls_client_lrc_operation"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_rls_client_lrc_operation/"
description: "LRC Operations –"
---

<h2 class="name">NAME</h2>
<p> LRC Operations &#8211; </p>
<p> Functions to view and update data managed by a LRC server.</p>
<h3>Data Structures</h3>
<p> struct <code>globus_rls_rli_info_t</code><br />
 <i>Information about RLI server, returned by </i><code>globus_rls_client_lrc_rli_info()</code> and <code>globus_rls_client_lrc_rli_list()</code>.</p>
<h3>Defines</h3>
<p> #define <code>FRLI_BLOOMFILTER</code> 0x1 </p>
<p> #define <code>MAXURL</code> 256 </p>
<h3>Functions</h3>
<p> globus_result_t <code>globus_rls_client_lrc_attr_add</code> (<code>globus_rls_handle_t</code> *h, char *key, <code>globus_rls_attribute_t</code> *attr) </p>
<p> globus_result_t <code>globus_rls_client_lrc_attr_add_bulk</code> (<code>globus_rls_handle_t</code> *h, globus_list_t *attr_obj_list, globus_list_t **str2bulk_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_attr_create</code> (<code>globus_rls_handle_t</code> *h, char *name, <code>globus_rls_obj_type_t</code> objtype, <code>globus_rls_attr_type_t</code> type) </p>
<p> globus_result_t <code>globus_rls_client_lrc_attr_delete</code> (<code>globus_rls_handle_t</code> *h, char *name, <code>globus_rls_obj_type_t</code> objtype, globus_bool_t clearvalues) </p>
<p> globus_result_t <code>globus_rls_client_lrc_attr_get</code> (<code>globus_rls_handle_t</code> *h, char *name, <code>globus_rls_obj_type_t</code> objtype, globus_list_t **attr_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_attr_modify</code> (<code>globus_rls_handle_t</code> *h, char *key, <code>globus_rls_attribute_t</code> *attr) </p>
<p> globus_result_t <code>globus_rls_client_lrc_attr_remove</code> (<code>globus_rls_handle_t</code> *h, char *key, <code>globus_rls_attribute_t</code> *attr) </p>
<p> globus_result_t <code>globus_rls_client_lrc_attr_remove_bulk</code> (<code>globus_rls_handle_t</code> *h, globus_list_t *attr_obj_list, globus_list_t **str2bulk_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_attr_search</code> (<code>globus_rls_handle_t</code> *h, char *name, <code>globus_rls_obj_type_t</code> objtype, <code>globus_rls_attr_op_t</code> op, <code>globus_rls_attribute_t</code> *operand1, <code>globus_rls_attribute_t</code> *operand2, int *offset, int reslimit, globus_list_t **attr_obj_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_attr_value_get</code> (<code>globus_rls_handle_t</code> *h, char *key, char *name, <code>globus_rls_obj_type_t</code> objtype, globus_list_t **attr_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_attr_value_get_bulk</code> (<code>globus_rls_handle_t</code> *h, globus_list_t *keylist, char *name, <code>globus_rls_obj_type_t</code> objtype, globus_list_t **attr_obj_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_add</code> (<code>globus_rls_handle_t</code> *h, char *lfn, char *pfn) </p>
<p> globus_result_t <code>globus_rls_client_lrc_add_bulk</code> (<code>globus_rls_handle_t</code> *h, globus_list_t *str2_list, globus_list_t **str2bulk_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_clear</code> (<code>globus_rls_handle_t</code> *h) </p>
<p> globus_result_t <code>globus_rls_client_lrc_create</code> (<code>globus_rls_handle_t</code> *h, char *lfn, char *pfn) </p>
<p> globus_result_t <code>globus_rls_client_lrc_create_bulk</code> (<code>globus_rls_handle_t</code> *h, globus_list_t *str2_list, globus_list_t **str2bulk_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_delete</code> (<code>globus_rls_handle_t</code> *h, char *lfn, char *pfn) </p>
<p> globus_result_t <code>globus_rls_client_lrc_delete_bulk</code> (<code>globus_rls_handle_t</code> *h, globus_list_t *str2_list, globus_list_t **str2bulk_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_exists</code> (<code>globus_rls_handle_t</code> *h, char *key, <code>globus_rls_obj_type_t</code> objtype) </p>
<p> globus_result_t <code>globus_rls_client_lrc_exists_bulk</code> (<code>globus_rls_handle_t</code> *h, globus_list_t *keylist, <code>globus_rls_obj_type_t</code> objtype, globus_list_t **str2bulk_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_get_lfn</code> (<code>globus_rls_handle_t</code> *h, char *pfn, int *offset, int reslimit, globus_list_t **str2_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_get_lfn_bulk</code> (<code>globus_rls_handle_t</code> *h, globus_list_t *pfnlist, globus_list_t **str2bulk_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_get_lfn_wc</code> (<code>globus_rls_handle_t</code> *h, char *pfn_pattern, <code>globus_rls_pattern_t</code> type, int *offset, int reslimit, globus_list_t **str2_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_get_pfn</code> (<code>globus_rls_handle_t</code> *h, char *lfn, int *offset, int reslimit, globus_list_t **str2_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_get_pfn_bulk</code> (<code>globus_rls_handle_t</code> *h, globus_list_t *lfnlist, globus_list_t **str2bulk_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_get_pfn_wc</code> (<code>globus_rls_handle_t</code> *h, char *lfn_pattern, <code>globus_rls_pattern_t</code> type, int *offset, int reslimit, globus_list_t **str2_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_mapping_exists</code> (<code>globus_rls_handle_t</code> *h, char *lfn, char *pfn) </p>
<p> globus_result_t <code>globus_rls_client_lrc_renamelfn</code> (<code>globus_rls_handle_t</code> *h, char *oldname, char *newname) </p>
<p> globus_result_t <code>globus_rls_client_lrc_renamelfn_bulk</code> (<code>globus_rls_handle_t</code> *h, globus_list_t *str2_list, globus_list_t **str2bulk_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_renamepfn</code> (<code>globus_rls_handle_t</code> *h, char *oldname, char *newname) </p>
<p> globus_result_t <code>globus_rls_client_lrc_renamepfn_bulk</code> (<code>globus_rls_handle_t</code> *h, globus_list_t *str2_list, globus_list_t **str2bulk_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_rli_add</code> (<code>globus_rls_handle_t</code> *h, char *rli_url, int flags, char *pattern) </p>
<p> globus_result_t <code>globus_rls_client_lrc_rli_delete</code> (<code>globus_rls_handle_t</code> *h, char *rli_url, char *pattern) </p>
<p> globus_result_t <code>globus_rls_client_lrc_rli_get_part</code> (<code>globus_rls_handle_t</code> *h, char *rli_url, char *pattern, globus_list_t **str2_list) </p>
<p> globus_result_t <code>globus_rls_client_lrc_rli_info</code> (<code>globus_rls_handle_t</code> *h, char *rli_url, <code>globus_rls_rli_info_t</code> *info) </p>
<p> globus_result_t <code>globus_rls_client_lrc_rli_list</code> (<code>globus_rls_handle_t</code> *h, globus_list_t **rliinfo_list) </p>
<h2>Detailed Description</h2>
<p> Functions to view and update data managed by a LRC server.</p>
<h2>Define Documentation</h2>
<h3>#define FRLI_BLOOMFILTER 0x1</h3>
<p> Update RLI using bloom filters (see <code>globus_rls_client_lrc_rli_add()</code>).</p>
<h3>#define MAXURL 256</h3>
<p> Maximum length of URL string.</p>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_rls_client_lrc_attr_add (<code>globus_rls_handle_t</code> * h, char * key, <code>globus_rls_attribute_t</code> * attr)</h3>
<p> Add an attribute to an object in the LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>key</i> Logical or Physical File Name (LFN or PFN) that identifies object attribute should be added to.<br />
 <i>attr</i> Attribute to be added to object. <code>name, objtype, type and val </code> should be set in <i>attr</i>.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Attribute successfully associated with object.</dl>
<h3>globus_result_t globus_rls_client_lrc_attr_add_bulk (<code>globus_rls_handle_t</code> * h, globus_list_t * attr_obj_list, globus_list_t ** str2bulk_list)</h3>
<p> Bulk add attributes to objects in the LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>attr_obj_list</i> List of object names (LFN or PFN) and attributes to be added. Each list datum should be of type <code>globus_rls_attribute_object_t</code>.<br />
 <i>str2bulk_list</i> List of failed updates. Each list datum is a <code>globus_rls_string2_bulk_t</code> structure. <code>str2.s1</code> will be the oject name, <code>str2.s2</code> the attribute name, and <code>rc</code> will be the result code from the failed update. Only failed updates will be returned.</dl>
<h3>globus_result_t globus_rls_client_lrc_attr_create (<code>globus_rls_handle_t</code> * h, char * name, <code>globus_rls_obj_type_t</code> objtype, <code>globus_rls_attr_type_t</code> type)</h3>
<p> Define new attribute in LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an LRC server.<br />
 <i>name</i> Name of attribute.<br />
 <i>objtype</i> Object (LFN or PFN) type that attribute applies to.<br />
 <i>type</i> Type of attribute value.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Attribute successfully created.</dl>
<h3>globus_result_t globus_rls_client_lrc_attr_delete (<code>globus_rls_handle_t</code> * h, char * name, <code>globus_rls_obj_type_t</code> objtype, globus_bool_t clearvalues)</h3>
<p> Undefine attribute in LRC database, previously created with <code>globus_rls_client_lrc_attr_create()</code>. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an LRC server.<br />
 <i>name</i> Name of attribute.<br />
 <i>objtype</i> Object (LFN or PFN) type that attribute applies to.<br />
 <i>clearvalues</i> If GLOBUS_TRUE then any any values for this attribute are first removed from the objects they&#8217;re associated with. If GLOBUS_FALSE and any values exist then <code>GLOBUS_RLS_ATTR_EXIST</code> is returned.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Attribute successfully removed.</dl>
<h3>globus_result_t globus_rls_client_lrc_attr_get (<code>globus_rls_handle_t</code> * h, char * name, <code>globus_rls_obj_type_t</code> objtype, globus_list_t ** attr_list)</h3>
<p> Return definitions of attributes in LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>name</i> Name of attribute. If name is NULL all attributes of the specified <i>objtype</i> are returned.<br />
 <i>objtype</i> Object (LFN or PFN) type that attribute applies to.<br />
 <i>attr_list</i> Any attribute definitions found will be returned as a list of <code>globus_rls_attribute_t</code> structures.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Attribute definitions successfully retrieved. <i>attr_list</i> should be freed with <code>globus_rls_client_free_list()</code> when it is no longer needed.</dl>
<h3>globus_result_t globus_rls_client_lrc_attr_modify (<code>globus_rls_handle_t</code> * h, char * key, <code>globus_rls_attribute_t</code> * attr)</h3>
<p> Modify an attribute value. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>key</i> Name of object (LFN or PFN).<br />
 <i>attr</i> Attribute to be modified. The <code>objtype </code>, <code>name </code> and <code>type </code> fields should be set in <i>attr</i> to identify the attribute, the <code>val </code> field should be the new value.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Attribute successfully modified.</dl>
<h3>globus_result_t globus_rls_client_lrc_attr_remove (<code>globus_rls_handle_t</code> * h, char * key, <code>globus_rls_attribute_t</code> * attr)</h3>
<p> Remove an attribute from an object (LFN or PFN) in the LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>key</i> Name of object (LFN or PFN).<br />
 <i>attr</i> Attribute to be removed. The <code>objtype </code> and <code>name </code> fields should be set in <i>attr</i> to identify the attribute.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Attribute successfully removed.</dl>
<h3>globus_result_t globus_rls_client_lrc_attr_remove_bulk (<code>globus_rls_handle_t</code> * h, globus_list_t * attr_obj_list, globus_list_t ** str2bulk_list)</h3>
<p> Bulk remove attributes from objects in the LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>attr_obj_list</i> List of object names (LFN or PFN) and attributes to be removed. It is not necessary to set the attribute type or value. Each list datum should be of type <code>globus_rls_attribute_object_t</code>.<br />
 <i>str2bulk_list</i> List of failed updates. Each list datum is a <code>globus_rls_string2_bulk_t</code> structure. <code>str2.s1</code> will be the oject name, <code>str2.s2</code> the attribute name, and <code>rc</code> will be the result code from the failed update. Only failed updates will be returned.</dl>
<h3>globus_result_t globus_rls_client_lrc_attr_search (<code>globus_rls_handle_t</code> * h, char * name, <code>globus_rls_obj_type_t</code> objtype, <code>globus_rls_attr_op_t</code> op, <code>globus_rls_attribute_t</code> * operand1, <code>globus_rls_attribute_t</code> * operand2, int * offset, int reslimit, globus_list_t ** attr_obj_list)</h3>
<p> Search for objects (LFNs or PFNs) in a LRC database that have the specified attribute whose value matches a boolean expression. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>name</i> Name of attribute.<br />
 <i>objtype</i> Object (LFN or PFN) type that attribute applies to.<br />
 <i>op</i> Operator to be used in searching for values.<br />
 <i>operand1</i> First operand in boolean expression. <code>type </code> and <code>val </code> should be set in <code>globus_rls_attribute_t</code>.<br />
 <i>operand2</i> Second operand in boolean expression, only used when <i>op</i> is globus_rls_client_attr_op_btw. <code>type </code> and <code>val </code> should be set in <code>globus_rls_attribute_t</code>.<br />
 <i>offset</i> Offset into result list. Used in conjunction with <i>reslimit</i> to retrieve results a few at a time. Use 0 to begin with first result. If NULL then API will handle accumulating partial results transparently.<br />
 <i>reslimit</i> Maximum number of results to return. Used in conjunction with <i>offset</i> to retrieve results a few at a time. Use 0 to retrieve all results.<br />
 <i>attr_obj_list</i> Any objects with the specified attribute will be returned, with the attribute value, in a list of <code>globus_rls_attribute_object_t</code> structures.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Objects with specified attribute returned in <i>attr_obj_list</i>. <i>attr_obj_list</i> should be freed with <code>globus_rls_client_free_list()</code> when it is no longer needed. See <code>Query Results</code>.</dl>
<h3>globus_result_t globus_rls_client_lrc_attr_value_get (<code>globus_rls_handle_t</code> * h, char * key, char * name, <code>globus_rls_obj_type_t</code> objtype, globus_list_t ** attr_list)</h3>
<p> Return attributes in LRC database for specified object (LFN or PFN). <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>key</i> Logical or Physical File Name (LFN or PFN) that identifies object attributes should be retrieved for.<br />
 <i>name</i> Name of attribute to retrieve. If NULL all attributes for <i>key</i>, <i>objtype</i> are returned.<br />
 <i>objtype</i> Object (LFN or PFN) type that attribute applies to.<br />
 <i>attr_list</i> Any attributes found will be returned in this list of <code>globus_rls_attribute_t</code> structures.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Attributes successfully retrieved. <i>attr_list</i> should be freed with <code>globus_rls_client_free_list()</code> when it is no longer needed.</dl>
<h3>globus_result_t globus_rls_client_lrc_attr_value_get_bulk (<code>globus_rls_handle_t</code> * h, globus_list_t * keylist, char * name, <code>globus_rls_obj_type_t</code> objtype, globus_list_t ** attr_obj_list)</h3>
<p> Return attributes in LRC database for specified objects (LFN or PFN). <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>keylist</i> Logical or Physical File Names (LFNs or PFNs) that identify object attributes should be retrieved for. Each list datum should be a string containing the LFN or PFN.<br />
 <i>name</i> Name of attribute to retrieve. If NULL all attributes for <i>key</i>, <i>objtype</i> are returned.<br />
 <i>objtype</i> Object (LFN or PFN) type that attribute applies to.<br />
 <i>attr_obj_list</i> Any attributes found will be returned in this list of <code>globus_rls_attribute_object_t</code> structures.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Attributes successfully retrieved. <i>attr_obj_list</i> should be freed with <code>globus_rls_client_free_list()</code> when it is no longer needed.</dl>
<h3>globus_result_t globus_rls_client_lrc_add (<code>globus_rls_handle_t</code> * h, char * lfn, char * pfn)</h3>
<p> Add mapping to PFN to an existing LFN. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>lfn</i> LFN to add <i>pfn</i> mapping to, should already exist.<br />
 <i>pfn</i> PFN that <i>lfn</i> should map to.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> New mapping created.</dl>
<h3>globus_result_t globus_rls_client_lrc_add_bulk (<code>globus_rls_handle_t</code> * h, globus_list_t * str2_list, globus_list_t ** str2bulk_list)</h3>
<p> Bulk add LFN,PFN mappings in LRC database. LFNs must already exist. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>str2_list</i> LFN,PFN pairs to add mappings.<br />
 <i>str2bulk_list</i> List of failed updates. Each list datum is a <code>globus_rls_string2_bulk_t</code> structure. <code>str2.s1</code> will be the LFN, and <code>str2.s2</code> the PFN it maps to, and <code>rc</code> will be the result code from the failed update. Only failed updates will be returned.</dl>
<h3>globus_result_t globus_rls_client_lrc_clear (<code>globus_rls_handle_t</code> * h)</h3>
<p> Clear all mappings from LRC database. User needs both ADMIN and LRCUPDATE privileges to perform this operation. Note that if the LRC is cleared this will not be reflected in any RLI servers updated by the LRC until the next softstate update, even if immediate updates are enabled. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Mappings cleared.</dl>
<h3>globus_result_t globus_rls_client_lrc_create (<code>globus_rls_handle_t</code> * h, char * lfn, char * pfn)</h3>
<p> Create mapping between a LFN and PFN. LFN should not exist yet. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>lfn</i> LFN to add <i>pfn</i> mapping to, should not already exist.<br />
 <i>pfn</i> PFN that <i>lfn</i> should map to.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> New mapping created.</dl>
<h3>globus_result_t globus_rls_client_lrc_create_bulk (<code>globus_rls_handle_t</code> * h, globus_list_t * str2_list, globus_list_t ** str2bulk_list)</h3>
<p> Bulk create LFN,PFN mappings in LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>str2_list</i> LFN,PFN pairs to create mappings for.<br />
 <i>str2bulk_list</i> List of failed updates. Each list datum is a <code>globus_rls_string2_bulk_t</code> structure. <code>str2.s1</code> will be the LFN, and <code>str2.s2</code> the PFN it maps to, and <code>rc</code> will be the result code from the failed update. Only failed updates will be returned.</dl>
<h3>globus_result_t globus_rls_client_lrc_delete (<code>globus_rls_handle_t</code> * h, char * lfn, char * pfn)</h3>
<p> Delete mapping between LFN and PFN. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>lfn</i> LFN to remove mapping from.<br />
 <i>pfn</i> PFN that <i>lfn</i> maps to that is being removed.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Mapping removed.</dl>
<h3>globus_result_t globus_rls_client_lrc_delete_bulk (<code>globus_rls_handle_t</code> * h, globus_list_t * str2_list, globus_list_t ** str2bulk_list)</h3>
<p> Bulk delete LFN,PFN mappings in LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>str2_list</i> LFN,PFN pairs to add mappings.<br />
 <i>str2bulk_list</i> List of failed updates. Each list datum is a <code>globus_rls_string2_bulk_t</code> structure. <code>str2.s1</code> will be the LFN, and <code>str2.s2</code> the PFN it maps to, and <code>rc</code> will be the result code from the failed update. Only failed updates will be returned.</dl>
<h3>globus_result_t globus_rls_client_lrc_exists (<code>globus_rls_handle_t</code> * h, char * key, <code>globus_rls_obj_type_t</code> objtype)</h3>
<p> Check if an object exists in the LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>key</i> LFN or PFN that identifies object.<br />
 <i>objtype</i> Type of object <i>key</i> refers to (<code>globus_rls_obj_lrc_lfn</code> or <code>globus_rls_obj_lrc_pfn</code>).</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Object exists.</dl>
<h3>globus_result_t globus_rls_client_lrc_exists_bulk (<code>globus_rls_handle_t</code> * h, globus_list_t * keylist, <code>globus_rls_obj_type_t</code> objtype, globus_list_t ** str2bulk_list)</h3>
<p> Bulk check if objects exist in the LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>keylist</i> LFNs or PFNs that identify objects.<br />
 <i>objtype</i> Type of object <i>key</i> refers to (<code>globus_rls_obj_lrc_lfn</code> or <code>globus_rls_obj_lrc_pfn</code>).<br />
 <i>str2bulk_list</i> Results of existence check. Each list datum will be a <code>globus_rls_string2_bulk_t</code> structure. <code>str2.s1</code> will be the LFN or PFN, and <code>str2.s2</code> empty, and <code>rc</code> will be the result code indicating existence.</dl>
<h3>globus_result_t globus_rls_client_lrc_get_lfn (<code>globus_rls_handle_t</code> * h, char * pfn, int * offset, int reslimit, globus_list_t ** str2_list)</h3>
<p> Return LFNs mapped to PFN in the LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>pfn</i> PFN to search for.<br />
 <i>offset</i> Offset into result list. Used in conjunction with <i>reslimit</i> to retrieve results a few at a time. Use 0 to begin with first result. If NULL then API will handle accumulating partial results transparently.<br />
 <i>reslimit</i> Maximum number of results to return. Used in conjunction with <i>offset</i> to retrieve results a few at a time. Use 0 to retrieve all results.<br />
 <i>str2_list</i> List of LFNs that map to <i>pfn</i>. Each list datum will be a <code>globus_rls_string2_t</code> structure. <code>s1</code> will be the LFN, and <code>s2</code> the PFN it maps to.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> List of LFNs that map to <i>pfn</i> in <i>str2_list</i>. See <code>Query Results</code>.</dl>
<h3>globus_result_t globus_rls_client_lrc_get_lfn_bulk (<code>globus_rls_handle_t</code> * h, globus_list_t * pfnlist, globus_list_t ** str2bulk_list)</h3>
<p> Bulk return LFNs mapped to PFN in the LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>pfnlist</i> PFNs to search for.<br />
 <i>str2bulk_list</i> Results of queries. Each list datum will be a <code>globus_rls_string2_bulk_t</code> structure. <code>str2.s1</code> will be the LFN, and <code>str2.s2</code> the PFN it maps to, and <code>rc</code> will be the result code from the query.</dl>
<h3>globus_result_t globus_rls_client_lrc_get_lfn_wc (<code>globus_rls_handle_t</code> * h, char * pfn_pattern, <code>globus_rls_pattern_t</code> type, int * offset, int reslimit, globus_list_t ** str2_list)</h3>
<p> Return LFNs mapped to wildcarded PFN in the LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>pfn_pattern</i> PFN pattern to search for.<br />
 <i>type</i> Identifies wildcard characters used in <i>pfn_pattern</i>. Wildcard chars can be Unix file globbing chars (* matches 0 or more characters, ? matches any single character) or SQL &#8216;like&#8217; wildcard characters (% matches 0 or more charactes, _ matches any single character).<br />
 <i>offset</i> Offset into result list. Used in conjunction with <i>reslimit</i> to retrieve results a few at a time. Use 0 to begin with first result. If NULL then the API will handle accumulating partial results transparently.<br />
 <i>reslimit</i> Maximum number of results to return. Used in conjunction with <i>offset</i> to retrieve results a few at a time. Use 0 to retrieve all results.<br />
 <i>str2_list</i> List of LFNs that map to <i>pfn_pattern</i>. Each list datum will be a <code>globus_rls_string2_t</code> structure. <code>s1</code> will be the LFN, and <code>s2</code> the PFN it maps to.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> List of LFNs that map to <i>pfn_pattern</i> in <i>str2_list</i>. See <code>Query Results</code>.</dl>
<h3>globus_result_t globus_rls_client_lrc_get_pfn (<code>globus_rls_handle_t</code> * h, char * lfn, int * offset, int reslimit, globus_list_t ** str2_list)</h3>
<p> Return PFNs mapped to LFN in the LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>lfn</i> LFN to search for.<br />
 <i>offset</i> Offset into result list. Used in conjunction with <i>reslimit</i> to retrieve results a few at a time. Use 0 to begin with first result.<br />
 <i>reslimit</i> Maximum number of results to return. Used in conjunction with <i>offset</i> to retrieve results a few at a time. Use 0 to retrieve all results.<br />
 <i>str2_list</i> List of PFNs that map to <i>lfn</i>. Each list datum will be a <code>globus_rls_string2_t</code> structure. <code>s1</code> will be the LFN, and <code>s2</code> the PFN it maps to.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> List of PFNs that map to <i>lfn</i> in <i>str2_list</i>.</dl>
<h3>globus_result_t globus_rls_client_lrc_get_pfn_bulk (<code>globus_rls_handle_t</code> * h, globus_list_t * lfnlist, globus_list_t ** str2bulk_list)</h3>
<p> Bulk return PFNs mapped to LFN in the LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>lfnlist</i> LFNs to search for.<br />
 <i>str2bulk_list</i> Results of queries. Each list datum will be a <code>globus_rls_string2_bulk_t</code> structure. <code>str2.s1</code> will be the LFN, and <code>str2.s2</code> the PFN it maps to, and <code>rc</code> will be the result code from the query.</dl>
<h3>globus_result_t globus_rls_client_lrc_get_pfn_wc (<code>globus_rls_handle_t</code> * h, char * lfn_pattern, <code>globus_rls_pattern_t</code> type, int * offset, int reslimit, globus_list_t ** str2_list)</h3>
<p> Return PFNs mapped to wildcarded LFN in the LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>lfn_pattern</i> LFN pattern to search for.<br />
 <i>type</i> Identifies wildcard characters used in <i>lfn_pattern</i>. Wildcard chars can be Unix file globbing chars (* matches 0 or more characters, ? matches any single character) or SQL &#8216;like&#8217; wildcard characters (% matches 0 or more charactes, _ matches any single character).<br />
 <i>offset</i> Offset into result list. Used in conjunction with <i>reslimit</i> to retrieve results a few at a time. Use 0 to begin with first result.<br />
 <i>reslimit</i> Maximum number of results to return. Used in conjunction with <i>offset</i> to retrieve results a few at a time. Use 0 to retrieve all results.<br />
 <i>str2_list</i> List of PFNs that map to <i>lfn_pattern</i>. Each list datum will be a <code>globus_rls_string2_t</code> structure. <code>s1</code> will be the LFN, and <code>s2</code> the PFN it maps to.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> List of PFNs that map to <i>lfn_pattern</i> in <i>str2_list</i>. See <code>Query Results</code>.</dl>
<h3>globus_result_t globus_rls_client_lrc_mapping_exists (<code>globus_rls_handle_t</code> * h, char * lfn, char * pfn)</h3>
<p> Check if a mapping exists in the LRC database. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>lfn</i> LFN of mapping.<br />
 <i>pfn</i> PFN of mapping.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Object exists.</dl>
<h3>globus_result_t globus_rls_client_lrc_renamelfn (<code>globus_rls_handle_t</code> * h, char * oldname, char * newname)</h3>
<p> Rename LFN. If immediate mode is ON, the LRC will send update messages to associated RLIs. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>oldname</i> Existing LFN name, to be renamed.<br />
 <i>newname</i> New LFN name, to replace existing name.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> LFN renamed.</dl>
<h3>globus_result_t globus_rls_client_lrc_renamelfn_bulk (<code>globus_rls_handle_t</code> * h, globus_list_t * str2_list, globus_list_t ** str2bulk_list)</h3>
<p> Bulk rename LFN names in LRC database. LFNs must already exist. If immediate mode is ON, the LRC will send update messages to associated RLIs. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>str2_list</i> oldname,newname pairs such that newname replaces oldname for LFNs.<br />
 <i>str2bulk_list</i> List of failed updates. Each list datum is a <code>globus_rls_string2_bulk_t</code> structure. <code>str2.s1</code> will be the old LFN name, and <code>str2.s2</code> the new LFN name, and <code>rc</code> will be the result code from the failed update. Only failed updates will be returned.</dl>
<h3>globus_result_t globus_rls_client_lrc_renamepfn (<code>globus_rls_handle_t</code> * h, char * oldname, char * newname)</h3>
<p> Rename PFN. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>oldname</i> Exisintg PFN name, to be renamed.<br />
 <i>newname</i> New PFN name, to replace existing name.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> PFN renamed.</dl>
<h3>globus_result_t globus_rls_client_lrc_renamepfn_bulk (<code>globus_rls_handle_t</code> * h, globus_list_t * str2_list, globus_list_t ** str2bulk_list)</h3>
<p> Bulk rename PFN names in LRC database. PFNs must already exist. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>str2_list</i> oldname,newname pairs such that newname replaces oldname for PFNs.<br />
 <i>str2bulk_list</i> List of failed updates. Each list datum is a <code>globus_rls_string2_bulk_t</code> structure. <code>str2.s1</code> will be the old PFN name, and <code>str2.s2</code> the new PFN name, and <code>rc</code> will be the result code from the failed update. Only failed updates will be returned.</dl>
<h3>globus_result_t globus_rls_client_lrc_rli_add (<code>globus_rls_handle_t</code> * h, char * rli_url, int flags, char * pattern)</h3>
<p> LRC servers send information about LFNs in their database to the the list of RLI servers in the database, added with the following function. Updates may be partitioned amongst multiple RLIs by specifying one or more patterns for an RLI. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>rli_url</i> URL of RLI server that LRC should send updates to.<br />
 <i>flags</i> Should be zero or <code>FRLI_BLOOMFILTER</code>.<br />
 <i>pattern</i> If not NULL used to filter which LFNs are sent to <i>rli_url</i>. Standard Unix wildcard characters (*, ?) may be used to do wildcard matches.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> RLI (with pattern if not NULL) added to LRC database.</dl>
<h3>globus_result_t globus_rls_client_lrc_rli_delete (<code>globus_rls_handle_t</code> * h, char * rli_url, char * pattern)</h3>
<p> Delete an entry from the LRC rli/partition tables. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>rli_url</i> URL of RLI server to remove from LRC partition table.<br />
 <i>pattern</i> If not NULL then only the specific <i>rli_url/pattern</i> is removed, else all partition information for <i>rli_url</i> is removed.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> RLI and pattern (if specified) removed from LRC partition table.</dl>
<h3>globus_result_t globus_rls_client_lrc_rli_get_part (<code>globus_rls_handle_t</code> * h, char * rli_url, char * pattern, globus_list_t ** str2_list)</h3>
<p> Get RLI update partitions from LRC server. <code>Parameters:</code></p>
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
<h3>globus_result_t globus_rls_client_lrc_rli_info (<code>globus_rls_handle_t</code> * h, char * rli_url, <code>globus_rls_rli_info_t</code> * info)</h3>
<p> Get info about RLI server updated by an LRC server. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>rli_url</i> URL of RLI server to retrieve info for.<br />
 <i>info</i> Data about RLI server will be written here.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Info about RLI server successfully retrieved.</dl>
<h3>globus_result_t globus_rls_client_lrc_rli_list (<code>globus_rls_handle_t</code> * h, globus_list_t ** rliinfo_list)</h3>
<p> Return URLs of RLIs that LRC sends updates to. <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>h</i> Handle connected to an RLS server.<br />
 <i>rliinfo_list</i> List of RLIs updated by this LRC returned in this list. Each list datum is of type <code>globus_rls_rli_info_t</code>. <i>rliinfo_list</i> should be freed with <code>globus_rls_client_free_list()</code> when no longer needed.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> List of RLIs updated by this LRC returned in <i>rliinfo_list</i>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus rls client from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbBU">Author</a></p>
<dd></dl>
