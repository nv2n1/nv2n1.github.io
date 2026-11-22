---

title: "lwp-request(1)"
name: "lwp-request"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lwp-request/"
description: "lwp-request, GET, POST, HEAD – Simple command line user agent"
---

<p> lwp-request, GET, POST, HEAD &#8211; Simple command line user agent </p>
<h2>SYNOPSIS</h2>
<p> <code>lwp-request</code> [<code>-afPuUsSedvhx</code>] [<code>-m</code> <i>method</i>] [<code>-b</code> <i>base </i><i>URL</i><i></i>] [<code>-t</code> <i>timeout</i>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-i</code>&nbsp;<wbr><i>if-modified-since</i>]&nbsp;<wbr>[<code>-c</code>&nbsp;<wbr><i>content-type</i>]<br/>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[<code>-C</code>&nbsp;<wbr><i>credentials</i>]&nbsp;<wbr>[<code>-p</code>&nbsp;<wbr><i>proxy-url</i>]&nbsp;<wbr>[<code>-o</code>&nbsp;<wbr><i>format</i>]&nbsp;<wbr><i>url</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> This program can be used to send requests to WWW servers and your local file system. The request content for POST and PUT methods is read from stdin. The content of the response is printed on stdout. Error messages are printed on stderr. The program returns a status value indicating the number of URLs that failed. </p>
<p> The options are:</p>
<dl>
<dt>-m &lt;method&gt;</dt>
<dd> Set which method to use for the request. If this option is not used, then the method is derived from the name of the program.</dd>
<dt>-f</dt>
<dd> Force request through, even if the program believes that the method is illegal. The server might reject the request eventually.</dd>
<dt>-b &lt;uri&gt;</dt>
<dd> This URI will be used as the base URI for resolving all relative URIs given as argument.</dd>
<dt>-t &lt;timeout&gt;</dt>
<dd> Set the timeout value for the requests. The timeout is the amount of time that the program will wait for a response from the remote server before it fails. The default unit for the timeout value is seconds. You might append &#8220;m&#8221; or &#8220;h&#8221; to the timeout value to make it minutes or hours, respectively. The default timeout is &#8216;3m&#8217;, i.e. 3 minutes.</dd>
<dt>-i &lt;time&gt;</dt>
<dd> Set the If-Modified-Since header in the request. If <i>time</i> is the name of a file, use the modification timestamp for this file. If <i>time</i> is not a file, it is parsed as a literal date. Take a look at HTTP::Date for recognized formats.</dd>
<dt>-c &lt;content-type&gt;</dt>
<dd> Set the Content-Type for the request. This option is only allowed for requests that take a content, i.e. POST and PUT.  You can force methods to take content by using the <tt>&quot;-f&quot;</tt> option together with <tt>&quot;-c&quot;</tt>. The default Content-Type for POST is <tt>&quot;application/x-www-form-urlencoded&quot;</tt>. The default Content-type for the others is <tt>&quot;text/plain&quot;</tt>.</dd>
<dt>-p &lt;proxy-url&gt;</dt>
<dd> Set the proxy to be used for the requests. The program also loads proxy settings from the environment. You can disable this with the <tt>&quot;-P&quot;</tt> option.</dd>
<dt>-P</dt>
<dd> Don&#8217;t load proxy settings from environment.</dd>
<dt>-H &lt;header&gt;</dt>
<dd> Send this HTTP header with each request. You can specify several, e.g.: </dd>
<pre>
    lwp-request \
        -H 'Referer: <a rel="nofollow" href="http://other.url/'">http://other.url/'</a> \
        -H 'Host: somehost' \
        <a rel="nofollow" href="http://this.url/">http://this.url/</a>
</pre>
<dt>-C &lt;username&gt;:&lt;password&gt;</dt>
<dd> Provide credentials for documents that are protected by Basic Authentication. If the document is protected and you did not specify the username and password with this option, then you will be prompted to provide these values.</dd></dl>
<p> The following options controls what is displayed by the program:</p>
<dl>
<dt>-u</dt>
<dd> Print request method and absolute URL as requests are made.</dd>
<dt>-U</dt>
<dd> Print request headers in addition to request method and absolute URL.</dd>
<dt>-s</dt>
<dd> Print response status code. This option is always on for HEAD requests.</dd>
<dt>-S</dt>
<dd> Print response status chain. This shows redirect and authorization requests that are handled by the library.</dd>
<dt>-e</dt>
<dd> Print response headers. This option is always on for HEAD requests.</dd>
<dt>-E</dt>
<dd> Print response status chain with full response headers.</dd>
<dt>-d</dt>
<dd> Do <code>not</code> print the content of the response.</dd>
<dt>-o &lt;format&gt;</dt>
<dd> Process HTML content in various ways before printing it. If the content type of the response is not HTML, then this option has no effect. The legal format values are; <i>text</i>, <i>ps</i>, <i>links</i>, <i>html</i> and <i>dump</i>. </dd>
<p> If you specify the <i>text</i> format then the HTML will be formatted as plain latin1 text. If you specify the <i>ps</i> format then it will be formatted as Postscript. </p>
<p> The <i>links</i> format will output all links found in the HTML document. Relative links will be expanded to absolute ones. </p>
<p> The <i>html</i> format will reformat the HTML code and the <i>dump</i> format will just dump the HTML syntax tree. </p>
<p> Note that the <tt>&quot;HTML-Tree&quot;</tt> distribution needs to be installed for this option to work. In addition the <tt>&quot;HTML-Format&quot;</tt> distribution needs to be installed for <i>-o text</i> or <i>-o ps</i> to work.</p>
<dt>-v</dt>
<dd> Print the version number of the program and quit.</dd>
<dt>-h</dt>
<dd> Print usage message and quit.</dd>
<dt>-a</dt>
<dd> Set text(ascii) mode for content input and output. If this option is not used, content input and output is done in binary mode.</dd></dl>
<p> Because this program is implemented using the LWP library, it will only support the protocols that LWP supports.</p>
<h2>SEE ALSO</h2>
<p> lwp-mirror, LWP</p>
<h2>COPYRIGHT</h2>
<p> Copyright 1995-1999 Gisle Aas. </p>
<p> This library is free software; you can redistribute it and/or modify it under the same terms as Perl itself.</p>
<h2>AUTHOR</h2>
<p> Gisle Aas &lt;gisle [at] aas.no&gt; </p>
