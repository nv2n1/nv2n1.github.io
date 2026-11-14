---
title: "shasum(1)"
name: "shasum"
section: "1"
letter: "s"
url: "/docs/linux/man/1-shasum/"
---

<h2 class="name">NAME</h2>
 

 shasum - Print or Check SHA Checksums 

<h2>SYNOPSIS</h2>

 <pre><code>
 Usage: shasum [OPTION]... [FILE]...
 Print or check SHA checksums.
 With no FILE, or when FILE is -, read standard input.
   -a, --algorithm   1 (default), 224, 256, 384, 512, 512224, 512256
   -b, --binary      read in binary mode
   -c, --check       read SHA sums from the FILEs and check them
       --tag         create a BSD-style checksum
   -t, --text        read in text mode (default)
   -U, --UNIVERSAL   read in Universal Newlines mode
                         produces same digest on Windows/Unix/Mac
   -0, --01          read in BITS mode
                         ASCII '0' interpreted as 0-bit,
                         ASCII '1' interpreted as 1-bit,
                         all other characters ignored
 The following five options are useful only when verifying checksums:
       --ignore-missing  don't fail or report status for missing files
   -q, --quiet           don't print OK for each successfully verified file
   -s, --status          don't output anything, status code shows success
       --strict          exit non-zero for improperly formatted checksum lines
   -w, --warn            warn about improperly formatted checksum lines
   -h, --help        display this help and exit
   -v, --version     output version information and exit
 When verifying SHA-512/224 or SHA-512/256 checksums, indicate the
 algorithm explicitly using the -a option, e.g.
   shasum -a 512224 -c checksumfile
 The sums are computed as described in FIPS PUB 180-4.  When checking,
 the input should be a former output of this program.  The default
 mode is to print a line with checksum, a character indicating type
 (`*' for binary, ` ' for text, `U' for UNIVERSAL, `^' for BITS),
 and name for each FILE.  The line starts with a `\' character if the
 FILE name contains either newlines or backslashes, which are then
 replaced by the two-character sequences `\n' and `\\' respectively.
 Report shasum bugs to mshelor [at] cpan.org
</code></pre>

<h2>DESCRIPTION</h2>

 Running <i>shasum</i> is often the quickest way to compute <font SIZE="-1">SHA</font> message digests. The user simply feeds data to the script through files or standard input, and then collects the results from standard output. 

 The following command shows how to compute digests for typical inputs such as the <font SIZE="-1">NIST</font> test vector ``abc'': 

 <pre>
        perl -e &quot;print qq(abc)&quot; | shasum
</pre> 

 Or, if you want to use <font SIZE="-1">SHA-256</font> instead of the default <font SIZE="-1">SHA-1,</font> simply say: 

 <pre>
        perl -e &quot;print qq(abc)&quot; | shasum -a 256
</pre> 

 Since <i>shasum</i> mimics the behavior of the combined <font SIZE="-1">GNU</font> <i>sha1sum</i>, <i>sha224sum</i>, <i>sha256sum</i>, <i>sha384sum</i>, and <i>sha512sum</i> programs, you can install this script as a convenient drop-in replacement. 

 Unlike the <font SIZE="-1">GNU</font> programs, <i>shasum</i> encompasses the full <font SIZE="-1">SHA</font> standard by allowing partial-byte inputs. This is accomplished through the <font SIZE="-1">BITS</font> option (<i>-0</i>). The following example computes the <font SIZE="-1">SHA-224</font> digest of the 7-bit message <i>0001100</i>: 

 <pre>
        perl -e &quot;print qq(0001100)&quot; | shasum -0 -a 224
</pre>

<h2>AUTHOR</h2>

 Copyright (C) 2003-2018 Mark Shelor &lt;mshelor [at] cpan.org&gt;.

<h2>SEE ALSO</h2>

 <i>shasum</i> is implemented using the Perl module Digest::SHA. 

<h2>Index</h2>


