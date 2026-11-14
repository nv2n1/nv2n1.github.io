---
title: "cryptrijndael(3)"
name: "cryptrijndael"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cryptrijndael/"
---

Crypt::Rijndael - Crypt::CBC compliant Rijndael encryption module 

<h2>Synopsis</h2><pre> use Crypt::Rijndael;
 # keysize() is 32, but 24 and 16 are also possible
 # blocksize() is 16
 $cipher = Crypt::Rijndael-&gt;new( &quot;a&quot; x 32, Crypt::Rijndael::MODE_CBC() );
 $cipher-&gt;set_iv($iv);
 $crypted = $cipher-&gt;encrypt($plaintext);
 # - OR -
 $plaintext = $cipher-&gt;decrypt($crypted);</pre><h2>Description</h2>This module implements the Rijndael cipher, which has just been selected as the Advanced Encryption Standard.
<dl COMPACT><dt>keysize
<dd>Returns the keysize, which is 32 (bytes). The Rijndael cipher actually supports keylengths of 16, 24 or 32 bytes, but there is no way to communicate this to <tt>&quot;Crypt::CBC&quot;</tt>.
<dt>blocksize
<dd>The blocksize for Rijndael is 16 bytes (128 bits), although the algorithm actually supports any blocksize that is any multiple of our bytes. 128 bits, is however, the AES-specified block size, so this is all we support.
<dt>$cipher = Crypt::Rijndael-&gt;new( $key [, $mode] )
<dd>Create a new <tt>&quot;Crypt::Rijndael&quot;</tt> cipher object with the given key (which must be 128, 192 or 256 bits long). The additional <tt>$mode</tt> argument is the encryption mode, either <tt>&quot;MODE_ECB&quot;</tt> (electronic codebook mode, the default), <tt>&quot;MODE_CBC&quot;</tt> (cipher block chaining, the same that <tt>&quot;Crypt::CBC&quot;</tt> does), <tt>&quot;MODE_CFB&quot;</tt> (128-bit cipher feedback), <tt>&quot;MODE_OFB&quot;</tt> (128-bit output feedback), or <tt>&quot;MODE_CTR&quot;</tt> (counter mode). 

 <font SIZE="-1">ECB</font> mode is very insecure (read a book on cryptography if you don't know why!), so you should probably use <font SIZE="-1">CBC</font> mode.
<dt>$cipher-&gt;set_iv($iv)
<dd>This allows you to change the initial value vector used by the chaining modes. It is not relevant for <font SIZE="-1">ECB</font> mode.
<dt>$cipher-&gt;encrypt($data)
<dd>Encrypt data. The size of <tt>$data</tt> must be a multiple of <tt>&quot;blocksize&quot;</tt> (16 bytes), otherwise this function will croak. Apart from that, it can be of (almost) any length.
<dt>$cipher-&gt;decrypt($data)
<dd>Decrypts <tt>$data</tt>.</dl><h3>Encryption modes</h3>Use these constants to select the cipher type:
<dl COMPACT><dt><font SIZE="-1">MODE_CBC -</font> Cipher Block Chaining
<dd><dt><font SIZE="-1">MODE_CFB -</font> Cipher feedback
<dd><dt><font SIZE="-1">MODE_CTR -</font> Counter mode
<dd><dt><font SIZE="-1">MODE_ECB -</font> Electronic cookbook mode
<dd><dt><font SIZE="-1">MODE_OFB -</font> Output feedback
<dd><dt><font SIZE="-1">MODE_PCBC -</font> ignore this one for now :)
<dd></dl><h2>See Also</h2>Crypt::CBC, <a rel="nofollow" HREF="http://www.csrc.nist.gov/encryption/aes/">http://www.csrc.nist.gov/encryption/aes/</a>
<h2>Bugs</h2>Should <font SIZE="-1">EXPORT</font> or <font SIZE="-1">EXPORT_OK</font> the <font SIZE="-1">MODE</font> constants.
<h2>Author</h2>Currently maintained by brian d foy, <tt>&quot;&lt;bdfoy [at] cpan.org&gt;&quot;</tt>. 

 Original code by Rafael R. Sevilla. 

 The Rijndael Algorithm was developed by Vincent Rijmen and Joan Daemen, and has been selected as the <font SIZE="-1">US</font> Government's Advanced Encryption Standard.
<h2>Source</h2>This code is in Github: 

 <pre> <a HREF="git://github.com/briandfoy/crypt-rijndael.git">git://github.com/briandfoy/crypt-rijndael.git</a></pre><h2>License</h2>This software is licensed under the Lesser <font SIZE="-1">GNU</font> Public License v3 (29 June 2007). See the included <font SIZE="-1">COPYING</font> file for details.
