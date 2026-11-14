---
title: "dh_perl(1)"
name: "dh_perl"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_perl/"
description: "dh_perl – calculates Perl dependencies and cleans up after MakeMaker"
---

<h2 class="name">NAME</h2>
<p> dh_perl &#8211; calculates Perl dependencies and cleans up after MakeMaker </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_perl</code> [<i>debhelper options</i>] [<code>-d</code>] [<i>library dirs</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_perl</code> is a debhelper program that is responsible for generating the <code>${perl:Depends}</code> substitutions and adding them to substvars files. </p>
<p> The program will look at Perl scripts and modules in your package, and will use this information to generate a dependency on <code>perl</code> or <code>perlapi</code>. The dependency will be substituted into your package&#8217;s <i>control</i> file wherever you place the token <code>${perl:Depends}</code>. </p>
<p> <code>dh_perl</code> also cleans up empty directories that MakeMaker can generate when installing Perl modules.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code></p>
<dd> In some specific cases you may want to depend on <code>perl-base</code> rather than the full <code>perl</code> package. If so, you can pass the -d option to make <code>dh_perl</code> generate a dependency on the correct base package. This is only necessary for some packages that are included in the base system. </p>
<p> Note that this flag may cause no dependency on <code>perl-base</code> to be generated at all. <code>perl-base</code> is Essential, so its dependency can be left out, unless a versioned dependency is needed.</p>
<dt><code>-V</code></p>
<dd> By default, scripts and architecture independent modules don&#8217;t depend on any specific version of <code>perl</code>. The <code>-V</code> option causes the current version of the <code>perl</code> (or <code>perl-base</code> with <code>-d</code>) package to be specified.</p>
<dt><i>library dirs</i></p>
<dd> If your package installs Perl modules in non-standard directories, you can make <code>dh_perl</code> check those directories by passing their names on the command line. It will only check the <i>vendorlib</i> and <i>vendorarch</i> directories by default.</dl>
<h2>CONFORMS TO</h2>
<p> Debian policy, version 3.8.3 </p>
<p> Perl policy, version 1.20</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Brendan O&#8217;Dea &lt;bod [at] debian.org&gt; </p>
<h2>Index</h2>
