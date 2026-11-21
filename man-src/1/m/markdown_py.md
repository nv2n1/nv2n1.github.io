---

title: "markdown_py(1)"
name: "markdown_py"
section: "1"
letter: "m"
url: "/docs/linux/man/1-markdown_py/"
description: "markdown_py – a Python implementation of John Gruber’s Markdown."
---

<p> <code>markdown_py [</code><i>options</i>] [<i>INPUT_FILE</i>]</p>
<dl>
<dt>
</dt><dd> (STDIN is assumed if no INPUT_FILE is given) </dd>
</dl>
<p> Command-line Markdown compiler based on python-markdown module, with extensions support. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> Show program&#8217;s version number and exit.</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show the help message and exit.</dd>
<dt><code>-f </code><i>OUTPUT_FILE</i>, <code>&#8211;file=</code><i>OUTPUT_FILE</i></dt>
<dd> Write output to OUTPUT_FILE. Defaults to STDOUT.</dd>
<dt><code>-e </code><i>ENCODING</i>, <code>&#8211;encoding=</code><i>ENCODING</i></dt>
<dd> Encoding for input and output files.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Suppress all warnings.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Print all warnings.</dd>
<dt><code>-s </code><i>SAFE_MODE</i>, <code>&#8211;safe=</code><i>SAFE_MODE</i></dt>
<dd> &#8216;replace&#8217;, &#8216;remove&#8217; or &#8216;escape&#8217; HTML tags in input.</dd>
<dt><code>-o </code><i>OUTPUT_FORMAT</i>, <code>&#8211;output_format=</code><i>OUTPUT_FORMAT</i></dt>
<dd> &#8216;xhtml1&#8217; (default), &#8216;html4&#8217; or &#8216;html5&#8217;.</dd>
<dt><code>&#8211;noisy</code></dt>
<dd> Print debug messages.</dd>
<dt><code>-x </code><i>EXTENSION</i>, <code>&#8211;extension=</code><i>EXTENSION</i></dt>
<dd> Load extension EXTENSION.</dd>
<dt><code>-n</code>, <code>&#8211;no_lazy_ol</code></dt>
<dd> Observe number of first item of ordered lists. </dd>
</dl>
