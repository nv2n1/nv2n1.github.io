---
title: "intltoolize(8)"
name: "intltoolize"
section: "8"
letter: "i"
url: "/docs/linux/man/8-intltoolize/"
description: "intltoolize – copy intltool related files to software package"
---

<p>intltoolize &#8211; copy intltool related files to software package</p>
<h2>Synopsis</h2>
<p><code>intltoolize</code> [<i>option</i>]&#8230; </p>
<h2>Description</h2>
<p>This prepares a package to use intltool by linking or copying various files needed by intltool into place for use when building. Note that you must change your working directory to the top level directory of the package before running <code>intltoolize.</code> </p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;automake</code></dt>
<dd>Work silently and assume that <i>automake</i> is being used in software.</dd>
<dt><code>-c</code></dt>
<dd>
</dd><dt><code>&#8211;copy</code></dt>
<dd>Copy files rather than creating symbolic links to them.</dd>
<dt><code>&#8211;debug</code></dt>
<dd>Enable verbose shell tracing.</dd>
<dt><code>-n</code></dt>
<dd>
</dd><dt><code>&#8211;dry-run</code></dt>
<dd>Print commands only, instead of executing them.</dd>
<dt><code>-f</code></dt>
<dd>
</dd><dt><code>&#8211;force</code></dt>
<dd>Replace existing files if they exist.</dd>
<dt><code>&#8211;help</code></dt>
<dd>Show usage and basic help information.</dd>
<dt><code>&#8211;version</code></dt>
<dd>Show version information. </dd>
</dl>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="http://bugs.launchpad.net/intltool">http://bugs.launchpad.net/intltool</a></p>
<h2>Author</h2>
<p>Darin Adler &lt;darin [at] bentspoon.com&gt;<br/>
 Kenneth Christiansen &lt;kenneth [at] gnu.org&gt;<br/>
 Maciej Stachowiak &lt;mjs [at] eazel.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-intltool-prepare/">intltool-prepare</a></code>(8), <code><a href="/docs/linux/man/8-intltool-extract/">intltool-extract</a></code>(8), <code><a href="/docs/linux/man/8-intltool-merge/">intltool-merge</a></code>(8), <code><a href="/docs/linux/man/8-intltool-update/">intltool-update</a></code>(8) </p>
