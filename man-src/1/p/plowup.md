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
<dt><code>-i,</code><i> </i><code>&#8211;interface=</code><i>IFACE</i></dt>
<dd> If your machine has several network interfaces, force using <i>IFACE</i> interface.</dd>
<dt><code>-r,</code><i> </i><code>&#8211;max-retries=</code><i>N</i></dt>
<dd> Set maximum retries for upload failures. Apply on module exit value: <code>1</code> (fatal error), <code>3</code> (network error), <code>7</code> (captcha error). Default option value is 0 (no retry) and applies for one single upload.</dd>
<dt><code>-t,</code><i> </i><code>&#8211;timeout=</code><i>SECS</i></dt>
<dd> Cancel upload download after <i>SECS</i> seconds of waits. Apply on module exit value: <code>10</code> (temporary unavailable error). This error mainly occurs on remote upload operations. Default option value is disabled (no timeout, infinite) and applies for one single upload.</dd>
<dt><i> </i><code>&#8211;cache=</code><i>METHOD</i></dt>
<dd> Cache policy regarding module storage space. Each module is able to save data (credentials, authentication session, or tokens) in order to be reused later. Available values:</dd>
<dl>
<dt>
</dt><dd> <code>none</code> : module storage file is deleted before each item processing. Temporary directory is used.</dd></dl>
<dl>
<dt>
</dt><dd> <code>session</code> (default) : module storage file is deleted at the end of plowup execution. Temporary directory is used.</dd></dl>
<dl>
<dt>
</dt><dd> <code>shared</code> : module storage file is global and located (in <i>~/.config/plowshare/storage/</i>). It can be accessed by any other instance of plow* scripts. Warning: There is no atomicity (or file locking) on concurrent access. </dd>
<p> Example: Multiple file upload using a premium account. If supported by module, login stage could be performed once.</dl>
</dl>
<h3>Captcha options</h3>
<dl>
<dt><i> </i><code>&#8211;9kweu=</code><i>KEY</i></dt>
<dd> Use 9kw.eu service to solve captchas.</dd>
<dt><i> </i><code>&#8211;antigate=</code><i>KEY</i></dt>
<dd> Use Antigate.com service to solve captchas.</dd>
<dt><i> </i><code>&#8211;captchabhood=</code><i>USER:PASSWORD</i></dt>
<dd> Use Captcha Brotherhood service to solve captchas.</dd>
<dt><i> </i><code>&#8211;captchacoin=</code><i>KEY</i></dt>
<dd> Use CaptchaCoin service to solve captchas.</dd>
<dt><i> </i><code>&#8211;deathbycaptcha=</code><i>USER:PASSWORD</i></dt>
<dd> Use Death by Captcha service to solve captchas.</dd>
<dt><i> </i><code>&#8211;captchamethod=</code><i>METHOD</i></dt>
<dd> Force specific captcha solving method. Available values:</dd>
<dl>
<dt>
</dt><dd> <code>imgur</code> : upload image to Imgur.com service, print image url in console and prompt for manual entering. Useful for NAS and embedded devices.</dd></dl>
<dl>
<dt>
</dt><dd> <code>none</code> : abort if captcha solving is requested (even if automatic solving service is available).</dd></dl>
<dl>
<dt>
</dt><dd> <code>online</code> : use captcha solving website only (9kweu, Antigate, CaptchaBrotherhood, CaptchaCoin or DeathByCaptcha account required).</dd></dl>
<dl>
<dt>
</dt><dd> <code>fb</code> : display image in framebuffer console and prompt for manual entering. Looks for framebuffer viewers: fbi, fim. <i>FRAMEBUFFER</i> environment variable can contain device file. Default is <i>/dev/fb0</i>.</dd></dl>
<dl>
<dt>
</dt><dd> <code>nox</code> : display image in console (text) and prompt for manual entering. Looks for ascii viewers: img2txt, aview, tiv.</dd></dl>
<dl>
<dt>
</dt><dd> <code>x11</code> : display image in an X11 window and prompt for manual entering. Looks for viewers: display, feh, sxiv, qiv.</dd></dl>
<dt><i> </i><code>&#8211;captchaprogram=</code><i>PROGRAM</i></dt>
<dd> Call external program or script for solving captchas. Provided executable can be located in <i>PATH</i> environment variable. </dd>
<p> Three arguments are given:</p>
<dl>
<dt>
</dt><dd> <code>$1</code> module name (lowercase). For example: <i>mediafire</i>.</dd></dl>
<dl>
<dt>
</dt><dd> <code>$2</code> image filename (with full path).</dd></dl>
<dl>
<dt>
</dt><dd> <code>$3</code> hint or captcha type (string). For example: <i>recaptcha</i>, <i>solvemedia</i> or <i>digits-4</i>. </dd>
<p> Return value (on stdout) and exit status:</dl>
<dl>
<dt>
</dt><dd> <code>0</code> : solving success. Captcha Word(s) must be echo&#8217;ed.</dd></dl>
<dl>
<dt>
</dt><dd> <code>2</code> : external solver is not able to solve requested captcha. Let plowup continue solving it normally (will consider <code>&#8211;captchamethod</code> if specified).</dd></dl>
<dl>
<dt>
</dt><dd> <code>7</code> : external solver failed. Note: this exit code is eligible with retry policy (<code>-r</code>/<code>&#8211;max-retries</code>). </dd>
<p> Note: plowup legacy exit errors can also be returned, for example: <code>1</code> (fatal) or <code>3</code> (network).</dl>
</dl>
<h3>Tuning settings</h3>
<dl>
<dt><i> </i><code>&#8211;max-rate=</code><i>SPEED</i></dt>
<dd> Limit upload maximum speed in bytes per second. Suffixes are:</dd>
<dl>
<dt>
</dt><dd> <code>k</code> for kilobytes (kB i.e. 1000),</dd></dl>
<dl>
<dt>
</dt><dd> <code>M</code> for megabytes (MB i.e. 1000^2),</dd></dl>
<dl>
<dt>
</dt><dd> <code>K</code> or <code>Ki</code> for kibibytes (KB or KiB i.e. 1024),</dd></dl>
<dl>
<dt>
</dt><dd> <code>m</code> or <code>Mi</code> for mebibytes (mB or MiB i.e. 1024^2).</dd></dl>
<dt><i> </i><code>&#8211;min-rate=</code><i>SPEED</i></dt>
<dd> Limit upload minimum speed in bytes per second (for a delay of 30 seconds). Suffixes are the same than <code>&#8211;max-rate</code>.</dd>
<dt><i> </i><code>&#8211;temp-directory=</code><i>DIRECTORY</i></dt>
<dd> Directory for temporary files: cookies, images, &#8230;</dd>
<dt><i> </i><code>&#8211;name=</code><i>FORMAT</i></dt>
<dd> Format destination filename (applies on each file argument). Can be useful is you want to append or prepend a string to all your files. Default string is: <i>&quot;%f&quot;</i>. Interpreted sequences are:</dd>
<dl>
<dl>
<dt><i>%%</i></dt>
<dd> raw % character</dd>
<dt><i>%f</i></dt>
<dd> destination (remote) filename</dd>
<dt><i>%g</i></dt>
<dd> destination (remote) filename (without extension)</dd>
<dt><i>%G</i></dt>
<dd> destination (remote) filename (without extension, greedy)</dd>
<dt><i>%h</i></dt>
<dd> MD5 hash (32-digit hexadecimal number, lowercase letters)</dd>
<dt><i>%l</i></dt>
<dd> source (local) filename</dd>
<dt><i>%m</i></dt>
<dd> module name</dd>
<dt><i>%s</i></dt>
<dd> file size (in bytes)</dd>
<dt><i>%x</i></dt>
<dd> extension (without dot character) of %f (not greedy)</dd></dl>
</dl>
<dt><i> </i><code>&#8211;printf=</code><i>FORMAT</i></dt>
<dd> Print results (on stdout) in a given format (for each successful upload). Default string is: <i>&quot;%D%A%u%n&quot;</i>. Interpreted sequences are:</dd>
<dl>
<dl>
<dt><i>%%</i></dt>
<dd> raw % character</dd>
<dt><i>%a</i></dt>
<dd> admin url or admin code (rare case)</dd>
<dt><i>%A</i></dt>
<dd> empty if %a is empty, or alias to <code>&quot;#ADM %a%n&quot;</code>.</dd>
<dt><i>%d</i></dt>
<dd> delete url</dd>
<dt><i>%D</i></dt>
<dd> empty if %d is empty, or alias to <code>&quot;#DEL %d%n&quot;</code>.</dd>
<dt><i>%f</i></dt>
<dd> destination (remote) filename</dd>
<dt><i>%l</i></dt>
<dd> source (local) filename</dd>
<dt><i>%m</i></dt>
<dd> module name</dd>
<dt><i>%n</i></dt>
<dd> newline</dd>
<dt><i>%s</i></dt>
<dd> filesize (in bytes)</dd>
<dt><i>%t</i></dt>
<dd> tabulation character</dd>
<dt><i>%u</i></dt>
<dd> download url</dd></dl>
</dl>
</dl>
<h3>Logging options</h3>
<dl>
<dt><code>-v,</code><i> </i><code>&#8211;verbose=</code><i>LEVEL</i></dt>
<dd> Set output verbosity level:</dd>
<dl>
<dt>
</dt><dd> <code>0</code> none,</dd></dl>
<dl>
<dt>
</dt><dd> <code>1</code> errors,</dd></dl>
<dl>
<dt>
</dt><dd> <code>2</code> notice (default behavior),</dd></dl>
<dl>
<dt>
</dt><dd> <code>3</code> debug,</dd></dl>
<dl>
<dt>
</dt><dd> <code>4</code> report (very noisy, log HTML pages).</dd></dl>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> Alias for <code>-v0</code>. Do not print any debug messages.</dd></dl>
<h3>Miscellaneous options</h3>
<dl>
<dt><code> &#8211;no-curlrc</code></dt>
<dd> Do not use curl config file (~/.curlrc).</dd>
<dt><code> &#8211;no-plowsharerc</code></dt>
<dd> Do not consider any configuration file.</dd>
<dt><i> </i><code>&#8211;plowsharerc=</code><i>FILE</i></dt>
<dd> Force using an alternate configuration file (instead of per-user or systemwide plowshare.conf). This option has no effect when <code>&#8211;no-plowsharerc</code> is defined.</dd>
<dt><code> &#8211;modules</code></dt>
<dd> Display all supported module names (one per line) and exit. Useful for wrappers.</dd></dl>
<h3>Generic program information</h3>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display main help and exit.</dd>
<dt><code>-H, &#8211;longhelp</code></dt>
<dd> Display complete help (with module options) and exit.</dd>
<dt><code> &#8211;version</code></dt>
<dd> Output version information and exit. </dd>
</dl>
<h2>MODULE OPTIONS</h2>
<h3>Common options</h3>
<dl>
<dt><code>-a,</code><i> </i><code>&#8211;auth=</code><i>USER:PASSWORD</i></dt>
<dd> Use premium account.</dd>
<dt><code>-b,</code><i> </i><code>&#8211;auth-free=</code><i>USER:PASSWORD</i></dt>
<dd> Use free account.</dd>
<dt><code>-d,</code><i> </i><code>&#8211;description=</code><i>DESCRIPTION</i></dt>
<dd> Set file description.</dd>
<dt><i> </i><code>&#8211;folder=</code><i>FOLDER</i></dt>
<dd> Folder to upload files into. Usually a (leaf) folder name (no hierarchy assumed).</dd>
<dt><code>-p,</code><i> </i><code>&#8211;link-password=</code><i>PASSWORD</i></dt>
<dd> Protect your files with a password. May require premium account.</dd>
<dt><i> </i><code>&#8211;email-from=</code><i>EMAIL</i></dt>
<dd> &lt;From&gt; field for notification email.</dd>
<dt><i> </i><code>&#8211;email-to=</code><i>EMAIL</i></dt>
<dd> &lt;To&gt; field for notification email.</dd></dl>
<h3>Advanced options</h3>
<dl>
<dt><code> &#8211;async</code></dt>
<dd> Asynchronous remote upload (only start upload, don&#8217;t wait for link).</dd>
<dt><code> &#8211;private</code></dt>
<dd> Do not allow others to download the file.</dd></dl>
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
<dt><i>/etc/plowshare.conf</i></dt>
<dd> Systemwide configuration file.</dd>
<dt><i>~/.config/plowshare/plowshare.conf</i></dt>
<dd> This is the per-user configuration file.</dd>
<dt><i>~/.config/plowshare/exec/</i></dt>
<dd> Additional directory considered when searching for executable. See <code>&#8211;captchaprogram</code> switch.</dd>
<dt><i>~/.config/plowshare/storage/</i></dt>
<dd> Directory used for storing data (one file per module) among sessions. See <code>&#8211;cache=shared</code> switch.</dd></dl>
<p> The file format is described in <code><a href="/docs/linux/man/5-plowshare-conf/">plowshare.conf</a></code>(5). </p>
<h2>EXIT CODES</h2>
<p> Possible exit codes are:</p>
<dl>
<dt>0</dt>
<dd> Success.</dd>
<dt>1</dt>
<dd> Fatal error. Upstream site updated or unexpected result.</dd>
<dt>2</dt>
<dd> No available module (provided module name does not exist).</dd>
<dt>3</dt>
<dd> Network error. Mostly curl related.</dd>
<dt>4</dt>
<dd> Authentication failed (bad login/password).</dd>
<dt>5</dt>
<dd> Timeout reached (refer to <code>-t</code>/<code>&#8211;timeout</code> command-line option).</dd>
<dt>6</dt>
<dd> Maximum tries reached (refer to <code>-r</code>/<code>&#8211;max-retries</code> command-line option).</dd>
<dt>7</dt>
<dd> Captcha generic error.</dd>
<dt>8</dt>
<dd> System generic error.</dd>
<dt>10</dt>
<dd> Feature (upload service) seems temporarily unavailable from upstream (user account may be temporarily banned).</dd>
<dt>12</dt>
<dd> Authentication required (example: anonymous users can&#8217;t do remote upload).</dd>
<dt>14</dt>
<dd> Can&#8217;t upload too big file (hoster limitation or requires more permissions).</dd>
<dt>15</dt>
<dd> Unknown command line parameter or incompatible options.</dd>
<dt>16</dt>
<dd> Asynchronous remote upload started (can&#8217;t predict final status).</dd></dl>
<p> If <code>plowup</code> is invoked with multiple files and one or several errors occur, the first error code is returned added with 100. </p>
<h2>AUTHORS</h2>
<p> Plowshare was initially written by Arnau Sanchez. See the AUTHORS file for a list of some of the many other contributors. </p>
<p> Plowshare is (C) 2010-2014 The Plowshare Team</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-plowdown/">plowdown</a></code>(1), <code><a href="/docs/linux/man/1-plowdel/">plowdel</a></code>(1), <code><a href="/docs/linux/man/1-plowlist/">plowlist</a></code>(1), <code><a href="/docs/linux/man/1-plowprobe/">plowprobe</a></code>(1), <code><a href="/docs/linux/man/5-plowshare-conf/">plowshare.conf</a></code>(5). </p>
<h2>Index</h2>
