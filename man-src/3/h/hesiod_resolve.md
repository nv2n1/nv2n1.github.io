---
title: "hesiod_resolve(3)"
name: "hesiod_resolve"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hesiod_resolve/"
description: "hesiod, hesiod_init, hesiod_resolve, hesiod_free_list, hesiod_to_bind, hesiod_free_string, hesiod_end – Hesiod name server interface library"
---

<h2>NAME</h2>
<p> hesiod, hesiod_init, hesiod_resolve, hesiod_free_list, hesiod_to_bind, hesiod_free_string, hesiod_end &#8211; Hesiod name server interface library</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;hesiod.h&gt;
int hesiod_init(void **context) char **hesiod_resolve(void *context, const char *name,
                                                      const char *type) void hesiod_free_list(void *context, char **list);
char *hesiod_to_bind(void *context, const char *name,
                     const char *type) void hesiod_free_string(void *context, char *str);
char **hesiod_parse_result(void *context,
void hesiod_end(void *context)
cc file.c -lhesiod
</code></pre>
<h2>DESCRIPTION</h2>
<p> This family of functions allows you to perform lookups of Hesiod information, which is stored as text records in the Domain Name Service. To perform lookups, you must first initialize a <i>context</i>, an opaque object which stores information used internally by the library between calls. <i>hesiod_init</i> initializes a context, storing a pointer to the context in the location pointed to by the <i>context</i> argument. <i>hesiod_end</i> frees the resources used by a context. </p>
<p> <i>hesiod_resolve</i> is the primary interface to the library. If successful, it returns a list of one or more strings giving the records matching <i>name</i> and <i>type</i>. The last element of the list is followed by a NULL pointer. It is the caller&#8217;s responsibility to call <i>hesiod_free_list</i> to free the resources used by the returned list. </p>
<p> <i>hesiod_to_bind</i> converts <i>name</i> and <i>type</i> into the DNS name used by <i>hesiod_resolve</i>. It is the caller&#8217;s responsibility to free the returned string using <i>hesiod_free_string</i>. </p>
<p> <i>hesiod_parse_result</i> parses the result of a name server query into text records. It is the caller&#8217;s responsibility to call <i>hesiod_free_list</i> to free the resources used by the returned list.</p>
<h2>RETURN VALUES</h2>
<p> If successful, <i>hesiod_init</i> returns 0; otherwise it returns -1 and sets <i>errno</i> to indicate the error. On failure, <i>hesiod_resolve</i> and <i>hesiod_to_bind</i> return NULL and set the global variable <i>errno</i> to indicate the error.</p>
<h2>ENVIRONMENT</h2>
<p> If the environment variable <code>HES_DOMAIN</code> is set, it will override the domain in the Hesiod configuration file. If the environment variable <code>HESIOD_CONFIG</code> is set, it specifies the location of the Hesiod configuration file.</p>
<h2>SEE ALSO</h2>
<p> `Hesiod &#8211; Project Athena Technical Plan &#8212; Name Service&#8217;, <a href="/docs/linux/man/8-named/">named</a>(8), <a href="/docs/linux/man/5-hesiod-conf/">hesiod.conf</a>(5)</p>
<h2>ERRORS</h2>
<p> Hesiod calls may fail because of:</p>
<dl>
<dt>ENOMEM</p>
<dd> Insufficient memory was available to carry out the requested operation.</p>
<dt>ENOEXEC</p>
<dd> <i>hesiod_init</i> failed because the Hesiod configuration file was invalid.</p>
<dt>ECONNREFUSED</p>
<dd> <i>hesiod_resolve</i> failed because no name server could be contacted to answer the query.</p>
<dt>EMSGSIZE</p>
<dd> <i>hesiod_resolve</i> or <i>hesiod_to_bind</i> failed because the query or response was too big to fit into the packet buffers.</p>
<dt>ENOENT</p>
<dd> <i>hesiod_resolve</i> failed because the name server had no text records matching <i>name</i> and <i>type</i>, or <i>hesiod_to_bind</i> failed because the <i>name</i> argument had a domain extension which could not be resolved with type &#8220;rhs-extension&#8221; in the local Hesiod domain.</p>
<dt>EINVAL</p>
<dd> <i>hesiod_to_bind</i> failed to convert the resulting domain name from UTF-8 to an internationalized domain name.</dl>
<h2>AUTHOR</h2>
<p> Steve Dyer, IBM/Project Athena<br />
 Greg Hudson, MIT Team Athena<br />
 Copyright 1987, 1988, 1995, 1996, 2000 by the Massachusetts Institute of Technology.</p>
<h2>BUGS</h2>
<p> The strings corresponding to the <i>errno</i> values set by the Hesiod functions are not particularly indicative of what went wrong, especially for <i>ENOEXEC</i> and <i>ENOENT</i>. </p>
<h2>Index</h2>
