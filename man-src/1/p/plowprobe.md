---
title: "plowprobe(1)"
name: "plowprobe"
section: "1"
letter: "p"
url: "/docs/linux/man/1-plowprobe/"
description: "plowprobe – Gather information from file sharing download links"
---

<h2 class="name">NAME</h2>
<p> plowprobe &#8211; Gather information from file sharing download links</p>
<h2>SYNOPSIS</h2>
<p> <code>plowprobe</code> [<i>OPTIONS</i>]&#8230; [<i>MODULE_OPTIONS</i>]&#8230; <i>URL</i>|<i>FILE</i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>plowprobe</code> is a command-line tool designed for retrieving metadata from file-sharing download links. Information are printed on stdout (only alive links). Provided links can also be downloaded with <a href="/docs/linux/man/1-plowdown/">plowdown</a>(1). </p>
<p> Currently supported hosting sites list is available in README file. </p>
<h2>OPTIONS</h2>
<h3>Common options</h3>
<dl>
<dt><code>-i,</code><i> </i><code>&#8211;interface=</code><i>IFACE</i></p>
<dd> If your machine has several network interfaces, force using <i>IFACE</i> interface.</p>
<dt><i> </i><code>&#8211;printf=</code><i>FORMAT</i></p>
<dd> Print results (on stdout) in a given format (for each non-dead link). Default string is: <i>&quot;%F%u%n&quot;</i>. Interpreted sequences are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>%%</i></p>
<dd> raw % character</p>
<dt><i>%c</i></p>
<dd> probe function return status (0 for success, 13 for dead link, see list below)</p>
<dt><i>%f</i></p>
<dd> filename (can be empty string)</p>
<dt><i>%F</i></p>
<dd> empty if %f is empty, or alias to <code>&quot;# %f%n&quot;</code>.</p>
<dt><i>%h</i></p>
<dd> filehash (can be empty string if not available). Usually MD5 or SHA1. If hoster supports several algorithms, the longest digest is used.</p>
<dt><i>%i</i></p>
<dd> file identifier (can be empty string if not available). Usually included in input URL.</p>
<dt><i>%m</i></p>
<dd> module name</p>
<dt><i>%n</i></p>
<dd> newline</p>
<dt><i>%s</i></p>
<dd> filesize in bytes (can be empty string if not available). Note: it&#8217;s often approximative.</p>
<dt><i>%t</i></p>
<dd> tabulation character</p>
<dt><i>%T</i></p>
<dd> file timestamp (can be empty string if not available). Unix epoch time is preferred.</p>
<dt><i>%u</i></p>
<dd> download (source) url</dl>
<p> Note: Metadata are often not fully available from hosters nor implemented by all modules.</dl>
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
<dt><code> &#8211;follow</code></p>
<dd> If no module is found for link, follow HTTP redirects (curl -L). Default is disabled.</p>
<dt><code> &#8211;get-module</code></p>
<dd> Echo module name for each URL and exit. Faster than <code>&#8211;printf=%m</code>. Useful for wrappers.</p>
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
<dd> Display this help and exit.</p>
<dt><code>-H, &#8211;longhelp</code></p>
<dd> Display complete help (with module options) and exit.</p>
<dt><code> &#8211;version</code></p>
<dd> Output version information and exit. </p>
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
<dt><i>~/.config/plowshare/plowshare.conf</i></p>
<dd> This is the per-user configuration file.</p>
<dt><i>/etc/plowshare.conf</i></p>
<dd> Systemwide configuration file.</dl>
<p> The file format is described in <code><a href="/docs/linux/man/5-plowshare-conf/">plowshare.conf</a></code>(5). </p>
<h2>EXIT CODES</h2>
<p> Possible exit codes are:</p>
<dl>
<dt>0</p>
<dd> Success. Folder contain one or several files.</p>
<dt>1</p>
<dd> Fatal error. Upstream site updated or unexpected result.</p>
<dt>2</p>
<dd> No available module (provided URL is not supported).</p>
<dt>3</p>
<dd> Network error. Mostly curl related.</p>
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
<dt>15</p>
<dd> Unknown command line parameter or incompatible options.</dl>
<p> If <code>plowprobe</code> is invoked with multiple links and one or several errors occur, the first error code is returned added with 100. </p>
<h2>AUTHORS</h2>
<p> Plowshare was initially written by Arnau Sanchez. See the AUTHORS file for a list of some of the many other contributors. </p>
<p> Plowshare is (C) 2010-2014 The Plowshare Team</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-plowdown/">plowdown</a></code>(1), <code><a href="/docs/linux/man/1-plowup/">plowup</a></code>(1), <code><a href="/docs/linux/man/1-plowdel/">plowdel</a></code>(1), <code><a href="/docs/linux/man/1-plowlist/">plowlist</a></code>(1), <code><a href="/docs/linux/man/5-plowshare-conf/">plowshare.conf</a></code>(5). </p>
<h2>Index</h2>
