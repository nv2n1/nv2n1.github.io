---
title: "bitstring(3)"
name: "bitstring"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bitstring/"
description: "bit_alloc bit_clear bit_decl bit_ffs bit_nclear bit_nset bit_set bitstr_size bit_test – bit-string manipulation macros"
---

<h2 class="name">NAME</h2>
<p> <code>bit_alloc</code> <code>bit_clear</code> <code>bit_decl</code> <code>bit_ffs</code> <code>bit_nclear</code> <code>bit_nset</code> <code>bit_set</code> <code>bitstr_size</code> <code>bit_test</code> &#8211; bit-string manipulation macros </p>
<h2>SYNOPSIS</h2>
<p> In bsd/bitstring.h Ft bitstr_t * Fn bit_alloc int nbits Ft void Fn bit_decl bitstr_t *name int nbits Ft void Fn bit_clear bitstr_t *name int bit Ft void Fn bit_ffc bitstr_t *name int nbits int *value Ft void Fn bit_ffs bitstr_t *name int nbits int *value Ft void Fn bit_nclear bitstr_t *name int start int stop Ft void Fn bit_nset bitstr_t *name int start int stop Ft void Fn bit_set bitstr_t *name int bit Ft int Fn bitstr_size int nbits Ft int Fn bit_test bitstr_t *name int bit</p>
<h2>DESCRIPTION</h2>
<p> These macros operate on strings of bits. </p>
<p> The macro Fn bit_alloc returns a pointer of type &#8220;Fa bitstr_t * &#8221; to sufficient space to store Fa nbits bits, or <code>NULL</code> if no space is available. </p>
<p> The macro Fn bit_decl allocates sufficient space to store Fa nbits bits on the stack. </p>
<p> The macro Fn bitstr_size returns the number of elements of type Fa bitstr_t necessary to store Fa nbits bits. This is useful for copying bit strings. </p>
<p> The macros Fn bit_clear and Fn bit_set clear or set the zero-based numbered bit Fa bit , in the bit string <i>name</i> </p>
<p> The Fn bit_nset and Fn bit_nclear macros set or clear the zero-based numbered bits from Fa start through Fa stop in the bit string <i>name</i> </p>
<p> The Fn bit_test macro evaluates to non-zero if the zero-based numbered bit Fa bit of bit string Fa name is set, and zero otherwise. </p>
<p> The Fn bit_ffs macro stores in the location referenced by Fa value the zero-based number of the first bit set in the array of Fa nbits bits referenced by Fa name . If no bits are set, the location referenced by Fa value is set to -1. </p>
<p> The macro Fn bit_ffc stores in the location referenced by Fa value the zero-based number of the first bit not set in the array of Fa nbits bits referenced by Fa name . If all bits are set, the location referenced by Fa value is set to -1. </p>
<p> The arguments to these macros are evaluated only once and may safely have side effects.</p>
<h2>EXAMPLES</h2>
<blockquote>
<pre><code>
#include &lt;bsd/bitstring.h&gt;
#include &lt;limits.h&gt;
...
#define LPR_BUSY_BIT 0
#define LPR_FORMAT_BIT 1
#define LPR_DOWNLOAD_BIT 2
    ...
#define LPR_AVAILABLE_BIT 9
#define LPR_MAX_BITS 10
    make_lpr_available()
{
    bitstr_t bit_decl(bitlist, LPR_MAX_BITS);
    ... bit_nclear(bitlist, 0, LPR_MAX_BITS - 1);
    ... if (!bit_test(bitlist, LPR_BUSY_BIT))
    {
        bit_clear(bitlist, LPR_FORMAT_BIT);
        bit_clear(bitlist, LPR_DOWNLOAD_BIT);
        bit_set(bitlist, LPR_AVAILABLE_BIT);
    }
}
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-malloc/">malloc</a>(3)</p>
<h2>HISTORY</h2>
<p> The <code>bitstring</code> functions first appeared in BSD 4.4 </p>
<h2>Index</h2>
