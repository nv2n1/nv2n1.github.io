---
title: "dcmqrscp(1)"
name: "dcmqrscp"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcmqrscp/"
description: "dcmqrscp – DICOM image archive (central test node)"
---

<h2 class="name">NAME</h2>
<p> dcmqrscp &#8211; DICOM image archive (central test node) </p>
<h2>SYNOPSIS</h2>
<pre><code>
dcmqrscp[options][port]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The Image Central Test Node (<code>dcmqrscp</code>) Application implements a simple image archive. It manages a number of storage areas and allows images to be stored in these storage areas using the DICOM Storage Service Class. It also allows image attributes to be queried and images to be retrieved using the DICOM Query/Retrieve Service Class. The <code>dcmqrscp</code> application also implements access restriction rules to limit operations to specific peer application entities. </p>
<p> The <code>dcmqrscp</code> application is intended to be used in DICOM demonstrations and as a compatibilitiy test tool. In particular, <code>dcmqrscp</code> will delete images if its quota restrictions have been exceeded.</p>
<h2>PARAMETERS</h2>
<pre>
port  tcp/ip port number to listen on (default: in config file)
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
          use config file f for the logger<br />
  -c    &#8211;config  [f]ilename: string<br />
          use specific configuration file<br />
          (default: /usr/local/etc/dcmtk/dcmqrscp.cfg)<br />
#This option allows a specific configuration file to be<br />
#specified.By default, the configuration file in the<br />
#system configuration directory(&#8220;etc&#8221; on Unix systems and<br />
#current working directory on Windows systems) with the name<br />
#&#8221;dcmqrscp.cfg&#8221; will be used.It is an error if a valid<br />
#configuration file is not available.See the documentation<br />
#on configuration for more information(dcmqrcnf.txt and the<br />
#example configuration file dcmqrscp.cfg).</p>
<h3>multi-process options</h3>
<pre>
  -s    --single-process
          single process mode
  # This option instructs dcmqrscp to run in single process mode.
  # Normally, dcmqrscp will spawn a new copy of itself to handle
  # each association.  This option will prevent such copies being
  # spawned and is particularly useful when running within a
  # debugger.
        --fork
          fork child process for each association (default)
</pre>
<h3>database options</h3>
<p>association negotiation:<br />
        &#8211;require-find<br />
          reject all MOVE/GET presentation contexts for<br />
          which no corresponding FIND context is proposed<br />
#This option causes dcmqrscp to enforce a restriction about<br />
#FIND and MOVE presentation contexts.The RSNA&#8217;93 demonstration<br />
#required that a CTN refuse to accept a presentation context for<br />
#a MOVE if a FIND presentation context is not also requested.<br />
#This option enforces this restriction.<br />
        &#8211;no-parallel-store<br />
          reject multiple simultaneous STORE presentation<br />
          contexts for one application entity title<br />
#This option causes dcmqrscp to refuse storage presentations<br />
#contexts for AE Titles if another association has already<br />
#sucessfully negotiated storage presentation contexts for the<br />
#AE Title.This option should only be needed for debugging<br />
#since the dcmqrscp database back &#8211; end sequentialises access via<br />
#file &#8211; locking.<br />
        &#8211;disable-get<br />
          disable C-GET support<br />
        &#8211;allow-shutdown<br />
          allow external shutdown via a private SOP class<br />
checking identifier validity:<br />
  -XF   &#8211;check-find<br />
          check C-FIND identifier validity<br />
#This option causes dcmqrscp database back &#8211; end to perform checks<br />
#on the Query Identifiers for a C &#8211; FIND command.With this option,<br />
#dcmqrscp will reject any queries which do not conform to the very<br />
#strict DICOM rules for Query Identifiers.<br />
        &#8211;no-check-find<br />
          do not check C-FIND identifier validity (default)<br />
  -XM   &#8211;check-move<br />
          check C-MOVE identifier validity<br />
#This option causes dcmqrscp database back &#8211; end to perform checks<br />
#on the Query Identifiers for a C &#8211; MOVE command.With this option,<br />
#dcmqrscp will reject any queries which do not conform to the very<br />
#strict DICOM rules for Query Identifiers.<br />
        &#8211;no-check-move<br />
          do not check C-MOVE identifier validity (default)<br />
restriction of move targets:<br />
        &#8211;move-unrestricted<br />
          do not restrict move destination (default)<br />
  -ZA   &#8211;move-aetitle<br />
          restrict move destination to requesting AE title<br />
  -ZH   &#8211;move-host<br />
          restrict move destination to requesting host<br />
  -ZV   &#8211;move-vendor<br />
          restrict move destination to requesting vendor<br />
restriction of query/retrieve models:<br />
  -QP   &#8211;no-patient-root<br />
          do not support Patient Root Q/R models<br />
  -QS   &#8211;no-study-root<br />
          do not support Study Root Q/R models<br />
  -QO   &#8211;no-patient-study<br />
          do not support Patient/Study Only Q/R models</p>
