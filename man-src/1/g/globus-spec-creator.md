---
title: "globus-spec-creator(1)"
name: "globus-spec-creator"
section: "1"
letter: "g"
url: "/docs/linux/man/1-globus-spec-creator/"
description: "globus-spec-creator – Generate an RPM spec file from a GPT source package description"
---

<h2 class="name">NAME</h2>
<p> <code>globus-spec-creator</code> &#8211; Generate an <font SIZE="-1">RPM</font> spec file from a <font SIZE="-1">GPT</font> source package description </p>
<h2>SYNOPSIS</h2>
<p> <code>globus-spec-creator</code> [options] [patches &#8230;] </p>
<p> Options:</p>
<dl>
<dt><code>-gptfile</code> filename</p>
<dd> The package&#8217;s <font SIZE="-1">GPT</font> source package description file (mandatory)</p>
<dt><code>-setupfile</code> filename</p>
<dd> The corresponding setup package&#8217;s <font SIZE="-1">GPT</font> source package description file (default: none)</p>
<dt><code>-release</code> releasenumber</p>
<dd> The <font SIZE="-1">RPM</font> release number (default: 1)</p>
<dt><code>-directory</code> directory</p>
<dd> The package&#8217;s source directory in the toolkit installer</p>
<dt><code>-toolkitversion</code> versionnumber</p>
<dd> Globus toolkit version (default: 5.0.2)</p>
<dt><code>-email</code> emailaddress</p>
<dd> The packagers e-mail address (default: username [at] hostname)</p>
<dt><code>-nodoc</code></p>
<dd> Disable the generation of the doc <font SIZE="-1">RPM</font></p>
<dt><code>-help</code></p>
<dd> Show help</dl>
<p> Arguments: </p>
<p> Each additional argument will be added as a patch in the generated specfile.</p>
<h2>EXAMPLE</h2>
<p> globus-spec-creator -g globus_common-10.2/pkgdata/pkg_data_src.gpt.in -s globus_common_setup-2.6/pkgdata/pkg_data_src.gpt.in -r 3 -d common/source</p>
<h2>SEE ALSO</h2>
<p> See <a rel="nofollow" href="http://fedoraproject.org/wiki/PackagingDrafts/Globus">http://fedoraproject.org/wiki/PackagingDrafts/Globus</a> for additional information and examples.</p>
<h2>AUTHOR</h2>
<p> Mattias Ellert &lt;mattias.ellert [at] fysast.uu.se&gt; </p>
<h2>Index</h2>
