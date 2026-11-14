---
title: "ccrypt(1)"
name: "ccrypt"
section: "1"
letter: "c"
url: "/docs/linux/man/1-ccrypt/"
description: "ccrypt – encrypt and decrypt files and streams"
---

<h2>NAME</h2>
<p> ccrypt &#8211; encrypt and decrypt files and streams</p>
<h2>SYNOPSIS</h2>
<pre><code>
ccrypt[mode][options][file...] ccencrypt[options][file...] ccdecrypt[options][file...] ccat[options] file...
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ccrypt</code> is a utility for encrypting and decrypting files and streams. It was designed to replace the standard unix <code>crypt</code> utility, which is notorious for using a very weak encryption algorithm. <code>ccrypt</code> is based on the Rijndael block cipher, a version of which was also chosen by the U.S. government as the Advanced Encryption Standard (AES, see <a rel="nofollow" href="http://www.nist.gov/aes">http://www.nist.gov/aes</a>). This cipher is believed to provide very strong cryptographic security. </p>
<p> Unlike unix <code>crypt</code>, the algorithm provided by <code>ccrypt</code> is not symmetric, i.e., one must specify whether to encrypt or decrypt. The most common way to invoke <code>ccrypt</code> is via the commands <code>ccencrypt</code> and <code>ccdecrypt</code>. </p>
<p> Encryption and decryption depends on a keyword (or key phrase) supplied by the user. By default, the user is prompted to enter a keyword from the terminal. Keywords can consist of any number of characters, and all characters are significant (although <code>ccrypt</code> internally hashes the key to 256 bits). Longer keywords provide better security than short ones, since they are less likely to be discovered by exhaustive search.</p>
<h2>MODES</h2>
<p> <code>ccrypt</code> can operate in five different modes. If more than one mode is specified, the last one specified takes precedence. The aliases <code>ccencrypt</code>, <code>ccdecrypt</code>, and <code>ccat</code> are provided as a convenience; they are equivalent to <code>ccrypt -e</code>, <code>ccrypt -d</code>, and <code>ccrypt -c</code>, respectively.</p>
<dl>
<dt><code>-e, &#8211;encrypt</code></p>
<dd> Encrypt. This is the default mode. If filename arguments are given, encrypt the files and append the suffix <code>.cpt</code> to their names. Otherwise, run as a filter.</p>
<dt><code>-d, &#8211;decrypt</code></p>
<dd> Decrypt. If filename arguments are given, decrypt the files and strip the suffix <code>.cpt</code> from the filenames, if present. Otherwise, run as a filter.</p>
<dt><code>-c, &#8211;cat</code></p>
<dd> Decrypt one or more files to standard output. If no filename arguments are given, decrypt as a filter. Implies <code>-l</code>.</p>
<dt><code>-x, &#8211;keychange</code></p>
<dd> Change the key of encrypted data. In this mode, <code>ccrypt</code> prompts for two passwords: the old one and the new one. If filename arguments are given, modify the files. Otherwise, run as a filter.</p>
<dt><code>-u, &#8211;unixcrypt</code></p>
<dd> Simulate the old unix crypt command. Note: the cipher used by unix crypt has been broken and is not secure. Please use this option only to decrypt existing files. If filename arguments are given, decrypt the files to stdout. Otherwise, run as a filter. Note that for the unix crypt format, there is no easy way to detect whether a given key matches or not; thus, for safety, this mode does not overwrite files.</dl>
<h2>OPTIONS</h2>
<p> The following options are supported in addition to the modes described above:</p>
<dl>
<dt><code>-b, &#8211;brave</code></p>
<dd> When reading an encryption key from the terminal, ask the user only once for the key. By default, <code>ccrypt</code> will ask the user to enter such keys twice, as a safeguard against accidentally destroying data due to a mistyped key. Using the <code>&#8211;brave</code> option disables this safety check. Never use it, unless you know what you are doing. See also <code>&#8211;timid</code>.</p>
<dt><code>-E </code><i>var</i>, &#8211;envvar <i>var</i></p>
<dd> Read the keyword from the environment variable <i>var</i>. Note that this might be unsafe on certain systems, namely where users can use the <code>ps</code> command to see the environment of a process owner by another user. On most modern systems, however, such behavior of <code>ps</code> is disabled and the <code>-E</code> option should be safe there. Also, as an added security measure, <code>ccrypt</code> erases the keyword from its environment immediately after reading it.</p>
<dt><code>-f, &#8211;force</code></p>
<dd> Overwrite existing files or operate on write-protected files without asking any questions. Also, override <code>ccrypt</code>&#8216;s reluctance to write or read encrypted data to or from a terminal.</p>
<dt><code>-F </code><i>var</i>, &#8211;envvar2 <i>var</i></p>
<dd> Same as <code>-E</code>, except for second keyword (in keychange mode).</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Help. Print usage information and exit.</p>
<dt><code>-H </code><i>key</i>, &#8211;key2 <i>key</i></p>
<dd> Same as <code>-K</code>, except for second keyword (in keychange mode).</p>
<dt><code>-k </code><i>file</i>, &#8211;keyfile <i>file</i></p>
<dd> Read the keyword as the first line from the named file. In keychange mode, two keywords are read as the first two lines of the file. The filename &quot;-&quot; may be given for reading keywords from standard input. Using the <code>-k &#8211;</code> option and sending the keyword on stdin is probably the safest way to pass a keyword to <code>ccrypt</code> from another program or script.</p>
<dt><code>-K </code><i>key</i>, &#8211;key <i>key</i></p>
<dd> Specify the keyword on the command line. This is unsafe, because any other user can see the command line by running the <code>ps</code> command. Only use this option for testing purposes, and never with a real keyword.</p>
<dt><code>-y </code><i>file</i>, &#8211;keyref <i>file</i></p>
<dd> In encryption or keychange mode, check the encryption key against the named file, which must have been previously encrypted with the same key. Exit with an error message if the key does not match. This option is useful as an alternative to <code>&#8211;timid</code>, to guard against mistyped keys in situations where several files are encrypted with the same key. This option implies <code>&#8211;brave</code>, unless the <code>&#8211;timid</code> option is explicitly given after the <code>&#8211;keyref</code> option.</p>
<dt><code>-l, &#8211;symlinks</code></p>
<dd> Force encryption/decryption of symbolic links. By default, symbolic links are ignored except in cat or unixcrypt mode. Note that with the <code>-l</code> option, encryption/decryption of a symbolic link causes the suffix <code>.cpt</code> to be added/removed from the name of the link, not the name of the file pointed to.</p>
<dt><code>-L, &#8211;license</code></p>
<dd> Print license info and exit.</p>
<dt><code>-m, &#8211;mismatch</code></p>
<dd> Normally, <code>ccrypt</code> refuses to decrypt data with a key that does not seem to match. The <code>-m</code> option overrides this restriction. This can sometimes be useful in recovering data from a corrupted file (see RECOVERING DATA FROM CORRUPTED FILES). To avoid irretrievable loss of data when decrypting with a wrong key, this option cannot be used with modes that overwrite the input file.</p>
<dt><code>-P </code><i>prompt</i>, &#8211;prompt <i>prompt</i></p>
<dd> Use <i>prompt</i> instead of the default prompt &quot;Enter encryption/decryption key: &quot;. This may be useful in some shell scripts.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Suppress most warnings.</p>
<dt><code>-Q </code><i>prompt</i>, &#8211;prompt2 <i>prompt</i></p>
<dd> Same as <code>-P</code>, except for second keyword (in keychange mode).</p>
<dt><code>-r, &#8211;recursive</code></p>
<dd> Traverse subdirectories recursively.</p>
<dt><code>-R, &#8211;rec-symlinks</code></p>
<dd> Traverse subdirectories recursively, and also follow symbolic links to subdirectories.</p>
<dt><code>-s, &#8211;strictsuffix</code></p>
<dd> Refuse to encrypt files that already have the <code>.cpt</code> suffix (or that selected with <code>-S</code>). This can be useful when adding some files to a directory of already encrypted files. This option has no effect in decryption or keychange mode.</p>
<dt><code>-S </code><i>.suf</i>, &#8211;suffix <i>.suf</i></p>
<dd> Use the suffix <i>.suf</i> instead of the default suffix <code>.cpt</code>.</p>
<dt><code>-t, &#8211;timid</code></p>
<dd> When reading an encryption key from the terminal, ask the user to enter the key twice. If the two entered keys are not identical, abort. This is a safeguard against accidentally destroying data by encrypting it with a mistyped key. Note: this behavior is now the default, and can be overridden with the <code>&#8211;brave</code> option.</p>
<dt><code>-T, &#8211;tmpfiles</code></p>
<dd> This option causes <code>ccrypt</code> to use temporary files during encryption/decryption, rather than overwriting the file contents destructively. This method leaves the original file contents lying around in unused sectors of the file system, and thus is less secure than the default behavior. However, in situations where this loss of security is not important, the <code>&#8211;tmpfiles</code> option can provide a measure of protection against data being corrupted due to a system crash in the middle of overwriting a file.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Print progress information to stderr.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print version info and exit.</p>
<dt><code>&#8212;</code></p>
<dd> End of options. Any remaining arguments are interpreted as filenames. This also turns off filter mode, even if zero filenames follow. This might be useful in the context of shell pattern expansion; <code>ccrypt &#8212; *</code> will behave correctly even if no files match the pattern <code>*</code>.</dl>
<h2>NOTES ON USAGE</h2>
<p> The user interface of <code>ccrypt</code> intentionally resembles that of GNU <code>gzip</code>, although it is not identical. When invoked with filename arguments, <code>ccrypt</code> normally modifies the files in place, overwriting their old content. Unlike <code>gzip</code>, the output is not first written to a temporary file; instead, the data is literally overwritten. For encryption, this is usually the desired behavior, since one does not want copies of the unencrypted data to remain in hidden places in the file system. The disadvantage is that if <code>ccrypt</code> is interrupted in the middle of writing to a file, the file will end up in a corrupted, partially encrypted state. However, in such cases it is possible to recover most of the data; see RECOVERING DATA FROM CORRUPTED FILES below. If you want to force <code>ccrypt</code> to use temporary files, use the <code>&#8211;tmpfiles</code> option. </p>
<p> When <code>ccrypt</code> receives an interrupt signal (Ctrl-C) while updating a file in place, it does not exit immediately, but rather delays the exit until after it finishes writing to the current file. This is to prevent files from being partially overwritten and thus corrupted. If you want to force <code>ccrypt</code> to exit immediately, just press Ctrl-C twice quickly. </p>
<p> The encryption algorithm used by <code>ccrypt</code> uses a random seed that is different each time. As a result, encrypting the same file twice will never yield the same result. The advantage of this method is that similarities in plaintext do not lead to similarities in ciphertext; there is no way of telling whether the content of two encrypted files is similar or not. </p>
<p> Because of the use of a random seed, decrypting and re-encrypting a file with the same key will not lead to an identical file. It is primarily for this reason that <code>ccrypt</code> refuses to decrypt files with a non-matching key; if this were allowed, there would be no way afterwards to restore the original file, and the data would be irretrievably lost. </p>
<p> When overwriting files, special care is taken with hard links and symbolic links. Each physical file (i.e., each inode) is processed at most once, no matter how many paths to it are encountered on the command line or in subdirectories traversed recursively. For each file that has multiple hard links, a warning is printed, to alert the user that not all paths to the file might have been properly renamed. Symbolic links are ignored except in cat mode, or unless the <code>-l</code> or <code>-R</code> option is given. </p>
<p> Unlike <code>gzip</code>, <code>ccrypt</code> does not complain about files that have improper suffixes. It is legal to doubly encrypt a file. It is also legal to decrypt a file that does not have the <code>.cpt</code> suffix, provided the file contains valid data for the given decryption key. Use the <code>&#8211;strictsuffix</code> option if you want to prevent <code>ccrypt</code> from encrypting files that already have a <code>.cpt</code> suffix. </p>
<p> Regarding encryption and compression: encrypted data is statistically indistinguishable from random data, and thus it cannot be compressed. But of course it is possible to compress the data first, then encrypt it. Suggested file suffixes are <code>.gz.cpt</code> or <code>.gzc</code>.</p>
<h2>RECOVERING DATA FROM CORRUPTED FILES</h2>
<p> Encrypted data might be corrupted for a number of reasons. For instance, a file might have been partially encrypted or decrypted if <code>ccrypt</code> was interrupted while processing the file. Or data might be corrupted by a software or hardware error, or during transmission over a network. The encryption algorithm used by <code>ccrypt</code> is designed to allow recovery from errors. In general, only a few bytes of data will be lost near where the error occurred. </p>
<p> Data encrypted by <code>ccrypt</code> can be thought of as a sequence of 32-byte blocks. To decrypt a particular block, <code>ccrypt</code> only needs to know the decryption key, the data of the block itself, and the data of the block immediately preceding it. <code>ccrypt</code> cannot tell whether a block is corrupted or not, except the very first block, which is special. Thus, if the encrypted data has been altered in the middle or near the end of a file, <code>ccrypt</code> can be run to decrypt it as usual, and most of the data will be decrypted correctly, except near where the corruption occurred. </p>
<p> The very first block of encrypted data is special, because it does not actually correspond to any plaintext data; this block holds the random seed generated at encryption time. <code>ccrypt</code> also uses the very first block to decide whether the given keyword matches the data or not. If the first block has been corrupted, <code>ccrypt</code> will likely decide that the keyword does not match; in such cases, the <code>-m</code> option can be used to force <code>ccrypt</code> to decrypt the data anyway. </p>
<p> If a file contains some encrypted and some unencrypted data, or data encrypted with two different keys, one should decrypt the entire file with each applicable key, and then piece together the meaningful parts manually. </p>
<p> Finally, decryption will only produce meaningful results if the data is aligned correctly along block boundaries. If the block boundary information has been lost, one has to try all 32 possibilities.</p>
<h2>DESCRIPTION OF THE CIPHER</h2>
<p> <i>Block ciphers</i> operate on data segments of a fixed length. For instance, the Rijndael block cipher used in <code>ccrypt</code> has a block length of 32 bytes or 256 bits. Thus, this cipher encrypts 32 bytes at a time. </p>
<p> <i>Stream ciphers</i> operate on data streams of any length. There are several standard modes for operating a block cipher as a stream cipher. One such standard is <i>Cipher Feedback (CFB)</i>, defined in NIST Special Publication 800-38A and ANSI X3.106-1983. <code>ccrypt</code> implements a stream cipher by operating the Rijndael block cipher in CFB mode. </p>
<p> Let <i>P[i]</i> and <i>C[i]</i> be the <i>i</i>th block of the plaintext and ciphertext, respectively. CFB mode specifies that</p>
<dl>
<dt>
<dd>
<pre><code>
C[i] = P[i] ^ E(k, C[i - 1])
</code></pre>
</dl>
<p> Here <i>^</i> denotes the bitwise exclusive or function, and <i>E(k,x)</i> denotes the encryption of the block <i>x</i> under the key <i>k</i> using the block cipher. Thus, each block of the ciphertext is calculated from the corresponding block of plaintext and the previous block of ciphertext. Note that in fact, each byte of <i>P[i]</i> can be calculated from the corresponding byte of <i>C[i]</i>, so that the stream cipher can be applied to one byte at a time. In particular, the stream length need not be a multiple of the block size. </p>
<p> Assuming that blocks are numbered starting from <i>0</i>, a special &quot;initial&quot; ciphertext block <i>C[-1]</i> is needed to provide the base case for the above formula. This value <i>C[-1]</i> is called the <i>initialization vector</i> or <i>seed</i>. The seed is chosen at encryption time and written as the first block of the encrypted stream. It is important that the seed is unpredictable; in particular, the same seed should never by used more than once. Otherwise, the two resulting ciphertext blocks <i>C[0]</i> could be related by a simple xor to obtain information about the corresponding plaintext blocks <i>P[0]</i>. If unpredictable seeds are used, CFB is provably as secure as the underlying block cipher. </p>
<p> In <code>ccrypt</code>, the seed is constructed as follows: first, a nonce is contructed by hashing a combination of the host name, current time, process id, and an internal counter into a 28-byte value, using a cryptographic hash function. The nonce is combined with a fixed four-byte &quot;magic number&quot;, and the resulting 32-byte value is encrypted by one round of the Rijndael block cipher with the given key. This encrypted block is used as the seed and appended to the beginning of the ciphertext. The use of the magic number allows <code>ccrypt</code> to detect non-matching keys before decryption.</p>
<h2>SECURITY</h2>
<p> <code>ccrypt</code> is believed to provide very strong cryptographic security, equivalent to that of the Rijndael cipher with 256-bit block size and 256-bit key size. Another version of the Rijndael cipher (with a smaller block size) is used in the U.S. government&#8217;s Advanced Encryption Standard (AES, see <a rel="nofollow" href="http://www.nist.gov/aes">http://www.nist.gov/aes</a>). Therefore, this cipher is very well studied and subject to intensive public scrutiny. This scrutiny has a positive effect on the cipher&#8217;s security. In particular, if an exploitable weakness in this cipher were ever discovered, this would become widely publicized. </p>
<p> In practical terms, the security of <code>ccrypt</code> means that, without knowledge of the encryption key, it is effectively impossible to obtain any information about the plaintext from a given ciphertext. This is true even if a large number of plaintext-ciphertext pairs are already known for the same key. Moreover, because <code>ccrypt</code> uses a key size of 256 bits, an exhaustive search of the key space is not feasible, at least as long as sufficiently long keys are actually used in practice. No cipher is secure if users choose insecure keywords. </p>
<p> On the other hand, <code>ccrypt</code> does not attempt to provide <i>data integrity</i>, i.e., it will not attempt to detect whether the ciphertext was modified after encryption. In particular, encrypted data can be truncated, leaving the corresponding decrypted data also truncated, but otherwise consistent. If one needs to ensure data integrity as well as secrecy, this can be achieved by other methods. The recommended method is to prepend a cryptographic hash (for instance, an SHA-1 hash) to the data before encryption. </p>
<p> <code>ccrypt</code> does not claim to provide any particular safeguards against information leaking via the local operating system. While reasonable precautions are taken, there is no guarantee that keywords and plaintexts have been physically erased after encryption in completed; parts of such data might still exist in memory or on disk. <code>ccrypt</code> does not currently use privileged memory pages. </p>
<p> When encrypting files, <code>ccrypt</code> by default accesses them in read-write mode. This normally causes the original file to be physically overwritten, but on some file systems, this might not be the case. </p>
<p> Note that the use of the <code>-K</code> option is unsafe in a multiuser environment, because the command line of a process is visible to other users running the <code>ps</code> command. The use of the <code>-E</code> option is potentially unsafe for the same reason, although recent versions of <code>ps</code> don&#8217;t tend to display environment information to other users. The use of the <code>-T</code> option is unsafe for encryption because the original plaintext will remain in unused sectors of the file system.</p>
<h2>EMACS PACKAGE</h2>
<p> There is an emacs package for reading and writing encrypted files. (Note that this package currently only works with emacs, not with xemacs.) This package hooks into the low-level file I/O functions of emacs, prompting the user for a password where appropriate. It is implemented in much the same way as support for compressed files. If you have both the ps-ccrypt and jka-compr packages installed, emacs can open encrypted files and compressed files; however, it does not currently work for files that are encrypted and compressed. </p>
<p> To use the package, simply load ps-ccrypt, then edit as usual. When you open a file with the &quot;.cpt&quot; extension, emacs will prompt you for a password for the file. It will remember the password for the buffer, and when you save the file later, it will be automatically encrypted again (provided you save it with a &quot;.cpt&quot; extension). Except for the password prompt, the operation of the package should be transparent to the user. The command M-x ccrypt-set-buffer-password can be used to change the current password of a buffer. </p>
<p> The simplest way to use this package is to include the lines</p>
<dl>
<dt>
<dd>
<pre>
(setq load-path (cons &quot;<i>path</i>&quot; load-path)) 
(require 'ps-ccrypt &quot;ps-ccrypt.el&quot;)
</pre>
</dl>
<p> in your .emacs file, where <i>path</i> is the directory that holds the file ps-ccrypt.el. </p>
<p> Limitations of the emacs package: there is no guarantee that unencrypted information cannot leak to the file system; in fact, the package sometimes writes unencrypted data to temporary files. However, auto-saved files are normally treated correctly (i.e., encrypted). For details, see the comments in the file ps-ccrypt.el.</p>
<h2>EXIT STATUS</h2>
<p> The exit status is 0 on successful completion, and non-zero otherwise. An exit status of 1 means illegal command line, 2 is out of memory or another system error, 3 is a fatal i/o error, 4 is a non-matching key or wrong file format, 6 is interrupt, 7 is mistyped key in <code>&#8211;timid</code> mode, 8 is a non-fatal i/o error, and 9 means that no key was obtained because the user failed to enter it, or because the specified keyfile or environment variable could not be read. An exit status of 10 means that the file specified by the <code>&#8211;keyref</code> option could not be read, or did not match the requested encryption key. </p>
<p> Fatal i/o errors are those that occur while processing a file that is already open. Such errors cause ccrypt to abort its operation immediately with an exit status of 3. Non-fatal i/o errors are those that occur while handling files that are not already open; typically, such errors are caused by files that are missing, not readable, or can&#8217;t be created. When encountering a non-fatal i/o error, ccrypt simply continues to process the next available input file. The exit status of 8 is delayed until after all the files have been processed. </p>
<p> Non-matching keys and wrong file formats are also considered non-fatal errors, and cause ccrypt to continue with processing the next available input file. In this case, an exit status of 4 is given after all the files have been processed. If there is a conflict between exit status 4 and 8, then 8 is returned. </p>
<p> The former exit status 5 (&quot;wrong file format&quot;) has been eliminated, and is now covered under exit status 4 (&quot;non-matching key or wrong file format&quot;). Note that ccrypt does not really have a &quot;file format&quot; in the proper sense of the word; any file of length at least 32 bytes is potentially a valid encrypted file.</p>
<h2>BUGS</h2>
<p> While <code>ccrypt</code> can handle keywords of arbitrary length, some operating systems limit the length of an input line to 1024 characters. </p>
<p> The renaming of files (adding or removing the <code>.cpt</code> suffix) can go wrong if a filename is repeated on the command line. In this case, the file is only encrypted/decrypted once, but the suffix may be added or removed several times. This is because <code>ccrypt</code> thinks it encountered different hardlinks for the same file. </p>
<p> The <code>&#8211;strictsuffix</code> option can behave in unexpected ways if one file has several hardlinks, some of which have the suffix and some of which don&#8217;t. In this case, the inode will be encrypted/decrypted, but the suffix will be changed only for those filenames that allow it. Similarly, if a file cannot be renamed because a file of the given name already exists, the file may still be encrypted/decrypted if it has another hardlink.</p>
<h2>VERSION</h2>
<p> 1.10</p>
<h2>AUTHOR</h2>
<p> Peter Selinger &lt;selinger at users.sourceforge.net&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2012 Peter Selinger </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA. See also <a rel="nofollow" href="http://www.gnu.org/.">http://www.gnu.org/.</a> </p>
<h2>Index</h2>
