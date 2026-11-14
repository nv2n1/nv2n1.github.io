---
title: "bti-shrink-urls(1)"
name: "bti-shrink-urls"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bti-shrink-urls/"
description: "bti-shrink-urls – convert URLs to a shorter form using a web service"
---

<h2 class="name">NAME</h2>
<p> bti-shrink-urls &#8211; convert URLs to a shorter form using a web service </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>bti</code> [<code>&#8211;escaped</code>] [<code>&#8211;help</code>] [<code>URL</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>bti-shrink-urls converts URLs to a shorter form using a web service. </p>
<p> Currently <a rel="nofollow" href="http://2tu.us/">http://2tu.us/</a> (default) and <a href="http://bit.ly">http://bit.ly</a> / <a href="http://j.mp">http://j.mp</a> are supported.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;escaped</code></p>
<dl>
<dt>
<dd> Don&#8217;t escape special characters in the URL any more, they are already percent encoded.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print help text.</dl>
<p> <code>URL</code></p>
<dl>
<dt>
<dd> Specify the URL to be converted. If no URL is given bti-shrink-urls waits for input on stdin.</dl>
<h2>CONFIGURATION</h2>
<p> bti-shrink-urls is configured by setting some values in ~/.bti: </p>
<p> <code>shrink_host</code></p>
<dl>
<dt>
<dd> Possible values: 2tu.us (default), bit.ly, j.mp</dl>
<p> <code>shrink_bitly_login</code></p>
<dl>
<dt>
<dd> API login for bit.ly, j.mp, required if shrink_host is set to bit.ly or j.mp. See <a rel="nofollow" href="https://code.google.com/p/bitly-api/wiki/ApiDocumentation">https://code.google.com/p/bitly-api/wiki/ApiDocumentation</a></dl>
<p> <code>shrink_bitly_key</code></p>
<dl>
<dt>
<dd> API key for bit.ly, j.mp, required if shrink_host is set to bit.ly or j.mp. See <a rel="nofollow" href="https://code.google.com/p/bitly-api/wiki/ApiDocumentation">https://code.google.com/p/bitly-api/wiki/ApiDocumentation</a></dl>
<h2>AUTHOR</h2>
<p> Written by Bart Trojanowski bart [at] jukie.net.</p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright (C) 2009 Bart Trojanowski bart [at] jukie.net. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation version 2 of the License. </p>
<h2>Index</h2>
