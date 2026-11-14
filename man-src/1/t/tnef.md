---
title: "tnef(1)"
name: "tnef"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tnef/"
description: "tnef - decode Microsoft's Transport Neutral Encapsulation Format SYNOPSIS tnef [options] [FILE]"
---

<h2>NAME</h2>
<pre>
tnef - decode Microsoft's Transport Neutral Encapsulation Format
</pre>
<h2>SYNOPSIS</h2>
<p> <code>tnef</code> [options] [FILE] </p>
<p> <code>tnef</code> {<code>&#8211;help</code> | <code>&#8211;version</code>}</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents the <code>tnef</code> filter. <code>tnef</code> decodes e-mail attachments encoded in Microsoft&#8217;s Transport Neutral Encapsulation Format (hereafter, TNEF), which &quot;wraps&quot; Microsoft e-mail attachments. </p>
<p> Unfortunately, these &quot;wrapped&quot; attachments are inaccessible to any e-mail client that does not understand TNEF. Fortunately, the <code>tnef</code> filter can be used by any MIME-aware client to unpack these attachments.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code> FILE, <code>&#8211;file</code>=FILE</p>
<dd> use FILE as input (&#8216;-&#8216; denotes stdin). When this option is omitted, <code>tnef</code> reads data from stdin.</p>
<dt><code>-C</code> DIR, &#8212;<code>directory</code>=DIR</p>
<dd> unpack file attachments into DIR.</p>
<dt><code>-x SIZE, &#8211;maxsize=SIZE</code></p>
<dd> limit maximum size of extracted archive (bytes)</p>
<dt><code>-t, &#8211;list</code></p>
<dd> list attached files, do not extract.</p>
<dt><code>-w, &#8211;interactive, &#8211;confirmation</code></p>
<dd> ask for confirmation for every action.</p>
<dt><code>&#8211;overwrite</code></p>
<dd> when extracting attachments, overwrite existing files.</p>
<dt><code>&#8211;number-backups</code></p>
<dd> when extracting attachments, if file FOO will be overwritten, create FOO.n instead.</p>
<dt><code>&#8211;use-paths</code></p>
<dd> honor file pathnames specified in the TNEF attachment. For security reasons, paths to attached files are ignored by default.</p>
<dt><code>&#8211;save-body FILE</code></p>
<dd> Save message body data found in the TNEF data. There can be up to three message bodies in the file, plain text, HTML encoded, and RTF encoded. Which are saved is specified by the &#8211;body-pref option. By default the message bodies are written to a file named message with an extension based upon the type (txt, html, rtf).</p>
<dt><code>&#8211;body-pref PREF</code></p>
<dd> Specifies which of the possibly three message body formats will be saved. PREF can be up to three characters long and each character must be one of &#8216;r&#8217;, &#8216;h&#8217;, or &#8216;t&#8217; specifying RTF, HTML or text. The order is the order that the data will be checked, the first type found will be saved. If PREF is the special value of &#8216;all&#8217; then any and all message body data found will be saved. The default is &#8216;rht&#8217;.</p>
<dt><code>&#8211;save-rtf FILE</code></p>
<dd> DEPRECATED. Equivalent to &#8211;save-body=FILE &#8211;body-pref=r</p>
<dt><code>-h, &#8211;help</code></p>
<dd> show usage message.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> display version and copyright.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> produce verbose output.</p>
<dt><code>&#8211;debug</code></p>
<dd> enable debug output.</dl>
<h2>EXAMPLE</h2>
<p> The following example demonstrates typical <code>tnef</code> usage with a popular Unix mail client called &quot;mutt&quot;.</p>
<h3>Step 1 &#8212; Configure ~/.mailcap</h3>
<p> Mutt can&#8217;t use <code>tnef</code> for its intended purpose until an appropriate content type definition exists in ~/.mailcap . Here&#8217;s a sample definition: </p>
<dl>
<dt>
<dd> application/ms-tnef; tnef -w %s</dl>
<p> This mailcap entry says that whenever the MIME content type: </p>
<dl>
<dt>
<dd> application/ms-tnef</dl>
<p> is encountered, use this command to decode it: </p>
<dl>
<dt>
<dd> tnef -w %s</dl>
<p> The latter command string invokes <code>tnef</code>, specifying both the <code>-w</code> option and the attachment (created as a temporary file) as command line arguments.</p>
<h3>Step 2 &#8212; Add The Filter To $PATH</h3>
<p> Mutt can&#8217;t invoke <code>tnef</code> if the filter isn&#8217;t accessible via $PATH.</p>
<h3>Step 3 &#8212; Test Mutt</h3>
<p> Use mutt to read a message that includes a TNEF attachment. Mutt will note that an attachment of type &quot;application/ms-tnef is unsupported&quot;. </p>
<p> Press the &quot;v&quot; key to open mutt&#8217;s &quot;view attachment&quot; menu. </p>
<p> Move the cursor over the TNEF attachment and press the enter key to &quot;view&quot; the attachment. Mutt will launch <code>tnef</code> and invoke it using the command line syntax specified in ~/.mailcap (step 1). <code>tnef</code> then decodes all file(s) included in the TNEF attachment, prompting for confirmation prior to creating an individual file (refer to <code>-w</code> option above). <code>-w</code> is useful here because it gives the end user a chance to view the filename(s) included in the mail message. </p>
<p> Note that Mutt&#8217;s attachment menu also supports a pipe option, which permits the user to pipe attachments to an external filter (how convenient). So, to list the contents of a TNEF attachment prior to decoding it, press the &quot;|&quot; key and enter this command: </p>
<dl>
<dt>
<dd> tnef -t</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-metamail/">metamail</a></code>(1), <code><a href="/docs/linux/man/4-mailcap/">mailcap</a></code>(4), <code><a href="/docs/linux/man/1-mutt/">mutt</a></code>(1), other email clients.</p>
<h2>AUTHOR</h2>
<p> Mark Simpson.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to Mark Simpson &lt;verdammelt [at] gmail.com&gt;</p>
<h2>OTHER REFERENCES</h2>
<p> This web page: </p>
<pre>
<a rel="nofollow" href="http://support.microsoft.com/support/kb/articles/Q136/2/04.asp">http://support.microsoft.com/support/kb/articles/Q136/2/04.asp</a>
</pre>
<p> describes how to configure Microsoft email clients so that the TNEF format is disabled when sending messages to non-TNEF-compatible clients. </p>
<h2>Index</h2>
