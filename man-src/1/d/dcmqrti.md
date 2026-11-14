---
title: "dcmqrti(1)"
name: "dcmqrti"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmqrti/"
description: "dcmqrti – The Terminal Initiator Telnet Client Program"
---

<h2 class="name">NAME</h2>
<p> dcmqrti &#8211; The Terminal Initiator Telnet Client Program </p>
<h2>SYNOPSIS</h2>
<pre>
dcmqrti [options] peer...
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>dcmqrti</code> program (telnet initiator) is an interactive character based program intended to be used for examining the dcmqrscp image databases and sending images contained within these databases to Vendor nodes. During a DICOM Demonstration the <code>dcmqrti</code> program can be activated by a Vendor by logging onto the computer running the <code>dcmqrscp</code> program. Each vendor will have their own login account and the <code>dcmqrti</code> program will be started instead of a normal shell when they login. </p>
<p> The <code>dcmqrti</code> program takes one main argument, the hostname or vendor symbolic name (from the VendorTable in the configuration file) of a Vendor. It then searches in the configuration file for all AE titles associated with this hostname or vendor name, and all storage areas accessable to these AE titles. Thus only the accessable databases and peer applications discovered in the configuration file are available as choices within the <code>dcmqrti</code> user interface.</p>
<h2>PARAMETERS</h2>
<pre>
peer  peer host name or symbolic name from cfg file
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
  -c    --config  [f]ilename: string
          use specific configuration file
          (default: /usr/local/etc/dcmqrscp.cfg)
</code></pre>
<h3>network options</h3>
<p>  -to   &#8211;timeout  [s]econds: integer (default: unlimited)<br />
          timeout for connection requests<br />
  -ta   &#8211;acse-timeout  [s]econds: integer (default: 30)<br />
          timeout for ACSE messages<br />
  -td   &#8211;dimse-timeout  [s]econds: integer (default: unlimited)<br />
          timeout for DIMSE messages<br />
  -xi   &#8211;propose-implicit<br />
          propose implicit VR little endian TS only<br />
  -aet  &#8211;aetitle  [a]etitle: string<br />
          set my AE title (default: TELNET_INITIATOR)<br />
  -pdu  &#8211;max-pdu  [n]umber of bytes: integer (4096..131072)<br />
          set max receive pdu to n bytes<br />
          (default: use value from configuration file)</p>
<h3>other options</h3>
<p>  -u    &#8211;disable-new-vr<br />
          disable support for new VRs, convert to OB<br />
  -rmt  &#8211;remote  [t]itle: string<br />
          connect to remote database defined in cfg file</p>
<h2>NOTES</h2>
<h3>Commands</h3>
<p> All commands can be abbreviated. An abbreviation is allowed if it does not conflict with another command.</p>
<h3>&#8216;help&#8217; Command</h3>
<p> The &#8216;help&#8217; command gives a summary of all available commands. Its output is shown underneath. In order to separate the examples from surrounding text, all examples are bracketted by dashed lines. These lines do not appear when running the program. </p>
<p>&#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;Command Summary : help list this summary<br />
    ? short help<br />
          title[#] list[set] current peer AE title<br />
              database[#] list[set] current database<br />
                  study[#] list[set] current study<br />
                      series[#] list[set] current series<br />
                          image[#] list[set] current image<br />
                              display[#] display current[specific] image<br />
                                  send study[#] send current[specific] study<br />
                                      send series[#] send current[specific] series<br />
                                          send image[#] send current[specific] image<br />
                                              echo[#] verify connectivity[#times] quit quit program<br />
                                                  exit synonym for quit&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;</p>
<h3>&#8216;title&#8217; Command</h3>
<p> The &#8216;title&#8217; command without an argument allows the user to list the known remote Application Entities (AE). An example output might look like: </p>
<p>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;<br />
Peer AE Titles:<br />
     Peer AE          HostName:PortNumber<br />
* 0) ACME1            (swallow:2001)<br />
  1) ACME2            (swallow:2002)<br />
  2) UNITED1          (kolibri:2001)<br />
  3) UNITED2          (kolibri:2002)<br />
&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;</p>
<p> The current peer AE is marked with an asterisk (*). Each peer AE has an index (second column) which can be used as an argument to the &#8216;title&#8217; command in order to set the current peer AE. The third column gives the AE title of the peer AE. The fourth column shows the hostname and TCP/IP port number of the peer AE. </p>
<p> When invoked with an argument index, the &#8216;title&#8217; command will set the current peer AE. The <code>dcmqrti</code> program will attempt to initate an association to the current peer AE when asked to send a study/series/image or to send an echo.</p>
<h3>&#8216;database&#8217; Command</h3>
<p> The &#8216;database&#8217; command without an argument allows the user to list the know local databases (these correspond to dcmqrscp&#8217;s Application Entity Titles). An example output might look like: </p>
<p>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;<br />
Database Titles:<br />
     Database<br />
* 0) COMMON<br />
  1) ACME_QUERY<br />
  2) ACME_STORE<br />
  3) UNITED_QUERY<br />
&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;</p>
<p> The current database is marked with an asterisk (*). Each database has an index (second column) which can be used as an argument to the &#8216;database&#8217; command in order to set the current database. The third column shows the name of the database (i.e. the dcmqrscp Application Entity title for the particular storage area). </p>
<p> When invoked with an argument index, the &#8216;database&#8217; command will set the current database. The current database is used as the basis for further database specific actions.</p>
<h3>&#8216;study&#8217; Command</h3>
<p> The &#8216;study&#8217; command with no argument lists the studies in the current database. An example output might look like: </p>
<p>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;<br />
      Patient                        PatientID    StudyID<br />
*  0) JACKSON^ANDREW^^^              M4997106     20001<br />
   1) GRANT^MARY^^^                  F4997108     20002<br />
   2) ARTHUR^CHESTER^^^              M4997107     20003<br />
   3) JEFFERSON^THOMAS^^^            M4997096     9465<br />
   4) MADISON^DOLLY^^^               F4997097     9443<br />
