---
title: "wlmscpfs(1)"
name: "wlmscpfs"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wlmscpfs/"
description: "wlmscpfs – DICOM Basic Worklist Management SCP (based on data files)"
---

<h2 class="name">NAME</h2>
<p> wlmscpfs &#8211; DICOM Basic Worklist Management SCP (based on data files) </p>
<h2>SYNOPSIS</h2>
<pre>
wlmscpfs [options] port
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>wlmscpfs</code> application implements a Service Class Provider (SCP) for the Basic Worklist Management Service. The application will listen on a specified TCP/IP port for incoming association requests from a Worklist Management SCU. In case an association was acknowledged and a worklist query was received, the <code>wlmscpfs</code> application will query particular files in a certain directory (which can be specified through corresponding program options) on the file system for corresponding worklist information, and it will send this information back to the calling Worklist Management SCU. Aside from dealing with Worklist Management queries, the <code>wlmscpfs</code> application also supports the Verification Service Class as an SCP.</p>
<h2>PARAMETERS</h2>
<pre>
port  tcp/ip port number to listen on
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
<h3>multi-process options</h3>
<pre>
  -s    --single-process
          single process mode
        --fork
          fork child process for each association (default)
</pre>
<h3>input options</h3>
<p>general : -dfp&#8211; data &#8211; files &#8211; path[p] ath : string(default<br />
                                                     : / home / www / wlist) path to worklist data files handling of worklist files : -efr&#8211; enable<br />
                                                                                                                                      &#8211;<br />
                                                                                                                                      file &#8211; reject enable rejection of incomplete worklist files(default) &#8211; dfr&#8211; disable &#8211; file &#8211; reject disable rejection of incomplete worklist files</p>
<h3>processing options</h3>
<p>returned character set : -cs0&#8211; return -no &#8211; char &#8211; set return no specific character set(default) &#8211; cs1&#8211; return -iso &#8211; ir &#8211; 100 return specific character set ISO IR 100 &#8211; csk&#8211; keep &#8211; char &#8211; set return character set provided in file other processing options : -nse&#8211; no &#8211; sq &#8211; expansion disable expansion of empty sequences in C &#8211; FIND request messages</p>
<h3>network options</h3>
<pre><code>
preferred network transfer syntaxes:
  +x=   --prefer-uncompr
          prefer explicit VR local byte order (default)
  +xe   --prefer-little
          prefer explicit VR little endian TS
  +xb   --prefer-big
          prefer explicit VR big endian TS
  +xi   --implicit
          accept implicit VR little endian TS only
network host access control (tcp wrapper):
  -ac   --access-full
          accept connections from any host (default)
  +ac   --access-control
          enforce host access control rules
post-1993 value representations:
  +u    --enable-new-vr
          enable support for new VRs (UN/UT) (default)
  -u    --disable-new-vr
          disable support for new VRs, convert to OB
other network options:
  -ta   --acse-timeout  [s]econds: integer (default: 30)
          timeout for ACSE messages
  -td   --dimse-timeout  [s]econds: integer (default: unlimited)
          timeout for DIMSE messages
        --max-associations  [a]ssocs: integer (default: 50)
          limit maximum number of parallel associations
        --refuse
          refuse association
        --reject
          reject association if no implementation class UID
        --no-fail
          don't fail on an invalid query
        --sleep-after  [s]econds: integer
          sleep s seconds after find (default: 0)
        --sleep-during  [s]econds: integer
          sleep s seconds during find (default: 0)
  -pdu  --max-pdu  [n]umber of bytes: integer (4096..131072)
          set max receive pdu to n bytes (default: 16384)
  -dhl  --disable-host-lookup
          disable hostname lookup
