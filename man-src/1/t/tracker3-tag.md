---
title: "tracker3-tag(1)"
name: "tracker3-tag"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tracker3-tag/"
description: "tracker3-tag – Add, remove and list tags."
---

<h2 class="name">NAME</h2>
<p> tracker3-tag &#8211; Add, remove and list tags. </p>
<h2>SYNOPSIS</h2>
<pre><code>
tracker3 tag FILE1[FILE2...][-l&lt;limit&gt;][-o&lt;offset&gt;][-r] tracker3 tag - t [[TAG1] [TAG2]...][-s][-r] tracker3 tag - a&lt;TAG&gt;[-e&lt;description&gt;] tracker3 tag - d&lt;TAG&gt;
</code></pre>
<h2>DESCRIPTION</h2>
<p> List tags for local files or by the tag labels themselves if -t is used. </p>
<p> It&#8217;s also possible to manage tags with the -a and and -d options. </p>
<p> The <i>FILE</i> argument can be either a local path or a URI. It also does not have to be an absolute path.</p>
<h2>OPTIONS</h2>
<p> <code>-t, &#8211;list</code></p>
<dl>
<dt>
<dd> List all tags. Results include the number of files associated with that tag and the tag&#8217;s unique identifier. You can show the files associated with each tag by using &#8211;show-files.</dl>
<p> The <i>TAG</i> arguments are optional. If no <i>TAG</i> argument is specified, all tags are listed. If one or more <i>TAG</i>s are given, either matching tags are listed (OR condition). For example, this will match any tags named either <i>foo</i>, <i>bar</i> or <i>baz</i>: </p>
<dl>
<dt>
<dd>
<pre>
$ tracker3-tag -t foo bar baz
</pre>
</dl>
<p> <code>-s, &#8211;show-files</code></p>
<dl>
<dt>
<dd> Show the files associated with each tag. This option is ONLY available WITH the <code>&#8211;list</code> option.</dl>
<p> <code>-a, &#8211;add=TAG</code></p>
<dl>
<dt>
<dd> Add a tag with the name <i>TAG</i>. If no <i>FILE</i> arguments are specified, the tag is simply created (if it didn&#8217;talready exist) and no files are associated with it. Multiple <i>FILE</i> arguments can be specified.</dl>
<p> <code>-d, &#8211;delete=TAG</code></p>
<dl>
<dt>
<dd> Delete a tag with the name <i>TAG</i>. If no <i>FILE</i> arguments are specified, the tag is deleted for ALL files. If <i>FILE</i> arguments are specified, only those files have the <i>TAG</i> deleted.</dl>
<p> <code>-e, &#8211;description=STRING</code></p>
<dl>
<dt>
<dd> This option ONLY applies when using <code>&#8211;add</code> and provides a description to go with the tag label according to <i>STRING</i>.</dl>
<p> <code>-l, &#8211;limit=N</code></p>
<dl>
<dt>
<dd> Limit search to N results. The default is 512.</dl>
<p> <code>-o, &#8211;offset=N</code></p>
<dl>
<dt>
<dd> Offset the search results by N. For example, start at item number 10 in the results. The default is 0.</dl>
<p> <code>-r, &#8211;and-operator</code></p>
<dl>
<dt>
<dd> Use AND operator for search terms instead of OR (the default). For example:</dl>
<dl>
<dt>
<dd>
<pre>
$ tracker3-tag -s -t sliff sloff
</pre>
</dl>
<p> Should show files in the database that have both the <i>sliff</i> and <i>sloff</i> tags.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-tracker3-sparql/">tracker3-sparql</a></code>(1), <code><a href="/docs/linux/man/1-tracker3-search/">tracker3-search</a></code>(1), <code><a href="/docs/linux/man/1-tracker3-info/">tracker3-info</a></code>(1). </p>
<h2>Index</h2>
