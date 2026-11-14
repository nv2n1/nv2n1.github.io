---
title: "gpt-config(8)"
name: "gpt-config"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt-config/"
description: "gpt-config – Configure the current installation of GPT"
---

<p><code>gpt-config</code> &#8211; Configure the current installation of <font SIZE="-1">GPT</font></p>
<h2>Synopsis</h2>
<p><code>gpt-config</code> [options] </p>
<pre> Help-Related Options:
 --help brief help message
 --man full documentation
 --location location of the GPT installation
 --perl location of the perl program
 --gtar location of the GNU tar program
 --gunzip location of the GNU unzip program
 --gmake location of the GNU make program
 --rpm location of the rpm program
 --rpm location of the rpmbuild program
 --license value used for the software license in RPM packages
 --vendor value used for the software vendor in RPM packages
 --ftpsite value used for the software ftp site in RPM packages
 --url value used for the URL for the software in RPM packages
 --packager value used for the packager of the RPM packages
 --prefix value used for the installation directory of RPM packages
 --use-archive-tar Use the Archive::Tar module instead of the system tar program
 --list list the current configuration
 --probe probe for the various programs that GPT needs
 --ignore ignore any missing programs</pre>
<h2>Description</h2>
<p><code>gpt-config</code> is a runtime configuration script that is used to localize a <font SIZE="-1">GPT</font> installation. <font SIZE="-1">GPT</font> uses various programs and packaging parameters to do its job. These items can be listed and modified by this script. </p>
<p> Configuration information for <font SIZE="-1">GPT</font> is stored in the module <tt>$GPT_LOCATION</tt>/lib/perl/Grid/GPT/LocalEnv.pm. This module is regenerated when gpt-config is used to change the configuration.</p>
<h2>Options</h2>
<dl>
<dt><i>-builddir</i></p>
<dd>Specifies the where the source tar files should be untarred and the code is built.</p>
<dt><i>-location</i></p>
<dd>
<dt><i>-perl</i></p>
<dd>
<dt><i>-gtar</i></p>
<dd>
<dt><i>-gunzip</i></p>
<dd>
<dt><i>-gmake</i></p>
<dd>
<dt><i>-rpm</i></p>
<dd>
<dt><i>-rpmbuild</i></p>
<dd>Location of various programs that <font SIZE="-1">GPT</font> uses. These switches will override any searching done by the -probe switch..</p>
<dt><i>-license</i></p>
<dd>
<dt><i>-vendor</i></p>
<dd>
<dt><i>-ftpsite</i></p>
<dd>
<dt><i>-url</i></p>
<dd>
<dt><i>-packager</i></p>
<dd>
<dt><i>-prefix</i></p>
<dd>Values that are used by <font SIZE="-1">GPT</font> when generating <font SIZE="-1">RPM</font> packages. These values are not configured when the platform does not support <font SIZE="-1">RPM</font>.</p>
<dt><i>-list</i></p>
<dd>List the current configuration.</p>
<dt><i>-probe</i></p>
<dd>Probe for the various programs that <font SIZE="-1">GPT</font> needs. The probe examines each directory listed in the $PATH variable for these programs.</p>
<dt><i>-use-archive-tar</i></p>
<dd>Skip the probes for a system tar and unzip programs. Use Archive::Tar module to untar source packages. Using this modules slows down the build noticably.</p>
<dt><i>-ignore</i></p>
<dd>Ignore any missing programs and continue with the configuring.</dl>
<h2>Author</h2>
<p>Written by Chase Phillips and Michael Bletzinger.</p>
