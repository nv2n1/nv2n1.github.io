---
title: "virt-who(8)"
name: "virt-who"
section: "8"
letter: "v"
url: "/docs/linux/man/8-virt-who/"
description: "virt-who – Agent for reporting virtual guest IDs to Subscription Asset Manager, Satellite 6, or Satellite 5."
---

<p>virt-who &#8211; Agent for reporting virtual guest IDs to Subscription Asset Manager, Satellite 6, or Satellite 5.</p>
<h2>Synopsis</h2>
<p>virt-who [-d] [-i INTERVAL] [-b] [-o] [&#8211;sam|&#8211;satellite5|&#8211;satellite6] [&#8211;libvirt|&#8211;vdsm|&#8211;esx|&#8211;rhevm|&#8211;hyperv]</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>show this help message and exit</p>
<dt><code>-d</code>, <code>&#8211;debug</code></p>
<dd>Enable debugging output</p>
<dt><code>-o</code>, <code>&#8211;one-shot</code></p>
<dd>Send the list of guest IDs and exit immediately</p>
<dt><code>-i</code> INTERVAL, <code>&#8211;interval</code>=<i>INTERVAL</i></p>
<dd>Acquire and send guest information each N seconds; note that this option is recommendation only, requested interval might not been honoured and the actual interval might be longer or shorter depending on backend that is used.</p>
<dt><code>-p</code>, <code>&#8211;print</code></p>
<dd>Print the host/guests association in JSON format to stdout</p>
<dt><code>-c</code>, <code>&#8211;config</code></p>
<dd>Use configuration file directly, can be used multiple times. See <a href="/docs/linux/man/5-virt-who-config/">virt-who-config</a>(5) for details about configuration file format.</p>
<dd></dl>
<h3>Virtualization backend</h3>
<dl>
<dd>Choose virtualization backend that should be used to gather host/guest associations</p>
<dt><code>&#8211;libvirt</code></p>
<dd>Use libvirt to list virtual guests [default]</p>
<dt><code>&#8211;vdsm</code></p>
<dd>Use vdsm to list virtual guests</p>
<dt><code>&#8211;esx</code></p>
<dd>Register ESX machines using vCenter</p>
<dt><code>&#8211;rhevm</code></p>
<dd>Register guests using RHEV-M</p>
<dt><code>&#8211;hyperv</code></p>
<dd>Register guests using Hyper-V</p>
<dt><code>&#8211;xen</code></p>
<dd>Register XEN machines using XenServer</p>
<dd></dl>
<h3>Subscription manager</h3>
<dl>
<dd>Choose where the host/guest associations should be reported</p>
<dt><code>&#8211;sam</code></p>
<dd>Report host/guest associations to the Subscription Asset Manager or Satellite 6 [default]</p>
<dt><code>&#8211;satellite5</code></p>
<dd>Report host/guest associations to the Satellite 5 server</p>
<dd><code>&#8211;satellite6</code> Report host/guest associations to the Satellite 6 server</p>
<dd></dl>
<h3>Libvirt options</h3>
<dl>
<dd>Use this options with <code>&#8211;libvirt</code></p>
<dt><code>&#8211;libvirt-owner</code>=<i>OWNER</i></p>
<dd>Organization who has purchased subscriptions of the products, same as current system registration by default</p>
<dt><code>&#8211;libvirt-env</code>=<i>ENV</i></p>
<dd>Environment where the libvirt server belongs to, same as current system registration by default</p>
<dt><code>&#8211;libvirt-server</code>=<i>SERVER</i></p>
<dd>URL of the remote libvirt server to connect to, local server by default</p>
<dt><code>&#8211;libvirt-username</code>=<i>USERNAME</i></p>
<dd>Username for connecting to libvirt, username of current user by default</p>
<dt><code>&#8211;libvirt-password</code>=<i>PASSWORD</i></p>
<dd>Password for connecting to libvirt. This option doesn&#8217;t work with ssh transport (default), copy your public ssh key to the remote machine.</p>
<dd></dl>
<h3>vCenter/ESX options</h3>
<dl>
<dd>Use this options with <code>&#8211;esx</code></p>
<dt><code>&#8211;esx-owner</code>=<i>OWNER</i></p>
<dd>Organization who has purchased subscriptions of the products</p>
<dt><code>&#8211;esx-env</code>=<i>ENV</i></p>
<dd>Environment where the vCenter server belongs to</p>
<dt><code>&#8211;esx-server</code>=<i>SERVER</i></p>
<dd>URL of the vCenter server to connect to</p>
<dt><code>&#8211;esx-username</code>=<i>USERNAME</i></p>
<dd>Username for connecting to vCenter</p>
<dt><code>&#8211;esx-password</code>=<i>PASSWORD</i></p>
<dd>Password for connecting to vCenter</p>
<dd></dl>
<h3>RHEV-M options</h3>
<dl>
<dd>Use this options with <code>&#8211;rhevm</code></p>
<dt><code>&#8211;rhevm-owner</code>=<i>OWNER</i></p>
<dd>Organization who has purchased subscriptions of the products</p>
<dt><code>&#8211;rhevm-env</code>=<i>ENV</i></p>
<dd>Environment where the RHEV-M belongs to</p>
<dt><code>&#8211;rhevm-server</code>=<i>SERVER</i></p>
<dd>URL of the RHEV-M server to connect to</p>
<dt><code>&#8211;rhevm-username</code>=<i>USERNAME</i></p>
<dd>Username for connecting to RHEV-M</p>
<dt><code>&#8211;rhevm-password</code>=<i>PASSWORD</i></p>
<dd>Password for connecting to RHEV-M</p>
<dd></dl>
<h3>Hyper-V options</h3>
<dl>
<dd>Use this options with <code>&#8211;hyperv</code></p>
<dt><code>&#8211;hyperv-owner</code>=<i>OWNER</i></p>
<dd>Organization who has purchased subscriptions of the products</p>
<dt><code>&#8211;hyperv-env</code>=<i>ENV</i></p>
<dd>Environment where the Hyper-V belongs to</p>
<dt><code>&#8211;hyperv-server</code>=<i>SERVER</i></p>
<dd>URL of the Hyper-V server to connect to</p>
<dt><code>&#8211;hyperv-username</code>=<i>USERNAME</i></p>
<dd>Username for connecting to Hyper-V</p>
<dt><code>&#8211;hyperv-password</code>=<i>PASSWORD</i></p>
<dd>Password for connecting to Hyper-V</dl>
<h3>XenServer options</h3>
<dl>
<dd>Use this options with <code>&#8211;xen</code></p>
<dt><code>&#8211;xen-owner</code>=<i>OWNER</i></p>
<dd>Organization who has purchased subscriptions of the products</p>
<dt><code>&#8211;xen-env</code>=<i>ENV</i></p>
<dd>Environment where the XenServer belongs to</p>
<dt><code>&#8211;xen-server</code>=<i>SERVER</i></p>
<dd>URL of the XenServer server to connect to</p>
<dt><code>&#8211;xen-username</code>=<i>USERNAME</i></p>
<dd>Username for connecting to XenServer</p>
<dt><code>&#8211;xen-password</code>=<i>PASSWORD</i></p>
<dd>Password for connecting to XenServer</p>
<dd></dl>
<h3>Satellite 5 options:</h3>
<dl>
<dd>Use this options with <code>&#8211;satellite5</code></p>
<dt><code>&#8211;satellite-server</code>=<i>SAT_SERVER</p>
<dd>Satellite server URL</p>
<dt></i><code>&#8211;satellite-username</code>=<i>SAT_USERNAME</p>
<dd>Username for connecting to Satellite server</p>
<dt></i><code>&#8211;satellite-password</code>=<i>SAT_PASSWORD</p>
<dd>Password for connecting to Satellite server</dl>
<p> </i></p>
<h2>Environment</h2>
<p>virt-who also reads environmental variables. They have the same name as command line arguments but upper-cased, with underscore instead of dash and prefixed with VIRTWHO_ (e.g. VIRTWHO_ONE_SHOT). Empty variables are considered as disabled, non-empty as enabled</p>
<h2>Usage</h2>
<h3>Mode</h3>
<p>virt-who has three modes how it can run:</p>
<dl>
<dt>1. one-shot mode</p>
<dd># virt-who -o </p>
<p> In this mode virt-who just sends the host to guest association to the server once and then exits.</p>
<dt>2. interval mode</p>
<dd># virt-who </p>
<p> This is default mode. virt-who will listen to change events (if available) or do a polling with given interval, and will send the host to guest association when it changes. The default polling interval is 60 seconds and can be changed using &quot;-i INTERVAL&quot; (in seconds).</p>
<dt>3. print mode</p>
<dd># virt-who -p </p>
<p> This mode is similar to oneshot mode but the host to guest association is not send to server, but printed to standard output instead. </p>
</dl>
<h3>Virtualization Backend</h3>
<p>virt-who can use couple of virtualization backends.</p>
<dl>
<dt>1. libvirt</p>
<dd># virt-who </p>
<p> # virt-who &#8211;libvirt </p>
<p> Use libvirt as virtualization backend. This is default.</p>
<dd>NOTE: virt-who can monitor for events only in this mode.</p>
<dt>2. vdsm</p>
<dd># virt-who &#8211;vdsm </p>
<p> Use vdsm as virtualization backend.</p>
<dt>3. ESX</p>
<dd># virt-who &#8211;esx &#8211;esx-owner=ESX_OWNER &#8211;esx-env=ESX_ENV &#8211;esx-server=ESX_SERVER &#8211;esx-username=ESX_USERNAME &#8211;esx-password=ESX_PASSWORD </p>
<p> Use ESX (vCenter) as virtualization backend and specify option required to connect to ESX server. </p>
<dt>4. RHEV-M</p>
<dd># virt-who &#8211;rhevm &#8211;rhevm-owner=RHEVM_OWNER &#8211;rhevm-env=RHEVM_ENV &#8211;rhevm-server=RHEVM_SERVER &#8211;rhevm-username=RHEVM_USERNAME &#8211;rhevm-password=RHEVM_PASSWORD </p>
<p> Use RHEV-M as virtualization backend and specify option required to connect to RHEV-M server. </p>
<dt>5. Hyper-V</p>
<dd># virt-who &#8211;hyperv &#8211;hyperv-owner=HYPERV_OWNER &#8211;hyperv-env=HYPERV_ENV &#8211;hyperv-server=HYPERV_SERVER &#8211;hyperv-username=HYPERV_USERNAME &#8211;hyperv-password=HYPERV_PASSWORD </p>
<p> Use Hyper-V as virtualization backend and specify option required to connect to Hyper-V server. </p>
<dt>6. XenServer</p>
<dd># virt-who &#8211;xen &#8211;xen-owner=XEN_OWNER &#8211;xen-env=XEN_ENV &#8211;xen-server=XEN_SERVER &#8211;xen-username=XEN_USERNAME &#8211;xen-password=XEN_PASSWORD </p>
<p> Use Citrix XenServer as virtualization backend and specify option required to connect to XenServer server. </p>
<dt>7. Fake</p>
<dd>Fake virtualization backend fetches the host/guests association from file. This can be useful in environments where the hypervisor is not accessible by virt-who. It&#8217;s only available through configuration file, see <a href="/docs/linux/man/5-virt-who-config/">virt-who-config</a>(5) for details about configuration of this backend. </p>
</dl>
<h3>Subscription Manager</h3>
<p>virt-who can report host/guest associations to Subscription Asset Manager (SAM), to Satellite 5, or to Satellite 6.</p>
<dl>
<dt>1. Subscription Asset Manager or Satellite 6</p>
<dd># virt-who </p>
<p> # virt-who &#8211;sam </p>
<p> System must be registered using subscription-manager prior to using virt-who. Configuration for connecting to SAM is shared between subscription-manager and virt-who. This is default. </p>
<dt>2. Satellite 6</p>
<dd># virt-who &#8211;satellite6 </p>
<p> System must be registered using subscription-manager prior to using virt-who. Configuration for connecting to Satellite 6 is shared between subscription-manager and virt-who. </p>
<dt>2. Satellite 5</p>
<dd># virt-who &#8211;satellite5 &#8211;satellite-server=SAT_SERVER &#8211;satellite-username=SAT_USERNAME &#8211;satellite-password=SAT_PASSWORD </p>
<p> This option can&#8217;t be used for monitoring local guests, use rhn-virtualization-host instead. </p>
</dl>
<h2>Logging</h2>
<p>virt-who always writes error output to file /var/log/rhsm/rhsm.log. In all modes, excluding background (&quot;-b&quot;), it writes same output also to the standard error output. </p>
<p> virt-who can be started with option &quot;-d&quot; in all modes and with all backends. This option will enable verbose output with more information.</p>
<h2>Security</h2>
<p>Virt-who may present security concerns in some scenarios because it needs access to every hypervisor in the environment. To minimize security risk, virt-who is a network client, not a server. It only does outbound connections to find and register new hypervisors and does not need access to any virtual machines. To further reduce risk, deploy virt-who in a small virtual machine with a minimal installation and lock it down from any unsolicited inbound network connections. </p>
<p> Here is a list of ports that need to be open for different hypervisors: </p>
<p>&nbsp;<wbr>VMWare ESX/vCenter: 443/tcp<br />
&nbsp;<wbr>Hyper-V: 5985/tcp<br />
&nbsp;<wbr>RHEV-M: 443/tcp or 8443/tcp&nbsp;<wbr>(depending on version)<br />
&nbsp;<wbr>XenServer: 443/tcp<br />
&nbsp;<wbr>libvirt: depending on transport type, default&nbsp;<wbr>(for remote connections)&nbsp;<wbr>is qemu over ssh on port 22<br />
&nbsp;<wbr>local libvirt and vdsm use local connections and don&#8217;t need open ports </p>
<p> virt-who also needs to have access to Subscription Asset Manager, Satellite 5, or Satellite 6. Default port is 443/tcp. All the ports might be changed by system administrators. </p>
<p> Using the same network for machine running virt-who as for hypervisor management software instead of production VM networks is suggested.</p>
<h2>Author</h2>
<p>Radek Novacek &lt;rnovacek at redhat dot com&gt;</p>
