---
title: "slapo-valsort(5)"
name: "slapo-valsort"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-valsort/"
description: "slapo-valsort – Value Sorting overlay to slapd"
---

<p>slapo-valsort &#8211; Value Sorting overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The Value Sorting overlay can be used with a backend database to sort the values of specific multi-valued attributes within a subtree. The sorting occurs whenever the attributes are returned in a search response. Sorting can be specified in ascending or descending order, using either numeric or alphanumeric sort methods. Additionally, a &quot;weighted&quot; sort can be specified, which uses a numeric weight prepended to the attribute values. The weighted sort is always performed in ascending order, but may be combined with the other methods for values that all have equal weights. The weight is specified by prepending an integer weight {&lt;<i>weight</i>&gt;} in front of each value of the attribute for which weighted sorting is desired. This weighting factor is stripped off and not returned in search results unless the valsort control is specified (1.3.6.1.4.1.4203.666.5.14). The valsort control requires a value consisting of a Sequence that contains a boolean flag. The weighting factor is only returned if the boolean value is TRUE. In <code><a href="/docs/linux/man/3-lber-encode/">lber-encode</a></code>(3) format, the required value must conform to &quot;{b}&quot; syntax. </p>
<h2>Configuration</h2>
<p>These <i>slapd.conf</i> options apply to the Value Sorting overlay. They should appear after the <code>overlay</code> directive.</p>
<dl>
<dt>valsort-attr &lt;<i>attribute</i>&gt; &lt;<i>baseDN</i>&gt; (&lt;<i>sort-method</i>&gt; | weighted [&lt;<i>sort-method</i>&gt;])</p>
<dd>Configure a sorting method for the specified <i>attribute</i> in the subtree rooted at <i>baseDN</i>. The <i>sort-method</i> may be one of <code>alpha-ascend</code>, <code>alpha-descend</code>, <code>numeric-ascend</code>, or <code>numeric-descend</code>. If the special <code>weighted</code> method is specified, a secondary <i>sort-method</i> may also be specified. It is an error to specify an alphanumeric <i>sort-method</i> for an attribute with Integer or NumericString syntax, and it is an error to specify a numeric <i>sort-method</i> for an attribute with a syntax other than Integer or NumericString.</dl>
<h2>Examples</h2>
<pre> database bdb
 suffix dc=example,dc=com
 ...
 overlay valsort
 valsort-attr member ou=groups,dc=example,dc=com alpha-ascend</pre>
<p>To invoke <code><a href="/docs/linux/man/1-ldapsearch/">ldapsearch</a></code>(1) with the valsort control, the control value must be set appropriately. The following octets represent the desired &quot;{b}&quot; encoding: </p>
<pre> 0x30 0x03 0x01 0x01 0xff</pre>
<p>The control can be sent from the command-line using the base64 encoding of the value: </p>
<pre> ldapsearch -E 1.3.6.1.4.1.4203.666.5.14=::MAMBAf8=</pre>
<h2>Files</h2>
<dl>
<dt><i>/etc/openldap/slapd.conf</i></p>
<dd>default <code>slapd</code> configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5).</p>
<h2>Acknowledgements</h2>
<p>This module was written in 2005 by Howard Chu of Symas Corporation. The work was sponsored by Stanford University.</p>
