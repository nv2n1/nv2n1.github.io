---
title: "qbdefs-h(3)"
name: "qbdefs-h"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qbdefs-h/"
description: "qbdefs.h –"
---

<p>qbdefs.h &#8211;</p>
<h2>Synopsis</h2>
<h3>Macros</h3>
<pre><code>#define QB_ROUNDUP(x, y)   ((((x) + ((y) - 1)) / (y)) * (y))



#define QB_ABS(i)   (((i) &lt; 0) ? -(i) : (i))



#define QB_MAX(a, b)   (((a) &gt; (b)) ? (a) : (b))



#define QB_MIN(a, b)   (((a) &lt; (b)) ? (a) : (b))



#define QB_FALSE   0



#define QB_TRUE   (!QB_FALSE)



#define qb_bit_value(bit)   (1 &lt;&lt; (bit))



#define qb_bit_set(barray, bit)   (barray |= qb_bit_value(bit))



#define qb_bit_clear(barray, bit)   (barray &amp;= ~(qb_bit_value(bit)))



#define qb_bit_is_set(barray, bit)   (barray &amp; qb_bit_value(bit))



#define qb_bit_is_clear(barray, bit)   (!(barray &amp; qb_bit_value(bit)))



#define HZ   100                       /* 10ms */



#define QB_TIME_MS_IN_SEC   1000ULL



#define QB_TIME_US_IN_SEC   1000000ULL



#define QB_TIME_NS_IN_SEC   1000000000ULL



#define QB_TIME_US_IN_MSEC   1000ULL



#define QB_TIME_NS_IN_MSEC   1000000ULL



#define QB_TIME_NS_IN_USEC   1000ULL



#define QB_GNUC_DEPRECATED



#define QB_GNUC_DEPRECATED_FOR(f)   QB_GNUC_DEPRECATED



#define QB_GNUC_MAY_ALIAS</code></pre>
<h2>Detailed Description</h2>
<p><code>Author:</code></p>
<dl>
<dd>Angus Salkeld asalkeld [at] redhat.com</dl>
<p> These are some convience macros and defines.</p>
<h2>Macro Definition Documentation</h2>
<h3>#define HZ 100<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>/* 10ms */</h3>
<h3>#define QB_ABS(i) (((i) &lt; 0) ? -(i) : (i))</h3>
<h3>#define qb_bit_clear(barray, bit) (barray &amp;= ~(<code>qb_bit_value</code>(bit)))</h3>
<h3>#define qb_bit_is_clear(barray, bit) (!(barray &amp; <code>qb_bit_value</code>(bit)))</h3>
<h3>#define qb_bit_is_set(barray, bit) (barray &amp; <code>qb_bit_value</code>(bit))</h3>
<h3>#define qb_bit_set(barray, bit) (barray |= <code>qb_bit_value</code>(bit))</h3>
<h3>#define qb_bit_value(bit) (1 &lt;&lt; (bit))</h3>
<h3>#define QB_FALSE 0</h3>
<h3>#define QB_GNUC_DEPRECATED</h3>
<h3>#define QB_GNUC_DEPRECATED_FOR(f) <code>QB_GNUC_DEPRECATED</code></h3>
<h3>#define QB_GNUC_MAY_ALIAS</h3>
<h3>#define QB_MAX(a, b) (((a) &gt; (b)) ? (a) : (b))</h3>
<h3>#define QB_MIN(a, b) (((a) &lt; (b)) ? (a) : (b))</h3>
<h3>#define QB_ROUNDUP(x, y) ((((x) + ((y) &#8211; 1)) / (y)) * (y))</h3>
<h3>#define QB_TIME_MS_IN_SEC 1000ULL</h3>
<h3>#define QB_TIME_NS_IN_MSEC 1000000ULL</h3>
<h3>#define QB_TIME_NS_IN_SEC 1000000000ULL</h3>
<h3>#define QB_TIME_NS_IN_USEC 1000ULL</h3>
<h3>#define QB_TIME_US_IN_MSEC 1000ULL</h3>
<h3>#define QB_TIME_US_IN_SEC 1000000ULL</h3>
<h3>#define QB_TRUE (!<code>QB_FALSE</code>)</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libqb from the source code.</p>
