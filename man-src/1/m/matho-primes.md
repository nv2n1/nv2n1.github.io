---
title: "matho-primes(1)"
name: "matho-primes"
section: "1"
letter: "m"
url: "/docs/linux/man/1-matho-primes/"
description: "matho-primes – generate consecutive prime numbers"
---

<h2 class="name">NAME</h2>
<p> matho-primes &#8211; generate consecutive prime numbers</p>
<h2>SYNOPSIS</h2>
<p> <code>matho-primes</code> [start [stop]] [&quot;twin&quot;] [&quot;pal&quot; [base]]<br />
 <code>matho-primes</code> [-t] [-p base] [start [stop]] </p>
<h2>DESCRIPTION</h2>
<p> This command line utility is optionally part of the <code><a href="/docs/linux/man/1-mathomatic/">mathomatic</a></code>(1) package. It quickly computes any number of consecutive prime numbers using a windowing, memory efficient sieve of Eratosthenes algorithm, dumping them to standard output. They are displayed one prime per line in ascending order, unless the &quot;twin&quot; option is specified, which displays only twin primes, two primes per line. </p>
<p> Generates up to 18 decimal digit primes, or whatever is the number of digits of precision for a <code>long double</code> in the C compiler used to compile this utility. </p>
<p> A range may be specified on the command line, otherwise the starting number and the number of primes to output is prompted for. The range is <code>start</code> to <code>stop</code> inclusive, and <code>stop</code> must be greater than or equal to <code>start.</code> </p>
<p> If the &quot;-t&quot; or &quot;twin&quot; option is specified on the command line, only <code>twin primes</code> will be displayed. Twin primes are two primes that differ in value by 2. Each twin pair is displayed together on the same line separated by a space character. </p>
<p> If the &quot;-p&quot; or &quot;pal&quot; option is specified on the command line, only <code>palindromic primes</code> are displayed. Palindromes are symmetrical, they read exactly the same forward and backward. The palindrome number <code>base</code> may be specified, the default is base 10. The <code>base</code> can be any integer greater than 1. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mathomatic/">mathomatic</a></code>(1), <code><a href="/docs/linux/man/1-primorial/">primorial</a></code>(1), <code><a href="/docs/linux/man/1-matho-mult/">matho-mult</a></code>(1), <code><a href="/docs/linux/man/1-matho-sum/">matho-sum</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> George Gesslein II (gesslein [at] linux.com) </p>
<h2>Index</h2>
