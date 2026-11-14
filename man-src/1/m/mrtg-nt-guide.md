---
title: "mrtg-nt-guide(1)"
name: "mrtg-nt-guide"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtg-nt-guide/"
description: "mrtg-nt-guide – The MRTG 2.17.4 Windows Installation Guide"
---

<h2 class="name">NAME</h2>
<p> mrtg-nt-guide &#8211; The MRTG 2.17.4 Windows Installation Guide </p>
<h2>SYNOPSIS</h2>
<p> Installing <font SIZE="-1">MRTG</font> on a Windows box is not quite as &#8220;click and point&#8221; as some might want it to be. But then again, it is not all that difficult if you follow the instructions below.</p>
<h2>PREREQUISITES</h2>
<p> To get <font SIZE="-1">MRTG</font> to work on Windows you need the following:</p>
<dl>
<dt>&bull;</p>
<dd> A current copy of Perl. For Example ActivePerl 5.8.8 from ActiveState <a rel="nofollow" href="http://www.activestate.com/store/activeperl/download/">http://www.activestate.com/store/activeperl/download/</a></p>
<dt>&bull;</p>
<dd> The latest version of <font SIZE="-1">MRTG</font> from <a rel="nofollow" href="http://oss.oetiker.ch/mrtg/pub.">http://oss.oetiker.ch/mrtg/pub.</a> Look for mrtg-2.17.4.zip or better. The archive also contains a precompiled copy of rateup.exe for Win32.</dl>
<h2>INSTALLING</h2>
<p> I suggest you do the following from the machine that will be running <font SIZE="-1">MRTG</font>, which, in this case, is also a web server. All examples are for doing things to a <font SIZE="-1">LOCAL</font> machine.</p>
<dl>
<dt>First</p>
<dd> Unzip <font SIZE="-1">MRTG</font> to C:\mrtg-2.17.4 on the Windows machine of your choice.</p>
<dt>Next</p>
<dd> Install Perl on the same Windows machine. You might want to make sure that the Perl binary directory is listed in your system path. </p>
<pre>
 C:\Perlin;%SystemRoot%\system32;%SystemRoot%;...
</pre>
<p> You can manually check this by going to [Control Panel]-&gt;[System]-&gt;[Environment]</dl>
<p> To see if everything is installed properly you can open a Command Shell and go into <i>c:\mrtg-2.17.4in</i>. Type: </p>
<pre>
 perl mrtg
</pre>
<p> This should give you a friendly error message complaining about the missing <font SIZE="-1">MRTG</font> configuration file. Now, you have successfully installed <font SIZE="-1">MRTG</font> and Perl.</p>
<h2>CONFIGURING MRTG</h2>
<p> Now it is time to create a configuration for <font SIZE="-1">MRTG</font>. But before we begin you need to know a few things. Take an opportunity to gather the following information:</p>
<dl>
<dt>&bull;</p>
<dd> The <font SIZE="-1">IP</font> address or hostname and the <font SIZE="-1">SNMP</font> port number, (if non standard), of the device you want to monitor.</p>
<dt>&bull;</p>
<dd> If you want to monitor something other than bytes in and out, you must also know the <font SIZE="-1">SNMPOID</font> of what you want to monitor.</p>
<dt>&bull;</p>
<dd> Finally you need to know the read-only <font SIZE="-1">SNMP</font> community string for your device. If you don&#8217;t know it, try <code>public</code>, that is the default.</dl>
<p> For the rest of this document we will be using device <code>10.10.10.1</code> ( a <font SIZE="-1">CISCO</font> Catalyst 5000) with Community string <code>public</code>. We are interested in monitoring traffic, and the <font SIZE="-1">CPU</font> load. Let&#8217;s begin. </p>
<p> The first thing we do in setting up <font SIZE="-1">MRTG</font> is making a default config file. Get to a cmd prompt and change to the <i>c:\mrtg-2.17.4in</i> directory. Type the following command: </p>
<pre><code>
perl cfgmaker public[at] 10.10.10.1 --global "WorkDir: c:\www\mrtg" --output mrtg.cfg
</code></pre>
<p> This creates an initial <font SIZE="-1">MRTG</font> config file for you. Note that in this file all interfaces of your router will be stored by number. Unfortunately, these numbers are likely to change whenever you reconfigure your router. In order to work around this you can get <i>cfgmaker</i> to produce a configuration which is based on Ip numbers, or even Interface Descriptions. Check cfgmaker </p>
<p> If you get an error message complaining about <code>no such name</code> or <code>no response</code>, your community name is probably wrong. </p>
<p> Now, let&#8217;s take a look at the mrtg.cfg file that was created. </p>
<p> In Perl, a <tt>&quot;#&quot;</tt> is a comment, synonymous with <tt>&quot;REM&quot;</tt> in <font SIZE="-1">DOS</font>. </p>
<p> Add the following to the top of the mrtg.cfg file: </p>
<pre>
 WorkDir: c:\www\mrtg
