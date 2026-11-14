---
title: "qbatomic-h(3)"
name: "qbatomic-h"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qbatomic-h/"
description: "qbatomic.h –"
---

<p>qbatomic.h &#8211; </p>
<p> Basic atomic integer and pointer operations.</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;stdint.h&gt;

#include &lt;qb/qbdefs.h&gt;

#include &lt;qb/qbconfig.h&gt;</code></pre>
<h3>Macros</h3>
<pre><code>#define qb_atomic_int_get(atomic)



#define qb_atomic_int_set(atomic, newval)



#define qb_atomic_pointer_get(atomic)



#define qb_atomic_pointer_set(atomic, newval)



#define qb_atomic_int_inc(atomic)   (qb_atomic_int_add ((atomic), 1))


Atomically increments the integer pointed to by atomic by 1.


#define qb_atomic_int_dec_and_test(atomic)   (qb_atomic_int_exchange_and_add ((atomic), -1) == 1)


Atomically decrements the integer pointed to by atomic by 1.



Functions</code></pre>
<p> void <code>qb_atomic_init</code> (void) </p>
<p> int32_t <code>qb_atomic_int_exchange_and_add</code> (volatile int32_t <code>QB_GNUC_MAY_ALIAS</code> *atomic, int32_t val)<br />
 <i>Atomically adds val to the integer pointed to by atomic. </i><br />
 void <code>qb_atomic_int_add</code> (volatile int32_t <code>QB_GNUC_MAY_ALIAS</code> *atomic, int32_t val)<br />
 <i>Atomically adds val to the integer pointed to by atomic. </i><br />
 int32_t <code>qb_atomic_int_compare_and_exchange</code> (volatile int32_t <code>QB_GNUC_MAY_ALIAS</code> *atomic, int32_t oldval, int32_t newval)<br />
 <i>Compares oldval with the integer pointed to by atomic and if they are equal, atomically exchanges *atomic with newval. </i><br />
 int32_t <code>qb_atomic_pointer_compare_and_exchange</code> (volatile void *<code>QB_GNUC_MAY_ALIAS</code> *atomic, void *oldval, void *newval)<br />
 <i>Compares oldval with the pointer pointed to by atomic and if they are equal, atomically exchanges *atomic with newval. </i><br />
 int32_t <code>qb_atomic_int_get</code> (volatile int32_t <code>QB_GNUC_MAY_ALIAS</code> *atomic)<br />
 <i>Reads the value of the integer pointed to by atomic. </i><br />
 void <code>qb_atomic_int_set</code> (volatile int32_t <code>QB_GNUC_MAY_ALIAS</code> *atomic, int32_t newval)<br />
 <i>Sets the value of the integer pointed to by atomic. </i><br />
 void * <code>qb_atomic_pointer_get</code> (volatile void *<code>QB_GNUC_MAY_ALIAS</code> *atomic)<br />
 <i>Reads the value of the pointer pointed to by atomic. </i><br />
 void <code>qb_atomic_pointer_set</code> (volatile void *<code>QB_GNUC_MAY_ALIAS</code> *atomic, void *newval)<br />
 <i>Sets the value of the pointer pointed to by atomic. </i></p>
