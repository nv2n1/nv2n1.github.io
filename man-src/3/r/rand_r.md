---
title: "rand_r(3)"
name: "rand_r"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rand_r/"
description: "rand, rand_r, srand – pseudo-random number generator"
---

<p>rand, rand_r, srand &#8211; pseudo-random number generator</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;

int rand(void);

int rand_r(unsigned int *seedp);

void srand(unsigned int seed);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>rand_r</code>():</p>
<dl>
<dd>Since glibc 2.24:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199506L<br />
 Glibc 2.23 and earlier<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_POSIX_C_SOURCE</dl>
<h2>Description</h2>
<p>The <code>rand</code>() function returns a pseudo-random integer in the range 0 to <code>RAND_MAX</code> inclusive (i.e., the mathematical range [0,&nbsp;<code>RAND_MAX</code>]). </p>
<p> The <code>srand</code>() function sets its argument as the seed for a new sequence of pseudo-random integers to be returned by <code>rand</code>(). These sequences are repeatable by calling <code>srand</code>() with the same seed value. </p>
<p> If no seed value is provided, the <code>rand</code>() function is automatically seeded with a value of 1. </p>
<p> The function <code>rand</code>() is not reentrant, since it uses hidden state that is modified on each call. This might just be the seed value to be used by the next call, or it might be something more elaborate. In order to get reproducible behavior in a threaded application, this state must be made explicit; this can be done using the reentrant function <code>rand_r</code>(). </p>
<p> Like <code>rand</code>(), <code>rand_r</code>() returns a pseudo-random integer in the range [0,&nbsp;<code>RAND_MAX</code>]. The <i>seedp</i> argument is a pointer to an <i>unsigned int</i> that is used to store state between calls. If <code>rand_r</code>() is called with the same initial value for the integer pointed to by <i>seedp</i>, and that value is not modified between calls, then the same pseudo-random sequence will result. </p>
<p> The value pointed to by the <i>seedp</i> argument of <code>rand_r</code>() provides only a very small amount of state, so this function will be a weak pseudo-random generator. Try <code><a href="/docs/linux/man/3-drand48_r/">drand48_r</a></code>(3) instead.</p>
<h2>Return Value</h2>
<p>The <code>rand</code>() and <code>rand_r</code>() functions return a value between 0 and <code>RAND_MAX</code> (inclusive). The <code>srand</code>() function returns no value.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>rand</code>(), <code>rand_r</code>(), <code>srand</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>The functions <code>rand</code>() and <code>srand</code>() conform to SVr4, 4.3BSD, C89, C99, POSIX.1-2001. The function <code>rand_r</code>() is from POSIX.1-2001. POSIX.1-2008 marks <code>rand_r</code>() as obsolete.</p>
<h2>Notes</h2>
<p>The versions of <code>rand</code>() and <code>srand</code>() in the Linux C Library use the same random number generator as <code><a href="/docs/linux/man/3-random/">random</a></code>(3) and <code><a href="/docs/linux/man/3-srandom/">srandom</a></code>(3), so the lower-order bits should be as random as the higher-order bits. However, on older <code>rand</code>() implementations, and on current implementations on different systems, the lower-order bits are much less random than the higher-order bits. Do not use this function in applications intended to be portable when good randomness is needed. (Use <code><a href="/docs/linux/man/3-random/">random</a></code>(3) instead.)</p>
<h2>Examples</h2>
<p>POSIX.1-2001 gives the following example of an implementation of <code>rand</code>() and <code>srand</code>(), possibly useful when one needs the same sequence on two different machines. #include &lt;stdio.h&gt;<br />
#include &lt;stdlib.h&gt;<br />
int main(int argc, char *argv[])<br />
{<br />
    int r, nloops;<br />
    unsigned int seed;<br />
    if (argc != 3) {<br />
        fprintf(stderr, &quot;Usage: %s &lt;seed&gt; &lt;nloops&gt;
&quot;, argv[0]);<br />
        exit(EXIT_FAILURE);<br />
    }<br />
    seed = atoi(argv[1]);<br />
    nloops = atoi(argv[2]);<br />
    srand(seed);<br />
    for (int j = 0; j &lt; nloops; j++) {<br />
        r = rand();<br />
        printf(&quot;%d
&quot;, r);<br />
    }<br />
    exit(EXIT_SUCCESS);<br />
} The following program can be used to display the pseudo-random sequence produced by <code>rand</code>() when given a particular seed. </p>
<pre><code>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
int main(int argc, char *argv[])
{
    int r, nloops;
    unsigned int seed;
    if (argc != 3) {
        fprintf(stderr, &quot;Usage: %s &lt;seed&gt; &lt;nloops&gt;
&quot;, argv[0]);
        exit(EXIT_FAILURE);
    }
    seed = atoi(argv[1]);
    nloops = atoi(argv[2]);
    srand(seed);
    for (int j = 0; j &lt; nloops; j++) {
        r = rand();
        printf(&quot;%d
&quot;, r);
    }
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-drand48/">drand48</a></code>(3), <code><a href="/docs/linux/man/3-random/">random</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
