---
title: "uuencode(5)"
name: "uuencode"
section: "5"
letter: "u"
url: "/docs/linux/man/5-uuencode/"
---

uuencode - format of an encoded uuencode file

<h2>Description</h2>

Files output by <a HREF="/docs/linux/man/1-uuencode/">uuencode</a>(1) consist of a header line, followed by a number of body lines, and a trailer line. The <a HREF="/docs/linux/man/1-uudecode/">uudecode</a>(1) command will ignore any lines preceding the header or following the trailer. Lines preceding a header must not, of course, look like a header. 

 The header line is distinguished by having the first 5 characters be <i>begin</i> followed by a space, or else a hyphen and either <i>base64</i> or <i>encoded</i> or both (also separated with a hyphen). The <i>base64</i> option says the file has been encoded using base64. The <i>encoded</i> option says the output file <i>name</i> has been base64 encoded. It is never encoded with traditional uuencoding. This is a GNU extension. These are followed by a mode (in octal), and a string which names the remote file. The mode is separated from the <i>begin</i> clause and the file name by a single space character.

<h3>Traditional uuencoding</h3>

The traditional <i>uuencoded</i> file body consists of a number of lines, each at most 62 characters long (including the trailing newline). These consist of a character count letter, followed by the encoded characters, followed by a newline. The character count is a single printing character, and represents an integer, the number of bytes the rest of the line represents. Such integers are always in the range from 0 to 63 and can be determined by subtracting the character space (octal 40) from the character. 

 Groups of 3 bytes are stored in 4 characters, 6 bits per character. All are offset by a space to make the characters printing. The last line may be shorter than the normal 45 bytes. If the size is not a multiple of 3, this fact can be determined by the value of the count on the last line. Extra garbage will be included to make the character count a multiple of 4. The body is terminated by a line with a count of zero. This line consists of one ASCII space. 

 The trailer line consists of <i>end</i> on a line by itself.

<h3>base64 encoding</h3>

<i>base64</i> encoded files follow the specified format for the body, but also include a <i>begin-base64</i> header and a trailer line of four <i>=</i> characters.

<h2>Examples</h2>

<pre>begin-base64-encoded 644 VE9ETw==</pre>This introduces a base64 encoded file named, <i>TODO</i> with that name encoded using base64 encoding. 

 <pre>begin-encoded 644 5$]$3P``</pre>This introduces an encoded file named, <i>TODO</i> with that name encoded using uuencoding. The encoding is a lot less friendly. Please prefer base64 encoding.

<h2>Conforming To</h2>

IEEE Std 1003.1, plus extensions 

 The <i>-encoded</i> suffix to the <i>begin</i> header line is a GNU extension. Recipients must have the GNU <i>uudecode</i> program to decode them.

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-uuencode/">uuencode</a>(1), <a HREF="/docs/linux/man/1-uudecode/">uudecode</a>(1), base64(1GNU)

<h2>History</h2>

The <i>uuencode</i> file format appeared in BSD 4.0 .
