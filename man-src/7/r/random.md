---
title: "random(7)"
name: "random"
section: "7"
letter: "r"
url: "/docs/linux/man/7-random/"
description: "random – overview of interfaces for obtaining randomness"
---

<p>random &#8211; overview of interfaces for obtaining randomness</p>
<h2>Description</h2>
<p>The kernel random-number generator relies on entropy gathered from device drivers and other sources of environmental noise to seed a cryptographically secure pseudorandom number generator (CSPRNG). It is designed for security, rather than speed. </p>
<p> The following interfaces provide access to output from the kernel CSPRNG:</p>
<dl>
<dt>*</p>
<dd>The <i>/dev/urandom</i> and <i>/dev/random</i> devices, both described in <code><a href="/docs/linux/man/4-random/">random</a></code>(4). These devices have been present on Linux since early times, and are also available on many other systems.</p>
<dt>*</p>
<dd>The Linux-specific <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2) system call, available since Linux 3.17. This system call provides access either to the same source as <i>/dev/urandom</i> (called the <i>urandom</i> source in this page) or to the same source as <i>/dev/random</i> (called the <i>random</i> source in this page). The default is the <i>urandom</i> source; the <i>random</i> source is selected by specifying the <code>GRND_RANDOM</code> flag to the system call. (The <code><a href="/docs/linux/man/3-getentropy/">getentropy</a></code>(3) function provides a slightly more portable interface on top of <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2).)</dl>
<h3>Initialization of the entropy pool</h3>
<p>The kernel collects bits of entropy from the environment. When a sufficient number of random bits has been collected, the entropy pool is considered to be initialized.</p>
<h3>Choice of random source</h3>
<p>Unless you are doing long-term key generation (and most likely not even then), you probably shouldn&#8217;t be reading from the <i>/dev/random</i> device or employing <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2) with the <code>GRND_RANDOM</code> flag. Instead, either read from the <i>/dev/urandom</i> device or employ <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2) without the <code>GRND_RANDOM</code> flag. The cryptographic algorithms used for the <i>urandom</i> source are quite conservative, and so should be sufficient for all purposes. </p>
<p> The disadvantage of <code>GRND_RANDOM</code> and reads from <i>/dev/random</i> is that the operation can block for an indefinite period of time. Furthermore, dealing with the partially fulfilled requests that can occur when using <code>GRND_RANDOM</code> or when reading from <i>/dev/random</i> increases code complexity.</p>
<h3>Monte Carlo and other probabilistic sampling applications</h3>
<p>Using these interfaces to provide large quantities of data for Monte Carlo simulations or other programs/algorithms which are doing probabilistic sampling will be slow. Furthermore, it is unnecessary, because such applications do not need cryptographically secure random numbers. Instead, use the interfaces described in this page to obtain a small amount of data to seed a user-space pseudorandom number generator for use by such applications.</p>
<h3>Comparison between getrandom, /dev/urandom, and /dev/random</h3>
<p>The following table summarizes the behavior of the various interfaces that can be used to obtain randomness. <code>GRND_NONBLOCK</code> is a flag that can be used to control the blocking behavior of <code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2). The final column of the table considers the case that can occur in early boot time when the entropy pool is not yet initialized. </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Pool</code></td>
<td><code> Blocking behavior </code></td>
<td><code> Behavior when pool is not yet ready </code>
</td>
</tr>
<tr VALIGN=top>
<td> <i>/dev/random</i> </td>
<td> Blocking pool </td>
<td> If entropy too low, blocks until there is enough entropy again </td>
<td> Blocks until enough entropy gathered
</td>
</tr>
<tr VALIGN=top>
<td> <i>/dev/urandom</i> </td>
<td> CSPRNG output </td>
<td> Never blocks </td>
<td> Returns output from uninitialized CSPRNG (may be low entropy and unsuitable for cryptography)
</td>
</tr>
<tr VALIGN=top>
<td> <code>getrandom</code>() </td>
<td> Same as <i>/dev/urandom</i> </td>
<td> Does not block once is pool ready </td>
<td> Blocks until pool ready
</td>
</tr>
<tr VALIGN=top>
<td> <code>getrandom</code>() <code>GRND_RANDOM</code> </td>
<td> Same as <i>/dev/random</i> </td>
<td> If entropy too low, blocks until there is enough entropy again </td>
<td> Blocks until pool ready
</td>
</tr>
<tr VALIGN=top>
<td> <code>getrandom</code>() <code>GRND_NONBLOCK</code> </td>
<td> Same as <i>/dev/urandom</i> </td>
<td> Does not block once is pool ready </td>
<td> <code>EAGAIN</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>getrandom</code>() <code>GRND_RANDOM</code> + <code>GRND_NONBLOCK</code> </td>
<td> Same as <i>/dev/random</i> </td>
<td> <code>EAGAIN</code> if not enough entropy available </td>
<td> <code>EAGAIN</code>
</td>
</tr>
</table>
<h3>Generating cryptographic keys</h3>
<p>The amount of seed material required to generate a cryptographic key equals the effective key size of the key. For example, a 3072-bit RSA or Diffie-Hellman private key has an effective key size of 128 bits (it requires about 2^128 operations to break) so a key generator needs only 128 bits (16 bytes) of seed material from <i>/dev/random</i>. </p>
<p> While some safety margin above that minimum is reasonable, as a guard against flaws in the CSPRNG algorithm, no cryptographic primitive available today can hope to promise more than 256 bits of security, so if any program reads more than 256 bits (32 bytes) from the kernel random pool per invocation, or per reasonable reseed interval (not less than one minute), that should be taken as a sign that its cryptography is <i>not</i> skillfully implemented.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-getrandom/">getrandom</a></code>(2), <code><a href="/docs/linux/man/3-getauxval/">getauxval</a></code>(3), <code><a href="/docs/linux/man/3-getentropy/">getentropy</a></code>(3), <code><a href="/docs/linux/man/4-random/">random</a></code>(4), <code><a href="/docs/linux/man/4-urandom/">urandom</a></code>(4), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
