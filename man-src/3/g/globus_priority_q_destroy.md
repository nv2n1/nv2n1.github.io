---
title: "globus_priority_q_destroy(3)"
name: "globus_priority_q_destroy"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_priority_q_destroy/"
description: "Priority Queue –"
---

<h2 class="name">NAME</h2>
<p> Priority Queue &#8211; </p>
<h3>Data Structures</h3>
<p> struct <code>globus_priority_q_s</code><br />
 <i>Priority Queue Structure. </i></p>
<h3>Typedefs</h3>
<p> typedef int(* <code>globus_priority_q_cmp_func_t</code> )(void *priority_1, void *priority_2)<br />
 <i>Priority Comparison Predicate. </i><br />
 typedef struct <code>globus_priority_q_s</code> <code>globus_priority_q_t</code><br />
 <i>Priority Queue Structure. </i></p>
<h3>Functions</h3>
<p> int <code>globus_priority_q_init</code> (<code>globus_priority_q_t</code> *priority_q, <code>globus_priority_q_cmp_func_t</code> cmp_func)<br />
 <i>Initialize a priority queue. </i><br />
 int <code>globus_priority_q_destroy</code> (<code>globus_priority_q_t</code> *priority_q)<br />
 <i>Destroy a Priority Queue. </i><br />
 <code>globus_bool_t</code> <code>globus_priority_q_empty</code> (<code>globus_priority_q_t</code> *priority_q)<br />
 <i>Priority Queue Empty Predicate. </i><br />
 int <code>globus_priority_q_size</code> (<code>globus_priority_q_t</code> *priority_q)<br />
 <i>Priority Queue Size. </i><br />
 int <code>globus_priority_q_enqueue</code> (<code>globus_priority_q_t</code> *priority_q, void *datum, void *priority)<br />
 <i>Add a Datum to a Priority Queue. </i><br />
 void * <code>globus_priority_q_dequeue</code> (<code>globus_priority_q_t</code> *priority_q)<br />
 <i>Remove a Datum From A Priority Queue. </i><br />
 void * <code>globus_priority_q_first</code> (<code>globus_priority_q_t</code> *priority_q)<br />
 <i>Get the Highest-Priority Datum From a Priority Queue. </i><br />
 void * <code>globus_priority_q_first_priority</code> (<code>globus_priority_q_t</code> *priority_q)<br />
 <i>Get the Highest Priority in Priority Queue. </i><br />
 void * <code>globus_priority_q_remove</code> (<code>globus_priority_q_t</code> *priority_q, void *datum)<br />
 <i>Remove an Arbitrary Datum from a Priority Queue. </i><br />
 void * <code>globus_priority_q_modify</code> (<code>globus_priority_q_t</code> *priority_q, void *datum, void *new_priority)<br />
 <i>Modify the Priority of Datum. </i></p>
<h2>Detailed Description</h2>
<p> This module defines a priority queue for globus. It is implemented using a binary heap (minheap) and does NOT have a fifo fallback for like priorities. If you need fifo fallback, you should use a compound priority with the primary priority being the &#8216;real&#8217; priority and the secondary being a serial number. </p>
<p> To use this priority queue type, define a comparison function of type globus_priority_q_cmp_func_t and pass that to <code>globus_priority_q_init()</code>. </p>
<p> To add and remove items in priority order, use <code>globus_priority_q_enqueue()</code> and <code>globus_priority_q_dequeue()</code> respectively. </p>
<p> To remove a datum ignoring its priority, use <code>globus_priority_q_remove()</code>. </p>
<p> To inspect the first element and its priority, use <code>globus_priority_q_first()</code> and <code>globus_priority_q_first_priority()</code> respectively. </p>
<p> To determine whether a queue is empty or the number of data in it, use <code>globus_priority_q_empty()</code> and <code>globus_priority_q_size()</code>. </p>
<p> To modify the priority of a datum already in the queue, use <code>globus_priority_q_modify()</code>. </p>
<p> When finished with the queue, use <code>globus_priority_q_destroy()</code> to free data associated with the priority queue.</p>
<h2>Typedef Documentation</h2>
<h3>typedef int(* globus_priority_q_cmp_func_t)(void *priority_1, void *priority_2)</h3>
<p> Priority Comparison Predicate. This type is used to implement comparison of two priorities for inserting items into the priority queue. A function of this type is passed to <code>globus_priority_q_init()</code> to determine how priorities are computed in a newly created priority queue. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>priority_1</i> First priority to compare<br />
 <i>priority_2</i> Second priority to compare</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>&gt;</i> 0 The priority of priority_1 is less than that of priority_2.<br />
 <i>&lt;</i> 0 The priority of priority_1 is greater than that of priority_2.<br />
 <i>=</i> 0 The priorities of priority_1 and priority_2 are the same.</dl>
