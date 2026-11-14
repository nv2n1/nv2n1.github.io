---
title: "tst(3)"
name: "tst"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tst/"
description: "tst – ternary search trie functions"
---

<p>tst &#8211; ternary search trie functions</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;inn/tst.h&gt;

struct tst;

struct tst *tst_init(int node_line_width);

void tst_cleanup(struct tst *tst);

int tst_insert(struct tst *tst, const unsigned char *key, void *data, int option, void **exist_ptr);

void *tst_search(struct tst *tst, const unsigned char *key);

void *tst_delete(struct tst *tst, const unsigned char *key);</code></pre>
<h2>Description</h2>
<p><code>tst_init</code> allocates memory for members of <i>struct tst</i>, and allocates the first <i>node_line_width</i> nodes. A <font SIZE="-1">NULL</font> pointer is returned by <code>tst_init</code> if any part of the memory allocation fails. On success, a pointer to a <i>struct tst</i> is returned. </p>
<p> The value for <i>node_line_width</i> must be chosen very carefully. One node is required for every character in the tree. If you choose a value that is too small, your application will spend too much time calling <i><a href="/docs/linux/man/3-malloc/">malloc</a></i>(3) and your node space will be too spread out. Too large a value is just a waste of space. </p>
<p> <code>tst_cleanup</code> frees all memory allocated to nodes, internal structures, as well as <i>tst</i> itself. </p>
<p> <code>tst_insert</code> inserts the string <i>key</i> into the tree. Behavior when a duplicate key is inserted is controlled by <i>option</i>. If <i>key</i> is already in the tree then <font SIZE="-1"><code>TST_DUPLICATE_KEY</code></font> is returned, and the data pointer for the existing key is placed in <i>exist_ptr</i>. If <i>option</i> is set to <font SIZE="-1"><code>TST_REPLACE</code></font> then the existing data pointer for the existing key is replaced by <i>data</i>. Note that the old data pointer will still be placed in <i>exist_ptr</i>. </p>
<p> If a duplicate key is encountered and <i>option</i> is not set to <font SIZE="-1"><code>TST_REPLACE</code></font> then <font SIZE="-1"><code>TST_DUPLICATE_KEY</code></font> is returned. If <i>key</i> is zero length then <font SIZE="-1"><code>TST_NULL_KEY</code></font> is returned. A successful insert or replace returns <font SIZE="-1"><code>TST_OK</code></font>. A return value of <font SIZE="-1"><code>TST_ERROR</code></font> indicates that a memory allocation error occurred while trying to grow the node free. </p>
<p> Note that the <i>data</i> argument must never be <font SIZE="-1"><code>NULL</code></font>. If it is, then calls to <code>tst_search</code> will fail for a key that exists because the data value was set to <font SIZE="-1"><code>NULL</code></font>, which is what <code>tst_search</code> returns. If you just want a simple existence tree, use the <code>tst</code> pointer as the data pointer. </p>
<p> <code>tst_search</code> finds the string <i>key</i> in the tree if it exists and returns the data pointer associated with that key. </p>
<p> If <i>key</i> is not found then <font SIZE="-1"><code>NULL</code></font> is returned, otherwise the data pointer associated with <i>key</i> is returned. </p>
<p> <code>tst_delete</code> deletes the string <i>key</i> from the tree if it exists and returns the data pointer assocaited with that key. </p>
<p> If <i>key</i> is not found then <font SIZE="-1"><code>NULL</code></font> is returned, otherwise the data pointer associated with <i>key</i> is returned.</p>
<h2>History</h2>
<p>Converted to <font SIZE="-1">POD</font> from Peter A. Friend&#8217;s ternary search trie documentation by Alex Kiernan &lt;alex.kiernan [at] thus.net&gt; for InterNetNews 2.4.0. </p>
<p> <tt>$Id:</tt> tst.pod 9074 2010-05-31 19:01:32Z iulius $</p>
