---
title: "git-check-attr(1)"
name: "git-check-attr"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-check-attr/"
description: "git-check-attr – Display gitattributes information"
---

<h2 class="name">NAME</h2>
<p> git-check-attr &#8211; Display gitattributes information </p>
<h2>SYNOPSIS</h2>
<pre><code>
git check - attr[-a | --all | &lt;attr&gt;...][--]&lt;pathname&gt;... git check - attr-- stdin[-z][-a | --all | &lt;attr&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> For every pathname, this command will list if each attribute is <i>unspecified</i>, <i>set</i>, or <i>unset</i> as a gitattribute on that pathname.</p>
<h2>OPTIONS</h2>
<p> -a, &#8211;all</p>
<dl>
<dt>
<dd> List all attributes that are associated with the specified paths. If this option is used, then <i>unspecified</i> attributes will not be included in the output.</dl>
<p> &#8211;cached</p>
<dl>
<dt>
<dd> Consider <code>.gitattributes</code> in the index only, ignoring the working tree.</dl>
<p> &#8211;stdin</p>
<dl>
<dt>
<dd> Read pathnames from the standard input, one per line, instead of from the command-line.</dl>
<p> -z</p>
<dl>
<dt>
<dd> The output format is modified to be machine-parsable. If <code>&#8211;stdin</code> is also given, input paths are separated with a NUL character instead of a linefeed character.</dl>
<p> &#8212;</p>
<dl>
<dt>
<dd> Interpret all preceding arguments as attributes and all following arguments as path names.</dl>
<p> If none of <code>&#8211;stdin</code>, <code>&#8211;all</code>, or <code>&#8212;</code> is used, the first argument will be treated as an attribute and the rest of the arguments as pathnames.</p>
<h2>OUTPUT</h2>
<p> The output is of the form: &lt;path&gt; COLON SP &lt;attribute&gt; COLON SP &lt;info&gt; LF </p>
<p> unless <code>-z</code> is in effect, in which case NUL is used as delimiter: &lt;path&gt; NUL &lt;attribute&gt; NUL &lt;info&gt; NUL </p>
<p> &lt;path&gt; is the path of a file being queried, &lt;attribute&gt; is an attribute being queried and &lt;info&gt; can be either: </p>
<p> <i>unspecified</i></p>
<dl>
<dt>
<dd> when the attribute is not defined for the path.</dl>
<p> <i>unset</i></p>
<dl>
<dt>
<dd> when the attribute is defined as false.</dl>
<p> <i>set</i></p>
<dl>
<dt>
<dd> when the attribute is defined as true.</dl>
<p> &lt;value&gt;</p>
<dl>
<dt>
<dd> when a value has been assigned to the attribute.</dl>
<p> Buffering happens as documented under the <code>GIT_FLUSH</code> option in <code><a href="/docs/linux/man/1-git/">git</a></code>(1). The caller is responsible for avoiding deadlocks caused by overfilling an input buffer or reading from an empty output buffer.</p>
<h2>EXAMPLES</h2>
<p> In the examples, the following <i>.gitattributes</i> file is used: </p>
<dl>
<dt>
<dd>
<pre>
*.java diff=java -crlf myAttr
NoMyAttr.java !myAttr
README caveat=unspecified
</pre>
</dl>
<dl>
<dt>
<dd> &bull; Listing a single attribute:</dl>
<dl>
<dt>
<dd>
<pre>
$ git check-attr diff org/example/MyClass.java
org/example/MyClass.java: diff: java
</pre>
</dl>
<dl>
<dt>
<dd> &bull; Listing multiple attributes for a file:</dl>
<dl>
<dt>
<dd>
<pre>
$ git check-attr crlf diff myAttr -- org/example/MyClass.java
org/example/MyClass.java: crlf: unset
org/example/MyClass.java: diff: java
org/example/MyClass.java: myAttr: set
</pre>
</dl>
<dl>
<dt>
<dd> &bull; Listing all attributes for a file:</dl>
<dl>
<dt>
<dd>
<pre>
$ git check-attr --all -- org/example/MyClass.java
org/example/MyClass.java: diff: java
org/example/MyClass.java: myAttr: set
</pre>
</dl>
<dl>
<dt>
<dd> &bull; Listing an attribute for multiple files:</dl>
<dl>
<dt>
<dd>
<pre>
$ git check-attr myAttr -- org/example/MyClass.java org/example/NoMyAttr.java
org/example/MyClass.java: myAttr: set
org/example/NoMyAttr.java: myAttr: unspecified
</pre>
</dl>
<dl>
<dt>
<dd> &bull; Not all values are equally unambiguous:</dl>
<dl>
<dt>
<dd>
<pre>
$ git check-attr caveat README
README: caveat: unspecified
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-gitattributes/">gitattributes</a></code>(5).</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
