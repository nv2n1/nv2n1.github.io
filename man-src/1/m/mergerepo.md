---
title: "mergerepo(1)"
name: "mergerepo"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mergerepo/"
description: "mergerepo – Merge multiple repositories together"
---

<h2 class="name">NAME</h2>
<p> mergerepo &#8211; Merge multiple repositories together</p>
<h2>SYNOPSIS</h2>
<p> <code>mergerepo</code> &#8211;repo repo1 &#8211;repo repo2 </p>
<h2>DESCRIPTION</h2>
<p> <code>mergerepo</code> is a program that allows you merge multiple repositories into a single repository while referring to the remote location for all packages. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r &#8211;repo</code> &lt;url&gt;</p>
<dd> Url to a repository to be merged. </p>
<dt><code>-o &#8211;outputdir &lt;directory&gt;</code></p>
<dd> Path where merged repository metadata should be written to. If not specified repository metadata will be written to `pwd`/merged_repo/. </p>
<dt><code>-d &#8211;database</code></p>
<dd> Generate sqlite databases of the merged repository metadata. </p>
<dt><code>-a &#8211;archlist</code></p>
<dd> Specify a comma-separated list of architectures to use. Defaults to ALL. </p>
<dt><code>&#8211;nogroups</code></p>
<dd> Do not merge/include groups metadata in the repository. </p>
<dt><code>&#8211;noupdateinfo</code></p>
<dd> Do not merge/include updateinfo metadata in the repository. </p>
</dl>
<h2>EXAMPLES</h2>
<p> $ <code>mergerepo</code> &#8211;repo=<a rel="nofollow" href="http://myurl.org/repo1">http://myurl.org/repo1</a> &#8211;repo=<a href="http://myurl.org/repo2">http://myurl.org/repo2</a> -d -o /tmp/mymergedrepo </p>
<h2>SEE ALSO</h2>
<p> <i>createrepo (8)</i> </p>
<h2>AUTHORS</h2>
<pre>
Seth Vidal &lt;skvidal [at] fedoraproject.org&gt;
</pre>
<h2>BUGS</h2>
<p> Any bugs which are found should be emailed to the mailing list: rpm-metadata [at] lists.baseurl.org or filed as tickets at: <a rel="nofollow" href="http://createrepo.baseurl.org/">http://createrepo.baseurl.org/</a> </p>
<h2>Index</h2>
