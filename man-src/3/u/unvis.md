---
title: "unvis(3)"
name: "unvis"
section: "3"
letter: "u"
url: "/docs/linux/man/3-unvis/"
description: "unvis strunvis strnunvis – decode a visual representation of characters"
---

<p><code>unvis</code> <code>strunvis</code> <code>strnunvis</code> &#8211; decode a visual representation of characters</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<p>In bsd/vis.h Ft int Fn unvis char *cp char c int *astate int flag Ft int Fn strunvis char *dst char *src Ft ssize_t Fn strnunvis char *dst char *src size_t size</p>
<h2>Description</h2>
<p>The Fn unvis , Fn strunvis and Fn strnunvis functions are used to decode a visual representation of characters, as produced by the <a href="/docs/linux/man/3-vis/">vis</a>(3) function, back into the original form. Fn unvis is called with successive characters in Fa c until a valid sequence is recognized, at which time the decoded character is available at the character pointed to by Fa cp . </p>
<p> Fn strunvis decodes the characters pointed to by Fa src into the buffer pointed to by Fa dst . </p>
<p> Fn strnunvis decodes the characters pointed to by Fa src into the buffer pointed to by Fa dst , writing a maximum of Fa size bytes. The Fn strunvis function simply copies Fa src to Fa dst , decoding any escape sequences along the way, and returns the number of characters placed into Fa dst , or -1 if an invalid escape sequence was detected. The size of Fa dst should be equal to the size of Fa src (that is, no expansion takes place during decoding). Fn strunvis terminates the destination string with a trailing NUL byte; Fn strnunvis does so if Fa size is larger than 0. </p>
<p> The Fn unvis function implements a state machine that can be used to decode an arbitrary stream of bytes. All state associated with the bytes being decoded is stored outside the Fn unvis function (that is, a pointer to the state is passed in), so calls decoding different streams can be freely intermixed. To start decoding a stream of bytes, first initialize an integer to zero. Call Fn unvis with each successive byte, along with a pointer to this integer, and a pointer to a destination character.</p>
<h2>Return Values</h2>
<p>The Fn unvis function has several return codes that must be handled properly. They are:</p>
<dl>
<dt><code>0 (zero)</code></p>
<dd>Another character is necessary; nothing has been recognized yet.</p>
<dt><code>UNVIS_VALID</code></p>
<dd>A valid character has been recognized and is available at the location pointed to by Fa cp .</p>
<dt><code>UNVIS_VALIDPUSH</code></p>
<dd>A valid character has been recognized and is available at the location pointed to by Fa cp ; however, the character currently passed in should be passed in again.</p>
<dt><code>UNVIS_NOCHAR</code></p>
<dd>A valid sequence was detected, but no character was produced. This return code is necessary to indicate a logical break between characters.</p>
<dt><code>UNVIS_SYNBAD</code></p>
<dd>An invalid escape sequence was detected, or the decoder is in an unknown state. The decoder is placed into the starting state.</dl>
<p> When all bytes in the stream have been processed, call Fn unvis one more time with Fa flag set to <code>UNVIS_END</code> to extract any remaining character (the character passed in is ignored). </p>
<p> The Fn strunvis function returns the number of bytes written (not counting the trailing NUL byte) or -1 if an error occurred. </p>
<p> The Fn strnunvis function returns the number of bytes (not counting the trailing NUL byte) that would be needed to fully convert the input string, or -1 if an error occurred.</p>
<h2>Examples</h2>
<p>The following code fragment illustrates a proper use of Fn unvis . </p>
<blockquote>
<pre>int state = 0;
char out;
while ((ch = getchar()) != EOF) {
again:
 switch(unvis(&amp;out, ch, &amp;state, 0)) {
 case 0:
 case UNVIS_NOCHAR:
 break;
 case UNVIS_VALID:
 (void) putchar(out);
 break;
 case UNVIS_VALIDPUSH:
 (void) putchar(out);
 goto again;
 case UNVIS_SYNBAD:
 (void)fprintf(stderr, &quot;bad sequence!
&quot;);
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
 }
}
if (unvis(&amp;out, (char)0, &amp;state, UNVIS_END) == UNVIS_VALID)
 (void) putchar(out);</pre>
</blockquote>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-unvis/">unvis</a>(1), <a href="/docs/linux/man/1-vis/">vis</a>(1), <a href="/docs/linux/man/3-vis/">vis</a>(3)</p>
<h2>History</h2>
<p>The Fn unvis function first appeared in BSD 4.4</p>
