---
title: "hwloc_obj_cpuset_snprintf(3)"
name: "hwloc_obj_cpuset_snprintf"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_obj_cpuset_snprintf/"
description: "hwlocality_object_strings – Manipulating Object Type, Sets and Attributes as Strings"
---
<h2 class="name">NAME</h2>
<p> hwlocality_object_strings - Manipulating Object Type, Sets and Attributes as Strings </p>
<h3>Functions</h3>
<p> <br />
 const char * <code>hwloc_obj_type_string</code> (<code>hwloc_obj_type_t</code> type) <br />
 <br />
 int <code>hwloc_obj_type_sscanf</code> (const char *string, <code>hwloc_obj_type_t</code> *typep, int *depthattrp, void *typeattrp, size_t typeattrsize) <br />
 <br />
 int <code>hwloc_obj_type_snprintf</code> (char *restrict string, size_t size, <code>hwloc_obj_t</code> obj, int verbose) <br />
 <br />
 int <code>hwloc_obj_attr_snprintf</code> (char *restrict string, size_t size, <code>hwloc_obj_t</code> obj, const char *restrict separator, int verbose) <br />
 <br />
 int <code>hwloc_obj_cpuset_snprintf</code> (char *restrict str, size_t size, size_t nobj, const <code>hwloc_obj_t</code> *restrict objs) <br />
 <br />
 static const char * <code>hwloc_obj_get_info_by_name</code> (<code>hwloc_obj_t</code> obj, const char *name) <br />
 <br />
 void <code>hwloc_obj_add_info</code> (<code>hwloc_obj_t</code> obj, const char *name, const char *value) <br />
  </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<code></code><h3>void hwloc_obj_add_info ( hwloc_obj_t obj, const char * name, const char * value)</h3>
<p> Add the given info name and value pair to the given object. The info is appended to the existing info array even if another key with the same name already exists. </p>
<p> The input strings are copied before being added in the object infos. </p>
<p> <code>Note:</code> </p>
<dl>
<dd> <p> This function may be used to enforce object colors in the lstopo graphical output by using &#8216;lstopoStyle&#8217; as a name and &#8216;Background=#rrggbb&#8217; as a value. See CUSTOM COLORS in the lstopo(1) manpage for details. </p>
<p> If value contains some non-printable characters, they will be dropped when exporting to XML, see <code>hwloc_topology_export_xml()</code>. </p>
 </dd></dl>
<code></code><h3>int hwloc_obj_attr_snprintf (char *restrict string, size_t size, hwloc_obj_t obj, const char *restrict separator, int verbose)</h3>
<p> Stringify the attributes of a given topology object into a human-readable form. Attribute values are separated by separator. </p>
<p> Only the major attributes are printed in non-verbose mode. </p>
<p> If size is 0, string may safely be NULL. </p>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> the number of character that were actually written if not truncating, or that would have been written (not including the ending \0). </p>
 </dd></dl>
<code></code><h3>int hwloc_obj_cpuset_snprintf (char *restrict str, size_t size, size_t nobj, const hwloc_obj_t *restrict objs)</h3>
<p> Stringify the cpuset containing a set of objects. If size is 0, string may safely be NULL. </p>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> the number of character that were actually written if not truncating, or that would have been written (not including the ending \0). </p>
 </dd></dl>
<code></code><h3>static const char* hwloc_obj_get_info_by_name ( hwloc_obj_t obj, const char * name) [inline], [static]</h3>
<p> Search the given key name in object infos and return the corresponding value. If multiple keys match the given name, only the first one is returned. </p>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> NULL if no such key exists. </p>
 </dd></dl>
<code></code><h3>int hwloc_obj_type_snprintf (char *restrict string, size_t size, hwloc_obj_t obj, int verbose)</h3>
<p> Stringify the type of a given topology object into a human-readable form. It differs from <code>hwloc_obj_type_string()</code> because it prints type attributes such as cache depth and type. </p>
<p> If size is 0, string may safely be NULL. </p>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> the number of character that were actually written if not truncating, or that would have been written (not including the ending \0). </p>
 </dd></dl>
<code></code><h3>int hwloc_obj_type_sscanf (const char * string, hwloc_obj_type_t * typep, int * depthattrp, void * typeattrp, size_t typeattrsize)</h3>
<p> Return an object type and attributes from a type string. Convert strings such as &#8216;Package&#8217; or &#8216;Cache&#8217; into the corresponding types. Matching is case-insensitive, and only the first letters are actually required to match. </p>
<p> Types that have specific attributes, for instance caches and groups, may be returned in depthattrp and typeattrp. They are ignored when these pointers are NULL. </p>
<p> For instance &#8216;L2i&#8217; or &#8216;L2iCache&#8217; would return type HWLOC_OBJ_CACHE in typep, 2 in depthattrp, and HWLOC_OBJ_CACHE_TYPE_INSTRUCTION in typeattrp (this last pointer should point to a hwloc_obj_cache_type_t). &#8216;Group3&#8217; would return type HWLOC_OBJ_GROUP type and 3 in depthattrp. Attributes that are not specified in the string (for instance &#8216;Group&#8217; without a depth, or &#8216;L2Cache&#8217; without a cache type) are set to -1. </p>
<p> typeattrp is only filled if the size specified in typeattrsize is large enough. It is currently only used for caches, and the required size is at least the size of hwloc_obj_cache_type_t. </p>
<p> <code>Returns:</code> </p>
<dl>
<dd> <p> 0 if a type was correctly identified, otherwise -1. </p>
 </dd></dl>
<p> <code>Note:</code> </p>
<dl>
<dd> <p> This is an extended version of the now deprecated hwloc_obj_type_of_string() </p>
 </dd></dl>
<code></code><h3>const char* hwloc_obj_type_string ( hwloc_obj_type_t type)</h3>
<p> Return a stringified topology object type.  </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dl>
<dt><a href="#lbAB">NAME</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAC">Functions</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAD">Detailed Description</a></dt>
<dd>  </dd>
<dt><a href="#lbAE">Function Documentation</a></dt>
<dd>  </dd>
<dl>
<dt><a href="#lbAF">void hwloc_obj_add_info (<code>hwloc_obj_t</code> obj, const char * name, const char * value)</a></dt>
<dd>  </dd>
<dt><a href="#lbAG">int hwloc_obj_attr_snprintf (char *restrict string, size_t size, <code>hwloc_obj_t</code> obj, const char *restrict separator, int verbose)</a></dt>
<dd>  </dd>
<dt><a href="#lbAH">int hwloc_obj_cpuset_snprintf (char *restrict str, size_t size, size_t nobj, const <code>hwloc_obj_t</code> *restrict objs)</a></dt>
<dd>  </dd>
<dt><a href="#lbAI">static const char* hwloc_obj_get_info_by_name (<code>hwloc_obj_t</code> obj, const char * name) [inline], [static]</a></dt>
<dd>  </dd>
<dt><a href="#lbAJ">int hwloc_obj_type_snprintf (char *restrict string, size_t size, <code>hwloc_obj_t</code> obj, int verbose)</a></dt>
<dd>  </dd>
<dt><a href="#lbAK">int hwloc_obj_type_sscanf (const char * string, <code>hwloc_obj_type_t</code> * typep, int * depthattrp, void * typeattrp, size_t typeattrsize)</a></dt>
<dd>  </dd>
<dt><a href="#lbAL">const char* hwloc_obj_type_string (<code>hwloc_obj_type_t</code> type)</a></dt>
<dd>  </dd></dl>
<dt><a href="#lbAM">Author</a></dt>
<dd>  </dd></dl>
