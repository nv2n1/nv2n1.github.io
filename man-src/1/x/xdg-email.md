---

title: "xdg-email(1)"
name: "xdg-email"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xdg-email/"
description: "xdg-email – command line tool for sending mail using the user’s preferred e-mail composer"
---

<p> xdg-email &#8211; command line tool for sending mail using the user&#8217;s preferred e-mail composer </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xdg-email</code> [<code>&#8211;utf8</code>] [<code>&#8211;cc</code>&nbsp;<i>address</i>] [<code>&#8211;bcc</code>&nbsp;<i>address</i>] [<code>&#8211;subject</code>&nbsp;<i>text</i>] [<code>&#8211;body</code>&nbsp;<i>text</i>] [<code>&#8211;attach</code>&nbsp;<i>file</i>] [<i>mailto-uri</i> | <i>address(es)</i>]</dt>
<dt> <code>xdg-email</code> {<code>&#8211;help</code> | <code>&#8211;manual</code> | <code>&#8211;version</code>}</dt></dl>
<h2>DESCRIPTION</h2>
<dd>xdg-email opens the user&#8217;s preferred e-mail composer in order to send a mail to <i>address(es)</i> or <i>mailto-uri</i>. RFC2368 defines mailto: URIs. xdg-email limits support to, cc, subject and body fields in <i>mailto-uri</i>, all other fields are silently ignored. <i>address(es)</i> must follow the syntax of RFC822. Multiple addresses may be provided as separate arguments. </dd>
<p> All information provided on the command line is used to prefill corresponding fields in the user&#8217;s e-mail composer. The user will have the opportunity to change any of this information before actually sending the e-mail. </p>
<p> xdg-email is for use inside a desktop session only. It is not recommended to use xdg-email as root.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;utf8</code></p>
<dl>
<dt>
</dt><dd> Indicates that all command line options that follow are in utf8. Without this option, command line options are expected to be encoded according to locale. If the locale already specifies utf8 this option has no effect. This option does not affect mailto URIs that are passed on the command line.</dd></dl>
<p> <code>&#8211;cc</code> <i>address</i></p>
<dl>
<dt>
</dt><dd> Specify a recipient to be copied on the e-mail.</dd></dl>
<p> <code>&#8211;bcc</code> <i>address</i></p>
<dl>
<dt>
</dt><dd> Specify a recipient to be blindly copied on the e-mail.</dd></dl>
<p> <code>&#8211;subject</code> <i>text</i></p>
<dl>
<dt>
</dt><dd> Specify a subject for the e-mail.</dd></dl>
<p> <code>&#8211;body</code> <i>text</i></p>
<dl>
<dt>
</dt><dd> Specify a body for the e-mail. Since the user will be able to make changes before actually sending the e-mail, this can be used to provide the user with a template for the e-mail. <i>text</i> may contain linebreaks.</dd></dl>
<p> <code>&#8211;attach</code> <i>file</i></p>
<dl>
<dt>
</dt><dd> Specify an attachment for the e-mail. <i>file</i> must point to an existing file. </dd>
<p> Some e-mail applications require the file to remain present after xdg-email returns.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
</dt><dd> Show command synopsis.</dd></dl>
<p> <code>&#8211;manual</code></p>
<dl>
<dt>
</dt><dd> Show this manual page.</dd></dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
</dt><dd> Show the xdg-utils version information.</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> xdg-email honours the following environment variables: </p>
<p> XDG_UTILS_DEBUG_LEVEL</p>
<dl>
<dt>
</dt><dd> Setting this environment variable to a non-zero numerical value makes xdg-email do more verbose reporting on stderr. Setting a higher value increases the verbosity.</dd></dl>
<h2>EXIT CODES</h2>
<p> An exit code of 0 indicates success while a non-zero exit code indicates failure. The following failure codes can be returned: </p>
<p> <code>1</code></p>
<dl>
<dt>
</dt><dd> Error in command line syntax.</dd></dl>
<p> <code>2</code></p>
<dl>
<dt>
</dt><dd> One of the files passed on the command line did not exist.</dd></dl>
<p> <code>3</code></p>
<dl>
<dt>
</dt><dd> A required tool could not be found.</dd></dl>
<p> <code>4</code></p>
<dl>
<dt>
</dt><dd> The action failed.</dd></dl>
<p> <code>5</code></p>
<dl>
<dt>
</dt><dd> No permission to read one of the files passed on the command line.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-xdg-open/">xdg-open</a></code>(1), <code><a href="/docs/linux/man/1-xdg-mime/">xdg-mime</a></code>(1), m[blue]<code>MIME applications associations specification</code>m[][1], m[blue]<code>RFC 6068 &#8211; The &#8216;mailto&#8217; URI Scheme</code>m[][2]</p>
<h2>EXAMPLES</h2>
<dl>
<dt>
</dt><dd>
<pre>
xdg-email 'Jeremy White &lt;jwhite [at] example.com&gt;'
</pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre><code>
xdg - email-- attach / tmp / logo.png-- subject 'Logo contest' --body 'Attached you find the logo for the contest.' 'jwhite [at] example.com'
</code></pre>
</dd></dl>
<dl>
<dt>
</dt><dd>
<pre><code>
xdg - email-- subject 'Your password is about to expire' 'jwhite [at] example.com' 'bastian [at] example.com' 'whipple [at] example.com'
</code></pre>
</dd></dl>
<h2>AUTHORS</h2>
<p> <code>Kevin Krammer</code></p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<p> <code>Jeremy White</code></p>
<dl>
<dt>
</dt><dd> Author.</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2006 </p>
<h2>NOTES</h2>
<dl>
<dt> 1.</dt>
<dd> MIME applications associations specification</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="http://www.freedesktop.org/wiki/Specifications/mime-apps-spec/">http://www.freedesktop.org/wiki/Specifications/mime-apps-spec/</a></dd></dl>
<dt> 2.</dt>
<dd> RFC 6068 &#8211; The &#8216;mailto&#8217; URI Scheme</dd>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="https://tools.ietf.org/html/rfc6068">https://tools.ietf.org/html/rfc6068</a></dd></dl>
</dl>
