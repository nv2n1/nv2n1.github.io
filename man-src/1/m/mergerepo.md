---

title: "mergerepo(1)"
name: "mergerepo"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mergerepo/"
description: "mergerepo – Merge multiple repositories together"
---

<p> <code>mergerepo</code> &#8211;repo repo1 &#8211;repo repo2 </p>
<p> <code>mergerepo</code> is a program that allows you merge multiple repositories into a single repository while referring to the remote location for all packages. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r &#8211;repo</code> &lt;url&gt;</dt>
<dd> Url to a repository to be merged. </dd>
<dt><code>-o &#8211;outputdir &lt;directory&gt;</code></dt>
<dd> Path where merged repository metadata should be written to. If not specified repository metadata will be written to `pwd`/merged_repo/. </dd>
<dt><code>-d &#8211;database</code></dt>
<dd> Generate sqlite databases of the merged repository metadata. </dd>
<dt><code>-a &#8211;archlist</code></dt>
<dd> Specify a comma-separated list of architectures to use. Defaults to ALL. </dd>
<dt><code>&#8211;nogroups</code></dt>
<dd> Do not merge/include groups metadata in the repository. </dd>
<dt><code>&#8211;noupdateinfo</code></dt>
<dd> Do not merge/include updateinfo metadata in the repository. </dd>
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
