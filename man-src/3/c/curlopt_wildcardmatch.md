---
title: "curlopt_wildcardmatch(3)"
name: "curlopt_wildcardmatch"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_wildcardmatch/"
description: "CURLOPT_WILDCARDMATCH – enable directory wildcard transfers"
---

<p>CURLOPT_WILDCARDMATCH &#8211; enable directory wildcard transfers</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_WILDCARDMATCH, long onoff);</p>
<h2>Description</h2>
<p>Set <i>onoff</i> to 1 if you want to transfer multiple files according to a file name pattern. The pattern can be specified as part of the <i><a href="/docs/linux/man/3-curlopt_url/">CURLOPT_URL</a>(3)</i> option, using an fnmatch-like pattern (Shell Pattern Matching) in the last part of URL (file name). </p>
<p> By default, libcurl uses its internal wildcard matching implementation. You can provide your own matching function by the <i><a href="/docs/linux/man/3-curlopt_fnmatch_function/">CURLOPT_FNMATCH_FUNCTION</a>(3)</i> option. </p>
<p> A brief introduction of its syntax follows:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>* &#8211; ASTERISK</p>
<dd><a href="ftp://example.com/some/path/">ftp://example.com/some/path/</a><code>*.txt</code> (for all txt&#8217;s from the root directory)</dl>
</dl>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>? &#8211; QUESTION MARK</p>
<dd>Question mark matches any (exactly one) character. </p>
<p> <a href="ftp://example.com/some/path/">ftp://example.com/some/path/</a><code>photo?.jpeg</code></dl>
</dl>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>[ &#8211; BRACKET EXPRESSION</p>
<dd>The left bracket opens a bracket expression. The question mark and asterisk have no special meaning in a bracket expression. Each bracket expression ends by the right bracket and matches exactly one character. Some examples follow: </p>
<p> <code>[a-zA-Z0-9]</code> or <code>[f-gF-G]</code> &#8211; character interval </p>
<p> <code>[abc]</code> &#8211; character enumeration </p>
<p> <code>[^abc]</code> or <code>[!abc]</code> &#8211; negation </p>
<p> <code>[[:</code><i>name</i><code>:]]</code> class expression. Supported classes are <code>alnum</code>,<code>lower</code>, <code>space</code>, <code>alpha</code>, <code>digit</code>, <code>print</code>, <code>upper</code>, <code>blank</code>, <code>graph</code>, <code>xdigit</code>. </p>
<p> <code>[][-!^]</code> &#8211; special case &#8211; matches only &#8216;-&#8216;, &#8216;]&#8217;, &#8216;[&#8216;, &#8216;!&#8217; or &#8216;^&#8217;. These characters have no special purpose. </p>
<p> <code>[\[\]\]</code> &#8211; escape syntax. Matches &#8216;[&#8216;, &#8216;]&#8217; or &#8216;\&#8217;. </p>
<p> Using the rules above, a file name pattern can be constructed: </p>
<p> <a href="ftp://example.com/some/path/">ftp://example.com/some/path/</a><code>[a-z[:upper:]\].jpeg</code></dl>
</dl>
<h2>Protocols</h2>
<p>This feature is only supported for FTP download.</p>
<h2>Example</h2>
<p>See <a rel="nofollow" href="http://curl.haxx.se/libcurl/c/ftp-wildcard.html">http://curl.haxx.se/libcurl/c/ftp-wildcard.html</a></p>
<h2>Availability</h2>
<p>Added in 7.21.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_fnmatch_function/">CURLOPT_FNMATCH_FUNCTION</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_url/">CURLOPT_URL</a></code>(3),</p>
