---
title: "sane-airscan(5)"
name: "sane-airscan"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-airscan/"
description: "sane-airscan – SANE backend for AirScan (eSCL) and WSD scanners and MFP"
---

<p><code>sane-airscan</code> &#8211; SANE backend for AirScan (eSCL) and WSD scanners and MFP</p>
<h2>Description</h2>
<p>The <code>sane-airscan</code> is the universal backend for &quot;driverless&quot; document scanning. Currently it supports two protocols:</p>
<dl>
<dd>
<pre>1. eSCL, also known as AirScan or AirPrint scan
2. WSD, also known as WS-Scan</pre>
<dd></dl>
<h2>Configuration</h2>
<p>The sane-airscan loads its configuration files from the following places:</p>
<dl>
<dd>
<pre>1. /etc/sane.d/airscan.conf
2. /etc/sane.d/airscan.d/*</pre>
<dd></dl>
<p> The configuration file syntax is very similar to the .INI file syntax. It consist of sections, each section contains some variables. Comments are started from # or ; characters and continies until end of line</p>
<dl>
<dd>
<pre># This is a comment
[section 1]
variable 1 = value 1 ; and another comment
variable 2 = value 2</pre>
<dd></dl>
<p> Leading and trailing spaces of variable name and value are striped. If you want to preserve them, put name or value into quotes (&quot;like this&quot;).</p>
<h2>Configuration Of Devices</h2>
<p>If scanner and computer are connected to the same LAN segment, everything expected to &quot;just work&quot; out of box, without any need of manual configuration. </p>
<p> However, in some cases manual configuration can be useful. For example:</p>
<dl>
<dd>
<pre>1. If computer and scanner are connected via IP router
2. There are a lot of devices on a corporate network, but
 only few of them are interesting
3. Automatic discovery works unreliable</pre>
<dd></dl>
<p> To manually configure a device, add the following section to the configuration file:</p>
<dl>
<dd>
<pre>[devices]
&quot;Kyocera eSCL&quot; = <a rel="nofollow" href="http://192.168.1.102:9095/eSCL,">http://192.168.1.102:9095/eSCL,</a> eSCL
&quot;Kyocera WSD&quot; = <a rel="nofollow" href="http://192.168.1.102:5358/WSDScanner,">http://192.168.1.102:5358/WSDScanner,</a> WSD
&quot;Device I do not want to see&quot; = disable</pre>
<dd></dl>
<p> The <code>[devices]</code> section contains all manually configured devices, one line per device, and each line contains a device name on a left side of equation and device URL on a rights side, followed by protocol (eSCL or WSD). If protocol is omitted, eSCL is assumed. You may also disable particular device by using the <code>disable</code> keyword instead of URL. </p>
<p> In addition, you can manually configure a device by directly passing its URL in a device name without adding it to the configuration file. This takes the format <code>protocol:Device Name:URL</code>. The examples above could be written as <code>escl:Kyocera eSCL:<a rel="nofollow" href="http://192.168.1.102:9095/eSCL">http://192.168.1.102:9095/eSCL</a></code> and <code>wsd:Kyocera WSD:<a rel="nofollow" href="http://192.168.1.102:5358/WSDScanner">http://192.168.1.102:5358/WSDScanner</a></code>. </p>
<p> To figure out URLs of available devices, the simplest way is to run a supplied <code>airscan-discover</code> tool on a computer connected with scanner to the same LAN segment. On success, this program will dump to its standard output a list of discovered devices in a format suitable for inclusion into the configuration file. </p>
<p> If running <code>airscan-discover</code> on same LAN segment as a scanner is not possible, you will have to follow a hard way. Your administrator must know device IP address, consult your device manual for the eSCL port, and the URL path component most likely is the &quot;/eSCL&quot;, though on some devices it may differ. Discovering WSD URLs doing this way is much harder, because it is very difficult to guess TCP port and URL path, that in a case of eSCL. </p>
<p> For eSCL devices, the URL can also use the unix:// scheme, such as <a href="unix://scanner.sock/eSCL.">unix://scanner.sock/eSCL.</a> The &quot;host&quot; from the URL is a file name that will be searched for in the directory specified by socket_dir (see below). When connecting to the scanner, all traffic will be sent to the specified UNIX socket instead of a TCP connection.</p>
<h2>Configuration Options</h2>
<p>Miscellaneous options all goes to the <code>[options]</code> section. Currently the following options are supported:</p>
<dl>
<dd>
<pre>[options]
; If there are a lot of scanners around and you are only
; interested in few of them, disable auto discovery and
; configure scanners manually
discovery = enable | disable
; Choose what SANE apps will show in a list of devices:
; scanner network name (the default) or hardware model name
model = network | hardware
; If device supports both eSCL and WSD protocol, sane-airscan
; may either choose the &quot;best&quot; protocol automatically, or
; expose all variants for user, allowing manual protocol selection.
; The default is &quot;auto&quot;
protocol = auto | manual
; Discovery of WSD devices may be &quot;fast&quot; or &quot;full&quot;. The &quot;fast&quot;
; mode works as fast as DNS-SD discovery, but in some cases
; may be unreliable. The &quot;full&quot; mode is slow and reliable.
; This is also possible to disable automatic discovery
; of WSD devices. The default is &quot;fast&quot;.
ws-discovery = fast | full | off
; Scanners that use the unix:// schema in their URL can only specify a
; socket name (not a full path). The name will be searched for in the
; directory specified here. The default is /var/run.
socket_dir = /path/to/directory</pre>
<dd></dl>
<h2>Blacklisting Devices</h2>
<p>This feature can be useful, if you are on a very big network and have a lot of devices around you, while interesting only in a few of them.</p>
<dl>
<dd>
<pre>[blacklist]
model = &quot;Xerox*&quot; ; blacklist by model name
name = &quot;HP*&quot; ; blacklist by network name
ip = 192.168.0.1 ; blacklist by address
ip = 192.168.0.0/24 ; blacklist the whole subnet</pre>
<dd></dl>
<p> Network names come from DNS-SD, WS-Discovery doesn&#8217;t provide this information. For filtering by network name to work, Avahi must be enabled and device must be discoverable via DNS-SD (not necessarily as a scanner, it&#8217;s enough if WSD scanner is discoverable as a printer via DNS-SD). </p>
<p> Blacklisting only affects automatic discovery, and doesn&#8217;t affect manually configured devices</p>
<h2>Debugging</h2>
<p>sane-airscan provides very good instrumentation for troubleshooting without physical access to the problemmatic device. </p>
<p> Debugging facilities can be controlled using the <code>[debug]</code> section of the configuration file:</p>
<dl>
<dd>
<pre>[debug]
; Enable or disable console logging
enable = false | true
; Enable protocol trace and configure output directory
; for trace files. Like in shell, to specify path relative to
; the home directory, start it with tilda character, followed
; by slash, i.e., &quot;~/airscan/trace&quot;. The directory will
; be created automatically.
trace = path
; Hex dump all traffic to the trace file (very verbose!)
hexdump = false | true</pre>
<dd></dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/sane.d/airscan.conf</code>, <code>/etc/sane.d/airscan.d/*</code></p>
<dd>The backend configuration files</p>
<dt><code>/usr/LIBDIR/sane/libsane-airscan.so</code></p>
<dd>The shared library implementing this backend</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_AIRSCAN</code></p>
<dd>This variable if set to <code>true</code> or non-zero numerical value, enables debug messages, that are printed to stdout</p>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This variable alters the search path for configuration files. This is a colon-separated list of directories. These directories are searched for the airscan.conf configuration file and for the airscan.d subdirectory, before the standard path (/etc/sane.d) is searched.</dl>
<h2>Bugs And Support</h2>
<p>If you have found a bug, please file a GitHub issue on a GitHub project page: <code><a rel="nofollow" href="https://github.com/alexpevzner/sane-airscan">https://github.com/alexpevzner/sane-airscan</a></code></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-sane/">sane</a>(7), <a href="/docs/linux/man/1-scanimage/">scanimage</a>(1), <a href="/docs/linux/man/1-xsane/">xsane</a>(1), <a href="/docs/linux/man/1-airscan-discover/">airscan-discover</a>(1)</p>
<h2>Author</h2>
<p>Alexander Pevzner &lt;pzz [at] apevzner.com&gt;</p>
