---
title: "bson_visitor_t(3)"
name: "bson_visitor_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_visitor_t/"
description: "bson_visitor_t – The bson_visitor_t structure provides a series of callbacks that can be called while iterating a BSON document. This may simplify the conversion of a bson_t to a higher level langu..."
---

<h2>NAME</h2>
<p> bson_visitor_t &#8211; The bson_visitor_t structure provides a series of callbacks that can be called while iterating a BSON document. This may simplify the conversion of a bson_t to a higher level language structure.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;bson.h&gt;
typedef struct
{
    bool (*visit_before)(const bson_iter_t *iter,
                         const char *key,
                         void *data);
    bool (*visit_after)(const bson_iter_t *iter,
                        const char *key,
                        void *data);
    void (*visit_corrupt)(const bson_iter_t *iter,
                          void *data);
    bool (*visit_double)(const bson_iter_t *iter,
                         const char *key,
                         double v_double,
                         void *data);
    bool (*visit_utf8)(const bson_iter_t *iter,
                       const char *key,
                       size_t v_utf8_len,
                       const char *v_utf8,
                       void *data);
    bool (*visit_document)(const bson_iter_t *iter,
                           const char *key,
                           const bson_t *v_document,
                           void *data);
    bool (*visit_array)(const bson_iter_t *iter,
                        const char *key,
                        const bson_t *v_array,
                        void *data);
    bool (*visit_binary)(const bson_iter_t *iter,
                         const char *key,
                         bson_subtype_t v_subtype,
                         size_t v_binary_len,
                         const uint8_t *v_binary,
                         void *data);
    bool (*visit_undefined)(const bson_iter_t *iter,
                            const char *key,
                            void *data);
    bool (*visit_oid)(const bson_iter_t *iter,
                      const char *key,
                      const bson_oid_t *v_oid,
                      void *data);
    bool (*visit_bool)(const bson_iter_t *iter,
                       const char *key,
                       bool v_bool,
                       void *data);
    bool (*visit_date_time)(const bson_iter_t *iter,
                            const char *key,
                            int64_t msec_since_epoch,
                            void *data);
    bool (*visit_null)(const bson_iter_t *iter,
                       const char *key,
                       void *data);
    bool (*visit_regex)(const bson_iter_t *iter,
                        const char *key,
                        const char *v_regex,
                        const char *v_options,
                        void *data);
    bool (*visit_dbpointer)(const bson_iter_t *iter,
                            const char *key,
                            size_t v_collection_len,
                            const char *v_collection,
                            const bson_oid_t *v_oid,
                            void *data);
    bool (*visit_code)(const bson_iter_t *iter,
                       const char *key,
                       size_t v_code_len,
                       const char *v_code,
                       void *data);
    bool (*visit_symbol)(const bson_iter_t *iter,
                         const char *key,
                         size_t v_symbol_len,
                         const char *v_symbol,
                         void *data);
    bool (*visit_codewscope)(const bson_iter_t *iter,
                             const char *key,
                             size_t v_code_len,
                             const char *v_code,
                             const bson_t *v_scope,
                             void *data);
    bool (*visit_int32)(const bson_iter_t *iter,
                        const char *key,
                        int32_t v_int32,
                        void *data);
    bool (*visit_timestamp)(const bson_iter_t *iter,
                            const char *key,
                            uint32_t v_timestamp,
                            uint32_t v_increment,
                            void *data);
    bool (*visit_int64)(const bson_iter_t *iter,
                        const char *key,
                        int64_t v_int64,
                        void *data);
    bool (*visit_maxkey)(const bson_iter_t *iter,
                         const char *key,
                         void *data);
    bool (*visit_minkey)(const bson_iter_t *iter,
                         const char *key,
                         void *data);
    void *padding[9];
} bson_visitor_t;
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bson_visitor_t</code> structure provides a series of callbacks that can be called while iterating a BSON document. This may simplify the conversion of a <code>bson_t</code> to a higher level language structure. </p>
<h2>EXAMPLE</h2>
<pre><code>
#include &lt;bson.h&gt;
#include &lt;stdio.h&gt;
static bool
my_visit_before(const bson_iter_t *iter,
                const char *key,
                void *data)
{
    int *count = (int *)data;
    (*count)++;
    /* returning true stops further iteration of the document */
    return false;
}
static void
count_fields(bson_t *doc)
{
    bson_visitor_t visitor;
    bson_iter_t iter;
    int count = 0;
    visitor.visit_before = my_visit_before;
    if (bson_iter_init(&amp;iter, doc)) {
        bson_iter_visit_all(&amp;iter, &amp;visitor, &amp;count);
    }
    printf("Found %d fields.
", count);
}
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
