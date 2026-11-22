---

title: "globus-spec-creator(1)"
name: "globus-spec-creator"
section: "1"
letter: "g"
url: "/docs/linux/man/1-globus-spec-creator/"
description: "globus-spec-creator – Generate an RPM spec file from a GPT source package description"
---

<p> <code>globus-spec-creator</code> &#8211; Generate an RPM spec file from a GPT source package description </p>
<h2>SYNOPSIS</h2>
<p> <code>globus-spec-creator</code> [options] [patches &#8230;] </p>
<p> Options:</p>
<dl>
<dt><code>-gptfile</code> filename</dt>
<dd> The package&#8217;s GPT source package description file (mandatory)</dd>
<dt><code>-setupfile</code> filename</dt>
<dd> The corresponding setup package&#8217;s GPT source package description file (default: none)</dd>
<dt><code>-release</code> releasenumber</dt>
<dd> The RPM release number (default: 1)</dd>
<dt><code>-directory</code> directory</dt>
<dd> The package&#8217;s source directory in the toolkit installer</dd>
<dt><code>-toolkitversion</code> versionnumber</dt>
<dd> Globus toolkit version (default: 5.0.2)</dd>
<dt><code>-email</code> emailaddress</dt>
<dd> The packagers e-mail address (default: username [at] hostname)</dd>
<dt><code>-nodoc</code></dt>
<dd> Disable the generation of the doc RPM</dd>
<dt><code>-help</code></dt>
<dd> Show help</dd></dl>
<p> Arguments: </p>
<p> Each additional argument will be added as a patch in the generated specfile.</p>
<h2>EXAMPLE</h2>
<p> globus-spec-creator -g globus_common-10.2/pkgdata/pkg_data_src.gpt.in -s globus_common_setup-2.6/pkgdata/pkg_data_src.gpt.in -r 3 -d common/source</p>
<h2>SEE ALSO</h2>
<p> See <a rel="nofollow" href="http://fedoraproject.org/wiki/PackagingDrafts/Globus">http://fedoraproject.org/wiki/PackagingDrafts/Globus</a> for additional information and examples.</p>
<h2>AUTHOR</h2>
<p> Mattias Ellert &lt;mattias.ellert [at] fysast.uu.se&gt; </p>
