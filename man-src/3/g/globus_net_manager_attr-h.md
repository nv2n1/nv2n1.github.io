---
title: "globus_net_manager_attr-h(3)"
name: "globus_net_manager_attr-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_net_manager_attr-h/"
description: "attr/globus_net_manager_attr.h –"
---

<p>attr/globus_net_manager_attr.h &#8211; </p>
<p> Globus Network Manager Attributes.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217; </p>
<h3>Data Structures</h3>
<p>struct <code>globus_net_manager_attr_s</code><br />
 <i>Net Manager Attributes. </i></p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_NET_MANAGER_NULL_ATTR</code><br />
 <i>End of attribute array static initializer. </i></p>
<h3>Typedefs</h3>
<p>typedef struct<br />
 <code>globus_net_manager_attr_s</code> <code>globus_net_manager_attr_t</code>&quot;<br />
 <i>Net Manager Attributes. </i></p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_net_manager_attr_init</code> (<code>globus_net_manager_attr_t</code> *attr, const char *scope, const char *name, const char *value)<br />
 <i>Initialize the contents of an attribute. </i><br />
 void <code>globus_net_manager_attr_destroy</code> (<code>globus_net_manager_attr_t</code> *attr)<br />
 <i>Destroy the contents of an attribute. </i><br />
 globus_result_t <code>globus_net_manager_attr_array_from_string</code> (<code>globus_net_manager_attr_t</code> **attr, const char *scope, const char *attr_string)<br />
 <i>Parse an array of Network Manager attributes from a string. </i><br />
 globus_result_t <code>globus_net_manager_attr_array_copy</code> (<code>globus_net_manager_attr_t</code> **dest_array, const <code>globus_net_manager_attr_t</code> *src_array)<br />
 <i>Copy an array of Network Manager attributes. </i><br />
 void <code>globus_net_manager_attr_array_delete</code> (<code>globus_net_manager_attr_t</code> *attrs)<br />
 <i>Destroy an array of Network Manager attributes. </i></p>
<h3>Variables</h3>
<p>const <code>globus_net_manager_attr_t</code> <code>globus_net_manager_null_attr</code><br />
 <i>End of array value. </i></p>
<h2>Detailed Description</h2>
<p>Globus Network Manager Attributes. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_net_manager from the source code.</p>
