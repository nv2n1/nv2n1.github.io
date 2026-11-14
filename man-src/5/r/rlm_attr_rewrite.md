---
title: "rlm_attr_rewrite(5)"
name: "rlm_attr_rewrite"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rlm_attr_rewrite/"
description: "rlm_attr_rewrite – FreeRADIUS Module"
---

<p>rlm_attr_rewrite &#8211; FreeRADIUS Module</p>
<h2>Description</h2>
<p>The <i>rlm_attr_rewrite</i> module provides functionality to rewrite data in radius packets on the fly. This can be useful in authorization and accounting functions. The main configuration items to be aware of are:</p>
<dl>
<dt>attribute</p>
<dd>The name of the attribute that you want to be rewritten</p>
<dt>searchfor</p>
<dd>String to be replaced.</p>
<dt>searchin</p>
<dd>Where to look for the attribute. Valid values are: <code>packet,</code> <code>reply,</code> <code>proxy,</code> <code>proxy_reply,</code> <code>config</code></p>
<dt>replacewith</p>
<dd>String to replace &quot;searchfor&quot;.</p>
<dt>append</p>
<dd>Set to yes or no. If set to yes then the replace string will be appended to the original string.</p>
<dt>ignore_case</p>
<dd>Set to yes or no. Determines whether search will be case insensitive or case sensitive.</p>
<dt>new_attribute</p>
<dd>Set to yes or no. If set to yes, then new attribute will be created with values from &quot;searchin&quot; and &quot;replacewith&quot;. Other options will be ignored.</p>
<dt>max_matches</p>
<dd>Set the max number of attributes to match against. This is useful if you need to rewrite the value in multiple Vendor Specific Attributes.</dl>
<h2>Sections</h2>
<p><code>authorization,</code> <code>authentication,</code> <code>postauthentication,</code> <code>preaccounting,</code> <code>accounting,</code> <code>preproxy,</code> <code>postproxy</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Chris Parker, cparker [at] segv.org</p>
