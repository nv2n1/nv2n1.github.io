---
title: "ne_status(3)"
name: "ne_status"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_status/"
description: "ne_status – HTTP status structure"
---

<p>ne_status &#8211; HTTP status structure</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_utils.h&gt;

typedef struct {
    int major_version, minor_version;
    int code, klass;
    const char *reason_phrase;
} ne_status;</code></pre>
<h2>Description</h2>
<p>An <code>ne_status</code> type represents an HTTP response status; used in response messages giving a result of request. The <i>major_version</i> and <i>minor_version</i> fields give the HTTP version supported by the server issuing the response. The <i>code</i> field gives the status code of the result (lying between 100 and 999 inclusive), and the <i>klass</i> field gives the class<font SIZE="-2">[1]</font>, which is equal to the most significant digit of the status. </p>
<p> There are five classes of HTTP status code defined by RFC2616: </p>
<p> 1xx</p>
<dl>
<dd>Informational response.</dl>
<p> 2xx</p>
<dl>
<dd>Success: the operation was successful</dl>
<p> 3xx</p>
<dl>
<dd>Redirection</dl>
<p> 4xx</p>
<dl>
<dd>Client error: the request made was incorrect in some manner.</dl>
<p> 5xx</p>
<dl>
<dd>Server error</dl>
<h2>See Also</h2>
<p>ne_get_status.</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>the field is named &#8220;klass&#8221; not &#8220;class&#8221; so that the header can be used from a C++ program, in which &#8220;class&#8221; is a reserved word) </p>