</code></pre>
<h2>NOTES</h2>
<p> The semantic impacts of the above mentioned options is clear for the majority of options. Some particular options, however, are so specific that they need detailed descriptions which will be given in this passage. </p>
<p> The returned character set options are intended for situations in which the <code>wlmscpfs</code> application will return attribute values which are not composed of characters from the DICOM default character repertoire. In such cases, for example option <i>&#8211;return-iso-ir-100</i> can be used to specify that a response to a modality&#8217;s worklist management C-FIND request shall contain DICOM&#8217;s Specific Character Set attribute (0008,0005) with a corresponding value, indicating the character repertoire from which the characters of returned attribute values were taken (in this example the repertoire ISO IR 100). Please note that the <code>wlmscpfs</code> application will not make sure that all returned values are actually made up of this character repertoire; the application expects this to be the case. </p>
<p> In general, the Specific Character Set attribute (0008,0005) will only be included in the C-FIND response if it contains any attributes that are affected by the character set, i.e. for value representations PN, LO, LT, SH, ST and UT. </p>
<p> Please note that a C-FIND request which is handled by this application may contain DICOM&#8217;s Specific Character Set attribute (0008,0005), but this application will never use this attribute&#8217;s value for matching. Besides, the question if DICOM&#8217;s Specific Character Set attribute (0008,0005) will be contained in a C-FIND response which is returned by this application is always determined by the returned character set option which was specified when this application was started. </p>
<p> The options &#8211;enable-file-reject and &#8211;disable-file-reject can be used to enable or disable a file rejection mechanism which makes sure only complete worklist files will be used during the matching process. A worklist file is considered to be complete if it contains all necessary type 1 information which the SCP might have to return to an SCU in a C-FIND response message. Table K.6-1 in part 4 annex K of the DICOM standard lists all corresponding type 1 attributes (see column &#8216;Return Key Type&#8217;).</p>
<h3>DICOM Conformance</h3>
<p> The <code>wlmscpfs</code> application supports the following SOP Classes as an SCP: </p>
<pre>
VerificationSOPClass                  1.2.840.10008.1.1
FINDModalityWorklistInformationModel  1.2.840.10008.5.1.4.31
</pre>
<p> The <code>wlmscpfs</code> application will accept presentation contexts for all of the abovementioned supported SOP Classes using any of the transfer syntaxes: </p>
<pre>
LittleEndianImplicitTransferSyntax    1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax    1.2.840.10008.1.2.1
BigEndianExplicitTransferSyntax       1.2.840.10008.1.2.2
</pre>
<p> The default behaviour of the <code>wlmscpfs</code> application is to prefer transfer syntaxes having an explicit encoding over the default implicit transfer syntax. If <code>wlmscpfs</code> is running on big-endian hardware it will prefer BigEndianExplicit to LittleEndianExplicit transfer syntax (and vice versa). This behaviour can be changed with the <i>&#8211;prefer</i> options (see above). </p>
<p> The <code>wlmscpfs</code> application does not support extended negotiation. </p>
<p> Currently, the <code>wlmscpfs</code> application supports the following attributes as matching keys: </p>
<pre>
(0008,0050) AccessionNumber
(0008,0090) ReferringPhysicianName
(0010,0010) PatientName
(0010,0020) PatientID
(0010,0030) PatientBirthDate
(0010,0040) PatientSex
(0032,1032) RequestingPhysician
(0038,0010) AdmissionID
(0040,0100) ScheduledProcedureStepSequence
  (0008,0060) &gt; Modality
  (0040,0001) &gt; ScheduledStationAETitle
  (0040,0002) &gt; ScheduledProcedureStepStartDate
  (0040,0003) &gt; ScheduledProcedureStepStartTime
  (0040,0006) &gt; ScheduledPerformingPhysicianName
(0040,1001) RequestedProcedureID
(0040,1003) RequestedProcedurePriority
</pre>
<p> As return keys the following attributes are currently supported by <code>wlmscpfs:</code> </p>
<pre>
(0008,0050) AccessionNumber
(0008,0080) InstitutionName
(0008,0081) InstitutionAddress
(0008,0090) ReferringPhysicianName
(0008,1080) AdmittingDiagnosesDescription
(0008,1110) ReferencedStudySequence
  (0008,1150) &gt; ReferencedSOPClassUID
  (0008,1155) &gt; ReferencedSOPInstanceUID
(0008,1120) ReferencedPatientSequence
  (0008,1150) &gt; ReferencedSOPClassUID
  (0008,1155) &gt; ReferencedSOPInstanceUID
