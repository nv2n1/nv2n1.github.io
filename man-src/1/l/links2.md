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
<h2>SYNOPSIS</h2>
<p> <code>links</code> <i>[options] URL</i></p>
<h2>DESCRIPTION</h2>
<p> <code>links</code> is a text mode WWW browser with ncurses interface, supporting colors, correct table rendering, background downloading, menu driven configuration interface and slim code. </p>
<p> Frames are supported. You can have different file formats associated with external viewers. mailto: and telnet: are supported via external clients. </p>
<p> <i>links</i> can handle local (file://) or remote (http:// or <a href="ftp://)">ftp://)</a> URLs. </p>
<h2>OPTIONS</h2>
<p> Most options can be set in the user interface or config file, so usually you do not need to care about them. </p>
<dl>
<dt><code>-help</code></p>
<dd> Print a help screen </p>
<dt><code>-version</code></p>
<dd> Prints the <i>links</i> version number and exit. </p>
<dt><code>-lookup </code><i>&lt;hostname&gt;</i></p>
<dd> Does name lookup, like command &quot;host&quot;. </p>
<dt><code>-g</code></p>
<dd> Run Links in graphics mode. If not given, Links will run in text mode. Running in graphics mode means that Links will probe all compiled-in graphics devices and run on the first found. If none found, links will not run in graphics mode. This option works only if &#8211;enable-graphics was given to ./configure. </p>
<dt><code>-no-g</code></p>
<dd> Run in text mode (overrides previous -g). </p>
<dt><code>-driver </code><i>&lt;driver name&gt;</i></p>
<dd> Graphics driver to use. Drivers are: x, svgalib, fb, directfb, pmshell, atheos. List of drivers will be shown if you give it an unknown driver. Available drivers depend on your operating system and available libraries. </p>
<dt><code>-mode </code><i>&lt;parameter&gt;</i></p>
<dd> Pass a parameter to the graphics driver. On SVGAlib, this is widthxheightxdepth, (where depth is 16, 256, 32K, 64K, 16M or 16M32) and defines the graphics mode, on X the format is WIDTHxHEIGHT and defines the window size. </p>
<dt><code>-display </code><i>&lt;x-display&gt;</i></p>
<dd> Set Xwindow display. </p>
<dt><code>-force-html</code></p>
<dd> Treat files with unknown type as html rather than text. (can be toggled with &#8216;\&#8217; key) </p>
<dt><code>-source </code><i>&lt;url&gt;</i></p>
<dd> Write unformatted data stream to stdout. </p>
<dt><code>-dump </code><i>&lt;url&gt;</i></p>
<dd> Write formatted document to stdout. </p>
<dt><code>-width </code><i>&lt;number&gt;</i></p>
<dd> For dump, document will be formatted to this screen width (but it can still exceed it if lines can&#8217;t be broken). </p>
<dt><code>-codepage </code><i>&lt;codepage&gt;</i></p>
<dd> For dump, convert output to specified character set &#8212; for eaxmple iso-8859-2, windows-1250. </p>
<dt><code>-anonymous</code></p>
<dd> Restrict links so that it can run on an anonymous account. No local file browsing. No downloads. Executing of viewers is allowed, but user can&#8217;t add or modify entries in association table. </p>
<dt><code>-no-connect</code></p>
<dd> Runs links as a separate instance &#8211; instead of connecting to existing instance. </p>
<dt><code>-download-dir </code><i>&lt;path&gt;</i></p>
<dd> Default download directory. (default: actual dir) </p>
<dt><code>-language </code><i>&lt;language&gt;</i></p>
<dd> Set user interface language. </p>
<dt><code>-max-connections </code><i>&lt;max&gt;</i></p>
<dd> Maximum number of concurrent connections. (default: 10) </p>
<dt><code>-max-connections-to-host </code><i>&lt;max&gt;</i></p>
<dd> Maximum number of concurrent connection to a given host. (default: 2) </p>
<dt><code>-retries </code><i>&lt;retry&gt;</i></p>
<dd> Number of retries. (default: 3) </p>
<dt><code>-receive-timeout </code><i>&lt;sec&gt;</i></p>
<dd> Timeout on receive. (default: 120) </p>
<dt><code>-unrestartable-receive-timeout </code><i>&lt;sec&gt;</i></p>
<dd> Timeout on non restartable connections. (default: 600) </p>
<dt><code>-bind-address </code><i>&lt;ip address&gt;</i></p>
<dd> Use a specific local IP address. </p>
<dt><code>-bind-address-ipv6 </code><i>&lt;ipv6 address&gt;</i></p>
<dd> Use a specific local IPv6 address. </p>
<dt><code>-no-libevent</code></p>
<dd> Don&#8217;t use libevent library. </p>
<dt><code>-no-openmp</code></p>
<dd> Don&#8217;t use OpenMP. </p>
<dt><code>-async-dns </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Asynchronous DNS resolver <a href="/docs/linux/man/1-on/">on</a>(1)/off(0). </p>
<dt><code>-download-utime </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Set time of downloaded files to last modification time reported by server. </p>
<dt><code>-format-cache-size </code><i>&lt;num&gt;</i></p>
<dd> Number of formatted document pages cached. (default: 5) </p>
<dt><code>-memory-cache-size </code><i>&lt;bytes&gt;</i></p>
<dd> Cache memory in bytes. (default: 1048576) </p>
<dt><code>-image-cache-size </code><i>&lt;bytes&gt;</i></p>
<dd> Cache memory in bytes. (default: 1048576) </p>
<dt><code>-font-cache-size </code><i>&lt;bytes&gt;</i></p>
<dd> Cache memory in bytes. (default: 2097152) </p>
<dt><code>-aggressive-cache </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Always cache everything regardless of server&#8217;s caching recomendations. Many servers deny caching even if their content is not changing just to get more hits and more money from ads. </p>
<dt><code>-address-preference </code><i>&lt;0&gt;/&lt;1&gt;/&lt;2&gt;/&lt;3&gt;/&lt;4&gt;</i></p>
<dd> (default 0) 0 &#8211; use system default. 1 &#8211; prefer IPv4. 2 &#8211; prefer IPv6. 3 &#8211; use only IPv4. 4 &#8211; use only IPv6. </p>
<dt><code>-http-proxy </code><i>&lt;host:port&gt;</i></p>
<dd> Host and port number of the HTTP proxy, or blank. (default: blank) </p>
<dt><code>-ftp-proxy </code><i>&lt;host:port&gt;</i></p>
<dd> Host and port number of the FTP proxy, or blank. (default: blank) </p>
<dt><code>-https-proxy </code><i>&lt;host:port&gt;</i></p>
<dd> Host and port number of the HTTPS proxy, or blank. (default: blank) </p>
<dt><code>-socks-proxy </code><i>&lt;user [at] host:port&gt;</i></p>
<dd> Userid, host and port of Socks4a, or blank. (default: blank) </p>
<dt><code>-append-text-to-dns-lookups </code><i>&lt;text&gt;</i></p>
<dd> Append text to dns lookups. It is useful for specifying fixed tor exit node. (default: blank) </p>
<dt><code>-only-proxies </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> &quot;1&quot; causes that Links won&#8217;t initiate any non-proxy connection. It is useful for anonymization with tor or similar networks. </p>
<dt><code>-ssl.certificates </code><i>&lt;0&gt;/&lt;1&gt;/&lt;2&gt;</i></p>
<dd> (default 1) 0 &#8211; ignore invalid certificate. 1 &#8211; warn on invalid certificate. 2 &#8211; reject invalid certificate. </p>
<dt><code>-ssl.client-cert-key </code><i>&lt;filename&gt;</i></p>
<dd> Name of the PEM encoded file with the user private key for client certificate authentication. </p>
<dt><code>-ssl.client-cert-crt </code><i>&lt;filename&gt;</i></p>
<dd> Name of the PEM encoded file with the user certificate for client certificate authentication. </p>
<dt><code>-ssl.client-cert-password </code><i>&lt;text&gt;</i></p>
<dd> Password for the user private key. </p>
<dt><code>-http-bugs.http10 </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> (default 0) &quot;1&quot; forces using only HTTP/1.0 protocol. (useful for buggy servers that claim to be HTTP/1.1 compliant but are not) &quot;0&quot; enables using both HTTP/1.0 and HTTP/1.1. </p>
<dt><code>-http-bugs.allow-blacklist </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> (default 1) &quot;1&quot; defaults to using list of servers that have broken HTTP/1.1 support. When links finds such server, it will retry the request with HTTP/1.0. </p>
<dt><code>-http-bugs.bug-302-redirect </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> (default 1) Process 302 redirect in a way that is incompatible with RFC1945 and RFC2068, but the same as Netscape and MSIE. Many pages depend on it. </p>
<dt><code>-http-bugs.bug-post-no-keepalive </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> (default 0) No keepalive connection after post requests. For some buggy servers. </p>
<dt><code>-http-bugs.bug-no-accept-charset </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> (default 0) Do not send Accept-Charset field of HTTP header. Because it is too long some servers will deny the request. Other servers will convert content to plain ascii when Accept-Charset is missing. </p>
<dt><code>-http-bugs.no-compression </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> (default 0) &quot;1&quot; causes that links won&#8217;t advertise HTTP compression support (but it will still accept compressed data). Use it when you communicate with server that has broken compression support. </p>
<dt><code>-http-bugs.retry-internal-errors </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> (default 0) Retry on internal server errors (50x). </p>
<dt><code>-http.fake-firefox </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> (default 0) Fake that the browser is Firefox in the HTTP header. </p>
<dt><code>-http.do-not-track </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> (default 0) Send &quot;do not track&quot; request in the HTTP header. </p>
<dt><code>-http.referer </code><i>&lt;0&gt;/&lt;1&gt;/&lt;2&gt;/&lt;3&gt;/&lt;4&gt;</i></p>
<dd> (default 0) 0 &#8211; do not send referer. 1 &#8211; send the requested URL as referer. 2 &#8211; send fake referer. 3 &#8211; send real referer. 4 &#8211; send real referer only to the same server. </p>
<dt><code>-http.fake-referer </code><i>&lt;string&gt;</i></p>
<dd> Fake referer value. </p>
<dt><code>-http.fake-user-agent </code><i>&lt;string&gt;</i></p>
<dd> Fake user agent value. </p>
<dt><code>-http.extra-header </code><i>&lt;string&gt;</i></p>
<dd> Extra string added to HTTP header. </p>
<dt><code>&#8211;<a href="ftp://ftp.anonymous-password">ftp.anonymous-password</a> </code><i>&lt;string&gt;</i></p>
<dd> Password for anonymous ftp access. </p>
<dt><code>&#8211;<a href="ftp://ftp.use-passive">ftp.use-passive</a> </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Use ftp PASV command to bypass firewalls. </p>
<dt><code>&#8211;<a href="ftp://ftp.use-erpt-epsv">ftp.use-erpt-epsv</a> </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Use EPRT and EPSV commands instead of PORT and PASV. </p>
<dt><code>&#8211;<a href="ftp://ftp.fast">ftp.fast</a> </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Send more ftp commands simultaneously. Faster response when browsing ftp directories, but it is incompatible with RFC and some servers don&#8217;t like it. </p>
<dt><code>&#8211;<a href="ftp://ftp.set-iptos">ftp.set-iptos</a> </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Set IP Type-of-service to high throughput on ftp connections. </p>
<dt><code>-smb.allow-hyperlinks-to-smb </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Allow hyperlinks to SMB protocol. Disabling this improves security, because internet sites cannot exploit possible bugs in the SMB client. </p>
<dt><code>-menu-font-size </code><i>&lt;size&gt;</i></p>
<dd> Size of font in menu. </p>
<dt><code>-menu-background-color </code><i>0xRRGGBB</i></p>
<dd> Set menu background color in graphics mode. RRGGBB are hex. </p>
<dt><code>-menu-foreground-color </code><i>0xRRGGBB</i></p>
<dd> Set menu foreground color in graphics mode. RRGGBB are hex. </p>
<dt><code>-scroll-bar-area-color </code><i>0xRRGGBB</i></p>
<dd> Set color of scroll bar area. RRGGBB are hex. </p>
<dt><code>-scroll-bar-bar-color </code><i>0xRRGGBB</i></p>
<dd> Set color of scroll bar. RRGGBB are hex. </p>
<dt><code>-scroll-bar-frame-color </code><i>0xRRGGBB</i></p>
<dd> Set color of scroll bar frame. RRGGBB are hex. </p>
<dt><code>-bookmarks-file </code><i>&lt;file&gt;</i></p>
<dd> File to store bookmarks. </p>
<dt><code>-bookmarks-codepage </code><i>&lt;codepage&gt;</i></p>
<dd> Character set of bookmarks file. </p>
<dt><code>-save-url-history </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Save URL history on exit. </p>
<dt><code>-display-red-gamma </code><i>&lt;fp-value&gt;</i></p>
<dd> Red gamma of display. (default 2.2) </p>
<dt><code>-display-green-gamma </code><i>&lt;fp-value&gt;</i></p>
<dd> Green gamma of display. (default 2.2) </p>
<dt><code>-display-blue-gamma </code><i>&lt;fp-value&gt;</i></p>
<dd> Blue gamma of display. (default 2.2) </p>
<dt><code>-user-gamma </code><i>&lt;fp-value&gt;</i></p>
<dd> Additional gamma. (defult 1) </p>
<dt><code>-bfu-aspect </code><i>&lt;fp-value&gt;</i></p>
<dd> Display aspect ration. </p>
<dt><code>-dither-letters </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Do letter dithering. </p>
<dt><code>-dither-images </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Do image dithering. </p>
<dt><code>-display-optimize </code><i>&lt;0&gt;/&lt;1&gt;/&lt;2&gt;</i></p>
<dd> Optimize for CRT (0), LCD RGB (1), LCD BGR (2). </p>
<dt><code>-gamma-correction </code><i>&lt;0&gt;/&lt;1&gt;/&lt;2&gt;</i></p>
<dd> Type of gamma correction: (default 2) 0 &#8211; 8-bit (fast). 1 &#8211; 16-bit (slow). 2 &#8211; automatically detect according to speed of FPU. </p>
<dt><code>-overwrite-instead-of-scroll </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Overwrite the screen instead of scrolling it (valid for svgalib and framebuffer). Overwriting may or may not be faster, depending on hardware. </p>
<dt><code>-html-assume-codepage </code><i>&lt;codepage&gt;</i></p>
<dd> Use the given codepage when the webpage did not specify its codepage. (default: ISO 8859-1) </p>
<dt><code>-html-hard-assume </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Use always character set from &quot;-html-assume-codepage&quot; no matter what server sent. </p>
<dt><code>-html-tables </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Render tables. (0) causes tables being rendered like in lynx. </p>
<dt><code>-html-frames </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Render frames. (0) causes frames rendered like in lynx. </p>
<dt><code>-html-break-long-lines </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Break long lines in &lt;pre&gt; sections. </p>
<dt><code>-html-images </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Display links to unnamed images as [IMG] </p>
<dt><code>-html-image-names </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Display filename of an image instead of [IMG]. </p>
<dt><code>-html-display-images </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Display images in graphics mode. </p>
<dt><code>-html-image-scale </code><i>&lt;percent&gt;</i></p>
<dd> Scale images in graphics mode. </p>
<dt><code>-html-bare-image-autoscale </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Autoscale images displayed in full screen. </p>
<dt><code>-html-numbered-links </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Number links in text mode. Allow quick link selection by typing link number and enter. </p>
<dt><code>-html-table-order </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> In text mode, walk through table by rows (0) or columns (1). </p>
<dt><code>-html-auto-refresh </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Process refresh to other page (1), or display link to that page (0). </p>
<dt><code>-html-target-in-new-window </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Allow opening new windows from html. </p>
<dt><code>-html-margin </code><i>&lt;number of spaces&gt;</i></p>
<dd> Margin in text mode. </p>
<dt><code>-html-user-font-size </code><i>&lt;size&gt;</i></p>
<dd> Size of font on pages in graphics mode. </p>
<dt><code>-html-t-text-color </code><i>&lt;0&gt;-&lt;15&gt;</i></p>
<dd> Text color in text mode. </p>
<dt><code>-html-t-link-color </code><i>&lt;0&gt;-&lt;15&gt;</i></p>
<dd> Link color in text mode. </p>
<dt><code>-html-t-background-color </code><i>&lt;0&gt;-&lt;7&gt;</i></p>
<dd> Background color in text mode. </p>
<dt><code>-html-t-ignore-document-color </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Ignore colors specified in html document in text mode. </p>
<dt><code>-html-g-text-color </code><i>0xRRGGBB</i></p>
<dd> Text color in graphics mode. </p>
<dt><code>-html-g-link-color </code><i>0xRRGGBB</i></p>
<dd> Link color in graphics mode. </p>
<dt><code>-html-g-background-color </code><i>0xRRGGBB</i></p>
<dd> Background color in graphics mode. </p>
<dt><code>-html-g-ignore-document-color </code><i>&lt;0&gt;/&lt;1&gt;</i></p>
<dd> Ignore colors specified in html document in graphics mode. </p>
</dl>
<p> More options can be seen with links -h </p>
<h2>NAVIGATION KEYS</h2>
<p> The keys you may use while navigating are</p>
<dl>
<dt><code>ESC</code></p>
<dd> menu/escape</p>
<dt><code>F9</code></p>
<dd> menu</p>
<dt><code>F10</code></p>
<dd> file menu</p>
<dt><code>TAB</code></p>
<dd> next frame</p>
<dt><code>PGDN</code></p>
<dd> page down</p>
<dt><code>Space</code></p>
<dd> page down</p>
<dt><code>PGUP</code></p>
<dd> page up</p>
<dt><code>b</code></p>
<dd> page up</p>
<dt><code>CursorDOWN</code></p>
<dd> next link/down</p>
<dt><code>CursorUP</code></p>
<dd> prev link/up</p>
<dt><code>INS</code></p>
<dd> scroll up</p>
<dt><code>^P</code></p>
<dd> scroll up</p>
<dt><code>DEL</code></p>
<dd> scroll down</p>
<dt><code>^N</code></p>
<dd> scroll down</p>
<dt><code>[</code></p>
<dd> scroll left</p>
<dt><code>]</code></p>
<dd> scroll right</p>
<dt><code>HOME</code></p>
<dd> home</p>
<dt><code>END</code></p>
<dd> end of page</p>
<dt><code>CursorRIGHT</code></p>
<dd> enter link/press button</p>
<dt><code>ENTER</code></p>
<dd> enter link/press button</p>
<dt><code>CursorLEFT</code></p>
<dd> go back</p>
<dt><code>d</code></p>
<dd> download link</p>
<dt><code>/</code></p>
<dd> search in the page</p>
<dt><code>?</code></p>
<dd> search back in the page</p>
<dt><code>n</code></p>
<dd> find next match</p>
<dt><code>N</code></p>
<dd> find next match backwards</p>
<dt><code>f</code></p>
<dd> zoom actual frame</p>
<dt><code>^R</code></p>
<dd> reload page</p>
<dt><code>g</code></p>
<dd> go to URL</p>
<dt><code>G</code></p>
<dd> edit the current URL and goto the result</p>
<dt><code>^G</code></p>
<dd> edit the current link and goto the result</p>
<dt><code>s</code></p>
<dd> bookmark manager</p>
<dt><code>q</code></p>
<dd> quit, close window if more windows are open</p>
<dt><code>Q</code></p>
<dd> quit without asking</p>
<dt><code>=</code></p>
<dd> document information</p>
<dt><code>\</code></p>
<dd> toggle HTML source/rendered view </p>
</dl>
<h2>EDITING KEYS</h2>
<p> The following keys can be used while editing a line/jumping to a URL:</p>
<dl>
<dt><code>CursorRIGHT</code></p>
<dd> move right</p>
<dt><code>CursorLEFT</code></p>
<dd> move left</p>
<dt><code>HOME</code></p>
<dd> jump at the beginning</p>
<dt><code>^A</code></p>
<dd> jump at the beginning</p>
<dt><code>END</code></p>
<dd> jump at the end</p>
<dt><code>^E</code></p>
<dd> jump at the end</p>
<dt><code>^X</code></p>
<dd> cut to clipboard</p>
<dt><code>^B</code></p>
<dd> copy to clipboard</p>
<dt><code>^V</code></p>
<dd> paste from clipboard</p>
<dt><code>ENTER</code></p>
<dd> enter line</p>
<dt><code>BACKSPACE</code></p>
<dd> delete back character</p>
<dt><code>^H</code></p>
<dd> delete back character</p>
<dt><code>DEL</code></p>
<dd> delete character</p>
<dt><code>^D</code></p>
<dd> delete character</p>
<dt><code>^U</code></p>
<dd> delete from beginning of the line</p>
<dt><code>^K</code></p>
<dd> delete to the end of the line or delete line (in textarea)</p>
<dt><code>^W</code></p>
<dd> auto complete line </p>
</dl>
<h2>FILES</h2>
<dl>
<dt>
<dt>~/.links/links.cfg</p>
<dd>
<dd> Per-user configfile, automatically created by <code>links.</code></dl>
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
<h2>Index</h2>
