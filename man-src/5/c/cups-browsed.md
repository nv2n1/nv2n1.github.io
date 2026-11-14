---
title: "cups-browsed(5)"
name: "cups-browsed"
section: "5"
letter: "c"
url: "/docs/linux/man/5-cups-browsed/"
description: "cups-browsed.conf – server configuration file for cups-browsed"
---

<p><code>cups-browsed.conf </code>&#8211; server configuration file for cups-browsed</p>
<h2>Description</h2>
<p>The cups-browsed.conf file configures the cups-browsed daemon. It is normally located in the /etc/cups directory. Each line in the file can be a configuration directive, a blank line, or a comment. Comment lines start with the # character.</p>
<h2>Directives</h2>
<p>The BrowseAllow directive specifies a system or network to accept CUPS browse packets from. The default is to accept browse packets from all hosts when BrowseRemoteProtocols uses the CUPS protocol. </p>
<pre> BrowseAllow 192.168.7.20
 BrowseAllow 192.168.7.0/24
 BrowseAllow 192.168.7.0/255.255.255.0</pre>
<p>The BrowsePoll directive polls a server for available printers once every 60 seconds. Multiple BrowsePoll directives can be specified to poll multiple servers. The default port to connect to is 631. BrowsePoll works independently of whether CUPS browsing is activated in BrowseRemoteProtocols. </p>
<pre> BrowsePoll 192.168.7.20
 BrowsePoll 192.168.7.65:631
 BrowsePoll host.example.com:631</pre>
<p>The BrowseLocalProtocols directive specifies the protocols to use when advertising local shared printers on the network. The default is &quot;none&quot;. Control of advertising of local shared printers using dnssd is done in /etc/cups/cupsd.conf. </p>
<pre> BrowseLocalProtocols none
 BrowseLocalProtocols CUPS</pre>
<p>The BrowseRemoteProtocols directive specifies the protocols to use when finding remote shared printers on the network. Multiple protocols can be specified by separating them with spaces. The default is &quot;dnssd cups&quot;. </p>
<pre> BrowseRemoteProtocols none
 BrowseRemoteProtocols CUPS dnssd
 BrowseRemoteProtocols CUPS
 BrowseRemoteProtocols dnssd</pre>
<p>The BrowseProtocols directive specifies the protocols to use when finding remote shared printers on the network and advertising local shared printers. &quot;dnssd&quot; is ignored for BrowseLocalProtocols. Multiple protocols can be specified by separating them with spaces. The default is &quot;none&quot; for BrowseLocalProtocols and &quot;dnssd cups&quot; for BrowseRemoteProtocols. </p>
<pre> BrowseProtocols none
 BrowseProtocols CUPS dnssd
 BrowseProtocols CUPS
 BrowseProtocols dnssd</pre>
<p>The DomainSocket directive specifies the domain socket through which the locally running CUPS daemon is accessed. If not specified the standard domain socket of CUPS is used. Use this if you have specified an alternative domain socket for CUPS via a Listen directive in /etc/cups/cupsd.conf. If cups-browsed is not able to access the local CUPS daemon via a domain socket it accesses it via localhost. </p>
<pre> DomainSocket /var/run/cups/cups.sock</pre>
<p>The CreateIPPPrinterQueues directive specifies whether cups-browsed should discover IPP printers (via Bonjour) and if they understand a known page description language (PWG Raster, PDF, PostScript, PCL XL, PCL 5c/e) create PPD-less print queues (using a System V interface script to control the filter chain). Clients have to IPP-poll the capabilities of the printer and send option settings as standard IPP attributes. We do not poll the capabilities by ourselves to not wake up the printer from power-saving mode when creating the queues. Jobs have to be sent in PDF format. Other formats are not accepted. This functionality is primarily for mobile devices running CUPS to not need a printer setup tool nor a collection of printer drivers and PPDs. </p>
<pre> CreateIPPPrinterQueues Yes</pre>
<p>The AutoShutdown directive specifies whether cups-browsed should automatically terminate when it has no local raw queues set up pointing to any discovered remote printers (auto shutdown mode). Setting it to &quot;On&quot; activates the auto-shutdown mode, setting it to &quot;Off&quot; deactiivates it (the default). The special mode &quot;avahi&quot; turns auto shutdown off while avahi-daemon is running and on when avahi-daemon stops. This allows running cups-browsed on-demand when avahi-daemon is run on-demand. </p>
<pre> AutoShutdown Off
 AutoShutdown On
 AutoShutdown avahi</pre>
<p>The AutoShutdownTimeout directive specifies after how many seconds without local raw queues set up pointing to any discovered remote printers cups-browsed should actually shut down in auto shutdown mode. Default is 30 seconds, 0 means immediate shutdown. </p>
<pre> AutoShutdownTimeout 20</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-cups-browsed/">cups-browsed</a></code>(8) </p>
<p> /usr/share/doc/cups-browsed/README.gz</p>
<h2>Author</h2>
<p>The authors of cups-browsed are listed in /usr/share/doc/cups-browsed/AUTHORS. </p>
<p> This manual page was written for the Debian Project, but it may be used by others.</p>
