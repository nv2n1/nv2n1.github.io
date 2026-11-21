---

title: "plowdown(1)"
name: "plowdown"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plowdown/"
description: "plowdown – Simple download manager for file sharing websites"
---

<p> plowdown &#8211; Simple download manager for file sharing websites</p>
<h2>SYNOPSIS</h2>
<p> <code>plowdown</code> [<i>OPTIONS</i>]&#8230; [<i>MODULE_OPTIONS</i>]&#8230; <i>URL</i>|<i>FILE</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>plowdown</code> is a command-line tool designed for automatic download on file-sharing websites. It acts like a web browser, retrieving pages and filling HTML forms (including captchas). </p>
<p> Currently supported hosting sites list is available in README file. </p>
<h2>OPTIONS</h2>
<h3>Common options</h3>
<dl>
<dt><code>-i,</code><i> </i><code>&#8211;interface=</code><i>IFACE</i></dt>
<dd> If your machine has several network interfaces, force using <i>IFACE</i> interface.</dd>
<dt><code>-m, &#8211;mark-downloaded</code></dt>
<dd> Mark downloaded links in (regular) file arguments.</dd>
<dt><code>-o,</code><i> </i><code>&#8211;output-directory=</code><i>DIRECTORY</i></dt>
<dd> Directory where files will be saved. Default is current directory.</dd>
<dt><code>-r,</code><i> </i><code>&#8211;max-retries=</code><i>N</i></dt>
<dd> Set maximum retries for download failures. Apply on module exit status: <code>3</code> (network error), <code>7</code> (captcha error). Default option value is 2 (i.e. 3 tries) and applies for one single URL download.</dd>
<dt><code>-t,</code><i> </i><code>&#8211;timeout=</code><i>SECS</i></dt>
<dd> Cancel download after <i>SECS</i> seconds of waits. Apply on module exit status: <code>10</code> (temporary unavailable error). This error can be returned in various cases: unallowed parallel download, daily downloads limit reached, remote hoster overloaded. Default option value is disabled (no timeout, infinite) and applies for one single URL download.</dd>
<dt><code>-x, &#8211;no-overwrite</code></dt>
<dd> Do not overwrite existing files. Existing file will be preserved and filename will be suffixed with .1, .2, and so on.</dd>
<dt><i> </i><code>&#8211;cache=</code><i>METHOD</i></dt>
<dd> Cache policy regarding module storage space. Each module is able to save data (credentials, authentication session, or tokens) in order to be reused later. Available values:</dd>
<dl>
<dt>
</dt><dd> <code>none</code> : module storage file is deleted before each URL processing. Temporary directory is used.</dd></dl>
<dl>
<dt>
</dt><dd> <code>session</code> (default) : module storage file is deleted at the end of plowdown execution. Temporary directory is used.</dd></dl>
<dl>
<dt>
</dt><dd> <code>shared</code> : module storage file is global and located (in <i>~/.config/plowshare/storage/</i>). It can be accessed by any other instance of plow* scripts. Warning: There is no atomicity (or file locking) on concurrent access. </dd>
<p> Example: Multiple links download using a premium account. If supported by module, login stage could be performed once.</dl>
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
</dt><dd> <code>2</code> : external solver is not able to solve requested captcha. Let plowdown continue solving it normally (will consider <code>&#8211;captchamethod</code> if specified).</dd></dl>
<dl>
<dt>
</dt><dd> <code>7</code> : external solver failed. Note: this exit code is eligible with retry policy (<code>-r</code>/<code>&#8211;max-retries</code>). </dd>
<p> Note: plowdown legacy exit errors can also be returned, for example: <code>1</code> (fatal) or <code>3</code> (network).</dl>
</dl>
<h3>Tuning settings</h3>
<dl>
<dt><i> </i><code>&#8211;min-space=</code><i>LIMIT</i></dt>
<dd> Define threshold amount of available disk space before quitting plowdown. You must specify a suffix. Suffixes are:</dd>
<dl>
<dt>
</dt><dd> <code>M</code> for megabytes (MB i.e. 1000^2),</dd></dl>
<dl>
<dt>
</dt><dd> <code>G</code> for gigabytes (GB i.e. 1000^3),</dd></dl>
<dl>
<dt>
</dt><dd> <code>Mi</code> or <code>m</code> for mebibytes (MiB i.e. 1024^2),</dd></dl>
<dl>
<dt>
</dt><dd> <code>Gi</code> for gibibytes (GiB i.e. 1024^3).</dd></dl>
<dt><i> </i><code>&#8211;max-rate=</code><i>SPEED</i></dt>
<dd> Limit download speed in bytes per second. Suffixes are:</dd>
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
<dt><i> </i><code>&#8211;temp-directory=</code><i>DIRECTORY</i></dt>
<dd> Directory for temporary files: final link download, cookies, images, &#8230;</dd>
<dt><code> &#8211;temp-rename</code></dt>
<dd> Append .part suffix to filename while file is being downloaded. Download resume will not work with this option.</dd>
<dt><code> &#8211;skip-final</code></dt>
<dd> Don&#8217;t process final link (returned by module download function), just skip it. This is applied for each input URL. If you are using this option, you should need <code>&#8211;run-after</code> or <code>&#8211;printf</code> too.</dd>
<dt><i> </i><code>&#8211;run-before=</code><i>PROGRAM</i></dt>
<dd> Call external program or script before new link processing. Provided executable can be located in <i>PATH</i> environment variable. Messages can be sent to stderr, stdout is trashed. </dd>
<p> Three arguments are given:</p>
<dl>
<dt>
</dt><dd> <code>$1</code> module name (lowercase). For example: <i>mediafire</i>.</dd></dl>
<dl>
<dt>
</dt><dd> <code>$2</code> download URL.</dd></dl>
<dl>
<dt>
</dt><dd> <code>$3</code> cookie (empty) file given to download module function. </dd>
<p> Exit status:</dl>
<dl>
<dt>
</dt><dd> <code>0</code> : script success. Plowdown continue normally.</dd></dl>
<dl>
<dt>
</dt><dd> <code>2</code> : script explicitily requests skipping current link. </dd>
<p> Note: Any other script exit status like <code>1</code> (fatal) or <code>3</code> (network) will be ignored (an error message will be reported).</dl>
<dt><i> </i><code>&#8211;run-after=</code><i>PROGRAM</i></dt>
<dd> Call external program or script after final link successful download. Provided executable can be located in <i>PATH</i> environment variable. Messages can be sent to stderr, stdout is trashed. </dd>
<p> Five arguments are given:</p>
<dl>
<dt>
</dt><dd> <code>$1</code> module name (lowercase). For example: <i>mediafire</i>.</dd></dl>
<dl>
<dt>
</dt><dd> <code>$2</code> download URL.</dd></dl>
<dl>
<dt>
</dt><dd> <code>$3</code> cookie file fulfilled by download module function.</dd></dl>
<dl>
<dt>
</dt><dd> <code>$4</code> final URL.</dd></dl>
<dl>
<dt>
</dt><dd> <code>$5</code> final filename. </dd>
<p> Exit status:</dl>
<dl>
<dt>
</dt><dd> <code>0</code> : script success. Plowdown continue normally. </dd>
<p> Note: Any other (non zero) exit status will be ignored (an error message will be reported).</dl>
<dt><i> </i><code>&#8211;printf=</code><i>FORMAT</i></dt>
<dd> Print results (on stdout) in a given format (for each successful download). Default string is: <i>&quot;%F%n&quot;</i>. Interpreted sequences are:</dd>
<dl>
<dl>
<dt><i>%%</i></dt>
<dd> raw % character</dd>
<dt><i>%c</i></dt>
<dd> final cookie filename (with output directory if specified). Name template is <i>plowdown-cookies-NNNN.txt</i>.</dd>
<dt><i>%C</i></dt>
<dd> %c or empty string if module does not require it</dd>
<dt><i>%d</i></dt>
<dd> download (final) url</dd>
<dt><i>%f</i></dt>
<dd> destination (local) filename</dd>
<dt><i>%F</i></dt>
<dd> destination (local) filename (with output directory if specified)</dd>
<dt><i>%m</i></dt>
<dd> module name</dd>
<dt><i>%n</i></dt>
<dd> newline</dd>
<dt><i>%s</i></dt>
<dd> destination (local) file size (in bytes). Important: empty string is returned when <code>&#8211;skip-final</code> switch is specified.</dd>
<dt><i>%t</i></dt>
<dd> tabulation character</dd>
<dt><i>%u</i></dt>
<dd> download (source) url</dd></dl>
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
<dt><code> &#8211;fallback</code></dt>
<dd> If no module is found for link, simply download it (HTTP GET).</dd>
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
<dt><code>-p,</code><i> </i><code>&#8211;link-password=</code><i>PASSWORD</i></dt>
<dd> Used for password-protected files.</dd></dl>
<p> All switches are not implemented nor required for all modules. See long help message for detailed modules option list. </p>
<h2>NOTES</h2>
<h3>Command line authentication string format</h3>
<p> Complete login must have <i>USER:PASSWORD</i> format. The first semi-colon character is the separator. So, <i>PASSWORD</i> can contain a semi-colon character without any trouble.</p>
<dl>
<dt>Don&#8217;t forget to single-quote string if your password contain shell expandable characters (like space, $ or &amp;).</dt>
<dd>
</dd></dl>
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
<dt><i>/etc/plowshare.conf</i></dt>
<dd> Systemwide configuration file.</dd>
<dt><i>~/.config/plowshare/plowshare.conf</i></dt>
<dd> This is the per-user configuration file.</dd>
<dt><i>~/.config/plowshare/exec/</i></dt>
<dd> Additional directory considered when searching for executable. See <code>&#8211;captchaprogram</code>, <code>&#8211;run-before</code> and <code>&#8211;run-after</code> switches.</dd>
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
<dd> No available module (provided URL is not supported).</dd>
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
<dd> Link alive but temporarily unavailable.</dd>
<dt>11</dt>
<dd> Link alive but requires a password.</dd>
<dt>12</dt>
<dd> Link alive but requires some authentication (private or premium link).</dd>
<dt>13</dt>
<dd> Link is dead.</dd>
<dt>14</dt>
<dd> Can&#8217;t download link because file is too big (need permissions).</dd>
<dt>15</dt>
<dd> Unknown command line parameter or incompatible options.</dd></dl>
<p> If <code>plowdown</code> is invoked with multiple links or link-list files and one or several errors occur, the first error code is returned added with 100. </p>
<h2>AUTHORS</h2>
<p> Plowshare was initially written by Arnau Sanchez. See the AUTHORS file for a list of some of the many other contributors. </p>
<p> Plowshare is (C) 2010-2014 The Plowshare Team</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-plowup/">plowup</a></code>(1), <code><a href="/docs/linux/man/1-plowdel/">plowdel</a></code>(1), <code><a href="/docs/linux/man/1-plowlist/">plowlist</a></code>(1), <code><a href="/docs/linux/man/1-plowprobe/">plowprobe</a></code>(1), <code><a href="/docs/linux/man/5-plowshare-conf/">plowshare.conf</a></code>(5). </p>
