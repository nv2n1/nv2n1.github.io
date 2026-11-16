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
<dt><code>&lt;file&gt;</code></dt>
<dd>policy file, or read stdin</dd>
<dt><code>-a</code>, &#8211;parse-only</dt>
<dd>exit immediately after parsing scripts</dd>
<dt><code>-b</code>, &#8211;bare-mode</dt>
<dd>don&#8217;t load scripts from the base/ directory</dd>
<dt><code>-d</code>, &#8211;debug-policy</dt>
<dd>activate policy file debugging</dd>
<dt><code>-e</code>, &#8211;exec &lt;bro code&gt;</dt>
<dd>augment loaded policies by given code</dd>
<dt><code>-f</code>, &#8211;filter &lt;filter&gt;</dt>
<dd>tcpdump filter</dd>
<dt><code>-g</code>, &#8211;dump-config</dt>
<dd>dump current config into .state dir</dd>
<dt><code>-h</code>, &#8211;help|-?</dt>
<dd>command line help</dd>
<dt><code>-i</code>, &#8211;iface &lt;interface&gt;</dt>
<dd>read from given interface</dd>
<dt><code>-p</code>, &#8211;prefix &lt;prefix&gt;</dt>
<dd>add given prefix to policy file resolution</dd>
<dt><code>-r</code>, &#8211;readfile &lt;readfile&gt;</dt>
<dd>read from given tcpdump file</dd>
<dt><code>-s</code>, &#8211;rulefile &lt;rulefile&gt;</dt>
<dd>read rules from given file</dd>
<dt><code>-t</code>, &#8211;tracefile &lt;tracefile&gt;</dt>
<dd>activate execution tracing</dd>
<dt><code>-w</code>, &#8211;writefile &lt;writefile&gt;</dt>
<dd>write to given tcpdump file</dd>
<dt><code>-v</code>, &#8211;version</dt>
<dd>print version and exit</dd>
<dt><code>-x</code>, &#8211;print-state &lt;file.bst&gt;</dt>
<dd>print contents of state file</dd>
<dt><code>-z</code>, &#8211;analyze &lt;analysis&gt;</dt>
<dd>run the specified policy file analysis</dd>
<dt><code>-C</code>, &#8211;no-checksums</dt>
<dd>ignore checksums</dd>
<dt><code>-F</code>, &#8211;force-dns</dt>
<dd>force DNS</dd>
<dt><code>-I</code>, &#8211;print-id &lt;ID name&gt;</dt>
<dd>print out given ID</dd>
<dt><code>-J</code>, &#8211;set-seed &lt;seed&gt;</dt>
<dd>set the random number seed</dd>
<dt><code>-K</code>, &#8211;md5-hashkey &lt;hashkey&gt;</dt>
<dd>set key for MD5-keyed hashing</dd>
<dt><code>-N</code>, &#8211;print-plugins</dt>
<dd>print available plugins and exit (<code>-NN</code> for verbose)</dd>
<dt><code>-P</code>, &#8211;prime-dns</dt>
<dd>prime DNS</dd>
<dt><code>-Q</code>, &#8211;time</dt>
<dd>print execution time summary to stderr</dd>
<dt><code>-R</code>, &#8211;replay &lt;events.bst&gt;</dt>
<dd>replay events</dd>
<dt><code>-S</code>, &#8211;debug-rules</dt>
<dd>enable rule debugging</dd>
<dt><code>-T</code>, &#8211;re-level &lt;level&gt;</dt>
<dd>set &#8216;RE_level&#8217; for rules</dd>
<dt><code>-U</code>, &#8211;status-file &lt;file&gt;</dt>
<dd>Record process status in file</dd>
<dt><code>-W</code>, &#8211;watchdog</dt>
<dd>activate watchdog timer</dd>
<dt><code>-X</code>, &#8211;broxygen &lt;cfgfile&gt;</dt>
<dd>generate documentation based on config file</dd>
<dt><code>&#8211;pseudo-realtime[=</code>&lt;speedup&gt;]</dt>
<dd>enable pseudo-realtime for performance evaluation (default 1)</dd>
<dt><code>&#8211;load-seeds</code> &lt;file&gt;</dt>
<dd>load seeds from given file</dd>
<dt><code>&#8211;save-seeds</code> &lt;file&gt;</dt>
<dd>save seeds to given file</dd>
<dt>The following option is available only when Bro is built with the &#8211;enable-debug configure option:</dt>
<dd>
</dd><dt><code>-B</code>, &#8211;debug &lt;dbgstreams&gt;</dt>
<dd>Enable debugging output for selected streams (&#8216;-B help&#8217; for help)</dd>
<dt>The following options are available only when Bro is built with gperftools support (use the &#8211;enable-perftools and &#8211;enable-perftools-debug configure options):</dt>
<dd>
</dd><dt><code>-m</code>, &#8211;mem-leaks</dt>
<dd>show leaks</dd>
<dt><code>-M</code>, &#8211;mem-profile</dt>
<dd>record heap</dd></dl>
<h2>Environment</h2>
<dl>
<dt><code>BROPATH</code></dt>
<dd>file search path</dd>
<dt><code>BRO_PLUGIN_PATH</code></dt>
<dd>plugin search path</dd>
<dt><code>BRO_PLUGIN_ACTIVATE</code></dt>
<dd>plugins to always activate</dd>
<dt><code>BRO_PREFIXES</code></dt>
<dd>prefix list</dd>
<dt><code>BRO_DNS_FAKE</code></dt>
<dd>disable DNS lookups</dd>
<dt><code>BRO_SEED_FILE</code></dt>
<dd>file to load seeds from</dd>
<dt><code>BRO_LOG_SUFFIX</code></dt>
<dd>ASCII log file extension</dd>
<dt><code>BRO_PROFILER_FILE</code></dt>
<dd>Output file for script execution statistics</dd>
<dt><code>BRO_DISABLE_BROXYGEN</code></dt>
<dd>Disable Broxygen documentation support</dd></dl>
<h2>Author</h2>
<p><code>bro</code> was written by The Bro Project &lt;info [at] bro.org&gt;.</p>