<h2>Detailed Description</h2>
<p>Basic atomic integer and pointer operations. </p>
<p> The following functions can be used to atomically access integers and pointers. They are implemented as inline assembler function on most platforms and use slower fall-backs otherwise. Using them can sometimes save you from using a performance-expensive pthread_mutex to protect the integer or pointer. </p>
<p> The most important usage is reference counting. Using <code>qb_atomic_int_inc()</code> and <code>qb_atomic_int_dec_and_test()</code> makes reference counting a very fast operation. </p>
<p> You must not directly read integers or pointers concurrently accessed by multiple threads, but use the atomic accessor functions instead. That is, always use <code>qb_atomic_int_get()</code> and <code>qb_atomic_pointer_get()</code> for read outs. They provide the necessary synchonization mechanisms like memory barriers to access memory locations concurrently. </p>
<p> If you are using those functions for anything apart from simple reference counting, you should really be aware of the implications of doing that. There are literally thousands of ways to shoot yourself in the foot. So if in doubt, use a pthread_mutex. If you don&#8217;t know, what memory barriers are, do not use anything but <code>qb_atomic_int_inc()</code> and <code>qb_atomic_int_dec_and_test()</code>. </p>
<p> It is not safe to set an integer or pointer just by assigning to it, when it is concurrently accessed by other threads with the following functions. Use <code>qb_atomic_int_compare_and_exchange()</code> or <code>qb_atomic_pointer_compare_and_exchange()</code> respectively.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define qb_atomic_int_dec_and_test(atomic) (<code>qb_atomic_int_exchange_and_add</code> ((atomic), -1) == 1)</h3>
<p>Atomically decrements the integer pointed to by atomic by 1. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>atomic</i> a pointer to an integer</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>QB_TRUE if the integer pointed to by atomic is 0 after decrementing it</dl>
<h3>#define qb_atomic_int_get(atomic)</h3>
<p><code>Value:</code> </p>
<pre>((void) sizeof (char* [sizeof (*(atomic)) == sizeof (int32_t) ? 1 : -1]), (qb_atomic_int_get) ((volatile int32_t QB_GNUC_MAY_ALIAS *) (volatile void *) (atomic)))</pre>
<h3>#define qb_atomic_int_inc(atomic) (<code>qb_atomic_int_add</code> ((atomic), 1))</h3>
<p>Atomically increments the integer pointed to by atomic by 1. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>atomic</i> a pointer to an integer.</dl>
<h3>#define qb_atomic_int_set(atomic, newval)</h3>
<p><code>Value:</code> </p>
<pre>((void) sizeof (char* [sizeof (*(atomic)) == sizeof (int32_t) ? 1 : -1]), (qb_atomic_int_set) ((volatile int32_t QB_GNUC_MAY_ALIAS *) (volatile void *) (atomic), (newval)))</pre>
<h3>#define qb_atomic_pointer_get(atomic)</h3>
<p><code>Value:</code> </p>
<pre>((void) sizeof (char* [sizeof (*(atomic)) == sizeof (void*) ? 1 : -1]), (qb_atomic_pointer_get) ((volatile void* QB_GNUC_MAY_ALIAS *) (volatile void *) (atomic)))</pre>
<h3>#define qb_atomic_pointer_set(atomic, newval)</h3>
<p><code>Value:</code> </p>
<pre>((void) sizeof (char* [sizeof (*(atomic)) == sizeof (void*) ? 1 : -1]), (qb_atomic_pointer_set) ((volatile void* QB_GNUC_MAY_ALIAS *) (volatile void *) (atomic), (newval)))</pre>
<h2>Function Documentation</h2>
<h3>void qb_atomic_init (void)</h3>
<h3>void qb_atomic_int_add (volatile int32_t <code>QB_GNUC_MAY_ALIAS</code> *atomic, int32_tval)</h3>
<p>Atomically adds val to the integer pointed to by atomic. Also acts as a memory barrier. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>atomic</i> a pointer to an integer<br />
 <i>val</i> the value to add to *atomic</dl>
<h3>int32_t qb_atomic_int_compare_and_exchange (volatile int32_t <code>QB_GNUC_MAY_ALIAS</code> *atomic, int32_toldval, int32_tnewval)</h3>
<p>Compares oldval with the integer pointed to by atomic and if they are equal, atomically exchanges *atomic with newval. Also acts as a memory barrier. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>atomic</i> a pointer to an integer<br />
 <i>oldval</i> the assumed old value of *atomic<br />
 <i>newval</i> the new value of *atomic</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>QB_TRUE, if *atomic was equal oldval. QB_FALSE otherwise.</dl>
<h3>int32_t qb_atomic_int_exchange_and_add (volatile int32_t <code>QB_GNUC_MAY_ALIAS</code> *atomic, int32_tval)</h3>
<p>Atomically adds val to the integer pointed to by atomic. It returns the value of *atomic just before the addition took place. Also acts as a memory barrier. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>atomic</i> a pointer to an integer<br />
 <i>val</i> the value to add to *atomic</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the value of *atomic before the addition.</dl>
<h3>int32_t qb_atomic_int_get (volatile int32_t <code>QB_GNUC_MAY_ALIAS</code> *atomic)</h3>
<p>Reads the value of the integer pointed to by atomic. Also acts as a memory barrier. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>atomic</i> a pointer to an integer</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the value of atomic</dl>
<h3>void qb_atomic_int_set (volatile int32_t <code>QB_GNUC_MAY_ALIAS</code> *atomic, int32_tnewval)</h3>
<p>Sets the value of the integer pointed to by atomic. Also acts as a memory barrier. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>atomic</i> a pointer to an integer<br />
 <i>newval</i> the new value</dl>
<h3>int32_t qb_atomic_pointer_compare_and_exchange (volatile void *<code>QB_GNUC_MAY_ALIAS</code> *atomic, void *oldval, void *newval)</h3>
<p>Compares oldval with the pointer pointed to by atomic and if they are equal, atomically exchanges *atomic with newval. Also acts as a memory barrier. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>atomic</i> a pointer to a void*<br />
 <i>oldval</i> the assumed old value of *atomic<br />
 <i>newval</i> the new value of *atomic</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>QB_TRUE if atomic was equal oldval, else QB_FALSE.</dl>
<h3>void* qb_atomic_pointer_get (volatile void *<code>QB_GNUC_MAY_ALIAS</code> *atomic)</h3>
<p>Reads the value of the pointer pointed to by atomic. Also acts as a memory barrier. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>atomic</i> a pointer to a void*.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the value to add to atomic.</dl>
<h3>void qb_atomic_pointer_set (volatile void *<code>QB_GNUC_MAY_ALIAS</code> *atomic, void *newval)</h3>
<p>Sets the value of the pointer pointed to by atomic. Also acts as a memory barrier. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>atomic</i> a pointer to a void*<br />
 <i>newval</i> the new value</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libqb from the source code.</p>
