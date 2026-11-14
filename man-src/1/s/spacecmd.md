---
title: "spacecmd(1)"
name: "spacecmd"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spacecmd/"
description: "spacecmd – a command-line interface to Spacewalk and Satellite servers"
---

<h2>NAME</h2>
<p> spacecmd &#8211; a command-line interface to Spacewalk and Satellite servers</p>
<h2>SYNOPSIS</h2>
<p> <code>spacecmd</code> [<i>options</i>] [<i>command</i>]</p>
<h2>OVERVIEW</h2>
<pre>
spacecmd is a command-line interface to Spacewalk and Satellite servers.
It is written in Python and uses the XML-RPC API provided by the server.
Nearly all aspects of the Satellite can be managed by spacecmd.  These
include managing systems, software channels, configuration channels,
activation keys, Kickstarts and users.
spacecmd can be run as an interactive shell by running it without a
command.  It can also run a single command by passing the command
and the required arguments on the command line.
Run 'spacecmd help' to list the actions that are availble.
Run 'spacecmd -- &lt;command&gt; --help' to get help for a particular command.
</pre>
<h2>RUNNING SINGLE COMMANDS</h2>
<pre>
When running spacecmd non-interactively, you must take care to escape
arguments passed to the spacecmd functions.  This involves putting a '--'
before the command starts so that the arguments to the function are not
treated as global arguments to spacecmd.  You must also escape any quotes
that you pass to the functions so that the shell does not interpret them.
<code>Example:</code>
spacecmd -s server1 -- softwarechannel_create -n \'My Channel\' \
                                              -l channel1 \
                                              -a x86_64
</pre>
<h2>OPTIONS</h2>
<dl>
<dt><code>-u USERNAME, &#8211;username=USERNAME</code></p>
<dd> use this username to connect to the server</p>
<dt><code>-p PASSWORD, &#8211;password=PASSWORD</code></p>
<dd> use this password to connect to the server</p>
<dt><code>-s SERVER, &#8211;server=SERVER</code></p>
<dd> connect to this server [default: localhost]</p>
<dt><code>&#8211;nossl</code></p>
<dd> use HTTP instead of HTTPS</p>
<dt><code>&#8211;nohistory</code></p>
<dd> do not store command history</p>
<dt><code>-y, &#8211;yes</code></p>
<dd> answer yes for all questions</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> print only error messages</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> print debug messages</p>
<dt><code>-h, &#8211;help</code></p>
<dd> show this help message and exit</dl>
<h2>CONFIGURATION FILES</h2>
<pre>
Configuration files are loaded from /etc/spacecmd.conf and ~/.spacecmd/config.
The default section is [spacecmd].  It can then be overridden with server
specific sections.  Command-line arguments always override options in the
configuration files.
</pre>
<pre><code>
[spacecmd] server = localhost
    username = admin
        password = redhat
            nossl = 0
                [satellite.example.com] username = joe
                    password = secret
                        nossl = 1
