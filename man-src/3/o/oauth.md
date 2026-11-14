---
title: "oauth(3)"
name: "oauth"
section: "3"
letter: "o"
url: "/docs/linux/man/3-oauth/"
description: "src/oauth.h –"
---

<p>src/oauth.h &#8211; </p>
<p> OAuth.net implementation in POSIX-C.</p>
<h2>Synopsis</h2>
<h3>Defines</h3>
<p> #define <code>OA_GCC_VERSION_AT_LEAST</code>(x, y) 0 </p>
<p> #define <code>attribute_deprecated</code> </p>
<h3>Enumerations</h3>
<p> enum <code>OAuthMethod</code> { <code>OA_HMAC</code> = 0, <code>OA_RSA</code>, <code>OA_PLAINTEXT</code> }<br />
 <i>signature method to used for signing the request. </i></p>
<h3>Functions</h3>
<p> char * <code>oauth_encode_base64</code> (int size, const unsigned char *src)<br />
 <i>Base64 encode and return size data in &#8216;src&#8217;. </i><br />
 int <code>oauth_decode_base64</code> (unsigned char *dest, const char *src)<br />
 <i>Decode the base64 encoded string &#8216;src&#8217; into the memory pointed to by &#8216;dest&#8217;. </i><br />
 char * <code>oauth_url_escape</code> (const char *string)<br />
 <i>Escape &#8216;string&#8217; according to RFC3986 and <a rel="nofollow" href="http://oauth.net/core/1.0/#encoding_parameters.">http://oauth.net/core/1.0/#encoding_parameters.</a> </i><br />
 char * <code>oauth_url_unescape</code> (const char *string, size_t *olen)<br />
 <i>Parse RFC3986 encoded &#8216;string&#8217; back to unescaped version. </i><br />
 char * <code>oauth_sign_hmac_sha1</code> (const char *m, const char *k)<br />
 <i>returns base64 encoded HMAC-SHA1 signature for given message and key. </i><br />
 char * <code>oauth_sign_hmac_sha1_raw</code> (const char *m, const size_t ml, const char *k, const size_t kl)<br />
 <i>same as </i><code>oauth_sign_hmac_sha1</code> but allows to specify length of message and key (in case they contain null chars).<br />
 char * <code>oauth_sign_plaintext</code> (const char *m, const char *k)<br />
 <i>returns plaintext signature for the given key. </i><br />
 char * <code>oauth_sign_rsa_sha1</code> (const char *m, const char *k)<br />
 <i>returns RSA-SHA1 signature for given data. </i><br />
 int <code>oauth_verify_rsa_sha1</code> (const char *m, const char *c, const char *s)<br />
 <i>verify RSA-SHA1 signature. </i><br />
 char * <code>oauth_catenc</code> (int len,&#8230;)<br />
 <i>url-escape strings and concatenate with &#8216;&amp;&#8217; separator. </i><br />
 int <code>oauth_split_url_parameters</code> (const char *url, char ***argv)<br />
 <i>splits the given url into a parameter array. </i><br />
 int <code>oauth_split_post_paramters</code> (const char *url, char ***argv, short qesc)<br />
 <i>splits the given url into a parameter array. </i><br />
 char * <code>oauth_serialize_url</code> (int argc, int start, char **argv)<br />
 <i>build a url query string from an array. </i><br />
 char * <code>oauth_serialize_url_sep</code> (int argc, int start, char **argv, char *sep, int mod)<br />
 <i>encode query parameters from an array. </i><br />
 char * <code>oauth_serialize_url_parameters</code> (int argc, char **argv)<br />
 <i>build a query parameter string from an array. </i><br />
 char * <code>oauth_gen_nonce</code> ()<br />
 <i>generate a random string between 15 and 32 chars length and return a pointer to it. </i><br />
 int <code>oauth_cmpstringp</code> (const void *p1, const void *p2)<br />
 <i>string compare function for oauth parameters. </i><br />
 int <code>oauth_param_exists</code> (char **argv, int argc, char *key)<br />
 <i>search array for parameter key. </i><br />
 void <code>oauth_add_param_to_array</code> (int *argcp, char ***argvp, const char *addparam)<br />
 <i>add query parameter to array </i><br />
 void <code>oauth_free_array</code> (int *argcp, char ***argvp)<br />
 <i>free array args </i><br />
 int <code>oauth_time_independent_equals_n</code> (const char *a, const char *b, size_t len_a, size_t len_b)<br />
 <i>compare two strings in constant-time (as to not let an attacker guess how many leading chars are correct: <a rel="nofollow" href="http://rdist.root.org/2010/01/07/timing-independent-array-comparison/">http://rdist.root.org/2010/01/07/timing-independent-array-comparison/</a> ) </i><br />
 int <code>oauth_time_indepenent_equals_n</code> (const char *a, const char *b, size_t len_a, size_t len_b) attribute_deprecated </p>
<p> int <code>oauth_time_independent_equals</code> (const char *a, const char *b)<br />
 <i>compare two strings in constant-time. </i><br />
 int <code>oauth_time_indepenent_equals</code> (const char *a, const char *b) attribute_deprecated </p>
<p> char * <code>oauth_sign_url2</code> (const char *url, char **postargs, <code>OAuthMethod</code> method, const char *http_method, const char *c_key, const char *c_secret, const char *t_key, const char *t_secret)<br />
 <i>calculate OAuth-signature for a given HTTP request URL, parameters and oauth-tokens. </i><br />
 char * <code>oauth_sign_url</code> (const char *url, char **postargs, <code>OAuthMethod</code> method, const char *c_key, const char *c_secret, const char *t_key, const char *t_secret) attribute_deprecated </p>
<p> void <code>oauth_sign_array2_process</code> (int *argcp, char ***argvp, char **postargs, <code>OAuthMethod</code> method, const char *http_method, const char *c_key, const char *c_secret, const char *t_key, const char *t_secret)<br />
 <i>the back-end behind by /ref oauth_sign_array2. </i><br />
 char * <code>oauth_sign_array2</code> (int *argcp, char ***argvp, char **postargs, <code>OAuthMethod</code> method, const char *http_method, const char *c_key, const char *c_secret, const char *t_key, const char *t_secret)<br />
 <i>same as /ref oauth_sign_url with the url already split into parameter array </i><br />
 char * <code>oauth_sign_array</code> (int *argcp, char ***argvp, char **postargs, <code>OAuthMethod</code> method, const char *c_key, const char *c_secret, const char *t_key, const char *t_secret) attribute_deprecated </p>
<p> char * <code>oauth_body_hash_file</code> (char *filename)<br />
 <i>calculate body hash (sha1sum) of given file and return a oauth_body_hash=xxxx parameter to be added to the request. </i><br />
 char * <code>oauth_body_hash_data</code> (size_t length, const char *data)<br />
 <i>calculate body hash (sha1sum) of given data and return a oauth_body_hash=xxxx parameter to be added to the request. </i><br />
 char * <code>oauth_body_hash_encode</code> (size_t len, unsigned char *digest)<br />
 <i>base64 encode digest, free it and return a URL parameter with the oauth_body_hash. </i><br />
 char * <code>oauth_sign_xmpp</code> (const char *xml, <code>OAuthMethod</code> method, const char *c_secret, const char *t_secret)<br />
 <i>xep-0235 &#8211; TODO </i><br />
 char * <code>oauth_http_get</code> (const char *u, const char *q)<br />
 <i>do a HTTP GET request, wait for it to finish and return the content of the reply. </i><br />
 char * <code>oauth_http_get2</code> (const char *u, const char *q, const char *customheader)<br />
 <i>do a HTTP GET request, wait for it to finish and return the content of the reply. </i><br />
 char * <code>oauth_http_post</code> (const char *u, const char *p)<br />
 <i>do a HTTP POST request, wait for it to finish and return the content of the reply. </i><br />
 char * <code>oauth_http_post2</code> (const char *u, const char *p, const char *customheader)<br />
 <i>do a HTTP POST request, wait for it to finish and return the content of the reply. </i><br />
 char * <code>oauth_post_file</code> (const char *u, const char *fn, const size_t len, const char *customheader)<br />
 <i>http post raw data from file. </i><br />
 char * <code>oauth_post_data</code> (const char *u, const char *data, size_t len, const char *customheader)<br />
 <i>http post raw data the returned string needs to be freed by the caller (requires libcurl) </i><br />
 char * <code>oauth_post_data_with_callback</code> (const char *u, const char *data, size_t len, const char *customheader, void(*callback)(void *, int, size_t, size_t), void *callback_data)<br />
 <i>http post raw data, with callback. </i><br />
 char * <code>oauth_send_data</code> (const char *u, const char *data, size_t len, const char *customheader, const char *httpMethod)<br />
 <i>http send raw data. </i><br />
 char * <code>oauth_send_data_with_callback</code> (const char *u, const char *data, size_t len, const char *customheader, void(*callback)(void *, int, size_t, size_t), void *callback_data, const char *httpMethod)<br />
 <i>http post raw data, with callback. </i></p>
<h2>Detailed Description</h2>
<p> OAuth.net implementation in POSIX-C. </p>
<p> <code>Author:</code></p>
<dl COMPACT>
<dt>
<dd> Robin Gareus &lt;robin [at] gareus.org&gt;</dl>
<p> Copyright 2007-2011 Robin Gareus &lt;robin [at] gareus.org&gt; </p>
<p> Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &#8216;Software&#8217;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: </p>
<p> The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. </p>
<p> THE SOFTWARE IS PROVIDED &#8216;AS IS&#8217;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. </p>
<p> Definition in file <code>oauth.h</code>.</p>
<h2>Define Documentation</h2>
<h3>#define attribute_deprecated</h3>
<p> Definition at line 54 of file oauth.h.</p>
<h3>#define OA_GCC_VERSION_AT_LEAST(x, y) 0</h3>
<p> Definition at line 47 of file oauth.h.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>OAuthMethod</code></h3>
<p> signature method to used for signing the request. </p>
<p> <code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>OA_HMAC </i></p>
<dd> use HMAC-SHA1 request signing method</p>
<dt><i>OA_RSA </i></p>
<dd> use RSA signature</p>
<dt><i>OA_PLAINTEXT </i></p>
<dd> use plain text signature (for testing only)</dl>
<p> Definition at line 65 of file oauth.h.</p>
<h2>Function Documentation</h2>
<h3>void oauth_add_param_to_array (int * argcp, char *** argvp, const char * addparam)</h3>
<p> add query parameter to array <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>argcp</i> pointer to array length int<br />
 <i>argvp</i> pointer to array values<br />
 <i>addparam</i> parameter to add (eg. &#8216;foo=bar&#8217;)</dl>
<h3>char* oauth_body_hash_data (size_t length, const char * data)</h3>
<p> calculate body hash (sha1sum) of given data and return a oauth_body_hash=xxxx parameter to be added to the request. The returned string needs to be freed by the calling function. The returned string is not yet url-escaped and suitable to be passed as argument to <code>oauth_catenc</code>. </p>
<p> see <a rel="nofollow" href="http://oauth.googlecode.com/svn/spec/ext/body_hash/1.0/oauth-bodyhash.html">http://oauth.googlecode.com/svn/spec/ext/body_hash/1.0/oauth-bodyhash.html</a> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>length</i> length of the data parameter in bytes<br />
 <i>data</i> to calculate the hash for</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> URL oauth_body_hash parameter string</dl>
<p> <code>Examples: </code> <code>tests/oauthbodyhash.c</code>.</p>
<h3>char* oauth_body_hash_encode (size_t len, unsigned char * digest)</h3>
<p> base64 encode digest, free it and return a URL parameter with the oauth_body_hash. The returned hash needs to be freed by the calling function. The returned string is not yet url-escaped and thus suitable to be passed to <code>oauth_catenc</code>. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>len</i> length of the digest to encode<br />
 <i>digest</i> hash value to encode</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> URL oauth_body_hash parameter string</dl>
<h3>char* oauth_body_hash_file (char * filename)</h3>
<p> calculate body hash (sha1sum) of given file and return a oauth_body_hash=xxxx parameter to be added to the request. The returned string needs to be freed by the calling function. </p>
<p> see <a rel="nofollow" href="http://oauth.googlecode.com/svn/spec/ext/body_hash/1.0/oauth-bodyhash.html">http://oauth.googlecode.com/svn/spec/ext/body_hash/1.0/oauth-bodyhash.html</a> </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>filename</i> the filename to calculate the hash for</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> URL oauth_body_hash parameter string</dl>
<p> <code>Examples: </code> <code>tests/oauthbodyhash.c</code>.</p>
<h3>char* oauth_catenc (int len, &#8230;)</h3>
<p> url-escape strings and concatenate with &#8216;&amp;&#8217; separator. The number of strings to be concatenated must be given as first argument. all arguments thereafter must be of type (char *) </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>len</i> the number of arguments to follow this parameter</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> pointer to memory holding the concatenated strings &#8211; needs to be free(d) by the caller. or NULL in case we ran out of memory.</dl>
<p> <code>Examples: </code> <code>tests/oauthbodyhash.c</code>.</p>
<h3>int oauth_cmpstringp (const void * p1, const void * p2)</h3>
<p> string compare function for oauth parameters. used with qsort. needed to normalize request parameters. see <a rel="nofollow" href="http://oauth.net/core/1.0/#anchor14">http://oauth.net/core/1.0/#anchor14</a> </p>
<p> <code>Examples: </code> <code>tests/oauthexample.c</code>, <code>tests/oauthtest.c</code>, and <code>tests/oauthtest2.c</code>.</p>
<h3>int oauth_decode_base64 (unsigned char * dest, const char * src)</h3>
<p> Decode the base64 encoded string &#8216;src&#8217; into the memory pointed to by &#8216;dest&#8217;. <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>dest</i> Pointer to memory for holding the decoded string. Must be large enough to receive the decoded string.<br />
 <i>src</i> A base64 encoded string.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the length of the decoded string if decode succeeded otherwise 0.</dl>
<h3>char* oauth_encode_base64 (int size, const unsigned char * src)</h3>
<p> Base64 encode and return size data in &#8216;src&#8217;. The caller must free the returned string. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>size</i> The size of the data in src<br />
 <i>src</i> The data to be base64 encode</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> encoded string otherwise NULL</dl>
<h3>void oauth_free_array (int * argcp, char *** argvp)</h3>
<p> free array args <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>argcp</i> pointer to array length int<br />
 <i>argvp</i> pointer to array values to be free()d</dl>
<p> <code>Examples: </code> <code>tests/oauthtest2.c</code>.</p>
<h3>char* oauth_gen_nonce ()</h3>
<p> generate a random string between 15 and 32 chars length and return a pointer to it. The value needs to be freed by the caller </p>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> zero terminated random string.</dl>
<h3>char* oauth_http_get (const char * u, const char * q)</h3>
<p> do a HTTP GET request, wait for it to finish and return the content of the reply. (requires libcurl or a command-line HTTP client) </p>
<p> If compiled <code>without</code> libcurl this function calls a command-line executable defined in the environment variable OAUTH_HTTP_GET_CMD &#8211; it defaults to curl -sA &#8216;liboauth-agent/0.1&#8217; &#8216;%u&#8217; where %u is replaced with the URL and query parameters. </p>
<p> bash &amp; wget example: export OAUTH_HTTP_CMD=&#8217;wget -q -U &#8216;liboauth-agent/0.1&#8217; &#8216;%u&#8217; &#8216; </p>
<p> WARNING: this is a tentative function. it&#8217;s convenient and handy for testing or developing OAuth code. But don&#8217;t rely on this function to become a stable part of this API. It does not do much error checking or handling for one thing.. </p>
<p> NOTE: <i>u</i> and <i>q</i> are just concatenated with a &#8216;?&#8217; in between, unless <i>q</i> is NULL. in which case only <i>u</i> will be used. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>u</i> base url to get<br />
 <i>q</i> query string to send along with the HTTP request or NULL.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> In case of an error NULL is returned; otherwise a pointer to the replied content from HTTP server. latter needs to be freed by caller.</dl>
<p> <code>Examples: </code> <code>tests/oauthexample.c</code>, and <code>tests/oauthtest.c</code>.</p>
<h3>char* oauth_http_get2 (const char * u, const char * q, const char * customheader)</h3>
<p> do a HTTP GET request, wait for it to finish and return the content of the reply. (requires libcurl) </p>
<p> This is equivalent to /ref oauth_http_get but allows to specifiy a custom HTTP header and has has no support for commandline-curl. </p>
<p> If liboauth is compiled <code>without</code> libcurl this function always returns NULL. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>u</i> base url to get<br />
 <i>q</i> query string to send along with the HTTP request or NULL.<br />
 <i>customheader</i> specify custom HTTP header (or NULL for none) Multiple header elements can be passed separating them with &#8216;
&#8217;</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> In case of an error NULL is returned; otherwise a pointer to the replied content from HTTP server. latter needs to be freed by caller.</dl>
<p> <code>Examples: </code> <code>tests/oauthtest2.c</code>.</p>
<h3>char* oauth_http_post (const char * u, const char * p)</h3>
<p> do a HTTP POST request, wait for it to finish and return the content of the reply. (requires libcurl or a command-line HTTP client) </p>
<p> If compiled <code>without</code> libcurl this function calls a command-line executable defined in the environment variable OAUTH_HTTP_CMD &#8211; it defaults to curl -sA &#8216;liboauth-agent/0.1&#8217; -d &#8216;%p&#8217; &#8216;%u&#8217; where %p is replaced with the postargs and %u is replaced with the URL. </p>
<p> bash &amp; wget example: export OAUTH_HTTP_CMD=&#8217;wget -q -U &#8216;liboauth-agent/0.1&#8242; &#8211;post-data=&#8217;%p&#8217; &#8216;%u&#8217; &#8216; </p>
<p> NOTE: This function uses the curl&#8217;s default HTTP-POST Content-Type: application/x-www-form-urlencoded which is the only option allowed by oauth core 1.0 spec. Experimental code can use the Environment variable to transmit custom HTTP headers or parameters. </p>
<p> WARNING: this is a tentative function. it&#8217;s convenient and handy for testing or developing OAuth code. But don&#8217;t rely on this function to become a stable part of this API. It does not do much error checking for one thing.. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>u</i> url to query<br />
 <i>p</i> postargs to send along with the HTTP request.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> replied content from HTTP server. needs to be freed by caller.</dl>
<p> <code>Examples: </code> <code>tests/oauthexample.c</code>, and <code>tests/oauthtest.c</code>.</p>
<h3>char* oauth_http_post2 (const char * u, const char * p, const char * customheader)</h3>
<p> do a HTTP POST request, wait for it to finish and return the content of the reply. (requires libcurl) </p>
<p> It&#8217;s equivalent to /ref oauth_http_post, but offers the possibility to specify a custom HTTP header and has no support for commandline-curl. </p>
<p> If liboauth is compiled <code>without</code> libcurl this function always returns NULL. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>u</i> url to query<br />
 <i>p</i> postargs to send along with the HTTP request.<br />
 <i>customheader</i> specify custom HTTP header (or NULL for none) Multiple header elements can be passed separating them with &#8216;
&#8217;</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> replied content from HTTP server. needs to be freed by caller.</dl>
<h3>int oauth_param_exists (char ** argv, int argc, char * key)</h3>
<p> search array for parameter key. <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>argv</i> length of array to search<br />
 <i>argc</i> parameter array to search<br />
 <i>key</i> key of parameter to check.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> FALSE (0) if array does not contain a parameter with given key, TRUE (1) otherwise.</dl>
<h3>char* oauth_post_data (const char * u, const char * data, size_t len, const char * customheader)</h3>
<p> http post raw data the returned string needs to be freed by the caller (requires libcurl) see dislaimer: /ref oauth_http_post </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>u</i> url to retrieve<br />
 <i>data</i> data to post<br />
 <i>len</i> length of the data in bytes.<br />
 <i>customheader</i> specify custom HTTP header (or NULL for default) Multiple header elements can be passed separating them with &#8216;
&#8217;</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> returned HTTP reply or NULL on error</dl>
<p> <code>Examples: </code> <code>tests/oauthbodyhash.c</code>.</p>
<h3>char* oauth_post_data_with_callback (const char * u, const char * data, size_t len, const char * customheader, void(*)(void *, int, size_t, size_t) callback, void * callback_data)</h3>
<p> http post raw data, with callback. the returned string needs to be freed by the caller (requires libcurl) </p>
<p> Invokes the callback &#8211; in no particular order &#8211; when HTTP-request status updates occur. The callback is called with: void * callback_data: supplied on function call. int type: 0=data received, 1=data sent. size_t size: amount of data received or amount of data sent so far size_t totalsize: original amount of data to send, or amount of data received </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>u</i> url to retrieve<br />
 <i>data</i> data to post along<br />
 <i>len</i> length of the file in bytes. set to &#8216;0&#8217; for autodetection<br />
 <i>customheader</i> specify custom HTTP header (or NULL for default) Multiple header elements can be passed separating them with &#8216;
&#8217;<br />
 <i>callback</i> specify the callback function<br />
 <i>callback_data</i> specify data to pass to the callback function</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> returned HTTP reply or NULL on error</dl>
<h3>char* oauth_post_file (const char * u, const char * fn, const size_t len, const char * customheader)</h3>
<p> http post raw data from file. the returned string needs to be freed by the caller (requires libcurl) </p>
<p> see dislaimer: /ref oauth_http_post </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>u</i> url to retrieve<br />
 <i>fn</i> filename of the file to post along<br />
 <i>len</i> length of the file in bytes. set to &#8216;0&#8217; for autodetection<br />
 <i>customheader</i> specify custom HTTP header (or NULL for default). Multiple header elements can be passed separating them with &#8216;
&#8217;</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> returned HTTP reply or NULL on error</dl>
<h3>char* oauth_send_data (const char * u, const char * data, size_t len, const char * customheader, const char * httpMethod)</h3>
<p> http send raw data. similar to /ref oauth_http_post but provides for specifying the HTTP request method. </p>
<p> the returned string needs to be freed by the caller (requires libcurl) </p>
<p> see dislaimer: /ref oauth_http_post </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>u</i> url to retrieve<br />
 <i>data</i> data to post<br />
 <i>len</i> length of the data in bytes.<br />
 <i>customheader</i> specify custom HTTP header (or NULL for default) Multiple header elements can be passed separating them with &#8216;
&#8217;<br />
 <i>httpMethod</i> specify http verb (&#8216;GET&#8217;/&#8217;POST&#8217;/&#8217;PUT&#8217;/&#8217;DELETE&#8217;) to be used. if httpMethod is NULL, a POST is executed.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> returned HTTP reply or NULL on error</dl>
<h3>char* oauth_send_data_with_callback (const char * u, const char * data, size_t len, const char * customheader, void(*)(void *, int, size_t, size_t) callback, void * callback_data, const char * httpMethod)</h3>
<p> http post raw data, with callback. the returned string needs to be freed by the caller (requires libcurl) </p>
<p> Invokes the callback &#8211; in no particular order &#8211; when HTTP-request status updates occur. The callback is called with: void * callback_data: supplied on function call. int type: 0=data received, 1=data sent. size_t size: amount of data received or amount of data sent so far size_t totalsize: original amount of data to send, or amount of data received </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>u</i> url to retrieve<br />
 <i>data</i> data to post along<br />
 <i>len</i> length of the file in bytes. set to &#8216;0&#8217; for autodetection<br />
 <i>customheader</i> specify custom HTTP header (or NULL for default) Multiple header elements can be passed separating them with &#8216;
&#8217;<br />
 <i>callback</i> specify the callback function<br />
 <i>callback_data</i> specify data to pass to the callback function<br />
 <i>httpMethod</i> specify http verb (&#8216;GET&#8217;/&#8217;POST&#8217;/&#8217;PUT&#8217;/&#8217;DELETE&#8217;) to be used.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> returned HTTP reply or NULL on error</dl>
<h3>char* oauth_serialize_url (int argc, int start, char ** argv)</h3>
<p> build a url query string from an array. <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>argc</i> the total number of elements in the array<br />
 <i>start</i> element in the array at which to start concatenating.<br />
 <i>argv</i> parameter-array to concatenate.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> url string needs to be freed by the caller.</dl>
<h3>char* oauth_serialize_url_parameters (int argc, char ** argv)</h3>
<p> build a query parameter string from an array. This function is a shortcut for <code>oauth_serialize_url</code> (argc, 1, argv). It strips the leading host/path, which is usually the first element when using oauth_split_url_parameters on an URL. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>argc</i> the total number of elements in the array<br />
 <i>argv</i> parameter-array to concatenate.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> url string needs to be freed by the caller.</dl>
<h3>char* oauth_serialize_url_sep (int argc, int start, char ** argv, char * sep, int mod)</h3>
<p> encode query parameters from an array. <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>argc</i> the total number of elements in the array<br />
 <i>start</i> element in the array at which to start concatenating.<br />
 <i>argv</i> parameter-array to concatenate.<br />
 <i>sep</i> separator for parameters (usually &#8216;&amp;&#8217;)<br />
 <i>mod</i> &#8211; bitwise modifiers: 1: skip all values that start with &#8216;oauth_&#8217; 2: skip all values that don&#8217;t start with &#8216;oauth_&#8217; 4: double quotation marks are added around values (use with sep &#8216;, &#8216; for HTTP Authorization header).</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> url string needs to be freed by the caller.</dl>
<p> <code>Examples: </code> <code>tests/oauthtest2.c</code>.</p>
<h3>char* oauth_sign_array (int * argcp, char *** argvp, char ** postargs, <code>OAuthMethod</code> method, const char * c_key, const char * c_secret, const char * t_key, const char * t_secret)<code>Deprecated</code></h3>
<dl COMPACT>
<dt>
<dd> Use <code>oauth_sign_array2()</code> instead.</dl>
<h3>char* oauth_sign_array2 (int * argcp, char *** argvp, char ** postargs, <code>OAuthMethod</code> method, const char * http_method, const char * c_key, const char * c_secret, const char * t_key, const char * t_secret)</h3>
<p> same as /ref oauth_sign_url with the url already split into parameter array <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>argcp</i> pointer to array length int<br />
 <i>argvp</i> pointer to array values (argv[0]=&#8217;<a rel="nofollow" href="http://example.org:80/'">http://example.org:80/&#8217;</a> argv[1]=&#8217;first=QueryParamater&#8217; .. the array is modified: fi. oauth_ parameters are added) These arrays can be generated with /ref oauth_split_url_parameters or /ref oauth_split_post_paramters.<br />
 <i>postargs</i> This parameter points to an area where the return value is stored. If &#8216;postargs&#8217; is NULL, no value is stored.<br />
 <i>method</i> specify the signature method to use. It is of type <code>OAuthMethod</code> and most likely <code>OA_HMAC</code>.<br />
 <i>http_method</i> The HTTP request method to use (ie &#8216;GET&#8217;, &#8216;PUT&#8217;,..) If NULL is given as &#8216;http_method&#8217; this defaults to &#8216;GET&#8217; when &#8216;postargs&#8217; is also NULL and when postargs is not NULL &#8216;POST&#8217; is used.<br />
 <i>c_key</i> consumer key<br />
 <i>c_secret</i> consumer secret<br />
 <i>t_key</i> token key<br />
 <i>t_secret</i> token secret</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the signed url or NULL if an error occurred.</dl>
<h3>void oauth_sign_array2_process (int * argcp, char *** argvp, char ** postargs, <code>OAuthMethod</code> method, const char * http_method, const char * c_key, const char * c_secret, const char * t_key, const char * t_secret)</h3>
<p> the back-end behind by /ref oauth_sign_array2. however it does not serialize the signed URL again. The user needs to call /ref oauth_serialize_url (oA) and /ref oauth_free_array to do so. </p>
<p> This allows to split parts of the URL to be used for OAuth HTTP Authorization header: see <a rel="nofollow" href="http://oauth.net/core/1.0a/#consumer_req_param">http://oauth.net/core/1.0a/#consumer_req_param</a> the oauthtest2 example code does so. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>argcp</i> pointer to array length int<br />
 <i>argvp</i> pointer to array values (argv[0]=&#8217;<a rel="nofollow" href="http://example.org:80/'">http://example.org:80/&#8217;</a> argv[1]=&#8217;first=QueryParamater&#8217; .. the array is modified: fi. oauth_ parameters are added) These arrays can be generated with /ref oauth_split_url_parameters or /ref oauth_split_post_paramters.<br />
 <i>postargs</i> This parameter points to an area where the return value is stored. If &#8216;postargs&#8217; is NULL, no value is stored.<br />
 <i>method</i> specify the signature method to use. It is of type <code>OAuthMethod</code> and most likely <code>OA_HMAC</code>.<br />
 <i>http_method</i> The HTTP request method to use (ie &#8216;GET&#8217;, &#8216;PUT&#8217;,..) If NULL is given as &#8216;http_method&#8217; this defaults to &#8216;GET&#8217; when &#8216;postargs&#8217; is also NULL and when postargs is not NULL &#8216;POST&#8217; is used.<br />
 <i>c_key</i> consumer key<br />
 <i>c_secret</i> consumer secret<br />
 <i>t_key</i> token key<br />
 <i>t_secret</i> token secret</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> void</dl>
<p> <code>Examples: </code> <code>tests/oauthtest2.c</code>.</p>
<h3>char* oauth_sign_hmac_sha1 (const char * m, const char * k)</h3>
<p> returns base64 encoded HMAC-SHA1 signature for given message and key. both data and key need to be urlencoded. </p>
<p> the returned string needs to be freed by the caller </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>m</i> message to be signed<br />
 <i>k</i> key used for signing</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> signature string.</dl>
<p> <code>Examples: </code> <code>tests/selftest_wiki.c</code>.</p>
<h3>char* oauth_sign_hmac_sha1_raw (const char * m, const size_t ml, const char * k, const size_t kl)</h3>
<p> same as <code>oauth_sign_hmac_sha1</code> but allows to specify length of message and key (in case they contain null chars). <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>m</i> message to be signed<br />
 <i>ml</i> length of message<br />
 <i>k</i> key used for signing<br />
 <i>kl</i> length of key</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> signature string.</dl>
<h3>char* oauth_sign_plaintext (const char * m, const char * k)</h3>
<p> returns plaintext signature for the given key. the returned string needs to be freed by the caller </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>m</i> message to be signed<br />
 <i>k</i> key used for signing</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> signature string</dl>
<h3>char* oauth_sign_rsa_sha1 (const char * m, const char * k)</h3>
<p> returns RSA-SHA1 signature for given data. the returned signature needs to be freed by the caller. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>m</i> message to be signed<br />
 <i>k</i> private-key PKCS and Base64-encoded</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> base64 encoded signature string.</dl>
<p> <code>Examples: </code> <code>tests/selftest_wiki.c</code>.</p>
<h3>char* oauth_sign_url (const char * url, char ** postargs, <code>OAuthMethod</code> method, const char * c_key, const char * c_secret, const char * t_key, const char * t_secret)<code>Deprecated</code></h3>
<dl COMPACT>
<dt>
<dd> Use <code>oauth_sign_url2()</code> instead.</dl>
<h3>char* oauth_sign_url2 (const char * url, char ** postargs, <code>OAuthMethod</code> method, const char * http_method, const char * c_key, const char * c_secret, const char * t_key, const char * t_secret)</h3>
<p> calculate OAuth-signature for a given HTTP request URL, parameters and oauth-tokens. if &#8216;postargs&#8217; is NULL a &#8216;GET&#8217; request is signed and the signed URL is returned. Else this fn will modify &#8216;postargs&#8217; to point to memory that contains the signed POST-variables and returns the base URL. </p>
<p> both, the return value and (if given) &#8216;postargs&#8217; need to be freed by the caller. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>url</i> The request URL to be signed. append all GET or POST query-parameters separated by either &#8216;?&#8217; or &#8216;&amp;&#8217; to this parameter.<br />
 <i>postargs</i> This parameter points to an area where the return value is stored. If &#8216;postargs&#8217; is NULL, no value is stored.<br />
 <i>method</i> specify the signature method to use. It is of type <code>OAuthMethod</code> and most likely <code>OA_HMAC</code>.<br />
 <i>http_method</i> The HTTP request method to use (ie &#8216;GET&#8217;, &#8216;PUT&#8217;,..) If NULL is given as &#8216;http_method&#8217; this defaults to &#8216;GET&#8217; when &#8216;postargs&#8217; is also NULL and when postargs is not NULL &#8216;POST&#8217; is used.<br />
 <i>c_key</i> consumer key<br />
 <i>c_secret</i> consumer secret<br />
 <i>t_key</i> token key<br />
 <i>t_secret</i> token secret</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> the signed url or NULL if an error occurred.</dl>
<p> <code>Examples: </code> <code>tests/oauthbodyhash.c</code>, <code>tests/oauthexample.c</code>, and <code>tests/oauthtest.c</code>.</p>
<h3>char* oauth_sign_xmpp (const char * xml, <code>OAuthMethod</code> method, const char * c_secret, const char * t_secret)</h3>
<p> xep-0235 &#8211; TODO</p>
<h3>int oauth_split_post_paramters (const char * url, char *** argv, short qesc)</h3>
<p> splits the given url into a parameter array. (see <code>oauth_serialize_url</code> and <code>oauth_serialize_url_parameters</code> for the reverse) </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>url</i> the url or query-string to parse.<br />
 <i>argv</i> pointer to a (char *) array where the results are stored. The array is re-allocated to match the number of parameters and each parameter-string is allocated with strdup. &#8211; The memory needs to be freed by the caller.<br />
 <i>qesc</i> use query parameter escape (vs post-param-escape) &#8211; if set to 1 all &#8216;+&#8217; are treated as spaces &#8216; &#8216;</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> number of parameter(s) in array.</dl>
<h3>int oauth_split_url_parameters (const char * url, char *** argv)</h3>
<p> splits the given url into a parameter array. (see <code>oauth_serialize_url</code> and <code>oauth_serialize_url_parameters</code> for the reverse) (see <code>oauth_split_post_paramters</code> for a more generic version) </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>url</i> the url or query-string to parse; may be NULL<br />
 <i>argv</i> pointer to a (char *) array where the results are stored. The array is re-allocated to match the number of parameters and each parameter-string is allocated with strdup. &#8211; The memory needs to be freed by the caller.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> number of parameter(s) in array.</dl>
<p> <code>Examples: </code> <code>tests/oauthexample.c</code>, <code>tests/oauthtest.c</code>, and <code>tests/oauthtest2.c</code>.</p>
<h3>int oauth_time_independent_equals (const char * a, const char * b)</h3>
<p> compare two strings in constant-time. wrapper to <code>oauth_time_independent_equals_n</code> which calls strlen() for each argument. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>a</i> string to compare<br />
 <i>b</i> string to compare</dl>
<p> returns 0 (false) if strings are not equal, and 1 (true) if strings are equal.</p>
<h3>int oauth_time_independent_equals_n (const char * a, const char * b, size_t len_a, size_t len_b)</h3>
<p> compare two strings in constant-time (as to not let an attacker guess how many leading chars are correct: <a rel="nofollow" href="http://rdist.root.org/2010/01/07/timing-independent-array-comparison/">http://rdist.root.org/2010/01/07/timing-independent-array-comparison/</a> ) <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>a</i> string to compare<br />
 <i>b</i> string to compare<br />
 <i>len_a</i> length of string a<br />
 <i>len_b</i> length of string b</dl>
<p> returns 0 (false) if strings are not equal, and 1 (true) if strings are equal.</p>
<h3>int oauth_time_indepenent_equals (const char * a, const char * b)<code>Deprecated</code></h3>
<dl COMPACT>
<dt>
<dd> Use <code>oauth_time_independent_equals()</code> instead.</dl>
<h3>int oauth_time_indepenent_equals_n (const char * a, const char * b, size_t len_a, size_t len_b)<code>Deprecated</code></h3>
<dl COMPACT>
<dt>
<dd> Use <code>oauth_time_independent_equals_n()</code> instead.</dl>
<h3>char* oauth_url_escape (const char * string)</h3>
<p> Escape &#8216;string&#8217; according to RFC3986 and <a rel="nofollow" href="http://oauth.net/core/1.0/#encoding_parameters.">http://oauth.net/core/1.0/#encoding_parameters.</a> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>string</i> The data to be encoded</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> encoded string otherwise NULL The caller must free the returned string.</dl>
<h3>char* oauth_url_unescape (const char * string, size_t * olen)</h3>
<p> Parse RFC3986 encoded &#8216;string&#8217; back to unescaped version. <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>string</i> The data to be unescaped<br />
 <i>olen</i> unless NULL the length of the returned string is stored there.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> decoded string or NULL The caller must free the returned string.</dl>
<h3>int oauth_verify_rsa_sha1 (const char * m, const char * c, const char * s)</h3>
<p> verify RSA-SHA1 signature. returns the output of EVP_VerifyFinal() for a given message, cert/pubkey and signature. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dt>
<dd> <i>m</i> message to be verified<br />
 <i>c</i> public-key or x509 certificate<br />
 <i>s</i> base64 encoded signature</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dt>
<dd> 1 for a correct signature, 0 for failure and -1 if some other error occurred</dl>
<p> <code>Examples: </code> <code>tests/selftest_wiki.c</code>.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for OAuth library functions from the source code.</p>
