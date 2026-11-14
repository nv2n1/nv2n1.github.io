---
title: "movescu(1)"
name: "movescu"
section: "1"
letter: "m"
url: "/docs/linux/man/1-movescu/"
description: "movescu – DICOM retrieve (C-MOVE) SCU"
---

<h2 class="name">NAME</h2>
<p> movescu &#8211; DICOM retrieve (C-MOVE) SCU </p>
<h2>SYNOPSIS</h2>
<pre><code>
movescu[options] peer port[dcmfile - in...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>movescu</code> application implements both an SCU for the Query/Retrieve Service Class and an SCP for the Storage Service Class. <code>movescu</code> supports retrieve functionality using the C-MOVE message. It sends query keys to an SCP and awaits responses. It will accept associations for the purpose of receiving images sent as a result of the C-MOVE request. The application can be used to test SCPs of the Query/Retrieve Service Class. The <code>movescu</code> application can initiate the transfer of images to a third party or can retrieve images to itself. Note that the use of the term &#8216;move&#8217; is a misnomer. The C-MOVE operation actually performs an image copy (no images will be deleted from the SCP).</p>
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
  -k    &#8211;key  [k]ey: gggg,eeee=&#8221;str&#8221; or dictionary name=&#8221;str&#8221;<br />
          override matching key<br />
query information model:<br />
  -P    &#8211;patient<br />
          use patient root information model (default)<br />
  -S    &#8211;study<br />
          use study root information model<br />
  -O    &#8211;psonly<br />
          use patient/study only information model<br />
application entity titles:<br />
  -aet  &#8211;aetitle  [a]etitle: string<br />
          set my calling AE title (default: MOVESCU)<br />
  -aec  &#8211;call  [a]etitle: string<br />
          set called AE title of peer (default: ANY-SCP)<br />
  -aem  &#8211;move  [a]etitle: string<br />
          set move destination AE title (default: MOVESCU)<br />
preferred network transfer syntaxes (incoming associations):<br />
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
  +xa   &#8211;accept-all<br />
          accept all supported transfer syntaxes<br />
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
network host access control (tcp wrapper):<br />
  -ac   &#8211;access-full<br />
          accept connections from any host (default)<br />
  +ac   &#8211;access-control<br />
          enforce host access control rules<br />
port for incoming network associations:<br />
        &#8211;no-port<br />
          no port for incoming associations (default)<br />
  +P    &#8211;port  [n]umber: integer<br />
          port number for incoming associations<br />
handling of illegal datasets following &#8216;pending&#8217; move responses:<br />
  -pi   &#8211;pending-ignore<br />
          assume no dataset present (default)<br />
  -pr   &#8211;pending-read<br />
          read and ignore dataset<br />
other network options:<br />
  -to   &#8211;timeout  [s]econds: integer (default: unlimited)<br />
          timeout for connection requests<br />
  -ta   &#8211;acse-timeout  [s]econds: integer (default: 30)<br />
          timeout for ACSE messages<br />
  -td   &#8211;dimse-timeout  [s]econds: integer (default: unlimited)<br />
          timeout for DIMSE messages<br />
  -pdu  &#8211;max-pdu  [n]umber of bytes: integer (4096..131072)<br />
          set max receive pdu to n bytes (default: 16384)<br />
  -dhl  &#8211;disable-host-lookup<br />
          disable hostname lookup<br />
        &#8211;repeat  [n]umber: integer<br />
          repeat n times<br />
        &#8211;abort<br />
          abort association instead of releasing it<br />
        &#8211;ignore<br />
          ignore store data, receive but do not store<br />
        &#8211;cancel  [n]umber: integer<br />
          cancel after n responses (default: never)<br />
  -up   &#8211;uid-padding<br />
          silently correct space-padded UIDs</p>
<h3>output options</h3>
<p>general:<br />
  -od   &#8211;output-directory  [d]irectory: string (default: &#8220;.&#8221;)<br />
          write received objects to existing directory d<br />
bit preserving mode:<br />
  -B    &#8211;normal<br />
          allow implicit format conversions (default)<br />
  +B    &#8211;bit-preserving<br />
          write data exactly as read<br />
output file format:<br />
  +F    &#8211;write-file<br />
          write file format (default)<br />
  -F    &#8211;write-dataset<br />
          write data set without file meta information<br />
output transfer syntax<br />
(not with &#8211;bit-preserving or compressed transmission):<br />
  +t=   &#8211;write-xfer-same<br />
          write with same TS as input (default)<br />
  +te   &#8211;write-xfer-little<br />
          write with explicit VR little endian TS<br />
  +tb   &#8211;write-xfer-big<br />
          write with explicit VR big endian TS<br />
  +ti   &#8211;write-xfer-implicit<br />
          write with implicit VR little endian TS<br />
  +td   &#8211;write-xfer-deflated<br />
          write with deflated explicit VR little endian TS<br />
post-1993 value representations (not with &#8211;bit-preserving):<br />
  +u    &#8211;enable-new-vr<br />
          enable support for new VRs (UN/UT) (default)<br />
  -u    &#8211;disable-new-vr<br />
          disable support for new VRs, convert to OB<br />
group length encoding (not with &#8211;bit-preserving):<br />
  +g=   &#8211;group-length-recalc<br />
          recalculate group lengths if present (default)<br />
  +g    &#8211;group-length-create<br />
          always write with group length elements<br />
  -g    &#8211;group-length-remove<br />
          always write without group length elements<br />
length encoding in sequences and items (not with &#8211;bit-preserving):<br />
  +e    &#8211;length-explicit<br />
          write with explicit lengths (default)<br />
  -e    &#8211;length-undefined<br />
          write with undefined lengths<br />
data set trailing padding<br />
(not with &#8211;write-dataset or &#8211;bit-preserving):<br />
  -p    &#8211;padding-off<br />
          no padding (default)<br />
  +p    &#8211;padding-create  [f]ile-pad [i]tem-pad: integer<br />
          align file on multiple of f bytes and items on<br />
          multiple of i bytes<br />
deflate compression level (only with &#8211;write-xfer-deflated/same):<br />
  +cl   &#8211;compression-level  [l]evel: integer (default: 6)<br />
          0=uncompressed, 1=fastest, 9=best compression</p>
<h2>NOTES</h2>
<p> Each file supplied on the command line will be sent to the SCP as part of a C-MOVE request. The query file must be a valid DICOM data set containing the dataset part of a C-MOVE-RQ message. The query file could, for instance, be created with the <code>dump2dcm</code> utility from a script like the following example: </p>
<p>#request all images for the patient with ID = PAT001<br />
(0008, 0052) CS[PATIENT] #QueryRetrieveLevel(0010, 0020) LO[PAT001] #PatientID</p>
<p> Individual attributes of each file sent can be modified or supplemented using the &#8216;-k key&#8217; option. For example the command: </p>
<pre>
movescu -k 0010,0020=PAT002 caesar 5678 patqry.dcm
</pre>
<p> will, when sent to the SCP caesar at TCP/IP port 5678, cause any PatientID attribute in patqry.dcm to have the value &#8216;PAT002&#8217;. If such an attribute is present it will be replaced, if absent it will be inserted. The <i>-k</i> option can be present more than once. The value part (after the &#8216;=&#8217;) may be absent causing the attribute to be sent with zero length. It is not possible to replace or insert attributes within sequences using the <i>-k</i> option. </p>
<p> If no file is specified on the command line, the query must be specified completely with one or more &#8216;-k key&#8217; options. </p>
<p> For all uses of <code>movescu</code>, the SCP must be configured to &#8216;know&#8217; about the AE title where the images are to be transmitted. This is required since the C-MOVE request only contains the AE Title of the target and the SCP must be able to convert this AE Title into TCP/IP address and port number in order to actually send the images over a separate association. </p>
<p> The C-MOVE operation of the Query/Retrieve Service Class is able retrieve images or to initiate a copy of images to a third party.</p>
<h3>Known Problems</h3>
<p> <code>movescu</code> is intended to be used as a testing tool for DICOM software developers. The query keys file must be created by hand based upon the contents of the SCP. </p>
<p> Even when using a third-party move it may be necessary to set the TCP/IP port number to a reasonable value (via the <i>&#8211;port</i> option). Per default, port number 104 is used which is a restricted port on many systems. <code>movescu</code> always tries to listen for incoming associations. </p>
<p> The <code>movescu</code> application makes no attempt to prevent incorrect queries. In particular, the query keys of a C-MOVE request should only contain the QueryRetrieveLevel attribute and one or more of the so-called &#8216;unique key attributes&#8217; (PatientID, StudyInstanceUID, SeriesInstanceUID and SOPInstanceUID).</p>
<h3>DICOM Conformance</h3>
<h3>SCU Conformance</h3>
<p> The <code>movescu</code> application supports the following SOP Classes as an SCU: </p>
<pre>
MOVEPatientRootQueryRetrieveInformationModel         1.2.840.10008.5.1.4.1.2.1.2
MOVEStudyRootQueryRetrieveInformationModel           1.2.840.10008.5.1.4.1.2.2.2
MOVEPatientStudyOnlyQueryRetrieveInformationModel    1.2.840.10008.5.1.4.1.2.3.2
</pre>
<p> The <code>movescu</code> application will propose presentation contexts for one of the abovementioned supported SOP Classes depending on command line options (<i>-P</i>, <i>-S</i>, or <i>-O</i>). Each proposed presentation context will propose the transfer syntaxes: </p>
<pre>
LittleEndianImplicitTransferSyntax                   1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax                   1.2.840.10008.1.2.1
BigEndianExplicitTransferSyntax                      1.2.840.10008.1.2.2
</pre>
<p> This behaviour can be changed with the <i>&#8211;propose</i> options.</p>
<h3>SCP Conformance</h3>
<p> The <code>movescu</code> application supports the following SOP Classes as an SCP: </p>
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
<p> The <code>movescu</code> application will accept presentation contexts for all of the abovementioned supported SOP Classes using any of the transfer syntaxes: </p>
<pre>
LittleEndianImplicitTransferSyntax                   1.2.840.10008.1.2
LittleEndianExplicitTransferSyntax                   1.2.840.10008.1.2.1
BigEndianExplicitTransferSyntax                      1.2.840.10008.1.2.2
</pre>
<p> When acting as an SCP, the <code>movescu</code> application will prefer transfer syntaxes having an explicit encoding over the default implicit transfer syntax. If <code>movescu</code> is running on big-endian hardware it will prefer BigEndianExplicit to LittleEndianExplicit transfer syntax (and vice versa). This behaviour can be changed with the <i>&#8211;prefer</i> options (see above). Using option <i>&#8211;accept-all</i> any of the following transfer syntaxes is supported: </p>
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
<p> The <code>movescu</code> application does not support extended negotiation.</p>
<h3>Access Control</h3>
<p> When compiled on Unix platforms with TCP wrapper support, host-based access control can be enabled with the <i>&#8211;access-control</i> command line option. In this case the access control rules defined in the system&#8217;s host access control tables for <code>movescu</code> are enforced. The default locations of the host access control tables are <i>/etc/hosts.allow</i> and <i>/etc/hosts.deny</i>. Further details are described in <code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5).</p>
<h2>EXAMPLES</h2>
<pre><code>
movescu-- patient-- port 9876 --move TEST_AE-- call ARCHIVE caesar 104 q.dcm
</code></pre>
<p> sends the attributes contained in the DICOM file &#8216;q.dcm&#8217; as part of a C-MOVE request to application entity ARCHIVE on the host caesar at port 104 using the Patient Root query model. <code>movescu</code> itself uses the default AE title MOVESCU. The C-MOVE request will specifiy that images should be transferred to the destination AE title TEST_AE (via the <i>&#8211;move</i> option). How the SCP interprets this request depends on its configuration. <code>movescu</code> will listen on part 9876 for incoming associations in order to receive the requested images from the SCP. </p>
<p> Images can be copied to a third party by using a different destination AE title (e.g. <code>&#8211;move</code> ANOTHER_AE). Of course, the SCP must &#8216;know&#8217; this AE title and the destination must be acting as an SCP of the Storage Service Class (the <code>storescp</code> application can be used for this purpose).</p>
<h2>LOGGING</h2>
<p> The level of logging output of the various command line tools and underlying libraries can be specified by the user. By default, only errors and warnings are written to the standard error stream. Using option <i>&#8211;verbose</i> also informational messages like processing details are reported. Option <i>&#8211;debug</i> can be used to get more details on the internal activity, e.g. for debugging purposes. Other logging levels can be selected using option <i>&#8211;log-level</i>. In <i>&#8211;quiet</i> mode only fatal errors are reported. In such very severe error events, the application will usually terminate. For more details on the different logging levels, see documentation of module &#8216;oflog&#8217;. </p>
<p> In case the logging output should be written to file (optionally with logfile rotation), to syslog (Unix) or the event log (Windows) option <i>&#8211;log-config</i> can be used. This configuration file also allows for directing only certain messages to a particular output stream and for filtering certain messages based on the module or application where they are generated. An example configuration file is provided in <i>&lt;etcdir&gt;/logger.cfg</i>).</p>
<h2>COMMAND LINE</h2>
<p> All command line tools use the following notation for parameters: square brackets enclose optional values (0-1), three trailing dots indicate that multiple values are allowed (1-n), a combination of both means 0 to n values. </p>
<p> Command line options are distinguished from parameters by a leading &#8216;+&#8217; or &#8216;-&#8216; sign, respectively. Usually, order and position of command line options are arbitrary (i.e. they can appear anywhere). However, if options are mutually exclusive the rightmost appearance is used. This behaviour conforms to the standard evaluation rules of common Unix shells. </p>
<p> In addition, one or more command files can be specified using an &#8216;@&#8217; sign as a prefix to the filename (e.g. <i>@command.txt</i>). Such a command argument is replaced by the content of the corresponding text file (multiple whitespaces are treated as a single separator unless they appear between two quotation marks) prior to any further evaluation. Please note that a command file cannot contain another command file. This simple but effective approach allows to summarize common combinations of options/parameters and avoids longish and confusing command lines (an example is provided in file <i>&lt;datadir&gt;/dumppat.txt</i>).</p>
<h2>ENVIRONMENT</h2>
<p> The <code>movescu</code> utility will attempt to load DICOM data dictionaries specified in the <i>DCMDICTPATH</i> environment variable. By default, i.e. if the <i>DCMDICTPATH</i> environment variable is not set, the file <i>&lt;datadir&gt;/dicom.dic</i> will be loaded unless the dictionary is built into the application (default for Windows). </p>
<p> The default behaviour should be preferred and the <i>DCMDICTPATH</i> environment variable only used when alternative data dictionaries are required. The <i>DCMDICTPATH</i> environment variable has the same format as the Unix shell <i>PATH</i> variable in that a colon (&#8216;:&#8217;) separates entries. On Windows systems, a semicolon (&#8216;;&#8217;) is used as a separator. The data dictionary code will attempt to load each file specified in the <i>DCMDICTPATH</i> environment variable. It is an error if no data dictionary can be loaded.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-findscu/">findscu</a></code>(1), <code><a href="/docs/linux/man/1-dump2dcm/">dump2dcm</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1994-2010 by OFFIS e.V., Escherweg 2, 26121 Oldenburg, Germany. </p>
<h2>Index</h2>
