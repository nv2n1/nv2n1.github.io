---
title: "stdexperimentaloveraligned_tagstdexperimentaloveraligned(3)"
name: "stdexperimentaloveraligned_tagstdexperimentaloveraligned"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentaloveraligned_tagstdexperimentaloveraligned/"
---

std::experimental::overaligned_tag,std::experimental::overaligned - std::experimental::overaligned_tag,std::experimental::overaligned

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / simd&gt;

    template &lt;std::size_t N&gt;

    struct overaligned_tag {
};
template &lt;std::size_t N&gt;

inline constexpr overaligned_tag&lt;N&gt; overaligned{};</code></pre> 
This tag type indicates that the buffer of copy_from and copy_to is aligned to N. 

<h2>See also</h2>