(0010,0010) PatientName
(0010,0020) PatientID
(0010,0030) PatientBirthDate
(0010,0040) PatientSex
(0010,1000) OtherPatientIDs
(0010,1001) OtherPatientNames
(0010,1020) PatientSize
(0010,1030) PatientWeight
(0010,1040) PatientAddress
(0010,1080) MilitaryRank
(0010,2000) MedicalAlerts
(0010,2110) ContrastAllergies
(0010,2160) EthnicGroup
(0010,21a0) SmokingStatus
(0010,21b0) AdditionalPatientHistory
(0010,21c0) PregnancyStatus
(0010,21d0) LastMenstrualDate
(0010,4000) PatientComments
(0020,000d) StudyInstanceUID
(0032,1032) RequestingPhysician
(0032,1033) RequestingService
(0032,1060) RequestedProcedureDescription
(0032,1064) RequestedProcedureCodeSequence
  (0008,0100) &gt; CodeValue
  (0008,0102) &gt; CodingSchemeDesignator
  (0008,0103) &gt; CodingSchemeVersion
  (0008,0104) &gt; CodeMeaning
(0038,0010) AdmissionID
(0038,0011) IssuerOfAdmissionID
(0038,0050) SpecialNeeds
(0038,0300) CurrentPatientLocation
(0038,0500) PatientState
(0040,0100) ScheduledProcedureStepSequence
  (0008,0060) &gt; Modality
  (0032,1070) &gt; RequestedContrastAgent
  (0040,0001) &gt; ScheduledStationAETitle
  (0040,0002) &gt; ScheduledProcedureStepStartDate
  (0040,0003) &gt; ScheduledProcedureStepStartTime
  (0040,0004) &gt; ScheduledProcedureStepEndDate
  (0040,0005) &gt; ScheduledProcedureStepEndTime
  (0040,0006) &gt; ScheduledPerformingPhysicianName
  (0040,0007) &gt; ScheduledProcedureStepDescription
  (0040,0008) &gt; ScheduledProtocolCodeSequence
    (0008,0100) &gt;  &gt; CodeValue
    (0008,0102) &gt;  &gt; CodingSchemeDesignator
    (0008,0103) &gt;  &gt; CodingSchemeVersion
    (0008,0104) &gt;  &gt; CodeMeaning
  (0040,0009) &gt; ScheduledProcedureStepID
  (0040,0010) &gt; ScheduledStationName
  (0040,0011) &gt; ScheduledProcedureStepLocation
  (0040,0012) &gt; PreMedication
  (0040,0020) &gt; ScheduledProcedureStepStatus
  (0040,0400) &gt; CommentsOnTheScheduledProcedureStep
(0040,1001) RequestedProcedureID
(0040,1002) ReasonForTheRequestedProcedure
(0040,1003) RequestedProcedurePriority
(0040,1004) PatientTransportArrangements
(0040,1005) RequestedProcedureLocation
(0040,1008) ConfidentialityCode
(0040,1009) ReportingPriority
(0040,1010) NamesOfIntendedRecipientsOfResults
(0040,1400) RequestedProcedureComments
(0040,2001) ReasonForTheImagingServiceRequest
(0040,2004) IssueDateOfImagingServiceRequest
(0040,2005) IssueTimeOfImagingServiceRequest
(0040,2008) OrderEnteredBy
(0040,2009) OrderEnterersLocation
(0040,2010) OrderCallbackPhoneNumber
(0040,2016) PlacerOrderNumberImagingServiceRequest
(0040,2017) FillerOrderNumberImagingServiceRequest
(0040,2400) ImagingServiceRequestComments
(0040,3001) ConfidentialityConstraintOnPatientDataDescription
</pre>
<p> The attribute (0008,0005) SpecificCharacterSet is a special case and its support by <code>wlmscpfs</code> is discussed in the NOTES section above.</p>
<h3>Access Control</h3>
<p> When compiled on Unix platforms with TCP wrapper support, host-based access control can be enabled with the <i>&#8211;access-control</i> command line option. In this case the access control rules defined in the system&#8217;s host access control tables for <code>wlmscpfs</code> are enforced. The default locations of the host access control tables are <i>/etc/hosts.allow</i> and <i>/etc/hosts.deny</i>. Further details are described in <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5).</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>wlmscpfs</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1996-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
