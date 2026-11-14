---
title: "spice-client(1)"
name: "spice-client"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spice-client/"
---

<h2 class="name">NAME</h2>
 

 Spice-GTK - a client-side library to access remote SPICE displays 

<h2>DESCRIPTION</h2>

 Spice-GTK is a library allowing access to remote displays over the <font SIZE="-1">SPICE</font> protocol. At the moment It's mainly used to access remote virtual machines. 

 The Spice-GTK library provides a set of command line options which can be used to tweak some SPICE-specific option.

<h2>URI</h2>

 The most basic <font SIZE="-1">SPICE URI</font> which can be used is in the form 
&nbsp;<wbr>&nbsp;<wbr><a HREF="spice://hostname.example.com:5900">spice://hostname.example.com:5900</a> 

 This will try to initiate a <font SIZE="-1">SPICE</font> connection to hostname.example.com to port 5900. This connection will be unencrypted. This <font SIZE="-1">URI</font> is equivalent to 
&nbsp;<wbr>&nbsp;<wbr><a HREF="spice://hostname.example.com?port=5900">spice://hostname.example.com?port=5900</a> 

 In order to start a <font SIZE="-1">TLS</font> connection, one would use 
&nbsp;<wbr>&nbsp;<wbr><a HREF="spice://hostname.example.com?tls-port=5900">spice://hostname.example.com?tls-port=5900</a> 

 Other valid <font SIZE="-1">URI</font> parameters are 'username' and 'password'. Be careful that passing a password through a <font SIZE="-1">SPICE URI</font> might cause the password to be visible by any local user through 'ps'. 

 Several parameters can be specified at once if they are separated by &amp; or ; 
&nbsp;<wbr>&nbsp;<wbr><a HREF="spice://hostname.example.com?port=5900;tls-port=5901">spice://hostname.example.com?port=5900;tls-port=5901</a> 

 When using 'tls-port', it's recommended to not specify any non-TLS port. If you give both 'port' and 'tls-port', make sure you use the --spice-secure-channels options to indicate which channels must be secure. Otherwise, Spice-GTK first attempts a connection to the non-TLS port, and then try to use the <font SIZE="-1">TLS</font> port. This means a man-in-the-middle could force the whole <font SIZE="-1">SPICE</font> session to go in clear text regardless of the <font SIZE="-1">TLS</font> settings of the <font SIZE="-1">SPICE</font> server.

<h2>OPTIONS</h2>

 The following options are accepted when running a <font SIZE="-1">SPICE</font> client which makes use of the default Spice-GTK options:
<dl>
<dt>--spice-secure-channels=&lt;main,display,inputs,...,all&gt;
<dd> Force the specified channels to be secured 

 This instructs the <font SIZE="-1">SPICE</font> client that it must use a <font SIZE="-1">TLS</font> connection for these channels. If the server only offers non-TLS connections for these channels, the client will not use these. If the special value ``all'' is used, this indicates that all <font SIZE="-1">SPICE</font> channels must be encrypted. 

 The current <font SIZE="-1">SPICE</font> channels are: main, display, inputs, cursor, playback, record, smartcard, usbredir.
<dt>--spice-disable-effects=&lt;wallpaper,font-smooth,animation,all&gt;
<dd> Disable guest display effects 

 This tells the <font SIZE="-1">SPICE</font> client that it should attempt to disable some guest features in order to lower bandwidth usage. This requires guest support, usually through a <font SIZE="-1">SPICE</font> agent. This is currently only supported on Windows guests. 

 ``wallpaper'' will disable the guest wallpaper, ``font-smooth'' will disable font antialiasing, ``animation'' will try to disable some of the desktop environment animations. ``all'' will attempt to disable everything which can be disabled.
<dt>--spice-color-depth=&lt;16,32&gt;
<dd> Guest display color depth 

 This tells the <font SIZE="-1">SPICE</font> client that it should attempt to force the guest <font SIZE="-1">OS</font> color depth. A lower color depth should lower bandwith usage. This requires guest support, usually through a <font SIZE="-1">SPICE</font> agent. This is currently only supported on Windows guests.
<dt>--spice-ca-file=&lt;file&gt;
<dd> Truststore file for secure connections 

 This option is used to specify a .crt file containing the <font SIZE="-1">CA</font> certificate with which the <font SIZE="-1">SPICE</font> server <font SIZE="-1">TLS</font> certificates are signed. This is useful when using self-signed <font SIZE="-1">TLS</font> certificates rather than certificates signed by an official <font SIZE="-1">CA.</font>