<h3>typedef struct <code>globus_priority_q_s</code> <code>globus_priority_q_t</code></h3>
<p> Priority Queue Structure. A pointer to a structure of this type is passed to all functions in the <code>Priority Queue </code> module. It is not intended to be inspected or modified outside of this API.</p>
<h2>Function Documentation</h2>
<h3>void* globus_priority_q_dequeue (<code>globus_priority_q_t</code> *priority_q)</h3>
<p> Remove a Datum From A Priority Queue. The <code>globus_priority_q_dequeue()</code> function removes the highest-priority datum from the given priority queue and returns it. If the priority_q pointer is NULL or the priority queue is empty, this function returns NULL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>priority_q</i> Pointer to the priority queue to remove from.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns the highest-priority datum from the priority queue.</dl>
<h3>int globus_priority_q_destroy (<code>globus_priority_q_t</code> *priority_q)</h3>
<p> Destroy a Priority Queue. The <code>globus_priority_q_destroy()</code> function destroys the contents of a priority queue. After this function returns, the structure pointed to by priority_q is invalid and must not be passed to any functions in the <code>Priority Queue </code> module other <code>globus_priority_q_init()</code>. </p>
<p> Note that this function does not call any destructors for the data inserted into the priority queue, so the caller must be sure to either have other references to those data or free them before calling this function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>priority_q</i> Pointer to the priority_q to destroy.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_FAILURE</i> Failure</dl>
<h3><code>globus_bool_t</code> globus_priority_q_empty (<code>globus_priority_q_t</code> *priority_q)</h3>
<p> Priority Queue Empty Predicate. The <code>globus_priority_q_empty()</code> function checks the given priority queue to determine if it is empty. It is considered empty if it has been initialized via <code>globus_priority_q_init()</code> and there are no items which have been inserted via <code>globus_priority_q_enqueue()</code> which have not been removed by calling <code>globus_priority_q_remove()</code> or <code>globus_priority_q_dequeue()</code>. If it is empty, this function returns GLOBUS_TRUE; otherwise it returns GLOBUS_FALSE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>priority_q</i> Pointer to the priority queue to check</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_TRUE</i> The priority queue is empty<br />
 <i>GLOBUS_FALSE</i> The priority queue is not empty, or the priority queue is invalid</dl>
<h3>int globus_priority_q_enqueue (<code>globus_priority_q_t</code> *priority_q, void *datum, void *priority)</h3>
<p> Add a Datum to a Priority Queue. The <code>globus_priority_q_enqueue()</code> function inserts a datum into the priority queue based on its priority. When an item is inserted, the pointers to both the datum and the priority are copied into the priority_q data structure, so neither may be freed until the datum is removed from the priority queue, or undefined behavior may occur. </p>
<p> Note that there is no fifo fallback for priorities, so the order of two items with equivalent priorities is not specified relative to each other. To enable fifo fallback, use a compound priority that includes a priority level and a sequence number as the value pointed to by the priority parameter and pass a suitable comparison function to initialize the priority queue. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>priority_q</i> Pointer to the priority queue to insert datum into<br />
 <i>datum</i> The datum to insert into the queue<br />
 <i>priority</i> The priority of the datum</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_FAILURE</i> Failure</dl>
