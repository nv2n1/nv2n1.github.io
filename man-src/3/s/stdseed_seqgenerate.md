---
title: "stdseed_seqgenerate(3)"
name: "stdseed_seqgenerate"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stdseed_seqgenerate/"
---

std::seed_seq::generate - std::seed_seq::generate

<h2>Synopsis</h2>

<pre><code>template &lt;class RandomIt&gt;
(since C++ 11)

    void generate(RandomIt begin, RandomIt end);</code></pre> 
Fills the range [begin, end) with unsigned integer values i, 0 ≤ i &lt; 232 
, based on the data originally provided in the constructor of this seed_seq. The produced values are distributed over the entire 32-bit range even if the initial values were strongly biased. 
The following algorithm is used (adapted from the initialization sequence of the Mersenne Twister generator by Makoto_Matsumoto_and_Takuji_Nishimura, incorporating the improvements made by Mutsuo_Saito_in_2007) 
* If begin == end, do nothing. Otherwise, 
* First, set each element of the output range to the value 0x8b8b8b8b 
* Transform the elements of the output range according to the following algorithm: 
For k = 0,..., m-1 
where m=max(s+1, n) 
and n=end-begin 
and s=v.size() 
and v is the private container holding the values originally provided by the constructor of this seed_seq object, 1. begin[k+p] += r1

2. begin[k+q] += r2

3. begin[k] = r2, 
where p=(n-t)/2 
and q=p+t 
and t=(n &gt;= 623) ? 11 : (n &gt;= 68) ? 7 : (n &gt;= 39) ? 5 : (n &gt;= 7) ? 3 : (n - 1) / 2 
and r1=1664525 * T(begin[k]^begin[k+p]^begin[k−1]) 
and T(x) = x ^ (x &gt;&gt; 27) 
and r2=r1+s if k==0, r2=r1 + k%n + v[k-1] if 0&lt;k&lt;=s, r2=r1 + k%n if k&gt;s. 
For k = m,..., m+n-1, 1. begin[k+p] ^= r3

2. begin[k+q] ^= r4

3. begin[k]=r4 
where r3 = 1566083941 * T(begin[k]+begin[k+p]+begin[k-1]) 
and r4=r3 - k%n 
where all calculations are performed modulo 232 
and where the indexing of the output range (begin[x]) is taken modulo n. 

<h2>Parameters</h2>

begin, end - mutable random-access iterators whose std::iterator_traits&lt;&gt;::value_type is an unsigned integer type suitable for storing 32-bit values

<h2>Type requirements</h2>

- 
RandomIt must meet the requirements of LegacyRandomAccessIterator.

<h2>Return value</h2>

none, the results are written to the [begin, end) range. 

<h2>Exceptions</h2>

Only throws if the operations on begin and end throw.

<h2>Example</h2>

// Run this code <pre><code>#include &lt;random&gt;

#include &lt;iostream&gt;
int main()

{
    std::seed_seq seq({1, 2, 3, 4, 5});
    std::vector&lt;std::uint32_t&gt; seeds(10);
    seq.generate(seeds.begin(), seeds.end());

    // Step 1: fill with 0x8b8b8b8b

    // seeds = {2341178251, 2341178251, 2341178251, 2341178251, 2341178251,

    //          2341178251, 2341178251, 2341178251, 2341178251, 2341178251 }

    //

    // Step 2:

    // n = 10, s = 5, t = 3, p = 3, q = 6, m = 10

    //

    // First iteration, k = 0; r1 = 1371501266, r2 = 1371501271

    //

    // seeds = {1371501271, 2341178251, 2341178251, 3712679517, 2341178251,

    //          2341178251, 3712679522, 2341178251, 2341178251, 2341178251 }

    //

    // Iterations from k = 1 to k = 5 (r2 = r1 + k%n + v[k-1])

    //

    // r1 = 2786190137, 3204727651, 4173325571, 1979226628, 401983366

    // r2 = 2786190139, 3204727655, 4173325577, 1979226636, 401983376

    //

    // seeds = {3350727907, 3188173515, 3204727655, 4173325577, 1979226636,

    //           401983376, 3591037797, 2811627722, 1652921976, 2219536532 }

    //

    // Iterations from k = 6 to k = 9 (r2 = r1 + k%n)

    //

    // r1 = 2718637909, 1378394210, 2297813071, 1608643617

    // r2 = 2718637915, 1378394217, 2297813079, 1608643626

    //

    // seeds = { 434154821, 1191019290, 3237041891, 1256752498, 4277039715,

    //          2010627002, 2718637915, 1378394217, 2297813079, 1608643626 }

    //

    // Step 3

    // iterations from k = 10 to k = 19, using ^= to modify the output

    //

    // r1 = 1615303485, 3210438310, 893477041, 2884072672, 1918321961,

    // r2 = 1615303485, 3210438309, 893477039, 2884072669, 1918321957

    //

    // seeds = { 303093272, 3210438309,  893477039, 2884072669, 1918321957,

    //          1117182731, 1772877958, 2669970405, 3182737656, 4094066935 }

    //

    // r1 =  423054846, 46783064, 3904109085, 1534123446, 1495905687

    // r2 =  423054841, 46783058, 3904109078, 1534123438, 1495905678

    //

    // seeds = { 4204997637, 4246533866, 1856049002, 1129615051, 690460811,

    //           1075771511,   46783058, 3904109078, 1534123438, 1495905678 }
    for (std::uint32_t n : seeds)
        std::cout &lt;&lt; n &lt;&lt; '\n';
}
</code></pre>

<h2>Output:</h2>

&nbsp;<wbr>&nbsp;4204997637 
&nbsp;<wbr>&nbsp;4246533866 
&nbsp;<wbr>&nbsp;1856049002 
&nbsp;<wbr>&nbsp;1129615051 
&nbsp;<wbr>&nbsp;690460811 
&nbsp;<wbr>&nbsp;1075771511 
&nbsp;<wbr>&nbsp;46783058 
&nbsp;<wbr>&nbsp;3904109078 
&nbsp;<wbr>&nbsp;1534123438 
&nbsp;<wbr>&nbsp;1495905678
