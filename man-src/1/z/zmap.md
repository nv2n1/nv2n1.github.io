---

title: "zmap(1)"
name: "zmap"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zmap/"
description: "zmap – The Fast Internet Scanner"
---

<h2>NAME</h2>
<p> <code>zmap</code> &#8211; The Fast Internet Scanner</p>
<p> zmap [ -p &lt;port&gt; ] [ -o &lt;outfile&gt; ] [ OPTIONS&#8230; ] [ ip/hostname/range ]</p>
<p> <i>ZMap</i> is a network tool for scanning the entire Internet (or large samples). ZMap is capable of scanning the entire Internet in around 45 minutes on a gigabit network connection, reaching ~98% theoretical line speed.</p>
<h2>OPTIONS</h2>
<h3>BASIC OPTIONS</h3>
<dl>
<dt><code>ip</code>/<code>hostname</code>/<code>range</code></dt>
<dd> IP addresses or DNS hostnames to scan. Accepts IP ranges in CIDR block notation. Defaults to 0.0.0/8</dd>
<dt><code>-p</code>, <code>&#8211;target-port=port</code></dt>
<dd> TCP or UDP port number to scan (for SYN scans and basic UDP scans)</dd>
<dt><code>-o</code>, <code>&#8211;output-file=name</code></dt>
<dd> When using an output module that uses a file, write results to this file. Use &#8211; for stdout.</dd>
<dt><code>-b</code>, <code>&#8211;blacklist-file=path</code></dt>
<dd> File of subnets to exclude, in CIDR notation, one-per line. It is recommended you use this to exclude RFC 1918 addresses, multicast, IANA reserved space, and other IANA special-purpose addresses. An example blacklist file <code>blacklist.conf</code> for this purpose.</dd></dl>
<h3>SCAN OPTIONS</h3>
<dl>
<dt><code>-n</code>, <code>&#8211;max-targets=n</code></dt>
<dd> Cap the number of targets to probe. This can either be a number (e.g. -n 1000) or a percentage (e.g. -n 0.1%) of the scannable address space (after excluding blacklist)</dd>
<dt><code>-N</code>, <code>&#8211;max-results=n</code></dt>
<dd> Exit after receiving this many results</dd>
<dt><code>-t</code>, <code>&#8211;max-runtime=secs</code></dt>
<dd> Cap the length of time for sending packets</dd>
<dt><code>-r</code>, <code>&#8211;rate=pps</code></dt>
<dd> Set the send rate in packets/sec</dd>
<dt><code>-B</code>, <code>&#8211;bandwidth=bps</code></dt>
<dd> Set the send rate in bits/second (supports suffixes G, M, and K (e.g. -B 10M for 10 mbps). Thi s overrides the &#8211;rate flag.</dd>
<dt><code>-c</code>, <code>&#8211;cooldown-time=secs</code></dt>
<dd> How long to continue receiving after sending has completed (default=8)</dd>
<dt><code>-e</code>, <code>&#8211;seed=n</code></dt>
<dd> Seed used to select address permutation. Use this if you want to scan addresses in the same order for multiple ZMap runs.</dd>
<dt><code>&#8211;shards=N</code></dt>
<dd> Split the scan up into N shards/partitions among different instances of zmap (default=1). When sharding, <code>&#8211;seed</code> is required.</dd>
<dt><code>&#8211;shard=n</code></dt>
<dd> Set which shard to scan (default=0). Shards are 0-indexed in the range [0, N), where N is the total number of shards. When sharding <code>&#8211;seed</code> is required.</dd>
<dt><code>-T</code>, <code>&#8211;sender-threads=n</code></dt>
<dd> Threads used to send packets. ZMap will attempt to detect the optimal number of send threads based on the number of processor cores.</dd>
<dt><code>-P</code>, <code>&#8211;probes=n</code></dt>
<dd> Number of probes to send to each IP (default=1)</dd>
<dt><code>-d</code>, <code>&#8211;dryrun</code></dt>
<dd> Print out each packet to stdout instead of sending it (useful for debugging)</dd></dl>
<h3>NETWORK OPTIONS</h3>
<dl>
<dt><code>-s</code>, <code>&#8211;source-port=port|range</code></dt>
<dd> Source port(s) to send packets from</dd>
<dt><code>-S</code>, <code>&#8211;source-ip=ip|range</code></dt>
<dd> Source address(es) to send packets from. Either single IP or range (e.g. 10.0.0.1-10.0.0.9)</dd>
<dt><code>-G</code>, <code>&#8211;gateway-mac=addr</code></dt>
<dd> Gateway MAC address to send packets to (in case auto-detection does not work)</dd>
<dt><code>-i</code>, <code>&#8211;interface=name</code></dt>
<dd> Network interface to use</dd></dl>
<h3>PROBE OPTIONS</h3>
<p> ZMap allows users to specify and write their own probe modules. Probe modules are responsible for generating probe packets to send, and processing responses from hosts.</p>
<dl>
<dt><code>&#8211;list-probe-modules</code></dt>
<dd> List available probe modules (e.g. tcp_synscan)</dd>
<dt><code>-M</code>, <code>&#8211;probe-module=name</code></dt>
<dd> Select probe module (default=tcp_synscan)</dd>
<dt><code>&#8211;probe-args=args</code></dt>
<dd> Arguments to pass to probe module</dd>
<dt><code>&#8211;list-output-fields</code></dt>
<dd> List the fields the selected probe module can send to the output module</dd></dl>
<h3>OUTPUT OPTIONS</h3>
<p> ZMap allows users to specify and write their own output modules for use with ZMap. Output modules are responsible for processing the fieldsets returned by the probe module, and outputing them to the user. Users can specify output fields, and write filters over the output fields.</p>
<dl>
<dt><code>&#8211;list-output-modules</code></dt>
<dd> List available output modules (e.g. tcp_synscan)</dd>
<dt><code>-O</code>, <code>&#8211;output-module=name</code></dt>
<dd> Select output module (default=csv)</dd>
<dt><code>&#8211;output-args=args</code></dt>
<dd> Arguments to pass to output module</dd>
<dt><code>-f</code>, <code>&#8211;output-fields=fields</code></dt>
<dd> Comma-separated list of fields to output</dd>
<dt><code>&#8211;output-filter</code></dt>
<dd> Specify an output filter over the fields defined by the probe module. See the output filter section for more details.</dd></dl>
<h3>ADDITIONAL OPTIONS</h3>
<dl>
<dt><code>-C</code>, <code>&#8211;config=filename</code></dt>
<dd> Read a configuration file, which can specify any other options.</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> Do not print status updates once per second</dd>
<dt><code>-g</code>, <code>&#8211;summary</code></dt>
<dd> Print configuration and summary of results at the end of the scan</dd>
<dt><code>-v</code>, <code>&#8211;verbosity=n</code></dt>
<dd> Level of log detail (0-5, default=3)</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Print help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> Print version and exit</dd></dl>
<h3>UDP PROBE MODULE OPTIONS</h3>
<p> These arguments are all passed using the <code>&#8211;probe-args=args</code> option. Only one argument may be passed at a time.</p>
<dl>
<dt><code>file:/path/to/file</code></dt>
<dd> Path to payload file to send to each host over UDP.</dd>
<dt><code>template:/path/to/template</code></dt>
<dd> Path to template file. For each destination host, the template file is populated, set as the UDP payload, and sent.</dd>
<dt><code>text:&lt;text&gt;</code></dt>
<dd> ASCII text to send to each destination host</dd>
<dt><code>hex:&lt;hex&gt;</code></dt>
<dd> Hex-encoded binary to send to each destination host</dd>
<dt><code>template-fields</code></dt>
<dd> Print information about the allowed template fields and exit.</dd></dl>
<h3>OUPUT FILTERS</h3>
<p> Results generated by a probe module can be filtered before being passed to the output module. Filters are defined over the output fields of a probe module. Filters are written in a simple filtering language, similar to SQL, and are passed to ZMap using the <code>&#8211;output-filter</code> option. Output filters are commonly used to filter out duplicate results, or to only pass only sucessful responses to the output module. </p>
<p> Filter expressions are of the form <code>&lt;fieldname&gt; &lt;operation&gt; &lt;value&gt;</code>. The type of <code>&lt;value&gt;</code> must be either a string or unsigned integer literal, and match the type of <code>&lt;fieldname&gt;</code>. The valid operations for integer comparisons are = !=, <i>,</i>, <i>=,</i>=. The operations for string comparisons are =, !=. The <code>&#8211;list-output-fields</code> flag will print what fields and types are available for the selected probe module, and then exit. </p>
<p> Compound filter expressions may be constructed by combining filter expressions using parenthesis to specify order of operations, the &amp;&amp; (logical AND) and || (logical OR) operators. </p>
<p> For example, a filter for only successful, non-duplicate responses would be written as: <code>&#8211;output-filter=&quot;success = 1 &amp;&amp; repeat = 0&quot;</code> </p>
