---
title: "erb2-7(1)"
name: "erb2-7"
section: "1"
letter: "e"
url: "/docs/linux/man/1-erb2-7/"
description: "erb – Ruby Templating"
---

<p>UNIX</p>
<h2>Name</h2>
<p><code>erb</code> &#8211; Ruby Templating </p>
<h2>Synopsis</h2>
<p>[-<code>-version</code> ] [-<code>UPdnvx</code> ] [-<code>E </code><i>ext </i>[<code>: int</code> ] ] [-<code>S </code><i>level</i> ] [-<code>T </code><i>mode</i> ] [-<code>r </code><i>library</i> ] [- ] [file &#8230;] </p>
<h2>Description</h2>
<p>is a command line front-end for <code>ERB</code> library, which is an implementation of eRuby. </p>
<p> ERB provides an easy to use but powerful templating system for Ruby. Using ERB, actual Ruby code can be added to any plain text document for the purposes of generating document information details and/or flow control. </p>
<p> is a part of <code>Ruby</code> </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd>Prints the version of <code>.</code> </dd>
<dt><code>-E </code><i>external </i>[: <i>internal</i> ]</dt>
<dd>
</dd><dt><code>&#8211;encoding </code><i>external </i>[: <i>internal</i> ]</dt>
<dd>Specifies the default value(s) for external encodings and internal encoding. Values should be separated with colon (:). </dd>
<p> You can omit the one for internal encodings, then the value ( <code>Encoding.default_internal ) will be nil.</code> </p>
<dt><code>-P</code></dt>
<dd>Disables ruby code evaluation for lines beginning with <code>%</code> </dd>
<dt><code>-S </code><i>level</i></dt>
<dd>Specifies the safe level in which eRuby script will run. </dd>
<dt><code>-T </code><i>mode</i></dt>
<dd>Specifies trim mode (default 0). <i>mode</i> can be one of</dd>
<dl>
<dt><code>0</code></dt>
<dd>EOL remains after the embedded ruby script is evaluated. </dd>
<dt><code>1</code></dt>
<dd>EOL is removed if the line ends with <code>%&gt;</code> </dd>
<dt><code>2</code></dt>
<dd>EOL is removed if the line starts with <code>&lt;%</code> and ends with <code>%&gt;</code> </dd>
<dt><code>&#8211;</code></dt>
<dd>EOL is removed if the line ends with <code>-%&gt;</code> And leading whitespaces are removed if the erb directive starts with <code>&lt;%-</code> </dd>
</dl>
<dt><code>-r</code></dt>
<dd>Load a library </dd>
<dt><code>-U</code></dt>
<dd>can be one of Sets the default value for internal encodings ( <code>Encoding.default_internal ) to UTF-8.</code> </dd>
<dt><code>-d</code></dt>
<dd>
</dd><dt><code>&#8211;debug</code></dt>
<dd>Turns on debug mode. <code>$DEBUG</code> will be set to true. </dd>
<dt><code>-h</code></dt>
<dd>
</dd><dt><code>&#8211;help</code></dt>
<dd>Prints a summary of the options. </dd>
<dt><code>-n</code></dt>
<dd>Used with &#8211;<code>x</code> Prepends the line number to each line in the output. </dd>
<dt><code>-v</code></dt>
<dd>Enables verbose mode. <code>$VERBOSE</code> will be set to true. </dd>
<dt><code>-x</code></dt>
<dd>Converts the eRuby script into Ruby script and prints it without line numbers. </dd>
</dl>
<h2>Examples</h2>
<p>Here is an eRuby script </p>
<blockquote>
<pre>&lt;?xml version=&quot;1.0&quot; ?&gt;
&lt;% require 'prime' -%&gt;
&lt;erb-example&gt;
 &lt;calc&gt;&lt;%= 1+1 %&gt;&lt;/calc&gt;
 &lt;var&gt;&lt;%= __FILE__ %&gt;&lt;/var&gt;
 &lt;library&gt;&lt;%= Prime.each(10).to_a.join(&quot;, &quot;) %&gt;&lt;/library&gt;
&lt;/erb-example&gt;</pre>
</blockquote>
<p> Command </p>
<blockquote><p><tt>&quot;% erb -T - example.erb&quot;</tt></p></blockquote>
<p> prints </p>
<blockquote>
<pre>&lt;?xml version=&quot;1.0&quot; ?&gt;
&lt;erb-example&gt;
 &lt;calc&gt;2&lt;/calc&gt;
 &lt;var&gt;example.erb&lt;/var&gt;
 &lt;library&gt;2, 3, 5, 7&lt;/library&gt;
&lt;/erb-example&gt;</pre>
</blockquote>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ruby/">ruby</a>(1). </p>
<p> And see <a href="/docs/linux/man/1-ri/">ri</a>(1) documentation for <code>ERB</code> class. </p>
<h2>Reporting Bugs</h2>
<ul>
<li> Security vulnerabilities should be reported via an email to Mt security [at] ruby-lang.org . Reported problems will be published after being fixed.
<li> Other bugs and feature requests can be reported via the Ruby Issue Tracking System (Lk <a rel="nofollow" href="https://bugs.ruby-lang.org/">https://bugs.ruby-lang.org/</a> ) Do not report security vulnerabilities via this system because it publishes the vulnerabilities immediately. </ul>
<h2>Authors</h2>
<p>Written by Masatoshi SEKI.</p>
