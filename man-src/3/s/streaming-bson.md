---
title: "streaming-bson(3)"
name: "streaming-bson"
section: "3"
letter: "s"
url: "/docs/linux/man/3-streaming-bson/"
description: "Streaming_BSON – None"
---

<p>Streaming_BSON &#8211; None</p>
<h2>Reading From A Bson Stream</h2>
<p><code>bson_reader_t</code> provides a convenient API to read sequential BSON documents from a file-descriptor or memory buffer. The <code><a href="/docs/linux/man/3-bson_reader_read/">bson_reader_read</a>(3)</code> function will read forward in the underlying stream and returna <code>bson_t</code> that can be inspected and iterated upon. </p>
<p> See <code><a href="/docs/linux/man/3-bson_reader_new_from_fd/">bson_reader_new_from_fd</a>(3)</code> , <code><a href="/docs/linux/man/3-bson_reader_new_from_file/">bson_reader_new_from_file</a>(3)</code> , and <code><a href="/docs/linux/man/3-bson_reader_new_from_data/">bson_reader_new_from_data</a>(3)</code> for more information.</p>
<h2>Writing A Sequence Of Bson Documents</h2>
