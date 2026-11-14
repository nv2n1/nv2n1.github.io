---
title: "httrack(1)"
name: "httrack"
section: "1"
letter: "h"
url: "/docs/linux/man/1-httrack/"
description: "httrack – offline browser : copy websites to a local directory"
---

<h2>NAME</h2>
<p> httrack &#8211; offline browser : copy websites to a local directory</p>
<h2>SYNOPSIS</h2>
<p> <code>httrack [ url ]&#8230; [ -filter ]&#8230; [ +filter ]&#8230; [ </code> <code>-O, &#8211;path </code> ] [ <code>-w, &#8211;mirror </code> ] [ <code>-W, &#8211;mirror-wizard </code> ] [ <code>-g, &#8211;get-files </code> ] [ <code>-i, &#8211;continue </code> ] [ <code>-Y, &#8211;mirrorlinks </code> ] [ <code>-P, &#8211;proxy </code> ] [ <code>-%f, &#8211;httpproxy-ftp[=N] </code> ] [ <code>-%b, &#8211;bind </code> ] [ <code>-rN, &#8211;depth[=N] </code> ] [ <code>-%eN, &#8211;ext-depth[=N] </code> ] [ <code>-mN, &#8211;max-files[=N] </code> ] [ <code>-MN, &#8211;max-size[=N] </code> ] [ <code>-EN, &#8211;max-time[=N] </code> ] [ <code>-AN, &#8211;max-rate[=N] </code> ] [ <code>-%cN, &#8211;connection-per-second[=N] </code> ] [ <code>-GN, &#8211;max-pause[=N] </code> ] [ <code>-cN, &#8211;sockets[=N] </code> ] [ <code>-TN, &#8211;timeout[=N] </code> ] [ <code>-RN, &#8211;retries[=N] </code> ] [ <code>-JN, &#8211;min-rate[=N] </code> ] [ <code>-HN, &#8211;host-control[=N] </code> ] [ <code>-%P, &#8211;extended-parsing[=N] </code> ] [ <code>-n, &#8211;near </code> ] [ <code>-t, &#8211;test </code> ] [ <code>-%L, &#8211;list </code> ] [ <code>-%S, &#8211;urllist </code> ] [ <code>-NN, &#8211;structure[=N] </code> ] [ <code>-%D, &#8211;cached-delayed-type-check </code> ] [ <code>-%M, &#8211;mime-html </code> ] [ <code>-LN, &#8211;long-names[=N] </code> ] [ <code>-KN, &#8211;keep-links[=N] </code> ] [ <code>-x, &#8211;replace-external </code> ] [ <code>-%x, &#8211;disable-passwords </code> ] [ <code>-%q, &#8211;include-query-string </code> ] [ <code>-o, &#8211;generate-errors </code> ] [ <code>-X, &#8211;purge-old[=N] </code> ] [ <code>-%p, &#8211;preserve </code> ] [ <code>-%T, &#8211;utf8-conversion </code> ] [ <code>-bN, &#8211;cookies[=N] </code> ] [ <code>-u, &#8211;check-type[=N] </code> ] [ <code>-j, &#8211;parse-java[=N] </code> ] [ <code>-sN, &#8211;robots[=N] </code> ] [ <code>-%h, &#8211;http-10 </code> ] [ <code>-%k, &#8211;keep-alive </code> ] [ <code>-%B, &#8211;tolerant </code> ] [ <code>-%s, &#8211;updatehack </code> ] [ <code>-%u, &#8211;urlhack </code> ] [ <code>-%A, &#8211;assume </code> ] [ <code>-@iN, &#8211;protocol[=N] </code> ] [ <code>-%w, &#8211;disable-module </code> ] [ <code>-F, &#8211;user-agent </code> ] [ <code>-%R, &#8211;referer </code> ] [ <code>-%E, &#8211;from </code> ] [ <code>-%F, &#8211;footer </code> ] [ <code>-%l, &#8211;language </code> ] [ <code>-%a, &#8211;accept </code> ] [ <code>-%X, &#8211;headers </code> ] [ <code>-C, &#8211;cache[=N] </code> ] [ <code>-k, &#8211;store-all-in-cache </code> ] [ <code>-%n, &#8211;do-not-recatch </code> ] [ <code>-%v, &#8211;display </code> ] [ <code>-Q, &#8211;do-not-log </code> ] [ <code>-q, &#8211;quiet </code> ] [ <code>-z, &#8211;extra-log </code> ] [ <code>-Z, &#8211;debug-log </code> ] [ <code>-v, &#8211;verbose </code> ] [ <code>-f, &#8211;file-log </code> ] [ <code>-f2, &#8211;single-log </code> ] [ <code>-I, &#8211;index </code> ] [ <code>-%i, &#8211;build-top-index </code> ] [ <code>-%I, &#8211;search-index </code> ] [ <code>-pN, &#8211;priority[=N] </code> ] [ <code>-S, &#8211;stay-on-same-dir </code> ] [ <code>-D, &#8211;can-go-down </code> ] [ <code>-U, &#8211;can-go-up </code> ] [ <code>-B, &#8211;can-go-up-and-down </code> ] [ <code>-a, &#8211;stay-on-same-address </code> ] [ <code>-d, &#8211;stay-on-same-domain </code> ] [ <code>-l, &#8211;stay-on-same-tld </code> ] [ <code>-e, &#8211;go-everywhere </code> ] [ <code>-%H, &#8211;debug-headers </code> ] [ <code>-%!, &#8211;disable-security-limits </code> ] [ <code>-V, &#8211;userdef-cmd </code> ] [ <code>-%W, &#8211;callback </code> ] [ <code>-K, &#8211;keep-links[=N] </code> ] [</p>
<h2>DESCRIPTION</h2>
<p> <code>httrack</code> allows you to download a World Wide Web site from the Internet to a local directory, building recursively all directories, getting HTML, images, and other files from the server to your computer. HTTrack arranges the original site&#8217;s relative link-structure. Simply open a page of the &quot;mirrored&quot; website in your browser, and you can browse the site from link to link, as if you were viewing it online. HTTrack can also update an existing mirrored site, and resume interrupted downloads.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>httrack <a rel="nofollow" href="http://www.someweb.com">www.someweb.com</a>/bob/</code></p>
<dd>
&nbsp;<wbr>mirror site&nbsp;<wbr><a rel="nofollow" href="http://www.someweb.com">www.someweb.com</a>/bob/&nbsp;<wbr>and only this site</p>
<dt><code>httrack <a rel="nofollow" href="http://www.someweb.com">www.someweb.com</a>/bob/ <a href="http://www.anothertest.com">www.anothertest.com</a>/mike/ +*.com/*.jpg -mime:application/*</code></p>
<dd>
&nbsp;<wbr>mirror the two sites together&nbsp;<wbr>(with shared links)&nbsp;<wbr>and accept any .jpg files on .com sites</p>
<dt><code>httrack <a rel="nofollow" href="http://www.someweb.com">www.someweb.com</a>/bob/bobby.html +* -r6</code></p>
<dd> means get all files starting from bobby.html, with 6 link-depth, and possibility of going everywhere on the web</p>
<dt><code>httrack <a rel="nofollow" href="http://www.someweb.com">www.someweb.com</a>/bob/bobby.html &#8211;spider -P proxy.myhost.com:8080</code></p>
<dd> runs the spider on <a rel="nofollow" href="http://www.someweb.com">www.someweb.com</a>/bob/bobby.html using a proxy</p>
<dt><code>httrack &#8211;update</code></p>
<dd> updates a mirror in the current folder</p>
<dt><code>httrack</code></p>
<dd> will bring you to the interactive mode</p>
<dt><code>httrack &#8211;continue</code></p>
<dd> continues a mirror in the current folder</dl>
<h2>OPTIONS</h2>
<h3>General options:</h3>
<dl>
<dt>-O</p>
<dd> path for mirror/logfiles+cache (-O path mirror[,path cache and logfiles]) (&#8211;path &lt;param&gt;) </p>
</dl>
<h3>Action options:</h3>
<dl>
<dt>-w</p>
<dd> *mirror web sites (&#8211;mirror)</p>
<dt>-W</p>
<dd> mirror web sites, semi-automatic (asks questions) (&#8211;mirror-wizard)</p>
<dt>-g</p>
<dd> just get files (saved in the current directory) (&#8211;get-files)</p>
<dt>-i</p>
<dd> continue an interrupted mirror using the cache (&#8211;continue)</p>
<dt>-Y</p>
<dd> mirror ALL links located in the first level pages (mirror links) (&#8211;mirrorlinks) </p>
</dl>
<h3>Proxy options:</h3>
<dl>
<dt>-P</p>
<dd> proxy use (-P proxy:port or -P user:pass [at] proxy:port) (&#8211;proxy &lt;param&gt;)</p>
<dt>-%f</p>
<dd> *use proxy for ftp (f0 don t use) (&#8211;httpproxy-ftp[=N])</p>
<dt>-%b</p>
<dd> use this local hostname to make/send requests (-%b hostname) (&#8211;bind &lt;param&gt;) </p>
</dl>
<h3>Limits options:</h3>
<dl>
<dt>-rN</p>
<dd> set the mirror depth to N (* r9999) (&#8211;depth[=N])</p>
<dt>-%eN</p>
<dd> set the external links depth to N (* %e0) (&#8211;ext-depth[=N])</p>
<dt>-mN</p>
<dd> maximum file length for a non-html file (&#8211;max-files[=N])</p>
<dt>-mN,N2</p>
<dd> maximum file length for non html (N) and html (N2)</p>
<dt>-MN</p>
<dd> maximum overall size that can be uploaded/scanned (&#8211;max-size[=N])</p>
<dt>-EN</p>
<dd> maximum mirror time in seconds (60=1 minute, 3600=1 hour) (&#8211;max-time[=N])</p>
<dt>-AN</p>
<dd> maximum transfer rate in bytes/seconds (1000=1KB/s max) (&#8211;max-rate[=N])</p>
<dt>-%cN</p>
<dd> maximum number of connections/seconds (*%c10) (&#8211;connection-per-second[=N])</p>
<dt>-GN</p>
<dd> pause transfer if N bytes reached, and wait until lock file is deleted (&#8211;max-pause[=N]) </p>
</dl>
<h3>Flow control:</h3>
<dl>
<dt>-cN</p>
<dd> number of multiple connections (*c8) (&#8211;sockets[=N])</p>
<dt>-TN</p>
<dd> timeout, number of seconds after a non-responding link is shutdown (&#8211;timeout[=N])</p>
<dt>-RN</p>
<dd> number of retries, in case of timeout or non-fatal errors (*R1) (&#8211;retries[=N])</p>
<dt>-JN</p>
<dd> traffic jam control, minimum transfert rate (bytes/seconds) tolerated for a link (&#8211;min-rate[=N])</p>
<dt>-HN</p>
<dd> host is abandonned if: 0=never, 1=timeout, 2=slow, 3=timeout or slow (&#8211;host-control[=N]) </p>
</dl>
<h3>Links options:</h3>
<dl>
<dt>-%P</p>
<dd> *extended parsing, attempt to parse all links, even in unknown tags or Javascript (%P0 don t use) (&#8211;extended-parsing[=N])</p>
<dt>-n</p>
<dd> get non-html files near an html file (ex: an image located outside) (&#8211;near)</p>
<dt>-t</p>
<dd> test all URLs (even forbidden ones) (&#8211;test)</p>
<dt>-%L</p>
<dd> &lt;file&gt; add all URL located in this text file (one URL per line) (&#8211;list &lt;param&gt;)</p>
<dt>-%S</p>
<dd> &lt;file&gt; add all scan rules located in this text file (one scan rule per line) (&#8211;urllist &lt;param&gt;) </p>
</dl>
<h3>Build options:</h3>
<dl>
<dt>-NN</p>
<dd> structure type (0 *original structure, 1+: see below) (&#8211;structure[=N])</p>
<dt>-or</p>
<dd> user defined structure (-N &quot;%h%p/%n%q.%t&quot;)</p>
<dt>-%N</p>
<dd> delayed type check, don t make any link test but wait for files download to start instead (experimental) (%N0 don t use, %N1 use for unknown extensions, * %N2 always use)</p>
<dt>-%D</p>
<dd> cached delayed type check, don t wait for remote type during updates, to speedup them (%D0 wait, * %D1 don t wait) (&#8211;cached-delayed-type-check)</p>
<dt>-%M</p>
<dd> generate a RFC MIME-encapsulated full-archive (.mht) (&#8211;mime-html)</p>
<dt>-LN</p>
<dd> long names (L1 *long names / L0 8-3 conversion / L2 ISO9660 compatible) (&#8211;long-names[=N])</p>
<dt>-KN</p>
<dd> keep original links (e.g. <a rel="nofollow" href="http://www.adr/link)">http://www.adr/link)</a> (K0 *relative link, K absolute links, K4 original links, K3 absolute URI links, K5 transparent proxy link) (&#8211;keep-links[=N])</p>
<dt>-x</p>
<dd> replace external html links by error pages (&#8211;replace-external)</p>
<dt>-%x</p>
<dd> do not include any password for external password protected websites (%x0 include) (&#8211;disable-passwords)</p>
<dt>-%q</p>
<dd> *include query string for local files (useless, for information purpose only) (%q0 don t include) (&#8211;include-query-string)</p>
<dt>-o</p>
<dd> *generate output html file in case of error (404..) (o0 don t generate) (&#8211;generate-errors)</p>
<dt>-X</p>
<dd> *purge old files after update (X0 keep delete) (&#8211;purge-old[=N])</p>
<dt>-%p</p>
<dd> preserve html files as is (identical to -K4 -%F &quot;&quot; ) (&#8211;preserve)</p>
<dt>-%T</p>
<dd> links conversion to UTF-8 (&#8211;utf8-conversion) </p>
</dl>
<h3>Spider options:</h3>
<dl>
<dt>-bN</p>
<dd> accept cookies in cookies.txt (0=do not accept,* 1=accept) (&#8211;cookies[=N])</p>
<dt>-u</p>
<dd> check document type if unknown (cgi,asp..) (u0 don t check, * u1 check but /, u2 check always) (&#8211;check-type[=N])</p>
<dt>-j</p>
<dd> *parse Java Classes (j0 don t parse, bitmask: |1 parse default, |2 don t parse .class |4 don t parse .js |8 don t be aggressive) (&#8211;parse-java[=N])</p>
<dt>-sN</p>
<dd> follow robots.txt and meta robots tags (0=never,1=sometimes,* 2=always, 3=always (even strict rules)) (&#8211;robots[=N])</p>
<dt>-%h</p>
<dd> force HTTP/1.0 requests (reduce update features, only for old servers or proxies) (&#8211;http-10)</p>
<dt>-%k</p>
<dd> use keep-alive if possible, greately reducing latency for small files and test requests (%k0 don t use) (&#8211;keep-alive)</p>
<dt>-%B</p>
<dd> tolerant requests (accept bogus responses on some servers, but not standard!) (&#8211;tolerant)</p>
<dt>-%s</p>
<dd> update hacks: various hacks to limit re-transfers when updating (identical size, bogus response..) (&#8211;updatehack)</p>
<dt>-%u</p>
<dd> url hacks: various hacks to limit duplicate URLs (strip //, <a rel="nofollow" href="http://www.foo.com">www.foo.com</a>==foo.com..) (&#8211;urlhack)</p>
<dt>-%A</p>
<dd> assume that a type (cgi,asp..) is always linked with a mime type (-%A php3,cgi=text/html;dat,bin=application/x-zip) (&#8211;assume &lt;param&gt;)</p>
<dt>-can</p>
<dd> also be used to force a specific file type: &#8211;assume foo.cgi=text/html</p>
<dt>-@iN</p>
<dd> internet protocol (0=both ipv6+ipv4, 4=ipv4 only, 6=ipv6 only) (&#8211;protocol[=N])</p>
<dt>-%w</p>
<dd> disable a specific external mime module (-%w htsswf -%w htsjava) (&#8211;disable-module &lt;param&gt;) </p>
</dl>
<h3>Browser ID:</h3>
<dl>
<dt>-F</p>
<dd> user-agent field sent in HTTP headers (-F &quot;user-agent name&quot;) (&#8211;user-agent &lt;param&gt;)</p>
<dt>-%R</p>
<dd> default referer field sent in HTTP headers (&#8211;referer &lt;param&gt;)</p>
<dt>-%E</p>
<dd> from email address sent in HTTP headers (&#8211;from &lt;param&gt;)</p>
<dt>-%F</p>
<dd> footer string in Html code (-%F &quot;Mirrored [from host %s [file %s [at %s]]]&quot; (&#8211;footer &lt;param&gt;)</p>
<dt>-%l</p>
<dd> preffered language (-%l &quot;fr, en, jp, *&quot; (&#8211;language &lt;param&gt;)</p>
<dt>-%a</p>
<dd> accepted formats (-%a &quot;text/html,image/png;q=0.9,*/*;q=0.1&quot; (&#8211;accept &lt;param&gt;)</p>
<dt>-%X</p>
<dd> additional HTTP header line (-%X &quot;X-Magic: 42&quot; (&#8211;headers &lt;param&gt;) </p>
</dl>
<h3>Log, index, cache</h3>
<dl>
<dt>-C</p>
<dd> create/use a cache for updates and retries (C0 no cache,C1 cache is prioritary,* C2 test update before) (&#8211;cache[=N])</p>
<dt>-k</p>
<dd> store all files in cache (not useful if files on disk) (&#8211;store-all-in-cache)</p>
<dt>-%n</p>
<dd> do not re-download locally erased files (&#8211;do-not-recatch)</p>
<dt>-%v</p>
<dd> display on screen filenames downloaded (in realtime) &#8211; * %v1 short version &#8211; %v2 full animation (&#8211;display)</p>
<dt>-Q</p>
<dd> no log &#8211; quiet mode (&#8211;do-not-log)</p>
<dt>-q</p>
<dd> no questions &#8211; quiet mode (&#8211;quiet)</p>
<dt>-z</p>
<dd> log &#8211; extra infos (&#8211;extra-log)</p>
<dt>-Z</p>
<dd> log &#8211; debug (&#8211;debug-log)</p>
<dt>-v</p>
<dd> log on screen (&#8211;verbose)</p>
<dt>-f</p>
<dd> *log in files (&#8211;file-log)</p>
<dt>-f2</p>
<dd> one single log file (&#8211;single-log)</p>
<dt>-I</p>
<dd> *make an index (I0 don t make) (&#8211;index)</p>
<dt>-%i</p>
<dd> make a top index for a project folder (* %i0 don t make) (&#8211;build-top-index)</p>
<dt>-%I</p>
<dd> make an searchable index for this mirror (* %I0 don t make) (&#8211;search-index) </p>
</dl>
<h3>Expert options:</h3>
<dl>
<dt>-pN</p>
<dd> priority mode: (* p3) (&#8211;priority[=N])</p>
<dt>-p0</p>
<dd> just scan, don t save anything (for checking links)</p>
<dt>-p1</p>
<dd> save only html files</p>
<dt>-p2</p>
<dd> save only non html files</p>
<dt>-*p3</p>
<dd> save all files</p>
<dt>-p7</p>
<dd> get html files before, then treat other files</p>
<dt>-S</p>
<dd> stay on the same directory (&#8211;stay-on-same-dir)</p>
<dt>-D</p>
<dd> *can only go down into subdirs (&#8211;can-go-down)</p>
<dt>-U</p>
<dd> can only go to upper directories (&#8211;can-go-up)</p>
<dt>-B</p>
<dd> can both go up&amp;down into the directory structure (&#8211;can-go-up-and-down)</p>
<dt>-a</p>
<dd> *stay on the same address (&#8211;stay-on-same-address)</p>
<dt>-d</p>
<dd> stay on the same principal domain (&#8211;stay-on-same-domain)</p>
<dt>-l</p>
<dd> stay on the same TLD (eg: .com) (&#8211;stay-on-same-tld)</p>
<dt>-e</p>
<dd> go everywhere on the web (&#8211;go-everywhere)</p>
<dt>-%H</p>
<dd> debug HTTP headers in logfile (&#8211;debug-headers) </p>
</dl>
<h3>Guru options: (do NOT use if possible)</h3>
<dl>
<dt>-#X</p>
<dd> *use optimized engine (limited memory boundary checks) (&#8211;fast-engine)</p>
<dt>-#0</p>
<dd> filter test (-#0 *.gif <a rel="nofollow" href="http://www.bar.com">www.bar.com</a>/foo.gif ) (&#8211;debug-testfilters &lt;param&gt;)</p>
<dt>-#1</p>
<dd> simplify test (-#1 ./foo/bar/../foobar)</p>
<dt>-#2</p>
<dd> type test (-#2 /foo/bar.php)</p>
<dt>-#C</p>
<dd> cache list (-#C *.com/spider*.gif (&#8211;debug-cache &lt;param&gt;)</p>
<dt>-#R</p>
<dd> cache repair (damaged cache) (&#8211;repair-cache)</p>
<dt>-#d</p>
<dd> debug parser (&#8211;debug-parsing)</p>
<dt>-#E</p>
<dd> extract new.zip cache meta-data in meta.zip</p>
<dt>-#f</p>
<dd> always flush log files (&#8211;advanced-flushlogs)</p>
<dt>-#FN</p>
<dd> maximum number of filters (&#8211;advanced-maxfilters[=N])</p>
<dt>-#h</p>
<dd> version info (&#8211;version)</p>
<dt>-#K</p>
<dd> scan stdin (debug) (&#8211;debug-scanstdin)</p>
<dt>-#L</p>
<dd> maximum number of links (-#L1000000) (&#8211;advanced-maxlinks)</p>
<dt>-#p</p>
<dd> display ugly progress information (&#8211;advanced-progressinfo)</p>
<dt>-#P</p>
<dd> catch URL (&#8211;catch-url)</p>
<dt>-#R</p>
<dd> old FTP routines (debug) (&#8211;repair-cache)</p>
<dt>-#T</p>
<dd> generate transfer ops. log every minutes (&#8211;debug-xfrstats)</p>
<dt>-#u</p>
<dd> wait time (&#8211;advanced-wait)</p>
<dt>-#Z</p>
<dd> generate transfer rate statictics every minutes (&#8211;debug-ratestats) </p>
</dl>
<h3>Dangerous options: (do NOT use unless you exactly know what you are doing)</h3>
<dl>
<dt>-%!</p>
<dd> bypass built-in security limits aimed to avoid bandwidth abuses (bandwidth, simultaneous connections) (&#8211;disable-security-limits)</p>
<dt>-IMPORTANT</p>
<dd> NOTE: DANGEROUS OPTION, ONLY SUITABLE FOR EXPERTS</p>
<dt>-USE</p>
<dd> IT WITH EXTREME CARE </p>
</dl>
<h3>Command-line specific options:</h3>
<dl>
<dt>-V</p>
<dd> execute system command after each files ($0 is the filename: -V &quot;rm \$0&quot;) (&#8211;userdef-cmd &lt;param&gt;)</p>
<dt>-%W</p>
<dd> use an external library function as a wrapper (-%W myfoo.so[,myparameters]) (&#8211;callback &lt;param&gt;) </p>
</dl>
<h3>Details: Option N</h3>
<dl>
<dt>-N0</p>
<dd> Site-structure (default)</p>
<dt>-N1</p>
<dd> HTML in web/, images/other files in web/images/</p>
<dt>-N2</p>
<dd> HTML in web/HTML, images/other in web/images</p>
<dt>-N3</p>
<dd> HTML in web/, images/other in web/</p>
<dt>-N4</p>
<dd> HTML in web/, images/other in web/xxx, where xxx is the file extension (all gif will be placed onto web/gif, for example)</p>
<dt>-N5</p>
<dd> Images/other in web/xxx and HTML in web/HTML</p>
<dt>-N99</p>
<dd> All files in web/, with random names (gadget !)</p>
<dt>-N100</p>
<dd> Site-structure, without <a rel="nofollow" href="http://www.domain.xxx">www.domain.xxx</a>/</p>
<dt>-N101</p>
<dd> Identical to N1 exept that &quot;web&quot; is replaced by the site s name</p>
<dt>-N102</p>
<dd> Identical to N2 exept that &quot;web&quot; is replaced by the site s name</p>
<dt>-N103</p>
<dd> Identical to N3 exept that &quot;web&quot; is replaced by the site s name</p>
<dt>-N104</p>
<dd> Identical to N4 exept that &quot;web&quot; is replaced by the site s name</p>
<dt>-N105</p>
<dd> Identical to N5 exept that &quot;web&quot; is replaced by the site s name</p>
<dt>-N199</p>
<dd> Identical to N99 exept that &quot;web&quot; is replaced by the site s name</p>
<dt>-N1001</p>
<dd> Identical to N1 exept that there is no &quot;web&quot; directory</p>
<dt>-N1002</p>
<dd> Identical to N2 exept that there is no &quot;web&quot; directory</p>
<dt>-N1003</p>
<dd> Identical to N3 exept that there is no &quot;web&quot; directory (option set for g option)</p>
<dt>-N1004</p>
<dd> Identical to N4 exept that there is no &quot;web&quot; directory</p>
<dt>-N1005</p>
<dd> Identical to N5 exept that there is no &quot;web&quot; directory</p>
<dt>-N1099</p>
<dd> Identical to N99 exept that there is no &quot;web&quot; directory</dl>
<h3>Details: User-defined option N</h3>
<p>%n&nbsp;<wbr>&nbsp;<wbr>Name of file without file type&nbsp;<wbr>(ex: image)<br />
%N&nbsp;<wbr>&nbsp;<wbr>Name of file, including file type&nbsp;<wbr>(ex: image.gif)<br />
%t&nbsp;<wbr>&nbsp;<wbr>File type&nbsp;<wbr>(ex: gif)<br />
%p&nbsp;<wbr>&nbsp;<wbr>Path&nbsp;<wbr>[without ending&nbsp;<wbr>/]&nbsp;<wbr>(ex:&nbsp;<wbr>/someimages)<br />
%h&nbsp;<wbr>&nbsp;<wbr>Host name&nbsp;<wbr>(ex:&nbsp;<wbr><a rel="nofollow" href="http://www.someweb.com">www.someweb.com</a>)<br />
%M&nbsp;<wbr>&nbsp;<wbr>URL MD5&nbsp;<wbr>(128 bits, 32 ascii bytes)<br />
%Q&nbsp;<wbr>&nbsp;<wbr>query string MD5&nbsp;<wbr>(128 bits, 32 ascii bytes)<br />
%k&nbsp;<wbr>&nbsp;<wbr>full query string<br />
%r&nbsp;<wbr>&nbsp;<wbr>protocol name&nbsp;<wbr>(ex: http)<br />
%q&nbsp;<wbr>&nbsp;<wbr>small query string MD5&nbsp;<wbr>(16 bits, 4 ascii bytes)<br />
%s?&nbsp;<wbr>&nbsp;<wbr>Short name version&nbsp;<wbr>(ex:&nbsp;<wbr>%sN)<br />
%[param]&nbsp;<wbr>&nbsp;<wbr>param variable in query string<br />
%[param:before:after:empty:notfound]&nbsp;<wbr>&nbsp;<wbr>advanced variable extraction</p>
<h3>Details: User-defined option N and advanced variable extraction</h3>
<p>%[param:before:after:empty:notfound]</p>
<dl>
<dt>-param</p>
<dd> : parameter name</p>
<dt>-before</p>
<dd> : string to prepend if the parameter was found</p>
<dt>-after</p>
<dd> : string to append if the parameter was found</p>
<dt>-notfound</p>
<dd> : string replacement if the parameter could not be found</p>
<dt>-empty</p>
<dd> : string replacement if the parameter was empty</p>
<dt>-all</p>
<dd> fields, except the first one (the parameter name), can be empty </p>
</dl>
<h3>Details: Option K</h3>
<dl>
<dt>-K0</p>
<dd> foo.cgi?q=45 -&gt; foo4B54.html?q=45 (relative URI, default)</p>
<dt>-K</p>
<dd> -&gt; <a rel="nofollow" href="http://www.foobar.com/folder/foo.cgi?q=45">http://www.foobar.com/folder/foo.cgi?q=45</a> (absolute URL) (&#8211;keep-links[=N])</p>
<dt>-K3</p>
<dd> -&gt; /folder/foo.cgi?q=45 (absolute URI)</p>
<dt>-K4</p>
<dd> -&gt; foo.cgi?q=45 (original URL)</p>
<dt>-K5</p>
<dd> -&gt; <a rel="nofollow" href="http://www.foobar.com/folder/foo4B54.html?q=45">http://www.foobar.com/folder/foo4B54.html?q=45</a> (transparent proxy URL) </p>
</dl>
<h3>Shortcuts:</h3>
<dl>
<dt>&#8211;mirror</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&lt;URLs&gt;&nbsp;<wbr>*make a mirror of site(s)&nbsp;<wbr>(default)</p>
<dt>&#8211;get</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&lt;URLs&gt;&nbsp;<wbr>&nbsp;<wbr>get the files indicated, do not seek other URLs&nbsp;<wbr>(-qg)</p>
<dt>&#8211;list</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&lt;text file&gt;&nbsp;<wbr>&nbsp;<wbr>add all URL located in this text file&nbsp;<wbr>(-%L)</p>
<dt>&#8211;mirrorlinks</p>
<dd> &lt;URLs&gt; mirror all links in 1st level pages (-Y)</p>
<dt>&#8211;testlinks</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&lt;URLs&gt;&nbsp;<wbr>&nbsp;<wbr>test links in pages&nbsp;<wbr>(-r1p0C0I0t)</p>
<dt>&#8211;spider</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&lt;URLs&gt;&nbsp;<wbr>&nbsp;<wbr>spider site(s), to test links: reports Errors&nbsp;<wbr>&amp;&nbsp;<wbr>Warnings&nbsp;<wbr>(-p0C0I0t)</p>
<dt>&#8211;testsite</p>
<dd>
&lt;URLs&gt;&nbsp;<wbr>&nbsp;<wbr>identical to &#8211;spider</p>
<dt>&#8211;skeleton</p>
<dd>
&lt;URLs&gt;&nbsp;<wbr>&nbsp;<wbr>make a mirror, but gets only html files&nbsp;<wbr>(-p1)</p>
<dt>&#8211;update</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>update a mirror, without confirmation&nbsp;<wbr>(-iC2)</p>
<dt>&#8211;continue</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>continue a mirror, without confirmation&nbsp;<wbr>(-iC1) </p>
<dt>&#8211;catchurl</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>create a temporary proxy to capture an URL or a form post URL</p>
<dt>&#8211;clean</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>erase cache&nbsp;<wbr>&amp;&nbsp;<wbr>log files </p>
<dt>&#8211;http10</p>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>force http/1.0 requests&nbsp;<wbr>(-%h) </p>
</dl>
<h3>Details: Option %W: External callbacks prototypes</h3>
<h3>see htsdefines.h</h3>
<h2>FILES</h2>
<p> <i>/etc/httrack.conf</i></p>
<dl>
<dt>
<dd> The system wide configuration file.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt>HOME</p>
<dd> Is being used if you defined in /etc/httrack.conf the line <i>path ~/websites/# </i></dl>
<h2>DIAGNOSTICS</h2>
<p> Errors/Warnings are reported to <i>hts-log.txt</i> by default, or to stderr if the <i>-v</i> option was specified.</p>
<h2>LIMITS</h2>
<p> These are the principals limits of HTTrack for that moment. Note that we did not heard about any other utility that would have solved them. </p>
<p> <font SIZE="-1">&#8211; Several scripts generating complex filenames may not find them (ex: img.src=&#8217;image&#8217;+a+Mobj.dst+&#8217;.gif&#8217;)</font> </p>
<p> <font SIZE="-1">&#8211; Some java classes may not find some files on them (class included)</font> </p>
<p> <font SIZE="-1">&#8211; Cgi-bin links may not work properly in some cases (parameters needed). To avoid them: use filters like -*cgi-bin*</font></p>
<h2>BUGS</h2>
<p> Please reports bugs to <code>&lt;bugs [at] httrack.com&gt;.</code> Include a complete, self-contained example that will allow the bug to be reproduced, and say which version of httrack you are using. Do not forget to detail options used, OS version, and any other information you deem necessary.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1998-2016 Xavier Roche and other contributors </p>
<p> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. </p>
<p> You should have received a copy of the GNU General Public License along with this program. If not, see &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/">http://www.gnu.org/licenses/</a>&gt;. </p>
<h2>AVAILABILITY</h2>
<p> The most recent released version of httrack can be found at: <code><a rel="nofollow" href="http://www.httrack.com">http://www.httrack.com</a></code></p>
<h2>AUTHOR</h2>
<p> Xavier Roche &lt;roche [at] httrack.com&gt;</p>
<h2>SEE ALSO</h2>
<p> The <code>HTML </code> documentation (available online at <code><a rel="nofollow" href="http://www.httrack.com/html/">http://www.httrack.com/html/</a></code> ) contains more detailed information. Please also refer to the <code>httrack FAQ</code> (available online at <code><a rel="nofollow" href="http://www.httrack.com/html/faq.html">http://www.httrack.com/html/faq.html</a></code> ) </p>
<h2>Index</h2>
