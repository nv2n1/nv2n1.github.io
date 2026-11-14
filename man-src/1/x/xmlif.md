---
title: "xmlif(1)"
name: "xmlif"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmlif/"
description: "xmlif – conditional processing instructions for XML"
---

<h2 class="name">NAME</h2>
<p> xmlif &#8211; conditional processing instructions for XML </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xmlif</code> [attrib=value&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>xmlif filters XML according to conditionalizing markup. This can be useful for formatting one of several versions of an XML document depending on conditions passed to the command. </p>
<p> Attribute/value pairs from the command line are matched against the attributes associated with certain processing instructions in the document. The instructions are &lt;?xmlif if?&gt; and its inverse &lt;?xmlif if not?&gt;, &lt;?xmlif elif?&gt; and its inverse &lt;?xmlif elif not?&gt;, &lt;?xmlif else?&gt;, and &lt;?xmlif fi?&gt;. </p>
<p> Argument/value pairs given on the command line are checked against the value of corresponding attributes in the conditional processing instructions. An `attribute match&#8217; happens if an attribute occurs in both the command-line arguments and the tag, and the values match. An `attribute mismatch&#8217; happens if an attribute occurs in both the command-line arguments and the tag, but the values do not match. </p>
<p> Spans between &lt;?xmlif if?&gt; or &lt;?xmlif elif?&gt; and the next conditional processing instruction at the same nesting level are passed through unaltered if there is at least one attribute match and no attribute mismatch; spans between &lt;?xmlif if not?&gt; and &lt;?xmlif elif not?&gt; and the next conditional processing instruction are passed otherwise. Spans between &lt;?xmlif else?&gt; and the next conditional-processing tag are passed through only if no previous span at the same level has been passed through. &lt;?xmlif if?&gt; and &lt;?xmlif fi?&gt; (and their `not&#8217; variants) change the current nesting level; &lt;?xmlif else?&gt; and &lt;?xmlif elif?&gt; do not. </p>
<p> All these processing instructions will be removed from the output produced. Aside from the conditionalization, all other input is passed through untouched; in particular, entity references are not resolved. </p>
<p> Value matching is by string equality, except that &quot;|&quot; in an attribute value is interpreted as an alternation character. Thus, saying foo=&#8217;red|blue&#8217; on the command line enables conditions red and blue. Saying color=&#8217;black|white&#8217; in a tag matches command-line conditions color=&#8217;black&#8217; and color=&#8217;white&#8217;. </p>
<p> Here is an example: </p>
<dl>
<dt>
<dd>
<pre><code>
Always issue this text.&lt; ? xmlif if condition = 'html' ? &gt;
                                                             Issue this text if 'condition=html' is given on the command line.&lt;
                           ? xmlif elif condition = 'pdf|ps' ? &gt;
                                                                       Issue this text if 'condition=pdf' or
                                                                   'condition=ps' is given on the command line.&lt;
                             ? xmlif else
                             ? &gt;
                                   Otherwise issue this text.&lt;
                             ? xmlif fi
                             ? &gt;
                                   Always issue this text.
</code></pre>
</dl>
<h2>AUTHOR</h2>
<p> <code>Eric S. Raymond</code> &lt;esr [at] snark.thyrsus.com&gt;</p>
<dl>
<dt>
<dd> Author of xmlif program</dl>
<h2>Index</h2>
