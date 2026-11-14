---
title: "rlm_attr_filter(5)"
name: "rlm_attr_filter"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_attr_filter/"
description: "rlm_attr_filter – FreeRADIUS Module"
---

<p>rlm_attr_filter &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_attr_filter</i> module exists for filtering certain attributes and values in received ( or transmitted ) radius packets. It gives the server a flexible framework to filter the attributes we send to or receive from home servers or NASes. This makes sense, for example, in an out-sourced dialup situation to various policy decisions, such as restricting a client to certain ranges of Idle-Timeout or Session-Timeout. Filter rules are normally defined and applied on a per-realm basis, where the realm is anything that is defined and matched based on the configuration of the <i>rlm_realm</i> module. Filter rules can optionally be applied using another attribute, by editing the <i>key</i> configuration for this module. In 2.0.1 and earlier versions, the &quot;accounting&quot; section filtered the Accounting-Request, even though it was documented as filtering the response. This issue has been fixed in version 2.0.2 and later versions. The &quot;preacct&quot; section may now be used to filter Accounting-Request packets. The &quot;accounting&quot; section now filters Accounting-Response packets. Administrators using &quot;attr_filter&quot; in the &quot;accounting&quot; section SHOULD move the reference to &quot;attr_filter&quot; from &quot;accounting&quot; to &quot;preacct&quot;. The file that defines the attribute filtering rules follows a similar syntax to the <i>users</i> file. There are a few differences however:</p>
<dl>
<dd>
<pre> There are no check-items allowed other than the name of the key.
 There can only be a single DEFAULT entry.
The rules for each entry are parsed to top to bottom, and an
attribute must pass *all* the rules which affect it in order to
make it past the filter. Order of the rules is important.
The operators and their purpose in defining the rules are as
follows:
<dl><dt><code>= </code>
<dd>THIS OPERATOR IS NOT ALLOWED. If used, and warning message is
printed and it is treated as ==
<dt><code>:= </code>
<dd>Set, this attribute and value will always be placed in the
output A/V Pairs. If the attribute exists, it is overwritten.
<dt><code>== </code>
<dd>Equal, value must match exactly.
<dt><code>=* </code>
<dd>Always Equal, allow all values for the specified attribute.
<dt><code>!* </code>
<dd>Never Equal, disallow all values for the specified attribute.
( This is redundant, as any A/V Pair not explicitly permitted
will be dropped ).
<dt><code>!= </code>
<dd>Not Equal, value must not match.
<dt><code>&gt;= </code>
<dd>Greater Than or Equal
<dt><code>&lt;= </code>
<dd>Less Than or Equal
<dt><code>&gt; </code>
<dd>Greater Than
<dt><code>&lt; </code>
<dd>Less Than
</dl>
If regular expressions are enabled the following operators are
also possible. ( Regular Expressions are included by default
unless your system doesn't support them, which should be rare ).
The value field uses standard regular expression syntax.
<dl><dt><code>=~ </code>
<dd>Regular Expression Equal
<dt><code>!~ </code>
<dd>Regular Expression Not Equal
</dl>
See the default <i>/etc/raddb/attrs</i> for working examples of
sample rule ordering and how to use the different operators.</pre>
</dl>
<p> The configuration items are:</p>
<dl>
<dt>file</p>
<dd>This specifies the location of the file used to load the filter rules. This file is used to filter the accounting response, packet before it is proxied, proxy response from the home server, or our response to the NAS.</p>
<dt>key</p>
<dd>Usually %{Realm} (the default). Can also be %{User-Name}, or other attribute that exists in the request. Note that the module always keys off of attributes in the request, and NOT in any other packet.</p>
<dt>relaxed</p>
<dd>If set to &#8216;yes&#8217;, then attributes which do not match any filter rules explicitly, will also be allowed. This behaviour may be overridden for an individual filter block using the Relax-Filter check item. The default for this configuration item is &#8216;no&#8217;.</dl>
<h2>Sections</h2>
<dl>
<dt>preacct</p>
<dd>Filters Accounting-Request packets.</p>
<dt>accounting</p>
<dd>Filters Accounting-Response packets.</p>
<dt>pre-proxy</p>
<dd>Filters Accounting-Request or Access-Request packets prior to proxying them.</p>
<dt>post-proxy</p>
<dd>Filters Accounting-Response, Access-Accept, Access-Reject, or Access-Challenge responses from a home server.</p>
<dt>authorize</p>
<dd>Filters Access-Request packets.</p>
<dt>post-auth</p>
<dd>Filters Access-Accept or Access-Reject packets.</dl>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf</i> <i>/etc/raddb/filter/*</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Chris Parker, cparker [at] segv.org</p>
