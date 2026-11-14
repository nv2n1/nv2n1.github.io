---
title: "rancid_intro(1)"
name: "rancid_intro"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rancid_intro/"
description: "rancid_intro – introduction to the Really Awesome New Cisco confIg Differ"
---

<h2>NAME</h2>
<p> rancid_intro &#8211; introduction to the Really Awesome New Cisco confIg Differ</p>
<h2>INTRODUCTION</h2>
<p> <code>rancid</code> is really more than just a Cisco configuration differ. It handles several different device&#8217;s configurations; currently including Alteon, Arista, Bay Networks (Nortel), Cisco, Extreme, F5 BigIP, Force10, Fortinet, Foundry, HP Procurve switches, Hitachi, Juniper Routers and edge (ERX) routers, MRTd daemon, Microtik routers, Netscalar load balancers, Netscreen firewalls, Procket, Redback, SMC switches, Xirrus arrays, Zebra routing software, and the ADC-Kentrox EZ-T3 mux. </p>
<p> <code>rancid</code> uses an expect script to login using ssh, telnet, or rsh to each of a list of devices and run a set of commands for that device-type and collects the output. The output is run through some filtering to summarize, reformat, and/or snip unwanted or security related data such as chassis temperature and easily reverse-able passwords. </p>
<p> Named after the device&#8217;s name in the group&#8217;s configuration file (<i>router.db</i>), the resulting files are saved in the directory &lt;group&gt;/configs. Except for the data filtered from the configuration file for security reasons, such as reversable passwords, these files are suitable for loading directly to restore a lost configuration. See <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5) for more information on &lt;group&gt;s. </p>
<p> After filtering, a uni-diff (see <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1)) of the result is produced for each of the devices in a group against that of the previous run of <code>rancid</code> and is e-mailed to that group&#8217;s mail list, &quot;rancid-&lt;group&gt;&quot;. This e-mail will also include any differences of the device list in the group&#8217;s configuration file, <i>router.db.</i> </p>
<p> Lastly, all the updated files are checked into the revision control system (CVS, Subversion, or git). And, administrative messages, such as collections that are failing for longer than <code>OLDTIME,</code> are mailed to &quot;rancid-admin-&lt;group&gt;&quot;. </p>
<p> Additional utilities, including a looking glass, come with rancid. See rancid&#8217;s share directory ( <i>share/rancid</i>).</p>
<h2>EXAMPLE E-MAIL</h2>
<p> Below is a sample of a uni-diff produced from the group &quot;shrubbery&quot; for the device named dfw.shrubbery.net, which happens to be a Cisco GSR. </p>
<pre><code>
From : rancid
           To : rancid -
                shrubbery[at] shrubbery.net
                        Subject : shrubbery router config diffs
                                      Precedence : bulk

                                                       Index : configs /
                    dfw.shrubbery.net ==
    == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
    =
        retrieving revision 1.144 diff - u - 4 - r1 .144 dfw.shrubbery.net @ @-57,
    14 + 57, 8 @ @!Slot 2 / MBUS : hvers 1.1 !Slot 2 / MBUS : software 01.36(RAM)(ROM version is 01.33) !Slot 2 / MBUS : 128 Mbytes DRAM, 16384 Kbytes SDRAM !-!Slot 6 : 1 Port Gigabit Ethernet - !Slot 6 / PCA : part 73 - 3302 - 03 rev C0 ver 3, serial CAB031216OL - !Slot 6 / PCA : hvers 1.1 - !Slot 6 / MBUS : part 73 - 2146 - 07 rev B0 dev 0, serial CAB031112SB - !Slot 6 / MBUS : hvers 1.2 - !Slot 6 / MBUS : software 01.36(RAM)(ROM version is 01.33) !Slot 7 : Route Processor !Slot 7 / PCA : part 73 - 2170 - 03 rev B0 ver 3, serial CAB024901SI !Slot 7 / PCA : hvers 1.4 !Slot 7 / MBUS : part 73 - 2146 - 06 rev A0 dev 0, serial CAB02060044
</code></pre>
<p> In this example, we see that a Gigabit Ethernet linecard was removed from slot 6. However, since this data is collected from &quot;show&quot; commands on the router, it could just as easily be that the card crashed so the RP can not communicate with it to collect information.</p>
<h2>GETTING STARTED</h2>
<p> Installation instructions are included in the distribution&#8217;s top-level directory in the README file (which will be installed in share/rancid). Once the installation is complete, start by reading the man pages listed below or follow the basic instructions included in the README file. </p>
<p> See <a rel="nofollow" href="http://www.shrubbery.net/rancid">http://www.shrubbery.net/rancid</a> for information on new versions, mail lists, etc.</p>
<h2>ADDING NEW GROUPS</h2>
<p> Follow this procedure for adding new groups:</p>
<dl>
<dt>o</p>
<dd> Update the <i>LIST_OF_GROUPS</i> variable in <i>etc/rancid.conf</i> (see <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5)).</p>
<dt>o</p>
<dd> Run <code><a href="/docs/linux/man/1-rancid-cvs/">rancid-cvs</a></code>(1).</p>
<dt>o</p>
<dd> Update the system&#8217;s mail aliases file <i>/etc/aliases</i> (see <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5)).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-clogin/">clogin</a></code>(1), <code><a href="/docs/linux/man/5-cloginrc/">cloginrc</a></code>(5), <code><a href="/docs/linux/man/1-control_rancid/">control_rancid</a></code>(1), <code><a href="/docs/linux/man/1-lg_intro/">lg_intro</a></code>(1), <code><a href="/docs/linux/man/1-rancid/">rancid</a></code>(1), <code><a href="/docs/linux/man/1-rancid-run/">rancid-run</a></code>(1), <code><a href="/docs/linux/man/5-rancid-conf/">rancid.conf</a></code>(5), <code><a href="/docs/linux/man/5-router-db/">router.db</a></code>(5) </p>
<h2>Index</h2>
