---
title: "hwloc_obj_type_string(3)"
name: "hwloc_obj_type_string"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_obj_type_string/"
description: "hwlocality_object_strings – Manipulating Object Type, Sets and Attributes as Strings"
---

<h2 class="name">NAME</h2>
<p> hwlocality_object_strings &#8211; Manipulating Object Type, Sets and Attributes as Strings </p>
<h3>Functions</h3>
<p> const char * <code>hwloc_obj_type_string</code> (<code>hwloc_obj_type_t</code> type) </p>
<p> int <code>hwloc_obj_type_sscanf</code> (const char *string, <code>hwloc_obj_type_t</code> *typep, int *depthattrp, void *typeattrp, size_t typeattrsize) </p>
<p> int <code>hwloc_obj_type_snprintf</code> (char *restrict string, size_t size, <code>hwloc_obj_t</code> obj, int verbose) </p>
<p> int <code>hwloc_obj_attr_snprintf</code> (char *restrict string, size_t size, <code>hwloc_obj_t</code> obj, const char *restrict separator, int verbose) </p>
<p> int <code>hwloc_obj_cpuset_snprintf</code> (char *restrict str, size_t size, size_t nobj, const <code>hwloc_obj_t</code> *restrict objs) </p>
<p> static const char * <code>hwloc_obj_get_info_by_name</code> (<code>hwloc_obj_t</code> obj, const char *name) </p>
<p> void <code>hwloc_obj_add_info</code> (<code>hwloc_obj_t</code> obj, const char *name, const char *value) </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>void hwloc_obj_add_info (<code>hwloc_obj_t</code> obj, const char * name, const char * value)</h3>
<p> Add the given info name and value pair to the given object. The info is appended to the existing info array even if another key with the same name already exists. </p>
<p> The input strings are copied before being added in the object infos. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> This function may be used to enforce object colors in the lstopo graphical output by using &#8216;lstopoStyle&#8217; as a name and &#8216;Background=#rrggbb&#8217; as a value. See CUSTOM COLORS in the <a href="/docs/linux/man/1-lstopo/">lstopo</a>(1) manpage for details. </p>
<p> If value contains some non-printable characters, they will be dropped when exporting to XML, see <code>hwloc_topology_export_xml()</code>.</dl>
<h3>int hwloc_obj_attr_snprintf (char *restrict string, size_t size, <code>hwloc_obj_t</code> obj, const char *restrict separator, int verbose)</h3>
<p> Stringify the attributes of a given topology object into a human-readable form. Attribute values are separated by separator. </p>
<p> Only the major attributes are printed in non-verbose mode. </p>
<p> If size is 0, string may safely be NULL. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the number of character that were actually written if not truncating, or that would have been written (not including the ending 
