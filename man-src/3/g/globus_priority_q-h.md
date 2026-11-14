---
title: "globus_priority_q-h(3)"
name: "globus_priority_q-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_priority_q-h/"
description: "globus_priority_q.h –"
---

<p>globus_priority_q.h &#8211; </p>
<p> Priority Queue.</p>
<h2>Synopsis</h2>
<p>#include &#8216;globus_types.h&#8217;<br />
 #include &#8216;globus_memory.h&#8217; </p>
<h3>Data Structures</h3>
<p>struct <code>globus_priority_q_s</code><br />
 <i>Priority Queue Structure. </i></p>
<h3>Typedefs</h3>
<p>typedef int(* <code>globus_priority_q_cmp_func_t</code> )(void *priority_1, void *priority_2)<br />
 <i>Priority Comparison Predicate. </i><br />
 typedef struct <code>globus_priority_q_s</code> <code>globus_priority_q_t</code><br />
 <i>Priority Queue Structure. </i></p>
<h3>Functions</h3>
<p>int <code>globus_priority_q_init</code> (<code>globus_priority_q_t</code> *priority_q, <code>globus_priority_q_cmp_func_t</code> cmp_func)<br />
 <i>Initialize a priority queue. </i><br />
 int <code>globus_priority_q_destroy</code> (<code>globus_priority_q_t</code> *priority_q)<br />
 <i>Destroy a Priority Queue. </i><br />
 <code>globus_bool_t</code> <code>globus_priority_q_empty</code> (<code>globus_priority_q_t</code> *priority_q)<br />
 <i>Priority Queue Empty Predicate. </i><br />
 int <code>globus_priority_q_size</code> (<code>globus_priority_q_t</code> *priority_q)<br />
 <i>Priority Queue Size. </i><br />
 int <code>globus_priority_q_enqueue</code> (<code>globus_priority_q_t</code> *priority_q, void *datum, void *priority)<br />
 <i>Add a Datum to a Priority Queue. </i><br />
 void * <code>globus_priority_q_remove</code> (<code>globus_priority_q_t</code> *priority_q, void *datum)<br />
 <i>Remove an Arbitrary Datum from a Priority Queue. </i><br />
 void * <code>globus_priority_q_modify</code> (<code>globus_priority_q_t</code> *priority_q, void *datum, void *new_priority)<br />
 <i>Modify the Priority of Datum. </i><br />
 void * <code>globus_priority_q_dequeue</code> (<code>globus_priority_q_t</code> *priority_q)<br />
 <i>Remove a Datum From A Priority Queue. </i><br />
 void * <code>globus_priority_q_first</code> (<code>globus_priority_q_t</code> *priority_q)<br />
 <i>Get the Highest-Priority Datum From a Priority Queue. </i><br />
 void * <code>globus_priority_q_first_priority</code> (<code>globus_priority_q_t</code> *priority_q)<br />
 <i>Get the Highest Priority in Priority Queue. </i></p>
<h2>Detailed Description</h2>
<p>Priority Queue. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_common from the source code.</p>
