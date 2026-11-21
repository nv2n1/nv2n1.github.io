---

title: "codeblocks(1)"
name: "codeblocks"
section: "1"
letter: "c"
url: "/docs/linux/man/1-codeblocks/"
description: "Code::Blocks – The open-source, cross-platform IDE"
---

<p> Code::Blocks &#8211; The open-source, cross-platform IDE</p>
<h2>SYNOPSIS</h2>
<p> <code>codeblocks [-h] [-ns] [-d] [&#8211;prefix &lt;str&gt;] [-p &lt;str&gt;] [&#8211;profile &lt;str&gt;]</code> <code>[&#8211;rebuild] [&#8211;build] [&#8211;target &lt;str&gt;] [&#8211;no-batch-window-close]</code> <code>[&#8211;batch-build-notify]</code> <i>[filename(s)&#8230;]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>codeblocks</code> launches the Code::Blocks IDE. Its various command-line arguments are listed below.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Displays the list of accepted command-line arguments.</dd>
<dt><code>-ns</code></dt>
<dd> Do not display a splash screen on startup. The splash screen can be completely disabled in the program&#8217;s environment options.</dd>
<dt><code>-d</code></dt>
<dd> Enable the debugging log.</dd>
<dt><code>&#8211;prefix</code></dt>
<dd> Specify an alternate path for Code::Blocks to find its shared files.</dd>
<dt><code>-p, &#8211;profile</code></dt>
<dd> Set which profile to use. If you set the profile to <code>ask</code> , Code::Blocks will display a list with all the known profiles to choose from.</dd>
<dt><code>&#8211;rebuild</code></dt>
<dd> Start a batch rebuild (i.e. &quot;clean&quot; and &quot;build&quot;) job on the filenames passed as arguments. The filenames can be either projects or workspaces.</dd>
<dt><code>&#8211;build</code></dt>
<dd> Start a batch build (i.e. no &quot;clean&quot;) job on the filenames passed as arguments. The filenames can be either projects or workspaces.</dd>
<dt><code>&#8211;target</code></dt>
<dd> Specify a single build target to build in the batch build (or rebuild) job.</dd>
<dt><code>&#8211;no-batch-window-close</code></dt>
<dd> When the batch job ends, the log window closes too. This option keeps it open until you manually close it.</dd>
<dt><code>&#8211;batch-build-notify</code></dt>
<dd> Display a message when the batch job finishes. </dd>
</dl>
<h2>EXAMPLES</h2>
<p> Batch build myproject.cpp, only the &quot;Debug&quot; target and keep the batch job window open when finished: </p>
<pre><code>
codeblocks-- build-- target = "Debug" --no - batch - window - close myproject.cbp Batch rebuild everything in myproject.cbp : codeblocks-- rebuild myproject.cbp
</code></pre>
<h2>AUTHOR</h2>
<pre>
Yiannis &quot;mandrav&quot; Mandravellos (mandrav [at] codeblocks.org)
</pre>
<h2>HISTORY</h2>
<p> 2006 &#8211; Initial version </p>
