---
title: "globus_net_manager-h(3)"
name: "globus_net_manager-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_net_manager-h/"
description: "globus_net_manager.h –"
---

<p>globus_net_manager.h &#8211; </p>
<p> Globus Net Manager Interface.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_common.h&#8217;<br />
 #include &#8216;globus_net_manager_attr.h&#8217; </p>
<h3>Data Structures</h3>
<p>struct <code>globus_net_manager_s</code><br />
 <i>Net Manager Definition. </i></p>
<h3>Macros</h3>
<p>#define <code>GLOBUS_NET_MANAGER_MODULE</code><br />
 <i>Module descriptor. </i></p>
<h3>Typedefs</h3>
<p>typedef globus_result_t(* <code>globus_net_manager_pre_listen</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Net Manager Pre-Listen Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_post_listen</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array, char **local_contact_out, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Net Manager Post-Listen Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_end_listen</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array)<br />
 <i>Net Manager End-Listen Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_pre_accept</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Net Manager Pre-Accept Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_post_accept</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Net Manager Post-Accept Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_pre_connect</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, char **remote_contact_out, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Net Manager Pre-Connect Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_post_connect</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array, <code>globus_net_manager_attr_t</code> **attr_array_out)<br />
 <i>Net Manager Post-Connect Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_pre_close</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array)<br />
 <i>Net Manager Pre-Close Function Signature. </i><br />
 typedef globus_result_t(* <code>globus_net_manager_post_close</code> )(struct <code>globus_net_manager_s</code> *manager, const <code>globus_net_manager_attr_t</code> *manager_attr_array, const char *task_id, const char *transport, const char *local_contact, const char *remote_contact, const <code>globus_net_manager_attr_t</code> *attr_array)<br />
 <i>Net Manager Post-Close Function Signature. </i><br />
 typedef struct <code>globus_net_manager_s</code> <code>globus_net_manager_t</code><br />
 <i>Net Manager Definition. </i></p>
<h3>Functions</h3>
<p>globus_result_t <code>globus_net_manager_register</code> (<code>globus_net_manager_t</code> *manager, globus_module_descriptor_t *module)<br />
 <i>Register a network manager. </i><br />
 globus_result_t <code>globus_net_manager_unregister</code> (<code>globus_net_manager_t</code> *manager)<br />
 <i>Unregister a network manager. </i></p>
<h2>Detailed Description</h2>
<p>Globus Net Manager Interface. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_net_manager from the source code.</p>