</pre>
<p> This is where the web pages are created, usually a web root. </p>
<pre>
 ######################################################################
 # Description: LCP SUWGB
 # Contact: Administrator
 # System Name: LC-Bridge
 # Location: Here
 #.....................................................................
</pre>
<p> TargetDevice&#8217;s <font SIZE="-1">IP</font> Address:Interface Number:Community:IP Address </p>
<p>Target[10.10.10.1.1] : 1 : public[at] 10.10.10.1</p>
<p> This is the interface speed (Default is 10 megabits; for 100Mbit devices use 12500000 and so on&#8230;) </p>
<p>MaxBytes[10.10.10.1.1] : 1250000 Title[10.10.10.1.1] : LC &#8211; Bridge(sample.device)<br />
    : ether0</p>
<p> This section determines how the web page headers will look </p>
<p> PageTop[10.10.10.1.1]: &lt;H1&gt;Traffic Analysis for ether0&lt;/H1&gt;<br />
  &lt;TABLE&gt;<br />
  &lt;TR&gt;&lt;TD&gt;System:&lt;/TD&gt;&lt;TD&gt;LC-Bridge inAndover&lt;/TD&gt;&lt;/TR&gt;<br />
  &lt;TR&gt;&lt;TD&gt;Maintainer:&lt;/TD&gt;&lt;TD&gt;Administrator&lt;/TD&gt;&lt;/TR&gt;<br />
  &lt;TR&gt;&lt;TD&gt;Interface:&lt;/TD&gt;&lt;TD&gt;ether0(1)&lt;/TD&gt;&lt;/TR&gt;<br />
  &lt;TR&gt;&lt;TD&gt;IP:&lt;/TD&gt;&lt;TD&gt;sample.device(10.10.10.1)&lt;/TD&gt;&lt;/TR&gt;<br />
  &lt;TR&gt;&lt;TD&gt;Max Speed:&lt;/TD&gt;<br />
  &lt;TD&gt;1250.0 kBytes/s (ethernetCsmacd)&lt;/TD&gt;&lt;/TR&gt;<br />
  &lt;/TABLE&gt;<br />
  Target[10.10.10.1.2]: 2:public [at] 10.10.10.1<br />
  MaxBytes[10.10.10.1.2]: 1250000<br />
  Title[10.10.10.1.2]: LC-Bridge (): ulink0<br />
  PageTop[10.10.10.1.2]: &lt;H1&gt;Traffic Analysis for ulink0&lt;/H1&gt;<br />
   &lt;TABLE&gt;<br />
   &lt;TR&gt;&lt;TD&gt;System:&lt;/TD&gt;&lt;TD&gt;LC-Bridge inAndover&lt;/TD&gt;&lt;/TR&gt;<br />
   &lt;TR&gt;&lt;TD&gt;Maintainer:&lt;/TD&gt;&lt;TD&gt;Administrator&lt;/TD&gt;&lt;/TR&gt;<br />
   &lt;TR&gt;&lt;TD&gt;Interface:&lt;/TD&gt;&lt;TD&gt;ulink0(2)&lt;/TD&gt;&lt;/TR&gt;<br />
   &lt;TR&gt;&lt;TD&gt;IP:&lt;/TD&gt;&lt;TD&gt;()&lt;/TD&gt;&lt;/TR&gt;<br />
   &lt;TR&gt;&lt;TD&gt;Max Speed:&lt;/TD&gt;<br />
   &lt;TD&gt;1250.0 kBytes/s (ethernetCsmacd)&lt;/TD&gt;&lt;/TR&gt;<br />
   &lt;/TABLE&gt;<br />
#&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;</p>
<p> And that&#8217;s a very basic <font SIZE="-1">MRTG</font> config file. You can run this and see your results by going into the <i>c:\mrtg-2.17.4in</i> directory and typing: </p>
<pre>
 perl mrtg mrtg.cfg
</pre>
<p> It is normal to get errors for the first two times you run this command. The errors will alert you about the fact that there have not been any log files in existence before. </p>
<p> If you take a look at those web pages they are not very exciting (yet). You need to have the <font SIZE="-1">MRTG</font> files run every five minutes to produce the desired results. Just run it again after a few minutes. You should now be able to see the first lines in your graphs.</p>
<h2>MAKE MRTG RUN ALL THE TIME</h2>
<p> Starting <font SIZE="-1">MRTG</font> by hand every time you want to run it is not going to make you happy I guess. </p>
<p> There is a special option you can set in the <font SIZE="-1">MRTG</font> configuration file so so that <font SIZE="-1">MRTG</font> will not terminate after it was started. Instead it will wait for 5 minutes and then run again. </p>
<p> Add the option </p>
<pre>
 RunAsDaemon: yes
</pre>
<p> to your mrtg.cfg file and start it with: </p>
<pre>
 start /Dc:\mrtg-2.17.4in wperl mrtg --logging=eventlog mrtg.cfg
</pre>
<p> If you use <code>wperl</code> instead of <code>perl</code>, no console window will show. <font SIZE="-1">MRTG</font> is now running in the background. If it runs into problems it will tell you so over the EventLog. To stop <font SIZE="-1">MRTG</font>, open the Task Manager and terminate the <code>wperl.exe</code> process. If mrtg has anything to tell you these messages can be found in the event log. </p>
<p> If you put a shortcut with </p>
<pre>
 Target:    wperl mrtg --logging=eventlog mrtg.cfg
 Start in:  c:\mrtg-2.17.4in
</pre>
<p> into your start-up folder, <font SIZE="-1">MRTG</font> will now start whenever you login to your <font SIZE="-1">NT</font> box. </p>
<p> If you do not want to log into your box just to start <font SIZE="-1">MRTG</font>. Have a look at <a rel="nofollow" href="http://www.firedaemon.com/mrtg-howto.html">http://www.firedaemon.com/mrtg-howto.html</a> which describes a free tool to start any program as a Service. The pages gives specific instructions for <font SIZE="-1">MRTG</font> users.</p>
<h2>HOW TO SETUP MRTG AS A WINDOWS SERVICE</h2>
<h3>Additional Prerequisites</h3>
<dl>
<dt>&bull;</p>
<dd> <font SIZE="-1">MRTG</font> must be installed and fully configured on the target system. In the following exercise the assumption is that <font SIZE="-1">MRTG</font> is installed under c:\mrtg\ and all the sample files use this location.</p>
<dt>&bull;</p>
<dd> Microsoft Tools <font SIZE="-1"><code>SRVANY</code></font><code>.exe</code> (Applications as Services Utility) and <font SIZE="-1"><code>INSTSRV</code></font><code>.exe</code> (Service Installer) &#8211; Those files can be downloaded from Microsoft as a part of Windows 2000 Resource Kit at &lt;<a rel="nofollow" href="http://www.microsoft.com/windows2000/techinfo/reskit/tools/default.asp">http://www.microsoft.com/windows2000/techinfo/reskit/tools/default.asp</a>&gt;. They are also available from other locations such as &lt;<a rel="nofollow" href="http://www.electrasoft.com/srvany/srvany.htm">http://www.electrasoft.com/srvany/srvany.htm</a>&gt;, &lt;<a rel="nofollow" href="http://www.iopus.com/guides/srvany.htm">http://www.iopus.com/guides/srvany.htm</a>&gt;, etc. Detailed instructions on how to use this package are available at &lt;<a rel="nofollow" href="http://support.microsoft.com/kb/q137890/">http://support.microsoft.com/kb/q137890/</a>&gt;. In order to follow the steps in this HOW-TO you <font SIZE="-1"><code>MUST</code></font> obtain both executables.</p>
<dt>&bull;</p>
<dd> You must have administrative rights on the target system.</dl>
<h3>Preparation</h3>
<p> Please complete the following steps before starting the installation:</p>
<dl>
<dt>&bull;</p>
<dd> Copy <code>srvany.exe</code> and <code>instsrv.exe</code> to c:\mrtg-2.17.4in\ (your <font SIZE="-1">MRTG</font> bin directory).</p>
<dt>&bull;</p>
<dd> Create a file called <code>mrtg.reg</code> anywhere on your system and paste the following content into it: </p>
<pre>
 Windows Registry Editor Version 5.00
 [HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MRTG\Parameters]
 &quot;Application&quot;=&quot;c:\perl\bin\wperl.exe&quot;
 &quot;AppParameters&quot;=&quot;c:\mrtg-2.17.4\bin\mrtg --logging=eventlog c:\mrtg-2.17.4\bin\mrtg.cfg&quot;
 &quot;AppDirectory&quot;=&quot;c:\mrtg-2.17.4\bin\&quot;
</pre>
</dl>
<h3>Service Installation</h3>
<p> Once again, assuming that <font SIZE="-1">MRTG</font> is already fully installed and configured on the target system under c:\mrtg\ the following steps are necessary to setup <font SIZE="-1">MRTG</font> as a service. </p>
<p> Using the command prompt go into the temporary directory where you unzipped the package. When there type the following command to create a service named &#8220;<font SIZE="-1">MRTG</font>&#8221; in the Windows Services management console: </p>
<pre>
 instsrv MRTG c:\mrtgin\srvany.exe
</pre>
<p> Now you need to create the <code>App*</code> entries required for the new service. You can do this by either right-clicking on the mrtg.reg file and selecting &#8216;merge&#8217; or by running the following command: </p>
<pre>
 regedit /s mrtg.reg
</pre>
<p> After setting up the registry entry it is time to point it to your <font SIZE="-1">MRTG</font> installation. If you have installed <font SIZE="-1">MRTG</font> under <i>c:\mrtg\</i>, you can skip this step. Open your registry editor (Start -&gt; Run -&gt; regedt32), and locate the <code>[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MRTG]</code> key. Make sure that the <code>ImagePath</code> variable is correctly pointing to <code>srvany.exe</code> located in your <font SIZE="-1">MRTG</font> bin directory (for example c:\mrtgin\srvany.exe). Next you have to expand the <font SIZE="-1">MRTG</font> tree, and go to the <code>[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\MRTG\Parameters]</code> key. Under Parameters make sure that all the <code>Application</code> variables are setup properly. </p>
<p> At this point you are ready to run the service. The only thing left to do is to start the <font SIZE="-1">MRTG</font> service in the Services management console. After you do this, you should see two new processes running on your system: srvany.exe and wperl.exe. Make sure to stop any previously running <font SIZE="-1">MRTG</font> processes to avoid conflict. </p>
<p> Note that it is imperative to set the <code>RunAsDaemon: yes</code> option or the service will stop after just one single run!</p>
<h2>EXAMPLE</h2>
<p> Now lets look at a config file to monitor what we wanted to on our mythical Cisco Cat 5000 &#8212; utilization on ports 3, 5, 10, and 24, and the <font SIZE="-1">CPU</font> Load, which will show us nonstandard mrtg configurations as well as more options.. </p>
<pre><code>
 WorkDir: c:\www\mrtg
 RunAsDaemon: yes
 ######################################################################
#Description : LCP SUWGB
#Contact : Administrator
#System Name : LC - Bridge
#Location : Here
#.....................................................................
 Target[10.10.10.1.1]: 3:public [at] 10.10.10.1
 MaxBytes[10.10.10.1.1]: 1250000
 Title[10.10.10.1.1]: LC-Bridge (sample-device): ether0
 PageTop[10.10.10.1.1]: &lt;H1&gt;Traffic Analysis for ether0&lt;/H1&gt;
  &lt;TABLE&gt;
 &lt;TR&gt;&lt;TD&gt;System:&lt;/TD&gt;&lt;TD&gt;LC-Bridge inAndover&lt;/TD&gt;&lt;/TR&gt;
 &lt;TR&gt;&lt;TD&gt;Maintainer:&lt;/TD&gt;&lt;TD&gt;Administrator&lt;/TD&gt;&lt;/TR&gt;
 &lt;TR&gt;&lt;TD&gt;Interface:&lt;/TD&gt;&lt;TD&gt;ether0(3)&lt;/TD&gt;&lt;/TR&gt;
 &lt;TR&gt;&lt;TD&gt;IP:&lt;/TD&gt;&lt;TD&gt;sample-device(10.10.10.1)&lt;/TD&gt;&lt;/TR&gt;
 &lt;TR&gt;&lt;TD&gt;Max Speed:&lt;/TD&gt;
 &lt;TD&gt;1250.0 kBytes/s (ethernetCsmacd)&lt;/TD&gt;&lt;/TR&gt;
 &lt;/TABLE&gt;
#-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -
 Target[10.10.10.1.2]: 5:public [at] 10.10.10.1
 MaxBytes[10.10.10.1.2]: 1250000
 Title[10.10.10.1.2]: LC-Bridge (): ulink0
 PageTop[10.10.10.1.2]: &lt;H1&gt;Traffic Analysis for ulink0&lt;/H1&gt;
  &lt;TABLE&gt;
  &lt;TR&gt;&lt;TD&gt;System:&lt;/TD&gt;&lt;TD&gt;LC-Bridge inAndover&lt;/TD&gt;&lt;/TR&gt;
  &lt;TR&gt;&lt;TD&gt;Maintainer:&lt;/TD&gt;&lt;TD&gt;Administrator&lt;/TD&gt;&lt;/TR&gt;
  &lt;TR&gt;&lt;TD&gt;Interface:&lt;/TD&gt;&lt;TD&gt;ulink0(5)&lt;/TD&gt;&lt;/TR&gt;
  &lt;TR&gt;&lt;TD&gt;IP:&lt;/TD&gt;&lt;TD&gt;()&lt;/TD&gt;&lt;/TR&gt;
  &lt;TR&gt;&lt;TD&gt;Max Speed:&lt;/TD&gt;
  &lt;TD&gt;1250.0 kBytes/s (ethernetCsmacd)&lt;/TD&gt;&lt;/TR&gt;
  &lt;/TABLE&gt;
#-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -
 Target[10.10.10.1.1]: 10:public [at] 10.10.10.1
 MaxBytes[10.10.10.1.1]: 1250000
 Title[10.10.10.1.1]: LC-Bridge (sample-device): ether0
 PageTop[10.10.10.1.1]: &lt;H1&gt;Traffic Analysis for ether0&lt;/H1&gt;
  &lt;TABLE&gt;
  &lt;TR&gt;&lt;TD&gt;System:&lt;/TD&gt;&lt;TD&gt;LC-Bridge inAndover&lt;/TD&gt;&lt;/TR&gt;
  &lt;TR&gt;&lt;TD&gt;Maintainer:&lt;/TD&gt;&lt;TD&gt;Administrator&lt;/TD&gt;&lt;/TR&gt;
  &lt;TR&gt;&lt;TD&gt;Interface:&lt;/TD&gt;&lt;TD&gt;ether0(10)&lt;/TD&gt;&lt;/TR&gt;
  &lt;TR&gt;&lt;TD&gt;IP:&lt;/TD&gt;&lt;TD&gt;sample-device(10.10.10.1)&lt;/TD&gt;&lt;/TR&gt;
  &lt;TR&gt;&lt;TD&gt;Max Speed:&lt;/TD&gt;
  &lt;TD&gt;1250.0 kBytes/s (ethernetCsmacd)&lt;/TD&gt;&lt;/TR&gt;
  &lt;/TABLE&gt;
#-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -
 Target[10.10.10.1.2]: 24:public [at] 10.10.10.1
 MaxBytes[10.10.10.1.2]: 1250000
 Title[10.10.10.1.2]: LC-Bridge (): ulink0
 PageTop[10.10.10.1.2]: &lt;H1&gt;Traffic Analysis for ulink0&lt;/H1&gt;
  &lt;TABLE&gt;
  &lt;TR&gt;&lt;TD&gt;System:&lt;/TD&gt;&lt;TD&gt;LC-Bridge inAndover&lt;/TD&gt;&lt;/TR&gt;
  &lt;TR&gt;&lt;TD&gt;Maintainer:&lt;/TD&gt;&lt;TD&gt;Administrator&lt;/TD&gt;&lt;/TR&gt;
  &lt;TR&gt;&lt;TD&gt;Interface:&lt;/TD&gt;&lt;TD&gt;ulink0(24)&lt;/TD&gt;&lt;/TR&gt;
  &lt;TR&gt;&lt;TD&gt;IP:&lt;/TD&gt;&lt;TD&gt;()&lt;/TD&gt;&lt;/TR&gt;
  &lt;TR&gt;&lt;TD&gt;Max Speed:&lt;/TD&gt;
  &lt;TD&gt;1250.0 kBytes/s (ethernetCsmacd)&lt;/TD&gt;&lt;/TR&gt;
  &lt;/TABLE&gt;
#-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -
#Router CPU load %
 Target[cpu.1]:1.3.6.1.4.1.9.2.1.58.0&amp;1.3.6.1.4.1.9.2.1.58.0:public [at] 10.10.10.1
 RouterUptime[cpu.1]: public [at] 10.10.10.1
 MaxBytes[cpu.1]: 100
 Title[cpu.1]: CPU LOAD
 PageTop[cpu.1]: &lt;H1&gt;CPU Load %&lt;/H1&gt;
 Unscaled[cpu.1]: ymwd
 ShortLegend[cpu.1]: %
 XSize[cpu.1]: 380
 YSize[cpu.1]: 100
 YLegend[cpu.1]: CPU Utilization
 Legend1[cpu.1]: CPU Utilization in % (Load)
 Legend2[cpu.1]: CPU Utilization in % (Load)
 Legend3[cpu.1]:
 Legend4[cpu.1]:
 LegendI[cpu.1]:
 LegendO[cpu.1]: &amp;nbsp;
 Usage
     Options[cpu .1] : gauge
</code></pre>
<p> This is a nice example of how to monitor any <font SIZE="-1">SNMP</font> device if you know what <font SIZE="-1">OID</font> you want to use. Once again, for an explanation of the more advance features of mrtg, please see the rest of the documentation.</p>
<h2>AUTHORS</h2>
<p> Tobi Oetiker &lt;tobi [at] oetiker.ch&gt;, David S. Divins &lt;ddivins [at] moon.jic.com&gt;, Steve Pierce &lt;MRTG [at] HDL.com&gt;, Artyom Adjemov &lt;one.bofh [at] gmail.com&gt;, Ilja Ivanov &lt;ivanov [at] bseu.by&gt; Karel Fajkus &lt;<a rel="nofollow" href="http://fajkus.cz/">http://fajkus.cz/</a>&gt; </p>
<h2>Index</h2>
