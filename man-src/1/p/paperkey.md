---
title: "paperkey(1)"
name: "paperkey"
section: "1"
letter: "p"
url: "/docs/linux/man/1-paperkey/"
description: "paperkey – extract secret information out of OpenPGP secret keys"
---

<h2>NAME</h2>
<p> paperkey &#8211; extract secret information out of OpenPGP secret keys</p>
<h2>SYNOPSIS</h2>
<p> <code>paperkey</code> [<code>&#8211;secret-key=</code><i>FILE</i>] [<code>&#8211;output=</code><i>FILE</i>] [<code>&#8211;output-type=</code><code>base16</code>|<code>raw</code>] [<code>&#8211;output-width=</code><i>WIDTH</i>] </p>
<p> <code>paperkey</code> <code>&#8211;pubring=</code><i>FILE</i> [<code>&#8211;secrets=</code><i>FILE</i>] [<code>&#8211;input-type=</code><code>auto</code>|<code>base16</code>|<code>raw</code>] [<code>&#8211;output=</code><i>FILE</i>] [<code>&#8211;ignore-crc-error</code>] [<code>&#8211;comment=</code><i>STRING</i>] [<code>&#8211;file-format</code>] </p>
<p> <code>paperkey</code> <code>&#8211;version</code></p>
<h2>MOTIVATION</h2>
<p> As with all data, secret keys should be backed up. In fact, secret keys should be backed up even better than other data, because they are impossible to recreate should they ever be lost. All files encrypted to lost keys are forever (or at least for a long time) undecipherable. In addition to keeping backups of secret key information on digital media such as USB-sticks or CDs it is reasonable to keep an if-all-else-fails copy on plain old paper, for use should your digital media ever become unreadable for whatever reason. Stored properly, paper is able to keep information for several decades or longer. </p>
<p> With GnuPG, PGP, or other OpenPGP implementations the secret key usually contains a lot more than just the secret numbers that are important. They also hold all the public values of key pairs, user ids, expiration times and more. In order to minimize the information that has to be entered manually or with the help of OCR, QR code or similar software, <code>paperkey</code> extracts just the secret information out of OpenPGP secret keys. For recovering a secret key it is assumed that the public key is still available, for instance from public Internet keyservers.</p>
<h2>DESCRIPTION</h2>
<p> <code>paperkey</code> has two modes of operation: </p>
<p> The first mode creates &quot;paperkeys&quot; by extracting just the secret information from a secret key, formatting the data in a way suitable for printing or in a raw mode for further processing. </p>
<p> The other mode rebuilds secret keys from such a paperkey and a copy of the public key, also verifying the checksums embedded in the paperkey. This mode is selected when the <code>&#8211;pubring</code> option is used, which is required in that case. If a passphrase was set on the original secret key, the same passphrase is set on the rebuilt key. </p>
<p> Input is read from standard-in except when the <code>&#8211;secret-key</code> or <code>&#8211;secrets</code> option is used; output is printed to standard-out, unless changed with the <code>&#8211;output</code> option.</p>
<h2>SECURITY CONSIDERATIONS</h2>
<p> Please note that <code>paperkey</code> does not change the protection and encryption status of and security requirements for storing your secret key. If the secret key was protected by a passphrase so is the paperkey. If the secret key was unprotected the paperkey will not be protected either.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;help</code>, <code>-h</code> Display a short help message and exit successfully. </p>
<dl>
<dt><code>&#8211;version</code>, <code>-V</code></p>
<dd> Print version information and copyright information and exit successfully.</dl>
<dl>
<dt><code>&#8211;verbose</code>, <code>-v</code></p>
<dd> Print status and progress information to standard-error while processing the input. Repeat for even more output.</dl>
<dl>
<dt><code>&#8211;output=</code><i>FILE</i>, <code>-o</code></p>
<dd> Redirect output to the file given instead of printing to standard-output.</dl>
<dl>
<dt><code>&#8211;comment=</code><i>STRING</i></p>
<dd> Include the specified comment in the base16 output.</dl>
<dl>
<dt><code>&#8211;file-format</code></p>
<dd> Paperkey automatically includes the file format it uses as comments at the top of the base16 output. This command simply prints out the file format and exits successfully.</dl>
<h2>OPTIONS FOR EXTRACTING SECRET INFORMATION</h2>
<dl>
<dt><code>&#8211;output-type=base16</code>, <code>&#8211;output-type=raw</code></p>
<dd> Select the output type. The base16 style encodes the information in the style of a classic hex-dump, including line numbers and per-line CRC checksums to facilitate localizing errors in the input file during the recovery phase. The raw, or binary, mode is just a raw dump of the secret information, intended for feeding to barcode generators or the like.</dl>
<dl>
<dt><code>&#8211;output-width=</code><i>WIDTH</i></p>
<dd> Choose line width in the base16 output mode. The default is 78 characters.</dl>
<dl>
<dt><code>&#8211;secret-key=</code><i>FILE</i></p>
<dd> File to read the secret key from. If this option is not given <code>paperkey</code> reads from standard-input.</dl>
<h2>OPTIONS FOR RE-CREATING PRIVATE KEYS</h2>
<dl>
<dt><code>&#8211;input-type=auto</code>, <code>&#8211;input-type=base16</code>, <code>&#8211;input-type=raw</code></p>
<dd> Specify that the given input is either in base16 format, as produced by <code>paperkey</code>, or in raw format. The default, auto, tries to automatically detect the format in use.</dl>
<dl>
<dt><code>&#8211;pubring=</code><i>FILE</i></p>
<dd> File to read public key information from. It is assumed that the user can get the public key from sources like public Internet keyservers.</dl>
<dl>
<dt><code>&#8211;secrets=</code><i>FILE</i></p>
<dd> File to read the extracted secrets, the paperkey, from. If this is not given then the information is read from standard-input.</dl>
<dl>
<dt><code>&#8211;ignore-crc-error</code></p>
<dd> Do not reject corrupt input and continue despite any CRC errors.</dl>
<h2>EXAMPLES</h2>
<p> Take the secret key in key.gpg and generate a text file to-be-printed.txt that contains the secret data: </p>
<p> <code>$ paperkey &#8211;secret-key my-secret-key.gpg &#8211;output to-be-printed.txt</code> </p>
<p> Take the secret key data in my-key-text-file.txt and combine it with my-public-key.gpg to reconstruct my-secret-key.gpg: </p>
<p> <code>$ paperkey &#8211;pubring my-public-key.gpg &#8211;secrets my-key-text-file.txt &#8211;output my-secret-key.gpg</code> </p>
<p> If &#8211;output is not specified, the output goes to stdout. If &#8211;secret-key is not specified, the data is read from stdin so you can do things like: </p>
<p> <code>$ gpg &#8211;export-secret-key my-key | paperkey | lpr</code></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1), <code><a rel="nofollow" href="http://www.jabberwocky.com/software/paperkey/">http://www.jabberwocky.com/software/paperkey/</a></code></p>
<h2>AUTHORS</h2>
<p> <code>paperkey</code> is written by David Shaw &lt;dshaw [at] jabberwocky.com&gt;. </p>
<h2>Index</h2>
