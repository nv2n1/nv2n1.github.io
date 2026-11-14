---
title: "plowdown(1)"
name: "plowdown"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plowdown/"
description: "plowdown – Simple download manager for file sharing websites"
---

<h2 class="name">NAME</h2>
<p> plowdown &#8211; Simple download manager for file sharing websites</p>
<h2>SYNOPSIS</h2>
<p> <code>plowdown</code> [<i>OPTIONS</i>]&#8230; [<i>MODULE_OPTIONS</i>]&#8230; <i>URL</i>|<i>FILE</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>plowdown</code> is a command-line tool designed for automatic download on file-sharing websites. It acts like a web browser, retrieving pages and filling HTML forms (including captchas). </p>
<p> Currently supported hosting sites list is available in README file. </p>
<h2>OPTIONS</h2>
<h3>Common options</h3>
<dl>
<dt><code>-i,</code><i> </i><code>&#8211;interface=</code><i>IFACE</i></p>
<dd> If your machine has several network interfaces, force using <i>IFACE</i> interface.</p>
<dt><code>-m, &#8211;mark-downloaded</code></p>
<dd> Mark downloaded links in (regular) file arguments.</p>
<dt><code>-o,</code><i> </i><code>&#8211;output-directory=</code><i>DIRECTORY</i></p>
<dd> Directory where files will be saved. Default is current directory.</p>
<dt><code>-r,</code><i> </i><code>&#8211;max-retries=</code><i>N</i></p>
<dd> Set maximum retries for download failures. Apply on module exit status: <code>3</code> (network error), <code>7</code> (captcha error). Default option value is 2 (i.e. 3 tries) and applies for one single URL download.</p>
<dt><code>-t,</code><i> </i><code>&#8211;timeout=</code><i>SECS</i></p>
<dd> Cancel download after <i>SECS</i> seconds of waits. Apply on module exit status: <code>10</code> (temporary unavailable error). This error can be returned in various cases: unallowed parallel download, daily downloads limit reached, remote hoster overloaded. Default option value is disabled (no timeout, infinite) and applies for one single URL download.</p>
<dt><code>-x, &#8211;no-overwrite</code></p>
<dd> Do not overwrite existing files. Existing file will be preserved and filename will be suffixed with .1, .2, and so on.</p>
<dt><i> </i><code>&#8211;cache=</code><i>METHOD</i></p>
<dd> Cache policy regarding module storage space. Each module is able to save data (credentials, authentication session, or tokens) in order to be reused later. Available values:</p>
<dl>
<dt>
<dd> <code>none</code> : module storage file is deleted before each URL processing. Temporary directory is used.</dl>
<dl>
<dt>
<dd> <code>session</code> (default) : module storage file is deleted at the end of plowdown execution. Temporary directory is used.</dl>
<dl>
<dt>
<dd> <code>shared</code> : module storage file is global and located (in <i>~/.config/plowshare/storage/</i>). It can be accessed by any other instance of plow* scripts. Warning: There is no atomicity (or file locking) on concurrent access. </p>
<p> Example: Multiple links download using a premium account. If supported by module, login stage could be performed once.</dl>
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
<dd> <code>2</code> : external solver is not able to solve requested captcha. Let plowdown continue solving it normally (will consider <code>&#8211;captchamethod</code> if specified).</dl>
<dl>
<dt>
<dd> <code>7</code> : external solver failed. Note: this exit code is eligible with retry policy (<code>-r</code>/<code>&#8211;max-retries</code>). </p>
<p> Note: plowdown legacy exit errors can also be returned, for example: <code>1</code> (fatal) or <code>3</code> (network).</dl>
</dl>
<h3>Tuning settings</h3>
<dl>
<dt><i> </i><code>&#8211;min-space=</code><i>LIMIT</i></p>
<dd> Define threshold amount of available disk space before quitting plowdown. You must specify a suffix. Suffixes are:</p>
<dl>
<dt>
<dd> <code>M</code> for megabytes (MB i.e. 1000^2),</dl>
<dl>
<dt>
<dd> <code>G</code> for gigabytes (GB i.e. 1000^3),</dl>
<dl>
<dt>
<dd> <code>Mi</code> or <code>m</code> for mebibytes (MiB i.e. 1024^2),</dl>
<dl>
<dt>
<dd> <code>Gi</code> for gibibytes (GiB i.e. 1024^3).</dl>
<dt><i> </i><code>&#8211;max-rate=</code><i>SPEED</i></p>
<dd> Limit download speed in bytes per second. Suffixes are:</p>
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
<dt><i> </i><code>&#8211;temp-directory=</code><i>DIRECTORY</i></p>
<dd> Directory for temporary files: final link download, cookies, images, &#8230;</p>
<dt><code> &#8211;temp-rename</code></p>
<dd> Append .part suffix to filename while file is being downloaded. Download resume will not work with this option.</p>
<dt><code> &#8211;skip-final</code></p>
<dd> Don&#8217;t process final link (returned by module download function), just skip it. This is applied for each input URL. If you are using this option, you should need <code>&#8211;run-after</code> or <code>&#8211;printf</code> too.</p>
<dt><i> </i><code>&#8211;run-before=</code><i>PROGRAM</i></p>
<dd> Call external program or script before new link processing. Provided executable can be located in <i>PATH</i> environment variable. Messages can be sent to stderr, stdout is trashed. </p>
<p> Three arguments are given:</p>
<dl>
<dt>
<dd> <code>$1</code> module name (lowercase). For example: <i>mediafire</i>.</dl>
<dl>
<dt>
<dd> <code>$2</code> download URL.</dl>
<dl>
<dt>
<dd> <code>$3</code> cookie (empty) file given to download module function. </p>
<p> Exit status:</dl>
<dl>
<dt>
<dd> <code>0</code> : script success. Plowdown continue normally.</dl>
<dl>
<dt>
<dd> <code>2</code> : script explicitily requests skipping current link. </p>
<p> Note: Any other script exit status like <code>1</code> (fatal) or <code>3</code> (network) will be ignored (an error message will be reported).</dl>
<dt><i> </i><code>&#8211;run-after=</code><i>PROGRAM</i></p>
<dd> Call external program or script after final link successful download. Provided executable can be located in <i>PATH</i> environment variable. Messages can be sent to stderr, stdout is trashed. </p>
<p> Five arguments are given:</p>
<dl>
<dt>
<dd> <code>$1</code> module name (lowercase). For example: <i>mediafire</i>.</dl>
<dl>
<dt>
<dd> <code>$2</code> download URL.</dl>
<dl>
<dt>
<dd> <code>$3</code> cookie file fulfilled by download module function.</dl>
<dl>
<dt>
<dd> <code>$4</code> final URL.</dl>
<dl>
<dt>
<dd> <code>$5</code> final filename. </p>
<p> Exit status:</dl>
<dl>
<dt>
<dd> <code>0</code> : script success. Plowdown continue normally. </p>
<p> Note: Any other (non zero) exit status will be ignored (an error message will be reported).</dl>
<dt><i> </i><code>&#8211;printf=</code><i>FORMAT</i></p>
<dd> Print results (on stdout) in a given format (for each successful download). Default string is: <i>&quot;%F%n&quot;</i>. Interpreted sequences are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>%%</i></p>
<dd> raw % character</p>
<dt><i>%c</i></p>
<dd> final cookie filename (with output directory if specified). Name template is <i>plowdown-cookies-NNNN.txt</i>.</p>
<dt><i>%C</i></p>
<dd> %c or empty string if module does not require it</p>
<dt><i>%d</i></p>
<dd> download (final) url</p>
<dt><i>%f</i></p>
<dd> destination (local) filename</p>
<dt><i>%F</i></p>
<dd> destination (local) filename (with output directory if specified)</p>
<dt><i>%m</i></p>
<dd> module name</p>
<dt><i>%n</i></p>
<dd> newline</p>
<dt><i>%s</i></p>
<dd> destination (local) file size (in bytes). Important: empty string is returned when <code>&#8211;skip-final</code> switch is specified.</p>
<dt><i>%t</i></p>
<dd> tabulation character</p>
<dt><i>%u</i></p>
<dd> download (source) url</dl>
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
<dt><code> &#8211;fallback</code></p>
<dd> If no module is found for link, simply download it (HTTP GET).</p>
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
<dt><code>-p,</code><i> </i><code>&#8211;link-password=</code><i>PASSWORD</i></p>
<dd> Used for password-protected files.</dl>
<p> All switches are not implemented nor required for all modules. See long help message for detailed modules option list. </p>
<h2>NOTES</h2>
<h3>Command line authentication string format</h3>
<p> Complete login must have <i>USER:PASSWORD</i> format. The first semi-colon character is the separator. So, <i>PASSWORD</i> can contain a semi-colon character without any trouble.</p>
<dl>
<dt>Don&#8217;t forget to single-quote string if your password contain shell expandable characters (like space, $ or &amp;).</p>
<dd>
</dl>
<h2>EXAMPLES</h2>
<h3>1) Download one or several files</h3>
<p> $ plowdown <a rel="nofollow" href="http://www.rapidshare.com/files/12345678/foo.rar">http://www.rapidshare.com/files/12345678/foo.rar</a> </p>
<p> # Downloads are successive (not parallel) $ plowdown <a rel="nofollow" href="http://depositfiles.com/files/fv2u9xqya">http://depositfiles.com/files/fv2u9xqya</a> \<br />
&nbsp;<wbr><a rel="nofollow" href="http://rapidgator.net/file/49b1b874">http://rapidgator.net/file/49b1b874</a> </p>
<p> # Download a password-protected file from mediafire $ plowdown -p somepassword <a rel="nofollow" href="http://www.mediafire.com/?mt0egmhietj60iy">http://www.mediafire.com/?mt0egmhietj60iy</a> </p>
<p> # Download using an account (free or premium, not supported by all modules) $ plowdown -a &#8216;myuser:mypassword&#8217; <a rel="nofollow" href="http://rapidgator.net/file/49b1b874">http://rapidgator.net/file/49b1b874</a></p>
<h3>2) Download a list of links (one link per line) commenting out (with #) those successfully downloaded</h3>
<p> $ plowdown -m file_with_links.txt</p>
<h3>3) Download with restrictions</h3>
<p> $ plowdown &#8211;max-rate 900K -i eth1 <a rel="nofollow" href="http://depositfiles.com/files/fv2u9xqya">http://depositfiles.com/files/fv2u9xqya</a></p>
<h3>4) Download with a proxy (3128 is the default port)</h3>
<p> $ export http_proxy=<a rel="nofollow" href="http://192.168.0.20:80">http://192.168.0.20:80</a> $ plowdown <a rel="nofollow" href="http://www.rapidshare.com/files/12345678/foo.rar">http://www.rapidshare.com/files/12345678/foo.rar</a></p>
<h3>5) Don&#8217;t download file but only display final download URL (alternative HTTP retriever can be used).</h3>
<p> # Depending hosters, cookie file might be required. $ plowdown -v1 &#8211;skip-final &#8211;printf &#8216;# %f%n%d%n&#8217; \<br />
&nbsp;<wbr><a rel="nofollow" href="http://uploading.com/files/39267me4/foo.zip/">http://uploading.com/files/39267me4/foo.zip/</a></p>
<h3>6) Safe download. Each URL will be limited in the number of tries and wait delays.</h3>
<p> $ alias plowdown=&#8217;plowdown &#8211;no-overwrite &#8211;max-retries=10 &#8211;timeout=3600&#8242; $ plowdown -m file_with_links.txt </p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/plowshare.conf</i></p>
<dd> Systemwide configuration file.</p>
<dt><i>~/.config/plowshare/plowshare.conf</i></p>
<dd> This is the per-user configuration file.</p>
<dt><i>~/.config/plowshare/exec/</i></p>
<dd> Additional directory considered when searching for executable. See <code>&#8211;captchaprogram</code>, <code>&#8211;run-before</code> and <code>&#8211;run-after</code> switches.</p>
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
<dd> No available module (provided URL is not supported).</p>
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
<dd> Link alive but temporarily unavailable.</p>
<dt>11</p>
<dd> Link alive but requires a password.</p>
<dt>12</p>
<dd> Link alive but requires some authentication (private or premium link).</p>
<dt>13</p>
<dd> Link is dead.</p>
<dt>14</p>
<dd> Can&#8217;t download link because file is too big (need permissions).</p>
<dt>15</p>
<dd> Unknown command line parameter or incompatible options.</dl>
<p> If <code>plowdown</code> is invoked with multiple links or link-list files and one or several errors occur, the first error code is returned added with 100. </p>
<h2>AUTHORS</h2>
<p> Plowshare was initially written by Arnau Sanchez. See the AUTHORS file for a list of some of the many other contributors. </p>
<p> Plowshare is (C) 2010-2014 The Plowshare Team</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-plowup/">plowup</a></code>(1), <code><a href="/docs/linux/man/1-plowdel/">plowdel</a></code>(1), <code><a href="/docs/linux/man/1-plowlist/">plowlist</a></code>(1), <code><a href="/docs/linux/man/1-plowprobe/">plowprobe</a></code>(1), <code><a href="/docs/linux/man/5-plowshare-conf/">plowshare.conf</a></code>(5). </p>
<h2>Index</h2>
