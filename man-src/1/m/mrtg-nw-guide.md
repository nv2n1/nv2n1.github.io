---

title: "mrtg-nw-guide(1)"
name: "mrtg-nw-guide"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtg-nw-guide/"
description: "mrtg-nw-guide – MRTG for NetWare"
---

<p> mrtg-nw-guide &#8211; MRTG for NetWare </p>
<h2>SYNOPSIS</h2>
<p> This guide is intended to aid in the installation and configuration of MRTG on a NetWare server.</p>
<h2>OVERVIEW</h2>
<p> MRTG is a relative newcomer to the NetWare platform. Earlier versions of NetWare could not run MRTG natively for several reasons:</p>
<dl>
<dt>&bull;</dt>
<dd> Absence of NetWare OS support in the MRTG package.</dd>
<dt>&bull;</dt>
<dd> A NetWare server commandline length limitation.</dd>
<dt>&bull;</dt>
<dd> Absence of the Rateup executable (Rateup.nlm).</dd>
<dt>&bull;</dt>
<dd> A standard installation method.</dd>
<dt>&bull;</dt>
<dd> Problems with NetWare&#8217;s implementation of Perl.</dd></dl>
<p> Support for the NetWare OS has now been fully added into MRTG, beginning with MRTG release 2.12.2. </p>
<p> Liberallly minded operating systems support a commandline length approaching 1000 characters. In such environments it was an easy matter to pass the sometimes high number of parameters used by MRTG&#8216;s Rateup executable directly on the commandline. Until NetWare 6.5, NetWare had a commandline limit of 512 characters. This limitation was also removed for NetWare 6.0 by Service Pack 5. For other NetWare versions and earlier Service Packs, this limitation remains. To permit a &#8216;standard&#8217; interface for NetWare, the Rateup executable has been modified to also read its parameters from a file, and the MRTG script has been modified to support this method on a NetWare platform. (See New Rateup Switch) </p>
<p> A Rateup NLM is now available, along with the necessary scripts to build it if required. See the NetWare Support section of this document for further details. Additionally, mrtg.pl has been revised because of the unique (to NetWare) name of executables (NLM). </p>
<p> The absence of a specific installation procedure has caused MRTG to fail in the past because the Perl script could not find or load the Rateup executable. The installation method supplied here will solve this problem for now. </p>
<p> The MRTG.pl script in the 2.12.2 (or later) version of MRTG has been configured to suit all likely versions of NetWare able to use Perl5, and bypasses all of the known problems with NetWare Perl running MRTG.</p>
<h2>PREREQUISITES</h2>
<p> You will need the following:</p>
<dl>
<dt>&bull;</dt>
<dd> Perl 5.8.0 for NetWare with latest Perl Updates (February, 2005 or later; previous versions MAY work)</dd>
<dt>&bull;</dt>
<dd> NetWare 5.1 w/ SP8, NetWare 6.0 w/ SP5 or NetWare 6.5 w/ SP2.</dd>
<dt>&bull;</dt>
<dd> A copy of the MRTG Package (v2.12.2 at time of writting)</dd>
<dt>&bull;</dt>
<dd> Three .ncf files to execute the Perl scripts at the NetWare server console.</dd>
<dt>&bull;</dt>
<dd> A copy of the Rateup NLM (Pre-built or compiled)</dd>
<dt>&bull;</dt>
<dd> Optionally, any NetWare supported Web Server (Netscape, Apache 1.3 or 2.0)</dd></dl>
<p> For copies of the .ncf files and Rateup NLM, see NetWare Support in this document.</p>
<h2>INSTALLING MRTG</h2>
<dl>
<dt>1.</dt>
<dd> Install the latest Perl 5.8.x release on your server. See the Perl documentation for details.</dd>
<dt>2.</dt>
<dd> Create the following directories: </dd>
<pre>
         SYS:/Mrtg
         SYS:/Mrtg/bin
         SYS:/Mrtg/contrib    (Optional for this document)
         SYS:/Mrtg/doc        (Optional for this document)
         SYS:/Mrtg/html
         SYS:/Mrtg/html/images
         SYS:/Mrtg/html/work
         SYS:/Mrtg/lib
         SYS:/Mrtg/logs
         SYS:/Mrtg/translate
</pre>
<dt>3.</dt>
<dd> Copy from the MRTG package the following files: </dd>
<pre>
 in\*        to  SYS:/Mrtg/bin              All files. See Note 1.