</code></pre>
<h2>EXAMPLES</h2>
<p> <code>Make temporary groups on-the-fly</code> </p>
<pre>
spacecmd&gt; ssm_add search:driver:bnx2
Systems Selected: 111
spacecmd&gt; ssm_add search:device:vmware
Systems Selected: 285
spacecmd&gt; ssm_add search:hostname:external.example.com
Systems Selected: 16
</pre>
<p> <code>Add and remove packages from the commandline</code><br />
[user @sat] $ spacecmd &#8211; y system_installpackage www *mod_python Scheduled 6 system(s)[user @sat] $ spacecmd &#8211; y system_removepackage wiki02 mod_perl Scheduled 1 system(s)</p>
<p> <code>Schedule reboots from the commandline</code><br />
[user @sat] $ spacecmd &#8211; y&#8211; system_reboot ldap * -s + 6h Start Time : 20160106T07 : 01 : 00 Systems&#8211; &#8212; &#8212; -ldap01 ldap02 ldap03[user @sat] $ spacecmd &#8211; y system_reboot www01 Start Time : 20160106T02 : 01 : 00 Systems&#8211; &#8212; &#8212; -www01</p>
<p> <code>Apply errata from the command line</code><br />
[user @sat] $ spacecmd &#8211; y errata_apply RHSA &#8211; 2010 : 0423 Scheduled 42 system(s)[user @sat] $ spacecmd &#8211; y system_applyerrata group : web_servers RHSA &#8211; 2010 : 0040 Scheduled 16 system(s)</p>
<p> <code>Quickly generate reports</code> </p>
<pre><code>
spacecmd &gt; system_listerrata ldap03
                   System : ldap03
                                Security Errata : RHSA -
                                                  2010 : 0458 Moderate : perl security update 6 / 7 / 10 RHSA - 2010 : 0449 Moderate : rhn - client - tools security update 6 / 1 / 10 RHSA - 2010 : 0423 Important : krb5 security update 5 / 18 / 10 spacecmd &gt;
    report_errata
#Systems Errata
        -- -- -- -- - -- -- --CLA -
        2010 : 0474 88 CLA - 2010 : 0475 6 CLA - 2010 : 0488 183 CLA - 2010 : 0490 273 CLA - 2010 : 0500 4 CLA - 2010 : 0501 5 RHBA - 2010 : 0402 1 RHSA - 2010 : 0474 2 RHSA - 2010 : 0488 1 RHSA - 2010 : 0490 5 spacecmd &gt;
    report_outofdatesystems
        System Packages-- -- -- -- -- -- --monkey 310 shark 63 hedgehog 39 pomeranian 4 spacecmd &gt; report_ipaddresses
                                                                                                       System Hostname IP-- -- -- -- -- -- -- --dns01 dns01.dmz.example.com 192.168.254.53 www01 www01.dmz.example.com 192.168.254.80 ztest ztest.test.example.com 192.168.42.111 spacecmd &gt; report_kernels
                                                                                                                                                                                                                                                                                                     System Kernel-- -- -- -- -- --system01 2.6.9 -
                                                                                                                                                                                                                                                                                                 89.0.25.ELsmp system02 2.6.9 - 89.0.3.ELsmp system03 2.6.9 - 89.0.26.ELsmp
</code></pre>
<p> <code>Tab completion of everything</code> </p>
<pre>
spacecmd&gt; system_installpackage ssm vmware-tools [tab]
vmware-tools         vmware-tools-kmod
vmware-tools-common  vmware-tools-nox
</pre>
<p> <code>Easily view system information</code> </p>
<pre>
spacecmd&gt; system_details www01.example.com
Name:          www01.example.com
System ID:     1000010001
Locked:        False
Registered:    20100311 19:31:36
Last Checkin:  20100621 18:31:53
OSA Status:    online
Hostname:      www01.example.com
IP Address:    192.168.1.80
Kernel:        2.6.18-164.el5
Software Channels:
  custom-rhel-i386-server-5
    |-- custom-extras-i386-rhel5
    |-- clone-rhn-tools-rhel-i386-server-5
Configuration Channels:
  sudoers
  base
  base-rhel5
Entitlements:
  Management
  Provisioning
System Groups:
  all_linux_systems
  all_linux_VMs
  rhel5-i386
</pre>
<h2>BUGS</h2>
<pre>
Please report any bugs to <a rel="nofollow" href="https://bugzilla.redhat.com/">https://bugzilla.redhat.com/</a> under the &quot;spacecmd&quot;
component.
</pre>
<h2>HOMEPAGE</h2>
<p> <a rel="nofollow" href="https://fedorahosted.org/spacewalk/wiki/spacecmd">https://fedorahosted.org/spacewalk/wiki/spacecmd</a></p>
<h2>AUTHOR</h2>
<p> spacecmd was written by Aron Parsons &lt;aronparsons [at] gmail.com&gt; </p>
<h2>Index</h2>
