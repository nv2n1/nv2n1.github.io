---
title: "struct_rs_control(9)"
name: "struct_rs_control"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_rs_control/"
description: "struct_rs_control – rs control structure"
---

<p>struct_rs_control &#8211; rs control structure</p>
<h2>Synopsis</h2>
<pre><code>struct rs_control {
    int mm;
    int nn;
    uint16_t *alpha_to;
    uint16_t *index_of;
    uint16_t *genpoly;
    int nroots;
    int fcr;
    int prim;
    int iprim;
    int gfpoly;
    int (*gffunc)(int);
    int users;
    struct list_head list;
};</code></pre>
<h2>Members</h2>
<p>mm</p>
<dl>
<dd>Bits per symbol</dl>
<p> nn</p>
<dl>
<dd>Symbols per block (= (1&lt;&lt;mm)-1)</dl>
<p> alpha_to</p>
<dl>
<dd>log lookup table</dl>
<p> index_of</p>
<dl>
<dd>Antilog lookup table</dl>
<p> genpoly</p>
<dl>
<dd>Generator polynomial</dl>
<p> nroots</p>
<dl>
<dd>Number of generator roots = number of parity symbols</dl>
<p> fcr</p>
<dl>
<dd>First consecutive root, index form</dl>
<p> prim</p>
<dl>
<dd>Primitive element, index form</dl>
<p> iprim</p>
<dl>
<dd>prim-th root of 1, index form</dl>
<p> gfpoly</p>
<dl>
<dd>The primitive generator polynominal</dl>
<p> gffunc</p>
<dl>
<dd>Function to generate the field, if non-canonical representation</dl>
<p> users</p>
<dl>
<dd>Users of this structure</dl>
<p> list</p>
<dl>
<dd>List entry for the rs control list</dl>
<h2>Author</h2>
<p><code>Thomas Gleixner</code> &lt;tglx [at] linutronix.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
