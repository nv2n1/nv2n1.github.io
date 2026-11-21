---

title: "git-prune(1)"
name: "git-prune"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-prune/"
description: "git-prune – Prune all unreachable objects from the object database"
---

<p> git-prune &#8211; Prune all unreachable objects from the object database </p>
<h2>SYNOPSIS</h2>
<pre><code>
git prune[-n][-v][--progress][--expire&lt;time&gt;][--][&lt;head&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<dl>
<dt>
</dt><dd>
 <font SIZE="+1"> <code>Note</code> </font> </dd>
<p> In most cases, users should run <i>git gc</i>, which calls <i>git prune</i>. See the section &quot;NOTES&quot;, below. </p>
</dl>
<p> This runs <i>git fsck &#8211;unreachable</i> using all the refs available in <code>refs/</code>, optionally with additional set of objects specified on the command line, and prunes all unpacked objects unreachable from any of these head objects from the object database. In addition, it prunes the unpacked objects that are also found in packs by running <i>git prune-packed</i>. It also removes entries from .git/shallow that are not reachable by any ref. </p>
<p> Note that unreachable, packed objects will remain. If this is not desired, see <code><a href="/docs/linux/man/1-git-repack/">git-repack</a></code>(1).</p>
<h2>OPTIONS</h2>
<p> -n, &#8211;dry-run</p>
<dl>
<dt>
</dt><dd> Do not remove anything; just report what it would remove.</dd></dl>
<p> -v, &#8211;verbose</p>
<dl>
<dt>
</dt><dd> Report all removed objects.</dd></dl>
<p> &#8211;progress</p>
<dl>
<dt>
</dt><dd> Show progress.</dd></dl>
<p> &#8211;expire &lt;time&gt;</p>
<dl>
<dt>
</dt><dd> Only expire loose objects older than &lt;time&gt;.</dd></dl>
<p> &#8212;</p>
<dl>
<dt>
</dt><dd> Do not interpret any more arguments as options.</dd></dl>
<p> &lt;head&gt;&#8230;</p>
<dl>
<dt>
</dt><dd> In addition to objects reachable from any of our references, keep objects reachable from listed &lt;head&gt;s.</dd></dl>
<h2>EXAMPLES</h2>
<p> To prune objects not used by your repository or another that borrows from your repository via its <code>.git/objects/info/alternates</code>: </p>
<dl>
<dt>
</dt><dd>
<pre>
$ git prune $(cd ../another &amp;&amp; git rev-parse --all)
</pre>
</dd></dl>
<h2>NOTES</h2>
<p> In most cases, users will not need to call <i>git prune</i> directly, but should instead call <i>git gc</i>, which handles pruning along with many other housekeeping tasks. </p>
<p> For a description of which objects are considered for pruning, see <i>git fsck</i>&#8216;s &#8211;unreachable option.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-git-fsck/">git-fsck</a></code>(1), <code><a href="/docs/linux/man/1-git-gc/">git-gc</a></code>(1), <code><a href="/docs/linux/man/1-git-reflog/">git-reflog</a></code>(1)</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
