---
title: "bson_context_t(3)"
name: "bson_context_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_context_t/"
description: "bson_context_t – BSON OID Generation Context"
---

<h2>NAME</h2>
<p> bson_context_t &#8211; BSON OID Generation Context</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;bson.h&gt;
typedef enum {
    BSON_CONTEXT_NONE = 0,
    BSON_CONTEXT_THREAD_SAFE = (1 &lt;&lt; 0),
    BSON_CONTEXT_DISABLE_HOST_CACHE = (1 &lt;&lt; 1),
    BSON_CONTEXT_DISABLE_PID_CACHE = (1 &lt;&lt; 2),
#if defined(__linux__)
    BSON_CONTEXT_USE_TASK_ID = (1 &lt;&lt; 3),
#endif
} bson_context_flags_t;
typedef struct _bson_context_t bson_context_t;
bson_context_t *bson_context_get_default(void) BSON_GNUC_CONST;
bson_context_t *bson_context_new(bson_context_flags_t flags);
void bson_context_destroy(bson_context_t *context);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bson_context_t</code> structure is context for generation of BSON Object IDs. This context allows for specialized overriding of how ObjectIDs are generated based on the applications requirements. For example, disabling of PID caching can be configured if the application cannot detect when a call to <code><a href="/docs/linux/man/3-fork/">fork</a>(3)</code> has occurred. \&amp;.</p>
<h2>EXAMPLE</h2>
<pre><code>
#include &lt;bson.h&gt;
int main(int argc, char *argv[])
{
    bson_context_t *ctx = NULL;
    bson_oid_t oid;
    /* use default context, via bson_context_get_default() */
    bson_oid_init(&amp;oid, NULL);
    /* specify a local context for additional control */
    ctx = bson_context_new(BSON_CONTEXT_DISABLE_PID_CACHE | BSON_CONTEXT_THREAD_SAFE);
    bson_oid_init(&amp;oid, ctx);
    bson_context_destroy(ctx);
    return 0;
}
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
