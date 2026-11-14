---
title: "oz-examples(1)"
name: "oz-examples"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oz-examples/"
---

<h2 class="name">NAME</h2>
 

 oz-examples - example TDL files for Oz.

<h2>DESCRIPTION</h2>

 The <i><a HREF="/docs/linux/man/1-oz-install/">oz-install</a>(1)</i> , <i><a HREF="/docs/linux/man/1-oz-customize/">oz-customize</a>(1)</i> , and <i><a HREF="/docs/linux/man/1-oz-generate-icicle/">oz-generate-icicle</a>(1)</i> man pages explain the command-line usage of the Oz commands. One of the required input parameters to all of the above commands is a TDL (Template Description Language) file, which describes the OS the user wants to install, where to get the media from, and any additional packages or actions the user wants to take on the operating system. This man page describes a number of TDL examples and what happens when they are used. Since the TDL is XML, standard XPath notation is used to describe various elements of the XML. 

<h2>EXAMPLE 1 - Minimal guest</h2>

 Assume we want to install a minimal Fedora 13 x86_64 operating system from a Fedora 13 DVD ISO located at <a rel="nofollow" HREF="http://example.org/fedora-13-x86_64.iso">http://example.org/fedora-13-x86_64.iso</a> 

 To do this install we first build a TDL XML file, then feed it to oz-install. The TDL file would look like: 

 
&nbsp;<wbr>&lt;template&gt; 
&lt;name&gt;fedora13_x86_64&lt;/name&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;os&gt; 
&nbsp;<wbr>&lt;name&gt;Fedora&lt;/name&gt; 
&nbsp;<wbr>&lt;version&gt;13&lt;/version&gt; 
&nbsp;<wbr>&lt;arch&gt;x86_64&lt;/arch&gt; 
&nbsp;<wbr>&lt;install type='iso'&gt; 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&lt;iso&gt;<a rel="nofollow" HREF="http://example.org/fedora-13-x86_64.iso">http://example.org/fedora-13-x86_64.iso</a>&lt;/iso&gt; 
&nbsp;<wbr>&lt;/install&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;/os&gt; 
&lt;description&gt;My Fedora 13 x86_64 template&lt;/description&gt; 
&nbsp;<wbr>&lt;/template&gt; 

 /template/name is a user-defined name. This can be anything the user wants, but must be unique among all TDLs the user wants to build. 

 /template/os/name is the name of the operating system we want to install, /template/os/version is the version we want, and /template/os/arch is the architecture we want. A full list of supported operating systems can be obtained by running: 

<dl>
<dt>
<dd> # oz-install -h</dl>
 

 /template/os/install tells Oz where to get the installation media from. In this example, we set type to 'iso' which means that we need an &lt;iso&gt; element in the XML pointing to the ISO install media (install methods other than ISO are supported, and described in other examples). 

 /template/description is an optional, human-readable description of the template. This can be anything the user wants, and is ignored by Oz. 

 That's all of the input that Oz needs. To actually do the installation, save the above to a file (say fedora13.tdl), and then run oz-install: 

<dl>
<dt>
<dd> # oz-install /path/to/fedora13.tdl</dl>
 

 Running this command will download and prepare the installation media, then run an automated install in a KVM guest. Assuming the install succeeds, the minimal operating system will be installed on a file in /var/lib/libvirt/images/fedora13_x86_64.dsk (by default, the output location can be overridden in the configuration file). 

<h2>EXAMPLE 2 - Guest with additional packages</h2>

 Assume we want to install a Fedora 14 x86_64 operating system from a Fedora 14 DVD ISO located at <a rel="nofollow" HREF="http://example.org/fedora-14-x86_64.iso">http://example.org/fedora-14-x86_64.iso</a> 

 Additionally assume we want to install the postgresql-server package on the operating system. To do this install, we first need to build a TDL XML file and then feed that to oz-install. The TDL file would look like: 

 
&nbsp;<wbr>&lt;template&gt; 
&lt;name&gt;fedora14_postgres&lt;/name&gt; 
&lt;os&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;Fedora&lt;/name&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;version&gt;14&lt;/version&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;arch&gt;x86_64&lt;/arch&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;install type='iso'&gt; 
&nbsp;<wbr>&lt;iso&gt;<a rel="nofollow" HREF="http://example.org/fedora-14-x86_64.iso">http://example.org/fedora-14-x86_64.iso</a>&lt;/iso&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;/install&gt; 
&lt;/os&gt; 
&lt;description&gt;Fedora 14 x86_64 with postgres&lt;/description&gt; 
&lt;packages&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;package name='postgresql-server'/&gt; 
&lt;/packages&gt; 
&nbsp;<wbr>&lt;/template&gt; 

 Notice that this is very similar to Example 1, except we specified an additional package to be installed in the /packages/package portion of the TDL. Multiple packages can be specified here, and they will all be installed on the operating system. In this example, all packages are downloaded and installed from the default operating system package repositories. Running the installation is done the same way as in Example 1, except we have to add a command-line parameter to actually do the customization: 

