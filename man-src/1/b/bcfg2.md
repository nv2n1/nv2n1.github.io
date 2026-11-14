---
title: "bcfg2(1)"
name: "bcfg2"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bcfg2/"
description: "bcfg2 – reconfigure machine based on settings in BCFG2"
---

<h2>NAME</h2>
<p> bcfg2 &#8211; reconfigure machine based on settings in BCFG2</p>
<h2>SYNOPSIS</h2>
<p> <code>bcfg2</code> <i>[-d] [-v] [-p] [-c cache file] [-e] [-f config file] [-I] [-q] [-b bundle]</i> [-r removal mode]</p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>bcfg2</code></p>
<dd> Runs the bcfg2 configuration process on the current host. This process consists of first fetching and executing probes, uploading probe results, fetching the client configuration, checking the current client state, attempting to install the desired configuration, and finally uploading statistics about the bcfg2 execution and client state.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code></p>
<dd> Run in agent (continuous) mode, wait for reconfigure command from server.</p>
<dt><code>-B</code></p>
<dd> Run bcfg2 in build mode. Services aren&#8217;t started, as the system may still be in miniroot.</p>
<dt><code>-D &lt;driver1&gt;,&lt;driver2&gt;</code></p>
<dd> Specify a set of bcfg2 tool drivers. NOTE: only drivers listed will be loaded. (IE, if you don&#8217;t include POSIX, you will be unable to verify/install ConfigFiles, etc)</p>
<dt><code>-E &lt;encoding&gt;</code></p>
<dd> Specify the encoding of Cfg files.</p>
<dt><code>-F &lt;f1,f2&gt;</code></p>
<dd> Specify the server fingerprint.</p>
<dt><code>-I</code></p>
<dd> Run bcfg2 in interactive mode. The user will be prompted before each change.</p>
<dt><code>-K &lt;SSL key file&gt;</code></p>
<dd> Specify the path to the SSL key.</p>
<dt><code>-O</code></p>
<dd> Omit lock check.</p>
<dt><code>-P</code></p>
<dd> Run bcfg2 in paranoid mode. Diffs will be logged for configuration files marked as paranoid by the Bcfg2 server.</p>
<dt><code>-R &lt;retry count&gt;</code></p>
<dd> Specify the number of times that the client will attempt to retry network communication.</p>
<dt><code>-S <a rel="nofollow" href="https://server:port">https://server:port</a></code></p>
<dd> Manually specify the server location (as opposed to using the value in bcfg2.conf).</p>
<dt><code>-b &lt;bundle&gt;</code></p>
<dd> Run bcfg2 against only one bundle in the configuration.</p>
<dt><code>-c &lt;cachefile&gt;</code></p>
<dd> Cache a copy of the configuration in cachefile</p>
<dt><code>-d</code></p>
<dd> Run bcfg2 in debug mode.</p>
<dt><code>-e</code></p>
<dd> When in verbose mode, display extra entry information (temporary until verbosity rework)</p>
<dt><code>-f &lt;specification path&gt;</code></p>
<dd> Configure from a file rather than querying the server.</p>
<dt><code>-g &lt;agent port&gt;</code></p>
<dd> Allows you to specify which port to bind.</p>
<dt><code>-h</code></p>
<dd> Print Usage information.</p>
<dt><code>-i</code></p>
<dd> Daemonize the agent.</p>
<dt><code>-k</code></p>
<dd> Run in bulletproof mode. This currently only effect behavior in the debian toolset; it calls apt-get update and clean and dpkg &#8211;configure &#8211;pending.</p>
<dt><code>-l &lt;whitelist|blacklist&gt;</code></p>
<dd> Run the client in the server decision list mode. This approach is needed when particular changes are deemed &quot;high risk&quot;. It gives the ability to centrally specify these changes, but only install them on clients when administrator supervision is available. Because collaborative configuration is one of the remaining hard issues in configuration management, these issues typically crop up in environments with several administrators and much configuration variety.</p>
<dt><code>-n</code></p>
<dd> Run bcfg2 in dry-run mode. No changes will be made to the system.</p>
<dt><code>-o</code>&lt;LogFile<code>Path&gt;</code></p>
<dd> Writes a log to the specified path.</p>
<dt><code>-p &lt;profile&gt;</code></p>
<dd> Assert a profile for the current client.</p>
<dt><code>-q</code></p>
<dd> Run bcfg2 in quick mode. Package checksum verification won&#8217;t be performed. This mode relaxes the constraints of correctness, and thus should only be used in safe conditions.</p>
<dt><code>-r &lt;mode&gt;</code></p>
<dd> Cause bcfg2 to remove extra configuration elements it detects. Mode is one of all, Services, or Packages. All removes all entries. Likewise, Services and Packages remove only the extra configuration elements of the respective type.</p>
<dt><code>-u &lt;user&gt;</code></p>
<dd> Attempt to authenticate as &#8216;user&#8217;.</p>
<dt><code>-x &lt;password&gt;</code></p>
<dd> Use &#8216;password&#8217; for client communication.</p>
<dt><code>-v</code></p>
<dd> Run bcfg2 in verbose mode.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-bcfg2-server/">bcfg2-server</a>(8),</code> <code><a href="/docs/linux/man/8-bcfg2-info/">bcfg2-info</a>(8)</code></p>
<h2>BUGS</h2>
<h2>Index</h2>
