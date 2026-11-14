---
title: "amanda-match(7)"
name: "amanda-match"
section: "7"
letter: "a"
url: "/docs/linux/man/7-amanda-match/"
description: "amanda-match – Common Amanda Match Expression"
---

<p>amanda-match &#8211; Common Amanda Match Expression</p>
<h2>Description</h2>
<p>Several Amanda commands allow the user to specify dumps using &quot;match expressions&quot;. This manual page describes the syntax of these expressions. </p>
<p> In some places, only certain match expressions are allowed. However, several commands take a dump specification (&quot;dumpspec&quot;) consisting of a sequence of several expressions intended to match particular dumps in the catalog. Other applications take a DLE specification which indicates a set of DLEs to be operated on. These formats are described below. </p>
<p> An expression can be disabled be preceding it with the &#8216;=&#8217; character, in that case, an exact match is used. </p>
<p> Many program have an &#8216;&#8211;exact-match&#8217; argument that disable expression and exact match are used.</p>
<h2>HOST &amp; DISK EXPRESSIONS</h2>
<p>The hosts and disks match by word. Each word is a glob expression, and words are separated by the character &#8216;.&#8217; for host expressions and &#8216;/&#8217; for disk expressions. You can anchor the expression on the left with a &#8216;^&#8217; or on the right with a &#8216;$&#8217;. The matcher is case insensitive for hosts but case sensitive for disks. A match succeeds if all words in the expression match contiguous words in the host or disk. </p>
<p> If the disk is a UNC (&quot;\windows\share&quot;) then all &#8216;\&#8217; are converted to &#8216;/&#8217; before the match. Using &#8216;\&#8217; is complicated because of the extra quoting required by the shell and amanda. It&#8217;s easier to use &#8216;/&#8217; because it requires less quoting (&quot;//windows/share&quot;) </p>
<p> The special characters follow. Note that the shell interprets some of these characters, so when used on the command line, they must be escaped appropriately for the shell. </p>
<p> dot (.)</p>
<dl>
<dd>word separator for a host</dl>
<p> /</p>
<dl>
<dd>word separator for a disk</dl>
<p> \</p>
<dl>
<dd>word separator for a UNC disk</dl>
<p> ^</p>
<dl>
<dd>anchor at left of word</dl>
<p> $</p>
<dl>
<dd>anchor at right of word</dl>
<p> ?</p>
<dl>
<dd>match exactly one character except the separator</dl>
<p> *</p>
<dl>
<dd>match zero or more characters except the separator</dl>
<p> **</p>
<dl>
<dd>match zero or more characters including the separator</dl>
<p> [&#8230;]</p>
<dl>
<dd>match exactly one of the characters enclosed by the brackets.</dl>
<p> [!&#8230;]</p>
<dl>
<dd>match exactly one character that is not enclosed by the brackets.</dl>
<h3>Examples</h3>
<p>hosta</p>
<dl>
<dd>Will match hosta, foo.hosta.org, and hoSTA.dOMAIna.ORG but not hostb.</dl>
<p> host</p>
<dl>
<dd>Will match host but not hosta.</dl>
<p> host?</p>
<dl>
<dd>Will match hosta and hostb, but not host or hostabc.</dl>
<p> ho*na</p>
<dl>
<dd>Will match hoina but not ho.aina.org.</dl>
<p> ho**na</p>
<dl>
<dd>Will match hoina and ho.aina.org.</dl>
<p> ^hosta</p>
<dl>
<dd>Will match hosta but not foo.hosta.org.</dl>
<p> sda*</p>
<dl>
<dd>Will match /dev/sda1 and /dev/sda12.</dl>
<p> /opt</p>
<dl>
<dd>Will match the disk opt but not the host opt.</dl>
<p> (note dots:) .opt.</p>
<dl>
<dd>Will match the host opt but not the disk opt.</dl>
<p> /</p>
<dl>
<dd>Will match the disk / but no other disk.</dl>
<p> /usr</p>
<dl>
<dd>Will match the disks /usr and /usr/local.</dl>
<p> /usr$</p>
<dl>
<dd>Will match the disks /usr but not /usr/local.</dl>
<p> share</p>
<dl>
<dd>Will match the disks \windows1\share and \windows2\share.</dl>
<p> share*</p>
<dl>
<dd>Will match the disks \windows\share1 and \windows\share2.</dl>
<p> //windows/share</p>
<dl>
<dd>Will match the disk \windows\share.</dl>
<h2>Datestamp Expressions</h2>
<p>A datestamp expression is either a prefix of the datestamp, or a range expression (separated by &#8216;-&#8216;) matching several prefixes. A leading ^ is removed, while arailing $ will force an exact match.</p>
<h3>Examples</h3>
<p>20001212-14</p>
<dl>
<dd>match all dates beginning with 20001212, 20001213 or 20001214</dl>
<p> 20001212-4</p>
<dl>
<dd>same as previous</dl>
<p> 20001212-24</p>
<dl>
<dd>match all dates between 20001212 and 20001224</dl>
<p> 2000121</p>
<dl>
<dd>match all dates that start with 2000121 (20001210-20001219)</dl>
<p> 2</p>
<dl>
<dd>match all dates that start with 2 (20000101-29991231)</dl>
<p> 2000-10</p>
<dl>
<dd>match all dates between 20000101-20101231</dl>
<p> 200010$</p>
<dl>
<dd>match only 200010</dl>
<h2>Level Expressions</h2>
<p>Level expressions are either prefix matches e.g., &quot;1&quot;, which matches &quot;1&quot;, &quot;10&quot;, and &quot;123&quot;, absolute matches e.g., &quot;3$&quot; which only matches &quot;3&quot;, or a range e.g., &quot;3-5&quot; which only matches levels 3, 4, and 5.</p>
<h2>Dump Specifications</h2>
<p>A dump specification is used to select one or more dumps from the catalog. It consists of a sequence of match expressions in the order host, disk, datestamp, and level. Note that some commands do not take a level argument, out of historical accident. Note, too, that the datestamp expression matches the time that the dump was made on the Amanda client, rather than the date it was moved to tape.</p>
<h3>Examples</h3>
<p>amtool MyConfig ^vpdesktop$</p>
<dl>
<dd>all dumps of host &quot;vpdesktop&quot;</dl>
<p> amtool MyConfig &#8216;*&#8217; /var/stage</p>
<dl>
<dd>All dumps of /var/stage on any host</dl>
<p> amtool MyConfig www1 /var/www &#8216;*&#8217; www2 /var/www &#8216;*&#8217;</p>
<dl>
<dd>All dumps of /var/www on www1 and www2 (assuming amtool does not require a level argument)</dl>
<h2>Dle Specifications</h2>
<p>A DLE specification is used to select one or more DLEs. It consists of a sequence of match expressions. The first must be a host, and subsequent expressions will be experimentally matched against both hosts and disks in the <code><a href="/docs/linux/man/5-disklist/">disklist</a></code>(5), preferring hosts. This dynamic matching process can lead to odd behavior in extreme cases (e.g., where a disk and a host have the same name), but for most uses does exactly what is expected.</p>
<h3>Examples</h3>
<p>amtool MyConfig vpdesktop /home/anderson</p>
<dl>
<dd>/home/anderson on host vpdesktop</dl>
<p> amtool MyConfig &#8216;*&#8217; ^/etc &#8216;*&#8217; ^/var</p>
<dl>
<dd>All DLEs matching ^/var or ^/etc on any host</dl>
<p> amtool MyConfig web1 www web2 www</p>
<dl>
<dd>If no host matches &quot;www&quot;, all DLEs matching www on hosts web1 and web2. If a host matches &quot;www&quot;, then all DLEs on hosts www, web1, and web2.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/8-amfetchdump/">amfetchdump</a></code>(8), <code><a href="/docs/linux/man/8-amrestore/">amrestore</a></code>(8), <code><a href="/docs/linux/man/8-amadmin/">amadmin</a></code>(8), <code><a href="/docs/linux/man/8-amvault/">amvault</a></code>(8), <code><a href="/docs/linux/man/8-amflush/">amflush</a></code>(8), <code><a href="/docs/linux/man/8-amdump/">amdump</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Author</h2>
<p><code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