<h3>network options</h3>
<p>preferred network transfer syntaxes (incoming associations):<br />
  +x=   &#8211;prefer-uncompr<br />
          prefer explicit VR local byte order (default)<br />
  +xe   &#8211;prefer-little<br />
          prefer explicit VR little endian TS<br />
  +xb   &#8211;prefer-big<br />
          prefer explicit VR big endian TS<br />
  +xs   &#8211;prefer-lossless<br />
          prefer default JPEG lossless TS<br />
  +xy   &#8211;prefer-jpeg8<br />
          prefer default JPEG lossy TS for 8 bit data<br />
  +xx   &#8211;prefer-jpeg12<br />
          prefer default JPEG lossy TS for 12 bit data<br />
  +xv   &#8211;prefer-j2k-lossless<br />
          prefer JPEG 2000 lossless TS<br />
  +xw   &#8211;prefer-j2k-lossy<br />
          prefer JPEG 2000 lossy TS<br />
  +xt   &#8211;prefer-jls-lossless<br />
          prefer JPEG-LS lossless TS<br />
  +xu   &#8211;prefer-jls-lossy<br />
          prefer JPEG-LS lossy TS<br />
  +xm   &#8211;prefer-mpeg2<br />
          prefer MPEG2 Main Profile @ Main Level TS<br />
  +xh   &#8211;prefer-mpeg2-high<br />
          prefer MPEG2 Main Profile @ High Level TS<br />
  +xr   &#8211;prefer-rle<br />
          prefer RLE lossless TS<br />
  +xd   &#8211;prefer-deflated<br />
          prefer deflated explicit VR little endian TS<br />
  +xi   &#8211;implicit<br />
          accept implicit VR little endian TS only<br />
proposed transmission transfer syntaxes (outgoing associations):<br />
  -x=   &#8211;propose-uncompr<br />
          propose all uncompressed TS, explicit VR<br />
          with local byte ordering first (default)<br />
  -xe   &#8211;propose-little<br />
          propose all uncompressed TS, explicit VR little endian first<br />
  -xb   &#8211;propose-big<br />
          propose all uncompressed TS, explicit VR big endian first<br />
  -xi   &#8211;propose-implicit<br />
          propose implicit VR little endian TS only<br />
  -xs   &#8211;propose-lossless<br />
          propose default JPEG lossless TS<br />
          and all uncompressed transfer syntaxes<br />
  -xy   &#8211;propose-jpeg8<br />
          propose default JPEG lossy TS for 8 bit data<br />
          and all uncompressed transfer syntaxes<br />
  -xx   &#8211;propose-jpeg12<br />
          propose default JPEG lossy TS for 12 bit data<br />
          and all uncompressed transfer syntaxes<br />
  -xv   &#8211;propose-j2k-lossless<br />
          propose JPEG 2000 lossless TS<br />
          and all uncompressed transfer syntaxes<br />
  -xw   &#8211;propose-j2k-lossy<br />
          propose JPEG 2000 lossy TS<br />
          and all uncompressed transfer syntaxes<br />
  -xt   &#8211;propose-jls-lossless<br />
          propose JPEG-LS lossless TS<br />
          and all uncompressed transfer syntaxes<br />
  -xu   &#8211;propose-jls-lossy<br />
          propose JPEG-LS lossy TS<br />
          and all uncompressed transfer syntaxes<br />
  -xm   &#8211;propose-mpeg2<br />
          propose MPEG2 Main Profile @ Main Level TS only<br />
  -xh   &#8211;propose-mpeg2-high<br />
          propose MPEG2 Main Profile @ High Level TS only<br />
  -xr   &#8211;propose-rle<br />
          propose RLE lossless TS<br />
          and all uncompressed transfer syntaxes<br />
  -xd   &#8211;propose-deflated<br />
          propose deflated explicit VR little endian TS<br />
          and all uncompressed transfer syntaxes<br />
network host access control (tcp wrapper):<br />
  -ac   &#8211;access-full<br />
          accept connections from any host (default)<br />
  +ac   &#8211;access-control<br />
          enforce host access control rules<br />
other network options:<br />
  -to   &#8211;timeout  [s]econds: integer (default: unlimited)<br />
          timeout for connection requests<br />
  -ta   &#8211;acse-timeout  [s]econds: integer (default: 30)<br />
          timeout for ACSE messages<br />
  -td   &#8211;dimse-timeout  [s]econds: integer (default: unlimited)<br />
          timeout for DIMSE messages<br />
  -pdu  &#8211;max-pdu  [n]umber of bytes: integer (4096..131072)<br />
          set max receive pdu to n bytes<br />
          (default: use value from configuration file)<br />
  -dhl  &#8211;disable-host-lookup<br />
          disable hostname lookup<br />
        &#8211;refuse<br />
          refuse association<br />
        &#8211;reject<br />
          reject association if no implementation class UID<br />
        &#8211;ignore<br />
          ignore store data, receive but do not store<br />
#This option causes dcmqrscp database back &#8211; end to ignore<br />
#all images received by the Storage Service Class.All images<br />
#will be received from the network but not stored to disk nor<br />
#recorded in database.<br />
  -up   &#8211;uid-padding<br />
          silently correct space-padded UIDs</p>
<h3>encoding options</h3>
<p>post-1993 value representations:<br />
  +u    &#8211;enable-new-vr<br />
          enable support for new VRs (UN/UT) (default)<br />
  -u    &#8211;disable-new-vr<br />
          disable support for new VRs, convert to OB<br />
#This option disables generation of new VRs(UN / UT) when writing<br />
#DICOM encoded data to a file to the network.This option can be<br />
#used to force compatibility with applications which do not support<br />
#these value representations.</p>
<h3>output options</h3>
<pre><code>
bit preserving mode : -B-- normal
                          allow implicit format conversions(default) +
                      B-- bit - preserving write data exactly as read output file format : +F-- write - file write file format(default) - F-- write - dataset write data set without file meta information output transfer syntax : (not with-- bit - preserving or compressed transmission) + t = --write - xfer - same write with same TS as input(default) + te-- write - xfer - little write with explicit VR little endian TS
                                                                                                                                                                                                                                                                                                   + tb-- write - xfer - big write with explicit VR big endian TS
                                                                                                                                                                                                                                                                                                   + ti-- write - xfer - implicit write with implicit VR little endian TS
                                                                                                                                                                                                                                                                                                   + td-- write - xfer - deflated write with deflated explicit VR little endian TS group length encoding(not with-- bit - preserving)
    : +g = --group - length - recalc recalculate group lengths if present (default) + g-- group - length - create always write with group length elements
               - g-- group - length - remove always write without group length elements length encoding in sequences
           and items(not with-- bit - preserving)
    : +e-- length - explicit write with explicit lengths(default) - e-- length - undefined write with undefined lengths data set trailing padding(not with-- write - dataset or --bit - preserving)
    : -p-- padding - off no padding(default) + p-- padding - create[f] ile - pad[i] tem - pad : integer align file on multiple of f bytes
           and items on multiple of i bytes deflate compression level(only with-- propose - deflated or --write - xfer - deflated / same)
    : +cl-- compression - level[l] evel : integer(default : 6) 0 = uncompressed,
                                                                                                                                                                                                                                                                                               1 = fastest, 9 = best compression
