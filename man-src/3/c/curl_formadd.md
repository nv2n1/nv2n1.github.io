---
title: "curl_formadd(3)"
name: "curl_formadd"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_formadd/"
description: "curl_formadd – add a section to a multipart/formdata HTTP POST"
---

<h2>NAME</h2>
<p> curl_formadd &#8211; add a section to a multipart/formdata HTTP POST</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>CURLFORMcode curl_formadd(struct curl_httppost ** </code><i>firstitem,</i> <code>struct curl_httppost ** </code><i>lastitem,</i><code> &#8230;);</code></p>
<h2>DESCRIPTION</h2>
<p> curl_formadd() is used to append sections when building a multipart/formdata HTTP POST (sometimes referred to as RFC2388-style posts). Append one section at a time until you&#8217;ve added all the sections you want included and then you pass the <i>firstitem</i> pointer as parameter to <code>CURLOPT_HTTPPOST</code>. <i>lastitem</i> is set after each <i><a href="/docs/linux/man/3-curl_formadd/">curl_formadd</a>(3)</i> call and on repeated invokes it should be left as set to allow repeated invokes to find the end of the list faster. </p>
<p> After the <i>lastitem</i> pointer follow the real arguments. </p>
<p> The pointers <i>firstitem</i> and <i>lastitem</i> should both be pointing to NULL in the first call to this function. All list-data will be allocated by the function itself. You must call <i><a href="/docs/linux/man/3-curl_formfree/">curl_formfree</a>(3)</i> on the <i>firstitemP after the form post has been done to free the resources. </p>
<p> Using POST with HTTP 1.1 implies the use of a &quot;Expect: 100-continue&quot; header. You can disable this header with CURLOPT_HTTPHEADER</i> as usual. </p>
<p> First, there are some basics you need to understand about multipart/formdata posts. Each part consists of at least a NAME and a CONTENTS part. If the part is made for file upload, there are also a stored CONTENT-TYPE and a FILENAME. Below, we&#8217;ll discuss what options you use to set these properties in the parts you want to add to your post. </p>
<p> The options listed first are for making normal parts. The options from <i>CURLFORM_FILE</i> through <i>CURLFORM_BUFFERLENGTH</i> are for file upload parts.</p>
<h2>OPTIONS</h2>
<dl>
<dt>CURLFORM_COPYNAME</dt>
<dd> followed by a string which provides the <i>name</i> of this part. libcurl copies the string so your application doesn&#8217;t need to keep it around after this function call. If the name isn&#8217;t NUL-terminated, or if you&#8217;d like it to contain zero bytes, you must set its length with <code>CURLFORM_NAMELENGTH</code>. The copied data will be freed by <i><a href="/docs/linux/man/3-curl_formfree/">curl_formfree</a>(3)</i>.</dd>
<dt>CURLFORM_PTRNAME</dt>
<dd> followed by a string which provides the <i>name</i> of this part. libcurl will use the pointer and refer to the data in your application, so you must make sure it remains until curl no longer needs it. If the name isn&#8217;t NUL-terminated, or if you&#8217;d like it to contain zero bytes, you must set its length with <code>CURLFORM_NAMELENGTH</code>.</dd>
<dt>CURLFORM_COPYCONTENTS</dt>
<dd> followed by a pointer to the contents of this part, the actual data to send away. libcurl copies the provided data, so your application doesn&#8217;t need to keep it around after this function call. If the data isn&#8217;t null terminated, or if you&#8217;d like it to contain zero bytes, you must set the length of the name with <code>CURLFORM_CONTENTSLENGTH</code>. The copied data will be freed by <i><a href="/docs/linux/man/3-curl_formfree/">curl_formfree</a>(3)</i>.</dd>
<dt>CURLFORM_PTRCONTENTS</dt>
<dd> followed by a pointer to the contents of this part, the actual data to send away. libcurl will use the pointer and refer to the data in your application, so you must make sure it remains until curl no longer needs it. If the data isn&#8217;t NUL-terminated, or if you&#8217;d like it to contain zero bytes, you must set its length with <code>CURLFORM_CONTENTSLENGTH</code>.</dd>
<dt>CURLFORM_CONTENTSLENGTH</dt>
<dd> followed by a long giving the length of the contents. Note that for <i>CURLFORM_STREAM</i> contents, this option is mandatory.</dd>
<dt>CURLFORM_FILECONTENT</dt>
<dd> followed by a filename, causes that file to be read and its contents used as data in this part. This part does <i>not</i> automatically become a file upload part simply because its data was read from a file.</dd>
<dt>CURLFORM_FILE</dt>
<dd> followed by a filename, makes this part a file upload part. It sets the <i>filename</i> field to the basename of the provided filename, it reads the contents of the file and passes them as data and sets the content-type if the given file match one of the internally known file extensions. For <code>CURLFORM_FILE</code> the user may send one or more files in one part by providing multiple <code>CURLFORM_FILE</code> arguments each followed by the filename (and each <i>CURLFORM_FILE</i> is allowed to have a <i>CURLFORM_CONTENTTYPE</i>).</dd>
<dt>CURLFORM_CONTENTTYPE</dt>
<dd> is used in combination with <i>CURLFORM_FILE</i>. Followed by a pointer to a string which provides the content-type for this part, possibly instead of an internally chosen one.</dd>
<dt>CURLFORM_FILENAME</dt>
<dd> is used in combination with <i>CURLFORM_FILE</i>. Followed by a pointer to a string, it tells libcurl to use the given string as the <i>filename</i> in the file upload part instead of the actual file name.</dd>
<dt>CURLFORM_BUFFER</dt>
<dd> is used for custom file upload parts without use of <i>CURLFORM_FILE</i>. It tells libcurl that the file contents are already present in a buffer. The parameter is a string which provides the <i>filename</i> field in the content header.</dd>
<dt>CURLFORM_BUFFERPTR</dt>
<dd> is used in combination with <i>CURLFORM_BUFFER</i>. The parameter is a pointer to the buffer to be uploaded. This buffer must not be freed until after <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i> is called. You must also use <i>CURLFORM_BUFFERLENGTH</i> to set the number of bytes in the buffer.</dd>
<dt>CURLFORM_BUFFERLENGTH</dt>
<dd> is used in combination with <i>CURLFORM_BUFFER</i>. The parameter is a long which gives the length of the buffer.</dd>
<dt>CURLFORM_STREAM</dt>
<dd> Tells libcurl to use the <i>CURLOPT_READFUNCTION</i> callback to get data. The parameter you pass to <i>CURLFORM_STREAM</i> is the pointer passed on to the read callback&#8217;s fourth argument. If you want the part to look like a file upload one, set the <i>CURLFORM_FILENAME</i> parameter as well. Note that when using <i>CURLFORM_STREAM</i>, <i>CURLFORM_CONTENTSLENGTH</i> must also be set with the total expected length of the part. (Option added in libcurl 7.18.2)</dd>
<dt>CURLFORM_ARRAY</dt>
<dd> Another possibility to send options to curl_formadd() is the <code>CURLFORM_ARRAY</code> option, that passes a struct curl_forms array pointer as its value. Each curl_forms structure element has a CURLformoption and a char pointer. The final element in the array must be a CURLFORM_END. All available options can be used in an array, except the CURLFORM_ARRAY option itself! The last argument in such an array must always be <code>CURLFORM_END</code>.</dd>
<dt>CURLFORM_CONTENTHEADER</dt>
<dd> specifies extra headers for the form POST section. This takes a curl_slist prepared in the usual way using <code>curl_slist_append</code> and appends the list of headers to those libcurl automatically generates. The list must exist while the POST occurs, if you free it before the post completes you may experience problems. </dd>
<p> When you&#8217;ve passed the HttpPost pointer to <i><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a>(3)</i> (using the <i>CURLOPT_HTTPPOST</i> option), you must not free the list until after you&#8217;ve called <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i> for the curl handle. </p>
<p> See example below.</dl>
<h2>RETURN VALUE</h2>
<p> 0 means everything was ok, non-zero means an error occurred corresponding to a CURL_FORMADD_* constant defined in <i>&lt;curl/curl.h&gt;</i></p>
<h2>EXAMPLE</h2>
<pre><code>
struct curl_httppost *post = NULL;
struct curl_httppost *last = NULL;
char namebuffer[] = "name buffer";
long namelength = strlen(namebuffer);
char buffer[] = "test buffer";
char htmlbuffer[] = "&lt;HTML&gt;test buffer&lt;/HTML&gt;";
long htmlbufferlength = strlen(htmlbuffer);
struct curl_forms forms[3];
char file1[] = "my-face.jpg";
char file2[] = "your-face.jpg";
/* add null character into htmlbuffer, to demonstrate that
   transfers of buffers containing null characters actually work
*/
htmlbuffer[8] = '</code>\0';
 /* Add simple name/content section */
 curl_formadd(&amp;post, &amp;last, CURLFORM_COPYNAME, &quot;name&quot;,
              CURLFORM_COPYCONTENTS, &quot;content&quot;, CURLFORM_END);
 /* Add simple name/content/contenttype section */
 curl_formadd(&amp;post, &amp;last, CURLFORM_COPYNAME, &quot;htmlcode&quot;,
              CURLFORM_COPYCONTENTS, &quot;&lt;HTML&gt;&lt;/HTML&gt;&quot;,
              CURLFORM_CONTENTTYPE, &quot;text/html&quot;, CURLFORM_END);
 /* Add name/ptrcontent section */
 curl_formadd(&amp;post, &amp;last, CURLFORM_COPYNAME, &quot;name_for_ptrcontent&quot;,
              CURLFORM_PTRCONTENTS, buffer, CURLFORM_END);
 /* Add ptrname/ptrcontent section */
 curl_formadd(&amp;post, &amp;last, CURLFORM_PTRNAME, namebuffer,
              CURLFORM_PTRCONTENTS, buffer, CURLFORM_NAMELENGTH,
              namelength, CURLFORM_END);
 /* Add name/ptrcontent/contenttype section */
 curl_formadd(&amp;post, &amp;last, CURLFORM_COPYNAME, &quot;html_code_with_hole&quot;,
              CURLFORM_PTRCONTENTS, htmlbuffer,
              CURLFORM_CONTENTSLENGTH, htmlbufferlength,
              CURLFORM_CONTENTTYPE, &quot;text/html&quot;, CURLFORM_END);
 /* Add simple file section */
 curl_formadd(&amp;post, &amp;last, CURLFORM_COPYNAME, &quot;picture&quot;,
              CURLFORM_FILE, &quot;my-face.jpg&quot;, CURLFORM_END);
 /* Add file/contenttype section */
 curl_formadd(&amp;post, &amp;last, CURLFORM_COPYNAME, &quot;picture&quot;,
              CURLFORM_FILE, &quot;my-face.jpg&quot;,
              CURLFORM_CONTENTTYPE, &quot;image/jpeg&quot;, CURLFORM_END);
 /* Add two file section */
 curl_formadd(&amp;post, &amp;last, CURLFORM_COPYNAME, &quot;pictures&quot;,
              CURLFORM_FILE, &quot;my-face.jpg&quot;,
              CURLFORM_FILE, &quot;your-face.jpg&quot;, CURLFORM_END);
 /* Add two file section using CURLFORM_ARRAY */
 forms[0].option = CURLFORM_FILE;
 forms[0].value = file1;
 forms[1].option = CURLFORM_FILE;
 forms[1].value = file2;
 forms[2].option = CURLFORM_END;
 /* Add a buffer to upload */
 curl_formadd(&amp;post, &amp;last,
              CURLFORM_COPYNAME, &quot;name&quot;,
              CURLFORM_BUFFER, &quot;data&quot;,
              CURLFORM_BUFFERPTR, record,
              CURLFORM_BUFFERLENGTH, record_length,
              CURLFORM_END);
 /* no option needed for the end marker */
 curl_formadd(&amp;post, &amp;last, CURLFORM_COPYNAME, &quot;pictures&quot;,
              CURLFORM_ARRAY, forms, CURLFORM_END);
 /* Add the content of a file as a normal post text value */
 curl_formadd(&amp;post, &amp;last, CURLFORM_COPYNAME, &quot;filecontent&quot;,
              CURLFORM_FILECONTENT, &quot;.bashrc&quot;, CURLFORM_END);
 /* Set the form info */
 curl_easy_setopt(curl, CURLOPT_HTTPPOST, post);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_easy_setopt/">curl_easy_setopt</a></code>(3), <code><a href="/docs/linux/man/3-curl_formfree/">curl_formfree</a></code>(3) </p>
