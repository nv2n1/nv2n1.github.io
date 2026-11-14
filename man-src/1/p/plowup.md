---
title: "plowup(1)"
name: "plowup"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plowup/"
description: "plowup – Simple upload manager for file sharing websites"
---

<h2 class="name">NAME</h2>
<p> plowup &#8211; Simple upload manager for file sharing websites</p>
<h2>SYNOPSIS</h2>
<p> <code>plowup</code> [<i>OPTIONS</i>]&#8230; [<i>MODULE_OPTIONS</i>]&#8230; <i>MODULE</i> <i>URL</i>|<i>FILE</i>[<i>:DESTNAME</i>]&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>plowup</code> is a command-line tool designed for automatic upload on file-sharing websites. It acts like a web browser, retrieving pages and filling HTML forms. </p>
<p> Currently supported hosting sites list is available in README file. </p>
<p> Anonymous upload is not allowed by all sites, some of them may require authentication. See specific module options below. </p>
<h2>OPTIONS</h2>
<h3>Common options</h3>
<dl>
<dt><code>-i,</code><i> </i><code>&#8211;interface=</code><i>IFACE</i></p>
<dd> If your machine has several network interfaces, force using <i>IFACE</i> interface.</p>
<dt><code>-r,</code><i> </i><code>&#8211;max-retries=</code><i>N</i></p>
<dd> Set maximum retries for upload failures. Apply on module exit value: <code>1</code> (fatal error), <code>3</code> (network error), <code>7</code> (captcha error). Default option value is 0 (no retry) and applies for one single upload.</p>
<dt><code>-t,</code><i> </i><code>&#8211;timeout=</code><i>SECS</i></p>
<dd> Cancel upload download after <i>SECS</i> seconds of waits. Apply on module exit value: <code>10</code> (temporary unavailable error). This error mainly occurs on remote upload operations. Default option value is disabled (no timeout, infinite) and applies for one single upload.</p>
<dt><i> </i><code>&#8211;cache=</code><i>METHOD</i></p>
<dd> Cache policy regarding module storage space. Each module is able to save data (credentials, authentication session, or tokens) in order to be reused later. Available values:</p>
<dl>
<dt>
<dd> <code>none</code> : module storage file is deleted before each item processing. Temporary directory is used.</dl>
<dl>
<dt>
<dd> <code>session</code> (default) : module storage file is deleted at the end of plowup execution. Temporary directory is used.</dl>
<dl>
<dt>
<dd> <code>shared</code> : module storage file is global and located (in <i>~/.config/plowshare/storage/</i>). It can be accessed by any other instance of plow* scripts. Warning: There is no atomicity (or file locking) on concurrent access. </p>
<p> Example: Multiple file upload using a premium account. If supported by module, login stage could be performed once.</dl>
</dl>
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
<dd> <code>2</code> : external solver is not able to solve requested captcha. Let plowup continue solving it normally (will consider <code>&#8211;captchamethod</code> if specified).</dl>
<dl>
<dt>
<dd> <code>7</code> : external solver failed. Note: this exit code is eligible with retry policy (<code>-r</code>/<code>&#8211;max-retries</code>). </p>
<p> Note: plowup legacy exit errors can also be returned, for example: <code>1</code> (fatal) or <code>3</code> (network).</dl>
</dl>
<h3>Tuning settings</h3>
<dl>
<dt><i> </i><code>&#8211;max-rate=</code><i>SPEED</i></p>
<dd> Limit upload maximum speed in bytes per second. Suffixes are:</p>
<dl>
<dt>
<dd> <code>k</code> for kilobytes (kB i.e. 1000),</dl>
<dl>
<dt>
<dd> <code>M</code> for megabytes (MB i.e. 1000^2),</dl>
<dl>
<dt>
<dd> <code>K</code> or <code>Ki</code> for kibibytes (KB or KiB i.e. 1024),</dl>
<dl>
<dt>
<dd> <code>m</code> or <code>Mi</code> for mebibytes (mB or MiB i.e. 1024^2).</dl>
<dt><i> </i><code>&#8211;min-rate=</code><i>SPEED</i></p>
<dd> Limit upload minimum speed in bytes per second (for a delay of 30 seconds). Suffixes are the same than <code>&#8211;max-rate</code>.</p>
<dt><i> </i><code>&#8211;temp-directory=</code><i>DIRECTORY</i></p>
<dd> Directory for temporary files: cookies, images, &#8230;</p>
<dt><i> </i><code>&#8211;name=</code><i>FORMAT</i></p>
<dd> Format destination filename (applies on each file argument). Can be useful is you want to append or prepend a string to all your files. Default string is: <i>&quot;%f&quot;</i>. Interpreted sequences are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>%%</i></p>
<dd> raw % character</p>
<dt><i>%f</i></p>
<dd> destination (remote) filename</p>
<dt><i>%g</i></p>
<dd> destination (remote) filename (without extension)</p>
<dt><i>%G</i></p>
<dd> destination (remote) filename (without extension, greedy)</p>
<dt><i>%h</i></p>
<dd> MD5 hash (32-digit hexadecimal number, lowercase letters)</p>
<dt><i>%l</i></p>
<dd> source (local) filename</p>
<dt><i>%m</i></p>
<dd> module name</p>
<dt><i>%s</i></p>
<dd> file size (in bytes)</p>
<dt><i>%x</i></p>
<dd> extension (without dot character) of %f (not greedy)</dl>
</dl>
<dt><i> </i><code>&#8211;printf=</code><i>FORMAT</i></p>
<dd> Print results (on stdout) in a given format (for each successful upload). Default string is: <i>&quot;%D%A%u%n&quot;</i>. Interpreted sequences are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>%%</i></p>
<dd> raw % character</p>
<dt><i>%a</i></p>
<dd> admin url or admin code (rare case)</p>
<dt><i>%A</i></p>
<dd> empty if %a is empty, or alias to <code>&quot;#ADM %a%n&quot;</code>.</p>
<dt><i>%d</i></p>
<dd> delete url</p>
<dt><i>%D</i></p>
<dd> empty if %d is empty, or alias to <code>&quot;#DEL %d%n&quot;</code>.</p>
<dt><i>%f</i></p>
<dd> destination (remote) filename</p>
<dt><i>%l</i></p>
<dd> source (local) filename</p>
<dt><i>%m</i></p>
<dd> module name</p>
<dt><i>%n</i></p>
<dd> newline</p>
<dt><i>%s</i></p>
<dd> filesize (in bytes)</p>
<dt><i>%t</i></p>
<dd> tabulation character</p>
<dt><i>%u</i></p>
<dd> download url</dl>
</dl>
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
<dt><code> &#8211;no-curlrc</code></p>
<dd> Do not use curl config file (~/.curlrc).</p>
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
<dd> Use premium account.</p>
<dt><code>-b,</code><i> </i><code>&#8211;auth-free=</code><i>USER:PASSWORD</i></p>
<dd> Use free account.</p>
<dt><code>-d,</code><i> </i><code>&#8211;description=</code><i>DESCRIPTION</i></p>
<dd> Set file description.</p>
<dt><i> </i><code>&#8211;folder=</code><i>FOLDER</i></p>
<dd> Folder to upload files into. Usually a (leaf) folder name (no hierarchy assumed).</p>
<dt><code>-p,</code><i> </i><code>&#8211;link-password=</code><i>PASSWORD</i></p>
<dd> Protect your files with a password. May require premium account.</p>
<dt><i> </i><code>&#8211;email-from=</code><i>EMAIL</i></p>
<dd> &lt;From&gt; field for notification email.</p>
<dt><i> </i><code>&#8211;email-to=</code><i>EMAIL</i></p>
<dd> &lt;To&gt; field for notification email.</dl>
<h3>Advanced options</h3>
<dl>
<dt><code> &#8211;async</code></p>
<dd> Asynchronous remote upload (only start upload, don&#8217;t wait for link).</p>
<dt><code> &#8211;private</code></p>
<dd> Do not allow others to download the file.</dl>
<p> All switches are not implemented nor required for all modules. See long help message for detailed modules option list. </p>
<h2>EXAMPLES</h2>
<h3>1) Upload a single file anonymously</h3>
<p> $ plowup bayfiles /tmp/foo.bar </p>
<p> # Add a text description $ plowup -d &quot;Important document&quot; megashares /path/myfile.tex </p>
<p> # Abort slow upload (if rate is below limit during 30 seconds) $ plowup &#8211;min-rate 100k mediafire /path/bigfile.zip</p>
<h3>2) Upload a single file with authentication</h3>
<p> # Change destination filename $ plowup -a &#8216;myuser:mypassword&#8217; turbobit /path/myfile.txt:anothername.txt</p>
<h3>3) Remote upload</h3>
<p> Note: URL fetching is rarely implemented by modules. </p>
<p> # Feature dedicated to premium members $ plowup -a myuser:mypassword rapidgator \<br />
&nbsp;<wbr><a rel="nofollow" href="http://www.somewherefarbeyond.com/somefile">http://www.somewherefarbeyond.com/somefile</a> </p>
<p> # Change destination filename $ plowup -a myuser:mypassword rapidgator \<br />
&nbsp;<wbr><a rel="nofollow" href="http://www.somewherefarbeyond.com/somefile:anothername">http://www.somewherefarbeyond.com/somefile:anothername</a> </p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/plowshare.conf</i></p>
<dd> Systemwide configuration file.</p>
<dt><i>~/.config/plowshare/plowshare.conf</i></p>
<dd> This is the per-user configuration file.</p>
<dt><i>~/.config/plowshare/exec/</i></p>
<dd> Additional directory considered when searching for executable. See <code>&#8211;captchaprogram</code> switch.</p>
<dt><i>~/.config/plowshare/storage/</i></p>
<dd> Directory used for storing data (one file per module) among sessions. See <code>&#8211;cache=shared</code> switch.</dl>
<p> The file format is described in <code><a href="/docs/linux/man/5-plowshare-conf/">plowshare.conf</a></code>(5). </p>
<h2>EXIT CODES</h2>
<p> Possible exit codes are:</p>
<dl>
<dt>0</p>
<dd> Success.</p>
<dt>1</p>
<dd> Fatal error. Upstream site updated or unexpected result.</p>
<dt>2</p>
<dd> No available module (provided module name does not exist).</p>
<dt>3</p>
<dd> Network error. Mostly curl related.</p>
<dt>4</p>
<dd> Authentication failed (bad login/password).</p>
<dt>5</p>
<dd> Timeout reached (refer to <code>-t</code>/<code>&#8211;timeout</code> command-line option).</p>
<dt>6</p>
<dd> Maximum tries reached (refer to <code>-r</code>/<code>&#8211;max-retries</code> command-line option).</p>
<dt>7</p>
<dd> Captcha generic error.</p>
<dt>8</p>
<dd> System generic error.</p>
<dt>10</p>
<dd> Feature (upload service) seems temporarily unavailable from upstream (user account may be temporarily banned).</p>
<dt>12</p>
<dd> Authentication required (example: anonymous users can&#8217;t do remote upload).</p>
<dt>14</p>
<dd> Can&#8217;t upload too big file (hoster limitation or requires more permissions).</p>
<dt>15</p>
<dd> Unknown command line parameter or incompatible options.</p>
<dt>16</p>
<dd> Asynchronous remote upload started (can&#8217;t predict final status).</dl>
<p> If <code>plowup</code> is invoked with multiple files and one or several errors occur, the first error code is returned added with 100. </p>
<h2>AUTHORS</h2>
<p> Plowshare was initially written by Arnau Sanchez. See the AUTHORS file for a list of some of the many other contributors. </p>
<p> Plowshare is (C) 2010-2014 The Plowshare Team</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-plowdown/">plowdown</a></code>(1), <code><a href="/docs/linux/man/1-plowdel/">plowdel</a></code>(1), <code><a href="/docs/linux/man/1-plowlist/">plowlist</a></code>(1), <code><a href="/docs/linux/man/1-plowprobe/">plowprobe</a></code>(1), <code><a href="/docs/linux/man/5-plowshare-conf/">plowshare.conf</a></code>(5). </p>
<h2>Index</h2>