<dt>--spice-host-subject=&lt;host-subject&gt;
<dd> Subject of the host certificate (field=value pairs separated by commas) 

 When using self-signed certificates, or when the guest is migrated between different hosts, the subject/altSubject of the <font SIZE="-1">TLS</font> certificate the <font SIZE="-1">SPICE</font> server will provide will not necessarily match the hostname we are connecting to. This option makes it possible to override the expected subject of the <font SIZE="-1">TLS</font> certificate. 

 The subject must correspond to the ``Subject:'' line returned by: 
&nbsp;<wbr>&nbsp;<wbr>openssl x509 -noout -text -in server-cert.pem
<dt>--spice-debug
<dd> Enable Spice-GTK debugging. This can also be toggled on with the <font SIZE="-1">SPICE_DEBUG</font> environment variable, or using G_MESSAGES_DEBUG=all
<dt>--spice-disable-audio
<dd> Disable audio support
<dt>--spice-disable-usbredir
<dd> Disable <font SIZE="-1">USB</font> redirection support
<dt>--spice-usbredir-auto-redirect-filter=&lt;filter-string&gt;
<dd> Filter selecting <font SIZE="-1">USB</font> devices to be auto-redirected when plugged in 

 This filter specifies which <font SIZE="-1">USB</font> devices should be automatically redirected when they are plugged in during the lifetime of a <font SIZE="-1">SPICE</font> session. 

 A rule has the form of: <tt>&quot;class,vendor,product,version,allow&quot;</tt> 

 -1 can be used instead of class, vendor, product or version in order to accept any value. Several rules can be concatenated with '|': <tt>&quot;rule1|rule2|rule3&quot;</tt>
<dt>--spice-usbredir-redirect-on-connect=&lt;filter-string&gt;
<dd> Filter selecting <font SIZE="-1">USB</font> devices to redirect on connect 

 This filter specifies which <font SIZE="-1">USB</font> devices should be automatically redirected when a <font SIZE="-1">SPICE</font> connection to a remote display has been established.
<dt>--spice-gtk-version
<dd> Display Spice-GTK version information
<dt>--spice-smartcard
<dd> Enable smartcard support
<dt>--spice-smartcard-db=&lt;certificate-db&gt;
<dd> Path to the local certificate database to use for software smartcard certificates 

 This option is only useful for testing purpose. Instead of having a hardware smartcard reader, and a physical smartcard, you can specify a file containing 3 certificates which will be used to emulate a smartcard in software. See <tt>&quot;<a rel="nofollow" HREF="http://www.spice-space.org/page/SmartcardUsage#Using_a_software_smartcard">http://www.spice-space.org/page/SmartcardUsage#Using_a_software_smartcard</a>&quot;</tt> for more details about how to generate these certificates.
<dt>--spice-smartcard-certificates=&lt;certificates&gt;
<dd> Certificates to use for software smartcards (field=values separated by commas) 

 This option is only useful for testing purpose. This allows to specify which certificates from the certificate database specified with --spice-smartcard-db should be used for smartcard emulation.
<dt>--spice-cache-size=&lt;bytes&gt;
<dd> Image cache size 

 This option should only be used for testing/debugging.
<dt>--spice-glz-window-size=&lt;bytes&gt;
<dd> Glz compression history size 

 This option should only be used for testing/debugging.</dl>

<h2>BUGS</h2>

 Report bugs to the mailing list <tt>&quot;<a rel="nofollow" HREF="http://lists.freedesktop.org/mailman/listinfo/spice-devel">http://lists.freedesktop.org/mailman/listinfo/spice-devel</a>&quot;</tt>

<h2>COPYRIGHT</h2>

 Copyright (C) 2011, 2014 Red Hat, Inc., and various contributors. This is free software. You may redistribute copies of it under the terms of the <font SIZE="-1">GNU</font> Lesser General Public License <tt>&quot;<a rel="nofollow" HREF="https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html">https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html</a>&quot;</tt>. There is <font SIZE="-1">NO WARRANTY,</font> to the extent permitted by law.

<h2>SEE ALSO</h2>

 <tt>&quot;<a HREF="/docs/linux/man/1-virt-viewer/">virt-viewer</a>(1)&quot;</tt>, the project website <tt>&quot;<a rel="nofollow" HREF="http://spice-space.org">http://spice-space.org</a>&quot;</tt> 

<h2>Index</h2>


