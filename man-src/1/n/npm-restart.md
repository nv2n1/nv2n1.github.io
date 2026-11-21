---

title: "npm-restart(1)"
name: "npm-restart"
section: "1"
letter: "n"
url: "/docs/linux/man/1-npm-restart/"
description: "npm-restart – Restart a package"
---

<p> <code>npm-restart</code> &#8211; Restart a package </p>
<h3>Synopsis</h3>
<dl>
<dt>
</dt><dd>
<pre>
npm restart [-- &lt;args&gt;]
</pre>
</dd></dl>
<h3>Description</h3>
<p> This restarts a package. </p>
<p> This runs a package&#8217;s &quot;stop&quot;, &quot;restart&quot;, and &quot;start&quot; scripts, and associated pre- and post- scripts, in the order given below:</p>
<dl>
<dl>
<dt>1.</dt>
<dd> prerestart</dd>
<dt>2.</dt>
<dd> prestop</dd>
<dt>3.</dt>
<dd> stop</dd>
<dt>4.</dt>
<dd> poststop</dd>
<dt>5.</dt>
<dd> restart</dd>
<dt>6.</dt>
<dd> prestart</dd>
<dt>7.</dt>
<dd> start</dd>
<dt>8.</dt>
<dd> poststart</dd>
<dt>9.</dt>
<dd> postrestart </dd>
</dl>
</dl>
<h3>Note</h3>
<p> Note that the &quot;restart&quot; script is run <code>in addition to</code> the &quot;stop&quot; and &quot;start&quot; scripts, not instead of them. </p>
<p> This is the behavior as of <code>npm</code> major version 2. A change in this behavior will be accompanied by an increase in major version number</p>
<h3>See Also</h3>
<dl>
<dl>
<dt>&bull;</dt>
<dd> npm help run-script</dd>
<dt>&bull;</dt>
<dd> npm help scripts</dd>
<dt>&bull;</dt>
<dd> npm help test</dd>
<dt>&bull;</dt>
<dd> npm help start</dd>
<dt>&bull;</dt>
<dd> npm help stop</dd>
<dt>&bull;</dt>
<dd> npm help restart </dd>
</dl>
</dl>
