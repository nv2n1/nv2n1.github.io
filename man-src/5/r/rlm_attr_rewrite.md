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
<dt>attribute</dt>
<dd>The name of the attribute that you want to be rewritten</dd>
<dt>searchfor</dt>
<dd>String to be replaced.</dd>
<dt>searchin</dt>
<dd>Where to look for the attribute. Valid values are: <code>packet,</code> <code>reply,</code> <code>proxy,</code> <code>proxy_reply,</code> <code>config</code></dd>
<dt>replacewith</dt>
<dd>String to replace &quot;searchfor&quot;.</dd>
<dt>append</dt>
<dd>Set to yes or no. If set to yes then the replace string will be appended to the original string.</dd>
<dt>ignore_case</dt>
<dd>Set to yes or no. Determines whether search will be case insensitive or case sensitive.</dd>
<dt>new_attribute</dt>
<dd>Set to yes or no. If set to yes, then new attribute will be created with values from &quot;searchin&quot; and &quot;replacewith&quot;. Other options will be ignored.</dd>
<dt>max_matches</dt>
<dd>Set the max number of attributes to match against. This is useful if you need to rewrite the value in multiple Vendor Specific Attributes.</dd></dl>
<h2>Sections</h2>
<p><code>authorization,</code> <code>authentication,</code> <code>postauthentication,</code> <code>preaccounting,</code> <code>accounting,</code> <code>preproxy,</code> <code>postproxy</code></p>
<h2>Files</h2>
<p><i>/etc/raddb/radiusd.conf</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-radiusd/">radiusd</a></code>(8), <code><a href="/docs/linux/man/5-radiusd-conf/">radiusd.conf</a></code>(5)</p>
<h2>Author</h2>
<p>Chris Parker, cparker [at] segv.org</p>
