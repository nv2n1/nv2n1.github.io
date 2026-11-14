---
title: "stoken(1)"
name: "stoken"
section: "1"
letter: "s"
url: "/docs/linux/man/1-stoken/"
description: "stoken – software token for cryptographic authentication"
---

<h2 class="name">NAME</h2>
<p> stoken &#8211; software token for cryptographic authentication </p>
<h2>SYNOPSIS</h2>
<p> <code>stoken</code> [<code>tokencode</code>] [<code>&#8211;stdin</code>] [<code>&#8211;force</code>] [<code>&#8211;next</code>] [<i>opts</i>] </p>
<p> <code>stoken</code> <code>import</code> {<code>&#8211;file=</code><i>file</i> | <code>&#8211;token=</code><i>token_string</i>} [<code>&#8211;force</code>] [<i>opts</i>] </p>
<p> <code>stoken</code> <code>setpin</code> [<i>opts</i>] </p>
<p> <code>stoken</code> <code>setpass</code> [<i>opts</i>] </p>
<p> <code>stoken</code> <code>show</code> [<code>&#8211;seed</code>] [<i>opts</i>] </p>
<p> <code>stoken</code> <code>export</code> [{<code>&#8211;blocks</code> | <code>&#8211;iphone</code> | <code>&#8211;android</code> | <code>&#8211;v3</code> | <code>&#8211;sdtid</code> | <code>&#8211;qr=</code><i>file.png</i> | <code>&#8211;show-qr</code>}] [<i>opts</i>] </p>
<p> <code>stoken</code> <code>issue</code> [&#8211;<code>template</code>=<i>file</i>] </p>
<p> <code>stoken</code> <code>help</code> </p>
<p> <code>stoken</code> <code>version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>stoken</code> is a software token compatible with RSA SecurID 128-bit (AES) tokens. The command-line interface provides facilities for importing new tokens, displaying the current tokencode, encrypting the seed with a user-specified password, storing the user&#8217;s PIN alongside the token, and viewing or exporting the token data.</p>
<h2>BASIC USAGE</h2>
<p> Use <code>stoken import</code> to decode a token string and write it into <i>~/.stokenrc</i>. This may prompt for a device ID and/or password, depending on what options your administrator used to create the token. The token string can be provided on the command line, or read from a text file. </p>
<p> <code>stoken</code> will autodetect the following types of token strings:</p>
<dl>
<dt><code>286510182209303756117707012447003320623006&#8230;</code></p>
<dd>
<dt><code>29658-21098-45467-64675-65731-01441-11337&#8230;</code></p>
<dd> Pure numeric (81-digit) &quot;ctf&quot; (compressed token format) strings, with or without dashes. These may have been furnished as-is, or they could have been derived from an <i>sdtid</i> file by the RSA <i>TokenConverter</i> program.</p>
<dt><code>com.rsa.securid.<a href="iphone://ctf?ctfData=229639330774927764401...">iphone://ctf?ctfData=229639330774927764401&#8230;</a></code></p>
<dd> iPhone-compatible token strings.</p>
<dt><code><a rel="nofollow" href="http://127.0.0.1/securid/ctf?ctfData=250494932146245277466...">http://127.0.0.1/securid/ctf?ctfData=250494932146245277466&#8230;</a></code></p>
<dd>
<dt><code><a rel="nofollow" href="http://127.0.0.1/securid/ctf?ctfData=AwAAfBc3QSopPxxjLGnxf...">http://127.0.0.1/securid/ctf?ctfData=AwAAfBc3QSopPxxjLGnxf&#8230;</a></code></p>
<dd> Android-compatible token strings.</p>
<dt><code>&lt;?xml version=&#8230;</code></p>
<dd> RSA <i>sdtid</i>-formatted XML files. These should be imported from a file: <code>stoken import &#8211;file=FILE.SDTID</code>.</dl>
<p> Tokens supplied as QR codes can be converted back to standard URIs by running <code><a href="/docs/linux/man/1-zbarimg/">zbarimg</a></code>(1) on the image file. </p>
<p> The device ID, if used, can be viewed in the &quot;about&quot; menu for the RSA soft token app on the phone. Numeric ctf strings and smartphone tokens bound to a device ID contain a seed that is encrypted using the device ID, so the ID must be furnished before stoken can successfully import the token. <i>sdtid</i> files can be imported without knowledge of the device ID, as long as the password (if any) is known. </p>
<p> By default, <code>stoken import</code> will refuse to overwrite an existing token in <i>~/.stokenrc</i>. The <code>&#8211;force</code> switch overrides this check. </p>
<p> <code>stoken import</code> will normally prompt for a new password, which is used to encrypt the seed before storing it in <i>~/.stokenrc</i>. This can be bypassed by entering an empty password, or specifying <code>&#8211;new-password=&#8221;</code> on the command line. It is recommended to choose a longer, hard-to-guess passphrase for this purpose. </p>
<p> After a token has been imported, running <code>stoken</code> with no arguments will prompt for any required password or PIN, then display the current tokencode. </p>
<p> Tokencodes are computed from the raw (decrypted) seed data, the current time of day, and the PIN. If the same seed is installed on multiple devices, they should all produce identical tokencodes. If they do not, double-check the timezone setting and consider using NTP to synchronize the system time to a known good source. </p>
<p> <code>stoken setpin</code> can be used to save the PIN in <i>~/.stokenrc</i>. Not all tokens will require a PIN; this can be configured by the SecurID administrator when generating new tokens. Setting an empty PIN will remove the PIN from <i>~/.stokenrc</i> so that the user will be prompted every time it is required. See the <code>SECURITY CONSIDERATIONS</code> section below for additional details. </p>
<p> <code>stoken setpass</code> encrypts the seed and PIN (if present) in <i>~/.stokenrc</i> with a user-selectable password or passphrase. If an empty password is entered, the password will be removed. See the <code>SECURITY CONSIDERATIONS</code> section below for additional details.</p>
<h2>VIEWING TOKENS</h2>
<p> <code>stoken show</code> displays information about the current token, typically read from <i>~/.stokenrc</i>. The <code>&#8211;seed</code> option displays the encrypted and decrypted seed bytes (which should be treated as sensitive data, as they can be used to derive tokencodes). </p>
<p> <code>stoken export</code> translates the current token into a format suitable for importation to another device. </p>
<p> <code>stoken issue</code> generates a new software token in XML <i>sdtid</i> format. A template file, itself in <i>sdtid</i> format, may be provided to override some or all of the human-readable fields. This would permit appropriate serial numbers, expiration dates, usernames, etc. to be specified. If Secret, Seed, or MAC fields are present in the template file, they will be ignored.</p>
<h2>GLOBAL OPTIONS</h2>
<dl>
<dt><code>&#8211;rcfile=</code><i>file</i></p>
<dd> Use an alternate <i>.stokenrc</i> configuration file. This is typically used to support multiple tokens on the same user&#8217;s UNIX account. Note that the <i>.stokenrc</i> file stores additional data (such as the PIN), so it cannot be parsed as a &quot;raw&quot; token string by <code>stoken &#8211;file</code>.</p>
<dt><code>&#8211;password=</code><i>password</i>, <code>-p</code> <i>password</i></p>
<dd> Use a password supplied from the command line, instead of prompting the user. See notes in <code>SECURITY CONSIDERATIONS</code> below.</p>
<dt><code>&#8211;pin=</code><i>pin</i>, <code>-n</code> <i>pin</i></p>
<dd> Use a PIN supplied from the command line, instead of prompting the user. See notes in <code>SECURITY CONSIDERATIONS</code> below. If you save your PIN in <i>~/.stokenrc</i>, note that <code>&#8211;pin=0000</code> is often required when activating a new soft token for the first time.</p>
<dt><code>&#8211;devid=</code><i>devid</i></p>
<dd> Use a device ID supplied from the command line to decrypt the token. A token can be bound to a class GUID device ID (i.e. a certain type of device, such as &quot;iPhone&quot; or &quot;Android&quot;), a unique device ID (one specific unit), or nothing. <code>stoken</code> will attempt to autodetect matches with a class GUID, but on rare occasions this results in false positives due to hash collisions. In these cases, the bound device ID should be specified on the command line to override autodetection.</dl>
<h2>EXPORT OPTIONS</h2>
<dl>
<dt><code>&#8211;new-password=</code><i>password</i></p>
<dd> Supply the encryption password from the command line for operations that write out a token string or <i>.stokenrc</i> file: <code>import</code>, <code>export</code>, <code>setpass</code>, and <code>issue</code>. See notes in <code>SECURITY CONSIDERATIONS</code> below.</p>
<dt><code>&#8211;keep-password</code></p>
<dd> If the token in the <i>.stokenrc</i> file is protected with a password, retain the same password when exporting the token. By default, the <code>export</code> operation will not encrypt the token with a password; note that it may not be possible to enter all possible passwords on devices with limited text input capabilities (such as feature phones).</p>
<dt><code>&#8211;new-pin=</code><i>pin</i></p>
<dd> Supply a new PIN from the command line for the <code>setpin</code> operation. See notes in <code>SECURITY CONSIDERATIONS</code> below.</p>
<dt><code>&#8211;new-devid=</code><i>devid</i></p>
<dd> Used with the <code>export</code> or <code>issue</code> command to encrypt the new token with a specific device ID. This is only used for testing purposes.</p>
<dt><code>&#8211;blocks</code>, <code>&#8211;iphone</code>, <code>&#8211;android</code>, <code>&#8211;v3</code></p>
<dd> Used with the <code>export</code> command to select the output format. See examples in <code>BASIC USAGE</code>. By default, the <code>export</code> command will print an unformatted 81-digit string to standard output.</p>
<dt><code>&#8211;sdtid</code>, <code>&#8211;xml</code></p>
<dd> These options are synonyms. Both export a token to standard output in RSA&#8217;s <i>sdtid</i> XML format.</p>
<dt><code>&#8211;qr=</code><i>file.png</i></p>
<dd> Encode the token as a QR code and write it to <i>file.png</i>. This requires the <code>qrencode</code> program to be installed.</p>
<dt><code>&#8211;show-qr</code></p>
<dd> Encode the token as a QR code and immediately display it on the screen. This requires the <code>qrencode</code> program to be installed. If the <code>QR_VIEWER</code> environment variable is set, <code>stoken</code> will use that program as the preferred viewer. Otherwise it will try to execute a few common Linux image viewers, and give up if none of them exist.</p>
<dt><code>&#8211;template=</code><i>file</i></p>
<dd> Used with the <code>export</code> or <code>issue</code> commands to override fields in the XML output. The template file should look like any standard <i>sdtid</i> file, but all fields are optional and will default to reasonably sane values if omitted. This can be used to force the output XML to use a specific serial number, user name, expiration date, etc. Correct MAC checksums will be (re)computed on the provided values. See the <i>examples</i> directory in the source distribution for more information.</dl>
<h2>OTHER OPTIONS</h2>
<dl>
<dt><code>&#8211;use-time=</code>{<i>unix_time</i>|<code>+</code><i>offset</i>|<code>&#8211;</code><i>offset</i>}</p>
<dd> Instead of generating a tokencode based on the current time of day, force a specific time, or adjust the current time based on a positive or negative offset (specified in seconds). This is only used for testing purposes.</p>
<dt><code>&#8211;next</code></p>
<dd> Generate the next tokencode instead of the current tokencode. For a 60-second token, this is equivalent to <code>&#8211;use-time=+60</code>.</p>
<dt><code>&#8211;stdin</code>, <code>-s</code></p>
<dd> When generating a tokencode that requires <i>either</i> a password or PIN, read the password or PIN as single line from standard input. This is intended to allow external programs to call <i>stoken</i> to generate single-use passwords without user intervention; see <code>NON-INTERACTIVE USE</code> below.</p>
<dt><code>&#8211;force</code>, <code>-f</code></p>
<dd> Override token expiration date checks (for <code>tokencode</code>) or token overwrite checks (for <code>import</code>).</p>
<dt><code>&#8211;batch</code>, <code>-b</code></p>
<dd> Abort with an error exit code if any user input is required. Intended for automated operation and testing.</p>
<dt><code>&#8211;file=</code><i>file</i></p>
<dd> Read a ctf string, an Android/iPhone URI, or an XML <i>sdtid</i> token from <i>file</i> instead of the <i>.stokenrc</i> configuration. Most <code>stoken</code> commands accept this flag, but it is expected that the typical user will save his token in <i>~/.stokenrc</i> instead of supplying it by hand on every invocation. Typically <code>&#8211;file</code> and <code>&#8211;token</code> are only used for the <code>import</code> command.</p>
<dt><code>&#8211;token=</code><i>token_string</i></p>
<dd> Use a token from the command line instead of the <i>.stokenrc</i> file. See above notes on <code>&#8211;file</code>.</p>
<dt><code>&#8211;random</code></p>
<dd> Generate a random token on the fly. Used for testing or demonstrations only. These tokens should <code>not</code> be used for real authentication.</p>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> Display basic usage information.</p>
<dt><code>&#8211;version</code>, <code>-v</code></p>
<dd> Display version information.</dl>
<h2>SECURITY CONSIDERATIONS</h2>
<p> Software tokens, unlike hardware tokens, are relatively easy to replicate. Systems that store soft token seeds should be carefully guarded to prevent unauthorized disclosure. The use of whole-disk encryption, such as TrueCrypt, is strongly recommended for laptops and other portable devices that are easily lost or stolen. </p>
<p> <code>stoken</code> permits users to store their PIN in <i>~/.stokenrc</i> to allow for automated (scriptable) generation of tokencodes, but the risks of this approach should be carefully weighed against the benefits. </p>
<p> Using the <code>setpass</code> command to encrypt the seed and PIN in <i>~/.stokenrc</i> provides some degree of protection against unauthorized access, but does not necessarily cover all possible attack vectors. A host that is already compromised (e.g. running a keylogger) will not provide adequate protection for any seed(s) stored on it. </p>
<p> <code>stoken</code> encryption passwords may be up to 40 characters long. A longer passphrase constructed from several random words can provide more protection from brute-force attacks than a shorter password. </p>
<p> Entering a password or PIN on the command line is generally unsafe on multiuser systems, as other users may be able to view the command line arguments in <code>ps</code> or similar utilities. The command line could also be cached in shell history files. </p>
<p> Encoding QR tokens may expose the seed data through <code>ps</code>, and the <code>&#8211;show-qr</code> option writes temporary PNG files in <code>/tmp</code>. </p>
<p> <code>stoken</code> attempts to lock pages to prevent swapping out to disk, but does not scrub secrets from process memory.</p>
<h2>NON-INTERACTIVE USE</h2>
<p> Other applications, such as VPN clients, may want to invoke <code>stoken</code> non-interactively to generate single-use passwords. Three usage modes are supported, depending on the level of security (and/or convenience) that is required:</p>
<h3>No password or PIN</h3>
<p> The user configures <code>stoken</code> to print a tokencode immediately upon invocation, with no prompts, by using <code>setpin</code> to store the PIN in <i>~/.stokenrc</i> and using <code>setpass</code> to set an empty password. The other application can then invoke <code>stoken &#8211;batch</code> and read the tokencode through a pipe from standard output. </p>
<p> This provides no security for the seed, but may be useful in applications where (re-)authentication is frequent or unattended operation is required.</p>
<h3>Save the PIN and set a password</h3>
<p> The user configures <code>stoken</code> to encrypt the <i>~/.stokenrc</i> secrets with a password using <code>setpass</code>, then saves the PIN with <code>setpin</code>. The PIN and the seed will both be encrypted with the password. The other application will request the password from the user, then call <code>stoken &#8211;stdin</code>, write the password to <code>stoken</code>&#8216;s standard input through a pipe, and read back a tokencode from <code>stoken</code>&#8216;s standard output.</p>
<h3>No password; prompt for the PIN</h3>
<p> Similar to above, but set an empty password using <code>setpass</code>, do not save the PIN in <i>~/.stokenrc</i>, and pass the PIN to <code>stoken &#8211;stdin</code> via standard input.</p>
<h2>BUGS/TODO</h2>
<p> <i>sdtid</i> support is still new and may choke on unexpected input. As a short-term workaround you can try commenting out the sanity checks in <code>sdtid_decrypt()</code> to see if the problem goes away. </p>
<p> Features under development include: hardware token seeds (and the <code>stoken split</code> command needed to work with them), and support for non-Linux hosts. </p>
<p> Patches are always welcome.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-stoken-gui/">stoken-gui</a></code>(1).</p>
<h2>FILES</h2>
<dl>
<dt>~/.stokenrc</p>
<dd> Default configuration file.</dl>
<h2>AUTHOR</h2>
<p> Kevin Cernekee &lt;cernekee [at] gmail.com&gt; </p>
<h2>Index</h2>
