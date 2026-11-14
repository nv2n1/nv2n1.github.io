---
title: "sasl_listmech(3)"
name: "sasl_listmech"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sasl_listmech/"
description: "sasl_listmech – Retrieve a list of the supported SASL mechanisms"
---

<p>sasl_listmech &#8211; Retrieve a list of the supported SASL mechanisms</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sasl/sasl.h&gt;

int sasl_listmech(sasl_conn_t *conn,
                  const char *user,
                  const char *prefix,
                  const char *sep,
                  const char *suffix,
                  const char **result,
                  unsigned *plen,
                  int *pcount);</code></pre>
<h2>Description</h2>
<p><code>sasl_listmech()</code> returns a string listing the SASL names of all the mechanisms available to the specified user. This is typically given to the client through a capability command or initial server response. Client applications need this list so that they know what mechanisms the server supports. </p>
<p> <i>conn</i> the SASL context for this connection <i>user</i> (optional) restricts the mechanism list to only those available to the user. <i>prefix</i> appended to beginning of result <i>sep</i> appended between mechanisms <i>suffix</i> appended to end of result <i>result</i> NULL terminated result string (allocated/freed by library) <i>plen</i> length of result filled in by library. May be NULL <i>pcount</i> Number of mechanisms available (filled in by library). May be NULL </p>
<pre>Example:
sasl_listmech(conn,NULL,&quot;(&quot;,&quot;,&quot;,&quot;)&quot;,&amp;mechlist,NULL,NULL);
may give the string 
<code>(ANONYMOUS,KERBEROS_V4,DIGEST-MD5)</code>
as a result</pre>
<h2>Return Value</h2>
<p>Returns SASL_OK on success. SASL error code on failure. </p>
<h2>Conforming To</h2>
<p>RFC 4422</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-sasl/">sasl</a>(3), <a href="/docs/linux/man/3-sasl_errors/">sasl_errors</a>(3), <a href="/docs/linux/man/3-sasl_server_new/">sasl_server_new</a>(3), <a href="/docs/linux/man/3-sasl_client_new/">sasl_client_new</a>(3) </p>
