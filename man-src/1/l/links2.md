---

title: "links2(1)"
name: "links2"
section: "1"
letter: "l"
url: "/docs/linux/man/1-links2/"
description: "links – lynx-like alternative character mode WWW browser"
---

<h2>NAME</h2>
<p> links &#8211; lynx-like alternative character mode WWW browser</p>
<p> <code>links</code> <i>[options] URL</i></p>
<p> <code>links</code> is a text mode WWW browser with ncurses interface, supporting colors, correct table rendering, background downloading, menu driven configuration interface and slim code. </p>
<p> Frames are supported. You can have different file formats associated with external viewers. mailto: and telnet: are supported via external clients. </p>
<p> <i>links</i> can handle local (file://) or remote (http:// or <a href="ftp://)">ftp://)</a> URLs. </p>
<h2>OPTIONS</h2>
<p> Most options can be set in the user interface or config file, so usually you do not need to care about them. </p>
<dl>
<dt><code>-help</code></dt>
<dd> Print a help screen </dd>
<dt><code>-version</code></dt>
<dd> Prints the <i>links</i> version number and exit. </dd>
<dt><code>-lookup </code><i>&lt;hostname&gt;</i></dt>
<dd> Does name lookup, like command &quot;host&quot;. </dd>
<dt><code>-g</code></dt>
<dd> Run Links in graphics mode. If not given, Links will run in text mode. Running in graphics mode means that Links will probe all compiled-in graphics devices and run on the first found. If none found, links will not run in graphics mode. This option works only if &#8211;enable-graphics was given to ./configure. </dd>
<dt><code>-no-g</code></dt>
<dd> Run in text mode (overrides previous -g). </dd>
<dt><code>-driver </code><i>&lt;driver name&gt;</i></dt>
<dd> Graphics driver to use. Drivers are: x, svgalib, fb, directfb, pmshell, atheos. List of drivers will be shown if you give it an unknown driver. Available drivers depend on your operating system and available libraries. </dd>
<dt><code>-mode </code><i>&lt;parameter&gt;</i></dt>
<dd> Pass a parameter to the graphics driver. On SVGAlib, this is widthxheightxdepth, (where depth is 16, 256, 32K, 64K, 16M or 16M32) and defines the graphics mode, on X the format is WIDTHxHEIGHT and defines the window size. </dd>
<dt><code>-display </code><i>&lt;x-display&gt;</i></dt>
<dd> Set Xwindow display. </dd>
<dt><code>-force-html</code></dt>
<dd> Treat files with unknown type as html rather than text. (can be toggled with &#8216;\&#8217; key) </dd>
<dt><code>-source </code><i>&lt;url&gt;</i></dt>
<dd> Write unformatted data stream to stdout. </dd>
<dt><code>-dump </code><i>&lt;url&gt;</i></dt>
<dd> Write formatted document to stdout. </dd>
<dt><code>-width </code><i>&lt;number&gt;</i></dt>
<dd> For dump, document will be formatted to this screen width (but it can still exceed it if lines can&#8217;t be broken). </dd>
<dt><code>-codepage </code><i>&lt;codepage&gt;</i></dt>
<dd> For dump, convert output to specified character set &#8212; for eaxmple iso-8859-2, windows-1250. </dd>
<dt><code>-anonymous</code></dt>
<dd> Restrict links so that it can run on an anonymous account. No local file browsing. No downloads. Executing of viewers is allowed, but user can&#8217;t add or modify entries in association table. </dd>
<dt><code>-no-connect</code></dt>
<dd> Runs links as a separate instance &#8211; instead of connecting to existing instance. </dd>
<dt><code>-download-dir </code><i>&lt;path&gt;</i></dt>
<dd> Default download directory. (default: actual dir) </dd>
<dt><code>-language </code><i>&lt;language&gt;</i></dt>
<dd> Set user interface language. </dd>
<dt><code>-max-connections </code><i>&lt;max&gt;</i></dt>
<dd> Maximum number of concurrent connections. (default: 10) </dd>
<dt><code>-max-connections-to-host </code><i>&lt;max&gt;</i></dt>
<dd> Maximum number of concurrent connection to a given host. (default: 2) </dd>
<dt><code>-retries </code><i>&lt;retry&gt;</i></dt>
<dd> Number of retries. (default: 3) </dd>
<dt><code>-receive-timeout </code><i>&lt;sec&gt;</i></dt>
<dd> Timeout on receive. (default: 120) </dd>
<dt><code>-unrestartable-receive-timeout </code><i>&lt;sec&gt;</i></dt>
<dd> Timeout on non restartable connections. (default: 600) </dd>
<dt><code>-bind-address </code><i>&lt;ip address&gt;</i></dt>
<dd> Use a specific local IP address. </dd>
<dt><code>-bind-address-ipv6 </code><i>&lt;ipv6 address&gt;</i></dt>
<dd> Use a specific local IPv6 address. </dd>
<dt><code>-no-libevent</code></dt>
<dd> Don&#8217;t use libevent library. </dd>
<dt><code>-no-openmp</code></dt>
<dd> Don&#8217;t use OpenMP. </dd>
<dt><code>-async-dns </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Asynchronous DNS resolver on(1)/off(0). </dd>
<dt><code>-download-utime </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Set time of downloaded files to last modification time reported by server. </dd>
<dt><code>-format-cache-size </code><i>&lt;num&gt;</i></dt>
<dd> Number of formatted document pages cached. (default: 5) </dd>
<dt><code>-memory-cache-size </code><i>&lt;bytes&gt;</i></dt>
<dd> Cache memory in bytes. (default: 1048576) </dd>
<dt><code>-image-cache-size </code><i>&lt;bytes&gt;</i></dt>
<dd> Cache memory in bytes. (default: 1048576) </dd>
<dt><code>-font-cache-size </code><i>&lt;bytes&gt;</i></dt>
<dd> Cache memory in bytes. (default: 2097152) </dd>
<dt><code>-aggressive-cache </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Always cache everything regardless of server&#8217;s caching recomendations. Many servers deny caching even if their content is not changing just to get more hits and more money from ads. </dd>
<dt><code>-address-preference </code><i>&lt;0&gt;/&lt;1&gt;/&lt;2&gt;/&lt;3&gt;/&lt;4&gt;</i></dt>
<dd> (default 0) 0 &#8211; use system default. 1 &#8211; prefer IPv4. 2 &#8211; prefer IPv6. 3 &#8211; use only IPv4. 4 &#8211; use only IPv6. </dd>
<dt><code>-http-proxy </code><i>&lt;host:port&gt;</i></dt>
<dd> Host and port number of the HTTP proxy, or blank. (default: blank) </dd>
<dt><code>-ftp-proxy </code><i>&lt;host:port&gt;</i></dt>
<dd> Host and port number of the FTP proxy, or blank. (default: blank) </dd>
<dt><code>-https-proxy </code><i>&lt;host:port&gt;</i></dt>
<dd> Host and port number of the HTTPS proxy, or blank. (default: blank) </dd>
<dt><code>-socks-proxy </code><i>&lt;user [at] host:port&gt;</i></dt>
<dd> Userid, host and port of Socks4a, or blank. (default: blank) </dd>
<dt><code>-append-text-to-dns-lookups </code><i>&lt;text&gt;</i></dt>
<dd> Append text to dns lookups. It is useful for specifying fixed tor exit node. (default: blank) </dd>
<dt><code>-only-proxies </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> &quot;1&quot; causes that Links won&#8217;t initiate any non-proxy connection. It is useful for anonymization with tor or similar networks. </dd>
<dt><code>-ssl.certificates </code><i>&lt;0&gt;/&lt;1&gt;/&lt;2&gt;</i></dt>
<dd> (default 1) 0 &#8211; ignore invalid certificate. 1 &#8211; warn on invalid certificate. 2 &#8211; reject invalid certificate. </dd>
<dt><code>-ssl.client-cert-key </code><i>&lt;filename&gt;</i></dt>
<dd> Name of the PEM encoded file with the user private key for client certificate authentication. </dd>
<dt><code>-ssl.client-cert-crt </code><i>&lt;filename&gt;</i></dt>
<dd> Name of the PEM encoded file with the user certificate for client certificate authentication. </dd>
<dt><code>-ssl.client-cert-password </code><i>&lt;text&gt;</i></dt>
<dd> Password for the user private key. </dd>
<dt><code>-http-bugs.http10 </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> (default 0) &quot;1&quot; forces using only HTTP/1.0 protocol. (useful for buggy servers that claim to be HTTP/1.1 compliant but are not) &quot;0&quot; enables using both HTTP/1.0 and HTTP/1.1. </dd>
<dt><code>-http-bugs.allow-blacklist </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> (default 1) &quot;1&quot; defaults to using list of servers that have broken HTTP/1.1 support. When links finds such server, it will retry the request with HTTP/1.0. </dd>
<dt><code>-http-bugs.bug-302-redirect </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> (default 1) Process 302 redirect in a way that is incompatible with RFC1945 and RFC2068, but the same as Netscape and MSIE. Many pages depend on it. </dd>
<dt><code>-http-bugs.bug-post-no-keepalive </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> (default 0) No keepalive connection after post requests. For some buggy servers. </dd>
<dt><code>-http-bugs.bug-no-accept-charset </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> (default 0) Do not send Accept-Charset field of HTTP header. Because it is too long some servers will deny the request. Other servers will convert content to plain ascii when Accept-Charset is missing. </dd>
<dt><code>-http-bugs.no-compression </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> (default 0) &quot;1&quot; causes that links won&#8217;t advertise HTTP compression support (but it will still accept compressed data). Use it when you communicate with server that has broken compression support. </dd>
<dt><code>-http-bugs.retry-internal-errors </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> (default 0) Retry on internal server errors (50x). </dd>
<dt><code>-http.fake-firefox </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> (default 0) Fake that the browser is Firefox in the HTTP header. </dd>
<dt><code>-http.do-not-track </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> (default 0) Send &quot;do not track&quot; request in the HTTP header. </dd>
<dt><code>-http.referer </code><i>&lt;0&gt;/&lt;1&gt;/&lt;2&gt;/&lt;3&gt;/&lt;4&gt;</i></dt>
<dd> (default 0) 0 &#8211; do not send referer. 1 &#8211; send the requested URL as referer. 2 &#8211; send fake referer. 3 &#8211; send real referer. 4 &#8211; send real referer only to the same server. </dd>
<dt><code>-http.fake-referer </code><i>&lt;string&gt;</i></dt>
<dd> Fake referer value. </dd>
<dt><code>-http.fake-user-agent </code><i>&lt;string&gt;</i></dt>
<dd> Fake user agent value. </dd>
<dt><code>-http.extra-header </code><i>&lt;string&gt;</i></dt>
<dd> Extra string added to HTTP header. </dd>
<dt><code>&#8211;<a href="ftp://ftp.anonymous-password">ftp.anonymous-password</a> </code><i>&lt;string&gt;</i></dt>
<dd> Password for anonymous ftp access. </dd>
<dt><code>&#8211;<a href="ftp://ftp.use-passive">ftp.use-passive</a> </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Use ftp PASV command to bypass firewalls. </dd>
<dt><code>&#8211;<a href="ftp://ftp.use-erpt-epsv">ftp.use-erpt-epsv</a> </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Use EPRT and EPSV commands instead of PORT and PASV. </dd>
<dt><code>&#8211;<a href="ftp://ftp.fast">ftp.fast</a> </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Send more ftp commands simultaneously. Faster response when browsing ftp directories, but it is incompatible with RFC and some servers don&#8217;t like it. </dd>
<dt><code>&#8211;<a href="ftp://ftp.set-iptos">ftp.set-iptos</a> </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Set IP Type-of-service to high throughput on ftp connections. </dd>
<dt><code>-smb.allow-hyperlinks-to-smb </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Allow hyperlinks to SMB protocol. Disabling this improves security, because internet sites cannot exploit possible bugs in the SMB client. </dd>
<dt><code>-menu-font-size </code><i>&lt;size&gt;</i></dt>
<dd> Size of font in menu. </dd>
<dt><code>-menu-background-color </code><i>0xRRGGBB</i></dt>
<dd> Set menu background color in graphics mode. RRGGBB are hex. </dd>
<dt><code>-menu-foreground-color </code><i>0xRRGGBB</i></dt>
<dd> Set menu foreground color in graphics mode. RRGGBB are hex. </dd>
<dt><code>-scroll-bar-area-color </code><i>0xRRGGBB</i></dt>
<dd> Set color of scroll bar area. RRGGBB are hex. </dd>
<dt><code>-scroll-bar-bar-color </code><i>0xRRGGBB</i></dt>
<dd> Set color of scroll bar. RRGGBB are hex. </dd>
<dt><code>-scroll-bar-frame-color </code><i>0xRRGGBB</i></dt>
<dd> Set color of scroll bar frame. RRGGBB are hex. </dd>
<dt><code>-bookmarks-file </code><i>&lt;file&gt;</i></dt>
<dd> File to store bookmarks. </dd>
<dt><code>-bookmarks-codepage </code><i>&lt;codepage&gt;</i></dt>
<dd> Character set of bookmarks file. </dd>
<dt><code>-save-url-history </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Save URL history on exit. </dd>
<dt><code>-display-red-gamma </code><i>&lt;fp-value&gt;</i></dt>
<dd> Red gamma of display. (default 2.2) </dd>
<dt><code>-display-green-gamma </code><i>&lt;fp-value&gt;</i></dt>
<dd> Green gamma of display. (default 2.2) </dd>
<dt><code>-display-blue-gamma </code><i>&lt;fp-value&gt;</i></dt>
<dd> Blue gamma of display. (default 2.2) </dd>
<dt><code>-user-gamma </code><i>&lt;fp-value&gt;</i></dt>
<dd> Additional gamma. (defult 1) </dd>
<dt><code>-bfu-aspect </code><i>&lt;fp-value&gt;</i></dt>
<dd> Display aspect ration. </dd>
<dt><code>-dither-letters </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Do letter dithering. </dd>
<dt><code>-dither-images </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Do image dithering. </dd>
<dt><code>-display-optimize </code><i>&lt;0&gt;/&lt;1&gt;/&lt;2&gt;</i></dt>
<dd> Optimize for CRT (0), LCD RGB (1), LCD BGR (2). </dd>
<dt><code>-gamma-correction </code><i>&lt;0&gt;/&lt;1&gt;/&lt;2&gt;</i></dt>
<dd> Type of gamma correction: (default 2) 0 &#8211; 8-bit (fast). 1 &#8211; 16-bit (slow). 2 &#8211; automatically detect according to speed of FPU. </dd>
<dt><code>-overwrite-instead-of-scroll </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Overwrite the screen instead of scrolling it (valid for svgalib and framebuffer). Overwriting may or may not be faster, depending on hardware. </dd>
<dt><code>-html-assume-codepage </code><i>&lt;codepage&gt;</i></dt>
<dd> Use the given codepage when the webpage did not specify its codepage. (default: ISO 8859-1) </dd>
<dt><code>-html-hard-assume </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Use always character set from &quot;-html-assume-codepage&quot; no matter what server sent. </dd>
<dt><code>-html-tables </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Render tables. (0) causes tables being rendered like in lynx. </dd>
<dt><code>-html-frames </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Render frames. (0) causes frames rendered like in lynx. </dd>
<dt><code>-html-break-long-lines </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Break long lines in &lt;pre&gt; sections. </dd>
<dt><code>-html-images </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Display links to unnamed images as [IMG] </dd>
<dt><code>-html-image-names </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Display filename of an image instead of [IMG]. </dd>
<dt><code>-html-display-images </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Display images in graphics mode. </dd>
<dt><code>-html-image-scale </code><i>&lt;percent&gt;</i></dt>
<dd> Scale images in graphics mode. </dd>
<dt><code>-html-bare-image-autoscale </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Autoscale images displayed in full screen. </dd>
<dt><code>-html-numbered-links </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Number links in text mode. Allow quick link selection by typing link number and enter. </dd>
<dt><code>-html-table-order </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> In text mode, walk through table by rows (0) or columns (1). </dd>
<dt><code>-html-auto-refresh </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Process refresh to other page (1), or display link to that page (0). </dd>
<dt><code>-html-target-in-new-window </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Allow opening new windows from html. </dd>
<dt><code>-html-margin </code><i>&lt;number of spaces&gt;</i></dt>
<dd> Margin in text mode. </dd>
<dt><code>-html-user-font-size </code><i>&lt;size&gt;</i></dt>
<dd> Size of font on pages in graphics mode. </dd>
<dt><code>-html-t-text-color </code><i>&lt;0&gt;-&lt;15&gt;</i></dt>
<dd> Text color in text mode. </dd>
<dt><code>-html-t-link-color </code><i>&lt;0&gt;-&lt;15&gt;</i></dt>
<dd> Link color in text mode. </dd>
<dt><code>-html-t-background-color </code><i>&lt;0&gt;-&lt;7&gt;</i></dt>
<dd> Background color in text mode. </dd>
<dt><code>-html-t-ignore-document-color </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Ignore colors specified in html document in text mode. </dd>
<dt><code>-html-g-text-color </code><i>0xRRGGBB</i></dt>
<dd> Text color in graphics mode. </dd>
<dt><code>-html-g-link-color </code><i>0xRRGGBB</i></dt>
<dd> Link color in graphics mode. </dd>
<dt><code>-html-g-background-color </code><i>0xRRGGBB</i></dt>
<dd> Background color in graphics mode. </dd>
<dt><code>-html-g-ignore-document-color </code><i>&lt;0&gt;/&lt;1&gt;</i></dt>
<dd> Ignore colors specified in html document in graphics mode. </dd>
</dl>
<p> More options can be seen with links -h </p>
<h2>NAVIGATION KEYS</h2>
<p> The keys you may use while navigating are</p>
<dl>
<dt><code>ESC</code></dt>
<dd> menu/escape</dd>
<dt><code>F9</code></dt>
<dd> menu</dd>
<dt><code>F10</code></dt>
<dd> file menu</dd>
<dt><code>TAB</code></dt>
<dd> next frame</dd>
<dt><code>PGDN</code></dt>
<dd> page down</dd>
<dt><code>Space</code></dt>
<dd> page down</dd>
<dt><code>PGUP</code></dt>
<dd> page up</dd>
<dt><code>b</code></dt>
<dd> page up</dd>
<dt><code>CursorDOWN</code></dt>
<dd> next link/down</dd>
<dt><code>CursorUP</code></dt>
<dd> prev link/up</dd>
<dt><code>INS</code></dt>
<dd> scroll up</dd>
<dt><code>^P</code></dt>
<dd> scroll up</dd>
<dt><code>DEL</code></dt>
<dd> scroll down</dd>
<dt><code>^N</code></dt>
<dd> scroll down</dd>
<dt><code>[</code></dt>
<dd> scroll left</dd>
<dt><code>]</code></dt>
<dd> scroll right</dd>
<dt><code>HOME</code></dt>
<dd> home</dd>
<dt><code>END</code></dt>
<dd> end of page</dd>
<dt><code>CursorRIGHT</code></dt>
<dd> enter link/press button</dd>
<dt><code>ENTER</code></dt>
<dd> enter link/press button</dd>
<dt><code>CursorLEFT</code></dt>
<dd> go back</dd>
<dt><code>d</code></dt>
<dd> download link</dd>
<dt><code>/</code></dt>
<dd> search in the page</dd>
<dt><code>?</code></dt>
<dd> search back in the page</dd>
<dt><code>n</code></dt>
<dd> find next match</dd>
<dt><code>N</code></dt>
<dd> find next match backwards</dd>
<dt><code>f</code></dt>
<dd> zoom actual frame</dd>
<dt><code>^R</code></dt>
<dd> reload page</dd>
<dt><code>g</code></dt>
<dd> go to URL</dd>
<dt><code>G</code></dt>
<dd> edit the current URL and goto the result</dd>
<dt><code>^G</code></dt>
<dd> edit the current link and goto the result</dd>
<dt><code>s</code></dt>
<dd> bookmark manager</dd>
<dt><code>q</code></dt>
<dd> quit, close window if more windows are open</dd>
<dt><code>Q</code></dt>
<dd> quit without asking</dd>
<dt><code>=</code></dt>
<dd> document information</dd>
<dt><code>\</code></dt>
<dd> toggle HTML source/rendered view </dd>
</dl>
<h2>EDITING KEYS</h2>
<p> The following keys can be used while editing a line/jumping to a URL:</p>
<dl>
<dt><code>CursorRIGHT</code></dt>
<dd> move right</dd>
<dt><code>CursorLEFT</code></dt>
<dd> move left</dd>
<dt><code>HOME</code></dt>
<dd> jump at the beginning</dd>
<dt><code>^A</code></dt>
<dd> jump at the beginning</dd>
<dt><code>END</code></dt>
<dd> jump at the end</dd>
<dt><code>^E</code></dt>
<dd> jump at the end</dd>
<dt><code>^X</code></dt>
<dd> cut to clipboard</dd>
<dt><code>^B</code></dt>
<dd> copy to clipboard</dd>
<dt><code>^V</code></dt>
<dd> paste from clipboard</dd>
<dt><code>ENTER</code></dt>
<dd> enter line</dd>
<dt><code>BACKSPACE</code></dt>
<dd> delete back character</dd>
<dt><code>^H</code></dt>
<dd> delete back character</dd>
<dt><code>DEL</code></dt>
<dd> delete character</dd>
<dt><code>^D</code></dt>
<dd> delete character</dd>
<dt><code>^U</code></dt>
<dd> delete from beginning of the line</dd>
<dt><code>^K</code></dt>
<dd> delete to the end of the line or delete line (in textarea)</dd>
<dt><code>^W</code></dt>
<dd> auto complete line </dd>
</dl>
<h2>FILES</h2>
<dl>
<dt>
</dt><dt>~/.links/links.cfg</dt>
<dd>
</dd><dd> Per-user configfile, automatically created by <code>links.</code></dd></dl>
<h2>PLATFORMS</h2>
<p> <code>links</code> is known to work on Linux, FreeBSD, Solaris, IRIX, HPUX, Digital Unix, AIX, OS/2, BeOS and Win32.</p>
<h2>BUGS</h2>
<p> You can&#8217;t upload large files; it takes _lots_ of memory. </p>
<p> Please report any other bugs you find to Mikulas Patocka &lt;mikulas [at] artax.karlin.mff.cuni.cz&gt; </p>
<h2>LICENSE</h2>
<p> <code>links</code> is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<h2>AUTHOR</h2>
<p> <i>links</i> was written by <code>Mikulas Patocka, Karel &#8216;Clock&#8217; Kulhavy, Petr &#8216;Brain&#8217; Kulhavy, and Martin &#8216;PerM&#8217; Pergel.</code> See file <i>AUTHORS</i> for a list of people contributing to this project. </p>
<p> The homepage of links can be found at <code><a rel="nofollow" href="http://atrey.karlin.mff.cuni.cz/~clock/twibright/links">http://atrey.karlin.mff.cuni.cz/~clock/twibright/links</a></code> </p>
<p> This manual page was written by Peter Gervai &lt;grin [at] tolna.net&gt;, using excerpts from a (yet?) unknown <i>links</i> fan for the Debian GNU/Linux system (but may be used by others). Updated by Karel Kulhavy. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lynx/">lynx</a></code>(1), <code><a href="/docs/linux/man/1-w3m/">w3m</a></code>(1) </p>
