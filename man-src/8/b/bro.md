---
title: "bro(8)"
name: "bro"
section: "8"
letter: "b"
url: "/docs/linux/man/8-bro/"
description: "bro – passive network traffic analyzer"
---

<p>bro &#8211; passive network traffic analyzer</p>
<h2>Synopsis</h2>
<p><code>bro</code> / [<i>options</i>] [<i>file</i> &#8230;]</p>
<h2>Description</h2>
<p>Bro is primarily a security monitor that inspects all traffic on a link in depth for signs of suspicious activity. More generally, however, Bro supports a wide range of traffic analysis tasks even outside of the security domain, including performance measurements and helping with trouble-shooting. </p>
<p> Bro comes with built-in functionality for a range of analysis and detection tasks, including detecting malware by interfacing to external registries, reporting vulnerable versions of software seen on the network, identifying popular web applications, detecting SSH brute-forcing, validating SSL certificate chains, among others.</p>
<h2>Options</h2>
<dl>
<dt><code>&lt;file&gt;</code></p>
<dd>policy file, or read stdin</p>
<dt><code>-a</code>, &#8211;parse-only</p>
<dd>exit immediately after parsing scripts</p>
<dt><code>-b</code>, &#8211;bare-mode</p>
<dd>don&#8217;t load scripts from the base/ directory</p>
<dt><code>-d</code>, &#8211;debug-policy</p>
<dd>activate policy file debugging</p>
<dt><code>-e</code>, &#8211;exec &lt;bro code&gt;</p>
<dd>augment loaded policies by given code</p>
<dt><code>-f</code>, &#8211;filter &lt;filter&gt;</p>
<dd>tcpdump filter</p>
<dt><code>-g</code>, &#8211;dump-config</p>
<dd>dump current config into .state dir</p>
<dt><code>-h</code>, &#8211;help|-?</p>
<dd>command line help</p>
<dt><code>-i</code>, &#8211;iface &lt;interface&gt;</p>
<dd>read from given interface</p>
<dt><code>-p</code>, &#8211;prefix &lt;prefix&gt;</p>
<dd>add given prefix to policy file resolution</p>
<dt><code>-r</code>, &#8211;readfile &lt;readfile&gt;</p>
<dd>read from given tcpdump file</p>
<dt><code>-s</code>, &#8211;rulefile &lt;rulefile&gt;</p>
<dd>read rules from given file</p>
<dt><code>-t</code>, &#8211;tracefile &lt;tracefile&gt;</p>
<dd>activate execution tracing</p>
<dt><code>-w</code>, &#8211;writefile &lt;writefile&gt;</p>
<dd>write to given tcpdump file</p>
<dt><code>-v</code>, &#8211;version</p>
<dd>print version and exit</p>
<dt><code>-x</code>, &#8211;print-state &lt;file.bst&gt;</p>
<dd>print contents of state file</p>
<dt><code>-z</code>, &#8211;analyze &lt;analysis&gt;</p>
<dd>run the specified policy file analysis</p>
<dt><code>-C</code>, &#8211;no-checksums</p>
<dd>ignore checksums</p>
<dt><code>-F</code>, &#8211;force-dns</p>
<dd>force DNS</p>
<dt><code>-I</code>, &#8211;print-id &lt;ID name&gt;</p>
<dd>print out given ID</p>
<dt><code>-J</code>, &#8211;set-seed &lt;seed&gt;</p>
<dd>set the random number seed</p>
<dt><code>-K</code>, &#8211;md5-hashkey &lt;hashkey&gt;</p>
<dd>set key for MD5-keyed hashing</p>
<dt><code>-N</code>, &#8211;print-plugins</p>
<dd>print available plugins and exit (<code>-NN</code> for verbose)</p>
<dt><code>-P</code>, &#8211;prime-dns</p>
<dd>prime DNS</p>
<dt><code>-Q</code>, &#8211;time</p>
<dd>print execution time summary to stderr</p>
<dt><code>-R</code>, &#8211;replay &lt;events.bst&gt;</p>
<dd>replay events</p>
<dt><code>-S</code>, &#8211;debug-rules</p>
<dd>enable rule debugging</p>
<dt><code>-T</code>, &#8211;re-level &lt;level&gt;</p>
<dd>set &#8216;RE_level&#8217; for rules</p>
<dt><code>-U</code>, &#8211;status-file &lt;file&gt;</p>
<dd>Record process status in file</p>
<dt><code>-W</code>, &#8211;watchdog</p>
<dd>activate watchdog timer</p>
<dt><code>-X</code>, &#8211;broxygen &lt;cfgfile&gt;</p>
<dd>generate documentation based on config file</p>
<dt><code>&#8211;pseudo-realtime[=</code>&lt;speedup&gt;]</p>
<dd>enable pseudo-realtime for performance evaluation (default 1)</p>
<dt><code>&#8211;load-seeds</code> &lt;file&gt;</p>
<dd>load seeds from given file</p>
<dt><code>&#8211;save-seeds</code> &lt;file&gt;</p>
<dd>save seeds to given file</p>
<dt>The following option is available only when Bro is built with the &#8211;enable-debug configure option:</p>
<dd>
<dt><code>-B</code>, &#8211;debug &lt;dbgstreams&gt;</p>
<dd>Enable debugging output for selected streams (&#8216;-B help&#8217; for help)</p>
<dt>The following options are available only when Bro is built with gperftools support (use the &#8211;enable-perftools and &#8211;enable-perftools-debug configure options):</p>
<dd>
<dt><code>-m</code>, &#8211;mem-leaks</p>
<dd>show leaks</p>
<dt><code>-M</code>, &#8211;mem-profile</p>
<dd>record heap</dl>
<h2>Environment</h2>
<dl>
<dt><code>BROPATH</code></p>
<dd>file search path</p>
<dt><code>BRO_PLUGIN_PATH</code></p>
<dd>plugin search path</p>
<dt><code>BRO_PLUGIN_ACTIVATE</code></p>
<dd>plugins to always activate</p>
<dt><code>BRO_PREFIXES</code></p>
<dd>prefix list</p>
<dt><code>BRO_DNS_FAKE</code></p>
<dd>disable DNS lookups</p>
<dt><code>BRO_SEED_FILE</code></p>
<dd>file to load seeds from</p>
<dt><code>BRO_LOG_SUFFIX</code></p>
<dd>ASCII log file extension</p>
<dt><code>BRO_PROFILER_FILE</code></p>
<dd>Output file for script execution statistics</p>
<dt><code>BRO_DISABLE_BROXYGEN</code></p>
<dd>Disable Broxygen documentation support</dl>
<h2>Author</h2>
<p><code>bro</code> was written by The Bro Project &lt;info [at] bro.org&gt;.</p>
