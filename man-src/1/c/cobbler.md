---
title: "cobbler(1)"
name: "cobbler"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cobbler/"
description: "cobbler – a provisioning and update server"
---

<h2 class="name">NAME</h2>
<p> cobbler &#8211; a provisioning and update server </p>
<p> cobbler is a provisioning (installation) and update server. It supports deployments via PXE (network booting), virtualization (Xen, QEMU/KVM, or VMware), and re-installs of existing Linux systems. The latter two features are enabled by usage of &#8216;koan&#8217; on the remote system. Update server features include yum mirroring and integration of those mirrors with kickstart. Cobbler has a command line interface, Web UI, and extensive Python and XMLRPC APIs for integration with external scripts and applications. </p>
<h2>SYNOPSIS</h2>
<p> cobbler command [subcommand] [&#8211;arg1=value1] [&#8211;arg2=value2]</p>
<h2>DESCRIPTION</h2>
<p> Cobbler manages provisioning using a tiered concept of Distributions, Profiles, Systems, and (optionally) Images and Repositories. </p>
<p> Distributions contain information about what kernel and initrd are used, plus metadata (required kernel parameters, etc). </p>
<p> Profiles associate a Distribution with a kickstart file and optionally customize the metadata further. </p>
<p> Systems associate a <font SIZE="-1">MAC, IP,</font> and other networking details with a profile and optionally customize the metadata further. </p>
<p> Repositories contain yum mirror information. Using cobbler to mirror repositories is an optional feature, though provisioning and package management share a lot in common. </p>
<p> Images are a catch-all concept for things that do not play nicely in the &#8220;distribution&#8221; category. Most users will not need these records initially and these are described later in the document. </p>
<p> The main advantage of cobbler is that it glues together many disjoint technologies and concepts and abstracts the user from the need to understand them. It allows the systems administrator to concentrate on what he needs to do, and not how it is done. </p>
<p> This manpage will focus on the cobbler command line tool for use in configuring cobbler. There is also mention of the Cobbler WebUI which is usable for day-to-day operation of Cobbler once installed/configured. Docs on the <font SIZE="-1">API</font> and <font SIZE="-1">XMLRPC</font> components are available online at <a rel="nofollow" href="http://cobbler.github.io">http://cobbler.github.io</a> </p>
<p> Most users will be interested in the Web <font SIZE="-1">UI</font> and should set it up, though the command line is needed for initial configuration &#8212; in particular &#8220;cobbler check&#8221; and &#8220;cobbler import&#8221;, as well as the repo mirroring features. All of these are described later in the documentation.</p>
<h2>SEE ALSO</h2>
<p> For help in building kickstarts, try using the &#8220;system-config-kickstart&#8221; tool, or install a new system and look at the /root/anaconda-ks.cfg file left over from the installer. General kickstart questions can also be asked at kickstart-list [at] redhat.com. Cobbler ships some kickstart templates in /etc/cobbler that may also prove helpful. </p>
<p> Also see the aforementioned webpages for additional documentation, user contributed tips, and so on.</p>
<h2>COBBLER USAGE</h2>
<h3><font SIZE="-1">SETUP</font></h3>
<p> After installing, run &#8220;cobbler check&#8221; to verify that cobbler&#8217;s ecosystem is configured correctly. Cobbler check will direct you on how to modify it&#8217;s config files using a text editor. </p>
<p> Any problems detected should be corrected, with the potential exception of <font SIZE="-1">DHCP</font> related warnings where you will need to use your judgement as to whether they apply to your environment. Run &#8220;cobbler sync&#8221; after making any changes to the configuration files to ensure those changes are applied to the environment. </p>
<p> It is especially important that the server name field be accurate in /etc/cobbler/settings, without this field being correct, kickstart trees will not be found, and automated installations will fail. </p>
<p> For <font SIZE="-1">PXE,</font> if <font SIZE="-1">DHCP</font> is to be run from the cobbler server, the dhcp configuration file should be changed as suggested by &#8220;cobbler check&#8221;. If <font SIZE="-1">DHCP</font> is not run locally, the &#8220;next-server&#8221; field on the <font SIZE="-1">DHCP</font> server should at minimum point to the cobbler server&#8217;s <font SIZE="-1">IP</font> and the filename should be set to &#8220;pxelinux.0&#8221;. Alternatively, cobbler can also generate your dhcp configuration file if you want to run dhcp locally &#8212; this is covered in a later section. If you don&#8217;t already have a <font SIZE="-1">DHCP</font> setup managed by some other tool, allowing cobbler to manage your <font SIZE="-1">DHCP</font> environment will prove to be useful as it can manage <font SIZE="-1">DHCP</font> reservations and other data. If you already have a <font SIZE="-1">DHCP</font> setup, moving an existing setup to be managed from within cobbler is relatively painless &#8212; though usage of the <font SIZE="-1">DHCP</font> management feature is entirely optional. If you are not interested in network booting via <font SIZE="-1">PXE</font> and just want to use koan to install virtual systems or replace existing ones, <font SIZE="-1">DHCP</font> configuration can be totally ignored. Koan also has a live <font SIZE="-1">CD </font>(see koan&#8217;s manpage) capability that can be used to simulate <font SIZE="-1">PXE</font> environments.</p>
<h3><font SIZE="-1">DISTRIBUTIONS</font></h3>
<p> This first step towards configuring what you want to install is to add a distribution record to cobbler&#8217;s configuration. </p>
<p> If there is an rsync mirror, <font SIZE="-1">DVD, NFS,</font> or filesystem tree available that you would rather import instead, skip down to the documentation about the &#8220;import&#8221; command. It&#8217;s really a lot easier to follow the import workflow &#8212; it only requires waiting for the mirror content to be copied and/or scanned. Imported mirrors also save time during install since they don&#8217;t have to hit external install sources. </p>
<p> If you want to be explicit with distribution definition, however, here&#8217;s how it works: </p>
<p> <code>cobbler distro add &#8211;name=string &#8211;kernel=path &#8211;initrd=path [&#8211;kopts=string] [&#8211;kopts-post=string] [&#8211;ksmeta=string] [&#8211;arch=x86|x86_64|ia64] [&#8211;breed=redhat|debian|suse] [&#8211;template-files=string]</code></p>
<dl>
<dt>name</p>
<dd> a string identifying the distribution, this should be something like &#8220;rhel4&#8221;.</p>
<dt>kernel</p>
<dd> An absolute filesystem path to a kernel image</p>
<dt>initrd</p>
<dd> An absolute filesystem path to a initrd image</p>
<dt>kopts</p>
<dd> Sets kernel command-line arguments that the distro, and profiles/systems depending on it, will use. To remove a kernel argument that may be added by a higher cobbler object (or in the global settings), you can prefix it with a &#8220;!&#8221;. </p>
<p> Example: &#8211;kopts=&#8220;foo=bar baz=3 asdf !gulp&#8221; </p>
<p> This example passes the arguments &#8220;foo=bar baz=3 asdf&#8221; but will make sure &#8220;gulp&#8221; is not passed even if it was requested at a level higher up in the cobbler configuration.</p>
<dt>kopts-post</p>
<dd> This is just like &#8211;kopts, though it governs kernel options on the installed <font SIZE="-1">OS,</font> as opposed to kernel options fed to the installer. The syntax is exactly the same. This requires some special snippets to be found in your kickstart template in order for this to work. Kickstart templating is described later on in this document. </p>
<p> Example: &#8220;noapic&#8221;</p>
<dt>arch</p>
<dd> Sets the architecture for the <font SIZE="-1">PXE</font> bootloader and also controls how koan&#8217;s &#8211;replace-self option will operate. </p>
<p> The default setting (&#8216;standard&#8217;) will use pxelinux. Set to &#8216;ia64&#8217; to use elilo. &#8216;ppc&#8217; and &#8216;ppc64&#8217; use yaboot. &#8216;s390x&#8217; is not PXEable, but koan supports it for reinstalls. </p>
<p> &#8216;x86&#8217; and &#8216;x86_64&#8217; effectively do the same thing as standard. </p>
<p> If you perform a cobbler import, the arch field will be auto-assigned.</p>
<dt>ksmeta</p>
<dd> This is an advanced feature that sets kickstart variables to substitute, thus enabling kickstart files to be treated as templates. Templates are powered using Cheetah and are described further along in this manpage as well as on the Cobbler Wiki. </p>
<p> Example: &#8211;ksmeta=&#8220;foo=bar baz=3 asdf&#8221; </p>
<p> See the section on &#8220;Kickstart Templating&#8221; for further information.</p>
<dt>breed</p>
<dd> Controls how various physical and virtual parameters, including kernel arguments for automatic installation, are to be treated. Defaults to &#8220;redhat&#8221;, which is a suitable value for Fedora and CentOS as well. It means anything redhat based. </p>
<p> There is limited experimental support for specifying &#8220;debian&#8221;, &#8220;ubuntu&#8221;, or &#8220;suse&#8221;, which treats the kickstart file as a different format and changes the kernel arguments appropriately. Support for other types of distributions is possible in the future. See the Wiki for the latest information about support for these distributions. </p>
<p> The file used for the answer file, regardless of the breed setting, is the value used for &#8211;kickstart when creating the profile. In other words, if another distro calls their answer file something other than a &#8220;kickstart&#8221;, the kickstart parameter still governs where that answer file is.</p>
<dt>os-version</p>
<dd> Generally this field can be ignored. It is intended to alter some hardware setup for virtualized instances when provisioning guests with koan. The valid options for &#8211;os-version vary depending on what is specified for &#8211;breed. If you specify an invalid option, the error message will contain a list of valid os versions that can be used. If you do not know the os version or it does not appear in the list, omitting this argument or using &#8220;other&#8221; should be perfectly fine. Largely this is needed to support older distributions in virtualized settings, such as &#8220;rhel2.1&#8221;, one of the <font SIZE="-1">OS</font> choices if the breed is set to &#8220;redhat&#8221;. If you do not encounter any problems with virtualized instances, this option can be safely ignored.</p>
<dt>owners</p>
<dd> Users with small sites and a limited number of admins can probably ignore this option. All cobbler objects (distros, profiles, systems, and repos) can take a &#8211;owners parameter to specify what cobbler users can edit particular objects. This only applies to the Cobbler WebUI and <font SIZE="-1">XMLRPC</font> interface, not the &#8220;cobbler&#8221; command line tool run from the shell. Furthermore, this is only respected by the &#8220;authz_ownership&#8221; module which must be enabled in /etc/cobbler/modules.conf. The value for &#8211;owners is a space separated list of users and groups as specified in /etc/cobbler/users.conf. For more information see the users.conf file as well as the Cobbler Wiki. In the default Cobbler configuration, this value is completely ignored, as is users.conf.</p>
<dt>template-files</p>
<dd> This feature allows cobbler to be used as a configuration management system. The argument is a space delimited string of key=value pairs. Each key is the path to a template file, each value is the path to install the file on the system. This is described in further detail on the Cobbler Wiki and is implemented using special code in the post install. Koan also can retrieve these files from a cobbler server on demand, effectively allowing cobbler to function as a lightweight templated configuration management system.</p>
<dt>redhat-management-key</p>
<dd> If you&#8217;re using Red Hat Network, Red Hat Satellite Server, or Spacewalk, you can store your authentication keys here and Cobbler can add the neccessary authentication code to your kickstart where the snippet named &#8220;redhat_register&#8221; is included. Read more about setup in /etc/cobbler/settings.</dl>
<h3><font SIZE="-1">PROFILES</font></h3>
<p> A profile associates a distribution to additional specialized options, such as a kickstart automation file. Profiles are the core unit of provisioning and at least one profile must exist for every distribution to be provisioned. A profile might represent, for instance, a web server or desktop configuration. In this way, profiles define a role to be performed. </p>
<p> <code>cobbler profile add &#8211;name=string &#8211;distro=string [&#8211;kickstart=path] [&#8211;kopts=string] [&#8211;ksmeta=string] [&#8211;virt-file-size=gigabytes] [&#8211;virt-ram=megabytes] [&#8211;virt-type=string] [&#8211;virt-cpus=integer] [&#8211;virt-path=string] [&#8211;virt-bridge=string] [&#8211;server] [&#8211;parent=profile]</code> </p>
<p> Arguments are the same as listed for distributions, save for the removal of &#8220;arch&#8221; and &#8220;breed&#8221;, and with the additions listed below:</p>
<dl>
<dt>name</p>
<dd> A descriptive name. This could be something like &#8220;rhel5webservers&#8221; or &#8220;f9desktops&#8221;.</p>
<dt>distro</p>
<dd> The name of a previously defined cobbler distribution. This value is required.</p>
<dt>kickstart</p>
<dd> Local filesystem path to a kickstart file. </p>
<p> If this parameter is not provided, the kickstart file will default to /var/lib/cobbler/kickstarts/default.ks. This file is initially blank, meaning default kickstarts are not automated &#8220;out of the box&#8221;. Admins can change the default.ks if they desire. </p>
<p> When using kickstart files, they must be placed in /var/lib/cobbler/kickstarts. If using the webapp to create new kickstarts, this is where the web application will put them.</p>
<dt>nameservers</p>
<dd> If your nameservers are not provided by <font SIZE="-1">DHCP,</font> you can specify a space separated list of addresses here to configure each of the installed nodes to use them (provided the kickstarts used are installed on a per-system basis). Users with <font SIZE="-1">DHCP</font> setups should not need to use this option. This is available to set in profiles to avoid having to set it repeatedly for each system record.</p>
<dt>virt-file-size</p>
<dd> (Virt-only) How large the disk image should be in Gigabytes. The default is &#8220;5&#8221;. This can be a comma separated list (ex: &#8220;5,6,7&#8221;) to allow for multiple disks of different sizes depending on what is given to &#8211;virt-path. This should be input as a integer or decimal value without units.</p>
<dt>virt-ram</p>
<dd> (Virt-only) How many megabytes of <font SIZE="-1">RAM</font> to consume. The default is 512 <font SIZE="-1">MB. </font> This should be input as an integer without units.</p>
<dt>virt-type</p>
<dd> (Virt-only) Koan can install images using either Xen paravirt (&#8220;xenpv&#8221;) or <font SIZE="-1">QEMU/KVM </font>(&#8220;qemu&#8221;). Choose one or the other strings to specify, or values will default to attempting to find a compatible installation type on the client system (&#8220;auto&#8221;). See the &#8220;koan&#8221; manpage for more documentation. The default virt-type can be configured in the cobbler settings file such that this parameter does not have to be provided. Other virtualization types are supported, for information on those options (such as VMware), see the Cobbler Wiki.</p>
<dt>virt-cpus</p>
<dd> (Virt-only) How many virtual CPUs should koan give the virtual machine? The default is 1. This is an integer.</p>
<dt>virt-path</p>
<dd> (Virt-only) Where to store the virtual image on the host system. Except for advanced cases, this parameter can usually be omitted. For disk images, the value is usually an absolute path to an existing directory with an optional file name component. There is support for specifying partitions &#8220;/dev/sda4&#8221; or volume groups &#8220;VolGroup00&#8221;, etc. </p>
<p> For multiple disks, separate the values with commas such as &#8220;VolGroup00,VolGroup00&#8221; or &#8220;/dev/sda4,/dev/sda5&#8221;. Both those examples would create two disks for the <font SIZE="-1">VM.</font></p>
<dt>virt-bridge</p>
<dd> (Virt-only) This specifies the default bridge to use for all systems defined under this profile. If not specified, it will assume the default value in the cobbler settings file, which as shipped in the <font SIZE="-1">RPM</font> is &#8216;xenbr0&#8217;. If using <font SIZE="-1">KVM,</font> this is most likely not correct. You may want to override this setting in the system object. Bridge settings are important as they define how outside networking will reach the guest. For more information on bridge setup, see the Cobbler Wiki, where there is a section describing koan usage.</p>
<dt>repos</p>
<dd> This is a space delimited list of all the repos (created with &#8220;cobbler repo add&#8221; and updated with &#8220;cobbler reposync&#8221;) that this profile can make use of during kickstart installation. For example, an example might be &#8211;repos=&#8220;fc6i386updates fc6i386extras&#8221; if the profile wants to access these two mirrors that are already mirrored on the cobbler server. Repo management is described in greater depth later in the manpage.</p>
<dt>parent</p>
<dd> This is an advanced feature. </p>
<p> Profiles may inherit from other profiles in lieu of specifying &#8211;distro. Inherited profiles will override any settings specified in their parent, with the exception of &#8211;ksmeta (templating) and &#8211;kopts (kernel options), which will be blended together. </p>
<p> Example: If profile A has &#8211;kopts=&#8220;x=7 y=2&#8221;, B inherits from A, and B has &#8211;kopts=&#8220;x=9 z=2&#8221;, the actual kernel options that will be used for B are &#8220;x=9 y=2 z=2&#8221;. </p>
<p> Example: If profile B has &#8211;virt-ram=256 and A has &#8211;virt-ram of 512, profile B will use the value 256. Example: If profile A has a &#8211;virt-file-size of 5 and B does not specify a size, B will use the value from A.</p>
<dt>server</p>
<dd> This parameter should be useful only in select circumstances. If machines are on a subnet that cannot access the cobbler server using the name/IP as configured in the cobbler settings file, use this parameter to override that server name. See also &#8211;dhcp-tag for configuring the next server and <font SIZE="-1">DHCP</font> information of the system if you are also using Cobbler to help manage your <font SIZE="-1">DHCP</font> configuration.</dl>
<h3><font SIZE="-1">SYSTEMS</font></h3>
<p> System records map a piece of hardware (or a virtual machine) with the cobbler profile to be assigned to run on it. This may be thought of as choosing a role for a specific system. </p>
<p> Note that if provisioning via koan and <font SIZE="-1">PXE</font> menus alone, it is not required to create system records in cobbler, though they are useful when system specific customizations are required. One such customization would be defining the <font SIZE="-1">MAC</font> address. If there is a specific role intended for a given machine, system records should be created for it. </p>
<p> System commands have a wider variety of control offered over network details. In order to use these to the fullest possible extent, the kickstart template used by cobbler must contain certain kickstart snippets (sections of code specifically written for Cobbler to make these values become reality). Compare your kickstart templates with the stock ones in /var/lib/cobbler/kickstarts if you have upgraded, to make sure you can take advantage of all options to their fullest potential. If you are a new cobbler user, base your kickstarts off of these templates. Non-kickstart based distributions, while supported by Cobbler, may not be able to use all of these features. </p>
<p> Read more about networking setup at: <a rel="nofollow" href="https://github.com/cobbler/cobbler/wiki/Advanced-networking">https://github.com/cobbler/cobbler/wiki/Advanced-networking</a> </p>
<p> <code>cobbler system add &#8211;name=string &#8211;profile=string [&#8211;mac=macaddress] [&#8211;ip-address=ipaddress] [&#8211;hostname=hostname] [&#8211;kopts=string] [&#8211;ksmeta=string] [&#8211;kickstart=path] [&#8211;netboot-enabled=Y/N] [&#8211;server=string] [&#8211;gateway=string] [&#8211;dns-name=string] [&#8211;static-routes=string] [&#8211;power-address=string] [&#8211;power-type=string] [&#8211;power-user=string] [&#8211;power-pass=string] [&#8211;power-id=string]</code> </p>
<p> Adds a cobbler System to the configuration. Arguments are specified as per &#8220;profile add&#8221; with the following changes:</p>
<dl>
<dt>name</p>
<dd> The system name works like the name option for other commands. </p>
<p> If the name looks like a <font SIZE="-1">MAC</font> address or an <font SIZE="-1">IP,</font> the name will implicitly be used for either &#8211;mac or &#8211;ip of the first interface, respectively. However, it&#8217;s usually better to give a descriptive name &#8212; don&#8217;t rely on this behavior. </p>
<p> A system created with name &#8220;default&#8221; has special semantics. If a default system object exists, it sets all undefined systems to <font SIZE="-1">PXE</font> to a specific profile. Without a &#8220;default&#8221; system name created, <font SIZE="-1">PXE</font> will fall through to local boot for unconfigured systems. </p>
<p> When using &#8220;default&#8221; name, don&#8217;t specify any other arguments than &#8211;profile &#8230; they won&#8217;t be used.</p>
<dt>&#8211;mac</p>
<dd> Specifying a mac address via &#8211;mac allows the system object to boot directly to a specific profile via <font SIZE="-1">PXE,</font> bypassing cobbler&#8217;s <font SIZE="-1">PXE</font> menu. If the name of the cobbler system already looks like a mac address, this is inferred from the system name and does not need to be specified. </p>
<p> <font SIZE="-1">MAC</font> addresses have the format <font SIZE="-1">AA:BB:CC:DD:EE:FF.</font> It&#8217;s highly recommended to register your MAC-addresses in Cobbler if you&#8217;re using static addressing with multiple interfaces, or if you are using any of the advanced networking features like bonding, bridges or VLANs. </p>
<p> Cobbler does contain a feature (enabled in /etc/cobbler/settings) that can automatically add new system records when it finds profiles being provisioned on hardware it has seen before. This may help if you do not have a report of all the <font SIZE="-1">MAC</font> addresses in your datacenter/lab configuration.</p>
<dt>&#8211;ip-address</p>
<dd> If cobbler is configured to generate a <font SIZE="-1">DHCP</font> configuration (see advanced section), use this setting to define a specific <font SIZE="-1">IP</font> for this system in <font SIZE="-1">DHCP. </font> Leaving off this parameter will result in no <font SIZE="-1">DHCP</font> management for this particular system. </p>
<p> Example: &#8211;ip-address=192.168.1.50 </p>
<p> Note for Itanium users: this setting is always required for <font SIZE="-1">IA64</font> regardless of whether <font SIZE="-1">DHCP</font> management is enabled. </p>
<p> If <font SIZE="-1">DHCP</font> management is disabled and the interface is labelled &#8211;static=1, this setting will be used for static <font SIZE="-1">IP</font> configuration. </p>
<p> Special feature: To control the default <font SIZE="-1">PXE</font> behavior for an entire subnet, this field can also be passed in using <font SIZE="-1">CIDR</font> notation. If &#8211;ip is <font SIZE="-1">CIDR,</font> do not specify any other arguments other than &#8211;name and &#8211;profile. </p>
<p> When using the <font SIZE="-1">CIDR</font> notation trick, don&#8217;t specify any arguments other than &#8211;name and &#8211;profile&#8230; they won&#8217;t be used.</p>
<dt>&#8211;dns-name</p>
<dd> If using the <font SIZE="-1">DNS</font> management feature (see advanced section &#8212; cobbler supports auto-setup of <font SIZE="-1">BIND</font> and dnsmasq), use this to define a hostname for the system to receive from <font SIZE="-1">DNS.</font> </p>
<p> Example: &#8211;dns-name=mycomputer.example.com </p>
<p> This is a per-interface parameter. If you have multiple interfaces, it may be different for each interface, for example, assume a <font SIZE="-1">DMZ /</font> dual-homed setup.</p>
<dt>&#8211;gateway and &#8211;subnet</p>
<dd> If you are using static <font SIZE="-1">IP</font> configurations and the interface is flagged &#8211;static=1, these will be applied. </p>
<p> Subnet is a per-interface parameter. Because of the way gateway is stored on the installed <font SIZE="-1">OS,</font> gateway is a global parameter. You may use &#8211;static-routes for per-interface customizations if required.</p>
<dt>&#8211;hostname</p>
<dd> This field corresponds to the hostname set in a systems /etc/sysconfig/network file. This has no bearing on <font SIZE="-1">DNS,</font> even when manage_dns is enabled. Use &#8211;dns-name instead for that feature. </p>
<p> This parameter is assigned once per system, it is not a per-interface setting.</p>
<dt>&#8211;power-address, &#8211;power-type, &#8211;power-user, &#8211;power-pass, &#8211;power-id</p>
<dd> Cobbler contains features that enable integration with power management for easier installation, reinstallation, and management of machines in a datacenter environment. These parameters are described online at <a rel="nofollow" href="https://github.com/cobbler/cobbler/wiki/Power-management.">https://github.com/cobbler/cobbler/wiki/Power-management.</a> If you have a power-managed datacenter/lab setup, usage of these features may be something you are interested in.</p>
<dt>&#8211;static</p>
<dd> Indicates that this interface is statically configured. Many fields (such as gateway/subnet) will not be used unless this field is enabled. </p>
<p> This is a per-interface setting.</p>
<dt>&#8211;static-routes</p>
<dd> This is a space delimited list of ip/mask:gateway routing information in that format. Most systems will not need this information. </p>
<p> This is a per-interface setting.</p>
<dt>&#8211;virt-bridge</p>
<dd> (Virt-only) While &#8211;virt-bridge is present in the profile object (see above), here it works on an interface by interface basis. For instance it would be possible to have &#8211;virt-bridge0=xenbr0 and &#8211;virt-bridge1=xenbr1. If not specified in cobbler for each interface, koan will use the value as specified in the profile for each interface, which may not always be what is intended, but will be sufficient in most cases. </p>
<p> This is a per-interface setting.</p>
<dt>&#8211;kickstart</p>
<dd> While it is recommended that the &#8211;kickstart parameter is only used within for the &#8220;profile add&#8221; command, there are limited scenarios when an install base switching to cobbler may have legacy kickstarts created on a per-system basis (one kickstart for each system, nothing shared) and may not want to immediately make use of the cobbler templating system. This allows specifying a kickstart for use on a per-system basis. Creation of a parent profile is still required. If the kickstart is a filesystem location, it will still be treated as a cobbler template.</p>
<dt>&#8211;netboot-enabled</p>
<dd> If set false, the system will be provisionable through koan but not through standard <font SIZE="-1">PXE. </font> This will allow the system to fall back to default <font SIZE="-1">PXE</font> boot behavior without deleting the cobbler system object. The default value allows <font SIZE="-1">PXE. </font> Cobbler contains a <font SIZE="-1">PXE</font> boot loop prevention feature (pxe_just_once, can be enabled in /etc/cobbler/settings) that can automatically trip off this value after a system gets done installing. This can prevent installs from appearing in an endless loop when the system is set to <font SIZE="-1">PXE</font> first in the <font SIZE="-1">BIOS</font> order.</p>
<dt>&#8211;ldap-enabled, &#8211;ldap-type</p>
<dd> Cobbler contains features that enable ldap management for easier configuration after system provisioning. If set true, koan will run the ldap command as defined by the systems ldap_type. The default value is false.</p>
<dt>&#8211;monit-enabled</p>
<dd> If set true, koan will reload monit after each configuration run. The default value is false.</p>
<dt>&#8211;repos-enabled</p>
<dd> If set true, koan can reconfigure repositories after installation. This is described further on the Cobbler Wiki, <a rel="nofollow" href="https://github.com/cobbler/cobbler/wiki/Manage-yum-repos.">https://github.com/cobbler/cobbler/wiki/Manage-yum-repos.</a></p>
<dt>&#8211;dhcp-tag</p>
<dd> If you are setting up a <font SIZE="-1">PXE</font> environment with multiple subnets/gateways, and are using cobbler to manage a <font SIZE="-1">DHCP</font> configuration, you will probably want to use this option. If not, it can be ignored. </p>
<p> By default, the dhcp tag for all systems is &#8220;default&#8221; and means that in the <font SIZE="-1">DHCP</font> template files the systems will expand out where <tt>$insert_cobbler_systems_definitions</tt> is found in the <font SIZE="-1">DHCP</font> template. However, you may want certain systems to expand out in other places in the <font SIZE="-1">DHCP</font> config file. Setting &#8211;dhcp-tag=subnet2 for instance, will cause that system to expand out where <tt>$insert_cobbler_system_definitions_subnet2</tt> is found, allowing you to insert directives to specify different subnets (or other parameters) before the <font SIZE="-1">DHCP</font> configuration entries for those particular systems. </p>
<p> This is described further on the Cobbler Wiki.</p>
<dt>&#8211;interface</p>
<dd> By default flags like &#8211;ip, &#8211;mac, &#8211;dhcp-tag, &#8211;dns-name, &#8211;subnet, &#8211;virt-bridge, and &#8211;static-routes operate on the first network interface defined for a system (eth0). However, cobbler supports an arbitrary number of interfaces. Using &#8211;interface=eth1 for instance, will allow creating and editing of a second interface. </p>
<p> Interface naming notes: </p>
<p> Additional interfaces can be specified (for example: eth1, or any name you like, as long as it does not conflict with any reserved names such as kernel module names) for use with the edit command. Defining VLANs this way is also supported, of you want to add <font SIZE="-1">VLAN 5</font> on interface eth0, simply name your interface eth0.5. </p>
<p> Example: </p>
<p> cobbler system edit &#8211;name=foo &#8211;ip-address=192.168.1.50 &#8211;mac=AA:BB:CC:DD:EE:A0 cobbler system edit &#8211;name=foo &#8211;interface=eth0 &#8211;ip-address=192.168.1.51 &#8211;mac=AA:BB:CC:DD:EE:A1 cobbler system report foo </p>
<p> Interfaces can be deleted using the &#8211;delete-interface option. </p>
<p> Example: </p>
<p> cobbler system edit &#8211;name=foo &#8211;interface=eth2 &#8211;delete-interface</p>
<dt>&#8211;interface-type, &#8211;interface-master and &#8211;bonding-opts/&#8211;bridge-opts</p>
<dd> One of the other advanced networking features supported by Cobbler is <font SIZE="-1">NIC</font> bonding and bridging. You can use this to bond multiple physical network interfaces to one single logical interface to reduce single points of failure in your network, or to create bridged interfaces for things like tunnels and virtual machine networks. Supported values for the &#8211;interface-type parameter are &#8220;bond&#8221;, &#8220;bond_slave&#8221;, &#8220;bridge&#8221;, &#8220;bridge_slave&#8221; and &#8220;bonded_bridge_slave&#8221;. If one of the &#8220;_slave&#8221; options is specified, you also need to define the master-interface for this bond using &#8211;interface-master=INTERFACE. Bonding and bridge options for the master-interface may be specified using &#8211;bonding-opts=&#8220;foo=1 bar=2&#8221; or &#8211;bridge-opts=&#8220;foo=1 bar=2&#8221;, respectively. </p>
<p> Example: </p>
<p> cobbler system edit &#8211;name=foo &#8211;interface=eth0 &#8211;mac=AA:BB:CC:DD:EE:00 &#8211;interface-type=bond_slave &#8211;interface-master=bond0 cobbler system edit &#8211;name=foo &#8211;interface=eth1 &#8211;mac=AA:BB:CC:DD:EE:01 &#8211;interface-type=bond_slave &#8211;interface-master=bond0 cobbler system edit &#8211;name=foo &#8211;interface=bond0 &#8211;interface-type=bond &#8211;bonding-opts=&#8220;mode=active-backup miimon=100&#8221; &#8211;ip-address=192.168.0.63 &#8211;subnet=255.255.255.0 &#8211;gateway=192.168.0.1 &#8211;static=1 </p>
<p> More information about networking setup is available at <a rel="nofollow" href="https://github.com/cobbler/cobbler/wiki/Advanced-networking">https://github.com/cobbler/cobbler/wiki/Advanced-networking</a> </p>
<p> To review what networking configuration you have for any object, run &#8220;cobbler system report&#8221; at any time: </p>
<p> Example: </p>
<p> cobbler system report &#8211;name=foo</dl>
<h3><font SIZE="-1">REPOSITORIES</font></h3>
<p> Repository mirroring allows cobbler to mirror not only install trees (&#8220;cobbler import&#8221; does this for you) but also optional packages, 3rd party content, and even updates. Mirroring all of this content locally on your network will result in faster, more up-to-date installations and faster updates. If you are only provisioning a home setup, this will probably be overkill, though it can be very useful for larger setups (labs, datacenters, etc). </p>
<p> <code>cobbler repo add &#8211;mirror=url &#8211;name=string [&#8211;rpmlist=list] [&#8211;creatrepo-flags=string] [&#8211;keep-updated=Y/N] [&#8211;priority=number] [&#8211;arch=string] [&#8211;mirror-locally=Y/N] [&#8211;breed=yum|rsync|rhn]</code></p>
<dl>
<dt>mirror</p>
<dd> The address of the yum mirror. This can be an rsync:// <font SIZE="-1">URL,</font> an ssh location, or a http:// or ftp:// mirror location. Filesystem paths also work. </p>
<p> The mirror address should specify an exact repository to mirror &#8212; just one architecture and just one distribution. If you have a separate repo to mirror for a different arch, add that repo separately. </p>
<p> Here&#8217;s an example of what looks like a good <font SIZE="-1">URL:</font> </p>
<p> <a href="rsync://yourmirror.example.com/fedora-linux-core/updates/6/i386">rsync://yourmirror.example.com/fedora-linux-core/updates/6/i386</a> (for rsync protocol) <a rel="nofollow" href="http://mirrors.kernel.org/fedora/extras/6/i386/">http://mirrors.kernel.org/fedora/extras/6/i386/</a> (for <a href="http://)">http://)</a> user [at] yourmirror.example.com/fedora-linux-core/updates/6/i386 (for <font SIZE="-1">SSH</font>) </p>
<p> Experimental support is also provided for mirroring <font SIZE="-1">RHN</font> content when you need a fast local mirror. The mirror syntax for this is &#8211;mirror=<a href="rhn://channel-name">rhn://channel-name</a> and you must have entitlements for this to work. This requires the cobbler server to be installed on <font SIZE="-1">RHEL5</font> or later. You will also need a version of yum-utils equal or greater to 1.0.4.</p>
<dt>name</p>
<dd> This name is used as the save location for the mirror. If the mirror represented, say, Fedora Core 6 i386 updates, a good name would be &#8220;fc6i386updates&#8221;. Again, be specific. </p>
<p> This name corresponds with values given to the &#8211;repos parameter of &#8220;cobbler profile add&#8221;. If a profile has a &#8211;repos value that matches the name given here, that repo can be automatically set up during provisioning (when supported) and installed systems will also use the boot server as a mirror (unless &#8220;yum_post_install_mirror&#8221; is disabled in the settings file). By default the provisioning server will act as a mirror to systems it installs, which may not be desirable for laptop configurations, etc. </p>
<p> Distros that can make use of yum repositories during kickstart include <font SIZE="-1">FC6</font> and later, <font SIZE="-1">RHEL 5</font> and later, and derivative distributions. </p>
<p> See the documentation on &#8220;cobbler profile add&#8221; for more information.</p>
<dt>rpm-list</p>
<dd> By specifying a space-delimited list of package names for &#8211;rpm-list, one can decide to mirror only a part of a repo (the list of packages given, plus dependencies). This may be helpful in conserving time/space/bandwidth. For instance, when mirroring <font SIZE="-1">FC6</font> Extras, it may be desired to mirror just cobbler and koan, and skip all of the game packages. To do this, use &#8211;rpm-list=&#8220;cobbler koan&#8221;. </p>
<p> This option only works for http:// and ftp:// repositories (as it is powered by yumdownloader). It will be ignored for other mirror types, such as local paths and rsync:// mirrors.</p>
<dt>createrepo-flags</p>
<dd> Specifies optional flags to feed into the createrepo tool, which is called when &#8220;cobbler reposync&#8221; is run for the given repository. The defaults are &#8216;-c cache&#8217;.</p>
<dt>keep-updated</p>
<dd> Specifies that the named repository should not be updated during a normal &#8220;cobbler reposync&#8221;. The repo may still be updated by name. The repo should be synced at least once before disabling this feature See &#8220;cobbler reposync&#8221; below.</p>
<dt>mirror-locally</p>
<dd> When set to &#8220;N&#8221;, specifies that this yum repo is to be referenced directly via kickstarts and not mirrored locally on the cobbler server. Only http:// and ftp:// mirror urls are supported when using &#8211;mirror-locally=N, you cannot use filesystem URLs.</p>
<dt>priority</p>
<dd> Specifies the priority of the repository (the lower the number, the higher the priority), which applies to installed machines using the repositories that also have the yum priorities plugin installed. The default priority for the plugin is 99, as is that of all cobbler mirrored repositories.</p>
<dt>arch</p>
<dd> Specifies what architecture the repository should use. By default the current system arch (of the server) is used, which may not be desirable. Using this to override the default arch allows mirroring of source repositories (using &#8211;arch=src).</p>
<dt>yumopts</p>
<dd> Sets values for additional yum options that the repo should use on installed systems. For instance if a yum plugin takes a certain parameter &#8220;alpha&#8221; and &#8220;beta&#8221;, use something like &#8211;yumopts=&#8220;alpha=2 beta=3&#8221;.</p>
<dt>breed</p>
<dd> Ordinarily cobbler&#8217;s repo system will understand what you mean without supplying this parameter, though you can set it explicitly if needed.</dl>
<h3><font SIZE="-1">MANAGEMENT CLASSES</font></h3>
<p> Management classes allows cobbler to function as an configuration management system. Cobbler currently supports the following resource types:</p>
<dl>
<dt>1. Packages</p>
<dd>
<dt>2. Files</p>
<dd></dl>
<p> Resources are executed in the order listed above. </p>
<p> <code>cobbler mgmtclass add &#8211;name=string &#8211;comment=string [&#8211;packages=list] [&#8211;files=list]</code></p>
<dl>
<dt>name</p>
<dd> The name of the mgmtclass. Use this name when adding a management class to a system, profile, or distro. To add a mgmtclass to an existing system use something like (cobbler system edit &#8211;name=&#8220;madhatter&#8221; &#8211;mgmt-classes=&#8220;http mysql&#8221;).</p>
<dt>comment</p>
<dd> A comment that describes the functions of the management class.</p>
<dt>packages</p>
<dd> Specifies a list of package resources required by the management class.</p>
<dt>files</p>
<dd> Specifies a list of file resources required by the management class.</dl>
<h2>MANAGEMENT RESOURCES</h2>
<p> Resources are the lego blocks of configuration management. Resources are grouped together via Management Classes, which are then linked to a system. Cobbler supports two (2) resource types. Resources are configured in the order listed below.</p>
<dl>
<dt>1. Packages</p>
<dd>
<dt>2. Files</p>
<dd></dl>
<h3><font SIZE="-1">PACKAGE RESOURCES</font></h3>
<p> Package resources are managed using cobbler package add </p>
<p> <i>Actions</i></p>
<dl>
<dt>install</p>
<dd> Install the package. [Default]</p>
<dt>uninstall</p>
<dd> Uninstall the package.</dl>
<p> <i>Attributes</i></p>
<dl>
<dt>installer</p>
<dd> Which package manager to use, vaild options [rpm|yum].</p>
<dt>version</p>
<dd> Which version of the package to install.</dl>
<p> <i>Examples</i> </p>
<p> <code>cobbler package add &#8211;name=string &#8211;comment=string [&#8211;action=install|uninstall] &#8211;installer=string [&#8211;version=string]</code></p>
<h3><font SIZE="-1">FILE RESOURCES</font></h3>
<p> <i>Actions</i></p>
<dl>
<dt>create</p>
<dd> Create the file. [Default]</p>
<dt>remove</p>
<dd> Remove the file.</dl>
<p> <i>Attributes</i></p>
<dl>
<dt>mode</p>
<dd> Permission mode (as in chmod).</p>
<dt>group</p>
<dd> The group owner of the file.</p>
<dt>user</p>
<dd> The user for the file.</p>
<dt>path</p>
<dd> The path for the file.</p>
<dt>template</p>
<dd> The template for the file.</dl>
<p> <i>Examples</i> </p>
<p> <code>cobbler file add &#8211;name=string &#8211;comment=string [&#8211;action=string] &#8211;mode=string &#8211;group=string &#8211;owner=string &#8211;path=string [&#8211;template=string]</code></p>
<h3><font SIZE="-1">DISPLAYING CONFIGURATION ENTRIES</font></h3>
<p> The following commands are usable regardless of how you are using cobbler. &#8220;report&#8221; gives detailed configuration info. &#8220;list&#8221; just lists the names of items in the configuration. Run these commands to check how you have cobbler configured. </p>
<p> <code>cobbler list</code> </p>
<p> <code>cobbler distro|profile|system|repo|image|mgmtclass|package|file list</code> </p>
<p> <code>cobbler report</code> </p>
<p> <code>cobbler distro|profile|system|repo|image|mgmtclass|package|file report &#8211;name=[object-name]</code> </p>
<p> Alternatively, you could look at the configuration files in /var/lib/cobbler to see the same information.</p>
<h3><font SIZE="-1">DELETING CONFIGURATION ENTRIES</font></h3>
<p> If you want to remove a specific object, use the remove command with the name that was used to add it. </p>
<p> <code>cobbler distro remove &#8211;name=string</code> </p>
<p> <code>cobbler profile remove &#8211;name=string</code> </p>
<p> <code>cobbler system remove &#8211;name=string</code> </p>
<p> <code>cobbler repo remove &#8211;name=string</code> </p>
<p> <code>cobbler image remove &#8211;name=string</code> </p>
<p> <code>cobbler mgmtclass remove &#8211;name=string</code> </p>
<p> <code>cobbler package remove &#8211;name=string</code> </p>
<p> <code>cobbler file remove &#8211;name=string</code></p>
<h3><font SIZE="-1">EDITING</font></h3>
<p> If you want to change a particular setting without doing an &#8220;add&#8221; again, use the &#8220;edit&#8221; command, using the same name you gave when you added the item. Anything supplied in the parameter list will overwrite the settings in the existing object, preserving settings not mentioned. </p>
<p> <code>cobbler distro|profile|system|repo|image|mgmtclass|package|file edit &#8211;name=string [parameterlist]</code></p>
<h3><font SIZE="-1">COPYING</font></h3>
<p> Objects can also be copied: </p>
<p> <code>cobbler distro|profile|system|repo|image|mgmtclass|package|file copy &#8211;name=oldname &#8211;newname=newname</code></p>
<h3><font SIZE="-1">RENAMING</font></h3>
<p> Objects can also be renamed, as long as other objects don&#8217;t reference them. </p>
<p> <code>cobbler distro|profile|system|repo|image|mgmtclass|package|file rename &#8211;name=oldname &#8211;newname=newname</code></p>
<h3><font SIZE="-1">REPLICATING</font></h3>
<p> Cobbler can replicate configurations from a master cobbler server. Each cobbler server is still expected to have a locally relevant /etc/cobbler/cobbler.conf and modules.conf, as these files are not synced. </p>
<p> This feature is intended for load-balancing, disaster-recovery, backup, or multiple geography support. </p>
<p> <code>cobbler replicate &#8211;master=cobbler.example.org [&#8211;distros=pattern] [&#8211;profiles=pattern] [&#8211;systems=pattern] [&#8211;repos-pattern] [&#8211;images=pattern] [&#8211;prune] [&#8211;omit-data]</code> </p>
<p> Cobbler can replicate data from a central server. </p>
<p> Objects that need to be replicated should be specified with a pattern, such as &#8211;profiles=&#8220;webservers* dbservers*&#8221; or &#8211;systems=&#8220;*.example.org&#8221;. All objects matched by the pattern, and all dependencies of those objects matched by the pattern (recursively) will be transferred from the remote server to the central server. This is to say if you intend to transfer &#8220;*.example.org&#8221; and the definition of the systems have not changed, but a profile above them has changed, the changes to that profile will also be transferred. </p>
<p> In the case where objects are more recent on the local server, those changes will not be overridden locally. </p>
<p> Common data locations will be rsync&#8217;ed from the master server unless &#8211;omit-data is specified. </p>
<p> To delete objects that are no longer present on the master server, use &#8211;prune. Warning: this will delete all object types not present on the remote server from the local server, and is recursive. If you use prune, it is best to manage cobbler centrally and not expect changes made on the slave servers to be preserved. It is not currently possible to just prune objects of a specific type.</p>
<h3><font SIZE="-1">REBUILDING CONFIGURATIONS</font></h3>
<p> <code>cobbler sync</code> </p>
<p> Cobbler sync is used to repair or rebuild the contents /tftpboot or /var/www/cobbler when something has changed behind the scenes. It brings the filesystem up to date with the configuration as understood by cobbler. </p>
<p> Sync should be run whenever files in /var/lib/cobbler are manually edited (which is not recommended except for the settings file) or when making changes to kickstart files. In practice, this should not happen often, though running sync too many times does not cause any adverse effects. </p>
<p> If using cobbler to manage a <font SIZE="-1">DHCP</font> and/or <font SIZE="-1">DNS</font> server (see the advanced section of this manpage), sync does need to be run after systems are added to regenerate and reload the <font SIZE="-1">DHCP/DNS</font> configurations. </p>
<p> The sync process can also be kicked off from the web interface.</p>
<h2>EXAMPLES</h2>
<h3><font SIZE="-1">IMPORT WORKFLOW</font></h3>
<p> Import is a very useful command that makes starting out with cobbler very quick and easy. </p>
<p> This example shows how to create a provisioning infrastructure from a distribution mirror or <font SIZE="-1">DVD ISO.</font> Then a default <font SIZE="-1">PXE</font> configuration is created, so that by default systems will <font SIZE="-1">PXE</font> boot into a fully automated install process for that distribution. </p>
<p> You can use a network rsync mirror, a mounted <font SIZE="-1">DVD</font> location, or a tree you have available via a network filesystem. </p>
<p> Import knows how to autodetect the architecture of what is being imported, though to make sure things are named correctly, it&#8217;s always a good idea to specify &#8211;arch. For instance, if you import a distribution named &#8220;fedora8&#8221; from an <font SIZE="-1">ISO,</font> and it&#8217;s an x86_64 <font SIZE="-1">ISO,</font> specify &#8211;arch=x86_64 and the distro will be named &#8220;fedora8-x86_64&#8221; automatically, and the right architecture field will also be set on the distribution object. If you are batch importing an entire mirror (containing multiple distributions and arches), you don&#8217;t have to do this, as cobbler will set the names for things based on the paths it finds. </p>
<p> <code>cobbler check</code> </p>
<p> <code>cobbler import &#8211;path=<a href="rsync://yourfavoritemirror.com/rhel/5/os/x86_64">rsync://yourfavoritemirror.com/rhel/5/os/x86_64</a> &#8211;name=rhel5 &#8211;arch=x86_64</code> </p>
<p> # <font SIZE="-1">OR </font> </p>
<p> <code>cobbler import &#8211;path=/mnt/dvd &#8211;name=rhel5 &#8211;arch=x86_64</code> </p>
<p> # <font SIZE="-1">OR </font>(using an external <font SIZE="-1">NAS</font> box without mirroring) </p>
<p> <code>cobbler import &#8211;path=/path/where/filer/is/mounted &#8211;name=anyname &#8211;available-as=<a href="nfs://nfs.example.org:/where/mounted/">nfs://nfs.example.org:/where/mounted/</a></code> </p>
<p> # wait for mirror to rsync&#8230; </p>
<p> <code>cobbler report</code> </p>
<p> <code>cobbler system add &#8211;name=default &#8211;profile=name_of_a_profile1</code> </p>
<p> <code>cobbler system add &#8211;name=AA:BB:CC:DD:EE:FF &#8211;profile=name_of_a_profile2</code> </p>
<p> <code>cobbler sync</code></p>
<h3>NON-IMPORT (<font SIZE="-1">MANUAL</font>) <font SIZE="-1">WORKFLOW</font></h3>
<p> The following example uses a local kernel and initrd file (already downloaded), and shows how profiles would be created using two different kickstarts &#8212; one for a web server configuration and one for a database server. Then, a machine is assigned to each profile. </p>
<p> <code>cobbler check</code> </p>
<p> <code>cobbler distro add &#8211;name=rhel4u3 &#8211;kernel=/dir1/vmlinuz &#8211;initrd=/dir1/initrd.img</code> </p>
<p> <code>cobbler distro add &#8211;name=fc5 &#8211;kernel=/dir2/vmlinuz &#8211;initrd=/dir2/initrd.img</code> </p>
<p> <code>cobbler profile add &#8211;name=fc5webservers &#8211;distro=fc5-i386 &#8211;kickstart=/dir4/kick.ks &#8211;kopts=&#8220;something_to_make_my_gfx_card_work=42 some_other_parameter=foo&#8221;</code> </p>
<p> <code>cobbler profile add &#8211;name=rhel4u3dbservers &#8211;distro=rhel4u3 &#8211;kickstart=/dir5/kick.ks</code> </p>
<p> <code>cobbler system add &#8211;name=AA:BB:CC:DD:EE:FF &#8211;profile=fc5-webservers</code> </p>
<p> <code>cobbler system add &#8211;name=AA:BB:CC:DD:EE:FE &#8211;profile=rhel4u3-dbservers</code> </p>
<p> <code>cobbler report</code></p>
<h3><font SIZE="-1">REPOSITORY MIRRORING WORKFLOW</font></h3>
<p> The following example shows how to set up a repo mirror for two repositories, and create a profile that will auto install those repository configurations on provisioned systems using that profile. </p>
<p> <code>cobbler check</code> </p>
<p> # set up your cobbler distros here. </p>
<p> <code>cobbler repo add &#8211;mirror=<a rel="nofollow" href="http://mirrors.kernel.org/fedora/core/updates/6/i386/">http://mirrors.kernel.org/fedora/core/updates/6/i386/</a> &#8211;name=fc6i386updates</code> </p>
<p> <code>cobbler repo add &#8211;mirror=<a rel="nofollow" href="http://mirrors.kernel.org/fedora/extras/6/i386/">http://mirrors.kernel.org/fedora/extras/6/i386/</a> &#8211;name=fc6i386extras</code> </p>
<p> <code>cobbler reposync</code> </p>
<p> <code>cobbler profile add &#8211;name=p1 &#8211;distro=existing_distro_name &#8211;kickstart=/var/lib/cobbler/kickstarts/kickstart_fc6.ks &#8211;repos=&#8220;fc6i386updates fc6i386extras&#8221;</code></p>
<h3><font SIZE="-1">VIRTUALIZATION</font></h3>
<p> For Virt, be sure the distro uses the correct kernel (if paravirt) and follow similar steps as above, adding additional parameters as desired: </p>
<p> <code>cobbler distro add &#8211;name=fc7virt [options&#8230;]</code> </p>
<p> Specify reasonable values for the Virt image size (in <font SIZE="-1">GB</font>) and <font SIZE="-1">RAM</font> requirements (in <font SIZE="-1">MB</font>): </p>
<p> <code>cobbler profile add &#8211;name=virtwebservers &#8211;distro=fc7virt &#8211;kickstart=path &#8211;virt-file-size=10 &#8211;virt-ram=512 [&#8230;]</code> </p>
<p> Define systems if desired. koan can also provision based on the profile name. </p>
<p> <code>cobbler system add &#8211;name=AA:BB:CC:DD:EE:FE &#8211;profile=virtwebservers [&#8230;]</code> </p>
<p> If you have just installed cobbler, be sure that the &#8220;cobblerd&#8221; service is running and that port 25151 is unblocked. </p>
<p> See the manpage for koan for the client side steps.</p>
<h2>ADVANCED TOPICS</h2>
<h3><font SIZE="-1">PXE MENUS</font></h3>
<p> Cobbler will automatically generate <font SIZE="-1">PXE</font> menus for all profiles it has defined. Running &#8220;cobbler sync&#8221; is required to generate and update these menus. </p>
<p> To access the menus, type &#8220;menu&#8221; at the &#8220;boot:&#8221; prompt while a system is <font SIZE="-1">PXE</font> booting. If nothing is typed, the network boot will default to a local boot. If &#8220;menu&#8221; is typed, the user can then choose and provision any cobbler profile the system knows about. </p>
<p> If the association between a system (<font SIZE="-1">MAC</font> address) and a profile is already known, it may be more useful to just use &#8220;system add&#8221; commands and declare that relationship in cobbler; however many use cases will prefer having a <font SIZE="-1">PXE</font> system, especially when provisioning is done at the same time as installing new physical machines. </p>
<p> If this behavior is not desired, run &#8220;cobbler system add &#8211;name=default &#8211;profile=plugh&#8221; to default all <font SIZE="-1">PXE</font> booting machines to get a new copy of the profile &#8220;plugh&#8221;. To go back to the menu system, run &#8220;cobbler system remove &#8211;name=default&#8221; and then &#8220;cobbler sync&#8221; to regenerate the menus. </p>
<p> When using <font SIZE="-1">PXE</font> menu deployment exclusively, it is not necessary to make cobbler system records, although the two can easily be mixed. </p>
<p> Additionally, note that all files generated for the pxe menu configurations are templatable, so if you wish to change the color scheme or equivalent, see the files in /etc/cobbler.</p>
<h3><font SIZE="-1">KICKSTART TEMPLATING</font></h3>
<p> The &#8211;ksmeta options above require more explanation. </p>
<p> If and only if &#8211;kickstart options reference filesystem URIs, &#8211;ksmeta allows for templating of the kickstart files to achieve advanced functions. If the &#8211;ksmeta option for a profile read &#8211;ksmeta=&#8220;foo=7 bar=llama&#8221;, anywhere in the kickstart file where the string &#8220;$bar&#8221; appeared would be replaced with the string &#8220;llama&#8221;. </p>
<p> To apply these changes, &#8220;cobbler sync&#8221; must be run to generate custom kickstarts for each profile/system. </p>
<p> Templated kickstart files are processed by the templating program/package Cheetah, so anything you can do in a Cheetah template can be done to a kickstart template. Learn more at <a rel="nofollow" href="http://www.cheetahtemplate.org/learn.html">http://www.cheetahtemplate.org/learn.html</a> </p>
<p> When working with Cheetah, be sure to escape any shell macros that look like &#8220;$(this)&#8221; with something like &#8220;\$(this)&#8221; or errors may show up during the sync process. </p>
<p> The Cobbler Wiki also contains numerous Cheetah examples that should prove useful in using this feature.</p>
<h3><font SIZE="-1">KICKSTART SNIPPETS</font></h3>
<p> Anywhere a kickstart template mentions SNIPPET::snippet_name, the file named /var/lib/cobbler/snippets/snippet_name (if present) will be included automatically in the kickstart template. This serves as a way to recycle frequently used kickstart snippets without duplication. Snippets can contain templating variables, and the variables will be evaluated according to the profile and/or system as one would expect. </p>
<p> Snippets can also be overridden for specific profile names or system names. This is described on the Cobbler Wiki.</p>
<h3><font SIZE="-1">KICKSTART VALIDATION</font></h3>
<p> To check for potential errors in kickstarts, prior to installation, use &#8220;cobbler validateks&#8221;. This function will check all profile and system kickstarts for detectable errors. Since pykickstart is not future-Anaconda-version aware, there may be some false positives. It should be noted that &#8220;cobbler validateks&#8221; runs on the rendered kickstart output, not kickstart templates themselves.</p>
<h3><font SIZE="-1">DHCP MANAGEMENT</font></h3>
<p> Cobbler can optionally help you manage <font SIZE="-1">DHCP</font> server. This feature is off by default. </p>
<p> Choose either &#8220;management = isc_and_bind&#8221; in /etc/cobbler/dhcp.template or &#8220;management = &#8221;dnsmasq&#8220; in /etc/cobbler/modules.conf. Then set &#8221;manage_dhcp&quot; to 1 in /etc/cobbler/settings. </p>
<p> This allows <font SIZE="-1">DHCP</font> to be managed via &#8220;cobbler system add&#8221; commands, when you specify the mac address and <font SIZE="-1">IP</font> address for systems you add into cobbler. </p>
<p> Depending on your choice, cobbler will use /etc/cobbler/dhcpd.template or /etc/cobbler/dnsmasq.template as a starting point. This file must be user edited for the user&#8217;s particular networking environment. Read the file and understand how the particular app (<font SIZE="-1">ISC</font> dhcpd or dnsmasq) work before proceeding. </p>
<p> If you already have <font SIZE="-1">DHCP</font> configuration data that you would like to preserve (say <font SIZE="-1">DHCP</font> was manually configured earlier), insert the relevant portions of it into the template file, as running &#8220;cobbler sync&#8221; will overwrite your previous configuration. </p>
<p> <font SIZE="-1">NOTE:</font> Itanium systems names also need to be assigned to a distro that was created with the &#8220;&#8211;arch=ia64&#8221; parameter. If you have Itanium systems, you must (for now) choose &#8216;dhcp_isc&#8217; for /etc/cobbler/modules.conf and manage_dhcp in the /etc/cobbler/settings file, and are required to use &#8211;ip when creating the system object in order for those systems to <font SIZE="-1">PXE. </font> This is due to an elilo limitation. </p>
<p> By default, the <font SIZE="-1">DHCP</font> configuration file will be updated each time &#8220;cobbler sync&#8221; is run, and not until then, so it is important to remember to use &#8220;cobbler sync&#8221; when using this feature. </p>
<p> If omapi_enabled is set to 1 in /etc/cobbler/settings, the need to sync when adding new system records can be eliminated. However, the omapi feature is experimental and is not recommended for most users.</p>
<h3><font SIZE="-1">DNS CONFIGURATION MANAGEMENT</font></h3>
<p> Cobbler can optionally manage <font SIZE="-1">DNS</font> configuration using <font SIZE="-1">BIND</font> and dnsmasq. </p>
<p> Choose either &#8220;management = isc_and_bind&#8221; or &#8220;management = dnsmasq&#8221; in /etc/cobbler/modules.conf and then enable manage_dns in /etc/cobbler/settings. </p>
<p> This feature is off by default. If using <font SIZE="-1">BIND,</font> you must define the zones to be managed with the options &#8216;manage_forward_zones&#8217; and &#8216;manage_reverse_zones&#8217;. (See the Wiki for more information on this). </p>
<p> If using <font SIZE="-1">BIND,</font> Cobbler will use /etc/cobbler/named.template and /etc/cobbler/zone.template as a starting point for the named.conf and individual zone files, respectively. You may drop zone-specific template files in /etc/cobbler/zone_templates/name-of-zone which will override the default. These files must be user edited for the user&#8217;s particular networking environment. Read the file and understand how <font SIZE="-1">BIND</font> works before proceeding. </p>
<p> If using dnsmasq, the template is /etc/cobbler/dnsmasq.template. Read this file and understand how dnsmasq works before proceeding. </p>
<p> All managed files (whether zone files and named.conf for <font SIZE="-1">BIND,</font> or dnsmasq.conf for dnsmasq) will be updated each time &#8220;cobbler sync&#8221; is run, and not until then, so it is important to remember to use &#8220;cobbler sync&#8221; when using this feature.</p>
<h3><font SIZE="-1">SERVICE DISCOVERY </font>(<font SIZE="-1">AVAHI</font>)</h3>
<p> If the avahi-tools package is installed, cobblerd will broadcast it&#8217;s presence on the network, allowing it to be discovered by koan with the koan &#8211;server=DISCOVER parameter.</p>
<h3><font SIZE="-1">IMPORTING TREES</font></h3>
<p> Cobbler can auto-add distributions and profiles from remote sources, whether this is a filesystem path or an rsync mirror. This can save a lot of time when setting up a new provisioning environment. Import is a feature that many users will want to take advantage of, and is very simple to use. </p>
<p> After an import is run, cobbler will try to detect the distribution type and automatically assign kickstarts. By default, it will provision the system by erasing the hard drive, setting up eth0 for dhcp, and using a default password of &#8220;cobbler&#8221;. If this is undesirable, edit the kickstart files in /etc/cobbler to do something else or change the kickstart setting after cobbler creates the profile. </p>
<p> Mirrored content is saved automatically in /var/www/cobbler/ks_mirror. </p>
<p> Example: <code>cobbler import &#8211;path=<a href="rsync://mirrorserver.example.com/path/">rsync://mirrorserver.example.com/path/</a> &#8211;name=fedora &#8211;arch=x86</code> </p>
<p> Example2: <code>cobbler import &#8211;path=root [at] 192.168.1.10:/stuff &#8211;name=bar</code> </p>
<p> Example3: <code>cobbler import &#8211;path=/mnt/dvd &#8211;name=baz &#8211;arch=x86_64</code> </p>
<p> Example4: <code>cobbler import &#8211;path=/path/to/stuff &#8211;name=glorp</code> </p>
<p> Example5: <code>cobbler import &#8211;path=/path/where/filer/is/mounted &#8211;name=anyname &#8211;available-as=<a href="nfs://nfs.example.org:/where/mounted/">nfs://nfs.example.org:/where/mounted/</a></code> </p>
<p> Once imported, run a &#8220;cobbler list&#8221; or &#8220;cobbler report&#8221; to see what you&#8217;ve added. </p>
<p> By default, the rsync operations will exclude content of certain architectures, debug RPMs, and <font SIZE="-1">ISO</font> images &#8212; to change what is excluded during an import, see /etc/cobbler/rsync.exclude. </p>
<p> Note that all of the import commands will mirror install tree content into /var/www/cobbler unless a network accessible location is given with &#8211;available-as. &#8211;available-as will be primarily used when importing distros stored on an external <font SIZE="-1">NAS</font> box, or potentially on another partition on the same machine that is already accessible via http:// or <a href="ftp://.">ftp://.</a> </p>
<p> For import methods using rsync, additional flags can be passed to rsync with the option &#8211;rsync-flags. </p>
<p> Should you want to force the usage of a specific cobbler kickstart template for all profiles created by an import, you can feed the option &#8211;kickstart to import, to bypass the built-in kickstart auto-detection.</p>
<h3><font SIZE="-1">DEFAULT PXE BOOT BEHAVIOR</font></h3>
<p> What happens when <font SIZE="-1">PXE</font> booting a system when cobbler has no record of the system being booted? </p>
<p> By default, cobbler will configure <font SIZE="-1">PXE</font> to boot to the contents of /etc/cobbler/default.pxe, which (if unmodified) will just fall through to the local boot process. Administrators can modify this file if they like to change that behavior. </p>
<p> An easy way to specify a default cobbler profile to <font SIZE="-1">PXE</font> boot is to create a system named &#8220;default&#8221;. This will cause /etc/cobbler/default.pxe to be ignored. To restore the previous behavior do a &#8220;cobbler system remove&#8221; on the &#8220;default&#8221; system. </p>
<p> <code>cobbler system add &#8211;name=default &#8211;profile=boot_this</code> </p>
<p> <code>cobbler system remove &#8211;name=default</code> </p>
<p> As mentioned in earlier sections, it is also possible to control the default behavior for a specific network: </p>
<p> <code>cobbler system add &#8211;name=network1 &#8211;ip-address=192.168.0.0/24 &#8211;profile=boot_this</code></p>
<h3><font SIZE="-1">REPO MANAGEMENT</font></h3>
<p> This has already been covered a good bit in the command reference section. </p>
<p> Yum repository management is an optional feature, and is not required to provision through cobbler. However, if cobbler is configured to mirror certain repositories, it can then be used to associate profiles with those repositories. Systems installed under those profiles will then be autoconfigured to use these repository mirrors in /etc/yum.repos.d, and if supported (Fedora Core 6 and later) these repositories can be leveraged even within Anaconda. This can be useful if (A) you have a large install base, (B) you want fast installation and upgrades for your systems, or (C) have some extra software not in a standard repository but want provisioned systems to know about that repository. </p>
<p> Make sure there is plenty of space in cobbler&#8217;s webdir, which defaults to /var/www/cobbler. </p>
<p> <code>cobbler reposync [&#8211;tries=N] [&#8211;no-fail]</code> </p>
<p> Cobbler reposync is the command to use to update repos as configured with &#8220;cobbler repo add&#8221;. Mirroring can take a long time, and usage of cobbler reposync prior to usage is needed to ensure provisioned systems have the files they need to actually use the mirrored repositories. If you just add repos and never run &#8220;cobbler reposync&#8221;, the repos will never be mirrored. This is probably a command you would want to put on a crontab, though the frequency of that crontab and where the output goes is left up to the systems administrator. </p>
<p> For those familiar with yum&#8217;s reposync, cobbler&#8217;s reposync is (in most uses) a wrapper around the yum command. Please use &#8220;cobbler reposync&#8221; to update cobbler mirrors, as yum&#8217;s reposync does not perform all required steps. Also cobbler adds support for rsync and <font SIZE="-1">SSH</font> locations, where as yum&#8217;s reposync only supports what yum supports (http/ftp). </p>
<p> If you ever want to update a certain repository you can run: </p>
<p> <code>cobbler reposync &#8211;only=&#8220;reponame1&#8221; &#8230;</code> </p>
<p> When updating repos by name, a repo will be updated even if it is set to be not updated during a regular reposync operation (ex: cobbler repo edit &#8211;name=reponame1 &#8211;keep-updated=0). </p>
<p> Note that if a cobbler import provides enough information to use the boot server as a yum mirror for core packages, cobbler can set up kickstarts to use the cobbler server as a mirror instead of the outside world. If this feature is desirable, it can be turned on by setting yum_post_install_mirror to 1 in /etc/settings ((and running &#8220;cobbler sync&#8221;). You should not use this feature if machines are provisioned on a different VLAN/network than production, or if you are provisioning laptops that will want to acquire updates on multiple networks. </p>
<p> The flags &#8211;tries=N (for example, &#8211;tries=3) and &#8211;no-fail should likely be used when putting reposync on a crontab. They ensure network glitches in one repo can be retried and also that a failure to synchronize one repo does not stop other repositories from being synchronized.</p>
<h3><font SIZE="-1">PXE BOOT LOOP PREVENTION</font></h3>
<p> If you have your machines set to <font SIZE="-1">PXE</font> first in the boot order (ahead of hard drives), change the &#8220;pxe_just_once&#8221; flag in /etc/cobbler/settings to 1. This will set the machines to not <font SIZE="-1">PXE</font> on successive boots once they complete one install. To re-enable <font SIZE="-1">PXE</font> for a specific system, run the following command: </p>
<p> <code>cobbler system edit &#8211;name=name &#8211;netboot-enabled=1</code></p>
<h3><font SIZE="-1">KICKSTART TRACKING</font></h3>
<p> Cobbler knows how to keep track of the status of kickstarting machines. </p>
<p> <code>cobbler status</code> </p>
<p> Using the status command will show when cobbler thinks a machine started kickstarting and when it finished, provided the proper snippets are found in the kickstart template. This is a good way to track machines that may have gone interactive (or stalled/crashed) during kickstarts.</p>
<h3><font SIZE="-1">IMAGES</font></h3>
<p> Cobbler can help with booting images physically and virtually, though the usage of these commands varies substantially by the type of image. Non-image based deployments are generally easier to work with and lead to more sustaintable infrastructure. Some manual use of other commands beyond of what is typically required of cobbler may be needed to prepare images for use with this feature.</p>
<h3><font SIZE="-1">TRIGGERS</font></h3>
<p> Triggers provide a way to integrate cobbler with arbitrary 3rd party software without modifying cobbler&#8217;s code. When adding a distro, profile, system, or repo, all scripts in /var/lib/cobbler/triggers/add are executed for the particular object type. Each particular file must be executable and it is executed with the name of the item being added as a parameter. Deletions work similarly &#8212; delete triggers live in /var/lib/cobbler/triggers/delete. Order of execution is arbitrary, and cobbler does not ship with any triggers by default. There are also other kinds of triggers &#8212; these are described on the Cobbler Wiki. For larger configurations, triggers should be written in Python &#8212; in which case they are installed differently. This is also documented on the Wiki.</p>
<h3><font SIZE="-1">API</font></h3>
<p> Cobbler also makes itself available as an <font SIZE="-1">XMLRPC API</font> for use by higher level management software. Learn more at <a rel="nofollow" href="http://cobbler.github.io.">http://cobbler.github.io.</a></p>
<h3><font SIZE="-1">WEB USER INTERFACE</font></h3>
<p> Most of the day-to-day actions in cobbler&#8217;s command line can be performed in Cobbler&#8217;s Web <font SIZE="-1">UI. </font> To enable and access the WebUI, see the following documentation: </p>
<p> <a rel="nofollow" href="https://github.com/cobbler/cobbler/wiki/Cobbler-web-interface">https://github.com/cobbler/cobbler/wiki/Cobbler-web-interface</a></p>
<h3><font SIZE="-1">BOOT CD</font></h3>
<p> Cobbler can build all of it&#8217;s profiles into a bootable <font SIZE="-1">CD</font> image using the &#8220;cobbler buildiso&#8221; command. This allows for PXE-menu like bringup of bare metal in environments where <font SIZE="-1">PXE</font> is not possible. Another more advanced method is described in the koan manpage, though this method is easier and sufficient for most applications.</p>
<h3><font SIZE="-1">POWER MANAGEMENT</font></h3>
<p> Cobbler contains a power management feature that allows the user to associate system records in cobbler with the power management configuration attached to them. This can ease installation by making it easy to reassign systems to new operating systems and then reboot those systems. Read more about this feature at <a rel="nofollow" href="https://github.com/cobbler/cobbler/wiki/Power-management">https://github.com/cobbler/cobbler/wiki/Power-management</a></p>
<h3><font SIZE="-1">CONFIG MANAGEMENT INTEGRATION</font></h3>
<p> Cobbler contains features for integrating an installation environment with a configuration management system, which handles the configuration of the system after it is installed by allowing changes to configuration files and settings. You can read more about this feature at <a rel="nofollow" href="https://github.com/cobbler/cobbler/wiki/Built-in-configuration-management">https://github.com/cobbler/cobbler/wiki/Built-in-configuration-management</a> and <a href="https://github.com/cobbler/cobbler/wiki/Using-cobbler-with-a-configuration-management-system.">https://github.com/cobbler/cobbler/wiki/Using-cobbler-with-a-configuration-management-system.</a> Both features may be considered experimental as of time of the 1.4 release.</p>
<h2>EXIT_STATUS</h2>
<p> cobbler&#8217;s command line returns a zero for success and non-zero for failure.</p>
<h2>ADDITIONAL RESOURCES</h2>
<p> Cobbler has a mailing list for user and development-related questions/comments at cobbler [at] lists.fedorahosted.org. To subscribe, visit <a rel="nofollow" href="https://fedorahosted.org/mailman/listinfo/cobbler">https://fedorahosted.org/mailman/listinfo/cobbler</a> </p>
<p> <font SIZE="-1">IRC</font> channel: irc.freenode.net (#cobbler) </p>
<p> Official web site, bug tracker, and Wiki: <a rel="nofollow" href="http://cobbler.github.io.">http://cobbler.github.io.</a></p>
<h2>AUTHOR</h2>
<p> Michael DeHaan &lt;michael.dehaan <font SIZE="-1">AT</font> gmail&gt; </p>
<h2>Index</h2>
<dt><a href="#lbAM">MANAGEMENT RESOURCES</a></p>
<dd>
<dt><a href="#lbAW">EXAMPLES</a></p>
<dd>
<dt><a href="#lbBB">ADVANCED TOPICS</a></p>
<dd>
<dt><a href="#lbBV">EXIT_STATUS</a></p>
<dd>
<dt><a href="#lbBW">ADDITIONAL RESOURCES</a></p>
<dd>
<dt><a href="#lbBX">AUTHOR</a></p>
<dd></dl>
