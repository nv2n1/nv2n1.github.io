---
title: "mcrypt(1)"
name: "mcrypt"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mcrypt/"
description: "mcrypt, mdecrypt – encrypt or decrypt files"
---

<h2>NAME</h2>
<p> mcrypt, mdecrypt &#8211; encrypt or decrypt files</p>
<h2>SYNOPSIS</h2>
<p> <code>mcrypt</code> [<code> -dLFubhvrzp </code>] [<code>-a algorithm</code>] [<code>-c config_file</code>] [<code>-m mode</code>] [<code>-s keysize</code>] [<code>-o keymode</code>] [<code>-k key1 key2 &#8230;</code>] [<code>-f keyfile</code>] [ <i>filename &#8230;</i> ] </p>
<p> <code>mdecrypt</code> [<code> -LFusbhvzp </code>] [<code>-a algorithm</code>] [<code>-c config_file</code>] [<code>-m mode</code>] [<code>-s keysize</code>] [<code>-o keymode</code>] [<code>-k key1 key2 &#8230;</code>] [<code>-f keyfile</code>] [ <i>filename &#8230;</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <i>Mcrypt</i> is a simple crypting program, a replacement for the old unix <i><a href="/docs/linux/man/1-crypt/">crypt</a></i>(1). When encrypting or decrypting a file, a new file is created with the extension <code>.nc</code> and mode 0600. The new file keeps the modification date of the original. The original file may be deleted by specifying the -u parameter. If no files are specified, the standard input is encrypted to the standard output. </p>
<p> <i>Mcrypt</i> uses all the symmetric algorithms included in libmcrypt. </p>
<h2>HINTS</h2>
<p> By default, <i>mcrypt</i> , when one of these algorithms is specified, prompts something like:<br />
&nbsp;<wbr>Enter passphrase: &#8230;<br />
&nbsp;<wbr>You should then enter a passphrase long enough&nbsp;<wbr>(512 characters is the maximum length). Now in order to encrypt the file, The passphrase is transformed using the specified (or the default) key generation algorithm, and a random salt. The produced value is then used as the key, which is fed to the algorithm. </p>
<p> <code>Algorithm Vulnerability:</code> Most algorithms today are designed to resist in specific attacks. None of them is proved not to be vulnerable to some kind of attack not as yet known. </p>
<p> <code>Compression:</code> By compressing your data before encryption you gain both in efficiency (faster encryption) and safety of your data (language redundancy is removed). A drawback is that most compression programs will add specific headers in the compressed file, thus making known plaintext attacks easier. Compression after encryption is useless and may result to compressed files with longer size than the original. </p>
<p> <code>Error Recovery:</code> There is some error recovery in mcrypt. If bytes are removed or lost from the file or stream in ECB, CBC and OFB modes, are impossible to recover, although CFB mode will recover. If some bytes are altered then a full block of plaintext is affected in ECB mode, two blocks in CBC and CFB modes, but only the corresponding byte in OFB mode. Mcrypt uses a 32 bit CRC to check for errors in the encrypted files. </p>
<p> <code>Extra security:</code> For the very paranoid, if mcrypt is executed with superuser privileges it ensures that no important data (keys etc.) are written to disk, as swap etc. Keep in mind that mcrypt was not designed to be a setuid program, so you shouldn&#8217;t make it one. </p>
<p> Do not rely on the fact that an algorithm has a large key size, try to use long passphrases and try to make them unpredictable. </p>
<p> All the block algorithms above support these modes of encryption: </p>
<p> <code>ECB: </code> The Electronic CodeBook mode. It is the simplest mode to use with a block cipher. Encrypts each block independently. </p>
<p> <code>CBC:</code> The Cipher Block Chaining mode. It is better than ECB since the plaintext is XOR&#8217;ed with the previous ciphertext. A random block is placed as the first block so the same block or messages always encrypt to something different. (This is the default mode) </p>
<p> <code>CFB:</code> The Cipher-Feedback Mode (in 8bit). This is a self-synchronizing stream cipher implemented from a block cipher. </p>
<p> <code>OFB:</code> The Output-Feedback Mode (in 8bit). This is a synchronous stream cipher implemented from a block cipher. It is intended for use in noisy lines, because corrupted ciphertext blocks do not corrupt the plaintext blocks that follow. Insecure when used to encrypt large amounts of data, so I recommend against using it. </p>
<p> <code>nOFB:</code> The Output-Feedback Mode (in nbit). n Is the size of the block of the algorithm. This is a synchronous stream cipher implemented from a block cipher. It is intended for use in noisy lines, because corrupted ciphertext blocks do not corrupt the plaintext blocks that follow. </p>
<p> Encrypted files can be restored to their original form using <i>mcrypt -d</i> or <i>mdecrypt</i> </p>
<p> <i>mdecrypt</i> takes a list of files on its command line and creates a new file for each file whose name ends with .nc by removing the &quot;.nc&quot; or by adding &quot;.dc&quot; to the end of the file name if .nc is not in the encrypted file&#8217;s name. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-F &#8211;force</code></p>
<dd> Force output on standard output or input from stdin if that is a terminal. By default mcrypt will not output encrypted data to terminal, nor read encrypted data from it.</p>
<dt><code>-z &#8211;gzip</code></p>
<dd> Use gzip (if it exists in your system) to compress files before encryption. If specified at decryption time it will decompress these files.</p>
<dt><code>-p &#8211;bzip2</code></p>
<dd> Use bzip2 (if it exists in your system) to compress files before encryption. If specified at decryption time it will decompress these files.</p>
<dt><code>&nbsp;<wbr>&#8211;openpgp-z INT</code></p>
<dd> This option will enable compression in OpenPGP (RFC2440) encrypted files.</p>
<dt><code>-d &#8211;decrypt</code></p>
<dd> Decrypt.</p>
<dt><code>&nbsp;<wbr>&#8211;help</code></p>
<dd> Display a help screen and quit.</p>
<dt><code>-v &#8211;version</code></p>
<dd> Version. Display the version number and quit.</p>
<dt><code>-L &#8211;license</code></p>
<dd> Display the <i>mcrypt&#8217;s</i> license and quit.</p>
<dt><code>-o &#8211;keymode MODE</code></p>
<dd> MODE may be one of the keymodes listed by the &#8211;list-keymodes parameter. It actually is the conversion to the key before it is fed to the algorithm. It is recommended to leave it as is, if you do not know what it is. However if you still want to use this option, you might want to use the &#8216;hex&#8217; mode which allows you to specify the key in hex (and no conversion will be applied).</p>
<dt><code>-h &#8211;hash HASH_ALGORITHM</code></p>
<dd> HASH_ALGORITHM may be one of the algorithms listed by the &#8211;list-hash parameter. This is the digest that will be appended to the file to be encrypted, in order to detect file corruption. The default is the CRC32 checksum.</p>
<dt><code>-s &#8211;keysize SIZE</code></p>
<dd> SIZE is the algorithm&#8217;s key size in bytes (not the size of the passphrase). It defaults to the maximum key supported by the algorithm. The maximum key sizes of the algorithms may be obtained by the &#8211;list parameter. It is safe not to touch this.</p>
<dt><code>-g &#8211;openpgp</code></p>
<dd> This option will make mcrypt to use the OpenPGP (RFC2440) file format for encrypted files. This will make files encrypted by mcrypt accessible from any OpenPGP compliant application.</p>
<dt><code>-b &#8211;bare</code></p>
<dd> No important information like the algorithm, mode, the bit mode and the crc32 of the original file are written in the encrypted file. The security lies on the algorithm not on obscurity so this is NOT the default. This flag must also be specified when decrypting a bare encrypted file. When the bare flag is specified decryption and encryption are faster. This may be useful when using mcrypt to encrypt a link or something like that.</p>
<dt><code>&#8211;flush</code></p>
<dd> Flushes the output (ciphertext or plaintext) immediately. Useful if mcrypt is used with pipes.</p>
<dt><code>&#8211;time</code></p>
<dd> Prints some timing information (encryption speed etc.)</p>
<dt><code>&#8211;nodelete</code></p>
<dd> When this option is specified mcrypt does not delete the output file, even if decryption failed. This is useful if you want to decrypt a corrupted file.</p>
<dt><code>-q &#8211;quiet</code></p>
<dd> Suppress some not critical warnings.</p>
<dt><code>-u &#8211;unlink</code></p>
<dd> Unlink (delete) the input file if the whole process of encryption/decryption succeeds. This is not the default in order to use an external program to remove sensitive data.</p>
<dt><code>&nbsp;<wbr>&#8211;list</code></p>
<dd> Lists all the algorithms current supported.</p>
<dt><code>&nbsp;<wbr>&#8211;list-keymodes</code></p>
<dd> Lists all the key modes current supported.</p>
<dt><code>&nbsp;<wbr>&#8211;list-hash</code></p>
<dd> Lists all the hash algorithms current supported.</p>
<dt><code>-r &#8211;random</code></p>
<dd> Use /dev/(s)random instead of /dev/urandom. This may need some key input or mouse move to proceed. If your system does not support /dev/random or /dev/urandom, a random gatherer will be used.</p>
<dt><code>-k &#8211;key KEY1 KEY2 &#8230;</code></p>
<dd> Enter the keyword(s) via the command line. The KEY(s) is/are then used as keyword instead of prompting for them. Keep in mind that someone may see the command you are executing and so your keyword(s).</p>
<dt><code>-c &#8211;config FILE</code></p>
<dd> Use the specified configuration file. The default is .mcryptrc in your home directory. The format of the configuration file is the same as the parameters. An example file is:<br />
&nbsp;<wbr>algorithm safer+<br />
&nbsp;<wbr>mode cbc<br />
&nbsp;<wbr>key a_very_secret_one </p>
<dt><code>-f &#8211;keyfile FILE</code></p>
<dd> Enter the keyword(s) via a file. One keyword is read per line. The first keyword read is used for the first file, the second for the second file etc. If the keywords are less than the files then the last keyword is used for the remaining. A limitation is that you cannot use the NULL (
