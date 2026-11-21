---

title: "newer(1)"
name: "newer"
section: "1"
letter: "n"
url: "/docs/linux/man/1-newer/"
description: "newer – compare file modification times"
---

<p> <code>newer</code> [<i>option</i>] <i>src1 </i> [ <i>src2 &#8230; srcN</i> ] <i>target</i></p>
<p> Exit successfully if files <i>src1 &#8230; srcN</i> exist and at least one of them is not older than <i>target</i>. Also exit successfully if <i>target</i> doesn&#8217;t exist.</p>
<h2>OPTIONS</h2>
<p> <code>newer</code> accepts the following options:</p>
<dl>
<dt><code>&#8211;help</code></dt>
<dd> Print help message and exit.</dd>
<dt><code>&#8211;quiet, -q</code></dt>
<dd> Do not print any output, including error messages.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print version information and exit.</dd>
<dt><code>&#8211;verbose, -v</code></dt>
<dd> List missing source files. This is the default. </dd>
</dl>
