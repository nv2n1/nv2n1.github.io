---
title: "nodeunit(1)"
name: "nodeunit"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nodeunit/"
description: "nodeunit — simple node.js unit testing tool"
---

<h2>NAME</h2>
<p> <code>nodeunit</code> &#8212; simple node.js unit testing tool</p>
<h2>SYNOPSIS</h2>
<pre><code>
nodeunit[options]&lt;file - or -directory&gt;[ &lt; file - or -directory &gt; ...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> Nodeunit is a simple unit testing tool based on the node.js assert module.</p>
<dl>
<dt>&bull;</p>
<dd> Simple to use</p>
<dt>&bull;</p>
<dd> Just export the tests from a module</p>
<dt>&bull;</p>
<dd> Helps you avoid common pitfalls when testing asynchronous code</p>
<dt>&bull;</p>
<dd> Easy to add test cases with setUp and tearDown functions if you wish</p>
<dt>&bull;</p>
<dd> Allows the use of mocks and stubs</p>
<dt>
<dd></dl>
<h2>OPTIONS</h2>
<p>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;config FILE</code>: </p>
<p>Load config options from a JSON file, allows the customisation<br />
of color schemes for the default test reporter etc.<br />
See bin/nodeunit.json for current available options. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;reporter FILE</code>: </p>
<p>You can set the test reporter to a custom module or on of the modules<br />
in nodeunit/lib/reporters, when omitted, the default test runner is used. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>&#8211;list-reporters</code>: </p>
<p>List available build-in reporters. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>-h</code>,&nbsp;<wbr><code>&#8211;help</code>: </p>
<p>Display the help and exit. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>-v</code>,&nbsp;<wbr><code>&#8211;version</code>: </p>
<p>Output version information and exit. </p>
<p>&nbsp;<wbr>&nbsp;<wbr><code>&lt;file-or-directory&gt;</code>:<br />
You can run nodeunit on specific files or on all&nbsp;<wbr><i>*.js</i>&nbsp;<wbr>files inside </p>
<p>a directory.</p>
<h2>AUTHORS</h2>
<p> Written by Caolan McMahon and other nodeunit contributors.<br />
 Contributors list: <i><a rel="nofollow" href="http://github.com/caolan/nodeunit/contributors">http://github.com/caolan/nodeunit/contributors</a></i>.</p>
<h2>REPORTING BUGS</h2>
<p> Report nodeunit bugs to <i><a rel="nofollow" href="http://github.com/caolan/nodeunit/issues">http://github.com/caolan/nodeunit/issues</a></i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright © 2010 Caolan McMahon.<br />
 Nodeunit has been released under the MIT license:<br />
 <i><a rel="nofollow" href="http://github.com/caolan/nodeunit/raw/master/LICENSE">http://github.com/caolan/nodeunit/raw/master/LICENSE</a></i>.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-node/">node</a>(1) </p>
<h2>Index</h2>
