---

title: "flickcurl-config(1)"
name: "flickcurl-config"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flickcurl-config/"
description: "flickcurl-config – script to get information about the installed version of flickcurl"
---

<h2>NAME</h2>
<p> flickcurl-config &#8211; script to get information about the installed version of flickcurl</p>
<p> <code>flickcurl-config</code> [ <i>OPTION</i> ]</p>
<dl>
<dt>
</dt><dd> This program is <code>DEPRECATED</code> and <a href="/docs/linux/man/1-pkg-config/">pkg-config</a>(1) should be used to get flickcurl library parameters and dependencies. The compiling and linking flags are likely to not work since they do not import dependendent libraries (such as Raptor).</dd></dl>
<p> Known values for OPTION are:</p>
<dl>
<dt><code>&#8211;prefix</code></dt>
<dd> Get the flickcurl installation prefix.</dd>
<dt><code>&#8211;libs</code></dt>
<dd> Print library linking information.</dd>
<dt><code>&#8211;private-libs</code></dt>
<dd> Print library private/static linking information.</dd>
<dt><code>&#8211;cflags</code></dt>
<dd> Print pre-processor and compiler flags</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information</dd>
<dt><code>&#8211;version-decimal</code></dt>
<dd> Output version as a decimal integer.</dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Kumar Appaiah &lt;akumar [at] ee.iitm.ac.in&gt;, for the Debian project (but may be used by others). </p>
