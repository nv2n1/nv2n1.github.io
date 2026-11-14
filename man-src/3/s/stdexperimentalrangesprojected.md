---
title: "stdexperimentalrangesprojected(3)"
name: "stdexperimentalrangesprojected"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalrangesprojected/"
---

std::experimental::ranges::projected - std::experimental::ranges::projected

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / ranges / iterator&gt;

    template &lt;Readable I, IndirectRegularUnaryInvocable&lt;I&gt; Proj&gt;

    struct projected {

    using value_type =

        std::remove_cv_t&lt;std::remove_reference_t&lt;ranges::indirect_result_of_t&lt;Proj &amp;(I)&gt;&gt;&gt;;

    ranges::indirect_result_of_t&lt;Proj &amp;(I)&gt; operator*() const;
};
(ranges TS) template &lt;WeaklyIncrementable I, class Proj&gt;

struct difference_type&lt;projected&lt;I, Proj&gt;&gt; {

    using type = ranges::difference_type_t&lt;I&gt;;
};</code></pre> 
The class template projected bundles a Readable type I and a function Proj into a new Readable type whose reference type is the result of applying Proj to the reference type of I. It exists solely to ease constraint specification, and so its operator*() may not be actually defined. 
