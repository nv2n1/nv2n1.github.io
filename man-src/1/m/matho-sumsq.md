---
title: "matho-sumsq(1)"
name: "matho-sumsq"
section: "1"
letter: "m"
url: "/docs/linux/man/1-matho-sumsq/"
description: "matho-sumsq – Find the minimum sum of the squares for integers"
---

<h2 class="name">NAME</h2>
<p> matho-sumsq &#8211; Find the minimum sum of the squares for integers</p>
<h2>SYNOPSIS</h2>
<p> <code>matho-sumsq</code> [<i>numbers</i>] </p>
<h2>DESCRIPTION</h2>
<p> This command line utility is optionally part of the <code><a href="/docs/linux/man/1-mathomatic/">mathomatic</a></code>(1) package. It finds the minimum number of positive integers that when squared and added together, equal the given number. There is a proof that no more than 4 squares summed together are required to represent any positive integer. </p>
<p> The command line may contain positive integers, less than 2147483648 (2^31), to find the squares of, otherwise the program counts up from 0. If the number of squares is 2, this program displays all possible combinations, otherwise it just displays the first combination it finds. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mathomatic/">mathomatic</a></code>(1), <code><a href="/docs/linux/man/1-matho-pascal/">matho-pascal</a></code>(1), <code><a href="/docs/linux/man/1-matho-primes/">matho-primes</a></code>(1) </p>
<h2>AUTHOR</h2>
<p> George Gesslein II (gesslein [at] linux.com) </p>
<h2>Index</h2>
