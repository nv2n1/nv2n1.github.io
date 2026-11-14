---
title: "otp(1)"
name: "otp"
section: "1"
letter: "o"
url: "/docs/linux/man/1-otp/"
description: "otp – manages one-time passwords"
---

<h2 class="name">NAME</h2>
<p> <code>otp</code> &#8211; manages one-time passwords </p>
<h2>SYNOPSIS</h2>
<p> <code>otp</code> [-<code>dhlor</code> ] [-<code>f </code><i>algorithm</i> ] [-<code>u </code><i>user</i> ] <i>sequence-number</i> <i>seed</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>otp</code> program initializes and updates your current series of one-time passwords (OTPs). </p>
<p> Use this to set a new series of one-time passwords. Only perform this on the console or over an encrypted link as you will have to supply your pass-phrase. The other two parameters are <i>sequence-number</i> and <i>seed</i> </p>
<p> Options are:</p>
<dl>
<dt><code>-d</code></p>
<dd> To delete a one-time password.</p>
<dt><code>-f</code></p>
<dd> Choose a different <i>algorithm</i> from the default md5. Pick any of: md4, md5, and sha.</p>
<dt><code>-h</code></p>
<dd> For getting a help message.</p>
<dt><code>-l</code></p>
<dd> List the current table of one-time passwords.</p>
<dt><code>-o</code></p>
<dd> To open (unlock) the otp-entry for a user.</p>
<dt><code>-r</code></p>
<dd> To renew a one-time password series. This operation can be performed over an potentially eavesdropped link because you do not supply the pass-phrase. First you need to supply the current one-time password and then the new one corresponding to the supplied <i>sequence-number</i> and <i>seed</i></p>
<dt><code>-u</code></p>
<dd> To choose a different <i>user</i> to set one-time passwords for. This only works when running <code>otp</code> as root.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-otpprint/">otpprint</a>(1) </p>
<h2>Index</h2>
