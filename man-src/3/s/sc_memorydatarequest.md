---
title: "sc_memorydatarequest(3)"
name: "sc_memorydatarequest"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_memorydatarequest/"
---

sc::MemoryDataRequest -

<h2>Synopsis</h2>



<h3>Public Types</h3>

<pre><code>enum { NData = 6 }

enum Request { Deactivate,
               Sync,
               Retrieve,
               Replace,
               DoubleSum }

Public Member Functions
MemoryDataRequest(Request r, int node = 0, int offset = 0, int size = 0, int lock = 0, int serial = 0)

    void assign(Request r, int node, int offset, int size, int lock, int serial)

        void *data() const

    int nbytes() const

    const char *request_string() const

    MemoryDataRequest::Request request() const

    int node() const

    int offset() const

    int size() const

    int serial_number() const

    int lock() const

    int touches_data() const

    int reactivate() const

    void
    operator=(const MemoryDataRequest &amp;r)

        void print(const char *msg = 0, std::ostream &amp;o = ExEnv::out0()) const
</code></pre>

<h2>Author</h2>

Generated automatically by Doxygen for MPQC from the source code.
