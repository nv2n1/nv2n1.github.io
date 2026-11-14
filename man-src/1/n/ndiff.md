---
title: "ndiff(1)"
name: "ndiff"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ndiff/"
description: "ndiff – Utility to compare the results of Nmap scans"
---

<h2 class="name">NAME</h2>
<p> ndiff &#8211; Utility to compare the results of Nmap scans </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>ndiff</code> [<i>options</i>] {<i>a.xml</i>} {<i>b.xml</i>}</dl>
<h2>DESCRIPTION</h2>
<dd>Ndiff is a tool to aid in the comparison of Nmap scans. It takes two Nmap XML output files and prints the differences between them. The differences observed are: </p>
<dl>
<dt>
<dd> &bull; Host states (e.g. up to down)</dl>
<dl>
<dt>
<dd> &bull; Port states (e.g. open to closed)</dl>
<dl>
<dt>
<dd> &bull; Service versions (from <code>-sV</code>)</dl>
<dl>
<dt>
<dd> &bull; OS matches (from <code>-O</code>)</dl>
<dl>
<dt>
<dd> &bull; Script output</dl>
<p> Ndiff, like the standard <code>diff</code> utility, compares two scans at a time.</p>
<h2>OPTIONS SUMMARY</h2>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show a help message and exit.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Include all hosts and ports in the output, not only those that have changed.</dl>
<p> <code>&#8211;text</code></p>
<dl>
<dt>
<dd> Write output in human-readable text format.</dl>
<p> <code>&#8211;xml</code></p>
<dl>
<dt>
<dd> Write output in machine-readable XML format. The document structure is defined in the file ndiff.dtd included in the distribution.</dl>
<p> Any other arguments are taken to be the names of Nmap XML output files. There must be exactly two.</p>
<h2>EXAMPLE</h2>
<p> Let&#8217;s use Ndiff to compare the output of two Nmap scans that use different options. In the first, we&#8217;ll do a fast scan (<code>-F</code>), which scans fewer ports for speed. In the second, we&#8217;ll scan the larger default set of ports, and run an NSE script. </p>
<dl>
<dt>
<dd>
<pre>
# <code>nmap -F scanme.nmap.org -oX scanme-1.xml</code>
# <code>nmap --script=html-title scanme.nmap.org -oX scanme-2.xml</code>
$ <code>ndiff -v scanme-1.xml scanme-2.xml</code>
-Nmap 5.35DC1 at 2010-07-16 12:09
+Nmap 5.35DC1 at 2010-07-16 12:13
 scanme.nmap.org (64.13.134.52):
 Host is up.
-Not shown: 95 filtered ports
+Not shown: 993 filtered ports
 PORT      STATE  SERVICE VERSION
 22/tcp    open   ssh
 25/tcp    closed smtp
 53/tcp    open   domain
+70/tcp    closed gopher
 80/tcp    open   http
+|_ html-title: Go ahead and ScanMe!
 113/tcp   closed auth
