---
title: "netsnmp_container_iterator(3)"
name: "netsnmp_container_iterator"
section: "3"
letter: "n"
url: "/docs/linux/man/3-netsnmp_container_iterator/"
description: "Container_iterator –"
---

<p>Container_iterator &#8211;</p>
<h3>Typedefs</h3>
<p>typedef int( <code>Netsnmp_Iterator_Loop_Key</code> )(void *iterator_ctx, netsnmp_ref_void *loop_ctx, netsnmp_ref_void *key) </p>
<p> typedef int( <code>Netsnmp_Iterator_Loop_Data</code> )(void *iterator_ctx, netsnmp_ref_void *loop_ctx, netsnmp_ref_void *data) </p>
<p> typedef int( <code>Netsnmp_Iterator_Ctx</code> )(void *iterator_ctx, netsnmp_ref_void *loop_ctx) </p>
<p> typedef int( <code>Netsnmp_Iterator_Ctx_Dup</code> )(void *iterator_ctx, netsnmp_ref_void *loop_ctx, netsnmp_ref_void *dup_ctx, int reuse) </p>
<p> typedef int( <code>Netsnmp_Iterator_Op</code> )(void *iterator_ctx) </p>
<p> typedef int( <code>Netsnmp_Iterator_Data</code> )(void *iterator_ctx, const void *data)</p>
<h3>Functions</h3>
<pre><code>void netsnmp_container_iterator_init (void)



netsnmp_container * netsnmp_container_iterator_get (void *iterator_user_ctx, netsnmp_container_compare *compare, Netsnmp_Iterator_Loop_Key *get_first, Netsnmp_Iterator_Loop_Key *get_next, Netsnmp_Iterator_Loop_Data *get_data, Netsnmp_Iterator_Ctx_Dup *save_pos, Netsnmp_Iterator_Ctx *init_loop_ctx, Netsnmp_Iterator_Ctx *cleanup_loop_ctx, Netsnmp_Iterator_Data *free_user_ctx, int sorted)



void netsnmp_container_iterator_set_data_cb (netsnmp_container *c, Netsnmp_Iterator_Data *insert_data, Netsnmp_Iterator_Data *remove_data, Netsnmp_Iterator_Op *get_size)
</code></pre>
