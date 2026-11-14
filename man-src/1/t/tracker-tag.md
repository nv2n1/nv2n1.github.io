---
title: "tracker-tag(1)"
name: "tracker-tag"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker-tag/"
description: "tracker-tag – Add, remove and list tags."
---

<h2 class="name">NAME</h2>
<p> tracker-tag &#8211; Add, remove and list tags.</p>
<h2>SYNOPSIS</h2>
<pre><code>
tracker tag FILE1[FILE2...][-l&lt;limit&gt;][-o&lt;offset&gt;][-r] tracker tag - t [[TAG1] [TAG2]...][-s][-r] tracker tag - a&lt;TAG&gt;[-e&lt;description&gt;] tracker tag - d&lt;TAG&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> List tags for local files or by the tag labels themselves if -t is used. </p>
<p> It&#8217;s also possible to manage tags with the -a and and -d options. </p>
<p> The <i>FILE</i> argument can be either a local path or a URI. It also does not have to be an absolute path. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-t, &#8211;list</code></p>
<dd> List all tags. Results include the number of files associated with that tag and the tag&#8217;s unique identifier. You can show the files associated with each tag by using &#8211;show-files. </p>
<p> The <i>TAG</i> arguments are optional. If no <i>TAG</i> argument is specified, all tags are listed. If one or more <i>TAG</i>s are given, either matching tags are listed (OR condition). For example, this will match any tags named either <i>foo</i>, <i>bar</i> or <i>baz</i>: </p>
<pre>
$ tracker-tag -t foo bar baz
</pre>
<dt><code>-s, &#8211;show-files</code></p>
<dd> Show the files associated with each tag. This option is ONLY available WITH the <code>&#8211;list</code> option.</p>
<dt><code>-a, &#8211;add=TAG</code></p>
<dd> Add a tag with the name <i>TAG</i>. If no <i>FILE</i> arguments are specified, the tag is simply created (if it didn&#8217;talready exist) and no files are associated with it. Multiple <i>FILE</i> arguments can be specified.</p>
<dt><code>-d, &#8211;delete=TAG</code></p>
<dd> Delete a tag with the name <i>TAG</i>. If no <i>FILE</i> arguments are specified, the tag is deleted for ALL files. If <i>FILE</i> arguments are specified, only those files have the <i>TAG</i> deleted.</p>
<dt><code>-e, &#8211;description=STRING</code></p>
<dd> This option ONLY applies when using <code>&#8211;add</code> and provides a description to go with the tag label according to <i>STRING</i>.</p>
<dt><code>-l, &#8211;limit=N</code></p>
<dd> Limit search to N results. The default is 512.</p>
<dt><code>-o, &#8211;offset=N</code></p>
<dd> Offset the search results by N. For example, start at item number 10 in the results. The default is 0.</p>
<dt><code>-r, &#8211;and-operator</code></p>
<dd> Use AND operator for search terms instead of OR (the default). For example: </p>
<pre>
$ tracker-tag -s -t sliff sloff
</pre>
<p> Should show files in the database that have both the <i>sliff</i> and <i>sloff</i> tags. </p>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>TRACKER_SPARQL_BACKEND</code></p>
<dd> This option allows you to choose which backend you use for connecting to the database. This choice can limit your functionality. There are three settings. </p>
<p> With &quot;<code>direct</code>&quot; the connection to the database is made directly to the file itself on the disk, there is no intermediary daemon or process. The &quot;<code>direct</code>&quot; approach is purely <i>read-only</i>. </p>
<p> With &quot;<code>bus</code>&quot; the <code>tracker-store</code> process is used to liase with the database queuing all requests and managing the connections via an IPC / D-Bus. This adds a small overhead <i>BUT</i> this is the only approach you can use if you want to <i>write</i> to the database. </p>
<p> With &quot;<code>auto</code>&quot; the backend is decided for you, much like it would be if this environment variable was undefined. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker-store/">tracker-store</a></code>(1), <code><a href="/docs/linux/man/1-tracker-sparql/">tracker-sparql</a></code>(1), <code><a href="/docs/linux/man/1-tracker-search/">tracker-search</a></code>(1), <code><a href="/docs/linux/man/1-tracker-info/">tracker-info</a></code>(1). </p>
<h2>Index</h2>