</pre>
<p> Note 1: Add a .pl extension to the mrtg, cfgmaker and indexmaker files. The rateup.exe will NOT be needed on the NetWare server. </p>
<pre>
<pre><code> \contrib\* to SYS:/Mrtg/contrib/ Include sub-directories
 \doc\* to SYS:/Mrtg/doc/ All files
 \images\* to SYS:/Mrtg/html/images/ All files
 \translate\* to SYS:/Mrtg/translate/ All files. See Note 2.
</code></pre>
<p> Note 2: For English-only language support, all \translate files EXCEPT Locales_mrtg may be deleted. </p>
<pre><code> \lib\* to SYS:/Mrtg/lib Include sub-directories. See Note 3.
</code></pre>
<p> Note 3: This will create the SYS:/Mrtg/lib/mrtg2 and ./pod directories. </p>
<dt>4.</dt>
<dd> <p> Create copies of the three .ncf files and install them: </p>
<pre><code> *.ncf to SYS:/Mrtg/bin
</code></pre>
<p> See NetWare Support in this document for details on how to create copies of these files. </p>
 </dd>
<dt>5.</dt>
<dd> <p> See Compiling Rateup.nlm&quot;&gt; in this document for details on compiling the Rateup NLM yourself if desired. A prebuit verion is available in the .\mrtg\bin directory where it must remain. </p>
 </dd></dl>
