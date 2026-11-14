---
title: "npm-restart(1)"
name: "npm-restart"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-restart/"
description: "npm-restart – Restart a package"
---

<h2 class="name">NAME</h2>
<p> <code>npm-restart</code> &#8211; Restart a package </p>
<h3>Synopsis</h3>
<dl>
<dt>
<dd>
<pre>
npm restart [-- &lt;args&gt;]
</pre>
</dl>
<h3>Description</h3>
<p> This restarts a package. </p>
<p> This runs a package&#8217;s &quot;stop&quot;, &quot;restart&quot;, and &quot;start&quot; scripts, and associated pre- and post- scripts, in the order given below:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.</p>
<dd> prerestart</p>
<dt>2.</p>
<dd> prestop</p>
<dt>3.</p>
<dd> stop</p>
<dt>4.</p>
<dd> poststop</p>
<dt>5.</p>
<dd> restart</p>
<dt>6.</p>
<dd> prestart</p>
<dt>7.</p>
<dd> start</p>
<dt>8.</p>
<dd> poststart</p>
<dt>9.</p>
<dd> postrestart </p>
</dl>
</dl>
<h3>Note</h3>
<p> Note that the &quot;restart&quot; script is run <code>in addition to</code> the &quot;stop&quot; and &quot;start&quot; scripts, not instead of them. </p>
<p> This is the behavior as of <code>npm</code> major version 2. A change in this behavior will be accompanied by an increase in major version number</p>
<h3>See Also</h3>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> npm help run-script</p>
<dt>&bull;</p>
<dd> npm help scripts</p>
<dt>&bull;</p>
<dd> npm help test</p>
<dt>&bull;</p>
<dd> npm help start</p>
<dt>&bull;</p>
<dd> npm help stop</p>
<dt>&bull;</p>
<dd> npm help restart </p>
</dl>
</dl>
<h2>Index</h2>
