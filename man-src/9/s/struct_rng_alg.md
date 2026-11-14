---
title: "struct_rng_alg(9)"
name: "struct_rng_alg"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_rng_alg/"
description: "struct_rng_alg – random number generator definition"
---

<p>struct_rng_alg &#8211; random number generator definition</p>
<h2>Synopsis</h2>
<pre><code>struct rng_alg {
    int (*generate)(struct crypto_rng *tfm, const u8 *src, unsigned int slen, u8 *dst, unsigned int dlen);
    int (*seed)(struct crypto_rng *tfm, const u8 *seed, unsigned int slen);
    void (*set_ent)(struct crypto_rng *tfm, const u8 *data, unsigned int len);
    unsigned int seedsize;
    struct crypto_alg base;
};</code></pre>
<h2>Members</h2>
<p>generate</p>
<dl>
<dd>The function defined by this variable obtains a random number. The random number generator transform must generate the random number out of the context provided with this call, plus any additional data if provided to the call.</dl>
<p> seed</p>
<dl>
<dd>Seed or reseed the random number generator. With the invocation of this function call, the random number generator shall become ready for generation. If the random number generator requires a seed for setting up a new state, the seed must be provided by the consumer while invoking this function. The required size of the seed is defined with <i>seedsize</i> .</dl>
<p> set_ent</p>
<dl>
<dd>Set entropy that would otherwise be obtained from entropy source. Internal use only.</dl>
<p> seedsize</p>
<dl>
<dd>The seed size required for a random number generator initialization defined with this variable. Some random number generators does not require a seed as the seeding is implemented internally without the need of support by the consumer. In this case, the seed size is set to zero.</dl>
<p> base</p>
<dl>
<dd>Common crypto API algorithm data structure.</dl>
<h2>Authors</h2>
<p><code>Stephan Mueller</code> &lt;smueller [at] chronox.de&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Marek Vasut</code> &lt;marek [at] denx.de&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