4 Studies in Database: COMMON<br />
&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;</p>
<p> The current study is marked with an asterisk (*). Each study has an index (second column) which can be used as an argument to the &#8216;study&#8217; command in order to set the current study. The third column shows the patient name, the fourth column the patient ID and the fifth column the study ID. </p>
<p> When invoked with an argument index, the &#8216;study&#8217; command will set the current study. The current study is used as the basis for further study specific actions.</p>
<h3>&#8216;series&#8217; Command</h3>
<p> The &#8216;series&#8217; command with no argument lists the series in the current study. An example output might look like: </p>
<p>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;<br />
      Series Modality SeriesInstanceUID<br />
*  0) 1      MR       1.2.840.113654.2.3.1993.201<br />
   1) 2      MR       1.2.840.113654.2.3.1993.202<br />
   2) 3      MR       1.2.840.113654.2.3.1993.203<br />
   3) 4      MR       1.2.840.113654.2.3.1993.204<br />
   4) 5      MR       1.2.840.113654.2.3.1993.205<br />
5 Series in StudyID 05381,<br />
  Patient: MONROE^JAMES^^^ (Database: COMMON)<br />
&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;</p>
<p> The current series is marked with an asterisk (*). Each series has an index (second column) which can be used as an argument to the &#8216;series&#8217; command in order to set the current series. The third column shows the series number, the fourth column the series modality, and the fifth column the series instance UID. </p>
<p> When invoked with an argument index, the &#8216;series&#8217; command will set the current series. The current series is used as the basis for further series specific actions.</p>
<h3>&#8216;image&#8217; Command</h3>
<p> The &#8216;image&#8217; command with no argument lists the images in the current series. An example output might look like: </p>
<p>&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;<br />
      Image ImageInstanceUID<br />
*  0) 1     1.2.840.113654.2.3.1993.9.123.6.2674<br />
   1) 2     1.2.840.113654.2.3.1993.9.123.6.2675<br />
   2) 3     1.2.840.113654.2.3.1993.9.123.6.2676<br />
   3) 4     1.2.840.113654.2.3.1993.9.123.6.2677<br />
   4) 5     1.2.840.113654.2.3.1993.9.123.6.2678<br />
   5) 6     1.2.840.113654.2.3.1993.9.123.6.2679<br />
   6) 7     1.2.840.113654.2.3.1993.9.123.6.2680<br />
   7) 8     1.2.840.113654.2.3.1993.9.123.6.2681<br />
   8) 9     1.2.840.113654.2.3.1993.9.123.6.2682<br />
   9) 10    1.2.840.113654.2.3.1993.9.123.6.2683<br />
  10) 11    1.2.840.113654.2.3.1993.9.123.6.2684<br />
  11) 12    1.2.840.113654.2.3.1993.9.123.6.2685<br />
  12) 13    1.2.840.113654.2.3.1993.9.123.6.2686<br />
13 Images in MR Series, StudyID 05381,<br />
  Patient: MONROE^JAMES^^^ (Database: COMMON)<br />
