---
title: "hwloc_topology_export_xmlbuffer(3)"
name: "hwloc_topology_export_xmlbuffer"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_topology_export_xmlbuffer/"
description: "hwlocality_xmlexport – Exporting Topologies to XML"
---

<h2 class="name">NAME</h2>
<p> hwlocality_xmlexport &#8211; Exporting Topologies to XML </p>
<h3>Functions</h3>
<p> int <code>hwloc_topology_export_xml</code> (<code>hwloc_topology_t</code> topology, const char *xmlpath) </p>
<p> int <code>hwloc_topology_export_xmlbuffer</code> (<code>hwloc_topology_t</code> topology, char **xmlbuffer, int *buflen) </p>
<p> void <code>hwloc_free_xmlbuffer</code> (<code>hwloc_topology_t</code> topology, char *xmlbuffer) </p>
<p> void <code>hwloc_topology_set_userdata_export_callback</code> (<code>hwloc_topology_t</code> topology, void(*export_cb)(void *reserved, <code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj)) </p>
<p> int <code>hwloc_export_obj_userdata</code> (void *reserved, <code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj, const char *name, const void *buffer, size_t length) </p>
<p> int <code>hwloc_export_obj_userdata_base64</code> (void *reserved, <code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj, const char *name, const void *buffer, size_t length) </p>
<p> void <code>hwloc_topology_set_userdata_import_callback</code> (<code>hwloc_topology_t</code> topology, void(*import_cb)(<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj, const char *name, const void *buffer, size_t length)) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>int hwloc_export_obj_userdata (void * reserved, <code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj, const char * name, const void * buffer, size_t length)</h3>
<p> Export some object userdata to XML. This function may only be called from within the export() callback passed to <code>hwloc_topology_set_userdata_export_callback()</code>. It may be invoked one of multiple times to export some userdata to XML. The buffer content of length length is stored with optional name name. </p>
<p> When importing this XML file, the import() callback (if set) will be called exactly as many times as <code>hwloc_export_obj_userdata()</code> was called during export(). It will receive the corresponding name, buffer and length arguments. </p>
<p> reserved, topology and obj must be the first three parameters that were given to the export callback. </p>
<p> Only printable characters may be exported to XML string attributes. If a non-printable character is passed in name or buffer, the function returns -1 with errno set to EINVAL. </p>
<p> If exporting binary data, the application should first encode into printable characters only (or use <code>hwloc_export_obj_userdata_base64()</code>). It should also take care of portability issues if the export may be reimported on a different architecture.</p>
<h3>int hwloc_export_obj_userdata_base64 (void * reserved, <code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj, const char * name, const void * buffer, size_t length)</h3>
<p> Encode and export some object userdata to XML. This function is similar to <code>hwloc_export_obj_userdata()</code> but it encodes the input buffer into printable characters before exporting. On import, decoding is automatically performed before the data is given to the import() callback if any. </p>
<p> This function may only be called from within the export() callback passed to <code>hwloc_topology_set_userdata_export_callback()</code>. </p>
<p> The function does not take care of portability issues if the export may be reimported on a different architecture.</p>
<h3>void hwloc_free_xmlbuffer (<code>hwloc_topology_t</code> topology, char * xmlbuffer)</h3>
<p> Free a buffer allocated by <code>hwloc_topology_export_xmlbuffer()</code></p>
<h3>int hwloc_topology_export_xml (<code>hwloc_topology_t</code> topology, const char * xmlpath)</h3>
<p> Export the topology into an XML file. This file may be loaded later through <code>hwloc_topology_set_xml()</code>. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 if a failure occured.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> See also <code>hwloc_topology_set_userdata_export_callback()</code> for exporting application-specific object userdata. </p>
<p> The topology-specific userdata pointer is ignored when exporting to XML. </p>
<p> Only printable characters may be exported to XML string attributes. Any other character, especially any non-ASCII character, will be silently dropped. </p>
<p> If name is &#8216;-&#8216;, the XML output is sent to the standard output.</dl>
<h3>int hwloc_topology_export_xmlbuffer (<code>hwloc_topology_t</code> topology, char ** xmlbuffer, int * buflen)</h3>
<p> Export the topology into a newly-allocated XML memory buffer. xmlbuffer is allocated by the callee and should be freed with <code>hwloc_free_xmlbuffer()</code> later in the caller. </p>
<p> This memory buffer may be loaded later through <code>hwloc_topology_set_xmlbuffer()</code>. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> -1 if a failure occured.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> See also <code>hwloc_topology_set_userdata_export_callback()</code> for exporting application-specific object userdata. </p>
<p> The topology-specific userdata pointer is ignored when exporting to XML. </p>
<p> Only printable characters may be exported to XML string attributes. Any other character, especially any non-ASCII character, will be silently dropped.</dl>
<h3>void hwloc_topology_set_userdata_export_callback (<code>hwloc_topology_t</code> topology, void(*)(void *reserved, <code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj) export_cb)</h3>
<p> Set the application-specific callback for exporting object userdata. The object userdata pointer is not exported to XML by default because hwloc does not know what it contains. </p>
<p> This function lets applications set export_cb to a callback function that converts this opaque userdata into an exportable string. </p>
<p> export_cb is invoked during XML export for each object whose userdata pointer is not NULL. The callback should use <code>hwloc_export_obj_userdata()</code> or <code>hwloc_export_obj_userdata_base64()</code> to actually export something to XML (possibly multiple times per object). </p>
<p> export_cb may be set to NULL if userdata should not be exported to XML. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The topology-specific userdata pointer is ignored when exporting to XML.</dl>
<h3>void hwloc_topology_set_userdata_import_callback (<code>hwloc_topology_t</code> topology, void(*)(<code>hwloc_topology_t</code> topology, <code>hwloc_obj_t</code> obj, const char *name, const void *buffer, size_t length) import_cb)</h3>
<p> Set the application-specific callback for importing userdata. On XML import, userdata is ignored by default because hwloc does not know how to store it in memory. </p>
<p> This function lets applications set import_cb to a callback function that will get the XML-stored userdata and store it in the object as expected by the application. </p>
<p> import_cb is called during <code>hwloc_topology_load()</code> as many times as <code>hwloc_export_obj_userdata()</code> was called during export. The topology is not entirely setup yet. Object attributes are ready to consult, but links between objects are not. </p>
<p> import_cb may be NULL if userdata should be ignored during import. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> buffer contains length characters followed by a null byte (&#8216;