+31337/tcp closed Elite
</pre>
</dl>
<p> Changes are marked by a &#8211; or + at the beginning of a line. We can see from the output that the scan without the <code>-F</code> fast scan option found two additional ports: 70 and 31337. The html-title script produced some additional output for port 80. From the port counts, we may infer that the fast scan scanned 100 ports (95 filtered, 3 open, and 2 closed), while the normal scan scanned 1000 (993 filtered, 3 open, and 4 closed). </p>
<p> The <code>-v</code> (or <code>&#8211;verbose</code>) option to Ndiff made it show even the ports that didn&#8217;t change, like 22 and 25. Without <code>-v</code>, they would not have been shown.</p>
<h2>OUTPUT</h2>
<p> There are two output modes: text and XML. Text output is the default, and can also be selected with the <code>&#8211;text</code> option. Text output resembles a unified diff of Nmap&#8217;s normal terminal output. Each line is preceded by a character indicating whether and how it changed. &#8211; means that the line was in the first scan but not in the second; + means it was in the second but not the first. A line that changed is represented by a &#8211; line followed by a + line. Lines that did not change are preceded by a blank space. </p>
<p> Example 1 is an example of text output. Here, port 80 on the host photos-cache-snc1.facebook.com gained a service version (lighttpd 1.5.0). The host at 69.63.179.25 changed its reverse DNS name. The host at 69.63.184.145 was completely absent in the first scan but came up in the second. </p>
<p> <code>Example 1. Ndiff text output</code> </p>
<dl>
<dt>
<dd>
<pre>
-Nmap 4.85BETA3 at 2009-03-15 11:00
+Nmap 4.85BETA4 at 2009-03-18 11:00
 photos-cache-snc1.facebook.com (69.63.178.41):
 Host is up.
 Not shown: 99 filtered ports
 PORT   STATE SERVICE VERSION
-80/tcp open  http
+80/tcp open  http    lighttpd 1.5.0
-cm.out.snc1.tfbnw.net (69.63.179.25):
+mailout-snc1.facebook.com (69.63.179.25):
 Host is up.
 Not shown: 100 filtered ports
+69.63.184.145:
+Host is up.
+Not shown: 98 filtered ports
+PORT    STATE SERVICE  VERSION
+80/tcp  open  http     Apache httpd 1.3.41.fb1
+443/tcp open  ssl/http Apache httpd 1.3.41.fb1
</pre>
</dl>
<p> XML output, intended to be processed by other programs, is selected with the <code>&#8211;xml</code> option. It is based on Nmap&#8217;s XML output, with a few additional elements to indicate differences. The XML document is enclosed in <i>nmapdiff</i> and <i>scandiff</i> elements. Host differences are enclosed in <i>hostdiff</i> tags and port differences are enclosed in <i>portdiff</i> tags. Inside a <i>hostdiff</i> or <i>portdiff</i>, <i>a</i> and <i>b</i> tags show the state of the host or port in the first scan (<i>a</i>) or the second scan (<i>b</i>). </p>
<p> Example 2 shows the XML diff of the same scans shown above in Example 1. Notice how port 80 of photos-cache-snc1.facebook.com is enclosed in <i>portdiff</i> tags. For 69.63.179.25, the old hostname is in <i>a</i> tags and the new is in <i>b</i>. For the new host 69.63.184.145, there is a <i>b</i> in the <i>hostdiff</i> without a corresponding <i>a</i>, indicating that there was no information for the host in the first scan. </p>
<p> <code>Example 2. Ndiff XML output</code> </p>
<dl>
<dt>
<dd>
<pre>
&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;nmapdiff version=&quot;1&quot;&gt;
  &lt;scandiff&gt;
    &lt;hostdiff&gt;
      &lt;host&gt;
        &lt;status state=&quot;up&quot;/&gt;
        &lt;address addr=&quot;69.63.178.41&quot; addrtype=&quot;ipv4&quot;/&gt;
        &lt;hostnames&gt;
          &lt;hostname name=&quot;photos-cache-snc1.facebook.com&quot;/&gt;
        &lt;/hostnames&gt;
        &lt;ports&gt;
          &lt;extraports count=&quot;99&quot; state=&quot;filtered&quot;/&gt;
          &lt;portdiff&gt;
            &lt;port portid=&quot;80&quot; protocol=&quot;tcp&quot;&gt;
              &lt;state state=&quot;open&quot;/&gt;
              &lt;a&gt;
                &lt;service name=&quot;http&quot;/&gt;
              &lt;/a&gt;
              &lt;b&gt;
                &lt;service name=&quot;http&quot; product=&quot;lighttpd&quot; version=&quot;1.5.0&quot;/&gt;
              &lt;/b&gt;
            &lt;/port&gt;
          &lt;/portdiff&gt;
        &lt;/ports&gt;
      &lt;/host&gt;
    &lt;/hostdiff&gt;
    &lt;hostdiff&gt;
      &lt;host&gt;
        &lt;status state=&quot;up&quot;/&gt;
        &lt;address addr=&quot;69.63.179.25&quot; addrtype=&quot;ipv4&quot;/&gt;
        &lt;hostnames&gt;
          &lt;a&gt;
            &lt;hostname name=&quot;cm.out.snc1.tfbnw.net&quot;/&gt;
          &lt;/a&gt;
          &lt;b&gt;
            &lt;hostname name=&quot;mailout-snc1.facebook.com&quot;/&gt;
          &lt;/b&gt;
        &lt;/hostnames&gt;
        &lt;ports&gt;
          &lt;extraports count=&quot;100&quot; state=&quot;filtered&quot;/&gt;
        &lt;/ports&gt;
      &lt;/host&gt;
    &lt;/hostdiff&gt;
    &lt;hostdiff&gt;
      &lt;b&gt;
        &lt;host&gt;
          &lt;status state=&quot;up&quot;/&gt;
          &lt;address addr=&quot;69.63.184.145&quot; addrtype=&quot;ipv4&quot;/&gt;
          &lt;ports&gt;
            &lt;extraports count=&quot;98&quot; state=&quot;filtered&quot;/&gt;
            &lt;port portid=&quot;80&quot; protocol=&quot;tcp&quot;&gt;
              &lt;state state=&quot;open&quot;/&gt;
              &lt;service name=&quot;http&quot; product=&quot;Apache httpd&quot;
                       version=&quot;1.3.41.fb1&quot;/&gt;
            &lt;/port&gt;
            &lt;port portid=&quot;443&quot; protocol=&quot;tcp&quot;&gt;
              &lt;state state=&quot;open&quot;/&gt;
              &lt;service name=&quot;http&quot; product=&quot;Apache httpd&quot; tunnel=&quot;ssl&quot;
                       version=&quot;1.3.41.fb1&quot;/&gt;
            &lt;/port&gt;
          &lt;/ports&gt;
        &lt;/host&gt;
      &lt;/b&gt;
    &lt;/hostdiff&gt;
  &lt;/scandiff&gt;
&lt;/nmapdiff&gt;
</pre>
</dl>
<h2>PERIODIC DIFFS</h2>
<p> Using Nmap, Ndiff, cron, and a shell script, it&#8217;s possible to scan a network daily and get email reports of the state of the network and changes since the previous scan. Example 3 shows the script that ties it together. </p>
<p> <code>Example 3. Scanning a network periodically with Ndiff and cron</code> </p>
<dl>
<dt>
<dd>
<pre><code>
#!/ bin / sh
TARGETS = "targets" OPTIONS = "-v -T4 -F -sV" date =`date + % F` cd / root / scans nmap $OPTIONS $TARGETS - oA scan - $date &gt; / dev / null if[-e scan - prev.xml];
then
            ndiff scan -
        prev.xml scan - $date.xml &gt;
    diff - $date echo "*** NDIFF RESULTS ***" cat diff - $date echo fi echo "*** NMAP RESULTS ***" cat scan - $date.nmap ln - sf scan - $date.xml scan - prev.xml
</code></pre>
</dl>
<p> If the script is saved as /root/scan-ndiff.sh, add the following line to root&#8217;s crontab: </p>
<dl>
<dt>
<dd>
<pre>
0 12 * * * /root/scan-ndiff.sh
</pre>
</dl>
<h2>EXIT CODE</h2>
<p> The exit code indicates whether the scans are equal. </p>
<dl>
<dt>
<dd> &bull; 0 means that the scans are the same in all the aspects Ndiff knows about.</dl>
<dl>
<dt>
<dd> &bull; 1 means that the scans differ.</dl>
<dl>
<dt>
<dd> &bull; 2 indicates a runtime error, such as the failure to open a file.</dl>
<h2>BUGS</h2>
<p> Report bugs to the nmap-dev mailing list at &lt;dev [at] nmap.org&gt;.</p>
<h2>HISTORY</h2>
<p> Ndiff started as a project by Michael Pattrick during the 2008 Google Summer of Code. Michael designed the program and led the discussion of its output formats. He wrote versions of the program in Perl and C++, but the summer ended shortly after it was decided to rewrite the program in Python for the sake of Windows (and Zenmap) compatibility. This Python version was written by David Fifield. James Levine m[blue]<code>released</code>m[]<font SIZE="-2">[1]</font> a Perl script named Ndiff with similar functionality in 2000.</p>
<h2>AUTHORS</h2>
<p> David Fifield &lt;david [at] bamsoftware.com&gt; </p>
<p> Michael Pattrick &lt;mpattrick [at] rhinovirus.org&gt;</p>
<h2>WEB SITE</h2>
<p> m[blue]<code><a rel="nofollow" href="http://nmap.org/ndiff/">http://nmap.org/ndiff/</a></code>m[]</p>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> released</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://seclists.org/nmap-hackers/2000/315">http://seclists.org/nmap-hackers/2000/315</a></dl>
</dl>
<h2>Index</h2>
