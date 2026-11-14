---
title: "netsnmp_iterator_info_s(3)"
name: "netsnmp_iterator_info_s"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_iterator_info_s/"
description: "iterator_info_s – Holds iterator information containing functions which should be called by the iterator_handler to loop over your data set and sort it in a SNMP specific manner."
---

<p>iterator_info_s &#8211; Holds iterator information containing functions which should be called by the iterator_handler to loop over your data set and sort it in a SNMP specific manner. </p>
<h2>Synopsis</h2>
<h3>Data Fields</h3>
<p><code>netsnmp_container</code> <code>c</code> </p>
<p> <code>Netsnmp_Iterator_Loop_Key</code> * <code>get_first</code> </p>
<p> <code>Netsnmp_Iterator_Loop_Key</code> * <code>get_next</code> </p>
<p> <code>Netsnmp_Iterator_Loop_Data</code> * <code>get_data</code> </p>
<p> <code>Netsnmp_Iterator_Data</code> * <code>free_user_ctx</code> </p>
<p> <code>Netsnmp_Iterator_Ctx</code> * <code>init_loop_ctx</code> </p>
<p> <code>Netsnmp_Iterator_Ctx</code> * <code>cleanup_loop_ctx</code> </p>
<p> <code>Netsnmp_Iterator_Ctx_Dup</code> * <code>save_pos</code> </p>
<p> <code>Netsnmp_Iterator_Data</code> * <code>release_data</code> </p>
<p> <code>Netsnmp_Iterator_Data</code> * <code>insert_data</code> </p>
<p> <code>Netsnmp_Iterator_Data</code> * <code>remove_data</code> </p>
<p> <code>Netsnmp_Iterator_Op</code> * <code>get_size</code> </p>
<p> int <code>sorted</code> </p>
<p> void * <code>user_ctx</code><br />
 <i>This can be used by client handlers to store any information they need. </i></p>
<h2>Detailed Description</h2>
<p>Holds iterator information containing functions which should be called by the iterator_handler to loop over your data set and sort it in a SNMP specific manner. </p>
<p> The iterator_info typedef can be used instead of directly calling this struct if you would prefer. </p>
<p> Definition at line 39 of file container_iterator.c.</p>
<h2>Field Documentation</h2>
<h3>void* <code>iterator_info_s::user_ctx</code></h3>
<p>This can be used by client handlers to store any information they need. </p>
<p> Definition at line 69 of file container_iterator.c. </p>
<p> Referenced by netsnmp_container_iterator_get().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for net-snmp from the source code.</p>
