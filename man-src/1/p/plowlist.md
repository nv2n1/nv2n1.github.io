---
title: "plowlist(1)"
name: "plowlist"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plowlist/"
description: "plowlist – List links from shared folders websites"
---

<h2 class="name">NAME</h2>
<p> plowlist &#8211; List links from shared folders websites</p>
<h2>SYNOPSIS</h2>
<p> <code>plowlist</code> [<i>OPTIONS</i>]&#8230; [<i>MODULE_OPTIONS</i>]&#8230; <i>URL</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>plowlist</code> is a command-line tool designed for listing links (files) on file-sharing websites. Provided links can be downloaded with <a href="/docs/linux/man/1-plowdown/">plowdown</a>(1). </p>
<p> Currently supported hosting sites list is available in README file. </p>
<h2>OPTIONS</h2>
<h3>Common options</h3>
<dl>
<dt><code>-i,</code><i> </i><code>&#8211;interface=</code><i>IFACE</i></dt>
<dd> If your machine has several network interfaces, force using <i>IFACE</i> interface.</dd>
<dt><code>-R, &#8211;recursive</code></dt>
<dd> Recurse into sub folders.</dd>
<dt><i> </i><code>&#8211;printf=</code><i>FORMAT</i></dt>
<dd> Print results (on stdout) in a given format (for each non-dead link). Default string is: <i>&quot;%F%u%n&quot;</i>. Interpreted sequences are:</dd>
<dl>
<dl>
<dt><i>%%</i></dt>
<dd> raw % character</dd>
<dt><i>%f</i></dt>
<dd> filename (can be empty string if module list function does not report any name)</dd>
<dt><i>%F</i></dt>
<dd> empty if %f is empty, or alias to <code>&quot;# %f%n&quot;</code>.</dd>
<dt><i>%m</i></dt>
<dd> module name</dd>
<dt><i>%n</i></dt>
<dd> newline</dd>
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
<dt><code> &#8211;fallback</code></dt>
<dd> If no module is found for link, get page (HTTP GET) and simply grep all URLs contained inside.</dd>
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
<dt><code>-p,</code><i> </i><code>&#8211;link-password=</code><i>PASSWORD</i></dt>
<dd> Used for password-protected folders.</dd></dl>
<p> All switches are not implemented nor required for all modules. See help message for detailed modules option list. </p>
<h2>EXAMPLES</h2>
<h3>1) List links providing shared folder URL(s)</h3>
<p> $ plowlist <a rel="nofollow" href="http://rapidgator.net/folder/1689302/Test.html">http://rapidgator.net/folder/1689302/Test.html</a> </p>
<p> # First URL is processed, then the second one (this is not parallel) $ plowlist <a rel="nofollow" href="http://www.mediafire.com/?qouncpzfe74s9">http://www.mediafire.com/?qouncpzfe74s9</a> \<br />
&nbsp;<wbr><a rel="nofollow" href="http://www.sendspace.com/folder/5njdw7">http://www.sendspace.com/folder/5njdw7</a></p>
<h3>2) Custom results format</h3>
<p> # List to give to plowdown (only links, no filenames) $ plowlist &#8211;printf &#8216;%u%n&#8217; <a rel="nofollow" href="http://www.sendspace.com/folder/5njdw7">http://www.sendspace.com/folder/5njdw7</a> &gt;mylist.txt </p>
<p> # vBulletin &quot;BB&quot; syntax $ plowlist &#8211;printf &#8216;[url=%u]%f[/url]%n&#8217; \<br />
&nbsp;<wbr><a rel="nofollow" href="http://www.sendspace.com/folder/5njdw7">http://www.sendspace.com/folder/5njdw7</a>&nbsp;<wbr>&gt;mylist.txt </p>
<h2>FILES</h2>
<dl>
<dt><i>~/.config/plowshare/plowshare.conf</i></dt>
<dd> This is the per-user configuration file.</dd>
<dt><i>/etc/plowshare.conf</i></dt>
<dd> Systemwide configuration file.</dd></dl>
<p> The file format is described in <code><a href="/docs/linux/man/5-plowshare-conf/">plowshare.conf</a></code>(5). </p>
<h2>EXIT CODES</h2>
<p> Possible exit codes are:</p>
<dl>
<dt>0</dt>
<dd> Success. Folder contain one or several files.</dd>
<dt>1</dt>
<dd> Fatal error. Upstream site updated or unexpected result.</dd>
<dt>2</dt>
<dd> No available module (provided URL is not supported).</dd>
<dt>3</dt>
<dd> Network error. Mostly curl related.</dd>
<dt>10</dt>
<dd> Links are temporarily unavailable. This is used by mirroring/multi-upload services, maybe uploads are still beeing processed.</dd>
<dt>11</dt>
<dd> Folder is password protected.</dd>
<dt>13</dt>
<dd> Folder has been deleted or does not exist or is empty.</dd>
<dt>15</dt>
<dd> Unknown command line parameter or incompatible options.</dd></dl>
<p> If <code>plowlist</code> is invoked with multiple links and one or several errors occur, the first error code is returned added with 100. </p>
<h2>AUTHORS</h2>
<p> Plowshare was initially written by Arnau Sanchez. See the AUTHORS file for a list of some of the many other contributors. </p>
<p> Plowshare is (C) 2010-2014 The Plowshare Team</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-plowdown/">plowdown</a></code>(1), <code><a href="/docs/linux/man/1-plowup/">plowup</a></code>(1), <code><a href="/docs/linux/man/1-plowdel/">plowdel</a></code>(1), <code><a href="/docs/linux/man/1-plowprobe/">plowprobe</a></code>(1), <code><a href="/docs/linux/man/5-plowshare-conf/">plowshare.conf</a></code>(5). </p>
