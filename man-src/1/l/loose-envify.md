---
title: "loose-envify(1)"
name: "loose-envify"
section: "1"
letter: "l"
url: "/docs/linux/man/1-loose-envify/"
description: "loose-envify – replace Node.js environment variables with plain strings"
---

<h2 class="name">NAME</h2>
<p> <code>loose-envify</code> &#8211; replace Node.js environment variables with plain strings </p>
<h2>SYNOPSIS</h2>
<p> loose-envify &lt;javascript_source_file.js&gt;</p>
<h2>DESCRIPTION</h2>
<p> Performs a Javascript source-to-source transformation (transpiling), that efficiently replaces Node.js process.env environment variables with plain strings. This makes the environment variable checks faster and easier to optimize out.</p>
<h2>EXAMPLES</h2>
<p> Running this source code: </p>
<dl>
<dt>
<dd>
<pre><code>
if (process.env.NODE_ENV == = "development") {
    console.log('development only')
}
</code></pre>
</dl>
<p> through loose-envify: </p>
<dl>
<dt>
<dd>
<pre>
loose-envify index.js &gt; bundle.js
</pre>
</dl>
<p> with NODE_ENV set to production results in: </p>
<dl>
<dt>
<dd>
if (&#8220;production&#8221; == = &#8220;development&#8221;) {<br />
    console.log(&#8216;development only&#8217;)<br />
}
</dl>
<p> which, when run through a minifier, would be stripped out completely. </p>
<p> However, if you run the same script through loose-envify with NODE_ENV set to development it gives: </p>
<dl>
<dt>
<dd>
<pre><code>
if ("development" == = "development") {
    console.log('development only')
}
</code></pre>
</dl>
<p> The if statement will evaluate to true, so the code won&#8217;t be removed.</p>
<h2>AUTHOR</h2>
<p> Andres Suarez <code>&lt;zertosh [at] gmail.com&gt;</code></p>
<h2>COPYRIGHT</h2>
<p> This manual page was written by Paolo Greppi <code>&lt;paolo.greppi [at] libpf.com&gt;</code> for the Debian project (and may be used by others), also based on material from the envify README (<a rel="nofollow" href="https://github.com/hughsk/envify)">https://github.com/hughsk/envify)</a> by Hugh Kennedy <code>&lt;hughskennedy [at] gmail.com&gt;</code> and the envify contributors. </p>
<h2>Index</h2>
