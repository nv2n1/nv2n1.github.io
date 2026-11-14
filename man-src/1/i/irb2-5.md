---
title: "irb2-5(1)"
name: "irb2-5"
section: "1"
letter: "i"
url: "/docs/linux/man/1-irb2-5/"
description: "irb – Interactive Ruby Shell"
---

<p>UNIX</p>
<h2>Name</h2>
<p><code>irb</code> &#8211; Interactive Ruby Shell </p>
<h2>Synopsis</h2>
<p>[-<code>-version</code> ] [-<code>dfm</code> ] [-<code>I </code><i>directory</i> ] [-<code>r </code><i>library</i> ] [-<code>&#8211; </code>[no <code>inspect</code> ] ] [-<code>&#8211; </code>[no <code>readline</code> ] ] [-<code>-prompt </code><i>mode</i> ] [-<code>-prompt-mode </code><i>mode</i> ] [-<code>-inf-ruby-mode</code> ] [-<code>-simple-prompt</code> ] [-<code>-noprompt</code> ] [-<code>-tracer</code> ] [-<code>-back-trace-limit </code><i>n</i> ] [-<code>-irb_debug </code><i>n</i> ] [- ] [program_file] [argument &#8230;] </p>
<h2>Description</h2>
<p>is the REPL(read-eval-print loop) environment for Ruby programs. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</code></p>
<dd>Prints the version of <code>.</code> </p>
<dt><code>-E </code><i>external </i>[: <i>internal</i> ]</p>
<dd>
<dt><code>&#8211;encoding </code><i>external </i>[: <i>internal</i> ]</p>
<dd>Same as `ruby -E&#8217; . Specifies the default value(s) for external encodings and internal encoding. Values should be separated with colon (:). </p>
<p> You can omit the one for internal encodings, then the value ( <code>Encoding.default_internal ) will be nil.</code> </p>
<dt><code>-I </code><i>path</i></p>
<dd>Same as `ruby -I&#8217; . Specifies <code>$LOAD_PATH</code> directory </p>
<dt><code>-U</code></p>
<dd>Same as `ruby -U&#8217; . Sets the default value for internal encodings ( <code>Encoding.default_internal ) to UTF-8.</code> </p>
<dt><code>-d</code></p>
<dd>Same as `ruby -d&#8217; . Sets <code>$DEBUG</code> to true. </p>
<dt><code>-f</code></p>
<dd>Suppresses read of ~/.irbrc </p>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd>Prints a summary of the options. </p>
<dt><code>-r </code><i>library</i></p>
<dd>Same as `ruby -r&#8217;. Causes irb to load the library using require. </p>
<dt><code>&#8211;inspect</code></p>
<dd>Uses `inspect&#8217; for output (default except for bc mode) </p>
<dt><code>&#8211;noinspect</code></p>
<dd>Doesn&#8217;t use inspect for output </p>
<dt><code>&#8211;readline</code></p>
<dd>Uses Readline extension module. </p>
<dt><code>&#8211;noreadline</code></p>
<dd>Doesn&#8217;t use Readline extension module. </p>
<dt><code>&#8211;prompt </code><i>mode</i></p>
<dd>
<dt><code>&#8211;prompt-mode </code><i>mode</i></p>
<dd>Switch prompt mode. Pre-defined prompt modes are `default&#8217;, `simple&#8217;, `xmp&#8217; and `inf-ruby&#8217;. </p>
<dt><code>&#8211;inf-ruby-mode</code></p>
<dd>Uses prompt appropriate for inf-ruby-mode on emacs. Suppresses &#8211;readline. </p>
<dt><code>&#8211;simple-prompt</code></p>
<dd>Makes prompts simple. </p>
<dt><code>&#8211;noprompt</code></p>
<dd>No prompt mode. </p>
<dt><code>&#8211;tracer</code></p>
<dd>Displays trace for each execution of commands. </p>
<dt><code>&#8211;back-trace-limit </code><i>n</i></p>
<dd>Displays backtrace top <i>n</i> and tail <i>n </i> The default value is 16. </p>
<dt><code>&#8211;irb_debug </code><i>n</i></p>
<dd>Sets internal debug level to n (not for popular use) </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>IRBRC</code></p>
<dd></dl>
<p> Also depends on same variables as <a href="/docs/linux/man/1-ruby/">ruby</a>(1). </p>
<h2>Files</h2>
<dl>
<dt><code>~/.irbrc </code></p>
<dd>Personal irb initialization. </p>
</dl>
<h2>Examples</h2>
<blockquote><p><tt>% irb</tt></p></blockquote>
<blockquote><p><tt>irb(main):001:0&gt; </tt><code>1 + 1</code> </p></blockquote>
<blockquote><p><tt>2</tt></p></blockquote>
<blockquote><p><tt>irb(main):002:0&gt; </tt><code>def t(x)</code> </p></blockquote>
<blockquote><p><tt>irb(main):003:1&gt; </tt><code>x+1</code> </p></blockquote>
<blockquote><p><tt>irb(main):004:1&gt; </tt><code>end</code> </p></blockquote>
<blockquote><p><tt>=&gt; :t</tt></p></blockquote>
<blockquote><p><tt>irb(main):005:0&gt; </tt><code><a href="/docs/linux/man/3-t/">t</a>(3)</code> </p></blockquote>
<blockquote><p><tt>=&gt; 4</tt></p></blockquote>
<blockquote><p><tt>irb(main):006:0&gt; </tt><code>if <a href="/docs/linux/man/3-t/">t</a>(3) == 4</code> </p></blockquote>
<blockquote><p><tt>irb(main):007:1&gt; </tt><code>p :ok</code> </p></blockquote>
<blockquote><p><tt>irb(main):008:1&gt; </tt><code>end</code> </p></blockquote>
<blockquote><p><tt>:ok</tt></p></blockquote>
<blockquote><p><tt>=&gt; :ok</tt></p></blockquote>
<blockquote><p><tt>irb(main):009:0&gt; </tt><code>quit</code> </p></blockquote>
<blockquote><p><tt>%</tt></p></blockquote>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-ruby/">ruby</a>(1). </p>
<h2>Reporting Bugs</h2>
<ul>
<li> Security vulnerabilities should be reported via an email to Mt security [at] ruby-lang.org . Reported problems will be published after being fixed.
<li> Other bugs and feature requests can be reported via the Ruby Issue Tracking System (Lk <a rel="nofollow" href="https://bugs.ruby-lang.org/">https://bugs.ruby-lang.org/</a> ) Do not report security vulnerabilities via this system because it publishes the vulnerabilities immediately. </ul>
<h2>Authors</h2>
<p>Written by Keiju ISHITSUKA.</p>
