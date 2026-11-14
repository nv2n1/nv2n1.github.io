---
title: "uuid_unparse(3)"
name: "uuid_unparse"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uuid_unparse/"
description: "uuid_unparse – convert a UUID from binary representation to a string"
---

<p>uuid_unparse &#8211; convert a UUID from binary representation to a string</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;uuid.h&gt;

void uuid_unparse(uuid_t uu, char *out);
void uuid_unparse_upper(uuid_t uu, char *out);
void uuid_unparse_lower(uuid_t uu, char *out);</code></pre>
<h2>Description</h2>
<p>The <code>uuid_unparse</code> function converts the supplied UUID <i>uu</i> from the binary representation into a 36-byte string (plus trailing &#8216;
