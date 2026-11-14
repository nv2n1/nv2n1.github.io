---
title: "globus_net_manager_context-h(3)"
name: "globus_net_manager_context-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_net_manager_context-h/"
description: "context/globus_net_manager_context.h –"
---

<p>context/globus_net_manager_context.h &#8211; </p>
<p> Globus Network Manager Context.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217;<br />
 #include &#8216;globus_net_manager.h&#8217;<br />
 #include &#8216;globus_net_manager_attr.h&#8217; </p>
<h3>Typedefs</h3>
<p>typedef struct<br />
 globus_i_net_manager_context_s * <code>globus_net_manager_context_t</code>&quot;<br />
 <i>Net Manager Context. </i></p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_net_manager_context_init</code> (<code>globus_net_manager_context_t</code> *context, const <code>globus_net_manager_attr_t</code> *attrs)<br />
 <i>Initialize Context. </i><br />
 void <code>globus_net_manager_context_destroy</code> (<code>globus_net_manager_context_t</code> context)<br />
 <i>Destroy Context. </i><br />
 globus_result_t <code>globus_net_manager_context_pre_listen</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Call Context Pre Listen. </i><br />
 globus_result_t <code>globus_net_manager_context_post_listen</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array, char **local_contact_out, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Call Context Post Listen. </i><br />
 globus_result_t <code>globus_net_manager_context_end_listen</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array)<br />
 <i>Call Context End Listen. </i><br />
 globus_result_t <code>globus_net_manager_context_pre_accept</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Call Context Pre Accept. </i><br />
 globus_result_t <code>globus_net_manager_context_post_accept</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Call Context Post Accept. </i><br />
 globus_result_t <code>globus_net_manager_context_pre_connect</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, char **remote_contact_out, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Call Context Pre Connect. </i><br />
 globus_result_t <code>globus_net_manager_context_post_connect</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Call Context Post Connect. </i><br />
 globus_result_t <code>globus_net_manager_context_pre_close</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array)<br />
 <i>Call Context Pre Close. </i><br />
 globus_result_t <code>globus_net_manager_context_post_close</code> (<code>globus_net_manager_context_t</code> context, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array)<br />
 <i>Call Context Post Close. </i></p>
<h2>Detailed Description</h2>
<p>Globus Network Manager Context. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_net_manager from the source code.</p>
