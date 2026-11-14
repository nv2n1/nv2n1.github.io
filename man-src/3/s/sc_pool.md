---
title: "sc_pool(3)"
name: "sc_pool"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_pool/"
description: "sc::Pool –"
---

<p>sc::Pool &#8211;</p>
<h2>Synopsis</h2>
<h3>Public Member Functions</h3>
<pre><code>Pool(size_t)

    size_t size()

        void *allocate(size_t size)

            void release(void *d)

                double *allocate_double(size_t n)

                    void release(double *d)

                        int *allocate_int(size_t n)

                            void release(int *d)

                                void print(std::ostream &amp;o = ExEnv::out0())

                                    void check()

                                        Protected Types
    enum { freelist_size = sizeof(size_t) * 8 }

Protected Member Functions</code></pre>
<p> <code>PoolData</code> * <code>voidptr_to_pd</code> (void *d) </p>
<p> int <code>freelist_find_slot</code> (size_t) </p>
<p> void <code>freelist_add</code> (<code>PoolData</code> *) </p>
<p> void <code>freelist_del</code> (<code>PoolData</code> *)</p>
<h3>Protected Attributes</h3>
<p><code>PoolData</code> * <code>freelist_</code> [freelist_size] </p>
<p> size_t <code>size_</code> </p>
<p> <code>PoolData</code> * <code>firstdatum_</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
