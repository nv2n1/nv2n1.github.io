---
title: "check_updates(1)"
name: "check_updates"
section: "1"
letter: "c"
url: "/docs/linux/man/1-check_updates/"
---

<h2 class="name">NAME</h2>
 

 &quot;check_updates&quot; - a Nagios plugin to check if Red Hat or Fedora system is up-to-date 

<h2>DESCRIPTION</h2>

 check_updates is a Nagios plugin to check if Red Hat or Fedora system is up-to-date

<h2>VERSION</h2>

 Version 1.6.18

<h2>SYNOPSIS</h2>

 <pre><code>
check_updates[OPTIONS] - ?, --usage Print usage information - h, --help Print detailed help screen - V, --version Print version information-- extra - opts = [&lt;section&gt;[@&lt;config_file&gt;]] Section and / or config_file from which to load extra options(may repeat)-- boot - check Check if the machine was booted with the newest kernel(default)-- boot - check - warning Like-- boot - check but state is warning instead of critical-- no - boot - check Do not complain if the machine was booted with an old kernel-- clean Cleans YUM / DNF caches - w, --warning = INTEGER Exit with WARNING status if more than INTEGER updates are available - c, --critical = INTEGER Exit with CRITICAL status if more than INTEGER updates are available-- security - only Ignores non - security updates - a, --yum - arguments = STRING specific Yum arguments as STRING - t, --timeout = INTEGER Seconds before plugin times out(default : 15) - v, --verbose Show details for command - line debugging(can repeat up to 3 times)
</code></pre>

<h2>OPTIONS</h2>

 <pre><code>
- ?, --usage Print usage information - h, --help Print detailed help screen - V, --version Print version information-- extra - opts =
                                                                                     [&lt;section&gt;[@&lt;config_file&gt;]
] Section and / or config_file from which to load extra options(may repeat)-- boot - check Check if the machine was booted with the newest kernel(default)-- boot - check - warning Like-- boot - check but state is warning instead of critical-- no - boot - check Do not complain if the machine was booted with an old kernel-- clean Cleans YUM / DNF caches - w,
                                                                                                                               --warning = INTEGER Exit with WARNING status if more than INTEGER non - security updates are available - c, --critical = INTEGER Exit with CRITICAL status if more than INTEGER non - security updates are available-- security - only Ignores non - security updates - a, --yum - arguments = STRING Specifies additional arguments for Yum.Arguments containing spaces must be quoted(e.g., ./ check_updates - a "-d 20") - t, --timeout = INTEGER Seconds before plugin times out(default:15) - v, --verbose Show details for command - line debugging(can repeat up to 3 times)
</code></pre> 

 Security updates always force a <font SIZE="-1">CRITICAL</font> state

<h2>SECURITY UPDATES</h2>

 If yum's security plugin is available

<h2>EXAMPLE</h2>

 check_updates 

 check_updates checks if the system is up-to-date

<h2>DIAGNOSTICS</h2>

 You can specify multiple --verbose options to increase the program verbosity.

<h2>EXIT STATUS</h2>

 0 if <font SIZE="-1">OK, 1</font> in case of a warning, 2 in case of a critical status and 3 in case of an unkown problem

<h2>DEPENDENCIES</h2>

 check_updates depends on
<dl>
<dt>&bull;
<dd> Carp
<dt>&bull;
<dd> English
<dt>&bull;
<dd> Getopt::Long
<dt>&bull;
<dd> Monitoring::Plugin
<dt>&bull;
<dd> Monitoring::Plugin::Getopt
<dt>&bull;
<dd> Monitoring::Plugin::Threshold
<dt>&bull;
<dd> <font SIZE="-1">POSIX</font>
<dt>&bull;
<dd> Readonly</dl>

<h2>INCOMPATIBILITIES</h2>

 None reported.

<h2>SEE ALSO</h2>

 Nagios documentation

<h2>BUGS AND LIMITATIONS</h2>

 Some versions of you deliver a wrong number of secuirty updates. For example 

 <pre>
        $ yum --security  check-update
        Loaded plugins: downloadonly, product-id, rhnplugin, security
        This system is receiving updates from RHN Classic or RHN Satellite.
        Limiting package lists to security relevant ones
        No packages needed for security; 7 packages available
        mysql-libs.i686                                  5.1.73-5.el6_6                                   rhel-x86_64-server-6
</pre> 

 Either is mysql-libs a secuirity update (and the text should report it) or the package is wrongly listed. If yum delivers a wrong count, the pluging will do the same. 

 Please report any bugs or feature requests to matteo [at] corti.li, or through the web interface at <a rel="nofollow" HREF="https://github.com/matteocorti/check_updates/issues">https://github.com/matteocorti/check_updates/issues</a> 

 Be sure to include the output produced by the plugin with the --verbose option: 

 <pre>
  check_updates -v -v -v
</pre>

<h2>AUTHOR</h2>

 Matteo Corti &lt;matteo [at] corti.li&gt;

<h2>LICENSE AND COPYRIGHT</h2>

 Copyright (c) 2007-2016, Matteo Corti 

 This module is free software; you can redistribute it and/or modify it under the terms of <font SIZE="-1">GNU</font> general public license (gpl) version 3 or (at your option) any later version. See the <font SIZE="-1">LICENSE</font> file for details.

<h2>DISCLAIMER OF WARRANTY</h2>

 <font SIZE="-1">BECAUSE THIS SOFTWARE IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY FOR THE SOFTWARE, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE SOFTWARE ``AS IS'' WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE SOFTWARE IS WITH YOU. SHOULD THE SOFTWARE PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR, OR CORRECTION.</font> 

 <font SIZE="-1">IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MAY MODIFY AND/OR REDISTRIBUTE THE SOFTWARE AS PERMITTED BY THE ABOVE LICENCE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE SOFTWARE </font>(<font SIZE="-1">INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE SOFTWARE TO OPERATE WITH ANY OTHER SOFTWARE</font>), <font SIZE="-1">EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.</font>

<h2>ACKNOWLEDGMENTS</h2>

 Many thanks to:
<dl>
<dt>&bull;
<dd> Peter Bircher &amp; Cristian Tuduce for several bug fixes
<dt>&bull;
<dd> Mark Greenheigh for the prompt and precise bug reports
<dt>&bull;
<dd> Jose Pedro Oliveria for the build and release fixes
<dt>&bull;
<dd> Tomas Edwardsson for a patch fixing the detection of <font SIZE="-1">RH EL 6</font> systems
<dt>&bull;
<dd> Cott Lang for the Amazon Linux patch
<dt>&bull;
<dd> Joop Boonen for the yum arguments patch
<dt>&bull;
<dd> Franky Van Liedekerke for the perfomance data and security plugin patch and for the openvz kernels patch
<dt>&bull;
<dd> Andreas Dijkman for the Oracle <font SIZE="-1">UEK</font> patch
<dt>&bull;
<dd> PhiBo (<a rel="nofollow" HREF="https://github.com/phibos)">https://github.com/phibos)</a> for the --boot-check-warning patch 

</dl>

<h2>Index</h2>


