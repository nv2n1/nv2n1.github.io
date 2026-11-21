---

title: "vows(1)"
name: "vows"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vows/"
description: "vows – Asynchronous behavior-driven development (BDD) framework"
---

<p> vows &#8211; Asynchronous behavior-driven development (BDD) framework</p>
<h2>SYNOPSIS</h2>
<p> Usage: vows [FILE, &#8230;] [options]</p>
<h2>DESCRIPTION</h2>
<p> Vows is an asynchronous behavior-driven development (BDD) framework for Node.js. </p>
<p> Vows was built from the ground up to test asynchronous code. It executes your tests in parallel when it makes sense, and sequentially when there are dependencies. Emphasis was put on speed of execution, clarity and user experience.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> Enable verbose output</dd>
<dt><code>-w</code>, <code>&#8211;watch</code></dt>
<dd> Watch mode</dd>
<dt><code>-s</code>, <code>&#8211;silent</code></dt>
<dd> Don&#8217;t report</dd>
<dt><code>-i</code>, <code>&#8211;isolate</code></dt>
<dd> Run each test in it&#8217;s own vows process</dd>
<dt><code>-m</code></dt>
<dd> PATTERN Only run tests matching the PATTERN string</dd>
<dt><code>-r</code></dt>
<dd> PATTERN Only run tests matching the PATTERN regexp</dd>
<dt><code>&#8211;json</code></dt>
<dd> Use JSON reporter</dd>
<dt><code>&#8211;spec</code></dt>
<dd> Use Spec reporter</dd>
<dt><code>&#8211;tap</code></dt>
<dd> Use TAP reporter</dd>
<dt><code>&#8211;dot-matrix</code></dt>
<dd> Use Dot-Matrix reporter</dd>
<dt><code>&#8211;xunit</code></dt>
<dd> Use xUnit reporter</dd>
<dt><code>&#8211;cover-plain</code></dt>
<dd> Print plain coverage map if detected</dd>
<dt><code>&#8211;cover-html</code></dt>
<dd> Write coverage map to &quot;coverage.html&quot;</dd>
<dt><code>&#8211;cover-json</code></dt>
<dd> Write unified coverage map to &quot;coverage.json&quot;</dd>
<dt><code>&#8211;cover-xml</code></dt>
<dd> Write coverage map to &quot;coverage.xml&quot; in Emma xml</dd>
<dt><code>&#8211;no-color</code></dt>
<dd> Don&#8217;t use terminal colors</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> You&#8217;re staring at it</dd></dl>
<h2>REPORTING BUGS</h2>
<p> Please report bugs on the GitHub issue tracker: &lt;<code><a rel="nofollow" href="https://github.com/cloudhead/vows/issues">https://github.com/cloudhead/vows/issues</a></code>&gt; </p>
