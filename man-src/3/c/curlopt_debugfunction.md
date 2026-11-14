---
title: "curlopt_debugfunction(3)"
name: "curlopt_debugfunction"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_debugfunction/"
description: "CURLOPT_DEBUGFUNCTION – debug callback"
---

<p>CURLOPT_DEBUGFUNCTION &#8211; debug callback</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
typedef enum {
 CURLINFO_TEXT = 0,
 CURLINFO_HEADER_IN, /* 1 */
 CURLINFO_HEADER_OUT, /* 2 */
 CURLINFO_DATA_IN, /* 3 */
 CURLINFO_DATA_OUT, /* 4 */
 CURLINFO_SSL_DATA_IN, /* 5 */
 CURLINFO_SSL_DATA_OUT, /* 6 */
 CURLINFO_END
} curl_infotype;
int debug_callback(CURL *handle,
 curl_infotype type,
 char *data,
 size_t size,
 void *userptr);
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_DEBUGFUNCTION,
 debug_callback);</pre>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> <i><a href="/docs/linux/man/3-curlopt_debugfunction/">CURLOPT_DEBUGFUNCTION</a>(3)</i> replaces the standard debug function used when <i><a href="/docs/linux/man/3-curlopt_verbose/">CURLOPT_VERBOSE</a>(3)</i> is in effect. This callback receives debug information, as specified in the <i>type</i> argument. This function must return 0. The <i>data</i> pointed to by the char * passed to this function WILL NOT be zero terminated, but will be exactly of the <i>size</i> as told by the <i>size</i> argument. </p>
<p> The <i>userptr</i> argument is the pointer set with <i><a href="/docs/linux/man/3-curlopt_debugdata/">CURLOPT_DEBUGDATA</a>(3)</i>. </p>
<p> Available curl_infotype values:</p>
<dl COMPACT>
<dt>CURLINFO_TEXT</p>
<dd>The data is informational text.</p>
<dt>CURLINFO_HEADER_IN</p>
<dd>The data is header (or header-like) data received from the peer.</p>
<dt>CURLINFO_HEADER_OUT</p>
<dd>The data is header (or header-like) data sent to the peer.</p>
<dt>CURLINFO_DATA_IN</p>
<dd>The data is protocol data received from the peer.</p>
<dt>CURLINFO_DATA_OUT</p>
<dd>The data is protocol data sent to the peer.</p>
<dt>CURLINFO_SSL_DATA_OUT</p>
<dd>The data is SSL/TLS (binary) data sent to the peer.</p>
<dt>CURLINFO_SSL_DATA_IN</p>
<dd>The data is SSL/TLS (binary) data received from the peer.</dl>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>All</p>
<h2>Example</h2>
<pre>static
void dump(const char *text,
 FILE *stream, unsigned char *ptr, size_t size)
{
 size_t i;
 size_t c;
 unsigned int width=0x10;
 fprintf(stream, &quot;%s, %10.10ld bytes (0x%8.8lx),
 text, (long)size, (long)size);
 for(i=0; i&lt;size; i+= width) {
 fprintf(stream, &quot;%4.4lx: &quot;, (long)i);
 /* show hex to the left */
 for(c = 0; c &lt; width; c++) {
 if(i+c &lt; size)
 fprintf(stream, &quot;%02x &quot;, ptr[i+c]);
 else
 fputs(&quot; &quot;, stream);
 }
 /* show data on the right */
 for(c = 0; (c &lt; width) &amp;&amp; (i+c &lt; size); c++)
 fputc(ptr[i+c]&gt;=0x20) &amp;&amp; (ptr[i+c]&lt;0x80)?ptr[i+c]:'.', stream);
 fputc(', stream); /* newline */
 }
}
static
int my_trace(CURL *handle, curl_infotype type,
 char *data, size_t size,
 void *userp)
{
 const char *text;
 (void)handle; /* prevent compiler warning */
 switch (type) {
 case CURLINFO_TEXT:
 fprintf(stderr, &quot;== Info: %s&quot;, data);
 default: /* in case a new one is introduced to shock us */
 return 0;
 case CURLINFO_HEADER_OUT:
 text = &quot;=&gt; Send header&quot;;
 break;
 case CURLINFO_DATA_OUT:
 text = &quot;=&gt; Send data&quot;;
 break;
 case CURLINFO_SSL_DATA_OUT:
 text = &quot;=&gt; Send SSL data&quot;;
 break;
 case CURLINFO_HEADER_IN:
 text = &quot;&lt;= Recv header&quot;;
 break;
 case CURLINFO_DATA_IN:
 text = &quot;&lt;= Recv data&quot;;
 break;
 case CURLINFO_SSL_DATA_IN:
 text = &quot;&lt;= Recv SSL data&quot;;
 break;
 }
 dump(text, stderr, (unsigned char *)data, size);
 return 0;
}
int main(void)
{
 CURL *curl;
 CURLcode res;
 curl = curl_easy_init();
 if(curl) {
 curl_easy_setopt(curl, CURLOPT_DEBUGFUNCTION, my_trace);
 /* the DEBUGFUNCTION has no effect until we enable VERBOSE */
 curl_easy_setopt(curl, CURLOPT_VERBOSE, 1L);
 /* example.com is redirected, so we tell libcurl to follow redirection */
 curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
 curl_easy_setopt(curl, CURLOPT_URL, &quot;<a rel="nofollow" href="http://example.com/">http://example.com/</a>&quot;);
 res = curl_easy_perform(curl);
 /* Check for errors */
 if(res != CURLE_OK)
 fprintf(stderr, &quot;curl_easy_perform() failed: %s,
 curl_easy_strerror(res));
 /* always cleanup */
 curl_easy_cleanup(curl);
 }
 return 0;
}</pre>
<h2>Availability</h2>
<p>Always</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_verbose/">CURLOPT_VERBOSE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_debugdata/">CURLOPT_DEBUGDATA</a></code>(3),</p>