<h3>void* globus_priority_q_first (<code>globus_priority_q_t</code> *priority_q)</h3>
<p> Get the Highest-Priority Datum From a Priority Queue. The <code>globus_priority_q_first()</code> function returns the highest-priority datum from the priority queue pointed to by priority_q. The datum is not removed from the queue; to do that, use <code>globus_priority_q_dequeue()</code> instead. If the priority_q pointer is NULL or the queue is empty, this function returns NULL. The priority queue retains a reference to the returned datum, so the pointer value returned must not freed until the datum is removed from the queue. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>priority_q</i> Pointer to the priority queue to inspect</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns the highest-priority datum from the priority queue.</dl>
<h3>void* globus_priority_q_first_priority (<code>globus_priority_q_t</code> *priority_q)</h3>
<p> Get the Highest Priority in Priority Queue. The <code>globus_priority_q_first_priority()</code> function returns the value of highest priority in the priority queue (not the datum associated with that priority). If the priority_q pointer is NULL or empty, this function returns NULL. The priority queue retains a reference to the returned priority, so the pointer value returned must not be freed until the datum associated with it is removed from the queue. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>priority_q</i> Pointer to the priority queue to inspect</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns the highest priority value in the priority queue.</dl>
<h3>int globus_priority_q_init (<code>globus_priority_q_t</code> *priority_q, <code>globus_priority_q_cmp_func_t</code>cmp_func)</h3>
<p> Initialize a priority queue. The <code>globus_priority_q_init()</code> function initializes a globus_priority_q_t structure for use with the other functions in the <code>Priority Queue </code> module. If this function returns GLOBUS_SUCCESS, the caller is responsible for deallocating the members of this structure when it is no longer needed by passing it to <code>globus_priority_q_destroy()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>priority_q</i> Pointer to the priority queue structure to initialize.<br />
 <i>cmp_func</i> Pointer to a function which computes the relative relationship between two priorities. See the documentation of <code>globus_priority_q_cmp_func_t</code> for details on how to implement that function.</dl>
<p> <code>Return values:</code></p>
<dl>
<dt>
<dd> <i>GLOBUS_SUCCESS</i> Success<br />
 <i>GLOBUS_FAILURE</i> Failure</dl>
<h3>void* globus_priority_q_modify (<code>globus_priority_q_t</code> *priority_q, void *datum, void *new_priority)</h3>
<p> Modify the Priority of Datum. The <code>globus_priority_q_modify()</code> function modifies the priority of the highest-priority instance of datum in the priority queue so that it new_priority. The old priority of the datum is returned. If the priority_q is NULL or the datum is not present, this function returns NULL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>priority_q</i> Pointer to the priority queue to modify<br />
 <i>datum</i> Pointer to the datum whose priority is being modified<br />
 <i>new_priority</i> Pointer to the new priority</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns the old priority of datum.</dl>
<h3>void* globus_priority_q_remove (<code>globus_priority_q_t</code> *priority_q, void *datum)</h3>
<p> Remove an Arbitrary Datum from a Priority Queue. The <code>globus_priority_q_remove()</code> function removes the highest-priority instance of the specified datum from the priority queue and returns the datum if it is found. If the priority_q is NULL or the datum is not found, this function returns NULL. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>priority_q</i> Pointer to the priority queue to modify<br />
 <i>datum</i> Pointer to the datum to search for.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns datum if it was present in the priority queue</dl>
<h3>int globus_priority_q_size (<code>globus_priority_q_t</code> *priority_q)</h3>
<p> Priority Queue Size. The <code>globus_priority_q_size()</code> function returns the size of the priority queue, that is, the number of elements that are currently enqueued in it. The special value GLOBUS_FAILURE is returned if a null pointer is passed to this function. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>priority_q</i> Pointer to the priority queue to check</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> This function returns the number of elements in the queue, or GLOBUS_FAILURE if the priority_q pointer is invalid.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for globus_common from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAJ">Function Documentation</a></p>
<dd>
<dt><a href="#lbAU">Author</a></p>
<dd></dl>
