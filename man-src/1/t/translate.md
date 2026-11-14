---
title: "translate(1)"
name: "translate"
section: "1"
letter: "t"
url: "/docs/linux/man/1-translate/"
description: "translate – translate a text or web page"
---

<h2>NAME</h2>
<p> translate &#8211; translate a text or web page</p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>translate</code> {<code>-?</code> | <code>-v</code> | <code>&#8211;list-services</code>}</p>
<dt> <code>translate</code> [-s&nbsp;<wbr><i>services</i>] [-f&nbsp;<wbr><i>lang</i>] [-t&nbsp;<wbr><i>lang</i>] {-l}</p>
<dt> <code>translate</code> [-s&nbsp;<wbr><i>services</i>] [-f&nbsp;<wbr><i>lang</i>] [-t&nbsp;<wbr><i>lang</i>] {<i>http_url</i> | <i>https_url</i>}</p>
<dt> <code>translate</code> [-s&nbsp;<wbr><i>services</i>] [-f&nbsp;<wbr><i>lang</i>] [-t&nbsp;<wbr><i>lang</i>] [&#8211;max-threads=<i>n</i>] [&#8211;max-retries=<i>n</i>] [<i>file</i>] </p>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>translate</code> translates a text or web page. </p>
<dd>If the first synopsis form is used, <code>translate</code> prints a quick help, the version information or the list of available translation services to standard output. </p>
<p> If the second synopsis form is used, <code>translate</code> prints the list of available language pairs to standard output. </p>
<p> If the third synopsis form is used, <code>translate</code> translates the web page pointed to by <i>http_url</i> or <i>https_url</i>, and prints the URL of the translated web page to standard output (<i>http_url</i> must be a string starting with <a rel="nofollow" href="http://,">http://,</a> and <i>https_url</i> must be a string starting with <a href="https://">https://</a>). </p>
<p> If the fourth synopsis form is used, <code>translate</code> translates the text contained in <i>file</i>, and prints the translation to standard output (if <i>file</i> is omitted or given as a single dash, standard input is used instead). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Prints a quick help to standard output. </p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Prints version information to standard output. </p>
<dt><code>&#8211;list-services</code></p>
<dd> Lists the available translation services. </p>
<dt><code>-s</code> <i>services</i>, <code>&#8211;services</code>=<i>services</i></p>
<dd> Specifies the translation services to use. The <i>services</i> argument must be a comma-separated list of service names (default value: all the available services). </p>
<p> The list of services determines the available language pairs. The order of the list is important, as libtranslate iterates over the list until the requested translation can be performed. </p>
<dt><code>-l</code>, <code>&#8211;list-pairs</code></p>
<dd> Lists the available language pairs. </p>
<p> The <code>-f</code> and <code>-t</code> options can be used to specify a source and/or destination language filter. If neither <code>-f</code> nor <code>-t</code> is specified, all the pairs are listed. </p>
<dt><code>-f</code> <i>lang</i>, <code>&#8211;from</code>=<i>lang</i></p>
<dd> Specifies the source language of a translation. The <i>lang</i> argument must be a RFC 3066 language tag such as en or zh-TW (default value: see Language Selection). </p>
<dt><code>-t</code> <i>lang</i>, <code>&#8211;to</code>=<i>lang</i></p>
<dd> Specifies the destination language of a translation. The <i>lang</i> argument must be a RFC 3066 language tag such as en or zh-TW (default value: see Language Selection). </p>
<dt><code>&#8211;max-threads</code>=<i>n</i></p>
<dd> Specifies the maximum number of concurrent threads to use for translating text (default value: 8). </p>
<dt><code>&#8211;max-retries</code>=<i>n</i></p>
<dd> Specifies the maximum number of retries per text chunk (default value: 3). </p>
</dl>
<h2>LANGUAGE SELECTION</h2>
<p> Definitions: in this section, <i>default_from</i> is defined as the contents of the environment variable <code>TRANSLATE_DEFAULT_FROM</code>, or, if that variable is not set, en; <i>default_to</i> is defined as the contents of the environment variable <code>TRANSLATE_DEFAULT_TO</code>, or, if that variable is not set, fr. </p>
<p> If the source language is not specified, it defaults to <i>default_from</i>, or, if the destination language is equal to <i>default_from</i>, <i>default_to</i>. </p>
<p> If the destination language is not specified, it defaults to <i>default_to</i>, or, if the source language is equal to <i>default_to</i>, <i>default_from</i>. </p>
<h2>CHARACTER SET HANDLING</h2>
<p> Internally, libtranslate uses the UTF-8 encoding. </p>
<p> If the input text is not encoded in UTF-8, <code>translate</code> assumes it is encoded in the character set of the current locale, and attempts to convert it to UTF-8. If the conversion fails, <code>translate</code> exits with an error. </p>
<p> The output text is converted to the character set of the current locale before printing. </p>
<h2>EXAMPLES</h2>
<p> In the following examples, it is assumed that <code>TRANSLATE_DEFAULT_FROM</code> is set to es and that <code>TRANSLATE_DEFAULT_TO</code> is set to de. </p>
<dl>
<dt><code>translate</code> <code>-f</code> fr <code>-l</code></p>
<dd> Lists all the available language pairs where the source language is French. </p>
<dt><code>translate</code> document1</p>
<dd> Translates the contents of the file document1 from Spanish to German and prints the result to standard output. </p>
<dt><code>translate</code> <code>-s</code> babelfish,freetranslation document1</p>
<dd> Translates the contents of the file document1 from Spanish to German, only using the Babel Fish and FreeTranslation services, and prints the result to standard output. </p>
<dt><code>translate</code> <code>-f</code> de document1</p>
<dd> Translates the contents of the file document1 from German to Spanish and prints the result to standard output. </p>
<dt><code>echo</code> &quot;Le problème est résolu.&quot; | <code>translate</code> <code>-f</code> fr <code>-t</code> en</p>
<dd> Translates the text given on standard input from French to English and prints the result to standard output. </p>
<dt><code>translate</code> <code>-t</code> en <a rel="nofollow" href="http://www.freebsd.org/es/index.html">http://www.freebsd.org/es/index.html</a></p>
<dd> Translates the web page pointed to by <a rel="nofollow" href="http://www.freebsd.org/es/index.html">http://www.freebsd.org/es/index.html</a> from Spanish to English and prints an URL pointing to the result to standard output. </p>
</dl>
<h2>DIAGNOSTICS</h2>
<p> The <code>translate</code> utility exits with a status of 0 on success, and &gt;0 if an error occurs. </p>
<h2>ENVIRONMENT</h2>
<p> The following environment variables affect the execution of <code>translate</code>: </p>
<dl>
<dt><code>HTTP_PROXY</code></p>
<dd> The URL of the proxy to use for HTTP requests. </p>
<dt><code>http_proxy</code></p>
<dd> Same as HTTP_PROXY, for compatibility. </p>
<dt><code>TRANSLATE_DEFAULT_FROM</code></p>
<dd> The default source language (see Language Selection). </p>
<dt><code>TRANSLATE_DEFAULT_TO</code></p>
<dd> The default destination language (see Language Selection). </p>
</dl>
<h2>SEE ALSO</h2>
<p> The libtranslate Reference Manual </p>
<h2>AUTHOR</h2>
<p> Jean-Yves Lefort. </p>
<h2>Index</h2>
