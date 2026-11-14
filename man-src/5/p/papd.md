---
title: "papd(5)"
name: "papd"
section: "5"
letter: "p"
url: "/docs/linux/man/5-papd/"
description: "papd.conf – Configuration file used by"
---

<p>papd.conf &#8211; Configuration file used by </p>
<p><a href="/docs/linux/man/8-papd/">papd</a>(8) to determine the configuration of printers used by the Netatalk printing daemon</p>
<h2>Description</h2>
<p><code>/etc/atalk//papd.conf</code> is the configuration file used by papd to configure the printing services offered by netatalk. Please note that papd must be enabled in <code>/etc/atalk//netatalk.conf</code> for this to take any effect. <code>papd</code> shares the same defaults as lpd on many systems, but not Solaris. </p>
<p> Any line not prefixed with <code>#</code> is interpreted. The configuration lines are composed like: </p>
<p> <i>printername:[options]</i> </p>
<p> On systems running a System V printing system the simplest case is to have either no papd.conf, or to have one that has no active lines. In this case, atalkd should auto-discover the local printers on the machine. Please note that you can split lines by using <code>\fR.</code> </p>
<p> printername may be just a name (<code>Printer 1</code>), or it may be a full name in nbp_name format (<code>Printer 1:LaserWriter@My Zone</code>). </p>
<p> Systems using a BSD printing system should make use of a pipe to the printing command in question within the <code>pr</code> option (eg. <code>pr=|/usr/bin/lpr -J%J -u%U</code>). Note: When printing using a pipe, papd recognizes several wildcards: %F will be replaced by the name present in the &quot;%%For:&quot; comment in the PostScript stream, same with %J for the &quot;%%Title:&quot; comment. %U will be substituted with the login name (the latter applies only when authenticated printing is in effect). </p>
<p> When CUPS support is compiled in, then <code>cupsautoadd </code> as the first entry in papd.conf will automagically share all CUPS printers by papd utilizing the PPDs assigned in CUPS (customizable &#8212; see below). This can be overwritten for individal printers by subsequently adding individual entries using the CUPS queue name as <code>pr </code> entry. Note: CUPS support is mutually exclusive with System V support described above. </p>
<p> The possible options are colon delimited (<code>:</code>), and lines must be terminated with colons. The possible options and flags are: </p>
<p> <code>am=(uams list)</code></p>
<dl>
<dd>The <code>am</code> option allows specific UAMs to be specified for a particular printer. It has no effect if the <code>au</code> flag is not present or if papd authentication was not built into netatalk. Note: possible values are <code>uams_guest.so</code> and <code> uams_clrtxt.so</code> only. The first method requires a valid username, but no password. The second requires both a valid username and the correct password.</dl>
<p> <code>au</code></p>
<dl>
<dd>If present, this flag enables authentication for the printer. Please note that papd authentication must be built into netatalk for this to take effect.</dl>
<p> <code>co=(CUPS options)</code></p>
<dl>
<dd>The <code>co</code> option allows options to be passed through to CUPS (eg. <code>co=&quot;protocol=TBCP&quot; </code> or <code>co=&quot;raw&quot;</code>).</dl>
<p> <code>cupsautoadd[:type][@zone]</code></p>
<dl>
<dd>If used as the first entry in papd.conf this will share all CUPS printers via papd. type/zone settings as well as other parameters assigned to this special printer share will apply to all CUPS printers. Unless the <code>pd</code> option is set, the CUPS PPDs will be used. To overwrite these global settings for individual printers simply add them subsequently to papd.conf and assign different settings.</dl>
<p> <code>fo</code></p>
<dl>
<dd>If present, this flag enables a hack to translate line endings originating from pre Mac OS X LaserWriter drivers to let <code>foomatic-rip</code> recognize foomatic PPD options set in the printer dialog. Attention: Use with caution since this might corrupt binary print jobs!</dl>
<p> <code>op=(operator)</code></p>
<dl>
<dd>This specifies the operator name, for lpd spooling.</dl>
<p> <code>pa=(appletalk address)</code></p>
<dl>
<dd>Allows specification of Appletalk addresses. Usually not needed.</dl>
<p> <code>pd=(path to ppd file)</code></p>
<dl>
<dd>Specifies a particular PPD (printer description file) to associate with the selected printer.</dl>
<p> <code>pr=(lpd/CUPS printer name or pipe command)</code></p>
<dl>
<dd>Sets the <code>lpd</code> or <code>CUPS</code> printer that this is spooled to.</dl>
<h2>Examples</h2>
<p>Unless CUPS support has been compiled in (which is default from Netatalk 2.0 on) one simply defines the lpd queue in question by setting the <code>pr</code> parameter to the queue name, in the following example &quot;ps&quot;. If no <code>pr</code> parameter is set, the default printer will be used. <code>Example. papd.conf System V printing system examples</code> The first spooler is known by the AppleTalk name Mac Printer Spooler, and uses a PPD file located in /usr/share/lib/ppd. In addition, the user mcs will be the owner of all jobs that are spooled. The second spooler is known as HP Printer and all options are the default.</p>
<dl>
<dd>
<pre>Mac Printer Spooler:\
 :pr=ps:\
 :pd=/usr/share/lib/ppd/HPLJ_4M.PPD:\
 :op=mcs:
HP Printer:\
 :</pre>
</dl>
<p> An alternative to the technique outlined above is to direct papd&#8217;s output via a pipe into another program. Using this mechanism almost all printing systems can be driven. Netatalk supplies three &quot;wildcards&quot; that get substituted with values of the already printed job: <code>%F</code>, <code>%U</code> and <code>%J</code>. Using these wildcards, one can pass those parameters directly to programs or implement small wrapper scripts to call the printing system in question. <code>Example. papd.conf examples using pipes</code> The first spooler is known as HP 8100. It pipes the print job to <code>/usr/bin/lpr</code> for printing using the value of the <i>%%Title: </i> comment as job name. PSSP authenticated printing is enabled, as is CAP-style authenticated printing. Both methods support guest and cleartext authentication as specified by the &#8216;<code>am</code>&#8216; option. The PPD used is /etc/atalk/ppds/hp8100.ppd. The second spooler is called &quot;Dump PostScript&quot; and uses a pipe to <code>cat</code> to send the raw PostScript code into the user&#8217;s home directory into a file called like the printjob.</p>
<dl>
<dd>
<pre>HP 8100:\
 :pr=|/usr/bin/lpr -Plp -J&quot;%J&quot;:\
 :sp:\
 :ca=/tmp/print:\
 :am=uams_guest.so,uams_pam.so:\
 :pd=/etc/atalk/ppds/hp8100.ppd:
Dump PostScript:LaserWriter [at] Server:\
 :pr=|cat &gt;/home/%U/%J-prn.out:\
 :pd=/usr/share/lib/ppd/mooralana.ppd:\
 :sp:au:op=lp:\
 :am=uams_clrtxt.so:</pre>
</dl>
<p> Starting with Netatalk 2.0 direct CUPS integration is available. In this case, defining only a queue name as <code>pr</code> parameter won&#8217;t invoke the SysV lpd daemon but uses CUPS instead. Unless a specific PPD has been assigned using the <code>pd</code> switch, the PPD configured in CUPS will be used by <code>papd</code>, too. There exists one special share named &quot;cupsautoadd&quot;. If this is present as the first entry then all available CUPS queues will be served automagically using the parameters assigned to this global share. But subsequent printer definitions can be used to override these global settings for individual spoolers. <code>Example. papd.conf CUPS examples</code> The first entry sets up automatic sharing of all CUPS printers. All those shares appear in the zone &quot;1st floor&quot; and since no additional settings have been made, they use the CUPS printer name as NBP name and use the PPD configured in CUPS. The second entry defines different settings for one single CUPS printer. It&#8217;s NBP name is differing from the printer&#8217;s name and the registration happens in another zone.</p>
<dl>
<dd>
<pre>cupsautoadd@1st floor:op=root:
Boss' LaserWriter@2nd floor:\
 :pr=laserwriter-chief:</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-papd/">papd</a></code>(8), <code><a href="/docs/linux/man/5-atalkd-conf/">atalkd.conf</a></code>(5), <code><a href="/docs/linux/man/8-lpd/">lpd</a></code>(8), <code><a href="/docs/linux/man/8-lpoptions/">lpoptions</a></code>(8) </p>
