---
title: "uuid_parse(3)"
name: "uuid_parse"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uuid_parse/"
description: "uuid_parse – convert an input UUID string into binary representation"
---

<p>uuid_parse &#8211; convert an input UUID string into binary representation</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;uuid.h&gt;

int uuid_parse(char *in, uuid_t uu);</code></pre>
<h2>Description</h2>
<p>The <code>uuid_parse</code> function converts the UUID string given by <i>in</i> into the binary representation. The input UUID is a string of the form 1b4e28ba-2fa1-11d2-883f-b9a761bde3fb (in <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3) format &quot;%08x-%04x-%04x-%04x-%012x&quot;, 36 bytes plus the trailing &#8216;
