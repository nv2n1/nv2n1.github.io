---

title: "bcfg2(1)"
name: "bcfg2"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bcfg2/"
description: "bcfg2 – reconfigure machine based on settings in BCFG2"
---

<p> bcfg2 &#8211; reconfigure machine based on settings in BCFG2</p>
<h2>SYNOPSIS</h2>
<p> <code>bcfg2</code> <i>[-d] [-v] [-p] [-c cache file] [-e] [-f config file] [-I] [-q] [-b bundle]</i> [-r removal mode]</p>
<h2>DESCRIPTION</h2>
<dl>
<dt><code>bcfg2</code></dt>
<dd> Runs the bcfg2 configuration process on the current host. This process consists of first fetching and executing probes, uploading probe results, fetching the client configuration, checking the current client state, attempting to install the desired configuration, and finally uploading statistics about the bcfg2 execution and client state.</dd></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code></dt>
<dd> Run in agent (continuous) mode, wait for reconfigure command from server.</dd>
<dt><code>-B</code></dt>
<dd> Run bcfg2 in build mode. Services aren&#8217;t started, as the system may still be in miniroot.</dd>
<dt><code>-D &lt;driver1&gt;,&lt;driver2&gt;</code></dt>
<dd> Specify a set of bcfg2 tool drivers. NOTE: only drivers listed will be loaded. (IE, if you don&#8217;t include POSIX, you will be unable to verify/install ConfigFiles, etc)</dd>
<dt><code>-E &lt;encoding&gt;</code></dt>
<dd> Specify the encoding of Cfg files.</dd>
<dt><code>-F &lt;f1,f2&gt;</code></dt>
<dd> Specify the server fingerprint.</dd>
<dt><code>-I</code></dt>
<dd> Run bcfg2 in interactive mode. The user will be prompted before each change.</dd>
<dt><code>-K &lt;SSL key file&gt;</code></dt>
<dd> Specify the path to the SSL key.</dd>
<dt><code>-O</code></dt>
<dd> Omit lock check.</dd>
<dt><code>-P</code></dt>
<dd> Run bcfg2 in paranoid mode. Diffs will be logged for configuration files marked as paranoid by the Bcfg2 server.</dd>
<dt><code>-R &lt;retry count&gt;</code></dt>
<dd> Specify the number of times that the client will attempt to retry network communication.</dd>
<dt><code>-S <a rel="nofollow" href="https://server:port">https://server:port</a></code></dt>
<dd> Manually specify the server location (as opposed to using the value in bcfg2.conf).</dd>
<dt><code>-b &lt;bundle&gt;</code></dt>
<dd> Run bcfg2 against only one bundle in the configuration.</dd>
<dt><code>-c &lt;cachefile&gt;</code></dt>
<dd> Cache a copy of the configuration in cachefile</dd>
<dt><code>-d</code></dt>
<dd> Run bcfg2 in debug mode.</dd>
<dt><code>-e</code></dt>
<dd> When in verbose mode, display extra entry information (temporary until verbosity rework)</dd>
<dt><code>-f &lt;specification path&gt;</code></dt>
<dd> Configure from a file rather than querying the server.</dd>
<dt><code>-g &lt;agent port&gt;</code></dt>
<dd> Allows you to specify which port to bind.</dd>
<dt><code>-h</code></dt>
<dd> Print Usage information.</dd>
<dt><code>-i</code></dt>
<dd> Daemonize the agent.</dd>
<dt><code>-k</code></dt>
<dd> Run in bulletproof mode. This currently only effect behavior in the debian toolset; it calls apt-get update and clean and dpkg &#8211;configure &#8211;pending.</dd>
<dt><code>-l &lt;whitelist|blacklist&gt;</code></dt>
<dd> Run the client in the server decision list mode. This approach is needed when particular changes are deemed &quot;high risk&quot;. It gives the ability to centrally specify these changes, but only install them on clients when administrator supervision is available. Because collaborative configuration is one of the remaining hard issues in configuration management, these issues typically crop up in environments with several administrators and much configuration variety.</dd>
<dt><code>-n</code></dt>
<dd> Run bcfg2 in dry-run mode. No changes will be made to the system.</dd>
<dt><code>-o</code>&lt;LogFile<code>Path&gt;</code></dt>
<dd> Writes a log to the specified path.</dd>
<dt><code>-p &lt;profile&gt;</code></dt>
<dd> Assert a profile for the current client.</dd>
<dt><code>-q</code></dt>
<dd> Run bcfg2 in quick mode. Package checksum verification won&#8217;t be performed. This mode relaxes the constraints of correctness, and thus should only be used in safe conditions.</dd>
<dt><code>-r &lt;mode&gt;</code></dt>
<dd> Cause bcfg2 to remove extra configuration elements it detects. Mode is one of all, Services, or Packages. All removes all entries. Likewise, Services and Packages remove only the extra configuration elements of the respective type.</dd>
<dt><code>-u &lt;user&gt;</code></dt>
<dd> Attempt to authenticate as &#8216;user&#8217;.</dd>
<dt><code>-x &lt;password&gt;</code></dt>
<dd> Use &#8216;password&#8217; for client communication.</dd>
<dt><code>-v</code></dt>
<dd> Run bcfg2 in verbose mode.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-bcfg2-server/">bcfg2-server</a>(8),</code> <code><a href="/docs/linux/man/8-bcfg2-info/">bcfg2-info</a>(8)</code></p>
<h2>BUGS</h2>
