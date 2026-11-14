---
title: "rlm_policy(5)"
name: "rlm_policy"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_policy/"
description: "rlm_policy – FreeRADIUS Module"
---

<p>rlm_policy &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <code>rlm_policy</code> module implements a simple &quot;policy&quot; language. The policy language implemented by this module is simple, and specific to RADIUS. It does not implement variables, arrays, loops, goto&#8217;s, or any other feature of a real language. If those features are needed for your system, we suggest using <code>rlm_perl</code>. What the policy module implements is a simple way to look for attributes in the request packet (or other places), and to add attributes to the reply packet (or other places) based on those decisions. Where the module shines is that it is significantly more flexible than the old-style <code>users</code> file. The module has one configuration item:</p>
<dl>
<dt>filename</p>
<dd>The file where the policy is stored. </p>
<h2>Policy Language</h2>
<h3>Named policies</h3>
<p>The policy is composed of a series of named policies. The following example defines a policy named &quot;foo&quot;. </p>
<dl>
<dd>
<pre> policy foo {
<br>
 ...
<br>
 }</pre>
</dl>
<p> Policy names MAY NOT be the same as attributes in the dictionary. Defining a policy with the same name as a dictionary attribute will cause an error message to be printed, and the policy will not be loaded. </p>
<p> When the policy module is listed in a module section like &quot;authorize&quot;, the module calls a policy named &quot;authorize&quot;. The &quot;post-auth&quot;, etc. sections behave the same. These names cannot be changed. </p>
<dl>
<dd>
<pre> include &quot;policy.txt&quot;</pre>
</dl>
<p> The filename must be in a double-quoted string, and is assumed to be relative to the location of the current file. If the filename ends with a &#8216;/&#8217;, then it is assumed to be a directory, and all files in that directory will be read. </p>
<dl>
<dd>
<pre> include &quot;dir/&quot;</pre>
</dl>
<p> All file in &quot;dir/&quot; will be read and included into the policy definition. Any dot files (&quot;.&quot;, &quot;..&quot;, etc.) will not be included, however.</p>
<h3>Including multiple files</h3>
<p>The main file referred to from the <i>radiusd.conf</i> may include one or more other files, as in the following example.</p>
<h3>Referencing a named policy</h3>
<p>The following example references a named policy</p>
<dl>
<dd>
<pre> foo()</pre>
</dl>
<p> While the brackets are required, no arguments may be passed.</p>
<h3>Conditions</h3>
<p>&quot;if&quot; statements are supported. </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>if (expression) {</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}</p>
<p> and &quot;else&quot; </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>if (expression) {</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>} else {</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}</p>
<p> also, &quot;else if&quot; </p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>if (expression) {</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>} else if (expression) {</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}</p>
<h3>Expressions within if statements</h3>
<p>Always have to have brackets around them. Sorry. </p>
<p> The following kinds of expressions may be used, with their meanings.</p>
<dl>
<dt>(attribute-reference)</p>
<dd>TRUE if the referenced attribute exists, FALSE otherwise. See below for details on attribute references.</p>
<dt>(!(expression))</p>
<dd>FALSE if the expression returned TRUE, and TRUE if the nested expression returned FALSE.</p>
<dt>(attribute-reference == value)</p>
<dd>Compares the attribute to the value. The operators here can be &quot;==&quot;, &quot;!=&quot;, &quot;=~&quot;, &quot;!~&quot;, &quot;&lt;&quot;, &quot;&lt;=&quot;, &quot;&gt;&quot;, and &quot;&gt;=&quot;.</p>
<dt>(string1 == string2)</p>
<dd>A special case of the above. The &quot;string1&quot; is dynamically expanded at run time, while &quot;string2&quot; is not. The operators here can be &quot;==&quot;, &quot;!=&quot;, &quot;=~&quot;,and &quot;!~&quot;. Of these, the most useful is &quot;=~&#8217;, which lets you do things like (&quot;%{ldap:query&#8230;}&quot; =~ &quot;foo=(.*) &quot;). The results of the regular expression match are put into %{1}, and can be used later. See &quot;doc/variables.txt&quot; for more information.</p>
<dt>((expression1) || (expression2))</p>
<dd>Short-circuit &quot;or&quot;. If expression1 is TRUE, expression2 is not evaluated.</p>
<dt>((expression1) &amp;&amp; (expression2))</p>
<dd>Short-circuit &quot;and&quot;. If expression1 is FALSE, expression2 is not evaluated.</p>
<dt>Limitations.</p>
<dd>The &amp;&amp; and || operators have equal precedence. You can&#8217;t call a function as a expression.</dl>
<h3>Attribute references</h3>
<p>Attribute references are:</p>
<dl>
<dt>Attribute-Name</p>
<dd>Refers to an attribute of that name in the Access-Request or Accounting-Request packet. May also refer to &quot;server-side&quot; attributes, which are not documented anywhere.</p>
<dt>request:Attribute-Name</p>
<dd>An alternate way of referencing an attribute in the request packet.</dl>
<dl>
<dt>reply:Attribute-Name</p>
<dd>An attribute in the reply packet</dl>
<dl>
<dt>proxy-request:Attribute-Name</p>
<dd>An attribute in the Access-Request or Accounting-Request packet which will be proxied to the home server.</dl>
<dl>
<dt>proxy-reply:Attribute-Name</p>
<dd>An attribute in the Access-Accept or other packet which was received from a home server.</dl>
<dl>
<dt>control:Attribute-Name</p>
<dd>An attribute in the per-request configuration and control attributes. Also known as &quot;check&quot; attributes (doc/variables.txt).</dl>
<h3>Adding attributes to reply packet (or other location)</h3>
<p><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>reply .= {</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>attribute-name = value</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>attribute-name = value</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>}</p>
<p> The first name can be &quot;request&quot;, &quot;reply&quot;, &quot;control&quot;, &quot;proxy-request&quot;, or &quot;proxy-reply&quot;. </p>
<p> The operator can be </p>
<p>&nbsp;<wbr>.=&nbsp;<wbr>&#8211; appends attributes to end of the list </p>
<p>&nbsp;<wbr>:=&nbsp;<wbr>&#8211; replaces existing list with the attributes in the list&nbsp;<wbr>(bad idea) </p>
<p>&nbsp;<wbr>=&nbsp;<wbr>&#8211; use operators from&nbsp;<wbr>&quot;attribute&nbsp;<wbr>=&nbsp;<wbr>value&quot;&nbsp;<wbr>to decide what to do.&nbsp;<wbr>(see&nbsp;<wbr>&quot;users&quot;) </p>
<p> The block must contain only attributes and values. Nothing else is permitted.</p>
<h2>Sections</h2>
<p><code>authorize</code> <code>post-auth</code> <code>pre-proxy</code> <code>post-proxy</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-users/">users</a></code>(5), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Alan DeKok &lt;aland [at] ox.org&gt;</p>
