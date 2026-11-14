---
title: "oz-customize(1)"
name: "oz-customize"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oz-customize/"
description: "oz-customize – tool to automatically modify installed operating system files"
---

<h2 class="name">NAME</h2>
<p> oz-customize &#8211; tool to automatically modify installed operating system files</p>
<h2>SYNOPSIS</h2>
<p> <code>oz-customize [OPTIONS] &lt;tdl-file&gt; &lt;libvirt-xml-file&gt;</code> </p>
<h2>DESCRIPTION</h2>
<p> This is a tool to modify already installed operating systems. Modifications typically involve installing additional packages. This program can be used as a counterpart to oz-install, though it does not have to be used in conjunction. </p>
<p> Note that oz-customize does the actual customization using a combination of KVM and libvirt, so both of these must be available (and working) for oz-customize to have a chance to succeed. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c &lt;config&gt;</code></p>
<dd> Get the configuration from config file <code>config</code>, instead of the default /etc/oz/oz.cfg. If neither one exists, Oz will use sensible defaults. The config file is in standard ini format; for an explanation of the sections and keys, see the <code>CONFIGURATION FILE</code> section.</p>
<dt><code>-d &lt;loglevel&gt;</code></p>
<dd> Turn on debugging output to level <code>loglevel</code>. The log levels are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0 &#8211; errors only (this is the default)</p>
<dd>
<dt>1 &#8211; errors and warnings</p>
<dd>
<dt>2 &#8211; errors, warnings, and information</p>
<dd>
<dt>3 &#8211; all messages</p>
<dd>
<dt>4 &#8211; all messages, prepended with the level and classname</p>
<dd></dl>
</dl>
<dt><code>-h</code></p>
<dd> Print a short help message. </p>
</dl>
<h2>CONFIGURATION FILE</h2>
<p> The Oz configuration file is in standard INI format with several sections. If any section or configuration key is missing, Oz will use a sensible default. For true/false configuration keys, the values of &quot;true&quot;, &quot;True&quot;, &quot;yes&quot;, or &quot;Yes&quot; can be used to turn the option on, and &quot;false&quot;, &quot;False&quot;, &quot;no&quot;, or &quot;No&quot; can be used to turn the behavior off. The configuration file should have the following form: </p>
<pre><code>
[paths] output_dir = / var / lib / libvirt / images data_dir = / var / lib / oz screenshot_dir =.sshprivkey = / etc / oz / id_rsa - icicle - gen[libvirt] uri = qemu : /// system
                                                                                                                                                                       type = kvm
                                                                                                                                                                           bridge_name = virbr0
                                                                                                                                                                               cpus = 1 memory = 1024 image_type = raw
                                                                                                                                                                                   [cache] original_media = yes
                                                                                                                                                                                       modified_media = no
                                                                                                                                                                                           jeos = no
                                                                                                                                                                                               [icicle] safe_generation = no
</code></pre>
<p> The <code>paths</code> section defines the paths that Oz will use for storing data. The <code>output_dir</code> key describes where to store the images after they are built, and the <code>data_dir</code> key describes where to cache install media and use temporary storage. Both locations must have a decent amount of free disk space in order for Oz to work properly. The <code>screenshot_dir</code> key describes where to store screenshots of failed installs. The <code>sshprivkey</code> key describes where the ssh keys are stored, which are required by Oz to do customization of the image. </p>
<p> The <code>libvirt</code> section allows some manipulation of how Oz uses libvirt. The <code>uri</code> key describes the libvirt URI to use to do the guest installation. The <code>type</code> key defines what type of virtualization to use. The <code>bridge_name</code> key defines which bridge Oz should place the guests that it launches on. The <code>cpus</code> key defines how many cpus should be used inside the virtual machine. The <code>memory</code> key defines how much memory (in megabytes) should be used inside the virtual machine. The <code>image_type</code> key defines which output disk type should be used; this can be any value that libvirt supports. </p>
<p> The <code>cache</code> section allows some manipulation of how Oz caches data. The caching of data in Oz is a tradeoff between installation time and storage space. The <code>original_media</code> key tells Oz to cache the original installation media so that it does not have to download it the next time an install for the same operating system is requested. The <code>modified_media</code> key tells Oz to cache the oz-modified installation media so that it does not have to download and modify it the next time an install for the same operating system is requested. The <code>jeos</code> key tells Oz to cache the installed operating system after installation. This can significantly speed up subsequent installation of the same operating system, with the additional downside of the operating system getting out-of-date with respect to security updates. Use with care. </p>
<p> The <code>icicle</code> section allows some manipulation of how Oz generates ICICLE output. ICICLE is a package manifest that can optionally be generated at the end of installs. The <code>safe_generation</code> key controls whether Oz uses a throwaway overlay file while generating the ICICLE. If it is set to &quot;no&quot; (the default), then Oz will boot up the guest at the end of the install and run the appropriate commands to generate the ICICLE. If it is set to &quot;yes&quot;, then Oz will use a throwaway overlay file while generating the ICICLE. After the ICICLE is generated, Oz will delete the backing file, leaving the original disk image pristine. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-oz-generate-icicle/">oz-generate-icicle</a>(1), <a href="/docs/linux/man/1-oz-install/">oz-install</a>(1), <a href="/docs/linux/man/1-oz-cleanup-cache/">oz-cleanup-cache</a>(1), <a href="/docs/linux/man/1-oz-examples/">oz-examples</a>(1) </p>
<h2>AUTHOR</h2>
<p> Chris Lalancette &lt;clalancette [at] gmail.com&gt; </p>
<h2>Index</h2>
