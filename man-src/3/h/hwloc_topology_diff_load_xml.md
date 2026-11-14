---
title: "hwloc_topology_diff_load_xml(3)"
name: "hwloc_topology_diff_load_xml"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hwloc_topology_diff_load_xml/"
description: "hwlocality_diff – Topology differences"
---

<h2 class="name">NAME</h2>
<p> hwlocality_diff &#8211; Topology differences </p>
<h3>Data Structures</h3>
<p> union <code>hwloc_topology_diff_obj_attr_u</code> </p>
<p> struct <code>hwloc_topology_diff_obj_attr_u::hwloc_topology_diff_obj_attr_uint64_s</code> </p>
<p> struct <code>hwloc_topology_diff_obj_attr_u::hwloc_topology_diff_obj_attr_string_s</code> </p>
<p> struct <code>hwloc_topology_diff_obj_attr_u::hwloc_topology_diff_obj_attr_generic_s</code> </p>
<p> union <code>hwloc_topology_diff_u</code> </p>
<p> struct <code>hwloc_topology_diff_u::hwloc_topology_diff_too_complex_s</code> </p>
<p> struct <code>hwloc_topology_diff_u::hwloc_topology_diff_obj_attr_s</code> </p>
<p> struct <code>hwloc_topology_diff_u::hwloc_topology_diff_generic_s</code> </p>
<h3>Typedefs</h3>
<p> typedef enum <code>hwloc_topology_diff_obj_attr_type_e</code> <code>hwloc_topology_diff_obj_attr_type_t</code> </p>
<p> typedef enum <code>hwloc_topology_diff_type_e</code> <code>hwloc_topology_diff_type_t</code> </p>
<p> typedef union <code>hwloc_topology_diff_u</code> * <code>hwloc_topology_diff_t</code> </p>
<h3>Enumerations</h3>
<p> enum <code>hwloc_topology_diff_obj_attr_type_e</code> { <code>HWLOC_TOPOLOGY_DIFF_OBJ_ATTR_SIZE</code>, <code>HWLOC_TOPOLOGY_DIFF_OBJ_ATTR_NAME</code>, <code>HWLOC_TOPOLOGY_DIFF_OBJ_ATTR_INFO</code> } </p>
<p> enum <code>hwloc_topology_diff_type_e</code> { <code>HWLOC_TOPOLOGY_DIFF_OBJ_ATTR</code>, <code>HWLOC_TOPOLOGY_DIFF_TOO_COMPLEX</code> } </p>
<p> enum <code>hwloc_topology_diff_apply_flags_e</code> { <code>HWLOC_TOPOLOGY_DIFF_APPLY_REVERSE</code> } </p>
<h3>Functions</h3>
<p> int <code>hwloc_topology_diff_build</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_topology_t</code> newtopology, unsigned long flags, <code>hwloc_topology_diff_t</code> *diff) </p>
<p> int <code>hwloc_topology_diff_apply</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_topology_diff_t</code> diff, unsigned long flags) </p>
<p> int <code>hwloc_topology_diff_destroy</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_topology_diff_t</code> diff) </p>
<p> int <code>hwloc_topology_diff_load_xml</code> (<code>hwloc_topology_t</code> topology, const char *xmlpath, <code>hwloc_topology_diff_t</code> *diff, char **refname) </p>
<p> int <code>hwloc_topology_diff_export_xml</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_topology_diff_t</code> diff, const char *refname, const char *xmlpath) </p>
<p> int <code>hwloc_topology_diff_load_xmlbuffer</code> (<code>hwloc_topology_t</code> topology, const char *xmlbuffer, int buflen, <code>hwloc_topology_diff_t</code> *diff, char **refname) </p>
<p> int <code>hwloc_topology_diff_export_xmlbuffer</code> (<code>hwloc_topology_t</code> topology, <code>hwloc_topology_diff_t</code> diff, const char *refname, char **xmlbuffer, int *buflen) </p>
<h2>Detailed Description</h2>
<p> Applications that manipulate many similar topologies, for instance one for each node of a homogeneous cluster, may want to compress topologies to reduce the memory footprint. </p>
<p> This file offers a way to manipulate the difference between topologies and export/import it to/from XML. Compression may therefore be achieved by storing one topology entirely while the others are only described by their differences with the former. The actual topology can be reconstructed when actually needed by applying the precomputed difference to the reference topology. </p>
<p> This interface targets very similar nodes. Only very simple differences between topologies are actually supported, for instance a change in the memory size, the name of the object, or some info attribute. More complex differences such as adding or removing objects cannot be represented in the difference structures and therefore return errors. </p>
<p> It means that there is no need to apply the difference when looking at the tree organization (how many levels, how many objects per level, what kind of objects, CPU and node sets, etc) and when binding to objects. However the difference must be applied when looking at object attributes such as the name, the memory size or info attributes.</p>
<h2>Typedef Documentation</h2>
<h3>typedef enum <code>hwloc_topology_diff_obj_attr_type_e</code> <code>hwloc_topology_diff_obj_attr_type_t</code></h3>
<p> Type of one object attribute difference.</p>
<h3>typedef union <code>hwloc_topology_diff_u</code> * <code>hwloc_topology_diff_t</code></h3>
<p> One element of a difference list between two topologies.</p>
<h3>typedef enum <code>hwloc_topology_diff_type_e</code> <code>hwloc_topology_diff_type_t</code></h3>
<p> Type of one element of a difference list.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>hwloc_topology_diff_apply_flags_e</code></h3>
<p> Flags to be given to <code>hwloc_topology_diff_apply()</code>. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>HWLOC_TOPOLOGY_DIFF_APPLY_REVERSE </i></p>
<dd> Apply topology diff in reverse direction.</dl>
<h3>enum <code>hwloc_topology_diff_obj_attr_type_e</code></h3>
<p> Type of one object attribute difference. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>HWLOC_TOPOLOGY_DIFF_OBJ_ATTR_SIZE </i></p>
<dd> The object local memory is modified. The union is a <code>hwloc_topology_diff_obj_attr_u::hwloc_topology_diff_obj_attr_uint64_s</code> (and the index field is ignored).</p>
<dt><i>HWLOC_TOPOLOGY_DIFF_OBJ_ATTR_NAME </i></p>
<dd> The object name is modified. The union is a <code>hwloc_topology_diff_obj_attr_u::hwloc_topology_diff_obj_attr_string_s</code> (and the name field is ignored).</p>
<dt><i>HWLOC_TOPOLOGY_DIFF_OBJ_ATTR_INFO </i></p>
<dd> the value of an info attribute is modified. The union is a <code>hwloc_topology_diff_obj_attr_u::hwloc_topology_diff_obj_attr_string_s</code>.</dl>
<h3>enum <code>hwloc_topology_diff_type_e</code></h3>
<p> Type of one element of a difference list. </p>
<p> <code>Enumerator</code></p>
<dl>
<dt><i>HWLOC_TOPOLOGY_DIFF_OBJ_ATTR </i></p>
<dd> An object attribute was changed. The union is a hwloc_topology_diff_obj_attr_u::hwloc_topology_diff_obj_attr_s.</p>
<dt><i>HWLOC_TOPOLOGY_DIFF_TOO_COMPLEX </i></p>
<dd> The difference is too complex, it cannot be represented. The difference below this object has not been checked. <code>hwloc_topology_diff_build()</code> will return 1. The union is a hwloc_topology_diff_obj_attr_u::hwloc_topology_diff_too_complex_s.</dl>
<h2>Function Documentation</h2>
<h3>int hwloc_topology_diff_apply (<code>hwloc_topology_t</code> topology, <code>hwloc_topology_diff_t</code> diff, unsigned long flags)</h3>
<p> Apply a topology diff to an existing topology. flags is an OR&#8217;ed set of <code>hwloc_topology_diff_apply_flags_e</code>. </p>
<p> The new topology is modified in place. <code>hwloc_topology_dup()</code> may be used to duplicate it before patching. </p>
<p> If the difference cannot be applied entirely, all previous applied elements are unapplied before returning. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 on success. </p>
<p> -N if applying the difference failed while trying to apply the N-th part of the difference. For instance -1 is returned if the very first difference element could not be applied.</dl>
<h3>int hwloc_topology_diff_build (<code>hwloc_topology_t</code> topology, <code>hwloc_topology_t</code> newtopology, unsigned long flags, <code>hwloc_topology_diff_t</code> * diff)</h3>
<p> Compute the difference between 2 topologies. The difference is stored as a list of <code>hwloc_topology_diff_t</code> entries starting at diff. It is computed by doing a depth-first traversal of both topology trees simultaneously. </p>
<p> If the difference between 2 objects is too complex to be represented (for instance if some objects have different types, or different numbers of children), a special diff entry of type <code>HWLOC_TOPOLOGY_DIFF_TOO_COMPLEX</code> is queued. The computation of the diff does not continue below these objects. So each such diff entry means that the difference between two subtrees could not be computed. </p>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> 0 if the difference can be represented properly. </p>
<p> 0 with diff pointing to NULL if there is no difference between the topologies. </p>
<p> 1 if the difference is too complex (see above). Some entries in the list will be of type <code>HWLOC_TOPOLOGY_DIFF_TOO_COMPLEX</code>. </p>
<p> -1 on any other error.</dl>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> flags is currently not used. It should be 0. </p>
<p> The output diff has to be freed with <code>hwloc_topology_diff_destroy()</code>. </p>
<p> The output diff can only be exported to XML or passed to <code>hwloc_topology_diff_apply()</code> if 0 was returned, i.e. if no entry of type <code>HWLOC_TOPOLOGY_DIFF_TOO_COMPLEX</code> is listed. </p>
<p> The output diff may be modified by removing some entries from the list. The removed entries should be freed by passing them to to <code>hwloc_topology_diff_destroy()</code> (possible as another list).</dl>
<h3>int hwloc_topology_diff_destroy (<code>hwloc_topology_t</code> topology, <code>hwloc_topology_diff_t</code> diff)</h3>
<p> Destroy a list of topology differences. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The topology parameter must be a valid topology but it is not required that it is related to diff.</dl>
<h3>int hwloc_topology_diff_export_xml (<code>hwloc_topology_t</code> topology, <code>hwloc_topology_diff_t</code> diff, const char * refname, const char * xmlpath)</h3>
<p> Export a list of topology differences to a XML file. If not NULL, refname defines an identifier string for the reference topology which was used as a base when computing this difference. This identifier is usually the name of the other XML file that contains the reference topology. This attribute is given back when reading the diff from XML. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The topology parameter must be a valid topology but it is not required that it is related to diff.</dl>
<h3>int hwloc_topology_diff_export_xmlbuffer (<code>hwloc_topology_t</code> topology, <code>hwloc_topology_diff_t</code> diff, const char * refname, char ** xmlbuffer, int * buflen)</h3>
<p> Export a list of topology differences to a XML buffer. If not NULL, refname defines an identifier string for the reference topology which was used as a base when computing this difference. This identifier is usually the name of the other XML file that contains the reference topology. This attribute is given back when reading the diff from XML. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The XML buffer should later be freed with <code>hwloc_free_xmlbuffer()</code>. </p>
<p> The topology parameter must be a valid topology but it is not required that it is related to diff.</dl>
<h3>int hwloc_topology_diff_load_xml (<code>hwloc_topology_t</code> topology, const char * xmlpath, <code>hwloc_topology_diff_t</code> * diff, char ** refname)</h3>
<p> Load a list of topology differences from a XML file. If not NULL, refname will be filled with the identifier string of the reference topology for the difference file, if any was specified in the XML file. This identifier is usually the name of the other XML file that contains the reference topology. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The topology parameter must be a valid topology but it is not required that it is related to diff. </p>
<p> the pointer returned in refname should later be freed by the caller.</dl>
<h3>int hwloc_topology_diff_load_xmlbuffer (<code>hwloc_topology_t</code> topology, const char * xmlbuffer, int buflen, <code>hwloc_topology_diff_t</code> * diff, char ** refname)</h3>
<p> Load a list of topology differences from a XML buffer. If not NULL, refname will be filled with the identifier string of the reference topology for the difference file, if any was specified in the XML file. This identifier is usually the name of the other XML file that contains the reference topology. </p>
<p> <code>Note:</code></p>
<dl>
<dt>
<dd> The topology parameter must be a valid topology but it is not required that it is related to diff. </p>
<p> the pointer returned in refname should later be freed by the caller.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for Hardware Locality (hwloc) from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Enumeration Type Documentation</a></p>
<dd>
<dt><a href="#lbAP">Function Documentation</a></p>
<dd>
<dt><a href="#lbAX">Author</a></p>
<dd></dl>
