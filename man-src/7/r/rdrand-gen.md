---
title: "rdrand-gen(7)"
name: "rdrand-gen"
section: "7"
letter: "r"
url: "/docs/linux/man/7-rdrand-gen/"
description: "rdrand-gen – Generate randomness by using RdRand on Intel’s CPUs."
---

<p>rdrand-gen &#8211; Generate randomness by using RdRand on Intel&#8217;s CPUs.</p>
<h2>Synopsis</h2>
<p>rdrand-gen [&#8211;amount NUM] [&#8211;method NAME] [&#8211;output FILE]<br />
 [&#8211;threads NUM] [&#8211;aes-ctr [&#8211;aes-keys FILE]] [&#8211;verbose] [&#8211;version]<br />
 [&#8211;help] </p>
<h2>Description</h2>
<p>RdRand is an instruction for returning random numbers from an Intel on-chip hardware random number generator. RdRand is available on Ivy Bridge and later processors. It uses cascade construction, combining a HW RNG operating at 3Gbps with CSPRNG with all components sealed on CPU. The entropy source is a metastable circuit, with unpredictable behavior based on thermal noise. The entropy is fed into a 3:1 compression ratio entropy extractor (whitener) based on AES-CBC-MAC. Online statistical tests are performed at this stage and only high quality random data are used as the seed for cryptograhically secure SP800-90 AES-CTR DRBG compliant PRNG. This generator is producing maximum of 512 128-bit AES blocks before it&#8217;s reseeded. According to documentation the 512 blocks is a upper limit for reseed, in practice it reseeds much more frequently. Despite the statistical tests did not reveal any flaws in RdRand&#8217;s output, it&#8217;s intern operation cannot be verified (with a possibility for the backdoor to be built into it). rdrand-gen is a simple application for generating randomness on Intel&#8217;s CPUs (Ivy Bridge and newers) using the HW RNG on the CPU. It can use three methods of generating: Default <code>get_bytes</code> &#8211; is fastest (on a laptop with a Core i7 about 200 MiB/s in one thread) and simply pulls out randomness from the HW RNG, and two slow, but more secure methods. These two methods, <code>reseed_delay</code> and <code>reseed_skip</code> are enforcing full regeneration of the CPU&#8217;s pool before each single value that is pushed out. <code>reseed_delay</code> is putting small delays (20 microseconds), long enough to allow the HW to reseed the RdRand&#8217;s internal generator with new thermal noise based entropy so that two consequent values returned by reseed_delay are guaranteed to be produced with different seed. <code>reseed_skip</code> is taking one of 1025 64bit values (the size of the inner pool) and throwing away the rest, forcing the HW to reseed. The perfomance of these reseeding methods is about 1/1000 of the default one. The performance differs on each machine, one one machine the <code>reseed_skip</code> is faster than <code>reseed_delay</code> , while on another one it can be different. If <code>aes-ctr</code> is set, then the output of RdRand instruction is encrypted with AES-CTR from OpenSSL. It can either use a random key, or you can give it a set of keys and nonces to use by using <code>aes-keys</code> parameter. If AES is not enabled by the first flag, the keys are ignored. Syntax of the key file is following:<br />
 On each line is a hexadecimal string containing a key and a nonce. There can be 128 lines at max. Length of a single key is twice of the nonce, so if K stands for a key character and N for a nonce, a single line in the key file will look like the following.<br />
 <i>KKKKNN</i> 24 bytes (48 characters) for a key and a nonce represents a 128bit key. This is also the only currently supported length of the key. See Examples for a simple way of generating the key file. </p>
<h2>Options</h2>
<p>&nbsp;<wbr>&nbsp;<wbr>&#8211;help&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-h&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Print this help.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;amount&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-n&nbsp;<wbr> <i>NUM </i> Generate given amount of bytes. Suffixes: K, M, G, T. Without the option or when 0, generate unlimited amount.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;method&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-m&nbsp;<wbr> <i>NAME</i> Use method NAME (default is <code>get_bytes</code> , others are <code>reseed_skip</code> and <code>reseed_delay</code> ).<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;output&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-o&nbsp;<wbr> <i>FILE</i> Save the generated data to the file.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;threads&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-t&nbsp;<wbr> <i>NUM</i> Run the generator in NUM threads (default 2).<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;aes-ctr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-a Encrypt the output with AES-CTR.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;aes-keys&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-k <i>FILE </i> Use given key file for the AES encryption </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>instead of random one. Works only when -a is set.<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;verbose&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-v Be verbose (will print on stderr).<br />
&nbsp;<wbr>&nbsp;<wbr>&#8211;version&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>-V Print version. </p>
<p> AES keys in file for -k argument has to be 24 bytes long in hexadecimal form.</p>
<h2>Examples</h2>
<p><code>Write 10.5MB of random data to the file /tmp/random</code><br />
 rdrand-gen -n 10.5M -o /tmp/random <code>Generate 20 random passwords of length 20 build from all letters</code> <code>and digits. Use the secure get_uint64_array_reseed_skip method.</code><br />
 (rdrand-gen -n2k -m reseed_skip | tr -cd &#8216;[:alnum:]&#8217; | fold -w 20 &amp;&amp; echo ) | head -20 <code>Create GPG encrypted keyfile for aespipe. </code><br />
 <code>Encrypt: </code><br />
 tar -cvf &#8211; files&#8230; | bzip2 | aespipe -w 10 -K keyfile.gpg &gt;archive.aes<br />
 <code>Decrypt: </code><br />
 aespipe -d -K keyfile.gpg &lt; /tmp/archive.aes | bzip2 -d -q | tar -tvf &#8211;<br />
 rdrand-gen -n3705 -m reseed_skip | uuencode -m &#8211; | head -n 66 | tail -n 65 | \<br />
 gpg &#8211;symmetric -a &gt; keyfile.gpg <code>Test the randomness of the generated data with dieharder test suite</code><br />
 rdrand-gen | dieharder -g 200 -a <code>Measure the speed of generation.</code><br />
 rdrand-gen | pv &gt; /dev/null <code>Create a key file for AES encryption</code><br />
 head -n 3100 /dev/random | xxd -p -c 24 | head -n 129 | tail -n 128 &gt; keys.txt <code>Create the keys and pass them to the rdrand-gen without saving the keys</code> <code>on disk</code><br />
 rdrand-gen -a -k &lt;(head -n 3100 /dev/random | \<br />
 xxd -p -c 24 | head -n 129 | tail -n 128) </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/3-librdrand/">librdrand</a>(3) <a href="/docs/linux/man/3-librdrand-aes/">librdrand-aes</a>(3) </p>
<h2>Bugs</h2>
<p>No known bugs. </p>
<h2>Author</h2>
<p>Jan Tulak (jan [at] tulak.me) Jiri Hladky (hladky.jiri [at] gmail.com)</p>
