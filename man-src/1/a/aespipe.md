---
title: "aespipe(1)"
name: "aespipe"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aespipe/"
description: "aespipe – AES encrypting or decrypting pipe"
---

<h2>NAME</h2>
<p> aespipe &#8211; AES encrypting or decrypting pipe</p>
<h2>SYNOPSIS</h2>
<p> <code>aespipe</code> [options] &lt;inputfile &gt;outputfile</p>
<h2>DESCRIPTION</h2>
<p> <code>aespipe</code> reads from standard input and writes to standard output. It can be used to create and restore encrypted tar or cpio archives. It can be used to encrypt and decrypt loop-AES compatible encrypted disk images. <code>aespipe</code> encrypts and decrypts blocks of data. If you are looking for general purpose encrypting tool that preserves data size at byte granularity, then please take a look at GnuPG. </p>
<p> The AES cipher is used in CBC (cipher block chaining) mode. Data is encrypted and decrypted in 512 byte chains. <code>aespipe</code> supports three key setup modes; single-key, multi-key-v2 and multi-key-v3 modes. Single-key mode uses simple sector IV and one AES key to encrypt and decrypt all data sectors. Multi-key-v2 mode uses cryptographically more secure MD5 IV and 64 different AES keys to encrypt and decrypt data sectors. In multi-key mode first key is used for first sector, second key for second sector, and so on. Multi-key-v3 is same as multi-key-v2 except is uses one extra 65th key as additional input to MD5 IV computation. See -K option for more information about how to enable multi-key-v3 mode. </p>
<p> Recommended key setup mode is multi-key-v3, which is based on gpg encrypted key files. In this mode, the passphrase is protected against optimized dictionary attacks via salting and key iteration of gpg. Passphrase length should be 20 characters or more. </p>
<p> Single-key mode preserves input size at 16 byte granularity. Multi-key mode preserves input size at 512 byte granularity. If input size is not multiple of 16 or 512 bytes, input data is padded with null bytes so that both input and output sizes are multiples of 16 or 512 bytes. </p>
<p> If &quot;ulimit -l&quot; is set to &quot;unlimited&quot; then <code>aespipe</code> attempts to lock its RAM so that encryption keys do not leak to unencrypted swap. If &quot;ulimit -l&quot; is something other than &quot;unlimited&quot; then <code>aespipe</code> will proceed without locked RAM.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A </code><i>gpgAgentSocket</i></p>
<dd> Read passphrase of gpg encrypted key file from gpg-agent instead of the terminal. aespipe runs gpg to decrypt a key file, and gpg talks to gpg-agent using <i>gpgAgentSocket</i>. Usually this data is in GPG_AGENT_INFO environment variable. The environment that is passed to gpg is very minimal. Normally gpg passes some environment variables to gpg-agent, but in this case, there aren&#8217;t any. For best results, you may want to configure gpg-agent so that it &quot;keeps&quot; and uses its own environment. Defining &quot;keep-tty&quot;, &quot;keep-display&quot; and &quot;pinentry-program&quot; in $HOME/.gnupg/gpg-agent.conf configuration file is a good start.</p>
<dt><code>-C </code><i>itercountk</i></p>
<dd> Runs hashed passphrase through <i>itercountk</i> thousand iterations of AES-256 before using it for data encryption. This consumes lots of CPU cycles at program start time but not thereafter. In combination with passphrase seed this slows down dictionary attacks. Iteration is not done in multi-key mode.</p>
<dt><code>-d</code></p>
<dd> Decrypt data. If this option is not specified, default operation is to encrypt data.</p>
<dt><code>-e </code><i>encryption</i></p>
<dd> Following <i>encryption</i> types are recognized: AES128 (default), AES192 and AES256. Encryption type names are case insensitive. AES128 defaults to using SHA-256 passphrase hash, AES192 defaults to using SHA-384 passphrase hash, and AES256 defaults to using SHA-512 passphrase hash.</p>
<dt><code>-G </code><i>gpghome</i></p>
<dd> Set gpg home directory to <i>gpghome</i>, so that gpg uses public/private keys on <i>gpghome</i> directory. This is only used when gpgkey file needs to be decrypted using public/private keys. If gpgkey file is encrypted with symmetric cipher only, public/private keys are not required and this option has no effect.</p>
<dt><code>-H </code><i>phash</i></p>
<dd> Uses <i>phash</i> function to hash passphrase. Available hash functions are sha256, sha384, sha512 and rmd160. unhashed1 and unhashed2 functions also exist for compatibility with some obsolete implementations. Hash type names are case insensitive.</p>
<dt><code>-K </code><i>gpgkey</i></p>
<dd> Passphrase is piped to gpg so that gpg can decrypt file <i>gpgkey</i> which contains the real keys that are used to encrypt data. If decryption requires public/private keys and gpghome is not specified, all users use their own gpg public/private keys to decrypt <i>gpgkey</i>. Decrypted <i>gpgkey</i> should contain 1 or 64 or 65 keys, each key at least 20 characters and separated by newline. If decrypted <i>gpgkey</i> contains 64 or 65 keys, then aespipe is put to multi-key mode. 65th key, if present, is used as additional input to MD5 IV computation.</p>
<dt><code>-O </code><i>sectornumber</i></p>
<dd> Set IV offset in 512 byte units. Default is zero. Data is encrypted in 512 byte CBC chains and each 512 byte chain starts with IV whose computation depends on offset within the data. This option can be used to start encryption or decryption in middle of some existing encrypted disk image.</p>
<dt><code>-p </code><i>fdnumber</i></p>
<dd> Read the passphrase from file descriptor <i>fdnumber</i> instead of the terminal. If -K option is not being used (no gpg key file), then aespipe attempts to read 65 keys from <i>passwdfd</i>, each key at least 20 characters and separated by newline. If aespipe successfully reads 64 or 65 keys, then aespipe is put to multi-key mode. If aespipe encounters end-of-file before 64 keys are read, then only first key is used in single-key mode.</p>
<dt><code>-P </code><i>cleartextkey</i></p>
<dd> Read the passphrase from file <i>cleartextkey</i> instead of the terminal. If -K option is not being used (no gpg key file), then aespipe attempts to read 65 keys from <i>cleartextkey</i>, each key at least 20 characters and separated by newline. If aespipe successfully reads 64 or 65 keys, then aespipe is put to multi-key mode. If aespipe encounters end-of-file before 64 keys are read, then only first key is used in single-key mode. If both -p and -P options are used, then -p option takes precedence. These are equivalent: </p>
<p> aespipe -p3 -K foo.gpg -e AES128 &#8230; 3&lt;someFileName </p>
<p> aespipe -P someFileName -K foo.gpg -e AES128 &#8230; </p>
<p> In first line of above example, in addition to normal open file descriptors (0==stdin 1==stdout 2==stderr), shell opens the file and passes open file descriptor to started aespipe program. In second line of above example, aespipe opens the file itself.</p>
<dt><code>-q</code></p>
<dd> Be quiet and don&#8217;t complain about write errors.</p>
<dt><code>-S </code><i>pseed</i></p>
<dd> Sets encryption passphrase seed <i>pseed</i> which is appended to user supplied passphrase before hashing. Using different seeds makes dictionary attacks slower but does not prevent them if user supplied passphrase is guessable. Seed is not used in multi-key mode.</p>
<dt><code>-T</code></p>
<dd> Asks passphrase twice instead of just once.</p>
<dt><code>-v</code></p>
<dd> Verbose mode. Prints diagnostics to stderr about key length, single/multi key mode, and selected code optimizations (x86/amd64/padlock/intelaes).</p>
<dt><code>-w </code><i>number</i></p>
<dd> Wait <i>number</i> seconds before asking passphrase.</dl>
<h2>RETURN VALUE</h2>
<p> <code>aespipe</code> returns 0 on success, nonzero on failure.</p>
<h2>AVAILABILITY</h2>
<p> Source is available from <a rel="nofollow" href="http://loop-aes.sourceforge.net/">http://loop-aes.sourceforge.net/</a></p>
<h2>AUTHORS</h2>
<p> Jari Ruusu </p>
<h2>Index</h2>