&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;</p>
<p> The current image is marked with an asterisk (*). Each image has an index (second column) which can be used as an argument to the &#8216;image&#8217; command in order to set the current image. The third column shows the image number, and the fourth column the image instance UID (SOP Instance UID). </p>
<p> When invoked with an argument index, the &#8216;image&#8217; command will set the current image. The current image is used as the basis for further image specific actions.</p>
<h3>&#8216;display&#8217; Command</h3>
<p> The display command serves no purpose in the current version of DCMTK. It was used in prior releases to request the CTN Display Program to display an image.</p>
<h3>&#8216;send&#8217; Command</h3>
<p> The &#8216;send&#8217; command allows a complete study/series or individual image to be stored on a remote AE. When this command is invoked, the <code>dcmqrti</code> program will operate as a SCU of the DICOM Storage Service Class and attempt to initiate an association with the current peer AE (defined via the &#8216;title&#8217; command). Presentation contexts for all relevant Storage SOP Classes will be proposed. An attempt will be made to store all specified images. If no association could be negotiated an error message will be printed. If an storage operation fails or if no appropriate presentation context is available and error message will be printed. </p>
<p>The &#8220;send&#8221; command exists in three forms : send study[#] send series[#] send image[#]</p>
<p> The &#8216;study&#8217; keyword means send all images in the current study. When invoked with an argument index, the specified study in the current database will be stored. The &#8216;series&#8217; keyword means send all images in the current series. When invoked with an argument index, the specified series in the current study will be stored. The &#8216;image&#8217; keyword means send the current image. When invoked with an argument index, the specified image in the current series will be stored. </p>
<p> When an image is stored, a message will be printed of the form: </p>
<p>&#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;New Association Started(swallow : 2001, ACME1)<br />
                                                                                           [MsgID 1] Store,<br />
    PatientName : JACKSON ^ ANDREW ^ ^^, StudyID : 20001,<br />
    Series : 2, Modality : CR, Image : 1, Image UID : 1.2.840.113654.2.3.1993.9.123.6.1834 0 % ________25 % _________50 % __________75 % ________100 % &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8211;[MsgID 1] Complete [Status:Success] Released Association(swallow : 2001, ACME1)&#8211; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212; &#8212;</p>
<h3>&#8216;echo&#8217; Command</h3>
<p> The &#8216;echo&#8217; command allows the user to verify connectivity with the current peer AE (defined via the &#8216;title&#8217; command). When invoked, the <code>dcmqrti</code> program acts as an SCU of the Verification Service Class. </p>
<p> When invoked without an argument, only one C-ECHO message is generated. When invoked with an argument, the specified number of C-ECHO messages will be sent. A message will be printed of the form: </p>
<pre><code>
-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --New Association Started(localhost : 2001, CMOVE)
                                                                                           [MsgID 1] Echo,
Complete [Status:Success] Released Association(localhost : 2001, CMOVE)-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
</code></pre>
<h3>&#8216;quit&#8217;, &#8216;exit&#8217; Commands</h3>
<p> The &#8216;quit&#8217; and &#8216;exit&#8217; commands have the same effect. They terminate the <code>dcmqrti</code> program.</p>
<h3>DICOM Conformance</h3>
<p> The <code>dcmqrti</code> application supports the same set of SOP Classes as an SCU as the <code>dcmqrscp</code> application &#8211; see dcmqrscp documentation. </p>
<p> The <code>dcmqrti</code> application will propose presentation contexts for all of the abovementioned supported SOP Classes using the transfer syntaxes: </p>
<pre>
LittleEndianImplicitTransferSyntax  1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax  1.2.840.10008.1.2.1
BigEndianExplicitTransferSyntax     1.2.840.10008.1.2.2
</pre>
<p> The <code>dcmqrti</code> application does not support extended negotiation.</p>
<h3>Configuration</h3>
<p> The <code>dcmqrti</code> program uses the same configuration file as the <code>dcmqrscp</code> program. See the documentation on configuration for more information (<i>dcmqrcnf.txt</i> and the example configuration file <i>dcmqrscp.cfg</i>).</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmqrti</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>FILES</h2>
<p> <i>&lt;docdir&gt;/dcmqrcnf.txt</i> &#8211; configuration information<br />
 <i>&lt;docdir&gt;/dcmqrset.txt</i> &#8211; setup information<br />
 <i>&lt;etcdir&gt;/dcmqrscp.cfg</i> &#8211; example configuration file</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmqrscp/">dcmqrscp</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1993-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
