---
title: "rename-ul(1)"
name: "rename-ul"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rename-ul/"
description: "rename – rename files"
---

<p>rename &#8211; rename files </p>
<h2>Synopsis</h2>
<p><code>rename</code> [options] <i>expression replacement file</i>&#8230;</p>
<h2>Description</h2>
<p><code>rename</code> will rename the specified files by replacing the first occurrence of <i>expression</i> in their name by <i>replacement</i>.</p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-s</code>,<code> &#8211;symlink</code></dt>
<dd>Do not rename a symlink but its target.</dd>
<dt><code>-v</code>,<code> &#8211;verbose</code></dt>
<dd>Show which files were renamed, if any.</dd>
<dt><code>-n</code>,<code> &#8211;no-act</code></dt>
<dd>Do not make any changes; add <code>&#8211;verbose</code> to see what would be made.</dd>
<dt><code>-o</code>,<code> &#8211;no-overwrite</code></dt>
<dd>Do not overwrite existing files. When <code>&#8211;symlink</code> is active, do not overwrite symlinks pointing to existing targets.</dd>
<dt><code>-i</code>,<code> &#8211;interactive</code></dt>
<dd>Ask before overwriting existing files.</dd>
<dt><code>-V</code>,<code> &#8211;version</code></dt>
<dd>Display version information and exit.</dd>
<dt><code>-h</code>,<code> &#8211;help</code></dt>
<dd>Display help text and exit.</dd></dl>
<h2>Examples</h2>
<p>Given the files <i>foo1</i>, &#8230;, <i>foo9</i>, <i>foo10</i>, &#8230;, <i>foo278</i>, the commands</p>
<dl COMPACT>
<dd>
<pre>rename foo foo00 foo?
rename foo foo0 foo??</pre>
</dd></dl>
<p> will turn them into <i>foo001</i>, &#8230;, <i>foo009</i>, <i>foo010</i>, &#8230;, <i>foo278</i>. And</p>
<dl COMPACT>
<dd>
<pre>rename .htm .html *.htm</pre>
</dd></dl>
<p> will fix the extension of your html files. Provide an empty string for shortening:</p>
<dl COMPACT>
<dd>
<pre>rename '_with_long_name' '' file_with_long_name.*</pre>
</dd></dl>
<p> will remove the substring in the filenames.</p>
<h2>Warning</h2>
<p>The renaming has no safeguards by default or without any one of the options <code>&#8211;no-overwrite</code>, <code>&#8211;interactive</code> or <code>&#8211;no-act</code>. If the user has permission to rewrite file names, the command will perform the action without any questions. For example, the result can be quite drastic when the command is run as root in the /lib directory. Always make a backup before running the command, unless you truly know what you are doing.</p>
<h2>Interactive Mode</h2>
<p>As most standard utilities rename can be used with a terminal device (tty in short) in canonical mode, where the line is buffered by the tty and you press ENTER to validate the user input. If you put your tty in cbreak mode however, rename requires only a single key press to answer the prompt. To set cbreak mode, run for example:</p>
<dl COMPACT>
<dd>
<pre>sh -c 'stty -icanon min 1; &quot;$0&quot; &quot;$@&quot;; stty icanon' rename -i from to files</pre>
</dd></dl>
<h2>Exit Status</h2>
<dl COMPACT>
<dd>
</dd><dl COMPACT>
<dt><code>0</code></dt>
<dd>all requested rename operations were successful</dd>
<dt><code>1</code></dt>
<dd>all rename operations failed</dd>
<dt><code>2</code></dt>
<dd>some rename operations failed</dd>
<dt><code>4</code></dt>
<dd>nothing was renamed</dd>
<dt><code>64</code></dt>
<dd>unanticipated error occurred</dd></dl>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mv/">mv</a></code>(1)</p>
<h2>Availability</h2>
<p>The rename command is part of the util-linux package and is available from <a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/.">https://www.kernel.org/pub/linux/utils/util-linux/.</a></p>