<dl>
<dt>
<dd> # oz-install -u /path/to/fedora14.tdl</dl>
 

 Running this command will download and prepare the installation media, then run an automated install in a KVM guest. 

 Assuming the initial install succeeds, Oz will then boot the operating system and run native commands to install the additional packages. For more information about why this approach is used, please see the Oz Architecture document at <a rel="nofollow" HREF="http://github.com/clalancette/oz/wiki/Oz-architecture.">http://github.com/clalancette/oz/wiki/Oz-architecture.</a> 

 Assuming this final step succeeds, the operating system with the additional packages will be installed on a file in /var/lib/libvirt/images/fedora14_postgres.dsk (by default, the output location can be overridden in the configuration file). 

<h2>EXAMPLE 3 - Generate a package manifest (ICICLE) after installation</h2>

 Assume we want to install a RHEL-5 x86_64 operating system from a RHEL-5 DVD ISO located at <a rel="nofollow" HREF="http://example.org/rhel-5-x86_64.iso">http://example.org/rhel-5-x86_64.iso</a> 

 Additionally assume we want to get a package manifest out of the operating system after the install is done. To do this install, we first need to build a TDL XML file and then feed that to oz-install. The TDL file would look like: 

 
&nbsp;<wbr>&lt;template&gt; 
&lt;name&gt;rhel5_x86_64&lt;/name&gt; 
&lt;os&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;RHEL-5&lt;/name&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;version&gt;U6&lt;/version&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;arch&gt;x86_64&lt;/arch&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;install type='iso'&gt; 
&nbsp;<wbr>&lt;iso&gt;<a rel="nofollow" HREF="http://example.org/rhel-5-x86_64.iso">http://example.org/rhel-5-x86_64.iso</a>&lt;/iso&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;/install&gt; 
&lt;/os&gt; 
&lt;description&gt;RHEL-5 x86_64&lt;/description&gt; 
&nbsp;<wbr>&lt;/template&gt; 

 This is essentially the same as Example 1, except we want to install RHEL-5 instead of Fedora-13. 

 Running the installation is done the same was as in Example 1, except we have to add a command-line parameter to generate the manifest at the end: 

<dl>
<dt>
<dd> # oz-install -g /path/to/rhel5.tdl</dl>
 

 Running this command will download and prepare the installation media, then run an automated install in a KVM guest. 

 Assuming the initial install succeeds, Oz will then boot the operating system and run native commands to query all of the packages in the system. It will then output an XML document (called an ICICLE) describing the entire manifest. 

 Assuming this step succeeds, the minimal operating system will be install on a file in /var/lib/libvirt/images/rhel5_x86_64.dsk (by default, the output location can be overridden in the configuration file). 

<h2>EXAMPLE 4 - Install a package from an alternate repository</h2>

 Assume we want to install a RHEL-6 x86_64 operating system from a RHEL-6 DVD ISO located at <a rel="nofollow" HREF="http://example.org/rhel-6-x86_64.iso">http://example.org/rhel-6-x86_64.iso</a> 

 Additionally assume that we want to install the ccache package from the EPEL-6 repositories on the operating system. To do this install, we first need to build a TDL XML file and then feed that to oz-install. The TDL file would look like: 

 
&nbsp;<wbr>&lt;template&gt; 
&lt;name&gt;rhel6_ccache&lt;/name&gt; 
&lt;os&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;RHEL-6&lt;/name&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;version&gt;1&lt;/version&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;arch&gt;x86_64&lt;/arch&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;install type='iso'&gt; 
&nbsp;<wbr>&lt;iso&gt;<a rel="nofollow" HREF="http://example.org/rhel-6-x86_64.iso">http://example.org/rhel-6-x86_64.iso</a>&lt;/iso&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;/install&gt; 
&lt;/os&gt; 
&lt;description&gt;RHEL-6 x86_64 with ccache&lt;/description&gt; 
&lt;repositories&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;repository name='epel-6'&gt; 
&nbsp;<wbr>&lt;url&gt;<a rel="nofollow" HREF="http://download.fedoraproject.org/pub/epel/6/$basearch">http://download.fedoraproject.org/pub/epel/6/$basearch</a>&lt;/url&gt; 
&nbsp;<wbr>&lt;signed&gt;yes&lt;/signed&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;/repository&gt; 
&lt;/repositories&gt; 
&lt;packages&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;package name='ccache'/&gt; 
&lt;/packages&gt; 
&nbsp;<wbr>&lt;/template&gt; 

 Notice that this is very similar to Example 2, except we have specified an additional repository from which to download packages. The /repositories/repository section of the TDL specified the URL to the package repository along with whether the packages in the repository are signed. Running the installation is done the same way as in Example 2: 

