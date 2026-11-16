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
<dt><code>-h, &#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>-f FORMAT, &#8211;format=FORMAT</code></dt>
<dd> yum, kickstart or human; yum gives the result as a yum command line; kickstart the content of a %packages section; &quot;human&quot; readable is default.</dd>
<dt><code>-i INPUT, &#8211;input=INPUT</code></dt>
<dd> File to read the package list from instead of using the rpmdb. &#8211; for stdin. The file must contain package names only separated by white space (including newlines). rpm -qa &#8211;qf=&#8217;%{name}
&#8217; produces proper output.</dd>
<dt><code>-o OUTPUT, &#8211;output=OUTPUT</code></dt>
<dd> File to write the result to. Stdout is used if option is omitted.</dd>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> Do not show warnings.</dd>
<dt><code>-e, &#8211;no-excludes</code></dt>
<dd> Only show groups that are installed completely. Do not use exclude lines.</dd>
<dt><code>&#8211;global-excludes</code></dt>
<dd> Print exclude lines at the end and not after the groups requiring them.</dd>
<dt><code>&#8211;global-addons</code></dt>
<dd> Print package names at the end and not after the groups offering them as addon.</dd>
<dt><code>&#8211;addons-by-group</code></dt>
<dd> Also show groups not selected to sort packages contained by them. Those groups are commented out with a &quot;# &quot; at the begin of the line.</dd>
<dt><code>-m, &#8211;allow-mandatories</code></dt>
<dd> Check if just installing the mandatory packages gives better results. Uses &quot;.&quot; to mark those groups.</dd>
<dt><code>-a, &#8211;allow-all</code></dt>
<dd> Check if installing all packages in the groups gives better results. Uses &quot;*&quot; to mark those groups.</dd>
<dt><code>&#8211;ignore-missing</code></dt>
<dd> Ignore packages missing in the repos.</dd>
<dt><code>&#8211;ignore-missing-excludes</code></dt>
<dd> Do not produce exclude lines for packages not in the repository. </dd>
</dl>
<h2>Index</h2>
