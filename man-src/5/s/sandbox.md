---
title: "sandbox(5)"
name: "sandbox"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sandbox/"
description: "sandbox.conf – user config file for the SELinux sandbox"
---

<p>sandbox.conf &#8211; user config file for the SELinux sandbox</p>
<h2>Description</h2>
<p>When running sandbox with the -C argument, it will be confined using control groups and a system administrator can specify how the sandbox is confined. Everything after &quot;#&quot; is ignored, as are empty lines. All arguments should be separated by and equals sign (&quot;=&quot;). These keywords are allowed.</p>
<dl>
<dd>
</dd><dl>
<dt><code>NAME</code></dt>
<dd>The name of the sandbox control group. Default is &quot;sandbox&quot;.</dd>
<dt><code>CPUAFFINITY</code></dt>
<dd>Which cpus to assign sandbox to. The default is ALL, but users can specify a comma-separated list with dashes (&quot;-&quot;) to represent ranges. Ex: 0-2,5</dd>
<dt><code>MEMUSAGE</code></dt>
<dd>How much memory to allow sandbox to use. The default is 80%. Users can specify either a percentage or a value in the form of a number followed by one of the suffixes K, M, G to denote kilobytes, megabytes or gigabytes respectively. Ex: 50% or 100M</dd>
<dt><code>CPUUSAGE</code></dt>
<dd>Percentage of cpu sandbox should be allowed to use. The default is 80%. Specify a value followed by a percent sign (&quot;%&quot;). Ex: 50% </dd>
<h2>See Also</h2>
<dl>
<dt><a href="/docs/linux/man/8-sandbox/">sandbox</a>(8)</dt>
<dd></dd></dl>
<h2>Author</h2>
<p>This manual page was written by <i>Thomas Liu &lt;tliu [at] fedoraproject.org&gt;</i></p>
</dl></dl>