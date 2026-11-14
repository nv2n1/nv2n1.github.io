---
title: "stdexperimentalvector_aligned_tagstdexperimentalvector_aligned(3)"
name: "stdexperimentalvector_aligned_tagstdexperimentalvector_aligned"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdexperimentalvector_aligned_tagstdexperimentalvector_aligned/"
---

std::experimental::vector_aligned_tag,std::experimental::vector_aligned - std::experimental::vector_aligned_tag,std::experimental::vector_aligned

<h2>Synopsis</h2>

<pre><code>Defined in header&lt;experimental / simd&gt;

    struct vector_aligned_tag {
};

inline constexpr vector_aligned_tag vector_aligned{};</code></pre> 
This tag type indicates that the buffer of copy_from and copy_to is aligned to memory_alignment_v&lt;T, U&gt;, where the copy operation operates on the simd/simd_mask type T, and the buffer with element type U. 

<h2>Notes</h2>

This tag type allows to implement vector-aligned load and store. 

<h2>See also</h2>