</code></pre>
<h2>NOTES</h2>
<h3>Operation</h3>
<p> <code>dcmqrscp</code> waits for another application to connect at the presentation address (port number) specified in its configuration file (or overridden by a command line option). When another application connects, <code>dcmqrscp</code> expects it to be a DICOM application and to use calling and called AE Titles specified in <code>dcmqrscp&#8217;s</code> configuration file. <code>dcmqrscp</code> will accept associations with Presentation Contexts for SOP Classes of the Verification Service Class, Storage Service Class and Query/Retreive Service Class. Associations will be rejected or Presentation Contexts will be refused if the peer application does not have appropriate access rights as specified by <code>dcmqrscp</code> configuration file. </p>
<p> <code>dcmqrscp</code> will receive images on Presentation Contexts of the Storage Service Class, write them to a configurable storage area associated with the class AE title, extract attributes from these images and store them in a database. <code>dcmqrscp</code> will receive query requests and generate query responses on Presentation Contexts of the Query/Retrieve Service class. <code>dcmqrscp</code> will receive retrieve requests and generate retrieve responses on Presentation Contexts of the Query/Retrieve Service class. <code>dcmqrscp</code> will also process C-CANCEL messages to interrupt query/retrieve operations. </p>
<p> Under normal operations <code>dcmqrscp</code> will never exit, it keeps on waiting for new associations until killed.</p>
<h3>DICOM Conformance</h3>
<h3>SCU Conformance</h3>
<p> The <code>dcmqrscp</code> application supports the following SOP Classes as an SCU: </p>
<pre>
VerificationSOPClass                                 1.2.840.10008.1.1
RETIRED_StoredPrintStorage                           1.2.840.10008.5.1.1.27
RETIRED_HardcopyGrayscaleImageStorage                1.2.840.10008.5.1.1.29
RETIRED_HardcopyColorImageStorage                    1.2.840.10008.5.1.1.30
ComputedRadiographyImageStorage                      1.2.840.10008.5.1.4.1.1.1
DigitalXRayImageStorageForPresentation               1.2.840.10008.5.1.4.1.1.1.1
DigitalXRayImageStorageForProcessing                 1.2.840.10008.5.1.4.1.1.1.1.1
DigitalMammographyXRayImageStorageForPresentation    1.2.840.10008.5.1.4.1.1.1.2
DigitalMammographyXRayImageStorageForProcessing      1.2.840.10008.5.1.4.1.1.1.2.1
DigitalIntraOralXRayImageStorageForPresentation      1.2.840.10008.5.1.4.1.1.1.3
DigitalIntraOralXRayImageStorageForProcessing        1.2.840.10008.5.1.4.1.1.1.3.1
CTImageStorage                                       1.2.840.10008.5.1.4.1.1.2
EnhancedCTImageStorage                               1.2.840.10008.5.1.4.1.1.2.1
RETIRED_UltrasoundMultiframeImageStorage             1.2.840.10008.5.1.4.1.1.3
UltrasoundMultiframeImageStorage                     1.2.840.10008.5.1.4.1.1.3.1
MRImageStorage                                       1.2.840.10008.5.1.4.1.1.4
EnhancedMRImageStorage                               1.2.840.10008.5.1.4.1.1.4.1
MRSpectroscopyStorage                                1.2.840.10008.5.1.4.1.1.4.2
EnhancedMRColorImageStorage                          1.2.840.10008.5.1.4.1.1.4.3
RETIRED_NuclearMedicineImageStorage                  1.2.840.10008.5.1.4.1.1.5
RETIRED_UltrasoundImageStorage                       1.2.840.10008.5.1.4.1.1.6
UltrasoundImageStorage                               1.2.840.10008.5.1.4.1.1.6.1
EnhancedUSVolumeStorage                              1.2.840.10008.5.1.4.1.1.6.2
SecondaryCaptureImageStorage                         1.2.840.10008.5.1.4.1.1.7
MultiframeSingleBitSecondaryCaptureImageStorage      1.2.840.10008.5.1.4.1.1.7.1
MultiframeGrayscaleByteSecondaryCaptureImageStorage  1.2.840.10008.5.1.4.1.1.7.2
MultiframeGrayscaleWordSecondaryCaptureImageStorage  1.2.840.10008.5.1.4.1.1.7.3
MultiframeTrueColorSecondaryCaptureImageStorage      1.2.840.10008.5.1.4.1.1.7.4
RETIRED_StandaloneOverlayStorage                     1.2.840.10008.5.1.4.1.1.8
RETIRED_StandaloneCurveStorage                       1.2.840.10008.5.1.4.1.1.9
DRAFT_WaveformStorage                                1.2.840.10008.5.1.4.1.1.9.1
TwelveLeadECGWaveformStorage                         1.2.840.10008.5.1.4.1.1.9.1.1
GeneralECGWaveformStorage                            1.2.840.10008.5.1.4.1.1.9.1.2
AmbulatoryECGWaveformStorage                         1.2.840.10008.5.1.4.1.1.9.1.3
HemodynamicWaveformStorage                           1.2.840.10008.5.1.4.1.1.9.2.1
CardiacElectrophysiologyWaveformStorage              1.2.840.10008.5.1.4.1.1.9.3.1
BasicVoiceAudioWaveformStorage                       1.2.840.10008.5.1.4.1.1.9.4.1
GeneralAudioWaveformStorage                          1.2.840.10008.5.1.4.1.1.9.4.2
ArterialPulseWaveformStorage                         1.2.840.10008.5.1.4.1.1.9.5.1
RespiratoryWaveformStorage                           1.2.840.10008.5.1.4.1.1.9.6.1
RETIRED_StandaloneModalityLUTStorage                 1.2.840.10008.5.1.4.1.1.10
RETIRED_StandaloneVOILUTStorage                      1.2.840.10008.5.1.4.1.1.11
GrayscaleSoftcopyPresentationStateStorage            1.2.840.10008.5.1.4.1.1.11.1
ColorSoftcopyPresentationStateStorage                1.2.840.10008.5.1.4.1.1.11.2
PseudoColorSoftcopyPresentationStateStorage          1.2.840.10008.5.1.4.1.1.11.3
BlendingSoftcopyPresentationStateStorage             1.2.840.10008.5.1.4.1.1.11.4
XAXRFGrayscaleSoftcopyPresentationStateStorage       1.2.840.10008.5.1.4.1.1.11.5
XRayAngiographicImageStorage                         1.2.840.10008.5.1.4.1.1.12.1
EnhancedXAImageStorage                               1.2.840.10008.5.1.4.1.1.12.1.1
XRayRadiofluoroscopicImageStorage                    1.2.840.10008.5.1.4.1.1.12.2
EnhancedXRFImageStorage                              1.2.840.10008.5.1.4.1.1.12.2.1
XRay3DAngiographicImageStorage                       1.2.840.10008.5.1.4.1.1.13.1.1
XRay3DCraniofacialImageStorage                       1.2.840.10008.5.1.4.1.1.13.1.2
BreastTomosynthesisImageStorage                      1.2.840.10008.5.1.4.1.1.13.1.3
RETIRED_XRayAngiographicBiPlaneImageStorage          1.2.840.10008.5.1.4.1.1.12.3
NuclearMedicineImageStorage                          1.2.840.10008.5.1.4.1.1.20
RawDataStorage                                       1.2.840.10008.5.1.4.1.1.66
SpatialRegistrationStorage                           1.2.840.10008.5.1.4.1.1.66.1
SpatialFiducialsStorage                              1.2.840.10008.5.1.4.1.1.66.2
DeformableSpatialRegistrationStorage                 1.2.840.10008.5.1.4.1.1.66.3
SegmentationStorage                                  1.2.840.10008.5.1.4.1.1.66.4
SurfaceSegmentationStorage                           1.2.840.10008.5.1.4.1.1.66.5
RealWorldValueMappingStorage                         1.2.840.10008.5.1.4.1.1.67
RETIRED_VLImageStorage                               1.2.840.10008.5.1.4.1.1.77.1
VLEndoscopicImageStorage                             1.2.840.10008.5.1.4.1.1.77.1.1
VideoEndoscopicImageStorage                          1.2.840.10008.5.1.4.1.1.77.1.1.1
VLMicroscopicImageStorage                            1.2.840.10008.5.1.4.1.1.77.1.2
VideoMicroscopicImageStorage                         1.2.840.10008.5.1.4.1.1.77.1.2.1
VLSlideCoordinatesMicroscopicImageStorage            1.2.840.10008.5.1.4.1.1.77.1.3
VLPhotographicImageStorage                           1.2.840.10008.5.1.4.1.1.77.1.4
VideoPhotographicImageStorage                        1.2.840.10008.5.1.4.1.1.77.1.4.1
OphthalmicPhotography8BitImageStorage                1.2.840.10008.5.1.4.1.1.77.1.5.1
OphthalmicPhotography16BitImageStorage               1.2.840.10008.5.1.4.1.1.77.1.5.2
StereometricRelationshipStorage                      1.2.840.10008.5.1.4.1.1.77.1.5.3
OphthalmicTomographyImageStorage                     1.2.840.10008.5.1.4.1.1.77.1.5.4
VLWholeSlideMicroscopyImageStorage                   1.2.840.10008.5.1.4.1.1.77.1.6
RETIRED_VLMultiFrameImageStorage                     1.2.840.10008.5.1.4.1.1.77.2
LensometryMeasurementsStorage                        1.2.840.10008.5.1.4.1.1.78.1
AutorefractionMeasurementsStorage                    1.2.840.10008.5.1.4.1.1.78.2
KeratometryMeasurementsStorage                       1.2.840.10008.5.1.4.1.1.78.3
SubjectiveRefractionMeasurementsStorage              1.2.840.10008.5.1.4.1.1.78.4
VisualAcuityMeasurementsStorage                      1.2.840.10008.5.1.4.1.1.78.5
SpectaclePrescriptionReportStorage                   1.2.840.10008.5.1.4.1.1.78.6
OphthalmicAxialMeasurementsStorage                   1.2.840.10008.5.1.4.1.1.78.7
IntraocularLensCalculationsStorage                   1.2.840.10008.5.1.4.1.1.78.8
MacularGridThicknessAndVolumeReportStorage           1.2.840.10008.5.1.4.1.1.79.1
OphthalmicVisualFieldStaticPerimetryMeasurementsSt.  1.2.840.10008.5.1.4.1.1.80.1
DRAFT_SRTextStorage                                  1.2.840.10008.5.1.4.1.1.88.1
DRAFT_SRAudioStorage                                 1.2.840.10008.5.1.4.1.1.88.2
DRAFT_SRDetailStorage                                1.2.840.10008.5.1.4.1.1.88.3
DRAFT_SRComprehensiveStorage                         1.2.840.10008.5.1.4.1.1.88.4
BasicTextSRStorage                                   1.2.840.10008.5.1.4.1.1.88.11
EnhancedSRStorage                                    1.2.840.10008.5.1.4.1.1.88.22
ComprehensiveSRStorage                               1.2.840.10008.5.1.4.1.1.88.33
ProcedureLogStorage                                  1.2.840.10008.5.1.4.1.1.88.40
MammographyCADSRStorage                              1.2.840.10008.5.1.4.1.1.88.50
KeyObjectSelectionDocumentStorage                    1.2.840.10008.5.1.4.1.1.88.59
ChestCADSRStorage                                    1.2.840.10008.5.1.4.1.1.88.65
XRayRadiationDoseSRStorage                           1.2.840.10008.5.1.4.1.1.88.67
ColonCADSRStorage                                    1.2.840.10008.5.1.4.1.1.88.69
ImplantationPlanSRDocumentStorage                    1.2.840.10008.5.1.4.1.1.88.70
EncapsulatedPDFStorage                               1.2.840.10008.5.1.4.1.1.104.1
EncapsulatedCDAStorage                               1.2.840.10008.5.1.4.1.1.104.2
PositronEmissionTomographyImageStorage               1.2.840.10008.5.1.4.1.1.128
RETIRED_StandalonePETCurveStorage                    1.2.840.10008.5.1.4.1.1.129
EnhancedPETImageStorage                              1.2.840.10008.5.1.4.1.1.130
BasicStructuredDisplayStorage                        1.2.840.10008.5.1.4.1.1.131
RTImageStorage                                       1.2.840.10008.5.1.4.1.1.481.1
RTDoseStorage                                        1.2.840.10008.5.1.4.1.1.481.2
RTStructureSetStorage                                1.2.840.10008.5.1.4.1.1.481.3
RTBeamsTreatmentRecordStorage                        1.2.840.10008.5.1.4.1.1.481.4
RTPlanStorage                                        1.2.840.10008.5.1.4.1.1.481.5
RTBrachyTreatmentRecordStorage                       1.2.840.10008.5.1.4.1.1.481.6
RTTreatmentSummaryRecordStorage                      1.2.840.10008.5.1.4.1.1.481.7
RTIonPlanStorage                                     1.2.840.10008.5.1.4.1.1.481.8
RTIonBeamsTreatmentRecordStorage                     1.2.840.10008.5.1.4.1.1.481.9
DRAFT_RTBeamsDeliveryInstructionStorage              1.2.840.10008.5.1.4.34.1
GenericImplantTemplateStorage                        1.2.840.10008.5.1.4.43.1
ImplantAssemblyTemplateStorage                       1.2.840.10008.5.1.4.44.1
ImplantTemplateGroupStorage                          1.2.840.10008.5.1.4.45.1
</pre>
<p> The <code>dcmqrscp</code> application will propose presentation contexts for all of the abovementioned supported SOP Classes using the transfer syntaxes: </p>
<pre>
LittleEndianImplicitTransferSyntax                   1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax                   1.2.840.10008.1.2.1
BigEndianExplicitTransferSyntax                      1.2.840.10008.1.2.2
</pre>
<p> This default behaviour can be changed with the <i>&#8211;propose</i> options (see above). Depending on these options, the following transfer syntaxes are supported: </p>
<pre>
LittleEndianImplicitTransferSyntax                   1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax                   1.2.840.10008.1.2.1
DeflatedExplicitVRLittleEndianTransferSyntax         1.2.840.10008.1.2.1.99
BigEndianExplicitTransferSyntax                      1.2.840.10008.1.2.2
JPEGProcess1TransferSyntax                           1.2.840.10008.1.2.4.50
JPEGProcess2_4TransferSyntax                         1.2.840.10008.1.2.4.51
JPEGProcess14SV1TransferSyntax                       1.2.840.10008.1.2.4.70
JPEGLSLosslessTransferSyntax                         1.2.840.10008.1.2.4.80
JPEGLSLossyTransferSyntax                            1.2.840.10008.1.2.4.81
JPEG2000LosslessOnlyTransferSyntax                   1.2.840.10008.1.2.4.90
JPEG2000TransferSyntax                               1.2.840.10008.1.2.4.91
MPEG2MainProfileAtMainLevelTransferSyntax            1.2.840.10008.1.2.4.100
MPEG2MainProfileAtHighLevelTransferSyntax            1.2.840.10008.1.2.4.101
RLELosslessTransferSyntax                            1.2.840.10008.1.2.5
</pre>
<p> The <code>dcmqrscp</code> application does not support extended negotiation.</p>
<h3>SCP Conformance</h3>
<p> The <code>dcmqrscp</code> application supports the following SOP Classes as an SCP: </p>
<pre>
VerificationSOPClass                                 1.2.840.10008.1.1
FINDPatientRootQueryRetrieveInformationModel         1.2.840.10008.5.1.4.1.2.1.1
FINDPatientStudyOnlyQueryRetrieveInformationModel    1.2.840.10008.5.1.4.1.2.3.1
FINDStudyRootQueryRetrieveInformationModel           1.2.840.10008.5.1.4.1.2.2.1
GETPatientRootQueryRetrieveInformationModel          1.2.840.10008.5.1.4.1.2.1.3
GETPatientStudyOnlyQueryRetrieveInformationModel     1.2.840.10008.5.1.4.1.2.3.3
GETStudyRootQueryRetrieveInformationModel            1.2.840.10008.5.1.4.1.2.2.3
MOVEPatientRootQueryRetrieveInformationModel         1.2.840.10008.5.1.4.1.2.1.2
MOVEPatientStudyOnlyQueryRetrieveInformationModel    1.2.840.10008.5.1.4.1.2.3.2
MOVEStudyRootQueryRetrieveInformationModel           1.2.840.10008.5.1.4.1.2.2.2
RETIRED_StoredPrintStorage                           1.2.840.10008.5.1.1.27
RETIRED_HardcopyGrayscaleImageStorage                1.2.840.10008.5.1.1.29
RETIRED_HardcopyColorImageStorage                    1.2.840.10008.5.1.1.30
ComputedRadiographyImageStorage                      1.2.840.10008.5.1.4.1.1.1
DigitalXRayImageStorageForPresentation               1.2.840.10008.5.1.4.1.1.1.1
DigitalXRayImageStorageForProcessing                 1.2.840.10008.5.1.4.1.1.1.1.1
DigitalMammographyXRayImageStorageForPresentation    1.2.840.10008.5.1.4.1.1.1.2
DigitalMammographyXRayImageStorageForProcessing      1.2.840.10008.5.1.4.1.1.1.2.1
DigitalIntraOralXRayImageStorageForPresentation      1.2.840.10008.5.1.4.1.1.1.3
DigitalIntraOralXRayImageStorageForProcessing        1.2.840.10008.5.1.4.1.1.1.3.1
CTImageStorage                                       1.2.840.10008.5.1.4.1.1.2
EnhancedCTImageStorage                               1.2.840.10008.5.1.4.1.1.2.1
RETIRED_UltrasoundMultiframeImageStorage             1.2.840.10008.5.1.4.1.1.3
UltrasoundMultiframeImageStorage                     1.2.840.10008.5.1.4.1.1.3.1
MRImageStorage                                       1.2.840.10008.5.1.4.1.1.4
EnhancedMRImageStorage                               1.2.840.10008.5.1.4.1.1.4.1
MRSpectroscopyStorage                                1.2.840.10008.5.1.4.1.1.4.2
EnhancedMRColorImageStorage                          1.2.840.10008.5.1.4.1.1.4.3
RETIRED_NuclearMedicineImageStorage                  1.2.840.10008.5.1.4.1.1.5
RETIRED_UltrasoundImageStorage                       1.2.840.10008.5.1.4.1.1.6
UltrasoundImageStorage                               1.2.840.10008.5.1.4.1.1.6.1
EnhancedUSVolumeStorage                              1.2.840.10008.5.1.4.1.1.6.2
SecondaryCaptureImageStorage                         1.2.840.10008.5.1.4.1.1.7
MultiframeSingleBitSecondaryCaptureImageStorage      1.2.840.10008.5.1.4.1.1.7.1
MultiframeGrayscaleByteSecondaryCaptureImageStorage  1.2.840.10008.5.1.4.1.1.7.2
MultiframeGrayscaleWordSecondaryCaptureImageStorage  1.2.840.10008.5.1.4.1.1.7.3
MultiframeTrueColorSecondaryCaptureImageStorage      1.2.840.10008.5.1.4.1.1.7.4
RETIRED_StandaloneOverlayStorage                     1.2.840.10008.5.1.4.1.1.8
RETIRED_StandaloneCurveStorage                       1.2.840.10008.5.1.4.1.1.9
DRAFT_WaveformStorage                                1.2.840.10008.5.1.4.1.1.9.1
TwelveLeadECGWaveformStorage                         1.2.840.10008.5.1.4.1.1.9.1.1
GeneralECGWaveformStorage                            1.2.840.10008.5.1.4.1.1.9.1.2
AmbulatoryECGWaveformStorage                         1.2.840.10008.5.1.4.1.1.9.1.3
HemodynamicWaveformStorage                           1.2.840.10008.5.1.4.1.1.9.2.1
CardiacElectrophysiologyWaveformStorage              1.2.840.10008.5.1.4.1.1.9.3.1
BasicVoiceAudioWaveformStorage                       1.2.840.10008.5.1.4.1.1.9.4.1
GeneralAudioWaveformStorage                          1.2.840.10008.5.1.4.1.1.9.4.2
ArterialPulseWaveformStorage                         1.2.840.10008.5.1.4.1.1.9.5.1
RespiratoryWaveformStorage                           1.2.840.10008.5.1.4.1.1.9.6.1
RETIRED_StandaloneModalityLUTStorage                 1.2.840.10008.5.1.4.1.1.10
RETIRED_StandaloneVOILUTStorage                      1.2.840.10008.5.1.4.1.1.11
GrayscaleSoftcopyPresentationStateStorage            1.2.840.10008.5.1.4.1.1.11.1
ColorSoftcopyPresentationStateStorage                1.2.840.10008.5.1.4.1.1.11.2
PseudoColorSoftcopyPresentationStateStorage          1.2.840.10008.5.1.4.1.1.11.3
BlendingSoftcopyPresentationStateStorage             1.2.840.10008.5.1.4.1.1.11.4
XAXRFGrayscaleSoftcopyPresentationStateStorage       1.2.840.10008.5.1.4.1.1.11.5
XRayAngiographicImageStorage                         1.2.840.10008.5.1.4.1.1.12.1
EnhancedXAImageStorage                               1.2.840.10008.5.1.4.1.1.12.1.1
XRayRadiofluoroscopicImageStorage                    1.2.840.10008.5.1.4.1.1.12.2
EnhancedXRFImageStorage                              1.2.840.10008.5.1.4.1.1.12.2.1
XRay3DAngiographicImageStorage                       1.2.840.10008.5.1.4.1.1.13.1.1
XRay3DCraniofacialImageStorage                       1.2.840.10008.5.1.4.1.1.13.1.2
BreastTomosynthesisImageStorage                      1.2.840.10008.5.1.4.1.1.13.1.3
RETIRED_XRayAngiographicBiPlaneImageStorage          1.2.840.10008.5.1.4.1.1.12.3
NuclearMedicineImageStorage                          1.2.840.10008.5.1.4.1.1.20
RawDataStorage                                       1.2.840.10008.5.1.4.1.1.66
SpatialRegistrationStorage                           1.2.840.10008.5.1.4.1.1.66.1
SpatialFiducialsStorage                              1.2.840.10008.5.1.4.1.1.66.2
DeformableSpatialRegistrationStorage                 1.2.840.10008.5.1.4.1.1.66.3
SegmentationStorage                                  1.2.840.10008.5.1.4.1.1.66.4
SurfaceSegmentationStorage                           1.2.840.10008.5.1.4.1.1.66.5
RealWorldValueMappingStorage                         1.2.840.10008.5.1.4.1.1.67
RETIRED_VLImageStorage                               1.2.840.10008.5.1.4.1.1.77.1
VLEndoscopicImageStorage                             1.2.840.10008.5.1.4.1.1.77.1.1
VideoEndoscopicImageStorage                          1.2.840.10008.5.1.4.1.1.77.1.1.1
VLMicroscopicImageStorage                            1.2.840.10008.5.1.4.1.1.77.1.2
VideoMicroscopicImageStorage                         1.2.840.10008.5.1.4.1.1.77.1.2.1
VLSlideCoordinatesMicroscopicImageStorage            1.2.840.10008.5.1.4.1.1.77.1.3
VLPhotographicImageStorage                           1.2.840.10008.5.1.4.1.1.77.1.4
VideoPhotographicImageStorage                        1.2.840.10008.5.1.4.1.1.77.1.4.1
OphthalmicPhotography8BitImageStorage                1.2.840.10008.5.1.4.1.1.77.1.5.1
OphthalmicPhotography16BitImageStorage               1.2.840.10008.5.1.4.1.1.77.1.5.2
StereometricRelationshipStorage                      1.2.840.10008.5.1.4.1.1.77.1.5.3
OphthalmicTomographyImageStorage                     1.2.840.10008.5.1.4.1.1.77.1.5.4
VLWholeSlideMicroscopyImageStorage                   1.2.840.10008.5.1.4.1.1.77.1.6
RETIRED_VLMultiFrameImageStorage                     1.2.840.10008.5.1.4.1.1.77.2
LensometryMeasurementsStorage                        1.2.840.10008.5.1.4.1.1.78.1
AutorefractionMeasurementsStorage                    1.2.840.10008.5.1.4.1.1.78.2
KeratometryMeasurementsStorage                       1.2.840.10008.5.1.4.1.1.78.3
SubjectiveRefractionMeasurementsStorage              1.2.840.10008.5.1.4.1.1.78.4
VisualAcuityMeasurementsStorage                      1.2.840.10008.5.1.4.1.1.78.5
SpectaclePrescriptionReportStorage                   1.2.840.10008.5.1.4.1.1.78.6
OphthalmicAxialMeasurementsStorage                   1.2.840.10008.5.1.4.1.1.78.7
IntraocularLensCalculationsStorage                   1.2.840.10008.5.1.4.1.1.78.8
MacularGridThicknessAndVolumeReportStorage           1.2.840.10008.5.1.4.1.1.79.1
OphthalmicVisualFieldStaticPerimetryMeasurementsSt.  1.2.840.10008.5.1.4.1.1.80.1
DRAFT_SRTextStorage                                  1.2.840.10008.5.1.4.1.1.88.1
DRAFT_SRAudioStorage                                 1.2.840.10008.5.1.4.1.1.88.2
DRAFT_SRDetailStorage                                1.2.840.10008.5.1.4.1.1.88.3
DRAFT_SRComprehensiveStorage                         1.2.840.10008.5.1.4.1.1.88.4
BasicTextSRStorage                                   1.2.840.10008.5.1.4.1.1.88.11
EnhancedSRStorage                                    1.2.840.10008.5.1.4.1.1.88.22
ComprehensiveSRStorage                               1.2.840.10008.5.1.4.1.1.88.33
ProcedureLogStorage                                  1.2.840.10008.5.1.4.1.1.88.40
MammographyCADSRStorage                              1.2.840.10008.5.1.4.1.1.88.50
KeyObjectSelectionDocumentStorage                    1.2.840.10008.5.1.4.1.1.88.59
ChestCADSRStorage                                    1.2.840.10008.5.1.4.1.1.88.65
XRayRadiationDoseSRStorage                           1.2.840.10008.5.1.4.1.1.88.67
ColonCADSRStorage                                    1.2.840.10008.5.1.4.1.1.88.69
ImplantationPlanSRDocumentStorage                    1.2.840.10008.5.1.4.1.1.88.70
EncapsulatedPDFStorage                               1.2.840.10008.5.1.4.1.1.104.1
EncapsulatedCDAStorage                               1.2.840.10008.5.1.4.1.1.104.2
PositronEmissionTomographyImageStorage               1.2.840.10008.5.1.4.1.1.128
RETIRED_StandalonePETCurveStorage                    1.2.840.10008.5.1.4.1.1.129
EnhancedPETImageStorage                              1.2.840.10008.5.1.4.1.1.130
BasicStructuredDisplayStorage                        1.2.840.10008.5.1.4.1.1.131
RTImageStorage                                       1.2.840.10008.5.1.4.1.1.481.1
RTDoseStorage                                        1.2.840.10008.5.1.4.1.1.481.2
RTStructureSetStorage                                1.2.840.10008.5.1.4.1.1.481.3
RTBeamsTreatmentRecordStorage                        1.2.840.10008.5.1.4.1.1.481.4
RTPlanStorage                                        1.2.840.10008.5.1.4.1.1.481.5
RTBrachyTreatmentRecordStorage                       1.2.840.10008.5.1.4.1.1.481.6
RTTreatmentSummaryRecordStorage                      1.2.840.10008.5.1.4.1.1.481.7
RTIonPlanStorage                                     1.2.840.10008.5.1.4.1.1.481.8
RTIonBeamsTreatmentRecordStorage                     1.2.840.10008.5.1.4.1.1.481.9
DRAFT_RTBeamsDeliveryInstructionStorage              1.2.840.10008.5.1.4.34.1
GenericImplantTemplateStorage                        1.2.840.10008.5.1.4.43.1
ImplantAssemblyTemplateStorage                       1.2.840.10008.5.1.4.44.1
ImplantTemplateGroupStorage                          1.2.840.10008.5.1.4.45.1
PrivateShutdownSOPClass                              1.2.276.0.7230010.3.4.1915765545.18030.917282194.0
</pre>
<p> The <code>dcmqrscp</code> application will accept presentation contexts for all of the above mentioned supported SOP Classes using any of the transfer syntaxes: </p>
<pre>
LittleEndianImplicitTransferSyntax                   1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax                   1.2.840.10008.1.2.1
BigEndianExplicitTransferSyntax                      1.2.840.10008.1.2.2
</pre>
<p> The <code>dcmqrscp</code> application will prefer transfer syntaxes having an explicit encoding over the default implicit transfer syntax. If <code>dcmqrscp</code> is running on big-endian hardware it will prefer BigEndianExplicit to LittleEndianExplicit transfer syntax (and vice versa). This behaviour can be changed with the <i>&#8211;prefer</i> options (see above). Depending on these options, the following transfer syntaxes are supported: </p>
<pre>
LittleEndianImplicitTransferSyntax                   1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax                   1.2.840.10008.1.2.1
DeflatedExplicitVRLittleEndianTransferSyntax         1.2.840.10008.1.2.1.99
BigEndianExplicitTransferSyntax                      1.2.840.10008.1.2.2
JPEGProcess1TransferSyntax                           1.2.840.10008.1.2.4.50
JPEGProcess2_4TransferSyntax                         1.2.840.10008.1.2.4.51
JPEGProcess14SV1TransferSyntax                       1.2.840.10008.1.2.4.70
JPEGLSLosslessTransferSyntax                         1.2.840.10008.1.2.4.80
JPEGLSLossyTransferSyntax                            1.2.840.10008.1.2.4.81
JPEG2000LosslessOnlyTransferSyntax                   1.2.840.10008.1.2.4.90
JPEG2000TransferSyntax                               1.2.840.10008.1.2.4.91
MPEG2MainProfileAtMainLevelTransferSyntax            1.2.840.10008.1.2.4.100
MPEG2MainProfileAtHighLevelTransferSyntax            1.2.840.10008.1.2.4.101
RLELosslessTransferSyntax                            1.2.840.10008.1.2.5
</pre>
<p> The <code>dcmqrscp</code> application does not support extended negotiation.</p>
<h3>Query Keys</h3>
<p> The <code>dcmqrscp</code> application supports the following attributes as query keys. </p>
<p> Query/Retrieve Level: PATIENT (or STUDY for the Study Root Q/R model) </p>
<pre>
(0010,0010) PatientName
(0010,0020) PatientID
(0010,0030) PatientBirthDate
(0010,0032) PatientBirthTime
(0010,0040) PatientSex
(0010,1000) OtherPatientIDs
(0010,1001) OtherPatientNames
(0010,2160) EthnicGroup
(0010,4000) PatientComments
(0020,1200) NumberOfPatientRelatedStudies
(0020,1202) NumberOfPatientRelatedSeries
(0020,1204) NumberOfPatientRelatedInstances
</pre>
<p> Query/Retrieve Level: STUDY </p>
<pre>
(0008,0020) StudyDate
(0008,0030) StudyTime
(0008,0050) AccessionNumber
(0008,0090) ReferringPhysicianName
(0008,1030) StudyDescription
(0008,1060) NameOfPhysiciansReadingStudy
(0008,1080) AdmittingDiagnosesDescription
(0010,1010) PatientAge
(0010,1020) PatientSize
(0010,1030) PatientWeight
(0010,2180) Occupation
(0010,21B0) AdditionalPatientHistory
(0020,000D) StudyInstanceUID
(0020,0010) StudyID
(0020,1070) RETIRED_OtherStudyNumbers
(0020,1206) NumberOfStudyRelatedSeries
(0020,1208) NumberOfStudyRelatedInstances
</pre>
<p> Query/Retrieve Level: SERIES </p>
<pre>
(0008,0060) Modality
(0020,000E) SeriesInstanceUID
(0020,0011) SeriesNumber
</pre>
<p> Query/Retrieve Level: IMAGE </p>
<pre>
(0008,0018) SOPInstanceUID
(0020,0013) InstanceNumber
</pre>
<h3>Configuration</h3>
<p> The <code>dcmqrscp</code> program uses the same configuration file as the <code>dcmqrti</code> program. See the documentation on configuration for more information.</p>
<h3>Access Control</h3>
<p> When compiled on Unix platforms with TCP wrapper support, host-based access control can be enabled with the <i>&#8211;access-control</i> command line option. In this case the access control rules defined in the system&#8217;s host access control tables for <code>dcmqrscp</code> are enforced. The default locations of the host access control tables are <i>/etc/hosts.allow</i> and <i>/etc/hosts.deny</i>. Further details are described in <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5).</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>dcmqrscp</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>FILES</h2>
<p> <i>&lt;docdir&gt;/dcmqrcnf.txt</i> &#8211; configuration information<br />
 <i>&lt;docdir&gt;/dcmqrset.txt</i> &#8211; setup information<br />
 <i>&lt;etcdir&gt;/dcmqrscp.cfg</i> &#8211; example configuration file</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dcmqrti/">dcmqrti</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1993-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
