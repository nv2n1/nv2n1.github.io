---
title: "virt-xml(1)"
name: "virt-xml"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-xml/"
description: "virt-xml – Edit libvirt XML using command line options."
---

<h2 class="name">NAME</h2>
<p> virt-xml &#8211; Edit libvirt XML using command line options. </p>
<h2>SYNOPSIS</h2>
<p> <code>virt-xml</code> <font SIZE="-1">DOMAIN</font> XML-ACTION XML-OPTION [<font SIZE="-1">OUTPUT-OPTION</font>] [<font SIZE="-1">MISC-OPTIONS</font>] &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>virt-xml</code> is a command line tool for editing libvirt <font SIZE="-1">XML</font> using explicit command line options. See the <font SIZE="-1">EXAMPLES</font> section at the end of this document to jump right in. </p>
<p> Each <code>virt-xml</code> invocation requires 3 things: name of an existing domain to alter (or <font SIZE="-1">XML</font> passed on stdin), an action to on the <font SIZE="-1">XML,</font> and an <font SIZE="-1">XML</font> change to make. actions are one of: </p>
<p> &#8211;add-device: Append a new device definition to the <font SIZE="-1">XML</font> &#8211;remove-device: Remove an existing device definition &#8211;edit: Edit an existing <font SIZE="-1">XML</font> block &#8211;build-xml: Just build the requested <font SIZE="-1">XML</font> block and print it (no domain or input <font SIZE="-1">XML</font> are required here). </p>
<p> An <font SIZE="-1">XML</font> change is one instance of any of the <font SIZE="-1">XML</font> options provided by virt-xml, for example &#8211;disk or &#8211;boot. </p>
<p> <code>virt-xml</code> only allows one action and <font SIZE="-1">XML</font> pair per invocation. If you need to make multiple edits, invoke the command multiple times.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <font SIZE="-1">URI</font></p>
<dd>
<dt><code>&#8211;connect</code>=URI</p>
<dd> Connect to a non-default hypervisor. See <i><a href="/docs/linux/man/1-virt-install/">virt-install</a></i>(1) for details</p>
<dt><code>domain</code></p>
<dd> domain is the name, <font SIZE="-1">UUID,</font> or <font SIZE="-1">ID</font> of the existing <font SIZE="-1">VM.</font> This can be omitted if using &#8211;build-xml, or if <font SIZE="-1">XML</font> is passed on stdin. </p>
<p> When a domain is specified, the default output action is &#8211;define, even if the <font SIZE="-1">VM</font> is running. To update the running <font SIZE="-1">VM</font> configuration, add the &#8211;update option (but not all options/devices support updating the running <font SIZE="-1">VM</font> configuration). </p>
<p> If <font SIZE="-1">XML</font> is passed on stdin, the default output is &#8211;print-xml.</dl>
<h2>XML ACTIONS</h2>
<dl>
<dt><code>&#8211;edit</code> [<font SIZE="-1">EDIT-OPTIONS</font>]</p>
<dd> Edit the specified <font SIZE="-1">XML</font> block. EDIT-OPTIONS tell <code>virt-xml</code> which block to edit. The type of <font SIZE="-1">XML</font> that we are editing is decided by <font SIZE="-1">XML</font> option that is passed to <code>virt-xml</code>. So if &#8211;disk is passed, EDIT-OPTIONS select which &lt;disk&gt; block to edit. </p>
<p> Certain <font SIZE="-1">XML</font> options only ever map to a single <font SIZE="-1">XML</font> block, like &#8211;cpu, &#8211;security, &#8211;boot, &#8211;clock, and a few others. In those cases, <code>virt-xml</code> will not complain if a corresponding <font SIZE="-1">XML</font> block does not already exist, it will create it for you. </p>
<p> Most <font SIZE="-1">XML</font> options support a special value &#8216;clearxml=yes&#8217;. When combined with &#8211;edit, it will completely blank out the <font SIZE="-1">XML</font> block being edited before applying the requested changes. This allows completely rebuilding an <font SIZE="-1">XML</font> block. See <font SIZE="-1">EXAMPLES</font> for some usage. </p>
<p> EDIT-OPTIONS examples:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;edit</code></p>
<dd> &#8211;edit without any options implies &#8216;edit the first block&#8217;. So &#8216;&#8211;edit &#8211;disk <font SIZE="-1">DISK-OPTIONS</font>&#8216; means &#8216;edit the first &lt;disk&gt;&#8217;. </p>
<p> For the single <font SIZE="-1">XML</font> block options mentioned above, plain &#8216;&#8211;edit&#8217; without any options is what you always want to use.</p>
<dt><code>&#8211;edit</code> #</p>
<dd> Select the specified <font SIZE="-1">XML</font> block number. So &#8216;&#8211;edit 2 &#8211;disk <font SIZE="-1">DISK-OPTS</font>&#8216; means &#8216;edit the second &lt;disk&gt;&#8217;. This option only really applies for device <font SIZE="-1">XML.</font></p>
<dt><code>&#8211;edit</code> all</p>
<dd> Modify every <font SIZE="-1">XML</font> block of the <font SIZE="-1">XML</font> option type. So &#8216;&#8211;edit all &#8211;disk <font SIZE="-1">DISK-OPTS</font>&#8216; means &#8216;edit ever &lt;disk&gt; block&#8217;. This option only really applies for device <font SIZE="-1">XML.</font></p>
<dt><code>&#8211;edit</code> DEVICE-OPTIONS</p>
<dd> Modify every <font SIZE="-1">XML</font> block that matches the passed device options. The device options are in the same format as would be passed to the <font SIZE="-1">XML</font> option. </p>
<p> So &#8216;&#8211;edit path=/tmp/foo &#8211;disk <font SIZE="-1">DISK-OPTS</font>&#8216; means &#8216;edit every &lt;disk&gt; with path /tmp/foo&#8217;. This option only really applies for device <font SIZE="-1">XML.</font></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt><code>&#8211;add-device</code></p>
<dd> Append the specified <font SIZE="-1">XML</font> options to the <font SIZE="-1">XML</font> &lt;devices&gt; list. Example: &#8216;&#8211;add-device &#8211;disk <font SIZE="-1">DISK-OPTIONS</font>&#8216; will create a new &lt;disk&gt; block and add it to the <font SIZE="-1">XML.</font> </p>
<p> This option will error if specified with a non-device <font SIZE="-1">XML</font> option (see &#8211;edit section for a partial list).</p>
<dt><code>&#8211;remove-device</code></p>
<dd> Remove the specified device from the <font SIZE="-1">XML.</font> The device to remove is chosen by the <font SIZE="-1">XML</font> option, which takes arguments in the same format as &#8211;edit. Examples</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;remove-device</code> &#8211;disk 2</p>
<dd> Remove the second disk device</p>
<dt><code>&#8211;remove-device</code> &#8211;network all</p>
<dd> Remove all network devices</p>
<dt><code>&#8211;remove-device</code> &#8211;sound pcspk</p>
<dd> Remove all sound devices with model=&#8217;pcspk&#8217;</dl>
</dl>
<dl>
<dt>
<dd>
<p> This option will error if specified with a non-device <font SIZE="-1">XML</font> option (see &#8211;edit section for a partial list).</dl>
<dt><code>&#8211;build-xml</code></p>
<dd> Just build the specified <font SIZE="-1">XML,</font> and print it to stdout. No input domain or input <font SIZE="-1">XML</font> is required. Example: &#8216;&#8211;build-xml &#8211;disk <font SIZE="-1">DISK-OPTIONS</font>&#8216; will just print the new &lt;disk&gt; device. </p>
<p> This option will error if specified with an <font SIZE="-1">XML</font> option that does not map cleanly to a specific <font SIZE="-1">XML</font> block, like &#8211;vcpus or &#8211;memory.</dl>
<h2>OUTPUT OPTIONS</h2>
<p> These options decide what action to take after altering the <font SIZE="-1">XML.</font> In the common case these do not need to be specified, as &#8216;<font SIZE="-1">XML</font> actions&#8217; will imply a default output action, described in detail above. These are only needed if you want to modify the default output.</p>
<dl>
<dt><code>&#8211;update</code></p>
<dd> If the specified domain is running, attempt to alter the running <font SIZE="-1">VM</font> configuration. If combined with &#8211;edit, this is an update operation. If combined with &#8211;add-device, this is a device hotplug. If combined with &#8211;remove-device, this is a device hotunplug. </p>
<p> Keep in mind, most <font SIZE="-1">XML</font> properties and devices do not support live update operations, so don&#8217;t expect it to succeed in all cases.</p>
<dt><code>&#8211;define</code></p>
<dd> Define the requested <font SIZE="-1">XML</font> change. This is typically the default if no output option is specified, but if a &#8211;print option is specified, &#8211;define is required to force the change.</p>
<dt><code>&#8211;print-diff</code></p>
<dd> Print the generated <font SIZE="-1">XML</font> change in unified diff format. If only this output option is specified, all other output options are disabled and no persistent change is made.</p>
<dt><code>&#8211;print-xml</code></p>
<dd> Print the generated <font SIZE="-1">XML</font> in its entirety. If only this output option is specified, all other output options are disabled and no persistent change is made.</p>
<dt><code>&#8211;confirm</code></p>
<dd> Before defining or updating the domain, show the generated <font SIZE="-1">XML</font> diff and interactively request confirmation.</dl>
<h2>XML OPTIONS</h2>
<dl>
<dt><code>&#8211;disk</code></p>
<dd>
<dt><code>&#8211;network</code></p>
<dd>
<dt><code>&#8211;graphics</code></p>
<dd>
<dt><code>&#8211;metadata</code></p>
<dd>
<dt><code>&#8211;memory</code></p>
<dd>
<dt><code>&#8211;vcpus</code></p>
<dd>
<dt><code>&#8211;cpu</code></p>
<dd>
<dt><code>&#8211;security</code></p>
<dd>
<dt><code>&#8211;numatune</code></p>
<dd>
<dt><code>&#8211;features</code></p>
<dd>
<dt><code>&#8211;clock</code></p>
<dd>
<dt><code>&#8211;pm</code></p>
<dd>
<dt><code>&#8211;boot</code></p>
<dd>
<dt><code>&#8211;filesystem</code></p>
<dd>
<dt><code>&#8211;controller</code></p>
<dd>
<dt><code>&#8211;input</code></p>
<dd>
<dt><code>&#8211;serial</code></p>
<dd>
<dt><code>&#8211;parallel</code></p>
<dd>
<dt><code>&#8211;channel</code></p>
<dd>
<dt><code>&#8211;console</code></p>
<dd>
<dt><code>&#8211;hostdev</code></p>
<dd>
<dt><code>&#8211;sound</code></p>
<dd>
<dt><code>&#8211;watchdog</code></p>
<dd>
<dt><code>&#8211;video</code></p>
<dd>
<dt><code>&#8211;smartcard</code></p>
<dd>
<dt><code>&#8211;redirdev</code></p>
<dd>
<dt><code>&#8211;memballoon</code></p>
<dd>
<dt><code>&#8211;tpm</code></p>
<dd>
<dt><code>&#8211;rng</code></p>
<dd>
<dt><code>&#8211;panic</code></p>
<dd> These options alter the <font SIZE="-1">XML</font> for a single class of <font SIZE="-1">XML</font> elements. More complete documentation is found in <i><a href="/docs/linux/man/1-virt-install/">virt-install</a></i>(1). </p>
<p> Generally these options map pretty straightforwardly to the libvirt <font SIZE="-1">XML,</font> documented at &lt;<a rel="nofollow" href="http://libvirt.org/formatdomain.html">http://libvirt.org/formatdomain.html</a>&gt; </p>
<p> Option strings are in the format of: &#8211;option opt=val,opt2=val2,&#8230; example: &#8211;disk path=/tmp/foo,shareable=on. Properties can be used with &#8216;&#8211;option opt=,&#8217;, so to clear a disks cache setting you could use &#8216;&#8211;disk cache=,&#8217; </p>
<p> For any option, use &#8211;option=? to see a list of all available sub options, example: &#8211;disk=? or &#8211;boot=? </p>
<p> &#8211;help output also lists a few general examples. See the <font SIZE="-1">EXAMPLES</font> section below for some common examples.</dl>
<h2>MISCELLANEOUS OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd>
<dt><code>&#8211;help</code></p>
<dd> Show the help message and exit</p>
<dt><code>&#8211;version</code></p>
<dd> Show program&#8217;s version number and exit</p>
<dt><code>-q</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Avoid verbose output.</p>
<dt><code>-d</code></p>
<dd>
<dt><code>&#8211;debug</code></p>
<dd> Print debugging information</dl>
<h2>EXAMPLES</h2>
<p> See a list of all suboptions that &#8211;disk and &#8211;network take </p>
<pre>
  # virt-xml --disk=? --network=?
</pre>
<p> Change the &lt;description&gt; of domain &#8216;<font SIZE="-1">EXAMPLE</font>&#8216;: </p>
<pre>
  # virt-xml EXAMPLE --edit --metadata description=&quot;my new description&quot;
</pre>
<p> # Enable the boot device menu for domain &#8216;<font SIZE="-1">EXAMPLE</font>&#8216;: </p>
<pre>
  # virt-xml EXAMPLE --edit --boot menu=on
</pre>
<p> Clear the previous &lt;cpu&gt; definition of domain &#8216;winxp&#8217;, change it to &#8216;host-model&#8217;, but interactively confirm the diff before saving: </p>
<pre>
  # virt-xml winxp --edit --cpu host-model,clearxml=yes --confirm
</pre>
<p> Change the second sound card to model=ich6 on &#8216;fedora19&#8217;, but only output the diff: </p>
<pre>
  # virt-xml fedora19 --edit 2 --sound model=ich6 --print-diff
</pre>
<p> Update the every graphics device password to &#8216;foo&#8217; of the running <font SIZE="-1">VM </font>&#8216;rhel6&#8217;: </p>
<pre>
  # virt-xml rhel6 --edit all --graphics password=foo --update
</pre>
<p> Remove the disk path from disk device hdc: </p>
<pre>
  # virt-xml rhel6 --edit target=hdc --disk path=
</pre>
<p> Change all disk devices of type &#8216;disk&#8217; to use cache=none, using <font SIZE="-1">XML</font> from stdin, printing the new <font SIZE="-1">XML</font> to stdout. </p>
<pre>
  # cat &lt;xmlfile&gt; | virt-xml --edit device=disk --disk cache=none
</pre>
<p> Change disk &#8216;hda&#8217; <font SIZE="-1">IO</font> to native and use startup policy as &#8216;optional&#8217;. </p>
<pre>
  # virt-xml fedora20 --edit target=hda \
             --disk io=native,startup_policy=optional
</pre>
<p> Change all host devices to use driver_name=vfio for <font SIZE="-1">VM </font>&#8216;fedora20&#8217; on the remote connection </p>
<pre>
  # virt-xml --connect qemu+<a href="ssh://remotehost/system">ssh://remotehost/system</a> \
             fedora20 --edit all --hostdev driver_name=vfio
</pre>
<p> Hotplug host <font SIZE="-1">USB</font> device 001.003 to running domain &#8216;fedora19&#8217;: </p>
<pre>
  # virt-xml fedora19 --update --add-device --hostdev 001.003
</pre>
<p> Add a spicevmc channel to the domain &#8216;winxp&#8217;, that will be available after the next <font SIZE="-1">VM</font> shutdown. </p>
<pre>
  # virt-xml winxp --add-device --channel spicevmc
</pre>
<p> Create a 10G qcow2 disk image and attach it to &#8216;fedora18&#8217; for the next <font SIZE="-1">VM</font> startup: </p>
<pre>
  # virt-xml fedora18 --add-device \
    --disk /var/lib/libvirt/images/newimage.qcow2,format=qcow2,size=10
</pre>
<p> Hotunplug the disk vdb from the running domain &#8216;rhel7&#8217;: </p>
<pre>
  # virt-xml rhel7 --update --remove-device --disk target=vdb
</pre>
<p> Remove all graphics devices from the <font SIZE="-1">VM </font>&#8216;rhel7&#8217; after the next shutdown: </p>
<pre>
  # virt-xml rhel7 --remove-device --graphics all
</pre>
<p> Generate <font SIZE="-1">XML</font> for a virtio console device and print it to stdout: </p>
<pre>
  # virt-xml --build-xml --console pty,target_type=virtio
</pre>
<h2>BUGS</h2>
<p> Please see <a rel="nofollow" href="http://virt-manager.org/page/BugReporting">http://virt-manager.org/page/BugReporting</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) Red Hat, Inc, and various contributors. This is free software. You may redistribute copies of it under the terms of the <font SIZE="-1">GNU</font> General Public License <tt>&quot;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&quot;</tt>. There is <font SIZE="-1">NO WARRANTY,</font> to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virt-install/">virt-install</a></i>(1), the project website <tt>&quot;<a rel="nofollow" href="http://virt-manager.org">http://virt-manager.org</a>&quot;</tt> </p>
<h2>Index</h2>
