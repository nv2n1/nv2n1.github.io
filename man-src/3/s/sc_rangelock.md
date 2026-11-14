---
title: "sc_rangelock(3)"
name: "sc_rangelock"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_rangelock/"
---

sc::RangeLock -

<h2>Synopsis</h2>



<h3>Public Member Functions</h3>

<pre><code>RangeLock (Pool *pool=0)



void increment (int start, int fence)



void decrement (int start, int fence)



void set (int start, int fence, int value)



void sum (int start, int fence, int delta)



int checkeq (int start, int fence, int value)



int checkgr (int start, int fence, int value)



void check ()



void print (std::ostream &amp;o=ExEnv::out0()) const



int lockvalue (int i)
</code></pre>

<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