<dl>
<dt>
<dd> # oz-install -u /path/to/rhel6_ccache.tdl</dl>
 

 Running this command will download and prepare the installation media, then run an automated install in a KVM guest. 

 Assuming the initial install succeeds, Oz will then boot the operating system and run native commands to setup the additional repositories and install the additional packages. For more information about why this approach is used, please see the Oz Architecture document at <a rel="nofollow" HREF="http://github.com/clalancette/oz/wiki/Oz-architecture.">http://github.com/clalancette/oz/wiki/Oz-architecture.</a> 

 Assuming this final step succeeds, the operating system with the additional packages will be installed on a file in /var/lib/libvirt/images/rhel6_ccache.dsk (by default, the output location can be overridden in the configuration file). 

<h2>EXAMPLE 5 - Install a custom file from information in the TDL</h2>

 Assume we want to install a RHEL-6 x86_64 operating system from a RHEL-6 DVD ISO located at <a rel="nofollow" HREF="http://example.org/rhel-6-x86_64.iso">http://example.org/rhel-6-x86_64.iso</a> 

 Additionally assume that we want to write some data to the file /etc/test.out inside the guest. To do this install, we first need to build a TDL XML file and then feed that to oz-install. The TDL file would look like: 

 
&nbsp;<wbr>&lt;template&gt; 
&lt;name&gt;rhel6_testout&lt;/name&gt; 
&lt;os&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;RHEL-6&lt;/name&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;version&gt;1&lt;/version&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;arch&gt;x86_64&lt;/arch&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;install type='iso'&gt; 
&nbsp;<wbr>&lt;iso&gt;<a rel="nofollow" HREF="http://example.org/rhel-6-x86_64.iso">http://example.org/rhel-6-x86_64.iso</a>&lt;/iso&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;/install&gt; 
&lt;/os&gt; 
&lt;description&gt;RHEL-6 x86_64 with test.out&lt;/description&gt; 
&lt;files&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;file name='/etc/test.out'&gt;THIS=extra_data&lt;/file&gt; 
&lt;/files&gt; 
&nbsp;<wbr>&lt;/template&gt; 

 Multiple files can be specified here, and they will all be installed on the operating system in the specified locations. Files can be specified inline in raw text in the TDL, as base64 encoded data in the TDL, or as URLs. We need to run the installation with customization for this to work: 

<dl>
<dt>
<dd> # oz-install -u /path/to/rhel6_testout.tdl</dl>
 

 Running this command will download and prepare the installation media, then run an automated install in a KVM guest. 

 Assuming the initial install succeeds, Oz will then boot the operating system and run native commands to upload the files specified in the TDL. For more information about why this approach is used, please see the Oz Architecture document at <a rel="nofollow" HREF="http://github.com/clalancette/oz/wiki/Oz-architecture.">http://github.com/clalancette/oz/wiki/Oz-architecture.</a> 

 Assuming this final step succeeds, the operating system with the additional files will be installed on a file in /var/lib/libvirt/images/rhel6_testout.dsk (by default, the output location can be overridden in the configuration file). 

<h2>EXAMPLE 6 - Install a custom file from base64-encoded information in the TDL</h2>

 Assume we want to install a RHEL-6 x86_64 operating system from a RHEL-6 DVD ISO located at <a rel="nofollow" HREF="http://example.org/rhel-6-x86_64.iso">http://example.org/rhel-6-x86_64.iso</a> 

 Additionally assume that we want to write some data to the file /etc/test.out inside the guest. Since this data may be binary, we want to base64 encode it first. To do this install, we first need to build a TDL XML file and then feed that to oz-install. The TDL file would look like: 

 
