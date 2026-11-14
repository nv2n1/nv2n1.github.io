---
title: "plowdel(1)"
name: "plowdel"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plowdel/"
description: "plowdel – Delete files from file sharing websites links"
---

<h2 class="name">NAME</h2>
<p> plowdel &#8211; Delete files from file sharing websites links</p>
<h2>SYNOPSIS</h2>
<p> <code>plowdel</code> [<i>OPTIONS</i>]&#8230; [<i>MODULE_OPTIONS</i>]&#8230; <i>URL</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>plowdel</code> is a command-line tool designed for deleting files on file-sharing websites. It acts like a web browser, retrieving pages and filling HTML forms. </p>
<p> Currently supported hosting sites list is available in README file. </p>
<p> Some sites may require authentication (login) for deleting files. See specific module options below. Login process may sometimes require captcha solving. </p>
<h2>OPTIONS</h2>
<h3>Common options</h3>
<dl>
<dt><code>-i,</code><i> </i><code>&#8211;interface=</code><i>IFACE</i></p>
<dd> If your machine has several network interfaces, force using <i>IFACE</i> interface.</dl>
<h3>Captcha options</h3>
<dl>
<dt><i> </i><code>&#8211;9kweu=</code><i>KEY</i></p>
<dd> Use 9kw.eu service to solve captchas.</p>
<dt><i> </i><code>&#8211;antigate=</code><i>KEY</i></p>
<dd> Use Antigate.com service to solve captchas.</p>
<dt><i> </i><code>&#8211;captchabhood=</code><i>USER:PASSWORD</i></p>
<dd> Use Captcha Brotherhood service to solve captchas.</p>
<dt><i> </i><code>&#8211;captchacoin=</code><i>KEY</i></p>
<dd> Use CaptchaCoin service to solve captchas.</p>
<dt><i> </i><code>&#8211;deathbycaptcha=</code><i>USER:PASSWORD</i></p>
<dd> Use Death by Captcha service to solve captchas.</p>
<dt><i> </i><code>&#8211;captchamethod=</code><i>METHOD</i></p>
<dd> Force specific captcha solving method. Available values:</p>
<dl>
<dt>
<dd> <code>imgur</code> : upload image to Imgur.com service, print image url in console and prompt for manual entering. Useful for NAS and embedded devices.</dl>
<dl>
<dt>
<dd> <code>none</code> : abort if captcha solving is requested (even if automatic solving service is available).</dl>
<dl>
<dt>
<dd> <code>online</code> : use captcha solving website only (9kweu, Antigate, CaptchaBrotherhood, CaptchaCoin or DeathByCaptcha account required).</dl>
<dl>
<dt>
<dd> <code>fb</code> : display image in framebuffer console and prompt for manual entering. Looks for framebuffer viewers: fbi, fim. <i>FRAMEBUFFER</i> environment variable can contain device file. Default is <i>/dev/fb0</i>.</dl>
<dl>
<dt>
<dd> <code>nox</code> : display image in console (text) and prompt for manual entering. Looks for ascii viewers: img2txt, aview, tiv.</dl>
<dl>
<dt>
<dd> <code>x11</code> : display image in an X11 window and prompt for manual entering. Looks for viewers: display, feh, sxiv, qiv.</dl>
<dt><i> </i><code>&#8211;captchaprogram=</code><i>PROGRAM</i></p>
<dd> Call external program or script for solving captchas. Provided executable can be located in <i>PATH</i> environment variable. </p>
<p> Three arguments are given:</p>
<dl>
<dt>
<dd> <code>$1</code> module name (lowercase). For example: <i>mediafire</i>.</dl>
<dl>
<dt>
<dd> <code>$2</code> image filename (with full path).</dl>
<dl>
<dt>
<dd> <code>$3</code> hint or captcha type (string). For example: <i>recaptcha</i>, <i>solvemedia</i> or <i>digits-4</i>. </p>
<p> Return value (on stdout) and exit status:</dl>
<dl>
<dt>
<dd> <code>0</code> : solving success. Captcha Word(s) must be echo&#8217;ed.</dl>
<dl>
<dt>
<dd> <code>2</code> : external solver is not able to solve requested captcha. Let plowdel continue solving it normally (will consider <code>&#8211;captchamethod</code> if specified).</dl>
<dl>
<dt>
<dd> <code>7</code> : external solver failed. </p>
<p> Note: plowdel legacy exit errors can also be returned, for example: <code>1</code> (fatal) or <code>3</code> (network).</dl>
</dl>
<h3>Logging options</h3>
<dl>
<dt><code>-v,</code><i> </i><code>&#8211;verbose=</code><i>LEVEL</i></p>
<dd> Set output verbosity level:</p>
<dl>
<dt>
<dd> <code>0</code> none,</dl>
<dl>
<dt>
<dd> <code>1</code> errors,</dl>
<dl>
<dt>
<dd> <code>2</code> notice (default behavior),</dl>
<dl>
<dt>
<dd> <code>3</code> debug,</dl>
<dl>
<dt>
<dd> <code>4</code> report (very noisy, log HTML pages).</dl>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Alias for <code>-v0</code>. Do not print any debug messages.</dl>
<h3>Miscellaneous options</h3>
<dl>
<dt><code> &#8211;no-plowsharerc</code></p>
<dd> Do not consider any configuration file.</p>
<dt><i> </i><code>&#8211;plowsharerc=</code><i>FILE</i></p>
<dd> Force using an alternate configuration file (instead of per-user or systemwide plowshare.conf). This option has no effect when <code>&#8211;no-plowsharerc</code> is defined.</p>
<dt><code> &#8211;modules</code></p>
<dd> Display all supported module names (one per line) and exit. Useful for wrappers.</dl>
<h3>Generic program information</h3>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Display main help and exit.</p>
<dt><code>-H, &#8211;longhelp</code></p>
<dd> Display complete help (with module options) and exit.</p>
<dt><code> &#8211;version</code></p>
<dd> Output version information and exit. </p>
</dl>
<h2>MODULE OPTIONS</h2>
<h3>Common options</h3>
<dl>
<dt><code>-a,</code><i> </i><code>&#8211;auth=</code><i>USER:PASSWORD</i></p>
<dd> Use premium account. Free account can be used sometimes.</dl>
<p> All switches are not implemented nor required for all modules. See help message for detailed modules option list. </p>
<h2>EXAMPLES</h2>
<h3>1) Delete one or several files (using delete link)</h3>
<p> $ plowdel <a rel="nofollow" href="http://d01.megashares.com/?dl=6EUeDtS">http://d01.megashares.com/?dl=6EUeDtS</a> </p>
<p> # Deletes are successive (not parallel) $ plowdel <a rel="nofollow" href="http://d01.megashares.com/?dl=6EUeDtS">http://d01.megashares.com/?dl=6EUeDtS</a> \<br />
&nbsp;<wbr><a rel="nofollow" href="http://depositfiles.com/rmv/1643181821669253">http://depositfiles.com/rmv/1643181821669253</a> </p>
<h2>FILES</h2>
<dl>
<dt><i>~/.config/plowshare/plowshare.conf</i></p>
<dd> This is the per-user configuration file.</p>
<dt><i>~/.config/plowshare/exec/</i></p>
<dd> Additional directory considered when searching for executable. See <code>&#8211;captchaprogram</code> switch.</p>
<dt><i>/etc/plowshare.conf</i></p>
<dd> Systemwide configuration file.</dl>
<p> The file format is described in <code><a href="/docs/linux/man/5-plowshare-conf/">plowshare.conf</a></code>(5). </p>
<h2>EXIT CODES</h2>
<p> Possible exit codes are:</p>
<dl>
<dt>0</p>
<dd> Success. File was successfully deleted.</p>
<dt>1</p>
<dd> Fatal error. Upstream site updated or unexpected result.</p>
<dt>2</p>
<dd> No available module (provided URL is not supported).</p>
<dt>3</p>
<dd> Network error. Mostly curl related.</p>
<dt>4</p>
<dd> Authentication failed (bad login/password).</p>
<dt>11</p>
<dd> Link requires an admin or removal code.</p>
<dt>12</p>
<dd> Authentication required (anonymous users can&#8217;t delete files).</p>
<dt>13</p>
<dd> Link is dead. File has been previously deleted.</p>
<dt>15</p>
<dd> Unknown command line parameter or incompatible options.</dl>
<p> If <code>plowdel</code> is invoked with multiple links and one or several errors occur, the first error code is returned added with 100. </p>
<h2>AUTHORS</h2>
<p> Plowshare was initially written by Arnau Sanchez. See the AUTHORS file for a list of some of the many other contributors. </p>
<p> Plowshare is (C) 2010-2014 The Plowshare Team</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-plowdown/">plowdown</a></code>(1), <code><a href="/docs/linux/man/1-plowup/">plowup</a></code>(1), <code><a href="/docs/linux/man/1-plowlist/">plowlist</a></code>(1), <code><a href="/docs/linux/man/1-plowprobe/">plowprobe</a></code>(1), <code><a href="/docs/linux/man/5-plowshare-conf/">plowshare.conf</a></code>(5). </p>
<h2>Index</h2>
