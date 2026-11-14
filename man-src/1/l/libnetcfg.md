---
title: "libnetcfg(1)"
name: "libnetcfg"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libnetcfg/"
---

<h2 class="name">NAME</h2>
 

 libnetcfg - configure libnet 

<h2>DESCRIPTION</h2>

 The libnetcfg utility can be used to configure the libnet. Starting from perl 5.8 libnet is part of the standard Perl distribution, but the libnetcfg can be used for any libnet installation.

<h2>USAGE</h2>

 Without arguments libnetcfg displays the current configuration. 

 <pre>
    $ libnetcfg
    # old config ./libnet.cfg
    daytime_hosts        ntp1.none.such
    ftp_int_passive      0
    ftp_testhost         <a HREF="ftp://ftp.funet.fi">ftp.funet.fi</a>
    inet_domain          none.such
    nntp_hosts           nntp.none.such
    ph_hosts             
    pop3_hosts           pop.none.such
    smtp_hosts           smtp.none.such
    snpp_hosts           
    test_exist           1
    test_hosts           1
    time_hosts           ntp.none.such
    # libnetcfg -h for help
    $
</pre> 

 It tells where the old configuration file was found (if found). 

 The <tt>&quot;-h&quot;</tt> option will show a usage message. 

 To change the configuration you will need to use either the <tt>&quot;-c&quot;</tt> or the <tt>&quot;-d&quot;</tt> options. 

 The default name of the old configuration file is by default ``libnet.cfg'', unless otherwise specified using the -i option, <tt>&quot;-i oldfile&quot;</tt>, and it is searched first from the current directory, and then from your module path. 

 The default name of the new configuration file is ``libnet.cfg'', and by default it is written to the current directory, unless otherwise specified using the -o option, <tt>&quot;-o newfile&quot;</tt>.

<h2>SEE ALSO</h2>

 Net::Config, libnetFAQ

<h2>AUTHORS</h2>

 Graham Barr, the original Configure script of libnet. 

 Jarkko Hietaniemi, conversion into libnetcfg for inclusion into Perl 5.8. 

<h2>Index</h2>


