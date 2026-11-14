---
title: "ifup(8)"
name: "ifup"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ifup/"
description: "ifup – bring a network interface up"
---

<p>ifup &#8211; bring a network interface up </p>
<p> ifdown &#8211; take a network interface down </p>
<p> ifquery &#8211; parse interface configuration</p>
<h2>Synopsis</h2>
<p><code>ifup </code> [<code>-nv</code>] [<code>&#8211;no-act</code>] [<code>&#8211;verbose</code>] [<code>-i</code> <i>FILE</i>|<code>&#8211;interfaces=</code><i>FILE</i>] [<code>&#8211;state-dir=</code><i>DIR</i>] [<code>&#8211;allow</code> <i>CLASS</i>] <code>-a</code>|<i>IFACE</i>&#8230;<br />
 <code>ifup </code> <code>-h</code>|<code>&#8211;help</code><br />
 <code>ifup </code> <code>-V</code>|<code>&#8211;version</code> </p>
<p> <code>ifdown</code> [<code>-nv</code>] [<code>&#8211;no-act</code>] [<code>&#8211;verbose</code>] [<code>-i</code> <i>FILE</i>|<code>&#8211;interfaces=</code><i>FILE</i>] [<code>&#8211;state-dir=</code><i>DIR</i>] [<code>&#8211;allow</code> <i>CLASS</i>] <code>-a</code>|<i>IFACE</i>&#8230; </p>
<p> <code>ifquery</code> [<code>-nv</code>] [<code>&#8211;verbose</code>] [<code>-i</code> <i>FILE</i>|<code>&#8211;interfaces=</code><i>FILE</i>] [<code>&#8211;state-dir=</code><i>DIR</i>] [<code>&#8211;allow</code> <i>CLASS</i>] <i>IFACE</i>&#8230; </p>
<p> <code>ifquery</code> <code>-l</code>|<code>&#8211;list</code> [<code>-nv</code>] [<code>&#8211;verbose</code>] [<code>-i</code> <i>FILE</i>|<code>&#8211;interfaces=</code><i>FILE</i>] [<code>&#8211;state-dir=</code><i>DIR</i>] [<code>&#8211;allow</code> <i>CLASS</i>] [<code>-a</code>|<i>IFACE</i>&#8230;] </p>
<p> <code>ifquery</code> <code>&#8211;state</code> [<code>&#8211;state-dir=</code><i>DIR</i>] [<code>&#8211;allow</code> <i>CLASS</i>] [<code>-a</code>|<i>IFACE</i>&#8230;]</p>
<h2>Description</h2>
<p>The <code>ifup</code> and <code>ifdown</code> commands may be used to configure (or, respectively, deconfigure) network interfaces based on interface definitions in the file <i>/etc/network/interfaces</i>. <code>ifquery</code> command may be used to parse interfaces configuration.</p>
<h2>Options</h2>
<p>A summary of options is included below.</p>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd>If given to <code>ifup</code>, affect all interfaces marked <code>auto</code>. Interfaces are brought up in the order in which they are defined in <i>/etc/network/interfaces</i>. Combined with <code>&#8211;allow</code>, acts on all interfaces of a specified class instead. If given to <code>ifdown</code>, affect all defined interfaces. Interfaces are brought down in the order in which they are currently listed in the state file. Only interfaces defined in <i>/etc/network/interfaces</i> will be brought down.</p>
<dt><code>&#8211;force</code></p>
<dd>Force configuration or deconfiguration of the interface.</p>
<dt><code>&#8211;ignore-errors</code></p>
<dd>If any of the commands of scripts fails, continue.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>Show summary of options.</p>
<dt><code>&#8211;allow=</code><i>CLASS</i></p>
<dd>Only allow interfaces listed in an <i>allow-CLASS</i> line in <i>/etc/network/interfaces</i> to be acted upon.</p>
<dt><code>-i</code> <i>FILE</i>, <code>&#8211;interfaces=</code><i>FILE</i></p>
<dd>Read interface definitions from <i>FILE</i> instead of from <i>/etc/network/interfaces</i>.</p>
<dt><code>&#8211;state-dir=</code><i>DIR</i></p>
<dd>Keep interface state in <i>DIR</i> instead of in <i>/run/network</i>.</p>
<dt><code>-X</code><i> PATTERN</i>, <code>&#8211;exclude=</code><i>PATTERN</i></p>
<dd>Exclude interfaces from the list of interfaces to operate on by the <i>PATTERN</i>. <i>PATTERN</i> uses a usual shell glob syntax. If shell wildcards are not used, it must match the exact interface name. This option may be specified multiple times resulting in more than one pattern being excluded.</p>
<dt><code>-o</code><i> OPTION</i><code>=</code><i>VALUE</i></p>
<dd>Set <i>OPTION</i> to <i>VALUE</i> as though it were in <i>/etc/network/interfaces</i>.</p>
<dt><code>-n</code>, <code>&#8211;no-act</code></p>
<dd>Don&#8217;t configure any interfaces or run any &quot;up&quot; or &quot;down&quot; commands.</p>
<dt><code>&#8211;no-mappings</code></p>
<dd>Don&#8217;t run any mappings. See <code><a href="/docs/linux/man/5-interfaces/">interfaces</a></code>(5) for more information about the mapping feature.</p>
<dt><code>&#8211;no-scripts</code></p>
<dd>Don&#8217;t run any scripts under /etc/network/if-*.d/</p>
<dt><code>&#8211;no-loopback</code></p>
<dd>Disable special handling of the loopback interface. By default, the loopback interface (<i>lo</i> on Linux) is predefined internally as an auto interface, so it&#8217;s brought up on <code>ifup -a</code> automatically. In the case the loopback device is redefined by user, the interface is configured just once anyway. If, however, another interface is also defined as loopback, it&#8217;s configured as usual. Specifying this option disables this behaviour, so the loopback interface won&#8217;t be configured automatically.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd>Show copyright and version information.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Show commands as they are executed.</p>
<dt><code>-l</code>, <code>&#8211;list</code></p>
<dd>For <code>ifquery</code>, list all the interfaces which match the specified class. If no class specified, prints all the interfaces listed as <code>auto</code>.</p>
<dt><code>&#8211;state</code></p>
<dd>For <code>ifquery</code>, dump the state of the interfaces. When no interfaces specified, lists all interfaces brought up together with logical interfaces assigned to them and exits with a status code indicating success. If one or more interfaces specified, display state of these interfaces only; successful code is returned if all of interfaces given as arguments are up. Otherwise, 0 is returned.</dl>
<h2>Examples</h2>
<dl>
<dt><code>ifup -a</code></p>
<dd>Bring up all the interfaces defined with <i>auto</i> in <i>/etc/network/interfaces</i></p>
<dt><code>ifup eth0</code></p>
<dd>Bring up interface <code>eth0</code></p>
<dt><code>ifup eth0=home</code></p>
<dd>Bring up interface <code>eth0</code> as logical interface <code>home</code></p>
<dt><code>ifdown -a</code></p>
<dd>Bring down all interfaces that are currently up.</p>
<dt><code>ifquery -l</code></p>
<dd>Print names of all interfaces specified with the <code>auto</code> keyword.</p>
<dt><code>ifquery -l &#8211;allow=hotplug</code></p>
<dd>Print names of all interfaces specified with the <code>allow-hotplug</code> keyword.</p>
<dt><code>ifquery eth0</code></p>
<dd>Display the interface options as specified in the <code>ifupdown</code> configuration. Each key-value pair is printed out on individual line using &quot;<code>: </code>&quot; as separator.</dl>
<h2>Notes</h2>
<p><code>ifup</code>, <code>ifdown</code>, and <code>ifquery</code> are actually the same program called by different names. </p>
<p> The program does not configure network interfaces directly; it runs low level utilities such as <code>ip</code> to do its dirty work. </p>
<p> When invoked, <code>ifdown</code> checks if <code>ifup</code> is still running. In that case, <code>SIGTERM</code> is sent to ifup. </p>
<p> During interface deconfiguration, <code>ifdown</code> ignores errors the same way as if <code>&#8211;ignore-errors</code> was specified.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/network/interfaces</i></p>
<dd>definitions of network interfaces See <code><a href="/docs/linux/man/5-interfaces/">interfaces</a></code>(5) for more information.</p>
<dt><i>/run/network/ifstate</i></p>
<dd>current state of network interfaces</dl>
<h2>Concurrency</h2>
<p>Ifupdown uses per-interface locking to ensure that concurrent ifup and ifdown calls to the same interface are run in serial. However, calls to different interfaces will be able to run in parallel.</p>
<h2>Exit Status</h2>
<p>For <code>ifup</code> and <code>ifdown</code>, the exit status will be 0 if the given interface(s) have all been (de)configured successfully, 1 if there was any error. The result of these commands is idempotent; running <code>ifup</code> on an interface that is already up will result in an exit status of 0, and similarly running <code>ifdown</code> on an interface that is not up will also result in an exit status of 0. </p>
<p> <code>ifquery</code> will normally return with exit status 0 if an interface with a matching iface stanza, 1 if there is no matching stanza. <code>ifquery &#8211;state</code> will also return with exit status 1 if the given interface was known but was not up.</p>
<h2>Known Bugs/Limitations</h2>
<p>The program keeps records of whether network interfaces are up or down. Under exceptional circumstances these records can become inconsistent with the real states of the interfaces. For example, an interface that was brought up using <code>ifup</code> and later deconfigured using <code>ifconfig</code> will still be recorded as up. To fix this you can use the <code>&#8211;force</code> option to force <code>ifup</code> or <code>ifdown</code> to run configuration or deconfiguration commands despite what it considers the current state of the interface to be. </p>
<p> The file <i>/run/network/ifstate</i> must be writable for <code>ifup</code> or <code>ifdown</code> to work properly. If that location is not writable (for example, because the root filesystem is mounted read-only for system recovery) then <i>/run/network/ifstate</i> should be made a symbolic link to a writable location. If that is not possible then you can use the <code>&#8211;force</code> option to run configuration or deconfiguration commands without updating the file. </p>
<p> Note that the program does not run automatically: <code>ifup</code> alone does not bring up interfaces that appear as a result of hardware being installed and <code>ifdown</code> alone does not bring down interfaces that disappear as a result of hardware being removed. To automate the configuration of network interfaces you need to install other packages such as <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7) or <code><a href="/docs/linux/man/8-ifplugd/">ifplugd</a></code>(8).</p>
<h2>Authors</h2>
<p>The ifupdown suite was created by Anthony Towns &lt;aj [at] azure.humbug.org.au&gt;, and is currently maintained by Guus Sliepen &lt;guus [at] debian.org&gt;. </p>
<p> Many others have helped develop ifupdown over time, see /usr/share/doc/ifupdown/changelog.Debian.gz for a full history.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-interfaces/">interfaces</a></code>(5), <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8), <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8). </p>
