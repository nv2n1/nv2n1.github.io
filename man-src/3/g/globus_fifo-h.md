---
title: "globus_fifo-h(3)"
name: "globus_fifo-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_fifo-h/"
description: "globus_fifo.h –"
---

<p>globus_fifo.h &#8211; </p>
<p> Globus FIFO.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_list.h&#8217; </p>
<h3>Typedefs</h3>
<p>typedef struct globus_fifo_s * <code>globus_fifo_t</code> </p>
<h3>Functions</h3>
<p>int <code>globus_fifo_init</code> (<code>globus_fifo_t</code> *fifo)<br />
 <i>Initialize the fifo structure. </i><br />
 void <code>globus_fifo_destroy</code> (<code>globus_fifo_t</code> *fifo) </p>
<p> void <code>globus_fifo_destroy_all</code> (<code>globus_fifo_t</code> *fifo, void(*datum_free)(void *)) </p>
<p> int <code>globus_fifo_empty</code> (const <code>globus_fifo_t</code> *fifo) </p>
<p> int <code>globus_fifo_size</code> (const <code>globus_fifo_t</code> *fifo) </p>
<p> int <code>globus_fifo_enqueue</code> (<code>globus_fifo_t</code> *fifo, void *datum) </p>
<p> <code>globus_fifo_t</code> * <code>globus_fifo_copy</code> (const <code>globus_fifo_t</code> *fifo) </p>
<p> void * <code>globus_fifo_peek</code> (<code>globus_fifo_t</code> *fifo) </p>
<p> void * <code>globus_fifo_tail_peek</code> (<code>globus_fifo_t</code> *fifo) </p>
<p> void * <code>globus_fifo_remove</code> (<code>globus_fifo_t</code> *headp, void *datum) </p>
<p> void * <code>globus_fifo_dequeue</code> (<code>globus_fifo_t</code> *fifo) </p>
<p> int <code>globus_fifo_move</code> (<code>globus_fifo_t</code> *fifo_dest, <code>globus_fifo_t</code> *fifo_src) </p>
<p> <code>globus_list_t</code> * <code>globus_fifo_convert_to_list</code> (<code>globus_fifo_t</code> *fifo) </p>
<h2>Detailed Description</h2>
<p>Globus FIFO. </p>
<p> This file defines the globus_fifo_t type useful for queuing arbitrary data (via void-pointer)</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_common from the source code.</p>
