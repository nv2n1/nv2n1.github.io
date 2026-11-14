---
title: "auparse_feed(3)"
name: "auparse_feed"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_feed/"
description: "auparse_feed – feed data into parser"
---

<h2>NAME</h2>
<p> auparse_feed &#8211; feed data into parser</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<pre><code>
int auparse_feed(auparse_state_t *au, const char *data, size_t data_len);
</code></pre>
<dl>
<dt><i>au</i></p>
<dd> The audit parse state</p>
<dt><i>data</i></p>
<dd> a buffer of data to feed into the parser, it is <i>data_len</i> bytes long. The data is copied in the parser, upon return the caller may free or reuse the data buffer.</p>
<dt><i>data_len</i></p>
<dd> number of bytes in <i>data</i> </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <i>auparse_feed</i> supplies new data for the parser to consume. <i>auparse_init()</i> must have been called with a source type of AUSOURCE_FEED and a NULL pointer. </p>
<p> The parser consumes as much data as it can invoking a user supplied callback specified with <i>auparse_add_callback</i> with a cb_event_type of <i>AUPARSE_CB_EVENT_READY</i> each time the parser recognizes a complete event in the data stream. Data not fully parsed will persist and be prepended to the next feed data. After all data has been feed to the parser <i>auparse_flush_feed</i> should be called to signal the end of input data and flush any pending parse data through the parsing system. </p>
<h2>EXAMPLE</h2>
<pre><code>
void auparse_callback(auparse_state_t *au, auparse_cb_event_t cb_event_type,
                      void *user_data)
{
    int *event_cnt = (int *)user_data;
    if (cb_event_type == AUPARSE_CB_EVENT_READY) {
        if (auparse_first_record(au) &lt;= 0)
            return;
        printf("event: %d
", *event_cnt);
        printf("records:%d
", auparse_get_num_records(au));
        do {
            printf("fields:%d
", auparse_get_num_fields(au));
            printf("type=%d ", auparse_get_type(au));
            const au_event_t *e = auparse_get_timestamp(au);
            if (e == NULL)
                return;
            printf("event time: %u.%u:%lu
",
                   (unsigned)e-&gt;sec, e-&gt;milli, e-&gt;serial);
            auparse_first_field(au);
            do {
                printf("%s=%s (%s)
", auparse_get_field_name(au),
                       auparse_get_field_str(au),
                       auparse_interpret_field(au));
            } while (auparse_next_field(au) &gt; 0);
            printf("
");
        } while (auparse_next_record(au) &gt; 0);
        (*event_cnt)++;
    }
}
main(int argc, char **argv)
{
    char *filename = argv[1];
    FILE *fp;
    char buf[256];
    size_t len;
    int *event_cnt = malloc(sizeof(int));
    au = auparse_init(AUSOURCE_FEED, 0);
    *event_cnt = 1;
    auparse_add_callback(au, auparse_callback, event_cnt, free);
    if ((fp = fopen(filename, "r")) == NULL) {
        fprintf(stderr, "could not open '%s', %s
", filename, strerror(errno));
        return 1;
    }
    while ((len = fread(buf, 1, sizeof(buf), fp))) {
        auparse_feed(au, buf, len);
    }
    auparse_flush_feed(au);
}
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns -1 if an error occurs; otherwise, 0 for success. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_add_callback/">auparse_add_callback</a></code>(3), <code><a href="/docs/linux/man/3-auparse_flush_feed/">auparse_flush_feed</a></code>(3), <code><a href="/docs/linux/man/3-auparse_feed_age_events/">auparse_feed_age_events</a></code>(3), <code><a href="/docs/linux/man/3-auparse_feed_has_data/">auparse_feed_has_data</a></code>(3) </p>
<h2>AUTHOR</h2>
<p> John Dennis </p>
<h2>Index</h2>
