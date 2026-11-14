---
title: "stonith(8)"
name: "stonith"
section: "8"
letter: "s"
url: "/docs/linux/man/8-stonith/"
description: "stonith – extensible interface for remotely powering down a node in the cluster"
---

<p>stonith &#8211; extensible interface for remotely powering down a node in the cluster</p>
<h2>Synopsis</h2>
<pre><code>stonith -h

stonith [-svh] -L

stonith [-svh] -t stonith-device-type -n

stonith [-svh] -t stonith-device-type {-p stonith-device-parameters | -F stonith-device-parameters-file | name=value...} [-c count] -lS

stonith [-svh] -t stonith-device-type {-p stonith-device-parameters | -F stonith-device-parameters-file | name=value...} [-c count] [-lS] [-T {reset|on|off}] nodename</code></pre>
<h2>Description</h2>
<p>The STONITH module (a.k.a. STOMITH) provides an extensible interface for remotely powering down a node in the cluster. (STONITH = Shoot The Other Node In The Head). The idea is quite simple: when the software running on one machine wants to make sure another machine in the cluster is not using a resource, pull the plug on the other machine. It&#8217;s simple and reliable, albeit admittedly brutal.</p>
<h2>Options</h2>
<dl>
<dt><code>-c count</code></p>
<dd>Perform any actions identified by the -l, -S and -T options <code>count</code> times.</p>
<dt><code>-F stonith-device-parameters-file</code></p>
<dd>Path of file specifying parameters for a stonith device. To determine the syntax of the parameters file for a given device type run: </p>
<pre><code>stonith</code> -t stonith-device-type -n</pre>
<p>All of the listed parameters need to appear in order on a single line in the parameters file and be delimited by whitespace.</p>
<dt><code>-h </code></p>
<dd>Display detailed information about a stonith device including description, configuration information, parameters and any other related information. When specified without a stonith-device-type, detailed information on all stonith devices is displayed. </p>
<p> If you don&#8217;t yet own a stonith device and want to know more about the ones we support, this information is likely to be helpful.</p>
<dt><code>-L</code></p>
<dd>List the valid stonith device types, suitable for passing as an argument to the -t option.</p>
<dt><code>-l</code></p>
<dd>List the hosts controlled by the stonith device.</p>
<dt><code>-n</code></p>
<dd>Output the parameter names of the stonith device.</p>
<dt><code>name=value</code></p>
<dd>Parameter, in the form of a name/value pair, to pass directly to the stonith device. To determine the syntax of the parameters for a given device type run: </p>
<pre><code>stonith</code> -t stonith-device-type -n</pre>
<p>All of the listed parameter names need to be passed with their corresponding values.</p>
<dt><code>-p stonith-device-parameters</code></p>
<dd>Parameters to pass directly to the stonith device. To determine the syntax of the parameters for a given device type run: </p>
<pre><code>stonith</code> -t stonith-device-type -n</pre>
<p>All of the listed parameter names need to appear in order and be delimited by whitespace.</p>
<dt><code>-S</code></p>
<dd>Show the status of the stonith device.</p>
<dt><code>-s</code></p>
<dd>Silent operation. Suppress logging of error messages to standard error.</p>
<dt><code>-T action</code></p>
<dd>The stonith action to perform on the node identified by nodename. Chosen from <code>reset</code>, <code>on</code>, and <code>off</code>. </p>
<p> <code>NOTE:</code> If a nodename is specified without the -T option, the stonith action defaults to <code>reset</code>.</p>
<dt><code>-t stonith-device-type</code></p>
<dd>The type of the stonith device to be used to effect stonith. A list of supported devices for an installation may be obtained using the -L option.</p>
<dt><code>-v</code></p>
<dd>Ignored.</dl>
<h2>Examples</h2>
<p>To determine which stonith devices are available on your installation, use the -L option: </p>
<pre><code>stonith</code> -L</pre>
<p>All of the supported devices will be displayed one per line. Choose one from this list that is best for your environment &#8211; let&#8217;s use wti_nps for the rest of this example. To get detailed information about this device, use the -h option: </p>
<pre><code>stonith</code> -t wti_nps -h</pre>
<p>Included in the output is the list of valid parameter names for wti_nps. To get JUST the list of valid parameter names, use the -n option instead: </p>
<pre><code>stonith</code> -t wti_nps -n</pre>
<p>All of the required parameter names will be displayed one per line. For wti_nps the output is: </p>
<pre>ipaddr
password</pre>
<p>There are three ways to pass these parameters to the device. The first (and preferred) way is by passing name/value pairs on the stonith command line: </p>
<pre><code>stonith</code> -t wti_nps ipaddr=my-dev-ip password=my-dev-pw ...</pre>
<p>The second way, which is maintained only for backward compatibility with legacy clusters, is passing the values IN ORDER on the stonith command line with the -p option: </p>
<pre><code>stonith</code> -t wti_nps -p &quot;my-dev-ip my-dev-pw&quot; ...</pre>
<p>The third way, which is also maintained only for backward compatibility with legacy clusters, is placing the values IN ORDER on a single line in a config file: </p>
<pre>my-dev-ip my-dev-pw</pre>
<p>and passing the name of the file on the stonith command line with the -F option: </p>
<pre><code>stonith</code> -t wti_nps -F ~/my-wtinps-config ...</pre>
<p>To make sure you have the configuration set up correctly and that the device is available for stonith operations, use the -S option: </p>
<pre><code>stonith</code> -t wti_nps ipaddr=my-dev-ip password=my-dev-pw -S</pre>
<p>If all is well at this point, you should see something similar to: </p>
<pre>stonith: wti_nps device OK.</pre>
<p>If you don&#8217;t, some debugging may be necessary to determine if the config info is correct, the device is powered on, etc. The -d option can come in handy here &#8211; you can add it to any stonith command to cause it to generate debug output. </p>
<p> To get the list of hosts controlled by the device, use the -l option: </p>
<pre><code>stonith</code> -t wti_nps ipaddr=my-dev-ip password=my-dev-pw -l</pre>
<p>All of the hosts controlled by the device will be displayed one per line. For wti_nps the output could be: </p>
<pre>node1
node2
node3</pre>
<p>To power off one of these hosts, use the -T option: </p>
<pre><code>stonith</code> -t wti_nps ipaddr=my-dev-ip password=my-dev-pw -T off node2</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-heartbeat/">heartbeat</a></code>(8), <code><a href="/docs/linux/man/8-meatclient/">meatclient</a></code>(8)</p>
<h2>Authors</h2>
<pre>stonith - Alan Robertson &lt;alanr [at] unix.sh&gt; et al.
man page - Horms &lt;horms [at] verge.net.au&gt;</pre>
