---

title: "otp(1)"
name: "otp"
section: "1"
letter: "o"
url: "/docs/linux/man/1-otp/"
description: "otp – manages one-time passwords"
---

<p> <code>otp</code> &#8211; manages one-time passwords </p>
<p> <code>otp</code> [-<code>dhlor</code> ] [-<code>f </code><i>algorithm</i> ] [-<code>u </code><i>user</i> ] <i>sequence-number</i> <i>seed</i></p>
<p> The <code>otp</code> program initializes and updates your current series of one-time passwords (OTPs). </p>
<p> Use this to set a new series of one-time passwords. Only perform this on the console or over an encrypted link as you will have to supply your pass-phrase. The other two parameters are <i>sequence-number</i> and <i>seed</i> </p>
<p> Options are:</p>
<dl>
<dt><code>-d</code></dt>
<dd> To delete a one-time password.</dd>
<dt><code>-f</code></dt>
<dd> Choose a different <i>algorithm</i> from the default md5. Pick any of: md4, md5, and sha.</dd>
<dt><code>-h</code></dt>
<dd> For getting a help message.</dd>
<dt><code>-l</code></dt>
<dd> List the current table of one-time passwords.</dd>
<dt><code>-o</code></dt>
<dd> To open (unlock) the otp-entry for a user.</dd>
<dt><code>-r</code></dt>
<dd> To renew a one-time password series. This operation can be performed over an potentially eavesdropped link because you do not supply the pass-phrase. First you need to supply the current one-time password and then the new one corresponding to the supplied <i>sequence-number</i> and <i>seed</i></dd>
<dt><code>-u</code></dt>
<dd> To choose a different <i>user</i> to set one-time passwords for. This only works when running <code>otp</code> as root.</dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-otpprint/">otpprint</a>(1) </p>
