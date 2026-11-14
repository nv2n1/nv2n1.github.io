---
title: "git-replace(1)"
name: "git-replace"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-replace/"
description: "git-replace – Create, list, delete refs to replace objects"
---

<h2 class="name">NAME</h2>
<p> git-replace &#8211; Create, list, delete refs to replace objects </p>
<h2>SYNOPSIS</h2>
<pre><code>
git replace[-f]&lt;object&gt;&lt;replacement&gt;
        git replace[-f]-- edit&lt;object&gt;
            git replace[-f]-- graft&lt;commit&gt;[&lt;parent&gt;...] git replace[-f]-- convert - graft - file git replace - d&lt;object&gt;... git replace[--format = &lt;format&gt;][-l[&lt;pattern&gt;]]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Adds a <i>replace</i> reference in <code>refs/replace/</code> namespace. </p>
<p> The name of the <i>replace</i> reference is the SHA-1 of the object that is replaced. The content of the <i>replace</i> reference is the SHA-1 of the replacement object. </p>
<p> The replaced object and the replacement object must be of the same type. This restriction can be bypassed using <code>-f</code>. </p>
<p> Unless <code>-f</code> is given, the <i>replace</i> reference must not yet exist. </p>
<p> There is no other restriction on the replaced and replacement objects. Merge commits can be replaced by non-merge commits and vice versa. </p>
<p> Replacement references will be used by default by all Git commands except those doing reachability traversal (prune, pack transfer and fsck). </p>
<p> It is possible to disable use of replacement references for any command using the <code>&#8211;no-replace-objects</code> option just after <i>git</i>. </p>
<p> For example if commit <i>foo</i> has been replaced by commit <i>bar</i>: </p>
<dl>
<dt>
<dd>
<pre>
$ git --no-replace-objects cat-file commit foo
</pre>
</dl>
<p> shows information about commit <i>foo</i>, while: </p>
<dl>
<dt>
<dd>
<pre>
$ git cat-file commit foo
</pre>
</dl>
<p> shows information about commit <i>bar</i>. </p>
<p> The <code>GIT_NO_REPLACE_OBJECTS</code> environment variable can be set to achieve the same effect as the <code>&#8211;no-replace-objects</code> option.</p>
<h2>OPTIONS</h2>
<p> -f, &#8211;force</p>
<dl>
<dt>
<dd> If an existing replace ref for the same object exists, it will be overwritten (instead of failing).</dl>
<p> -d, &#8211;delete</p>
<dl>
<dt>
<dd> Delete existing replace refs for the given objects.</dl>
<p> &#8211;edit &lt;object&gt;</p>
<dl>
<dt>
<dd> Edit an object&#8217;s content interactively. The existing content for &lt;object&gt; is pretty-printed into a temporary file, an editor is launched on the file, and the result is parsed to create a new object of the same type as &lt;object&gt;. A replacement ref is then created to replace &lt;object&gt; with the newly created object. See <code><a href="/docs/linux/man/1-git-var/">git-var</a></code>(1) for details about how the editor will be chosen.</dl>
<p> &#8211;raw</p>
<dl>
<dt>
<dd> When editing, provide the raw object contents rather than pretty-printed ones. Currently this only affects trees, which will be shown in their binary form. This is harder to work with, but can help when repairing a tree that is so corrupted it cannot be pretty-printed. Note that you may need to configure your editor to cleanly read and write binary data.</dl>
<p> &#8211;graft &lt;commit&gt; [&lt;parent&gt;&#8230;]</p>
<dl>
<dt>
<dd> Create a graft commit. A new commit is created with the same content as &lt;commit&gt; except that its parents will be [&lt;parent&gt;&#8230;] instead of &lt;commit&gt;&#8217;s parents. A replacement ref is then created to replace &lt;commit&gt; with the newly created commit. Use <code>&#8211;convert-graft-file</code> to convert a <code>$GIT_DIR/info/grafts</code> file and use replace refs instead.</dl>
<p> &#8211;convert-graft-file</p>
<dl>
<dt>
<dd> Creates graft commits for all entries in <code>$GIT_DIR/info/grafts</code> and deletes that file upon success. The purpose is to help users with transitioning off of the now-deprecated graft file.</dl>
<p> -l &lt;pattern&gt;, &#8211;list &lt;pattern&gt;</p>
<dl>
<dt>
<dd> List replace refs for objects that match the given pattern (or all if no pattern is given). Typing &quot;git replace&quot; without arguments, also lists all replace refs.</dl>
<p> &#8211;format=&lt;format&gt;</p>
<dl>
<dt>
<dd> When listing, use the specified &lt;format&gt;, which can be one of <i>short</i>, <i>medium</i> and <i>long</i>. When omitted, the format defaults to <i>short</i>.</dl>
<h2>FORMATS</h2>
<p> The following format are available: </p>
<dl>
<dt>
<dd> &bull; <i>short</i>: &lt;replaced sha1&gt;</dl>
<dl>
<dt>
<dd> &bull; <i>medium</i>: &lt;replaced sha1&gt; &rarr; &lt;replacement sha1&gt;</dl>
<dl>
<dt>
<dd> &bull; <i>long</i>: &lt;replaced sha1&gt; (&lt;replaced type&gt;) &rarr; &lt;replacement sha1&gt; (&lt;replacement type&gt;)</dl>
<h2>CREATING REPLACEMENT OBJECTS</h2>
<p> <code><a href="/docs/linux/man/1-git-hash-object/">git-hash-object</a></code>(1), <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1), and m[blue]<code>git-filter-repo</code>m[]<font SIZE="-2">[1]</font>, among other git commands, can be used to create replacement objects from existing objects. The <code>&#8211;edit</code> option can also be used with <i>git replace</i> to create a replacement object by editing an existing object. </p>
<p> If you want to replace many blobs, trees or commits that are part of a string of commits, you may just want to create a replacement string of commits and then only replace the commit at the tip of the target string of commits with the commit at the tip of the replacement string of commits.</p>
<h2>BUGS</h2>
<p> Comparing blobs or trees that have been replaced with those that replace them will not work properly. And using <code>git reset &#8211;hard</code> to go back to a replaced commit will move the branch to the replacement commit instead of the replaced commit. </p>
<p> There may be other problems when using <i>git rev-list</i> related to pending objects.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-hash-object/">git-hash-object</a></code>(1) <code><a href="/docs/linux/man/1-git-rebase/">git-rebase</a></code>(1) <code><a href="/docs/linux/man/1-git-tag/">git-tag</a></code>(1) <code><a href="/docs/linux/man/1-git-branch/">git-branch</a></code>(1) <code><a href="/docs/linux/man/1-git-commit/">git-commit</a></code>(1) <code><a href="/docs/linux/man/1-git-var/">git-var</a></code>(1) <code><a href="/docs/linux/man/1-git/">git</a></code>(1) m[blue]<code>git-filter-repo</code>m[]<font SIZE="-2">[1]</font></p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> git-filter-repo</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://github.com/newren/git-filter-repo">https://github.com/newren/git-filter-repo</a></dl>
</dl>
<h2>Index</h2>
