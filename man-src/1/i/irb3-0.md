---
title: "irb3-0(1)"
name: "irb3-0"
section: "1"
letter: "i"
url: "/docs/linux/man/1-irb3-0/"
description: "irb – Interactive Ruby Shell"
---

<p>UNIX</p>
<h2>Name</h2>
<p><code>irb</code> &#8211; Interactive Ruby Shell </p>
<h2>Synopsis</h2>
<p><code>irb</code> [-<code>-version</code> ] [-<code>dfUw </code>[-<code>I </code><i>directory</i> ] ] [-<code>r </code><i>library</i> ] [-<code>E </code><i>external </i>[: <i>internal</i> ] ] [-<code>W </code>[<i>level</i> ] ] [-<code>&#8211; </code>[no <code>inspect</code> ] ] [-<code>&#8211; </code>[no <code>multiline</code> ] ] [-<code>&#8211; </code>[no <code>singleline</code> ] ] [-<code>&#8211; </code>[no <code>echo</code> ] ] [-<code>&#8211; </code>[no <code>colorize</code> ] ] [-<code>&#8211; </code>[no <code>verbose</code> ] ] [-<code>-prompt </code><i>mode</i> ] [-<code>-prompt-mode </code><i>mode</i> ] [-<code>-inf-ruby-mode</code> ] [-<code>-simple-prompt</code> ] [-<code>-noprompt</code> ] [-<code>-tracer</code> ] [-<code>-back-trace-limit </code><i>n</i> ] [- ] [program_file] [argument &#8230;] </p>
<h2>Description</h2>
<p><code>irb</code> is the REPL(read-eval-print loop) environment for Ruby programs. </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;version</code></dt>
<dd>Prints the version of <code>irb.</code> </dd>
<dt><code>-E </code><i>external </i>[: <i>internal</i> ]</dt>
<dd>
</dd><dt><code>&#8211;encoding </code><i>external </i>[: <i>internal</i> ]</dt>
<dd>Same as `ruby -E&#8217; . Specifies the default value(s) for external encodings and internal encoding. Values should be separated with colon (:). </dd>
<p> You can omit the one for internal encodings, then the value ( <code>Encoding.default_internal ) will be nil.</code> </p>
<dt><code>-I </code><i>path</i></dt>
<dd>Same as `ruby -I&#8217; . Specifies <code>$LOAD_PATH</code> directory </dd>
<dt><code>-U</code></dt>
<dd>Same as `ruby -U&#8217; . Sets the default value for internal encodings ( <code>Encoding.default_internal ) to UTF-8.</code> </dd>
<dt><code>-d</code></dt>
<dd>Same as `ruby -d&#8217; . Sets <code>$DEBUG</code> to true. </dd>
<dt><code>-f</code></dt>
<dd>Suppresses read of ~/.irbrc </dd>
<dt><code>-w</code></dt>
<dd>Same as `ruby -w&#8217; . </dd>
<dt><code>-W</code></dt>
<dd>Same as `ruby -W&#8217; . </dd>
<dt><code>-h</code></dt>
<dd>
</dd><dt><code>&#8211;help</code></dt>
<dd>Prints a summary of the options. </dd>
<dt><code>-r </code><i>library</i></dt>
<dd>Same as `ruby -r&#8217;. Causes irb to load the library using require. </dd>
<dt><code>&#8211;inspect</code></dt>
<dd>Uses `inspect&#8217; for output (default except for bc mode) </dd>
<dt><code>&#8211;noinspect</code></dt>
<dd>Doesn&#8217;t use inspect for output </dd>
<dt><code>&#8211;multiline</code></dt>
<dd>Uses multiline editor module. </dd>
<dt><code>&#8211;nomultiline</code></dt>
<dd>Doesn&#8217;t use multiline editor module. </dd>
<dt><code>&#8211;singleline</code></dt>
<dd>Uses singleline editor module. </dd>
<dt><code>&#8211;nosingleline</code></dt>
<dd>Doesn&#8217;t use singleline editor module. </dd>
<dt><code>&#8211;echo</code></dt>
<dd>Show result(default). </dd>
<dt><code>&#8211;noecho</code></dt>
<dd>Don&#8217;t show result. </dd>
<dt><code>&#8211;colorize</code></dt>
<dd>Use colorization. </dd>
<dt><code>&#8211;nocolorize</code></dt>
<dd>Don&#8217;t use colorization. </dd>
<dt><code>&#8211;verbose</code></dt>
<dd>Show details. </dd>
<dt><code>&#8211;noverbose</code></dt>
<dd>Don&#8217;t show details. </dd>
<dt><code>&#8211;prompt </code><i>mode</i></dt>
<dd>
</dd><dt><code>&#8211;prompt-mode </code><i>mode</i></dt>
<dd>Switch prompt mode. Pre-defined prompt modes are `default&#8217;, `simple&#8217;, `xmp&#8217; and `inf-ruby&#8217;. </dd>
<dt><code>&#8211;inf-ruby-mode</code></dt>
<dd>Uses prompt appropriate for inf-ruby-mode on emacs. Suppresses &#8211;multiline and &#8211;singleline. </dd>
<dt><code>&#8211;simple-prompt</code></dt>
<dd>Makes prompts simple. </dd>
<dt><code>&#8211;noprompt</code></dt>
<dd>No prompt mode. </dd>
<dt><code>&#8211;tracer</code></dt>
<dd>Displays trace for each execution of commands. </dd>
<dt><code>&#8211;back-trace-limit </code><i>n</i></dt>
<dd>Displays backtrace top <i>n</i> and tail <i>n </i> The default value is 16.</dd></dl>
<h2>Environment</h2>
<dl>
<dt><code>IRBRC</code></dt>
<dd></dd></dl>
<p> Also <code>irb</code> depends on same variables as <a href="/docs/linux/man/1-ruby/">ruby</a>(1). </p>
<h2>Files</h2>
<dl>
<dt><code>~/.irbrc </code></dt>
<dd>Personal irb initialization. </dd>
</dl>
<h2>Examples</h2>
<blockquote><p><tt>% irb</tt></p></blockquote>
<blockquote><p><tt>irb(main):001:0&gt; </tt><code>1 + 1</code> </p></blockquote>
<blockquote><p><tt>2</tt></p></blockquote>
<blockquote><p><tt>irb(main):002:0&gt; </tt><code>def t(x)</code> </p></blockquote>
<blockquote><p><tt>irb(main):003:1&gt; </tt><code>x + 1</code> </p></blockquote>
<blockquote><p><tt>irb(main):004:1&gt; </tt><code>end</code> </p></blockquote>
<blockquote><p><tt>=&gt; :t</tt></p></blockquote>
<blockquote><p><tt>irb(main):005:0&gt; </tt><code>t(3)</code> </p></blockquote>
<blockquote><p><tt>=&gt; 4</tt></p></blockquote>
<blockquote><p><tt>irb(main):006:0&gt; </tt><code>if t(3) == 4</code> </p></blockquote>
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
