---
title: "dcmsign(1)"
name: "dcmsign"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmsign/"
description: "dcmsign – Sign and Verify DICOM Files"
---

<h2 class="name">NAME</h2>
<p> dcmsign &#8211; Sign and Verify DICOM Files </p>
<h2>SYNOPSIS</h2>
<pre><code>
dcmsign[options] dcmfile - in[dcmfile - out]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmsign</code> utility reads a DICOM file (<i>dcmfile-in</i>), performs a digital signature operation and, if any modification has taken place, writes the DICOM object to an output file (<i>dcmfile-out</i>). </p>
<p> Five digital signature operations are supported: </p>
<dl>
<dt>&bull;</p>
<dd> verification of all signatures in the DICOM file</p>
<dt>&bull;</p>
<dd> creation of a new digital signature located in the main dataset,</p>
<dt>&bull;</p>
<dd> creation of a new digital signature in an item of a sequence embedded within the dataset,</p>
<dt>&bull;</p>
<dd> removal of a single digital signature from the DICOM file, and</p>
<dt>&bull;</p>
<dd> removal of all digital signatures from the DICOM file.</dl>
<h2>PARAMETERS</h2>
<pre>
dcmfile-in   DICOM input filename to be processed
dcmfile-out  DICOM output filename
</pre>
<h2>OPTIONS</h2>
<h3>general options</h3>
<p>&#8211; h&#8211; help<br />
        print this help text and exit&#8211; version<br />
            print version information and exit&#8211; arguments<br />
                print expanded command line arguments &#8211;<br />
    q&#8211; quiet<br />
        quiet mode,<br />
    print no warnings and errors &#8211; v&#8211; verbose<br />
                                       verbose mode,<br />
    print processing details &#8211; d&#8211; debug<br />
                                   debug mode,<br />
    print debug information &#8211; ll&#8211; log &#8211; level[l] evel:string<br />
                                                       constant(fatal, error, warn, info, debug, trace)<br />
          use level l for the logger<br />
  -lc   &#8211;log-config  [f]ilename: string<br />
          use config file f for the logger</p>
<h3>input options</h3>
<p>input file format : +f&#8211; read &#8211; file<br />
                                    read file format or<br />
    data set(default) + fo&#8211; read &#8211; file &#8211; only read file format only<br />
        &#8211; f&#8211; read &#8211; dataset read data set without file meta information input transfer syntax : -t = &#8211;read &#8211; xfer &#8211; auto use TS recognition(default) &#8211; td&#8211; read &#8211; xfer &#8211; detect ignore TS specified in the file meta header<br />
                                                                                                      &#8211; te&#8211; read &#8211; xfer &#8211; little read with explicit VR little endian TS<br />
                                                                                                      &#8211; tb&#8211; read &#8211; xfer &#8211; big read with explicit VR big endian TS<br />
                                                                                                      &#8211; ti&#8211; read &#8211; xfer &#8211; implicit read with implicit VR little endian TS</p>
<h3>signature commands</h3>
<p>&#8211;verify<br />
        verify all signatures(default) +<br />
    s&#8211; sign[p] rivate key file,<br />
    [c] ertificate file : string<br />
                          create signature in main object<br />
                          +<br />
                          si&#8211; sign &#8211; item[k] eyfile,<br />
    [c] ertfile, [i] tem location : string create signature in sequence item + r&#8211; remove[s] ignature UID : string remove signature + ra&#8211; remove &#8211; all remove all signatures from data set</p>
