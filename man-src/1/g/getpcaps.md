---
title: "getpcaps(1)"
name: "getpcaps"
section: "1"
letter: "g"
url: "/docs/linux/man/1-getpcaps/"
description: "getpcaps – List Process Capabilities"
---

<h2 class="name">NAME</h2>
<p> getpcaps &#8211; List Process Capabilities </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>getpcaps</code> &lt;pid&gt; [&lt;pid&gt; &#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>getpcaps</code></p>
<dd>is a simple utility to display the capabilities on the queried process(es). The capabilities are displayed in the <a href="/docs/linux/man/3-cap_from_text/">cap_from_text</a>(3) format, portions of which are reproduced in the section &quot;TEXTUAL REPRESENTATION&quot; below.</p>
<h2>TEXTUAL REPRESENTATION</h2>
<p> A textual representation of capability sets consists of one or more whitespace-separated <i>clauses</i>. Each clause specifies some operations on a capability set; the set starts out with all capabilities lowered, and the meaning of the string is the state of the capability set after all the clauses have been applied in order. </p>
<p> Each clause consists of a list of comma-separated capability names (or the word `<code>all</code>&#8216;), followed by an <i>action-list</i>. An action-list consists of a sequence of <i>operator flag</i> pairs. Legal operators are: `<code>=</code>&#8216;, &#8216;<code>+</code>&#8216;, and `<code>&#8211;</code>&#8216;. Legal flags are: `<code>e</code>&#8216;, `<code>i</code>&#8216;, and `<code>p</code>&#8216;. These flags are case-sensitive and specify the Effective, Inheritable and Permitted sets respectively. </p>
<p> In the capability name lists, all names are case-insensitive. The special name `<code>all</code>&#8216; specifies all capabilities; it is equivalent to a list naming every capability individually. </p>
<p> Unnamed capabilities can also be specified by number. This feature ensures that libcap can support capabilities that were not allocated at the time libcap was compiled. However, generally upgrading libcap will add names for recently allocated capabilities. </p>
<p> The `<code>=</code>&#8216; operator indicates that the listed capabilities are first reset in all three capability sets. The subsequent flags (which are optional when associated with this operator) indicate that the listed capabilities for the corresponding set are to be raised. For example: &quot;all=p&quot; means lower every capability in the Effective and Inheritable sets but raise all of the Permitted capabilities; or, &quot;cap_fowner=ep&quot; means raise the Effective and Permitted override-file-ownership capability, while lowering this Inheritable capability. </p>
<p> In the case that the leading operator is `<code>=</code>&#8216;, and no list of capabilities is provided, the action-list is assumed to refer to `all&#8217; capabilities. For example, the following three clauses are equivalent to each other (and indicate a completely empty capability set): &quot;all=&quot;; &quot;=&quot;; &quot;cap_chown,&lt;every-other-capability&gt;=&quot;. </p>
<p> The operators, `+&#8217; and `-&#8216; both require an explicit preceding capability list and one or more explicit trailing flags. The `+&#8217; operator will raise all of the listed capabilities in the flagged capability sets. The `-&#8216; operator will lower all of the listed capabilities in the flagged capability sets. For example: &quot;all+p&quot; will raise all of the Permitted capabilities; &quot;cap_fowner+p-i&quot; will raise the override-file-ownership capability in the Permitted capability set and lower this Inheritable capability; &quot;cap_fowner+pe-i&quot; and &quot;cap_fowner=+pe&quot; are equivalent.</p>
<h2>FILES</h2>
<p> None</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cap_from_text/">cap_from_text</a></code>(3).</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997-8,2007 Andrew G. Morgan &lt;morgan [at] kernel.org&gt; </p>
<h2>Index</h2>
