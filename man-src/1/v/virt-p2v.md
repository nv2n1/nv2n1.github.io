---
title: "virt-p2v(1)"
name: "virt-p2v"
section: "1"
letter: "v"
url: "/docs/linux/man/1-virt-p2v/"
description: "virt-p2v – Convert a physical machine to use KVM"
---

<h2 class="name">NAME</h2>
<p> virt-p2v &#8211; Convert a physical machine to use KVM </p>
<h2>SYNOPSIS</h2>
<pre>
 virt-p2v
 virt-p2v.iso
</pre>
<h2>DESCRIPTION</h2>
<p> Virt-p2v converts a physical machine to run virtualized on <font SIZE="-1">KVM,</font> managed by libvirt, OpenStack, oVirt, Red Hat Enterprise Virtualisation (<font SIZE="-1">RHEV</font>), or one of the other targets supported by <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1). </p>
<p> Normally you don&#8217;t run the virt-p2v program directly. Instead you have to boot the physical machine using the bootable CD-ROM, <font SIZE="-1">ISO</font> or <font SIZE="-1">PXE</font> image. This bootable image contains the virt-p2v binary and runs it automatically. Booting from a CD-ROM/etc is required because the disks which are being converted must be quiescent. It is not safe to try to convert a running physical machine where other programs may be modifying the disk content at the same time. </p>
<p> This manual page documents running the virt-p2v program. To create the bootable image you should look at <i><a href="/docs/linux/man/1-virt-p2v-make-disk/">virt-p2v-make-disk</a></i>(1) or <i><a href="/docs/linux/man/1-virt-p2v-make-kickstart/">virt-p2v-make-kickstart</a></i>(1).</p>
<h2>NETWORK SETUP</h2>
<p> Virt-p2v runs on the physical machine which you want to convert. It has to talk to another server called the &#8220;conversion server&#8221; which must have <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1) installed on it. It always talks to the conversion server over <font SIZE="-1">SSH:</font> </p>
<pre>
 ┌──────────────┐                  ┌─────────────────┐
 │ virt-p2v     │                  │ virt-v2v        │
 │ (physical    │  ssh connection  │ (conversion     │
 │  server)   ╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍&#x25b6; server)       │
 └──────────────┘                  └─────────────────┘
</pre>
<p> The virt-v2v program on the conversion server does the actual conversion (physical to virtual, and virtual to virtual conversions are sufficiently similar that we use the same program to do both). </p>
<p> The <font SIZE="-1">SSH</font> connection is always initiated from the physical server. All data is transferred over the <font SIZE="-1">SSH</font> connection. In terms of firewall and network configuration, you only need to ensure that the physical server has access to a port (usually <font SIZE="-1">TCP</font> port 22) on the conversion server. Note that the physical machine may reconnect several times during the conversion process. </p>
<p> The reverse port forwarding feature of ssh (ie. <tt>&quot;ssh -R&quot;</tt>) is required by virt-p2v, and it will not work if this is disabled on the conversion server. (<tt>&quot;AllowTcpForwarding&quot;</tt> must be <tt>&quot;yes&quot;</tt> in the <i><a href="/docs/linux/man/5-sshd_config/">sshd_config</a></i>(5) file on the conversion server). </p>
<p> The scp (secure copy) feature of ssh is required by virt-p2v so it can send over small files (this is <i>not</i> the method by which disks are copied). </p>
<p> The conversion server does not need to be a physical machine. It could be a virtual machine, as long as it has sufficient memory and disk space to do the conversion, and as long as the physical machine can connect directly to its <font SIZE="-1">SSH</font> port. (See also &#8220;<font SIZE="-1">RESOURCE REQUIREMENTS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1)). </p>
<p> Because all of the data on the physical server&#8217;s hard drive(s) has to be copied over the network, the speed of conversion is largely determined by the speed of the network between the two machines.</p>
<h2>GUI INTERACTIVE CONFIGURATION</h2>
<p> When you start virt-p2v, you&#8217;ll see a graphical configuration dialog that walks you through connection to the conversion server, asks for the password, which local hard disks you want to convert, and other things like the name of the guest to create and the number of virtual CPUs to give it.</p>
<h3><font SIZE="-1">SSH CONFIGURATION DIALOG</font></h3>
<p> When virt-p2v starts up in <font SIZE="-1">GUI</font> mode, the first dialog looks like this: </p>
<pre><code>
┌────────────────────────────────────────────────────────┐
 │ virt - p2v                          │
 │                                                        │
 │ Conversion server : [_______________________] : [22___] │
 │                                                        │
 │ User name : [root_____________________________] │
 │                                                        │
 │ Password : [_________________________________] │
 │                                                        │
 │ SSH Identity URL : [_________________________________] │
 │                                                        │
</code></pre>
<p> In the fields above, you must enter the details of the conversion server: the hostname, <font SIZE="-1">SSH</font> port number, remote user name, and either the password or <font SIZE="-1">SSH</font> identity (private key) <font SIZE="-1">URL. </font> The conversion server must have an up to date version of virt-v2v. </p>
<p> Normally you must log in to the conversion server as root, but if you check the following box: </p>
<pre>
 │                                                        │
 │                    [ ] Use sudo when running virt-v2v  │
 │                                                        │
</pre>
<p> then you can log in as another user, and virt-p2v will use the <i><a href="/docs/linux/man/8-sudo/">sudo</a></i>(8) command to elevate privileges to root. Note that sudo must not require a password. </p>
<p> It is also possible to run virt-v2v on the conversion server entirely as non-root, but output modes may be limited. Consult the <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1) manual page for details. </p>
<p> At the bottom of the dialog are these buttons: </p>
<p>│                                                        │<br />
 │ [Test connection]                     │<br />
 │                                                        │<br />
 │ [Configure network][About virt &#8211; p2v][Next] │<br />
 │                                                        │<br />
 └────────────────────────────────────────────────────────┘</p>
<p> You must press the <tt>&quot;Test connection&quot;</tt> button first to test the <font SIZE="-1">SSH</font> connection to the conversion server. If that is successful (ie. you have supplied the correct server name, user name, password, etc., and a suitable version of virt-v2v is available remotely) then press the <tt>&quot;Next&quot;</tt> button to move to the next dialog. </p>
<p> You can use the <tt>&quot;Configure network&quot;</tt> button if you need to assign a static <font SIZE="-1">IP</font> address to the physical machine, or use Wifi, bonding or other network features.</p>
<h3><font SIZE="-1">DISK AND NETWORK CONFIGURATION DIALOG</font></h3>
<p> The second configuration dialog lets you configure the details of conversion, including what to convert and where to send the guest. </p>
<p> In the left hand column, starting at the top, the target properties let you select the name of the guest (ie. after conversion) and how many virtual CPUs and how much <font SIZE="-1">RAM</font> to give it. The defaults come from the physical machine, and you can usually leave them unchanged: </p>
<p>┌─────────────────────────────────────── ─ ─ ─ ─<br />
 │ Target properties :<br />
 │<br />
 │ Name : [hostname______________]<br />
 │<br />
 │ #vCPUs : [4_____________________]<br />
 │<br />
 │ Memory(MB)<br />
    : [16384_________________]<br />
 │</p>
<p> The second panel on the left controls the virt-v2v output options. To understand these options it is a really good idea to read the <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1) manual page. You can leave the options at the default to create a guest as a disk image plus libvirt <font SIZE="-1">XML</font> file located in <i>/var/tmp</i> on the conversion host. This is a good idea if you are a first-time virt-p2v user. </p>
<p>│<br />
 │ Virt &#8211; v2v output options :<br />
 │<br />
 │ Output to(-o)<br />
    : [local             ▼]<br />
 │<br />
 │ Output conn.(-oc)<br />
    : [___________________]<br />
 │<br />
 │ Output storage(-os)<br />
    : [/ var / tmp___________]<br />
 │<br />
 │ Output format(-of)<br />
    : [___________________]<br />
 │<br />
 │ Output allocation(-oa)<br />
    : [sparse            ▼]<br />
 │</p>
<p> All output options and paths are relative to the conversion server (<i>not</i> to the physical server). </p>
<p> Finally in the left hand column is an information box giving the version of virt-p2v (on the physical server) and virt-v2v (on the conversion server). You should supply this information when reporting bugs. </p>
<p> In the right hand column are three panels which control what hard disks, removable media devices, and network interfaces, will be created in the output guest. Normally leaving these at the default settings is fine. </p>
<p>─ ─ ───────────────────────────────────────┐ Fixed hard disks                       │<br />
                                            │ Convert Device                        │<br />
        [&#x2714;] sda                           │ 1024G HITACHI                 │ s /<br />
    n 12345                     │<br />
        [&#x2714;] sdb                           │ 119G HITACHI                  │ s /<br />
    n 12346                     │<br />
                                            │</p>
<p> Normally you would want to convert all hard disks. If you want virt-p2v to completely ignore a local hard disk, uncheck it. The hard disk that contains the operating system must be selected. If a hard disk is part of a <font SIZE="-1">RAID</font> array or <font SIZE="-1">LVM</font> volume group (<font SIZE="-1">VG</font>), then either all hard disks in that array/VG must be selected, or none of them. </p>
<pre>
                                            │
     Removable media                        │
                                            │
     Convert  Device                        │
     [&#x2714;]      sr0                           │
                                            │
</pre>
<p> If the physical machine has <font SIZE="-1">CD</font> or <font SIZE="-1">DVD</font> drives, then you can use the Removable media panel to create corresponding drives on the guest after conversion. Note that any data CDs/DVDs which are mounted in the drives are <i>not</i> copied over. </p>
<p>│ Network interfaces                     │<br />
                                            │ Convert Device Connect to&#8230; |<br />
    [&#x2714;] em1[default_____________] │<br />
        [] wlp3s0[default_____________] │<br />
                                            │</p>
<p> In the Network interfaces panel, select the network interfaces that should be created in the guest after conversion. You can also connect these to target hypervisor networks (for further information about this feature, see &#8220;<font SIZE="-1">NETWORKS AND BRIDGES&#8221;</font> in <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1)). </p>
<p> On supported hardware, left-clicking on the device name (eg. <tt>&quot;em1&quot;</tt>) causes a light to start flashing on the physical interface, allowing the interface to be identified by the operator. </p>
<p> When you are ready to begin the conversion, press the <tt>&quot;Start conversion&quot;</tt> button: </p>
<p>│<br />
    [Back][Start conversion] │<br />
                                            │<br />
 ─ ─ ───────────────────────────────────────┘</p>
<h3><font SIZE="-1">CONVERSION RUNNING DIALOG</font></h3>
<p> When conversion is running you will see this dialog: </p>
<pre>
 ┌────────────────────────────────────────────────────────┐
 │                      virt-p2v                          │
 │                                                        │
 │  ┌──────────────────────────────────────────────────┐  │
 │  │                                                 ▲│  │
 │  │                                                  │  │
 │  │                                                  │  │
 ∼  ∼                                                  ∼  ∼
 │  │                                                  │  │
 │  │                                                  │  │
 │  │                                                 ▼│  │
 │  └──────────────────────────────────────────────────┘  │
 │                                                        │
 │ Log files ... to /tmp/virt-p2v-xxx                     │
 │                                                        │
 │ Doing conversion ...                                   │
 │                                                        │
 │                                 [ Cancel conversion ]  │
 │                                                        │
 └────────────────────────────────────────────────────────┘
</pre>
<p> In the main scrolling area you will see messages from the virt-v2v process. </p>
<p> Below the main area, virt-p2v shows you the location of the directory on the conversion server that contains log files and other debugging information. Below that is the current status and a button for cancelling conversion. </p>
<p> Once conversion has finished, you should shut down the physical machine. If conversion is successful, you should never reboot it.</p>
<h2>KERNEL COMMAND LINE CONFIGURATION</h2>
<p> If you don&#8217;t want to configure things using the graphical <font SIZE="-1">UI,</font> an alternative is to configure through the kernel command line. This is especially convenient if you are converting a lot of physical machines which are booted using <font SIZE="-1">PXE.</font> </p>
<p> Where exactly you set command line arguments depends on your <font SIZE="-1">PXE</font> implementation, but for pxelinux you put them in the <tt>&quot;APPEND&quot;</tt> field in the <i>pxelinux.cfg</i> file. For example: </p>
<pre>
 DEFAULT p2v
 TIMEOUT 20
 PROMPT 0
 LABEL p2v
   KERNEL vmlinuz0
   APPEND initrd=initrd0.img [....] p2v.server=conv.example.com p2v.password=secret p2v.o=libvirt
</pre>
<p> You have to set some or all of the following command line arguments:</p>
<dl>
<dt><code>p2v.server=SERVER</code></p>
<dd> The name or <font SIZE="-1">IP</font> address of the conversion server. </p>
<p> This is always required if you are using the kernel configuration method. If virt-p2v does not find this on the kernel command line then it switches to the <font SIZE="-1">GUI </font>(interactive) configuration method.</p>
<dt><code>p2v.port=NN</code></p>
<dd> The <font SIZE="-1">SSH</font> port number on the conversion server (default: <tt>22</tt>).</p>
<dt><code>p2v.username=USERNAME</code></p>
<dd> The <font SIZE="-1">SSH</font> username that we log in as on the conversion server (default: <tt>&quot;root&quot;</tt>).</p>
<dt><code>p2v.password=PASSWORD</code></p>
<dd> The <font SIZE="-1">SSH</font> password that we use to log in to the conversion server. </p>
<p> The default is to try with no password. If this fails then virt-p2v will ask the user to type the password (probably several times during conversion). </p>
<p> This setting is ignored if <tt>&quot;p2v.identity&quot;</tt> is present.</p>
<dt><code>p2v.identity=URL</code></p>
<dd> Provide a <font SIZE="-1">URL</font> pointing to an <font SIZE="-1">SSH</font> identity (private key) file. The <font SIZE="-1">URL</font> is interpreted by <i><a href="/docs/linux/man/1-curl/">curl</a></i>(1) so any <font SIZE="-1">URL</font> that curl supports can be used here, including <tt>&quot;https://&quot;</tt> and <tt>&quot;file://&quot;</tt>. For more information on using <font SIZE="-1">SSH</font> identities, see &#8220;<font SIZE="-1">SSH IDENTITIES&#8221;</font> below. </p>
<p> If <tt>&quot;p2v.identity&quot;</tt> is present, it overrides <tt>&quot;p2v.password&quot;</tt>. There is no fallback.</p>
<dt><code>p2v.sudo</code></p>
<dd> Use <tt>&quot;p2v.sudo&quot;</tt> to tell virt-p2v to use <i><a href="/docs/linux/man/8-sudo/">sudo</a></i>(8) to gain root privileges on the conversion server after logging in as a non-root user (default: do not use sudo).</p>
<dt><code>p2v.name=GUESTNAME</code></p>
<dd> The name of the guest that is created. The default is to try to derive a name from the physical machine&#8217;s hostname (if possible) else use a randomly generated name.</p>
<dt><code>p2v.vcpus=NN</code></p>
<dd> The number of virtual CPUs to give to the guest. The default is to use the same as the number of physical CPUs.</p>
<dt><code>p2v.memory=NN(M|G)</code></p>
<dd> The size of the guest memory. You must specify the unit as either megabytes or gigabytes by using (eg) <tt>&quot;p2v.memory=1024M&quot;</tt> or <tt>&quot;p2v.memory=1G&quot;</tt>. </p>
<p> The default is to use the same amount of <font SIZE="-1">RAM</font> as on the physical machine.</p>
<dt><code>p2v.disks=sdX,sdY,..</code></p>
<dd> A list of physical hard disks to convert, for example: </p>
<pre>
 p2v.disks=sda,sdc
</pre>
<p> The default is to convert all local hard disks that are found.</p>
<dt><code>p2v.removable=srX,srY,..</code></p>
<dd> A list of removable media to convert. The default is to create virtual removable devices for every physical removable device found. Note that the content of removable media is never copied over.</p>
<dt><code>p2v.interfaces=em1,..</code></p>
<dd> A list of network interfaces to convert. The default is to create virtual network interfaces for every physical network interface found.</p>
<dt><code>p2v.network=interface:target,&#8230;</code></p>
<dd> Controls how network interfaces are connected to virtual networks on the target hypervisor. The default is to connect all network interfaces to the target <tt>&quot;default&quot;</tt> network. </p>
<p> You give a comma-separated list of <tt>&quot;interface:target&quot;</tt> pairs, plus optionally a default target. For example: </p>
<pre>
 p2v.network=em1:rhevm
</pre>
<p> maps interface <tt>&quot;em1&quot;</tt> to target network <tt>&quot;rhevm&quot;</tt>. </p>
<pre>
 p2v.network=em1:rhevm,em2:management,other
</pre>
<p> maps interface <tt>&quot;em1&quot;</tt> to <tt>&quot;rhevm&quot;</tt>, and <tt>&quot;em2&quot;</tt> to <tt>&quot;management&quot;</tt>, and any other interface that is found to <tt>&quot;other&quot;</tt>.</p>
<dt><code>p2v.o=[libvirt|local|&#8230;]</code></p>
<dd> Set the output mode. This is the same as the virt-v2v <i>-o</i> option. See &#8220;<font SIZE="-1">OPTIONS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1). </p>
<p> If not specified, the default is <tt>&quot;local&quot;</tt>, and the converted guest is written to <i>/var/tmp</i>.</p>
<dt><code>p2v.oa=sparse|preallocated</code></p>
<dd> Set the output allocation mode. This is the same as the virt-v2v <i>-oa</i> option. See &#8220;<font SIZE="-1">OPTIONS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1).</p>
<dt><code>p2v.oc=&#8230;</code></p>
<dd> Set the output connection libvirt <font SIZE="-1">URI. </font> This is the same as the virt-v2v <i>-oc</i> option. See &#8220;<font SIZE="-1">OPTIONS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1) and <a rel="nofollow" href="http://libvirt.org/uri.html">http://libvirt.org/uri.html</a></p>
<dt><code>p2v.of=raw|qcow2|&#8230;</code></p>
<dd> Set the output format. This is the same as the virt-v2v <i>-of</i> option. See &#8220;<font SIZE="-1">OPTIONS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1).</p>
<dt><code>p2v.os=&#8230;</code></p>
<dd> Set the output storage. This is the same as the virt-v2v <i>-os</i> option. See &#8220;<font SIZE="-1">OPTIONS&#8221;</font> in <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1). </p>
<p> If not specified, the default is <i>/var/tmp</i> (on the conversion server).</p>
<dt><code>p2v.pre=COMMAND</code></p>
<dd>
<dt><code>p2v.pre=&quot;</code><font SIZE="-1"><code>COMMAND ARG &#8230;&quot;</code></font></p>
<dd> Select a pre-conversion command to run. Any command or script can be specified here. If the command contains spaces, you must quote the whole command with double quotes. The default is not to run any command.</p>
<dt><code>p2v.post=poweroff</code></p>
<dd>
<dt><code>p2v.post=reboot</code></p>
<dd>
<dt><code>p2v.post=COMMAND</code></p>
<dd>
<dt><code>p2v.post=&quot;</code><font SIZE="-1"><code>COMMAND ARG &#8230;&quot;</code></font></p>
<dd> Select a post-conversion command to run if conversion is successful. This can be any command or script. If the command contains spaces, you must quote the whole command with double quotes. </p>
<p> <i>If</i> virt-p2v is running as root, <i>and</i> the command line was set from <i>/proc/cmdline</i> (not <i>&#8211;cmdline</i>), then the default is to run the <i><a href="/docs/linux/man/8-poweroff/">poweroff</a></i>(8) command. Otherwise the default is not to run any command.</p>
<dt><code>p2v.fail=COMMAND</code></p>
<dd>
<dt><code>p2v.fail=&quot;</code><font SIZE="-1"><code>COMMAND ARG &#8230;&quot;</code></font></p>
<dd> Select a post-conversion command to run if conversion fails. Any command or script can be specified here. If the command contains spaces, you must quote the whole command with double quotes. The default is not to run any command.</p>
<dt><code>ip=dhcp</code></p>
<dd> Use <font SIZE="-1">DHCP</font> for configuring the network interface (this is the default).</dl>
<h2>SSH IDENTITIES</h2>
<p> As a somewhat more secure alternative to password authentication, you can use an <font SIZE="-1">SSH</font> identity (private key) for authentication. </p>
<p> First create a key pair. It must have an empty passphrase: </p>
<pre>
 ssh-keygen -t rsa -N '' -f id_rsa
</pre>
<p> This creates a private key (<tt>&quot;id_rsa&quot;</tt>) and a public key (<tt>&quot;id_rsa.pub&quot;</tt>) pair. </p>
<p> The public key should be appended to the <tt>&quot;authorized_keys&quot;</tt> file on the virt-v2v conversion server (usually to <tt>&quot;/root/.ssh/authorized_keys&quot;</tt>). </p>
<p> For distributing the private key, there are four scenarios from least secure to most secure:</p>
<dl>
<dt>1.</p>
<dd> Not using <font SIZE="-1">SSH</font> identities at all, ie. password authentication. </p>
<p> Anyone who can sniff the <font SIZE="-1">PXE</font> boot parameters from the network or observe the password some other way can log in to the virt-v2v conversion server.</p>
<dt>2.</p>
<dd> <font SIZE="-1">SSH</font> identity embedded in the virt-p2v <font SIZE="-1">ISO</font> or disk image. In the <font SIZE="-1">GUI,</font> use: </p>
<p> │          Password: [    &lt;leave this field blank&gt;       ] │<br />
 │                                                          │<br />
 │  SSH Identity URL: [file:///var/tmp/id_rsa_____________] │</p>
<p> or on the kernel command line: </p>
<pre>
 p2v.identity=file:///var/tmp/id_rsa
</pre>
<p> The <font SIZE="-1">SSH</font> private key can still be sniffed from the network if using standard <font SIZE="-1">PXE.</font></p>
<dt>3.</p>
<dd> <font SIZE="-1">SSH</font> identity downloaded from a website. In the <font SIZE="-1">GUI,</font> use: </p>
<pre><code>
 │          Password: [    &lt;leave this field blank&gt;       ] │
 │                                                          │
 │  SSH Identity URL: [https://internal.example.com/id_rsa] │
</code></pre>
<p> or on the kernel command line: </p>
<pre>
 p2v.identity=<a rel="nofollow" href="https://internal.example.com/id_rsa">https://internal.example.com/id_rsa</a>
</pre>
<p> Anyone could still download the private key and use it to log in to the virt-v2v conversion server, but you could provide some extra security by configuring the web server to only allow connections from P2V machines. </p>
<p> Note that <i><a href="/docs/linux/man/1-ssh-keygen/">ssh-keygen</a></i>(1) creates the <tt>&quot;id_rsa&quot;</tt> (private key) file with mode 0600. If you simply copy the file to a webserver, the webserver will not serve it. It will reply with &#8220;403 Forbidden&#8221; errors. You will need to change the mode of the file to make it publicly readable, for example by using: </p>
<pre>
 chmod 0644 id_rsa
</pre>
<dt>4.</p>
<dd> <font SIZE="-1">SSH</font> identity embedded in the virt-p2v <font SIZE="-1">ISO</font> or disk image (like 2.), <i>and</i> use of secure <font SIZE="-1">PXE, PXE</font> over separate physical network, or sneakernet to distribute virt-p2v to the physical machine.</dl>
<p> Both <i><a href="/docs/linux/man/1-virt-p2v-make-disk/">virt-p2v-make-disk</a></i>(1) and <i><a href="/docs/linux/man/1-virt-p2v-make-kickstart/">virt-p2v-make-kickstart</a></i>(1) have the same option <i>&#8211;inject-ssh-identity</i> for injecting the private key into the virt-p2v disk image / <font SIZE="-1">ISO. </font> See also the following manual sections: </p>
<p> &#8220;<font SIZE="-1">ADDING AN SSH IDENTITY&#8221;</font> in <i><a href="/docs/linux/man/1-virt-p2v-make-disk/">virt-p2v-make-disk</a></i>(1) </p>
<p> &#8220;<font SIZE="-1">ADDING AN SSH IDENTITY&#8221;</font> in <i><a href="/docs/linux/man/1-virt-p2v-make-kickstart/">virt-p2v-make-kickstart</a></i>(1)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display help.</p>
<dt><code>&#8211;cmdline=CMDLINE</code></p>
<dd> This is used for debugging. Instead of parsing the kernel command line from <i>/proc/cmdline</i>, parse the string parameter <tt>&quot;CMDLINE&quot;</tt>.</p>
<dt><code>&#8211;colors</code></p>
<dd>
<dt><code>&#8211;colours</code></p>
<dd> Use <font SIZE="-1">ANSI</font> colour sequences to colourize messages. This is the default when the output is a tty. If the output of the program is redirected to a file, <font SIZE="-1">ANSI</font> colour sequences are disabled unless you use this option.</p>
<dt><code>&#8211;iso</code></p>
<dd> This flag is passed to virt-p2v when it is launched inside the virt-p2v <font SIZE="-1">ISO</font> environment, ie. when it is running on a real physical machine (and thus not when testing). It enables various dangerous features such as the Reboot button.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> In libguestfs ≥ 1.33.41, debugging is always enabled on the conversion server, and this option does nothing.</p>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Display version number and exit.</dl>
<h2>HOW VIRT-P2V WORKS</h2>
<p> <code>Note this section is not normative.</code> We may change how virt-p2v works at any time in the future. </p>
<p> As described above, virt-p2v runs on a physical machine, interrogates the user or the kernel command line for configuration, and then establishes one or more ssh connections to the virt-v2v conversion server. The ssh connections are interactive shell sessions to the remote host, but the commands sent are generated entirely by virt-p2v itself, not by the user. For data transfer, virt-p2v will use the reverse port forward feature of ssh (ie. <tt>&quot;ssh -R&quot;</tt>). </p>
<p> It will first make one or more test connections, which are used to query the remote version of virt-v2v and its features. The test connections are closed before conversion begins. </p>
<pre>
 ┌──────────────┐                      ┌─────────────────┐
 │ virt-p2v     │                      │ virt-v2v        │
 │ (physical    │  control connection  │ (conversion     │
 │  server)   ╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍&#x25b6; server)       │
 └──────────────┘                      └─────────────────┘
</pre>
<p> Once virt-p2v is ready to start conversion, it will open a single ssh control connection. It first sends a mkdir command to create a temporary directory on the conversion server. The directory name is randomly chosen and is displayed in the <font SIZE="-1">GUI. </font> It has the form: </p>
<pre>
 /tmp/virt-p2v-YYYYMMDD-XXXXXXXX
</pre>
<p> where <tt>&quot;YYYYMMDD&quot;</tt> is the current date, and the X&#8217;s are random characters. </p>
<p> Into this directory are written various files which include:</p>
<dl>
<dt><i>dmesg</i></p>
<dd> <i>(before conversion)</i> </p>
<p> The dmesg output from the physical machine. Useful for detecting problems such as missing device drivers or firmware on the virt-p2v <font SIZE="-1">ISO.</font></p>
<dt><i>name</i></p>
<dd> <i>(before conversion)</i> </p>
<p> The name (usually the hostname) of the physical machine.</p>
<dt><i>physical.xml</i></p>
<dd> <i>(before conversion)</i> </p>
<p> Libvirt <font SIZE="-1">XML</font> describing the physical machine. It is used to pass data about the physical source host to <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1) via the <i>-i libvirtxml</i> option. </p>
<p> Note this is not &#8220;real&#8221; libvirt <font SIZE="-1">XML </font>(and must <code>never</code> be loaded into libvirt, which would reject it anyhow). Also it is not the same as the libvirt <font SIZE="-1">XML</font> which virt-v2v generates in certain output modes.</p>
<dt><i>status</i></p>
<dd> <i>(after conversion)</i> </p>
<p> The final status of the conversion. <tt>0</tt> if the conversion was successful. Non-zero if the conversion failed.</p>
<dt><i>time</i></p>
<dd> <i>(before conversion)</i> </p>
<p> The start date/time of conversion.</p>
<dt><i>virt-v2v-conversion-log.txt</i></p>
<dd> <i>(during/after conversion)</i> </p>
<p> The conversion log. This is just the output of the virt-v2v command on the conversion server. If conversion fails, you should examine this log file, and you may be asked to supply the <code>complete</code>, <code>unedited</code> log file in any bug reports or support tickets.</p>
<dt><i>virt-v2v-wrapper.sh</i></p>
<dd> <i>(during/after conversion)</i> </p>
<p> This is the wrapper script which is used when running virt-v2v. For interest only, do not attempt to run this script yourself.</dl>
<p> Before conversion actually begins, virt-p2v then makes one or more further ssh connections to the server for data transfer. The transfer protocol used currently is <font SIZE="-1">NBD </font>(Network Block Device), which is proxied over ssh. The server is <i><a href="/docs/linux/man/1-qemu-nbd/">qemu-nbd</a></i>(1). There is one ssh connection per physical hard disk on the source machine (the common case — a single hard disk — is shown below): </p>
<pre>
 ┌──────────────┐                      ┌─────────────────┐
 │ virt-p2v     │                      │ virt-v2v        │
 │ (physical    │  control connection  │ (conversion     │
 │  server)   ╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍&#x25b6; server)       │
 │              │                      │                 │
 │              │  data connection     │                 │
 │            ╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍&#x25b6;               │
 │qemu-nbd ← ─┘ │                      │└─ ← NBD         │
 │/dev/sda      │                      │     requests    │
 ∼              ∼                      ∼                 ∼
 └──────────────┘                      └─────────────────┘
</pre>
<p> Although the ssh data connection is originated from the physical server and terminates on the conversion server, in fact <font SIZE="-1">NBD</font> requests flow in the opposite direction. This is because the reverse port forward feature of ssh (<tt>&quot;ssh -R&quot;</tt>) is used to open a port on the loopback interface of the conversion server which is proxied back by ssh to the qemu-nbd server running on the physical machine. The effect is that virt-v2v via libguestfs can open nbd connections which directly read the hard disk(s) of the physical server. </p>
<p> Two layers of protection are used to ensure that there are no writes to the hard disks: Firstly, the qemu-nbd <i>-r</i> (readonly) option is used. Secondly libguestfs creates an overlay on top of the <font SIZE="-1">NBD</font> connection which stores writes in a temporary file on the conversion file. </p>
<p> The long <tt>&quot;virt-v2v -i libvirtxml physical.xml ...&quot;</tt> command is wrapped inside a wrapper script and uploaded to the conversion server. The final step is to run this wrapper script, in turn running the virt-v2v command. The virt-v2v command references the <i>physical.xml</i> file (see above), which in turn references the <font SIZE="-1">NBD</font> listening port(s) of the data connection(s). </p>
<p> Output from the virt-v2v command (messages, debugging etc) is saved both in the log file on the conversion server. Only informational messages are sent back over the control connection to be displayed in the graphical <font SIZE="-1">UI.</font></p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-virt-p2v-make-disk/">virt-p2v-make-disk</a></i>(1), <i><a href="/docs/linux/man/1-virt-p2v-make-kickstart/">virt-p2v-make-kickstart</a></i>(1), <i><a href="/docs/linux/man/1-virt-v2v/">virt-v2v</a></i>(1), <i><a href="/docs/linux/man/1-qemu-nbd/">qemu-nbd</a></i>(1), <i><a href="/docs/linux/man/1-ssh/">ssh</a></i>(1), <i><a href="/docs/linux/man/8-sshd/">sshd</a></i>(8), <i><a href="/docs/linux/man/5-sshd_config/">sshd_config</a></i>(5), <a rel="nofollow" href="http://libguestfs.org/.">http://libguestfs.org/.</a></p>
<h2>AUTHORS</h2>
<p> Matthew Booth </p>
<p> John Eckersberg </p>
<p> Richard W.M. Jones <a rel="nofollow" href="http://people.redhat.com/~rjones/">http://people.redhat.com/~rjones/</a> </p>
<p> Mike Latimer </p>
<p> Pino Toscano </p>
<p> Tingting Zheng</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2009-2016 Red Hat Inc.</p>
<h2>LICENSE</h2>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> General Public License for more details. </p>
<p> You should have received a copy of the <font SIZE="-1">GNU</font> General Public License along with this program; if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, <font SIZE="-1">MA 02110-1301 USA.</font></p>
<h2>BUGS</h2>
<p> To get a list of bugs against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/buglist.cgi?component=libguestfs">https://bugzilla.redhat.com/buglist.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> To report a new bug against libguestfs, use this link: <a rel="nofollow" href="https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs">https://bugzilla.redhat.com/enter_bug.cgi?component=libguestfs</a>&amp;product=Virtualization+Tools </p>
<p> When reporting a bug, please supply:</p>
<dl>
<dt>&bull;</p>
<dd> The version of libguestfs.</p>
<dt>&bull;</p>
<dd> Where you got libguestfs (eg. which Linux distro, compiled from source, etc)</p>
<dt>&bull;</p>
<dd> Describe the bug accurately and give a way to reproduce it.</p>
<dt>&bull;</p>
<dd> Run <i><a href="/docs/linux/man/1-libguestfs-test-tool/">libguestfs-test-tool</a></i>(1) and paste the <code>complete, unedited</code> output into the bug report. </p>
</dl>
<h2>Index</h2>
<dt><a href="#lbAJ">KERNEL COMMAND LINE CONFIGURATION</a></p>
<dd>
<dt><a href="#lbAK">SSH IDENTITIES</a></p>
<dd>
<dt><a href="#lbAL">OPTIONS</a></p>
<dd>
<dt><a href="#lbAM">HOW VIRT-P2V WORKS</a></p>
<dd>
<dt><a href="#lbAN">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAO">AUTHORS</a></p>
<dd>
<dt><a href="#lbAP">COPYRIGHT</a></p>
<dd>
<dt><a href="#lbAQ">LICENSE</a></p>
<dd>
<dt><a href="#lbAR">BUGS</a></p>
<dd></dl>
