---
title: "git-bugreport(1)"
name: "git-bugreport"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-bugreport/"
description: "git-bugreport – Collect information for user to file a bug report"
---

<h2 class="name">NAME</h2>
<p> git-bugreport &#8211; Collect information for user to file a bug report </p>
<h2>SYNOPSIS</h2>
<pre><code>
git bugreport[(-o | --output - directory) &lt; path &gt; ][(-s | --suffix) &lt; format &gt; ]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Captures information about the user&#8217;s machine, Git client, and repository state, as well as a form requesting information about the behavior the user observed, into a single text file which the user can then share, for example to the Git mailing list, in order to report an observed bug. </p>
<p> The following information is requested from the user: </p>
<dl>
<dt>
<dd> &bull; Reproduction steps</dl>
<dl>
<dt>
<dd> &bull; Expected behavior</dl>
<dl>
<dt>
<dd> &bull; Actual behavior</dl>
<p> The following information is captured automatically: </p>
<dl>
<dt>
<dd> &bull; <i>git version &#8211;build-options</i></dl>
<dl>
<dt>
<dd> &bull; uname sysname, release, version, and machine strings</dl>
<dl>
<dt>
<dd> &bull; Compiler-specific info string</dl>
<dl>
<dt>
<dd> &bull; A list of enabled hooks</dl>
<dl>
<dt>
<dd> &bull; $SHELL</dl>
<p> This tool is invoked via the typical Git setup process, which means that in some cases, it might not be able to launch &#8211; for example, if a relevant config file is unreadable. In this kind of scenario, it may be helpful to manually gather the kind of information listed above when manually asking for help.</p>
<h2>OPTIONS</h2>
<p> -o &lt;path&gt;, &#8211;output-directory &lt;path&gt;</p>
<dl>
<dt>
<dd> Place the resulting bug report file in <code>&lt;path&gt;</code> instead of the current directory.</dl>
<p> -s &lt;format&gt;, &#8211;suffix &lt;format&gt;</p>
<dl>
<dt>
<dd> Specify an alternate suffix for the bugreport name, to create a file named <i>git-bugreport-&lt;formatted suffix&gt;</i>. This should take the form of a <a href="/docs/linux/man/3-strftime/">strftime</a>(3) format string; the current local time will be used.</dl>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
