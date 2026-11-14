---
title: "stdexperimentalrangesindirectunaryinvocable(3)"
name: "stdexperimentalrangesindirectunaryinvocable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesindirectunaryinvocable/"
---

std::experimental::ranges::IndirectUnaryInvocable,std::experimental::ranges::IndirectRegularUnaryInvocable - std::experimental::ranges::IndirectUnaryInvocable,std::experimental::ranges::IndirectRegularUnaryInvocable

<h2>Synopsis</h2>

<pre><code>Defined in header &lt;experimental/ranges/iterator&gt;

template &lt;class F, class I&gt;

concept bool IndirectUnaryInvocable =

Readable&lt;I&gt; &amp;&amp; CopyConstructible&lt;F&gt; &amp;&amp;

Invocable&lt;F&amp;, ranges::value_type_t&lt;I&gt;&amp;&gt; &amp;&amp;

Invocable&lt;F&amp;, ranges::reference_t&lt;I&gt;&gt; &amp;&amp;                     (ranges TS)

Invocable&lt;F&amp;, ranges::iter_common_reference_t&lt;I&gt;&gt; &amp;&amp;

CommonReference&lt;

std::result_of_t&lt;F&amp;(ranges::value_type_t&lt;I&gt;&amp;)&gt;,

std::result_of_t&lt;F&amp;(ranges::reference_t&lt;I&gt;&amp;&amp;)&gt;&gt;;

template &lt;class F, class I&gt;

concept bool IndirectRegularUnaryInvocable =

Readable&lt;I&gt; &amp;&amp; CopyConstructible&lt;F&gt; &amp;&amp;

RegularInvocable&lt;F&amp;, ranges::value_type_t&lt;I&gt;&amp;&gt; &amp;&amp;

RegularInvocable&lt;F&amp;, ranges::reference_t&lt;I&gt;&gt; &amp;&amp;              (ranges TS)

RegularInvocable&lt;F&amp;, ranges::iter_common_reference_t&lt;I&gt;&gt; &amp;&amp;

CommonReference&lt;

std::result_of_t&lt;F&amp;(ranges::value_type_t&lt;I&gt;&amp;)&gt;,

std::result_of_t&lt;F&amp;(ranges::reference_t&lt;I&gt;&amp;&amp;)&gt;&gt;;
</code></pre> 
&nbsp;This section is incomplete 
&nbsp;Reason: add description and extra caveats 
