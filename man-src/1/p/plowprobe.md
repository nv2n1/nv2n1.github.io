---
title: "plowprobe(1)"
name: "plowprobe"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plowprobe/"
description: "plowprobe – Gather information from file sharing download links"
---

<h2>SYNOPSIS</h2>
<p> <code>plowprobe</code> [<i>OPTIONS</i>]&#8230; [<i>MODULE_OPTIONS</i>]&#8230; <i>URL</i>|<i>FILE</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>plowprobe</code> is a command-line tool designed for retrieving metadata from file-sharing download links. Information are printed on stdout (only alive links). Provided links can also be downloaded with <a href="/docs/linux/man/1-plowdown/">plowdown</a>(1). </p>
<p> Currently supported hosting sites list is available in README file. </p>
<h2>OPTIONS</h2>
<h3>Common options</h3>
<dl>
<dt><code>-i,</code><i> </i><code>&#8211;interface=</code><i>IFACE</i></dt>
<dd> If your machine has several network interfaces, force using <i>IFACE</i> interface.</dd>
<dt><i> </i><code>&#8211;printf=</code><i>FORMAT</i></dt>
<dd> Print results (on stdout) in a given format (for each non-dead link). Default string is: <i>&quot;%F%u%n&quot;</i>. Interpreted sequences are:</dd>
<dl>
<dl>
<dt><i>%%</i></dt>
<dd> raw % character</dd>
<dt><i>%c</i></dt>
<dd> probe function return status (0 for success, 13 for dead link, see list below)</dd>
<dt><i>%f</i></dt>
<dd> filename (can be empty string)</dd>
<dt><i>%F</i></dt>
<dd> empty if %f is empty, or alias to <code>&quot;# %f%n&quot;</code>.</dd>
<dt><i>%h</i></dt>
<dd> filehash (can be empty string if not available). Usually MD5 or SHA1. If hoster supports several algorithms, the longest digest is used.</dd>
<dt><i>%i</i></dt>
<dd> file identifier (can be empty string if not available). Usually included in input URL.</dd>
<dt><i>%m</i></dt>
<dd> module name</dd>
<dt><i>%n</i></dt>
<dd> newline</dd>
<dt><i>%s</i></dt>
<dd> filesize in bytes (can be empty string if not available). Note: it&#8217;s often approximative.</dd>
<dt><i>%t</i></dt>
<dd> tabulation character</dd>
<dt><i>%T</i></dt>
<dd> file timestamp (can be empty string if not available). Unix epoch time is preferred.</dd>
<dt><i>%u</i></dt>
<dd> download (source) url</dd></dl>
<p> Note: Metadata are often not fully available from hosters nor implemented by all modules.</dl>
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
<dt><code> &#8211;follow</code></dt>
<dd> If no module is found for link, follow HTTP redirects (curl -L). Default is disabled.</dd>
<dt><code> &#8211;get-module</code></dt>
<dd> Echo module name for each URL and exit. Faster than <code>&#8211;printf=%m</code>. Useful for wrappers.</dd>
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
<dd> Display this help and exit.</dd>
<dt><code>-H, &#8211;longhelp</code></dt>
<dd> Display complete help (with module options) and exit.</dd>
<dt><code> &#8211;version</code></dt>
<dd> Output version information and exit. </dd>
</dl>
<h2>MODULE OPTIONS</h2>
<p> There is none yet! </p>
<h2>EXAMPLES</h2>
<h3>1) Filter alive links in a text file</h3>
<p> $ plowprobe file_with_links.txt &gt; file_with_active_links.txt # Or $ cat file_with_links.txt | plowprobe &#8211; &gt; file_with_active_links.txt</p>
<h3>2) Custom results format</h3>
<p> # Print links information: filename and size $ plowprobe &#8211;printf &#8216;# %f (%s)%n%u%n&#8217; <a rel="nofollow" href="http://www.sendspace.com/file/5njdw7">http://www.sendspace.com/file/5njdw7</a> </p>
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
<dt>15</dt>
<dd> Unknown command line parameter or incompatible options.</dd></dl>
<p> If <code>plowprobe</code> is invoked with multiple links and one or several errors occur, the first error code is returned added with 100. </p>
<h2>AUTHORS</h2>
<p> Plowshare was initially written by Arnau Sanchez. See the AUTHORS file for a list of some of the many other contributors. </p>
<p> Plowshare is (C) 2010-2014 The Plowshare Team</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-plowdown/">plowdown</a></code>(1), <code><a href="/docs/linux/man/1-plowup/">plowup</a></code>(1), <code><a href="/docs/linux/man/1-plowdel/">plowdel</a></code>(1), <code><a href="/docs/linux/man/1-plowlist/">plowlist</a></code>(1), <code><a href="/docs/linux/man/5-plowshare-conf/">plowshare.conf</a></code>(5). </p>
