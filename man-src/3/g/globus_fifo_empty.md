---
title: "globus_fifo_empty(3)"
name: "globus_fifo_empty"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_fifo_empty/"
description: "FIFO Queue –"
---

<h2 class="name">NAME</h2>
<p> FIFO Queue &#8211; </p>
<p> FIFO Queue Implementation.</p>
<h3>Typedefs</h3>
<p> typedef struct globus_fifo_s * <code>globus_fifo_t</code> </p>
<h3>Functions</h3>
<p> int <code>globus_fifo_init</code> (<code>globus_fifo_t</code> *fifo)<br />
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
<p> FIFO Queue Implementation. </p>
<h2>Typedef Documentation</h2>
<h3>typedef struct globus_fifo_s* <code>globus_fifo_t</code></h3>
<p> Data type used in all function calls to manipulate a Globus FIFO</p>
<h2>Function Documentation</h2>
<h3><code>globus_list_t</code>* globus_fifo_convert_to_list (<code>globus_fifo_t</code> *fifo)</h3>
<p> Convert the fifo into a list.</p>
<h3><code>globus_fifo_t</code>* globus_fifo_copy (const <code>globus_fifo_t</code> *fifo)</h3>
<p> Make a copy of the fifo. <code>globus_fifo_destroy()</code> must be called the returned pointer to free memory associated with it.</p>
<h3>void* globus_fifo_dequeue (<code>globus_fifo_t</code> *fifo)</h3>
<p> dequeue the element at the front of the queue.</p>
<h3>void globus_fifo_destroy (<code>globus_fifo_t</code> *fifo)</h3>
<p> Destroy the fifo data structure. </p>
<p> This function destroys the memory associate with the fifo data structure. For every call to <code>globus_fifo_init()</code> there must be a corresponding call to <code>globus_fifo_destroy()</code></p>
<h3>void globus_fifo_destroy_all (<code>globus_fifo_t</code> *fifo, void(*)(void *)datum_free)</h3>
<p> Destroy the fifo data structure. </p>
<p> This function destroys the memory associate with the fifo data structure. It calls datum_free() on behalf of all remaining nodes in the queue. For every call to <code>globus_fifo_init()</code> there must be a corresponding call to <code>globus_fifo_destroy()</code></p>
<h3>int globus_fifo_empty (const <code>globus_fifo_t</code> *fifo)</h3>
<p> This function returns a boolean indicating whether or not the fifo is empty.</p>
<h3>int globus_fifo_enqueue (<code>globus_fifo_t</code> *fifo, void *datum)</h3>
<p> Add data to the back of the queue.</p>
<h3>int globus_fifo_init (<code>globus_fifo_t</code> *fifo)</h3>
<p> Initialize the fifo structure. This function initializes the fifo data structure. The structure must be initalized before it can be used with any other function.</p>
<h3>int globus_fifo_move (<code>globus_fifo_t</code> *fifo_dest, <code>globus_fifo_t</code> *fifo_src)</h3>
<p> Move the queue from fifo_src pointer to fifo_dest pointer.</p>
<h3>void* globus_fifo_peek (<code>globus_fifo_t</code> *fifo)</h3>
<p> get a pointer to the element at the front of the queue.</p>
<h3>void* globus_fifo_remove (<code>globus_fifo_t</code> *headp, void *datum)</h3>
<p> remove datum from anywhere in the queue.</p>
<h3>int globus_fifo_size (const <code>globus_fifo_t</code> *fifo)</h3>
<p> This function returns a interger representing the number of elements in the queue.</p>
<h3>void* globus_fifo_tail_peek (<code>globus_fifo_t</code> *fifo)</h3>
<p> Get a pointer to the element at the back of the queue.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAH">Function Documentation</a></p>
<dd>
<dt><a href="#lbAV">Author</a></p>
<dd></dl>
