---
title: "npm-coding-style(7)"
name: "npm-coding-style"
section: "7"
letter: "n"
url: "/docs/linux/man/7-npm-coding-style/"
description: "npm-coding-style – npm’s \"funny\" coding style"
---

<p><code>npm-coding-style</code> &#8211; npm&#8217;s &quot;funny&quot; coding style</p>
<h2>Description</h2>
<p>npm&#8217;s coding style is a bit unconventional. It is not different for difference&#8217;s sake, but rather a carefully crafted style that is designed to reduce visual clutter and make bugs more apparent. </p>
<p> If you want to contribute to npm (which is very encouraged), you should make your code conform to npm&#8217;s style. </p>
<p> Note: this concerns npm&#8217;s code not the specific packages that you can download from the npm registry.</p>
<h2>Line Length</h2>
<p>Keep lines shorter than 80 characters. It&#8217;s better for lines to be too short than to be too long. Break up long lists, objects, and other statements onto multiple lines.</p>
<h2>Indentation</h2>
<p>Two-spaces. Tabs are better, but they look like hell in web browsers (and on GitHub), and node uses 2 spaces, so that&#8217;s that. </p>
<p> Configure your editor appropriately.</p>
<h2>Curly braces</h2>
<p>Curly braces belong on the same line as the thing that necessitates them. </p>
<p> Bad:</p>
<dl>
<dd>
<pre>function ()
{</pre>
<dd></dl>
<p> Good:</p>
<dl>
<dd>
<pre>function () {</pre>
<dd></dl>
<p> If a block needs to wrap to the next line, use a curly brace. Don&#8217;t use it if it doesn&#8217;t. </p>
<p> Bad:</p>
<dl>
<dd>
<pre>if (foo) { bar() }
while (foo)
 bar()</pre>
<dd></dl>
<p> Good:</p>
<dl>
<dd>
<pre>if (foo) bar()
while (foo) {
 bar()
}</pre>
<dd></dl>
<h2>Semicolons</h2>
<p>Don&#8217;t use them except in four situations:</p>
<dl>
<dt>&bull;</p>
<dd><code>for (;;)</code> loops. They&#8217;re actually required.</p>
<dt>&bull;</p>
<dd>null loops like: <code>while (something) ;</code> (But you&#8217;d better have a good reason for doing that.)</p>
<dt>&bull;</p>
<dd><code>case &#8216;foo&#8217;: doSomething(); break</code></p>
<dt>&bull;</p>
<dd>In front of a leading <code>(</code> or <code>[</code> at the start of the line. This prevents the expression from being interpreted as a function call or property access, respectively.</p>
<dd></dl>
<p> Some examples of good semicolon usage:</p>
<dl>
<dd>
<pre>;(x || y).doSomething()
;[a, b, c].forEach(doSomething)
for (var i = 0; i &lt; 10; i ++) {
 switch (state) {
 case 'begin': start(); continue
 case 'end': finish(); break
 default: throw new Error('unknown state')
 }
 end()
}</pre>
<dd></dl>
<p> Note that starting lines with <code>&#8211;</code> and <code>+</code> also should be prefixed with a semicolon, but this is much less common.</p>
<h2>Comma First</h2>
<p>If there is a list of things separated by commas, and it wraps across multiple lines, put the comma at the start of the next line, directly below the token that starts the list. Put the final token in the list on a line by itself. For example:</p>
<dl>
<dd>
<pre>var magicWords = [ 'abracadabra'
 , 'gesundheit'
 , 'ventrilo'
 ]
 , spells = { 'fireball' : function () { setOnFire() }
 , 'water' : function () { putOut() }
 }
 , a = 1
 , b = 'abc'
 , etc
 , somethingElse</pre>
<dd></dl>
<h2>Quotes</h2>
<p>Use single quotes for strings except to avoid escaping. </p>
<p> Bad:</p>
<dl>
<dd>
<pre>var notOk = &quot;Just double quotes&quot;</pre>
<dd></dl>
<p> Good:</p>
<dl>
<dd>
<pre>var ok = 'String contains &quot;double&quot; quotes'
var alsoOk = &quot;String contains 'single' quotes or apostrophe&quot;</pre>
<dd></dl>
<h2>Whitespace</h2>
<p>Put a single space in front of ( for anything other than a function call. Also use a single space wherever it makes things more readable. </p>
<p> Don&#8217;t leave trailing whitespace at the end of lines. Don&#8217;t indent empty lines. Don&#8217;t use more spaces than are helpful.</p>
<h2>Functions</h2>
<p>Use named functions. They make stack traces a lot easier to read.</p>
<h2>Callbacks, Sync/async Style</h2>
<p>Use the asynchronous/non-blocking versions of things as much as possible. It might make more sense for npm to use the synchronous fs APIs, but this way, the fs and http and child process stuff all uses the same callback-passing methodology. </p>
<p> The callback should always be the last argument in the list. Its first argument is the Error or null. </p>
<p> Be very careful never to ever ever throw anything. It&#8217;s worse than useless. Just send the error message back as the first argument to the callback.</p>
<h2>Errors</h2>
<p>Always create a new Error object with your message. Don&#8217;t just return a string message to the callback. Stack traces are handy.</p>
<h2>Logging</h2>
<p>Logging is done using the npmlog <i><a rel="nofollow" href="https://github.com/npm/npmlog">https://github.com/npm/npmlog</a></i> utility. </p>
<p> Please clean up logs when they are no longer helpful. In particular, logging the same object over and over again is not helpful. Logs should report what&#8217;s happening so that it&#8217;s easier to track down where a fault occurs. </p>
<p> Use appropriate log levels. See npm help 7 <code>npm-config</code> and search for &quot;loglevel&quot;.</p>
<h2>Case, naming, etc.</h2>
<p>Use <code>lowerCamelCase</code> for multiword identifiers when they refer to objects, functions, methods, properties, or anything not specified in this section. </p>
<p> Use <code>UpperCamelCase</code> for class names (things that you&#8217;d pass to &quot;new&quot;). </p>
<p> Use <code>all-lower-hyphen-css-case</code> for multiword filenames and config keys. </p>
<p> Use named functions. They make stack traces easier to follow. </p>
<p> Use <code>CAPS_SNAKE_CASE</code> for constants, things that should never change and are rarely used. </p>
<p> Use a single uppercase letter for function names where the function would normally be anonymous, but needs to call itself recursively. It makes it clear that it&#8217;s a &quot;throwaway&quot; function.</p>
<h2>null, undefined, false, 0</h2>
<p>Boolean variables and functions should always be either <code>true</code> or <code>false</code>. Don&#8217;t set it to 0 unless it&#8217;s supposed to be a number. </p>
<p> When something is intentionally missing or removed, set it to <code>null</code>. </p>
<p> Don&#8217;t set things to <code>undefined</code>. Reserve that value to mean &quot;not yet set to anything.&quot; </p>
<p> Boolean objects are verboten.</p>
<h2>See Also</h2>
<dl>
<dt>&bull;</p>
<dd>npm help 7 developers</p>
<dt>&bull;</p>
<dd>npm help 7 faq</p>
<dt>&bull;</p>
<dd>npm help npm</p>
<dd>
