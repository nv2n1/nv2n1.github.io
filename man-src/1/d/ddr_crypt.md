---
title: "ddr_crypt(1)"
name: "ddr_crypt"
section: "1"
letter: "d"
url: "/docs/linux/man/1-ddr_crypt/"
description: "ddr_crypt – Data de/encryption plugin for dd_rescue"
---

<h2>NAME</h2>
<p> ddr_crypt &#8211; Data de/encryption plugin for dd_rescue</p>
<h2>SYNOPSIS</h2>
<p> <code>-L crypt[=option[:option[:&#8230;]]]</code><br />
 or<br />
 <code>-L /path/to/libddr_crypt.so[=option[:option[:&#8230;]]]</code></p>
<h2>DESCRIPTION</h2>
<h3>About</h3>
<p> This plugin allows to en/decrypt data on the fly as it is written out by <code>dd_rescue.</code> It supports a variance of AES ciphers and uses the hardware acceleration on x86 (AESNI) and ARMv8 &#8212; if available &#8212; to provide good performance. </p>
<p> This plugin has been written for <code>dd_rescue</code> and uses the plugin interface from it. See the <code><a href="/docs/linux/man/1-dd_rescue/">dd_rescue</a>(1)</code> man page for more information on <code>dd_rescue.</code></p>
<h2>OPTIONS</h2>
<p> Options are passed using <code>dd_rescue</code> option passing syntax: The name of the plugin (crypt) is followed by an equal sign (=) and options are separated by a colon (:). the <code>crypt</code> plugin also allows for some options to be abbreviated. At least encryption or decryption and a way to determine the key (and IV) needs to be passed.</p>
<h3>Help</h3>
<p> Pass <code>help</code> to have ddr_crypt output a short list of options.</p>
<h3>Encryption or Decryption</h3>
<p> The crypt dd_rescue plugin (subsequently referred to as just ddr_crypt which reflects the variable parts of the file name libddr_crypt.so) need to be told whether to encrypt or decrypt. This is done by specifying <code>enc[rypt]</code> or <code>dec[rypt]</code> parameters on the command line.</p>
<h3>De/encryption algorithm</h3>
<p> The crypt plugin supports a number of the de/encryption variants of AES. You can specify which one you want to use by passing</p>
<dl>
<dt><code>algo=AESxxx-yyy</code>,</p>
<dd> where xxx can be 128, 192, 256, 128+, 192+, 256+, 128&#215;2, 192&#215;2, or 256&#215;2, and yyy can be ECB, CBC, or CTR. Pass <code>algo=help</code> to get a list of available algorithms. See section ALGORITHMS AND STREAM MODES for a discussion of the options. Note that decrypting a file can only be successful if the exact same algorithms is chosen as was used for encryption. There is no way to tell from an encrypted file which algorithm has been chosen.<br />
 The default (AES192-CTR) is a good choice if you can ensure that the key/IV combination is NEVER reused.</dl>
<h3>Crypto engine</h3>
<p> There are several implementations of the AES algorithms that this plugin can currently use:</p>
<dl>
<dt><code>engine=aesni</code></p>
<dd> This will use an own AES implementation using the AESNI instructions of the intel x86 core CPUs since Westmere. If possible, this should be used, as it provides both superior performance and avoids some of the cache timing attacks that the lookup tables used in discrete implementations may be prone to. This engine supports all algorithms.</p>
<dt><code>engine=aesarm64</code></p>
<dd> This will use an own AES implementation using the AESv8 crypto extensions of the ARMv8 (AArch64 = ARM 64bit) architecture (available on CPUs/SOCs based on ARM&#8217;s Cortex A53,A57,A72 or Qualcomm&#8217;s Kryo or Apple&#8217;s A7x or newer designs). If possible, this should be used, as it provides both superior performance and avoids some of the cache timing attacks that the lookup tables used in discrete implementations may be prone to. This engine supports all algorithms.</p>
<dt><code>engine=aes_c</code></p>
<dd> This uses an AES implementation in C which is based on the rijndael reference code. It is available on all CPUs and supports all algorithms. Some prefetching is done on the tables to make cache timing attacks a bit harder, but this is most likely insufficient to thwart sophisticated attackers.</p>
<dt><code>engine=openssl</code></p>
<dd> This uses the openssl library to implement the AES routines, which should take advantage of hardware acceleration where available and have received some hardening against attacks. Note that the openssl implementation does not support the + variants (increased number of rounds) that the other engines provide.</dl>
<p> The engines are used in this order if available, which means that <i>aesni</i> will be used by default on x86 if supported, <i>aesarm64</i> will be used on ARMv8 and <i>aes_c</i> by default on all other platforms.</p>
<h3>Padding</h3>
<p> As AES is a block cipher (with a block size of 16 bytes), files which are not a multiple of the block size need padding at the end to have a full block.</p>
<dl>
<dt><code>pad=zero</code></p>
<dd> The last block is filled up with zeroes and then encrypted. Note that on decryption, these zeroes can&#8217;t be automatically stripped, as the decryptor has no way to tell whether there true trailing zeros or whether those had been added by padding. This option is thus not recommended for copying files of arbitrary length.</p>
<dt><code>pad=always</code></p>
<dd> This uses the PKCS7 scheme used by openssl, appending one to sixteen bytes with the number of bytes to discard when decrypting. This is always safe, but always makes the output file larger than the input file. Use this when copying files.</p>
<dt><code>pad=asneeded</code></p>
<dd> This is a hybrid between zero and always. This does PKCS7 padding when the file size does not fill a complete block, but does no padding when it does. This mechanism has in the worst case (no pad bytes) a chance of 1/255 to produce an incorrect decryption result by wrong unpadding (which means that it has an overall chance of misrepresenting the final file size of 1/4080 for arbitrary file sizes). Don&#8217;t use this unless you can deal with such errors (or exclude them)!</dl>
<p> Note that the CTR stream mode does NOT require padding and indeed ddr_crypt does not apply any padding regardless of the pad option when it is used.</p>
<h3>Debugging and Benchmarking</h3>
<p> The <code>debug</code> parameter makes the ddr_crypt module output some debugging information. With <code>outkeyiv</code> the key and IV will be output. The <code>benchmark</code> parameter will result in reporting the en/decryption speed.</p>
<h2>Setting key and IV</h2>
<p> There are many ways to set the key and IV (for -CBC and -CTR stream modes).</p>
<h3>Setting directly</h3>
<p> They can be set directly using <code>keyhex= </code> and <code>ivhex=</code> on the command line. The argument is interpreted as a hex ASCII representation of the key/IV (without leading 0x). This way to specify keys/IVs should only be used for testing &#8211; the key will be visible to all local users by looking at the command line (unless specific measures are taken to lock down access to /proc). Not normally a good idea on a multi-user system. ddr_crypt does overwrite the sensitive data with X to make the attack a bit harder, but this still leaks the length and &#8212; more importantly &#8212; there is still a time window where the sensitive data is visible.</p>
<h3>Reading from file of file descriptor</h3>
<p> It&#8217;s better to pass in the key and IV via a file descriptor via <code>keyfd=</code> and <code>ivfd= .</code> If the integer is preceded by an x, the key/IV will be read as hex string, otherwise binary data will be used. Optionally, @OFF@LEN can be appended, designating the offset and length (in bytes) to be read in the file passed via the file descriptor. Note that a file descriptor of 0 without shell redirection will result in an interactive prompt to the user and the answer won&#8217;t be echoed to the screen of course.<br />
 This is useful mainly when dd_rescue is called from another program. </p>
<p> Alternatively, with <code>keyfile=</code> and <code>ivfile=</code> a file name to be opened and read from can be specified. The syntax does support the same optional @OFF@LEN designation, but the key and IV will always be read in binary form. (See below, Index files for a way to read in hex form.) Currently (unlike with salt) there is no way to use ddr_crypt to write out binary key and IV data with these options.</p>
<h3>Generating random key and IV</h3>
<p> The Operating System&#8217;s random number generator can be used to generate key and IV on the fly; if your system offers good random numbers, this is the most secure way to specify and encryption key. The options to specify are <code>keygen</code> and <code>ivgen .</code> You need to save the key/IV somehow, otherwise you can not decrypt again later. (The program will warn you!) Best way is to use the next options.</p>
<h3>Index files</h3>
<p> Keys and IVs can be stored as hex strings in index files; the file format is the same as the one used in MD5SUMS: The hex representation of the key/IV is followed by the file name. Obviously, appropriate care needs to be taken to keep those files confidential. </p>
<p> If the ddr_crypt plugin gets the option <code>keysfile</code> and <code>ivsfile</code> it will store already created keys/IVs (from the other options) to files names KEYS.algname and IVS.algname in the MD5SUMS format. (The files will be created or updated accordingly.) If key/IV have not been created yet, ddr_crypt will try to retrieve the key/IV from those files and error out upon failure.<br />
 These options combine well with keygen and ivgen on encryption (and should be used alone on decryption).</p>
<h3>Extended attributes</h3>
<p> Similar to index files, keys and IVs can also be stored in and retrieved from the encrypted file&#8217;s extended attributes. This can be achieved using the options <code>keyxattr</code> and <code>ivxattr .</code> Please review the comments in the main dd_rescue (1) man page for general considerations about using extended attributes (xattrs).<br />
 Note that storing the key in the xattr is normally <code>not</code> a good idea. A user who can access the encrypted file can (locally) also read the xattrs &#8212; so the secrecy normally achieved by encryption is defeated this way. (There may be valid scenarios, though, e.g. when the file tself is only accessible via a remote protocol that does not expose the xattrs, such as http or DAV or NFS.)<br />
 You can specify <code>kxfallb[ack]</code> and <code>ixfallb[ack]</code> in addition if you want ddr_crypt to try using xattrs and falling back to keysfile and ivsfile in case the file system does not support the extended attributes.</p>
<h3>Password based key and IV generation</h3>
<p> Using the same key/IV for many files harms security severely (see below in ALGORITHMS). So using a directly specified (non-generated) key is not a good idea. However, if you prefer to have something memorable rather than stored, you can use a password and salt to generate many keys from one password. </p>
<p> The key and IV are derived from an expensive to compute (and even more expensive to revert) function of password and salt. By default, ddr_crypt uses 17000 rounds of pbkdf2() for the key (and a third for the IV), although a more compute intense function (like scrypt) is planned for the future. The expensiveness of this function is a protection against brute forcing passwords. To use pbkdf2, you need to specify <code>pbkdf2</code> or <code>pbkdf2=rounds .</code> The latter format allows overriding the number of iterations for key generation. (IV generation will be done with a third again.) </p>
<p> For compatibility with openssl, key and IV can also be derived using an openssl compatible key derivation function with <code>opbkdf .</code> Note that this is not recommended; only one round of md5 hashing is used which makes brute-forcing very effective. Using this option also has the side-effect of writing (encryption) or parsing (decryption) an openSSL style Salted__ header. </p>
<p> The salt can be derived automatically from the name (and length) of the encrypted file; this allows to work with just one password to be memorized. However, be aware that file size or name changes will result in a different salt and thus different key/IV which render your encrypted file undecryptable. If there is a risk of this to happen, rather memorize one salt per file (or better save key and IV using keysfile and ivsfile options or save the salt using saltsfile or saltxattr, see below). Remember that file names are case sensitive (as always with Un*x). Of course the keysfile needs to be well protected from being read by unauthorized persons. </p>
<p> Password and salt can be specified with a string <code>pass=</code> and <code>salt=</code> or using the <code>passfd=</code> <code>passfile=</code> and <code>salthex=</code> <code>saltfd=</code> <code>saltfile=</code> options with the same possible parameters as above for direct specification of key and IV. (Note that the salt is hashed, like when derived from file name and length.) The password/passphrase is treated as a string, null-terminated and with a trailing CRLF stripped off.<br />
 The warnings about passing confidential data (here: pass, salt, salthex) on the command line apply &#8212; only do it for testing or in a single-user environment. </p>
<p> If the file name based automatic salt derivation is used, the assumed file length for salt generation can be overridden by <code>saltlen= .</code> </p>
<p> Alternatively, the salts can also be stored and retrieved from an MD5SUMS style index file (like with keysfile and ivsfile) by specifying the option <code>saltsfile .</code> When saltsfile is used to store salts, using random salts on encryption becomes a good idea. This can be achieved by specifying the <code>saltgen</code> option. </p>
<p> Instead of a salt index file (saltsfile), the salt can also be stored in (and retrieved from) an extended attribute. This can be done using the <code>saltxattr[=xattr_name]</code> option. The attribute name is optional and defaults to user.salt.ALGNAME (with ALGNAME replaced by the algorithm). Since ddr_crypt 1.99, the password-based key derivation function (and the number of iterations) is also stored and retrieved in the xattr user.pbkdf with this option.<br />
 It&#8217;s also possible to try using the xattr feature and fall back to using the index file (saltsfile) if your file system does not support extended attributes. Use the <code>sxfallback</code> option to tell ddr_crypt to do this. Note that the pbkdf can not be stored (or retrieved) if the fallback actually takes place.<br />
 See the main dd_rescue (1) man page for a discussion of advantages and disadvantages of using extended attributes.</p>
<h2>ALGORITHMS AND STREAM MODES</h2>
<p> The AES (Rijndael) family of algorithms is considered cryptographically safe at the time of writing, as no practicable attacks have been published against it. It is up to the reader to judge whether (s)he believes that the worst criminals or intelligence agencies are significantly ahead of common (published) knowledge. In reality, it is typically easier to use social engineering or flaws in key handling and random number generation to carry out attacks.</p>
<h3>Plus modes</h3>
<p> Given that the best known attacks are against AES versions with a reduced number of rounds with only small round number reductions, it appears that increasing the number of rounds would seem a reasonable countermeasure against cryptographic attacks. (This has been inspired by a comment from Bruce Schneier who the author of this document has very high respect for.) </p>
<p> The C and AESNI implementations support AES128,192,256 modes with 2,3,4 additional rounds respectively, resulting in 12, 15, 18 rounds. These modes are named AES128+, AES192+, and AES256+ (plus modes) respectively. They do offer a computationally relatively cheap way to enhance security. The author of this document e.g. would chose AES192+ over AES256. While the author of this document would never judge himself as a cryptography expert strong enough to create new algorithms or even devise significant changes to existing ones, he considers this variation a choice that is more secure than the original. Please note however, that these custom algorithms result in files that can not be decrypted using any other tools. Also, the openSSL engine does not support the plus modes.</p>
<h3>Double modes</h3>
<p> A computationally more expensive method to enhance security is doubling the number of rounds. This is equivalent to encrypting twice (where the second key is a simple derivation of the first). These methods are supported by all engines and are named AES128x2, AES192x2, and AES256x2.</p>
<h3>Stream modes</h3>
<p> The AES algorithm is a block cipher &#8212; it transforms 16 byte blocks. The trivial application to a file of arbitrary size is to apply this to every block in the file. This is called ECB (electronic codebook) mode. This is very insecure &#8230; the same input will always result in the same output. Patterns can be easily recognized and known plain text attacks are trivial. </p>
<p> It&#8217;s better to make the transformation dependent on the previous content of the file or the position within it. This is what the CBC (chained block cipher) and CTR modes do. </p>
<p> The CBC mode has several disadvantages: It can&#8217;t be parallelized (every block depends on all previous blocks for encryption; things are better for decryption) and random access is impossible. </p>
<p> The CTR mode has many desirable properties. It is basically a stream of (reproducible) pseudo random numbers that are XORed with the input for encryption. Decryption is just another XOR of course. It&#8217;s a one time pad &#8212; which has been proven to be secure, if the pad is unknown to an attacker and only used once.<br />
 The latter can&#8217;t be stressed enough: Don&#8217;t ever use the same key/IV combination for two files. Mathematically spoken: c1 = r1 XOR p1 and c2 = r2 XOR p2 (c = ciphertext, r = AES random numbers, p = plaintext). With r == r1 == r2, it can be trivially seen that the attacker can calculate c1 XOR c2 = r XOR p1 XOR r XOR p2 = p1 XOR p2. If the plaintext of one of the files is partially known, so is the other. </p>
<p> The CTR mode has more nice properties: It allows random access as the AES random numbers (belonging to a key/IV combination) with a certain offset can be directly calculated and the last block does not require padding, as partial blocks can be processed. </p>
<p> The author of this documents prefers CTR stream mode and ensures that keys/IVs are not reused.</p>
<h2>Supported dd_rescue features</h2>
<p> With CTR mode, you can do partial writes to encrypted files and the result will still be a consistent file (of course assuming that the used key and IV are the same). Same with appending (-x) or reverse direction copies.<br />
 With ECB mode, this will only work, if file size and offsets are all block (16byte) aligned. With CBC, none of this is possible. </p>
<p> The ddr_crypt plugin has no specific support for encoding holes; if however previous correctly encrypted content is present in a hole, the support for partial writes in CTR and ECB mode will result in a meaningful output. If no previous content is in holes, then the result of decrypting zeros will result upon decryption.<br />
 You can pass the option <code>skiphole</code> to make ddr_crypt leave 512byte blocks of zeros untouched. This will reveal blocks of zeros and may thus disclose valuable information to an attacker, so use with care. Also note that you need to use this with en- and decryption and with the same alignment (mod 512) for encryption to be reversible. You have been warned. (You don&#8217;t need to be worried about misdetecting zeros on decrypting &#8212; the chances of non-zero plaintext resulting in an aligned 512byte block of zeros is smaller than 2^-4096. So this option is safe on decrypting &#8212; if some of the ciphertext has been overwritten with blocks of zeros, you might even prefer to have zeros in the decrypted file rather than random gibberish.) </p>
<p> Note that you can compress and encode holes with ddr_lzo and then pass to ddr_crypt to encrypt and pass through ddr_crypt to decrypt and ddr_lzo to uncompress and extract holes again. This only works with CTR mode. </p>
<p> The option <code>weakrnd</code> is provided for testing in environments, where strong random numbers are not available. It will cause weaker random numbers to be used for key generation. Don&#8217;t use it if you want security.</p>
<h2>openssl compatibility</h2>
<p> Files that are encrypted with openssl enc where you specify the key (with -K) and the IV (with -iv) result in the same output that ddr_crypt generates for -ECB and -CBC modes. ddr_crypt uses a 64bit counter in -CTR modes. </p>
<p> With the option <code>opbkdf</code> ddr_crypt also reads/writes the openSSL Salted__ header to be compatible with openssl. This function needs more testing and better error handling though.</p>
<h2>BUGS/LIMITATIONS</h2>
<h3>Maturity</h3>
<p> The plugin is new as of dd_rescue 1.98. Do not yet rely on data saved with ddr_crypt as the only backup for valuable data. Also expect some changes to ddr_crypt in the not too distant future. </p>
<p> Due to an issue in ddr_crypt&#8217;s initialization of the IV for CTR mode, the last 32bits would always be zeroed out prior to adding the counter. This has been fixed in 1.99. It order to be compatible with 1.98, the option <code>ctrbug198</code> can be specified on the command line. </p>
<h3>Security</h3>
<p> While care has been applied to check the result of memory allocations &#8230;, the code has not been audited and only limited fuzzing has been applied to ensure it&#8217;s not vulnerable to malicious data &#8212; be careful when you process data from untrusted sources.<br />
 Key handling is a tricky business &#8212; the author may have screwed up resulting in some ways to use this program to encrypt data may not result in the level of secrecy that is desired.</p>
<h3>Testing</h3>
<p> The crypt plugin does not yet have the same test coverage as the other plugins, which means it has not been tested as intensively as the others.</p>
<h3>Future work</h3>
<p> Except for more testing and auditing a few more features are envisioned for this plugin:<br />
 Support for other (non-AES) algorithms such as twofish (and possibly also threefish).<br />
 Stronger function to derive keys/IVs from passwords than pbkdf2.<br />
 Support for other streaming modes (XTS, GCM, &#8230;)</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>dd_rescue -ptAL crypt=algo=AES256-CTR:enc:keygen:ivgen:keysfile:ivsfile infile outfile</code></p>
<dd> encrypts data from <i>infile</i> with AES256 in CTR mode using a generated (random) key and IV and writes the result to <i>outfile</i> It adds a line to KEYS.AES256-CTR and to IVS.AES256-CTR where the used key and IV are written to respectively. (Please ensure that this file is not accessible by any unauthorized person!) Decryption can be performed by</dl>
<p> <code>dd_rescue -ptAL crypt=algo=AES256-CTR:dec:keysfile:ivsfile outfile infile</code></p>
<dl>
<dt><code>dd_rescue -AL crypt=AES192+-CTR:enc:saltgen:saltxattr:sxfallback:passfd=0:pbkdf2 infile outfile</code></p>
<dd> will ask for a password, generate a random salt and store it in the extended attribute of <code>outfile </code> (and fallback to SALTS.AES192+-CTR index file) and uses pbkdf2 function to produce a key and IV for encrypting the data. For decrypting, just omit the <code>saltgen </code> parameter.</p>
<dt><code>dd_rescue -ptL lzo=compr,crypt=AES256-CTR:enc:keygen:ivgen:keysfile:ivsfile infile outfile</code></p>
<dd> will compress the data (using lzo) and then encrypt. Use the reverse order and omit keygen and ivgen to decrypt and uncompress. Compression has the nice side effect of dealing with holes, which otherwise get compressed to non-zero values (unless you specify skiphole). Feel free to add the hash plugin at the beginning and/or the end to produce cryptographic checksums for both the original file and the end result.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dd_rescue/">dd_rescue</a></code>(1)</p>
<h2>AUTHOR</h2>
<p> Kurt Garloff &lt;kurt [at] garloff.de&gt;</p>
<h2>CREDITS</h2>
<p> The x86 AESNI optimized AES implementation has been inspired by an intel whitepaper from 2009: <a rel="nofollow" href="https://software.intel.com/sites/default/files/article/165683/aes-wp-2012-09-22-v01.pdf">https://software.intel.com/sites/default/files/article/165683/aes-wp-2012-09-22-v01.pdf</a><br />
 The ARMv8 AES support has been inspired by studying openSSL assembly as well as Linaro&#8217;s in-kernel implementation.</p>
<h2>COPYRIGHT</h2>
<p> This plugin is under the same license as dd_rescue: The GNU General Public License (GPL) v2 or v3 &#8211; at your option.</p>
<h2>HISTORY</h2>
<p> ddr_crypt plugin was first introduced with dd_rescue 1.98 (May 2015).<br />
 Version 1.99 brought support for ARMv8 crypto acceleration and support for openssl style key derivation and Salted__ headers. It also added storing pbkdf related infos in xattrs and added support for storing and retrieving keys (not recommended!) and IVs in/from xattrs. A bug with CTR initialization was resolved (see ctrbug198 option). </p>
<p> Some additional information can be found on<br />
 <a rel="nofollow" href="http://garloff.de/kurt/linux/ddrescue/">http://garloff.de/kurt/linux/ddrescue/</a> </p>
<h2>Index</h2>