<h2>CONFIGURING MRTG</h2>
<dl>
<dt>&bull;</dt>
<dd> <p> Refer to Novell documentation on configuring and loading SNMP support on your server if this is the device to be monitored. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Edit sys:/mrtg/bin/MakeMrtgCfg.ncf: </p>
<p> replace ccccc with the GET community name for the SNMP device (typically &#8216;public&#8217;), </p>
<p> replace ddddd with the DNS name or IP address of the device to be monitored. e.g public [at] www.myserver.com, public [at] 10.202.65.180 </p>
<p> Note 1: These are NOT mail addresses, they just look like one! </p>
<p> Note 2: If multiple devices are to be monitored, add their entries to the same line: </p>
<p> e.g perl cfgmaker.pl public [at] www.myserver.com public [at] 10.202.65.180 &gt; sys:/mrtg/bin/mrtg.cfg </p>
<p> In this ``Getting Started&#8217;&#8216;, it is &#8216;suggested&#8217; to only monitor a single device. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> At the server console, run: </p>
<pre><code> sys:/mrtg/bin/MakeMrtgCfg.ncf
</code></pre>
<p> This will create Mrtg.cfg in sys:/mrtg/bin. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Edit the Mrtg.cfg configuration file created in the previous step. Note the following: </p>
<p> It was found, when testing MRTG on a NetWare 6.5 server using a NIC Interface, that mrtg.cfg contained the following message: </p>
<pre><code> ### Interface 1 &gt;&gt; Descr: 'Intel(R)-8255x-based-Network-Connection'...
 ### The following interface is commented out because:
 ### * has a speed of 0 which makes no sense
 #
 ...
</code></pre>
<p> If this occurs, edit MakeMrtgCfg.ncf and add the following parameter as shown: </p>
<pre><code> perl sys:\mrtg\bin\cfgmaker.pl --zero-speed=nnn public [at] 10.202.65.180 &gt; sys:\mrtg\bin\Mrtg.cfg
</code></pre>
<p> where <code>nnn</code> is the interface speed in bits per second. For a 100 Megabit LAN NIC, nnn = 10000000. It will be necessary to re-execute the MakeMrtgCfg.ncf script before continuing with this section. </p>
<p> Below line 16 (*** Global Defaults), add: </p>
<pre><code> HtmlDir: &lt;a path&gt; e.g HtmlDir: sys:/mrtg/html
 ImageDir: &lt;a path&gt; e.g ImageDir: sys:/mrtg/html/work
 LogDir: &lt;a path&gt; e.g LogDir: sys:/mrtg/logs
 IconDir: &lt;a path&gt; e.g IconDir: ./images
</code></pre>
<p> Note 1. The HtmlDir entry specifies where MRTG will create its HTML pages. </p>
<p> Note 2. The ImageDir entry specifies where the created graphic icons are placed. </p>
<p> Note 3. The IconDir entry specifies where the supplied MRTG icons are located. It MUST be a relative path from HtmlDir or absolute URL. The value shown is recommended. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> At the server console run: </p>
<pre><code> sys:/mrtg/bin/RunMrtg.ncf
</code></pre>
<p> several times. By the third time it should run without showing error messages on the console screen. </p>
<p> This should create. </p>
<p> &#8211; A HTML page in the (HtmlDir) directory for each monitored device, </p>
<p> &#8211; A .dat file in the (ImageDir) directory for each monitored device, </p>
<p> &#8211; Several .png icons in the (ImageDir) directory, </p>
<p> &#8211; Some log file entries in the (LogDir) directory. </p>
<p> Note: If you experience a ``Use of uninitialised value in split&#8217;&#8216; error, it will be necessary to create a &#8216;Path&#8217; environment variable at the server console; use the following example </p>
<pre><code> env path=&quot;SYS:\&quot; (The actual value is immaterial, as long as the var itself exists.)
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Edit sys:/mrtg/bin/MakeMrtgIndex.ncf. Change the indicated &lt;path&gt; shown in the following example to match the value entered for (HtmlDir). </p>
<pre><code> perl --noscreen sys:/mrtg/bin/indexmaker.pl sys:/mrtg/bin/Mrtg.cfg &gt; &lt;path&gt;/index.html
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Create an index.html page linking the seperate device HTML page(s). At the server console, run: </p>
<pre><code> sys:/mrtg/bin/MakeMrtgIndex.ncf
</code></pre>
<p> This will create index.html in the (HtmlDir) directory. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Optionally, configure a Web Server to permit access to the directory specified in (HtmlDir) to view the MRTG graphs remotely, at, for example: </p>
<pre><code>http://ip_or_dns/mrtg/index.html
</code></pre>
<p> A sample configuration for an Apache Webserver is shown: </p>
<pre><code> Alias /mrtg/ &quot;SYS:/mrtg/html/&quot;
 &lt;Directory &quot;SYS:/mrtg/html&quot;&gt;
             AllowOverride None
             Order allow,deny
             Allow from all
 &lt;/Directory&gt;
</code></pre>
 </dd>
<dt>&bull;</dt>
<dd> <p> Set the property of the directory pointed to by (ImageDir), to &#8216;Purge Immediate&#8217;. </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Finally, read the MRTG documentation for much more detailed configuration/usage information. </p>
 </dd></dl>
<p> Welcome to MRTG!!  </p>
<h2>MAKE MRTG RUN ALL THE TIME</h2>
<p> MRTG can be made to run periodically by at least two means: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Using CRON Scheduling </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Running MRTG in Daemon Mode </p>
 </dd></dl>
<h3>CRON Scheduling</h3>
<p> To use CRON scheduling, create a CRON Scheduler entry to execute the RunMrtg.ncf file on a frequency appropriate for the server environment and information desired. The following entry in the sys:\etc\crontab file will execute MRTG every five minutes: </p>
<pre><code> 0,5,10,15,20,25,30,35,40,45,50,55 * * * * sys:\mrtg\bin\runmrtg.ncf
</code></pre>
<p> The CRON Scheduler (cron.nlm) can be started automatically by adding it in AUTOEXEC.ncf or, manually loading it at the server console.  </p>
<h3>MRTG in Daemon Mode</h3>
<p> Refer to the MRTG-Reference document for information about the &#8216;RunAsDaemon&#8217; option. Its use is outside the scope of this document.  </p>
<h2>TROUBLESHOOTING</h2>
<p> Read the MRTG documents, Perl documents or, finally, submit questions to the MRTG User forums. </p>
<p> For NetWare specific issues, submit questions to the Perl forum at <a href="news://developer-forums.novell.com/novell.devsup.perl">news://developer-forums.novell.com/novell.devsup.perl</a> (Novell Developer Forums).  </p>
<h2>COMPILING RATEUP.NLM</h2>
<p> In addition to the rateup.c and Makefile.Netware supplied with the MRTG release, you will also need: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> Metrowerks CodeWarrior with NetWare Support OR GCC Compiler (v3.0.3 or later) with NlmConv Utility </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> Novell LibC NDK (February 2004 or later) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> GD Graphics Library (v2.0.33 or later) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> LibPNG Graphics Library (v1.2.8 or later) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> ZLib Library (v1.2.3 or later) </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> The get_ver.awk script </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> A copy of the GNU build tools. (See <a rel="nofollow" href="http://sourceforge.net/projects/gnuwin32/)">http://sourceforge.net/projects/gnuwin32/)</a> </p>
 </dd></dl>
<p> The auxiliary libraries can be obtained from: </p>
<p> GD Graphics Library. (See <a rel="nofollow" href="http://www.boutell.com/gd/">http://www.boutell.com/gd/</a> ) </p>
<p> PNG Graphics Library. (See <a rel="nofollow" href="http://libpng.sourceforge.net/">http://libpng.sourceforge.net/</a> ) </p>
<p> zLib Compression Library. (See <a rel="nofollow" href="http://www.gzip.org/zlib/">http://www.gzip.org/zlib/</a> ) </p>
<p> Edit the Makefile.Netware file as required to match your installation paths; search the file for the key word &#8216;Edit&#8217;.  </p>
<h2>NETWARE SUPPORT</h2>
<p> For copies of the NCF and get_ver.awk scripts, see Appendix. </p>
<p> For NetWare specific issues, submit questions to the Perl forum at <a href="news://developer-forums.novell.com/novell.devsup.perl">news://developer-forums.novell.com/novell.devsup.perl</a> (Novell Developer Forums). </p>
<p> To move the MRTG application to a volume other than SYS: you will need to edit the NCF scripts provided plus the MRTG[.pl] script itself in two places.  </p>
<h2>NEW RATEUP SWITCH</h2>
<p> The MRTG[.pl] script, when used on a NetWare platform, uses Rateup[.nlm] with the new commandline switch: </p>
<pre><code>     RATEUP -f filename
</code></pre>
<p> where the filename parameter can include a leading path element. </p>
<p> The file format is exactly the same as that used on the commandline by other operating systems, including the leading path and name of the Rateup NLM.  </p>
<h2>APPENDIX</h2>
<p> The Appendix includes &#8216;copies&#8217; of the following files: </p>
<dl>
<dt>&bull;</dt>
<dd> <p> The NCF files used during MRTG configuration, </p>
 </dd></dl>
<p> To create copies of these files, simply &#8216;cut and paste&#8217; into your favourite &#8216;<code>text editor</code>&#8216; and save under their respective names. You should remove the leading space from each line. </p>
<p> <i>MakeMrtgCfg.NCF</i> </p>
<pre><code> # MakeMrtgCfg.NCF
 # Purpose : Create the MRTG Configuration File
 # Changed : 5/05/2005 New
 # Located : SYS:MRTG\BIN
 # Set For :
 # Params :
 # Edit this file and:
 # Replace ccccc with your device GET SNMP Community Name - If unsure try 'public'.
 # Replace ddddd with your device IP (n.n.n.n) or domain name.
 perl --noscreen sys:\mrtg\bin\cfgmaker.pl ccccc [at] ddddd &gt; sys:\mrtg\bin\Mrtg.cfg
 #
 # End of MakeMrtgCfg.NCF
</code></pre>
<p> <i>RunMrtg.NCF</i> </p>
<pre><code> # RunMrtg.NCF
 # Purpose : Run the MRTG Application
 # Changed : 5/05/2005 New
 # Located : SYS:MRTG\BIN
 # Set For :
 # Params :
 # The paths are as per the examples recommended in &quot;Getting Started&quot;.
 perl --noscreen sys:\mrtg\bin\mrtg.pl sys:\mrtg\bin\mrtg.cfg
 #
 # End of RunMrtg.NCF
</code></pre>
<p> <i>MakeMrtgIndex.NCF</i> </p>
<pre><code> # MakeMrtgIndex.NCF
 # Purpose : Create the HTML Index File for MRTG HTML data pages
 # Changed : 5/05/2005 New
 # Located : SYS:MRTG\BIN
 # Set For :
 # Params :
 # Note: Edit this file and change the redirected output to the location
 # specified for HtmlDir or WorkDir. The sys:\apache2\htdocs\mrtg\index.html
 # is based on the examples in &quot;Getting Started&quot;.
 perl --noscreen sys:\mrtg\bin\indexmaker.pl sys:\mrtg\bin\Mrtg.cfg &gt; sys:\mrtg\html\index.html
 #
 # End of MakeMrtgIndex.NCF
</code></pre>
<h2>LICENSE</h2>
<p> GNU General Public License  </p>
<h2>CREDITS</h2>
<p> The MRTG for NetWare exists largely through the efforts of Guenter Knauf and feedback from beta testers.  </p>
<h2>AUTHOR</h2>
<p> Norm W.. </p>
