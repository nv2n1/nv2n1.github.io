---
title: "sha3sum(1)"
name: "sha3sum"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sha3sum/"
---

<h2 class="name">NAME</h2>
 

 sha3sum - Print or Check SHA-3 Checksums 

<h2>SYNOPSIS</h2>

 <pre><code>
 Usage: sha3sum [OPTION]... [FILE]...
 Print or check SHA-3 checksums.
 With no FILE, or when FILE is -, read standard input.
   -a, --algorithm   224 (default), 256, 384, 512, 128000, 256000
   -b, --binary      read in binary mode
   -c, --check       read SHA-3 sums from the FILEs and check them
   -t, --text        read in text mode (default)
   -U, --UNIVERSAL   read in Universal Newlines mode
                         produces same digest on Windows/Unix/Mac
   -0, --01          read in BITS mode
                         ASCII '0' interpreted as 0-bit,
                         ASCII '1' interpreted as 1-bit,
                         all other characters ignored
   -p, --portable    read in portable mode (to be deprecated)
 The following two options are useful only when verifying checksums:
   -s, --status      don't output anything, status code shows success
   -w, --warn        warn about improperly formatted checksum lines
   -h, --help        display this help and exit
   -v, --version     output version information and exit
 The sums are computed as described in the FIPS 202 SHA-3 submission.
 When checking, the input should be a former output of this program.
 The default mode is to print a line with checksum, a character
 indicating type (`*' for binary, ` ' for text, `U' for UNIVERSAL,
 `^' for BITS, `?' for portable), and name for each FILE.
 Report sha3sum bugs to mshelor [at] cpan.org
</code></pre>

<h2>DESCRIPTION</h2>

 Running <i>sha3sum</i> is often the quickest way to compute <font SIZE="-1">SHA-3</font> message digests. The user simply feeds data to the script through files or standard input, and then collects the results from standard output. 

 The following command shows how to compute digests for typical inputs such as the <font SIZE="-1">NIST</font> test vector ``abc'': 

 <pre>
        perl -e &quot;print qq(abc)&quot; | sha3sum
</pre> 

 Or, if you want to use <font SIZE="-1">SHA3-256</font> instead of the default <font SIZE="-1">SHA3-224,</font> simply say: 

 <pre>
        perl -e &quot;print qq(abc)&quot; | sha3sum -a 256
</pre> 

 Unlike many other digest computation programs, <i>sha3sum</i> implements the full <font SIZE="-1">SHA-3</font> standard by allowing partial-byte inputs, which can be recognized through the <font SIZE="-1">BITS</font> option (<i>-0</i>). The following example computes the <font SIZE="-1">SHA3-384</font> digest of the 7-bit message <i>0001100</i>: 

 <pre>
        perl -e &quot;print qq(0001100)&quot; | sha3sum -0 -a 384
</pre>

<h2>AUTHOR</h2>

 Copyright (c) 2012-2015 Mark Shelor &lt;mshelor [at] cpan.org&gt;.

<h2>SEE ALSO</h2>

 <i>sha3sum</i> is implemented using the Perl module Digest::SHA3. 

<h2>Index</h2>


