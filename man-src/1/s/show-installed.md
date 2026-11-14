---
title: "show-installed(1)"
name: "show-installed"
section: "1"
letter: "s"
url: "/docs/linux/man/1-show-installed/"
description: "show-installed – show installed RPM packages and descriptions"
---

<h2>NAME</h2>
<p> show-installed &#8211; show installed RPM packages and descriptions</p>
<h2>SYNOPSIS</h2>
<p> <code>show-installed</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>show-installed</code> gives a compact description of the packages installed (or given) making use of the comps groups found in the repositories.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-f FORMAT, &#8211;format=FORMAT</code></p>
<dd> yum, kickstart or human; yum gives the result as a yum command line; kickstart the content of a %packages section; &quot;human&quot; readable is default.</p>
<dt><code>-i INPUT, &#8211;input=INPUT</code></p>
<dd> File to read the package list from instead of using the rpmdb. &#8211; for stdin. The file must contain package names only separated by white space (including newlines). rpm -qa &#8211;qf=&#8217;%{name}
&#8217; produces proper output.</p>
<dt><code>-o OUTPUT, &#8211;output=OUTPUT</code></p>
<dd> File to write the result to. Stdout is used if option is omitted.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Do not show warnings.</p>
<dt><code>-e, &#8211;no-excludes</code></p>
<dd> Only show groups that are installed completely. Do not use exclude lines.</p>
<dt><code>&#8211;global-excludes</code></p>
<dd> Print exclude lines at the end and not after the groups requiring them.</p>
<dt><code>&#8211;global-addons</code></p>
<dd> Print package names at the end and not after the groups offering them as addon.</p>
<dt><code>&#8211;addons-by-group</code></p>
<dd> Also show groups not selected to sort packages contained by them. Those groups are commented out with a &quot;# &quot; at the begin of the line.</p>
<dt><code>-m, &#8211;allow-mandatories</code></p>
<dd> Check if just installing the mandatory packages gives better results. Uses &quot;.&quot; to mark those groups.</p>
<dt><code>-a, &#8211;allow-all</code></p>
<dd> Check if installing all packages in the groups gives better results. Uses &quot;*&quot; to mark those groups.</p>
<dt><code>&#8211;ignore-missing</code></p>
<dd> Ignore packages missing in the repos.</p>
<dt><code>&#8211;ignore-missing-excludes</code></p>
<dd> Do not produce exclude lines for packages not in the repository. </p>
</dl>
<h2>Index</h2>
