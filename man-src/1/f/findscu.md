---
title: "findscu(1)"
name: "findscu"
section: "1"
letter: "f"
url: "/docs/linux/man/1-findscu/"
description: "findscu – DICOM query (C-FIND) SCU"
---

<h2 class="name">NAME</h2>
<p> findscu &#8211; DICOM query (C-FIND) SCU </p>
<h2>SYNOPSIS</h2>
<pre><code>
findscu[options] peer port[dcmfile - in...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>findscu</code> application implements an SCU for the Query/Retrieve Service Class and the Basic Worklist Management Service Class. <code>findscu</code> only supports query functionality using the C-FIND message. It sends query keys to an SCP and awaits responses. The application can be used to test SCPs of the Query/Retrieve and Basic Worklist Management Service Classes.</p>
<h2>PARAMETERS</h2>
<pre>
peer        hostname of DICOM peer
port        tcp/ip port number of peer
dcmfile-in  DICOM query file(s)
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
<h3>network options</h3>
<p>override matching keys:<br />
  -k    &#8211;key  [k]ey: gggg,eeee=&#8221;str&#8221;, path or dictionary name=&#8221;str&#8221;<br />
          override matching key<br />
query information model:<br />
  -W    &#8211;worklist<br />
          use modality worklist information model (default)<br />
  -P    &#8211;patient<br />
          use patient root information model<br />
  -S    &#8211;study<br />
          use study root information model<br />
  -O    &#8211;psonly<br />
          use patient/study only information model<br />
application entity titles:<br />
  -aet  &#8211;aetitle  [a]etitle: string<br />
          set my calling AE title (default: FINDSCU)<br />
  -aec  &#8211;call  [a]etitle: string<br />
          set called AE title of peer (default: ANY-SCP)<br />
post-1993 value representations:<br />
  +u    &#8211;enable-new-vr<br />
          enable support for new VRs (UN/UT) (default)<br />
  -u    &#8211;disable-new-vr<br />
          disable support for new VRs, convert to OB<br />
proposed transmission transfer syntaxes:<br />
  -x=   &#8211;propose-uncompr<br />
          propose all uncompressed TS, explicit VR<br />
          with local byte ordering first (default)<br />
  -xe   &#8211;propose-little<br />
          propose all uncompressed TS, explicit VR<br />
          little endian first<br />
  -xb   &#8211;propose-big<br />
          propose all uncompressed TS, explicit VR<br />
          big endian first<br />
  -xi   &#8211;propose-implicit<br />
          propose implicit VR little endian TS only<br />
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
          abort association instead of releasing it<br />
        &#8211;cancel  [n]umber: integer<br />
          cancel after n responses (default: never)<br />
  -X    &#8211;extract<br />
          extract responses to file (rsp0001.dcm, &#8230;)</p>
<h3>transport layer security (TLS) options</h3>
<p>transport protocol stack:<br />
  -tls  &#8211;disable-tls<br />
          use normal TCP/IP connection (default)<br />
  +tls  &#8211;enable-tls  [p]rivate key file, [c]ertificate file: string<br />
          use authenticated secure TLS connection<br />
  +tla  &#8211;anonymous-tls<br />
          use secure TLS connection without certificate<br />
private key password (only with &#8211;enable-tls):<br />
  +ps   &#8211;std-passwd<br />
          prompt user to type password on stdin (default)<br />
  +pw   &#8211;use-passwd  [p]assword: string<br />
          use specified password<br />
  -pw   &#8211;null-passwd<br />
          use empty string as password<br />
key and certificate file format:<br />
  -pem  &#8211;pem-keys<br />
          read keys and certificates as PEM file (default)<br />
  -der  &#8211;der-keys<br />
          read keys and certificates as DER file<br />
certification authority:<br />
  +cf   &#8211;add-cert-file  [c]ertificate filename: string<br />
          add certificate file to list of certificates<br />
  +cd   &#8211;add-cert-dir  [c]ertificate directory: string<br />
          add certificates in d to list of certificates<br />
ciphersuite:<br />
  +cs   &#8211;cipher  [c]iphersuite name: string<br />
          add ciphersuite to list of negotiated suites<br />
  +dp   &#8211;dhparam  [f]ilename: string<br />
          read DH parameters for DH/DSS ciphersuites<br />
pseudo random generator:<br />
  +rs   &#8211;seed  [f]ilename: string<br />
          seed random generator with contents of f<br />
  +ws   &#8211;write-seed<br />
          write back modified seed (only with &#8211;seed)<br />
  +wf   &#8211;write-seed-file  [f]ilename: string (only with &#8211;seed)<br />
          write modified seed to file f<br />
peer authentication:<br />
  -rc   &#8211;require-peer-cert<br />
          verify peer certificate, fail if absent (default)<br />
  -vc   &#8211;verify-peer-cert<br />
          verify peer certificate if present<br />
  -ic   &#8211;ignore-peer-cert<br />
          don&#8217;t verify peer certificate</p>
<h2>NOTES</h2>
<p> Each file supplied on the command line will be sent to the SCP as part of a C-FIND request. The query file must be a valid DICOM data set containing the dataset part of a C-FIND-RQ message. The query file could, for instance, be created with the <code>dump2dcm</code> utility from a script like the following example: </p>
<pre><code>
#query patient names and IDs
(0008, 0052) CS[PATIENT] #QueryRetrieveLevel(0010, 0010) PN[] #PatientName(0010, 0020) LO[] #PatientID
</code></pre>
<p> Individual attributes of each file sent can be modified or supplemented using the <i>-k</i> option. For example the command: </p>
<pre>
findscu -P -k &quot;(0010,0010)=HEWETT*&quot; caesar 5678 patqry.dcm
</pre>
<p> will, when sent to the SCP caesar at TCP/IP port 5678, cause any PatientName attribute in patqry.dcm to have the value &#8216;HEWETT*&#8217;. If such an attribute is present it will be replaced, if absent it will be inserted. The <i>-k</i> option can be present more than once. The value part (after the &#8216;=&#8217;) may be absent causing the attribute to be sent with zero length. </p>
<p> In earlier versions of <code>findscu</code>, the tag keys were specified without braces around group and element number, e. g. &#8216;0010,0010&#8217; instead of &#8216;(0010,0010)&#8217;. It is recommended switching to the new syntax; however, the old syntax is still working. </p>
<p> Also <i>-k</i> accepts dictionary names instead of element tags for specifying DICOM elements. For example, the <code>findscu</code> call above then reads like this: </p>
<pre>
findscu -P -k PatientName=&quot;HEWETT*&quot; caesar 5678 patqry.dcm
</pre>
<p> It is also possible to specify sequences, items and nested attributes using the <i>-k</i> option. In these cases, a special &#8216;path&#8217; notation has to be used, e. g. </p>
<pre>
findscu -W -k &quot;(0040,0100)[0].Modality=CT&quot; caesar 5678
</pre>
<p> This call queries a worklist server at host caesar for any planned procedures for CT modalities by specifing tag (0040,0100) &#8216;Scheduled Procedure Step Sequence&#8217; and an attribute &#8216;Modality&#8217; in the first item of this sequence with value &#8216;CT&#8217;. Details on this path notation can be found in the documentation of <code>dcmodify</code>. </p>
<p> If no file is specified on the command line, the query must be specified completely with one or more <i>-k</i> options. </p>
<p> Each set of response identifiers received will be printed to stdout unless option <i>&#8211;extract</i> is used.</p>
<h3>DICOM Conformance</h3>
<p> The <code>findscu</code> application supports the following SOP Classes as an SCU: </p>
<pre>
FINDPatientRootQueryRetrieveInformationModel       1.2.840.10008.5.1.4.1.2.1.1
FINDStudyRootQueryRetrieveInformationModel         1.2.840.10008.5.1.4.1.2.2.1
FINDPatientStudyOnlyQueryRetrieveInformationModel  1.2.840.10008.5.1.4.1.2.3.1
FINDModalityWorklistInformationModel               1.2.840.10008.5.1.4.31
</pre>
<p> The <code>findscu</code> application will propose presentation contexts for one of the abovementioned supported SOP Classes depending on command line options (<i>-P</i>, <i>-S</i>, <i>-O</i> or <i>-W</i>). Each proposed presentation context will propose the transfer syntaxes: </p>
<pre>
LittleEndianImplicitTransferSyntax                 1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax                 1.2.840.10008.1.2.1
BigEndianExplicitTransferSyntax                    1.2.840.10008.1.2.2
</pre>
<p> The <code>findscu</code> application does not support extended negotiation.</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>findscu</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-movescu/">movescu</a></code>(1), <code><a href="/docs/linux/man/1-dump2dcm/">dump2dcm</a></code>(1), <code><a href="/docs/linux/man/1-dcmodify/">dcmodify</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1994-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
