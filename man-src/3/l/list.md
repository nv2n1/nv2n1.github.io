---

title: "list(3)"
name: "list"
section: "3"
letter: "l"
url: "/docs/linux/man/3-list/"
description: "list – list routines"
---

<p> list &#8211; list routines </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;inn/list.h&gt;
struct node {
    struct node *succ;
    struct node *pred;
};
struct list {
    struct node *head;
    struct node *tail;
    struct node *tailpred;
};
void list_new(struct list *list);
struct node *list_addhead(struct list *list, struct node *node);
struct node *list_addtail(struct list *list, struct node *node);
struct node *list_head(struct list *list);
struct node *list_tail(struct list *list);
struct node *list_succ(struct node *node);
struct node *list_pred(struct node *node);
struct node *list_remhead(struct list *list);
struct node *list_remtail(struct list *list);
struct node *list_remove(struct node *node);
struct node *list_insert(struct list *list, struct node *node, struct node *pred);
bool list_isempty(struct list *list);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>list_new</code> initialises the list header <i>list</i> so as to create an empty list. </p>
<p> <code>list_addhead</code> adds <i>node</i> to the head of <i>list</i>, returning the node just added. </p>
<p> <code>list_addtail</code> adds <i>node</i> to the tail of <i>list</i>, returning the node just added. </p>
<p> <code>list_head</code> returns a pointer to the the node at the head of <i>list</i> or <code>NULL</code> if the list is empty. </p>
<p> <code>list_tail</code> returns a pointer to the the node at the tail of <i>list</i> or <code>NULL</code> if the list is empty. </p>
<p> <code>list_succ</code> returns the next (successor) node on the list after <i>node</i> or <code>NULL</code> if <i>node</i> was the final node. </p>
<p> <code>list_pred</code> returns the previous (predecessor) node on the list before <i>node</i> or <code>NULL</code> if <i>node</i> was the first node. </p>
<p> <code>list_remhead</code> removes the first node from <i>list</i> and returns it to the caller. If the list is empty <code>NULL</code> is returned. </p>
<p> <code>list_remtail</code> removes the last node from <i>list</i> and returns it to the caller. If the list is empty <code>NULL</code> is returned. </p>
<p> <code>list_remove</code> removes <i>node</i> from the list it is on and returns it to the caller. </p>
<p> <code>list_insert</code> inserts <i>node</i> onto <i>list</i> after the node <i>pred</i>. If <i>pred</i> is <code>NULL</code> then <i>node</i> is added to the head of <i>list</i>.</p>
<h2>HISTORY</h2>
<p> Written by Alex Kiernan &lt;alex.kiernan [at] thus.net&gt; for InterNetNews 2.4.0. </p>
<p> <tt>$Id:</tt> list.pod 9074 2010-05-31 19:01:32Z iulius $ </p>
