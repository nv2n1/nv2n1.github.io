---
title: "remque(3)"
name: "remque"
section: "3"
letter: "r"
url: "/docs/linux/man/3-remque/"
description: "insque, remque – insert/remove an item from a queue"
---

<p>insque, remque &#8211; insert/remove an item from a queue</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;search.h&gt;

void insque(void *elem, void *prev);

void remque(void *elem);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>insque</code>(), <code>remque</code>():</p>
<dl>
<dd>_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE</dl>
<h2>Description</h2>
<p>The <code>insque</code>() and <code>remque</code>() functions manipulate doubly linked lists. Each element in the list is a structure of which the first two elements are a forward and a backward pointer. The linked list may be linear (i.e., NULL forward pointer at the end of the list and NULL backward pointer at the start of the list) or circular. </p>
<p> The <code>insque</code>() function inserts the element pointed to by <i>elem</i> immediately after the element pointed to by <i>prev</i>. </p>
<p> If the list is linear, then the call <i>insque(elem, NULL)</i> can be used to insert the initial list element, and the call sets the forward and backward pointers of <i>elem</i> to NULL. </p>
<p> If the list is circular, the caller should ensure that the forward and backward pointers of the first element are initialized to point to that element, and the <i>prev</i> argument of the <code>insque</code>() call should also point to the element. </p>
<p> The <code>remque</code>() function removes the element pointed to by <i>elem</i> from the doubly linked list.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>insque</code>(), <code>remque</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>On ancient systems, the arguments of these functions were of type <i>struct qelem *</i>, defined as: struct qelem {<br />
    struct qelem *q_forw;<br />
    struct qelem *q_back;<br />
    char q_data[1];<br />
}; This is still what you will get if <code>_GNU_SOURCE</code> is defined before including <i>&lt;search.h&gt;</i>. The location of the prototypes for these functions differs among several versions of UNIX. The above is the POSIX version. Some systems place them in <i>&lt;string.h&gt;</i>.</p>
<h2>Bugs</h2>
<p>In glibc 2.4 and earlier, it was not possible to specify <i>prev</i> as NULL. Consequently, to build a linear list, the caller had to build a list using an initial call that contained the first two elements of the list, with the forward and backward pointers in each element suitably initialized.</p>
<h2>Examples</h2>
<p>The program below demonstrates the use of <code>insque</code>(). Here is an example run of the program: </p>
<pre><code>$ ./a.out -c a b c

Traversing completed list:
a
b
c
That was a circular list



Program source



#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;unistd.h&gt;
#include &lt;search.h&gt;
struct element {
    struct element *forward;
    struct element *backward;
    char *name;
};
static struct element *
new_element(void)
{
    struct element *e = malloc(sizeof(*e));
    if (e == NULL) {
        fprintf(stderr, &quot;malloc() failed
&quot;);
        exit(EXIT_FAILURE);
    }
    return e;
}
int
main(int argc, char *argv[])
{
    struct element *first, *elem, *prev;
    int circular, opt, errfnd;
    /* The &quot;-c&quot; command-line option can be used to specify that the
    list is circular */
    errfnd = 0;
    circular = 0;
    while ((opt = getopt(argc, argv, &quot;c&quot;)) != -1) {
        switch (opt) {
            case 'c':
            circular = 1;
            break;
            default:
            errfnd = 1;
            break;
        }
    }
    if (errfnd || optind &gt;= argc) {
        fprintf(stderr,  &quot;Usage: %s [-c] string...
&quot;, argv[0]);
        exit(EXIT_FAILURE);
    }
    /* Create first element and place it in the linked list */
    elem = new_element();
    first = elem;
    elem-&gt;name = argv[optind];
    if (circular) {
        elem-&gt;forward = elem;
        elem-&gt;backward = elem;
        insque(elem, elem);
    } else {
        insque(elem, NULL);
    }
    /* Add remaining command-line arguments as list elements */
    while (++optind &lt; argc) {
        prev = elem;
        elem = new_element();
        elem-&gt;name = argv[optind];
        insque(elem, prev);
    }
    /* Traverse the list from the start, printing element names */
    printf(&quot;Traversing completed list:
&quot;);
    elem = first;
    do {
        printf(&quot;    %s
&quot;, elem-&gt;name);
        elem = elem-&gt;forward;
    } while (elem != NULL &amp;&amp; elem != first);
    if (elem == first)
    printf(&quot;That was a circular list
&quot;);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-queue/">queue</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
