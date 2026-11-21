---

title: "loose-envify(1)"
name: "loose-envify"
section: "1"
letter: "l"
url: "/docs/linux/man/1-loose-envify/"
description: "loose-envify – replace Node.js environment variables with plain strings"
---

<p> <code>loose-envify</code> &#8211; replace Node.js environment variables with plain strings </p>
<p> loose-envify &lt;javascript_source_file.js&gt;</p>
<p> Performs a Javascript source-to-source transformation (transpiling), that efficiently replaces Node.js process.env environment variables with plain strings. This makes the environment variable checks faster and easier to optimize out.</p>
<h2>EXAMPLES</h2>
<p> Running this source code: </p>
<dl>
<dt>
</dt><dd>
<pre><code>
if (process.env.NODE_ENV == = "development") {
    console.log('development only')
}
</code></pre>
</dd></dl>
<p> through loose-envify: </p>
<dl>
<dt>
</dt><dd>
<pre>
loose-envify index.js &gt; bundle.js
</pre>
</dd></dl>
<p> with NODE_ENV set to production results in: </p>
<dl>
<dt>
</dt><dd>
if (&#8220;production&#8221; == = &#8220;development&#8221;) {<br />
    console.log(&#8216;development only&#8217;)<br />
}
</dd></dl>
<p> which, when run through a minifier, would be stripped out completely. </p>
<p> However, if you run the same script through loose-envify with NODE_ENV set to development it gives: </p>
<dl>
<dt>
</dt><dd>
<pre><code>
if ("development" == = "development") {
    console.log('development only')
}
</code></pre>
</dd></dl>
<p> The if statement will evaluate to true, so the code won&#8217;t be removed.</p>
<h2>AUTHOR</h2>
<p> Andres Suarez <code>&lt;zertosh [at] gmail.com&gt;</code></p>
<h2>COPYRIGHT</h2>
<p> This manual page was written by Paolo Greppi <code>&lt;paolo.greppi [at] libpf.com&gt;</code> for the Debian project (and may be used by others), also based on material from the envify README (<a rel="nofollow" href="https://github.com/hughsk/envify)">https://github.com/hughsk/envify)</a> by Hugh Kennedy <code>&lt;hughskennedy [at] gmail.com&gt;</code> and the envify contributors. </p>
