---
title: "lwp-dump(1)"
name: "lwp-dump"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lwp-dump/"
description: "lwp-dump – See what headers and content is returned for a URL"
---

<h2 class="name">NAME</h2>
<p> lwp-dump &#8211; See what headers and content is returned for a URL </p>
<h2>SYNOPSIS</h2>
<p> <code>lwp-dump</code> [ <i>options</i> ] <i></i><font SIZE="-1"><i>URL</i></font><i></i></p>
<h2>DESCRIPTION</h2>
<p> The <code>lwp-dump</code> program will get the resource indentified by the <font SIZE="-1">URL</font> and then dump the response object to <font SIZE="-1">STDOUT. </font> This will display the headers returned and the initial part of the content, escaped so that it&#8217;s safe to display even binary content. The escapes syntax used is the same as for Perl&#8217;s double quoted strings. If there is no content the string &#8220;(no content)&#8221; is shown in its place. </p>
<p> The following options are recognized:</p>
<dl>
<dt><code>&#8211;agent</code> <i>str</i></p>
<dd> Override the user agent string passed to the server.</p>
<dt><code>&#8211;keep-client-headers</code></p>
<dd> <font SIZE="-1">LWP</font> internally generate various <tt>&quot;Client-*&quot;</tt> headers that are stripped by <code>lwp-dump</code> in order to show the headers exactly as the server provided them. This option will suppress this.</p>
<dt><code>&#8211;max-length</code> <i>n</i></p>
<dd> How much of the content to show. The default is 512. Set this to 0 for unlimited. </p>
<p> If the content is longer then the string is chopped at the limit and the string &#8220;&#8230;
(### more bytes not shown)&#8221; appended.</p>
<dt><code>&#8211;method</code> <i>str</i></p>
<dd> Use the given method for the request instead of the default &#8220;<font SIZE="-1">GET&#8221;.</font></p>
<dt><code>&#8211;parse-head</code></p>
<dd> By default <code>lwp-dump</code> will not try to initialize headers by looking at the head section of <font SIZE="-1">HTML</font> documents. This option enables this. This corresponds to &#8220;parse_head&#8221; in LWP::UserAgent.</p>
<dt><code>&#8211;request</code></p>
<dd> Also dump the request sent.</dl>
<h2>SEE ALSO</h2>
<p> lwp-request, <font SIZE="-1">LWP</font>, &#8220;dump&#8221; in HTTP::Message </p>
<h2>Index</h2>
