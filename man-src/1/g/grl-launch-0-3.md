---
title: "grl-launch-0-3(1)"
name: "grl-launch-0-3"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grl-launch-0-3/"
description: "grl-launch – run Grilo operations from the command line"
---

<p>grl-launch &#8211; run Grilo operations from the command line </p>
<h2>Synopsis</h2>
<p><code>grl-launch</code> [<i>OPTIONS</i>] OPERATION PARAMETERS</p>
<h2>Description</h2>
<p>This manual page documents briefly the <code>grl-launch</code> command. </p>
<p> <code>grl-launch</code> is a tool that allows the user to run Grilo operations from the command line.</p>
<h2>Operations</h2>
<dl>
<dt><code>browse</code><i> &lt;source&gt;|&lt;media box&gt;</i></dt>
<dd>
</dd><dt><code>may_resolve</code><i> &lt;key&gt; &lt;source&gt;|&lt;media box&gt; [&lt;source&gt;]</i></dt>
<dd>
</dd><dt><code>query</code><i> &lt;expression&gt; &lt;source&gt;</i></dt>
<dd>
</dd><dt><code>resolve</code><i> &lt;source&gt;|&lt;media&gt; [&lt;source&gt;]</i></dt>
<dd>
</dd><dt><code>search</code><i> &lt;term&gt; &lt;source&gt;</i></dt>
<dd>
</dd><dt><code>monitor</code><i> &lt;source&gt;</i></dt>
<dd>
</dd><dt><code>test_media_from_uri</code><i> &lt;uri&gt; [&lt;source&gt;]</i></dt>
<dd>
</dd><dt><code>media_from_uri</code><i> &lt;uri&gt; &lt;source&gt;</i></dt>
<dd></dd></dl>
<h2>Options</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd>Show summary of grl-launch options.</dd>
<dt><code>&#8211;help-grl</code></dt>
<dd>Show summary of Grilo options.</dd>
<dt><code>&#8211;help-all</code></dt>
<dd>Show summary of all options.</dd>
<dt><code>-C, &#8211;config</code></dt>
<dd>Configuration file to send to sources</dd>
<dt><code>-c, &#8211;count</code></dt>
<dd>Number of elements to return</dd>
<dt><code>-d, &#8211;delay</code></dt>
<dd>Wait some seconds before performing the operation (default 1 second)</dd>
<dt><code>-f, &#8211;flags=full|fast_only|idle_relay</code></dt>
<dd>List of comma-separated flags to use</dd>
<dt><code>-F, &#8211;full</code></dt>
<dd>Full serialize</dd>
<dt><code>-k, &#8211;keys</code></dt>
<dd>List of comma-separated keys to retrieve</dd>
<dt><code>-S, &#8211;serialize</code></dt>
<dd>Serialize</dd>
<dt><code>-s, &#8211;skip</code></dt>
<dd>Number of elements to skip</dd>
<dt><code>-T, &#8211;titles</code></dt>
<dd>Print column titles (useful for CSV spreadsheets)</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd>Print version</dd></dl>
<h2>Examples</h2>
<p>Print the ID for all the items searched in the Tracker source: </p>
<pre><dl><dt></dt><dd>grl-launch-0.3 search &quot;&quot; -S grl-tracker-source
</dd></dl></pre>
<dl>
<dt>Print the ID and title for the items in the Apple Trailers source:</dt>
<dd></dd></dl>
<pre><dl><dt></dt><dd>grl-launch-0.3 -k id,title browse grl-appletrailers-lua
</dd></dl></pre>
<dl>
<dt>Print the title for the videos indexed by Tracker:</dt>
<dd></dd></dl>
<pre><dl><dt></dt><dd>grl-launch-0.3 -S browse -k title grlcontainer://grl-tracker-source/videos
</dd></dl></pre>
<h2>Author</h2>
<p>This manual page was written by Alberto Garcia &lt;berto [at] igalia.com&gt;.</p>
