---
title: "echoscu(1)"
name: "echoscu"
section: "1"
letter: "e"
url: "/docs/linux/man/1-echoscu/"
description: "echoscu – DICOM verification (C-ECHO) SCU"
---

<h2 class="name">NAME</h2>
<p> echoscu &#8211; DICOM verification (C-ECHO) SCU </p>
<h2>SYNOPSIS</h2>
<pre>
echoscu [options] peer port
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>echoscu</code> application implements a Service Class User (SCU) for the Verification SOP Class. It sends a DICOM C-ECHO message to a Service Class Provider (SCP) and waits for a response. The application can be used to verify basic DICOM connectivity.</p>
<h2>PARAMETERS</h2>
<pre>
peer  hostname of DICOM peer
port  tcp/ip port number of peer
</pre>
<h2>OPTIONS</h2>
<h3>general options</h3>
<pre><code>
- h-- help
        print this help text and exit-- version
            print version information and exit-- arguments
                print expanded command line arguments -
    q-- quiet
        quiet mode,
    print no warnings and errors - v-- verbose
                                       verbose mode,
    print processing details - d-- debug
                                   debug mode,
    print debug information - ll-- log - level[l] evel:string
                                                       constant(fatal, error, warn, info, debug, trace)
          use level l for the logger
  -lc   --log-config  [f]ilename: string
          use config file f for the logger
</code></pre>
<h3>network options</h3>
<p>application entity titles:<br />
  -aet  &#8211;aetitle  [a]etitle: string<br />
          set my calling AE title (default: ECHOSCU)<br />
  -aec  &#8211;call  [a]etitle: string<br />
          set called AE title of peer (default: ANY-SCP)<br />
association negotiation debugging:<br />
  -pts  &#8211;propose-ts  [n]umber: integer (1..28)<br />
          propose n transfer syntaxes<br />
  -ppc  &#8211;propose-pc  [n]umber: integer (1..128)<br />
          propose n presentation contexts<br />
other network options:<br />
  -to   &#8211;timeout  [s]econds: integer (default: unlimited)<br />
          timeout for connection requests<br />
  -ta   &#8211;acse-timeout  [s]econds: integer (default: 30)<br />
          timeout for ACSE messages<br />
  -td   &#8211;dimse-timeout  [s]econds: integer (default: unlimited)<br />
          timeout for DIMSE messages<br />
  -pdu  &#8211;max-pdu  [n]umber of bytes: integer (4096..131072)<br />
          set max receive pdu to n bytes (default: 16384)<br />
        &#8211;repeat  [n]umber: integer<br />
          repeat n times<br />
        &#8211;abort<br />
          abort association instead of releasing it</p>
<h3>transport layer security (TLS) options</h3>
<pre><code>
transport protocol stack:
  -tls  --disable-tls
          use normal TCP/IP connection (default)
  +tls  --enable-tls  [p]rivate key file, [c]ertificate file: string
          use authenticated secure TLS connection
  +tla  --anonymous-tls
          use secure TLS connection without certificate
private key password (only with --enable-tls):
  +ps   --std-passwd
          prompt user to type password on stdin (default)
  +pw   --use-passwd  [p]assword: string
          use specified password
  -pw   --null-passwd
          use empty string as password
key and certificate file format:
  -pem  --pem-keys
          read keys and certificates as PEM file (default)
  -der  --der-keys
          read keys and certificates as DER file
certification authority:
  +cf   --add-cert-file  [c]ertificate filename: string
          add certificate file to list of certificates
  +cd   --add-cert-dir  [c]ertificate directory: string
          add certificates in d to list of certificates
ciphersuite:
  +cs   --cipher  [c]iphersuite name: string
          add ciphersuite to list of negotiated suites
  +dp   --dhparam  [f]ilename: string
          read DH parameters for DH/DSS ciphersuites
pseudo random generator:
  +rs   --seed  [f]ilename: string
          seed random generator with contents of f
  +ws   --write-seed
          write back modified seed (only with --seed)
  +wf   --write-seed-file  [f]ilename: string (only with --seed)
          write modified seed to file f
peer authentication:
  -rc   --require-peer-cert
          verify peer certificate, fail if absent (default)
  -vc   --verify-peer-cert
          verify peer certificate if present
  -ic   --ignore-peer-cert
          don't verify peer certificate
</code></pre>
<h2>NOTES</h2>
<h3>DICOM Conformance</h3>
<p> The <code>echoscu</code> application supports the following SOP Classes as an SCU: </p>
<pre>
VerificationSOPClass                1.2.840.10008.1.1
</pre>
<p> Unless the <i>&#8211;propose-ts</i> option is used, the echoscu application will only propose the transfer syntax </p>
<pre>
LittleEndianImplicitTransferSyntax  1.2.840.10008.1.2
</pre>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>echoscu</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1994-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
