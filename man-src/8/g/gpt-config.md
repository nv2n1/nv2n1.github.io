---
title: "gpt-config(8)"
name: "gpt-config"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt-config/"
description: "gpt-config – Configure the current installation of GPT"
---

<p><code>gpt-config</code> &#8211; Configure the current installation of GPT</p>
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
<p><code>gpt-config</code> is a runtime configuration script that is used to localize a GPT installation. GPT uses various programs and packaging parameters to do its job. These items can be listed and modified by this script. </p>
<p> Configuration information for GPT is stored in the module <tt>$GPT_LOCATION</tt>/lib/perl/Grid/GPT/LocalEnv.pm. This module is regenerated when gpt-config is used to change the configuration.</p>
<h2>Options</h2>
<dl>
<dt><i>-builddir</i></dt>
<dd>Specifies the where the source tar files should be untarred and the code is built.</dd>
<dt><i>-location</i></dt>
<dd>
</dd><dt><i>-perl</i></dt>
<dd>
</dd><dt><i>-gtar</i></dt>
<dd>
</dd><dt><i>-gunzip</i></dt>
<dd>
</dd><dt><i>-gmake</i></dt>
<dd>
</dd><dt><i>-rpm</i></dt>
<dd>
</dd><dt><i>-rpmbuild</i></dt>
<dd>Location of various programs that GPT uses. These switches will override any searching done by the -probe switch..</dd>
<dt><i>-license</i></dt>
<dd>
</dd><dt><i>-vendor</i></dt>
<dd>
</dd><dt><i>-ftpsite</i></dt>
<dd>
</dd><dt><i>-url</i></dt>
<dd>
</dd><dt><i>-packager</i></dt>
<dd>
</dd><dt><i>-prefix</i></dt>
<dd>Values that are used by GPT when generating RPM packages. These values are not configured when the platform does not support RPM.</dd>
<dt><i>-list</i></dt>
<dd>List the current configuration.</dd>
<dt><i>-probe</i></dt>
<dd>Probe for the various programs that GPT needs. The probe examines each directory listed in the $PATH variable for these programs.</dd>
<dt><i>-use-archive-tar</i></dt>
<dd>Skip the probes for a system tar and unzip programs. Use Archive::Tar module to untar source packages. Using this modules slows down the build noticably.</dd>
<dt><i>-ignore</i></dt>
<dd>Ignore any missing programs and continue with the configuring.</dd></dl>
<h2>Author</h2>
<p>Written by Chase Phillips and Michael Bletzinger.</p>