<h3>signature creation options (only with &#8211;sign or &#8211;sign-item):</h3>
<p>private<br />
key password : +ps&#8211; std &#8211; passwd prompt user to type password on stdin(default) + pw&#8211; use &#8211; passwd[p] assword : string use specified password<br />
                                                                                                                  &#8211;<br />
                                                                                                                  pw&#8211; null &#8211; passwd use empty string as password key and certificate file format : -pem&#8211; pem &#8211; keys read keys / certificates as PEM file(default) &#8211; der&#8211; der &#8211; keys read keys / certificates as DER file digital signature profile : -pf&#8211; profile &#8211; none don&#8217;t enforce any signature profile (default) + pb&#8211; profile &#8211; base enforce base RSA signature profile<br />
                                                                                                                                                                                                    +<br />
                                                                                                                                                                                                    pc&#8211; profile &#8211; creator enforce creator RSA signature profile<br />
                                                                                                                                                                                                    +<br />
                                                                                                                                                                                                    pa&#8211; profile &#8211; auth enforce authorization signature profile MAC algorithm : +mr&#8211; mac &#8211; ripemd160 use RIPEMD 160(default) + ms&#8211; mac &#8211; sha1 use SHA &#8211; 1 + mm&#8211; mac &#8211; md5 use MD 5 tag selection : -t&#8211; tag[t] ag : &#8220;gggg,eeee&#8221; or<br />
    dictionary name<br />
        sign only specified tag(this option can be specified multiple times) &#8211;<br />
        tf&#8211; tag &#8211; file[f] ilename : string read list of tags from text file signature format : -fn&#8211; format &#8211; new use correct DICOM signature format(default) &#8211; fo&#8211; format &#8211; old use old(pre &#8211; 3.5.4) DCMTK signature format,<br />
    non &#8211; conformant<br />
        if signature includes compressed pixel data</p>
<h3>output options</h3>
<p>output transfer syntax : +t = &#8211;write &#8211; xfer &#8211; same write with same TS as input(default) + te&#8211; write &#8211; xfer &#8211; little write with explicit VR little endian TS + tb&#8211; write &#8211; xfer &#8211; big write with explicit VR big endian TS + ti&#8211; write &#8211; xfer &#8211; implicit write with implicit VR little endian TS length encoding in sequences and items : +e&#8211; length &#8211; explicit write with explicit lengths(default) &#8211; e&#8211; length &#8211; undefined write with undefined lengths other output options : +d&#8211; dump[f] ilename : string dump byte stream fed into the MAC codec to file(only with&#8211; sign or &#8211;sign &#8211; item)</p>
<h2>NOTES</h2>
<h3>Files and Parameters</h3>
<p> The <code>dcmsign</code> utility reads and writes a number of files and file formats which are described in this section. </p>
<p> Public Key Certificates are expected in X.509v3 format, either with PEM or DER encoding. The dcmsign utility currently supports RSA and DSA public keys, although only RSA keys are defines in the Security Profiles of the DICOM standard. </p>
<p> Private Keys are expected in PEM or DER encoding. PEM is recommended (and default) because this allows to keep private keys in encrypted form. Command line options control the behaviour of <code>dcmsign</code> when an encrypted PEM key is opened (see above). In general it is not recommended to specify the encryption password in the command line because the command line may be visible to other processes in the system, e.g. &#8216;ps -ef&#8217;. </p>
<p> The list of data elements to sign can either be read from a file or specified on the command line or both (in this case the keys are combined). </p>
<p> On the command line, attribute keys are specified as </p>
<pre>
--tag &quot;gggg,eeee&quot;  where gggg and eeee are the hexadecimal group
                   and element numbers
--tag &quot;Name&quot;       where 'Name' is a symbolic attribute name from
                   the DICOM dictionary (see below).
</pre>
<p> When attribute tags are read from file with the <i>&#8211;tag-file</i> option, a plain text file of max. 64 kbyte is expected. Tags within the file are either symbolic names from the data dictionary or have the format (gggg,eeee) (with braces). Tags are separated by one or more whitespace characters. </p>
<p> The <i>&#8211;sign-item</i> operation requires a location string that describes in which sequence item a signature is to be created. The location string has the following format: </p>
<p>SequenceName[index].SequenceName[index].SequenceName[index](&#8230;)</p>
<p> where SequenceName is either a symbolic attribute name from the data dictionary or a numeric tag in the format (gggg,eeee) and index is an unsigned decimal integer for the item number, starting with zero for the first item in a sequence. As an example, the following location string </p>
<pre><code>
ReferencedSeriesSequence[0].ReferencedImageSequence[1]
</code></pre>
<p> would cause a digital signature to be created in the second item of the ReferencedImageSequence (0008,1140) which is located in the first item of the ReferencedSeriesSequence (0008,1115) which is located in the main DICOM dataset.</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmsign</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2000-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
