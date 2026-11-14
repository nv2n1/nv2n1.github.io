---
title: "git-cat-file(1)"
name: "git-cat-file"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-cat-file/"
description: "git-cat-file – Provide content or type and size information for repository objects"
---

<h2 class="name">NAME</h2>
<p> git-cat-file &#8211; Provide content or type and size information for repository objects </p>
<h2>SYNOPSIS</h2>
<pre><code>
git cat - file(-t[--allow - unknown - type] | -s[--allow - unknown - type] | -e | -p | &lt;type&gt; | --textconv | --filters)[--path = &lt;path&gt;]&lt;object&gt; git cat - file(--batch[=&lt;format&gt;] | --batch - check[=&lt;format&gt;])[--textconv | --filters][--follow - symlinks]
</code></pre>
<h2>DESCRIPTION</h2>
<p> In its first form, the command provides the content or the type of an object in the repository. The type is required unless <code>-t</code> or <code>-p</code> is used to find the object type, or <code>-s</code> is used to find the object size, or <code>&#8211;textconv</code> or <code>&#8211;filters</code> is used (which imply type &quot;blob&quot;). </p>
<p> In the second form, a list of objects (separated by linefeeds) is provided on stdin, and the SHA-1, type, and size of each object is printed on stdout. The output format can be overridden using the optional <code>&lt;format&gt;</code> argument. If either <code>&#8211;textconv</code> or <code>&#8211;filters</code> was specified, the input is expected to list the object names followed by the path name, separated by a single whitespace, so that the appropriate drivers can be determined.</p>
<h2>OPTIONS</h2>
<p> &lt;object&gt;</p>
<dl>
<dt>
<dd> The name of the object to show. For a more complete list of ways to spell object names, see the &quot;SPECIFYING REVISIONS&quot; section in <code><a href="/docs/linux/man/7-gitrevisions/">gitrevisions</a></code>(7).</dl>
<p> -t</p>
<dl>
<dt>
<dd> Instead of the content, show the object type identified by <code>&lt;object&gt;</code>.</dl>
<p> -s</p>
<dl>
<dt>
<dd> Instead of the content, show the object size identified by <code>&lt;object&gt;</code>.</dl>
<p> -e</p>
<dl>
<dt>
<dd> Exit with zero status if <code>&lt;object&gt;</code> exists and is a valid object. If <code>&lt;object&gt;</code> is of an invalid format exit with non-zero and emits an error on stderr.</dl>
<p> -p</p>
<dl>
<dt>
<dd> Pretty-print the contents of <code>&lt;object&gt;</code> based on its type.</dl>
<p> &lt;type&gt;</p>
<dl>
<dt>
<dd> Typically this matches the real type of <code>&lt;object&gt;</code> but asking for a type that can trivially be dereferenced from the given <code>&lt;object&gt;</code> is also permitted. An example is to ask for a &quot;tree&quot; with <code>&lt;object&gt;</code> being a commit object that contains it, or to ask for a &quot;blob&quot; with <code>&lt;object&gt;</code> being a tag object that points at it.</dl>
<p> &#8211;textconv</p>
<dl>
<dt>
<dd> Show the content as transformed by a textconv filter. In this case, <code>&lt;object&gt;</code> has to be of the form <code>&lt;tree-ish&gt;:&lt;path&gt;</code>, or <code>:&lt;path&gt;</code> in order to apply the filter to the content recorded in the index at <code>&lt;path&gt;</code>.</dl>
<p> &#8211;filters</p>
<dl>
<dt>
<dd> Show the content as converted by the filters configured in the current working tree for the given <code>&lt;path&gt;</code> (i.e. smudge filters, end-of-line conversion, etc). In this case, <code>&lt;object&gt;</code> has to be of the form <code>&lt;tree-ish&gt;:&lt;path&gt;</code>, or <code>:&lt;path&gt;</code>.</dl>
<p> &#8211;path=&lt;path&gt;</p>
<dl>
<dt>
<dd> For use with <code>&#8211;textconv</code> or <code>&#8211;filters</code>, to allow specifying an object name and a path separately, e.g. when it is difficult to figure out the revision from which the blob came.</dl>
<p> &#8211;batch, &#8211;batch=&lt;format&gt;</p>
<dl>
<dt>
<dd> Print object information and contents for each object provided on stdin. May not be combined with any other options or arguments except <code>&#8211;textconv</code> or <code>&#8211;filters</code>, in which case the input lines also need to specify the path, separated by whitespace. See the section <code>BATCH OUTPUT</code> below for details.</dl>
<p> &#8211;batch-check, &#8211;batch-check=&lt;format&gt;</p>
<dl>
<dt>
<dd> Print object information for each object provided on stdin. May not be combined with any other options or arguments except <code>&#8211;textconv</code> or <code>&#8211;filters</code>, in which case the input lines also need to specify the path, separated by whitespace. See the section <code>BATCH OUTPUT</code> below for details.</dl>
<p> &#8211;batch-all-objects</p>
<dl>
<dt>
<dd> Instead of reading a list of objects on stdin, perform the requested batch operation on all objects in the repository and any alternate object stores (not just reachable objects). Requires <code>&#8211;batch</code> or <code>&#8211;batch-check</code> be specified. By default, the objects are visited in order sorted by their hashes; see also <code>&#8211;unordered</code> below. Objects are presented as-is, without respecting the &quot;replace&quot; mechanism of <code><a href="/docs/linux/man/1-git-replace/">git-replace</a></code>(1).</dl>
<p> &#8211;buffer</p>
<dl>
<dt>
<dd> Normally batch output is flushed after each object is output, so that a process can interactively read and write from <code>cat-file</code>. With this option, the output uses normal stdio buffering; this is much more efficient when invoking <code>&#8211;batch-check</code> on a large number of objects.</dl>
<p> &#8211;unordered</p>
<dl>
<dt>
<dd> When <code>&#8211;batch-all-objects</code> is in use, visit objects in an order which may be more efficient for accessing the object contents than hash order. The exact details of the order are unspecified, but if you do not require a specific order, this should generally result in faster output, especially with <code>&#8211;batch</code>. Note that <code>cat-file</code> will still show each object only once, even if it is stored multiple times in the repository.</dl>
<p> &#8211;allow-unknown-type</p>
<dl>
<dt>
<dd> Allow <code>-s</code> or <code>-t</code> to query broken/corrupt objects of unknown type.</dl>
<p> &#8211;follow-symlinks</p>
<dl>
<dt>
<dd> With <code>&#8211;batch</code> or <code>&#8211;batch-check</code>, follow symlinks inside the repository when requesting objects with extended SHA-1 expressions of the form tree-ish:path-in-tree. Instead of providing output about the link itself, provide output about the linked-to object. If a symlink points outside the tree-ish (e.g. a link to <code>/foo</code> or a root-level link to <code>../foo</code>), the portion of the link which is outside the tree will be printed. </p>
<p> This option does not (currently) work correctly when an object in the index is specified (e.g. <code>:link</code> instead of <code>HEAD:link</code>) rather than one in the tree. </p>
<p> This option cannot (currently) be used unless <code>&#8211;batch</code> or <code>&#8211;batch-check</code> is used. </p>
<p> For example, consider a git repository containing: </p>
<dl>
<dt>
<dd>
<pre>
f: a file containing &quot;hello
&quot;
link: a symlink to f
dir/link: a symlink to ../f
plink: a symlink to ../f
alink: a symlink to /etc/passwd
</pre>
</dl>
<p> For a regular file <code>f</code>, <code>echo HEAD:f | git cat-file &#8211;batch</code> would print </p>
<dl>
<dt>
<dd>
<pre>
ce013625030ba8dba906f756967f9e9ca394464a blob 6
</pre>
</dl>
<p> And <code>echo HEAD:link | git cat-file &#8211;batch &#8211;follow-symlinks</code> would print the same thing, as would <code>HEAD:dir/link</code>, as they both point at <code>HEAD:f</code>. </p>
<p> Without <code>&#8211;follow-symlinks</code>, these would print data about the symlink itself. In the case of <code>HEAD:link</code>, you would see </p>
<dl>
<dt>
<dd>
<pre>
4d1ae35ba2c8ec712fa2a379db44ad639ca277bd blob 1
</pre>
</dl>
<p> Both <code>plink</code> and <code>alink</code> point outside the tree, so they would respectively print: </p>
<dl>
<dt>
<dd>
<pre>
symlink 4
../f
</pre>
</dl>
<dl>
<dt>
<dd>
<pre>
symlink 11
/etc/passwd
</pre>
</dl>
</dl>
<h2>OUTPUT</h2>
<p> If <code>-t</code> is specified, one of the <code>&lt;type&gt;</code>. </p>
<p> If <code>-s</code> is specified, the size of the <code>&lt;object&gt;</code> in bytes. </p>
<p> If <code>-e</code> is specified, no output, unless the <code>&lt;object&gt;</code> is malformed. </p>
<p> If <code>-p</code> is specified, the contents of <code>&lt;object&gt;</code> are pretty-printed. </p>
<p> If <code>&lt;type&gt;</code> is specified, the raw (though uncompressed) contents of the <code>&lt;object&gt;</code> will be returned.</p>
<h2>BATCH OUTPUT</h2>
<p> If <code>&#8211;batch</code> or <code>&#8211;batch-check</code> is given, <code>cat-file</code> will read objects from stdin, one per line, and print information about them. By default, the whole line is considered as an object, as if it were fed to <code><a href="/docs/linux/man/1-git-rev-parse/">git-rev-parse</a></code>(1). </p>
<p> You can specify the information shown for each object by using a custom <code>&lt;format&gt;</code>. The <code>&lt;format&gt;</code> is copied literally to stdout for each object, with placeholders of the form <code>%(atom)</code> expanded, followed by a newline. The available atoms are: </p>
<p> <code>objectname</code></p>
<dl>
<dt>
<dd> The full hex representation of the object name.</dl>
<p> <code>objecttype</code></p>
<dl>
<dt>
<dd> The type of the object (the same as <code>cat-file -t</code> reports).</dl>
<p> <code>objectsize</code></p>
<dl>
<dt>
<dd> The size, in bytes, of the object (the same as <code>cat-file -s</code> reports).</dl>
<p> <code>objectsize:disk</code></p>
<dl>
<dt>
<dd> The size, in bytes, that the object takes up on disk. See the note about on-disk sizes in the <code>CAVEATS</code> section below.</dl>
<p> <code>deltabase</code></p>
<dl>
<dt>
<dd> If the object is stored as a delta on-disk, this expands to the full hex representation of the delta base object name. Otherwise, expands to the null OID (all zeroes). See <code>CAVEATS</code> below.</dl>
<p> <code>rest</code></p>
<dl>
<dt>
<dd> If this atom is used in the output string, input lines are split at the first whitespace boundary. All characters before that whitespace are considered to be the object name; characters after that first run of whitespace (i.e., the &quot;rest&quot; of the line) are output in place of the <code>%(rest)</code> atom.</dl>
<p> If no format is specified, the default format is <code>%(objectname) %(objecttype) %(objectsize)</code>. </p>
<p> If <code>&#8211;batch</code> is specified, the object information is followed by the object contents (consisting of <code>%(objectsize)</code> bytes), followed by a newline. </p>
<p> For example, <code>&#8211;batch</code> without a custom format would produce: </p>
<dl>
<dt>
<dd>
<pre>
&lt;oid&gt; SP &lt;type&gt; SP &lt;size&gt; LF
&lt;contents&gt; LF
</pre>
</dl>
<p> Whereas <code>&#8211;batch-check=&#8217;%(objectname) %(objecttype)&#8217;</code> would produce: </p>
<dl>
<dt>
<dd>
<pre>
&lt;oid&gt; SP &lt;type&gt; LF
</pre>
</dl>
<p> If a name is specified on stdin that cannot be resolved to an object in the repository, then <code>cat-file</code> will ignore any custom format and print: </p>
<dl>
<dt>
<dd>
<pre>
&lt;object&gt; SP missing LF
</pre>
</dl>
<p> If a name is specified that might refer to more than one object (an ambiguous short sha), then <code>cat-file</code> will ignore any custom format and print: </p>
<dl>
<dt>
<dd>
<pre>
&lt;object&gt; SP ambiguous LF
</pre>
</dl>
<p> If <code>&#8211;follow-symlinks</code> is used, and a symlink in the repository points outside the repository, then <code>cat-file</code> will ignore any custom format and print: </p>
<dl>
<dt>
<dd>
<pre>
symlink SP &lt;size&gt; LF
&lt;symlink&gt; LF
</pre>
</dl>
<p> The symlink will either be absolute (beginning with a <code>/</code>), or relative to the tree root. For instance, if dir/link points to <code>../../foo</code>, then <code>&lt;symlink&gt;</code> will be <code>../foo</code>. <code>&lt;size&gt;</code> is the size of the symlink in bytes. </p>
<p> If <code>&#8211;follow-symlinks</code> is used, the following error messages will be displayed: </p>
<dl>
<dt>
<dd>
<pre>
&lt;object&gt; SP missing LF
</pre>
</dl>
<p> is printed when the initial symlink requested does not exist. </p>
<dl>
<dt>
<dd>
<pre>
dangling SP &lt;size&gt; LF
&lt;object&gt; LF
</pre>
</dl>
<p> is printed when the initial symlink exists, but something that it (transitive-of) points to does not. </p>
<dl>
<dt>
<dd>
<pre>
loop SP &lt;size&gt; LF
&lt;object&gt; LF
</pre>
</dl>
<p> is printed for symlink loops (or any symlinks that require more than 40 link resolutions to resolve). </p>
<dl>
<dt>
<dd>
<pre>
notdir SP &lt;size&gt; LF
&lt;object&gt; LF
</pre>
</dl>
<p> is printed when, during symlink resolution, a file is used as a directory name.</p>
<h2>CAVEATS</h2>
<p> Note that the sizes of objects on disk are reported accurately, but care should be taken in drawing conclusions about which refs or objects are responsible for disk usage. The size of a packed non-delta object may be much larger than the size of objects which delta against it, but the choice of which object is the base and which is the delta is arbitrary and is subject to change during a repack. </p>
<p> Note also that multiple copies of an object may be present in the object database; in this case, it is undefined which copy&#8217;s size or delta base will be reported.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
