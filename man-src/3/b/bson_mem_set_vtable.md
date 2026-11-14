---
title: "bson_mem_set_vtable(3)"
name: "bson_mem_set_vtable"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_mem_set_vtable/"
description: "bson_mem_set_table() – This function shall install a new memory allocator to be used by Libbson."
---

<h2>NAME</h2>
<p> bson_mem_set_table() &#8211; This function shall install a new memory allocator to be used by Libbson.</p>
<h2>SYNOPSIS</h2>
<pre><code>
typedef struct _bson_mem_vtable_t {
    void *(*malloc)(size_t num_bytes);
    void *(*calloc)(size_t n_members,
                    size_t num_bytes);
    void *(*realloc)(void *mem,
                     size_t num_bytes);
    void (*free)(void *mem);
    void *padding[4];
} bson_mem_vtable_t;
void bson_mem_set_vtable(const bson_mem_vtable_t *vtable);
</code></pre>
<h2>PARAMETERS</h2>
<dl>
<dt><code>vtable</code></p>
<dd> A bson_mem_vtable_t with every non-padding field set.</dl>
<h2>DESCRIPTION</h2>
<p> This function shall install a new memory allocator to be used by Libbson. </p>
<p> <code>NOTE</code></p>
<dl>
<dt>
<dd> This function <code>MUST</code> be called at the beginning of the process. Failure to do so will result in memory being freed by the wrong allocator.</dl>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
