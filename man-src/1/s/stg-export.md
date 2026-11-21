---

title: "stg-export(1)"
name: "stg-export"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stg-export/"
description: "stg-export – Export patches to a directory"
---

<p> stg-export &#8211; Export patches to a directory </p>
<h2>SYNOPSIS</h2>
<pre><code>
stg export[options][--][&lt;patch1&gt;][&lt;patch2&gt;][&lt;patch3&gt;..&lt;patch4&gt;]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Export a range of applied patches to a given directory (defaults to <i>patches-&lt;branch&gt;</i>) in a standard unified GNU diff format. A template file (defaulting to <i>.git/patchexport.tmpl</i> or <i>~/.stgit/templates/patchexport.tmpl</i> or <i>/usr/share/stgit/templates/patchexport.tmpl</i>) can be used for the patch format. The following variables are supported in the template file: </p>
<dl>
<dt>
</dt><dd>
<pre>
%(description)s - patch description
%(shortdescr)s  - the first line of the patch description
%(longdescr)s   - the rest of the patch description, after the first line
%(diffstat)s    - the diff statistics
%(authname)s    - author's name
%(authemail)s   - author's e-mail
%(authdate)s    - patch creation date
%(commname)s    - committer's name
%(commemail)s   - committer's e-mail
</pre>
</dd></dl>
<h2>OPTIONS</h2>
<p> -d DIR, &#8211;dir DIR</p>
<dl>
<dt>
</dt><dd> Export patches to DIR instead of the default.</dd></dl>
<p> -p, &#8211;patch</p>
<dl>
<dt>
</dt><dd> Append .patch to the patch names.</dd></dl>
<p> -e EXTENSION, &#8211;extension EXTENSION</p>
<dl>
<dt>
</dt><dd> Append .EXTENSION to the patch names.</dd></dl>
<p> -n, &#8211;numbered</p>
<dl>
<dt>
</dt><dd> Prefix the patch names with order numbers.</dd></dl>
<p> -t FILE, &#8211;template FILE</p>
<dl>
<dt>
</dt><dd> Use FILE as a template.</dd></dl>
<p> -b BRANCH, &#8211;branch BRANCH</p>
<dl>
<dt>
</dt><dd> Use BRANCH instead of the default branch.</dd></dl>
<p> -s, &#8211;stdout</p>
<dl>
<dt>
</dt><dd> Dump the patches to the standard output.</dd></dl>
<p> -O OPTIONS, &#8211;diff-opts OPTIONS</p>
<dl>
<dt>
</dt><dd> Extra options to pass to &quot;git diff&quot;.</dd></dl>
<h2>STGIT</h2>
<p> Part of the StGit suite &#8211; see <code><a href="/docs/linux/man/1-stg/">stg</a></code>(1) </p>
