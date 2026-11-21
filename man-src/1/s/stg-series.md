---

title: "stg-series(1)"
name: "stg-series"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-series/"
description: "stg-series – Print the patch series"
---

<pre><code>
stg series[options][--][&lt;patch - range&gt;]
</code></pre>
<p> Show all the patches in the series, or just those in the given range, ordered from top to bottom. </p>
<p> The applied patches are prefixed with a + (except the current patch, which is prefixed with a &gt;), the unapplied patches with a -, and the hidden patches with a !. </p>
<p> Empty patches are prefixed with a <i>0</i>.</p>
<h2>OPTIONS</h2>
<p> -b BRANCH, &#8211;branch BRANCH</p>
<dl>
<dt>
</dt><dd> Use BRANCH instead of the default branch.</dd></dl>
<p> -a, &#8211;all</p>
<dl>
<dt>
</dt><dd> Show all patches, including the hidden ones.</dd></dl>
<p> -A, &#8211;applied</p>
<dl>
<dt>
</dt><dd> Show the applied patches only.</dd></dl>
<p> -U, &#8211;unapplied</p>
<dl>
<dt>
</dt><dd> Show the unapplied patches only.</dd></dl>
<p> -H, &#8211;hidden</p>
<dl>
<dt>
</dt><dd> Show the hidden patches only.</dd></dl>
<p> -m BRANCH, &#8211;missing BRANCH</p>
<dl>
<dt>
</dt><dd> Show patches in BRANCH missing in current.</dd></dl>
<p> -c, &#8211;count</p>
<dl>
<dt>
</dt><dd> Print the number of patches in the series.</dd></dl>
<p> -d, &#8211;description</p>
<dl>
<dt>
</dt><dd> Show a short description for each patch.</dd></dl>
<p> &#8211;author</p>
<dl>
<dt>
</dt><dd> Show the author name for each patch.</dd></dl>
<p> -e, &#8211;empty</p>
<dl>
<dt>
</dt><dd> Before the +, &gt;, -, and ! prefixes, print a column that contains either 0 (for empty patches) or a space (for non-empty patches).</dd></dl>
<p> &#8211;showbranch</p>
<dl>
<dt>
</dt><dd> Append the branch name to the listed patches.</dd></dl>
<p> &#8211;noprefix</p>
<dl>
<dt>
</dt><dd> Do not show the patch status prefix.</dd></dl>
<p> -s, &#8211;short</p>
<dl>
<dt>
</dt><dd> List just the patches around the topmost patch.</dd></dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
