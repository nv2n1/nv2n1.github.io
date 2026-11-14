---
title: "sc_pooldata(3)"
name: "sc_pooldata"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_pooldata/"
---

sc::PoolData -

<h2>Synopsis</h2>



<h3>Public Types</h3>

<pre><code>enum { magic = 0x1f1d1e1c }

Public Member Functions
PoolData(size_t size)

    PoolData *next()

        PoolData *prev()

            void next(PoolData *)

                void prev(PoolData *)

                    void prev_next(PoolData *, PoolData *)

                        PoolData *next_free()

                            PoolData *prev_free()

                                void next_free(PoolData *)

                                    void prev_free(PoolData *)

                                        void prev_next_free(PoolData *, PoolData *)

                                            void set_magic(int = magic)

                                                void *data()

                                                    void check(void *lower = (void *)0x0, void *upper = (void *)0x7fffffffL)

                                                        Public Attributes
    int magic_

    size_t size_

    unsigned int free_ : 1

    unsigned int flags_ : 15

    union {

    FreeData f

        UsedData u
};
</code></pre>

<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
