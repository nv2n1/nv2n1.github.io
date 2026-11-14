---
title: "globus_list-h(3)"
name: "globus_list-h"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_list-h/"
description: "globus_list.h –"
---

<p>globus_list.h &#8211; </p>
<p> Linked List.</p>
<h2>Synopsis</h2>
<h3>Data Structures</h3>
<p>struct <code>globus_list</code><br />
 <i>List data type. </i></p>
<h3>Typedefs</h3>
<p>typedef struct <code>globus_list</code> <code>globus_list_t</code><br />
 <i>List data type. </i><br />
 typedef int(* <code>globus_list_pred_t</code> )(void *datum, void *arg)<br />
 <i>List search predicate. </i><br />
 typedef int(* <code>globus_list_relation_t</code> )(void *low_datum, void *high_datum, void *relation_arg)<br />
 <i>Relation predicate. </i></p>
<h3>Functions</h3>
<p>int <code>globus_list_empty</code> (<code>globus_list_t</code> *head)<br />
 <i>List empty predicate. </i><br />
 void * <code>globus_list_first</code> (<code>globus_list_t</code> *head)<br />
 <i>Retrieve head datum. </i><br />
 <code>globus_list_t</code> * <code>globus_list_rest</code> (<code>globus_list_t</code> *head)<br />
 <i>Get the remainder of the list. </i><br />
 int <code>globus_list_size</code> (<code>globus_list_t</code> *head)<br />
 <i>Get the number of elements in a list. </i><br />
 void * <code>globus_list_replace_first</code> (<code>globus_list_t</code> *head, void *datum)<br />
 <i>Replace first datum. </i><br />
 <code>globus_list_t</code> * <code>globus_list_search</code> (<code>globus_list_t</code> *head, void *datum)<br />
 <i>Search a list for a datum. </i><br />
 <code>globus_list_t</code> * <code>globus_list_search_pred</code> (<code>globus_list_t</code> *head, <code>globus_list_pred_t</code> predicate, void *pred_args)<br />
 <i>Search a list with a predicate. </i><br />
 <code>globus_list_t</code> * <code>globus_list_min</code> (<code>globus_list_t</code> *head, <code>globus_list_relation_t</code> relation, void *relation_args)<br />
 <i>Find the minimum value of a list. </i><br />
 <code>globus_list_t</code> * <code>globus_list_sort</code> (<code>globus_list_t</code> *head, <code>globus_list_relation_t</code> relation, void *relation_args)<br />
 <i>Sort a list. </i><br />
 int <code>globus_list_insert</code> (<code>globus_list_t</code> *volatile *headp, void *datum)<br />
 <i>Insert an item in a list. </i><br />
 <code>globus_list_t</code> * <code>globus_list_cons</code> (void *datum, <code>globus_list_t</code> *list)<br />
 <i>List constructor. </i><br />
 <code>globus_list_t</code> * <code>globus_list_copy</code> (<code>globus_list_t</code> *head)<br />
 <i>Copy constructor. </i><br />
 void * <code>globus_list_remove</code> (<code>globus_list_t</code> *volatile *headp, <code>globus_list_t</code> *entry)<br />
 <i>Remove a datum from a list. </i><br />
 void <code>globus_list_free</code> (<code>globus_list_t</code> *head)<br />
 <i>Free a list. </i></p>
<h2>Detailed Description</h2>
<p>Linked List. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_common from the source code.</p>