&nbsp;<wbr>&lt;template&gt; 
&lt;name&gt;rhel6_testout&lt;/name&gt; 
&lt;os&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;RHEL-6&lt;/name&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;version&gt;1&lt;/version&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;arch&gt;x86_64&lt;/arch&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;install type='iso'&gt; 
&nbsp;<wbr>&lt;iso&gt;<a rel="nofollow" HREF="http://example.org/rhel-6-x86_64.iso">http://example.org/rhel-6-x86_64.iso</a>&lt;/iso&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;/install&gt; 
&lt;/os&gt; 
&lt;description&gt;RHEL-6 x86_64 with test.out&lt;/description&gt; 
&lt;files&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;file name='/etc/test.out'&nbsp;<wbr>type='base64'&gt;VEhJUz1leHRyYV9kYXRhCg==&lt;/file&gt; 
&lt;/files&gt; 
&nbsp;<wbr>&lt;/template&gt; 

 Multiple files can be specified here, and they will all be installed on the operating system in the specified locations. Files can be specified inline in raw text in the TDL, as base64 encoded data in the TDL, or as URLs. We need to run the installation with customization for this to work: 

<dl>
<dt>
<dd> # oz-install -u /path/to/rhel6_testout.tdl</dl>
 

 Running this command will download and prepare the installation media, then run an automated install in a KVM guest. 

 Assuming the initial install succeeds, Oz will then boot the operating system and run native commands to upload the files specified in the TDL. For more information about why this approach is used, please see the Oz Architecture document at <a rel="nofollow" HREF="http://github.com/clalancette/oz/wiki/Oz-architecture.">http://github.com/clalancette/oz/wiki/Oz-architecture.</a> 

 Assuming this final step succeeds, the operating system with the additional files will be installed on a file in /var/lib/libvirt/images/rhel6_testout.dsk (by default, the output location can be overridden in the configuration file). 

<h2>EXAMPLE 7 - Install a custom file from a URL</h2>

 Assume we want to install a RHEL-6 x86_64 operating system from a RHEL-6 DVD ISO located at <a rel="nofollow" HREF="http://example.org/rhel-6-x86_64.iso">http://example.org/rhel-6-x86_64.iso</a> 

 Additionally assume that we want to write some data to the file /etc/test.out inside the guest. We want to fetch this data from a URL and upload into the guest. To do this install, we first need to build a TDL XML file and then feed that to oz-install. The TDL file would look like: 

 
&nbsp;<wbr>&lt;template&gt; 
&lt;name&gt;rhel6_testout&lt;/name&gt; 
&lt;os&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;name&gt;RHEL-6&lt;/name&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;version&gt;1&lt;/version&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;arch&gt;x86_64&lt;/arch&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;install type='iso'&gt; 
&nbsp;<wbr>&lt;iso&gt;<a rel="nofollow" HREF="http://example.org/rhel-6-x86_64.iso">http://example.org/rhel-6-x86_64.iso</a>&lt;/iso&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;/install&gt; 
&lt;/os&gt; 
&lt;description&gt;RHEL-6 x86_64 with test.out&lt;/description&gt; 
&lt;files&gt; 
&nbsp;<wbr>&nbsp;<wbr>&lt;file name='/etc/test.out'&nbsp;<wbr>type='url'&gt;<a rel="nofollow" HREF="http://example.org/orig.out">http://example.org/orig.out</a>&lt;/file&gt; 
&lt;/files&gt; 
&nbsp;<wbr>&lt;/template&gt; 

 Multiple files can be specified here, and they will all be installed on the operating system in the specified locations. Files can be specified inline in raw text in the TDL, as base64 encoded data in the TDL, or as URLs. We need to run the installation with customization for this to work: 

<dl>
<dt>
<dd> # oz-install -u /path/to/rhel6_testout.tdl</dl>
 

 Running this command will download and prepare the installation media, then run an automated install in a KVM guest. 

 Assuming the initial install succeeds, Oz will then boot the operating system and run native commands to upload the files specified in the TDL. For more information about why this approach is used, please see the Oz Architecture document at <a rel="nofollow" HREF="http://github.com/clalancette/oz/wiki/Oz-architecture.">http://github.com/clalancette/oz/wiki/Oz-architecture.</a> 

 Assuming this final step succeeds, the operating system with the additional files will be installed on a file in /var/lib/libvirt/images/rhel6_testout.dsk (by default, the output location can be overridden in the configuration file). 

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/1-oz-install/">oz-install</a>(1), <a HREF="/docs/linux/man/1-oz-generate-icicle/">oz-generate-icicle</a>(1), <a HREF="/docs/linux/man/1-oz-customize/">oz-customize</a>(1), <a HREF="/docs/linux/man/1-oz-cleanup-cache/">oz-cleanup-cache</a>(1) 

<h2>AUTHOR</h2>

 Chris Lalancette &lt;clalancette [at] gmail.com&gt; 

<h2>Index</h2>


