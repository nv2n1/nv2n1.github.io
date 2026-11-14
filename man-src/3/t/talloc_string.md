---
title: "talloc_string(3)"
name: "talloc_string"
section: "3"
letter: "t"
url: "/docs/linux/man/3-talloc_string/"
description: "The talloc string functions. –"
---

<p>The talloc string functions. &#8211; </p>
<p> talloc string allocation and manipulation functions.</p>
<h3>Modules</h3>
<p><code>The talloc debugging support functions</code><br />
 <i>To aid memory debugging, talloc contains routines to inspect the currently allocated memory hierarchy. </i></p>
<h3>Functions</h3>
<p>char * <code>talloc_strdup</code> (const void *t, const char *p)<br />
 <i>Duplicate a string into a talloc chunk. </i><br />
 char * <code>talloc_strdup_append</code> (char *s, const char *a)<br />
 <i>Append a string to given string. </i><br />
 char * <code>talloc_strdup_append_buffer</code> (char *s, const char *a)<br />
 <i>Append a string to a given buffer. </i><br />
 char * <code>talloc_strndup</code> (const void *t, const char *p, size_t n)<br />
 <i>Duplicate a length-limited string into a talloc chunk. </i><br />
 char * <code>talloc_strndup_append</code> (char *s, const char *a, size_t n)<br />
 <i>Append at most n characters of a string to given string. </i><br />
 char * <code>talloc_strndup_append_buffer</code> (char *s, const char *a, size_t n)<br />
 <i>Append at most n characters of a string to given buffer. </i><br />
 char * <code>talloc_vasprintf</code> (const void *t, const char *fmt, va_list ap)<br />
 <i>Format a string given a va_list. </i><br />
 char * <code>talloc_vasprintf_append</code> (char *s, const char *fmt, va_list ap)<br />
 <i>Format a string given a va_list and append it to the given destination string. </i><br />
 char * <code>talloc_vasprintf_append_buffer</code> (char *s, const char *fmt, va_list ap)<br />
 <i>Format a string given a va_list and append it to the given destination buffer. </i><br />
 char * <code>talloc_asprintf</code> (const void *t, const char *fmt,&#8230;)<br />
 <i>Format a string. </i><br />
 char * <code>talloc_asprintf_append</code> (char *s, const char *fmt,&#8230;)<br />
 <i>Append a formatted string to another string. </i><br />
 char * <code>talloc_asprintf_append_buffer</code> (char *s, const char *fmt,&#8230;)<br />
 <i>Append a formatted string to another string. </i></p>
<h2>Detailed Description</h2>
<p>talloc string allocation and manipulation functions.</p>
<h2>Function Documentation</h2>
<h3>char* talloc_asprintf (const void *t, const char *fmt, &#8230;)</h3>
<p>Format a string. This function is the talloc equivalent of the C library function <a href="/docs/linux/man/3-asprintf/">asprintf</a>(3). </p>
<p> This functions sets the name of the new pointer to the new string. This is equivalent to: </p>
<pre>* talloc_set_name_const(ptr, ptr)
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>t</i> The talloc context to hang the result off.<br />
 <i>fmt</i> The format string.<br />
 <i>&#8230;</i> The parameters used to fill fmt.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The formatted string, NULL on error.</dl>
<h3>char* talloc_asprintf_append (char *s, const char *fmt, &#8230;)</h3>
<p>Append a formatted string to another string. This function appends the given formatted string to the given string. Use this variant when the string in the current talloc buffer may have been truncated in length. </p>
<p> This functions sets the name of the new pointer to the new string. This is equivalent to: </p>
<pre>* talloc_set_name_const(ptr, ptr)
* </pre>
<p>If s == NULL then new context is created. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> The string to append to.<br />
 <i>fmt</i> The format string.<br />
 <i>&#8230;</i> The parameters used to fill fmt.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The formatted string, NULL on error.</dl>
<h3>char* talloc_asprintf_append_buffer (char *s, const char *fmt, &#8230;)</h3>
<p>Append a formatted string to another string. This is a more efficient version of <code>talloc_asprintf_append()</code>. It determines the length of the destination string by the size of the talloc context. </p>
<p> Use this very carefully as it produces a different result than <code>talloc_asprintf_append()</code> when a zero character is in the middle of the destination string. </p>
<pre>* char *str_a = talloc_strdup(NULL, &quot;hello world&quot;);
* char *str_b = talloc_strdup(NULL, &quot;hello world&quot;);
* str_a[5] = str_b[5] = '&nbsp;<wbr>'
*
* char *app = talloc_asprintf_append(str_a, &quot;%s&quot;, &quot;, hello&quot;);
* char *buf = talloc_strdup_append_buffer(str_b, &quot;%s&quot;, &quot;, hello&quot;);
*
* printf(&quot;%s, app); // hello, hello (app = &quot;hello, hello&quot;)
* printf(&quot;%s, buf); // hello (buf = &quot;hello world, hello&quot;)
* </pre>
<p>If s == NULL then new context is created. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> The string to append to<br />
 <i>fmt</i> The format string.<br />
 <i>&#8230;</i> The parameters used to fill fmt.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The formatted string, NULL on error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>talloc_asprintf()</code> </p>
<p> <code>talloc_asprintf_append()</code></dl>
<h3>char* talloc_strdup (const void *t, const char *p)</h3>
<p>Duplicate a string into a talloc chunk. This function is equivalent to: </p>
<pre>* ptr = talloc_size(ctx, strlen(p)+1);
* if (ptr) memcpy(ptr, p, strlen(p)+1);
* </pre>
<p>This functions sets the name of the new pointer to the passed string. This is equivalent to: </p>
<pre>* talloc_set_name_const(ptr, ptr)
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>t</i> The talloc context to hang the result off.<br />
 <i>p</i> The string you want to duplicate.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The duplicated string, NULL on error.</dl>
<h3>char* talloc_strdup_append (char *s, const char *a)</h3>
<p>Append a string to given string. The destination string is reallocated to take strlen(s) + strlen(a) + 1 characters. </p>
<p> This functions sets the name of the new pointer to the new string. This is equivalent to: </p>
<pre>* talloc_set_name_const(ptr, ptr)
* </pre>
<p>If s == NULL then new context is created. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> The destination to append to.<br />
 <i>a</i> The string you want to append.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The concatenated strings, NULL on error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>talloc_strdup()</code> </p>
<p> <code>talloc_strdup_append_buffer()</code></dl>
<h3>char* talloc_strdup_append_buffer (char *s, const char *a)</h3>
<p>Append a string to a given buffer. This is a more efficient version of <code>talloc_strdup_append()</code>. It determines the length of the destination string by the size of the talloc context. </p>
<p> Use this very carefully as it produces a different result than <code>talloc_strdup_append()</code> when a zero character is in the middle of the destination string. </p>
<pre>* char *str_a = talloc_strdup(NULL, &quot;hello world&quot;);
* char *str_b = talloc_strdup(NULL, &quot;hello world&quot;);
* str_a[5] = str_b[5] = '&nbsp;<wbr>'
*
* char *app = talloc_strdup_append(str_a, &quot;, hello&quot;);
* char *buf = talloc_strdup_append_buffer(str_b, &quot;, hello&quot;);
*
* printf(&quot;%s, app); // hello, hello (app = &quot;hello, hello&quot;)
* printf(&quot;%s, buf); // hello (buf = &quot;hello world, hello&quot;)
* </pre>
<p>If s == NULL then new context is created. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> The destination buffer to append to.<br />
 <i>a</i> The string you want to append.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The concatenated strings, NULL on error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>talloc_strdup()</code> </p>
<p> <code>talloc_strdup_append()</code> </p>
<p> <code>talloc_array_length()</code></dl>
<h3>char* talloc_strndup (const void *t, const char *p, size_tn)</h3>
<p>Duplicate a length-limited string into a talloc chunk. This function is the talloc equivalent of the C library function <a href="/docs/linux/man/3-strndup/">strndup</a>(3). </p>
<p> This functions sets the name of the new pointer to the passed string. This is equivalent to: </p>
<pre>* talloc_set_name_const(ptr, ptr)
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>t</i> The talloc context to hang the result off.<br />
 <i>p</i> The string you want to duplicate.<br />
 <i>n</i> The maximum string length to duplicate.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The duplicated string, NULL on error.</dl>
<h3>char* talloc_strndup_append (char *s, const char *a, size_tn)</h3>
<p>Append at most n characters of a string to given string. The destination string is reallocated to take strlen(s) + strnlen(a, n) + 1 characters. </p>
<p> This functions sets the name of the new pointer to the new string. This is equivalent to: </p>
<pre>* talloc_set_name_const(ptr, ptr)
* </pre>
<p>If s == NULL then new context is created. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> The destination string to append to.<br />
 <i>a</i> The source string you want to append.<br />
 <i>n</i> The number of characters you want to append from the string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The concatenated strings, NULL on error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>talloc_strndup()</code> </p>
<p> <code>talloc_strndup_append_buffer()</code></dl>
<h3>char* talloc_strndup_append_buffer (char *s, const char *a, size_tn)</h3>
<p>Append at most n characters of a string to given buffer. This is a more efficient version of <code>talloc_strndup_append()</code>. It determines the length of the destination string by the size of the talloc context. </p>
<p> Use this very carefully as it produces a different result than <code>talloc_strndup_append()</code> when a zero character is in the middle of the destination string. </p>
<pre>* char *str_a = talloc_strdup(NULL, &quot;hello world&quot;);
* char *str_b = talloc_strdup(NULL, &quot;hello world&quot;);
* str_a[5] = str_b[5] = '&nbsp;<wbr>'
*
* char *app = talloc_strndup_append(str_a, &quot;, hello&quot;, 7);
* char *buf = talloc_strndup_append_buffer(str_b, &quot;, hello&quot;, 7);
*
* printf(&quot;%s, app); // hello, hello (app = &quot;hello, hello&quot;)
* printf(&quot;%s, buf); // hello (buf = &quot;hello world, hello&quot;)
* </pre>
<p>If s == NULL then new context is created. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> The destination buffer to append to.<br />
 <i>a</i> The source string you want to append.<br />
 <i>n</i> The number of characters you want to append from the string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The concatenated strings, NULL on error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>talloc_strndup()</code> </p>
<p> <code>talloc_strndup_append()</code> </p>
<p> <code>talloc_array_length()</code></dl>
<h3>char* talloc_vasprintf (const void *t, const char *fmt, va_listap)</h3>
<p>Format a string given a va_list. This function is the talloc equivalent of the C library function <a href="/docs/linux/man/3-vasprintf/">vasprintf</a>(3). </p>
<p> This functions sets the name of the new pointer to the new string. This is equivalent to: </p>
<pre>* talloc_set_name_const(ptr, ptr)
* </pre>
<p><code>Parameters:</code></p>
<dl>
<dd><i>t</i> The talloc context to hang the result off.<br />
 <i>fmt</i> The format string.<br />
 <i>ap</i> The parameters used to fill fmt.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The formatted string, NULL on error.</dl>
<h3>char* talloc_vasprintf_append (char *s, const char *fmt, va_listap)</h3>
<p>Format a string given a va_list and append it to the given destination string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> The destination string to append to.<br />
 <i>fmt</i> The format string.<br />
 <i>ap</i> The parameters used to fill fmt.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The formatted string, NULL on error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>talloc_vasprintf()</code></dl>
<p> Format a string given a va_list and append it to the given destination string. </p>
<p> Good for gradually accumulating output into a string buffer. Appends at the end of the string.</p>
<h3>char* talloc_vasprintf_append_buffer (char *s, const char *fmt, va_listap)</h3>
<p>Format a string given a va_list and append it to the given destination buffer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> The destination buffer to append to.<br />
 <i>fmt</i> The format string.<br />
 <i>ap</i> The parameters used to fill fmt.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>The formatted string, NULL on error.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>talloc_vasprintf()</code></dl>
<p> Format a string given a va_list and append it to the given destination buffer. </p>
<p> Always appends at the end of the talloc&#8217;ed buffer, not the end of the string.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for talloc from the source code.</p>
